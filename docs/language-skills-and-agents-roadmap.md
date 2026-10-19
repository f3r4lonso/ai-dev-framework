# Roadmap for broader language skills and agents

**Research date:** 2026-10-18  
**Goal:** Extend Workshop's language coverage while keeping shared resources portable, trusted, maintainable and useful across supported coding clients.

## Recommendation

Build a small, curated set of language skills around the open Agent Skills format, and keep Workshop's canonical definitions client-neutral. Do not bulk-copy “awesome skills” or install marketplace bundles. Use official language documentation and stable ecosystem tools as the source of truth; audit any third-party skill text and scripts before adoption, and record origin, revision and license in `docs/inventory.md`.

Treat GitHub Copilot / VS Code as an additional adapter target. Current VS Code documentation presents distinct customization surfaces for always-on and file-based instructions, reusable Agent Skills, custom agents, prompt files, hooks and MCP. GitHub documents `.github/skills` for repository skills. This maps naturally to Workshop's separation of procedures (skills), scoped roles (agents), and project-wide conventions (project instructions). The canonical Workshop resources should remain in `skills/` and `agents/`; do not make Copilot-only files the source of truth.

## What to build first

### Phase 1: language skills

Create one focused skill per language family where idioms and validation differ:

1. `c-development`
2. `cpp-development`
3. `rust-development`
4. `go-development`
5. `dotnet-development` (C# and .NET workflows)
6. `javascript-typescript-development`

Keep `vercel-react-best-practices` and `react-state-management` as the React-specific layer. The JavaScript/TypeScript skill should cover language, module/runtime distinctions, type safety and project tool discovery, not duplicate React performance guidance.

Each skill should explain when it applies; how to inspect the repository before choosing a language version, framework or command; idiomatic implementation concerns; error handling and security; tests and static checks; and how to report checks that were not run. Avoid prescribing a single package manager or framework where projects differ. Put deeper references in `references/` and keep the main `SKILL.md` concise.

### Phase 2: only add specialist agents when proven useful

Agents are roles with scoped tools; they are not a substitute for domain instructions. Start by pairing new skills with the existing `backend-architect`, `frontend-developer`, `debugger`, `code-reviewer`, `security-reviewer` and `qa-test-engineer` as appropriate.

After repeated real tasks show a clear role gap, consider a small set of specialists such as `systems-engineer` (C/C++), `rust-engineer`, `go-engineer`, or `dotnet-engineer`. Do not create one agent per language by default. Define each agent's task boundary, allowed tools, edit scope, verification expectations, and interaction with the existing quality/security agents. Codex does not enforce the generated per-agent tool limits, so instructions are not a security boundary; follow the existing `infra/SECURITY.md` guidance.

### Phase 3: Copilot compatibility and validation

- Confirm the current GitHub Copilot and VS Code skill discovery paths and supported frontmatter against official documentation before claiming compatibility.
- Add an adapter or documented symlink/copy workflow only if it preserves the canonical-source rule and can be maintained without divergent copies.
- Test discoverability and invocation in each actual client separately. Current support differs by client and harness; do not infer support from a shared file format alone.
- Consider generated `.agent.md` wrappers for Copilot only after validating how its tool allowlists, invocation and file locations behave in the target setup.
- Track compatibility as **verified**, **documented but unverified**, or **unsupported**, consistent with `docs/ai-architecture.md`.

## Cross-language workflow principles

- Start from the project's own instructions, configuration, lockfiles and CI commands; do not assume the newest language standard or preferred tool is already adopted.
- Make skills teach idioms and decision points, not merely restate general rules or paste a tutorial.
- Choose validation from the actual project: compiler/build, formatter, linter/static analysis, tests and security checks. Report exact commands and outcomes.
- Treat external skill repositories as untrusted input. Review their instructions, scripts, tool declarations, license and provenance before copying anything; never run their installers.
- Keep new dependencies out of shared skills unless required. If a skill needs a tool, explain installation and version discovery without silently adding it.
- Add resources to canonical catalogues and `docs/inventory.md`; regenerate client adapters only from canonical source files.

## Source-of-truth references by ecosystem

Prefer these maintained or authoritative sources when writing each skill. Tool suggestions are starting points; select versions and commands from the target project.

| Area | Recommended primary references | Skill content to derive |
|---|---|---|
| Agent Skills format | [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) | Portable directory/frontmatter structure, progressive disclosure and validation; format support still varies between clients |
| Copilot / VS Code customization | [VS Code agent customization](https://code.visualstudio.com/docs/copilot/concepts/customization), [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills), [custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents), and [GitHub Copilot skills](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | File locations and supported semantics for the relevant Copilot harness; keep separate from Workshop's source-of-truth format |
| C | [SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard), [GCC manuals](https://gcc.gnu.org/onlinedocs/) | Memory, integer, bounds and error-handling hazards; compiler and warning selection must follow project/toolchain |
| C++ | [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines), [Clang-Tidy documentation](https://clang.llvm.org/extra/clang-tidy/) | RAII, ownership, modern idioms and static-analysis choices; recognize existing language standard and build system |
| Rust | [The Rust Programming Language](https://doc.rust-lang.org/book/), [Rust Reference](https://doc.rust-lang.org/reference/), [Cargo Book](https://doc.rust-lang.org/cargo/) | Ownership/borrowing, error types, Cargo workflows, formatting and linting; preserve MSRV and edition settings |
| Go | [Go documentation](https://go.dev/doc/), [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) | Go idioms, modules, tests, formatting and concurrency; Effective Go itself notes it predates modules and generics, so supplement it |
| C# / .NET | [C# documentation](https://learn.microsoft.com/en-us/dotnet/csharp/), [.NET coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions), [.NET CLI](https://learn.microsoft.com/en-us/dotnet/core/tools/) | Target framework/language version, async, nullable reference types, analyzers, CLI tests/build and project conventions |
| JavaScript | [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), [ECMAScript specification](https://tc39.es/ecma262/) | Language features separately from host runtime APIs; distinguish browser, Node.js and other runtimes |
| TypeScript | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/), [TSConfig Reference](https://www.typescriptlang.org/tsconfig/) | Type narrowing, compiler options, declarations, module/resolution settings and JS interoperability |
| React | [React Learn](https://react.dev/learn), plus existing Workshop React skills | Keep framework guidance aligned with the project's React version and existing Workshop material |

## Acceptance checks for each candidate resource

Before adding it to the canonical tree:

1. Check that no existing skill already covers the same workflow; specify the boundary from related skills.
2. Write a clear frontmatter description with the situations that should activate the skill.
3. Test it against at least one representative repository/task and adjust instructions from observed gaps.
4. Review for outdated commands, untrusted instructions, unsafe automation, unnecessary dependencies and licensing constraints.
5. Add the resource to its catalogue and inventory, note its sources and local changes, and regenerate adapters.
6. Verify each supported client independently; mark untested compatibility clearly.

## Sources and freshness

This is an ecosystem research snapshot as of 2026-10-18. Official documentation and standards evolve. Recheck client format support and language-version guidance when implementing a resource; the roadmap is not evidence that any proposed skill or agent has been installed or tested.
