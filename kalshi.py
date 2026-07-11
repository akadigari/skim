"""
kalshi.py — the ONLY module that talks to the network. Public, keyless, read-only.

Everything is a plain GET against api.elections.kalshi.com; this repo is
structurally incapable of trading. Conventions ported from the author's mm_bot
(verified against the live API):
  * prices arrive as DOLLAR STRINGS ("0.8700") or integer cents; sizes as *_fp
    fractional strings — converted ONCE here, to float cents / float contracts;
  * GET /markets/{t}/orderbook returns TWO BID stacks (yes + no); a no-bid at p
    is a yes-ASK at 100-p — normalized here so callers see bids/asks best-first;
  * GET /markets/trades: taker_outcome_side "yes" => asks consumed,
    "no" => bids consumed. Oldest-first for tape replay.
  * GET /incentive_programs: period_reward is in CENTI-CENTS.
"""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone

import requests

import config

log = logging.getLogger("lab.kalshi")
RETRYABLE = {429, 500, 502, 503, 504}


def parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except (ValueError, AttributeError):
        return None


def dollars_to_cents(v):
    if v in (None, ""):
        return None
    return float(v) * 100.0


def fp_to_float(v):
    return float(v) if v not in (None, "") else 0.0


@dataclass
class Level:
    price_cents: float
    size: float


@dataclass
class Book:
    ticker: str
    ts: float
    bids: list = field(default_factory=list)   # yes-bids, best (highest) first
    asks: list = field(default_factory=list)   # yes-asks, best (lowest) first

    @property
    def best_bid(self):
        return self.bids[0].price_cents if self.bids else None

    @property
    def best_ask(self):
        return self.asks[0].price_cents if self.asks else None

    @property
    def mid(self):
        if self.best_bid is None or self.best_ask is None:
            return None
        return (self.best_bid + self.best_ask) / 2.0

    def size_at(self, side: str, price: float) -> float:
        levels = self.bids if side == "bid" else self.asks
        return sum(l.size for l in levels if abs(l.price_cents - price) < 1e-9)


@dataclass
class Trade:
    ts: float
    price_cents: float
    count: float
    taker_side: str      # "yes" -> asks consumed; "no" -> bids consumed


@dataclass
class Program:
    ticker: str
    pool_cents: float
    start_ts: float
    end_ts: float
    target_size: float
    discount_factor: float

    @property
    def pool_cents_per_day(self) -> float:
        period = max(self.end_ts - self.start_ts, 1.0)
        return min(self.pool_cents * 86400.0 / period, config.DAILY_POOL_CAP_CENTS)


class Kalshi:
    def __init__(self):
        self._s = requests.Session()
        self._s.headers.update({"User-Agent": "kalshi-paper-lab/1.0 (read-only research)"})
        self._lock = threading.Lock()
        self._last = 0.0
        self.request_count = 0

    def _get(self, path: str, params: dict | None = None) -> dict:
        for attempt in range(config.MAX_RETRIES + 1):
            with self._lock:
                gap = config.REQUEST_GAP_SECONDS - (time.time() - self._last)
                if gap > 0:
                    time.sleep(gap)
                self._last = time.time()
                self.request_count += 1
            try:
                r = self._s.get(f"{config.API_BASE}{path}", params=params,
                                timeout=config.TIMEOUT_SECONDS)
                if r.status_code == 200:
                    return r.json()
                if r.status_code not in RETRYABLE:
                    log.warning("GET %s -> %s", path, r.status_code)
                    return {}
            except requests.RequestException as e:
                log.warning("GET %s failed: %s", path, e)
            if attempt < config.MAX_RETRIES:
                time.sleep(1.5 * (2 ** attempt))
        return {}

    def _paginate(self, path, params, key, max_pages=30):
        out, cursor = [], None
        for _ in range(max_pages):
            p = dict(params)
            if cursor:
                p["cursor"] = cursor
            data = self._get(path, p)
            rows = data.get(key) or []
            out.extend(rows)
            # Kalshi is inconsistent: /markets uses "cursor", /incentive_programs
            # uses "next_cursor". Accept either.
            cursor = data.get("cursor") or data.get("next_cursor")
            if not cursor or not rows:
                break
        return out

    # -- incentive pools ----------------------------------------------------
    def liquidity_programs(self) -> list[Program]:
        rows = self._paginate("/incentive_programs", {"status": "active", "limit": 200},
                              "incentive_programs")
        out = []
        for r in rows:
            if r.get("incentive_type") != "liquidity":
                continue
            out.append(Program(
                ticker=r.get("market_ticker", ""),
                pool_cents=float(r.get("period_reward") or 0.0)
                           * config.PERIOD_REWARD_UNITS_TO_CENTS,
                start_ts=parse_iso(r.get("start_date")) or 0.0,
                end_ts=parse_iso(r.get("end_date")) or 0.0,
                target_size=fp_to_float(r.get("target_size_fp")),
                discount_factor=float(r.get("discount_factor_bps") or 10000) / 10000.0,
            ))
        return [p for p in out if p.ticker and p.pool_cents > 0]

    # -- books / trades / markets --------------------------------------------
    def book(self, ticker: str) -> Book:
        data = self._get(f"/markets/{ticker}/orderbook")
        ob = (data.get("orderbook_fp") or data.get("orderbook") or {})
        yes = ob.get("yes_dollars") or ob.get("yes") or []
        no = ob.get("no_dollars") or ob.get("no") or []

        def px(v):  # dollar-string in *_dollars form; integer cents in legacy form
            f = float(v)
            return f * 100.0 if f <= 1.5 else f

        bids = sorted([Level(px(p), fp_to_float(s)) for p, s in yes],
                      key=lambda l: -l.price_cents)
        asks = sorted([Level(100.0 - px(p), fp_to_float(s)) for p, s in no],
                      key=lambda l: l.price_cents)
        return Book(ticker=ticker, ts=time.time(), bids=bids, asks=asks)

    def trades_since(self, ticker: str, min_ts: float, limit: int = 200) -> list[Trade]:
        rows = self._get("/markets/trades",
                         {"ticker": ticker, "limit": limit, "min_ts": int(min_ts)}
                         ).get("trades") or []
        trades = [Trade(
            ts=parse_iso(r.get("created_time")) or 0.0,
            price_cents=dollars_to_cents(r.get("yes_price_dollars"))
                        if r.get("yes_price_dollars") is not None
                        else float(r.get("yes_price") or 0.0),
            count=fp_to_float(r.get("count_fp")) or float(r.get("count") or 0.0),
            taker_side=r.get("taker_outcome_side") or r.get("taker_side", ""),
        ) for r in rows]
        trades.sort(key=lambda t: t.ts)          # oldest first for tape replay
        return trades

    def market(self, ticker: str) -> dict:
        return self._get(f"/markets/{ticker}").get("market") or {}

    def open_markets(self, max_pages: int = 20) -> list[dict]:
        return self._paginate("/markets", {"status": "open", "limit": 200},
                              "markets", max_pages=max_pages)

    def result(self, ticker: str):
        """'yes' | 'no' | None (unsettled/void). Only terminal statuses count."""
        m = self.market(ticker)
        res = (m.get("result") or "").lower()
        return res if res in ("yes", "no") else None
