@AGENTS.md

## Claude Code only

- Claude Code discovers the shared agents and skills through the links in `clients/.claude/` (create them with
  `python scripts/codex-adapter.py link-claude`). In this repository start Claude with `claude --add-dir clients`;
  inside a project repo they load only when Claude is started with
  `claude --add-dir %USERPROFILE%\workshop\infra\clients` (Trading-app: its `start-claude.bat`).
- `clients/.codex/agents/` and `clients/.agents/skills/` are generated Codex adapters: never edit them by hand.
