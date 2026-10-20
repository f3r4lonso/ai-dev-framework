# Token-optimization candidate repositories — safety and fit review

Checked 2026-10-18 by reading the source of a shallow clone of each default branch (commit below) and the GitHub
API metadata. **Nothing was installed, built or run.** Labels: **Verified** (read in source at that commit),
**Inferred** (from naming, comments or docs, not traced end to end), **Requires verification** (not checked).
Used by [workshop-ai-token-optimization-integration](../tasks/projects/workshop-ai/workshop-ai-token-optimization-integration.md).

Workshop AI constraints applied (vision §17): Python standard library only for the `wai` core (§17.8; since
2026-10-18 the VS Code extension is TypeScript with no runtime npm dependencies, which these packages would also
break); state as Markdown or JSON files in
the project repository (§17.4); no scripted client runs before the §17.2 hard gate; user-level client configuration
(`~/.claude`, `~/.claude.json`, `~/.codex`) is not changed by the product.

## 1. Summary

| Repository | Commit | License | Stack | Last push | Safety verdict | Decision |
|---|---|---|---|---|---|---|
| [Open330/context-compress](https://github.com/Open330/context-compress) | `59fae35a7b38` | MIT | TypeScript, Node ≥ 22, native `better-sqlite3` | 2026-09-12 | High risk: runs code and fetches URLs by design; global hook | **Reject** as a dependency; reuse ideas only |
| [anvanster/compressor](https://github.com/anvanster/compressor) | `8d4213a791ae` | MIT | TypeScript, Node ≥ 20, Anthropic SDK | 2026-09-17 | Medium–high risk: rewrites client config and instruction files; very young | **Reject** as a dependency; reuse benchmark method |
| [MarceloCaporale/codex-agent-mem](https://github.com/MarceloCaporale/codex-agent-mem) | `d594c8a86207` | Apache-2.0 (+ NOTICE) | Python ≥ 3.12, FastAPI/uvicorn/pydantic/jinja2, SQLite FTS5 | 2026-05-07 | Lowest risk: loopback-only, no external calls found | **Reference design**; do not install (non-stdlib deps, SQLite storage, stalled) |
| [dan-calin/shared-agent-memory](https://github.com/dan-calin/shared-agent-memory) | `29e96c663a43` | MIT | JavaScript, Node ≥ 18, no declared deps | 2026-08-03 | High risk: downloads unpinned code at every start; global config and hooks | **Reject** as a dependency; reuse claim-board and secret-scan ideas |

**Recommendation:** adopt none of the four. Build a minimal native Python standard-library implementation and use
these repositories as design references, with attribution for any adapted idea under its license.

## 2. Findings per repository

### 2.1 context-compress

- **Verified:** the MCP server executes code by design. `SECURITY.md` states the model is a trusted operator, and
  `src/runtime/languages/` has runners for 11 languages (shell, Python, JS/TS, Go, Rust, Ruby, PHP, Perl, R, Elixir).
- **Verified:** it fetches web content (`src/util/fetch-code.ts`), with SSRF protection (`src/network.ts` blocks
  private IP ranges, pins DNS, blocks redirects).
- **Verified:** optional "auto" mode sends the command line plus a 500-byte output sample, after secret scrubbing,
  to `https://api.anthropic.com/v1/messages` with `ANTHROPIC_API_KEY` (`src/util/auto-mode.ts`). That is metered API
  use and sends project data off the machine.
- **Verified:** `setup` / `doctor` / `uninstall` and `src/hooks/pretooluse.ts` read or write Claude and Codex
  configuration; ships Claude and Codex plugin manifests and a PreToolUse hook that intercepts tool calls.
- **Verified:** native module `better-sqlite3` (compiled at install). Benchmark scripts exist; their claimed savings
  are **Requires verification**.
- **Worth reusing (idea only):** deterministic output filters, truncation with explicit markers, stored originals
  retrievable on demand.

### 2.2 compressor

- **Verified:** 1 star, created 2026-06-11, version 0.6.0 — little outside review.
- **Verified:** recommended installer is `irm <raw GitHub URL> | iex`; `install.ps1` downloads a zip of `main`, runs
  `npm install` and `npm run build`, then installs globally. `prepare` runs the build on any git install.
- **Verified:** adapters edit Claude Code settings and `CLAUDE.md` / `AGENTS.md` (marker blocks with backup and
  `restore`); `src/claude/transcripts.ts` reads Claude Code session transcripts under the config folder's `projects/`.
- **Verified:** `--exact` token counts call the Anthropic `countTokens` API with `ANTHROPIC_API_KEY`
  (`src/tokens/exact.ts`); estimated counts use `js-tiktoken` locally.
- **Worth reusing (idea only):** "every optimization is measured or it doesn't ship"; ablation-style benchmark
  (`src/bench/ablate.ts`); tiered compression by content type (logs, JSON, code).

### 2.3 codex-agent-mem

- **Verified:** network use is local: the daemon only accepts a loopback bind address (`mcp_daemon.py`), and the
  notify/stdio clients call a local API base (default `http://127.0.0.1:37770`). No other external URL found in `src/`.
- **Verified:** runtime dependencies FastAPI, uvicorn, pydantic, jinja2; storage SQLite with FTS5 (`schema.sql`);
  CI and CodeQL workflows present; read-only mode documented.
- **Inferred:** `bootstrap_codex.py` prints a `notify` block to paste into `~/.codex/config.toml` rather than
  writing it. **Requires verification** before any use.
- **Verified:** no push since 2026-05-07 (about 5 months). Claimed client compatibility beyond Codex is
  **Requires verification**.
- **Worth reusing (idea only):** project identity and scoping, compact "context packs", retrieval hygiene, schemas
  for observations. FTS5 search would need §17.4 reopened at a gate; JSON files are the default.

### 2.4 shared-agent-memory

- **Verified:** no declared dependencies, but `lib/memory-proxy.js` starts `npx -y @modelcontextprotocol/server-memory`
  (unpinned, latest from npm on each start), and the coordination hook may run `npx -y github:dan-calin/shared-agent-memory`
  (unpinned `main` branch) — a supply-chain risk each time an agent starts.
- **Verified:** writes `~/.claude.json`, `~/.claude/settings.json` (PreToolUse hook), `~/.claude/CLAUDE.md` and the
  Codex equivalents; memory is one global file `~/.agent-memory/memory.json` shared across all projects, against
  project isolation.
- **Verified:** a dependency-free secret scanner (`lib/secrets.js`) guards writes; `AUDIT.md` records 13 bugs fixed in
  v0.5.0, including an uninstall that left a broken global hook.
- **Worth reusing (idea only):** claim board for concurrent agents (`lib/board.js`, `lib/coordination.js`) — Stage 3;
  secret-pattern list for redaction tests.

## 3. Not checked

Transitive npm/PyPI dependency trees, open CVEs, test quality, and every benchmark claim. If a repository is
reconsidered as a dependency, run the `dependency-license-review` skill and the `security-reviewer` agent first.
