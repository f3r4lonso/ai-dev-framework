# Research Brief for Homero: VS Code Extension Engineering Agents, Skills, and Repositories

**Prepared:** 18 October 2026  
**Purpose:** Give Homero a structured research brief to evaluate reusable AI agents, skills, and technical references for building high-quality Visual Studio Code extensions, particularly for Workshop AI.

> **Research status:** This document consolidates repositories and architectural recommendations identified during the conversation. Repository links are provided as discovery starting points, not as a claim that every repository, skill, compatibility statement, or API is currently verified. Before adopting anything, Homero must inspect the live repository, license, recent activity, compatibility, dependencies, and security posture.

---

## 1. Product context and goal

Workshop AI aims to make AI work better, more efficiently, and more sustainably through collaboration among available AI clients. The extension should not merely be a unified chat interface. It should enable coordinated workflows among coding agents and tools while preserving the native strengths and interaction models of each client.

A promising approach is a shared coordination layer plus client-specific adapters. Avoid forcing every AI client into an identical interface or assuming every client supports the same protocol.

### Research objective

Find and evaluate existing agents, skills, and technical repositories that can help implement and maintain a robust VS Code extension stack. Prefer reuse over reinventing, but do not install or adopt repositories blindly.

### Desired outcomes

1. A curated repository catalog with verified links.
2. A mapping from each technology to useful agents, skills, and source references.
3. An adoption scorecard covering quality, compatibility, security, maintenance, and token efficiency.
4. A recommendation for which resources to adopt, adapt, reject, or monitor.
5. A portable skills architecture for supported coding agents, with client-specific configuration kept separate.

---

## 2. Core technologies to master

### Essential extension platform

- **TypeScript:** type system, interfaces, generics, discriminated unions, modules, async/await, error handling.
- **Node.js:** filesystem, environment variables, events, streams, process management.
- **VS Code Extension API:** activation lifecycle, commands, workspace, window, languages, configuration, diagnostics, Tree Views, status bar, tasks, terminals, extension context.
- **Extension packaging and distribution:** `@vscode/vsce`, VSIX packaging, extension manifests, activation events, compatibility requirements.
- **Git and package management:** Git, npm or pnpm, dependency auditing, lockfiles.

### UI technologies

- **Webview API:** embedded HTML UI, message passing, lifecycle, Content Security Policy.
- **React:** components, hooks, state management, component architecture.
- **HTML, CSS, JavaScript:** DOM, accessibility, responsive layout, safe rendering.
- **Vite:** UI development and bundling.
- **CSS Modules or Tailwind CSS:** optional styling approaches.
- **Zustand:** optional lightweight state management.
- **TanStack Query:** optional asynchronous data and cache management.
- **Lucide:** icons.
- **Storybook:** optional isolated component development.
- **Monaco Editor:** only if a separate browser-based code editor is needed; VS Code already provides its own editor.

### Process and communication technologies

- `child_process`, particularly `spawn`, and Node.js streams.
- `vscode.Terminal` for native integrated terminal workflows.
- PTY libraries when a genuine interactive terminal is required.
- JSON and JSONL message formats.
- HTTP/REST, WebSockets, Server-Sent Events, and IPC as appropriate.
- `AbortController` for cancellation.
- Event-driven coordination, task queues, state machines, retries, and timeout management.

### AI and agent interoperability

- MCP (Model Context Protocol), including client/server concepts, tools, resources, capability negotiation, sessions, and permissions.
- Client-specific CLI adapters for Claude Code CLI, OpenAI Codex CLI, and other supported clients.
- JSON Schema and runtime validation for protocol contracts.
- Tokenization, context budgets, prompt/context assembly, caching, and token usage measurements.
- RAG and embeddings only if semantic retrieval is needed.
- SQLite and Markdown for appropriate forms of local persistence and shared knowledge.
- Git-based traceability for code and instruction changes.

### Engineering practices

