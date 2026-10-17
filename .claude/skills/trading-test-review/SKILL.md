---
name: trading-test-review
description: Runs and reviews the tests before considering a strategy, a phase or a change to the Algo Lab risk engine, data or backtester finished, and writes an honest summary of what was tested, what failed and what was not tested.
---

# Test review

## Run (Windows / PowerShell, no network)
```
cd backend
.venv\Scripts\python -m unittest discover -s tests -t . -v
```
If the change touches the interface: `cd frontend; npm run build` (must build without errors).

## Review
1. That the tests **were run** and their real result (copy the summary: number of tests, OK/FAIL).
2. Coverage of the change: positive and negative cases, edge cases (minimums, rounding, zero-distance stop, empty data).
3. Regressions: the full suite passes, not just the new tests.
4. Project invariants that must always keep passing:
   no look-ahead (`TestNoLookAhead`), stop = −1R (`test_stop_trades_are_minus_one_r`), net accounting,
   reproducibility by hash, absence of order endpoints and secrets (`TestSafety`), separate modes.
5. For backtests with real data: the number of trades and the warnings; "it doesn't fail" is not enough.
6. Floats are compared with tolerance (`assertAlmostEqual`), never with exact equality.

## Summary (mandatory)
- **Tested** (real commands and results).
- **Failed** (and what was fixed).
- **Not tested** (and why: network, data, future phase).
Never mark as passed a test that was not run.
