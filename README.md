# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs):
shared agents, skills and instructions used across my application projects.

## Contents
- `CLAUDE.md` — workspace-wide rules loaded by Claude Code.
- `.claude/agents/` — subagents by area: `ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`.
- `.claude/skills/` — on-demand skills (UI/UX, frontend, backend, trading).
- `ai-infra/README.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `ai-infra/THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.

Application projects live in `Applications/` as separate repositories and are not part of this repo.

## Usage
Clone into the workspace root (e.g. `C:\Users\<you>\Repos`) and start Claude Code there, or from an application
repo with `claude --add-dir <workspace root>` so the shared agents and skills load.

## Agents

22 subagents in `.claude/agents/`, grouped by area.

**How to invoke an agent**
- **By name:** "Use the code-reviewer agent to review this branch."
- **Guaranteed:** type `@` and pick the agent, e.g. `@agent-code-reviewer`.
- **Automatically:** Claude Code delegates on its own when a request matches the agent's description.
- **Manage them:** `/agents` lists, edits or creates agents.
- **Where they load:** start Claude Code in the workspace root, or in an application repo with
  `claude --add-dir <workspace root>` (Trading-app ships `start-claude.bat` for this).

### AI / infrastructure
| Agent | Purpose | Responsibilities |
|---|---|---|
| `ai-environment-auditor` | Audits and maintains the AI setup | Inventories agents, skills and CLAUDE.md files; finds duplicates, conflicts and risks; proposes plans; in apply mode edits infrastructure files only (never app code, settings or vendor copies); audits itself. Modes: quick, full, focused, apply. |

### DevOps
| Agent | Purpose | Responsibilities |
|---|---|---|
| `git-workflow-manager` | Organizes repos and commits | Clean commits and branches; keeps the framework repo and each app repo separate; mandatory pre-push safety check; pushes only after user confirmation and never force-pushes. |

### Backend
| Agent | Purpose | Responsibilities |
|---|---|---|
| `backend-architect` | Designs backend systems | API design, service boundaries, resilience, observability. |
| `python-pro` | Python specialist | Modern Python, async code, performance, production-ready practices. |

### Frontend
| Agent | Purpose | Responsibilities |
|---|---|---|
| `frontend-developer` | Builds user interfaces | React and Next.js components, responsive layouts, client-side state. |
| `react-specialist` | Optimizes existing React apps | Performance, advanced React features, state management architecture. |

### Quality
| Agent | Purpose | Responsibilities |
|---|---|---|
| `code-reviewer` | Reviews code | Bugs, security vulnerabilities, performance and reliability issues. |
| `debugger` | Fixes problems | Investigates errors, failing tests and unexpected behavior. |
| `test-automator` | Builds automated tests | Test strategy, test suites, CI integration. |

### UI (visual design)
| Agent | Purpose | Responsibilities |
|---|---|---|
| `ui-designer` | Visual design | Components, layouts, mockups. |
| `design-system-architect` | Design systems | Design tokens, theming, reusable component libraries. |
| `accessibility-expert` | Accessibility | Keyboard and screen-reader support, WCAG compliance. |

### UX (user experience)
| Agent | Purpose | Responsibilities |
|---|---|---|
| `ui-ux-tester` | End-to-end interface testing | Tests every documented user flow and reports visual and functional defects. |
| `ux-researcher` | User research | Usability studies, behavior analysis, personas, competitive research. Read-only. |

### Trading
Built for the Trading-app project; they assume the project root as working directory.

| Agent | Purpose | Responsibilities |
|---|---|---|
| `quant-researcher` | Turns trading ideas into testable specs | Hypothesis, exact rules, costs, biases, out-of-sample test plan. Does not code or trade. |
| `strategy-engineer` | Implements strategies | Codes approved specs with versioned parameters and tests. Edits only strategy code and tests. |
| `risk-engineer` | Owns the central risk engine | Position sizing, leverage, exposure, daily/weekly limits, drawdown, kill switch. Edits only risk code and its tests. |
| `backtesting-auditor` | Independently checks backtests | Look-ahead, fills, costs, funding, sample size, reproducibility; recommends accept, reject or repeat. Never edits. |
| `qa-test-engineer` | Tests the Algo Lab | Edge cases, backtest reproduction, separation of backtest/paper/demo/live modes. Writes test files only. |
| `exchange-integration-engineer` | Exchange connections | Data adapters and (later) demo execution with idempotency and reconciliation. Never trades in production. |
| `security-reviewer` | Security audit | Secrets, dependencies, licenses, agent permissions; confirms real trading stays disabled and the risk engine cannot be bypassed. Strictly read-only. |
| `repo-researcher` | Vets external projects | License, version, activity and risks of outside repos and packages. Read-only; installs nothing. |

### Built into Claude Code
| Agent | Purpose |
|---|---|
| `Explore` | Fast read-only search across many files |
| `Plan` | Implementation plans |
| `general-purpose` | Multi-step research and tasks |
| `claude-code-guide` | Questions about Claude Code itself |

Known overlaps (candidates for consolidation): `frontend-developer` / `react-specialist`,
`test-automator` / `qa-test-engineer`, `code-reviewer` / `security-reviewer`.

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
