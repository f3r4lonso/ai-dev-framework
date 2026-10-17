# AI infrastructure — %USERPROFILE%\Repos

Date: 2026-10-17. Shared third-party agents and skills for backend, frontend, UI, UX and quality work,
plus own trading agents and skills (moved from the Trading-app project).
All external content is treated as **untrusted**: it was reviewed before copying and no installer was run
(`install.sh`, `npx skills add`, plugin scripts).

## Layout
- `vendor/` — full copies (`git clone --depth 1`) of the source repositories. Read-only.
- `prompts/personal-assistants/` — system prompts for claude.ai Projects (Homero, Thor). Not loaded by Claude Code.
- `../.claude/agents/` — installed agents (`ai`, `backend`, `devops`, `frontend`, `quality`, `trading`, `ui`, `ux`).
- `../.claude/skills/` — installed skills.
- `../CLAUDE.md` — shared rules for every session started under `%USERPROFILE%\Repos`.
- `../Applications/` — application projects, each its own git repo (e.g. `Trading-app`). Application code, data, tests, spec prompts and settings stay inside each project.

- `../SECURITY.md`, `../docs/onboarding.md` — security policy, leak response and per-user account/authentication setup.
- `../.githooks/pre-commit`, `../.gitleaks.toml`, `../.pre-commit-config.yaml`, `../.github/workflows/secret-scan.yml`,
  `../.gitattributes` — secret scanning: local hook (gitleaks if installed, built-in fallback; enable per clone with
  `git config core.hooksPath .githooks`), optional pre-commit framework config, CI scan, LF endings for hooks.

The root is a git repo (public on GitHub) with a whitelist `.gitignore`: only `README.md`, `CLAUDE.md`, `SECURITY.md`,
`.claude/`, `docs/`, `.githooks/`, `.github/`, `.gitattributes`, `.gitleaks.toml`, `.pre-commit-config.yaml`,
`ai-infra/README.md`, `ai-infra/THIRD_PARTY_NOTICES.md` and `ai-infra/prompts/` are versioned, and a deny block after
the whitelist keeps secret and personal files out even inside those folders. Projects are separate repos; `vendor/` is not versioned here.

Shared agents and skills load when Claude Code starts in `%USERPROFILE%\Repos`. Inside a project repo
(e.g. Trading-app) Claude only walks up to that repo's root, so start it with
`claude --add-dir %USERPROFILE%\Repos` (Trading-app ships `start-claude.bat` for this) or from the root folder.

## Conventions
- **Naming:** kebab-case, lowercase, ASCII, English for every file and folder under `.claude/` and `ai-infra/`
  (except `vendor/`). Tool-mandated names keep their form (`CLAUDE.md`, `SKILL.md`, `README.md`, `AGENTS.md`,
  `LICENSE.txt`). Agent and skill identity comes from the `name` frontmatter field; folder names should match it.
- **Language:** technical content in English, and Claude always replies to the user in English (outcome terms).
  User-facing app texts and strategy docs stay in Spanish.
- **Separation:** application code, data, tests, spec prompts (`<project>/.claude/prompts/`) and settings stay
  in the project. Reusable agents and skills live here, grouped by area; do not merge resources from different
  projects unless they are genuinely the same.
