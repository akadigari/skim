# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-21 20:29 UTC, **day 9.9 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-21 20:29 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 21 |
| current job age | 4.5h of 5.7h max |
| markets quoting / retired | 15 / 55 |
| favorites open (maker/taker/poly) | 60 / 60 / 43 |
| API requests last job | 26058 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-2502.49/day vs GO bar $5.00/day; earn/pay -0.44 vs 1.5; fills 4515/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 70 |
| est. rewards accrued | $+2087.60 |
| spread P&L (cash + mark) | $-9667.58 |
| adverse selection (markout) | $-16067.02 |
| maker fees | $-1250.05 |
| **decision number** | **$-24897.05** |
| decision at 0.25x rewards (share-optimism haircut) | $-26462.75 |
| decision at 0.10x rewards | $-26775.89 |
| fills / snapshots (counted) | 4515 / 333735 (304911) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXDXYDUD-26JUL20-T100.7560 | $218 | 47% | $+48.27 | $-22.59 | 19 | $+105.48 |
| KXWNBAMENTION-26JUL16NYDAL-CAIT | $51 | 45% | $+10.78 | $-2.15 | 7 | $+94.02 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWNBAMENTION-26JUL16NYDAL-OVER | $51 | 64% | $+15.51 | $-0.45 | 12 | $+58.71 |
| KXAAAGASD-26JUL22-4.070 | $193 | 68% | $+24.75 | $-22.35 | 23 | $+27.93 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXMLBMENTION-26JUL21LADPHI-WALK | $193 | 72% | $+26.30 | $-0.00 | 4 | $+26.30 |
| KXAAAGASD-26JUL22-4.080 | $193 | 61% | $+22.30 | $-0.01 | 6 | $+21.13 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXTEMPCHIH-26JUL2101-T75.99 | $1000 | 80% | $+5.02 | $-19.00 | 4 | $+20.77 |
| KXMLBMENTION-26JUL21LADPHI-PITC | $193 | 65% | $+23.57 | $-3.00 | 19 | $+19.44 |
| KXMLBMENTION-26JUL21LADPHI-EXTR | $193 | 53% | $+18.64 | $-0.04 | 2 | $+18.51 |
| KXMLBMENTION-26JUL21LADPHI-WILD | $193 | 50% | $+15.87 | $-0.00 | 13 | $+16.02 |
| KXMLBMENTION-26JUL21LADPHI-ROB | $193 | 49% | $+17.74 | $-1.10 | 6 | $+14.66 |
| KXWNBAMENTION-26JUL16NYDAL-TRAD | $51 | 51% | $+12.26 | $-0.00 | 0 | $+12.26 |
| KXMLBMENTION-26JUL21LADPHI-PINC | $193 | 53% | $+19.12 | $-5.13 | 15 | $+11.97 |
| KXTEMPCHIH-26JUL2101-T74.99 | $1000 | 85% | $+5.34 | $-1.58 | 3 | $+11.80 |
| KXWNBAMENTION-26JUL19CHIATL-TAUR | $51 | 90% | $+10.91 | $-0.00 | 0 | $+10.91 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWNBAMENTION-26JUL16NYDAL-ANKL | $51 | 47% | $+11.39 | $-0.24 | 3 | $+5.32 |
| KXWCATTEND-26JUL20-VIC | $63 | 35% | $+86.21 | $-136.03 | 101 | $+5.25 |
| KXMLBMENTION-26JUL21LADPHI-MVP | $193 | 74% | $+26.86 | $-11.11 | 18 | $+1.80 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXTRUMPPHOTO-26JUL26-7 | $34 | 19% | $+4.46 | $-0.48 | 13 | $-3.27 |
| KXWNBAMENTION-26JUL16NYDAL-TRAV | $51 | 48% | $+11.60 | $-9.00 | 2 | $-4.50 |
| KXTRUMPPHOTO-26JUL26-5 | $34 | 40% | $+11.99 | $-4.51 | 62 | $-7.48 |
| KXTEMPDCH-26JUL2101-T75.99 | $1000 | 36% | $+2.53 | $-4.18 | 3 | $-8.44 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXTEMPNYCH-26JUL2101-T73.99 | $1000 | 41% | $+2.59 | $-24.00 | 5 | $-14.25 |
| KXWCATTEND-26JUL20-TRAV | $63 | 17% | $+42.30 | $-68.91 | 80 | $-17.58 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXTRUMPPHOTO-26JUL26-4 | $34 | 15% | $+4.46 | $-10.69 | 16 | $-22.58 |
| KXWNBAMENTION-26JUL19CONNPHX-TECH | $51 | 67% | $+7.32 | $-29.90 | 10 | $-31.43 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXTEMPLAXH-26JUL2101-T70.99 | $1000 | 80% | $+6.52 | $-9.14 | 12 | $-51.83 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXTEMPAUSH-26JUL2101-T78.99 | $1000 | 58% | $+5.47 | $-60.20 | 11 | $-57.58 |
| KXWNBAMENTION-26JUL16NYDAL-TECH | $51 | 40% | $+9.79 | $-0.00 | 7 | $-63.06 |
| KXTRUMPPHOTO-26JUL26-6 | $34 | 45% | $+13.56 | $-33.40 | 32 | $-91.06 |
| KXWNBAMENTION-26JUL16NYDAL-AIRB | $51 | 38% | $+9.15 | $-1.06 | 3 | $-118.32 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL21LADPHI-BUNT | $193 | 53% | $+19.17 | $-41.95 | 24 | $-181.67 |
| KXTEMPNYCH-26JUL2101-T72.99 | $1000 | 51% | $+4.24 | $-71.00 | 5 | $-200.62 |
| KXTEMPAUSH-26JUL2101-T77.99 | $1000 | 70% | $+4.40 | $-53.20 | 9 | $-222.91 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+91.38 | $-75.01 | 140 | $-274.45 |
| KXTEMPLAXH-26JUL2101-T71.99 | $1000 | 66% | $+5.95 | $-95.00 | 12 | $-286.44 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-LEB | $63 | 45% | $+52.76 | $-402.84 | 330 | $-324.42 |
| KXTEMPAUSH-26JUL2013-T88.99 | $1000 | 61% | $+13.03 | $-151.72 | 20 | $-341.28 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWNBAMENTION-26JUL16NYDAL-BUZZ | $51 | 36% | $+7.57 | $-1.00 | 8 | $-373.20 |
| KXTEMPDCH-26JUL2101-T77.99 | $1000 | 81% | $+5.06 | $-197.71 | 18 | $-507.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-ZEN | $63 | 33% | $+82.27 | $-392.72 | 160 | $-579.27 |
| KXWCATTEND-26JUL20-PAR | $63 | 31% | $+78.27 | $-258.19 | 157 | $-606.33 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+104.42 | $-432.73 | 118 | $-706.66 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |
| KXWCATTEND-26JUL20-RYA | $63 | 30% | $+76.44 | $-464.85 | 215 | $-841.00 |
| KXTEMPLAXH-26JUL2013-T77.99 | $1000 | 66% | $+16.55 | $-375.02 | 40 | $-981.99 |
| KXWCATTEND-26JUL20-RIH | $63 | 39% | $+95.75 | $-845.98 | 172 | $-1141.35 |
| KXWCATTEND-26JUL20-KEN | $63 | 38% | $+94.63 | $-835.20 | 167 | $-1494.86 |
| KXWCATTEND-26JUL20-TOMH | $63 | 34% | $+85.34 | $-752.75 | 265 | $-1663.14 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+122.79 | $-1816.58 | 452 | $-2485.30 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+95.17 | $-2197.80 | 533 | $-2837.45 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+119.19 | $-2293.38 | 415 | $-3029.01 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+105.78 | $-2282.77 | 377 | $-3316.08 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 59/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 24 | 59 | 56 (win-rate CI 86%-98%) | $+23.91 | +4.47% |
| kalshi taker | 60 | - | 83 | 80 | $+27.11 | +3.53% |
| poly taker (zero-fee) | 43 | - | 136 | 120 | $-35.90 | -2.90% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.