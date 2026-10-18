---
name: vscode-extension-development
description: Build or review TypeScript extensions with the VS Code Extension API, including commands, views, terminals, workspace integration, and extension-host tests. Not for ordinary web applications.
---

# VS Code Extension Development

Use this skill when the deliverable is a VS Code extension. Treat the current official Extension API documentation as authoritative because the API evolves with VS Code releases. Read only the API guides needed for the feature being changed.

## Design and implementation

- Prefer built-in VS Code surfaces and contribution points for commands, views, status items, quick picks, and notifications. Use a webview only when the required interaction cannot be served well by the native workbench UI.
- Keep the extension host as a thin adapter around domain logic. Keep file formats, task state, and provider-independent decisions outside VS Code-specific classes where practical.
- Declare user-invoked commands and views in the extension manifest. Choose activation events deliberately; avoid activating on every workspace when a narrower event or explicit command works.
- Dispose event listeners, terminals, providers, and other extension-owned resources through `context.subscriptions` or an equivalent lifecycle owner. Handle workspace-folder changes and multi-root workspaces explicitly when the feature relies on project roots.
- Use typed, argument-array process APIs for external commands; do not build shell command strings from workspace paths or user input. Validate executable discovery, working directory, exit status, cancellation, and output size. Do not place credentials or private task content in command arguments or logs.
- Treat workspace content, task files, terminal output, and extension-provided data as untrusted. Do not convert text from them into commands or trust decisions without explicit validation and user approval.
- Prefer stable, documented APIs. A proposed API requires a documented need, an explicit compatibility decision, and a fallback; do not make a core workflow depend on it by accident.
- Keep user-facing strings concise and localizable. Respect VS Code theme, keyboard navigation, accessibility, and progress/cancellation conventions.

## Testing and dependencies

- Separate domain logic tests from extension-host integration tests. Cover activation, command registration, workspace edge cases, cancellation, subprocess failures, and any security boundary the feature relies on.
- Use the test and build tooling already approved by the project. Do not add runtime or development packages merely because a sample uses them; review and approve each dependency under the project's rules.
- Samples are examples, not a production architecture or a security review. Read the relevant sample and its current license before adapting code; preserve required notices and record provenance.

## Workshop AI project constraints

For Workshop AI, first read the active product task and the product repository's `AGENTS.md`. The extension task is a proposed specification with explicit gates; its recommended decisions are not approved product facts until the owner records them.

- The proposed stack is a TypeScript VS Code extension over the existing `wai` Python standard-library CLI. Keep `wai` as the state and workflow authority unless an approved decision changes that boundary.
- The task recommends no runtime npm dependencies and requires development tooling to be considered individually. It places extension code under `vscode-extension/` in the product repository; shared skills stay in the infrastructure repository.
- Never read client credential or session stores. Do not store task state in the public infrastructure repository. Do not claim usage-limit detection or terminal-output access exists without current official evidence.
- A terminal being interactive does not establish that a human supplied an approval. The extension must not write into a terminal where an approval prompt is or may be shown. Keep user approval and provider boundaries explicit.
- Do not implement client launching, automatic switching, unattended continuation, or changes to the extension during a specification-only task. Follow its gates and scope.

## Official references

- [VS Code Extension API](https://code.visualstudio.com/api/)
- [Extension API reference](https://code.visualstudio.com/api/references/vscode-api)
- [Extension guides and samples](https://code.visualstudio.com/api/extension-guides/overview)
- [Extension host](https://code.visualstudio.com/api/advanced-topics/extension-host)
- [Testing extensions](https://code.visualstudio.com/api/working-with-extensions/testing-extension)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Microsoft VS Code extension samples](https://github.com/microsoft/vscode-extension-samples) (use as optional local reference only when available; never run its setup scripts or installers without review).