- Modular architecture, SOLID, Clean Architecture where justified, dependency injection, adapters, repositories, and explicit interfaces.
- Unit, integration, and end-to-end tests.
- Security review, secret handling, input validation, process isolation, Webview CSP, and command-injection prevention.
- Performance and memory profiling.
- Cross-platform compatibility: Windows, macOS, and Linux.
- Accessibility, keyboard navigation, and theme compatibility.

### Optional technologies

Python/FastAPI, PostgreSQL, Redis, Docker, OpenTelemetry, LSP, Tree-sitter, WebAssembly, and Electron are optional. Adopt them only when a clear architectural requirement justifies their operational cost.

---

## 3. Candidate repositories: agents and skills

These are the first repositories to investigate. Their inclusion is a candidate recommendation, not a verified endorsement of every file.

### A. GitHub Awesome Copilot
Repository: https://github.com/github/awesome-copilot

Potential value:
- Discover reusable coding agents, instructions, prompts, and skills.
- Search for TypeScript, React, architecture, testing, security, and developer workflow resources.
- Use as a catalog, not as a reason to install everything.

Skills documentation starting point:
https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md

Homero should verify the current directory structure and exact content before relying on the documentation URL.

### B. Superpowers
Repository: https://github.com/obra/superpowers

Potential value:
- Structured software-development workflows.
- Planning, test-driven development, debugging, implementation, and code review practices.
- Could improve consistency and reduce repeated ad hoc prompting.

Evaluate the current installation model, supported clients, licenses, and whether adopting the full framework or selected skills is more suitable.

### C. Superpowers Skills
Repository: https://github.com/obra/superpowers-skills

Potential value:
- Investigate whether individual skills can be reused independently.
- Compare with the main Superpowers repository to avoid duplicating content.

Verify current existence, maintenance, overlap, and the intended relationship to the main repository.

### D. Awesome Agent Skills
Repository: https://github.com/VoltAgent/awesome-agent-skills

Potential value:
- Discover skills across coding, software engineering, and other specialist areas.
- Use for discovery and selection rather than bulk installation.

Homero should record the exact source repository for every skill selected from the catalog.

### E. Agent Skills specification
Repository: https://github.com/agentskills/agentskills

Potential value:
- Investigate a portable convention for packaging reusable agent skills.
- Evaluate how skills can be shared across clients while keeping platform-specific configuration separate.

Verify the current specification, required file structure, metadata conventions, and supported client implementations.

### F. Anthropic Skills
Repository: https://github.com/anthropics/skills

Potential value:
- Study concrete examples of reusable skills and supporting resources.
- Adapt useful instruction design patterns where license and compatibility permit.

Do not assume every skill is specifically for software engineering or directly portable to every coding client.

---

## 4. Official technical reference repositories

These are primarily source references and examples, not necessarily AI-agent or skill libraries.

### VS Code Extension Samples
https://github.com/microsoft/vscode-extension-samples

Use for:
- Extension activation and commands.
- Webviews.
- Tree Views and editor integrations.
- API usage patterns and test examples.

This should be a primary technical reference for implementation decisions.

### MCP TypeScript SDK
https://github.com/modelcontextprotocol/typescript-sdk

Use for:
- TypeScript-based MCP clients and servers.
- Protocol integration.
- Tool and resource interoperability.

Verify the current stable version, migration guidance, API status, and compatibility before implementation.

### TypeScript Website
https://github.com/microsoft/TypeScript-Website

Use as an educational and reference source for TypeScript. For implementation details, also consult the official documentation:
https://www.typescriptlang.org/docs/

### VS Code API documentation
https://code.visualstudio.com/api

Use as the primary reference for extension behavior, packaging, testing, Webviews, and publication.

### VS Code publishing documentation
https://code.visualstudio.com/api/working-with-extensions/publishing-extension

Use for VSIX packaging and publication workflow.

---

## 5. Proposed Workshop AI agent and skill taxonomy

These are proposed internal names, not claims that matching public repositories already exist.

