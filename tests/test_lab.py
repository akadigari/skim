"""Offline unit tests: published scoring math vs hand-computed values, the
queue-conservative fill engine, favorites settlement/fee math, and the gates.
Network-free by construction."""

import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
import report
import rewards
from favorites import Favorites
from kalshi import Book, Level, Trade
from mm_sim import MarketSim, SimQuote, maker_fee_cents, taker_fee_cents


class TestRewards(unittest.TestCase):
    def test_side_scores_hand_computed(self):
        # Bids: others 300@49, 800@48; us 200@49. Target 1000, factor 0.5.
        # Depth walk: 49c level = 500 (300 theirs + 200 ours) all eligible,
        # then 500 of the 800@48 eligible. Best=49 so 49c scores x1, 48c x0.5.
        mine, others, depth = rewards.side_scores(
            [(49.0, 300), (48.0, 800)], 49.0, 200, True, 1000, 0.5)
        self.assertAlmostEqual(mine, 200.0)                 # 200 * 0.5^0
        self.assertAlmostEqual(others, 300.0 + 500 * 0.5)   # 300 + 250
        self.assertAlmostEqual(depth, 1300.0)

    def test_improving_touch_decays_others_from_our_price(self):
        # We bid 50 when best other bid is 49: their tick distance is 1.
        mine, others, _ = rewards.side_scores(
            [(49.0, 1000)], 50.0, 100, True, 2000, 0.5)
        self.assertAlmostEqual(mine, 100.0)
        self.assertAlmostEqual(others, 500.0)               # 1000 * 0.5^1

    def test_both_sides_gate(self):
        # Ask side has only 100 < target 1000 -> snapshot pays no one.
        share, counts = rewards.estimate_share(
            [(49.0, 2000)], [(51.0, 100)], (49.0, 200), (51.0, 200), 1000, 0.5)
        self.assertFalse(counts)
        self.assertEqual(share, 0.0)

    def test_share_two_sided(self):
        share, counts = rewards.estimate_share(
            [(49.0, 800)], [(51.0, 800)], (49.0, 200), (51.0, 200), 1000, 0.5)
        self.assertTrue(counts)
        self.assertAlmostEqual(share, 0.2)                  # 200/1000 each side


class TestFills(unittest.TestCase):
    def _sim(self):
        s = MarketSim(ticker="T", pool_per_day=1000.0, target_size=1000,
                      discount_factor=0.5)
        s.bid = SimQuote(price=49.0, size=200, queue_ahead=300)
        s.ask = SimQuote(price=51.0, size=200, queue_ahead=100)
        return s

    def test_queue_absorbs_before_us(self):
        s = self._sim()
        ev = []
        s._replay([Trade(ts=1.0, price_cents=49.0, count=250, taker_side="no")], ev)
        self.assertAlmostEqual(s.bid.queue_ahead, 50.0)     # 300 - 250
        self.assertEqual(s.fills, 0)                        # nothing reached us

    def test_fill_after_queue_consumed(self):
        s = self._sim()
        ev = []
        s._replay([Trade(ts=1.0, price_cents=49.0, count=400, taker_side="no")], ev)
        # 300 absorbed by queue, 100 fills us: we BOUGHT 100 YES at 49.
        self.assertEqual(s.fills, 1)
        self.assertAlmostEqual(s.inventory, 100.0)
        self.assertAlmostEqual(s.cash_cents, -49.0 * 100)
        self.assertGreater(s.fees_cents, 0)

    def test_sweep_through_fills_all(self):
        s = self._sim()
        ev = []
        s._replay([Trade(ts=1.0, price_cents=47.0, count=50, taker_side="no")], ev)
        self.assertAlmostEqual(s.inventory, 200.0)          # level traded through
        self.assertIsNone(s.bid)

    def test_ask_side_mirror(self):
        s = self._sim()
        ev = []
        s._replay([Trade(ts=1.0, price_cents=51.0, count=150, taker_side="yes")], ev)
        self.assertEqual(s.fills, 1)                        # 100 queue, then 50 us
        self.assertAlmostEqual(s.inventory, -50.0)
        self.assertAlmostEqual(s.cash_cents, 51.0 * 50)

    def test_markout_counts_only_adverse_moves(self):
        s = self._sim()
        ev = []
        s.pending_markouts = [[0.0, "bid", 49.0, 100]]
        s._settle_markouts(now=1.0, mid=45.0, evidence=ev)  # bought 49, mid 45
        self.assertAlmostEqual(s.adverse_cents, 400.0)
        s.pending_markouts = [[0.0, "bid", 49.0, 100]]
        s._settle_markouts(now=1.0, mid=55.0, evidence=ev)  # favorable: no charge
        self.assertAlmostEqual(s.adverse_cents, 400.0)

    def test_state_roundtrip(self):
        s = self._sim()
        s2 = MarketSim.from_dict(s.to_dict())
        self.assertEqual(s2.ticker, "T")
        self.assertAlmostEqual(s2.bid.queue_ahead, 300)


