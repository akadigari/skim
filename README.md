# SKIM — Skimming Kalshi's Incentive Markets

A 14-day, fully-automated **paper trading** campaign that tests the two most
credible "actually makes money" ideas from my prediction-market research — with
**zero machines of my own** (it runs entirely on GitHub Actions) and **zero
ability to trade** (public read-only endpoints; no exchange credentials exist
anywhere in this repo or its secrets).

The name is the thesis: don't out-predict anyone — **skim** what's structurally
on offer. Kalshi pays daily liquidity-incentive **pools** for resting quotes
(experiment 1 skims the pools), and retail flow overpays for longshots
(experiment 2 skims the favorite side of that bias).

**Live scoreboard: [REPORT.md](REPORT.md)** — regenerated every 30 minutes while
the campaign runs. A dedicated Telegram bot DMs a daily digest and screams if
the pipeline dies.

## The experiments

### 1. MM breadth — liquidity-pool skimming
~3,900 active pools exist right now. SKIM hypothetically quotes the **top-15**
(200×200, join-the-touch), reproduces Kalshi's CFTC-filed scoring math every 20
seconds, and charges itself adverse selection via the real public trade tape
through a queue-conservative fill model.

**GO** iff decision ($ rewards + spread − adverse selection − fees) ≥ 3× the
3-market baseline ($1.67/day, the midpoint of mm_bot's paper $20-80/month) **and** earn/pay ≥ 1.5, **and** the fill/cost side actually has evidence (below a minimum fill count the gate reads UNMEASURED, never GO). Else **KILL**.

### 2. Favorites — does the favorite-longshot bias survive being filled?
Rest hypothetical maker bids at 85–95¢ on soon-resolving Kalshi markets, with a
taker control on the same candidates. If maker ROI < taker ROI conditional on
fill, the queue is adversely selected and the "edge" is a mirage. A
**Polymarket taker-only leg** (fees are zero there) tests whether the bias
exists at all under the cheapest possible execution; the pre-registered gate is
judged on the Kalshi maker leg only.

**GO** iff maker conditional-on-fill ROI > 0 after fees across ≥300 settled
positions; **UNDERPOWERED** is reported honestly until then.

## How it runs with the laptop off

- `campaign.yml` crons **every 6h**; each job long-runs ~5h40m, so coverage is a
  near-continuous chain. Checkpoints (state + evidence + REPORT.md) commit back
  every 30 min — a killed runner loses ≤30 min.
- `watchdog.yml` is the **dead-man's switch**: a 10-second job offset between
  campaign runs; if the committed heartbeat is >7.5h old it alerts Telegram.
  Silent when healthy.
- Public repo ⇒ GitHub-hosted runners are free.
- `data/evidence.jsonl` doubles as an orderbook/fill archive nobody else records.

## Telegram (dedicated bot — optional)

This project uses its **own** bot so it stays separate from my other scanners:

1. In Telegram: **@BotFather** → `/newbot` → name it (e.g. `SKIM Lab`) → copy the token.
2. Message the new bot once, then get your chat id from **@userinfobot**.
3. Repo → Settings → Secrets and variables → Actions → add
   `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.

You'll get one digest per day ("📊 SKIM day 3.2 — PAPER results…") plus health
alerts. Unset = everything still runs, just silently.

## Run it locally (optional)

```bash
pip install -r requirements.txt
python supervisor.py --once      # single smoke tick, no git
python -m unittest discover -s tests -q
```

## Honesty rules

- Paper first, always; every digest says PAPER out loud.
- Queue model understates fills (cancels assumed behind us). Review-corrected honesty note: for the decision number that bias is *optimistic* — rewards accrue without fills while fills mostly bring costs — so the GO gate requires a minimum body of fill evidence and the report prints reward-haircut sensitivity.
- The share estimator assumes competitors don't react to our quotes; the report prints the decision number at 1x / 0.25x / 0.1x reward haircuts so that optimism is visible, and an uncalibrated reward model demotes GO to NO VERDICT.
- Kill criteria are pre-registered in `config.py`/`report.py`; a null result is
  a finding, not a failure.
- Known clock: Kalshi's liquidity/volume incentive programs currently end
  **Sept 1, 2026** — a GO is only actionable before renewal risk.

*Scoring math ported from my mm_bot project (Kalshi's published Feb-2026 program
terms, including the period_reward centi-cents unit trap); Polymarket resolution
reader ported from my logical_arb project.*