| Proposed agent/skill | Main responsibilities | Key references |
|---|---|---|
| `vscode-extension-engineer` | Extension lifecycle, commands, configuration, Tree Views, Webviews | VS Code API; extension samples |
| `typescript-expert` | Type safety, generics, async code, module design | TypeScript documentation |
| `react-ui-engineer` | React UI, Vite, styling, state, accessibility | React and Vite documentation; vetted UI skills |
| `nodejs-process-engineer` | CLI execution, streams, PTY, cancellation, IPC | Node.js documentation; vetted process-management resources |
| `mcp-integration-engineer` | MCP clients/servers, tools, resources, capability handling | MCP specification and TypeScript SDK |
| `software-architect` | Boundaries, interfaces, adapters, SOLID, trade-offs | Vetted architecture skills; official examples |
| `testing-engineer` | Unit, integration, regression, and extension-host tests | VS Code testing documentation; selected testing skills |
| `security-auditor` | Secret management, Webview security, process safety, dependency review | Official security guidance and trusted advisories |
| `performance-engineer` | Activation time, memory, latency, CPU, token consumption | Profiling tools and performance documentation |
| `extension-release-engineer` | Build, VSIX packaging, CI/CD, compatibility, release checks | VS Code publishing documentation |

Recommended division:
- **Agents** handle multi-step tasks, coordination, decisions, and review.
- **Skills** provide reusable procedural knowledge for a narrow task.
- **Technical repositories and official documentation** are reference sources, not automatically installable skills.
- **Client adapters** translate the shared architecture to each CLI's native behavior.

---

## 6. Suggested architecture

```text
workshop/
├── agents/
│   ├── vscode-extension-engineer.md
│   ├── software-architect.md
│   ├── security-auditor.md
│   └── testing-engineer.md
├── skills/
│   ├── vscode-extension-api/
│   │   └── SKILL.md
│   ├── typescript-best-practices/
│   │   └── SKILL.md
│   ├── react-webviews/
│   │   └── SKILL.md
│   ├── cli-process-management/
│   │   └── SKILL.md
│   ├── mcp-integration/
│   │   └── SKILL.md
│   └── extension-security/
│       └── SKILL.md
├── clients/
│   ├── claude/
│   └── codex/
└── docs/
    └── extension-development/
        └── repository-catalog.md
```

This is a proposed layout. Adjust it to the existing Workshop AI repository and the native conventions of each client rather than imposing a duplicate hierarchy.

### Architecture principles

1. Keep the coordination/domain layer independent from any one AI vendor.
2. Implement separate adapters for each CLI and its native protocol.
3. Do not assume every client supports MCP or exposes identical features.
4. Keep UI concerns separate from process orchestration.
5. Model task state, cancellation, retries, errors, and resource cleanup explicitly.
6. Share stable skills where possible; keep client-specific metadata and configuration in their proper locations.
7. Avoid duplicating the same long instructions across agents and skills. Link to canonical shared resources when supported.
8. Use official documentation and versioned interfaces as the source of truth.

---

## 7. Adoption and audit checklist

Homero should evaluate each candidate before incorporating it.

### Repository checks
- [ ] Repository URL resolves to the intended project.
- [ ] License is explicit and compatible with intended use.
- [ ] Maintenance and recent activity are acceptable.
- [ ] Release/tag/version history is understood.
- [ ] Dependencies and transitive dependencies are reviewed.
- [ ] Instructions and scripts do not contain suspicious or unnecessary operations.
- [ ] No secrets or unsafe credential-handling patterns are present.
- [ ] Installation does not require unexplained broad permissions.

### Agent/skill quality checks
- [ ] Scope and expected inputs/outputs are clear.
- [ ] Instructions are concrete, testable, and non-contradictory.
- [ ] Compatible client formats and limitations are documented.
- [ ] No redundant overlap with existing Workshop AI skills.
- [ ] References point to authoritative, maintained documentation.
- [ ] The skill can be tested on representative tasks.
- [ ] Token cost and context footprint are reasonable.
- [ ] Failure handling and security constraints are addressed.

