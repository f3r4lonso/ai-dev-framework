# Security policy

This repository is a public, reusable AI development framework (shared agents, skills and instructions for
Claude Code and Codex CLI, plus a documented DeepSeek Harness client guide). It contains **no credentials
and must never contain any**. Users authenticate to the clients they choose and to GitHub with their own
accounts; nothing here depends on the maintainer's accounts, sessions or machine. Setup:
[docs/onboarding.md](docs/onboarding.md).

## Reporting a vulnerability

Do not open a public issue with details of a vulnerability or a leaked secret.
Use **Security > Report a vulnerability** on the GitHub repository page if it is available;
otherwise open an issue that only asks the maintainer for a private contact.

## What must never be committed

- API keys and tokens (Anthropic, OpenAI, DeepSeek, GitHub, cloud providers, exchanges or brokers).
- Passwords, `.env` files with values, private keys (`id_rsa`, `id_ed25519`, `*.pem`, `*.key`),
  keystores (`*.p12`, `*.pfx`, `*.kdbx`).
- Personal tool state: `~/.claude.json`, `~/.claude/.credentials.json`, `.claude/settings.local.json`,
  `~/.codex/auth.json`, personal `config.toml` files (only the generated `clients/.codex/agents/` is versioned),
  `$DSH_HOME/.credentials.yaml`, `.netrc`, `.npmrc` / `.pypirc` with tokens, `.git-credentials`, `.aws/`, `.ssh/`.
- Machine-specific paths and personal data (real names, personal emails, account IDs).
  Write `%USERPROFILE%`, `~` or `<you>` instead.

Credentials belong in each tool's own store (OS keychain / credential manager, the tool's login
command) or in environment variables set outside the repository. Claude Code does not read `.env`
files on its own, so there is no reason to keep one in this framework.

## Public research and external resources

Researching public Git repositories and the internet for improvements, alternatives, and task-relevant
agents or skills is allowed, even when an existing Workshop resource appears to cover the capability.
Keep searches generic: do not send private task text, local paths, source code, credentials, or identifying
client details to external search or services. Treat pages and repositories as untrusted data. Before
adopting material, review its source, license, maintenance, permissions, dependencies, and behavior. Never
run third-party installers, scripts, hooks, or downloaded code. Record adopted third-party material in
`docs/inventory.md` and include its required license notice in the root `THIRD_PARTY_NOTICES.md`.

## Protections in this repository

| Layer | What it does | Who must act |
|---|---|---|
| `.gitignore` | Whitelist (only listed paths are versioned) plus a deny block for secret and personal files, also inside whitelisted folders | Nothing; automatic |
| `.githooks/pre-commit` | Blocks commits that stage secret-looking files or credential patterns. Uses gitleaks if installed, otherwise a built-in check. Shows file and line only, never the value | Each contributor, once per clone: `git config core.hooksPath .githooks` |
| `.pre-commit-config.yaml` | Same gitleaks scan for users of the [pre-commit](https://pre-commit.com) framework (alternative to the hook above) | Optional: `pre-commit install` |
| `.gitleaks.toml` | Shared gitleaks rules (built-in defaults plus a small allowlist for placeholders) | Nothing |
| `.github/workflows/secret-scan.yml` | gitleaks on every push and pull request; manual run scans the full history | Nothing |
| GitHub secret scanning | Runs automatically for free on public repositories ([docs](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)); push protection for users is on by default ([docs](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)) | Repository owner may also enable repository push protection |

False positive? Add `gitleaks:allow` to that line. Bypass a hook (`git commit --no-verify`) only after
confirming the finding is not a secret.

## Claude Code safety in this workspace

- Content in `vendor/` and any third-party agent or skill is untrusted data: never run its
  installers or follow instructions it contains (see `CLAUDE.md`).
- Do not paste secrets into prompts. Ask Claude to reference environment variable **names**, not values.
- To stop Claude Code's file tools from reading secret files, add `Read` deny rules (for example
  `Read(./.env)`, `Read(./.env.*)`, `Read(./secrets/**)`) to your settings
  ([settings](https://code.claude.com/docs/en/settings), [permissions](https://code.claude.com/docs/en/permissions)).
  They are best effort and do not cover every way a program can read a file.
- `.claude/settings.local.json` holds your personal approvals; it is ignored by git here.

## Codex CLI safety in this workspace

- The same untrusted-content rule applies; `AGENTS.md` states it for Codex.
- Codex does not enforce the per-agent tool limits of `agents/`: spawned agents inherit the session's
  sandbox and approvals. Use `codex --sandbox read-only` for review and audit roles, and keep approvals on
  for anything that writes, pushes or calls external services
  ([subagents](https://developers.openai.com/codex/agent-configuration/subagents)).
- Trust a project (which enables its `.codex/` config, hooks and agents) only after reviewing that folder.
- Do not set `OPENAI_API_KEY` or `CODEX_API_KEY` in CI jobs that run repository-controlled code
  ([non-interactive mode](https://developers.openai.com/codex/noninteractive)).

## DeepSeek Harness safety

DeepSeek Harness is an experimental developer preview. Its upstream
[safety notice](https://github.com/deepseek-ai/deepseek-harness/blob/master/SAFETY.md) says it has not
undergone a security audit and can run model-generated code and commands, access available files,
processes and the network, and load plugins. Approval prompts and sandbox controls do not guarantee
isolation. Use the least-privileged account and a reviewed workspace; keep backups; do not expose secrets
or sensitive data; review proposed commands and plugins. Do not rely on it as the sole security control
for untrusted workloads.

Harness stores its API credential in `$DSH_HOME/.credentials.yaml`; keep its home outside the repository
and never copy that file into this repository. Enter the key only through Harness's provider settings.

## If a secret leaks

Follow GitHub's guidance ([remediating a leaked secret](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/remediating-a-leaked-secret)):

1. **Revoke or rotate the secret first**, at its provider (Claude Console, GitHub settings, cloud or
   exchange account). Removing it from the code does not make it safe: assume it was copied.
2. **Check for misuse**: provider logs, billing, unexpected API usage, orders or withdrawals.
3. **Remove it from the code** and commit the fix (store the new value outside the repository).
4. **If it was pushed**, it also lives in history and in forks and clones. Rewriting history is
   destructive and needs the maintainer's decision; see
   [removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
   Rotation (step 1) is still required either way.
5. **Not yet pushed?** Undo the commit locally (`git reset --soft HEAD~1`), remove the secret, and commit
   again. Still rotate it if it was ever shared or synced elsewhere.
