# Workshop AI v2: AI engines

Status: **approved** (2026-10-20, with decisions D-V2-01…09). Facts come from a read-only audit the same day: version checks on this laptop
plus the client guides in [`infra/clients/`](../../clients/). Facts not checked locally are marked *unverified*.

## 1. Capability levels

The app shows every engine, always, at the highest level that is **verified** for it. A level is unlocked only by
the evidence in the last column of §2; until then the card says what is missing.

| Level | Name in the UI | What the owner can do |
|---|---|---|
| 0 | Enlace | Open the engine's own website or app, copy a prepared text (brief, agent instructions) |
| 1 | Consola | Open the engine in a new terminal in the right folder, empty or with a task brief as the first message |
| 2 | Conversar | Chat from the app; the engine answers text only and has **no tools** (cannot read or change files) |
| 3 | Tarea de lectura | Run a task with read-only tools in the project folder; result and usage shown in the app |
| 4 | Tarea con cambios | Run a task that edits files in an **isolated copy**; the owner reviews the diff and approves before anything reaches the real folder |

## 2. Engine registry

| Engine | Kind | Installed (2026-10-20) | Current level | Target in v2 | How agents/skills reach it | Headless interface | Unlocks the next level |
|---|---|---|---|---|---|---|---|
| Claude Code | Coding agent CLI | Yes, 2.1.304 | 2 (tool-free dispatch built in the UI server) | 4 | `workshop` plugin, in place | `claude -p --output-format json` (built); `stream-json` documented, *unverified here* | Level 3: run with a read-only tool allowlist in the project folder, tested; level 4: isolated copy + diff approval (V6) |
| Codex CLI | Coding agent CLI | Yes, 0.163.0 | 1 | 2 (3 only after [architecture §8](architecture.md#8-required-design-changes-from-the-security-review-2026-10-20) C1 and H1 are met) | generated `clients/.codex/agents/*.toml` in a trusted project; `link-skills` | `codex exec --json` (JSONL), `--sandbox read-only` | Codex guide §5 manual checks pass; R7 terms check; then level 2–3 with `--sandbox read-only`. Per-agent tool limits are **not enforced** by Codex |
| Gemini CLI | Coding agent CLI | Yes, 0.64.0 | 1 | 2 (3 only after §8 H1 and L3 are met) | `GEMINI.md`; personal agents in the user's Gemini folder; skills via `link-skills --user` | `gemini -p --output-format json|stream-json`, `--approval-mode plan` | Local headless test in `plan` mode; R7 check; sign-in route check (Google moved some free users to another CLI on 2026-06-18, *unverified locally*) |
| GitHub Copilot CLI | Coding agent CLI | Yes, 1.0.100 | 1 | 2 | `AGENTS.md`; personal agents in the user's Copilot folder; shared skills folder | `copilot -p -s --no-ask-user --output-format=json` | Owner sign-in; local test with an empty `--available-tools`; never `--allow-all` / `--yolo` |
| DeepSeek Harness (`dsh`) | Experimental coding agent with its own local web UI | Yes, 0.2.1-rc.2 | 0–1 | 1 | Not integrated; may read `AGENTS.md` (*unverified*) | Headless flag *unverified* | Stays at Consola / link to its local page: unaudited, its approvals are not isolation |
| Ollama | Local model runtime | **No** | — | 2 | Does not load agents/skills; the app sends the agent's instructions as text | HTTP on loopback port 11434 (`/api/chat`, streams) | Task `ollama-install` (D-V2-09); then level 2 for private text work. Never for trading decisions |
| Suno | Music service operated by the owner | n/a | 0 | 0 | none | none; automation forbidden | — (stays a link plus help writing a brief with `music-composer`) |
| claude.ai Projects | Web app | n/a | 0 | 0 | personal agents pasted by hand | none | — (copy the personal agent's text) |
| Claude Desktop | Desktop app | *unverified* | — | 0 | reads the CLI settings and user skills (onboarding §3) | none | Detect install; add a client guide |
| AbletonMCP | MCP integration for Ableton Live | No (not cloned) | — | 0 | none | MCP stdio, *unverified* | Repository review and license check (its project page) |

The **Automático** engine choice picks the first engine, in the owner's preference order, that is at the level the
action needs and reports itself ready. It always shows which engine it picked, and if that engine fails it
**suggests** another one ("Claude no tiene cuota, ¿probar con Codex?"); it never switches by itself.

## 3. Rules for every engine

- Credentials are never read, stored or shown by the app. Sign-in happens in the engine's own console or site; the
  card says "Sesión: desconocida" until a harmless check proves otherwise. Environment variable names may be shown
  in help text; values never.
- Request content goes through stdin or the loopback API body, never on a command line.
- Each run has a timeout, an input and output size cap and a stop button; one run per engine at a time in v2.
- Output from an engine is untrusted text: rendered escaped, labelled when passed to another stage, never executed.
- A stray `ANTHROPIC_API_KEY` overrides a Claude subscription: the Claude card warns when the variable is set
  (presence only, not value).
- Level 3 and 4 also follow the binding requirements in [architecture.md §8](architecture.md#8-required-design-changes-from-the-security-review-2026-10-20) (neutralised flag sets, filtered copies, no `.git` in edit copies).
- Ollama must stay on loopback; cloud models and Ollama sign-in are forbidden.
- Adding an engine follows the contributor guide §5 (client guide, onboarding section, matrix column) **and** adds a
  row here and an adapter entry ([architecture.md §6](architecture.md#6-engine-adapters)).

## 4. Inconsistencies found (to fix in V0)

1. `wai` knows `claude, codex`; the UI knows `claude, codex, gemini, copilot`; neither knows `dsh` or Ollama. v2 uses
   one registry file read by both ([architecture.md §6](architecture.md#6-engine-adapters)).
2. ai-architecture §9 says clients start only interactively, while the UI already runs `claude -p` (resolved by D-V2-05).
3. The client-list contract treats any `clients/<folder>` with a README as a client, which wrongly includes `suno`
   and leaves out `personal`.
4. The compatibility matrix (ai-architecture §4) has no Copilot or Gemini columns.
5. `inventory.md` lists three clients and still describes `--add-dir clients`; `wai` `clients.py` still passes it.
6. The reading-assistant docs say "Gemini via REST", but the code translates with local Ollama, which is not
   installed, so translation does not work today.
7. Agent and skill counts disagree across ai-architecture, inventory and the Claude/Codex guides.
8. Ollama, Claude Desktop and claude.ai Projects have no client guide or inventory row.
