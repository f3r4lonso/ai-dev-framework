# AI infrastructure reorganization: handover report

> **Note (2026-10-17, later the same day):** the repository root was then moved from `Repos/` to `Repos/ai-infra/`.
> Paths in this report predate that move: drop the `ai-infra/` prefix, and `ai-infra/README.md` is now
> `docs/inventory.md`. Links below were updated. The two commits listed as pending were made (`af78db2`, `384cffc`).

Task: [ai-infrastructure-unification-and-workshop](../workshop/tasks/ai-infrastructure-unification-and-workshop.md)
(revision 2). Run on 2026-10-17 with Claude Code 2.1.302. Gates: A (checkpoint) declined by the maintainer, who
accepted the risk; B (plan) approved; C (commits) **pending**. All changes are uncommitted.

Evidence labels: **Observed**, **Documented** (official docs, URL and date), **Inference**, **Proposed**,
**Unverified**. `ai-environment-auditor` ran once in quick audit mode (read-only). Its labels were mapped as
Verified → Observed, Inference → Inference, Recommendation → Proposed, Unknown → Unverified.

## 1. Final directory tree (versioned infrastructure)

```text
Repos/
├── .gitignore  .gitattributes  .gitleaks.toml  .pre-commit-config.yaml
├── AGENTS.md  CLAUDE.md  README.md  SECURITY.md
├── .claude/agents/{ai,backend,devops,frontend,quality,trading,ui,ux}/*.md   20 agents (canonical)
├── .claude/skills/<name>/SKILL.md                                           23 skills (canonical)
├── .codex/agents/*.toml                                                     20 generated wrappers
├── .githooks/pre-commit
├── .github/workflows/adapter-check.yml  secret-scan.yml
├── ai-infra/
│   ├── README.md  THIRD_PARTY_NOTICES.md
│   ├── clients/claude-code-cli/README.md
│   ├── clients/codex-cli/README.md
│   ├── prompts/personal-assistants/homero-prompt-engineer.md  thor-writer.md
│   ├── scripts/codex-adapter.py
│   └── workshop/
│       ├── README.md
│       ├── catalogues/agents.md  skills.md  tasks.md
│       ├── manuals/contributor-guide.md
│       ├── projects/README.md
│       ├── projects/trading-app/README.md
│       └── tasks/README.md
│           ai-infrastructure-unification-and-workshop.md
│           homero-self-improvement-and-prompt-reviewer-task.md
│           unified-ai-client-workshop-reorganization.md
│           unified-ai-engineering-infrastructure-prompt.md
└── docs/ai-architecture.md  ai-infrastructure-handover.md  onboarding.md  prompt-engineering-review.md
```

Not versioned: `.agents/skills/` (local junctions), `ai-infra/vendor/`, `projects/applications/<id>/`.

## 2. Migration map

