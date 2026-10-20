# Workshop

The client-neutral navigation layer of this framework: what exists, how to choose it and how to add to it. It holds
indexes, catalogues, task prompts and manuals only. Agent and skill bodies stay in `agents/` and `skills/`; task prompts are
grouped in `tasks/projects/` and `tasks/common/`;
architecture, security and onboarding in `docs/`. No AI client loads this folder automatically: people read it, or ask
their client to open a file here.

| Folder | Contents |
|---|---|
| [tasks/](../tasks/README.md) | Task prompts, and how to choose a client and a task |
| [catalogues/](catalogues/agents.md) | [Agents](catalogues/agents.md), [skills](catalogues/skills.md), [tasks](catalogues/tasks.md): one row each, linked to the canonical file |
| [manuals/](manuals/contributor-guide.md) | Contributor guide: add, change or retire resources, tasks, clients and projects |
| [projects/](projects/README.md) | New-project convention and one entry page per project (e.g. the [Trading-app demonstration](projects/trading-app/README.md)) |

Language coverage review and proposed expansion: [current assessment](language-coverage-assessment.md) and [skills and agents roadmap](language-skills-and-agents-roadmap.md).

**Workshop AI** is a separate application that consumes this layer and does not replace it:
[product vision and requirements](workshop-ai-product-vision.md).

Research proposal for adding music creation with Suno: [Suno Workshop integration](suno-workshop-integration-research.md).

For videogames, start with the [game design and planning resources](catalogues/agents.md#game-design-and-planning):
`game-designer` develops the creative concept, `game-developer` researches technical choices, and the
`game-ui-ux` and `save-systems` skills support interface and persistence planning.

## Quick start

1. Set up one client: [Claude Code CLI](../clients/claude-code-cli/README.md),
   [Codex CLI](../clients/codex-cli/README.md), or
   [DeepSeek Harness](../clients/deepseek-harness/README.md) (experimental developer preview).
2. Start it in the intended repository or project directory and follow the client guide's verification steps.
3. Pick a task, agent or skill: [tasks/README.md](../tasks/README.md).
4. Work on a project through its entry page in [projects/](projects/README.md).
5. Add something new: [contributor guide](manuals/contributor-guide.md).
