# Discovery brief — Workshop AI as a Windows desktop app

Status: active (discovery, 2026-10-18). For the `product-idea-excavator` agent. No implementation.

## 1. How to use this brief

Start Claude Code in `%USERPROFILE%\workshop` (the shared agents load from there) and say:

> "Usa el agente product-idea-excavator con el brief `infra/docs/workshop-ai-desktop-app-discovery-brief.md`."

The agent interviews the user, then delivers the idea brief described in §6. It reads files and may search the web;
it changes nothing.

## 2. The user's idea (their words, summarized)

A Windows desktop application where the user can **work with all their AI clients (Claude Code, Codex CLI, Copilot
CLI, others later) from one chat**, in order to:

1. **save tokens**;
2. **keep a shared infrastructure of agents and skills** that improves the work;
3. **save task context locally in Markdown files**, so any AI engine can continue a task another engine started;
4. **use different clients for different things**.

The user also wants help to **understand and order the existing documents** and turn them into a buildable project.

## 3. What already exists (verified 2026-10-18; re-check before relying on it)

Read these instead of asking the user to repeat them. Paths are relative to `%USERPROFILE%\workshop`.

| Document | What it is | Status |
|---|---|---|
| `infra/tasks/unified-ai-engineering-infrastructure-prompt.md` | First brief for shared Claude/Codex infrastructure | superseded |
| `infra/tasks/unified-ai-client-workshop-reorganization.md` | Early draft of the same reorganization | superseded |
| `infra/tasks/ai-infrastructure-unification-and-workshop.md` | Built the shared infrastructure (agents, skills, client guides, catalogues) | completed 2026-10-17 |
| `infra/tasks/homero-self-improvement-and-prompt-reviewer-task.md` | Improved the Homero prompt; added `prompt-reviewer` | completed 2026-10-17 |
| `infra/tasks/workshop-ai-product-foundation.md` | Product baseline and Stage 1 (`wai` CLI) | active: built, pilot not run, not closed |
| `infra/tasks/workshop-ai-token-optimization-integration.md` | Stage 2 POC: knowledge store, output compression, switch recap | active, blocked until the foundation task completes |
| `infra/docs/workshop-ai-product-vision.md` (v1.2) | **Governing vision**: requirements, roadmap §16, decisions §17, open decisions §17.11 | current |
| `applications/workshop-ai/` | Product repository: `wai` (Python stdlib), docs, tests, `vscode-extension/` | Stage 1 committed; extension E1 uncommitted |
| `applications/workshop-ai/docs/vscode-extension-spec.md`, `copilot-and-console-buttons-plan.md` | VS Code hub specification; Copilot CLI and per-client console buttons plan | proposed / owner decisions 2026-10-18 |
| `applications/workshop-ai-sandbox/` | Test project and pilot definitions | pilot results empty |

Key facts:

- **Already built (Observed in Stage 1):** `wai` creates a task contract, attaches selected context, starts Claude
  Code interactively after approval, saves a checkpoint (decisions, verified state) as Markdown/JSON in the project,
  resumes it, and builds a user-approved handoff package for another client. Ideas 2 and 3 in §2 are largely covered.
- **Decided 2026-10-18 (vision §17.1):** the main UI is a **VS Code extension** over `wai`; the record says *"no
  stand-alone desktop application"*. The new idea reopens this decision.
- **No evidence yet:** the Stage 1 pilot (plain session vs. `wai`, 3 tasks) has not been run. No token or effort
  saving can be claimed (vision §15).
- **Hard constraint (vision §17.2, §17.11 R4, R7):** Workshop AI starts clients only as interactive sessions. Any
  scripted or automated run (`claude -p`, `codex exec`, SDK) needs the user's recorded re-confirmation of each
  provider's terms. Anthropic's documented terms (checked 2026-10-17) do not let third-party apps offer Claude.ai
  login or route requests through plan credentials. A single chat box that drives several clients behind the scenes
  probably falls under this rule and may need API keys with usage billing. Verify against current official terms;
  do not assume.

## 4. Questions to resolve with the user (ask a few at a time, in Spanish)

1. **Why a desktop app now instead of the VS Code extension?** What concretely failed or is missing in VS Code?
   If the answer is only "a separate window", say that the extension may already cover it.
2. **What does "one chat" mean?**
   - (a) One window with a tab or panel per client; each client runs its own visible interactive session and the app
     saves and passes context at a switch: allowed, mostly built.
   - (b) One conversation box where one message goes to several clients and they read each other's replies:
     needs scripted runs, so it hits the §3 terms constraint and likely API billing. This is the riskiest assumption.
3. **Last real occurrence of the problem:** which client, which task, what was lost (time, re-explaining, limits
   hit)? Which client runs out first?
4. **Who is it for:** only the user, or other people later?
5. **Token saving:** saving the user's subscription limits, money, or time? How will they know it worked?

## 5. Working hypotheses (label as assumptions until confirmed)

- The real pain is continuity when a client hits its limit, not the number of windows.
- The cheapest test of value is the **existing Stage 1 pilot** (3 sandbox tasks, each with and without `wai`,
  acceptance criteria written first, vision §17.6), about one afternoon of the user's time, before any new UI.
- A desktop shell, if justified, would be a thin UI over `wai` (same backend decision as vision §17.10 D1), so the
  choice desktop vs. VS Code changes the packaging, not the core.

## 6. Expected output

An idea brief in the agent's format, in Spanish for the conversation and English for any file:

- working title; people affected and context; problem and current workaround;
- need served; proposed outcome and why it matters;
- evidence vs. assumptions vs. open questions (cite §3 paths);
- recommendation on desktop app vs. VS Code extension vs. both, with trade-offs;
- smallest useful project or experiment, and what is out of scope;
- feasibility, dependencies, provider-terms risk;
- success measures and **one** next step.

If the user decides to change the product boundary, the hand-off is an update to vision §17.1 through a new task
prompt in `infra/tasks/` (user approval required); the excavator does not edit it.

## 7. Boundaries

- Read-only. Do not edit `infra/`, `applications/` or this file; do not run `wai`, clients, installs or commits.
- Do not claim token savings, market demand or provider permissions without evidence; cite official sources with
  date for any terms check.
- Never read credentials or client session files.
