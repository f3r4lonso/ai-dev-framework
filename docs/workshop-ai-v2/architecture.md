# Workshop AI v2: architecture

Status: **approved** (2026-10-20, with decisions D-V2-01…09). Builds on the delivered UI server
([web-architecture.md](../../../applications/workshop-infrastructure-ui/docs/web-architecture.md)) and the `wai`
Stage 1 spec ([stage-1-spec.md](../../../applications/workshop-ai/docs/stage-1-spec.md)). Paths assume decision
D-V2-02 (one repository); with two repositories, the same modules live in their current repos.

## 1. Components

```text
Browser (React 19 + Vite, Spanish UI)
   │  HTTP on 127.0.0.1 only · per-start token · same-origin checks
   ▼
server/  (Python stdlib HTTP server, from workshop-infrastructure-ui)
   ├── catalog        reads agents, skills, tasks, docs, applications (existing workshop_data)
   ├── documents      open / validate / diff / save / create / restore (existing resource_interaction + versions)
   ├── conversations  persisted chats and chains (existing agent_chains, made durable)
   ├── tasks          board, lifecycle, checkpoints, handoffs  ──► calls workshop_ai (the wai core)
   ├── engines        registry + one adapter per engine (existing client_dispatch, generalised)
   └── registration   wizard saves: catalogue row, inventory line, adapter regeneration
workshop_ai/  (the wai package: formats, tasks, checkpoint, handoff, scan; stdlib) ◄── also the `wai` CLI
```

Rule: the server never re-implements a `wai` format. Task, checkpoint and handoff operations go through
`workshop_ai` functions (or `wai … --json` in a subprocess if a function is not yet importable).

## 2. Where state lives

| State | Location | Format | Notes |
|---|---|---|---|
| Shared resources (agents, skills, briefs, docs) | `infra/` | Markdown, unchanged | canonical; public repo |
| Project task state | `<project>/.workshop-ai/` | `wai` formats (`task.md`, `project-state.md`, `handoffs/`) | vision §13: never in infra |
| Workshop-level tasks (no project) | `workshop/.workshop-ai/` (workspace root, not a repo) | same `wai` formats | allows tasks like "review the infra" |
| Conversations and chain runs | `workshop/.workshop-ai/conversations/<id>.json` | JSON, one file per conversation | survives restart; deletable from Historial |
| Run output, briefs for consoles, approvals | `workshop/.workshop-ai/runs/`, `briefs/`, `approvals/` | text / JSON | private local data; never in a repo (§8) |
| File versions made by the app | `workshop/.workshop-ai/versions/<sha-of-path>/<timestamp>-<uuid>.bak` | raw bytes; timestamp/ID derived from filename | outside every git repo; self-describing entries avoid a separate index/backup consistency gap |
| App settings (engine preference order, language) | `workshop/.workshop-ai/settings.json` | JSON | no credentials, ever |
| Drafts | browser memory, keyed by resource identity with its base hash | text | survive in-app navigation; unload warns; no browser-restart recovery promised; personal notes never enter localStorage |

Retention: versions keep the last 50 per file and anything newer than 90 days; conversations are kept until the
owner deletes them. A "Limpiar" action in Historial shows what will be removed first.

## 3. Task lifecycle

`task.md` gains one owned header field, `state`, alongside the existing `status`:

```text
borrador ─► en-cola ─► en-curso ─► esperando-aprobacion ─► hecha ─► archivada
                 ▲          │               │
                 └──────────┴── pedir-cambios
```

- Moving a card writes `state` and appends a History line; everything else in `task.md` is preserved (owned
  sections rule from the Stage 1 spec).
- A run started from a task records metadata only in `runs/<n>.json` next to `task.md` (engine, level,
  start/end, exit, usage if reported); the output itself lives in `workshop/.workshop-ai/runs/` so it never lands in
  a project commit — this is FR-10 (run log) of the v1 vision.
- Checkpoints and handoffs use `wai checkpoint` / `wai handoff` semantics unchanged; the app adds buttons and an
  approval screen. The in-app approval replaces the y/N terminal prompt only under the conditions in §8 (C1), and
  only after the `wai` approval rule is changed by decision.

## 4. Files: editing and versions

- **Allowlist** (extends the current `save` route): `.md` and `.txt` under `infra/{docs,tasks,agents,skills}/`,
  `applications/*/README.md`, `applications/*/docs/**`, `projects/music/**/*.md`, and the workspace root
  `INDEX.md` and `WORKSHOP-CONTEXT.md`. Everything in the current block list stays blocked (secrets, generated
  adapters, vendor, `.git`, client config folders, `pilot-results`). **Instruction files** (`AGENTS.md`,
  `CLAUDE.md`, `GEMINI.md`, `WORKSHOP-CONTEXT.md`, `INDEX.md`, `SKILL.md`) are editable only by the owner's own save,
  never by a level 4 apply or a chain output; `infra/AGENTS.md`, `infra/CLAUDE.md` and `infra/SECURITY.md` stay
  read-only in the app.
