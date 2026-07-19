# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-19 07:10 UTC, **day 7.4 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-19 07:10 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 16 |
| current job age | 2.5h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 60 / 60 / 53 |
| API requests last job | 14450 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-821.48/day vs GO bar $5.00/day; earn/pay -0.54 vs 1.5; fills 1347/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1467.86 |
| spread P&L (cash + mark) | $-3593.02 |
| adverse selection (markout) | $-3666.07 |
| maker fees | $-283.15 |
| **decision number** | **$-6074.38** |
| decision at 0.25x rewards (share-optimism haircut) | $-7175.28 |
| decision at 0.10x rewards | $-7395.46 |
| fills / snapshots (counted) | 1347 / 251775 (239589) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-RIH | $63 | 36% | $+82.89 | $-40.34 | 32 | $+64.73 |
| KXWCATTEND-26JUL20-VIC | $63 | 34% | $+76.84 | $-76.22 | 25 | $+48.63 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 16% | $+36.40 | $-6.16 | 10 | $+15.53 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-LEB | $63 | 47% | $+44.59 | $-91.32 | 79 | $-73.49 |
| KXWCATTEND-26JUL20-ZEN | $63 | 32% | $+73.76 | $-32.04 | 40 | $-106.23 |
| KXWCATTEND-26JUL20-PAR | $63 | 30% | $+67.67 | $-52.02 | 35 | $-137.46 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+107.67 | $-85.80 | 63 | $-147.92 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-TOMH | $63 | 31% | $+70.27 | $-95.55 | 73 | $-182.45 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+96.69 | $-166.24 | 76 | $-227.53 |
| KXWCATTEND-26JUL20-KEN | $63 | 37% | $+84.37 | $-99.64 | 51 | $-258.08 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+86.44 | $-52.37 | 124 | $-269.18 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+112.08 | $-457.13 | 111 | $-514.61 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+99.32 | $-287.54 | 77 | $-538.18 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+87.12 | $-278.55 | 119 | $-618.76 |
| KXWCATTEND-26JUL20-RYA | $63 | 29% | $+66.94 | $-295.75 | 65 | $-636.32 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 46/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 21 | 46 | 43 (win-rate CI 82%-98%) | $+11.59 | +2.77% |
| kalshi taker | 60 | - | 67 | 64 | $+15.54 | +2.50% |
| poly taker (zero-fee) | 53 | - | 77 | 72 | $+18.56 | +2.65% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.