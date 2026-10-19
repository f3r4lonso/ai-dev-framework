@AGENTS.md

## Claude Code only

- Claude Code loads every shared agent and skill from the `workshop` plugin (`.claude-plugin/`), read in place from
  this repository in every folder, no links and no `--add-dir`. Names carry the prefix: `workshop:<name>`. Setup:
  `clients/claude-code-cli/README.md`. After adding or renaming an agent run
  `python scripts/codex-adapter.py agents` (it also rebuilds the plugin's `agents` list) and `claude plugin validate .`.
- `clients/.codex/agents/` and `clients/personal/` are generated adapters: never edit them by hand.
