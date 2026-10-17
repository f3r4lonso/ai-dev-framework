# Projects

Each application is its **own git repository**, kept on disk under `projects/applications/<project-id>/`. That
folder is outside the whitelist and is never versioned in this framework repository. What this repository holds
is one public entry page per project, here.

| Project | Role | Entry |
|---|---|---|
| Trading-app (AutoTrade) | Demonstration project: verifies that the shared infrastructure works on a real codebase | [trading-app/](trading-app/README.md) |

## Start a new project

1. **Pick an id:** kebab-case, lowercase, English (e.g. `invoice-parser`).
2. **Create the repository** at `projects/applications/<project-id>/` and run `git init` there. Never commit it from
   the workspace root.
3. **Project rules:** add a short `CLAUDE.md` (and an `AGENTS.md` for Codex, or a `CLAUDE.md` that contains only
   `@AGENTS.md` plus Claude notes) at the project root: purpose, stage, commands, constraints. Project rules win
   over workspace rules except security and privacy.
4. **Load the shared resources** when you work in the project:
   - Claude Code: `claude --add-dir "$env:USERPROFILE\Repos"` (PowerShell) or `claude --add-dir ~/Repos` (Bash);
     a small launcher script in the project can do this.
   - Codex CLI: shared skills need `codex-adapter.py link-skills --user`; shared agents are only available when
     Codex starts in the workspace root ([codex-cli §2](../../clients/codex-cli/README.md#2-start-up-directory)).
5. **Project-specific agents or skills** stay in the project's own `.claude/` folder. Move one into the shared
   `.claude/` only when a second project needs it, following the [contributor guide](../manuals/contributor-guide.md).
6. **Entry page:** create `ai-infra/workshop/projects/<project-id>/README.md` from the template below, add a row to the
   table above, and add nothing else from the project to this repository.

## Entry page template

```markdown
# <Project name>

- **Purpose:** one or two sentences.
- **Stage:** idea / local POC / local MVP / pre-production / production.
- **Repository:** <public URL> | private repository
- **Start a session:** which client, from which folder, with which flags.
- **Shared resources it uses:** links to catalogue rows (agents, skills, tasks).
- **Project-specific resources:** "in the project repository" (do not list private file names).
```

Never put private material, private repository URLs, account names, absolute user paths or file listings from a
project in an entry page: this repository is public.
