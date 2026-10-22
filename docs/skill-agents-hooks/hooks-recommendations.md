# 20 useful AI hooks, ranked for this Workshop

Checked 2026-10-21 against official client documentation. “Best” here means useful, predictable and proportionate for this Workshop, not most popular. Hooks are client-specific automation points, not portable Workshop resources. The ideas below are behavior patterns; no third-party hook code is recommended or installed. Event availability and behavior can change by client version and surface; check the linked reference before configuring a hook.

## Recommended shortlist

| Rank | Hook pattern | What it does | Fit |
|---:|---|---|---|
| 1 | Completion notification | Notifies you when a long run finishes or waits for input. | High: lets you step away during multi-step work. |
| 2 | Protected-path guard | Blocks writes to secrets, generated adapters, archived projects, or other explicitly protected paths. | High: reinforces existing security and project rules. Must be narrowly scoped. |
| 3 | Secret-aware commit guard | Checks staged files or diffs for likely credentials before a commit. | High: complements the existing infra pre-commit and CI scans; never prints secret values. |
| 4 | Required handover reminder | At session end, asks for outcome, decisions, open items and next step to be saved in the project’s existing record. | High: useful across projects and resumable work. A reminder is safer than silently writing notes. |
| 5 | Session-start project context | On entering a project, points to its `AGENTS.md`/`CLAUDE.md` and status document. | High: reduces missed local rules. Inject only a short pointer, not whole documents. |
| 6 | Context-compaction reminder | Before history is compacted, preserve decisions, evidence, constraints and next actions. | High: protects continuity in long sessions. Verify the client event and whether it is synchronous. |
| 7 | Protected-command confirmation | Detects a small list of destructive or external commands and leaves the client’s approval prompt in place. | High: supports least privilege. Must never auto-approve. |
| 8 | Project-root boundary check | Warns or blocks when an operation targets a path outside the selected project/workspace. | High: helps prevent accidental cross-project edits. Do not treat it as a complete sandbox. |
| 9 | Post-edit formatting | Runs the project’s already-installed formatter on changed supported files. | Medium-high for application repositories; skip prose and projects without a configured formatter. |
| 10 | Focused verification reminder | After edits, reminds the agent/user of the project’s documented verification command. | Medium-high: useful, but avoid automatically running expensive or stateful commands. |
| 11 | Completion checklist | On a final response, checks for outcome, files affected, evidence, and unresolved limits. | Medium-high: matches Workshop reporting style. Prefer advisory feedback to forced retries. |
| 12 | External-action boundary | Flags commands that publish, deploy, send messages, trade, or call external services for explicit human review. | High for safety, but needs accurate command matching and must not claim to understand arbitrary scripts. |
| 13 | Trading-app live-trading guard | Blocks any attempt to enable real execution or bypass `backend/algo/risk.py`. | High for Trading-app only. The app must remain paper-trading; enforce in application code too. |
| 14 | Trading-data provenance reminder | On analysis tasks, prompts to distinguish observed data, assumptions, fees and execution limits. | Medium-high: useful for research quality; it cannot validate a strategy or forecast returns. |
| 15 | Research citation check | At the end of web research, checks that changing claims have direct sources and dates. | Medium: valuable for current tools, quotas, terms and regulations; best implemented as an advisory review. |
| 16 | Task-start scope note | For substantial work, records a one-sentence objective, deliverable and constraints before execution. | Medium: supports the existing engineering lifecycle; avoid interrupting simple questions. |
| 17 | Change-summary reminder | At completion, asks for a concise list of changed documents/resources and index updates where relevant. | Medium: helps keep Workshop navigation accurate. |
| 18 | Background job notification | Sends a notification when a long verification or generation process finishes. | Medium: useful only where the client has a supported async/background event. |
| 19 | MCP/external-tool audit notice | Logs that an external tool was called, with tool name and timestamp but without arguments or returned content. | Medium-low: may help audit integrations; keep logs local and minimize metadata. |
| 20 | Hook-health indicator | Reports which local hooks loaded and whether they timed out or failed. | Medium-low: useful after several hooks exist; avoid verbose per-event noise. |

## Best starting set for Jaime

Start by evaluating **1, 4 and 7**: notifications, a handover reminder, and a narrow risky-command confirmation. For path protections and secret scanning (**2 and 3**), first check the relevant client rules and existing Git/pre-commit protections; add a hook only if it closes a specific gap. Use **13** only inside Trading-app workflows, and never treat a client hook as the enforcement layer for real-trading safety. Keep trials advisory where possible, with logging that omits prompt text, file contents and secrets.

Do not install a “top 20 hooks” pack. Hook scripts execute automatically and may receive prompts, tool arguments, paths or results. Review every script and configuration locally, keep hooks short and deterministic, set timeouts, avoid network access and secret-bearing logs, and retain normal permission prompts. A hook is not a security sandbox.

## Client support and limits

- **Claude Code:** official hooks include lifecycle, tool-use, notification, compaction, and other events. It supports command hooks and additional prompt/agent/HTTP/MCP hook forms; those richer forms depend on judgement or external components and are not the first choice for deterministic guardrails. [Hooks guide](https://code.claude.com/docs/en/hooks-guide) · [Reference](https://code.claude.com/docs/en/hooks)
- **Codex:** official lifecycle hooks are available in current Codex surfaces; plugins can bundle hooks, but local scripts must exist in the execution environment and bundled hooks require review/trust. This Workshop’s compatibility matrix records hooks as documented but unused. Verify the exact current event schema and surface before implementation. [Hooks documentation](https://learn.chatgpt.com/docs/hooks) · [Plugin hook setup](https://developers.openai.com/plugins/build/plugins)
- **Gemini CLI:** official hooks include session, agent, model and tool events, with structured input/output and blocking decisions. Hook configuration is client-local, and its documentation emphasizes valid JSON output, exit behavior, trust and privacy. [Reference](https://geminicli.com/docs/hooks/reference/) · [Best practices](https://geminicli.com/docs/hooks/best-practices/)
- **Workshop AI:** the app’s engine registry and current architecture do not establish a common hook runtime. Treat these as client-specific until a product design explicitly defines a safe, portable event contract and per-client adapters. Do not assume an external hook will run inside Workshop AI.

## Practical selection rule

Use a hook when the action is deterministic and should happen every time. Use a skill/task prompt when it requires judgement or is only needed occasionally. Keep user approval for irreversible, external, financial, publishing and permission-changing actions. A hook cannot replace the client's permission system, operating-system protections, app-level safeguards, or review. Define a timeout and failure behavior deliberately; blocking checks are appropriate only when the condition is specific and reliably detectable.

## Sources

- Anthropic, [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide) and [Hooks reference](https://code.claude.com/docs/en/hooks).
- OpenAI, [Codex hooks](https://learn.chatgpt.com/docs/hooks), [plugin packaging and bundled hooks](https://developers.openai.com/plugins/build/plugins), and [plugin architecture](https://developers.openai.com/plugins/concepts/plugins).
- Google, [Gemini CLI Hooks reference](https://geminicli.com/docs/hooks/reference/) and [Hooks best practices](https://geminicli.com/docs/hooks/best-practices/).
