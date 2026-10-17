# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs) and
[OpenAI Codex CLI](https://developers.openai.com/codex/cli): one set of shared agents, skills and instructions,
with a native adapter for each client. Architecture, compatibility matrix and maintenance:
[docs/ai-architecture.md](docs/ai-architecture.md).

## Start here

1. **Pick a client and sign in with your own account:** [Claude Code CLI](ai-infra/clients/claude-code-cli/README.md)
   or [Codex CLI](ai-infra/clients/codex-cli/README.md). Install, authentication and troubleshooting for both:
   [docs/onboarding.md](docs/onboarding.md).
2. **Enable the secret guard once per clone:** `git config core.hooksPath .githooks` ([SECURITY.md](SECURITY.md)).
3. **Find what to use:** the [Workshop](ai-infra/workshop/README.md) lists every agent, skill and task prompt and
   explains how to choose one.

Clone into the workspace root (e.g. `C:\Users\<you>\Repos`) and start your client there, or from an application
repository as described in its client guide.

## Contents
- `AGENTS.md` — workspace-wide rules shared by all clients (Codex reads it; `CLAUDE.md` imports it).
- `CLAUDE.md` — `@AGENTS.md` plus Claude-only notes.
- `.claude/agents/` — 20 subagents by area: `ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`.
- `.claude/skills/` — 23 on-demand skills. Canonical for both clients.
- `.codex/agents/` — Codex wrappers generated from `.claude/agents/` by `ai-infra/scripts/codex-adapter.py`. Do not edit.
- `ai-infra/clients/` — one guide per AI client: start-up, discovery, permissions, limits.
- `ai-infra/workshop/` — catalogues, task prompts, manuals and the new-project convention.
- `ai-infra/README.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `ai-infra/THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.
- `docs/` — architecture and compatibility, onboarding (accounts and authentication), reviews and handover reports.
- `SECURITY.md`, `.githooks/`, `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/` — security policy,
  secret scanning (local hook and CI) and the Codex adapter drift check.

Application projects live in `projects/applications/` as separate repositories and are not part of this repo.

## Security
This repository holds no credentials: each contributor signs in with their own Claude, OpenAI, Git and GitHub
accounts. What must never be committed and what to do if a secret leaks: [SECURITY.md](SECURITY.md).

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
