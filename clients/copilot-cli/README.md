# Client guide: GitHub Copilot CLI

This guide covers GitHub Copilot CLI alongside the Workshop. Copilot CLI is a coding agent that can read and modify
files and run commands; it is not a read-only assistant by default.

**Status:** GitHub's current setup, custom-agent, instruction, and skill documentation was checked on 2026-10-20.
The Workshop's personal-agent and shared-skill adapters are documented here but have not been validated in a live
Copilot CLI session.

## 1. Install and sign in

Use the current steps in [onboarding](../../docs/onboarding.md#8-copilot-and-gemini-cli). GitHub currently documents
WinGet and npm installation on Windows. Copilot CLI requires an active Copilot subscription; an organization may
disable CLI access. Follow GitHub's current [installation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli)
and authenticate with `/login`.

Start Copilot in the narrowest trusted project directory. The Workshop root is not a Git repository; `infra/` and
each application are separate repositories. Review GitHub's trust prompt before continuing. Copilot may read,
modify, and execute files under the trusted directory, and asks for approval when using tools that can modify or
execute files.

## 2. Workshop instructions and resources

Copilot CLI documents discovery of `AGENTS.md`, `GEMINI.md`, and other supported instruction files in the current
repository path. Starting in `infra/` makes `infra/AGENTS.md` available. The workspace-level `WORKSHOP-CONTEXT.md`
is above that repository and is not guaranteed to load; open it explicitly when working across the Workshop.
Use `/instructions` to inspect the instruction files discovered in the current session.

Workshop agents and skills have distinct setup paths:

- **Personal assistants:** From the `infra/` repository root, run:

  ```powershell
  python scripts/codex-adapter.py personal
  python scripts/codex-adapter.py install-personal
  ```

  This generates the Copilot profiles from canonical files in `agents/personal-assistants/` and copies them to
  `%USERPROFILE%\.copilot\agents`. The installer does not overwrite existing files that are not marked as
  Workshop-generated. Start a new session and use `/agent` or name an assistant in your prompt.
- **Shared skills:** To expose Workshop skills as personal Agent Skills across supported clients, run
  `python scripts/codex-adapter.py link-skills --user` from `infra/`. It creates links under
  `%USERPROFILE%\.agents\skills`; existing files and links are left untouched. Copilot supports personal skills
  in this location. Use `/skills` to inspect them and `/skills reload` after a change.
- **Tasks, catalogues, and manuals:** These are plain files, not auto-loaded resources. Find them through the
  [Workshop index](../../../INDEX.md) and open the relevant files explicitly.

Generated profiles and links point back to canonical Workshop resources; do not edit generated adapters by hand.

## 3. Safety and limitations

- Keep Copilot's tool approval prompts enabled. Avoid blanket automatic approval such as `--allow-all-tools`;
  approving a tool for a session can permit it to run commands or change files without another prompt.
- Review proposed commands and changes before approving them. Do not start the client in the Workshop root or
  another directory containing unrelated or sensitive files.
- Never expose credentials in prompts or repository files. Follow [`infra/SECURITY.md`](../../SECURITY.md).
- A generated personal assistant's written read-only instructions are not a security boundary. Use restrictive
  client permissions and review actions.
- The instructions and skills described above are documented integration paths; their discovery and behavior have
  not been tested locally for this Workshop.

## 4. Sources and evidence

- [Copilot CLI overview](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli).
- [Install Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli).
- [Using Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview), including
  instructions, custom agents, and permission prompts.
- [Adding custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
  and [adding Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).
- [AI architecture and compatibility](../../docs/ai-architecture.md) and the
  [onboarding guide](../../docs/onboarding.md#8-copilot-and-gemini-cli).
