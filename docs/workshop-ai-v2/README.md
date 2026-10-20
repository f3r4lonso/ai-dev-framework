# Workshop AI v2: unified product documents

Status: **approved** (decisions D-V2-01…09 approved by the owner on 2026-10-20); V0 done, V1 next. The decisions are
listed in [product-vision.md §6](product-vision.md#6-decisions-to-approve).

Workshop AI v2 merges two things that grew apart into **one local app**:

- **Workshop AI (`wai`)**: the command-line core that keeps verified task state, checkpoints and reviewed handoffs
  ([applications/workshop-ai](../../../applications/workshop-ai/README.md)).
- **Workshop Infrastructure UI**: the local browser app that shows every Workshop resource, reads documents aloud
  and runs bounded Claude agent chains ([applications/workshop-infrastructure-ui](../../../applications/workshop-infrastructure-ui/README.md)).

Version 2 is one browser app, in Spanish, where the owner edits files, talks to agents, gives them tasks, adds
agents and skills, and uses **every AI engine registered in the Workshop** from one place. Task state and history
stay in plain files. The VS Code extension is **out of scope** for v2: it is paused, not deleted (see
[document-review.md §3](document-review.md#3-what-happens-to-each-existing-document)).

## Documents

| Document | What it answers |
|---|---|
| [product-vision.md](product-vision.md) | Who it is for, goals, principles, scope, requirements (V2-FR), decisions to approve |
| [ux-design.md](ux-design.md) | Navigation, screens, main flows and Spanish wording rules |
| [engines.md](engines.md) | Every AI engine in the Workshop, its capability level in the app and what unlocks the next level |
| [architecture.md](architecture.md) | Components, state model, file editing and versions, task lifecycle, engine adapters, security |
| [roadmap.md](roadmap.md) | Increments V0–V7 with acceptance criteria and approval gates |
| [document-review.md](document-review.md) | Review of every existing Workshop AI / UI document: status, contradictions, stale facts, fixes |
| [Task brief](../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md) | The task to run, increment by increment, once the decisions are approved |

## Reading order

Owner: this page → [product-vision.md](product-vision.md) §1–§3 and §6 → [ux-design.md](ux-design.md) §2.
Implementer: all of the above, then [architecture.md](architecture.md), [engines.md](engines.md) and the
[task brief](../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md).

## Evidence base (2026-10-20)

- `wai`: 50 unit tests pass (working tree, including the uncommitted `--json` change); commands, state model and
  handoff are built. The sandbox pilot has never been run, so there is no Observed end-to-end evidence.
- Infrastructure UI: 104 tests pass, 1 skipped (a symlink test Windows refused). The server already has a
  guarded `save` route and a tool-free Claude `dispatch` route, but **no screen calls them**. The UI does not use
  any `wai` state.
- Engines: Claude Code 2.1.304, Codex 0.163.0, Gemini CLI 0.64.0, Copilot CLI 1.0.100 and DeepSeek Harness
  0.2.1-rc.2 answered `--version`. Ollama is **not installed**.
- UX patterns: researched from Claude Code Desktop, GitHub Copilot agent sessions, the Codex app, Cline checkpoints,
  Open WebUI and Obsidian Properties. No usability test with the owner has taken place; findings are hypotheses.
