"""Regression tests for the adversarial-review findings: tape exactly-once,
one-sided-mid marking, price-field parsing, inventory cap, gate floors,
verdict freezing, and settlement markout flushing."""

import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
import report
import tape
from kalshi import Book, Kalshi, Level, Trade
from mm_sim import MarketSim, SimQuote


class FakeTapeApi:
    """Returns scripted trades per call, mimicking the API's int-floored min_ts
    (the exact behavior that caused double-processing)."""
    def __init__(self, script):
        self.script = list(script)      # list of trade-lists, one per call

    def trades_since(self, ticker, min_ts, **kw):
        batch = self.script.pop(0) if self.script else []
        return [t for t in batch if t.ts >= int(min_ts)]


def _tr(ts, price, count, side, tid):
    return Trade(ts=ts, price_cents=price, count=count, taker_side=side, trade_id=tid)


class TestTapeExactlyOnce(unittest.TestCase):
    def test_boundary_duplicate_dropped(self):
        # The review's phantom-fill repro: same trade returned by two fetches
        # because min_ts is int-floored. The cursor must process it ONCE.
        cur = tape.new_cursor(1000.0)
        t = _tr(1000.4, 49.0, 250, "no", "T1")
        api = FakeTapeApi([[t], [t]])
        first = tape.fresh_trades(api, "X", cur)
        second = tape.fresh_trades(api, "X", cur)
        self.assertEqual(len(first), 1)
        self.assertEqual(len(second), 0)          # duplicate at boundary: dropped

    def test_new_trade_same_second_still_processed(self):
        cur = tape.new_cursor(1000.0)
        t1 = _tr(1000.4, 49.0, 100, "no", "T1")
        t2 = _tr(1000.4, 49.0, 50, "no", "T2")    # same second, NEW id
        api = FakeTapeApi([[t1], [t1, t2]])
        self.assertEqual(len(tape.fresh_trades(api, "X", cur)), 1)
        out = tape.fresh_trades(api, "X", cur)
        self.assertEqual([t.trade_id for t in out], ["T2"])

    def test_failed_fetch_leaves_cursor(self):
        cur = tape.new_cursor(1000.0)
        api = FakeTapeApi([[], [_tr(1001.0, 49.0, 10, "no", "T9")]])
        self.assertEqual(tape.fresh_trades(api, "X", cur), [])
        self.assertEqual(cur["ts"], 1000.0)        # untouched: window retried
        self.assertEqual(len(tape.fresh_trades(api, "X", cur)), 1)

    def test_no_phantom_fill_across_ticks(self):
        # End-to-end: the exact review scenario. 250 lots at our bid with
        # queue_ahead 300 must absorb into the queue ONCE — the second sight
        # of the same trade must not manufacture a 200-lot fill.
        s = MarketSim(ticker="X", pool_per_day=0.0, target_size=1e9,
                      discount_factor=0.5)
        s.bid = SimQuote(price=49.0, size=200, queue_ahead=300)
        s.tape_cursor = tape.new_cursor(1000.0)
        t = _tr(1000.4, 49.0, 250, "no", "T1")
        api = FakeTapeApi([[t], [t]])
        s._replay(tape.fresh_trades(api, "X", s.tape_cursor), [])
        s._replay(tape.fresh_trades(api, "X", s.tape_cursor), [])
        self.assertEqual(s.fills, 0)
        self.assertAlmostEqual(s.inventory, 0.0)
        self.assertAlmostEqual(s.bid.queue_ahead, 50.0)   # decremented exactly once


