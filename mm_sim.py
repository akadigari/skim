"""
mm_sim.py — the MM BREADTH experiment: hypothetically quote the top-N pooled
markets and account, honestly, for what that would earn and cost.

WHAT ONE TICK DOES (per selected market)
  1. Replay ALL new public tape (exactly-once via tape.py's float-watermark +
     id-dedup cursor — never wall clock) through the queue fill model, even on
     book-fetch blips, so fills/AS are never silently dropped.
  2. Pull the book; JOIN THE TOUCH both sides at MM_QUOTE_SIZE (never improve),
     standing down on one-sided/crossed books and on any side that would push
     |inventory| past MM_MAX_INVENTORY (the $-reserve realism cap).
  3. Accrue reward: pool_per_day * share * dt/86400 (published scoring in
     rewards.py), with dt clamped and CLIPPED at the program's end_ts — an
     ended pool pays nothing, ever.
  4. Each fill schedules a MARKOUT check MM_MARKOUT_SECONDS later; the mid's
     move against us by then is booked as adverse selection. Unresolved
     markouts are flushed against the settlement value when a market resolves.

QUEUE MODEL BIAS — read carefully (review-corrected):
  We join the BACK of the displayed queue; cancels are assumed BEHIND us, so
  the model UNDERSTATES fills. For the DECISION NUMBER that bias is
  *optimistic*, not conservative: pool rewards accrue whether or not we fill,
  while fills mostly bring costs (adverse selection, fees). Fewer simulated
  fills therefore means fewer simulated costs against the same rewards. This
  is why report.py refuses a GO verdict without a minimum body of fill/cost
  evidence and prints reward-haircut sensitivity — see the gates there.

INVENTORY is marked at the last KNOWN two-sided mid (a one-sided or crossed
snapshot never clobbers the mark — that bug vanished short-inventory liability).
"""

from __future__ import annotations

import logging
import math
import time
from dataclasses import dataclass, field

import config
import rewards
import tape
from kalshi import Book, Kalshi, Program

log = logging.getLogger("lab.mm")


def taker_fee_cents(price_cents: float, contracts: float) -> float:
    p = max(0.0, min(1.0, price_cents / 100.0))
    raw = config.TAKER_FEE_COEF * contracts * p * (1.0 - p) * 100.0
    return math.ceil(round(raw, 6))   # round first: fp noise must not add a cent


def maker_fee_cents(price_cents: float, contracts: float) -> float:
    return config.MAKER_FEE_FRACTION * taker_fee_cents(price_cents, contracts)


@dataclass
class SimQuote:
    price: float
    size: float
    queue_ahead: float          # displayed contracts that fill before we do


