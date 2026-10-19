---
name: sqlite-data-safety
description: Design, change or review SQLite usage in Python applications - schema changes and migrations, transactions, concurrency between threads, backups and data integrity. Use before altering tables, adding queries that write data, or touching database connection code.
---

# SQLite Data Safety

Use this skill whenever code reads or writes a SQLite database through Python's `sqlite3` module, and especially
before changing a schema. The goal is that no change loses, corrupts or silently rewrites stored data.

## 1. Inspect first

- Find the connection code: `isolation_level`, `check_same_thread`, PRAGMAs (`journal_mode`, `foreign_keys`,
  `busy_timeout`), shared vs per-thread connections, and any lock or transaction helper. Reuse the existing helper.
- Find how the schema is created and changed (an inline `SCHEMA` script, a migrations folder, a `user_version`
  PRAGMA). Follow the existing mechanism.
- Note that `isolation_level=None` means autocommit: each statement commits on its own unless the code issues
  `BEGIN` explicitly.

## 2. Queries

- Always use parameter placeholders (`?` or `:name`); never format values into SQL strings. Table or column names that
  must vary come from a fixed allow-list, never from input.
- Select named columns, not `SELECT *`, in code that depends on column order.
- Store timestamps in one documented form (UTC epoch seconds or ISO-8601 with offset). Store money and quantities in a
  documented unit and precision; be explicit about float rounding.

## 3. Transactions and concurrency

- Group writes that must succeed or fail together in one transaction; use `BEGIN IMMEDIATE` when the transaction will
  write, so lock conflicts appear at the start, not halfway.
- Keep transactions short: no network calls, sleeps or user waits inside one.
- A connection shared across threads (`check_same_thread=False`) needs a lock around every use, including reads that
  span several statements. WAL mode lets readers proceed during a write but still allows only one writer.
- Set a `busy_timeout` (or handle `database is locked`) instead of failing on the first contention.
- `PRAGMA foreign_keys` is off by default per connection; if the schema relies on foreign keys, enable it.

## 4. Schema changes (migrations)

- **Back up first** (see section 5) and state the backup location in the report.
- Make changes additive when possible: new tables, new nullable columns or columns with defaults. `CREATE TABLE IF NOT
  EXISTS` does not change an existing table; adding a column to an existing database needs `ALTER TABLE ... ADD COLUMN`,
  guarded by a check (`PRAGMA table_info`) or a version number.
- Renaming or dropping columns, changing types or constraints: use the documented 12-step rebuild (create new table,
  copy, drop old, rename) inside one transaction, then run `PRAGMA foreign_key_check` and `PRAGMA integrity_check`.
- Record the schema version (`PRAGMA user_version` or a version table) and make each migration run once.
- Never delete or rewrite historical records (trades, orders, fills, audit logs) as part of a migration unless the
  user explicitly approved that exact change.

## 5. Backups and recovery

- Back up with the online backup API (`sqlite3.Connection.backup`) or `VACUUM INTO`, not by copying the `.db` file while
  the app runs; in WAL mode a plain copy can miss the `-wal` file.
- Restore by stopping the app, replacing the database and its `-wal`/`-shm` files together, then restarting.
- Database files are data, not code: keep them out of Git and out of shared repositories.

## 6. Testing

- Test against a temporary database (`:memory:` or a temp file), never the real data file.
- For migrations: build a database with the **old** schema and sample rows, run the migration, assert data is preserved
  and the new schema is correct; run it twice to prove it is idempotent.
- Test transaction rollback: a failure in the middle leaves no partial writes.

## Trading-app notes

- `backend/db.py` and `backend/algo/store.py` each hold one shared connection in autocommit mode with WAL, guarded by a
  lock; `db.transaction()` wraps `BEGIN IMMEDIATE ... COMMIT/ROLLBACK`. Use it for multi-statement writes.
- Databases live in `backend/data/`. Back up before any schema change and never mix backtest, paper, demo and real
  records without their mode label.

## Official references

- [sqlite3 module (Python)](https://docs.python.org/3/library/sqlite3.html)
- [SQLite ALTER TABLE and the 12-step rebuild](https://www.sqlite.org/lang_altertable.html)
- [Write-Ahead Logging](https://www.sqlite.org/wal.html) and [Backup API](https://www.sqlite.org/backup.html)
