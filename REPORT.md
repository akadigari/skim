# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-20 21:18 UTC, **day 9.0 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-20 21:18 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 19 |
| current job age | 5.0h of 5.7h max |
| markets quoting / retired | 15 / 35 |
| favorites open (maker/taker/poly) | 60 / 60 / 45 |
| API requests last job | 29021 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-2519.94/day vs GO bar $5.00/day; earn/pay -0.36 vs 1.5; fills 4231/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 50 |
| est. rewards accrued | $+1803.39 |
| spread P&L (cash + mark) | $-7845.20 |
| adverse selection (markout) | $-15393.44 |
| maker fees | $-1202.34 |
| **decision number** | **$-22637.59** |
| decision at 0.25x rewards (share-optimism haircut) | $-23990.13 |
| decision at 0.10x rewards | $-24260.64 |
| fills / snapshots (counted) | 4231 / 304485 (288618) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXDXYDUD-26JUL20-T100.7560 | $218 | 47% | $+45.74 | $-6.59 | 15 | $+114.32 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWNBAMENTION-26JUL16NYDAL-OVER | $51 | 64% | $+14.55 | $-0.45 | 12 | $+13.05 |
| KXWNBAMENTION-26JUL16NYDAL-TRAD | $51 | 51% | $+11.67 | $-0.00 | 0 | $+11.67 |
| KXTRUMPPHOTO-26JUL26-6 | $34 | 41% | $+6.11 | $-0.40 | 10 | $+11.30 |
| KXWNBAMENTION-26JUL19CHIATL-TAUR | $51 | 90% | $+10.91 | $-0.00 | 0 | $+10.91 |
| KXWNBAMENTION-26JUL16NYDAL-ANKL | $51 | 47% | $+10.70 | $-0.24 | 3 | $+10.15 |
| KXWNBAMENTION-26JUL16NYDAL-TECH | $51 | 42% | $+9.52 | $-0.00 | 5 | $+9.58 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWNBAMENTION-26JUL16NYDAL-AIRB | $51 | 38% | $+8.70 | $-1.06 | 3 | $+7.75 |
| KXWCATTEND-26JUL20-VIC | $63 | 35% | $+86.21 | $-136.03 | 101 | $+5.25 |
| KXWNBAMENTION-26JUL16NYDAL-BUZZ | $51 | 36% | $+7.35 | $-1.00 | 8 | $+5.13 |
| KXTRUMPPHOTO-26JUL26-7 | $34 | 25% | $+3.79 | $-0.48 | 10 | $+3.27 |
| KXWNBAMENTION-26JUL16NYDAL-CAIT | $51 | 44% | $+10.10 | $-2.15 | 6 | $+2.32 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXTRUMPPHOTO-26JUL26-5 | $34 | 31% | $+4.72 | $-1.63 | 23 | $-0.94 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWNBAMENTION-26JUL16NYDAL-TRAV | $51 | 48% | $+11.00 | $-7.00 | 1 | $-3.58 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-TRAV | $63 | 17% | $+42.30 | $-68.91 | 80 | $-17.58 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXTRUMPPHOTO-26JUL26-4 | $34 | 27% | $+4.11 | $-10.69 | 16 | $-20.56 |
| KXWNBAMENTION-26JUL19CONNPHX-TECH | $51 | 67% | $+7.32 | $-29.90 | 10 | $-31.43 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXTEMPAUSH-26JUL2013-T88.99 | $1000 | 61% | $+13.03 | $-151.72 | 20 | $-217.70 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+91.38 | $-75.01 | 140 | $-274.45 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-LEB | $63 | 45% | $+52.76 | $-402.84 | 330 | $-324.42 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-ZEN | $63 | 33% | $+82.27 | $-392.72 | 160 | $-579.27 |
| KXWCATTEND-26JUL20-PAR | $63 | 31% | $+78.27 | $-258.19 | 157 | $-606.33 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+104.42 | $-432.73 | 118 | $-706.66 |
| KXTEMPLAXH-26JUL2013-T77.99 | $1000 | 66% | $+16.55 | $-375.02 | 40 | $-758.09 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |
| KXWCATTEND-26JUL20-RYA | $63 | 30% | $+76.44 | $-464.85 | 215 | $-841.00 |
| KXWCATTEND-26JUL20-RIH | $63 | 39% | $+95.75 | $-845.98 | 172 | $-1141.35 |
| KXWCATTEND-26JUL20-KEN | $63 | 38% | $+94.63 | $-835.20 | 167 | $-1494.86 |
| KXWCATTEND-26JUL20-TOMH | $63 | 34% | $+85.34 | $-752.75 | 265 | $-1663.14 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+122.79 | $-1816.58 | 452 | $-2485.30 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+95.17 | $-2197.80 | 533 | $-2837.45 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+119.19 | $-2293.38 | 415 | $-3029.01 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+105.78 | $-2282.77 | 377 | $-3316.08 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 54/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 23 | 54 | 51 (win-rate CI 85%-98%) | $+18.80 | +3.83% |
| kalshi taker | 60 | - | 77 | 74 | $+22.46 | +3.15% |
| poly taker (zero-fee) | 45 | - | 117 | 103 | $-34.20 | -3.21% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.