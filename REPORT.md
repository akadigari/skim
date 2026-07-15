# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-15 16:10 UTC — **day 3.8 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-15 16:10 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 9 |
| current job age | 0.5h of 5.7h max |
| markets quoting / retired | 15 / 17 |
| favorites open (maker/taker/poly) | 57 / 57 / 40 |
| API requests last job | 2864 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-686.38/day vs GO bar $5.00/day; earn/pay -0.50 vs 1.5; fills 562/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 32 |
| est. rewards accrued | $+853.46 |
| spread P&L (cash + mark) | $-1713.77 |
| adverse selection (markout) | $-1637.28 |
| maker fees | $-89.47 |
| **decision number** | **$-2587.05** |
| decision at 0.25x rewards (share-optimism haircut) | $-3227.15 |
| decision at 0.10x rewards | $-3355.17 |
| fills / snapshots (counted) | 562 / 139155 (126969) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 28% | $+33.10 | $-0.00 | 3 | $+33.11 |
| KXWCATTEND-26JUL20-KYL | $63 | 43% | $+51.94 | $-16.74 | 19 | $+31.60 |
| KXWCATTEND-26JUL20-VIC | $63 | 31% | $+36.81 | $-0.00 | 8 | $+29.49 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-RIH | $63 | 20% | $+24.38 | $-0.00 | 2 | $+24.37 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 13% | $+16.08 | $-5.00 | 1 | $+9.71 |
| KXWCATTEND-26JUL20-PAR | $63 | 32% | $+37.86 | $-0.35 | 11 | $+8.75 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-LEO | $63 | 39% | $+46.71 | $-47.36 | 32 | $+1.10 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-DRA | $63 | 30% | $+35.84 | $-22.28 | 9 | $-9.88 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 37% | $+44.03 | $-43.00 | 7 | $-54.54 |
| KXWCATTEND-26JUL20-ZEN | $63 | 41% | $+49.66 | $-21.00 | 24 | $-64.70 |
| KXWCATTEND-26JUL20-TRA | $63 | 54% | $+65.21 | $-48.00 | 19 | $-84.29 |
| KXWCATTEND-26JUL20-TIM | $63 | 44% | $+52.78 | $-26.25 | 34 | $-88.69 |
| KXWCATTEND-26JUL20-RYA | $63 | 35% | $+41.49 | $-20.23 | 19 | $-123.56 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 47% | $+56.53 | $-180.19 | 43 | $-284.84 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+16.74 | $-145.00 | 8 | $-291.63 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 14/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 57 | 9 | 14 | 13 (win-rate CI 69%-99%) | $+3.48 | +2.75% |
| kalshi taker | 57 | — | 23 | 22 | $+5.80 | +2.72% |
| poly taker (zero-fee) | 40 | — | 32 | 31 | $+16.30 | +5.55% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.