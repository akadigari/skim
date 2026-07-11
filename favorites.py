"""
favorites.py — the FAVORITES experiment: does the favorite-longshot bias still
pay a small maker after fees, CONDITIONAL ON GETTING FILLED?

Evidence base (why this test exists): Whelan et al. (~300k Kalshi contracts)
found makers on the >=50c side earned ~+2.6% post-fee while <10c longshots lose
>60% — but that's an UNCONDITIONAL average over a maker population that turned
professional post-2024 (Becker, 72M trades). The open question is adverse
selection: are the fills you actually receive the bad ones? Two variants answer
it, on identical candidates:

  MAKER — hypothetically rest a bid joining the best bid in the 85-95c band on
          markets resolving within FAV_MAX_DAYS_TO_CLOSE; fills come from the
          public tape via the same queue-conservative model as mm_sim.
  TAKER — control: buy at the ask immediately (always fills, pays the spread
          and the full taker fee). If maker ROI < taker ROI, queue fills are
          adversely selected — the exact effect we're testing for.

One position per (market, variant), FAV_CONTRACTS each, graded at settlement:
YES pays 100-p per contract, NO loses p. All paper; nothing is ever sent.
"""

from __future__ import annotations

import logging
import time

import config
from kalshi import Kalshi, parse_iso
from mm_sim import maker_fee_cents, taker_fee_cents

log = logging.getLogger("lab.fav")


def scan_candidates(api: Kalshi) -> list[dict]:
    """Open markets with best bid in the band, closing within the window."""
    lo, hi = config.FAV_BAND_CENTS
    now = time.time()
    out = []
    for m in api.open_markets():
        bid = m.get("yes_bid")
        ask = m.get("yes_ask")
        bid = float(bid) if bid is not None else None
        ask = float(ask) if ask is not None else None
        close_ts = parse_iso(m.get("close_time"))
        if bid is None or ask is None or close_ts is None:
            continue
        days = (close_ts - now) / 86400.0
        if not (lo <= bid <= hi) or not (0.05 <= days <= config.FAV_MAX_DAYS_TO_CLOSE):
            continue
        out.append({"ticker": m.get("ticker"), "bid": bid, "ask": ask,
                    "close_ts": close_ts, "days_to_close": round(days, 2)})
    return out


