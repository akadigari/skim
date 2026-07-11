"""
config.py — every knob for the 2-week Kalshi paper campaign. Hand-set, inspectable.

TWO EXPERIMENTS, ONE VERDICT EACH (see report.py for the exact gates):
  MM BREADTH  — rest hypothetical two-sided quotes on the top-N liquidity-pool
                markets and measure what Kalshi's published scoring would pay,
                minus what the trade tape says adverse selection would cost.
  FAVORITES   — rest hypothetical maker bids at 85-95c on soon-resolving markets
                (plus a taker control) and measure conditional-on-fill ROI.

PAPER ONLY. This repo never sends an order; it only reads public endpoints.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATE_DIR = BASE_DIR / "state"     # small JSON state, committed back to the repo
DATA_DIR = BASE_DIR / "data"       # JSONL evidence (fills, scans, snapshots), committed

# --- Kalshi public API (no auth for any of this) ----------------------------
API_BASE = "https://api.elections.kalshi.com/trade-api/v2"
REQUEST_GAP_SECONDS = 0.15         # politeness gap between ANY two requests
TIMEOUT_SECONDS = 10
MAX_RETRIES = 2

# period_reward units are CENTI-CENTS (verified in mm_bot the hard way:
# 200000 == $20.00/period, not $2,000). Get this wrong -> 100x error.
PERIOD_REWARD_UNITS_TO_CENTS = 0.01
TICK_CENTS = 1.0
DAILY_POOL_CAP_CENTS = 100_000.0   # $1,000/day per-program payout bound (published)

# --- MM breadth experiment ---------------------------------------------------
MM_N_MARKETS = 15                  # how many pooled markets we quote concurrently
MM_QUOTE_SIZE = 200                # hypothetical contracts per side (audit assumption)
MM_CANDIDATE_POOL_LIMIT = 120      # rank this many top pools/day (book fetch each)
MM_POLL_SECONDS = 20               # sim tick; Kalshi snapshots 1/s — our share
                                   # estimator stays unbiased, just noisier
MM_MARKOUT_SECONDS = 300           # adverse-selection markout horizon (5 min)
MM_RESERVE_PER_MARKET_USD = 200.0  # capital reserve assumption for ranking
QUEUE_POLICY = "conservative"      # cancels assumed BEHIND us (understates fills)

# Maker fee: Kalshi now charges makers ~25% of the taker fee (pm.wiki, 2026).
# VERIFY against kalshi.com's fee schedule before any live decision.
TAKER_FEE_COEF = 0.07              # fee = ceil(coef * C * P * (1-P)), dollars
MAKER_FEE_FRACTION = 0.25

# --- Favorites experiment ----------------------------------------------------
FAV_BAND_CENTS = (85.0, 95.0)      # rest bids on the high-probability side here
FAV_MAX_DAYS_TO_CLOSE = 7          # only soon-resolving markets (per Whelan: avoid
                                   # final-day entries; we log entry-day for cuts)
FAV_CONTRACTS = 10                 # small hypothetical size per position
FAV_MIN_BID_SIZE = 50              # book must show some real size at our price
FAV_MAX_POSITIONS = 60             # cap concurrent open paper positions
FAV_SCAN_SECONDS = 3600            # scan cadence (hourly)

# --- Campaign / gates ----------------------------------------------------------
CAMPAIGN_DAYS = 14
# mm_bot's measured 3-market baseline was $20-80/month => ~$0.67-2.67/day.
# GO requires the breadth decision-number to reach 3x the midpoint of that.
MM_BASELINE_DECISION_PER_DAY_CENTS = 150.0     # $1.50/day midpoint baseline
MM_GO_MULTIPLE = 3.0                            # GO: decision/day >= 3x baseline
MM_GO_EARN_PAY_RATIO = 1.5                      # AND (rewards+spread)/(AS+fees) >= 1.5
FAV_GO_MIN_RESOLUTIONS = 300                    # favorites verdict needs n >= this
                                                # (report shows Wilson CI + power honestly)

# --- Polymarket favorites leg (phase 1: TAKER-ONLY — see polymarket.py) -------
POLY_ENABLED = True
POLY_SCAN_PAGES = 5                # top-volume gamma pages scanned per hour
POLY_MAX_SPREAD_CENTS = 3.0        # skip wide-spread books (unfair taker test)
POLY_TAKER_FEE_CENTS = 0.0         # Polymarket taker fee is currently zero
POLY_FAV_MAX_POSITIONS = 40        # separate cap from the Kalshi book

# --- Telegram (dedicated SKIM bot — separate from other projects' bots) -------
# Set as GitHub repo secrets TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID; env-only,
# everything no-ops silently when unset. Digest once a day; PAPER said out loud.
DIGEST_EVERY_HOURS = 20            # >= this long since last digest -> send one

# --- Health watchdog -----------------------------------------------------------
# Campaign jobs checkpoint every 30 min while running and chain every ~6h; if
# the committed state is older than this, something in the chain died.
HEALTH_STALE_HOURS = 7.5

# --- Long-runner scheduling (GitHub Actions) ----------------------------------
# The workflow crons every 6h; each job runs until this deadline then exits so
# the next queued job takes over (concurrency group serializes them).
JOB_DEADLINE_MINUTES = 340         # 5h40m << the 355-min workflow timeout
CHECKPOINT_MINUTES = 30            # persist state + git commit/push this often
