# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-11 23:13 UTC — **day 0.1 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: PENDING** — less than one day of data

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 15 |
| est. rewards accrued | $+118.39 |
| spread P&L (cash + mark) | $+144.25 |
| adverse selection (markout) | $-366.38 |
| maker fees | $-31.52 |
| **decision number** | **$-135.25** |
| decision at 0.25x rewards (share-optimism haircut) | $-224.05 |
| decision at 0.10x rewards | $-241.81 |
| fills / snapshots (counted) | 126 / 4080 (4080) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 64% | $+7.27 | $-83.02 | 30 | $+78.54 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+11.44 | $-37.00 | 5 | $+10.77 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+9.88 | $-0.00 | 0 | $+9.88 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 69% | $+8.39 | $-0.00 | 0 | $+8.39 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 67% | $+8.12 | $-0.00 | 0 | $+8.12 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 63% | $+7.62 | $-0.00 | 0 | $+7.62 |
| KXAAAGASD-26JUL12-3.870 | $198 | 51% | $+6.38 | $-0.00 | 23 | $+6.79 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 84% | $+10.25 | $-2.21 | 6 | $+5.49 |
| KXAAAGASD-26JUL12-3.875 | $198 | 72% | $+8.92 | $-12.18 | 13 | $-11.23 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 60% | $+6.83 | $-8.00 | 3 | $-12.94 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 32% | $+3.66 | $-4.90 | 5 | $-14.53 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 63% | $+7.19 | $-7.03 | 12 | $-17.85 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 80% | $+9.77 | $-13.86 | 4 | $-42.72 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 42% | $+4.79 | $-55.00 | 6 | $-46.67 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 70% | $+7.91 | $-143.19 | 19 | $-124.91 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 0/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 19 | 0 | 0 | 0 (win-rate CI 0%-100%) | $+0.00 | n/a |
| kalshi taker | 19 | — | 0 | 0 | $+0.00 | n/a |
| poly taker (zero-fee) | 4 | — | 0 | 0 | $+0.00 | n/a |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.