- **Save**: client sends `path`, `base_sha256`, new text → server re-resolves the path, checks the allowlist,
  compares the current hash (conflict → 409 with both texts), writes a version of the current bytes, writes the new
  text atomically (temp + `os.replace`), returns the new hash.
- **Header form**: today the server rejects any header change, because a partial parser could disagree with the
  adapter's parser. v2 lifts that lock only by using **the same parser as `infra/scripts/codex-adapter.py`**
  (shared module, not a copy); duplicate keys are rejected; unknown keys are preserved verbatim; changes to `tools`
  and `model` are shown as their own diff; `Agent` is never allowed in `tools` and `Bash`/web tools show a warning.
  If a file cannot be parsed safely, the form is disabled and only Modo avanzado is offered.
- **Create**: from templates in `infra/docs/manuals/templates/` (new), into an allowed folder; the new path is
  checked for collisions and naming (kebab-case).
- **Side effects after saving** an agent: regenerate adapters (`codex-adapter.py agents`, `personal` for personal
  assistants) as today, then run `--check`; a failure is shown and the version can be restored.
- **Restore** writes the chosen version through the same save path, so it is itself versioned.
- **Git stays the owner's**: the app never commits or pushes. Historial shows which repos have unsaved-to-git
  changes and suggests asking `git-workflow-manager`.

## 5. Agents and skills registration

A wizard save is one server transaction that prepares all changes, shows them as one diff set, and applies them
only after Guardar:

1. the agent file `infra/agents/<area>/<name>.md` or the skill folder `infra/skills/<name>/SKILL.md`;
2. a row in `infra/docs/catalogues/agents.md` or `skills.md` and a line in `infra/docs/inventory.md`;
3. the counts in `WORKSHOP-CONTEXT.md` and `infra/README.md`;
4. adapter generation (`codex-adapter.py agents` and `--check`; `link-skills --name <name>` for skills).

For agents, the preview includes the rendered Codex wrapper and the updated Claude plugin manifest. Saving
regenerates and checks those artifacts, then verifies that the generated bytes match the approved preview before
the transaction succeeds. A name collision with an existing Codex wrapper is rejected rather than overwritten.
The current wizard does not synchronize Copilot/Gemini or user/project copies. For skills, it creates only the
canonical definition and the shared `infra/clients/.agents/skills/` link; it does not install user/project copies.
The UI must state these limits and must not claim all-client installation or discovery.

Validation before Guardar (infra is a **public** repo): required keys present, name unique across agents and
skills, minimal `tools` from the known list, body not empty; the pre-commit secret patterns (and gitleaks when
installed) pass; no emails, account names or user-profile paths; `infra/.gitignore` will actually track the new
path. Text drafted by a model is labelled as such and never saved without the owner's diff review. The wizard
reminds the owner that Claude Code loads new agents only in a new session.

## 6. Engine adapters

One registry file `workshop_ai/engines.json` (read by the CLI and the server) lists each engine from
[engines.md](engines.md): id, display name, kind, executable name or URL, verified level, good-for text, guide
link. Each adapter implements only what its level allows:

| Method | Level | Notes |
|---|---|---|
| `detect()` | all | PATH lookup outside the workspace, `--version` with a 5 s timeout |
| `open_link()` / `copy_text()` | 0 | URL from the registry, never from the browser |
| `open_console(folder, brief_id?)` | 1 | Windows Terminal, fixed argument list; `folder` must be a registered project root from the server's own list; the brief is **never** put in argv (see §8 C2) |
| `ask(profile, messages) → stream` | 2 | tool-free, temp working directory; Claude: current `client_dispatch` flags; Ollama: loopback HTTP; Codex/Gemini/Copilot: after their checks |
| `run_task(task, tools="read")` | 3 | filtered read-only copy of the project, per-engine flag set (§8 H1) |
| `run_task(task, tools="edit")` | 4 | temp copy **without `.git`** (§8 C3); the server builds the diff; applied only on Aprobar through the versioned save path |

Limits per run (from the current dispatch): timeout, input/output caps, stdin only, `shell=False`, one run per
engine, usage parsed only from the engine's own structured output.

## 7. Security model

