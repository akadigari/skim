"""
mm_sim.py — the MM BREADTH experiment: hypothetically quote the top-N pooled
markets and account, honestly, for what that would earn and cost.

WHAT ONE TICK DOES (per selected market)
  1. Pull the book. Our policy is JOIN THE TOUCH on both sides at MM_QUOTE_SIZE
     (never improve — conservative on share, and it never invents a spread the
     market didn't display). No quote if the book is one-sided or crossed.
  2. Accrue reward:  pool_per_day * share(book, our quotes) * dt / 86400,
     using the published scoring in rewards.py.
  3. Replay the public trade tape since the last tick through a QUEUE-CONSERVATIVE
     fill model (below). Fills change our hypothetical inventory and pay/charge
     spread; each fill schedules a MARKOUT check MM_MARKOUT_SECONDS later — the
     mid's move against us by then is booked as adverse selection.
  4. Maker fees are charged per fill at MAKER_FEE_FRACTION of the taker formula.

QUEUE-CONSERVATIVE FILLS (ported from mm_bot's fills.py)
  We join the BACK of the displayed queue at our price. Tape trades at prices
  through ours consume the level (we fill on the remainder); trades AT our price
  consume the queue ahead first. Cancels are assumed BEHIND us — this UNDERSTATES
  fills, which for an experiment measuring adverse selection is the honest bias:
  it understates costs less than optimistic queueing overstates rewards.

INVENTORY is marked to the current mid every tick; unrealized P&L flows into the
decision number only via the markout (AS) term, and any inventory remaining when
a market settles is graded at resolution by the supervisor's grading pass.
"""

from __future__ import annotations

import json
import logging
import math
import time
from dataclasses import dataclass, field

import config
import rewards
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
    category: str = ""
    bid: SimQuote | None = None
    ask: SimQuote | None = None
    last_tick_ts: float = 0.0
    last_mid: float | None = None
    inventory: float = 0.0          # net YES contracts (fills only, hypothetical)
    cash_cents: float = 0.0         # -cost of buys, +proceeds of sells
    reward_cents: float = 0.0
    fees_cents: float = 0.0
    adverse_cents: float = 0.0      # positive = money lost to informed flow
    fills: int = 0
    snapshots: int = 0
    counted: int = 0
    share_sum: float = 0.0
    pending_markouts: list = field(default_factory=list)   # [ts_due, side, price, qty]

    # -- quoting policy ----------------------------------------------------
    def _requote(self, book: Book) -> None:
        bb, ba = book.best_bid, book.best_ask
        if bb is None or ba is None or ba <= bb:
            self.bid = self.ask = None          # one-sided or crossed: stand down
            return
        for side, best in (("bid", bb), ("ask", ba)):
            cur = self.bid if side == "bid" else self.ask
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
        self.cash_cents += -q.price * fill if side == "bid" else q.price * fill
        self.fees_cents += maker_fee_cents(q.price, fill)
        self.fills += 1
        self.pending_markouts.append(
            [t.ts + config.MM_MARKOUT_SECONDS, side, q.price, fill])
        evidence.append({"type": "mm_fill", "ticker": self.ticker, "ts": t.ts,
                         "side": side, "price": q.price, "qty": fill})
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

    # -- one tick ------------------------------------------------------------
    def tick(self, api: Kalshi, evidence: list) -> None:
        now = time.time()
        book = api.book(self.ticker)
        if not book.bids and not book.asks:
            self.last_tick_ts = now
            return
        if self.last_tick_ts:
            trades = api.trades_since(self.ticker, self.last_tick_ts)
            self._replay(trades, evidence)

        self._requote(book)
        my_bid = (self.bid.price, self.bid.size) if self.bid else None
        my_ask = (self.ask.price, self.ask.size) if self.ask else None
        share, counts = rewards.estimate_share(
            [(l.price_cents, l.size) for l in book.bids],
            [(l.price_cents, l.size) for l in book.asks],
            my_bid, my_ask, self.target_size, self.discount_factor,
            config.TICK_CENTS)

        dt = min(now - self.last_tick_ts, 4 * config.MM_POLL_SECONDS) \
            if self.last_tick_ts else config.MM_POLL_SECONDS
        self.snapshots += 1
        if counts:
            self.counted += 1
            self.share_sum += share
            self.reward_cents += self.pool_per_day * share * dt / 86400.0

        self.last_mid = book.mid
        self._settle_markouts(now, book.mid, evidence)
        self.last_tick_ts = now

    # -- accounting ----------------------------------------------------------
    @property
    def spread_pnl_cents(self) -> float:
        """Cash plus inventory marked at the last mid — realized + unrealized
        trading P&L (excludes rewards/fees/AS which are tracked separately;
        note the AS term double-counts part of a marked loss on purpose: the
        decision number is meant to be pessimistic about informed flow)."""
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
def select_markets(api: Kalshi, keep: list[str]) -> list[MarketSim]:
    """Rank active pools by pool$/day x simulated-join share / reserve; keep
    existing selections (continuity) and fill vacancies from the ranking."""
    programs = {p.ticker: p for p in api.liquidity_programs()}
    log.info("selection: %d active liquidity pools", len(programs))

    kept = [t for t in keep if t in programs]
    vacancies = config.MM_N_MARKETS - len(kept)
    if vacancies <= 0:
        return [_mk(programs[t]) for t in kept]

    ranked = sorted(programs.values(), key=lambda p: -p.pool_cents_per_day)
    scored = []
    for p in ranked[: config.MM_CANDIDATE_POOL_LIMIT]:
        if p.ticker in kept:
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

    chosen = [_mk(programs[t]) for t in kept]
    chosen += [_mk(p) for _s, p in scored[:vacancies]]
    log.info("selection: kept %d, added %d", len(kept), len(chosen) - len(kept))
    return chosen


def _mk(p: Program) -> MarketSim:
    return MarketSim(ticker=p.ticker, pool_per_day=p.pool_cents_per_day,
                     target_size=p.target_size, discount_factor=p.discount_factor,
                     category=p.ticker.split("-")[0])
