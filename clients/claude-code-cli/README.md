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

## 2. Install the `workshop` plugin (once per machine)

This repository is a Claude Code plugin and a local marketplace (`.claude-plugin/`). Claude reads the plugin in
place from this folder: no copies, no links, edits apply at the next session start or `/reload-plugins`
(Observed, Claude Code 2.1.303, 2026-10-19).

```text
claude plugin marketplace add "%USERPROFILE%\workshop\infra"
claude plugin install workshop@workshop-local --scope user
```

After that, every shared agent and skill loads in **every folder** (workshop root, `infra`, any application) with a
plain `claude`. Names carry the plugin prefix: agents `workshop:<name>`, skills `/workshop:<name>`. Atlas:
`claude --agent workshop:atlas-project-planner`. If you move `infra`, remove and re-add the marketplace.
Project rules still come from each folder's `CLAUDE.md`.

## 3. Discovery

| Resource | Where Claude Code looks | When | Status |
|---|---|---|---|
| Rules | `CLAUDE.md` from the working directory up to the repo root; this repo's `CLAUDE.md` imports `AGENTS.md` | session start | Observed |
| Agents | `workshop` plugin: the files listed in `.claude-plugin/plugin.json` (rebuilt by `python scripts/codex-adapter.py agents`) | session start or `/reload-plugins` | 25 agents observed (2026-10-19; 26 shared exist on 2026-10-20) from `applications\Trading-app` and the workshop root |
| Skills | `workshop` plugin: `skills/<name>/SKILL.md` | session start or `/reload-plugins` | 29 skills observed (2026-10-19; 31 exist on 2026-10-20) |
| Task prompts | not discovered; open them by path from [the Workshop](../../tasks/README.md) | on request | n/a |
| Catalogues, manuals | not discovered; read on request | on request | n/a |
| Hooks, commands, MCP | none are shipped by this repo | — | — |

Claude Code reads `AGENTS.md` on its own only when no `CLAUDE.md` exists, so the `@AGENTS.md` import is
required (Documented).

## 4. Invoking shared resources

- **Agent:** ask by name ("Use the code-reviewer agent to review this branch"), type `@agent-<name>` to force it,
  or let Claude delegate when a request matches the description. `/agents` lists and manages them.
- **Skill:** type `/<skill-name>` or let Claude load it when the request matches its description.
- **Task prompt:** "Run the task in `tasks/projects/<project>/<file>.md`" or
  "`tasks/common/<category>/<file>.md`" (check its status in the
  [task catalogue](../../docs/catalogues/tasks.md) first).
- Built-in agents (`Explore`, `Plan`, `general-purpose`, `claude-code-guide`) are always available.

## 5. Verify (first verified shared resource)

1. `/status`: your own account and the expected login method.
2. `/memory`: lists the workspace `CLAUDE.md` (and through it `AGENTS.md`).
3. `claude plugin list` shows `workshop@workshop-local` enabled and read from this folder; `/agents` lists
   `workshop:code-reviewer`, `workshop:prompt-reviewer`, and so on.
4. Ask: "Use the workshop:prompt-reviewer agent in quick mode on `tasks/README.md`." It should return a
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

[Onboarding troubleshooting](../../docs/onboarding.md#troubleshooting). Most common: agents missing → the `workshop`
plugin is not installed or is disabled (`claude plugin list`), the agent is not in the plugin's `agents` list (run
`python scripts/codex-adapter.py agents`), its frontmatter does not parse (`claude plugin validate .`), or it was
added after the session started (`/reload-plugins`).
