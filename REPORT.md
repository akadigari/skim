# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-18 05:47 UTC — **day 6.3 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-18 05:47 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 14 |
| current job age | 1.5h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 52 / 52 / 46 |
| API requests last job | 8740 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-783.35/day vs GO bar $5.00/day; earn/pay -0.55 vs 1.5; fills 1053/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1256.22 |
| spread P&L (cash + mark) | $-3014.47 |
| adverse selection (markout) | $-2993.90 |
| maker fees | $-211.81 |
| **decision number** | **$-4963.94** |
| decision at 0.25x rewards (share-optimism haircut) | $-5906.11 |
| decision at 0.10x rewards | $-6094.55 |
| fills / snapshots (counted) | 1053 / 218445 (206259) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-VIC | $63 | 32% | $+63.37 | $-76.06 | 23 | $+51.35 |
| KXWCATTEND-26JUL20-RIH | $63 | 32% | $+62.63 | $-39.33 | 22 | $+37.12 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TRAV | $63 | 15% | $+30.04 | $-5.00 | 3 | $+18.25 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCATTEND-26JUL20-LEB | $63 | 43% | $+27.47 | $-49.93 | 46 | $-22.25 |
| KXWCATTEND-26JUL20-ZEN | $63 | 33% | $+65.35 | $-21.00 | 25 | $-33.56 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-PAR | $63 | 29% | $+56.62 | $-29.02 | 26 | $-65.64 |
| KXWCATTEND-26JUL20-KYL | $63 | 42% | $+82.34 | $-73.74 | 30 | $-68.50 |
| KXWCATTEND-26JUL20-TRA | $63 | 46% | $+90.38 | $-56.19 | 49 | $-110.20 |
| KXWCATTEND-26JUL20-TOMH | $63 | 24% | $+47.99 | $-66.66 | 50 | $-111.41 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+83.42 | $-113.67 | 62 | $-140.06 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-KEN | $63 | 36% | $+71.38 | $-77.41 | 47 | $-195.73 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-TIM | $63 | 40% | $+79.33 | $-50.37 | 98 | $-284.42 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-KIM | $63 | 48% | $+94.85 | $-295.04 | 78 | $-460.34 |
| KXWCATTEND-26JUL20-DRA | $63 | 35% | $+69.57 | $-222.99 | 74 | $-526.25 |
| KXWCATTEND-26JUL20-RYA | $63 | 29% | $+56.66 | $-268.10 | 53 | $-559.22 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 45/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 52 | 21 | 45 | 42 (win-rate CI 82%-98%) | $+10.11 | +2.47% |
| kalshi taker | 52 | — | 66 | 63 | $+14.42 | +2.36% |
| poly taker (zero-fee) | 46 | — | 64 | 60 | $+13.89 | +2.37% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.