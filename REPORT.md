# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-18 17:08 UTC — **day 6.8 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-18 17:08 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 15 |
| current job age | 1.5h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 60 / 60 / 53 |
| API requests last job | 8678 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-780.40/day vs GO bar $5.00/day; earn/pay -0.56 vs 1.5; fills 1134/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1351.44 |
| spread P&L (cash + mark) | $-3248.20 |
| adverse selection (markout) | $-3186.14 |
| maker fees | $-231.19 |
| **decision number** | **$-5314.09** |
| decision at 0.25x rewards (share-optimism haircut) | $-6327.67 |
| decision at 0.10x rewards | $-6530.39 |
| fills / snapshots (counted) | 1134 / 233730 (221544) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-RIH | $63 | 35% | $+73.24 | $-39.71 | 27 | $+56.75 |
| KXWCATTEND-26JUL20-VIC | $63 | 33% | $+68.92 | $-76.06 | 23 | $+53.58 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 15% | $+31.82 | $-5.00 | 3 | $+20.03 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCATTEND-26JUL20-LEB | $63 | 47% | $+36.73 | $-52.93 | 56 | $-20.77 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCATTEND-26JUL20-ZEN | $63 | 32% | $+66.89 | $-29.00 | 29 | $-50.66 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-PAR | $63 | 28% | $+59.14 | $-29.02 | 26 | $-141.92 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-LEO | $63 | 44% | $+92.68 | $-132.67 | 64 | $-153.39 |
| KXWCATTEND-26JUL20-TOMH | $63 | 27% | $+57.53 | $-94.66 | 54 | $-155.24 |
| KXWCATTEND-26JUL20-TRA | $63 | 47% | $+98.82 | $-85.51 | 56 | $-175.33 |
| KXWCATTEND-26JUL20-KEN | $63 | 36% | $+76.67 | $-77.64 | 49 | $-190.65 |
| KXWCATTEND-26JUL20-KYL | $63 | 42% | $+89.63 | $-127.01 | 42 | $-244.59 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+80.56 | $-50.37 | 104 | $-282.46 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-DRA | $63 | 37% | $+77.60 | $-229.05 | 88 | $-496.36 |
| KXWCATTEND-26JUL20-KIM | $63 | 50% | $+105.09 | $-340.04 | 91 | $-505.71 |
| KXWCATTEND-26JUL20-RYA | $63 | 29% | $+61.31 | $-268.10 | 55 | $-534.29 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 45/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 21 | 45 | 42 (win-rate CI 82%-98%) | $+10.11 | +2.47% |
| kalshi taker | 60 | — | 66 | 63 | $+14.42 | +2.36% |
| poly taker (zero-fee) | 53 | — | 65 | 61 | $+15.09 | +2.54% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.