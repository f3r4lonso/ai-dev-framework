# Skills, agents and tools worth evaluating

Prepared: 2026-10-21.

This selection focuses on your work: trading research, application development, project organization, and creative projects. It is a practical shortlist, not a universal ranking. The linked repositories were checked as sources on 2026-10-21; that does not constitute a security, license, compatibility, maintenance, or quality audit of every item. Nothing here has been installed or tested locally.

A **skill** gives an AI a repeatable method for a task. An **agent** defines a specialist role, its responsibilities, and expected outputs. The potential benefits below are an assessment, not measured results.

## 12 skills worth considering

| # | Skill and download source | What it does | How it could improve your work |
|---|---|---|---|
| 1 | [XLSX — Anthropic](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Creates, edits, cleans, and formats spreadsheets, including formulas and charts. | Turn trading exports into an organized journal and comparison sheets with less manual work. |
| 2 | [PDF — Anthropic](https://github.com/anthropics/skills/tree/main/skills/pdf) | Extracts text and tables, processes scanned documents, and creates or combines PDFs. | Make research reports and trading documents easier to search and reuse. |
| 3 | [Playwright — OpenAI](https://github.com/openai/skills/tree/main/skills/.curated/playwright) | Automates a real browser: navigation, forms, screenshots, and interface inspection. | Check whether your applications work through actual user flows and document problems visually. |
| 4 | [Document coauthoring — Anthropic](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | Structures collaborative writing through context gathering, drafting, and reader review. | Produce clearer project briefs and specifications, reducing repeated explanations. Overlaps with Homero and Atlas. |
| 5 | [Systematic Debugging — Superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) | Investigates root causes through a structured debugging process. | Could reduce repeated attempts to fix the same application problem. Complements your existing debugger. |
| 6 | [Verification Before Completion — Superpowers](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion) | Requires evidence before declaring a change complete. | Give you clearer proof that a requested fix works. Overlaps with your engineering lifecycle. |
| 7 | [DOCX — Anthropic](https://github.com/anthropics/skills/tree/main/skills/docx) | Creates and edits Word documents, templates, comments, and tracked changes. | Prepare polished strategy manuals, project proposals, and editable reports. |
| 8 | [PPTX — Anthropic](https://github.com/anthropics/skills/tree/main/skills/pptx) | Creates, reads, edits, and reorganizes presentations. | Convert research or project plans into slides you can explain and share. |
| 9 | [MCP Builder — Anthropic](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | Guides development of connectors between AI assistants and external services. | Help build reusable connections for Workshop AI when an appropriate API exists. Requires development work. |
| 10 | [Frontend Design — Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Guides visual direction, typography, color, and layout. | Give your applications a more deliberate appearance. Already covered in your Workshop. |
| 11 | [React Best Practices — Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | Provides React and Next.js performance guidance. | Help keep dashboards responsive as they grow. Already covered in your Workshop. |
| 12 | [Web Design Guidelines — Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Reviews interfaces for accessibility, usability, and related implementation issues. | Improve forms, navigation, keyboard access, and mobile use. Already covered in your Workshop. |

## 8 agents worth considering

| # | Agent and download source | What it does | How it could improve your work |
|---|---|---|---|
| 13 | [Research Synthesist — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/research/research-synthesist.md) | Evaluates sources, traces claims, and combines evidence into a structured assessment. | Receive research that explains what is supported, disputed, or uncertain, with less repetition. |
| 14 | [Quant Analyst — wshobson](https://github.com/wshobson/agents/blob/main/plugins/quantitative-trading/agents/quant-analyst.md) | Covers financial models, backtesting, risk metrics, and market data analysis. | Help investigate strategy hypotheses with costs and out-of-sample checks. Substantial overlap with your existing trading agents. |
| 15 | [Sprint Prioritizer — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/product/product-sprint-prioritizer.md) | Prioritizes features, backlogs, and work allocation. | Choose the next useful increment across your projects. Complements Atlas's project planning. |
| 16 | [Reality Checker — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/testing/testing-reality-checker.md) | Reviews completion and release readiness against evidence. | Get an independent assessment of what works and what still needs attention. Overlaps with your review roles. |
| 17 | [Security Auditor — wshobson](https://github.com/wshobson/agents/blob/main/plugins/security-scanning/agents/security-auditor.md) | Reviews authentication, permissions, vulnerabilities, dependencies, and security practices. | Assess applications before exposing them online. Your existing security reviewer already covers much of this. |
| 18 | [UX Researcher — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/design/design-ux-researcher.md) | Plans user research and analyzes usability and behavior. | Discover why an application feels confusing and which changes deserve priority. Already covered in your Workshop. |
| 19 | [Economy Designer — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/game-development/economy-designer.md) | Models game currencies, rewards, resource consumption, progression, and inflation. | Particularly relevant to your castle MMO: examine PvP rewards, trading, upgrades, and premium currency together. |
| 20 | [Image Prompt Engineer — Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/design/design-image-prompt-engineer.md) | Writes detailed image prompts with photographic composition, lighting, and style. | Improve promotional imagery and visual references. Its focus is photography; game sprites need additional direction. |

## Recommended first evaluations

1. **XLSX:** organize trading exports and create reusable analysis sheets.
2. **PDF:** extract and reuse information from reports and documents.
3. **Playwright:** inspect application behavior through actual browser flows.
4. **Research Synthesist:** assess sources and produce clearer research conclusions.
5. **Economy Designer:** model the castle MMO's rewards, trading, and progression.

These are candidates to evaluate against the current Workshop catalogue. A match in name or capability does not establish equivalence. Do not replace existing resources until the specific candidate has been reviewed for content, maintenance, license, compatibility, permissions, and dependencies.

## Example workflows

**Trading research:** extract material from PDFs → evaluate its sources → investigate a testable hypothesis with the existing trading agents → export results to a spreadsheet.

**Application work:** define the brief → prioritize the next increment → implement → inspect browser flows with Playwright → review completion against evidence.

**Castle MMO:** use the existing game design agents → model rewards, trading, and upgrades with Economy Designer → review progression before implementation.

## Complementary tools and discovery sources

These are not skills or agents, so they are listed separately from the 20 candidates above.

| Resource | Type | Potential use | Status |
|---|---|---|---|
| [Context7](https://github.com/upstash/context7) | MCP documentation tool | Retrieve current library documentation during application work. | Candidate only; an external MCP connection needs privacy, permission, and reliability review. |
| [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP browser tool | Let an AI inspect and operate a browser for UI checks. | Candidate only; browser access can expose authenticated pages and perform actions, so use a disposable test account and review permissions. |
| [Superpowers](https://github.com/obra/superpowers) | Skill/workflow collection | Structured development workflows such as debugging and verification. | Candidate source; overlaps with parts of the existing engineering lifecycle. Review only a specific skill needed. |
| [Trail of Bits skills](https://github.com/trailofbits/skills) | Security skills | Security research and audit workflows. | Candidate source; does not replace project security review or automated checks. |
| [Anthropic skills](https://github.com/anthropics/skills) | Skills collection | Document creation, coding, and other task skills. | Candidate source; check each skill's license and compatibility individually. |
| [Agency Agents](https://github.com/msitarzewski/agency-agents) and [wshobson/agents](https://github.com/wshobson/agents) | Agent/skill collections | Discover specialist role ideas. | Directories to scout, not vetted packs to install. Check the Workshop catalogue first. |

## Compatibility and licensing

Download availability does not establish compatibility with every AI client. Some resources need dependencies or format adaptation. Browser automation also needs an appropriate browser environment.

Anthropic explicitly describes its four document skills—XLSX, PDF, DOCX, and PPTX—as **source-available under specific licenses**. Check their individual terms before reuse or redistribution. See the [Anthropic repository notes](https://github.com/anthropics/skills#about-this-repository).

This document records recommendations only. It does not install resources, adopt third-party instructions, or authorize running downloaded installers. Before adopting an item, follow the [contributor guide](../manuals/contributor-guide.md), register its source and license in the inventory, and review its files as untrusted input.
