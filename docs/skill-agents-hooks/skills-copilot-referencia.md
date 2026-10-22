# Skills de GitHub Copilot: lista de referencia

Este documento tiene dos partes. La primera es un ranking por estrellas de GitHub. La segunda es una lista de skills citadas en tres fuentes externas. No es un ranking de instalaciones: no hay una fuente fiable de instalaciones por skill para Copilot.

---

## 1. Ranking por estrellas de GitHub (repositorios de Copilot)

Las fuentes encontradas solo tienen una skill con relación directa a Copilot en el ranking general. El resto son skills cross-plataforma (formato SKILL.md, válido también para Copilot) y no se han separado por plataforma.

| # | Repositorio | Estrellas | Qué es | Enlace |
|---|-------------|-----------|--------|--------|
| 1 | github/awesome-copilot | 37,7k (página del repo) / 40,2k (skillleaderboard, 20 oct 2026) | Colección comunitaria de instrucciones, agentes, skills y configuraciones para GitHub Copilot. Incluye más de 100 skills, entre ellas creación de README, commits convencionales, ADRs, diagnóstico de Azure y más. | https://github.com/github/awesome-copilot |
| 2 | microsoft/skills | 3,1k | Catálogo de skills de Microsoft para Azure, Foundry, .NET, Python, TypeScript, Java y Rust, además de skill-creator y mcp-builder. | https://github.com/microsoft/skills |
| 3 | samueltauil/skills-hub | Sin verificar | Catálogo curado de skills de GitHub Copilot para buscar, explorar y descargar. | https://github.com/samueltauil/skills-hub |

Las cifras de estrellas de awesome-copilot difieren entre fuentes (37,7k frente a 40,2k). Usa la del propio repositorio como referencia.

---

## 2. Skills citadas en las fuentes

Las tres fuentes no coinciden en casi ninguna skill. La columna **Repositorio** solo tiene enlace cuando he podido comprobar la skill en `github/awesome-copilot` o `microsoft/skills`. En el resto aparece "Sin verificar".

### 2.1 Skills de skills-guides.com (24)

| Skill | Repositorio | Descripción |
|-------|-------------|-------------|
| React Hook Form Best Practices | Sin verificar | Evitar antipatrones de React Hook Form: reset, estado "dirty" e inputs controlados. |
| Firecrawl Build Search | Sin verificar | Usar la búsqueda de Firecrawl para descubrir webs antes de extraer contenido. |
| Set up pre-commit hooks with Husky, lint-staged, Prettier | Sin verificar | Hooks de pre-commit que formatean, comprueban tipos y ejecutan tests. |
| Playwright E2E Testing Patterns | Sin verificar | Page Object Model, integración con CI/CD y estrategias contra tests inestables. |
| Home Assistant Integration Knowledge | Sin verificar | Construir, probar y revisar integraciones de Home Assistant. |
| Grafana Panel & Viz Testing Strategy | Sin verificar | Tests unitarios y E2E para paneles de visualización de Grafana. |
| Database Migration | Sin verificar | Migraciones de esquema y datos entre ORMs, con estrategias de rollback. |
| Algorithms and Data Structures Education | Sin verificar | Implementaciones educativas documentadas y probadas de algoritmos en Java. |
| Latency-Critical Systems | Sin verificar | Diseñar y optimizar sistemas sensibles a la latencia. |
| Chakra UI Builder | Sin verificar | Componentes y temas accesibles con Chakra UI v3. |
| Create Admin Routing | Sin verificar | Rutas de administración en YAML para Symfony. |
| Dart/Flutter Patterns | Sin verificar | Null safety, gestión de estado y arquitectura en Dart y Flutter. |
| Find Ready-to-Merge PRs | Sin verificar | Buscar PRs de Home Assistant que se pueden fusionar ya. |
| Microservices Architecture Patterns | Sin verificar | Límites de servicios, comunicación y patrones de resiliencia. |
| Identify Assumptions (New Product) | Sin verificar | Detectar supuestos arriesgados en ocho categorías de riesgo. |
| Supabase Studio Error Handling | Sin verificar | Clasificación de errores, renderizado de UI y resolución de problemas en Supabase Studio. |
| Creating pull requests | Sin verificar | Convenciones del cuerpo de los PRs, como enlazar tickets e issues. |
| Laravel Verification Loop | Sin verificar | Flujo de verificación con linting, análisis, tests y auditoría de seguridad (marcada como "Caution"). |
| AWS CDK Reusable Patterns | Sin verificar | Constructos reutilizables de CDK y stacks de infraestructura en producción. Similar a `aws-cdk-python-setup` del repo de awesome-copilot, pero no es la misma skill. |
| Threat Modeling Expert | Sin verificar | STRIDE, PASTA, árboles de ataque y requisitos de seguridad. |
| Async Python Patterns | Sin verificar | Patrones de asyncio y concurrencia no bloqueante. |
| React State Management | Sin verificar | Redux Toolkit, Zustand, Jotai y React Query. |
| Influencer Brief | Sin verificar | Briefs estructurados para campañas con creadores. |
| DTO Contracts | Sin verificar | Estructura y reglas de transformación de DTOs. |

### 2.2 Skills de agensi.io (11)

