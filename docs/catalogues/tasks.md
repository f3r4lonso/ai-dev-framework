# Task catalogue

Task prompts are briefs you hand to a client to run a whole piece of work. They live in project-specific
`projects/<project>/` folders or reusable `common/<category>/` folders under [`../tasks/`](../../tasks/README.md).
This page lists them with their status. Run only **active** tasks.

### Common tasks — agents and prompts

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [homero-self-improvement-and-prompt-reviewer-task](../../tasks/common/agents-and-prompts/homero-self-improvement-and-prompt-reviewer-task.md) | completed (2026-10-17) | Improve Homero, add the `prompt-reviewer` agent, review a target task prompt | — (done; kept as a record) | Claude Code |

### AI infrastructure

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [ai-infrastructure-unification-and-workshop](../../tasks/projects/ai-infrastructure/ai-infrastructure-unification-and-workshop.md) | completed (2026-10-17) | Reorganize the shared infrastructure into clients, client-native resources, Workshop and projects | — (done; kept as a record) | Claude Code (run 2026-10-17) |
| [unified-ai-engineering-infrastructure-prompt](../../tasks/projects/ai-infrastructure/unified-ai-engineering-infrastructure-prompt.md) | superseded | First-run brief for the shared Claude/Codex infrastructure | — | do not run |
| [unified-ai-client-workshop-reorganization](../../tasks/projects/ai-infrastructure/unified-ai-client-workshop-reorganization.md) | superseded | Earlier draft of the client/Workshop reorganization | — | do not run |

### AI Reading Assistant

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [ai-spanish-reading-assistant](../../tasks/projects/ai-reading-assistant/ai-spanish-reading-assistant.md) | active | Build a local-first web app that prepares text locally, optionally translates it into Spanish, and reads it aloud at adjustable speeds | Dependency approval; approval before external translation or sending document content | Claude Code / Codex CLI |

### Ollama

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [ollama-install](../../tasks/projects/ollama/ollama-install.md) | active | Install Ollama for the current Windows user with one local translation model, then verify local API, GPU use and loopback-only access | Gate A (exact install plan); install requires a suitably authorized Windows session | Claude Code / Codex CLI |
| [ollama-local-model-runtime](../../tasks/projects/ollama/ollama-local-model-runtime.md) | active | Install the Ollama CLI and approved local models, verify they run on the GPU and stay on localhost, and register Ollama as a provider (client guide, onboarding, matrix, inventory, security) for private text work | Gates A (install and models), B (documentation plan), C (client-backend evaluation, optional), D (commits) | Claude Code / Codex CLI |

### Online Psychology Clinic

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [online-psychology-clinic-functional-specification](../../tasks/projects/online-psychology-clinic/online-psychology-clinic-functional-specification.md) | active | Define a vendor-neutral functional specification for a global online psychology clinic, including multilingual matching, patient billing, and psychologist compensation | No implementation or external actions; clarify material business decisions or label assumptions | Claude Code / Codex CLI |

### Persistent Castle MMO

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [persistent-castle-mmo-planning](../../tasks/projects/persistent-castle-mmo/persistent-castle-mmo-planning.md) | active | Design and plan an original persistent mobile castle strategy MMO, including playable systems, art/audio direction, monetization safeguards and online architecture | No implementation, repository setup, account, cloud, purchase, external sharing or publication; owner decisions required before technical commitment | Homero, game-designer, game-art-music-director, game-developer, prompt-reviewer |

### Workshop AI

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [workshop-ai-v2-unified-app](../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md) | active (D-V2-01…09 approved 2026-10-20; V0 done, V1 next) | Build Workshop AI v2: one Spanish browser app merging the Infrastructure UI and `wai` — safe file editing with versions, conversations with agents, task board, agent/skill wizard and every Workshop AI engine; requirements in [workshop-ai-v2/](../workshop-ai-v2/README.md) | Gate 0 (decisions), per increment Gates A (plan) and B (tests, security review, owner check), Gate C (commits); max 10 provider test runs per increment | Claude Code (to run); others per increment |
| [workshop-ai-product-foundation](../../tasks/projects/workshop-ai/workshop-ai-product-foundation.md) | active (rev. 2, 2026-10-17) | Turn the Workshop AI vision into a testable baseline and build the first single-client path with manual handoff, tested on a sandbox project | Gates A (decisions), B (baseline and plan), C (Codex, optional), D (commits) | Claude Code (to run); Codex CLI (handoff target, needs install) |
| [workshop-ai-token-optimization-integration](../../tasks/projects/workshop-ai/workshop-ai-token-optimization-integration.md) | active (rev. 2, 2026-10-18); starts only after the product foundation task is completed | Stage 2 proof of concept: project-local knowledge store (the VS Code extension's context storage), tool-output compression, handoff summary and switch recap, measured against a plain session; candidate repos used as references only ([review](../token-optimization-candidate-review.md)) | Gates A (design), B (benchmark plan), C (pilot runs), D (commits) | Claude Code (to run); Codex CLI (handoff target, if installed) |
| [workshop-ai-vscode-extension-specification](../../tasks/projects/workshop-ai/workshop-ai-vscode-extension-specification.md) | completed (2026-10-18) | Documents-only: specify Workshop AI as a VS Code extension hub (client detection, infra setup, client switching with saved context and recap) and realign the vision and tasks | — (done; kept as a record) | Claude Code (run 2026-10-18) |
| [workshop-ai-vscode-agents-skills-research-for-homero](../../tasks/projects/workshop-ai/workshop-ai-vscode-agents-skills-research-for-homero.md) | retired (2026-10-18) | Research brief for the Homero assistant on agents, skills and references for VS Code extension work | — (kept as a record) | do not run |

### Workshop Infrastructure UI

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [workshop-infrastructure-windows-ui](../../tasks/projects/workshop-infrastructure-ui/workshop-infrastructure-windows-ui.md) | superseded by [workshop-ai-v2-unified-app](../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md) (2026-10-20) | Unified local browser UI: resource discovery, Spanish reading, bounded agent chains, security boundaries and optional future editing/dispatch; [implementation evidence and limits](../../../applications/workshop-infrastructure-ui/docs/interaction-upgrade.md) | Dependency approval; external/paid requests and separately authorized system-wide installation, publication or external changes | Any AI coding client with workspace access |

Results of completed runs: [ai-infrastructure-handover.md](../ai-infrastructure-handover.md),
[prompt-engineering-review.md](../../docs/prompt-engineering-review.md).
