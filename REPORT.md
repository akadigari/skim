# SKIM — Skimming Kalshi's Incentive Markets (campaign report)

_Auto-generated 2026-07-14 03:37 UTC — **day 2.2 of 14**. 100% paper: this repo only reads public endpoints and cannot place orders._

## Health

| check | status |
|---|---|
| last checkpoint | 2026-07-14 03:37 UTC — if this is > 7.5h old, the watchdog has already alerted Telegram |
| jobs run (6h chain) | 5 |
| current job age | 5.7h of 5.7h max |
| markets quoting / retired | 15 / 16 |
| favorites open (maker/taker/poly) | 60 / 60 / 30 |
| API requests last job | 31826 |
| crons (UTC) | campaign :19 of 1,7,13,19 — watchdog :49 of 3,9,15,21 |

## Experiment 1 — MM breadth (liquidity-pool harvesting)

**Gate status: BEHIND** — decision $-895.44/day vs GO bar $5.00/day; earn/pay -0.45 vs 1.5; fills 505/30 evidence floor

| metric | value |
|---|---|
| markets quoting now / touched | 15 / 31 |
| est. rewards accrued | $+669.47 |
| spread P&L (cash + mark) | $-1295.00 |
| adverse selection (markout) | $-1311.78 |
| maker fees | $-74.01 |
| **decision number** | **$-2011.32** |
| decision at 0.25x rewards (share-optimism haircut) | $-2513.43 |
| decision at 0.10x rewards | $-2613.85 |
| fills / snapshots (counted) | 505 / 91860 (81715) |

### Per-market

| ticker | pool $/day | share | rewards | AS | fills | decision |
|---|---|---|---|---|---|---|
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI22 | $180 | 52% | $+8.73 | $-154.12 | 69 | $+72.88 |
| KXAAAGASD-26JUL12-3.870 | $198 | 50% | $+21.11 | $-9.00 | 44 | $+27.44 |
| KXWCATTEND-26JUL20-TOMH | $63 | 35% | $+25.58 | $-0.00 | 3 | $+25.59 |
| KXWCATTEND-26JUL20-KEN | $63 | 38% | $+28.34 | $-0.00 | 6 | $+25.30 |
| KXWCATTEND-26JUL20-TIM | $63 | 37% | $+27.41 | $-1.88 | 11 | $+22.61 |
| KXWCATTEND-26JUL20-RIH | $63 | 31% | $+22.59 | $-0.00 | 2 | $+22.59 |
| KXAAAGASD-26JUL12-3.875 | $198 | 69% | $+32.13 | $-30.68 | 80 | $+21.09 |
| KXWCATTEND-26JUL20-VIC | $63 | 34% | $+25.12 | $-0.00 | 8 | $+20.88 |
| KXWCATTEND-26JUL20-TRA | $63 | 63% | $+46.49 | $-14.00 | 15 | $+16.30 |
| KXWCATTEND-26JUL20-KYL | $63 | 48% | $+35.21 | $-0.61 | 18 | $+13.57 |
| KXWCATTEND-26JUL20-TRAV | $63 | 21% | $+15.38 | $-5.00 | 1 | $+9.01 |
| KXWCSTART-26JUL11ARGSUI-SUI-NOKAFO19 | $193 | 62% | $+9.58 | $-1.00 | 2 | $+8.44 |
| KXWCATTEND-26JUL20-PAR | $63 | 42% | $+31.20 | $-0.35 | 11 | $+2.09 |
| KXWCSTART-26JUL11ARGSUI-SUI-LJAQUE25 | $193 | 64% | $+10.51 | $-2.00 | 2 | $+0.38 |
| KXWCSTART-26JUL11ARGSUI-SUI-ZAMDOU23 | $193 | 63% | $+10.39 | $-3.00 | 3 | $-2.78 |
| KXWCATTEND-26JUL20-LEO | $63 | 53% | $+39.41 | $-47.36 | 31 | $-6.24 |
| KXWCSTART-26JUL11ARGSUI-ARG-TALMAD16 | $180 | 52% | $+7.46 | $-8.00 | 11 | $-13.01 |
| KXWCATTEND-26JUL20-DRA | $63 | 41% | $+30.38 | $-22.28 | 9 | $-15.34 |
| KXWCSTART-26JUL11ARGSUI-ARG-RDEPA7 | $180 | 27% | $+3.74 | $-4.90 | 6 | $-20.47 |
| KXWCSTART-26JUL11ARGSUI-ARG-JALVAR9 | $180 | 65% | $+8.99 | $-12.03 | 23 | $-47.00 |
| KXWCSTART-26JUL11ARGSUI-SUI-FRIEDE22 | $193 | 85% | $+12.75 | $-39.21 | 9 | $-49.70 |
| KXWCSTART-26JUL11ARGSUI-SUI-MMUHEI2 | $193 | 81% | $+12.72 | $-28.00 | 5 | $-49.96 |
| KXWCSTART-26JUL11ARGSUI-ARG-LMARTI6 | $180 | 35% | $+4.87 | $-55.00 | 6 | $-52.59 |
| KXWCATTEND-26JUL20-ZEN | $63 | 48% | $+35.27 | $-1.00 | 13 | $-71.01 |
| KXWCATTEND-26JUL20-RYA | $63 | 45% | $+32.97 | $-8.23 | 15 | $-118.24 |
| KXWCSTART-26JUL11ARGSUI-SUI-AJASHA14 | $193 | 94% | $+13.86 | $-69.00 | 6 | $-150.37 |
| KXMLBMENTION-26JUL12MILPIT-GRAN | $66 | 47% | $+5.48 | $-29.82 | 15 | $-265.48 |
| KXWCATTEND-26JUL20-KIM | $63 | 40% | $+29.81 | $-149.19 | 39 | $-273.48 |
| KXWCSTART-26JUL11ARGSUI-ARG-NMOLIN26 | $180 | 69% | $+8.72 | $-205.65 | 26 | $-298.97 |
| KXDXYDUD-26JUL13-T100.9650 | $218 | 39% | $+60.78 | $-136.62 | 6 | $-303.33 |
| KXWCSTART-26JUL11ARGSUI-SUI-RVARGA17 | $193 | 79% | $+12.47 | $-273.86 | 10 | $-561.49 |

## Experiment 2 — Favorites (85-95c maker vs taker control)

**Gate status: UNDERPOWERED** — 10/300 settled maker positions — no verdict yet (this is honest, not broken)

| variant | open | unfilled | settled | wins | P&L | cond-on-fill ROI |
|---|---|---|---|---|---|---|
| kalshi maker | 60 | 7 | 10 | 10 (win-rate CI 72%-100%) | $+8.95 | +9.84% |
| kalshi taker | 60 | — | 17 | 17 | $+11.15 | +7.06% |
| poly taker (zero-fee) | 30 | — | 19 | 18 | $+5.38 | +3.08% |

_If maker ROI < taker ROI, queue fills are adversely selected — the exact failure mode this experiment exists to measure. The Polymarket taker leg is the zero-fee existence test of the bias itself (phase 1: taker-only there; the pre-registered gate is judged on the Kalshi maker leg only)._

## Kill criteria (pre-registered)

- **MM breadth**: at day 14, KILL unless decision >= 3x the $1.67/day 3-market baseline AND earn/pay >= 1.5.
- **Favorites**: KILL if maker conditional-on-fill ROI <= 0 once 300 positions settle (report stays UNDERPOWERED until then rather than faking a verdict).
- The Kalshi liquidity/volume incentive programs end **Sept 1, 2026** — a GO here is only actionable before renewal risk.