class TestMarkGuards(unittest.TestCase):
    def test_one_sided_book_does_not_clobber_mark(self):
        # Review repro: short 200 @ 51c, mid 50 -> spread P&L +200c. A one-sided
        # snapshot must NOT vanish the buy-back liability.
        s = MarketSim(ticker="X", pool_per_day=0.0, target_size=1e9,
                      discount_factor=0.5)
        s.inventory = -200.0
        s.cash_cents = 10200.0
        s.last_mid = 50.0
        self.assertAlmostEqual(s.spread_pnl_cents, 200.0)
        one_sided = Book(ticker="X", ts=0, bids=[Level(50.0, 100)], asks=[])
        self.assertIsNone(one_sided.mid)
        if one_sided.mid is not None:              # mirrors the tick guard
            s.last_mid = one_sided.mid
        self.assertAlmostEqual(s.spread_pnl_cents, 200.0)   # unchanged

    def test_crossed_book_mid_is_none(self):
        b = Book(ticker="X", ts=0, bids=[Level(60.0, 10)], asks=[Level(55.0, 10)])
        self.assertIsNone(b.mid)

    def test_settlement_flushes_pending_markouts(self):
        s = MarketSim(ticker="X", pool_per_day=0.0, target_size=1e9,
                      discount_factor=0.5)
        s.pending_markouts = [[time.time() + 9999, "bid", 95.0, 100]]
        s.flush_markouts(0.0, [])                  # settled NO: bought 95, worth 0
        self.assertAlmostEqual(s.adverse_cents, 9500.0)
        self.assertEqual(s.pending_markouts, [])

    def test_inventory_cap_stands_down_bid(self):
        s = MarketSim(ticker="X", pool_per_day=0.0, target_size=1e9,
                      discount_factor=0.5)
        s.inventory = config.MM_MAX_INVENTORY      # at the cap
        book = Book(ticker="X", ts=0, bids=[Level(49.0, 500)],
                    asks=[Level(51.0, 500)])
        s._requote(book)
        self.assertIsNone(s.bid)                   # can't buy more
        self.assertIsNotNone(s.ask)                # reducing side still quotes


class TestPriceFields(unittest.TestCase):
    def test_market_price_cents_prefers_dollars(self):
        self.assertAlmostEqual(
            Kalshi.market_price_cents({"yes_bid_dollars": "0.87"}, "yes_bid"), 87.0)
        self.assertAlmostEqual(
            Kalshi.market_price_cents({"yes_bid": 87}, "yes_bid"), 87.0)
        self.assertIsNone(Kalshi.market_price_cents({}, "yes_bid"))


class TestGateFloors(unittest.TestCase):
    def _totals(self, fills, decision=8000.0, rewards=10000.0, adverse=2000.0,
                fees=1000.0):
        return {"rewards": rewards, "spread": 0.0, "adverse": adverse,
                "fees": fees, "decision": decision, "fills": fills}

    def test_no_go_without_fill_evidence(self):
        v, d = report.mm_gate(self._totals(fills=0), days=config.CAMPAIGN_DAYS)
        self.assertIn("UNMEASURED", v)
        v, _ = report.mm_gate(self._totals(fills=5), days=3)
        self.assertEqual(v, "UNMEASURED")

    def test_go_with_evidence(self):
        v, _ = report.mm_gate(self._totals(fills=config.MM_GO_MIN_FILLS),
                              days=config.CAMPAIGN_DAYS)
        self.assertEqual(v, "GO")     # 8000/14=571c/day >= 500.1 bar; ratio 3.3

    def test_kill_below_bar(self):
        v, _ = report.mm_gate(self._totals(fills=100, decision=-1500.0,
                                           rewards=1000.0), days=config.CAMPAIGN_DAYS)
        self.assertEqual(v, "KILL")

    def test_frozen_verdict_overrides(self):
        state = {"campaign_start_ts": time.time() - 20 * 86400,
                 "mm_final": {"verdict": "KILL", "detail": "frozen detail",
                              "totals": {}, "frozen_ts": 0},
                 "campaign_complete": True, "quoting_now": 1}
        s = MarketSim(ticker="T", pool_per_day=100.0, target_size=1000,
                      discount_factor=0.5)
        text = report.render(state, [s], {"maker": {}, "taker": {}, "poly_taker": {}})
        self.assertIn("FINAL: KILL", text)
        self.assertIn("CAMPAIGN COMPLETE", text)

    def test_calibration_tripwire_demotes_go(self):
        # Enormous modeled rewards/market/day on ON TRACK status must demote.
        state = {"campaign_start_ts": time.time() - 2 * 86400, "quoting_now": 1}
        s = MarketSim(ticker="T", pool_per_day=100000.0, target_size=1000,
                      discount_factor=0.5)
        s.reward_cents = 100000.0      # $1000 over 2 days on one market
        s.fills = 100                  # cost evidence exists
        s.adverse_cents = 100.0
        text = report.render(state, [s], {"maker": {}, "taker": {}, "poly_taker": {}})
        self.assertIn("UNCALIBRATED", text)


if __name__ == "__main__":
    unittest.main()