class TestFees(unittest.TestCase):
    def test_taker_fee_matches_formula(self):
        # 0.07 * 100 * 0.5 * 0.5 = $1.75 -> 175c, ceil'd.
        self.assertEqual(taker_fee_cents(50.0, 100), 175)

    def test_maker_fee_fraction(self):
        self.assertAlmostEqual(maker_fee_cents(50.0, 100),
                               0.25 * taker_fee_cents(50.0, 100))


class TestFavorites(unittest.TestCase):
    def _settled(self, price, result, variant="maker", qty=10.0):
        fav = Favorites()
        key = f"X|{variant}"
        fav.positions[key] = {
            "variant": variant, "ticker": "X", "price": price, "qty": qty,
            "filled_qty": qty, "fee_cents": 5.0, "queue_ahead": 0,
            "last_tape_ts": 0, "status": "open", "opened_ts": 0,
            "close_ts": time.time() - 10, "days_to_close_at_entry": 1.0,
        }

        class FakeApi:
            def market(self, t):
                return {"result": result or "", "close_time": None}
        fav.grade(FakeApi(), [])
        return fav

    def test_yes_settlement_pnl(self):
        fav = self._settled(90.0, "yes")
        p = fav.positions["X|maker"]
        self.assertEqual(p["status"], "settled")
        self.assertAlmostEqual(p["pnl_cents"], (100 - 90) * 10 - 5.0)

    def test_no_settlement_pnl(self):
        fav = self._settled(90.0, "no")
        self.assertAlmostEqual(fav.positions["X|maker"]["pnl_cents"],
                               -90.0 * 10 - 5.0)

    def test_unfilled_maker_is_not_a_trade(self):
        fav = self._settled(90.0, "yes")
        fav.positions["X|maker"]["status"] = "open"
        fav.positions["X|maker"]["filled_qty"] = 0.0

        class FakeApi:
            def market(self, t):
                return {"result": "yes", "close_time": None}
        fav.grade(FakeApi(), [])
        self.assertEqual(fav.positions["X|maker"]["status"], "unfilled")

    def test_stats_roi(self):
        fav = self._settled(90.0, "yes")
        st = fav.stats()["maker"]
        self.assertEqual(st["settled"], 1)
        self.assertAlmostEqual(st["roi_pct"], 100.0 * 95.0 / 900.0)


class TestGates(unittest.TestCase):
    def test_mm_gate_go_and_kill(self):
        good = {"rewards": 10000.0, "spread": 0.0, "adverse": 2000.0,
                "fees": 1000.0, "decision": 8000.0, "fills": 50}
        v, _ = report.mm_gate(good, days=config.CAMPAIGN_DAYS)
        self.assertEqual(v, "GO")            # 571c/day >= 500.1c bar; ratio 3.3
        bad = {"rewards": 1000.0, "spread": 0.0, "adverse": 2000.0,
               "fees": 500.0, "decision": -1500.0, "fills": 50}
        v, _ = report.mm_gate(bad, days=config.CAMPAIGN_DAYS)
        self.assertEqual(v, "KILL")

    def test_fav_gate_underpowered_until_n(self):
        v, d = report.fav_gate({"maker": {"settled": 10, "roi_pct": 5.0}})
        self.assertEqual(v, "UNDERPOWERED")
        v, _ = report.fav_gate({"maker": {"settled": 300, "roi_pct": 1.2}})
        self.assertEqual(v, "GO")
        v, _ = report.fav_gate({"maker": {"settled": 300, "roi_pct": -0.5}})
        self.assertEqual(v, "KILL")

    def test_report_renders(self):
        s = MarketSim(ticker="T", pool_per_day=1000.0, target_size=1000,
                      discount_factor=0.5)
        text = report.render({"campaign_start_ts": time.time() - 86400},
                             [s], Favorites().stats())
        self.assertIn("SKIM", text)
        self.assertIn("Gate status", text)
        self.assertIn("KILL", text)          # kill criteria section always present

    def test_wilson_sane(self):
        lo, hi = report.wilson(3, 5)
        self.assertTrue(0.2 < lo < 0.3 and 0.85 < hi < 0.92)
        self.assertEqual(report.wilson(0, 0), (0.0, 1.0))


if __name__ == "__main__":
    unittest.main()