class Favorites:
    """Position book for both variants. State is a plain dict (JSON-persisted)."""

    def __init__(self, state: dict | None = None):
        s = state or {}
        self.positions: dict = s.get("positions", {})   # key -> position dict
        self.last_scan_ts: float = s.get("last_scan_ts", 0.0)

    def to_dict(self) -> dict:
        return {"positions": self.positions, "last_scan_ts": self.last_scan_ts}

    # -- opening -------------------------------------------------------------
    def scan_and_open(self, api: Kalshi, evidence: list, poly=None) -> int:
        now = time.time()
        if now - self.last_scan_ts < config.FAV_SCAN_SECONDS:
            return 0
        self.last_scan_ts = now
        opened = self._open_kalshi(api, evidence, now)
        if poly is not None and config.POLY_ENABLED:
            opened += self._open_poly(poly, evidence, now)
        if opened:
            log.info("favorites: opened %d paper positions", opened)
        return opened

    def _open_count(self, venue: str) -> int:
        return sum(1 for p in self.positions.values()
                   if p["status"] == "open" and p.get("venue", "kalshi") == venue)

    def _open_kalshi(self, api: Kalshi, evidence: list, now: float) -> int:
        open_count = self._open_count("kalshi")
        opened = 0
        for c in scan_candidates(api):
            if open_count + opened >= config.FAV_MAX_POSITIONS:
                break
            book = api.book(c["ticker"])
            if book.best_bid is None or book.best_ask is None:
                continue
            if book.size_at("bid", book.best_bid) < config.FAV_MIN_BID_SIZE:
                continue    # nobody real at the touch — skip ghost books
            n = config.FAV_CONTRACTS
            for variant in ("maker", "taker"):
                key = f"kalshi|{c['ticker']}|{variant}"
                if key in self.positions or f"{c['ticker']}|{variant}" in self.positions:
                    continue                     # (second form: pre-venue keys)
                if variant == "taker":
                    price = book.best_ask
                    fee = taker_fee_cents(price, n)
                    pos = {"variant": "taker", "price": price, "qty": n,
                           "filled_qty": n, "fee_cents": fee, "status": "open"}
                else:
                    price = book.best_bid           # join, never improve
                    pos = {"variant": "maker", "price": price, "qty": n,
                           "filled_qty": 0.0, "fee_cents": 0.0,
                           "queue_ahead": book.size_at("bid", price),
                           "last_tape_ts": now, "status": "open"}
                pos.update({"venue": "kalshi", "ticker": c["ticker"], "opened_ts": now,
                            "close_ts": c["close_ts"],
                            "days_to_close_at_entry": c["days_to_close"]})
                self.positions[key] = pos
                opened += 1
                evidence.append({"type": "fav_open", **pos})
        return opened

    def _open_poly(self, poly, evidence: list, now: float) -> int:
        """Polymarket leg, phase 1: TAKER-ONLY at the ask, zero fees — the
        cheapest-execution test of whether the bias exists at all."""
        opened = 0
        open_count = self._open_count("polymarket")
        for c in poly.favorite_candidates():
            if open_count + opened >= config.POLY_FAV_MAX_POSITIONS:
                break
            key = f"polymarket|{c['ticker']}|taker"
            if key in self.positions:
                continue
            n = config.FAV_CONTRACTS
            pos = {"venue": "polymarket", "variant": "taker", "price": c["ask"],
                   "qty": n, "filled_qty": n,
                   "fee_cents": config.POLY_TAKER_FEE_CENTS * n,
                   "status": "open", "ticker": c["ticker"], "opened_ts": now,
                   "close_ts": c["close_ts"],
                   "days_to_close_at_entry": c["days_to_close"],
                   "question": c.get("question", "")}
            self.positions[key] = pos
            opened += 1
            evidence.append({"type": "fav_open", **pos})
        return opened

    # -- maker fill simulation (tape replay, queue-conservative; Kalshi only) --
    def update_maker_fills(self, api: Kalshi, evidence: list) -> None:
        for key, p in self.positions.items():
            if p["status"] != "open" or p["variant"] != "maker":
                continue
            if p.get("venue", "kalshi") != "kalshi":
                continue
            if p["filled_qty"] >= p["qty"]:
                continue
            for t in api.trades_since(p["ticker"], p["last_tape_ts"]):
                if t.taker_side != "no":            # only sells consume our bid
                    continue
                if t.price_cents < p["price"] - 1e-9:      # traded through us
                    fill = p["qty"] - p["filled_qty"]
                elif abs(t.price_cents - p["price"]) < 1e-9:
                    absorbed = min(t.count, p["queue_ahead"])
                    p["queue_ahead"] -= absorbed
                    fill = min(t.count - absorbed, p["qty"] - p["filled_qty"])
                else:
                    continue
                if fill > 0:
                    p["filled_qty"] += fill
                    p["fee_cents"] += maker_fee_cents(p["price"], fill)
                    evidence.append({"type": "fav_fill", "key": key,
                                     "ts": t.ts, "qty": fill})
            p["last_tape_ts"] = time.time()

    # -- grading ---------------------------------------------------------------
    def grade(self, api: Kalshi, evidence: list, poly=None) -> int:
        graded = 0
        for key, p in self.positions.items():
            if p["status"] != "open":
                continue
            if time.time() < p["close_ts"]:
                continue
            venue = p.get("venue", "kalshi")
            if venue == "polymarket":
                res = poly.result(p["ticker"]) if poly is not None else None
            else:
                res = api.result(p["ticker"])
            if res is None:
                # settle lag: give it the standard window, then void it out
                if time.time() - p["close_ts"] > 14 * 86400:
                    p["status"] = "void"
                continue
            n = p["filled_qty"]
            if n <= 0:
                p["status"] = "unfilled"          # maker never got filled: no trade
                continue
            gross = (100.0 - p["price"]) * n if res == "yes" else -p["price"] * n
            p["pnl_cents"] = gross - p["fee_cents"]
            p["result"] = res
            p["status"] = "settled"
            graded += 1
            evidence.append({"type": "fav_settle", "key": key, "result": res,
                             "pnl_cents": p["pnl_cents"]})
        return graded

    # -- stats -------------------------------------------------------------------
    def stats(self) -> dict:
        """'maker'/'taker' = the Kalshi experiment (the pre-registered gate);
        'poly_taker' = the Polymarket zero-fee existence test."""
        def bucket(venue, variant):
            ps = [p for p in self.positions.values()
                  if p["variant"] == variant and p.get("venue", "kalshi") == venue]
            settled = [p for p in ps if p["status"] == "settled"]
            risked = sum(p["price"] * p["filled_qty"] for p in settled)
            pnl = sum(p["pnl_cents"] for p in settled)
            wins = sum(1 for p in settled if p.get("result") == "yes")
            return {
                "open": sum(1 for p in ps if p["status"] == "open"),
                "unfilled": sum(1 for p in ps if p["status"] == "unfilled"),
                "settled": len(settled), "wins": wins,
                "pnl_cents": pnl,
                "roi_pct": (100.0 * pnl / risked) if risked else None,
            }
        return {"maker": bucket("kalshi", "maker"),
                "taker": bucket("kalshi", "taker"),
                "poly_taker": bucket("polymarket", "taker")}
