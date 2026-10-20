# Skill catalogue

One row per shared skill. The canonical definition is the linked `SKILL.md`; this page copies no bodies. Sources,
licenses and local modifications: [inventory](../../docs/inventory.md#installed-skills).

**Clients:** Claude Code loads every skill from `skills/` (Observed). Codex CLI reads the same folders
through local links in `clients/.agents/skills/` (Documented format; Unverified, see the
[Codex guide](../../clients/codex-cli/README.md#3-discovery)). Invoke with `/<name>` (Claude) or `$<name>` (Codex),
or let the client load it by description.

| Area | Skill | Use it when |
|---|---|---|
| Engineering | [engineering-lifecycle](../../skills/engineering-lifecycle/SKILL.md) | Starting any non-trivial change: requirements, plan, ADR, gates, report |
| Backend | [api-design-principles](../../skills/api-design-principles/SKILL.md) | Designing or reviewing REST/GraphQL APIs |
| Backend | [python-testing-patterns](../../skills/python-testing-patterns/SKILL.md) | Writing pytest suites, fixtures, mocks |
| Backend | [python-error-handling](../../skills/python-error-handling/SKILL.md) | Validation, exception hierarchies, partial failures |
| Backend | [python-resilience](../../skills/python-resilience/SKILL.md) | Timeouts, retries with backoff, rate limits, failure isolation for external calls |
| Backend | [sqlite-data-safety](../../skills/sqlite-data-safety/SKILL.md) | SQLite schema changes, transactions, thread safety, backups |
| Frontend | [vercel-react-best-practices](../../skills/vercel-react-best-practices/SKILL.md) | React/Next.js performance |
| Frontend | [react-state-management](../../skills/react-state-management/SKILL.md) | Choosing or setting up React state management |
| Frontend | [javascript-typescript-development](../../skills/javascript-typescript-development/SKILL.md) | General JavaScript/TypeScript: modules, async, types, tsconfig, project tooling |
| Frontend | [javascript-testing-patterns](../../skills/javascript-testing-patterns/SKILL.md) | Writing or reviewing JS/TS and React component tests |
| VS Code | [vscode-extension-development](../../skills/vscode-extension-development/SKILL.md) | Designing, implementing or reviewing TypeScript extensions with the VS Code API |
| UI/UX | [ui-ux-pro-max](../../skills/ui-ux-pro-max/SKILL.md) | Designing, building or reviewing interfaces (searchable local design data) |
| UI/UX | [frontend-design](../../skills/frontend-design/SKILL.md) | Giving a new UI a distinctive visual direction |
| UI/UX | [web-design-guidelines](../../skills/web-design-guidelines/SKILL.md) | Reviewing UI code against interface guidelines |
| UI/UX | [interaction-design](../../skills/interaction-design/SKILL.md) | Microinteractions, motion, loading states |
| UI/UX | [design-system-patterns](../../skills/design-system-patterns/SKILL.md) | Design tokens, theming, component architecture |
| UI/UX | [responsive-design](../../skills/responsive-design/SKILL.md) | Container queries, fluid type, mobile-first layouts |
| UI/UX | [wcag-audit-patterns](../../skills/wcag-audit-patterns/SKILL.md) | WCAG 2.2 audits and remediation |
| Game development | [game-ui-ux](../../skills/game-ui-ux/SKILL.md) | Game HUD/menu flows, touch, safe areas, input ownership and device UI review |
| Game development | [save-systems](../../skills/save-systems/SKILL.md) | Game save/load contracts, migration, recovery and interrupted sessions |
| Trading | [strategy-specification](../../skills/strategy-specification/SKILL.md) | Defining a deterministic strategy before coding it |
| Trading | [backtesting-audit](../../skills/backtesting-audit/SKILL.md) | Checking a backtest before trusting it |
| Trading | [risk-metrics-calculation](../../skills/risk-metrics-calculation/SKILL.md) | Computing or checking Sharpe, Sortino, drawdown, VaR/CVaR, profit factor, expectancy |
| Trading | [risk-management](../../skills/risk-management/SKILL.md) | Touching sizing, leverage, limits, kill switch |
| Trading | [market-data-quality](../../skills/market-data-quality/SKILL.md) | Adding or debugging a data provider or instrument |
| Trading | [exchange-integration](../../skills/exchange-integration/SKILL.md) | Adding exchange endpoints, connectors or a demo environment |
| Trading | [order-lifecycle-safety](../../skills/order-lifecycle-safety/SKILL.md) | Any code that sends, cancels or queries orders |
| Trading | [paper-trading-lifecycle](../../skills/paper-trading-lifecycle/SKILL.md) | Building or reviewing internal paper trading |
| Trading | [trading-test-review](../../skills/trading-test-review/SKILL.md) | Before calling a strategy, phase or risk change done |
| Trading | [repo-research](../../skills/repo-research/SKILL.md) | Evaluating an external repo or package (Trading-app specific content) |
| Trading | [dependency-license-review](../../skills/dependency-license-review/SKILL.md) | Before adding a dependency (Trading-app specific content) |

Trading skills assume the Trading-app root as the working directory.

Game skills added 2026-10-19: text-only adaptations without dependencies; live client discovery remains unverified.
