# Workshop AI v2: review of the existing documents

Status: review record (2026-10-20). Read-only reviews by four agents (Workshop AI documents and code, UI documents
and code, engine audit, UX research), consolidated here. VS Code extension documents were only noted, not reviewed.

## 1. What exists

**Workshop AI (`wai`)** — 50 tests pass. Built: `init`, `resources`, `status`, `task new`, `context add|remove|list`,
`start`, `resume`, `checkpoint`, `handoff create|approve|show`; `--json` (schema `wai.v1`) on five commands,
uncommitted. Only Claude Code is launched; Codex is a handoff target only. Never observed end to end: the sandbox
pilot results file is empty, and a stray empty task `321` sits in the sandbox.

**Workshop Infrastructure UI** — 104 tests pass, 1 skipped. Built: Spanish browser app with eight sections, search,
filters, reader (clean, Ollama translation, speech), console launch for Claude/Codex/Gemini/Copilot, tool-free
Claude dispatch and 2–5 step chains (memory only). Server routes `save` and `dispatch` exist and are tested but no
screen uses them. No `wai` integration.

## 2. Contradictions and stale facts

| # | Finding | Where |
|---|---|---|
| 1 | "No web UI and no stand-alone desktop application" vs a working web UI and a discovery brief that reopens the question | vision §17.1; foundation task §3; [desktop discovery brief](../workshop-ai-desktop-app-discovery-brief.md) |
| 2 | "Interactive sessions only / never `claude -p`" vs the UI's `claude -p` chains | ai-architecture §9; `wai` AGENTS.md; UI `client_dispatch.py` |
| 3 | "No daemon, service or network listener" vs the UI's loopback server | `wai` AGENTS.md |
| 4 | "Never writes files" vs the `save` route that writes and regenerates adapters | UI web-architecture §3–§4 |
| 5 | "Only processes started are the four client commands" — also `claude --version`, `claude -p`, `codex-adapter.py` | UI web-architecture §3 |
| 6 | Editing/dispatch "remain required scope" vs "optional future editing/dispatch" | UI brief vs task catalogue row |
| 7 | "Task and application commands stay as text to copy" — the copy UI was removed | UI README |
| 8 | `--add-dir "<infra>\clients"` still used though the plugin replaced it | `wai` `clients.py`, stage-1 spec §6/§11.2, sandbox user script, inventory.md |
| 9 | User script asks to type `reviewed` when gitleaks is missing; gitleaks is now installed | stage-1 spec §8.4, sandbox user script |
| 10 | "Codex CLI not on PATH" — Codex 0.163.0 is installed | foundation task §2 |
| 11 | Open register ends at R9; Copilot plan adds R10–R12; extension spec says R1–R8 | vision §17.11 |
| 12 | Handover file referenced but missing | foundation task → `workshop-ai-stage-1-handover.md` |
| 13 | Client lists differ: `wai` (claude, codex), UI (+gemini, copilot), neither has dsh/Ollama | [engines.md §4](engines.md#4-inconsistencies-found-to-fix-in-v0) |
| 14 | Reading assistant documented as "Gemini via REST"; code uses local Ollama, not installed | WORKSHOP-CONTEXT §2; reading-assistant project page |
| 15 | Test counts drift (71 / 91 / 95 / 102 vs 104 actual) | UI ui-review, interaction-upgrade |
| 16 | `ui-development-plan.md` still describes PowerShell/WinForms, "no chat, no client launching" | UI docs |
| 17 | Brief filename says "windows-ui" for a browser app | `infra/tasks/projects/workshop-infrastructure-ui/workshop-infrastructure-windows-ui.md` |
| 18 | Agent/skill counts disagree across ai-architecture, inventory and client guides | engines.md §4 item 7 |

Duplicated content (to stop copying, link instead): security rules (4 places), chain behaviour (6 places), stage
descriptions (4 places), approval rule (4 places), pilot design (3 places).

## 3. What happens to each existing document

| Document | v2 status | Action |
|---|---|---|
| [workshop-ai-product-vision.md](../workshop-ai-product-vision.md) | Kept, partly superseded | Banner pointing to v2 [product-vision.md §7](product-vision.md#7-what-changes-in-the-v12-vision-once-approved) |
| [workshop-ai-desktop-app-discovery-brief.md](../workshop-ai-desktop-app-discovery-brief.md) | Answered by v2 | Banner: question resolved by D-V2-01 (local web app, not desktop) |
| [vscode-extension-technology-research.md](../vscode-extension-technology-research.md) | Paused | Banner: out of scope for v2 |
| [projects/workshop-ai/README.md](../projects/workshop-ai/README.md) | Updated | Points to v2 |
| [projects/workshop-infrastructure-ui/README.md](../projects/workshop-infrastructure-ui/README.md) | Updated | Points to v2; marked "merging into Workshop AI" |
| [tasks/projects/workshop-ai/workshop-ai-product-foundation.md](../../tasks/projects/workshop-ai/workshop-ai-product-foundation.md) | Active until its pilot runs | Pilot becomes part of V1; then completed |
| [tasks/projects/workshop-ai/workshop-ai-token-optimization-integration.md](../../tasks/projects/workshop-ai/workshop-ai-token-optimization-integration.md) | Active, blocked | Becomes V7; the extension wording no longer applies |
| [tasks/projects/workshop-infrastructure-ui/workshop-infrastructure-windows-ui.md](../../tasks/projects/workshop-infrastructure-ui/workshop-infrastructure-windows-ui.md) | To be superseded | Superseded by the v2 task once D-V2-01 is approved |
| [tasks/projects/workshop-ai/workshop-ai-vscode-extension-specification.md](../../tasks/projects/workshop-ai/workshop-ai-vscode-extension-specification.md) | Completed record | No change |
| `applications/workshop-ai/docs/stage-1-spec.md` | Current (core) | Fix items 8–9 in V0 |
| `applications/workshop-ai/docs/stage-1-completion-plan.md` | Draft | Folded into V1 |
| `applications/workshop-ai/docs/stage-2-context-store-plan.md` | Draft | Folded into V7 |
| `applications/workshop-ai/docs/copilot-and-console-buttons-plan.md` | Partly superseded | Part A (Copilot adapter) → engines registry; Part B VS Code items paused; B1 `wai console` kept |
| `applications/workshop-ai/docs/vscode-extension-*.md`, `adr/0001` | Paused | Banner |
| `applications/workshop-infrastructure-ui/docs/web-architecture.md` | Current until merge | Fix items 4–5 |
| `applications/workshop-infrastructure-ui/docs/ui-development-plan.md` | Historical | Banner: superseded |
| `applications/workshop-infrastructure-ui/docs/ui-review.md`, `interaction-upgrade.md`, `agent-chain-design.md` | Records | Kept; linked from v2 |

## 4. Fixes to make in V0

1. Apply the banners in §3 (done with this document set where the file is in `infra/` or an application's `docs/`).
2. Remove `--add-dir` from `wai` `clients.py`, the stage-1 spec, the sandbox user script and inventory.md
   (code change: V1).
3. Correct the gitleaks instruction in the stage-1 spec and user script.
4. Update foundation task §2 (Codex installed, plugin replaces the junction).
5. Add R10–R12 to the vision register; correct the extension spec header.
6. Fix web-architecture §3–§4 ("never writes files", process list) and the UI README copy-text sentence.
7. Rename the UI brief when it is superseded (keep the old file with a superseded status line).
8. Correct the reading-assistant engine (Ollama, not Gemini) in WORKSHOP-CONTEXT and its project page.
9. Add Copilot and Gemini columns to the compatibility matrix; fix the client-list contract (exclude `suno`,
   include `personal` as a separate kind); add Ollama, Claude Desktop and claude.ai Projects to the inventory.
10. Reconcile agent/skill counts in one pass with `ai-environment-auditor`.
11. Delete the stray sandbox task `321` and the `.preview-edge/` profile folder in the UI repo (owner approval).
