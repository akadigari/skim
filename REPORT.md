# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-16 18:51 UTC — **day 4.9 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-16 18:51 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 11 |
| current job age | 3.0h of 5.7h max |
| markets quoting / retired | 15 / 17 |
| favorites open (maker/taker/poly) | 60 / 60 / 45 |
| API requests last job | 16856 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-815.42/day vs GO bar $5.00/day; earn/pay -0.51 vs 1.5; fills 768/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1077.83 |
| spread P&L (cash + mark) | $-2413.40 |
| adverse selection (markout) | $-2505.37 |
| maker fees | $-138.80 |
| **decision number** | **$-3979.74** |
| decision at 0.25x rewards (share-optimism haircut) | $-4788.11 |
| decision at 0.10x rewards | $-4949.79 |
| fills / snapshots (counted) | 768 / 176595 (164409) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-KYL | $63 | 46% | $+72.45 | $-21.74 | 20 | $+61.67 |
| KXWCATTEND-26JUL20-VIC | $63 | 33% | $+51.05 | $-69.06 | 17 | $+46.93 |
| KXWCATTEND-26JUL20-RIH | $63 | 26% | $+40.65 | $-0.33 | 6 | $+39.23 |
| KXWCATTEND-26JUL20-TOMH | $63 | 26% | $+40.03 | $-0.00 | 25 | $+30.13 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 16% | $+25.15 | $-5.00 | 2 | $+14.78 |
| KXWCATTEND-26JUL20-LEB | $63 | 54% | $+12.26 | $-0.00 | 0 | $+12.26 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCATTEND-26JUL20-PAR | $63 | 34% | $+53.46 | $-29.02 | 26 | $-37.28 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCATTEND-26JUL20-ZEN | $63 | 40% | $+62.53 | $-21.00 | 25 | $-52.16 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 37% | $+58.39 | $-46.87 | 16 | $-74.76 |
| KXWCATTEND-26JUL20-TRA | $63 | 49% | $+76.24 | $-48.00 | 24 | $-110.18 |
| KXWCATTEND-26JUL20-TIM | $63 | 41% | $+64.39 | $-35.69 | 66 | $-114.34 |
| KXWCATTEND-26JUL20-LEO | $63 | 40% | $+61.77 | $-78.36 | 51 | $-146.06 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 51% | $+78.97 | $-188.69 | 51 | $-279.97 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-DRA | $63 | 35% | $+55.16 | $-157.76 | 34 | $-311.50 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-RYA | $63 | 32% | $+50.54 | $-254.48 | 38 | $-551.97 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-783.50 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 15/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 9 | 15 | 14 (win-rate CI 70%-99%) | $+4.36 | +3.22% |
| kalshi taker | 60 | — | 24 | 23 | $+6.54 | +2.94% |
| poly taker (zero-fee) | 45 | — | 49 | 45 | $+0.94 | +0.21% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.