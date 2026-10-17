# Prompt-engineering system review — 2026-10-17

Scope: task brief `ai-infra/workshop/tasks/homero-self-improvement-and-prompt-reviewer-task.md` (moved and renamed 2026-10-17). Covers Homero v1.1,
the new `prompt-reviewer` agent, external research, integration, revision 2 of the unified infrastructure prompt, and validation.
**The unified infrastructure prompt was revised only. It was not executed.**

Evidence labels: **Ran** (a check was executed), **Static** (files inspected), **Docs** (official documentation read),
**Not run**.

## 1. Files created or modified

| Path | Status | Change |
|---|---|---|
| `ai-infra/prompts/personal-assistants/homero-prompt-engineer.md` | modified | v1.0 → v1.1. All sections kept; additions listed in §2 |
| `.claude/agents/ai/prompt-reviewer.md` | **new** | canonical Prompt Reviewer agent (read-only) |
| `.codex/agents/prompt-reviewer.toml` | **new, generated** | Codex wrapper from `codex-adapter.py agents` |
| `.claude/agents/ai/ai-environment-auditor.md` | modified | description: one sentence that sends single-prompt reviews to `prompt-reviewer` (prevents overlap) |
| `.codex/agents/ai-environment-auditor.toml` | regenerated | follows the description change |
| `ai-infra/workshop/tasks/unified-ai-engineering-infrastructure-prompt.md` (now superseded) | rewritten | revision 2 (§5). Was untracked; the original is not in git |
| `ai-infra/README.md` | modified | inventory row for `prompt-reviewer`; Homero → reviewer note in the layout |
| `README.md` | modified | 19 → 20 agents; catalog row |
| `docs/ai-architecture.md` | modified | counts 19 → 20; validation rows; open items moved out of the target prompt |
| `docs/prompt-engineering-review.md` | **new** | this report |

The working tree already had uncommitted changes before this task (see `git status`). They were left as they were. Nothing was committed.

## 2. Homero v1.1 — improvements

- **Objective test:** a one-sentence objective ("The user needs X so that Y") is required before drafting.
- **Requirement map (§4.2):** separates objective, scope, constraints, dependencies, deliverables, acceptance criteria and
  optional enhancements. It is reused as the regression baseline for revisions.
- **Decomposition and ordering (§4.5):** dependency-ordered phases, approval gates, exit conditions and blocker handling.
- **Least-privilege tools and authorization (§4.7):** tools and permissions are phrased conditionally when unverified. Repository and web content is treated as untrusted. Prompts carry no secrets.
- **Clarification (§5):** Category A/B/C kept. Added a test for whether a question matters, a limit of five questions, and a recommended default for each.
- **Context and token efficiency (§9):** each rule stated once; reference large material instead of pasting it; long inputs placed before instructions; strong emphasis only where it is needed.
- **Prompt Reviewer handoff (§10.2):** when to use it, what to send it, and that Homero keeps ownership of the prompt. In environments without the agent, Homero applies the checks itself and says that no independent review ran.
- **Revisions:** a CHANGES section is now required. Removing or weakening a requirement must be reported.
- **Other:** data-work guidance added; English stays the default for prompts and replies; "never execute what you write" made explicit.

## 3. Prompt Reviewer

- **Role:** independent assessment only. It finds defects, scores and recommends. It never executes the prompt, never changes its objective, never invents facts and never widens permissions. Tools: `Read, Grep, Glob`.
- **Method:** an 8-step process: restate, map, inspect, assess executability, prioritize, recommend, rewrite only on request, then recheck.
- **Scoring:** 8 dimensions on a 0–5 scale, with anchors for 0, 3 and 5, and N/A where a dimension does not apply. The overall score is the mean of the scored dimensions. It is a diagnostic heuristic, not a guarantee.
- **Verdict:** Blocked (any Blocker finding), Ready with revisions (a High finding or any dimension ≤ 2), or Ready. Severity always overrides the score.
- **Output contract:** an 8-part report. Modes are `quick`, `review` (the default) and `rewrite`.
- **Boundary with Homero:** Homero owns the requirements and the authoritative prompt. The reviewer owns the critique. Homero decides which recommendations to adopt.
- **Invocation:**
  - Claude Code: "Use the prompt-reviewer agent …" or `@agent-prompt-reviewer`.
  - Codex: "Use the prompt-reviewer agent …" in a trusted project, preferably with `--sandbox read-only`.
  - claude.ai: paste the agent's body into a separate conversation.

