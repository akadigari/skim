"""
telegram.py: SKIM's voice: a daily "is it making money?" digest and health
alerts, on a DEDICATED bot so this project stays separate from the others.

Config is env-only (GitHub repo secrets TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID);
with neither set every function is a silent no-op, so the lab runs fine keyless.
stdlib urllib, no new dependencies. Fail-soft: a Telegram outage can never
break a checkpoint or a tick.
"""

from __future__ import annotations

import json
import logging
import os
import ssl
import time
import urllib.request

import config

log = logging.getLogger("lab.telegram")


def _ctx() -> ssl.SSLContext:
    """Build an SSL context, preferring certifi's CA bundle if it's
    installed (some environments ship without a working default one)."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def configured() -> bool:
    """True if both Telegram secrets are set, i.e. sending is actually possible."""
    return bool(os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_CHAT_ID"))


def send(text: str) -> bool:
    """Send a plain-text message to the configured chat. Returns False (and
    never raises) if secrets aren't set or the request fails. Telegram
    being down must never break a checkpoint or a tick."""
    if not configured():
        return False
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
    payload = json.dumps({"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": text,
                          "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=_ctx()) as r:
            return 200 <= r.status < 300
    except Exception as e:
        log.warning("telegram send failed: %s", e)
        return False


def render_digest(state: dict, sims: list, fav_stats: dict,
                  mm_verdict: str, fav_verdict: str) -> str:
    """The daily money message. PAPER is said out loud every single time:
    this bot must never let a simulated number read like a real one."""
    start = state.get("campaign_start_ts") or time.time()
    day = max((time.time() - start) / 86400.0, 0.0)

    rewards = sum(s.reward_cents for s in sims)
    decision = sum(s.decision_cents for s in sims)
    adverse = sum(s.adverse_cents for s in sims)
    fills = sum(s.fills for s in sims)

    mk = fav_stats.get("maker", {})
    pt = fav_stats.get("poly_taker", {})

    def usd(c):
        """Format a cents value as a signed dollar string, e.g. 150 -> '+$1.50'."""
        return f"${c/100:+.2f}"

    lines = [
        f"📊 SKIM day {day:.1f}/{config.CAMPAIGN_DAYS}: PAPER results (nothing is real money)",
        "",
        f"MM pools [{mm_verdict}]: decision {usd(decision)} "
        f"(rewards {usd(rewards)}, AS {usd(-adverse)}, {fills} fills, "
        f"{len(sims)} markets)",
        f"Favorites [{fav_verdict}]: kalshi maker {mk.get('settled', 0)} settled, "
        f"P&L {usd(mk.get('pnl_cents', 0.0))}"
        + (f" | poly taker {pt.get('settled', 0)} settled, "
           f"P&L {usd(pt.get('pnl_cents', 0.0))}" if pt else ""),
        "",
        f"🩺 health: job #{state.get('jobs_started', '?')} of the 6h chain, "
        f"{state.get('quoting_now', len(sims))} markets quoting, "
        f"{state.get('api_requests_last_job', 0)} API reqs last job, "
        f"watchdog armed ({config.HEALTH_STALE_HOURS:g}h stale alarm)",
        "",
        "Full report: https://github.com/akadigari/skim/blob/main/REPORT.md",
    ]
    return "\n".join(lines)
