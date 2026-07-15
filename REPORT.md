# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-15 04:49 UTC — **day 3.3 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-15 04:49 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 8 |
| current job age | 0.5h of 5.7h max |
| markets quoting / retired | 15 / 17 |
| favorites open (maker/taker/poly) | 56 / 56 / 36 |
| API requests last job | 2974 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-790.75/day vs GO bar $5.00/day; earn/pay -0.55 vs 1.5; fills 550/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 32 |
| est. rewards accrued | $+791.40 |
| spread P&L (cash + mark) | $-1718.43 |
| adverse selection (markout) | $-1594.34 |
| maker fees | $-85.00 |
| **decision number** | **$-2606.37** |
| decision at 0.25x rewards (share-optimism haircut) | $-3199.92 |
| decision at 0.10x rewards | $-3318.63 |
| fills / snapshots (counted) | 550 / 123840 (111654) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 30% | $+31.49 | $-0.00 | 3 | $+31.50 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-KYL | $63 | 45% | $+47.27 | $-16.74 | 19 | $+26.92 |
| KXWCATTEND-26JUL20-VIC | $63 | 32% | $+33.34 | $-0.00 | 8 | $+26.02 |
| KXWCATTEND-26JUL20-RIH | $63 | 23% | $+24.38 | $-0.00 | 2 | $+24.37 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 15% | $+16.08 | $-5.00 | 1 | $+9.71 |
| KXWCATTEND-26JUL20-PAR | $63 | 36% | $+37.66 | $-0.35 | 11 | $+8.55 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCATTEND-26JUL20-LEO | $63 | 43% | $+44.87 | $-47.36 | 32 | $-0.75 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-DRA | $63 | 33% | $+34.15 | $-22.28 | 9 | $-11.57 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 39% | $+40.86 | $-43.00 | 7 | $-57.71 |
| KXWCATTEND-26JUL20-ZEN | $63 | 45% | $+47.34 | $-21.00 | 24 | $-67.02 |
| KXWCATTEND-26JUL20-TRA | $63 | 56% | $+58.74 | $-48.00 | 19 | $-90.76 |
| KXWCATTEND-26JUL20-RYA | $63 | 39% | $+40.49 | $-20.23 | 16 | $-132.64 |
| KXWCATTEND-26JUL20-TIM | $63 | 40% | $+41.98 | $-22.31 | 29 | $-138.31 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXRAIN-26JUL15-MIA | $87 | 91% | $+1.66 | $-106.00 | 4 | $-217.55 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 45% | $+46.79 | $-180.19 | 43 | $-294.07 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 14/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 56 | 8 | 14 | 13 (win-rate CI 69%-99%) | $+3.48 | +2.75% |
| kalshi taker | 56 | — | 22 | 21 | $+5.53 | +2.72% |
| poly taker (zero-fee) | 36 | — | 30 | 29 | $+14.24 | +5.17% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.