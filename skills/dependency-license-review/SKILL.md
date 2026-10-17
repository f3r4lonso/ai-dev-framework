---
name: dependency-license-review
description: Reviews license, origin, maintenance, transitive dependencies and install scripts before adding a dependency (pip/npm) or copying external code into the trading app.
---

# Dependency and license review

Current dependencies: `backend/requirements.txt` (Flask, pandas, numpy, requests, yfinance) and `frontend/package.json`
(react, react-dom, lightweight-charts, vite, @vitejs/plugin-react). Any addition requires the user's authorization.

## Steps
1. **Is it needed?** Does the standard library or an existing dependency solve it? Document the reason.
2. **Exact version** (release or commit) and its **license at that version** (read LICENSE, not just the SPDX id).
3. **Compatibility**: MIT / BSD / Apache-2.0 → reusable with attribution. GPL / AGPL → do not copy code (it would force
   licensing the app the same way). LGPL → only as an unmodified library. Commons Clause → not sellable. No license → do not use.
4. **Maintenance**: latest release, known security issues, whether it is archived.
5. **Transitive dependencies** and size from metadata only, without installing or building anything:
   PyPI JSON API (`https://pypi.org/pypi/<pkg>/<version>/json`, field `requires_dist`) and `npm view <pkg> dependencies`.
   Do not use `pip install --dry-run` on its own: for source-only packages pip runs the package's build backend
   (arbitrary code) to read metadata. If a resolver run is really needed, add `--only-binary=:all:` and ask first.
6. **Install scripts**: `setup.py`, `postinstall` hooks, downloaded binaries, telemetry.
7. **Permissions and network**: does it make external calls or need keys?

## Rules
- If compatibility or the right to reuse is unclear, **do not copy** the code.
- Copied or adapted code: keep license notices and record its provenance in `docs/REFERENCE_REPOS.md`.
- Pin exact versions in `requirements.txt` / `package.json`.

## Deliverable
Table: package · version · license · reason · risks · decision (add / reject / alternative).
