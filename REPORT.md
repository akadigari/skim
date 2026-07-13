# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-13 22:27 UTC — **day 2.0 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-13 22:27 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 5 |
| current job age | 0.5h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 30 |
| API requests last job | 2944 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-929.11/day vs GO bar $5.00/day; earn/pay -0.42 vs 1.5; fills 466/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+603.29 |
| spread P&L (cash + mark) | $-1161.78 |
| adverse selection (markout) | $-1261.80 |
| maker fees | $-66.67 |
| **decision number** | **$-1886.97** |
| decision at 0.25x rewards (share-optimism haircut) | $-2339.44 |
| decision at 0.10x rewards | $-2429.93 |
| fills / snapshots (counted) | 466 / 77910 (67765) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TRA | $63 | 63% | $+37.89 | $-0.00 | 2 | $+39.16 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+22.99 | $-0.00 | 8 | $+23.84 |
| KXWCATTEND-26JUL20-KEN | $63 | 44% | $+26.66 | $-0.00 | 6 | $+23.62 |
| KXWCATTEND-26JUL20-TOMH | $63 | 36% | $+21.67 | $-0.00 | 3 | $+21.68 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-RIH | $63 | 34% | $+20.55 | $-0.00 | 2 | $+20.54 |
| KXWCATTEND-26JUL20-VIC | $63 | 38% | $+22.88 | $-0.00 | 8 | $+18.64 |
| KXWCATTEND-26JUL20-ZEN | $63 | 53% | $+32.18 | $-1.00 | 13 | $+12.09 |
| KXWCATTEND-26JUL20-KYL | $63 | 51% | $+30.74 | $-0.61 | 17 | $+9.07 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 23% | $+13.62 | $-5.00 | 1 | $+7.25 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-PAR | $63 | 42% | $+25.64 | $-0.35 | 11 | $-3.47 |
| KXWCATTEND-26JUL20-LEO | $63 | 57% | $+34.45 | $-47.36 | 30 | $-10.86 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-DRA | $63 | 47% | $+28.35 | $-22.28 | 9 | $-17.38 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-RYA | $63 | 47% | $+28.23 | $-8.12 | 9 | $-124.87 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-KIM | $63 | 39% | $+23.48 | $-115.19 | 24 | $-211.01 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 47% | $+50.43 | $-136.62 | 6 | $-313.69 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 7/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 7 | 7 (win-rate CI 65%-100%) | $+6.39 | +10.07% |
| kalshi taker | 60 | — | 14 | 14 | $+9.01 | +6.91% |
| poly taker (zero-fee) | 30 | — | 18 | 17 | $+4.88 | +2.95% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.