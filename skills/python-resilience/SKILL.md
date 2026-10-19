---
name: python-resilience
description: Add or review timeouts, retries with backoff, rate-limit handling, fallbacks and failure isolation for Python code that calls networks, APIs, files or databases. Use when a Python service fetches external data or must keep working while a dependency is slow or down.
---

# Python Resilience

Use this skill when Python code depends on something that can be slow, fail or refuse requests: HTTP APIs, market
data feeds, exchanges, files, databases. It complements `python-error-handling` (exception design and validation).
For anything that sends, cancels or queries orders, `order-lifecycle-safety` takes precedence over this skill.

## 1. Inspect first

- Find the HTTP client in use (`requests`, `httpx`, `urllib`) and any existing retry or backoff helper; extend it
  rather than adding a second one.
- Do not add a retry library (for example `tenacity`) without the project's dependency review and user approval. A
  small, tested helper on the standard library is usually enough.

## 2. Timeouts

- Every network call has an explicit timeout. `requests` has no default timeout and can block forever; pass
  `timeout=(connect, read)`.
- Bound the total time of an operation, including retries, so a caller (a request handler, a scheduler tick) never
  waits longer than it can afford.
- Threads waiting on events, queues or locks also use timeouts, and the code handles the timeout case explicitly.

## 3. Retries

- Retry only failures that are **transient and safe to repeat**: connection errors, timeouts on reads, HTTP 429, 502,
  503, 504. Never retry 400, 401, 403, 404, validation errors or programming errors.
- Retry only **idempotent** operations (reads, or writes protected by an idempotency key or client order id). A
  timed-out write has an unknown outcome: check the real state before trying again.
- Use capped exponential backoff with jitter (for example 0.5 s, 1 s, 2 s… up to a cap, each multiplied by a random
  factor), a small attempt limit and a total time limit. Honour `Retry-After` on 429/503.
- Log each retry at warning level with the operation, attempt number and reason; never log secrets, tokens or full
  signed URLs. Count retries so a rising rate is visible.
- Keep retry policy in one helper, not copied into every call site.

## 4. Rate limits and degradation

- Respect documented rate limits proactively (spacing requests, batching) instead of relying on 429 responses.
- When a dependency is down, fail fast after the limit and show stale data **labelled as stale with its timestamp**,
  or no data with a clear status. Never present cached or default values as fresh.
- A circuit breaker (stop calling a failing dependency for a cool-down period) is worth it only when repeated calls
  cause harm or cost; keep its state visible and its reset explicit.
- Isolate failures: one failing instrument, feed or job must not stop the others or crash the process. Catch at the
  loop boundary, record the error, continue.

## 5. Background loops and threads

- Long-running loops catch and log exceptions per iteration, sleep with backoff after errors and stop cleanly on
  shutdown (a stop event, not a killed thread).
- Shared connections and sessions used from several threads must be thread-safe or protected by a lock.

## 6. Testing

- Test retry behaviour without real waits or real network: inject the sleep function and the clock, mock the client.
- Cover: success first try, transient failure then success, permanent failure (no retry), attempts exhausted, total
  time exceeded, `Retry-After` honoured, and a timed-out write that is checked instead of repeated.

## Trading-app notes

- The backend uses `requests` sessions with explicit timeouts for market data. Keep timeouts on every new call.
- Market-data failures must surface as stale or missing data (`market-data-quality`), never as silently reused prices.
- Order calls follow `order-lifecycle-safety`: an order whose status is unknown after a timeout is reconciled with the
  exchange before any retry. Retries must never bypass the central risk engine.

## Official references

- [requests: timeouts](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts)
- [urllib3 Retry](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry)
- [HTTP 429 and Retry-After (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After)
