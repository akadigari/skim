"""
rewards.py — Kalshi's PUBLISHED liquidity-incentive scoring, reproduced exactly.
Ported from the author's mm_bot (verified against the CFTC-filed Feb-2026 terms).

The rules, per scoring snapshot (Kalshi samples ~1/second at random instants):
  1. Snapshot COUNTS only if BOTH sides independently show >= Target Size.
  2. Walk each side best-first; only the first Target Size contracts of depth
     qualify (orders straddling the boundary qualify partially).
  3. A qualifying order scores  discount_factor ^ (ticks from best) * size
     — at the observed 0.5 factor, one tick off the touch HALVES your score.
  4. Sides are normalized separately; the pool pays pro-rata, capped $1k/day.

Our sim ticks every MM_POLL_SECONDS instead of every second: the share
estimator stays unbiased (we accrue pool_per_day * share * dt/86400), it is
just noisier. That residual sampling noise, not the formula, is the model risk.
"""

from __future__ import annotations


def side_scores(levels, my_price, my_size, is_bid, target_size, discount_factor,
                tick_cents=1.0):
    """Score ONE side. levels = [(price_cents, size)] displayed (any order).
    Returns (my_score, others_score, side_depth). 'Ticks from best' is measured
    from the best price INCLUDING ours — improving the touch decays everyone
    else from YOUR price."""
    rows = [(p, s, False) for p, s in levels]
    if my_price is not None and my_size > 0:
        rows.append((my_price, my_size, True))
    if not rows:
        return 0.0, 0.0, 0.0

    rows.sort(key=lambda r: -r[0] if is_bid else r[0])
    best = rows[0][0]

    target = target_size if target_size and target_size > 0 else float("inf")
    remaining = target
    mine = others = 0.0
    for price, size, is_mine in rows:
        if remaining <= 0:
            break
        eligible = min(size, remaining)
        remaining -= eligible
        ticks = round(abs(best - price) / tick_cents)
        score = (discount_factor ** ticks) * eligible
        if is_mine:
            mine += score
        else:
            others += score
    depth = sum(s for _, s, _ in rows)
    return mine, others, depth


def estimate_share(bids, asks, my_bid, my_ask, target_size, discount_factor,
                   tick_cents=1.0):
    """Expected share of ONE snapshot given displayed book + our (price,size)
    orders. Returns (share, snapshot_counts). Quoting one side caps you at 50%
    structurally (each side is half the pool)."""
    bp, bs = my_bid if my_bid else (None, 0.0)
    ap, asz = my_ask if my_ask else (None, 0.0)

    my_b, oth_b, depth_b = side_scores(bids, bp, bs, True, target_size,
                                       discount_factor, tick_cents)
    my_a, oth_a, depth_a = side_scores(asks, ap, asz, False, target_size,
                                       discount_factor, tick_cents)

    target = target_size if target_size and target_size > 0 else 0.0
    if not (depth_b >= target and depth_a >= target):
        return 0.0, False           # one-sided/shallow snapshot pays no one

    bid_share = my_b / (my_b + oth_b) if (my_b + oth_b) > 0 else 0.0
    ask_share = my_a / (my_a + oth_a) if (my_a + oth_a) > 0 else 0.0
    return (bid_share + ask_share) / 2.0, True