- **Trading area (`agents/trading/`, trading skills):** own resources moved from Trading-app on 2026-10-17
  (user request). They reference project paths relative to the Trading-app project root (`backend/algo/...`,
  `docs/...`, `.claude/prompts/...`), so they **assume the Trading-app root is the working directory**
  (start Claude with the project's `start-claude.bat`). Never hardcode the project's absolute path in them.

## Source repositories
| Repository | ★ / forks (2026-10-17) | Commit | License |
|---|---|---|---|
| [wshobson/agents](https://github.com/wshobson/agents) | 40,951 / 4,345 | `044b4b2` | MIT |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 25,778 / 3,009 | `408d3c9` | MIT |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 136,722 / 14,533 | `56ea9cf` | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 181,691 / 21,524 | `dbd4588` | Apache 2.0 (frontend-design) |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 32,549 / 2,842 | `063bee9` | MIT (README and SKILL) |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 996 / 69 | `434b7f9` | MIT |

## CI and tooling dependencies (not installed locally; reviewed 2026-10-17)
| Dependency | Used by | Pin | License |
|---|---|---|---|
| [actions/checkout](https://github.com/actions/checkout) | `secret-scan.yml` | v6.1.0 `d23441a48e516b6c34aea4fa41551a30e30af803` | MIT |
| [gitleaks/gitleaks-action](https://github.com/gitleaks/gitleaks-action) | `secret-scan.yml` (no license key needed for personal-account repos) | v3.0.0 `e0c47f4f8be36e29cdc102c57e68cb5cbf0e8d1e` | see repo |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | CI (`GITLEAKS_VERSION`), `.pre-commit-config.yaml`, optional local install | v8.30.1 | MIT |

## Installed agents
| Area | Agent | Source | Tools |
|---|---|---|---|
| Backend | backend-architect | wshobson (backend-development) | inherits all |
| Backend | python-pro | wshobson (python-development) | inherits all, opus model |
| Frontend | frontend-developer | wshobson (frontend-mobile-development) | inherits all |
| UI | ui-designer, design-system-architect, accessibility-expert | wshobson (ui-design) | inherits all |
| UX | ux-researcher | VoltAgent | read-only + web |
| UX | ui-ux-tester | VoltAgent | Read, Write, Edit, Bash, Glob, Grep, WebSearch |
| Quality | code-reviewer, debugger | wshobson | inherits all |
| Trading | quant-researcher, repo-researcher | own (Trading-app) | Read, Grep, Glob, WebFetch, WebSearch |
| Trading | strategy-engineer, risk-engineer, qa-test-engineer | own (Trading-app) | Read, Grep, Glob, Edit, Write, PowerShell; edit scope limited by instructions |
| Trading | exchange-integration-engineer | own (Trading-app) | Read, Grep, Glob, Edit, Write, PowerShell, WebFetch; no real orders |
| Trading | backtesting-auditor | own (Trading-app) | Read, Grep, Glob, PowerShell; Edit/Write disallowed |
| Trading | security-reviewer | own (Trading-app) | Read, Grep, Glob |
| AI | ai-environment-auditor | own (2026-10-17) | read-only audits + apply mode that edits infrastructure files only (never code, settings or vendor); self-audit; opus model |
| DevOps | git-workflow-manager | adapted from VoltAgent `git-workflow-manager` (MIT, `408d3c9`), rewritten 2026-10-17 | Read, Grep, Glob, Bash; commits freely, pushes/remotes only after user confirmation, never force-push; mandatory pre-push checklist; sonnet model |

## Installed skills
- UI/UX: `ui-ux-pro-max` (Python search scripts over local CSVs, standard library only, no network),
  `frontend-design`, `web-design-guidelines`, `interaction-design`, `design-system-patterns`,
  `responsive-design`, `visual-design-foundations`, `wcag-audit-patterns`.
- Frontend: `vercel-react-best-practices`, `react-state-management`.
- Backend: `api-design-principles`, `python-testing-patterns`, `python-error-handling`.
- Trading (own, from Trading-app; no `allowed-tools`): `strategy-specification`, `backtesting-audit`,
  `risk-management`, `market-data-quality`, `exchange-integration`, `order-lifecycle-safety`,
  `paper-trading-lifecycle`, `trading-test-review`, `repo-research`, `dependency-license-review`.
  The last two are generic in purpose but their content is Trading-app specific
  (`backend/requirements.txt`, `docs/REFERENCE_REPOS.md`); generalize only when a second project needs them.

## Local modifications (re-apply after every update)
- wshobson agents: the `name` field had a plugin prefix (`backend-development-backend-architect`…); only `name` was shortened.
- `web-design-guidelines`: fetched its rules from GitHub on every use; it now reads `guidelines.md`
  (reviewed copy) so remote instructions are never run unreviewed.
- `ui-ux-pro-max`: script paths changed from `${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/`
  (only substituted in plugin skills) to `${CLAUDE_SKILL_DIR}/scripts/`; the upstream `scripts/tests/` folder
  was removed (it validates the upstream repo layout and is not needed to use the skill).
- `ui-ux-tester`: removed the invalid tool names `chrome-mcp` and `computer-use` from `tools`.
- Folder `skills/react-best-practices` renamed to `vercel-react-best-practices` to match its `name`.

## Rejected / pending
- `anthropics/skills/webapp-testing`: requires installing Playwright and browsers (new dependency) and asks
  not to read its code. Downloaded to `vendor/`, not installed.
- `obra/superpowers` (300k★) and `affaan-m/ECC` (282k★): general frameworks with hooks and their own methodology
  that change global behavior; not specific to backend/frontend/UI/UX. Not downloaded.
- Review performed: licenses, frontmatter and tools of each agent, search for rule-bypass instructions,
  destructive commands, downloads, secrets and network imports in scripts.

## Retired (2026-10-17, audit)
Removed from `.claude/` (vendor copies remain for reference); restore only after a new review.
- `react-specialist` (VoltAgent): duplicate of `frontend-developer` plus the `vercel-react-best-practices` and
  `react-state-management` skills; its workflow relied on a non-existent "context manager" agent.
- `test-automator` (wshobson): enterprise-generic (self-healing/AI test platforms, CI/CD); for the actual stack
  `qa-test-engineer` plus `python-testing-patterns` cover it, and its proactive auto-delegation with all tools
  could take trading test work away from the scoped `qa-test-engineer` (edits `backend/tests/` only).

## Updating
`git -C vendor/<repo> pull`, review the diff (`git diff HEAD@{1}`), copy back only what was reviewed,
re-apply the local modifications above and update this file.
