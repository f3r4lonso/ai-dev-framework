# AgentDex — Documentación del proyecto

Oct 22, 2026 · @Fernando

**Estado: listo para empezar.** Revisado el repo `workshop-ai`: AgentDex será una sección de Workshop AI que sustituye y amplía «Agentes y Skills», con el mismo servidor y las mismas reglas de v2. Para arrancar D0 solo falta tu visto bueno a las decisiones propuestas de 10.

AgentDex es un catálogo tipo Pokédex pixel art de todo lo necesario para trabajar con IA, con dos niveles (Workshop y Cliente), y un Gym que mejora cada entidad con sus usos reales. Uso personal y local.

## Documentos

| Doc | Qué responde |
| --- | --- |
| 01 · PRD | Qué se construye: glosario, especies, alcance, historias, requisitos, aceptación |
| 02 · Modelo de dominio | Con qué datos: entidades, regla de niveles, agrupaciones |
| 03 · Gym | Cómo mejora cada entidad: ciclo, métricas, XP, versiones |
| 04 · Arquitectura | Cómo está hecho: diagrama, stack, local y nube, repo |
| 05 · API | Contrato de la API |
| 06 · UI y estilo pixel | Cómo se ve: imágenes de las vistas y guía de estilo |
| 07 · Integración Workshop | Dónde va dentro de Workshop AI y qué reglas aplica |
| 08 · Ingesta y clientes | De dónde salen las entidades y cómo se calcula la compatibilidad |
| 09 · Plan y backlog | En qué orden se hace: roadmap y backlog |
| 10 · Decisiones | Qué se decidió y qué falta |

## Cambios tras revisar Workshop AI

- Ya no es una app embebida: es una sección de la app, sin iframe, sin FastAPI y sin Docker (07, 04).
- El Gym usa los usos de Conversar y Tareas, evalúa cuando pulsas Entrenar y las versiones nuevas se guardan con el editor de V2 (03).
- La búsqueda en internet la hace el agente `task-resource-scout` cuando tú lo lanzas (08).
- El plan se encaja en los incrementos de v2: el dex de lectura puede empezar ya; el Gym espera a V2 y V3 (09).

## Listo para empezar

- [x] Alcance, especies y niveles
- [x] Gym diseñado dentro de las reglas de v2
- [x] Arquitectura, API e integración alineadas con el repo
- [x] Imágenes de la UI y guía de estilo
- [x] Backlog de D0 y D1
- [x] Punto de integración en Workshop UI (Q-07)
- [ ] Tu visto bueno a ADR-002 y ADR-007 a ADR-013

## Riesgos

- **Dependencia de V2 y V3:** sin editor ni conversaciones guardadas, el Gym no puede cerrar su ciclo; el dex de lectura sí.
- **Nivel 2 sin herramientas:** el reto solo mide texto; las entidades con herramientas esperan al nivel 3 (V6).
- **Formatos que cambian, sobre todo hooks:** reglas con fecha de verificación y tests por fixture.
- **Repo público:** `infra` lo es por diseño; `workshop-ai` está público ahora aunque el README dice privado (Q-13).
