# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-16 07:59 UTC — **day 4.4 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-16 07:59 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 10 |
| current job age | 3.5h of 5.7h max |
| markets quoting / retired | 15 / 17 |
| favorites open (maker/taker/poly) | 59 / 59 / 36 |
| API requests last job | 19615 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-894.81/day vs GO bar $5.00/day; earn/pay -0.53 vs 1.5; fills 708/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+988.15 |
| spread P&L (cash + mark) | $-2363.96 |
| adverse selection (markout) | $-2461.30 |
| maker fees | $-125.00 |
| **decision number** | **$-3962.10** |
| decision at 0.25x rewards (share-optimism haircut) | $-4703.21 |
| decision at 0.10x rewards | $-4851.43 |
| fills / snapshots (counted) | 708 / 162585 (150399) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCATTEND-26JUL20-KYL | $63 | 44% | $+63.28 | $-16.74 | 19 | $+77.36 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-VIC | $63 | 31% | $+44.86 | $-56.05 | 15 | $+32.56 |
| KXWCATTEND-26JUL20-RIH | $63 | 22% | $+31.31 | $-0.20 | 3 | $+30.91 |
| KXWCATTEND-26JUL20-PAR | $63 | 32% | $+45.77 | $-19.02 | 25 | $+28.83 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TOMH | $63 | 26% | $+37.51 | $-0.00 | 19 | $+27.37 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-LEB | $63 | 57% | $+5.18 | $-0.00 | 0 | $+5.18 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-TRAV | $63 | 14% | $+20.00 | $-5.00 | 2 | $-16.37 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-ZEN | $63 | 41% | $+57.77 | $-21.00 | 25 | $-56.92 |
| KXWCATTEND-26JUL20-KEN | $63 | 36% | $+51.53 | $-45.00 | 8 | $-75.03 |
| KXWCATTEND-26JUL20-TRA | $63 | 51% | $+72.98 | $-48.00 | 24 | $-91.20 |
| KXWCATTEND-26JUL20-TIM | $63 | 42% | $+59.63 | $-31.61 | 50 | $-105.21 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-LEO | $63 | 38% | $+54.55 | $-70.36 | 38 | $-153.77 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 50% | $+71.06 | $-186.69 | 48 | $-288.26 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-DRA | $63 | 35% | $+50.50 | $-157.76 | 27 | $-311.43 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-RYA | $63 | 33% | $+47.42 | $-254.48 | 38 | $-559.57 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-783.50 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 15/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 59 | 9 | 15 | 14 (win-rate CI 70%-99%) | $+4.36 | +3.22% |
| kalshi taker | 59 | — | 24 | 23 | $+6.54 | +2.94% |
| poly taker (zero-fee) | 36 | — | 46 | 42 | $-1.46 | -0.35% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.