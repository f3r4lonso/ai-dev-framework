# Contributor guide

How to add, change or retire shared resources without breaking either client. Architecture and the reasons behind
these rules: [ai-architecture.md](../../docs/ai-architecture.md). Security rules: [SECURITY.md](../../SECURITY.md).

## 1. Rules that always apply

1. **One canonical location.** Edit only canonical files: `AGENTS.md`, `CLAUDE.md`, `agents/`,
   `skills/`, `docs/`, and this Workshop. Never edit `clients/.codex/agents/` or `clients/.agents/skills/` by hand
   (they are generated), and never copy an agent or skill body anywhere else.
2. **Whitelist.** `.gitignore` versions only listed paths. A new top-level folder is silently ignored until you add a `!/<path>/` line. Check with `git status` and
   `git check-ignore -v <path>`.
3. **Public repository.** No credentials, absolute user paths, usernames, account names or private URLs in any
   versioned file. Write `%USERPROFILE%` or `<you>`.
4. **Register.** Every added, changed or retired agent or skill gets a line in [docs/inventory.md](../../docs/inventory.md)
   and a row in the matching [catalogue](../catalogues/agents.md). When adopted content is copied or adapted
   from a third party, also record its license and required notice in the root `THIRD_PARTY_NOTICES.md`.
5. **Third-party content** is untrusted: research is allowed, but review source, license, security, and fit before adopting it; never run its installers.
6. **Keep `AGENTS.md` short**: it is loaded into every supported client session.

## 2. Add or change an agent or skill

Create one only for a material, repeatable benefit. Research may compare broadly with public alternatives,
including where Workshop resources already exist; existing coverage is a baseline, not a search limit.
Check both catalogues and ask `ai-environment-auditor` to confirm the need and overlap before adding a shared resource.
When orchestrating this work, `task-resource-scout` must consult the auditor before installing a new shared agent or skill.
Document these fields in the definition or its proposal:

| Field | Content |
|---|---|
| Mission | One sentence |
| Trigger | When to invoke it (this becomes the `description`) |
| Inputs / outputs | What it needs, what it returns |
| Tool access | Minimal `tools:` list (Claude enforces it; Codex does not, so state limits in the body too) |
| Constraints and safety | What it must never do |
| Dependencies | Skills, files, other agents |
| Verification | How to tell it works |
| Scope | Shared or client-specific |
| Invocation | Claude Code: by name, `@agent-<name>`, `/<skill>`; Codex: "use the `<name>` agent", `$<skill>` |

Steps:
1. Agent: `agents/<area>/<name>.md` with `name`, `description`, `tools` frontmatter.
   Skill: `skills/<name>/SKILL.md` with `name`, `description`; long material in `references/`.
2. Agent added, renamed or frontmatter edited: `python scripts/codex-adapter.py agents`, then
   `python scripts/codex-adapter.py agents --check` (CI fails on drift). Use `python3` in Bash.
3. Skill added: `python scripts/codex-adapter.py link-skills` (and `--user` if you use it). A removed skill
   leaves a dangling link: delete it from `clients/.agents/skills/`.
4. Register (rule 4) and update counts in `README.md` and `docs/ai-architecture.md` if they changed.
5. Verify in Claude Code: restart `claude` in the repository root, run `/agents` (agents load only at session start).
   Verify in Codex if available: [codex-cli §5](../../clients/codex-cli/README.md#5-verify-manual-required-before-claiming-support).

## 3. Retire an agent or skill

Delete only after every reference is updated (`grep -rn <name>` excluding `vendor/` and `projects/`).
Regenerate the Codex adapter, and record the reason under "Retired" in [docs/inventory.md](../../docs/inventory.md).

## 4. Add a task prompt

Put it under [`../tasks/`](../../tasks/README.md): use `projects/<project-id>/` for project work or
`common/<category>/` for reusable work such as agents and prompts. Follow the task file convention, add a row to
the [task catalogue](../catalogues/tasks.md), and have `prompt-reviewer` review it before the first run. When a
task is replaced, mark the old one `Status: superseded by <file>` instead of deleting it.

## 5. Add a client or provider

Follow the procedure in [ai-architecture.md §8](../../docs/ai-architecture.md#8-adding-another-provider-procedure-not-implemented):
a new `clients/<client-id>/README.md` (start-up, discovery, permissions, limits), its install and
authentication section in `docs/onboarding.md`, an adapter generated from the canonical files, and a new column in
the compatibility matrix with evidence labels.

## 6. Start a new project

See the [new-project convention](../projects/README.md).

## 7. Before you commit

- `python scripts/codex-adapter.py agents --check` passes.
- `git status`: no tracked file became ignored; every new file shows up.
- No user paths or account names: `grep -rnE "C:\\\\Users\\\\[^<%]|/Users/[a-z]" --exclude-dir=vendor --exclude-dir=projects .`
- Secret guard on (`git config core.hooksPath .githooks`); commits and pushes only with the maintainer's approval.
