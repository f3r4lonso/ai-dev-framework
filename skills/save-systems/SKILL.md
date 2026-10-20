---
name: save-systems
description: Plan or review engine-neutral game persistence, schema migration, save validation, autosave, interrupted-session recovery and compatibility. Use for game-state save/load decisions and recovery acceptance criteria.
---

# Save systems

Workshop adaptation, 2026-10-19: rewritten from the save-systems skill in
gamedev-skills/awesome-gamedev-agent-skills at `cf44d99a0315dabff6ac6f407c6ccc026190f16c`.
Copyright 2026 Abhishek Barali and the awesome-gamedev-agent-skills contributors.
Apache-2.0; [license](LICENSE.txt), [notice](NOTICE.txt), [provenance](../../docs/inventory.md).
Modified: removed engine examples and external skill dependencies; strengthened recovery and trust boundaries.

## Method

1. Define authoritative data and schema/content versions; persist plain state rather than engine objects.
2. Select a format and storage mechanism proportionate to the requirements.
3. Plan validated, sequential migrations and bounded input parsing before constructing game objects.
4. Specify safe save boundaries, separate manual/autosave retention and known-good recovery data.
5. Use the [failure matrix](references/failure-matrix.md) to define evidence for recovery claims.

Deliver a persistence contract, compatibility policy, recovery behavior and future test cases.
Planning produces recommendations only; this skill neither authorizes writing saves nor installs tools.
Check engine/platform guarantees before claiming atomicity or durability. Local save files cannot establish
online purchase entitlement or authoritative competitive state. State unperformed tests as not run.
