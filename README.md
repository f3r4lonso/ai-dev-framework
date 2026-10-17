# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs):
shared agents, skills and instructions used across my application projects.

## Contents
- `CLAUDE.md` — workspace-wide rules loaded by Claude Code.
- `.claude/agents/` — subagents by area: `ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`.
- `.claude/skills/` — on-demand skills (UI/UX, frontend, backend, trading).
- `ai-infra/README.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `ai-infra/THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.

Application projects live in `Applications/` as separate repositories and are not part of this repo.

## Usage
Clone into the workspace root (e.g. `C:\Users\<you>\Repos`) and start Claude Code there, or from an application
repo with `claude --add-dir <workspace root>` so the shared agents and skills load.

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
