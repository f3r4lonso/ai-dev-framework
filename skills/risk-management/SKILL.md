---
name: risk-management
description: Reviews or modifies Algo Lab risk management (capital, risk per trade, size, leverage, stops, aggregate exposure, daily/weekly limits, drawdown, kill switch, circuit breakers). Use it before touching backend/algo/risk.py, settings.py or position sizing.
---

# Risk management

Central engine: `backend/algo/risk.py` (`evaluate`, `AccountState`, `DEFAULT_CONFIG`). Persistent configuration with
history: `backend/algo/settings.py`. Used by the backtester and the scanner; **nothing may bypass it**.

## Verify
1. **R** = quantity × (distance to stop × multiplier + estimated round-trip cost per unit). R includes costs.
2. **Size**: budget = equity × risk%; quantity rounded **down** to the step; if the instrument minimum
   risks more than the budget → **reject** (never raise the risk).
3. **Leverage / notional**: if exceeded, reduce quantity (never increase it); spot/ETF/stocks = 1x.
4. **Net reward/risk** after costs ≥ max(strategy minimum, global minimum).
5. **Exposure**: one exposure per underlying asset (BTC perpetual + BTC spot = same asset), maximum number of positions
   and aggregate open risk. BTC/ETH correlation: do not assume diversification.
6. **Limits**: UTC day and UTC ISO week in R; drawdown alert/review/pause/suspension; resuming requires explicit action.
7. **Kill switch**: blocks new entries; does **not** close positions.
8. **Failures**: stale or incomplete data → reject; stop on the wrong side → reject.
9. **Double counting**: realized and unrealized P&L must not be added twice in the limits.
10. **Audit trail**: every decision records its rules (`risk_decisions` table live; per-trade checks in backtest).

## Rules
- Do not recommend raising risk or leverage, or lowering minimums, to get a trade accepted.
- Allocated capital, notional, margin, monetary risk and drawdown are different quantities: do not mix them.
- Every change to `risk.py` needs tests in `backend/tests/test_algo.py` (class `TestCostsAndRisk`) and must pass the full suite.
