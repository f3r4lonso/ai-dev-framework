# Workshop AI — Product Vision and Requirements

**Document type:** Product vision and requirements baseline  
**Status:** Baseline for Stage 1. Development is governed by the gates of
[workshop-ai-product-foundation](../tasks/workshop-ai-product-foundation.md) (Gate B approves the Stage 1 build).  
**Version:** 1.1 (2026-10-17); 1.0 was the unreviewed proposal  
**Language:** English

Requirement keywords: **MUST** (required for the stated priority), **SHOULD** (expected unless a recorded reason
says otherwise), **MAY** (optional). Evidence labels follow [ai-architecture.md](ai-architecture.md): Observed,
Documented, Inference, Proposed, Unsupported/Unverified.

## 1. Executive Summary

Workshop AI is a collaborative working environment for multiple AI clients. Its purpose is not simply to place
several AI tools behind one interface. It is to help them work better together: use each client's strengths where
appropriate, preserve relevant knowledge between sessions, coordinate tasks, reduce duplicated analysis, and deliver
better results with less unnecessary computational work.

Workshop AI lets a user work with Claude Code CLI, OpenAI Codex CLI, and future compatible clients, independently or
in a coordinated workflow. It uses shared project context and reusable engineering resources without pretending that
all providers have the same capabilities, authentication, permissions, context limits, or billing models.

Collaboration is selective (§6.1, §9). This document sets the mission, principles, scope, functional and
non-functional requirements, success measures, and the decisions taken before implementation (§17). What may be built,
and when, is set by the roadmap gates (§16).

## 2. Source Alignment and Interpretation

Version 1.0 consolidated the user's mission and the earlier infrastructure prompts (multi-client support, shared
agents and skills, project isolation, CLI integration, task prompts, security, session continuity, future UI). It did
not audit the existing infrastructure.

Version 1.1 reconciles the vision with the infrastructure that already exists in this repository (gap analysis of
2026-10-17, §2.1), records the product-owner decisions (§17), and turns the requirements into testable statements.
Workshop AI builds on that infrastructure; it does not redesign it.

### 2.1 Existing baseline

What the infrastructure already provides, and what remains for Workshop AI. Stage = the roadmap stage (§16) that
closes the gap. Source: gap analysis of 2026-10-17 (main session; the `ai-environment-auditor` cross-check was run as
a labelled main-session fallback because the agent could not be invoked in that session).

