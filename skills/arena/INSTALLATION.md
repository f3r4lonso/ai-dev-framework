# Arena adoption record

Canonical shared skill: infra/skills/arena/, migrated 2026-10-21 at the owner's request.
Source: https://github.com/Jakeschincariol/arena-skill, revision
`df07b8e518e10cdecd8cd7712d9958b6f396250e`, MIT copyright 2026 Jake Schincariol.

Original instructions: references/upstream-skill.md. Original templates are extracted into
references/prompt-templates.md. bracket.py, rubric.md, strategies.json and LICENSE retain
upstream contents. Workshop rewrote the entrypoint for client-native delegation, actual
session concurrency, bounded failures and instruction-only bookkeeping. No upstream script
or tournament was executed. Live client discovery and tournament behavior remain unverified.

Install/update with `python infra/scripts/sync-resources.py` from the Workshop, or use
`--project <root>` for one project and `--user` for the OS user's global folders.
Do not edit generated copies. See infra/docs/manuals/shared-resource-installation.md.
