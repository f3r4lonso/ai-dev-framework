---
name: strategy-specification
description: Defines or reviews the deterministic specification of a trading strategy (entries, exits, stop, target, expiry, filters, costs, versioned parameters and test cases) before implementing or changing it in the Algo Lab.
---

# Strategy specification

Reference implementation: `backend/algo/strategies/trend_following.py` (DEFINITION, `prepare`, `signal_arrays`,
`stop_target`, `explain`). Registry in `backend/algo/strategies/__init__.py`. Versions in `backend/algo/versions.py`.

## The specification must define
1. Market **hypothesis** and when it should fail.
2. Compatible **instruments** (perpetual, spot, future, ETF, stock) and whether it allows shorts.
3. Context and entry **timeframes**; **closed** candles only.
4. Numbered **entry rules** (such as T1, T2, P1, R1…), each with a checkable value and threshold.
5. **Exit**: stop (method and formula), target (in R), time-based exit if applicable; evaluation order.
6. Signal **expiry and invalidation**.
7. Regime / volatility **filters**, if any, defined with numbers.
8. **Parameters** with default values in `default_params` and help in `param_help`. Changing them = new version.
9. **Minimum data** (warm-up candles) and behavior with incomplete data.
10. Relevant **costs** (commission, spread, slippage, funding) and minimum net reward/risk.
11. Strategy **acceptance and rejection criteria** (e.g. net expectancy > 0 out of sample with ≥ 30 trades).
12. **Test cases**: valid long, valid short, invalid trend, no pullback, insufficient history, gaps,
    incomplete candle, zero-distance stop, insufficient reward/risk.

## Rules
- No visual or discretionary interpretation ("looks like support"): everything must be computable.
- The strategy does **not** decide size or risk: the central risk engine sets them.
- Do not add a strategy just to use a popular indicator or to generate many signals.
- Do not design rules while looking at the test (out-of-sample) period.
