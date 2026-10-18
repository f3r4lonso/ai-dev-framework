# AI engineering infrastructure: architecture and client compatibility

Principle: **share what is common; separate what is platform-specific.** This repository is the shared
infrastructure; application projects in `%USERPROFILE%\workshop\applications\` (next to this repository) are separate repositories and are never changed by it.

Vendor facts below were checked against official documentation on 2026-10-17. Evidence labels:
**Observed** (seen working in the maintainer's environment), **Documented** (official docs, not observed
locally), **Inference** (reasoned from evidence), **Proposed** (designed here, not yet validated),
**Unsupported/Unverified**.

The infrastructure separates four concerns: **AI clients** (`clients/`), **client-native resources**
(canonical `agents/` and `skills/`, linked into `clients/.claude/`; generated `clients/.codex/agents/`,
`clients/.agents/skills/`), the shared **Workshop** (`tasks/`, `docs/`) and **project
workspaces** (`..\applications\`, one public entry page each in `docs/projects/`).

## 1. Layers and source of truth

| Layer | Location | Source of truth | Read by |
|---|---|---|---|
| Shared rules | `AGENTS.md` | canonical | Codex directly; Claude through `@AGENTS.md` in `CLAUDE.md` |
| Claude-only rules | `CLAUDE.md` (below the import) | canonical | Claude Code |
| Agents | `agents/<area>/<name>.md` | canonical (body shared, frontmatter Claude-native) | Claude Code natively |
| Codex agent wrappers | `clients/.codex/agents/<name>.toml` | **generated**, versioned | Codex CLI |
| Skills | `skills/<name>/SKILL.md` (+ `references/`, `scripts/`) | canonical (Agent Skills format) | Claude Code natively |
| Codex skill links | `clients/.agents/skills/<name>` → `skills/<name>` | **generated locally**, not versioned | Codex CLI |
| Generator | `scripts/codex-adapter.py` | canonical | maintainer, CI (`adapter-check.yml`) |
| Inventory, licenses | `docs/inventory.md`, `THIRD_PARTY_NOTICES.md` | canonical | humans, auditor agent |
| Security, onboarding (install, auth, troubleshooting for every client) | `SECURITY.md`, `docs/onboarding.md` | canonical | humans |
| Client guides (start-up, discovery, permissions, limits) | `clients/<client-id>/README.md` | canonical; link to onboarding for install/auth | humans |
| Claude Code links | `clients/.claude/agents` → `agents/`, `clients/.claude/skills` → `skills/` | **generated locally** (`link-claude`), not versioned | Claude Code (`--add-dir clients`) |
| Workshop: task prompts, catalogues, manuals, project entries | `tasks/`, `docs/catalogues/`, `docs/manuals/`, `docs/projects/` | catalogues **link to** canonical files; no copied bodies | humans; clients on request |
| claude.ai Project prompts | `agents/personal-assistants/` | canonical | pasted into claude.ai Projects |

Nothing is copied by hand: a Codex wrapper is a short pointer to the canonical agent file plus a translation of
its Claude-only fields, and a Codex skill is a link to the canonical folder.

## 2. Directory tree

```text
workshop/                       workspace folder (not a repository)
├── infra/                      shared infrastructure repo (whitelist .gitignore) — work here
│   ├── AGENTS.md               shared rules (all clients)
│   ├── CLAUDE.md               @AGENTS.md + Claude-only notes
│   ├── README.md  SECURITY.md  THIRD_PARTY_NOTICES.md
│   ├── agents/<area>/          20 canonical agents
│   ├── agents/personal-assistants/   claude.ai Project prompts (no frontmatter; not loaded by any CLI)
│   ├── skills/<name>/          24 canonical skills
│   ├── tasks/                  task prompts
│   ├── clients/                claude-code-cli/README.md, codex-cli/README.md
│   │   ├── .claude/            local links agents → ../../agents, skills → ../../skills (ignored by git)
│   │   ├── .codex/agents/      generated Codex wrappers (20 .toml)
│   │   └── .agents/skills/     local links for Codex (ignored by git; created by the script)
│   ├── scripts/codex-adapter.py
│   ├── docs/                   ai-architecture.md (this file), inventory.md, onboarding.md, workshop.md,
│   │                           catalogues/, manuals/, projects/,
│   │                           prompt-engineering-review.md, ai-infrastructure-handover.md
│   ├── .githooks/ .github/ .gitleaks.toml .pre-commit-config.yaml   secret scan + adapter drift check
│   └── vendor/                 untrusted upstream copies (not versioned)
├── applications/<id>/          separate git repos (e.g. Trading-app), outside this repository
├── documents/
└── projects/
```

## 3. Instruction precedence

| | Claude Code (v2.1.302 observed) | Codex CLI |
|---|---|---|
| Global personal | `~/.claude/CLAUDE.md` | `~/.codex/AGENTS.override.md` or `AGENTS.md` (`CODEX_HOME`) |
| Workspace | `CLAUDE.md` → imports `AGENTS.md` (Observed: this session loads it) | `AGENTS.md`, from the git root down to the working directory; closer files come later and override (Documented) |
| Project | the project's own `CLAUDE.md`/`AGENTS.md` (project repo root) | the project's `AGENTS.md` (project repo root) |
| Limits | warnings for long files (Documented) | `project_doc_max_bytes`, default 32 KiB combined (Documented) |

Claude reads `AGENTS.md` by itself only when no `CLAUDE.md` exists on the path (default setting
`claude-md-or-agents-md`, Documented), so the explicit import is required here. Project rules win over
workspace rules except security and privacy rules (stated in `AGENTS.md`).

**Workspace isolation:** each application is its own git repo. Codex walks only up to that repo's root, and
Claude without `--add-dir` does the same, so workspace rules do not leak into a project unless you opt in.

## 4. Compatibility matrix

| Resource | Claude Code: discovery / invocation | Status | Codex CLI: discovery / invocation | Status |
|---|---|---|---|---|
| Shared rules | `CLAUDE.md` + `@AGENTS.md` import at session start | Observed | `AGENTS.md` at session start | Documented |
| 24 skills | `.claude/skills/` from cwd up to repo root, or `--add-dir`; `/skill-name` or automatic by description | Observed (new `engineering-lifecycle` picked up live) | `.agents/skills/` from cwd up to repo root, or `~/.agents/skills/`; `$skill-name`, `/skills`, or automatic | Documented; links Proposed (junctions on Windows not yet seen by Codex) |
| `ui-ux-pro-max` scripts | `${CLAUDE_SKILL_DIR}` expanded | Observed (variable documented) | variable not expanded; SKILL.md tells the model to substitute the skill folder | Proposed |
| Skill frontmatter extras (`allowed-tools`, `metadata`) | honored | Documented | `name`, `description` required; extras not documented | Unverified (expected to be ignored) |
| 20 agents | `.claude/agents/**` (and `--add-dir`); by name, `@agent-<name>`, automatic, `/agents` | Observed | `clients/.codex/agents/*.toml` in a **trusted** project; ask "use the `<name>` agent"; `/subagents` to switch threads | Documented format; wrappers Proposed (TOML parses, not run in Codex) |
| Agent tool limits (`tools`, `disallowedTools`) | enforced | Documented | **not enforceable per agent**; subagents inherit the parent sandbox and approvals; wrappers state the limit as an instruction | Unsupported → mitigated by instruction; run read-only roles with `--sandbox read-only` |
| Agent `model:` | honored | Documented | omitted; inherits parent model (or `[agents].default_subagent_model`) | Documented |
| Agent `skills:` preload | honored | Documented | wrapper tells the agent to read those skills | Proposed |
| Hooks | `settings.json` hooks | Documented (none used here) | `hooks.json` / `[hooks]`, must be trusted | Documented (none used here) |
| Permissions | permission modes, allow/deny rules in settings | Documented | `sandbox_mode` + `approval_policy`; project `.codex/` loads only when trusted | Documented |
| Non-interactive | `claude -p` | Documented | `codex exec` (read-only sandbox by default, `--json`, `--output-schema`) | Documented |
| Workshop (task prompts, catalogues, manuals) | not discovered; plain Markdown opened by path on request | Observed (this task was run from it) | same | Inference (plain files, no client feature needed) |
| claude.ai Project prompts | not loaded by Claude Code | — | not loaded by Codex | — |

Claude-only features kept out of the shared core: agent tool allow/deny lists, `model`/`color` fields,
`${CLAUDE_SKILL_DIR}`, `@agent-` mentions, `--add-dir` loading. Codex-only: `agents/openai.yaml` skill metadata,
`$skill` syntax, per-agent `model_reasoning_effort`. None are needed today.

## 5. How to use each client

Client-native folders live in `clients/` (`.claude/` links, `.codex/`, `.agents/`); canonical bodies stay in `agents/` and `skills/`.
Start-up directory, discovery, invocation, permissions, limits and verification steps per client:
[Claude Code CLI](../clients/claude-code-cli/README.md) · [Codex CLI](../clients/codex-cli/README.md).
Install and authentication: [onboarding.md](onboarding.md). Choosing a task or resource:
[Workshop tasks](../tasks/README.md).

## 6. Maintaining

Step-by-step procedures (add, change or retire an agent, skill, task, client or project; regenerate the Codex
adapter; register in the inventory; checks before committing):
[contributor guide](manuals/contributor-guide.md). Keep `AGENTS.md` short: it is loaded into
every session of both clients.

## 7. Token and cost strategy

Implemented: one short always-loaded rule file (about 2 KB for `AGENTS.md` + `CLAUDE.md`); skills and agents
load by description only (progressive disclosure), with long material in `references/`; the generic
`engineering-lifecycle` skill keeps its checklists out of the main file; agents are used only for distinct roles
(retired duplicates are listed in `docs/inventory.md`); a standard short work-report contract.
The Workshop, client guides and catalogues are never loaded automatically: they cost tokens only when a
person or task opens them (`AGENTS.md` gained one pointer line to them, about 150 bytes, 2026-10-17).

Not measured: no baseline exists, so no saving is claimed. To measure: run the same 3 tasks per client before and
after a change and compare `/context` and `/cost` (Claude Code) and the token usage shown by Codex
(`codex exec --json` emits `turn.completed` usage events). Model routing (cheaper models for search/review,
stronger for design) is set per agent in Claude (`model:`) and globally for Codex subagents via
`[agents].default_subagent_model`; local models are not configured.

## 8. Adding another provider (procedure, not implemented)

1. Read its official docs for instruction files, agents/skills, permissions, sandbox, auth, data retention.
2. Map: shared rules → its instruction file (prefer reading `AGENTS.md` or importing it); skills → its skill
   mechanism or a link to `skills/`; agents → its agent format, generated by a new subcommand of
   `codex-adapter.py` (or a sibling script) from `agents/`.
3. Add `clients/<client-id>/README.md` (start-up, discovery, permissions, limits) and its install and
   authentication section in `docs/onboarding.md`. Put provider configuration in its own folder; never share credentials; add its auth/config files to
   `.gitignore`, `.gitleaks.toml` checks and `SECURITY.md`.
4. Record unsupported and provider-only features in the matrix above.
5. Validate discovery, invocation, permission behavior and output quality on 2–3 real tasks; label results.
6. Update `README.md`, the Workshop catalogues (a client column if support differs) and this file.

## 9. Future unified UI (preparation only — no UI is built)

No UI was built and no provider beyond Claude Code and Codex CLI was implemented. The product that will consume
these contracts, and its decision on the subscription question below, is Workshop AI:
[product vision and requirements](workshop-ai-product-vision.md) (§17.2).

Integration points that exist today (Documented): Claude Code `claude -p` (print mode, JSON output) and the
Claude Agent SDK; Codex `codex exec --json` (JSONL events, `resume`), the Codex TypeScript SDK and App Server.

**Contracts a future UI can consume** (all plain files in this repository; Proposed, stable as long as the
contributor guide is followed):

| Contract | Source | Fields |
|---|---|---|
| Agent catalogue | frontmatter of `agents/<area>/<name>.md` | `name`, `description`, `tools`, `model`; area = parent folder |
| Skill catalogue | frontmatter of `skills/<name>/SKILL.md` | `name`, `description` |
| Codex availability | `clients/.codex/agents/<name>.toml` exists and `codex-adapter.py agents --check` passes | boolean per agent |
| Task catalogue | `tasks/*.md` (except `README.md`) | title = first `# ` line; `Status:` line (active / completed / superseded by) |
| Client list | `clients/<client-id>/README.md` | client id = folder name |
| Project list | `docs/projects/<project-id>/README.md` | Purpose, Stage, Repository bullets |
| Support status | §4 matrix | evidence label per resource and client |

A future app would build its catalogue from these, dispatch a task to one or both CLIs as subprocesses, and keep
each client's own authentication. Unknowns to resolve first: whether subscription logins (Claude Pro/Max, ChatGPT
plans) may be driven by a third-party app under each provider's terms, or whether API keys (usage billing) are
required; cancellation and error semantics; rate limits. Nothing here combines accounts.

## 10. Validation status (2026-10-17)

| Check | Result |
|---|---|
| Claude Code loads shared rules, agents and skills in the repository root | Observed (this session) |
| Claude Code picks up the new `engineering-lifecycle` skill | Observed |
| Generated Codex agent files parse as TOML and contain only `name`, `description`, `developer_instructions` | Ran: 19/19 pass; re-run after adding `prompt-reviewer`: 20/20 pass |
| Drift check detects out-of-date wrappers | Ran: detected 2 changed files, then 0 after regeneration |
| `link-skills` is idempotent and skips non-link entries | Ran |
| Codex discovers `AGENTS.md`, skills and agents | **Not run**: Codex CLI 0.163.0 found on PATH (Observed 2026-10-17, installed by the maintainer outside any task); checks scheduled in the Workshop AI pilot; manual steps in [codex-cli §5](../clients/codex-cli/README.md#5-verify-manual-required-before-claiming-support) |
| Codex follows Windows directory junctions in `clients/.agents/skills/` | **Not run**; documented support covers symlinks, junctions are not mentioned (re-checked 2026-10-17). Fallback: replace each junction with a directory symlink (`mklink /D`, needs Developer Mode or Administrator) |
| `prompt-reviewer` agent discovered by Claude Code | **Observed** 2026-10-17: listed in the agent registry of a new session started in the repository root |
| Workshop reorganization (clients/, workshop/) keeps Claude discovery of `.claude/` | Agent and skill locations unchanged; manual re-check after restart: `claude` in the root, `/agents` |
| Trading-app demonstration checklist | **Not run**; steps in [the Trading-app entry](projects/trading-app/README.md) |

Prompt-engineering review (Homero v1.1, `prompt-reviewer`, target prompt revision 2): `docs/prompt-engineering-review.md`.

Results of the reorganization task: [ai-infrastructure-handover.md](ai-infrastructure-handover.md). On
2026-10-17 the repository root then moved from `%USERPROFILE%\Repos` to `%USERPROFILE%\Repos\ai-infra` (history kept;
backup bundle and tag `pre-root-move` made first). Later the same day the repository was copied (with its history) to
`%USERPROFILE%\workshop\infra`: canonical agents and skills moved from `.claude/` to `agents/` and `skills/`, task prompts
to `tasks/`, the Workshop pages into `docs/`, and the client-native folders into `clients/`. Applications now live in
`%USERPROFILE%\workshop\applications\`. The old copy in `%USERPROFILE%\Repos\ai-infra` no longer exists (checked 2026-10-17).

**Open items:**
1. Run the manual checks in the Codex client guide (Codex CLI is installed; checks not run yet).
2. Confirm that Codex follows Windows directory junctions in `clients/.agents/skills/`.
3. Push the commits when the user approves (committed locally 2026-10-17, not pushed).
4. An untracked installer binary sits inside the Trading-app repository; reported to the owner, not touched.
5. Run the Trading-app demonstration checklist in both clients.
6. Enable the secret guard in each clone (`git config core.hooksPath .githooks`); it was off in the maintainer's clone.

Known limitation: Codex does not enforce per-agent tool limits; use `codex --sandbox read-only` for review and audit roles.
