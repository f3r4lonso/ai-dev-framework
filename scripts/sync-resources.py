#!/usr/bin/env python3
"""Copy the canonical Workshop library into client discovery folders.

Default: install into the Workshop root and infra repository. --project PATH
selects a different project (repeatable). --user installs for the current OS user;
run that outside a restricted session when its home directories are not writable.
No client processes, configuration files, credentials or downloaded code are run.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ".workshop/resources.json"
IGNORED = {".git", "__pycache__", "node_modules", ".venv"}
PREFIXES = (".agents/skills/", ".claude/skills/", ".claude/agents/", ".codex/agents/",
            ".github/agents/", ".copilot/agents/", ".gemini/agents/")
spec = importlib.util.spec_from_file_location("workshop_adapter", ROOT / "scripts/codex-adapter.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_link(path: Path) -> bool:
    if path.is_symlink():
        return True
    try:
        attrs = getattr(path.lstat(), "st_file_attributes", 0)
    except FileNotFoundError:
        return False
    # Path.is_junction is only available in Python 3.12+. Check reparse attributes
    # as well so the advertised Python 3.11 minimum cannot bypass containment.
    return bool(attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def safe_target(base: Path, relative: str) -> Path:
    """Only owned resource paths; no symlink/junction ancestors, even within base."""
    if relative != MANIFEST and not relative.startswith(PREFIXES):
        raise ValueError(f"not a resource destination: {relative}")
    parts = Path(relative).parts
    if Path(relative).is_absolute() or any(p in ("..", ".") or ":" in p for p in parts):
        raise ValueError(f"unsafe resource destination: {relative}")
    current = base
    for part in parts:
        current = current / part
        if is_link(current):
            raise ValueError(f"refusing linked destination: {current}")
    current.resolve().relative_to(base.resolve())
    return current


def resource_files():
    for skill in sorted(ROOT.glob("skills/*/SKILL.md")):
        name = skill.parent.name
        if not re.fullmatch(r"[a-z0-9-]+", name):
            raise ValueError(f"invalid skill folder: {name}")
        for path in sorted(skill.parent.rglob("*")):
            relative = path.relative_to(skill.parent)
            if set(relative.parts) & IGNORED:
                continue
            if is_link(path):
                raise ValueError(f"linked skill source requires review: {path}")
            if not path.is_file():
                continue
            lower = path.name.lower()
            if (lower.startswith(".env") or lower in {"auth.json", "settings.local.json", ".netrc", ".npmrc"}
                    or "credential" in lower or lower.endswith((".key", ".pem", ".token"))):
                raise ValueError(f"forbidden resource file: {path}")
            yield f"{name}/{relative.as_posix()}", path.read_bytes()


def agent_profiles(src: Path) -> tuple[str, dict[str, bytes]]:
    fm = adapter.read_frontmatter(src)
    name, description = fm["name"], fm["description"]
    if not re.fullmatch(r"[a-z0-9-]+", name):
        raise ValueError(f"invalid agent name: {name}")
    # Reuse the established native-format renderer, for shared and personal agents.
    rendered = adapter.render_personal(src)
    denied = {v.strip() for v in fm.get("disallowedTools", "").split(",") if v.strip()}
    if denied:
        allowed = [v.strip() for v in fm.get("tools", "").split(",") if v.strip() not in denied]
        for client, mapping in (("copilot", adapter.COPILOT_TOOLS), ("gemini", adapter.GEMINI_TOOLS)):
            tools = sorted({mapped for v in allowed if v in mapping
                            for mapped in ([mapping[v]] if isinstance(mapping[v], str) else mapping[v])})
            filename, body = rendered[client]
            body = re.sub(r"^tools: .*?$", "tools: " + adapter.yaml_list(tools), body, count=1, flags=re.M)
            rendered[client] = filename, body
    note = (f"Canonical resource: {src.as_posix()}. Workshop root: {ROOT.parent.as_posix()}; "
            f"infrastructure root: {ROOT.as_posix()}. Paths starting infra/ or applications/ resolve "
            "from the Workshop root. Framework paths starting agents/, skills/, docs/ or tasks/ "
            "resolve from the infrastructure root. Paths belonging to the user's task/project "
            "retain their own working-directory meaning. "
            "Read the applicable project rules and infra/SECURITY.md before working. "
            "Claude-specific tool names describe intended capabilities; use available native equivalents. "
            "Preserve every denied tool and role scope as an instruction; mappings are not a sandbox. "
            f"Declared allowed tools: {fm.get('tools', 'all')}; denied: {', '.join(sorted(denied)) or 'none'}. "
            "If a required capability is unavailable, report it rather than claiming completion.\n\n")
    preload = [value for value in fm.get("skills", "").split() if value not in {"-", "[", "]"}]
    if preload:
        note += "Preload the role's declared skills from the infrastructure skills/<name>/SKILL.md: " + ", ".join(preload) + ".\n\n"
    for client, (filename, body) in list(rendered.items()):
        if client == "codex":
            # Parse, then serialize again: never edit an escaped TOML string by replacement.
            import tomllib
            profile = tomllib.loads(body)
            profile["developer_instructions"] = note + profile["developer_instructions"]
            body = "# GENERATED by scripts/sync-resources.py; edit the canonical agent.\n"
            body += "".join(f"{key} = {adapter.toml_str(value)}\n" for key, value in profile.items())
        else:
            if client == "copilot":
                body = body.replace("\n---\n", "\ninclude-custom-instructions: true\n---\n", 1)
            end = body.index("\n---", 3) + 4
            body = body[:end] + "\n\n" + note + body[end:].lstrip()
        rendered[client] = filename, body
    profiles = {}
    for client, (filename, body) in rendered.items():
        profiles[client] = body.encode("utf-8")
    claude_body = src.read_text(encoding="utf-8")
    end = claude_body.index("\n---", 3) + 4
    profiles["claude"] = (claude_body[:end] + "\n\n" + note + claude_body[end:].lstrip()).encode("utf-8")
    return name, profiles


def expected_files(user: bool) -> dict[str, bytes]:
    expected = {}
    for relative, content in resource_files():
        for folder in (".agents/skills", ".claude/skills"):
            expected[f"{folder}/{relative}"] = content
    seen = set()
    for src in adapter.agent_sources() + adapter.personal_sources():
        name, profiles = agent_profiles(src)
        if name in seen:
            raise ValueError(f"duplicate agent name: {name}")
        seen.add(name)
        for client, folder, suffix in (("claude", ".claude/agents", ".md"),
                                       ("codex", ".codex/agents", ".toml"),
                                       ("copilot", ".copilot/agents" if user else ".github/agents", ".agent.md"),
                                       ("gemini", ".gemini/agents", ".md")):
            expected[f"{folder}/{name}{suffix}"] = profiles[client]
    return expected


def legacy_profiles(user: bool) -> dict[str, bytes]:
    """Recognize exact prior adapter output, never ownership by a header alone."""
    legacy = {}
    for src in adapter.personal_sources():
        for client, (filename, body) in adapter.render_personal(src).items():
            folder = {"codex": ".codex/agents", "copilot": ".copilot/agents" if user else ".github/agents",
                      "gemini": ".gemini/agents"}[client]
            legacy[f"{folder}/{filename}"] = body.encode("utf-8")
    return legacy


def plan_sync(base: Path, expected: dict[str, bytes], legacy=None, keep_existing_agents=False, preserved=None):
    if not base.is_dir():
        raise ValueError(f"destination root does not exist: {base}")
    # Resolve ancestor links before the root, but reject a linked selected root itself.
    if is_link(base):
        raise ValueError(f"refusing linked destination root: {base}")
    manifest = safe_target(base, MANIFEST)
    old = {}
    if manifest.exists():
        stored = json.loads(manifest.read_text(encoding="utf-8"))
        if stored.get("schema") != 1 or not isinstance(stored.get("files"), dict):
            raise ValueError(f"unrecognized resource manifest: {manifest}")
        old = stored["files"]
    writes, deletes, conflicts = [], [], []
    preserved = preserved if preserved is not None else []
    for relative, data in expected.items():
        target = safe_target(base, relative)
        if target.exists():
            if not target.is_file():
                conflicts.append(relative)
                continue
            current = target.read_bytes()
            if current == data:
                continue  # Adopt a pre-existing copy only when its bytes match.
            if old.get(relative) != digest(current) and (legacy or {}).get(relative) != current:
                if keep_existing_agents and relative.startswith(tuple(p for p in PREFIXES if p.endswith('/agents/'))):
                    preserved.append(relative)
                    continue
                conflicts.append(relative)
                continue
        writes.append((target, data))
    for relative, previous in old.items():
        if relative in expected:
            continue
        if relative == MANIFEST:
            raise ValueError("manifest cannot own itself")
        target = safe_target(base, relative)
        if target.exists():
            if not target.is_file() or digest(target.read_bytes()) != previous:
                conflicts.append(relative)
            else:
                deletes.append(target)
    if conflicts:
        raise ValueError("preserved unowned or modified files in " + str(base) + ": " + ", ".join(conflicts))
    metadata = {"schema": 1, "files": {rel: digest(data) for rel, data in sorted(expected.items())
                                      if rel not in preserved}}
    if preserved:
        metadata["preserved_agents"] = sorted(preserved)
    metadata_bytes = (json.dumps(metadata, indent=2) + "\n").encode()
    if not manifest.exists() or manifest.read_bytes() != metadata_bytes:
        writes.append((manifest, metadata_bytes))
    return writes, deletes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project", action="append", type=Path, help="project root; may be repeated")
    scope.add_argument("--user", action="store_true", help="install across folders for the OS user")
    parser.add_argument("--keep-existing-agents", action="store_true",
                        help="preserve conflicting native agent files and install the remaining resources")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail on drift, without writes")
    mode.add_argument("--dry-run", action="store_true", help="show pending changes, without writes")
    args = parser.parse_args()
    try:
        expected = expected_files(args.user)
        bases = [Path.home()] if args.user else (args.project or [ROOT.parent, ROOT])
        # Preflight every destination before changing any of them.
        legacy = legacy_profiles(args.user)
        plans = []
        for base in dict.fromkeys(bases):
            preserved = []
            writes, deletes = plan_sync(base, expected, legacy, args.keep_existing_agents, preserved)
            plans.append((base, writes, deletes, preserved))
        changed = 0
        for base, writes, deletes, preserved in plans:
            changed += len(writes) + len(deletes)
            print(f"{base}: {len(expected)} resource files, {len(writes)} to write, {len(deletes)} retired copies")
            for relative in preserved:
                print(f"Preserved existing agent (not managed or updated): {relative}")
            if args.check or args.dry_run:
                continue
            for path, data in writes:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            for path in deletes:
                path.unlink()  # Individual unchanged manifest-owned files only; never recursive.
        return 1 if args.check and changed else 0
    except (OSError, ValueError, KeyError) as error:
        print(f"Resource sync stopped: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
