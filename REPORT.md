# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 00:58 UTC — **day 2.1 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 00:58 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 5 |
| current job age | 3.0h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 29 |
| API requests last job | 17024 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-908.90/day vs GO bar $5.00/day; earn/pay -0.41 vs 1.5; fills 478/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+635.43 |
| spread P&L (cash + mark) | $-1203.31 |
| adverse selection (markout) | $-1302.90 |
| maker fees | $-70.19 |
| **decision number** | **$-1940.98** |
| decision at 0.25x rewards (share-optimism haircut) | $-2417.55 |
| decision at 0.10x rewards | $-2512.86 |
| fills / snapshots (counted) | 478 / 84690 (74545) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TRA | $63 | 63% | $+41.99 | $-8.00 | 5 | $+26.97 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+25.35 | $-0.00 | 8 | $+26.20 |
| KXWCATTEND-26JUL20-KEN | $63 | 41% | $+27.44 | $-0.00 | 6 | $+24.40 |
| KXWCATTEND-26JUL20-TOMH | $63 | 35% | $+23.67 | $-0.00 | 3 | $+23.68 |
| KXWCATTEND-26JUL20-RIH | $63 | 32% | $+21.57 | $-0.00 | 2 | $+21.56 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-VIC | $63 | 36% | $+23.91 | $-0.00 | 8 | $+19.66 |
| KXWCATTEND-26JUL20-KYL | $63 | 49% | $+33.13 | $-0.61 | 17 | $+11.46 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 21% | $+14.35 | $-5.00 | 1 | $+7.98 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCATTEND-26JUL20-ZEN | $63 | 50% | $+33.39 | $-1.00 | 13 | $-0.31 |
| KXWCATTEND-26JUL20-PAR | $63 | 42% | $+28.48 | $-0.35 | 11 | $-0.63 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-LEO | $63 | 55% | $+37.18 | $-47.36 | 30 | $-8.49 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-DRA | $63 | 43% | $+29.09 | $-22.28 | 9 | $-16.64 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-RYA | $63 | 46% | $+30.74 | $-8.23 | 13 | $-120.48 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 38% | $+25.80 | $-148.19 | 29 | $-266.44 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 43% | $+55.81 | $-136.62 | 6 | $-308.31 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 7/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 7 | 7 (win-rate CI 65%-100%) | $+6.39 | +10.07% |
| kalshi taker | 60 | — | 14 | 14 | $+9.01 | +6.91% |
| poly taker (zero-fee) | 29 | — | 19 | 18 | $+5.38 | +3.08% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.