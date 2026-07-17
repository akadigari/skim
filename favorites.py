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
import tape
from kalshi import Kalshi, parse_iso
from mm_sim import maker_fee_cents, taker_fee_cents

log = logging.getLogger("lab.fav")


def scan_candidates(api: Kalshi) -> list[dict]:
    """Open markets with best bid in the band, closing within the window.
    Prices are read via Kalshi.market_price_cents — the live /markets payload
    carries only *_dollars fields, and reading the legacy field left this whole
    experiment silently dead (review finding). The close window is filtered
    SERVER-side so we see the real universe, not a 4,000-row prefix."""
    lo, hi = config.FAV_BAND_CENTS
    now = time.time()
    out = []
    rows = api.open_markets(max_pages=40, min_close_ts=int(now),
                            max_close_ts=int(now + config.FAV_MAX_DAYS_TO_CLOSE * 86400))
    for m in rows:
        bid = Kalshi.market_price_cents(m, "yes_bid")
        ask = Kalshi.market_price_cents(m, "yes_ask")
        close_ts = parse_iso(m.get("close_time"))
        if bid is None or ask is None or close_ts is None:
            continue
        days = (close_ts - now) / 86400.0
        if not (lo <= bid <= hi) or not (0.05 <= days <= config.FAV_MAX_DAYS_TO_CLOSE):
            continue
        if ask - bid > config.KALSHI_MAX_SPREAD_CENTS:
            continue                     # wide spread: unfair maker/taker comparison
        out.append({"ticker": m.get("ticker"), "bid": bid, "ask": ask,
                    "close_ts": close_ts, "days_to_close": round(days, 2)})
    log.info("favorites scan: %d kalshi candidates from %d rows", len(out), len(rows))
    return out


class Favorites:
    """Position book for both variants. State is a plain dict (JSON-persisted)."""

    def __init__(self, state: dict | None = None):
        """Load the position book from a saved state dict, or start empty."""
        s = state or {}
        self.positions: dict = s.get("positions", {})   # key -> position dict
        self.last_scan_ts: float = s.get("last_scan_ts", 0.0)

    def to_dict(self) -> dict:
        """Turn the position book back into a plain dict for JSON checkpointing."""
        return {"positions": self.positions, "last_scan_ts": self.last_scan_ts}

    # -- opening -------------------------------------------------------------
    def scan_and_open(self, api: Kalshi, evidence: list, poly=None) -> int:
        """If enough time has passed since the last scan, look for new
        favorite-band candidates on Kalshi (and Polymarket, if enabled) and
        open paper positions on them. Returns how many positions were opened."""
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
        """How many positions are currently open on one venue (kalshi or polymarket)."""
        return sum(1 for p in self.positions.values()
                   if p["status"] == "open" and p.get("venue", "kalshi") == venue)

    def _open_kalshi(self, api: Kalshi, evidence: list, now: float) -> int:
        """Scan Kalshi for favorite-band candidates and open a maker + taker
        paper position on each new one, up to FAV_MAX_POSITIONS."""
        open_count = self._open_count("kalshi")
        opened = 0
        for c in scan_candidates(api):
            if open_count + opened >= config.FAV_MAX_POSITIONS:
                break
            book = api.book(c["ticker"])
            if book.best_bid is None or book.best_ask is None:
                continue
            lo, hi = config.FAV_BAND_CENTS
            if not (lo <= book.best_bid <= hi):
                continue    # moved out of band between scan and entry
            if book.best_ask - book.best_bid > config.KALSHI_MAX_SPREAD_CENTS:
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
                           "tape_cursor": tape.new_cursor(now), "status": "open"}
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
        """Replay the public trade tape for each open maker position and fill
        it (partially or fully) whenever a real trade would have hit our
        resting bid, using the same queue-conservative model as mm_sim."""
        now = time.time()
        for key, p in self.positions.items():
            if p["status"] != "open" or p["variant"] != "maker":
                continue
            if p.get("venue", "kalshi") != "kalshi":
                continue
            if p["filled_qty"] >= p["qty"]:
                continue
            if now >= p["close_ts"]:
                continue                # market closed: no new tape can fill us
            if "tape_cursor" not in p:  # migrate any pre-cursor position
                p["tape_cursor"] = tape.new_cursor(p.get("last_tape_ts", now))
            for t in tape.fresh_trades(api, p["ticker"], p["tape_cursor"]):
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
                                     "ts": t.ts, "trade_id": t.trade_id,
                                     "qty": fill})

    # -- grading ---------------------------------------------------------------
    def grade(self, api: Kalshi, evidence: list, poly=None) -> int:
        """Check every open position whose market has closed, look up the
        real result, and settle it (pnl, win/loss) or void it if the result
        never shows up. Returns how many positions were settled this pass."""
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
                m = api.market(p["ticker"])
                r = (m.get("result") or "").lower()
                res = r if r in ("yes", "no") else None
                if res is None:
                    # Kalshi can push close_time later (delayed settlement).
                    # Restart the void clock from the CURRENT close so a real
                    # late outcome isn't silently dropped from the GO sample.
                    fresh_close = parse_iso(m.get("close_time"))
                    if fresh_close and fresh_close > p["close_ts"]:
                        p["close_ts"] = fresh_close
                        continue
            if res is None:
                # settle lag: give it the standard window, then void it out
                if time.time() - p["close_ts"] > 14 * 86400:
                    p["status"] = "void"
                    evidence.append({"type": "fav_void", "key": key})
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
            """Roll up one venue+variant slice (e.g. kalshi maker) into open/settled/pnl counts."""
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
