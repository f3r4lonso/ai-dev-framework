---
name: risk-metrics-calculation
description: Compute, implement or review performance and risk metrics for a strategy, backtest or portfolio - returns, volatility, Sharpe, Sortino, maximum drawdown, Calmar, VaR/CVaR, profit factor and expectancy - with one consistent set of definitions. Use when adding or checking any metric shown in a backtest or paper-trading report.
---

# Risk Metrics Calculation

Use this skill whenever code computes or a report shows performance or risk metrics. It fixes **one definition per
metric** so results are comparable across backtests, paper trading and reports. Formulas and edge cases:
[references/formulas.md](references/formulas.md) (read it before implementing or auditing a metric).

Related skills: `backtesting-audit` (whether the backtest itself can be trusted), `risk-management` (live limits,
sizing, kill switch), `trading-test-review` (done criteria). A correct metric on a flawed backtest is still wrong.

## 1. Rules that apply to every metric

- **State the inputs.** Every reported metric names its return series (from equity or from trades), sampling
  frequency (daily UTC, per trade), period covered, annualization factor, risk-free rate or target used, and whether
  results are **net of fees, spread, slippage and funding**. Gross-only metrics must be labelled gross.
- **Annualize consistently.** Use the periods per year of the instrument's calendar: 365 for 24/7 markets (crypto),
  252 for markets with trading days. Remove non-trading days *before* computing returns. Never mix calendars in one
  portfolio metric without resampling to a common calendar.
- **Respect sample size.** Report the number of periods or trades. Below the minimum in the formulas reference, show
  the metric as unavailable instead of a number. Annualized figures from a few weeks of data are not evidence.
- **Keep modes separate.** Never combine backtest, paper, demo and real results in one metric; label each.
- **Use several metrics.** No single number describes risk. Always pair a return/risk ratio with maximum drawdown and
  the trade count; add tail metrics (VaR/CVaR) when sizing or limits depend on them.
- **Do not assume normal returns.** Prefer historical (empirical) VaR/CVaR; if a parametric figure is shown, label it.
- **Never tune a strategy to improve a metric on the same data used to report it**; report out-of-sample metrics
  separately and as clearly as in-sample ones, including when they are worse.

## 2. Implementing

- Compute metrics in one module with pure functions over plain sequences or pandas Series; no I/O inside.
- Handle edge cases explicitly: empty series, a single period, zero standard deviation, no losing periods, equity that
  touches zero. Return "unavailable" (`None`) instead of `inf`, `NaN` or a misleading zero.
- Use sample standard deviation (ddof = 1) and document it.
- Do not round inside calculations; round only for display.

## 3. Testing and review

- Unit-test each metric against a small hand-computed example (included in the formulas reference) and against the
  edge cases above, with a float tolerance.
- When reviewing an existing implementation, check it line by line against the formulas reference; report any
  definition that differs (for example, a Sortino computed with the standard deviation of negative returns only, which
  is not the standard downside deviation) and its effect on the reported figure.
- Recompute at least one metric independently from the trade list or equity curve before trusting a report.

## Trading-app notes

- Backtest metrics live in `backend/algo/backtester.py` (daily UTC equity returns, 365 or 252 annualization, minimum
  30 daily returns). Changes there need `backtesting-auditor` review before results are accepted.
- Trade metrics in R (expectancy, R distribution) follow the definitions in `strategy-specification` and
  `risk-management`; this skill does not change limits or sizing.