@dataclass
class MarketSim:
    """Per-market accumulator. Serializable to/from plain dicts for state."""
    ticker: str
    pool_per_day: float
    target_size: float
    discount_factor: float
    end_ts: float = 0.0             # program end: accrual is CLIPPED here
    category: str = ""
    bid: SimQuote | None = None
    ask: SimQuote | None = None
    last_tick_ts: float = 0.0
    tape_cursor: dict = field(default_factory=dict)   # tape.py watermark state
    last_mid: float | None = None   # last KNOWN two-sided mid (never None-clobbered)
    inventory: float = 0.0          # net YES contracts (fills only, hypothetical)
    peak_abs_inventory: float = 0.0
    cash_cents: float = 0.0         # -cost of buys, +proceeds of sells
    reward_cents: float = 0.0
    fees_cents: float = 0.0
    adverse_cents: float = 0.0      # positive = money lost to informed flow
    fills: int = 0
    snapshots: int = 0
    counted: int = 0
    share_sum: float = 0.0
    pending_markouts: list = field(default_factory=list)   # [ts_due, side, price, qty]
    retired: bool = False           # settled/voided: keep totals, stop ticking

    # -- quoting policy ----------------------------------------------------
    def _requote(self, book: Book) -> None:
        bb, ba = book.best_bid, book.best_ask
        if bb is None or ba is None or ba <= bb:
            self.bid = self.ask = None          # one-sided or crossed: stand down
            return
        # Inventory realism cap: never quote the side that grows |inventory|
        # past the cap — the $/market reserve assumption must stay honest.
        allow_bid = self.inventory < config.MM_MAX_INVENTORY
        allow_ask = self.inventory > -config.MM_MAX_INVENTORY
        for side, best, allowed in (("bid", bb, allow_bid), ("ask", ba, allow_ask)):
            cur = self.bid if side == "bid" else self.ask
            if not allowed:
                if side == "bid":
                    self.bid = None
                else:
                    self.ask = None
                continue
            if cur is None or abs(cur.price - best) > 1e-9:
                q = SimQuote(price=best, size=config.MM_QUOTE_SIZE,
                             queue_ahead=book.size_at(side, best))
                if side == "bid":
                    self.bid = q
                else:
                    self.ask = q
            # same price: keep queue position (repricing costs priority)

    # -- tape replay ---------------------------------------------------------
    def _replay(self, trades, evidence) -> None:
        for t in trades:
            if t.taker_side == "no" and self.bid:        # aggressor sold YES -> bids consumed
                self._consume("bid", self.bid, t, evidence)
            elif t.taker_side == "yes" and self.ask:     # aggressor bought YES -> asks consumed
                self._consume("ask", self.ask, t, evidence)

    def _consume(self, side, q, t, evidence) -> None:
        swept = (t.price_cents < q.price - 1e-9) if side == "bid" \
                else (t.price_cents > q.price + 1e-9)
        at_level = abs(t.price_cents - q.price) < 1e-9
        fill = 0.0
        if swept:
            fill = q.size                                 # level traded through: all of us
        elif at_level:
            absorbed = min(t.count, q.queue_ahead)
            q.queue_ahead -= absorbed
            fill = min(t.count - absorbed, q.size)
        if fill <= 0:
            return
        q.size -= fill
        signed = fill if side == "bid" else -fill         # bid fill = we bought YES
        self.inventory += signed
        self.peak_abs_inventory = max(self.peak_abs_inventory, abs(self.inventory))
        self.cash_cents += -q.price * fill if side == "bid" else q.price * fill
        self.fees_cents += maker_fee_cents(q.price, fill)
        self.fills += 1
        self.pending_markouts.append(
            [t.ts + config.MM_MARKOUT_SECONDS, side, q.price, fill])
        evidence.append({"type": "mm_fill", "ticker": self.ticker, "ts": t.ts,
                         "trade_id": t.trade_id, "side": side, "price": q.price,
                         "qty": fill})
        if q.size <= 0:
            if side == "bid":
                self.bid = None
            else:
                self.ask = None

    def _settle_markouts(self, now: float, mid: float | None, evidence) -> None:
        if mid is None:
            return
        due = [m for m in self.pending_markouts if m[0] <= now]
        self.pending_markouts = [m for m in self.pending_markouts if m[0] > now]
        for _ts, side, price, qty in due:
            # We bought at `price` (bid) => the mid falling below it is adverse.
            move = (price - mid) if side == "bid" else (mid - price)
            adverse = max(move, 0.0) * qty       # only count moves AGAINST us
            self.adverse_cents += adverse
            evidence.append({"type": "mm_markout", "ticker": self.ticker,
                             "side": side, "price": price, "qty": qty,
                             "mid_later": mid, "adverse_cents": adverse})

    def flush_markouts(self, settle_value: float, evidence) -> None:
        """Resolution: grade EVERY outstanding markout against the terminal
        value so near-settlement adverse fills are never silently dropped."""
        self._settle_markouts(now=float("inf"), mid=settle_value, evidence=evidence)

    # -- one tick ------------------------------------------------------------
    def tick(self, api: Kalshi, evidence: list) -> None:
        if self.retired:
            return
        now = time.time()
        if not self.tape_cursor:
            self.tape_cursor = tape.new_cursor(now)

        # Stale resume (job-chain gap): our quotes are fictions from 20-60 min
        # ago — replaying gap tape against them would manufacture fills at
        # prices we'd never still be resting at. Drop quotes, skip the gap.
        if self.last_tick_ts and now - self.last_tick_ts > 4 * config.MM_POLL_SECONDS:
            self.bid = self.ask = None
            self.tape_cursor = tape.new_cursor(now)
            self._settle_markouts(self.last_tick_ts, self.last_mid, evidence)
            self.pending_markouts = []           # gap-spanning markouts: discard, noted
            evidence.append({"type": "mm_gap_resume", "ticker": self.ticker,
                             "gap_s": now - self.last_tick_ts})

        # 1. tape replay FIRST, exactly-once, even if the book fetch blips
        if self.last_tick_ts:
            self._replay(tape.fresh_trades(api, self.ticker, self.tape_cursor),
                         evidence)

        # 2. book + requote (one-sided/crossed/capped stand-down handled inside)
        book = api.book(self.ticker)
        self._requote(book)

        # 3. reward accrual, clipped at the program end
        my_bid = (self.bid.price, self.bid.size) if self.bid else None
        my_ask = (self.ask.price, self.ask.size) if self.ask else None
        share, counts = rewards.estimate_share(
            [(l.price_cents, l.size) for l in book.bids],
            [(l.price_cents, l.size) for l in book.asks],
            my_bid, my_ask, self.target_size, self.discount_factor,
            config.TICK_CENTS)
        acc_now = min(now, self.end_ts) if self.end_ts else now
        dt = max(0.0, min(acc_now - self.last_tick_ts, 4 * config.MM_POLL_SECONDS)) \
            if self.last_tick_ts else config.MM_POLL_SECONDS
        self.snapshots += 1
        if counts and dt > 0:
            self.counted += 1
            self.share_sum += share
            self.reward_cents += self.pool_per_day * share * dt / 86400.0
        if self.end_ts and now >= self.end_ts:
            self.bid = self.ask = None           # pool over: nothing left to skim

        # 4. mark + markouts — only a real two-sided mid may move the mark
        if book.mid is not None:
            self.last_mid = book.mid
        self._settle_markouts(now, self.last_mid, evidence)
        self.last_tick_ts = now

    # -- accounting ----------------------------------------------------------
    @property
    def spread_pnl_cents(self) -> float:
        """Cash plus inventory marked at the last KNOWN two-sided mid. If we
        hold inventory and have never seen a mid, the mark is zero and the
        fills-floor gate in report.py keeps that state from deciding anything."""
        mark = (self.last_mid or 0.0) * self.inventory
        return self.cash_cents + mark

    @property
    def decision_cents(self) -> float:
        return (self.reward_cents + self.spread_pnl_cents
                - self.adverse_cents - self.fees_cents)

    def to_dict(self) -> dict:
        d = self.__dict__.copy()
        d["bid"] = self.bid.__dict__ if self.bid else None
        d["ask"] = self.ask.__dict__ if self.ask else None
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "MarketSim":
        d = dict(d)
        d["bid"] = SimQuote(**d["bid"]) if d.get("bid") else None
        d["ask"] = SimQuote(**d["ask"]) if d.get("ask") else None
        return cls(**d)


