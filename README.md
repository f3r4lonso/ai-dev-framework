# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs),
[OpenAI Codex CLI](https://developers.openai.com/codex/cli), and
[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): one set of shared agents, skills and instructions,
with client-specific support documented for each. DeepSeek Harness is an experimental, unaudited developer preview.
Architecture, compatibility matrix and maintenance:
[docs/ai-architecture.md](docs/ai-architecture.md).

## Start here

1. **Pick a client and use your own account:** [Claude Code CLI](clients/claude-code-cli/README.md),
   [Codex CLI](clients/codex-cli/README.md), or [DeepSeek Harness](clients/deepseek-harness/README.md).
   Install, authentication and troubleshooting:
   [docs/onboarding.md](docs/onboarding.md).
2. **Enable the secret guard once per clone:** `git config core.hooksPath .githooks` ([SECURITY.md](SECURITY.md)).
3. **Install across clients:** follow the [shared installation standard](docs/manuals/shared-resource-installation.md); `python scripts/sync-resources.py --user` installs native copies for all supported coding clients. Review limits for manual-use clients.
4. **Find what to use:** the [Workshop](docs/workshop.md) lists every agent, skill and task prompt and
   explains how to choose one.

Clone into `C:\Users\<you>\workshop\infra` and start your client there (Claude Code loads everything from the `workshop` plugin: `clients/claude-code-cli/README.md`), or from an application
repository as described in its client guide.

## Contents
- `AGENTS.md` — rules shared by all clients (Codex reads it; `CLAUDE.md` imports it).
- `CLAUDE.md` — `@AGENTS.md` plus Claude-only notes.
- `agents/` — 26 shared subagents by area: `ai`, `backend`, `creative` (including game art/music direction), `devops`, `frontend`, `game-development`, `quality`, `trading`, `ui`, `ux`.
- `skills/` — 33 on-demand skills, including Arena and i-have-adhd. Canonical for all clients; native and manual-use paths are documented in the shared installation standard.
- `clients/.codex/agents/` — Codex wrappers generated from `agents/` by `scripts/codex-adapter.py`. Do not edit.
- `clients/` — one guide per AI client: start-up, discovery, permissions, limits.
- `tasks/` — task prompts.
- `.claude-plugin/` — Claude Code plugin and local marketplace manifests; Claude reads `agents/` and `skills/` in
  place from this folder.
- `docs/workshop.md`, `docs/catalogues/`, `docs/manuals/`, `docs/projects/` — Workshop index, catalogues, manuals
  and the new-project convention.
- `docs/inventory.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.
- `docs/` — architecture and compatibility, onboarding (accounts and authentication), reviews and handover reports.
- `SECURITY.md`, `.githooks/`, `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/` — security policy,
  secret scanning (local hook and CI) and the Codex adapter drift check.

Application projects live next to this folder, in `%USERPROFILE%\workshop\applications\`, as separate repositories; they are not part of this repo.

## Security
This repository holds no credentials: each contributor authenticates to their chosen AI clients, Git and
GitHub with their own accounts. What must never be committed and what to do if a secret leaks:
[SECURITY.md](SECURITY.md).

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