| Old path | New path / disposition | Reason | References updated | Validation |
|---|---|---|---|---|
| `ai-infra/prompts/tasks/ai-infrastructure-unification-and-workshop.md` | `ai-infra/workshop/tasks/` (same name), `Status: active` | Workshop holds task prompts | catalogue, `ai-infra/README.md` | link check pass |
| `ai-infra/prompts/tasks/unified_ai_engineering_infrastructure_prompt.md` | `ai-infra/workshop/tasks/unified-ai-engineering-infrastructure-prompt.md`, superseded header, user paths redacted | kebab-case, superseded | homero task, active task, `prompt-engineering-review.md`, `ai-architecture.md` | grep old name: 0 hits |
| `ai-infra/prompts/tasks/unified-ai-client-workshop-reorganization.md` | `ai-infra/workshop/tasks/` (same name), superseded header, user path and account name redacted | superseded | catalogue | grep: 0 personal hits |
| `ai-infra/prompts/tasks/homero_self_improvement_and_prompt_reviewer_task.md` | `ai-infra/workshop/tasks/homero-self-improvement-and-prompt-reviewer-task.md`, `Status: completed`, user paths redacted | kebab-case | `prompt-engineering-review.md`, active task | grep: 0 hits |
| `ai-infra/prompts/tasks/` | removed (empty) | — | `ai-infra/README.md` layout | — |
| `infra/` (empty, ignored, unreferenced) | removed | no purpose found | none | — |
| `README.md` Claude Code and Codex setup sections | consolidated into `docs/onboarding.md` (Claude install table moved there) | content existed twice | README links to client guides | link check pass |
| `README.md` agent tables | consolidated into `ai-infra/workshop/catalogues/agents.md` | content existed twice | README | 20/20 agents listed |
| `docs/ai-architecture.md` §5 (client usage) and §6 (maintaining) | replaced by links to client guides and contributor guide | no content in two places | — | link check pass |
| `Applications/` references (`AGENTS.md`, `CLAUDE.md`, `README.md`, `ai-infra/README.md`, `ai-architecture.md`, `prompt-engineering-review.md`, `git-workflow-manager.md` + its `.toml`) | `projects/applications/` | stale path | all | grep: 0 hits outside task prompts |
| `Applications/` mentions inside the 3 older and current task prompts | kept | historical text, or names the stale string on purpose | — | stated here |
| `.claude/agents/ai/ai-environment-auditor.md` | edited: rules live in `AGENTS.md`; Codex in scope; editable scope adds `AGENTS.md`, `ai-infra/clients/**`, `ai-infra/workshop/**`, AI-only `docs/` sections; never edits the generated Codex adapter; regenerate step | stale for two clients (its own self-audit finding) | inventory row, `.toml` regenerated | `--check` pass |
| `.claude/agents/devops/git-workflow-manager.md` | edited: project path, versioned file list | stale | inventory row, `.toml` regenerated | `--check` pass |
| `.claude/agents/ai/prompt-reviewer.md` | example path → `ai-infra/workshop/tasks/` | path moved | inventory row | `--check` pass |
| new: `ai-infra/clients/*`, `ai-infra/workshop/*`, this report | created | §5 decisions 2, 4 and 5 | whitelist, README, architecture | link check pass |

No new agent or skill was created: the inventory showed no material, repeatable gap.

## 3. Client catalogue

