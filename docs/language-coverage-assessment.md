# Workshop language and framework coverage assessment

**Reviewed:** 2026-10-18  
**Scope:** Shared canonical agents and skills listed in `docs/catalogues/agents.md` and `docs/catalogues/skills.md`.  
**Purpose:** Identify what Workshop already supports for C, C++, Rust, Go, C#, TypeScript, JavaScript and React.

## Summary

Workshop already has reusable engineering workflow, general backend/API, quality, security, and frontend roles. Its strongest explicit language and framework coverage is Python and React. It has no dedicated C, C++, Rust, Go, C#/.NET, or general JavaScript/TypeScript language skill or agent.

That means the current setup can still help with those languages through the general agents and `engineering-lifecycle`, but it does not provide curated idioms, ecosystem commands, compiler/toolchain guidance, or language-specific verification procedures. The existing React skills address React and UI concerns; they do not constitute broad JavaScript or TypeScript coverage.

## Current reusable coverage

| Area | Existing support | Fit for requested languages |
|---|---|---|
| General engineering | `engineering-lifecycle` | Strong cross-language requirements, planning, verification, review and reporting workflow |
| Backend design | `backend-architect`, `api-design-principles` | Useful across Go, C#, Rust and JavaScript services; architecture guidance rather than language idioms |
| Python | `python-pro`, `python-testing-patterns`, `python-error-handling` | Explicit and well covered, but not transferable as language instructions |
| React | `frontend-developer`, `vercel-react-best-practices`, `react-state-management` | Existing React coverage; includes component work, performance and state choices |
| TypeScript / JavaScript | `vscode-extension-development` | TypeScript only in the specific context of VS Code extensions; not general TS/JS application development |
| General quality | `code-reviewer`, `debugger`, `qa-test-engineer`, `security-reviewer` | Useful cross-language roles; project-specific build and test commands still need discovery |
| C / C++ / Rust / Go / C# | No dedicated canonical skill or agent | Gap in language-specific workflow and idiom coverage |

## Coverage findings

- **Verified from catalogues:** 21 agents and 24 skills are currently catalogued. The explicit non-trading language and stack resources are primarily Python, React, API design, and VS Code extension development.
- **Verified from catalogues:** `frontend-developer` supports React/Next.js component and layout work. The React skills are focused on performance and state management.
- **Verified from catalogues:** `vscode-extension-development` covers TypeScript only for the VS Code Extension API and Workshop AI context.
- **Inference:** General roles can assist in additional languages, but without a project rules file or an on-demand language skill they may miss language-specific safety rules, idioms, formatters, build systems and test commands.
- **Recommendation:** Add reusable language skills before multiplying agents. A skill can carry researched workflow and validation knowledge while the existing implementation and review agents perform the role.

## Suggested coverage model

| Language / framework | Initial shared skill | Suggested reusable specialist agent? |
|---|---|---|
| C | `c-development` | Consider a systems engineer only when recurring C work establishes a distinct role |
| C++ | `cpp-development` | Could share a systems role with C if its scope and tool permissions remain clear |
| Rust | `rust-development` | Consider after Rust work demonstrates repeatable implementation needs |
| Go | `go-development` | Consider for recurring service work beyond general backend architecture |
| C# / .NET | `dotnet-development` | Consider for recurring .NET implementation and framework-specific review |
| JavaScript / TypeScript | `javascript-typescript-development` | Existing `frontend-developer` may cover React implementation; assess a web engineer role only if needed |
| React | Keep existing React resources | No new React agent recommended from this inventory alone |

These are candidate names and scope suggestions, not resources already installed. Keep project-specific frameworks and commands in each application's `AGENTS.md` / `CLAUDE.md`; keep general knowledge and repeatable workflows in shared skills.

## Assessment limits

This is a catalogue-level assessment, not a line-by-line audit of every agent and skill body, nor a benchmark of coding quality. “No dedicated resource” means no such entry appears in the canonical catalogues. Recommendations should be validated against real tasks before being treated as proven improvements.

## Sources

- [Workshop agent catalogue](catalogues/agents.md)
- [Workshop skill catalogue](catalogues/skills.md)
- [Workshop third-party inventory and licensing record](inventory.md)
