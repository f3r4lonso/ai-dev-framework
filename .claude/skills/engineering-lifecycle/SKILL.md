---
name: engineering-lifecycle
description: Generic software engineering workflow and quality gates for any project (not trading-specific). Use when starting a non-trivial feature or change, writing requirements and acceptance criteria, planning tasks, recording an architecture decision (ADR), threat modeling, preparing CI/CD, observability or a release, or checking that work is really done before reporting it.
---

# Engineering lifecycle

Portable skill shared by Claude Code and Codex CLI. Use the stage that fits the task; do not run every
stage for a small change. Domain skills (trading, UI, API, Python, React) take precedence for their area;
this skill fills the generic gaps around them.

## Stages and gates

| Stage | Do | Gate before moving on |
|---|---|---|
| 1. Clarify | Restate the goal, users, constraints, non-goals. Ask only questions that change scope, risk or architecture. | Acceptance criteria written and testable |
| 2. Plan | Break into small, reversible steps; name files/areas touched, risks, rollback. | Each step has a verification |
| 3. Decide | For choices that are costly to reverse (data model, framework, public API, security boundary) write an ADR. | ADR accepted or decision explicitly deferred |
| 4. Build | Smallest change that meets the criteria; match surrounding code style; no unrelated refactors. | Builds, lints, existing tests pass |
| 5. Verify | Add or run tests at the right level (unit, integration, contract, e2e, a11y, performance, security). | Every acceptance criterion has evidence |
| 6. Review | Self-review the diff for correctness, security, secrets, error handling, naming, dead code. | No open blocker findings |
| 7. Ship | CI green, changelog/release notes, migration and rollback steps, monitoring in place. | Human approval for any deploy, push or publish |
| 8. Operate | Logs, metrics, alerts, runbook; incidents get a blameless root-cause note. | Owner and alert route known |

Templates for stages 1–3 and the report: `references/templates.md`.
Checklists for security, testing, operations and release: `references/checklists.md`.
Read a reference file only when the stage needs it.

## Rules that always apply

- Evidence over claims: never report a test, build or check as passed unless it ran; say "not run" and why.
- Label statements as verified, inferred or unknown when the reader could mistake one for another.
- Secrets: reference environment variable names only; never print, write or commit values.
- Ask before destructive, external or costly actions (deletes, history rewrites, pushes, deploys, paid API calls).
- Delegate to a subagent only when the task is large or parallel enough to repay the extra context.
- Keep summaries to decisions, evidence, open questions and next steps.