| Skill | Repositorio | Descripción |
|-------|-------------|-------------|
| code-reviewer | Sin verificar | Revisa código buscando bugs, problemas de seguridad, rendimiento y estilo, ordenados por gravedad. |
| git-commit-writer | Sin verificar | Escribe mensajes de commit convencionales a partir de los cambios en staging. Similar a `conventional-commit` de awesome-copilot. |
| readme-generator | Sin verificar | Analiza un proyecto y genera un README completo. Similar a `create-readme` de awesome-copilot. |
| env-doctor | Sin verificar | Diagnostica de forma sistemática los fallos al arrancar un proyecto. |
| pr-description-writer | Sin verificar | Escribe descripciones de pull request a partir de un diff. |
| changelog-generator | Sin verificar | Genera notas de versión a partir del historial de commits. |
| codex-grade-coding | Sin verificar | Protocolos estrictos y guiados por verificación para reducir errores de código. |
| ai-productivity | Sin verificar | Convierte prompts vagos en tareas estructuradas y comprime el contexto. |
| java-best-practice-checker | Sin verificar | Audita código Java (desde Java SE 8 hasta 24) buscando fugas de rendimiento, riesgos de hilos y falta de modernización. |
| skill-polisher | Sin verificar | Pule cualquier documentación en markdown. |
| lobster-debugging | Sin verificar | Marco de cuatro fases para encontrar causas raíz y evitar regresiones. |

### 2.3 Skills de getclaudeskills.com (24)

| Skill | Repositorio | Descripción |
|-------|-------------|-------------|
| Playwright Component Testing | Sin verificar (propietario: microsoft) | Tests aislados de componentes React y Vue con Playwright. |
| Heap Snapshot Analysis | Sin verificar (propietario: microsoft) | Análisis de snapshots del heap de V8 para detectar problemas de memoria. |
| VS Code Performance Workflow | Sin verificar (propietario: microsoft) | Automatiza investigaciones de rendimiento en VS Code. |
| GitHub Issues | Sin verificar (propietario: github) | Gestiona issues de GitHub mediante herramientas MCP. |
| Draw.io Diagram Generator | Sin verificar (propietario: github) | Crea y valida diagramas de draw.io. |
| WinMD API Search | Sin verificar (propietario: github) | Busca y explora APIs de escritorio de Windows. |
| Power Automate Flow Builder | Sin verificar (propietario: github) | Construye y despliega flujos de Power Automate. |
| Excalidraw Diagram Generator | Sin verificar (propietario: github) | Convierte lenguaje natural en diagramas de Excalidraw. |
| ClickHouse Logs Queries | Sin verificar (propietario: supabase) | Gestiona logs de Supabase con SQL de ClickHouse. |
| Skill Creator | `microsoft/skills` (skill-creator) | Guía para crear y gestionar skills. |
| Initiating Coverage | Sin verificar (propietario: anthropics) | Crea informes de análisis de renta variable. |
| GitHub Actions Hardening | Sin verificar (propietario: github) | Mejora la seguridad de los workflows de GitHub Actions. |
| Power BI Semantic Modeling | Sin verificar (propietario: github) | Optimiza modelos de datos de Power BI. |
| Azure Container Registry CLI | [azure-container-registry-cli](https://github.com/github/awesome-copilot/tree/main/skills/azure-container-registry-cli) | Gestiona Azure Container Registry con la CLI `az acr`. |
| Minecraft Plugin Development | Sin verificar (propietario: github) | Facilita la creación de plugins para servidores de Minecraft. |
| Azure Architecture Builder | Sin verificar (propietario: github). Similar a `azure-architecture-autopilot` de awesome-copilot | Diseña y despliega infraestructura de Azure a partir de lenguaje natural. |
| Plugin Structure | Sin verificar (propietario: anthropics) | Crea y organiza plugins de Claude Code. |
| Daily Focus Board | Sin verificar (propietario: github) | Apoya la gestión diaria de tareas y el foco. |
| Agent Development | Sin verificar (propietario: anthropics) | Crea y gestiona agentes autónomos para Claude Code. |
| Build MCP App | Sin verificar (propietario: anthropics). Similar a `mcp-builder` de microsoft/skills | Crea widgets de interfaz interactivos para servidores MCP. |
| Azure Pipelines Validation | Sin verificar (propietario: microsoft) | Valida cambios en pipelines de Azure DevOps en local. |
| Geofeed Tuner | Sin verificar (propietario: github) | Optimiza feeds de geolocalización IP en CSV. |
| WebMCPify | Sin verificar (propietario: github) | Hace que las aplicaciones web sean utilizables por agentes. |
| MVVM Toolkit | Sin verificar (propietario: github) | Agiliza el desarrollo de ViewModels con generadores de código fuente. |

---

## 3. Notas

- Las tres fuentes solo coinciden en el nombre de unas pocas skills, así que esta lista no refleja una "más citada" consensuada.
- Algunas cifras de las fuentes son ambiguas: skills-guides muestra números idénticos para skills no relacionadas, y getclaudeskills etiqueta sus cifras como "repo", no como instalaciones. Por eso no se han usado como ranking.
- Para skills de Copilot de calidad probada, empieza por `github/awesome-copilot` y `microsoft/skills`. Revisa la licencia y el contenido del SKILL.md antes de instalar cualquiera.
