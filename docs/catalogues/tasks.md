# Task catalogue

Task prompts are briefs you hand to a client to run a whole piece of work. They live in
[`../tasks/`](../../tasks/README.md); this page lists them with their status. Run only **active** tasks.

| Task | Status | Purpose | Approvals it asks for | Clients |
|---|---|---|---|---|
| [ai-infrastructure-unification-and-workshop](../../tasks/ai-infrastructure-unification-and-workshop.md) | completed (2026-10-17) | Reorganize the shared infrastructure into clients, client-native resources, Workshop and projects | — (done; kept as a record) | Claude Code (run 2026-10-17) |
| [workshop-ai-product-foundation](../../tasks/workshop-ai-product-foundation.md) | active (rev. 2, 2026-10-17) | Turn the Workshop AI vision into a testable baseline and build the first single-client path with manual handoff, tested on a sandbox project | Gates A (decisions), B (baseline and plan), C (Codex, optional), D (commits) | Claude Code (to run); Codex CLI (handoff target, needs install) |
| [workshop-ai-token-optimization-integration](../../tasks/workshop-ai-token-optimization-integration.md) | active (rev. 2, 2026-10-18); starts only after the product foundation task is completed | Stage 2 proof of concept: project-local knowledge store, tool-output compression and handoff summary, measured against a plain session; candidate repos used as references only ([review](../token-optimization-candidate-review.md)) | Gates A (design), B (benchmark plan), C (pilot runs), D (commits) | Claude Code (to run); Codex CLI (handoff target, if installed) |
| [workshop-ai-vscode-extension-specification](../../tasks/workshop-ai-vscode-extension-specification.md) | active (draft, rev. 2, reviewed 2026-10-18) | Documents-only: specify Workshop AI as a VS Code extension hub (client detection, infra setup, client switching with saved context and recap) and realign the vision and tasks | Gates A (decisions D1–D11 and edit list), B (specification and reviews), C (commits) | Claude Code (to run) |
| [homero-self-improvement-and-prompt-reviewer-task](../../tasks/homero-self-improvement-and-prompt-reviewer-task.md) | completed (2026-10-17) | Improve the Homero prompt, add the `prompt-reviewer` agent, review a target task prompt | — (done; kept as a record) | Claude Code |
| [unified-ai-engineering-infrastructure-prompt](../../tasks/unified-ai-engineering-infrastructure-prompt.md) | superseded | First-run brief for the shared Claude/Codex infrastructure | — | do not run |
| [unified-ai-client-workshop-reorganization](../../tasks/unified-ai-client-workshop-reorganization.md) | superseded | Earlier draft of the client/Workshop reorganization | — | do not run |

Results of completed runs: [ai-infrastructure-handover.md](../ai-infrastructure-handover.md),
[prompt-engineering-review.md](../../docs/prompt-engineering-review.md).
