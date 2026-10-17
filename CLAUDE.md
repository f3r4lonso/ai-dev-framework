@AGENTS.md

## Claude Code only

- Inside a project repo the shared agents and skills load only when Claude is started with
  `claude --add-dir %USERPROFILE%\Repos` (Trading-app: `projects/applications/Trading-app/start-claude.bat`).
- `.codex/agents/` and `.agents/skills/` are generated Codex adapters: never edit them by hand.
