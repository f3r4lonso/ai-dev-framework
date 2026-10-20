---
name: game-ui-ux
description: Plan or review engine-neutral game HUDs and menus, touch interaction, screen stacks, safe areas, accessibility and localization. Use for game UI flows and device layout validation, within the current task's authorization.
---

# Game UI/UX

Workshop adaptation, 2026-10-19: rewritten from the game-ui-ux skill in
gamedev-skills/awesome-gamedev-agent-skills at `cf44d99a0315dabff6ac6f407c6ccc026190f16c`.
Copyright 2026 Abhishek Barali and the awesome-gamedev-agent-skills contributors.
Apache-2.0; [license](LICENSE.txt), [notice](NOTICE.txt), [provenance](../../docs/inventory.md).
Modified: no engine-specific code, router or sibling-skill dependencies; added planning and input-safety boundaries.

## Method

1. Read confirmed platform, orientation, input and player requirements; leave unresolved choices explicit.
2. Specify flexible layout, aspect-ratio handling and safe-area behavior. Separate screen pixels from UI coordinates.
3. Define screens and overlays, input ownership, back behavior and focus restoration.
4. Decouple presentation from game-state updates. Plan readable feedback and localized layouts.
5. Apply the on-demand [review checklist](references/review-checklist.md).

Deliver a flow map, layout/input constraints and device test cases with observable outcomes.
In planning, return proposals only. Implementation, asset creation, packages and device execution require an
authorized implementation task. This skill grants no tool permissions and requires no scripts or dependencies.
Verify actual engine APIs against its selected version; report unperformed device tests as not run.
