# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 09:19 UTC — **day 2.5 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 09:19 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 6 |
| current job age | 5.0h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 32 |
| API requests last job | 28082 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-897.06/day vs GO bar $5.00/day; earn/pay -0.47 vs 1.5; fills 513/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+724.59 |
| spread P&L (cash + mark) | $-1436.22 |
| adverse selection (markout) | $-1439.78 |
| maker fees | $-76.89 |
| **decision number** | **$-2228.29** |
| decision at 0.25x rewards (share-optimism haircut) | $-2771.74 |
| decision at 0.10x rewards | $-2880.43 |
| fills / snapshots (counted) | 513 / 105405 (94357) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXWCATTEND-26JUL20-TOMH | $63 | 33% | $+28.99 | $-0.00 | 3 | $+29.00 |
| KXWCATTEND-26JUL20-TIM | $63 | 38% | $+32.81 | $-1.88 | 11 | $+28.01 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-RIH | $63 | 28% | $+24.14 | $-0.00 | 2 | $+24.13 |
| KXWCATTEND-26JUL20-VIC | $63 | 31% | $+26.95 | $-0.00 | 8 | $+22.71 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-KYL | $63 | 44% | $+38.54 | $-0.61 | 18 | $+16.89 |
| KXWCATTEND-26JUL20-TRAV | $63 | 18% | $+16.05 | $-5.00 | 1 | $+9.68 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-PAR | $63 | 40% | $+34.84 | $-0.35 | 11 | $+5.73 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-LEO | $63 | 48% | $+42.00 | $-47.36 | 31 | $-3.65 |
| KXWCATTEND-26JUL20-DRA | $63 | 38% | $+32.97 | $-22.28 | 9 | $-12.75 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-ZEN | $63 | 47% | $+41.37 | $-21.00 | 15 | $-73.32 |
| KXWCATTEND-26JUL20-KEN | $63 | 39% | $+33.57 | $-43.00 | 7 | $-77.08 |
| KXWCATTEND-26JUL20-TRA | $63 | 60% | $+52.35 | $-48.00 | 16 | $-100.34 |
| KXWCATTEND-26JUL20-RYA | $63 | 43% | $+37.29 | $-8.23 | 15 | $-113.93 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 44% | $+38.41 | $-180.19 | 43 | $-298.46 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-303.33 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 10/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 10 | 10 (win-rate CI 72%-100%) | $+8.95 | +9.84% |
| kalshi taker | 60 | — | 17 | 17 | $+11.15 | +7.06% |
| poly taker (zero-fee) | 32 | — | 20 | 19 | $+5.97 | +3.25% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.