# Workshop AI v2: roadmap

Status: **approved** (2026-10-20, with decisions D-V2-01…09). Each increment ends with tests, a row in the progress file
(`applications/workshop-ai/docs/v2-progress.md`), and the
owner's OK before the next starts. Commits only with the owner's approval. Run through the
[task brief](../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md).

| Inc. | Name | Delivers (requirements) | Acceptance | Gate |
|---|---|---|---|---|
| V0 | Decisions and cleanup | Owner approves D-V2-01…09 (answers recorded in product-vision §6); both apps' rules files updated to match; stale facts fixed ([document-review.md §4](document-review.md#4-fixes-to-make-in-v0)); old docs get status banners | Every fix in the list is done or explicitly deferred; INDEX and context updated | Owner approves decisions |
| V1 | One app, every engine visible | Repo merge (D-V2-02) or path import; shared engine registry; Motores section with all ten engines (V2-FR-01, 02); `wai` reads the plugin, not `--add-dir`; Stage 1 sandbox pilot run once through the CLI | All existing tests pass in the merged repo (≥ 154); pilot results recorded; Motores shows correct levels | Owner first-use session (15 min, observed, notes recorded) |
| V2 | Edit files safely | Editor with header form, Modo avanzado, diff, versions, restore, create from template (V2-FR-03, 04, 05, 19) | Tests for allowlist, conflict, restore, unknown-key preservation; `security-reviewer` pass | Owner edits one agent and restores it |
| V3 | Talk to agents | Conversar with agent + engine pickers, saved conversations, chains persisted, usage line (V2-FR-06, 15, 17); Claude level 2; Ollama level 2 after install | Conversation survives restart; chain stop works between stages; `security-reviewer` pass | Owner asks two agents a question |
| V4 | Tasks you can follow | Board, task page, "Guardar como tarea", "Empezar en…" (console with brief), checkpoints in the app (V2-FR-07…10) | Board and `wai status` agree; hand edit of `task.md` shows after refresh | Owner runs one real task end to end |
| V5 | Add agents and skills | Wizard, validation, test chat, automatic registration (V2-FR-13, 14) | New agent visible in a fresh Claude Code session; adapter `--check` passes | Owner creates one skill |
| V6 | Engines do more | Handoff in the app and approvals inbox (V2-FR-11, 12); level 3 for Claude, then Codex/Gemini only when architecture §8 C1/H1/L3 are met; level 4 for Claude in an isolated copy without `.git` (V2-FR-16) | Edits never reach the real folder before Aprobar; R7 result recorded per engine; `security-reviewer` pass | Owner approves the level-4 design |
| V7 | Spend fewer tokens | Stage 2 store, recap, compress surfaced in the task page; global search (V2-FR-18, 20) | Benchmark per the [Stage 2 plan](../../../applications/workshop-ai/docs/stage-2-context-store-plan.md), reported as Measured/Simulated/N/A | Owner reviews the benchmark |

Dependencies: V1 before everything; V2 before V5 (the wizard reuses the editor); V3 before V4's "Guardar como
tarea"; Ollama installed before V3 closes; R7 per engine before that engine reaches level 2+.

Agents and skills to use per increment (all exist; check the catalogues before proposing new ones):

| Increment | Agents | Skills |
|---|---|---|
| V0 | `ai-environment-auditor` (apply mode for infra fixes), `prompt-reviewer` (task brief) | `engineering-lifecycle` |
| V1 | `python-pro`, `frontend-developer`, `code-reviewer` | `python-testing-patterns`, `javascript-testing-patterns` |
| V2 | `frontend-developer`, `ui-designer`, `security-reviewer`, `accessibility-expert` | `ui-ux-pro-max`, `interaction-design`, `wcag-audit-patterns` |
| V3 | `backend-architect`, `frontend-developer`, `security-reviewer` | `python-resilience`, `react-state-management` |
| V4 | `python-pro`, `ux-researcher`, `ui-ux-tester` | `api-design-principles` |
| V5 | `ai-environment-auditor`, `frontend-developer` | `design-system-patterns` |
| V6 | `security-reviewer`, `backend-architect`, `debugger` | `python-error-handling` |
| V7 | `python-pro` | (Stage 2 plan) |
