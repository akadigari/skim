"""
supervisor.py — the long-runner GitHub Actions executes. One invocation:

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
    try:
        return json.loads(STATE_PATH.read_text())
    except (OSError, ValueError):
        return {"campaign_start_ts": time.time(), "mm": [], "favorites": {}}


def save_state(state: dict, sims: list, fav: Favorites) -> None:
    state["mm"] = [s.to_dict() for s in sims]
    state["favorites"] = fav.to_dict()
    config.STATE_DIR.mkdir(exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(STATE_PATH)


def append_evidence(rows: list) -> None:
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
    def run(*args):
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
            run("pull", "--rebase")
        log.warning("git push failed after retries; data is committed locally")


# ---------------------------------------------------------------------------
# MM inventory grading: settle inventory in markets that resolved
# ---------------------------------------------------------------------------
def grade_mm(api: Kalshi, sims: list, evidence: list) -> list:
    keep = []
    for s in sims:
        m = api.market(s.ticker)
        status = (m.get("status") or "").lower()
        res = (m.get("result") or "").lower()
        if res in ("yes", "no"):
            settle = 100.0 if res == "yes" else 0.0
            s.cash_cents += settle * s.inventory
            s.inventory = 0.0
            s.last_mid = settle                   # spread_pnl marks at settlement
            s.bid = s.ask = None                  # keep the accumulator, stop quoting
            evidence.append({"type": "mm_settle", "ticker": s.ticker, "result": res,
                             "decision_cents": s.decision_cents})
        keep.append(s)                            # unsettled / fetch blip: hold as-is
    return keep


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Kalshi paper-lab supervisor (paper-only)")
    ap.add_argument("--once", action="store_true", help="single tick, no git (smoke test)")
    ap.add_argument("--no-push", action="store_true", help="commit checkpoints, don't push")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    api = Kalshi()
    state = load_state()
    sims = [MarketSim.from_dict(d) for d in state.get("mm", [])]
    fav = Favorites(state.get("favorites"))
    evidence: list = []

    # start-of-job housekeeping: grade what resolved, refill the roster
    sims = grade_mm(api, sims, evidence)
    fav.grade(api, evidence)
    live = [s for s in sims if s.last_mid not in (0.0, 100.0)]
    roster = select_markets(api, keep=[s.ticker for s in live])
    have = {s.ticker for s in sims}
    sims += [s for s in roster if s.ticker not in have]
    quoting = [s for s in sims if s.ticker in {r.ticker for r in roster}]
    log.info("roster: %d quoting, %d total accumulators", len(quoting), len(sims))

    deadline = time.time() + config.JOB_DEADLINE_MINUTES * 60
    next_checkpoint = time.time() + config.CHECKPOINT_MINUTES * 60

    while True:
        tick_started = time.time()
        for s in quoting:
            try:
                s.tick(api, evidence)
            except Exception as e:                # one bad market never kills the job
                log.warning("tick %s failed: %s", s.ticker, e)
        try:
            fav.scan_and_open(api, evidence)      # internally hourly-throttled
            fav.update_maker_fills(api, evidence)
        except Exception as e:
            log.warning("favorites pass failed: %s", e)

        if args.once:
            break
        now = time.time()
        if now >= deadline:
            break
        if now >= next_checkpoint:
            save_state(state, sims, fav)
            append_evidence(evidence)
            REPORT_PATH.write_text(report.render(state, sims, fav.stats()))
            git_checkpoint(push=not args.no_push)
            next_checkpoint = now + config.CHECKPOINT_MINUTES * 60
        sleep = config.MM_POLL_SECONDS - (time.time() - tick_started)
        if sleep > 0:
            time.sleep(sleep)

    # final flush
    fav.grade(api, evidence)
    save_state(state, sims, fav)
    append_evidence(evidence)
    REPORT_PATH.write_text(report.render(state, sims, fav.stats()))
    if not args.once:
        git_checkpoint(push=not args.no_push)
    log.info("done: %d api requests this job", api.request_count)


if __name__ == "__main__":
    main()
