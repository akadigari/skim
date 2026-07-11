"""Tests for the SKIM additions: health staleness, digest rendering (no network),
Polymarket favorites leg, and per-venue stats."""

import json
import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
import health
import telegram
from favorites import Favorites
from mm_sim import MarketSim


class TestHealth(unittest.TestCase):
    def test_staleness_logic(self):
        self.assertFalse(health.is_stale(None))          # no state yet != dead
        self.assertFalse(health.is_stale(config.HEALTH_STALE_HOURS - 0.1))
        self.assertTrue(health.is_stale(config.HEALTH_STALE_HOURS + 0.1))

    def test_staleness_reads_checkpoint_ts(self):
        config.STATE_DIR.mkdir(exist_ok=True)
        p = health.STATE_PATH
        old = p.read_text() if p.exists() else None
        try:
            p.write_text(json.dumps({"last_checkpoint_ts": time.time() - 3600}))
            h = health.staleness_hours()
            self.assertAlmostEqual(h, 1.0, delta=0.1)
        finally:
            if old is None:
                p.unlink()
            else:
                p.write_text(old)


class TestDigest(unittest.TestCase):
    def test_render_says_paper_loudly(self):
        s = MarketSim(ticker="T", pool_per_day=1000.0, target_size=1000,
                      discount_factor=0.5)
        s.reward_cents = 123.0
        text = telegram.render_digest({"campaign_start_ts": time.time() - 86400},
                                      [s], Favorites().stats(), "ON TRACK",
                                      "UNDERPOWERED")
        self.assertIn("PAPER", text)
        self.assertIn("SKIM day 1.0", text)
        self.assertIn("ON TRACK", text)
        self.assertIn("REPORT.md", text)

    def test_send_is_noop_unconfigured(self):
        self.assertFalse(telegram.configured())
        self.assertFalse(telegram.send("nope"))


class FakePoly:
    def __init__(self, candidates=None, results=None):
        self._c = candidates or []
        self._r = results or {}

    def favorite_candidates(self):
        return self._c

    def result(self, market_id):
        return self._r.get(market_id)


class TestPolyFavorites(unittest.TestCase):
    def test_poly_taker_open_and_settle(self):
        fav = Favorites()
        cand = {"ticker": "12345", "bid": 90.0, "ask": 91.0,
                "close_ts": time.time() - 5, "days_to_close": 0.5, "question": "q"}
        fav.last_scan_ts = 0.0
        # open via the poly branch only (kalshi scan bypassed with a stub api)

        class NoKalshi:
            def open_markets(self, **kw):
                return []
        opened = fav.scan_and_open(NoKalshi(), [], poly=FakePoly([cand]))
        self.assertEqual(opened, 1)
        key = "polymarket|12345|taker"
        self.assertIn(key, fav.positions)
        self.assertEqual(fav.positions[key]["fee_cents"],
                         config.POLY_TAKER_FEE_CENTS * config.FAV_CONTRACTS)

        fav.grade(api=None, evidence=[], poly=FakePoly(results={"12345": "yes"}))
        p = fav.positions[key]
        self.assertEqual(p["status"], "settled")
        self.assertAlmostEqual(p["pnl_cents"], (100 - 91.0) * config.FAV_CONTRACTS)

    def test_stats_split_by_venue(self):
        fav = Favorites()
        fav.positions["polymarket|1|taker"] = {
            "venue": "polymarket", "variant": "taker", "price": 90.0,
            "qty": 10, "filled_qty": 10, "fee_cents": 0.0, "status": "settled",
            "pnl_cents": 100.0, "result": "yes"}
        fav.positions["kalshi|A|taker"] = {
            "venue": "kalshi", "variant": "taker", "price": 90.0,
            "qty": 10, "filled_qty": 10, "fee_cents": 5.0, "status": "settled",
            "pnl_cents": 95.0, "result": "yes"}
        st = fav.stats()
        self.assertEqual(st["poly_taker"]["settled"], 1)
        self.assertEqual(st["taker"]["settled"], 1)      # kalshi bucket unpolluted
        self.assertEqual(st["maker"]["settled"], 0)


if __name__ == "__main__":
    unittest.main()
