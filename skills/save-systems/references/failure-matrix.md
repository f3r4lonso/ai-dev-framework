# Persistence failure matrix

Workshop additions, 2026-10-19. Specify expected outcomes first; run these cases only in authorized development.

| Failure or transition | Required behavior |
|---|---|
| Unsupported newer schema | Preserve the file unchanged, explain incompatibility, and prevent autosave from replacing it. |
| Malformed or oversized data | Bound file size, nesting and collection lengths; validate finite numbers, IDs, types and ranges before allocation or mutation. |
| Interrupted update | Keep a previously validated recovery generation until the new generation is validated and committed; never rotate corrupt primary data over the last good backup. |
| Disk full, permission or replace failure | Check operation results, keep the existing valid generation and report failure; retry only with a bounded policy. |
| Migration failure | Migrate a copy, preserve the original, fail clearly and avoid partially mutating live state. Test retained fixtures from every supported release. |
| Background/termination | Checkpoint after complete game actions; do not depend solely on an exit callback. Define acceptable progress loss explicitly. |
| Procedural generation or RNG | Record required generator/content versions and RNG state, or authoritative generated outcomes; a seed alone may not reproduce later turns or changed generators. |
| Concurrent save requests | Serialize commits or define a transaction owner; prevent stale work replacing newer progress. |
| Cloud conflict, if approved | Define revision/conflict rules separately; timestamps alone do not establish authority. Never silently overwrite conflicting player progress. |

Atomic replacement and crash durability are distinct. A temporary file plus rename is not a universal guarantee;
verify the actual filesystem, engine API, synchronization and transaction semantics. Backups improve recovery only
when retained and validated correctly. Checksums detect some corruption; they do not prove authenticity.
Keep credentials out of saves. Avoid executing serialized object graphs. For SQLite, consult the existing
sqlite-data-safety skill only if that technology is selected; no database is required by this skill.