| Client | Guide | Install and authentication | Status |
|---|---|---|---|
| Claude Code CLI | [claude-code-cli](../clients/claude-code-cli/README.md) | [onboarding §1](onboarding.md#1-claude-code-cli) | Observed (2.1.302) |
| OpenAI Codex CLI | [codex-cli](../clients/codex-cli/README.md) | [onboarding §2](onboarding.md#2-codex-cli) | statically checked against Documented format; **not verified** (not installed) |
| Claude Desktop (optional) | — | [onboarding §3](onboarding.md#3-claude-desktop) | Documented |

## 4. Discovery rules

| Resource | Claude Code | Codex CLI |
|---|---|---|
| Rules | `CLAUDE.md` → `@AGENTS.md`, session start (Observed) | `AGENTS.md` git root → cwd (Documented) |
| Agents | `.claude/agents/**`, session start only (Observed) | `.codex/agents/*.toml`, trusted project only (Documented) |
| Skills | `.claude/skills/` (Observed) | `.agents/skills/` links, cwd → repo root, `~/.agents/skills/` (Documented, https://learn.chatgpt.com/docs/build-skills, 2026-10-17; junctions Unverified) |
| Task prompts | not discovered; open by path from [Workshop tasks](../workshop/tasks/README.md) | same |
| Catalogues, manuals | not discovered; [Workshop](../workshop/README.md) | same |
| Projects | separate repos; Claude with `--add-dir`; entry pages in [Workshop projects](../workshop/projects/README.md) | project `AGENTS.md` only; shared skills via `link-skills --user`; shared agents not available |

## 5. Compatibility matrix

Maintained in one place: [ai-architecture.md §4](ai-architecture.md#4-compatibility-matrix) (now includes Workshop
and claude.ai prompt rows). Summary: shared rules, skills and agents are shared, and agent tool limits and models
are client-native. Claude support is Observed; Codex is Documented or Unverified throughout.

## 6. Token and cost strategy

Controls in place: [ai-architecture.md §7](ai-architecture.md#7-token-and-cost-strategy). This task added about 150
bytes to the always-loaded `AGENTS.md` (now 1,871 bytes; with `CLAUDE.md` 2,201 bytes). The Workshop, client guides
and catalogues load only on request. **No measured results**: no baseline exists. Hypothesis to measure: catalogues
reduce exploratory file reads when choosing a resource (compare `/context` on 3 identical tasks before and after).

## 7. Security and privacy review

- **Whitelist changes (`.gitignore`):** added `!/ai-infra/clients/` and `!/ai-infra/workshop/`. No other change.
- Redacted before versioning: absolute user paths (3 task prompts) and a GitHub account/repository name (1 task
  prompt). A mention of a private file name inside a project repository was removed from 2 public docs.
- Scans of all 55 changed or new files, this report included (method: grep): user paths, usernames, account names and e-mail found 0
  hits (the only match is a generic `C:\Users\data\...` example in third-party UI data). Common secret patterns
  (Anthropic, OpenAI, GitHub, AWS, Slack keys, private-key headers) found 0 hits. gitleaks is not installed: **Not run**.
- Local secret guard was **off** (`core.hooksPath` unset) in the maintainer's clone. Not changed (hook settings are
  the user's); enable with `git config core.hooksPath .githooks` before committing.
- No web content was trusted as instructions; one official vendor page was read (Codex skills). No private content
  was sent anywhere.
- Projects: Trading-app unchanged by this task (clean / 1 untracked), same before and after.

## 8. Acceptance checklist (§7 of the task)

| # | Item | Result |
|---|---|---|
| 1 | One canonical location; catalogues link only | **Pass**: catalogues hold one-line purposes plus links; setup and agent tables de-duplicated |
| 2 | Client guides cover decision-5 topics, platform-labelled commands, fresh clone → own account → verified resource | **Pass** for Claude Code; Codex guide written but **Not run** live (Codex not installed). Steps: [codex-cli §5](../clients/codex-cli/README.md#5-verify-manual-required-before-claiming-support) |
| 3 | Client-native files where clients load them; Claude `/agents` still works | **Pass** (no client-native file moved; 20 agents listed at the start of this session). Manual re-check: start `claude` in the root, run `/agents` |
| 4 | `codex-adapter.py agents --check` | **Pass**: 20 agents, 0 out of date, 0 stale |
| 5 | Workshop tasks README | **Pass** |
| 6 | New-project convention; no project changed | **Pass**: Trading-app `git status` 1 untracked before and after |
| 7 | Internal links resolve | **Pass**: script (relative links and `#anchors` in all versioned Markdown outside `vendor/`, `projects/` and skill bodies), 144 links, 0 broken |
| 8 | No tracked file became untracked or ignored; new files versioned | **Pass**: `git ls-files -ci --exclude-standard` empty; all new files show as untracked-to-add in `git status` |
| 9 | No secrets or personal data in versioned files | **Pass** (grep); gitleaks **Not run** (not installed) |
| 10 | No user modification overwritten | **Pass**: edits were targeted replacements; the README rewrite kept every topic (moved to onboarding, catalogues or client guides) |
| 11 | Changed agents registered and documented | **Pass**: 3 inventory rows updated. The 3 agents were edited, not created, so the full §3 field set was not re-written into them. The field template is in the contributor guide |
| 12 | Architecture doc covers precedence, matrix, cost, provider procedure, UI contracts; nothing built | **Pass** (§3, §4, §7, §8, §9) |

## 9. Open items and next steps

1. **Gate C:** approve the commit plan below. No push.
2. Install Codex CLI (your authorization), run [codex-cli §5](../clients/codex-cli/README.md#5-verify-manual-required-before-claiming-support),
   including whether Windows junctions work.
3. Run the [Trading-app demonstration checklist](../workshop/projects/trading-app/README.md) in both clients.
4. Enable the secret guard; optionally install gitleaks and run `gitleaks dir . --config .gitleaks.toml`.
5. An untracked installer binary inside the Trading-app repository: the owner decides (not touched).
6. Backlog, deferred: generate the catalogues from frontmatter with a `--check` mode, to prevent catalogue drift.

**Gate C commit plan** (local commits on `main`, run with the secret guard on):

| # | Message | Files |
|---|---|---|
| 1 | `Add engineering-lifecycle skill and harden secret handling docs` | `.claude/skills/engineering-lifecycle/`, `.claude/skills/ui-ux-pro-max/SKILL.md`, `.gitattributes`, `SECURITY.md`, `ai-infra/prompts/personal-assistants/homero-prompt-engineer.md` |
| 2 | `Add Codex CLI adapter and reorganize into client guides and Workshop` | everything else in `git status` (rules, agents, `.codex/agents/`, adapter script and CI check, `.gitignore`, `README.md`, `ai-infra/`, `docs/`) |
