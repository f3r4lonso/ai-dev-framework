# Skill catalogue

One row per shared skill. The canonical definition is the linked `SKILL.md`; this page copies no bodies. Sources,
licenses and local modifications: [inventory](../../docs/inventory.md#installed-skills).

**Clients:** Claude Code loads every skill from `.claude/skills/` (Observed). Codex CLI reads the same folders
through local links in `.agents/skills/` (Documented format; Unverified, see the
[Codex guide](../../clients/codex-cli/README.md#3-discovery)). Invoke with `/<name>` (Claude) or `$<name>` (Codex),
or let the client load it by description.

| Area | Skill | Use it when |
|---|---|---|
| Engineering | [engineering-lifecycle](../../.claude/skills/engineering-lifecycle/SKILL.md) | Starting any non-trivial change: requirements, plan, ADR, gates, report |
| Backend | [api-design-principles](../../.claude/skills/api-design-principles/SKILL.md) | Designing or reviewing REST/GraphQL APIs |
| Backend | [python-testing-patterns](../../.claude/skills/python-testing-patterns/SKILL.md) | Writing pytest suites, fixtures, mocks |
| Backend | [python-error-handling](../../.claude/skills/python-error-handling/SKILL.md) | Validation, exception hierarchies, partial failures |
| Frontend | [vercel-react-best-practices](../../.claude/skills/vercel-react-best-practices/SKILL.md) | React/Next.js performance |
| Frontend | [react-state-management](../../.claude/skills/react-state-management/SKILL.md) | Choosing or setting up React state management |
| UI/UX | [ui-ux-pro-max](../../.claude/skills/ui-ux-pro-max/SKILL.md) | Designing, building or reviewing interfaces (searchable local design data) |
| UI/UX | [frontend-design](../../.claude/skills/frontend-design/SKILL.md) | Giving a new UI a distinctive visual direction |
| UI/UX | [web-design-guidelines](../../.claude/skills/web-design-guidelines/SKILL.md) | Reviewing UI code against interface guidelines |
| UI/UX | [interaction-design](../../.claude/skills/interaction-design/SKILL.md) | Microinteractions, motion, loading states |
| UI/UX | [design-system-patterns](../../.claude/skills/design-system-patterns/SKILL.md) | Design tokens, theming, component architecture |
| UI/UX | [responsive-design](../../.claude/skills/responsive-design/SKILL.md) | Container queries, fluid type, mobile-first layouts |
| UI/UX | [wcag-audit-patterns](../../.claude/skills/wcag-audit-patterns/SKILL.md) | WCAG 2.2 audits and remediation |
| Trading | [strategy-specification](../../.claude/skills/strategy-specification/SKILL.md) | Defining a deterministic strategy before coding it |
| Trading | [backtesting-audit](../../.claude/skills/backtesting-audit/SKILL.md) | Checking a backtest before trusting it |
| Trading | [risk-management](../../.claude/skills/risk-management/SKILL.md) | Touching sizing, leverage, limits, kill switch |
| Trading | [market-data-quality](../../.claude/skills/market-data-quality/SKILL.md) | Adding or debugging a data provider or instrument |
| Trading | [exchange-integration](../../.claude/skills/exchange-integration/SKILL.md) | Adding exchange endpoints, connectors or a demo environment |
| Trading | [order-lifecycle-safety](../../.claude/skills/order-lifecycle-safety/SKILL.md) | Any code that sends, cancels or queries orders |
| Trading | [paper-trading-lifecycle](../../.claude/skills/paper-trading-lifecycle/SKILL.md) | Building or reviewing internal paper trading |
| Trading | [trading-test-review](../../.claude/skills/trading-test-review/SKILL.md) | Before calling a strategy, phase or risk change done |
| Trading | [repo-research](../../.claude/skills/repo-research/SKILL.md) | Evaluating an external repo or package (Trading-app specific content) |
| Trading | [dependency-license-review](../../.claude/skills/dependency-license-review/SKILL.md) | Before adding a dependency (Trading-app specific content) |

Trading skills assume the Trading-app root as the working directory.