Kept exactly from the delivered UI server (do not weaken): loopback bind on 8770–8790 with exclusive address use;
Host header check; per-start random token on every POST, compared in constant time; exact same-origin Origin on
interaction routes; no CORS; strict CSP, `nosniff`, `X-Frame-Options: DENY`, `no-referrer`, `no-store`; JSON-only
bodies with size caps; chunked encoding rejected; workspace-relative paths only, no `..`, drives, dot segments,
junctions or symlinks; block lists for secrets and client config; executables from absolute PATH entries outside
the workspace; no request data on command lines; escaped rendering of all user and model text; no content in logs.

New in v2 and required before the matching increment ships:

- **Writes**: allowlist re-checked server-side on every write; versions written before every change; write lock.
- **Conversations folder**: may contain sensitive text; it lives outside repos and is listed in the security doc as
  private local data.
- **Level 3–4 runs**: read-only tool allowlist per engine; level 4 only in an isolated copy; no network tools unless
  the owner enables them per run; untrusted-output labelling between chain stages stays.
- **Handoffs**: unchanged `wai` scan + hash-locked manifest; the in-app approval is bound to the manifest hash.
- **Review**: `security-reviewer` reviews V2, V3 and V6 before they are called done.

## 8. Required design changes from the security review (2026-10-20)

A read-only `security-reviewer` pass on this design found three critical, five high and four medium issues. These
requirements are binding; an increment that touches the area cannot pass Gate B without them.

| ID | Sev | Requirement |
|---|---|---|
| C1 | Critical | **In-app approval.** Today `wai` approval needs a person at a terminal so an AI session's shell cannot approve, while the page token is readable by any local process. An in-app approval is accepted only while no level 3–4 run is active, requires a typed confirmation in the page, and is recorded in `workshop/.workshop-ai/approvals/<package>.json` against the SHA-256 of the manifest **excluding** its `approval` field; `wai handoff show` checks that record. Engines that can run shell commands or reach loopback HTTP never get level 3+ while this applies. It replaces the terminal rule only after a recorded decision changes the `wai` AGENTS.md. |
| C2 | Critical | **Console first message.** `wt … cmd /k` treats `;` and `& \| ^ %` as syntax, so a brief in argv is command injection. The server writes the brief to `workshop/.workshop-ai/briefs/<id>.md` and passes only a fixed server-built sentence pointing to that file; if the CLI cannot take it, the brief goes to the clipboard (the UI notes that other apps can read the clipboard). |
| C3 | Critical | **Level 4 isolation.** A git worktree shares `.git` (hooks, config). The copy is a temp folder without `.git`, `.workshop-ai`, dot-folders or secret-pattern files; the server computes the diff (`difflib`); only text files that pass the save allowlist are applied, never `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/`, `.codex/`, `.gemini/`, `.github/`, `.githooks/`, `.mcp.json`, package manifests, lockfiles, links or binaries; each file goes through the versioned save path. |
| H1 | High | **Level 3 neutralisation.** Each engine needs a written, tested flag set that disables project settings, hooks and MCP and allows only Read/Grep/Glob (no shell, web, sub-agents). Level 3 reads a filtered copy without secret-pattern files. Codex level 3 also needs a verified network block. Output is secret-scanned before it is stored. |
| H2 | High | **Workshop-level tasks** run at level 2, or level 3 on an explicit file list only. No engine run ever sees `workshop/.workshop-ai/`. |
| H3 | High | **Header editing** uses the adapter's parser (see §4). |
| H4 | High | **Wizard writes to a public repo** with the checks in §5. |
| H5 | High | **Instruction files** are owner-save only (see §4); `projects/**` narrowed to `projects/music/**/*.md`. |
| M1 | Medium | Every route that returns conversation, version, run, approval or task text requires the token (today only POST does). |
| M2 | Medium | Run output stays in `workshop/.workshop-ai/runs/`; projects keep metadata only (see §3). |
| M3 | Medium | Automático shows the chosen engine and whether it is local or cloud before sending; moving from Ollama to a cloud engine needs a confirmation. |
| M4 | Medium | `workshop/.workshop-ai/` is excluded from the catalogue, reader, handoff packages and engine copies; it must not be inside a synced folder (e.g. OneDrive); conversations get a default retention; deleting one removes its version copies; Historial flags items that fail the secret scan. |
| M5 | Medium | D-V2-04/05 and C1 are applied together with edits to both apps' rules files; no rule is overridden only by this document. |
| L1 | Low | Ollama install goes through `dependency-license-review`; `OLLAMA_HOST` held to 127.0.0.1; each model pull approved. |
| L2 | Low | Adapter regeneration output is shown (today it goes to DEVNULL) together with the `--check` result. |
| L3 | Low | Copilot (empty `--available-tools`) and Gemini (`--approval-mode plan`) stay at level 2 until a local test proves tools are really off; `plan` mode is not isolation. |
