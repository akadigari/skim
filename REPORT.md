# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-23 19:01 UTC, **day 11.9 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-23 19:01 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 25 |
| current job age | 3.0h of 5.7h max |
| markets quoting / retired | 15 / 88 |
| favorites open (maker/taker/poly) | 60 / 60 / 47 |
| API requests last job | 17261 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-2377.33/day vs GO bar $5.00/day; earn/pay -0.45 vs 1.5; fills 5133/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 103 |
| est. rewards accrued | $+2518.27 |
| spread P&L (cash + mark) | $-11324.12 |
| adverse selection (markout) | $-18069.88 |
| maker fees | $-1386.12 |
| **decision number** | **$-28261.85** |
| decision at 0.25x rewards (share-optimism haircut) | $-30150.55 |
| decision at 0.10x rewards | $-30528.29 |
| fills / snapshots (counted) | 5133 / 390885 (340831) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXDXYDUD-26JUL20-T100.7560 | $218 | 47% | $+48.27 | $-22.59 | 19 | $+106.46 |
| KXWNBAMENTION-26JUL16NYDAL-CAIT | $51 | 45% | $+10.78 | $-2.15 | 7 | $+94.02 |
| KXTEMPAUSH-26JUL2201-T80.99 | $1000 | 93% | $+4.54 | $-26.22 | 12 | $+79.24 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWNBAMENTION-26JUL16NYDAL-OVER | $51 | 64% | $+15.51 | $-0.45 | 12 | $+58.71 |
| KXAAAGASD-26JUL23-4.105 | $183 | 57% | $+24.63 | $-37.13 | 17 | $+53.40 |
| KXMLBMENTION-26JUL21LADPHI-WILD | $193 | 50% | $+15.87 | $-0.17 | 22 | $+51.10 |
| KXAAAGASD-26JUL23-4.100 | $183 | 59% | $+25.62 | $-108.60 | 39 | $+47.03 |
| KXAAAGASD-26JUL23-4.115 | $183 | 62% | $+26.72 | $-5.11 | 15 | $+46.20 |
| KXMLBMENTION-26JUL21LADPHI-WALK | $193 | 67% | $+30.57 | $-0.00 | 6 | $+37.74 |
| KXMLBMENTION-26JUL21LADPHI-PINC | $193 | 49% | $+22.19 | $-7.78 | 16 | $+37.04 |
| KXAAAGASD-26JUL23-4.120 | $183 | 62% | $+24.80 | $-5.67 | 12 | $+34.27 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXMLBMENTION-26JUL21LADPHI-EXTR | $193 | 50% | $+22.02 | $-0.04 | 3 | $+22.10 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXTEMPCHIH-26JUL2101-T75.99 | $1000 | 80% | $+5.02 | $-19.00 | 4 | $+20.77 |
| KXAAAGASD-26JUL22-4.080 | $193 | 54% | $+24.41 | $-11.19 | 14 | $+16.80 |
| KXAAAGASD-26JUL23-4.125 | $183 | 42% | $+15.55 | $-2.00 | 5 | $+13.28 |
| KXWNBAMENTION-26JUL16NYDAL-TRAD | $51 | 51% | $+12.26 | $-0.00 | 0 | $+12.26 |
| KXTEMPCHIH-26JUL2101-T74.99 | $1000 | 85% | $+5.34 | $-1.58 | 3 | $+11.80 |
| KXWNBAMENTION-26JUL19CHIATL-TAUR | $51 | 90% | $+10.91 | $-0.00 | 0 | $+10.91 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXEARNINGSMENTIONAAL-26JUL23-ATH | $67 | 54% | $+8.62 | $-1.51 | 16 | $+6.56 |
| KXWNBAMENTION-26JUL16NYDAL-ANKL | $51 | 47% | $+11.39 | $-0.24 | 3 | $+5.32 |
| KXAAAGASD-26JUL23-4.135 | $183 | 36% | $+6.58 | $-1.00 | 2 | $+5.31 |
| KXWCATTEND-26JUL20-VIC | $63 | 35% | $+86.21 | $-136.03 | 101 | $+5.25 |
| KXAAAGASD-26JUL22-4.070 | $193 | 67% | $+30.45 | $-25.72 | 43 | $+4.79 |
| KXMLBMENTION-26JUL21LADPHI-BUNT | $193 | 49% | $+22.46 | $-43.20 | 29 | $+4.68 |
| KXTEMPCHIH-26JUL2201-T66.99 | $1000 | 35% | $+1.85 | $-0.25 | 2 | $+0.84 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXAAAGASD-26JUL23-4.110 | $183 | 68% | $+29.16 | $-19.21 | 19 | $-0.78 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXTRUMPPHOTO-26JUL26-7 | $34 | 17% | $+4.46 | $-0.48 | 13 | $-3.27 |
| KXAAAGASD-26JUL23-4.145 | $183 | 8% | $+1.09 | $-1.00 | 2 | $-3.99 |
| KXWNBAMENTION-26JUL16NYDAL-TRAV | $51 | 48% | $+11.60 | $-9.00 | 2 | $-4.50 |
| KXTEMPDCH-26JUL2101-T75.99 | $1000 | 36% | $+2.53 | $-4.18 | 3 | $-8.44 |
| KXAAAGASD-26JUL23-4.140 | $183 | 18% | $+3.22 | $-1.79 | 7 | $-8.98 |
| KXEARNINGSMENTIONINTC-26JUL23-MOBI | $67 | 44% | $+10.81 | $-13.53 | 14 | $-9.39 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXTRUMPPHOTO-26JUL26-4 | $34 | 17% | $+10.09 | $-10.69 | 16 | $-13.78 |
| KXAAAGASD-26JUL23-4.130 | $183 | 42% | $+11.29 | $-6.11 | 5 | $-13.98 |
| KXTEMPNYCH-26JUL2101-T73.99 | $1000 | 41% | $+2.59 | $-24.00 | 5 | $-14.25 |
| KXEARNINGSMENTIONLMT-26JUL23-VENU | $67 | 33% | $+5.25 | $-10.30 | 10 | $-15.06 |
| KXWCATTEND-26JUL20-TRAV | $63 | 17% | $+42.30 | $-68.91 | 80 | $-17.58 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXEARNINGSMENTIONLMT-26JUL23-ORIO | $67 | 53% | $+8.41 | $-20.07 | 10 | $-24.68 |
| KXEARNINGSMENTIONLMT-26JUL23-VENT | $67 | 59% | $+9.44 | $-5.00 | 10 | $-25.30 |
| KXTEMPDCH-26JUL2201-T73.99 | $1000 | 93% | $+6.47 | $-3.03 | 6 | $-26.04 |
| KXEARNINGSMENTIONAAL-26JUL23-CENT | $67 | 48% | $+7.57 | $-20.24 | 26 | $-28.78 |
| KXWNBAMENTION-26JUL19CONNPHX-TECH | $51 | 67% | $+7.32 | $-29.90 | 10 | $-31.43 |
| KXMLBMENTION-26JUL21LADPHI-ROB | $193 | 44% | $+20.00 | $-1.10 | 9 | $-33.14 |
| KXTRUMPPHOTO-26JUL26-5 | $34 | 35% | $+21.36 | $-5.01 | 67 | $-36.41 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXTEMPNYCH-26JUL2201-T71.99 | $1000 | 79% | $+5.52 | $-13.00 | 4 | $-47.13 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXTEMPLAXH-26JUL2101-T70.99 | $1000 | 80% | $+6.52 | $-9.14 | 12 | $-51.83 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXEARNINGSMENTIONLMT-26JUL23-PERU | $67 | 39% | $+6.21 | $-41.06 | 15 | $-56.10 |
| KXTEMPAUSH-26JUL2101-T78.99 | $1000 | 58% | $+5.47 | $-60.20 | 11 | $-57.58 |
| KXWNBAMENTION-26JUL16NYDAL-TECH | $51 | 40% | $+9.79 | $-0.00 | 7 | $-63.06 |
| KXTEMPAUSH-26JUL2201-T78.99 | $1000 | 63% | $+3.21 | $-19.39 | 9 | $-65.38 |
| KXMLBMENTION-26JUL21LADPHI-MVP | $193 | 71% | $+32.20 | $-11.11 | 24 | $-72.67 |
| KXTRUMPPHOTO-26JUL26-6 | $34 | 52% | $+31.56 | $-33.40 | 32 | $-72.99 |
| KXEARNINGSMENTIONAAL-26JUL23-WORL | $67 | 43% | $+6.89 | $-25.78 | 19 | $-80.56 |
| KXEARNINGSMENTIONINTC-26JUL23-ARIZ | $67 | 56% | $+13.71 | $-40.30 | 33 | $-91.70 |
| KXTEMPLAXH-26JUL2201-T73.99 | $1000 | 80% | $+7.79 | $-55.21 | 11 | $-102.27 |
| KXTEMPDCH-26JUL2201-T72.99 | $1000 | 65% | $+4.48 | $-0.63 | 9 | $-116.19 |
| KXWNBAMENTION-26JUL16NYDAL-AIRB | $51 | 38% | $+9.15 | $-1.06 | 3 | $-118.32 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXTEMPCHIH-26JUL2201-T67.99 | $1000 | 86% | $+5.76 | $-57.55 | 8 | $-173.96 |
| KXTEMPNYCH-26JUL2101-T72.99 | $1000 | 51% | $+4.24 | $-71.00 | 5 | $-200.62 |
| KXTEMPCHIH-26JUL2201-T68.99 | $1000 | 85% | $+5.94 | $-137.29 | 14 | $-214.18 |
| KXTEMPAUSH-26JUL2101-T77.99 | $1000 | 70% | $+4.40 | $-53.20 | 9 | $-222.91 |
| KXCLAUDE-OPUS-26JUL27 | $87 | 66% | $+20.82 | $-203.14 | 62 | $-241.83 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+91.38 | $-75.01 | 140 | $-274.45 |
| KXTEMPNYCH-26JUL2201-T72.99 | $1000 | 84% | $+3.88 | $-60.00 | 4 | $-282.59 |
| KXTEMPLAXH-26JUL2101-T71.99 | $1000 | 66% | $+5.95 | $-95.00 | 12 | $-286.44 |
| KXMLBMENTION-26JUL21LADPHI-PITC | $193 | 61% | $+27.64 | $-13.01 | 25 | $-289.46 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXAAAGASD-26JUL23-4.095 | $183 | 63% | $+27.20 | $-118.24 | 56 | $-323.73 |
| KXWCATTEND-26JUL20-LEB | $63 | 45% | $+52.76 | $-402.84 | 330 | $-324.42 |
| KXTEMPAUSH-26JUL2013-T88.99 | $1000 | 61% | $+13.03 | $-151.72 | 20 | $-341.28 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXTEMPAUSH-26JUL2201-T79.99 | $1000 | 67% | $+3.12 | $-265.00 | 6 | $-367.68 |
| KXWNBAMENTION-26JUL16NYDAL-BUZZ | $51 | 36% | $+7.57 | $-1.00 | 8 | $-373.20 |
| KXTEMPDCH-26JUL2101-T77.99 | $1000 | 81% | $+5.06 | $-197.71 | 18 | $-507.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-ZEN | $63 | 33% | $+82.27 | $-392.72 | 160 | $-579.27 |
| KXWCATTEND-26JUL20-PAR | $63 | 31% | $+78.27 | $-258.19 | 157 | $-606.33 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+104.42 | $-432.73 | 118 | $-706.66 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |
| KXWCATTEND-26JUL20-RYA | $63 | 30% | $+76.44 | $-464.85 | 215 | $-841.00 |
| KXTEMPLAXH-26JUL2013-T77.99 | $1000 | 66% | $+16.55 | $-375.02 | 40 | $-981.99 |
| KXCLAUDE-OPUS-26JUL24 | $87 | 58% | $+18.00 | $-649.39 | 73 | $-1132.47 |
| KXWCATTEND-26JUL20-RIH | $63 | 39% | $+95.75 | $-845.98 | 172 | $-1141.35 |
| KXWCATTEND-26JUL20-KEN | $63 | 38% | $+94.63 | $-835.20 | 167 | $-1494.86 |
| KXWCATTEND-26JUL20-TOMH | $63 | 34% | $+85.34 | $-752.75 | 265 | $-1663.14 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+122.79 | $-1816.58 | 452 | $-2485.30 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+95.17 | $-2197.80 | 533 | $-2837.45 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+119.19 | $-2293.38 | 415 | $-3029.01 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+105.78 | $-2282.77 | 377 | $-3316.08 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 60/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 25 | 60 | 57 (win-rate CI 86%-98%) | $+25.19 | +4.63% |
| kalshi taker | 60 | - | 85 | 82 | $+28.88 | +3.67% |
| poly taker (zero-fee) | 47 | - | 164 | 143 | $-61.91 | -4.15% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.