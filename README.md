# kalshi-paper-lab

A 14-day, fully-automated **paper trading** campaign that answers two pre-registered
questions about making money on Kalshi — with **zero machines of my own** (it runs
entirely on GitHub Actions) and **zero ability to trade** (it only reads public
endpoints; there are no exchange credentials anywhere).

**Live scoreboard: [REPORT.md](REPORT.md)** — regenerated every 30 minutes while
the campaign runs.

## The two experiments

### 1. MM breadth — liquidity-pool harvesting
Kalshi pays ~$35k/day in per-market liquidity incentive pools (CFTC-filed scoring
rules) to whoever rests qualifying quotes near the touch. This experiment
hypothetically quotes the **top 15 pooled markets** (200×200, join-the-touch),
reproduces the published scoring math every 20 seconds, and charges itself for
adverse selection using the real public trade tape through a queue-conservative
fill model.

**GO** iff decision ($ rewards + spread − adverse selection − fees) ≥ 3× the
measured 3-market baseline ($1.50/day) **and** earn/pay ≥ 1.5. Otherwise **KILL**.

### 2. Favorites — does the favorite-longshot bias survive being filled?
Academic work (~300k contracts) says makers on the ≥50¢ side earned ~+2.6%
post-fee — *unconditionally*. The open question is adverse selection: are the
fills you actually receive the bad ones? This experiment rests hypothetical maker
bids at 85–95¢ on soon-resolving markets **and** runs a taker control on the same
candidates. If maker ROI < taker ROI conditional on fill, the queue is adversely
selected and the edge is a mirage.

**GO** iff maker conditional-on-fill ROI > 0 after fees across ≥300 settled
positions. Until then the report says **UNDERPOWERED** — honestly, not broken.

## How it runs with my computer off

- `.github/workflows/campaign.yml` crons **every 6 hours**; each job is a
  long-runner (~5h40m) so coverage is near-continuous. A concurrency group
  serializes jobs; each one checkpoints state + evidence + `REPORT.md` back to
  the repo every 30 minutes, so a killed runner loses ≤30 min of data.
- Public repo ⇒ GitHub-hosted runners are free.
- The raw evidence (`data/evidence.jsonl`) doubles as an order-book/fill archive
  nobody else is recording — it cannot be backfilled later.

## Run it locally (optional)

```bash
pip install -r requirements.txt
python supervisor.py --once      # single smoke tick, no git
python -m unittest discover -s tests -q
```

## Honesty rules

- Paper first, always; this repo is structurally incapable of placing an order.
- Queue model is **conservative** (cancels assumed behind us → understates fills).
- Kill criteria are pre-registered in `config.py`/`report.py` and printed in the
  report; a null result is a *finding*, not a failure.
- Known clock: Kalshi's liquidity & volume incentive programs currently end
  **Sept 1, 2026** — a GO is only actionable before renewal risk.

*Scoring math ported from my mm_bot project (Kalshi's published Feb-2026 program
terms), including the period_reward centi-cents unit trap.*
