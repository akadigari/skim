# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-19 09:41 UTC, **day 7.5 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-19 09:41 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 16 |
| current job age | 5.0h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 60 / 60 / 54 |
| API requests last job | 28812 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-827.04/day vs GO bar $5.00/day; earn/pay -0.55 vs 1.5; fills 1393/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1506.26 |
| spread P&L (cash + mark) | $-3713.40 |
| adverse selection (markout) | $-3705.31 |
| maker fees | $-289.62 |
| **decision number** | **$-6202.07** |
| decision at 0.25x rewards (share-optimism haircut) | $-7331.77 |
| decision at 0.10x rewards | $-7557.71 |
| fills / snapshots (counted) | 1393 / 258555 (246369) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCATTEND-26JUL20-RIH | $63 | 37% | $+87.68 | $-40.34 | 32 | $+75.00 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-VIC | $63 | 34% | $+79.11 | $-76.22 | 25 | $+50.91 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 16% | $+37.28 | $-6.16 | 10 | $+16.40 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-LEB | $63 | 46% | $+47.32 | $-91.55 | 81 | $-66.25 |
| KXWCATTEND-26JUL20-ZEN | $63 | 32% | $+74.97 | $-32.04 | 40 | $-105.01 |
| KXWCATTEND-26JUL20-PAR | $63 | 30% | $+71.37 | $-54.57 | 41 | $-143.27 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+110.89 | $-85.80 | 63 | $-144.69 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-TOMH | $63 | 32% | $+75.28 | $-111.55 | 75 | $-169.52 |
| KXWCATTEND-26JUL20-LEO | $63 | 41% | $+96.82 | $-166.24 | 80 | $-251.58 |
| KXWCATTEND-26JUL20-KEN | $63 | 37% | $+87.45 | $-99.64 | 53 | $-254.88 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+88.77 | $-52.37 | 124 | $-266.85 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-KIM | $63 | 48% | $+114.11 | $-463.13 | 118 | $-532.90 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+101.80 | $-290.56 | 81 | $-536.82 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+88.99 | $-289.99 | 129 | $-642.61 |
| KXWCATTEND-26JUL20-RYA | $63 | 30% | $+69.63 | $-295.75 | 74 | $-736.93 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 46/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 21 | 46 | 43 (win-rate CI 82%-98%) | $+11.59 | +2.77% |
| kalshi taker | 60 | - | 67 | 64 | $+15.54 | +2.50% |
| poly taker (zero-fee) | 54 | - | 79 | 73 | $+10.67 | +1.48% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.