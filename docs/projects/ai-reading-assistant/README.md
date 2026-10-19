# AI Reading Assistant

- **Purpose:** a local web app with a Spanish interface. You add a TXT or DOCX file or paste text, the app cleans the
  text locally for review and editing, translates it into Spanish with Google Gemini only when it is not already
  Spanish and the user asks, and reads it aloud with the browser's voices at 1.2×, 1.5×, 1.75× or 2×. PDF is not
  supported yet (it would need an approved dependency).
- **Stage:** local MVP.
- **Repository:** private repository, on disk at `%USERPROFILE%\workshop\applications\ai-reading-assistant\`.
- **Start a session:**
  - Use the app: run `INICIAR.bat` in the repository (Python 3.12, no packages). Translation needs the
    `GEMINI_API_KEY` environment variable.
  - Work on the app: Claude Code in its repository with `claude --add-dir "$env:USERPROFILE\workshop\infra\clients"`.
- **Shared resources it uses:** built under the
  [ai-spanish-reading-assistant](../../../tasks/ai-spanish-reading-assistant.md) task; follows the
  `engineering-lifecycle`, `dependency-license-review` and `wcag-audit-patterns` rows of the
  [skill catalogue](../../catalogues/skills.md).
- **Project-specific resources:** in the project repository.