| Requirement | Existing asset | Remaining gap | Stage |
|---|---|---|---|
| FR-01 Client registry | [compatibility matrix](ai-architecture.md#4-compatibility-matrix), client list contract in [ai-architecture.md §9](ai-architecture.md#9-future-unified-ui-preparation-only--no-ui-is-built), [Claude Code guide](../clients/claude-code-cli/README.md), [Codex guide](../clients/codex-cli/README.md) | human-readable only; Codex rows Documented/Unverified | 2 |
| FR-02 Client selection | [tasks/README.md §1](../tasks/README.md#1-choose-a-client) | no way to pick and record a client per task | 1 |
| FR-03 Task contract | task-file convention ([tasks/README.md §5](../tasks/README.md#5-task-file-convention)); `engineering-lifecycle` templates ([templates](../skills/engineering-lifecycle/references/templates.md)); task approval gates | no per-task record with status, owner and next action | 1 |
| FR-04 Resource catalogue | [agents](catalogues/agents.md), [skills](catalogues/skills.md), [tasks](catalogues/tasks.md) catalogues; catalogue contracts in [ai-architecture.md §9](ai-architecture.md#9-future-unified-ui-preparation-only--no-ui-is-built) | tool must read the existing contracts | 1 (read only) |
| FR-05 Handoffs | none | manual handoff package and its approval | 1 manual, 3 automated |
| FR-06 Project continuity | none (handover reports are written by hand per task) | project-state file and resume | 1 |
| FR-07 Context selection | progressive disclosure in the [token strategy](ai-architecture.md#7-token-and-cost-strategy) | per-task list of selected context | 1 |
| FR-08 Approvals | task gates; `engineering-lifecycle` stage gates; client permission modes ([matrix](ai-architecture.md#4-compatibility-matrix), "Permissions") | the tool's own approval points | 1 |
| FR-09 Privacy | [SECURITY.md](../SECURITY.md), `.gitleaks.toml`, `.githooks/`, whitelist `.gitignore`, secret rule in [AGENTS.md](../AGENTS.md) | secret check before a package leaves its provider | 1 |
| FR-10 Run history | handover reports (manual) | run log per task | 2 |
| FR-11 Gap identification | [`ai-environment-auditor`](../agents/ai/ai-environment-auditor.md); [tasks/README.md §4](../tasks/README.md#4-recommend-a-new-agent-skill-or-task) | none for Stage 1 | covered |
| FR-12 Evaluation | measurement method in the [token strategy](ai-architecture.md#7-token-and-cost-strategy) (never run) | no baseline yet | 1 pilot, 4 |
| FR-13 Extension contract | [add-a-provider procedure](ai-architecture.md#8-adding-another-provider-procedure-not-implemented); [contributor guide §5](manuals/contributor-guide.md#5-add-a-client-or-provider) | adapter boundary inside the tool | 5 |
| FR-14 Navigation | [workshop.md](workshop.md), [projects/README.md](projects/README.md), [tasks/README.md](../tasks/README.md) | list and resume commands | 1 partial |
| FR-15 Export | plain Markdown/JSON in git is portable | formal export | 2+ |
| NFR-01 Reliability | none | no silent overwrite; recoverable failures | 1 |
| NFR-02 Transparency | evidence labels ([ai-architecture.md](ai-architecture.md)) | tool output names client, context, labels | 1 |
| NFR-03 Extensibility | generator pattern of `scripts/codex-adapter.py`; provider procedure | client adapter boundary | 3, 5 |
| NFR-04 Security | as FR-09 (secret guard is off in the maintainer clone: [ai-architecture.md §10](ai-architecture.md#10-validation-status-2026-10-17), open item 6) | as FR-09 | 1 |
| NFR-05 Maintainability | contributor guide; one canonical source per resource | small, standard-library tool | 1 |
| NFR-06 Usability | client guides' start-up steps | single-client path stays short | 1 |
| NFR-07 Portability | plain files | documented formats | 1 |
| NFR-08 Observability | none | run log | 2 |
| §12 and §15.1 | [token strategy](ai-architecture.md#7-token-and-cost-strategy): no baseline, no saving claimed | the Stage 1 pilot is the first baseline | 1, 4 |

Because existing assets cover FR-01 and FR-04 as documents, both are P1, not P0 (§10).

## 3. Product Vision

**Workshop AI makes AI work better, more efficiently, and more sustainably by enabling available AI clients to
collaborate selectively, share relevant knowledge, and coordinate work within a coherent environment.**

It helps users obtain better outcomes than isolated, disconnected AI sessions by giving the right client the right
task, context, resources, and verification responsibility, without orchestration overhead that outweighs the
benefit.

## 4. Core Mission

Build a unified environment where different AI clients can collaborate, complement one another, share relevant
knowledge, and work together to deliver better results while minimizing unnecessary resource consumption: task
allocation, controlled handoffs, project continuity, reusable knowledge, and evidence-based evaluation of whether
collaboration adds value.

## 5. Problem Statement

When AI tools are used independently, users reconstruct context, repeat explanations, transfer decisions and
artifacts by hand, rediscover instructions, and reconcile inconsistent outputs. Using several clients adds further
costs: duplicated exploration, redundant tool calls, competing edits, context leakage, coordination delay, and higher
token or API consumption.

Workshop AI addresses these through a shared working model and selective coordination. It does not assume that more
clients or agents automatically improve quality or efficiency.

## 6. Guiding Principles

### 6.1 Better results through justified collaboration

Clients complement one another when they have distinct relevant strengths or when independent work materially
improves confidence. Collaboration is task-dependent, observable, and optional. Decision rule: §9.

### 6.2 Shared knowledge and continuity

Keep an authoritative, reusable record of goals, requirements, constraints, decisions, current state, artifacts, open
questions, and next steps, so a client can resume without reconstructing the conversation (FR-06, §11).

### 6.3 Token and context efficiency

Load only the context the active task needs (FR-07, §12).

### 6.4 Sustainable resource consumption

Reduce avoidable model calls, repeated reasoning, redundant tool execution, idle orchestration, and unnecessary
computation. Optimize for useful outcomes per unit of resource, not for the lowest token count in isolation (§12).

### 6.5 Intelligent task allocation

The user chooses a client/model or follows an explainable recommendation (FR-02).

### 6.6 Open and extensible architecture

Keep shared concepts and project knowledge independent from provider-specific adapters (FR-13, NFR-03).

### 6.7 Measurable value

Evaluate outcomes, not the number of clients or agents (§15).

### 6.8 Practical simplicity

Prefer the smallest architecture that solves a demonstrated problem. Avoid speculative abstractions, agent
proliferation, always-on orchestration, and integrations that cost more to maintain than they return.

### 6.9 Human control and transparent operation

Users can see which client is acting, what context is shared, what permissions are active, what is proposed, and
what was done (FR-08, NFR-02).

## 7. Product Goals and Non-Goals

### 7.1 Goals

- One coherent way to organize and use supported AI clients.
- Run a task with one client, or coordinate several.
- Preserve project knowledge and work state across sessions.
- Reuse the existing shared agents, skills, task prompts, rules and manuals (§2.1).
- Keep client-native configuration separate where required.
- Reduce repeated context reconstruction and duplicated work.
- Make collaboration overhead visible and measurable.
- Secure project boundaries, provider-specific authentication, controlled data sharing.
- An extensible client integration model.

### 7.2 Non-goals for the initial product

- Replacing the native Claude Code CLI, Codex CLI or future clients.
- Assuming a subscription grants API access or can be reused by another application (§17.2).
- Assuming all CLIs expose the same programmatic interface or execution modes.
- Running every task through every client.
- An agent for every discipline or task.
- Sharing all conversation history with all providers.
- Adding providers before their value and compatibility are evaluated (Stage 5).
- A workflow automation platform, IDE or cloud execution service without a separately approved requirement.
- Unmeasured claims of savings (§15).

## 8. Core Product Concepts

- **Workshop AI:** the application described here. It **consumes** the Workshop layer of this repository
  ([workshop.md](workshop.md): task prompts, catalogues, manuals, project entries) and **does not replace it**. Never
  shorten the product name to "Workshop", which names that layer.
- **AI client:** an application or CLI through which a user works with an AI provider (Claude Code CLI, Codex CLI).
- **Provider/model:** the AI service or model behind a client. Client identity and model identity are not
  interchangeable.
- **Agent:** a role and instruction set for a type of work, possibly with delegated tools or permissions.
- **Skill:** a reusable procedure, reference or capability.
- **Task:** a bounded unit of work with an objective, context, constraints, outputs and acceptance criteria.
- **Project:** a persistent workspace with its own requirements, decisions, artifacts and state; its own git
  repository ([projects/README.md](projects/README.md)).
- **Session:** a period of interaction with one client. Not the same as a project or a durable task record.
- **Run:** one execution of a task, by one or several clients.
- **Handoff:** a controlled transfer of task state, selected context, artifacts and responsibility between clients
  or agents.
- **Handoff package:** the files that carry a handoff (FR-05).
- **Canonical shared resource:** the single authoritative definition from which clients consume or adapt a shared
  agent, skill, workflow or instruction ([ai-architecture.md §1](ai-architecture.md#1-layers-and-source-of-truth)).

## 9. Product Operating Model

Single-client mode is the default unless the user chooses otherwise (§17.5).

### Mode A — Single-client execution

The user chooses one client/model; the task uses only that client's resources. The simplest path for
straightforward work.

### Mode B — Sequential collaboration

One client does a bounded task; another reviews, validates or continues it from a handoff package (FR-05). Examples:
implementation then independent review; planning then execution.

### Mode C — Parallel independent work

Two or more clients handle independent subtasks or give independent assessments. Only where results can be
reconciled without excessive overhead or conflicting writes (§17.7).

### Mode D — Selective escalation or specialist review

A primary client brings in a second client or a specialist agent on uncertainty, material risk, cross-domain
complexity, or a required independent check.

### Collaboration decision rule

Before adding another client or agent, weigh:

**Expected benefit = expected quality/risk/productivity gain − added resource cost − latency − coordination
overhead − data-sharing risk.**

This formula is **qualitative**: a checklist of terms to weigh, not a calculation. Its terms usually cannot be
measured precisely. Add a client only when the expected benefit is clearly positive, the user asks for it, or a
mandatory independent check requires it. If the benefit is uncertain, start with one client and escalate at a
defined decision point.

Two clients MUST NOT edit the same files at the same time unless each has been told which files the other owns. Any shared-work mode MUST define
ownership, artifact handoff, conflict detection and reconciliation before it is built (Stage 3).

## 10. Functional Requirements

Priorities: **P0** = required for the Stage 1 path; **P1** = high value after Stage 1 works; **P2** = later.
Priorities are planning decisions, not implementation status. Each requirement has one **observable check**: a
result a person can see without trusting the tool's own claims.

**P0 set:** FR-02, FR-03, FR-05 (manual handoff), FR-06, FR-07 (selected context only), FR-08, FR-09.

### FR-01 — Client registry and capability discovery (P1)

The tool SHOULD list the supported clients with their invocation method, permission model, limitations and evidence
label, taken from the existing sources in §2.1 rather than a second copy. It MUST NOT infer compatibility from a
resource merely being readable by a model.  
P1 because the compatibility matrix and client guides already cover it as documents (§2.1).  
**Check:** the tool's client list matches the clients and evidence labels in the compatibility matrix.

### FR-02 — User-controlled client selection (P0)

The user MUST be able to choose the client for each task, and the choice MUST be recorded in the task record. Any
recommendation SHOULD show its basis (task fit, cost, privacy, limitations) and MUST be overridable.  
**Check:** after creating a task for client X, the task record names X, and the session the tool starts is X.

### FR-03 — Task specification and execution state (P0)

Each task MUST have a contract file with at least: objective, acceptance criteria, selected client, status, and next
action. It SHOULD hold, where they apply: context, constraints and authorization boundaries, agents and skills,
inputs, artifacts and ownership, open questions. Trivial tasks need only the minimum fields.  
**Check:** a task created through the tool yields a hand-readable file containing the five minimum fields, and the
tool reads it back without error.

### FR-04 — Shared resource catalogue (P1)

The tool SHOULD list agents, skills and task prompts from the existing catalogue contracts
([ai-architecture.md §9](ai-architecture.md#9-future-unified-ui-preparation-only--no-ui-is-built)), copying no bodies.  
P1 because the catalogues already exist (§2.1).  
**Check:** the tool's resource list matches the rows of the agent, skill and task catalogues.

### FR-05 — Controlled collaboration and handoffs (P0, manual)

The tool MUST produce a handoff package containing only the task's selected context, decisions, constraints,
artifacts, open questions and next steps, never a full transcript by default. Where a client has no supported
automation path, the handoff MUST be a documented manual procedure; the tool MUST NOT imply automatic cross-client
execution exists. Automated handoff is Stage 3.  
**Check:** a new session (Claude Code, or Codex CLI once it is verified), given only the package folder, states the
recorded decisions and next step, without access to the first session's transcript.

### FR-06 — Project continuity (P0)

The tool MUST keep a project-state file sufficient to resume work: objective and status, requirements and
constraints, decisions with rationale, artifacts and links, open issues, last verified state, next steps. Updates
MUST be attributable to a task or run and MUST NOT silently overwrite conflicting content. The user MUST be able to
inspect, correct or delete the state by hand.  
**Check:** a new session given only the state file states the recorded decisions correctly.

### FR-07 — Context selection and retrieval (P0, selected context only)

A task MUST carry only the context the user selected (paths or sections), and canonical knowledge MUST stay separate
from session details. Automatic retrieval is P1. Provider context windows and memories are not shared.  
**Check:** the launch instructions and the handoff package reference only the selected items.

### FR-08 — Approval and permission boundaries (P0)

The tool MUST show which client acts and what it will do, respect client-native permission controls, and never
widen permissions silently. Explicit user approval MUST be obtained before any action that is destructive,
external, paid, sensitive, outside the approved workspace, or restricted by the rules in force (the governing task
prompt and the project's `CLAUDE.md`/`AGENTS.md`), and before a handoff package is released to another client
(§17.5). Approval MUST come from a person at a terminal; an AI session must not be able to give it. This section is
the single statement of the approval rule; other sections refer to it.  
**Check:** a client start declined at the prompt launches nothing, and showing an unapproved handoff package is
refused, both with an "approval required" message; neither can be approved from a non-terminal input.

### FR-09 — Privacy and data-flow control (P0)

Project and provider boundaries MUST be kept. Context MUST NOT pass between providers without approval (FR-08). A
secret check MUST run on every handoff package before release, and on the task, brief and project-state files at
each checkpoint. Secret values and authentication material MUST NEVER
appear in task state, prompts, logs, packages or catalogues. This section is the single statement of the credential
rule.  
**Check:** a package containing a planted test-secret pattern is blocked, and the block is reported.

### FR-10 — Run history and provenance (P1)

The tool SHOULD record task and run status, clients, handoffs, artifacts, decisions, verification outcomes, and
resource figures where available and authorized; model assertions MUST be distinguished from verified outcomes;
unnecessary private content SHOULD NOT be stored.  
**Check:** for a completed task, the run log names each client involved and labels each outcome Observed or not.

### FR-11 — Resource recommendation and gap identification (P1, covered)

Recommend existing agents and skills first; propose a new one only for a material, repeatable gap, with value,
overlap, maintenance cost and validation plan; never create one automatically without scoped user permission.
Covered today by [tasks/README.md §4](../tasks/README.md#4-recommend-a-new-agent-skill-or-task).  
**Check:** a recommendation names at least one existing resource before any new one.

### FR-12 — Outcome and efficiency evaluation (P1)

The tool SHOULD support the §15 measurements where reliable data exist; missing telemetry MUST be shown as N/A.  
**Check:** a pilot report lists every §15.2 metric with a value or N/A, none estimated.

### FR-13 — Client adapter and extension contract (P1)

Adding a client follows the [add-a-provider procedure](ai-architecture.md#8-adding-another-provider-procedure-not-implemented):
official interfaces and security model, capability mapping, minimal adapter, discovery/invocation/permission tests,
recorded limitations, updated documentation.  
**Check:** a new client is added without changing the task or project-state formats.

### FR-14 — User-facing task and project navigation (P1)

The tool SHOULD let the user choose or resume a project, see its state and resources, pick a task, and review
results, without screens or options that serve no defined workflow.  
**Check:** a user can list tasks and resume one with one command each.

### FR-15 — Export, recovery, and portability (P2)

Where justified, project state and task records SHOULD be exportable in documented formats and recoverable without a
provider's proprietary memory; exports MUST pass the FR-09 secret check.  
**Check:** an exported project restores into an empty folder and the tool reads it.

## 11. Shared Knowledge and Session Continuity

Knowledge is kept as structured, scoped, reviewable state, not as the full conversation history. Categories:

1. **Project facts and requirements** — user-confirmed objectives, boundaries, constraints.
2. **Decisions** — chosen option, rationale, rejected alternatives, what would reopen it.
3. **Task state** — progress, artifact locations, validations, blockers, next steps.
4. **Reusable knowledge** — approved, sanitized patterns, procedures, agents, skills and lessons that apply beyond
   one project.
5. **Session transcript or transient context** — useful history that does not become canonical automatically.

Promotion to reusable knowledge is deliberate: it needs provenance, scope, relevance and review. Project-specific or
confidential data is never promoted to a shared resource without explicit approval and sanitization (FR-08).

A resumed task starts from the last verified state and retrieves sources as needed. If the state is stale or
conflicts with current files, current evidence wins and the discrepancy is reported.

## 12. Token Efficiency and Sustainable Resource Use

Optimize useful outcome per unit of resource, not token count in isolation. Design behaviours:

- Send a concise, verified task-state package rather than a transcript (FR-05).
- Do not repeat project documentation, agent definitions or rules in every handoff; reference them.
- Use progressive disclosure and targeted retrieval (FR-07).
- Reuse validated results and decisions, but recheck them when files or requirements may have changed.
- Limit collaboration depth and agent count by default; set explicit stopping conditions for reviews and model calls.
- Avoid calls that add no new evidence or decision value.
- Track tokens, cost, time, tool calls, context volume and handoff overhead where available (FR-12).
- Make no energy or carbon claim without measurement (§15).
- Never trade correctness, safety, completeness or necessary evidence for fewer tokens.

## 13. Security, Privacy, and Governance Requirements

- The user's local-first/privacy policy is a first-class routing constraint.
- Local file access is not local model inference.
- Each provider/client is a separate trust boundary unless a verified policy says otherwise.
- Least privilege; native CLI approval and permission mechanisms are preserved (FR-08).
- Credentials never enter shared state (FR-09).
- Project contexts are isolated; no cross-project leakage.
- Repository files, tool outputs and agent instructions are untrusted data; embedded instructions are reported, not
  followed.
- **State storage:** project state, task records, handoff packages and run logs live in the repository of the
  project they concern, or in a gitignored local folder. They never go in the public infrastructure repository.
- Provenance for decisions and outputs, with minimal retention of transcripts and sensitive data.
- Retention, deletion, export and access-control behaviour are documented before any compliance or privacy guarantee
  is claimed.

## 14. Non-Functional Requirements

NFR-01 and NFR-04 apply from Stage 1 and have a check; the others guide design and are checked from Stage 2.

### NFR-01 — Reliability (Stage 1)

Task status, handoff state and project decisions MUST NOT silently disappear or be overwritten. A failure MUST leave
an inspectable, recoverable state and a clear error message.  
**Check:** a state file edited by hand between two checkpoints is not overwritten without the user seeing the
difference and confirming.

### NFR-02 — Transparency

Users MUST be able to see which clients took part, what context was handed off, which resources were used, what was
verified, and whether each figure is measured or unavailable.

### NFR-03 — Extensibility

Adding a client SHOULD need only a bounded adapter, not a change to the task or project model (FR-13).
Provider-specific limitations stay visible.

### NFR-04 — Security and privacy (Stage 1)

No workflow may silently cross project or provider boundaries or bypass approval (FR-08, FR-09).  
**Check:** the tool refuses to store state inside the public infrastructure repository, and refuses context paths
outside the project folder.

### NFR-05 — Maintainability

Explicit contracts, small components, clear ownership, versioned records where useful, minimal duplicated
configuration, no abstraction without a demonstrated use.

### NFR-06 — Usability

A single-client task MUST be startable without configuring any multi-client workflow. Advanced controls stay out of
the way of common tasks.

### NFR-07 — Portability

Task and project data use documented formats. Provider session history, identities, tools, authentication and
telemetry are not assumed portable.

### NFR-08 — Observability

Record enough status, timing, handoff and verification data to diagnose failed or inefficient workflows, without
unnecessary sensitive logging.

## 15. Measuring Whether Collaboration Works

This section is the single statement of the measurement rule: **no improvement in quality, tokens, cost, time or
energy is claimed without a baseline and a measurement.** Evaluation compares against a credible baseline, not the
mere fact that several clients took part.

### 15.1 Baseline method

1. Select representative tasks and write acceptance criteria before execution.
2. Run a baseline with the simplest suitable single-client workflow.
3. Run the proposed workflow on comparable tasks or under a controlled design.
4. Use the same requirements and quality rubric.
5. Record quality, acceptance-criteria results, wall-clock time, token/cost telemetry when available, redundant work,
   handoffs and human interventions.
6. Check whether added clients contributed distinct evidence or improvements.
7. Report sample size, variation, unavailable metrics and limitations. One success is not proof.

The Stage 1 pilot design is recorded in §17.6.

### 15.2 Recommended metrics

| Dimension | Indicator | Measurement guidance |
|---|---|---|
| Output quality | Acceptance-criteria pass rate; rubric score; defect/rework rate | Prefer independently verifiable checks and blinded review where practical. |
| Task success | Share of tasks completed correctly within scope | Define completion criteria before execution. |
| Continuity | Time or steps to resume; essential decisions recovered | Resume in a new session without the original transcript. |
| Token efficiency | Input/output tokens per accepted task where exposed | Keep provider data separate; unavailable counters are N/A. |
| Cost efficiency | Monetary cost per accepted task where reliably measurable | Subscription use is not metered API use; do not infer cost from tokens alone. |
| Time efficiency | End-to-end time to accepted result | Include waiting, handoffs, reconciliation and rework. |
| Duplication | Repeated context, repeated exploration, redundant tool calls, overlapping outputs | Define practical logging; no exact claims without instrumentation. |
| Collaboration value | Incremental quality/risk benefit versus added cost and latency | By task category and mode. |
| Knowledge reuse | Share of resumed tasks that used relevant prior decisions | Check that the reused material was still correct. |
| Safety | Unauthorized actions, unintended transfers, secret exposure, boundary violations | Target zero; record near misses; test failure paths. |
| Maintainability | Adapter/resource duplication, broken references, effort to add a client | Track during reviews and extension work. |

### 15.3 Decision criteria for collaboration

Keep a collaborative workflow for a task category only with a repeatable net benefit:

- better correctness or risk detection that justifies the extra resources; or
- comparable quality with materially less work, cost or time; or
- a required independent check the primary workflow cannot provide.

Targets are set at pilot planning, after baseline variance is known; no percentage is a product fact before
measurement and approval. If a workflow repeatedly adds cost and time without improving quality, risk or continuity,
simplify or remove it.

## 16. Scope and Delivery Roadmap

Each stage has one exit criterion and one gate. A stage starts only after the previous stage's gate is passed.

| Stage | Scope | Exit criterion | Gate |
|---|---|---|---|
| 0 — Resolve product decisions | target user, operating mode, privacy policy, persistence, integration constraints, first success criteria | §17 decisions recorded with date | Gate A of the foundation task (**passed 2026-10-17**) |
| 1 — Validate the single-client journey | choose client, create task, attach selected context, run, save verified state, resume, hand off manually (P0 set, §10) | journey, resume and manual handoff **Observed** on the sandbox project, pilot reported per §15.1, results committed after the foundation task's Gate D | Gate B of the foundation task (specification and build plan) |
| 2 — Continuity and reusable resources | run log (FR-10), registry and catalogue reading (FR-01, FR-04), provenance, knowledge promotion | decisions recovered correctly on at least 3 resumed tasks | user approval of a Stage 2 task prompt |
| 3 — Selective collaboration | smallest automated handoff between two clients, with ownership, boundaries, approval, errors and reconciliation; parallel work only with proven benefit | one automated sequential handoff Observed, with pilot data per §15.3 | user approval of a Stage 3 task prompt, which may be given only after the §17.2 hard gate is met |
| 4 — Measure and optimize | compare single and collaborative flows, reduce duplication, adjust routing | comparison report per §15 with sample size and limitations | user review of the report |
| 5 — Additional clients | add providers through FR-13 | new client passes step 5 of the add-a-provider procedure | user approval per provider |

## 17. Decisions

Decided at Gate A of [workshop-ai-product-foundation](../tasks/workshop-ai-product-foundation.md) on **2026-10-17**
by the product owner (the maintainer). Each decision may be reopened by a later gate.

1. **Product boundary:** a local command-line tool over the installed CLIs that reads this repository's catalogues.
   No web or desktop UI.  
   **Reopened 2026-10-18 by the product owner:** the product owner wants a Workshop AI **VS Code extension** as the
   main hub (client detection, infrastructure setup, opening and closing client terminals, saving context and
   continuing work in another client). Until the task that specifies it is approved and this decision is rewritten,
   the line above stands; that task is listed in the [task catalogue](catalogues/tasks.md).
2. **Invocation:** interactive client sessions plus a file-based manual handoff. Non-interactive modes (`claude -p`,
   `codex exec`) are **not** used by Workshop AI in Stage 1.  
   Provider terms checked 2026-10-17 (Documented; not legal advice):
   - Anthropic: Pro/Max OAuth supports ordinary use of Claude Code; `claude -p` and the Agent SDK on one's own plan
     draw from subscription limits; third-party apps may not offer Claude.ai login, route requests through plan
     credentials for others, or store Claude.ai credentials or tokens; an end user may sign in to the unmodified
     binary with their own plan.
     Sources: <https://code.claude.com/docs/en/legal-and-compliance>,
     <https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan>.
   - OpenAI: `codex exec` reuses the saved login; API keys are the recommended default for automation;
     ChatGPT-managed auth for automation only when one must run as one's own account, never for public or
     open-source repositories; API-key use bills API rates.
     Sources: <https://developers.openai.com/codex/noninteractive> (redirects to
     `learn.chatgpt.com/docs/non-interactive-mode`, observed 2026-10-17), <https://developers.openai.com/codex/auth>.  

   **Hard gate before Stage 3:** no automated or scripted client run is built until the user has re-confirmed, for
   each provider and plan, that the mechanism is allowed under the current terms, and that confirmation is recorded
   here with the source URL and date.
3. **Who runs the Stage 1 journey:** the user, from a step-by-step script; the agent then checks the resulting files.
4. **State storage:** Markdown or JSON files inside the project's repository, inspectable and editable by hand
   (rule in §13).
5. **Cross-provider sharing:** denied by default; the user reviews and approves each handoff package before another
   client reads it (FR-08). **Collaboration policy:** user-selected single-client mode by default; automatic routing
   only after evaluation (Stage 4).
6. **Pilot success:** three representative tasks on the sandbox project, acceptance criteria written before the run;
   each task runs once as a plain client session and once with the tool. Recorded per run: acceptance-criteria
   pass/fail, wall-clock time to an accepted result, user interventions, and `/context` and `/cost` figures where
   the client exposes them (meaningfulness of `/cost` on Pro/Max is to be verified); unavailable figures are N/A.
7. **Parallel conflicts:** independent work produces separate artifacts or branches first; one designated
   integrator reconciles, with user approval for consequential decisions. Not applicable before Stage 3.
8. **Projects and language:** the tool at `%USERPROFILE%\workshop\applications\workshop-ai\` and a sandbox at
   `%USERPROFILE%\workshop\applications\workshop-ai-sandbox\`, each its own git repository; Python standard library.
9. **Source files:** the v1.0 vision was moved from `tasks/` to this file; the unrevised reorganization draft was
   deleted (it was an untracked copy of a superseded task).

## 18. Acceptance Criteria for This Baseline

This baseline is ready when:

- the mission explains why Workshop AI exists beyond unifying client interfaces;
- single-client use stays simple and collaboration is selective and measurable;
- continuity and context management have explicit boundaries and a reviewable state model;
- efficiency is judged against outcome quality and end-to-end work, not token count alone;
- provider authentication, tools, permissions, context limits and billing are not assumed interchangeable;
- security, privacy, project isolation, approval and untrusted-input handling are requirements (FR-08, FR-09, §13);
- every FR has a priority and an observable check, and the Stage 1 NFRs (NFR-01, NFR-04) have a check;
- the existing baseline (§2.1) cites real paths;
- the §17 decisions are recorded with their date;
- development scope follows the roadmap gates (§16).

## 19. Final Product Principle

**Workshop AI should make the work of multiple AI clients more capable than disconnected individual use, but only
when coordination improves the result enough to justify its cost.**

Its success is not the number of clients connected, agents created or workflows orchestrated. It is better accepted
outcomes, less unnecessary effort, reliable continuity and responsible use of computational resources.
