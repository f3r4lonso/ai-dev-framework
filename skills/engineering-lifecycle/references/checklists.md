# Checklists

Use the sections that apply. Each item should end as done, not applicable, or an explicit open risk.

## Security and threat modeling

- Assets: what data, money or access is at stake; who could want it.
- Entry points and trust boundaries: user input, files, network, third-party APIs, AI tool calls.
- STRIDE pass per boundary: spoofing, tampering, repudiation, information disclosure, denial of service,
  elevation of privilege. Record the mitigation or accepted risk for each relevant threat.
- Input validation at boundaries; parameterized queries; output encoding; no `eval` of untrusted data.
- AuthN/AuthZ checked server-side; least privilege for tokens, service accounts and agent tools.
- Secrets only from the environment or a secret store; none in code, logs, prompts or test fixtures.
- Dependencies: license, maintenance, known vulnerabilities, install scripts reviewed before adding;
  versions pinned or locked.
- Security testing (scanners, fuzzing, penetration tests) only on systems you own or are authorized to test.

## Testing

- Each acceptance criterion maps to at least one test or a documented manual check.
- Unit tests for logic and edge cases (empty, boundary, invalid, concurrent, time zones, rounding).
- Integration or contract tests where components or services meet.
- Regression test for every fixed bug (fails before the fix, passes after).
- UI: keyboard and screen-reader paths, responsive widths, error and loading states.
- Performance: measure before optimizing; record baseline and result with the same workload.
- Tests are deterministic: fixed seeds, frozen time, no live network in unit tests.

## Debugging

- Reproduce first; write the smallest reproduction.
- Read the full error and stack trace; check recent changes (`git log`, `git diff`).
- Form one hypothesis at a time and test it; change one thing at a time.
- Fix the root cause, add a regression test, then remove temporary logging.

## CI/CD and environments

- CI runs lint, type checks, tests and secret scanning on every push and pull request.
- Third-party CI actions pinned to a commit SHA; workflow permissions minimal.
- Environments separated (local, test, production) with separate credentials.
- Infrastructure as code reviewed like application code; plans reviewed before apply.
- Deploys are repeatable, reversible and need human approval for production.

## Observability and operations

- Structured logs with request or correlation IDs; no secrets or personal data in logs.
- Metrics for rate, errors and duration of key operations; alerts on symptoms users feel.
- Health checks and timeouts on every external call; retries with backoff and limits.
- Runbook: how to diagnose, mitigate, roll back, and whom to notify.
- After an incident: timeline, root cause, follow-up actions with owners.

## Release and maintenance

- Version and changelog updated; breaking changes and migrations documented.
- Rollback plan tested or at least written.
- Documentation and onboarding updated with the change.
- Deprecations announced with a removal date; dead code and stale docs removed.
