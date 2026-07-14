# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 07:49 UTC — **day 2.4 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 07:49 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 6 |
| current job age | 3.5h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 29 |
| API requests last job | 19673 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-910.20/day vs GO bar $5.00/day; earn/pay -0.47 vs 1.5; fills 511/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+706.54 |
| spread P&L (cash + mark) | $-1414.14 |
| adverse selection (markout) | $-1419.78 |
| maker fees | $-76.46 |
| **decision number** | **$-2203.84** |
| decision at 0.25x rewards (share-optimism haircut) | $-2733.75 |
| decision at 0.10x rewards | $-2839.73 |
| fills / snapshots (counted) | 511 / 101355 (90577) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 34% | $+27.98 | $-0.00 | 3 | $+27.99 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+31.24 | $-1.88 | 11 | $+26.44 |
| KXWCATTEND-26JUL20-RIH | $63 | 28% | $+23.69 | $-0.00 | 2 | $+23.68 |
| KXWCATTEND-26JUL20-VIC | $63 | 32% | $+26.40 | $-0.00 | 8 | $+22.16 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-KYL | $63 | 45% | $+37.58 | $-0.61 | 18 | $+15.93 |
| KXWCATTEND-26JUL20-TRAV | $63 | 19% | $+15.98 | $-5.00 | 1 | $+9.61 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-PAR | $63 | 41% | $+33.78 | $-0.35 | 11 | $+4.67 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-LEO | $63 | 50% | $+41.21 | $-47.36 | 31 | $-4.44 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-DRA | $63 | 39% | $+32.19 | $-22.28 | 9 | $-13.54 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCATTEND-26JUL20-KEN | $63 | 36% | $+30.09 | $-43.00 | 7 | $-51.57 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-ZEN | $63 | 47% | $+39.42 | $-1.00 | 14 | $-61.75 |
| KXWCATTEND-26JUL20-TRA | $63 | 61% | $+50.88 | $-48.00 | 16 | $-101.81 |
| KXWCATTEND-26JUL20-RYA | $63 | 43% | $+35.99 | $-8.23 | 15 | $-115.23 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-KIM | $63 | 43% | $+35.82 | $-180.19 | 42 | $-301.05 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-303.33 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 10/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 10 | 10 (win-rate CI 72%-100%) | $+8.95 | +9.84% |
| kalshi taker | 60 | — | 17 | 17 | $+11.15 | +7.06% |
| poly taker (zero-fee) | 29 | — | 20 | 19 | $+5.97 | +3.25% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.