# ---------------------------------------------------------------------------
# Selection: rank pools by expected $/day for OUR size per $ reserved
# ---------------------------------------------------------------------------
def select_markets(api: Kalshi, kept: list[MarketSim]) -> list[MarketSim]:
    """Return the quoting roster: surviving kept sims (with their pool terms
    REFRESHED from the live program map — a shrunk/ended pool must never keep
    paying its stale rate) plus new picks for vacancies, ranked by
    pool$/day x simulated-join share / capital reserve."""
    programs = {p.ticker: p for p in api.liquidity_programs()}
    log.info("selection: %d active liquidity pools", len(programs))

    roster: list[MarketSim] = []
    for s in kept:
        p = programs.get(s.ticker)
        if p is None:
            continue                     # program gone: stop quoting it
        s.pool_per_day = p.pool_cents_per_day
        s.target_size = p.target_size
        s.discount_factor = p.discount_factor
        s.end_ts = p.end_ts
        roster.append(s)

    vacancies = config.MM_N_MARKETS - len(roster)
    if vacancies <= 0:
        return roster

    have = {s.ticker for s in roster}
    ranked = sorted(programs.values(), key=lambda p: -p.pool_cents_per_day)
    scored = []
    for p in ranked[: config.MM_CANDIDATE_POOL_LIMIT]:
        if p.ticker in have:
            continue
        book = api.book(p.ticker)
        if book.best_bid is None or book.best_ask is None:
            continue
        share, counts = rewards.estimate_share(
            [(l.price_cents, l.size) for l in book.bids],
            [(l.price_cents, l.size) for l in book.asks],
            (book.best_bid, config.MM_QUOTE_SIZE),
            (book.best_ask, config.MM_QUOTE_SIZE),
            p.target_size, p.discount_factor, config.TICK_CENTS)
        if not counts:
            continue
        expected_per_day = p.pool_cents_per_day * share
        scored.append((expected_per_day / config.MM_RESERVE_PER_MARKET_USD, p))
    scored.sort(key=lambda x: -x[0])

    added = [_mk(p) for _s, p in scored[:vacancies]]
    log.info("selection: kept %d, added %d", len(roster), len(added))
    return roster + added


def _mk(p: Program) -> MarketSim:
    return MarketSim(ticker=p.ticker, pool_per_day=p.pool_cents_per_day,
                     target_size=p.target_size, discount_factor=p.discount_factor,
                     end_ts=p.end_ts, category=p.ticker.split("-")[0])
