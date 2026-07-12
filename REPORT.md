# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-12 18:05 UTC — **day 0.8 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-12 18:05 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 2 |
| current job age | 2.0h of 5.7h max |
| markets quoting / retired | 15 / 15 |
| favorites open (maker/taker/poly) | 34 / 34 / 20 |
| API requests last job | 11386 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: PENDING** — less than one day of data

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 30 |
| est. rewards accrued | $+386.71 |
| spread P&L (cash + mark) | $-655.84 |
| adverse selection (markout) | $-1092.82 |
| maker fees | $-56.18 |
| **decision number** | **$-1418.12** |
| decision at 0.25x rewards (share-optimism haircut) | $-1708.16 |
| decision at 0.10x rewards | $-1766.16 |
| fills / snapshots (counted) | 343 / 36045 (26559) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-KEN | $63 | 87% | $+17.44 | $-0.00 | 0 | $+17.44 |
| KXWCATTEND-26JUL20-TRA | $63 | 85% | $+17.12 | $-0.00 | 0 | $+17.12 |
| KXWCATTEND-26JUL20-KYL | $63 | 85% | $+17.11 | $-0.00 | 0 | $+17.11 |
| KXWCATTEND-26JUL20-ZEN | $63 | 85% | $+16.99 | $-0.00 | 0 | $+16.99 |
| KXWCATTEND-26JUL20-RYA | $63 | 84% | $+16.82 | $-0.00 | 0 | $+16.82 |
| KXWCATTEND-26JUL20-TIM | $63 | 77% | $+15.44 | $-0.00 | 7 | $+16.34 |
| KXWCATTEND-26JUL20-TOMH | $63 | 71% | $+14.30 | $-0.00 | 2 | $+14.31 |
| KXWCATTEND-26JUL20-RIH | $63 | 68% | $+13.54 | $-0.00 | 2 | $+13.53 |
| KXWCATTEND-26JUL20-VIC | $63 | 59% | $+11.77 | $-0.00 | 0 | $+11.77 |
| KXWCATTEND-26JUL20-PAR | $63 | 57% | $+11.53 | $-0.00 | 0 | $+11.53 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 54% | $+10.78 | $-5.00 | 1 | $+4.41 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-DRA | $63 | 65% | $+13.11 | $-10.57 | 3 | $-8.72 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-LEO | $63 | 80% | $+15.97 | $-41.56 | 7 | $-64.29 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-170.98 |
| KXWCATTEND-26JUL20-KIM | $63 | 56% | $+11.27 | $-110.42 | 4 | $-215.39 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 0/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 34 | 0 | 0 | 0 (win-rate CI 0%-100%) | $+0.00 | n/a |
| kalshi taker | 34 | — | 0 | 0 | $+0.00 | n/a |
| poly taker (zero-fee) | 20 | — | 5 | 4 | $-5.83 | -12.71% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.