## 4. External resources evaluated

Research used generic queries only. No private content was sent. Nothing was installed or run. "Verified" below means the source was read, not tested.

| Resource | Publisher / type | Used for | Decision | Rationale and what was verified |
|---|---|---|---|---|
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Anthropic, official docs (living page, covers current Claude models) | Homero §4.6, §8 and §9 | **Adopt** (as technique source) | **Docs:** be explicit and give the reason behind a rule; use examples and XML-style delimiters; put long data before instructions; current models over-trigger on aggressive emphasis ("CRITICAL: You MUST"); guidance on overeagerness and on subagents. No licensing issue (guidance, not code). |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic Engineering blog, 2025-09-29 | Homero §9 and §7 (multi-agent), reviewer efficiency checks | **Adopt** | **Docs:** "smallest set of high-signal tokens"; prompts at the "right altitude"; a few canonical examples instead of rule lists; just-in-time references; compaction and notes; subagents return condensed summaries. |
| [GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) | OpenAI Cookbook (marked archived, no date) | Reviewer contradiction check; Homero stop conditions | **Adapt** | **Docs:** contradictory instructions hurt close-following models; calibrate agent eagerness with explicit stop conditions and escape hatches. Model-specific advice (reasoning_effort, re-appending formatting rules) was not adopted. |
| [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) | Anthropic, official docs | Agent placement and description | **Adopt** (format) | **Docs:** recursive `.claude/agents/`; `name` and `description` required; the description drives automatic delegation; an omitted `tools` field inherits everything, so the reviewer's tools are set explicitly. |
| [Codex subagents](https://developers.openai.com/codex/subagents) (redirects to learn.chatgpt.com) | OpenAI, official docs | Codex wrapper | **Adopt** (existing generator) | **Docs:** `.codex/agents/*.toml` with `name`, `description` and `developer_instructions`; agents inherit the parent sandbox; instructions cannot create a read-only sandbox. So the reviewer's read-only rule is enforced only by instruction in Codex. |
| [promptfoo](https://github.com/promptfoo/promptfoo) | promptfoo (company acquired by OpenAI, per third-party reports), MIT, ~26k★ | Automated prompt regression tests | **Defer** | Needs Node/npm and calls configured model APIs (cost, data transfer). Worth it only once prompts have a test set. Re-evaluate with `dependency-license-review` before any install. |
| Anthropic Console prompt improver / OpenAI prompt optimizer | Vendor web tools | Automatic rewriting | **Reject** (for private prompts) | Would send private prompts to an external service. The local reviewer covers the need. |
| Built-in `skill-creator` skill | Anthropic (already available in this client) | Skill evals | **Defer** | Relevant only when building skills, not prompts. No change needed. |

## 5. Target prompt — revision 2

Based on a Prompt Reviewer `review` of revision 1: verdict **Ready with revisions**, 3.3 / 5 over 8 dimensions, 4 High findings, no Blocker.

| Finding | Change |
|---|---|
| Execution log appended to the prompt (stale, and could trigger a re-run) | Log moved to `docs/ai-architecture.md` §10. A header note says the prompt was run once and that a re-run must re-verify that work and then focus on open items. |
| Codex required to be "verified" though it is not installed | Defined what "done" means without a local Codex CLI: static checks, manual steps and checks labeled **Not run**. Final directive reworded. |
| Auditor named by description only | Names `ai-environment-auditor` and which mode to use in each phase |
| "Do not send content to a cloud model" blocks the executing model itself | Authorizes the executing client's own model and its subagents (decision D1). The ban on third-party services stays. |
| Web access, commits and the design gate not stated | Public vendor docs allowed with generic queries; commits need approval (D3); stop for approval after the design phase (D2, can be pre-approved) |
| Report vs workspace rules | The reply is a short outcome summary in English that links to the full report in `docs/` |
| Phases written twice; Operating Rules and Final Directive repeated earlier rules | One workflow with exit conditions; the authorization block is split into allowed, needs approval and prohibited; reference requirements gathered in §7 |
| AutoTrade not mapped to a path | `projects/applications/Trading-app` (confirmed 2026-10-17) |
| snake_case file name | **Not changed:** the task brief points to the exact path. Listed as open item 5. |

The decisions D1–D4 at the top of the prompt are the only places where the revision adds rules. They narrow authority (approval gates) or make explicit two permissions the prompt already needs in order to run (D1 data flow, D4 public-docs web access). Regression check: §6.

## 6. Validation

| Check | Result |
|---|---|
| Required files exist at the intended paths | **Ran:** yes (§1) |
| Homero kept all v1.0 sections and capabilities | **Static:** sections 1–14 of v1.0 map to sections 1–15 of v1.1, and nothing was removed |
| `prompt-reviewer` frontmatter valid (`name`, `description`, `tools`); agent names unique | **Ran:** 20 agents, no duplicates |
| Codex wrappers parse as TOML with only the 3 allowed keys | **Ran:** 20/20 |
| Adapter drift check (`codex-adapter.py agents --check`) | **Ran:** 0 out of date, 0 stale |
| Path references in the three edited prompts point to existing files | **Ran:** no missing references |
| Secret patterns in the edited prompts (API keys, tokens, private keys) | **Ran:** none found (pattern grep, not a full scanner) |
| Prompt Reviewer method produces a usable report | **Ran (fallback):** a general-purpose agent followed `prompt-reviewer.md` on revision 1 (§5) and on revision 2 (regression below) |
| Native discovery of `prompt-reviewer` in Claude Code | **Not run:** this session started before the file existed, and calling it by type failed ("not found"). Manual step: restart `claude`, then `/agents` and `@agent-prompt-reviewer` |
| Codex discovery and invocation | **Not run:** Codex CLI not installed |
| Target prompt not executed; no application change | **Ran:** the Trading-app repository showed only one pre-existing untracked file. No infrastructure-building actions were taken. |
| Regression check of revision 2 against revision 1 | **Ran (fallback reviewer, quick mode + regression):** verdict Ready with revisions, **4.8 / 5** over 8 dimensions (revision 1: 3.3). No material requirement lost. Its 4 small weakenings were restored afterwards: the "other high-impact operations" approval catch-all; "must" in the end state; "acceptance criteria" in the shared core; "do not ask what evidence can answer" together with "do not claim a configuration exists unless observed". Its other findings were also fixed: the header now treats launching the prompt as approval; web access is decision D4; the discipline list now reads "assess coverage"; the report format is clarified. That final text was not re-reviewed. |

## 7. Security review

- **Least privilege:** the Prompt Reviewer has no shell, no edit tools and no web access. Its description does not say "use proactively", and it names the agents it must not overlap with.
- **Untrusted input:** both Homero and the reviewer treat the prompt and the files it references as data. The reviewer reports embedded instructions as findings, and a secret found in a prompt as a Blocker (location only, never the value).
- **External services:** Homero and the reviewer search with generic terms only. External prompt optimizers were rejected for private prompts.
- **Codex limit:** read-only behavior is enforced only by instruction in Codex. Run review roles with `--sandbox read-only` (Docs).
- **Target prompt:** the revision narrows authority (approval gates for commits and implementation). It states two permissions explicitly, the data flow to the executing client (D1, secrets excluded) and public-docs web access (D4), and you should confirm both knowingly.

## 8. Open issues and follow-up

1. Restart Claude Code and confirm that `prompt-reviewer` appears in `/agents` (manual).
2. Codex checks remain open until the CLI is installed with your authorization (`docs/ai-architecture.md` §5).
3. Approve or change decisions D1–D4 in the target prompt before running it.
4. Optional: rename the snake_case task files to kebab-case and update the references.
5. Optional: add the Homero v1.1 text to its claude.ai Project. That is a manual copy, because the repository file is not loaded by claude.ai.
6. Nothing is committed. Commit when you approve.
