---
name: backtesting-audit
description: Audits the methodology and results of an Algo Lab backtest (look-ahead, fills, costs, funding, splits, sample, reproducibility, metrics). Use it before accepting results, comparing versions or strategies, or enabling paper trading.
---

# Backtesting audit

Code: `backend/algo/backtester.py` (`simulate`, `metrics`, `execute`), `execution.py` (CostModel), `risk.py`.
Stored results: `backtests` table and `backend/data/algo/backtests/<id>.json.gz`; data in `backend/data/algo/datasets/`.
API: `GET /api/algo/backtests/<id>`, `POST /api/algo/backtests/<id>/reproduce`.

## Steps
1. **Identify**: id, engine version, strategy and version, parameters, instrument, interval, dataset (checksum).
2. **Data**: closed candles, UTC timestamps, no duplicates; gaps and backtest warnings (`market-data-quality` skill).
3. **Look-ahead / leakage**: the 4h context only uses closed candles (`merge_asof` on `close_time`); entry is at the
   open of the next candle; no indicator uses future data. Run `TestNoLookAhead`.
4. **Fills**: stop before target within the same candle; target only if exceeded by 1 tick; gaps fill at the open;
   commission on both sides; slippage and spread against you. Look for unrealistic fills.
5. **Costs**: compare gross vs net and the ×2 scenario. Funding applied on perpetuals (sign: long pays if rate > 0).
6. **Splits**: development / validation / test by time; the sensitivity analysis does not use the test period.
7. **Sample and stability**: number of trades per split (< 30 = inconclusive), P&L concentration in a few
   trades, stability of the sensitivity table (if only one cell wins, it is fragile).
8. **Metrics**: recompute at least net P&L, expectancy in R, profit factor and drawdown from the trade list.
9. **Reproducibility**: reproduce the backtest and confirm the result hash matches.
10. **Conclusions**: flag every claim not supported by the data.

## Rules
- Do not modify the strategy or the engine to "improve" the result during the audit.
- A profit factor > 1 on a small sample is **not** a statistical edge. Do not extrapolate to the future.

## Deliverable
Prioritized findings (confirmed / possible / unverifiable) with evidence (file:line, command, figure) and a
recommendation: **accept**, **reject** or **repeat** the backtest (stating what to change).
