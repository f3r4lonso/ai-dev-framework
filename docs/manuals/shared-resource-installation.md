# Shared agent and skill installation

Owner's standing instruction, 2026-10-21: every new or updated agent/skill must be available to
all clients. Ease of use takes priority over avoiding duplicate files. Keep one maintained
source and generate the copies and native adapters clients need. A Claude-only installation
is not the default. This instruction applies to resources obtained from any source.

## The standard workflow

1. Review the resource, license, dependencies, tool access and client-specific behavior.
2. Adopt it under `infra/agents/<area>/` or `infra/skills/<name>/`. Preserve required notices.
3. Adapt tool names, paths, model aliases, delegation, scripts and permissions for each client.
   A copied Markdown file cannot create tools the host lacks. Preserve the role's restrictions.
4. Update inventory/catalogues, run legacy adapter generation/checks if definitions changed,
   then synchronize copies and verify the same scope. Never edit generated files by hand.
5. Report where it is installed, how to invoke it, and which clients were actually tested.
   For a client without native support, provide the canonical file as an explicit manual-use
   path. Do not claim unsupported subagents, isolation or scripts work.

## One installation command

From the Workshop root, to install for the current OS user across project folders:

```powershell
python infra/scripts/sync-resources.py --user
python infra/scripts/sync-resources.py --user --check
```

The current restricted assistant session cannot write user-wide client folders. The owner can
run these commands from normal PowerShell. The command never reads client configuration or
credentials, changes permissions, signs in, or launches an AI client.

For Workshop root and infra only, omit `--user`. For a particular application's repository:

```powershell
python infra/scripts/sync-resources.py --project applications/<app>
python infra/scripts/sync-resources.py --project applications/<app> --check
```

Use `--dry-run` to inspect the plan. Project roots are explicit; this never scans or installs
into application repositories automatically. Restart/reload the chosen client and verify its
resource list. User-wide scope reaches projects where a local copy may override it; synchronize
or retire known older project copies deliberately. No commit or push is part of installation.

If installation stops on existing customized agent profiles, preserve those versions while
installing the remaining resources with `python infra/scripts/sync-resources.py --user --keep-existing-agents`
from the Workshop root. This option applies only to native agent files, never skill assets,
linked destinations or retirement conflicts. Preserved profiles are listed explicitly and
recorded separately in the manifest; they are not claimed as synchronized or managed copies.
Use the same option for subsequent `--check` calls while keeping those exceptions.

## Client coverage

| Client | Installed format | Invocation / limitation |
|---|---|---|
| Claude Code | `.claude/skills/<name>/`, `.claude/agents/<name>.md` | `/skill-name`, named agent; existing Workshop plugin also reads canonical resources |
| Codex | `.agents/skills/<name>/`, `.codex/agents/<name>.toml` | `$skill-name`, ask for the named agent; project trust applies |
| Copilot CLI | `.agents/skills/`, `.github/agents/*.agent.md` in projects; `.copilot/agents/` for user scope | Ask for skill; `/agent` or named agent; native tool mappings preserve intended scope |
| Gemini CLI | `.agents/skills/`, `.gemini/agents/*.md` | Activate skill, `@agent-name`; actual available tools and settings govern execution |
| DeepSeek Harness | Explicit canonical files via [skills](../catalogues/skills.md) and [agents](../catalogues/agents.md) | Ask it to read/follow the named file; native discovery and delegation unverified |
| Web/desktop chats without repository access | Manually attach/paste the canonical skill/agent and needed references/assets | No filesystem installation is claimed; local scripts and subagents may be unavailable |
| Ollama, Suno, other model/media services | No native agent/skill installation mechanism established | They are providers/services, not equivalent coding clients; use a compatible host or manual instructions where supported |

Shared and personal agent bodies are embedded in installed native profiles. Claude tool names
are mapped using the existing adapter. Model names are not copied across providers. Tool lists
and written restrictions are not a sandbox; the host's real permissions apply. A missing
delegation capability must be reported instead of silently simulated.

## Ownership and verification

Each installation root gets `.workshop/resources.json` with owned paths and SHA-256 values.
Identical existing files can be adopted; other unowned files and modified generated files cause
a visible conflict before writes. Resolve these deliberately; there is no force/overwrite flag.
Exact previous personal-agent output from the old adapter can also be migrated after a full
content comparison; a generated-looking header alone is never enough to overwrite a file.
All roots are preflighted. Symlink/junction destinations are rejected. Only unchanged,
manifest-owned retired files are removed individually; unrelated files are preserved.

The old `codex-adapter.py` continues to own its generated files under `clients/`; the new sync
command owns copies in native discovery folders. The two generators do not own the same paths.
Legacy links are not silently replaced.

## Migration status

33 canonical skills and 29 canonical agents (26 shared, 3 personal). Arena and i-have-adhd
moved from local-only copies into the canonical library. Copies for the four native CLI clients
are installed inside `infra/` and at user scope. After the owner ran the installer in PowerShell,
`--user --keep-existing-agents --check` passed: 504 resource paths checked, zero pending writes
or retired copies, with the existing Atlas profiles explicitly preserved in Codex, Copilot and
Gemini. Those three profiles remain owner-managed exceptions. Arena and the shared skills now
appear in this Codex session's available-skill catalogue. Workshop-root local copies have not
been fully synchronized; older local copies can override user-wide ones. Other clients' live
discovery and a live Arena tournament are not tested. Arena uses instruction-only bookkeeping,
so adoption does not bypass the existing ban on executing downloaded scripts.

Verified locally on 2026-10-21: 12 ownership/containment tests ran (11 passed, symlink creation test skipped
because Windows denied creating the test link); repeat synchronization and `--check` pass with
zero drift. All 29 profiles in each of four native formats and both skill discovery copies
were checked, including asset equality via the manifest. Legacy adapter drift checks pass. V2's shared header
parser correction regenerated one legacy adapter and four existing native profiles; the 504 resource files
inside infra pass synchronization checks with zero drift.
The native-format generator requires Python 3.11+ for standard-library TOML validation.

Official format references checked 2026-10-21: [Codex skills](https://learn.chatgpt.com/docs/build-skills),
[Codex agents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[Copilot agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli),
[Gemini skills](https://geminicli.com/docs/cli/skills/),
[Gemini agents](https://geminicli.com/docs/core/subagents/).
