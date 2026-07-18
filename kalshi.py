"""
kalshi.py: the ONLY module that talks to the network. Public, keyless, read-only.

Everything is a plain GET against api.elections.kalshi.com; this repo is
structurally incapable of trading. Conventions ported from the author's mm_bot
(verified against the live API):
  * prices arrive as DOLLAR STRINGS ("0.8700") or integer cents; sizes as *_fp
    fractional strings, converted ONCE here, to float cents / float contracts;
  * GET /markets/{t}/orderbook returns TWO BID stacks (yes + no); a no-bid at p
    is a yes-ASK at 100-p, normalized here so callers see bids/asks best-first;
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
    """Turn an ISO-8601 timestamp string (with or without a trailing Z) into
    a unix timestamp. Returns None if the string is missing or unparseable."""
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except (ValueError, AttributeError):
        return None


def dollars_to_cents(v):
    """Turn a dollar-string price like '0.8700' into cents (87.0). None stays None."""
    if v in (None, ""):
        return None
    return float(v) * 100.0


def fp_to_float(v):
    """Turn one of Kalshi's fractional-size strings ('*_fp') into a plain float. Missing -> 0.0."""
    return float(v) if v not in (None, "") else 0.0


@dataclass
class Level:
    """One price level in an order book: a price (in cents) and the size resting there."""
    price_cents: float
    size: float


@dataclass
class Book:
    """A snapshot of one market's order book: bids and asks, both sorted best-first."""
    ticker: str
    ts: float
    bids: list = field(default_factory=list)   # yes-bids, best (highest) first
    asks: list = field(default_factory=list)   # yes-asks, best (lowest) first

    @property
    def best_bid(self):
        """Highest bid price in cents, or None if the book has no bids."""
        return self.bids[0].price_cents if self.bids else None

    @property
    def best_ask(self):
        """Lowest ask price in cents, or None if the book has no asks."""
        return self.asks[0].price_cents if self.asks else None

    @property
    def mid(self):
        """Midpoint of best bid and best ask, or None if the book is empty or crossed."""
        if self.best_bid is None or self.best_ask is None:
            return None
        if self.best_ask <= self.best_bid:
            return None                            # crossed snapshot: don't trust it
        return (self.best_bid + self.best_ask) / 2.0

    def size_at(self, side: str, price: float) -> float:
        """How much size is resting at an exact price on one side ('bid' or 'ask')."""
        levels = self.bids if side == "bid" else self.asks
        return sum(l.size for l in levels if abs(l.price_cents - price) < 1e-9)


@dataclass
class Trade:
    """One print from the public trade tape."""
    ts: float
    price_cents: float
    count: float
    taker_side: str      # "yes" -> asks consumed; "no" -> bids consumed
    trade_id: str = ""   # for cross-tick dedup at the watermark boundary


@dataclass
class Program:
    """One active liquidity-incentive program for a market: the reward pool
    and the schedule it pays out over."""
    ticker: str
    pool_cents: float
    start_ts: float
    end_ts: float
    target_size: float
    discount_factor: float

    @property
    def pool_cents_per_day(self) -> float:
        """The pool's payout rate per day, capped at the published daily program limit."""
        period = max(self.end_ts - self.start_ts, 1.0)
        return min(self.pool_cents * 86400.0 / period, config.DAILY_POOL_CAP_CENTS)


