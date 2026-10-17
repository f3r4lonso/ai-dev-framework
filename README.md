# AI development framework

Personal, reusable setup for AI-assisted development with [Claude Code](https://code.claude.com/docs):
shared agents, skills and instructions used across my application projects.

## Contents
- `CLAUDE.md` — workspace-wide rules loaded by Claude Code.
- `.claude/agents/` — subagents by area: `ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`.
- `.claude/skills/` — on-demand skills (UI/UX, frontend, backend, trading).
- `ai-infra/README.md` — inventory: sources, commits, licenses, local modifications and conventions.
- `ai-infra/THIRD_PARTY_NOTICES.md` — licenses of the third-party agents and skills included here.
- `SECURITY.md`, `docs/` — security policy and onboarding guide.
- `.githooks/`, `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/` — secret scanning (local hook and CI).

Application projects live in `Applications/` as separate repositories and are not part of this repo.

## Usage
Clone into the workspace root (e.g. `C:\Users\<you>\Repos`) and start Claude Code there, or from an application
repo with `claude --add-dir <workspace root>` so the shared agents and skills load.

## Connect your Claude subscription (Claude Code CLI)

Each person signs in with **their own** Claude account. Claude Code needs a **Pro, Max, Team or Enterprise**
plan (or a Claude Console account); the free claude.ai plan does not include Claude Code.

1. **Install Claude Code** (no Administrator rights needed):

   | System | Command |
   |---|---|
   | Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` |
   | Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |
   | macOS, Linux, WSL | `curl -fsSL https://claude.ai/install.sh \| bash` |
   | Alternatives | `winget install Anthropic.ClaudeCode` · `brew install --cask claude-code` · `npm install -g @anthropic-ai/claude-code` (Node.js 22+) |

   On Windows, [Git for Windows](https://git-scm.com/downloads/win) is recommended (it gives Claude Code a Bash shell).
   Open a **new** terminal and check: `claude --version`.

2. **Sign in with your subscription:** open a terminal in the workspace root and run `claude`.
   A browser window opens: log in with your claude.ai account and approve. If the browser does not open,
   press `c` to copy the login URL. Already inside a session? Use `/login`.

3. **Verify:** inside Claude Code run `/status`. It shows the login method, account e-mail and organization.
   For a full health check run `claude doctor` from your shell.

4. **Make sure your subscription is the one in use:** if an `ANTHROPIC_API_KEY` environment variable is set,
   it can take priority over your subscription (and bill API usage instead). Remove it
   (PowerShell: `Remove-Item Env:ANTHROPIC_API_KEY`; bash/zsh: `unset ANTHROPIC_API_KEY`) and check `/status` again.

5. **Load this framework:** start `claude` in the workspace root, or from an application repo with
   `claude --add-dir <workspace root>`. Type `/agents` to confirm the shared agents are listed.

**Switch or sign out:** `/logout`, then run `claude` again. To keep work and personal accounts apart, give each its
own configuration folder with the `CLAUDE_CONFIG_DIR` environment variable.

**Where your login is stored:** in your home folder, never in this repository. Windows:
`%USERPROFILE%\.claude\.credentials.json`; macOS: Keychain; Linux: `~/.claude/.credentials.json`.
Never copy these files into the repo or share them.

**Troubleshooting:** `Login expired` → run `/login`. `API Error: 403` → subscription inactive or missing role.
Wrong account → `/logout` and sign in again. More in [docs/onboarding.md](docs/onboarding.md).

Sources: [Advanced setup](https://code.claude.com/docs/en/setup) ·
[Authentication](https://code.claude.com/docs/en/authentication) ·
[Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install).

## Security and onboarding
This repository holds no credentials: each contributor signs in with their own Claude, Git and GitHub accounts.
- [docs/onboarding.md](docs/onboarding.md): set up Claude Code / Claude Desktop authentication, Git identity and GitHub access.
- [SECURITY.md](SECURITY.md): what must never be committed, built-in protections, how to report issues and what to do if a secret leaks.
- After cloning, enable the secret guard once: `git config core.hooksPath .githooks`.

## Agents

19 subagents in `.claude/agents/`, grouped by area.

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

### Quality
| Agent | Purpose | Responsibilities |
|---|---|---|
| `code-reviewer` | Reviews code | Bugs, security vulnerabilities, performance and reliability issues. |
| `debugger` | Fixes problems | Investigates errors, failing tests and unexpected behavior. |

### UI (visual design)
| Agent | Purpose | Responsibilities |
|---|---|---|
| `ui-designer` | Visual design | Components, layouts, mockups. |
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

Known overlap, kept on purpose: `code-reviewer` (general code quality) / `security-reviewer` (trading security, read-only). Retired components and why: `ai-infra/README.md` § Retired.

## Conventions
kebab-case, lowercase, English names for files and folders; technical content in English.
Third-party content is reviewed before it is added and registered in the inventory.
