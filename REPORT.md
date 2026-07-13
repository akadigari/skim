# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-13 05:51 UTC — **day 1.3 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-13 05:51 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 3 |
| current job age | 1.0h of 5.7h max |
| markets quoting / retired | 15 / 15 |
| favorites open (maker/taker/poly) | 60 / 60 / 21 |
| API requests last job | 5950 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-882.50/day vs GO bar $5.00/day; earn/pay -0.02 vs 1.5; fills 387/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+466.09 |
| spread P&L (cash + mark) | $-485.25 |
| adverse selection (markout) | $-1104.53 |
| maker fees | $-57.99 |
| **decision number** | **$-1181.68** |
| decision at 0.25x rewards (share-optimism haircut) | $-1531.24 |
| decision at 0.10x rewards | $-1601.16 |
| fills / snapshots (counted) | 387 / 48645 (38500) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TRA | $63 | 77% | $+24.87 | $-0.00 | 0 | $+24.87 |
| KXWCATTEND-26JUL20-RYA | $63 | 72% | $+23.22 | $-0.00 | 0 | $+23.22 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-KYL | $63 | 67% | $+21.56 | $-0.00 | 4 | $+20.51 |
| KXWCATTEND-26JUL20-TOMH | $63 | 62% | $+19.83 | $-0.00 | 3 | $+19.84 |
| KXWCATTEND-26JUL20-TIM | $63 | 57% | $+18.53 | $-0.00 | 8 | $+19.38 |
| KXWCATTEND-26JUL20-RIH | $63 | 58% | $+18.64 | $-0.00 | 2 | $+18.63 |
| KXWCATTEND-26JUL20-KEN | $63 | 66% | $+21.32 | $-0.00 | 6 | $+18.28 |
| KXWCATTEND-26JUL20-PAR | $63 | 54% | $+17.35 | $-0.00 | 0 | $+17.35 |
| KXWCATTEND-26JUL20-ZEN | $63 | 67% | $+21.71 | $-0.00 | 6 | $+15.61 |
| KXWCATTEND-26JUL20-VIC | $63 | 51% | $+16.41 | $-0.00 | 8 | $+12.17 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 42% | $+13.45 | $-5.00 | 1 | $+7.08 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 74% | $+6.78 | $-0.00 | 0 | $+6.78 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-LEO | $63 | 65% | $+20.97 | $-41.56 | 13 | $-5.16 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCATTEND-26JUL20-DRA | $63 | 69% | $+22.13 | $-22.28 | 9 | $-23.60 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-30.43 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-KIM | $63 | 49% | $+15.79 | $-110.42 | 10 | $-210.10 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 0/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 0 | 0 | 0 (win-rate CI 0%-100%) | $+0.00 | n/a |
| kalshi taker | 60 | — | 0 | 0 | $+0.00 | n/a |
| poly taker (zero-fee) | 21 | — | 12 | 11 | $-0.12 | -0.11% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.