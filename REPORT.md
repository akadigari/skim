# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 17:41 UTC — **day 2.8 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 17:41 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 7 |
| current job age | 2.0h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 37 |
| API requests last job | 11360 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-782.56/day vs GO bar $5.00/day; earn/pay -0.43 vs 1.5; fills 529/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+751.34 |
| spread P&L (cash + mark) | $-1414.82 |
| adverse selection (markout) | $-1473.41 |
| maker fees | $-79.39 |
| **decision number** | **$-2216.28** |
| decision at 0.25x rewards (share-optimism haircut) | $-2779.78 |
| decision at 0.10x rewards | $-2892.48 |
| fills / snapshots (counted) | 529 / 112620 (101091) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 32% | $+30.03 | $-0.00 | 3 | $+30.03 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+36.06 | $-7.38 | 25 | $+27.84 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-RIH | $63 | 26% | $+24.38 | $-0.00 | 2 | $+24.37 |
| KXWCATTEND-26JUL20-VIC | $63 | 31% | $+29.52 | $-0.00 | 8 | $+22.20 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-KYL | $63 | 44% | $+41.02 | $-16.74 | 19 | $+20.67 |
| KXWCATTEND-26JUL20-TRAV | $63 | 17% | $+16.08 | $-5.00 | 1 | $+9.71 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-PAR | $63 | 39% | $+36.27 | $-0.35 | 11 | $+7.16 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCATTEND-26JUL20-LEO | $63 | 46% | $+43.48 | $-47.36 | 31 | $-2.36 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-DRA | $63 | 36% | $+33.57 | $-22.28 | 9 | $-12.15 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 40% | $+37.38 | $-43.00 | 7 | $-61.19 |
| KXWCATTEND-26JUL20-ZEN | $63 | 47% | $+44.22 | $-21.00 | 15 | $-70.47 |
| KXWCATTEND-26JUL20-TRA | $63 | 57% | $+54.00 | $-48.00 | 16 | $-98.69 |
| KXWCATTEND-26JUL20-RYA | $63 | 42% | $+39.18 | $-20.23 | 16 | $-133.95 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 44% | $+41.84 | $-180.19 | 43 | $-294.53 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-303.33 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 11/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 11 | 10 (win-rate CI 62%-98%) | $+0.23 | +0.23% |
| kalshi taker | 60 | — | 18 | 17 | $+2.27 | +1.36% |
| poly taker (zero-fee) | 37 | — | 24 | 23 | $+8.94 | +4.04% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.