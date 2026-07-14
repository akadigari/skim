# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 21:20 UTC — **day 3.0 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 21:20 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 7 |
| current job age | 5.7h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 40 |
| API requests last job | 31680 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-765.61/day vs GO bar $5.00/day; earn/pay -0.45 vs 1.5; fills 546/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+785.09 |
| spread P&L (cash + mark) | $-1498.77 |
| adverse selection (markout) | $-1488.34 |
| maker fees | $-82.79 |
| **decision number** | **$-2284.81** |
| decision at 0.25x rewards (share-optimism haircut) | $-2873.62 |
| decision at 0.10x rewards | $-2991.39 |
| fills / snapshots (counted) | 546 / 122475 (110289) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 30% | $+31.34 | $-0.00 | 3 | $+31.34 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-KYL | $63 | 45% | $+46.86 | $-16.74 | 19 | $+26.52 |
| KXWCATTEND-26JUL20-VIC | $63 | 32% | $+33.00 | $-0.00 | 8 | $+25.68 |
| KXWCATTEND-26JUL20-RIH | $63 | 24% | $+24.38 | $-0.00 | 2 | $+24.37 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 16% | $+16.08 | $-5.00 | 1 | $+9.71 |
| KXWCATTEND-26JUL20-PAR | $63 | 36% | $+37.61 | $-0.35 | 11 | $+8.50 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCATTEND-26JUL20-LEO | $63 | 43% | $+44.72 | $-47.36 | 32 | $-0.89 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-DRA | $63 | 33% | $+34.00 | $-22.28 | 9 | $-11.73 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 39% | $+40.55 | $-43.00 | 7 | $-58.02 |
| KXWCATTEND-26JUL20-ZEN | $63 | 45% | $+47.11 | $-21.00 | 24 | $-67.24 |
| KXWCATTEND-26JUL20-TIM | $63 | 39% | $+40.85 | $-22.31 | 29 | $-70.33 |
| KXWCATTEND-26JUL20-TRA | $63 | 56% | $+58.09 | $-48.00 | 19 | $-94.48 |
| KXWCATTEND-26JUL20-RYA | $63 | 39% | $+40.43 | $-20.23 | 16 | $-132.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 44% | $+45.76 | $-180.19 | 43 | $-290.61 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-303.33 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 11/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 11 | 10 (win-rate CI 62%-98%) | $+0.23 | +0.23% |
| kalshi taker | 60 | — | 18 | 17 | $+2.27 | +1.36% |
| poly taker (zero-fee) | 40 | — | 25 | 24 | $+9.44 | +4.09% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.