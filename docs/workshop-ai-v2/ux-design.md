# Workshop AI v2: UX design

Status: **approved** (2026-10-20, with decisions D-V2-01…09). Based on the existing UI review records and desk research of comparable
products (sources in §6). No usability session with the owner has taken place yet; V1 ends with one (roadmap).

## 1. Wording rules

- All screen text in Spanish; technical docs stay English.
- Words never shown: commit, git, YAML, frontmatter, worktree, stdin, JSON, handoff. Use instead: *versión*,
  *datos de la ficha*, *copia de trabajo*, *pasar a otro motor*.
- Every agent, skill and task card shows its Spanish summary first, the English description as secondary text.
- Errors say what happened and what to do next ("No se pudo guardar: el archivo cambió mientras lo editabas. Tu
  borrador está a salvo. [Ver diferencias]").

## 2. Navigation

A left sidebar with seven sections, a global search bar on top (Ctrl+K or `/`), and an engine status strip.

| Section | Purpose | Replaces today |
|---|---|---|
| **Inicio** | What needs me: approvals waiting, runs in progress, failures; recent work; engine strip | Inicio tiles |
| **Tareas** | Board by state; each card opens the task page | read-only Tareas list |
| **Conversar** | One composer: Agente picker, Motor picker (Automático or one engine), conversation list | Cadena de agentes tab (chains become a mode here) |
| **Agentes y Skills** | Library cards, "Nuevo", "Duplicar", "Editar", "Probar en una conversación" | Agentes, Skills, Asistentes sections |
| **Archivos** | Documents, briefs, plans, application docs; editor with versions | Documentos, Aplicaciones sections |
| **Motores** | One card per engine ([engines.md](engines.md)): level, status, "Probar", "Abrir consola", good-for line | Clientes IA section + sidebar launch buttons |
| **Historial** | Timeline of saves, runs, checkpoints and handoffs, searchable; restore from here | nothing |

Owner update (2026-10-21): the right-hand **Lector** is to be replaced by an editor for the selected document.
Remove its reading, translation and audio controls from that panel. Add personal TXT/Notepad and active Workshop
folder shortcuts. This V2 change is built locally and awaiting owner acceptance; the concrete layout, privacy
requirements and acceptance checks are in the [editor and notes plan](../../../applications/workshop-ai/docs/v2-editor-and-notes-plan.md).

## 3. Screens

### 3.1 Editor (Archivos, also used by the agent/skill library)

```text
┌ Ficha ───────────────────────────────┐┌ Contenido ─────────────────────────────┐
│ Nombre      [risk-engineer        ]  ││ Markdown editor with preview toggle     │
│ Para qué    [Revisa el motor de... ]  ││                                         │
│ Herramientas [Read][Grep][+]         ││                                         │
│ Motor por defecto [Claude ▾]          ││                                         │
└──────────────────────────────────────┘└─────────────────────────────────────────┘
[Modo avanzado]   [Versiones (12)]          [Revisar cambios]  [Guardar]
```

- The header form shows only fields the file type defines; unknown fields stay untouched and visible in
  Modo avanzado.
- "Revisar cambios" shows a side-by-side diff in plain colours; Guardar is enabled only after validation passes.
- "Versiones" lists app-made versions ("Hoy 10:32 · antes de tu edición") with Comparar and Restaurar.
- If the file changed on disk, the save stops, the draft is kept and the diff of both versions is offered.

### 3.2 Conversar

- Top: Agente picker (search, Spanish summaries, recently used) and Motor picker showing level and status.
- Answer area with streamed text where the engine supports it; a stop button; a usage line under each answer.
- Side list of saved conversations; each has "Guardar como tarea" and "Continuar en consola".
- **Modo cadena**: add 2–5 agents in order; each stage's output is shown and labelled before the next starts.

### 3.3 Tareas

- Columns: Borrador · En cola · En curso · Esperando mi aprobación · Hecha (Archivada hidden by default).
- Card: title, project, engine chip, last checkpoint time, pending-approval badge.
- Task page tabs: **Resumen** (objective, acceptance criteria, next action), **Decisiones**, **Ejecuciones** (runs with
  output and usage), **Cambios** (diffs), **Puntos de control**, **Pasar a otro motor**.
- Primary actions: "Empezar en…" (engine picker, shows the brief first), "Guardar punto de control",
  "Marcar como hecha".

### 3.4 Agentes y Skills wizard

Steps: 1 Plantilla (reviewer, editor, researcher, checklist skill, blank) → 2 Nombre y para qué sirve (name is
generated in kebab-case, collision check) → 3 Instrucciones (editor with template sections) → 4 Herramientas
(plain-language checkboxes: "leer archivos", "buscar", "editar archivos", "ejecutar comandos"; read-only preset
first) → 5 Probar en una conversación → 6 Revisar y guardar (shows every file that will change: the new file,
catalogue row, inventory line, adapter regeneration).

### 3.5 Motores

Card per engine: name, one-line "bueno para", level badge (Enlace / Consola / Conversar / Tarea de lectura / Tarea
con cambios), Instalado, Sesión (sí / no / desconocida), what unlocks the next level, buttons Probar and Abrir
consola. Engines that cannot be integrated (Suno, claude.ai) show their link and the rule that applies.

## 4. Main flows

1. **Edit an agent**: Agentes y Skills → card → Editar → change "Para qué" → Revisar cambios → Guardar → toast
   "Guardado. Versión anterior disponible en Versiones."
2. **Ask an agent something**: Conversar → Agente "quant-researcher" → Motor Automático (Claude chosen and shown) →
   type → answer → "Guardar como tarea".
3. **Give a task and follow it**: Tareas → Nueva → objective + criteria → Empezar en… Claude (Consola with brief,
   or Tarea de lectura) → card moves to En curso → result → Esperando mi aprobación → Aprobar → Hecha.
4. **Switch engine when quota runs out**: task page → Pasar a otro motor → choose Codex → review scanned package →
   Aprobar → Codex console opens with the package.
5. **Add a skill**: Agentes y Skills → Nuevo → Skill de lista de comprobación → … → Revisar y guardar.
6. **Undo a mistake**: Historial → find the save → Comparar → Restaurar.

## 5. Anti-patterns to avoid

Raw file editing as the only way; auto-applied agent edits; silent engine switch or spend; seven equal engine
buttons without guidance; terminals as the main interaction; mixed-language cards; memory-only state; too many
concepts (Open WebUI has five workspace concepts; we keep two: agentes and skills).

## 6. Sources

Claude Code Desktop (sessions sidebar, permission modes, diff view): https://code.claude.com/docs/en/desktop ·
GitHub Copilot agent sessions (mission control, steering, review): https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks/ ·
Cline checkpoints (compare and restore): https://docs.cline.bot/features/checkpoints · Cline task history:
https://docs.cline.bot/features/tasks/task-management · Open WebUI model presets: https://docs.openwebui.com/features/workspace/models ·
Obsidian Properties (typed header form, source fallback; community reports of template corruption) · Codex app review
queue (secondary source). Existing records: [ui-review.md](../../../applications/workshop-infrastructure-ui/docs/ui-review.md),
[interaction-upgrade.md](../../../applications/workshop-infrastructure-ui/docs/interaction-upgrade.md).
