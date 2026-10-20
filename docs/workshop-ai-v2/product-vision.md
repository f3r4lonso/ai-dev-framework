# Workshop AI v2: product vision and requirements

Status: **approved** (2026-10-20; every decision in §6 approved by the owner). This file supersedes the parts of
[workshop-ai-product-vision.md](../workshop-ai-product-vision.md) (v1.2) listed in §7. Everything not listed there
(knowledge categories, measurement rule, handoff rules) stays in force and is referenced, not copied.

## 1. Who it is for

The owner is a trader, not a developer, working in Spanish on a Windows laptop. They think of the Workshop as **a
team of assistants**, not as files, git or command lines. What they want to be able to say:

| Job | Today |
|---|---|
| "Give an assistant a job and see it done" | Only by opening a terminal and typing; chains are text-only |
| "Pick the right assistant and engine without knowing the difference" | Four equal console buttons, no guidance; three engines missing |
| "Change an assistant's instructions safely" | Edited outside the app; fear of breaking frontmatter |
| "Add a new assistant or skill" | Manual: file, catalogue row, inventory line, adapter regeneration |
| "Know what is running, what waits for me and what it costs" | Not visible; chain runs vanish on restart |
| "Pick up yesterday's work" | `wai resume` in a terminal; invisible in the UI |

## 2. Goals

1. **Edit any Workshop document from the app**, safely: a form for the header, a comfortable editor for the body,
   a "Revisar cambios" preview before saving and a version list with one-click restore.
2. **Talk to any agent and give it a task** from one composer: choose the agent, choose the engine (or
   "Automático"), get the answer, keep the conversation, turn it into a task.
3. **Track tasks**: a board with clear states, an "Esperando mi aprobación" inbox, live output, checkpoints and
   hand-offs between engines.
4. **Add agents and skills** with a guided wizard from templates, with validation and a test chat, and have the
   catalogues, inventory and client adapters updated automatically.
5. **Every registered engine in one place**, each with an honest status and a capability level
   ([engines.md](engines.md)).
6. **Easy to maintain**: one source of truth per kind of state, plain files the owner could read, nothing that
   disappears on restart, and documents that stay consistent with the code.

## 3. Principles

- **Spanish, plain words.** No "commit", "YAML", "frontmatter", "worktree" or "stdin" on screen. Each resource gets
  a short Spanish summary next to its English description.
- **Nothing changes without the owner seeing it.** Every file change and every agent edit goes through a diff and
  an explicit Guardar / Aprobar. No silent engine switch, no silent spend.
- **Every run is started by the owner.** No schedules, no background agents, no automatic retries in v2.
- **Files are the truth.** Task state stays in the `wai` Markdown formats; the app reads and writes them and keeps
  hand edits. A database, if ever used, is only a cache that can be rebuilt.
- **Honest capability.** An engine is shown at the level that is verified, with the reason when a feature is not
  available. "Installed" is never presented as "signed in".
- **Keep what is safe.** The UI server's security model ([architecture.md §7](architecture.md#7-security-model))
  and the `wai` handoff rules (scan, hash-locked manifest, approval) are kept, not weakened.
- **Reuse before building.** Extend the existing React app and the `wai` package; no new framework, no new
  runtime dependency without the dependency review and approval.

## 4. Scope

In scope for v2: the browser app; the `wai` core used as a library; engine registry and adapters; document editing
with versions; conversations; task board; agent/skill wizard; persisted agent chains; Spanish summaries.

Out of scope for v2: the VS Code extension (paused); a stand-alone desktop installer; scheduled or unattended runs;
automatic engine routing without a visible suggestion; driving Suno or claude.ai by automation (forbidden by their
guides); real trading anything (the Trading-app rules are untouched); remote access from another device.

## 5. Requirements

Priority: **P0** needed for the first usable release (V1–V4 in the [roadmap](roadmap.md)), **P1** next, **P2**
later. Each requirement has a check that decides when it is met.

