# Trading-app (AutoTrade) — demonstration project

- **Purpose:** a local trading laboratory (research, backtesting, risk engine, paper trading; real trading
  disabled). In this framework it is the **demonstration project** used to verify that the shared infrastructure
  works on a real codebase.
- **Stage:** local POC / MVP (Inference from its agents and skills: backtesting and paper trading, demo execution
  planned). Functionality is frozen for now; only infrastructure, naming and English changes.
- **Repository:** private repository, on disk at `projects/applications/Trading-app/`.
- **Start a session:**
  - Claude Code: run `start-claude.bat` in the project root (it adds the workspace root with `--add-dir`).
  - Codex CLI: start in the project root after `codex-adapter.py link-skills --user`; shared skills load, shared
    agents do not (Unverified, see [codex-cli §2](../../../clients/codex-cli/README.md#2-start-up-directory)).
- **Shared resources it uses:** the 8 trading agents in the [agent catalogue](../../catalogues/agents.md) and the
  10 trading skills in the [skill catalogue](../../catalogues/skills.md), plus `code-reviewer`, `python-pro`,
  `frontend-developer`, `engineering-lifecycle` and the UI/UX skills.
- **Project-specific resources:** in the project repository.

## Verification checklist (read-only; changes nothing in the project)

Run in a new session and record pass/fail with the date in
[ai-architecture.md §10](../../../../docs/ai-architecture.md#10-validation-status-2026-10-17).

| # | Check | Claude Code | Codex CLI |
|---|---|---|---|
| 1 | Project rules load | `/memory` lists the project `CLAUDE.md` | ask "List the instruction sources you loaded" |
| 2 | Shared agents visible | `/agents` lists the trading agents | not expected (see above) |
| 3 | Shared skills visible | type `/` and find `risk-management` | `/skills` lists `risk-management` |
| 4 | A read-only agent runs | "Use the backtesting-auditor agent to list what it would check for the latest backtest; do not edit anything" | ask the same with `codex --sandbox read-only` |
| 5 | Project stays unchanged | `git status` in the project shows nothing new | same |
