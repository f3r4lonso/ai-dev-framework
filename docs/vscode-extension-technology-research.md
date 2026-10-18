# Workshop AI VS Code extension — technology research for Gate A

Checked 2026-10-18. Input for the Gate A decisions of
[workshop-ai-vscode-extension-specification](../tasks/workshop-ai-vscode-extension-specification.md) (§6, D1–D11).
Nothing was installed, built or run; package data comes from registry metadata only.

Labels (from `docs/ai-architecture.md`, plus Requires verification): **Observed** (seen on the maintainer's machine),
**Verified** (read in the stable VS Code API typings `@types/vscode` 1.140.0), **Documented** (official docs, URL
below, read 2026-10-18), **Inference**, **Requires verification**.

## 1. Answers per decision

| Decision | Finding | Effect on the default |
|---|---|---|
| D1 backend | An extension can run local programs with Node's built-in `child_process.execFile` (no package needed), so it can call `wai <command> --json` and read the result (**Inference**, standard Node). `wai` has no machine-readable mode yet (**Observed**: README lists text output only). | Default holds. The build task must add a JSON output mode to `wai`. No daemon or HTTP needed. |
| D2 language and tooling | Extensions run in VS Code's own Node host; TypeScript or plain JavaScript (**Documented** [1]). Zero runtime packages is feasible: the `vscode` module is provided by the host (**Inference**). Dev tooling below (§2). | Default holds. Optional cheaper variant: plain JavaScript with type checking from `@types/vscode`, no compiler. |
| D3 infra clone | Git 2.56 and Python 3.12 are installed (**Observed**). Cloning by running `git clone <url> <folder>` through `execFile`, after a modal approval, needs no package. | Default holds. Check for an empty target folder before cloning; never pass user text through a shell. |
| D4 open and close clients | Stable API: `window.createTerminal` (name, shell path and args, working folder, env, `isTransient`, `hideFromUser`), `Terminal.dispose()` closes it, `onDidCloseTerminal` and `Terminal.exitStatus` say when and how it ended (**Verified**). So the extension can open a visible terminal running `wai start` / `wai resume` and close it after the checkpoint. | Default holds. `wai` stays the only launcher; the extension manages terminals. |
| D4 reading client output | Shell integration is stable: `Terminal.shellIntegration.executeCommand(...)` and `TerminalShellExecution.read()` stream a command's raw output (**Verified**). It works only when shell integration is active, and output includes escape codes (**Verified**, doc comment). | Not recommended: parsing a client's full-screen output is fragile and reads conversation content (D6). |
| D5 Claude Code usage | The status line receives JSON with `rate_limits.five_hour.used_percentage`, `rate_limits.seven_day.used_percentage` and `resets_at` (Pro/Max only, after the first response), and `context_window.used_percentage` (**Documented** [2]). It can be set in project settings, not only user settings (**Documented** [2]). Hooks: `StopFailure` with matcher `rate_limit` fires when a turn ends on a rate limit; `PreCompact` before compaction; both allowed in project `.claude/settings.json` (**Documented** [3]). | Automatic detection for Claude Code is **feasible**: a project-level status line script writes a small JSON file under `.workshop-ai/`, and the extension watches it (`createFileSystemWatcher`, **Verified**). Distinguishes context full (`context_window`) from plan limit (`rate_limits`). Needs its own gate: a project status line replaces the user's own one in that project (**Inference**, Requires verification). |
| D5 Codex usage | `/status` and the footer status line show 5-hour and weekly limits, display only (**Requires verification**: official search summary [4] and community reports; page not read). `notify` is user-level only and fires only on `agent-turn-complete`, with no usage fields (**Documented** [5]). Project hooks exist (trusted project only) but no usage or rate-limit field is documented (**Documented** [5][6]). The Codex app-server has `account/rateLimits/read` (**Requires verification**: from an official search summary [7]; page not read); it is a programmatic interface. | First increment for Codex: **manual trigger only**. The app-server route counts as scripted use until the §17.2 hard gate is met (**Inference**). |
| D6 save context | Watching files and writing JSON/Markdown needs only built-in APIs (`workspace.fs`, file watchers; **Verified**). | Default holds; no storage technology to add. |
| D7 approvals | Any extension can list every open terminal (`window.terminals`) and type into it (`Terminal.sendText`) (**Verified**). Any extension can run another extension's commands without restriction (**Documented** [8]). Modal dialogs exist (`MessageOptions.modal`, **Verified**); no API was found that lets an extension answer another's dialog (**Inference**, Requires verification). | Confirms the D7 risk: a terminal approval is not proof a person approved. A modal dialog opened by the extension itself is the stronger candidate, but it still needs the security review. Commands that start approvals must re-ask, never act on arguments alone. |
| Workspace trust | `workspace.isTrusted` and a grant event are stable (**Verified**). | The extension should declare that it is disabled in untrusted (Restricted Mode) workspaces. |
| D11 language | `vscode.l10n` is stable (**Verified**), with `package.nls.*.json` for manifest strings. | Spanish UI strings are supported natively; no package needed. |

## 2. Development tooling (registry metadata, 2026-10-18; not installed)

| Package | Version | License | Direct deps | Install scripts | Use | Recommendation |
|---|---|---|---|---|---|---|
| `@types/vscode` | 1.140.0 | MIT | 0 | none | API types | Needed (types only) |
| `typescript` | 7.0.2 | Apache-2.0 | 20 | none | compiler | Needed if TypeScript; review its 20 deps |
| `@vscode/vsce` | 4.0.0 | MIT | 26 | none | package a `.vsix` for local install | Needed to install outside the dev host |
| `@vscode/test-cli` | 0.0.15 | MIT | 9 | none | test runner | For integration tests |
| `@vscode/test-electron` | 3.1.0 | MIT | 5 | none | downloads a VS Code build for tests (network at test time, **Inference**) | For integration tests; needs approval |
| `esbuild` | 0.28.2 | MIT | 0 | **postinstall** (fetches a native binary) | bundler | **Avoid**: not needed with zero runtime deps |

Local runtimes: VS Code 1.142, Node 24.20, npm 11.19, Python 3.12.10, Git 2.56 (**Observed**). The extension should
target `engines.vscode` `^1.140.0`, matching the newest typings. Each package still goes through
`dependency-license-review` in the build task.

## 3. UI building blocks (all stable, **Verified**)

Commands and the command palette; a tree view (clients, tasks); a status bar item (usage level, active client); an
output channel (logs); modal and non-modal messages; quick picks (choose the next client, D9). A webview panel is
available but adds HTML/JS attack surface and content-security rules; not needed for the first increment.

## 4. Open items for Gate A

1. Does a project-level Claude Code status line replace the user's own status line in that project? (D5)
2. Does any documented Codex hook or `/status` output give usage in a form a script can read without the app-server? (D5)
3. Can any extension or IDE agent answer or auto-confirm a modal dialog opened by another extension? (D7, security review)
4. Is opening and closing interactive client terminals from an extension ordinary use under each provider's terms? (D4, §17.2)
5. Do the official Claude Code and Codex VS Code extensions expose an API the hub could use? Not checked.

## Sources

1. VS Code extension API: <https://code.visualstudio.com/api/references/vscode-api>
2. Claude Code status line: <https://code.claude.com/docs/en/statusline>
3. Claude Code hooks: <https://code.claude.com/docs/en/hooks>
4. Codex config reference (`tui.status_line`): <https://developers.openai.com/codex/config-reference>; Codex issue on
   status-line rate-limit tokens: <https://github.com/openai/codex/issues/24080>
5. Codex advanced configuration: <https://learn.chatgpt.com/docs/config-file/config-advanced>
6. Codex hooks: <https://developers.openai.com/codex/hooks>
7. Codex app-server: <https://developers.openai.com/codex/app-server>
8. VS Code `commands.executeCommand` note in [1]
9. Stable typings: <https://unpkg.com/@types/vscode@1.140.0/index.d.ts>; npm registry metadata for the §2 packages
