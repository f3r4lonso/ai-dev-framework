# Client guide: DeepSeek Harness

How DeepSeek Harness uses a project workspace. Install, API-key setup and credential storage are in
[onboarding §4](../../docs/onboarding.md#4-deepseek-harness).

**Status:** Installed locally as `@deepseek-ai/dsh` 0.2.1-rc.2 on 2026-10-19; `dsh --version` passed.
This is an experimental developer preview with breaking changes. The upstream project says it has not
undergone a security audit. Source and safety notice:
[GitHub](https://github.com/deepseek-ai/deepseek-harness),
[SAFETY.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/SAFETY.md).

## 1. Start a local session

Open PowerShell in the project repository you intend to work on, then run:

```powershell
Set-Location "C:\path\to\project"
dsh web
```

The default Web UI listens on `http://127.0.0.1:3080` and opens the browser. Add and select the project
workspace in the UI before starting a session. The current directory is the default workspace location.
Keep the service on loopback; do not expose it through a reverse proxy or public network.

## 2. Configure DeepSeek

1. Create an API key in your own [DeepSeek Platform account](https://platform.deepseek.com/api_keys).
2. In the Harness UI, open **Settings → Models**, enter the key in the DeepSeek card, and save.
3. Select a model in the model picker.

The key is write-only in the UI and is stored by Harness in `$DSH_HOME/.credentials.yaml`; never put it
in a project, this repository, a prompt, or a command. API requests are usage-billed by DeepSeek.

## 3. Workshop resources and instructions

The default instruction loader searches for `AGENTS.md` and `CLAUDE.md` in the workspace ancestry, plus
`AGENTS.local.md` and `CLAUDE.local.md` overlays. This behavior is documented in the upstream
[agent-instructions configuration](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/src/config.ts);
loading and precedence have not been verified locally.

The Harness does not use the Workshop Claude plugin or generated Codex adapters. Shared Workshop agents
and skills are not integrated or verified; open their canonical files by path if needed. Claude-specific
`@AGENTS.md` import processing is not verified.

## 4. Safety and limits

- Harness can run model-generated commands and code, modify workspace files, use network and processes,
  and load plugins. Approval prompts and sandbox controls are not guaranteed isolation.
- Use it only in a reviewed workspace, with the least access required. Keep backups and do not expose
  secrets or sensitive trading data. Review every command or plugin before allowing it.
- Do not use it as the sole control for untrusted workloads or in a production environment.
- The CLI can start other profiles, including headless mode; this Workshop guide supports only the
  local interactive Web UI workflow.

See the upstream [quickstart](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart)
and [model configuration guide](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers).
