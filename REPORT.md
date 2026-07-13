# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-13 12:36 UTC — **day 1.6 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-13 12:36 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 4 |
| current job age | 2.0h of 5.7h max |
| markets quoting / retired | 15 / 15 |
| favorites open (maker/taker/poly) | 60 / 60 / 30 |
| API requests last job | 11349 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-799.38/day vs GO bar $5.00/day; earn/pay -0.03 vs 1.5; fills 391/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+552.31 |
| spread P&L (cash + mark) | $-590.76 |
| adverse selection (markout) | $-1197.91 |
| maker fees | $-59.09 |
| **decision number** | **$-1295.46** |
| decision at 0.25x rewards (share-optimism haircut) | $-1709.69 |
| decision at 0.10x rewards | $-1792.53 |
| fills / snapshots (counted) | 391 / 66660 (56515) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TRA | $63 | 63% | $+31.44 | $-0.00 | 2 | $+31.45 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-KYL | $63 | 53% | $+26.52 | $-0.00 | 4 | $+25.47 |
| KXWCATTEND-26JUL20-RYA | $63 | 51% | $+25.31 | $-0.00 | 0 | $+25.31 |
| KXWCATTEND-26JUL20-TIM | $63 | 43% | $+21.53 | $-0.00 | 8 | $+22.38 |
| KXWCATTEND-26JUL20-ZEN | $63 | 57% | $+28.27 | $-0.00 | 6 | $+22.17 |
| KXWCATTEND-26JUL20-KEN | $63 | 49% | $+24.55 | $-0.00 | 6 | $+21.51 |
| KXWCATTEND-26JUL20-PAR | $63 | 43% | $+21.47 | $-0.00 | 0 | $+21.47 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-TOMH | $63 | 41% | $+20.29 | $-0.00 | 3 | $+20.30 |
| KXWCATTEND-26JUL20-RIH | $63 | 38% | $+19.05 | $-0.00 | 2 | $+19.04 |
| KXWCATTEND-26JUL20-VIC | $63 | 42% | $+21.01 | $-0.00 | 8 | $+16.77 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-TRAV | $63 | 27% | $+13.46 | $-5.00 | 1 | $+7.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-LEO | $63 | 62% | $+30.72 | $-41.56 | 13 | $-18.57 |
| KXWCATTEND-26JUL20-DRA | $63 | 54% | $+26.64 | $-22.28 | 9 | $-19.08 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-30.43 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 54% | $+38.06 | $-93.38 | 2 | $-138.79 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXWCATTEND-26JUL20-KIM | $63 | 41% | $+20.46 | $-110.42 | 10 | $-205.43 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 0/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 1 | 0 | 0 (win-rate CI 0%-100%) | $+0.00 | n/a |
| kalshi taker | 60 | — | 1 | 1 | $+0.37 | +3.85% |
| poly taker (zero-fee) | 30 | — | 12 | 11 | $-0.12 | -0.11% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.