"""
report.py — regenerate REPORT.md: the campaign's single honest scoreboard,
readable from a phone on GitHub. The GO/KILL gates are encoded here so the
verdict is computed, not vibed.

GATES (set in config.py, derived from the pre-registered falsification tests):
  MM BREADTH  GO iff  decision_cents/day >= MM_GO_MULTIPLE x baseline
                 AND  (rewards + spread) / (adverse + fees) >= MM_GO_EARN_PAY_RATIO
              where decision = rewards + spread_pnl - adverse_selection - fees.
  FAVORITES   verdict requires >= FAV_GO_MIN_RESOLUTIONS settled positions;
              GO iff maker conditional-on-fill ROI > 0 after fees (Wilson-CI
              shown; UNDERPOWERED is reported proudly, never papered over).
"""

from __future__ import annotations

import math
import time

import config


def wilson(k: int, n: int, z: float = 1.96):
    if n <= 0:
        return (0.0, 1.0)
    ph = k / n
    z2 = z * z
    den = 1 + z2 / n
    c = (ph + z2 / (2 * n)) / den
    m = (z * math.sqrt((ph * (1 - ph) + z2 / (4 * n)) / n)) / den
    return (max(0.0, c - m), min(1.0, c + m))


def mm_gate(totals: dict, days: float) -> tuple[str, str]:
    if days < 1:
        return "PENDING", "less than one day of data"
    dec_day = totals["decision"] / days
    earn = totals["rewards"] + totals["spread"]
    pay = totals["adverse"] + totals["fees"]
    ratio = (earn / pay) if pay > 0 else float("inf")
    need = config.MM_GO_MULTIPLE * config.MM_BASELINE_DECISION_PER_DAY_CENTS
    detail = (f"decision ${dec_day/100:.2f}/day vs GO bar ${need/100:.2f}/day; "
              f"earn/pay {ratio:.2f} vs {config.MM_GO_EARN_PAY_RATIO}")
    if days < config.CAMPAIGN_DAYS:
        return ("ON TRACK" if dec_day >= need and ratio >= config.MM_GO_EARN_PAY_RATIO
                else "BEHIND"), detail
    if dec_day >= need and ratio >= config.MM_GO_EARN_PAY_RATIO:
        return "GO", detail
    return "KILL", detail


def fav_gate(stats: dict) -> tuple[str, str]:
    mk = stats.get("maker", {})
    n = mk.get("settled", 0)
    roi = mk.get("roi_pct")
    if n < config.FAV_GO_MIN_RESOLUTIONS:
        return "UNDERPOWERED", (f"{n}/{config.FAV_GO_MIN_RESOLUTIONS} settled maker "
                                f"positions — no verdict yet (this is honest, not broken)")
    if roi is not None and roi > 0:
        return "GO", f"maker conditional-on-fill ROI {roi:+.2f}% over {n} settled"
    return "KILL", f"maker conditional-on-fill ROI {roi if roi is not None else 0:+.2f}% <= 0 over {n} settled"


