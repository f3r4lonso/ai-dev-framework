# Metric definitions

Notation: equity values `E_0 … E_n` sampled at a fixed frequency; simple period returns `r_t = E_t / E_(t-1) - 1`;
`N` = periods per year (365 for 24/7 markets, 252 for trading-day markets, adapted for other frequencies);
`T` = number of returns; `rf` = risk-free rate per period (0 unless stated); `MAR` = target return per period
(0 unless stated). `std` is the sample standard deviation (ddof = 1).

## Returns

| Metric | Definition | Notes |
|---|---|---|
| Total return | `E_n / E_0 - 1` | Net of all costs unless labelled gross |
| CAGR | `(E_n / E_0) ^ (1 / years) - 1`, `years = T / N` (or calendar days / 365.25) | Unavailable if `E_n <= 0` or `years` < 1 unless labelled "not annualized" |
| Annualized volatility | `std(r) * sqrt(N)` | |

## Risk-adjusted returns

| Metric | Definition | Minimum sample | Edge cases |
|---|---|---|---|
| Sharpe ratio | `mean(r - rf) / std(r - rf) * sqrt(N)` | 30 periods | `std = 0` → unavailable |
| Sortino ratio | `mean(r - MAR) / DD * sqrt(N)`, with downside deviation `DD = sqrt( sum(min(r_t - MAR, 0)^2) / T )` over **all** `T` periods | 30 periods | No period below `MAR` → unavailable (not infinite) |
| Calmar ratio | `CAGR / abs(MaxDD)` over the same period | 1 year of data | `MaxDD = 0` → unavailable |

Common Sortino mistake: dividing by `std` of the negative returns only. That ignores how often losses occur and how
far they fall from the target, and usually overstates the ratio when losses are rare and uniform.

## Drawdown

- Running peak: `P_t = max(E_0 … E_t)`.
- Drawdown: `DD_t = E_t / P_t - 1` (≤ 0).
- Maximum drawdown: `MaxDD = min_t DD_t`; report as a negative percentage or state the sign convention.
- Drawdown duration: periods from a peak to the recovery of that peak; if not recovered, report as "not recovered, X
  periods so far".
- Compute from the equity curve at the finest available frequency (intraday equity if positions are held intraday);
  daily closes understate intraday drawdowns, so state the frequency.

## Tail risk (historical)

For confidence level `c` (for example 0.95) over `T` returns:

- `q` = the `(1 - c)` empirical quantile of `r` (state the interpolation method used).
- VaR: `VaR_c = -q` (a positive number meaning "loss not exceeded with probability c over one period").
- CVaR / Expected Shortfall: `CVaR_c = -mean(r_t | r_t <= q)`.
- Minimum sample: at least `ceil(10 / (1 - c))` returns (200 for 95 %), otherwise unavailable.
- Scaling to longer horizons with `sqrt(h)` assumes independent returns; label any scaled figure.

## Trade statistics

Over closed trades with net P&L `p_i` (after fees, slippage, funding) and initial risk `R_i` (money at risk to the stop):

| Metric | Definition | Edge cases |
|---|---|---|
| Win rate | `count(p_i > 0) / count(trades)` | Break-even trades counted separately and disclosed |
| Profit factor | `sum(p_i > 0) / abs(sum(p_i < 0))` | No losing trade → unavailable |
| Average win / loss | mean of positive / negative `p_i` | |
| R-multiple | `p_i / R_i` | Trades without a defined initial risk are excluded and counted |
| Expectancy (R) | `mean(R-multiples)` | Minimum 30 trades for any claim |
| Expectancy (money) | `mean(p_i)` | |

## Worked example for tests

Equity: `100, 110, 99, 108.9, 98.01`.

- Returns: `0.10, -0.10, 0.10, -0.10`; mean `0.0`; `std` (ddof 1) `0.11547`.
- Total return: `-1.99 %`.
- Running peak: `100, 110, 110, 110, 110`; drawdowns `0, 0, -10 %, -1 %, -10.9 %`; MaxDD `-10.9 %`.
- Sortino with `MAR = 0`: `DD = sqrt((0.01 + 0.01) / 4) = 0.070711`; mean `0` → ratio `0`.
- Sharpe: `0`. (Use a series with non-zero mean to test the annualization factor.)
- Too few periods for any annualized ratio to be reported: the implementation should return unavailable here unless
  the minimum-sample check is disabled for the test.
