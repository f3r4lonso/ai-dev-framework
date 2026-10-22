"""Strict, lossless Workshop resource headers (standard library only).

This deliberately supports a small YAML subset, not arbitrary YAML. Unsupported
headers must stay in advanced mode; callers may retain an unchanged raw header
when saving only the body, but must never reinterpret changed invalid headers.
String values use decoded scalar semantics with the adapter's flat/list layout.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass

EDITABLE_FIELDS = frozenset({"name", "description", "tools", "disallowedTools", "model", "color", "skills"})
_KEY = re.compile(r"([A-Za-z][A-Za-z0-9_-]*):(?: +(.*))?$")


def _scalar(value: str) -> str:
    if not value:
        return ""
    if value[0] in "\"'":
        if len(value) < 2 or value[-1] != value[0]:
            raise ValueError("Unterminated quoted header value")
        if value[0] == '"':
            try:
                return json.loads(value)
            except ValueError as exc:
                raise ValueError("Unsupported quoted header syntax") from exc
        elif "'" in value[1:-1].replace("''", ""):
            raise ValueError("Unsupported quoted header syntax")
        return value[1:-1].replace("''", "'")
    if (value[0] in "&*!>|[{" or re.search(r"(?:\s#|:\s)", value)
            or any(c in value for c in "[]{}")):
        raise ValueError("Unsupported or ambiguous header syntax")
    return value


@dataclass(frozen=True)
class ParsedHeader:
    fields: dict[str, str]
    raw_header: str
    body: str
    editable_fields: tuple[str, ...]
    _lines: tuple[str, ...]
    _spans: dict[str, tuple[int, int]]

    def with_updates(self, updates: dict[str, str]) -> str:
        """Replace existing form-safe scalar fields; leave all other bytes alone."""
        if not isinstance(updates, dict):
            raise ValueError("Header updates must be a field mapping")
        lines = list(self._lines)
        for key, value in updates.items():
            if key not in self.editable_fields or not isinstance(value, str):
                raise ValueError("Field cannot be edited safely in the header form")
            if any(ord(c) < 32 for c in value):
                raise ValueError("Header form fields must be single-line text")
            start, _ = self._spans[key]
            ending = "\r\n" if lines[start].endswith("\r\n") else "\n" if lines[start].endswith("\n") else ""
            lines[start] = f"{key}: {json.dumps(value, ensure_ascii=False)}{ending}"
        result = "".join(lines) + self.body
        parse_frontmatter(result)
        return result


def parse_frontmatter(text: str) -> ParsedHeader:
    """Parse flat scalars, scalar lists, and one-level metadata maps strictly."""
    if not isinstance(text, str) or "\x00" in text:
        raise ValueError("Invalid header text")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError("Missing frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip("\r\n") == "---"), None)
    if end is None:
        raise ValueError("Unterminated frontmatter")
    fields, spans, shapes = {}, {}, {}
    current = None
    nested_keys = set()
    for i in range(1, end):
        line = lines[i].rstrip("\r\n")
        if not line.strip() or line.startswith("#"):
            continue
        if "\t" in line or any(ord(c) < 32 for c in line):
            raise ValueError("Unsupported header whitespace")
        if line.startswith(" ") or line.startswith("- "):
            if current is None:
                raise ValueError("Header continuation without a field")
            item = line.strip()
            if item.startswith("- ") and line in (item, "  " + item):
                shape = "list"
                item = "- " + _scalar(item[2:].strip())
            elif line == "  " + item and _KEY.fullmatch(item):
                shape = "mapping"
                if current in EDITABLE_FIELDS:
                    raise ValueError("Known header fields cannot contain nested mappings")
                match = _KEY.fullmatch(item)
                if match[1] in nested_keys:
                    raise ValueError("Duplicate nested header key")
                nested_keys.add(match[1])
                _scalar((match[2] or "").strip())
            else:
                raise ValueError("Unsupported or ambiguous header continuation")
            if ((fields[current] and shapes[current] == "scalar")
                    or shapes[current] not in ("scalar", shape)):
                raise ValueError("Mixed header field shapes")
            shapes[current] = shape
            fields[current] += " " + item
            spans[current] = (spans[current][0], i + 1)
            continue
        match = _KEY.fullmatch(line)
        if match is None:
            raise ValueError("Malformed header field")
        current, value = match[1], (match[2] or "").strip()
        if current in fields:
            raise ValueError("Duplicate header key")
        fields[current] = _scalar(value)
        shapes[current] = "scalar"
        spans[current] = (i, i + 1)
        nested_keys = set()
    editable = tuple(k for k in fields if k in EDITABLE_FIELDS and shapes[k] == "scalar")
    return ParsedHeader(fields, "".join(lines[:end + 1]), "".join(lines[end + 1:]),
                        editable, tuple(lines[:end + 1]), spans)
