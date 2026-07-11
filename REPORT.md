# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-11 22:13 UTC — **day 0.0 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: PENDING** — less than one day of data

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 15 |
| est. rewards accrued | $+43.83 |
| spread P&L (cash + mark) | $+117.34 |
| adverse selection (markout) | $-65.00 |
| maker fees | $-9.17 |
| **decision number** | **$+87.00** |
| decision at 0.25x rewards (share-optimism haircut) | $+54.13 |
| decision at 0.10x rewards | $+47.56 |
| fills / snapshots (counted) | 30 / 1365 (1365) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 88% | $+3.34 | $-20.00 | 10 | $+73.95 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 96% | $+3.88 | $-0.00 | 2 | $+3.92 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 83% | $+3.37 | $-0.00 | 0 | $+3.37 |
| KXAAAGASD-26JUL12-3.875 | $198 | 72% | $+3.00 | $-0.00 | 6 | $+3.29 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+3.46 | $-0.00 | 5 | $+3.20 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 78% | $+3.16 | $-0.00 | 0 | $+3.16 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 75% | $+2.85 | $-0.00 | 0 | $+2.85 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 69% | $+2.81 | $-0.00 | 0 | $+2.81 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 67% | $+2.73 | $-0.00 | 0 | $+2.73 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 61% | $+2.50 | $-0.00 | 0 | $+2.50 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 62% | $+2.35 | $-0.00 | 0 | $+2.35 |
| KXAAAGASD-26JUL12-3.870 | $198 | 52% | $+2.17 | $-0.00 | 0 | $+2.17 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 72% | $+2.72 | $-0.00 | 1 | $+1.53 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 61% | $+2.33 | $-0.00 | 2 | $-2.93 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 82% | $+3.13 | $-45.00 | 4 | $-17.90 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 0/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 12 | 0 | 0 | 0 (win-rate CI 0%-100%) | $+0.00 | n/a |
| kalshi taker | 12 | — | 0 | 0 | $+0.00 | n/a |
| poly taker (zero-fee) | 4 | — | 0 | 0 | $+0.00 | n/a |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.