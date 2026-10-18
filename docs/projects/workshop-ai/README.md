# Workshop AI

- **Purpose:** a local command-line tool (`wai`) that runs one task with one AI client, keeps the task's verified
  state in the project's own repository so a new session can resume it, and builds a reviewed, secret-checked
  handoff package for another client. It consumes the [Workshop](../../workshop.md) layer and does not replace it.
  Requirements: [product vision](../../workshop-ai-product-vision.md).
- **Stage:** local POC (Stage 1 of the vision's roadmap).
- **Repository:** private repository, on disk at `%USERPROFILE%\workshop\applications\workshop-ai\`; its pilot
  sandbox is a second private repository at `%USERPROFILE%\workshop\applications\workshop-ai-sandbox\`.
- **Start a session:**
  - Use the tool: PowerShell in a normal terminal, `Set-Alias wai "$env:USERPROFILE\workshop\applications\workshop-ai\wai.cmd"`,
    then `wai init` in a project repository.
  - Work on the tool itself: Claude Code in its repository with `claude --add-dir "$env:USERPROFILE\workshop\infra\clients"`.
- **Shared resources it uses:** reads the [agent](../../catalogues/agents.md), [skill](../../catalogues/skills.md)
  and [task](../../catalogues/tasks.md) catalogues through the contracts in
  [ai-architecture.md §9](../../ai-architecture.md#9-future-unified-ui-preparation-only--no-ui-is-built); built under
  the [workshop-ai-product-foundation](../../../tasks/workshop-ai-product-foundation.md) task.
- **Project-specific resources:** in the project repositories.
