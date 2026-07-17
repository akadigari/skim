"""
health.py — the dead-man's switch. A tiny separate workflow (watchdog.yml) runs
this every 6 hours, offset from the campaign jobs. It reads the last checkpoint
timestamp from the COMMITTED state file: if the campaign chain has gone quiet
for more than HEALTH_STALE_HOURS, it screams on Telegram. Silent when healthy.

Why a separate workflow: the campaign job can't report its own death. This one
is a 10-second job with its own schedule, so a crashed supervisor, a broken
push, a dead API, or a disabled workflow all surface as the same loud symptom —
a stale checkpoint. (If GitHub Actions itself is down, nothing can alert; the
daily digest doubles as a positive heartbeat for that case: no digest = look.)
"""

from __future__ import annotations

import argparse
import json
import sys
import time

import config
import telegram

STATE_PATH = config.STATE_DIR / "campaign.json"


def staleness_hours(now: float | None = None) -> float | None:
    """Hours since the last committed checkpoint; None if no state yet."""
    try:
        raw = STATE_PATH.read_text()
    except FileNotFoundError:
        return None                    # campaign hasn't started: not an alarm
    except OSError:
        return float("inf")            # unreadable state IS an alarm
    try:
        state = json.loads(raw)
    except ValueError:
        return float("inf")            # corrupt committed state IS an alarm
    ts = state.get("last_checkpoint_ts") or state.get("campaign_start_ts")
    if not ts:
        return None
    return ((now or time.time()) - ts) / 3600.0


def is_stale(hours: float | None) -> bool:
    """True if the last checkpoint is older than the alarm threshold.
    No state at all is treated as NOT stale: the campaign simply hasn't had
    its first run yet, and alerting on that would cry wolf on day zero."""
    return hours is not None and hours > config.HEALTH_STALE_HOURS


def main() -> int:
    """Entry point for the watchdog workflow: check staleness and, in
    --watchdog mode, send a Telegram alert if the campaign chain has gone quiet."""
    ap = argparse.ArgumentParser(description="SKIM health watchdog (read-only)")
    ap.add_argument("--watchdog", action="store_true")
    args = ap.parse_args()
    hours = staleness_hours()
    if args.watchdog and is_stale(hours):
        telegram.send(
            f"🚨 SKIM heartbeat is STALE: last checkpoint {hours:.1f}h ago "
            f"(threshold {config.HEALTH_STALE_HOURS}h).\n"
            "The campaign chain has stopped — check the Actions tab:\n"
            "https://github.com/akadigari/skim/actions")
        print(f"STALE: {hours:.1f}h")
        return 0          # alerting IS the job succeeding; don't fail the run
    print(f"ok: last checkpoint {hours if hours is None else round(hours, 2)}h ago")
    return 0


if __name__ == "__main__":
    sys.exit(main())
