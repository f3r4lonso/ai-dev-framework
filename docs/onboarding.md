# Onboarding: accounts, authentication and secure setup

Every contributor uses **their own** accounts. This repository never stores credentials, and nothing
in it depends on the maintainer's logins. Security rules and leak response: [SECURITY.md](../SECURITY.md).

Checklist:

1. [Claude Code CLI](#1-claude-code-cli) signed in with your account, verified with `/status`.
2. [Claude Desktop](#2-claude-desktop) (optional) signed in with your account.
3. [Git identity](#3-git-identity) set to your name and a private (noreply) email.
4. [GitHub authentication](#4-github-authentication) over SSH or HTTPS with your own credentials.
5. [Secret guard](#5-enable-the-secret-guard) enabled in your clone.

Statements below come from official documentation, linked in each section (checked 2026-10-17).

## 1. Claude Code CLI

Source: [Authentication](https://code.claude.com/docs/en/authentication),
[Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install).

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

Start Claude Code in the workspace root (the folder you cloned this repository into), or from an
application repository with `claude --add-dir <workspace root>`.

## 2. Claude Desktop

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

## 3. Git identity

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

## 4. GitHub authentication

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

## 5. Enable the secret guard

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
| Agents or skills from this repository not available | Start Claude Code in the workspace root or use `--add-dir` |
| `Permission denied (publickey)` | `ssh-add` your key, check it is on GitHub, retest `ssh -T git@github.com` |
| Push rejected for exposing your email | Set the noreply email (section 3) and amend the commit author |
| Commit blocked by the hook | Remove the secret; for a confirmed false positive add `gitleaks:allow` on that line |
| Hook fails with `\r` errors | Re-checkout the hook: `git checkout -- .githooks/pre-commit` (it must have LF line endings) |