def render(state: dict, sims: list, fav_stats: dict) -> str:
    start = state.get("campaign_start_ts") or time.time()
    days = max((time.time() - start) / 86400.0, 0.0)

    totals = {"rewards": 0.0, "spread": 0.0, "adverse": 0.0, "fees": 0.0,
              "decision": 0.0, "fills": 0, "snapshots": 0, "counted": 0}
    for s in sims:
        totals["rewards"] += s.reward_cents
        totals["spread"] += s.spread_pnl_cents
        totals["adverse"] += s.adverse_cents
        totals["fees"] += s.fees_cents
        totals["decision"] += s.decision_cents
        totals["fills"] += s.fills
        totals["snapshots"] += s.snapshots
        totals["counted"] += s.counted

    mm_verdict, mm_detail = mm_gate(totals, days)
    fv_verdict, fv_detail = fav_gate(fav_stats)
    mk, tk = fav_stats.get("maker", {}), fav_stats.get("taker", {})

    def usd(c):
        return f"${c/100:+.2f}"

    lines = [
        "# SKIM — Skimming Kalshi's Incentive Markets (campaign report)",
        "",
        f"_Auto-generated {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} — "
        f"**day {days:.1f} of {config.CAMPAIGN_DAYS}**. 100% paper: this repo only "
        "reads public endpoints and cannot place orders._",
        "",
        "## Experiment 1 — MM breadth (liquidity-pool harvesting)",
        "",
        f"**Gate status: {mm_verdict}** — {mm_detail}",
        "",
        "| metric | value |",
        "|---|---|",
        f"| markets quoted | {len(sims)} |",
        f"| est. rewards accrued | {usd(totals['rewards'])} |",
        f"| spread P&L (cash + mark) | {usd(totals['spread'])} |",
        f"| adverse selection (markout) | {usd(-totals['adverse'])} |",
        f"| maker fees | {usd(-totals['fees'])} |",
        f"| **decision number** | **{usd(totals['decision'])}** |",
        f"| fills / snapshots (counted) | {totals['fills']} / "
        f"{totals['snapshots']} ({totals['counted']}) |",
        "",
        "### Per-market",
        "",
        "| ticker | pool $/day | share | rewards | AS | fills | decision |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in sorted(sims, key=lambda x: -x.decision_cents):
        share = (s.share_sum / s.counted) if s.counted else 0.0
        lines.append(f"| {s.ticker} | ${s.pool_per_day/100:.0f} | {share:.0%} | "
                     f"{usd(s.reward_cents)} | {usd(-s.adverse_cents)} | "
                     f"{s.fills} | {usd(s.decision_cents)} |")

    n_mk, w_mk = mk.get("settled", 0), mk.get("wins", 0)
    lo, hi = wilson(w_mk, n_mk) if n_mk else (0.0, 1.0)

    def roi_str(v):
        return f"{v:+.2f}%" if v is not None else "n/a"

    pt = fav_stats.get("poly_taker", {})
    mk_roi, tk_roi = roi_str(mk.get("roi_pct")), roi_str(tk.get("roi_pct"))
    pt_roi = roi_str(pt.get("roi_pct"))
    lines += [
        "",
        "## Experiment 2 — Favorites (85-95c maker vs taker control)",
        "",
        f"**Gate status: {fv_verdict}** — {fv_detail}",
        "",
        "| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |",
        "|---|---|---|---|---|---|---|",
        f"| kalshi maker | {mk.get('open',0)} | {mk.get('unfilled',0)} | {n_mk} | "
        f"{w_mk} (win-rate CI {lo:.0%}-{hi:.0%}) | {usd(mk.get('pnl_cents',0.0))} | {mk_roi} |",
        f"| kalshi taker | {tk.get('open',0)} | — | {tk.get('settled',0)} | {tk.get('wins',0)} | "
        f"{usd(tk.get('pnl_cents',0.0))} | {tk_roi} |",
        f"| poly taker (zero-fee) | {pt.get('open',0)} | — | {pt.get('settled',0)} | "
        f"{pt.get('wins',0)} | {usd(pt.get('pnl_cents',0.0))} | {pt_roi} |",
        "",
        "_If maker ROI < taker ROI, queue fills are adversely selected — the exact "
        "failure mode this experiment exists to measure. The Polymarket taker leg is "
        "the zero-fee existence test of the bias itself (phase 1: taker-only there; "
        "the pre-registered gate is judged on the Kalshi maker leg only)._",
        "",
        "## Kill criteria (pre-registered)",
        "",
        f"- **MM breadth**: at day {config.CAMPAIGN_DAYS}, KILL unless decision >= "
        f"{config.MM_GO_MULTIPLE:.0f}x the ${config.MM_BASELINE_DECISION_PER_DAY_CENTS/100:.2f}/day "
        f"3-market baseline AND earn/pay >= {config.MM_GO_EARN_PAY_RATIO}.",
        "- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once "
        f"{config.FAV_GO_MIN_RESOLUTIONS} positions settle (report stays UNDERPOWERED "
        "until then rather than faking a verdict).",
        "- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO "
        "here is only actionable before renewal risk.",
    ]
    return "\n".join(lines)
