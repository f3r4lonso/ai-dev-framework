---
name: exchange-integration
description: Guide for integrating or reviewing an exchange or broker (Binance, Bitget, CCXT or other) in the Algo Lab, for both data and future demo execution. Use it before adding endpoints, connectors, credentials or a demo/testnet environment.
---

# Exchange integration

Current state: only Binance **public data** (USDⓈ-M and Spot) via direct REST in `backend/algo/data.py`.
No order code exists. Demo execution is Phase 5 and requires explicit authorization.

## Before writing code
1. Read the exchange's **current official documentation** for the exact market type (spot ≠ perpetual ≠ dated
   future). Note URL and date.
2. Verify for the instrument: identifier, tick size, step size, minimum quantity and notional, margin mode,
   position mode (one-way/hedge), funding, order types, weight/rate limits, WebSocket and reconnection,
   demo/testnet environment and regional availability for the user's account.
3. If you use CCXT: confirm the exchange really implements the required methods; a unified API does not guarantee
   parity. Do not install its skill or SDK without `dependency-license-review` and authorization.

## Mandatory design
- Separate interfaces: **market data** (public) and **execution** (private). Execution is only called from the
  execution service, after the risk engine (`backend/algo/risk.py`).
- Separate demo and production configuration; production disabled by default.
- Credentials only via environment variables or a secure store outside the repo; never in logs; no withdrawal permission.
- Apply the `order-lifecycle-safety` skill to everything that sends, cancels or queries orders.

## Tests required before allowing any execution
HTTP/network errors, rate limit (418/429), partial response, duplicate orders, ambiguous timeout + reconciliation,
WebSocket reconnection, rounding to tick/step and rejection for minimums. Use mocks or minimum-permission demo credentials.
