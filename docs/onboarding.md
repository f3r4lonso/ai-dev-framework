# Onboarding: accounts, authentication and secure setup

Every contributor uses **their own** accounts. This repository never stores credentials, and nothing
in it depends on the maintainer's logins. Security rules and leak response: [SECURITY.md](../SECURITY.md).

Checklist:

1. [Claude Code CLI](#1-claude-code-cli) signed in with your account, verified with `/status`.
2. [Codex CLI](#2-codex-cli) (optional, if you use OpenAI) signed in with your account, verified with `codex login status`.
3. [Claude Desktop](#3-claude-desktop) (optional) signed in with your account.
4. [Git identity](#4-git-identity) set to your name and a private (noreply) email.
5. [GitHub authentication](#5-github-authentication) over SSH or HTTPS with your own credentials.
6. [Secret guard](#6-enable-the-secret-guard) enabled in your clone.

You need at least one of the two CLIs. Which shared resources each one supports:
[compatibility matrix](ai-architecture.md#4-compatibility-matrix).

Statements below come from official documentation, linked in each section (checked 2026-10-17).

## 1. Claude Code CLI

Source: [Advanced setup](https://code.claude.com/docs/en/setup),
[Authentication](https://code.claude.com/docs/en/authentication),
[Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install).

Claude Code needs a **Pro, Max, Team or Enterprise** plan, or a Claude Console account; the free claude.ai plan
does not include it.

### Install

No Administrator rights needed.

| System | Command |
|---|---|
| Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` |
| Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |
| macOS, Linux, WSL (Bash) | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Alternatives | `winget install Anthropic.ClaudeCode` · `brew install --cask claude-code` · `npm install -g @anthropic-ai/claude-code` (Node.js 22+) |

On Windows, [Git for Windows](https://git-scm.com/downloads/win) is recommended (it gives Claude Code a Bash
shell). Open a **new** terminal and check `claude --version`.

### Choose an authentication method

| Method | For | How |
|---|---|---|
| Claude Pro or Max subscription | Individuals | Run `claude`; a browser opens to log in with your claude.ai account |
| Claude for Teams or Enterprise | Organizations | Log in with the claude.ai account your admin invited |
| Claude Console | API-based billing | Your admin invites you (role "Claude Code" or "Developer"); log in with Console credentials, with or without creating an API key |
| Amazon Bedrock, Google Cloud's Agent Platform (Vertex AI), Microsoft Foundry | Organizations on a cloud provider | Set the provider's environment variables before running `claude`, or pick **3rd-party platform** at the login prompt. Follow your organization's instructions |

Log out or switch account with `/logout`, then run `claude` again. If the browser does not open, press
`c` to copy the login URL. Over SSH, WSL2 or containers, paste the code shown in the browser at the
`Paste code here if prompted` prompt.

Separate work and personal accounts by giving each its own configuration directory with the
`CLAUDE_CONFIG_DIR` environment variable (for example an alias `claude-work` that sets it).

### Where credentials are stored

| OS | Location |
|---|---|
| Windows | `%USERPROFILE%\.claude\.credentials.json` (restricted to your user account by default) |
| macOS | Encrypted macOS Keychain (falls back to `~/.claude/.credentials.json` if the Keychain is locked) |
| Linux | `~/.claude/.credentials.json` (file mode `0600`) |

With `CLAUDE_CONFIG_DIR` set, the file lives under that directory instead. `~/.claude.json` holds your
sign-in session, MCP server configuration and per-project state. All of these live in your home
directory, outside this repository; never copy them into it or share them.

### Environment variables (all optional)

Only set these if your setup needs them. When several are present, Claude Code uses the first in this order:

| Variable | Use |
|---|---|
| `CLAUDE_CODE_USE_BEDROCK` / `CLAUDE_CODE_USE_VERTEX` / `CLAUDE_CODE_USE_FOUNDRY` | Use a cloud provider (plus that provider's own variables) |
| `ANTHROPIC_AUTH_TOKEN` | Bearer token for an LLM gateway or proxy |
| `ANTHROPIC_API_KEY` | Claude Console API key. Asked once for approval in interactive mode; always used with `-p` |
| `apiKeyHelper` (a setting, not a variable) | Script that returns a key, e.g. from a vault |
| `CLAUDE_CODE_OAUTH_TOKEN` | One-year token from `claude setup-token`, for CI or scripts without a browser |
| *(none)* | Subscription login from `/login` (the default for Pro, Max, Team and Enterprise) |

Keep them out of the repository:

- Set them in your user environment or shell profile, a secret manager, or CI secrets. Never in a
  committed file. This repository ignores `.env` files, but Claude Code does not read them anyway.
- A forgotten `ANTHROPIC_API_KEY` overrides your subscription and can cause
  `This organization has been disabled` errors. Remove it from your profile (PowerShell for the current
  session: `Remove-Item Env:ANTHROPIC_API_KEY`; bash/zsh: `unset ANTHROPIC_API_KEY`) and check `/status`.

### Verify

- Inside Claude Code, run `/status`: it shows the active login method, organization and email, and marks
  a credential that is present but not in use.
- Run `/doctor` inside Claude Code, or `claude doctor` from your shell if Claude Code will not start.
- Login problems: run `/logout`, close Claude Code, start `claude` and log in again.
  `API Error: 403` means the subscription is inactive or the Console role is missing.

### Load this framework's agents and skills

Start Claude Code in the repository root (`infra`, the folder you cloned) with `claude --add-dir clients`, or from an
application repository with `claude --add-dir %USERPROFILE%\workshop\infra\clients`. Discovery, permissions and limits:
[Claude Code client guide](../clients/claude-code-cli/README.md).

## 2. Codex CLI

Source: [Codex CLI](https://developers.openai.com/codex/cli), [Authentication](https://developers.openai.com/codex/auth),
[AGENTS.md](https://developers.openai.com/codex/guides/agents-md), [Skills](https://developers.openai.com/codex/skills),
[Subagents](https://developers.openai.com/codex/agent-configuration/subagents) (these redirect to learn.chatgpt.com).

### Install

| System | Command |
|---|---|
| Windows PowerShell (new window) | `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"` |
| macOS, Linux | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` |
| npm | `npm install -g @openai/codex` |
| Homebrew | `brew install --cask codex` |

The same command updates Codex (Homebrew: `brew upgrade --cask codex`). Check with `codex --version`.

### Choose an authentication method

| Method | Billing | How |
|---|---|---|
| Sign in with ChatGPT | Your ChatGPT plan; plan availability: [pricing](https://developers.openai.com/codex/pricing) | Run `codex` and pick **Sign in with ChatGPT**, or `codex login`. No browser (SSH, headless): `codex login --device-auth` |
| OpenAI API key | Usage billed to your OpenAI Platform account at API rates, not plan credits | `printenv OPENAI_API_KEY \| codex login --with-api-key` (Bash). Set the key outside the repository |

`CODEX_API_KEY` applies an API key to a single `codex exec` run. Do not set `OPENAI_API_KEY` or
`CODEX_API_KEY` in CI jobs that run repository-controlled code.

### Where credentials are stored

`cli_auth_credentials_store` in `~/.codex/config.toml` decides: `file` (`~/.codex/auth.json`, or under
`CODEX_HOME`), `keyring` (OS credential store), `auto` (keyring when available, else the file) or `ephemeral`
(memory only). Treat `auth.json` like a password: never copy it into a repository or share it. This repository
ignores `auth.json` and everything in `.codex/` except the generated `clients/.codex/agents/`.

### Verify and load this framework

1. `codex login status` shows the active method; `codex logout` signs out.
2. Once per clone, in the repository root: `python scripts/codex-adapter.py link-skills`
   (Windows creates directory junctions, no Administrator rights needed). Add `--user` to also link the
   skills into `~/.agents/skills/` so Codex sees them when started inside a project repository.
3. Start `codex` in the repository root and **trust the project** when asked; Codex loads project `.codex/`
   folders (the shared agents) only for trusted projects.
4. Check: `/skills` lists the shared skills; asking "List the instruction sources you loaded" names `AGENTS.md`;
   "Use the code-reviewer agent to review the last commit" spawns it (`/subagents` shows the thread).

Discovery rules and limits: [Codex CLI client guide](../clients/codex-cli/README.md).

### Permissions

Codex uses `sandbox_mode` and `approval_policy` (config or flags), and spawned agents inherit them. The
agents' Claude tool limits are **not** enforced by Codex; for review or audit roles start with
`codex --sandbox read-only`. `codex exec` runs read-only by default.

## 3. Claude Desktop

Source: [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop),
[Claude Code Desktop](https://code.claude.com/docs/en/desktop),
[Authentication](https://code.claude.com/docs/en/authentication).

- Install from the official download page (macOS 13+, Windows 10+, Linux Ubuntu 22.04+/Debian 12+), launch
  it and sign in with your Claude account (for example **Continue with email**, which sends a login link).
- Desktop uses OAuth with your claude.ai account. It does **not** read `ANTHROPIC_API_KEY`,
  `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` (except desktop sessions on a third-party inference configuration).
- The Code tab reads the same settings files as the CLI and your personal skills from `~/.claude/skills/`.
- Where Desktop stores its own session is not documented on these pages; treat the app's data folder as
  personal and never copy it into a repository. Sign out from the app's account menu to remove access.

## 4. Git identity

Source: [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address),
[Email addresses reference](https://docs.github.com/en/account-and-profile/reference/email-addresses-reference),
[Blocking command line pushes that expose your email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address).

Commits in a public repository publish your name and email permanently. Use your GitHub **noreply** address:

1. GitHub **Settings > Emails**: enable **Keep my email addresses private**, copy the noreply address
   shown (form `ID+USERNAME@users.noreply.github.com`), and enable
   **Block command line pushes that expose my email**.
2. Set it for every repository, or only for this clone (run inside the clone, overrides global):

```sh
git config --global user.name "Your Name or handle"
git config --global user.email "ID+USERNAME@users.noreply.github.com"
# or, for this repository only:
git config user.name "Your Name or handle"
git config user.email "ID+USERNAME@users.noreply.github.com"
```

Check with `git config user.name` and `git config user.email`.

## 5. GitHub authentication

Never share a token or private key, never paste one into a prompt, issue or file, and never put one in a
remote URL. Pick one method:

### Option A: SSH (ed25519)

Source: [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent),
[Testing your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection).

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"   # protect it with a passphrase
```

Start the agent and add the key:

- Windows PowerShell (admin, once): `Get-Service -Name ssh-agent | Set-Service -StartupType Manual`,
  then `Start-Service ssh-agent`, then `ssh-add $env:USERPROFILE\.ssh\id_ed25519`.
- Git Bash, Linux: `eval "$(ssh-agent -s)"` then `ssh-add ~/.ssh/id_ed25519`.
- macOS: `eval "$(ssh-agent -s)"` then `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`.

Add the **public** key (`id_ed25519.pub`) in GitHub **Settings > SSH and GPG keys**, then test:

```sh
ssh -T git@github.com
# Expected: Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

On first connection, compare the host fingerprint with GitHub's published fingerprints before typing `yes`.

### Option B: HTTPS (Git Credential Manager or GitHub CLI)

Source: [Caching your GitHub credentials in Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).

- **Git Credential Manager**: included with Git for Windows (stores credentials in Windows Credential
  Manager); on macOS install it with Homebrew (stores them in the Keychain). The first push opens a
  browser to sign in.
- **GitHub CLI**: `gh auth login`, choose `HTTPS`, and answer `Y` to authenticate Git with your GitHub credentials.
- Wrong account cached on Windows: remove the GitHub entry in **Control Panel > Credential Manager**.

### Optional: sign your commits with SSH

Source: [Telling Git about your signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key) (Git 2.34+).

```sh
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

Also add the public key to GitHub as a signing key so commits show as verified.

## 6. Enable the secret guard

Run once in your clone:

```sh
git config core.hooksPath .githooks
```

Every commit is then checked for secret files and credential patterns (see [SECURITY.md](../SECURITY.md)).
Installing [gitleaks](https://github.com/gitleaks/gitleaks) (v8.25+) makes the check more accurate; the hook
uses it automatically. Users of the pre-commit framework can run `pre-commit install` instead (not both).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Claude Code uses the wrong account or an API key | `/status`; remove stray `ANTHROPIC_API_KEY`; `/logout` then log in |
| `Login expired · Please run /login` | Run `/login` |
| Agents or skills from this repository not available | Run `python scripts/codex-adapter.py link-claude`, then start Claude Code with `--add-dir` pointing at `clients` |
| Codex: shared skills missing in `/skills` | Run `python scripts/codex-adapter.py link-skills` (or `--user`), restart Codex |
| Codex: shared agents not used | Trust the project; start Codex in the repository root (agents load from its `clients/.codex/agents/`) |
| Codex uses an API key instead of your ChatGPT plan | `codex login status`; `codex logout`, then `codex login` |
| `Permission denied (publickey)` | `ssh-add` your key, check it is on GitHub, retest `ssh -T git@github.com` |
| Push rejected for exposing your email | Set the noreply email (section 4) and amend the commit author |
| Commit blocked by the hook | Remove the secret; for a confirmed false positive add `gitleaks:allow` on that line |
| Hook fails with `\r` errors | Re-checkout the hook: `git checkout -- .githooks/pre-commit` (it must have LF line endings) |
