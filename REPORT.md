# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-16 05:28 UTC — **day 4.3 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-16 05:28 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 10 |
| current job age | 1.0h of 5.7h max |
| markets quoting / retired | 15 / 17 |
| favorites open (maker/taker/poly) | 59 / 59 / 36 |
| API requests last job | 5756 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-916.73/day vs GO bar $5.00/day; earn/pay -0.54 vs 1.5; fills 697/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+937.75 |
| spread P&L (cash + mark) | $-2319.30 |
| adverse selection (markout) | $-2458.57 |
| maker fees | $-123.38 |
| **decision number** | **$-3963.50** |
| decision at 0.25x rewards (share-optimism haircut) | $-4666.81 |
| decision at 0.10x rewards | $-4807.47 |
| fills / snapshots (counted) | 697 / 155820 (143634) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+58.23 | $-16.74 | 19 | $+72.31 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-RIH | $63 | 20% | $+26.76 | $-0.20 | 3 | $+26.34 |
| KXWCATTEND-26JUL20-VIC | $63 | 31% | $+41.97 | $-56.00 | 12 | $+25.38 |
| KXWCATTEND-26JUL20-TOMH | $63 | 26% | $+35.44 | $-0.00 | 19 | $+25.29 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-PAR | $63 | 30% | $+40.24 | $-18.35 | 25 | $+7.70 |
| KXWCATTEND-26JUL20-LEB | $63 | 62% | $+1.62 | $-0.00 | 0 | $+1.62 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-TRAV | $63 | 13% | $+17.24 | $-5.00 | 2 | $-19.13 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-ZEN | $63 | 39% | $+53.59 | $-21.00 | 25 | $-61.10 |
| KXWCATTEND-26JUL20-KEN | $63 | 35% | $+48.17 | $-43.00 | 7 | $-76.16 |
| KXWCATTEND-26JUL20-TRA | $63 | 52% | $+70.50 | $-48.00 | 24 | $-93.67 |
| KXWCATTEND-26JUL20-LEO | $63 | 38% | $+52.31 | $-70.36 | 38 | $-101.58 |
| KXWCATTEND-26JUL20-TIM | $63 | 42% | $+57.28 | $-31.61 | 50 | $-107.56 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+66.17 | $-186.69 | 48 | $-292.40 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-DRA | $63 | 35% | $+48.20 | $-157.76 | 24 | $-313.83 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-RYA | $63 | 33% | $+45.22 | $-254.48 | 34 | $-550.18 |
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