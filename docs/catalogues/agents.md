# Agent catalogue

One row per shared agent. The canonical definition is the linked file; this page copies no bodies. Sources,
licenses and local modifications: [inventory](../../docs/inventory.md#installed-agents).

**Clients:** every agent works in Claude Code (Observed: all 20 listed by `/agents`, 2026-10-17). In Codex CLI each
has a generated wrapper in `clients/.codex/agents/` (loading Unverified; tool limits not enforced, see the
[Codex guide](../../clients/codex-cli/README.md#7-limitations)). **Access:** RO = read-only; Edit = can change files.

| Area | Agent | Use it to | Access |
|---|---|---|---|
| AI | [ai-environment-auditor](../../agents/ai/ai-environment-auditor.md) | Audit agents, skills, rules, prompts and the client adapters; plan changes (apply mode edits infrastructure files only) | RO audit / Edit apply |
| AI | [prompt-reviewer](../../agents/ai/prompt-reviewer.md) | Score and harden one prompt or agent/skill instruction | RO |
| DevOps | [git-workflow-manager](../../agents/devops/git-workflow-manager.md) | Plan clean commits and branches; pre-push safety checks; pushes only after confirmation | Edit (git) |
| Backend | [backend-architect](../../agents/backend/backend-architect.md) | Design APIs, service boundaries, resilience, observability | Edit |
| Backend | [python-pro](../../agents/backend/python-pro.md) | Write or optimize modern Python | Edit |
| Frontend | [frontend-developer](../../agents/frontend/frontend-developer.md) | Build React/Next.js components, layouts, client state | Edit |
| Quality | [code-reviewer](../../agents/quality/code-reviewer.md) | Review code for bugs, security, performance | RO |
| Quality | [debugger](../../agents/quality/debugger.md) | Investigate errors, failing tests, unexpected behavior | Edit |
| Quality | [security-reviewer](../../agents/quality/security-reviewer.md) | Security review of any project or this repo: secrets, public-repo hygiene, data flow and handoffs, permissions, dependencies, licenses; trading safety checks in Trading-app | RO |
| UI | [ui-designer](../../agents/ui/ui-designer.md) | Visual design: components, layouts, mockups | Edit |
| UI | [accessibility-expert](../../agents/ui/accessibility-expert.md) | WCAG, keyboard and screen-reader support | Edit |
| UX | [ui-ux-tester](../../agents/ux/ui-ux-tester.md) | Test every documented user flow and report defects | Edit |
| UX | [ux-researcher](../../agents/ux/ux-researcher.md) | Usability studies, personas, competitive research | RO |
| Trading | [quant-researcher](../../agents/trading/quant-researcher.md) | Turn a trading idea into a testable specification | RO |
| Trading | [strategy-engineer](../../agents/trading/strategy-engineer.md) | Implement an approved strategy with tests | Edit (strategy code) |
| Trading | [risk-engineer](../../agents/trading/risk-engineer.md) | Change the central risk engine with tests | Edit (risk code) |
| Trading | [backtesting-auditor](../../agents/trading/backtesting-auditor.md) | Independently audit a backtest | RO |
| Trading | [qa-test-engineer](../../agents/trading/qa-test-engineer.md) | Unit, integration and regression tests | Edit (tests) |
| Trading | [exchange-integration-engineer](../../agents/trading/exchange-integration-engineer.md) | Exchange data and demo-execution adapters; never production trading | Edit |
| Trading | [repo-researcher](../../agents/trading/repo-researcher.md) | Vet an external repo or package | RO |

Trading agents assume the Trading-app root as the working directory (see
[Trading-app entry](../projects/trading-app/README.md)).

Known overlap, kept on purpose: `code-reviewer` (general code quality) and `security-reviewer` (workshop security rules,
plus trading checks in Trading-app; read-only). Retired agents and why: [inventory](../../docs/inventory.md#retired-2026-10-17-audit).

**Built into Claude Code** (not part of this repo): `Explore` (fast read-only search), `Plan` (implementation
plans), `general-purpose` (multi-step research), `claude-code-guide` (questions about Claude Code).
