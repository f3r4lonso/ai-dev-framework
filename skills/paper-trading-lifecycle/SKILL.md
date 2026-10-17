---
name: paper-trading-lifecycle
description: Designs and validates the simulated lifecycle signal → risk validation → order → fill → position → closed trade for the Algo Lab internal paper trading (Phase 4). Use it when implementing or reviewing the real-time simulation.
---

# Paper trading lifecycle

Status: Algo Lab paper trading is **Phase 4** (not implemented). The original app has its own paper trading
(`backend/paper.py`), which must **not** be mixed with the Algo Lab one.

## Separate entities (do not confuse)
Signal (`backend/algo/signals.py`, immutable) → risk decision → **simulated order** (own id, linked to the signal) →
**fill(s)** (price, quantity, time, commission) → **position** → **closed trade** (entries, exits, costs, net P&L, R).

## Rules
1. Valid signal states according to `TRANSITIONS` / `ENABLED_IN_MODE`; enable `Approved` and `Simulated` only in this phase.
2. Every simulated order goes through `risk.evaluate` with the real paper state (equity, day/week in R, open positions).
3. Record the **theoretical price** (signal), the **simulated price** (fill) and the difference (observed slippage).
4. Touching a price does not guarantee the fill: same policy as the backtest (target only if exceeded by 1 tick, stop first).
5. Costs and funding identical to the backtest, so paper and backtest are comparable.
6. Persistence and recovery after restart: open positions and orders survive closing the app.
7. Results labeled `mode = 'paper'`; never added to backtest or real results without separation.
8. Measure the signal → simulated execution difference as a metric of its own.

## Minimum tests
Approval and rejection by risk, entry fill, stop, target, expiry before the fill, kill switch during a
pending signal, restart with an open position, daily limits reached mid-session.
