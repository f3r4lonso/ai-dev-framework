# AI Reading Assistant

- **Purpose:** a local web app with a Spanish interface. You add a TXT or DOCX file or paste text, the app cleans the
  text locally for review and editing, translates it into Spanish with a local Ollama model (on this machine, no Internet) only when it is not
  already Spanish and the user asks, and reads it aloud with the browser's voices at 1.2×, 1.5×, 1.75× or 2×. PDF is not
  supported yet (it would need an approved dependency).
- **Stage:** local MVP.
- **Repository:** private repository, on disk at `%USERPROFILE%\workshop\applications\ai-reading-assistant\`.
- **Start a session:**
  - Use the app: run `INICIAR.bat` in the repository (Python 3.12, no packages). Translation needs Ollama
    running locally with a model (`READING_ASSISTANT_LOCAL_MODEL`); Ollama is not installed yet (task `ollama-install`),
    so translation is unavailable today.
  - Work on the app: Claude Code in its repository with plain `claude` (shared agents and skills load from the `workshop` plugin).
- **Shared resources it uses:** built under the
  [ai-spanish-reading-assistant](../../../tasks/projects/ai-reading-assistant/ai-spanish-reading-assistant.md) task; follows the
  `engineering-lifecycle`, `dependency-license-review` and `wcag-audit-patterns` rows of the
  [skill catalogue](../../catalogues/skills.md).
- **Project-specific resources:** in the project repository.
