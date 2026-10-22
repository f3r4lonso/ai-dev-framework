# Client guide: OpenAI Codex CLI

**Shared installation standard (2026-10-21):** [all-client installation](../../docs/manuals/shared-resource-installation.md) supersedes older link-only/personal-only setup below. Run `python scripts/sync-resources.py --user` from `infra/` for user-wide copies, or `--project <root>` for one project. Shared and personal agents are included. DeepSeek remains an explicit canonical-file/manual-use path; native discovery and delegation are unverified. No client setting or credential is changed.

How Codex CLI finds and uses this workspace's shared resources. Install, sign-in and credential storage are in
one place only: [onboarding §2](../../docs/onboarding.md#2-codex-cli).

**Status: not verified locally.** Codex CLI 0.163.0 is installed on the maintainer's machine (Observed 2026-10-17); the section 5 checks have not
been run yet.
Everything below is **Documented** (official docs checked 2026-10-17, e.g.
[skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS.md](https://developers.openai.com/codex/guides/agents-md),
[subagents](https://developers.openai.com/codex/agent-configuration/subagents)) or statically checked, never
**Observed**. The first contributor who runs section 5 should record the result in
[ai-architecture.md §10](../../docs/ai-architecture.md#10-validation-status-2026-10-17).

## 1. From a fresh clone to a working session

1. Install Codex and sign in with **your own** account: [onboarding §2](../../docs/onboarding.md#2-codex-cli).
   - **ChatGPT plan vs API key:** "Sign in with ChatGPT" uses your plan; an OpenAI API key bills usage at API
     rates, not plan credits.
   - **Check the active account:** `codex login status` (method in use); `codex logout` to switch.
2. Enable the secret guard once: `git config core.hooksPath .githooks`.
3. Expose the shared skills once per clone, in the repository root (Python 3 on PATH):
   - Windows PowerShell: `python scripts/codex-adapter.py link-skills`
   - Bash (macOS, Linux, Git Bash): `python3 scripts/codex-adapter.py link-skills`
   - Add `--user` to also link them into `~/.agents/skills/` for Codex sessions started in a project repo.
4. Start Codex in `clients/` (where the generated `.codex/agents/` and `.agents/skills/` live) and **trust the
   project** when asked (section 2), then verify (section 5). Unverified after the 2026-10-17 move to `clients/`.

## 2. Start-up directory

| Where you work | What loads (Documented) |
|---|---|
| Repository root, trusted | `AGENTS.md`, skills in `clients/.agents/skills/`, the shared agents in `clients/.codex/agents/` (26 wrappers on 2026-10-20) |
| Repository root, not trusted | `AGENTS.md` and skills; **no** project `.codex/` config, so no shared agents |
| An application repo | that repo's own `AGENTS.md` only (Codex stops at its git root); shared skills only if linked with `--user`; shared agents **not** available |

Trading-app has no `AGENTS.md` of its own, so Codex started there gets none of the workspace rules (Inference
from the documented discovery rule; Unverified).

## 3. Discovery

| Resource | Where Codex looks | How it gets there | Status |
|---|---|---|---|
| Rules | `AGENTS.md` from the git root down to the working directory; `~/.codex/AGENTS.md` | the root `AGENTS.md` itself | Documented |
| Skills | `.agents/skills/` in every folder from the working directory up to the repo root; `~/.agents/skills/` | local links to `skills/<name>` made by `link-skills` (not versioned) | Documented; Windows **junctions** are not mentioned in the docs (symlinks are) → Unverified |
| Agents | `.codex/agents/*.toml` in a trusted project | generated wrappers pointing at `agents/<area>/<name>.md` (`codex-adapter.py agents`, CI drift check) | format Documented; wrappers parse as TOML (Observed); loading Unverified |
| Task prompts, catalogues, manuals | not discovered; open by path from [the Workshop](../../tasks/README.md) | — | n/a |
| Hooks, MCP | none shipped by this repo | — | — |

## 4. Invoking shared resources

- **Skill:** `/skills` to list, `$skill-name` to call, or automatic by description.
- **Agent:** ask "Use the `<name>` agent to …"; `/subagents` shows and switches agent threads.
- **Task prompt:** "Run the task in `tasks/projects/<project>/<file>.md`" or
  "`tasks/common/<category>/<file>.md`".
- **Non-interactive:** `codex exec "<prompt>"` (read-only sandbox by default; `--json` for events).

## 5. Verify (manual; required before claiming support)

1. `codex login status` shows your own account and method.
2. `/skills` lists the 23 shared skills (if not, check that `clients/.agents/skills/` links exist and restart; if junctions
   are ignored, replace them with directory symlinks: `mklink /D` needs Developer Mode or Administrator).
3. Ask "List the instruction sources you loaded": it names `AGENTS.md`.
4. Ask "Use the code-reviewer agent to review the last commit": `/subagents` shows the thread.
5. Record each result (pass / fail, date, Codex version) in ai-architecture.md §10.

## 6. Permissions

- Codex uses `sandbox_mode` and `approval_policy` (config or flags); spawned agents inherit them.
- The agents' Claude tool limits are **not enforced** by Codex (Documented). Read-only roles state the limit in
  their instructions; start review and audit work with `codex --sandbox read-only`.
- Trust a project (enables its `.codex/` config and agents) only after reviewing that folder
  ([SECURITY.md](../../SECURITY.md#codex-cli-safety-in-this-workspace)).

## 7. Limitations

- No per-agent tool limits, no per-agent model (agents inherit the session model), no `@agent-` mentions.
- `${CLAUDE_SKILL_DIR}` is not expanded; `ui-ux-pro-max` tells the model to substitute the skill folder.
- Trading agents use the Claude `PowerShell` tool name and assume the Trading-app root; their wrappers only load
  in this repo, so they are not usable from Codex inside Trading-app (Inference; Unverified).
- Links made by `link-skills` hold absolute local paths; rerun it after moving the clone.

## 8. Troubleshooting

[Onboarding troubleshooting](../../docs/onboarding.md#troubleshooting): skills missing → rerun `link-skills`
and restart; agents missing → trust the project and start in the repository root; wrong account →
`codex logout`, then `codex login`.
