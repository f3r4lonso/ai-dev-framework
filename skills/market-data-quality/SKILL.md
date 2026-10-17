---
name: market-data-quality
description: Reviews market data quality (candles, funding, timestamps, gaps, duplicates, freshness) when adding or debugging an Algo Lab provider or instrument. Use it when touching backend/algo/data.py or instruments.py, or when investigating odd backtest results.
---

# Market data quality

Code involved: `backend/algo/data.py` (download, store, `validate`, `snapshot`), `backend/algo/instruments.py`.

## Checks
1. **Timestamps**: UTC seconds of the candle *open*; `close_time = open_time + tf`. Time zone converted to UTC
   (Yahoo delivers America/New_York). Do not mix milliseconds and seconds (Binance uses ms).
2. **Completed candles only**: nothing with `open_time + tf > now` enters the store or a signal.
3. **Order and duplicates**: `validate()` must give `duplicates = 0` and `out_of_order = 0`.
4. **Gaps**: 24/7 → any jump is a gap. With trading hours → jumps ≤ 4.5 days count as market closure; larger ones are gaps.
   Gaps inside the strategy window → **no** actionable signals are generated (`gap_flags`).
5. **Invalid values**: prices ≤ 0, high < low, NaN, negative volume.
6. **Freshness**: stale data → non-actionable signal and a visible warning (Health / Market).
7. **Symbol / contract changes**: Yahoo continuous futures series (`MES=F`…) have *roll* jumps; warn about them.
8. **Precision**: Binance tick/step/minimums from `exchangeInfo`; the rest are estimates marked `verified: estimate`.
9. **Derived series**: Yahoo 4h is aggregated from 1h in UTC blocks; document any derived series.
10. **Reproducibility**: a backtest must reference the checksum of the `snapshot` used.

## Rules
- Do not invent or fill in missing data. Do not interpolate.
- If a strategy depends on incomplete or stale data, it must reject or downgrade the signal explicitly.
- Add a test in `backend/tests/` for each data defect found.
