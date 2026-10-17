# Workshop

The client-neutral navigation layer of this framework: what exists, how to choose it and how to add to it. It holds
indexes, catalogues, task prompts and manuals only. Agent and skill bodies stay in `.claude/`; architecture,
security and onboarding stay in `docs/`. No AI client loads this folder automatically: people read it, or ask
their client to open a file here.

| Folder | Contents |
|---|---|
| [tasks/](tasks/README.md) | Task prompts, and how to choose a client and a task |
| [catalogues/](catalogues/agents.md) | [Agents](catalogues/agents.md), [skills](catalogues/skills.md), [tasks](catalogues/tasks.md): one row each, linked to the canonical file |
| [manuals/](manuals/contributor-guide.md) | Contributor guide: add, change or retire resources, tasks, clients and projects |
| [projects/](projects/README.md) | New-project convention and one entry page per project (e.g. the [Trading-app demonstration](projects/trading-app/README.md)) |

## Quick start

1. Set up one client: [Claude Code CLI](../clients/claude-code-cli/README.md) or [Codex CLI](../clients/codex-cli/README.md).
2. Start it in the repository root and run the client guide's verification steps.
3. Pick a task, agent or skill: [tasks/README.md](tasks/README.md).
4. Work on a project through its entry page in [projects/](projects/README.md).
5. Add something new: [contributor guide](manuals/contributor-guide.md).