| ID | Requirement | Pri | Check |
|---|---|---|---|
| V2-FR-01 | Single app shell with the navigation in [ux-design.md §2](ux-design.md#2-navigation) | P0 | All seven sections reachable by mouse and keyboard |
| V2-FR-02 | Engine registry lists every engine in [engines.md](engines.md) with status (instalado, sesión, nivel) and a "Probar" check | P0 | Ten engines shown; each non-available feature shows its reason |
| V2-FR-03 | Open and edit any allowed Markdown/text document: header form + body editor + raw "Modo avanzado" | P0 | Edit, preview diff, save, reopen shows the change |
| V2-FR-04 | Version history for every save made by the app, with compare and restore | P0 | Restore returns the exact previous bytes; a restore is itself a version |
| V2-FR-05 | Create a new document from a template (task brief, plan, note, project doc) in an allowed folder | P1 | New file appears in its section and in `INDEX.md` |
| V2-FR-06 | "Conversar": composer with agent picker and engine picker; answers rendered as text; conversations saved | P0 | A conversation survives a server restart |
| V2-FR-07 | "Guardar como tarea" turns a conversation into a `wai` task with objective, context and next action | P0 | A `task.md` in the `wai` format exists and opens on the board |
| V2-FR-08 | Task board with states Borrador, En cola, En curso, Esperando mi aprobación, Hecha, Archivada | P0 | Moving a card updates `task.md`; a hand edit to `task.md` shows on the board after refresh |
| V2-FR-09 | Task page: objective, acceptance criteria, decisions, checkpoints timeline, runs, files changed | P0 | Matches `wai status` for the same task |
| V2-FR-10 | Start a task in an engine: console with the task brief preloaded (level 1) or an in-app run (level 2+) | P0 | Claude console opens in the task's project with the brief as first message |
| V2-FR-11 | "Pasar a otro motor": builds a `wai` handoff, shows the scan and the package, asks approval | P1 | Same manifest and approval rules as `wai handoff` |
| V2-FR-12 | Approvals inbox: every pending diff, handoff or run result in one list with Aprobar / Pedir cambios | P1 | Nothing pending is reachable only from elsewhere |
| V2-FR-13 | Agent and skill wizard: template, name, purpose, instructions, tools, default engine, test chat, save | P1 | New agent loads in a fresh Claude Code session and in the generated Codex adapter check |
| V2-FR-14 | Registration is automatic: catalogue row, inventory line, Spanish summary, adapter regeneration, counts | P1 | `codex-adapter.py agents --check` passes after a wizard save |
| V2-FR-15 | Agent chains persisted to disk, resumable view after restart, stoppable between stages | P1 | Restarting the server keeps the last three runs |
| V2-FR-16 | Tool-using runs (read-only first, then edits in an isolated copy with diff approval) per engine level | P2 | Edits never touch the real folder before Aprobar |
| V2-FR-17 | Usage line per run (time, tokens or quota where the engine reports it; "no disponible" otherwise) | P1 | Never shows invented numbers |
| V2-FR-18 | Global search across resources, tasks, conversations and versions | P1 | Finds a word typed in yesterday's conversation |
| V2-FR-19 | Spanish summary field for agents, skills and tasks, shown in the UI | P1 | No English-only card in the library |
| V2-FR-20 | Token-saving features from the [Stage 2 plan](../../../applications/workshop-ai/docs/stage-2-context-store-plan.md) (store, recap, compress) surfaced in the task page | P2 | Measured against the baseline per vision §15 |

Non-functional (keep the v1 NFRs; additions):

| ID | Requirement |
|---|---|
| V2-NFR-01 | Local only: loopback server, no remote access, no telemetry |
| V2-NFR-02 | Works with only Python stdlib on the server and the four pinned front-end packages; new packages need the dependency review |
| V2-NFR-03 | A crash or restart loses nothing saved; unsaved drafts are kept per document in the browser |
| V2-NFR-04 | Keyboard reachable, visible focus, 200 % zoom usable, WCAG 2.2 AA contrast |
| V2-NFR-05 | Every write is atomic, version-checked and re-validated against the allowlist on the server |

## 6. Decisions to approve

Each decision changes an earlier rule; nothing is changed until the owner approves it. Recommended option first.

| ID | Decision | Recommended | Replaces | Decision (date) |
|---|---|---|---|---|
| D-V2-01 | One product: the browser app is the Workshop AI user interface; `wai` is its core library and stays a CLI | Approve | Vision §17.1 "no web UI"; foundation task "no web or desktop UI"; UI brief "keep separate from Workshop AI" | approved (2026-10-20) |
| D-V2-02 | One repository: move the UI (`server/`, `web/`, `tests/`) into `applications/workshop-ai/` next to `workshop_ai/`; retire the `workshop-infrastructure-ui` repo as read-only history | Approve (alternative: keep two repos and import `workshop_ai` by path) | Two separate project pages and briefs | approved (2026-10-20) |
| D-V2-03 | Pause the VS Code extension; keep `vscode-extension/` and its docs as a record; keep the `--json` output in `wai` because the app uses it | Approve | Vision §16 Stage 2 "observed through the extension" | approved (2026-10-20) |
| D-V2-04 | Allow a local loopback server in Workshop AI, with the UI server's security model as the minimum | Approve | `wai` AGENTS.md "no daemon, service or network listener" | approved (2026-10-20) |
| D-V2-05 | In-app (headless) engine runs are allowed when the owner starts each one, per engine level in [engines.md](engines.md); tool-free first | Approve, subject to R7 below | ai-architecture §9 "interactive sessions only"; `wai` AGENTS.md "never non-interactively" | approved (2026-10-20) |
| D-V2-06 | R7 (provider terms for scripted use of subscription logins): check each provider's current terms before enabling its level 2+, and record the result in its client guide | Approve | Vision §17.11 R7 stays open per engine | approved (2026-10-20) |
| D-V2-07 | The app may write files, limited to the allowlist in [architecture.md §4](architecture.md#4-files-editing-and-versions), with versions kept in a workspace state folder outside every git repo | Approve | UI "never writes files" wording | approved (2026-10-20) |
| D-V2-08 | Console buttons do not ask for approval when they open an empty console; they do ask when they start a task (the brief is shown first) | Approve | Copilot plan B "approve every console" | approved (2026-10-20) |
| D-V2-09 | Install Ollama (task [`ollama-install`](../../tasks/projects/ollama/ollama-install.md)) before V3 so a private local engine exists | Approve | — | approved (2026-10-20) |

## 7. What changes in the v1.2 vision once approved

| v1.2 section | Change |
|---|---|
| §16 Stages | Stage 2 becomes "unified app V1–V4" here; the extension is removed from the stage exits |
| §17.1 | Replaced by D-V2-01, D-V2-03, D-V2-04 |
| §17.11 register | R7 handled per engine (D-V2-06); R10–R12 from the Copilot plan added |
| FR-01 client registry | Implemented by V2-FR-02 with the levels in [engines.md](engines.md) |
| FR-05 / FR-08 handoff and approval | Unchanged; surfaced by V2-FR-11 and V2-FR-12 |
| §11 knowledge, §12 tokens, §13 state location, §15 measurement | Unchanged and binding |