class Kalshi:
    """Thin wrapper around Kalshi's public read-only API: the only place in
    this repo that makes a network call."""

    def __init__(self):
        """Set up the HTTP session and the politeness/rate-limit bookkeeping."""
        self._s = requests.Session()
        self._s.headers.update({"User-Agent": "kalshi-sim-lab/1.0 (read-only research)"})
        self._lock = threading.Lock()
        self._last = 0.0
        self.request_count = 0

    def _get(self, path: str, params: dict | None = None) -> dict:
        """One rate-limited GET with automatic retry on 429/5xx. Returns the
        parsed JSON body, or {} if every attempt failed."""
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
        """Walk a cursor-paginated endpoint and collect every row across all
        pages (up to max_pages), handling Kalshi's two different cursor field names."""
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
        else:
            log.warning("_paginate %s: max_pages hit with cursor live: TRUNCATED", path)
        return out

    # -- incentive pools ----------------------------------------------------
    def liquidity_programs(self) -> list[Program]:
        """Fetch every currently-active liquidity incentive program (the
        pools that pay makers for resting quotes)."""
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
        """Fetch and normalize one market's order book. Kalshi returns two
        BID stacks (yes-bids and no-bids); a no-bid at price p is really a
        yes-ask at 100-p, so that flip happens here. Callers just see
        plain bids/asks, best price first."""
        data = self._get(f"/markets/{ticker}/orderbook")
        ob = (data.get("orderbook_fp") or data.get("orderbook") or {})
        # Bind the unit conversion to WHICH key the response used, never to the
        # value's magnitude (a legacy 1-cent level must not become $1.00).
        if ob.get("yes_dollars") is not None or ob.get("no_dollars") is not None:
            yes, no = ob.get("yes_dollars") or [], ob.get("no_dollars") or []
            def px(v):
                """Dollar-string level price -> cents."""
                return float(v) * 100.0
        else:
            yes, no = ob.get("yes") or [], ob.get("no") or []
            def px(v):
                """Legacy integer-cents level price, already in cents."""
                return float(v)

        def ok(price):
            """Drop levels with an impossible price (must be strictly between 0 and 100 cents)."""
            return 0.0 < price < 100.0            # drop impossible levels

        bids = sorted([Level(px(p), fp_to_float(s)) for p, s in yes if ok(px(p))],
                      key=lambda l: -l.price_cents)
        asks = sorted([Level(100.0 - px(p), fp_to_float(s)) for p, s in no
                       if ok(100.0 - px(p))],
                      key=lambda l: l.price_cents)
        return Book(ticker=ticker, ts=time.time(), bids=bids, asks=asks)

    def trades_since(self, ticker: str, min_ts: float, limit: int = 200,
                     max_pages: int = 5) -> list[Trade]:
        """Public tape newer than min_ts, OLDEST FIRST, cursor-paginated so a busy
        window can't silently truncate at one page. min_ts is int-floored by the
        API; callers must therefore keep a FLOAT watermark + id-dedup (tape.py)."""
        rows, cursor, pages = [], None, 0
        while pages < max_pages:
            pages += 1
            params = {"ticker": ticker, "limit": limit, "min_ts": int(min_ts)}
            if cursor:
                params["cursor"] = cursor
            data = self._get("/markets/trades", params)
            page = data.get("trades") or []
            rows.extend(page)
            cursor = data.get("cursor") or data.get("next_cursor")
            if not cursor or not page:
                break
        else:
            log.warning("trades_since %s: page cap hit, tape window truncated", ticker)
        trades = [Trade(
            ts=parse_iso(r.get("created_time")) or 0.0,
            price_cents=dollars_to_cents(r.get("yes_price_dollars"))
                        if r.get("yes_price_dollars") is not None
                        else float(r.get("yes_price") or 0.0),
            count=fp_to_float(r.get("count_fp")) or float(r.get("count") or 0.0),
            taker_side=r.get("taker_outcome_side") or r.get("taker_side", ""),
            trade_id=str(r.get("trade_id") or ""),
        ) for r in rows]
        trades.sort(key=lambda t: t.ts)          # oldest first for tape replay
        return trades

    @staticmethod
    def market_price_cents(m: dict, field: str):
        """Read a price field off a /markets row, whichever shape the API used.
        Live payloads carry {field}_dollars ("0.87"); legacy carried integer
        cents. Returns cents float or None. (The favorites scan was dead without
        this: live /markets no longer returns the legacy field.)"""
        dollars = m.get(f"{field}_dollars")
        if dollars not in (None, ""):
            return float(dollars) * 100.0
        legacy = m.get(field)
        if legacy in (None, ""):
            return None
        return float(legacy)

    def market(self, ticker: str) -> dict:
        """Fetch the raw /markets/{ticker} row for one market."""
        return self._get(f"/markets/{ticker}").get("market") or {}

    def open_markets(self, max_pages: int = 20, min_close_ts: int | None = None,
                     max_close_ts: int | None = None) -> list[dict]:
        """Open markets, optionally close-window-filtered SERVER-side so a
        scan sees the real universe instead of an arbitrary page prefix."""
        params: dict = {"status": "open", "limit": 200}
        if min_close_ts is not None:
            params["min_close_ts"] = int(min_close_ts)
        if max_close_ts is not None:
            params["max_close_ts"] = int(max_close_ts)
        return self._paginate("/markets", params, "markets", max_pages=max_pages)

    def result(self, ticker: str):
        """'yes' | 'no' | None (unsettled/void). Only terminal statuses count."""
        m = self.market(ticker)
        res = (m.get("result") or "").lower()
        return res if res in ("yes", "no") else None
