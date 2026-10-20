# Client guide: Gemini CLI

This guide covers Gemini CLI alongside the Workshop. Gemini CLI can use project files, tools, custom agents, and
Agent Skills; the Workshop integrations must still be configured and verified.

**Status:** Google's current installation, authentication, context, subagent, and skill documentation was checked
on 2026-10-20. Workshop adapters are documented here but have not been validated in a live Gemini CLI session.

## 1. Install and sign in

Use the current steps in [onboarding](../../docs/onboarding.md#8-copilot-and-gemini-cli). Google's documented npm
installation requires Node.js 20 or later:

```powershell
npm install -g @google/gemini-cli
gemini
```

Follow the sign-in prompts with your own Google account. Organization accounts may require a Google Cloud project.
Gemini API key and Vertex AI authentication require different configuration; review Google's
[authentication](https://geminicli.com/docs/get-started/authentication/) and
[quota and pricing](https://geminicli.com/docs/resources/quota-and-pricing/) information before choosing a method.
Keep any API key outside the repository.

Start in the narrowest trusted project directory. The Workshop root is not a Git repository; `infra/` and each
application are separate repositories. Check which context files Gemini loaded with `/memory show`; use
`/memory reload` after changing them.

## 2. Workshop instructions and resources

Gemini CLI uses `GEMINI.md` context files by default. The workspace's root `GEMINI.md` points to
`WORKSHOP-CONTEXT.md`; verify that this pointer is in the loaded memory for your session. Gemini does not use
`AGENTS.md` by default unless its context file names are configured to include it. Open `infra/AGENTS.md`
explicitly when working in the infrastructure repository if it is not loaded.

Workshop agents and skills have distinct setup paths:

- **Personal assistants:** From the `infra/` repository root, run:

  ```powershell
  python scripts/codex-adapter.py personal
  python scripts/codex-adapter.py install-personal
  ```

  This generates Gemini subagent profiles from canonical files in `agents/personal-assistants/` and copies them to
  `%USERPROFILE%\.gemini\agents`. The installer does not overwrite existing files that are not marked as
  Workshop-generated. Start a new session and ask for a named assistant, for example `@thor-writer`.
- **Shared skills:** To expose Workshop skills across supported clients, run
  `python scripts/codex-adapter.py link-skills --user` from `infra/`. It creates links under
  `%USERPROFILE%\.agents\skills`; existing files and links are left untouched. Gemini CLI supports this personal
  Agent Skills location. Use `/skills list` to inspect the available skills and `/skills reload` after a change.
- **Tasks, catalogues, and manuals:** These are plain files, not auto-loaded resources. Find them through the
  [Workshop index](../../../INDEX.md) and open the relevant files explicitly.

Generated profiles and links point back to canonical Workshop resources; do not edit generated adapters by hand.

## 3. Safety and limitations

- Review Gemini's proposed tool actions and use trusted-folder and sandbox settings appropriate to the task.
  Workspace skills and context can influence what the agent does; inspect their sources before trusting them.
- Do not start the client in the Workshop root or another directory containing unrelated or sensitive files.
- Never expose credentials in prompts or repository files. Follow [`infra/SECURITY.md`](../../SECURITY.md).
- A generated personal assistant's written read-only instructions are not a security boundary. Use restrictive
  client permissions and review actions.
- The instructions, skills, and personal agents described above have not been tested locally for this Workshop.

## 4. Sources and evidence

- [Gemini CLI installation](https://geminicli.com/docs/get-started/installation/) and
  [authentication](https://geminicli.com/docs/get-started/authentication/).
- [Project context (`GEMINI.md`)](https://geminicli.com/docs/cli/gemini-md/),
  [custom subagents](https://geminicli.com/docs/core/subagents/), and
  [Agent Skills](https://geminicli.com/docs/cli/skills/).
- [AI architecture and compatibility](../../docs/ai-architecture.md) and the
  [onboarding guide](../../docs/onboarding.md#8-copilot-and-gemini-cli).
