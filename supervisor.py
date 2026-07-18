"""
supervisor.py: the long-runner GitHub Actions executes. One invocation:

    load state -> (re)select markets -> grade favorites -> LOOP until deadline:
        every MM_POLL_SECONDS: tick every MM market (book + tape -> sim)
        hourly:                favorites scan + maker-fill update
        every CHECKPOINT_MINUTES: persist state/evidence, refresh REPORT.md,
                                  git commit + push (so a killed runner loses
                                  at most one checkpoint of data)

The workflow crons every 6 hours with a concurrency group, so successive jobs
form a near-continuous chain; JOB_DEADLINE_MINUTES exits this one cleanly
before the next takes over. All endpoints are public; there is nothing here
that can trade. Run locally with --once for a single smoke tick (no git).
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import time

import config
import report
from favorites import Favorites
from kalshi import Kalshi
from mm_sim import MarketSim, select_markets

log = logging.getLogger("lab.supervisor")

STATE_PATH = config.STATE_DIR / "campaign.json"
EVIDENCE_PATH = config.DATA_DIR / "evidence.jsonl"
REPORT_PATH = config.BASE_DIR / "REPORT.md"


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
def load_state() -> dict:
    """Fresh state ONLY when no file exists. A corrupt/unreadable committed
    state must raise: a silent reset would wipe the campaign and be committed
    as truth within 30 minutes. The loud failure trips the health watchdog."""
    try:
        raw = STATE_PATH.read_text()
    except FileNotFoundError:
        return {"campaign_start_ts": time.time(), "mm": [], "favorites": {}}
    return json.loads(raw)   # ValueError/OSError propagate on purpose


def save_state(state: dict, sims: list, fav: Favorites) -> None:
    """Write the campaign state to state/campaign.json, via a temp file +
    atomic rename so a crash mid-write never leaves a half-written file
    that the health watchdog or next job would choke on."""
    state["mm"] = [s.to_dict() for s in sims]
    state["favorites"] = fav.to_dict()
    state["last_checkpoint_ts"] = time.time()   # the health watchdog reads this
    config.STATE_DIR.mkdir(exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(STATE_PATH)


def maybe_send_digest(state: dict, sims: list, fav: Favorites) -> None:
    """Once a day, tell the (dedicated) Telegram bot how the SIM money looks."""
    import report as report_mod
    import telegram
    if not telegram.configured():
        return
    if time.time() - state.get("last_digest_ts", 0.0) < config.DIGEST_EVERY_HOURS * 3600:
        return
    days = max((time.time() - state.get("campaign_start_ts", time.time())) / 86400.0, 0.0)
    totals = {"rewards": sum(s.reward_cents for s in sims),
              "spread": sum(s.spread_pnl_cents for s in sims),
              "adverse": sum(s.adverse_cents for s in sims),
              "fees": sum(s.fees_cents for s in sims),
              "decision": sum(s.decision_cents for s in sims)}
    mm_v, _ = report_mod.mm_gate(totals, days)
    fv_v, _ = report_mod.fav_gate(fav.stats())
    if telegram.send(telegram.render_digest(state, sims, fav.stats(), mm_v, fv_v)):
        state["last_digest_ts"] = time.time()


def append_evidence(rows: list) -> None:
    """Append this checkpoint's evidence rows (fills, settles, etc.) to
    data/evidence.jsonl, then clear the in-memory list so nothing is written twice."""
    if not rows:
        return
    config.DATA_DIR.mkdir(exist_ok=True)
    with open(EVIDENCE_PATH, "a") as f:
        for r in rows:
            f.write(json.dumps(r, default=str) + "\n")
    rows.clear()


# ---------------------------------------------------------------------------
# Git checkpointing (runs inside Actions; silently skipped when not a repo)
# ---------------------------------------------------------------------------
def git_checkpoint(push: bool) -> None:
    """Commit (and optionally push) the current state/data/REPORT.md as one
    checkpoint. No-ops outside a git repo. On a push race, pulls and retries
    a few times rather than leaving a half-finished rebase behind."""
    def run(*args):
        """Run one git command in the repo root and capture its output."""
        return subprocess.run(["git", *args], cwd=config.BASE_DIR,
                              capture_output=True, text=True)
    if run("rev-parse", "--is-inside-work-tree").returncode != 0:
        return
    run("add", "state", "data", "REPORT.md")
    if run("diff", "--cached", "--quiet").returncode == 0:
        return                                    # nothing new this checkpoint
    stamp = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    run("commit", "-m", f"lab: checkpoint {stamp}")
    if push:
        for _ in range(3):                        # tolerate a racing push
            if run("push").returncode == 0:
                return
            if run("pull", "--rebase").returncode != 0:
                run("rebase", "--abort")          # never leave a half-rebase behind
        log.warning("git push failed after retries; data is committed locally")


# ---------------------------------------------------------------------------
# MM inventory grading: settle inventory in markets that resolved
# ---------------------------------------------------------------------------
def grade_mm(api: Kalshi, sims: list, evidence: list) -> list:
    """Check every still-active MM sim's market for a real-world result and
    settle its hypothetical inventory (win/loss/void) if the market resolved."""
    for s in sims:
        if s.retired:
            continue
        m = api.market(s.ticker)
        status = (m.get("status") or "").lower()
        res = (m.get("result") or "").lower()
        if res in ("yes", "no"):
            settle = 100.0 if res == "yes" else 0.0
            s.flush_markouts(settle, evidence)    # near-settlement AS is never dropped
            s.cash_cents += settle * s.inventory
            s.inventory = 0.0
            s.last_mid = settle                   # spread_pnl marks at settlement
            s.bid = s.ask = None
            s.retired = True                      # keep the totals, stop ticking
            evidence.append({"type": "mm_settle", "ticker": s.ticker, "result": res,
                             "decision_cents": s.decision_cents})
        elif status in ("settled", "finalized", "determined"):
            # terminal WITHOUT a yes/no result: a void/scratch. Unwind at the
            # last known mark, inventing neither a win nor a loss.
            mark = s.last_mid or 0.0
            s.flush_markouts(mark, evidence)
            s.cash_cents += mark * s.inventory
            s.inventory = 0.0
            s.bid = s.ask = None
            s.retired = True
            evidence.append({"type": "mm_void", "ticker": s.ticker,
                             "decision_cents": s.decision_cents})
    return sims


# ---------------------------------------------------------------------------
# Wind-down (day 14 -> FAV_END_DAYS): freeze MM, keep grading favorites
# ---------------------------------------------------------------------------
def wind_down(api, poly, state, sims, fav, evidence, age_days, push) -> None:
    """After day CAMPAIGN_DAYS: no new exposure, no MM accrual. Freeze the MM
    verdict once, keep grading favorites until FAV_END_DAYS, then freeze that
    and mark the campaign complete. Each pass is a short job (~1 min)."""
    import report as report_mod
    if "mm_final" not in state:
        grade_mm(api, sims, evidence)     # settle anything already resolved first
        days = float(config.CAMPAIGN_DAYS)
        totals = {"rewards": sum(s.reward_cents for s in sims),
                  "spread": sum(s.spread_pnl_cents for s in sims),
                  "adverse": sum(s.adverse_cents for s in sims),
                  "fees": sum(s.fees_cents for s in sims),
                  "decision": sum(s.decision_cents for s in sims),
                  "fills": sum(s.fills for s in sims)}
        verdict, detail = report_mod.mm_gate(totals, days)
        state["mm_final"] = {"verdict": verdict, "detail": detail,
                             "totals": totals, "frozen_ts": time.time()}
        log.info("MM verdict FROZEN at day %.1f: %s", age_days, verdict)
    grade_mm(api, sims, evidence)         # settle stragglers for the record
    fav.grade(api, evidence, poly=poly)
    if age_days >= config.FAV_END_DAYS and "fav_final" not in state:
        verdict, detail = report_mod.fav_gate(fav.stats())
        state["fav_final"] = {"verdict": verdict, "detail": detail,
                              "frozen_ts": time.time()}
        state["campaign_complete"] = True
        log.info("Favorites verdict FROZEN: %s, campaign complete", verdict)
    state["api_requests_last_job"] = api.request_count
    append_evidence(evidence)
    save_state(state, sims, fav)
    REPORT_PATH.write_text(report.render(state, sims, fav.stats()))
    git_checkpoint(push=push)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    """Entry point for one supervisor run: load state, refresh the quoting
    roster, then loop ticking every quoted market and running the favorites
    scan until the job deadline, checkpointing to git along the way."""
    ap = argparse.ArgumentParser(description="Kalshi sim-lab supervisor (sim-only)")
    ap.add_argument("--once", action="store_true", help="single tick, no git (smoke test)")
    ap.add_argument("--no-push", action="store_true", help="commit checkpoints, don't push")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    api = Kalshi()
    poly = None
    if config.POLY_ENABLED:
        from polymarket import Polymarket
        poly = Polymarket()
    state = load_state()
    state["jobs_started"] = state.get("jobs_started", 0) + 1
    state["last_job_start_ts"] = time.time()
    sims = [MarketSim.from_dict(d) for d in state.get("mm", [])]
    fav = Favorites(state.get("favorites"))
    evidence: list = []

    # ---- campaign phases (review: the day-14 verdict must FREEZE) ----------
    age_days = (time.time() - state.get("campaign_start_ts", time.time())) / 86400.0
    if state.get("campaign_complete"):
        log.info("campaign complete, no-op run")
        return
    if age_days >= config.CAMPAIGN_DAYS:
        wind_down(api, poly, state, sims, fav, evidence, age_days,
                  push=not args.no_push and not args.once)
        return

    # start-of-job housekeeping: grade what resolved, refill the roster
    sims = grade_mm(api, sims, evidence)
    fav.grade(api, evidence, poly=poly)
    kept = [s for s in sims if not s.retired]
    roster = select_markets(api, kept)            # refreshes kept sims' pool terms
    have = {s.ticker for s in sims}
    sims += [s for s in roster if s.ticker not in have]
    quoting = roster
    state["quoting_now"] = len(quoting)
    log.info("roster: %d quoting, %d total accumulators", len(quoting), len(sims))

    deadline = time.time() + config.JOB_DEADLINE_MINUTES * 60
    next_checkpoint = time.time() + config.CHECKPOINT_MINUTES * 60
    next_fill_sweep = time.time() + config.FAV_FILL_CHECK_SECONDS
    next_fav_grade = time.time() + 3600

    while True:
        tick_started = time.time()
        for s in quoting:
            try:
                s.tick(api, evidence)
            except Exception as e:                # one bad market never kills the job
                log.warning("tick %s failed: %s", s.ticker, e)
        try:
            fav.scan_and_open(api, evidence, poly=poly)   # internally hourly-throttled
            now0 = time.time()
            if now0 >= next_fill_sweep:
                fav.update_maker_fills(api, evidence)
                next_fill_sweep = now0 + config.FAV_FILL_CHECK_SECONDS
            if now0 >= next_fav_grade:
                fav.grade(api, evidence, poly=poly)       # recycle slots hourly
                next_fav_grade = now0 + 3600
        except Exception as e:
            log.warning("favorites pass failed: %s", e)

        if args.once:
            break
        now = time.time()
        if now >= deadline:
            break
        if now >= next_checkpoint:
            state["api_requests_last_job"] = api.request_count
            maybe_send_digest(state, sims, fav)   # daily; no-op when unconfigured
            append_evidence(evidence)             # evidence first: rows the state
            save_state(state, sims, fav)          # doesn't count yet are benign
            REPORT_PATH.write_text(report.render(state, sims, fav.stats()))
            git_checkpoint(push=not args.no_push)
            next_checkpoint = now + config.CHECKPOINT_MINUTES * 60
        sleep = config.MM_POLL_SECONDS - (time.time() - tick_started)
        if sleep > 0:
            time.sleep(sleep)

    # final flush
    fav.grade(api, evidence, poly=poly)
    state["api_requests_last_job"] = api.request_count
    append_evidence(evidence)
    save_state(state, sims, fav)
    REPORT_PATH.write_text(report.render(state, sims, fav.stats()))
    if not args.once:
        git_checkpoint(push=not args.no_push)
    log.info("done: %d api requests this job", api.request_count)


if __name__ == "__main__":
    main()
