"""
report.py: regenerate REPORT.md: the campaign's single honest scoreboard,
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
    """Wilson score confidence interval for a win rate: k wins out of n
    trials. Returns (low, high), honest about uncertainty at small sample sizes."""
    if n <= 0:
        return (0.0, 1.0)
    ph = k / n
    z2 = z * z
    den = 1 + z2 / n
    c = (ph + z2 / (2 * n)) / den
    m = (z * math.sqrt((ph * (1 - ph) + z2 / (4 * n)) / n)) / den
    return (max(0.0, c - m), min(1.0, c + m))


def mm_gate(totals: dict, days: float) -> tuple[str, str]:
    """Decide the MM breadth experiment's verdict (GO/KILL/ON TRACK/etc.)
    from the running totals so far. Returns (verdict, human-readable detail)."""
    if days < 1:
        return "PENDING", "less than one day of data"
    dec_day = totals["decision"] / days
    earn = totals["rewards"] + totals["spread"]
    pay = totals["adverse"] + totals["fees"]
    fills = totals.get("fills", 0)
    ratio = (earn / pay) if pay > 0 else float("inf")
    need = config.MM_GO_MULTIPLE * config.MM_BASELINE_DECISION_PER_DAY_CENTS
    detail = (f"decision ${dec_day/100:.2f}/day vs GO bar ${need/100:.2f}/day; "
              f"earn/pay {ratio:.2f} vs {config.MM_GO_EARN_PAY_RATIO}; "
              f"fills {fills}/{config.MM_GO_MIN_FILLS} evidence floor")
    # The queue model UNDERSTATES fills, which flatters the decision number
    # (rewards accrue without fills; fills mostly bring costs). With no body
    # of fill/cost evidence, the ratio leg is vacuous: refuse to conclude.
    if fills < config.MM_GO_MIN_FILLS or pay <= 0:
        if days >= config.CAMPAIGN_DAYS:
            return "NO VERDICT (UNMEASURED)", detail + ", cost side never got evidence"
        return "UNMEASURED", detail + ", cost side lacks evidence so far"
    if days < config.CAMPAIGN_DAYS:
        return ("ON TRACK" if dec_day >= need and ratio >= config.MM_GO_EARN_PAY_RATIO
                else "BEHIND"), detail
    if dec_day >= need and ratio >= config.MM_GO_EARN_PAY_RATIO:
        return "GO", detail
    return "KILL", detail


def fav_gate(stats: dict) -> tuple[str, str]:
    """Decide the Favorites experiment's verdict from the maker leg's
    settled positions. Returns (verdict, human-readable detail)."""
    mk = stats.get("maker", {})
    n = mk.get("settled", 0)
    roi = mk.get("roi_pct")
    if n < config.FAV_GO_MIN_RESOLUTIONS:
        return "UNDERPOWERED", (f"{n}/{config.FAV_GO_MIN_RESOLUTIONS} settled maker "
                                f"positions, no verdict yet (this is honest, not broken)")
    if roi is not None and roi > 0:
        return "GO", f"maker conditional-on-fill ROI {roi:+.2f}% over {n} settled"
    return "KILL", f"maker conditional-on-fill ROI {roi if roi is not None else 0:+.2f}% <= 0 over {n} settled"


def render(state: dict, sims: list, fav_stats: dict) -> str:
    """Build the full text of REPORT.md: health block, both experiments'
    tables and gate verdicts, and the pre-registered kill criteria."""
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

    # Frozen (pre-registered horizon) verdicts override live recomputation:
    # a verdict that keeps mutating after day 14 isn't pre-registered at all.
    frozen_mm = state.get("mm_final")
    if frozen_mm:
        mm_verdict = f"FINAL: {frozen_mm['verdict']}"
        mm_detail = frozen_mm["detail"] + " (frozen at day 14)"
    frozen_fav = state.get("fav_final")
    if frozen_fav:
        fv_verdict = f"FINAL: {frozen_fav['verdict']}"
        fv_detail = frozen_fav["detail"] + f" (frozen at day {config.FAV_END_DAYS})"

    # Calibration tripwire: if the model claims rewards >10x the real-money
    # per-market baseline, the share model is uncalibrated. Never say GO.
    n_quoting = max(state.get("quoting_now", len(sims)), 1)
    rew_per_mkt_day = totals["rewards"] / max(days, 0.04) / n_quoting
    uncalibrated = rew_per_mkt_day > config.MM_CALIBRATION_MAX_PER_MARKET_DAY_CENTS
    if uncalibrated and not frozen_mm and mm_verdict in ("GO", "ON TRACK"):
        mm_verdict = "NO VERDICT (REWARD MODEL UNCALIBRATED)"
        mm_detail += (f"; modeled ${rew_per_mkt_day/100:.2f}/market/day exceeds the "
                      f"${config.MM_CALIBRATION_MAX_PER_MARKET_DAY_CENTS/100:.2f} tripwire")

    mk, tk = fav_stats.get("maker", {}), fav_stats.get("taker", {})
    pt = fav_stats.get("poly_taker", {})

    def usd(c):
        """Format a cents value as a signed dollar string, e.g. 150 -> '+$1.50'."""
        return f"${c/100:+.2f}"

    # -- health block: is the machine itself alive and behaving? ------------
    retired = sum(1 for s in sims if getattr(s, "retired", False))
    health = ["## Health", "", "| check | status |", "|---|---|"]
    last_cp = state.get("last_checkpoint_ts")
    if last_cp:
        health.append(
            f"| last checkpoint | {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(last_cp))} "
            f"(if this is > {config.HEALTH_STALE_HOURS}h old, the watchdog has already "
            "alerted Telegram) |")
    health.append(f"| jobs run (6h chain) | {state.get('jobs_started', 0)} |")
    job_start = state.get("last_job_start_ts")
    if job_start:
        health.append(f"| current job age | {(time.time() - job_start)/3600.0:.1f}h "
                      f"of {config.JOB_DEADLINE_MINUTES/60.0:.1f}h max |")
    health.append(f"| markets quoting / retired | {n_quoting} / {retired} |")
    health.append(f"| favorites open (maker/taker/poly) | {mk.get('open', 0)} / "
                  f"{tk.get('open', 0)} / {pt.get('open', 0)} |")
    health.append(f"| API requests last job | {state.get('api_requests_last_job', 0)} |")
    health.append("| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |")
    health.append("")

    lines = [
        "# SKIM: Skimming Kalshi's Incentive Markets (campaign report)",
        "",
        *(["**🏁 CAMPAIGN COMPLETE: verdicts below are FROZEN.**", ""]
          if state.get("campaign_complete") else []),
        f"_Auto-generated {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}, "
        f"**day {days:.1f} of {config.CAMPAIGN_DAYS}**. 100% sim: this repo only "
        "reads public endpoints and cannot place orders._",
        "",
        *health,
        "## Experiment 1: MM breadth (liquidity-pool harvesting)",
        "",
        f"**Gate status: {mm_verdict}**, {mm_detail}",
        "",
        "| metric | value |",
        "|---|---|",
        f"| markets quoting now / touched | {state.get('quoting_now', len(sims))} / {len(sims)} |",
        f"| est. rewards accrued | {usd(totals['rewards'])} |",
        f"| spread P&L (cash + mark) | {usd(totals['spread'])} |",
        f"| adverse selection (markout) | {usd(-totals['adverse'])} |",
        f"| maker fees | {usd(-totals['fees'])} |",
        f"| **decision number** | **{usd(totals['decision'])}** |",
        f"| decision at 0.25x rewards (share-optimism haircut) | "
        f"{usd(totals['decision'] - 0.75 * totals['rewards'])} |",
        f"| decision at 0.10x rewards | "
        f"{usd(totals['decision'] - 0.90 * totals['rewards'])} |",
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
        """Format an ROI percentage, or 'n/a' if there's nothing settled to compute it from."""
        return f"{v:+.2f}%" if v is not None else "n/a"

    mk_roi, tk_roi = roi_str(mk.get("roi_pct")), roi_str(tk.get("roi_pct"))
    pt_roi = roi_str(pt.get("roi_pct"))
    lines += [
        "",
        "## Experiment 2: Favorites (85-95c maker vs taker control)",
        "",
        f"**Gate status: {fv_verdict}**, {fv_detail}",
        "",
        "| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |",
        "|---|---|---|---|---|---|---|",
        f"| kalshi maker | {mk.get('open',0)} | {mk.get('unfilled',0)} | {n_mk} | "
        f"{w_mk} (win-rate CI {lo:.0%}-{hi:.0%}) | {usd(mk.get('pnl_cents',0.0))} | {mk_roi} |",
        f"| kalshi taker | {tk.get('open',0)} | - | {tk.get('settled',0)} | {tk.get('wins',0)} | "
        f"{usd(tk.get('pnl_cents',0.0))} | {tk_roi} |",
        f"| poly taker (zero-fee) | {pt.get('open',0)} | - | {pt.get('settled',0)} | "
        f"{pt.get('wins',0)} | {usd(pt.get('pnl_cents',0.0))} | {pt_roi} |",
        "",
        "_If maker ROI < taker ROI, queue fills are adversely selected: the exact "
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
        "- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO "
        "here is only actionable before renewal risk.",
    ]
    return "\n".join(lines)
