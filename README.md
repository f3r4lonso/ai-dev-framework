# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs) and
[OpenAI Codex CLI](https://developers.openai.com/codex/cli): one set of shared agents, skills and instructions,
with a native adapter for each client. Architecture, compatibility matrix and maintenance:
[docs/ai-architecture.md](docs/ai-architecture.md).

## Start here

1. **Pick a client and sign in with your own account:** [Claude Code CLI](clients/claude-code-cli/README.md)
   or [Codex CLI](clients/codex-cli/README.md). Install, authentication and troubleshooting for both:
   [docs/onboarding.md](docs/onboarding.md).
2. **Enable the secret guard once per clone:** `git config core.hooksPath .githooks` ([SECURITY.md](SECURITY.md)).
3. **Find what to use:** the [Workshop](docs/workshop.md) lists every agent, skill and task prompt and
   explains how to choose one.

Clone into `C:\Users\<you>\workshop\infra` and start your client there (Claude Code: `claude --add-dir clients`), or from an application
repository as described in its client guide.

## Contents
- `AGENTS.md` — rules shared by all clients (Codex reads it; `CLAUDE.md` imports it).
- `CLAUDE.md` — `@AGENTS.md` plus Claude-only notes.
- `agents/` — 20 subagents by area: `ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`.
- `skills/` — 23 on-demand skills. Canonical for both clients.
- `clients/.codex/agents/` — Codex wrappers generated from `agents/` by `scripts/codex-adapter.py`. Do not edit.
- `clients/` — one guide per AI client: start-up, discovery, permissions, limits.
- `tasks/` — task prompts.
- `clients/.claude/` — local links to `agents/` and `skills/` so Claude Code finds them with `--add-dir clients`
  (created by `python scripts/codex-adapter.py link-claude`; not versioned).
- `docs/workshop.md`, `docs/catalogues/`, `docs/manuals/`, `docs/projects/` — Workshop index, catalogues, manuals
  and the new-project convention.
- `docs/inventory.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.
- `docs/` — architecture and compatibility, onboarding (accounts and authentication), reviews and handover reports.
- `SECURITY.md`, `.githooks/`, `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/` — security policy,
  secret scanning (local hook and CI) and the Codex adapter drift check.

Application projects live next to this folder, in `%USERPROFILE%\workshop\applications\`, as separate repositories; they are not part of this repo.

## Security
This repository holds no credentials: each contributor signs in with their own Claude, OpenAI, Git and GitHub
accounts. What must never be committed and what to do if a secret leaks: [SECURITY.md](SECURITY.md).

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
