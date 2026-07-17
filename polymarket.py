"""
polymarket.py — second venue for the FAVORITES experiment, phase 1: TAKER-ONLY.

WHY TAKER-ONLY HERE (scope honesty): the maker-vs-taker adverse-selection
question is being answered on Kalshi, where the tape replay machinery lives.
Polymarket's role in phase 1 is a cleaner test of whether the favorite-longshot
bias EXISTS at all when execution is cheapest: taker fees are currently ZERO
there, so buying the 85-95c favorite at the ask is the bias with no fee excuse.
If even that loses, the bias is dead; if it wins, phase 2 can add tape-replay
maker fills. All endpoints public read-only (gamma API); nothing can trade.

API shapes ported from the author's logical_arb project (verified live 2026-07):
gamma /markets rows carry bestBid/bestAsk/outcomePrices as 0..1 dollar strings,
endDate ISO; resolution = closed==true with outcomePrices ~[1,0] or ~[0,1].
"""

from __future__ import annotations

import json
import logging
import time

import requests

import config
from kalshi import parse_iso

log = logging.getLogger("lab.poly")

GAMMA = "https://gamma-api.polymarket.com"


class Polymarket:
    """Thin wrapper around Polymarket's public read-only gamma API."""

    def __init__(self):
        """Set up the HTTP session used for every request."""
        self._s = requests.Session()
        self._s.headers.update({"User-Agent": "skim/1.0 (read-only research)"})
        self.request_count = 0

    def _get(self, path: str, params: dict | None = None):
        """One polite GET against the gamma API. Returns the parsed JSON
        body, or None on any error (bad status, timeout, bad JSON)."""
        time.sleep(config.REQUEST_GAP_SECONDS)
        self.request_count += 1
        try:
            r = self._s.get(f"{GAMMA}{path}", params=params,
                            timeout=config.TIMEOUT_SECONDS)
            return r.json() if r.status_code == 200 else None
        except (requests.RequestException, ValueError) as e:
            log.warning("GET %s failed: %s", path, e)
            return None

    @staticmethod
    def _jlist(v):
        """Gamma sometimes returns a list field as an actual list, sometimes
        as a JSON-encoded string. Normalize either shape to a plain list."""
        if isinstance(v, list):
            return v
        try:
            return json.loads(v) if v else []
        except (ValueError, TypeError):
            return []

    def favorite_candidates(self) -> list[dict]:
        """Open markets, by volume, with best bid in the band and closing within
        the window. Gamma hard-caps offsets (~2200 => 422), so the top volume
        pages are the honest reachable universe — fine: favorites need liquidity."""
        lo, hi = config.FAV_BAND_CENTS
        now = time.time()
        out = []
        for offset in range(0, config.POLY_SCAN_PAGES * 100, 100):
            rows = self._get("/markets", {"closed": "false", "limit": 100,
                                          "offset": offset, "order": "volume24hr",
                                          "ascending": "false"})
            if not rows:
                break
            for m in rows:
                try:
                    bid = float(m.get("bestBid")) * 100.0
                    ask = float(m.get("bestAsk")) * 100.0
                except (TypeError, ValueError):
                    continue
                close_ts = parse_iso(m.get("endDate"))
                if close_ts is None:
                    continue
                days = (close_ts - now) / 86400.0
                if not (lo <= bid <= hi) or not (0.05 <= days <= config.FAV_MAX_DAYS_TO_CLOSE):
                    continue
                if ask - bid > config.POLY_MAX_SPREAD_CENTS:
                    continue        # a wide spread makes the taker test unfair
                out.append({"ticker": str(m.get("id")), "bid": bid, "ask": ask,
                            "close_ts": close_ts, "days_to_close": round(days, 2),
                            "question": (m.get("question") or "")[:80]})
        return out

    def result(self, market_id: str):
        """'yes' | 'no' | None (unsettled / void / ambiguous). Mirrors the
        resolution reader battle-tested in logical_arb."""
        data = self._get(f"/markets/{market_id}")
        m = data[0] if isinstance(data, list) and data else data
        if not isinstance(m, dict) or not m.get("closed"):
            return None
        prices = self._jlist(m.get("outcomePrices"))
        try:
            yes_p = float(prices[0]) if len(prices) >= 2 else None
        except (ValueError, TypeError):
            return None
        if yes_p is None:
            return None
        if yes_p >= 0.99:
            return "yes"
        if yes_p <= 0.01:
            return "no"
        return None
