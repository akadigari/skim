# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-17 21:21 UTC — **day 6.0 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-17 21:21 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 13 |
| current job age | 5.5h of 5.7h max |
| markets quoting / retired | 15 / 18 |
| favorites open (maker/taker/poly) | 60 / 60 / 50 |
| API requests last job | 30651 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-793.88/day vs GO bar $5.00/day; earn/pay -0.54 vs 1.5; fills 1031/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 33 |
| est. rewards accrued | $+1228.34 |
| spread P&L (cash + mark) | $-2897.52 |
| adverse selection (markout) | $-2882.45 |
| maker fees | $-199.81 |
| **decision number** | **$-4751.44** |
| decision at 0.25x rewards (share-optimism haircut) | $-5672.70 |
| decision at 0.10x rewards | $-5856.95 |
| fills / snapshots (counted) | 1031 / 213975 (201789) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-VIC | $63 | 32% | $+61.83 | $-76.06 | 23 | $+43.17 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 15% | $+29.60 | $-5.00 | 3 | $+21.81 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-RIH | $63 | 31% | $+59.79 | $-29.33 | 21 | $-5.48 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCATTEND-26JUL20-LEB | $63 | 42% | $+24.92 | $-49.93 | 45 | $-25.47 |
| KXWCATTEND-26JUL20-ZEN | $63 | 34% | $+65.35 | $-21.00 | 25 | $-33.56 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-PAR | $63 | 29% | $+56.62 | $-29.02 | 26 | $-65.64 |
| KXWCATTEND-26JUL20-KYL | $63 | 42% | $+79.92 | $-73.74 | 29 | $-70.02 |
| KXWCATTEND-26JUL20-TRA | $63 | 46% | $+87.84 | $-52.19 | 48 | $-92.93 |
| KXWCATTEND-26JUL20-TOMH | $63 | 23% | $+44.72 | $-66.11 | 48 | $-113.26 |
| KXWCATTEND-26JUL20-LEO | $63 | 42% | $+80.49 | $-102.67 | 59 | $-134.75 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-TIM | $63 | 41% | $+78.60 | $-50.37 | 98 | $-202.57 |
| KXWCATTEND-26JUL20-KEN | $63 | 36% | $+69.53 | $-77.41 | 47 | $-206.99 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCATTEND-26JUL20-KIM | $63 | 48% | $+92.03 | $-222.28 | 72 | $-317.58 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-341.45 |
| KXWCATTEND-26JUL20-DRA | $63 | 35% | $+66.66 | $-209.85 | 67 | $-504.65 |
| KXWCATTEND-26JUL20-RYA | $63 | 29% | $+55.63 | $-268.10 | 53 | $-550.44 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |
| KXRAIN-26JUL15-MIA | $87 | 74% | $+30.50 | $-487.50 | 44 | $-770.04 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 16/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 10 | 16 | 15 (win-rate CI 72%-99%) | $+5.54 | +3.84% |
| kalshi taker | 60 | — | 26 | 25 | $+8.69 | +3.62% |
| poly taker (zero-fee) | 50 | — | 59 | 55 | $+8.59 | +1.59% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.