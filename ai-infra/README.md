# Infraestructura de IA — C:\Users\falon\Repos

Fecha: 17-10-2026. Agentes y skills de terceros para desarrollo backend, frontend, UI y UX.
Todo el contenido externo se trata como **no confiable**: se revisó antes de copiarlo y no se ejecutó
ningún instalador (`install.sh`, `npx skills add`, scripts de plugins).

## Estructura
- `vendor/` — copias completas (git clone --depth 1) de los repositorios de origen. Solo lectura.
- `../.claude/agents/` — agentes instalados (backend, frontend, ui, ux, calidad, ia).
- `../.claude/skills/` — skills instaladas.

Se cargan cuando Claude Code se arranca en `C:\Users\falon\Repos`. Dentro de un repo git (p. ej. Trading-app)
Claude solo sube hasta la raíz de ese repo, así que allí hay que usar `claude --add-dir C:\Users\falon\Repos`
o arrancar desde `C:\Users\falon\Repos`.

## Repositorios de origen
| Repositorio | ★ / forks (17-10-2026) | Commit | Licencia |
|---|---|---|---|
| [wshobson/agents](https://github.com/wshobson/agents) | 40.951 / 4.345 | `044b4b2` | MIT |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 25.778 / 3.009 | `408d3c9` | MIT |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 136.722 / 14.533 | `56ea9cf` | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 181.691 / 21.524 | `dbd4588` | Apache 2.0 (frontend-design) |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 32.549 / 2.842 | `063bee9` | MIT (README y SKILL) |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 996 / 69 | `434b7f9` | MIT |

## Agentes instalados
| Área | Agente | Origen | Herramientas |
|---|---|---|---|
| Backend | backend-architect | wshobson (backend-development) | hereda todas |
| Backend | python-pro | wshobson (python-development) | hereda todas, modelo opus |
| Frontend | frontend-developer | wshobson (frontend-mobile-development) | hereda todas |
| Frontend | react-specialist | VoltAgent | Read, Write, Edit, Bash, Glob, Grep |
| UI | ui-designer, design-system-architect, accessibility-expert | wshobson (ui-design) | hereda todas |
| UX | ux-researcher | VoltAgent | solo lectura + web |
| UX | ui-ux-tester | VoltAgent | Read, Write, Edit, Bash, web, navegador |
| Calidad | code-reviewer, debugger, test-automator | wshobson | hereda todas |

| IA | ai-environment-auditor | propio (17-10-2026) | solo lectura + Bash de consulta + web, modelo opus |

Cambio local: los agentes de wshobson tenían el nombre con prefijo de plugin
(`backend-development-backend-architect`…); se acortó solo el campo `name`.

## Skills instaladas
- UI/UX: `ui-ux-pro-max` (scripts Python de búsqueda en CSV locales, solo librería estándar, sin red),
  `frontend-design`, `web-design-guidelines`, `interaction-design`, `design-system-patterns`,
  `responsive-design`, `visual-design-foundations`, `wcag-audit-patterns`.
- Frontend: `vercel-react-best-practices`, `react-state-management`.
- Backend: `api-design-principles`, `python-testing-patterns`, `python-error-handling`.

Cambio local: `web-design-guidelines` descargaba sus reglas de GitHub en cada uso; ahora lee
`guidelines.md` (copia revisada) para no ejecutar instrucciones remotas sin revisar.

## Descartado / pendiente
- `anthropics/skills/webapp-testing`: requiere instalar Playwright y navegadores (dependencia nueva) y pide
  no leer su código. Descargado en `vendor/`, no instalado.
- `obra/superpowers` (300k★) y `affaan-m/ECC` (282k★): marcos generales con hooks y metodología propia que
  cambian el comportamiento global; no son específicos de back/front/UI/UX. No descargados.
- Revisión realizada: licencias, frontmatter y herramientas de cada agente, búsqueda de instrucciones de
  saltarse reglas, comandos destructivos, descargas, secretos e imports de red en scripts.

## Actualizar
`git -C vendor/<repo> pull`, revisar el diff (`git diff HEAD@{1}`) y volver a copiar solo lo revisado.
