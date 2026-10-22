# Workshop AI

> **v2 approved (2026-10-20):** one browser app over the `wai` core, merging the Workshop Infrastructure UI; the
> VS Code extension is paused. See [workshop-ai-v2/](../../workshop-ai-v2/README.md) and the task
> [workshop-ai-v2-unified-app](../../../tasks/projects/workshop-ai/workshop-ai-v2-unified-app.md).

- **Purpose:** one local Spanish browser app over the `wai` core. The app browses Workshop resources and engines;
  its V2 editor provides review/save, versions/restore, templates and private notes/folder shortcuts. The CLI
  preserves project task state, checkpoints and reviewed handoff packages. It consumes the
  [Workshop](../../workshop.md) layer. Requirements: [v2 product vision](../../workshop-ai-v2/product-vision.md).
- **Stage:** local POC; V1 built and committed, V2 built locally with automated checks and security review passed.
  Owner V1 pilot/first-use and V2 browser/native-action acceptance remain pending. The extension stays paused.
  [Current evidence and next work](../../../../applications/workshop-ai/docs/v2-progress.md).
- **Repository:** private repository, on disk at `%USERPROFILE%\workshop\applications\workshop-ai\`; its pilot
  sandbox is a second private repository at `%USERPROFILE%\workshop\applications\workshop-ai-sandbox\`.
- **Start a session:**
  - Open the app: `applications/workshop-ai/INICIAR.cmd` from the Workshop folder.
  - Use the tool: PowerShell in a normal terminal, `Set-Alias wai "$env:USERPROFILE\workshop\applications\workshop-ai\wai.cmd"`,
    then `wai init` in a project repository.
  - Work on the app itself: open a coding client in its repository and follow `AGENTS.md`; shared Claude agents
    load through the Workshop plugin.
- **Shared resources it uses:** reads the [agent](../../catalogues/agents.md), [skill](../../catalogues/skills.md)
  and [task](../../catalogues/tasks.md) catalogues through the contracts in
  [ai-architecture.md §9](../../ai-architecture.md#9-workshop-ai-consumer-of-these-contracts); built under
  the [workshop-ai-product-foundation](../../../tasks/projects/workshop-ai/workshop-ai-product-foundation.md) task.
- **Project-specific resources:** in the project repositories.
