---
name: order-lifecycle-safety
description: Reviews order lifecycle safety (idempotency, reconciliation, partial fills, cancellations, ambiguous timeouts, external orders) in any code that sends, cancels or queries orders, whether simulated, demo or real.
---

# Order lifecycle safety

Today there is no order code in the Algo Lab (`backend/algo/` has no order endpoints; a test verifies it).
This skill applies to Phase 4 (paper) and above all to Phase 5 (demo).

## States to distinguish
Not sent · send confirmed · rejection confirmed · **unknown outcome** · partially filled · fully filled ·
cancellation confirmed.

## Rules
1. **Idempotency**: every order carries a unique, deterministic `client_order_id`; a retry reuses the same id.
2. **Timeout ≠ failure**: if the outcome is unknown, **query the remote state** and reconcile before retrying.
   Never blindly create a second order.
3. **Disconnection ≠ outcome**: the connection state does not tell whether the order was accepted.
4. **Reconciliation on startup**: compare local orders and positions with the exchange before activating strategies;
   report unresolved ids and do not trade until they are resolved.
5. **External orders**: the exchange may report orders not created by the app; treat them as normal input.
6. **Partial fills** accumulated per order; the position is derived from fills, not from the send.
7. An "accepted" response does not prove a cancellation or modification finished, nor that the position is flat.
8. Every order originates from a signal approved by the risk engine; the kill switch blocks new entry orders.

## Required tests
Timeout followed by an existing order (do not duplicate), timeout followed by a non-existent order, partial + cancellation,
reconnection, startup with open orders, external order, rate limit, kill switch with a pending order.
