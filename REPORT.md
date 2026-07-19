# SKIM: Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-19 19:31 UTC, **day 7.9 of 14**. 100% sim: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-19 19:31 UTC (if this is > 7.5h old, the watchdog has already alerted Telegram) |
| jobs run (6h chain) | 17 |
| current job age | 3.5h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 58 / 58 / 56 |
| API requests last job | 20145 |
| crons (UTC) | campaign :19 of 1,7,13,19 (watchdog :49 of 3,9,15,21) |

## Experiment 1: MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND**, decision $-1601.40/day vs GO bar $5.00/day; earn/pay -0.50 vs 1.5; fills 2564/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1578.28 |
| spread P&L (cash + mark) | $-5819.64 |
| adverse selection (markout) | $-7753.38 |
| maker fees | $-670.60 |
| **decision number** | **$-12665.34** |
| decision at 0.25x rewards (share-optimism haircut) | $-13849.05 |
| decision at 0.10x rewards | $-14085.79 |
| fills / snapshots (counted) | 2564 / 269775 (257206) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-VIC | $63 | 35% | $+85.76 | $-108.40 | 64 | $+30.40 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 17% | $+40.84 | $-43.72 | 47 | $+1.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-RIH | $63 | 38% | $+94.65 | $-156.77 | 112 | $-159.32 |
| KXWCATTEND-26JUL20-PAR | $63 | 31% | $+75.94 | $-104.62 | 90 | $-201.90 |
| KXWCATTEND-26JUL20-ZEN | $63 | 32% | $+78.92 | $-109.27 | 89 | $-250.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+91.38 | $-75.01 | 140 | $-271.48 |
| KXWCATTEND-26JUL20-LEB | $63 | 45% | $+50.64 | $-301.76 | 221 | $-278.81 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+115.89 | $-291.67 | 155 | $-652.53 |
| KXWCATTEND-26JUL20-RYA | $63 | 30% | $+73.94 | $-351.53 | 135 | $-660.18 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+104.42 | $-432.73 | 118 | $-702.46 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+102.36 | $-356.76 | 167 | $-767.78 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |
| KXWCATTEND-26JUL20-TOMH | $63 | 33% | $+82.35 | $-557.12 | 151 | $-1065.83 |
| KXWCATTEND-26JUL20-KEN | $63 | 38% | $+93.26 | $-780.20 | 125 | $-1436.12 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+93.01 | $-1004.45 | 266 | $-1559.12 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+120.11 | $-1530.00 | 317 | $-2198.19 |

## Experiment 2: Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED**, 48/300 settled maker positions, no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 58 | 21 | 48 | 45 (win-rate CI 83%-98%) | $+13.75 | +3.16% |
| kalshi taker | 58 | - | 69 | 66 | $+17.31 | +2.71% |
| poly taker (zero-fee) | 56 | - | 86 | 80 | $+16.97 | +2.17% |

_If maker ROI < taker ROI, queue fills are adversely selected: the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026**, a GO here is only actionable before renewal risk.