### Integration checks
- [ ] Determine whether the resource should be adopted, adapted, linked, or rejected.
- [ ] Preserve original license and attribution requirements.
- [ ] Record source URL, version/commit, date checked, and local changes.
- [ ] Avoid copying entire repositories when a small, licensed, auditable skill is sufficient.
- [ ] Test in an isolated branch or sandbox before using it in production.
- [ ] Record platform-specific installation instructions separately from portable skill content.

---

## 8. Token efficiency and sustainability criteria

Because Workshop AI explicitly aims to make AI collaboration more efficient and sustainable, evaluate resources for operational cost as well as code quality.

Prioritize:
- Small, focused skills loaded only when relevant.
- Shared canonical instructions instead of duplicated long prompts.
- Clear task routing to the correct specialist.
- Structured outputs and concise handoffs between agents.
- Incremental context passing instead of repeatedly sending the entire repository.
- Reuse of test results, repository maps, and verified technical findings.
- Explicit stopping conditions and bounded retry policies.
- Instrumentation for token usage, latency, task success, and failure recovery.

Do not assume a skill automatically saves tokens. Measure the effect on representative Workshop AI tasks and compare quality as well as cost.

---

## 9. Initial prioritization

Start by evaluating these five resources:

1. **Awesome Copilot** — broad discovery of agents and skills.
   https://github.com/github/awesome-copilot
2. **Superpowers** — structured software-development workflows.
   https://github.com/obra/superpowers
3. **Awesome Agent Skills** — additional skills discovery.
   https://github.com/VoltAgent/awesome-agent-skills
4. **VS Code Extension Samples** — authoritative implementation examples.
   https://github.com/microsoft/vscode-extension-samples
5. **Agent Skills specification** — investigate reusable, portable skill packaging.
   https://github.com/agentskills/agentskills

Also evaluate the MCP TypeScript SDK if MCP integration is part of the immediate scope:
https://github.com/modelcontextprotocol/typescript-sdk

This is a starting shortlist, not a final ranking. Homero should verify current repository state and compare alternatives before making adoption decisions.

---

## 10. Instructions for Homero

Act as a senior AI tooling and developer-experience research engineer.

Your task is to turn this brief into an evidence-backed adoption plan for Workshop AI.

1. Inspect the existing Workshop AI architecture and repository conventions first, if repository access is available.
2. Verify every candidate repository and discover additional high-quality resources specifically relevant to TypeScript, VS Code extensions, Webviews/React, Node.js process management, MCP, testing, security, and agent skill portability.
3. Distinguish clearly between:
   - agent frameworks;
   - individual agents;
   - reusable skills;
   - official technical reference repositories;
   - SDKs and runtime dependencies.
4. For every candidate, record its purpose, URL, license, maintenance signals, supported clients, installation method, token/context implications, security concerns, overlap with existing resources, and recommendation.
5. Do not invent repository capabilities, compatibility, popularity, or maintenance status. Mark unverified fields as “Not verified.”
6. Prefer primary sources, official documentation, repository READMEs, license files, releases, and actual skill contents over second-hand summaries.
7. Recommend an initial minimal set of high-value resources and explain why each is worth adopting.
8. Identify resources that should only be referenced, not copied or installed.
9. Propose portable shared skills and client-specific adapters without forcing a lowest-common-denominator design.
10. Provide a phased implementation plan with acceptance criteria and a small evaluation suite to measure code quality, task success, latency, token usage, and maintainability.
11. Do not install dependencies, run untrusted scripts, modify production files, or alter repository configuration without explicit authorization.
12. Return a concise executive summary, an evidence-based repository matrix, the recommended architecture, a risk register, and prioritized next actions.

### Required deliverables

- `repository-catalog.md`: verified repository catalog with sources and evaluation.
- `agent-skill-mapping.md`: technology-to-agent/skill mapping.
- `adoption-plan.md`: prioritized adoption, adaptation, rejection, or monitoring decisions.
- `evaluation-plan.md`: reproducible tests and metrics for quality, cost, and reliability.

**Definition of done:** Every recommended adoption has a verified source, a clear use case, a compatibility assessment, a security/license review, and a measurable reason to include it in Workshop AI.
