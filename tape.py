"""
tape.py — exactly-once tape consumption for paper fill simulation.

THE BUG THIS KILLS (found in adversarial review, reproduced): the API floors
min_ts to whole seconds and our old cursor was wall-clock tick-start, so trades
in the boundary second were replayed twice — double-decrementing queue_ahead and
manufacturing phantom fills that OVERSTATED the decision number. And trades
printed between "now" and the fetch landing were processed, then re-fetched.

THE FIX: a cursor of (float watermark = max processed trade ts, ids seen AT that
exact ts). Each poll fetches from floor(watermark), then filters:
    keep t  iff  t.ts > watermark  OR  (t.ts == watermark AND t.trade_id unseen)
The watermark advances only from trades actually processed — never wall clock —
so a failed/empty fetch leaves the window intact for retry, and a duplicate at
the boundary is dropped by id. State is two small JSON-safe fields.
"""

from __future__ import annotations


def new_cursor(start_ts: float) -> dict:
    return {"ts": float(start_ts), "ids": []}


def fresh_trades(api, ticker: str, cursor: dict) -> list:
    """Fetch and return only never-processed trades (oldest first), advancing
    the cursor in place. Safe against int-floored min_ts, refetch overlap,
    fetch failures (cursor untouched), and boundary-second duplicates."""
    trades = api.trades_since(ticker, cursor["ts"])
    out = []
    for t in trades:
        if t.ts < cursor["ts"]:
            continue                                   # older than watermark
        if t.ts == cursor["ts"] and (not t.trade_id or t.trade_id in cursor["ids"]):
            continue                                   # boundary duplicate
        out.append(t)
    if out:
        max_ts = max(t.ts for t in out)
        boundary = [t.trade_id for t in out if t.ts == max_ts and t.trade_id]
        if max_ts == cursor["ts"]:
            cursor["ids"] = cursor["ids"] + boundary   # same second grew
        else:
            cursor["ts"] = max_ts
            cursor["ids"] = boundary
        cursor["ids"] = cursor["ids"][-200:]           # bounded state
    return out
