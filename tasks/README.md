# Tasks: choosing a client, a task and the right resources

A **task prompt** is a self-contained brief for a larger piece of work (scope, approvals, workflow, acceptance
checklist, report). Agents and skills are the tools a task uses. All task prompts are listed with their status in
the [task catalogue](../docs/catalogues/tasks.md).

## 1. Choose a client

| If you … | Use | Guide |
|---|---|---|
| have a Claude Pro/Max/Team/Enterprise plan or Console account | Claude Code CLI | [claude-code-cli](../clients/claude-code-cli/README.md) |
| have a ChatGPT plan or OpenAI API key | Codex CLI | [codex-cli](../clients/codex-cli/README.md) |
| need per-agent tool limits enforced (read-only reviewers, scoped editors) | Claude Code | Codex does not enforce them |
| want to verify the infrastructure on a real project | either, on the [Trading-app demonstration](../docs/projects/trading-app/README.md) | |

Both clients read the same rules (`AGENTS.md`), skills and agents. Support status per resource:
[compatibility matrix](../docs/ai-architecture.md#4-compatibility-matrix).

## 2. Choose a task

1. Open the [task catalogue](../docs/catalogues/tasks.md) and pick an **active** task. Never run a superseded one.
2. Read its scope and approval gates before starting: a task stops at each gate and waits for you.
3. Start your client in the folder the task names (usually the repository root) and say:
   "Run the task in `tasks/<file>.md`."
4. No task fits? Describe the goal in plain words. For non-trivial work the client follows the
   `engineering-lifecycle` skill (clarify → plan → build → verify → report).

## 3. Find agents and skills

- [Agent catalogue](../docs/catalogues/agents.md): who does what, and whether it can edit files.
- [Skill catalogue](../docs/catalogues/skills.md): checklists and know-how loaded on demand.
- Rule of thumb: a **skill** when you want the current session to follow a method; an **agent** when you want an
  independent role (reviewer, auditor) or a scoped editor.

## 4. Recommend a new agent, skill or task

1. Check both catalogues first; most needs are covered by an existing agent plus a skill.
2. Ask the `ai-environment-auditor` agent (audit mode): "Is there a gap for <need>? Recommend keep, extend or new."
3. Propose a new one only for a material, repeatable gap. Write the proposal with the fields in the
   [contributor guide](../docs/manuals/contributor-guide.md#2-add-or-change-an-agent-or-skill).
4. A new task prompt goes in this folder with a `Status:` line (see the contributor guide) and a catalogue row.

## 5. Task file convention

- Name: kebab-case, English, `.md`. Line 3 (after the title) states `Status: active | completed (<date>) |
  superseded by <file>`.
- No absolute user paths, account names or private URLs (write `%USERPROFILE%` or `<you>`): this folder is public.
