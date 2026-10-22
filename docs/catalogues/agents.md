# Agent catalogue

26 shared agents and 3 personal agents, one row each. All 29 have native generated copies for Claude/Codex/Copilot/Gemini via the [shared installation standard](../manuals/shared-resource-installation.md), plus explicit canonical-file access for manual-use clients. Live discovery is tracked separately from copied-file validation. The canonical definition is the linked file; this page copies no bodies. Sources,
licenses and local modifications: [inventory](../../docs/inventory.md#installed-agents).

**Clients:** 20 agents were observed in Claude Code on 2026-10-17; `product-idea-excavator` and `music-composer` were added on 2026-10-18 and require a Claude discovery re-check. In Codex CLI each
has a generated wrapper in `clients/.codex/agents/` (loading Unverified; tool limits not enforced, see the
[Codex guide](../../clients/codex-cli/README.md#7-limitations)). **Access:** RO = read-only; Edit = can change files.

| Area | Agent | Use it to | Access |
|---|---|---|---|
| AI | [ai-environment-auditor](../../agents/ai/ai-environment-auditor.md) | Audit agents, skills, rules, prompts and the client adapters; plan changes (apply mode edits infrastructure files only) | RO audit / Edit apply |
| AI | [task-resource-scout](../../agents/ai/task-resource-scout.md) | Research a task broadly, compare and vet Workshop or public agents/skills, install or improve useful shared resources, and update registries and adapters | Edit + web + shell + agent review (bounded to shared AI infrastructure; Claude/Codex adapters, other clients by supported path access) |
| AI | [prompt-reviewer](../../agents/ai/prompt-reviewer.md) | Score and harden one prompt or agent/skill instruction | RO |
| AI | [product-idea-excavator](../../agents/ai/product-idea-excavator.md) | Explore vague ideas through discovery questions, identify user and business or human value, and define an evidence-based MVP | RO + web |
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
| Game development | [game-developer](../../agents/game-development/game-developer.md) | Read-only game architecture, engine/platform research, persistence and future device validation; no implementation | RO + web |
| Creative | [game-designer](../../agents/creative/game-designer.md) | Develop a basic videogame idea into original concepts, cohesive play/systems, narrative/art/audio direction and a concrete design brief; no implementation | RO + web |
| Creative | [game-art-music-director](../../agents/creative/game-art-music-director.md) | Cohesive art/music direction, bibles, asset/cue briefs, adaptive music behavior and creative reviews; no asset production | RO + web |
| Creative | [music-composer](../../agents/creative/music-composer.md) | Compose, remix or arrange a track as a reproducible Python script that writes MIDI plus a WAV preview to `projects/music/` | Edit (track folder) |

Trading agents assume the Trading-app root as the working directory (see
[Trading-app entry](../projects/trading-app/README.md)).

## Game design and planning

Start with `workshop:game-designer` to expand a basic idea into original concepts, a worked play example and
a focused design brief. Use `workshop:game-developer` for engine/platform research, technical feasibility and
architecture. Both roles are read-only; programming and asset production need a separately scoped task.

Supporting skills: [game-ui-ux](../../skills/game-ui-ux/SKILL.md) for game interfaces and
[save-systems](../../skills/save-systems/SKILL.md) for persistence and recovery. For the persistent castle MMO
planning scope and approval gates, see the [task brief](../../tasks/projects/persistent-castle-mmo/persistent-castle-mmo-planning.md).

Use `workshop:game-art-music-director` to deepen approved creative pillars into visual/musical production
briefs and review criteria. It directs; `music-composer` and other production roles execute separately.
Added 2026-10-19 following focused auditor review; live client discovery remains unverified.

Both game agents were added on 2026-10-19. Generated registrations are checked; live Claude/Codex discovery
requires a fresh-session manual check. The creative agent has not yet been trialled with a real game idea.

Known overlap, kept on purpose: `code-reviewer` (general code quality) and `security-reviewer` (workshop security rules,
plus trading checks in Trading-app; read-only). Retired agents and why: [inventory](../../docs/inventory.md#retired-2026-10-17-audit).

**Built into Claude Code** (not part of this repo): `Explore` (fast read-only search), `Plan` (implementation
plans), `general-purpose` (multi-step research), `claude-code-guide` (questions about Claude Code).

## Personal agents

Installed at user level, so they are available in every folder. Claude Code: by name; Codex: "use the `<name>` agent";
Copilot CLI: `/agent` or `copilot --agent=<name>`; Gemini CLI: `@<name>`. After editing one, run
`python scripts/codex-adapter.py personal` and `install-personal`. Observed 2026-10-18 in Claude Code, Codex and
Copilot CLI; Gemini CLI unverified (daily quota exhausted during the test).

| Agent | Use it to | Access |
|---|---|---|
| [homero-prompt-engineer](../../agents/personal-assistants/homero-prompt-engineer.md) | Homero: turn ideas or specs into precise prompts, task briefs and agent definitions; revise prompts | RO |
| [atlas-project-planner](../../agents/personal-assistants/atlas-project-planner.md) | Atlas: turn an idea into a reviewed, ready-to-start project plan (Homero drafts, prompt-reviewer reviews, one question at a time); registers it and pushes after your OK. Claude Code: run as main session `claude --agent atlas-project-planner` from the workshop root | Edit + shell + web; orchestrator |
| [thor-writer](../../agents/personal-assistants/thor-writer.md) | Thor: proofread, translate (ES/EN), polish and draft replies, prepare input for Homero | RO |
