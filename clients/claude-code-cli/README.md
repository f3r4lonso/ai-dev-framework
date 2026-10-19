# Client guide: Claude Code CLI

How Claude Code finds and uses this workspace's shared resources. Install, sign-in and credential storage are in
one place only: [onboarding §1](../../docs/onboarding.md#1-claude-code-cli).

Evidence labels: **Observed** (seen in the maintainer's environment, Claude Code 2.1.302, 2026-10-17),
**Documented** (official docs checked 2026-10-17, linked in onboarding and in
[ai-architecture.md](../../docs/ai-architecture.md)), **Unverified**.

## 1. From a fresh clone to a working session

1. Install Claude Code and sign in with **your own** account: [onboarding §1](../../docs/onboarding.md#1-claude-code-cli).
   - **Subscription vs API:** a Pro, Max, Team or Enterprise login bills your plan; a Claude Console login or an
     `ANTHROPIC_API_KEY` bills API usage. A stray `ANTHROPIC_API_KEY` overrides your subscription
     ([details](../../docs/onboarding.md#environment-variables-all-optional)).
   - **Check the active account:** inside Claude Code run `/status` (login method, organization, e-mail).
2. Enable the secret guard once: `git config core.hooksPath .githooks`.
3. Start Claude Code in the right folder (section 2).
4. Verify with section 5.

## 2. Start-up directory

| Where you work | Command | What loads |
|---|---|---|
| This repository (`%USERPROFILE%\workshop\infra`) | `claude --add-dir clients` | Shared rules, all agents and skills (Observed) |
| An application repo, Windows PowerShell | `claude --add-dir "$env:USERPROFILE\workshop\infra\clients"` | Project rules + shared agents and skills (Documented) |
| An application repo, Bash (Git Bash, macOS, Linux) | `claude --add-dir ~/workshop/infra/clients` | Same |
| Trading-app | `start-claude.bat` in the project root | Same; it adds `..\..\infra\clients` |

Without `--add-dir`, Claude Code inside a project repo stops at that repo's root and sees none of the shared
resources (Documented).

## 3. Discovery

| Resource | Where Claude Code looks | When | Status |
|---|---|---|---|
| Rules | `CLAUDE.md` from the working directory up to the repo root; this repo's `CLAUDE.md` imports `AGENTS.md` | session start | Observed |
| Agents | `.claude/agents/**` in the working directory tree, `~/.claude/agents/`, and `--add-dir` folders | **session start only** | 20 existing agents observed (including `prompt-reviewer`); new agent requires manual re-check |
| Skills | `.claude/skills/<name>/SKILL.md`, same locations | session start; new skills can appear live | Observed |
| Task prompts | not discovered; open them by path from [the Workshop](../../tasks/README.md) | on request | n/a |
| Catalogues, manuals | not discovered; read on request | on request | n/a |
| Hooks, commands, MCP | none are shipped by this repo | — | — |

Claude Code reads `AGENTS.md` on its own only when no `CLAUDE.md` exists, so the `@AGENTS.md` import is
required (Documented).

## 4. Invoking shared resources

- **Agent:** ask by name ("Use the code-reviewer agent to review this branch"), type `@agent-<name>` to force it,
  or let Claude delegate when a request matches the description. `/agents` lists and manages them.
- **Skill:** type `/<skill-name>` or let Claude load it when the request matches its description.
- **Task prompt:** "Run the task in `tasks/<file>.md`" (check its status in the
  [task catalogue](../../docs/catalogues/tasks.md) first).
- Built-in agents (`Explore`, `Plan`, `general-purpose`, `claude-code-guide`) are always available.

## 5. Verify (first verified shared resource)

1. `/status`: your own account and the expected login method.
2. `/memory`: lists the workspace `CLAUDE.md` (and through it `AGENTS.md`).
3. `/agents`: lists the shared agents (for example `code-reviewer`, `prompt-reviewer`, `product-idea-excavator`).
4. Ask: "Use the prompt-reviewer agent in quick mode on `tasks/README.md`." It should return a
   scored review and change no file.

## 6. Permissions

- Permission modes and allow/deny rules live in `settings.json` (shared) and `settings.local.json` (personal,
  ignored by git here). This repo ships neither (Observed).
- Agent `tools:` lists and `disallowedTools` **are enforced** per agent (Documented); read-only agents cannot edit.
- To block reading secret files, add `Read(...)` deny rules ([SECURITY.md](../../SECURITY.md#claude-code-safety-in-this-workspace)).

## 7. Limitations

- New or renamed agents appear only after a restart (`exit`, then `claude` again).
- Trading agents and skills assume the Trading-app root as the working directory.
- Claude-only features used here: agent `tools`/`model`/`color` fields, `${CLAUDE_SKILL_DIR}`, `@agent-` mentions,
  `--add-dir`. Codex equivalents: [compatibility matrix](../../docs/ai-architecture.md#4-compatibility-matrix).

## 8. Troubleshooting

[Onboarding troubleshooting](../../docs/onboarding.md#troubleshooting). Most common: agents missing → you started
outside the repository root without `--add-dir`, or the agent was added after the session started.
