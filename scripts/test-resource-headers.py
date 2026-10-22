"""Run with python infra/scripts/test-resource-headers.py; no client writes."""
import importlib.util
import json
import sys
import unittest
from pathlib import Path

from resource_headers import parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]


class ResourceHeaderTests(unittest.TestCase):
    def test_preserves_unknown_fields_comments_crlf_and_body(self):
        text = ('---\r\nname: demo\r\n# retained\r\ncustom: "opaque"\r\n'
                'metadata:\r\n  author: example\r\ndescription: old\r\n---\r\n\r\nBody\r\n')
        parsed = parse_frontmatter(text)
        self.assertEqual(parsed.raw_header + parsed.body, text)
        updated = parsed.with_updates({"description": "new: text"})
        self.assertEqual(updated, text.replace('description: old', 'description: "new: text"'))
        self.assertEqual(parse_frontmatter(updated).fields['description'], 'new: text')

    def test_legacy_list_values(self):
        text = '---\nname: demo\nskills:\n  - one\n  - two\n---\nbody'
        parsed = parse_frontmatter(text)
        self.assertEqual(parsed.fields['skills'], ' - one - two')
        self.assertNotIn('skills', parsed.editable_fields)
        with self.assertRaises(ValueError):
            parsed.with_updates({'skills': 'one'})

    def test_rejects_duplicates_even_unknown(self):
        for header in ('name: one\nname: two', 'unknown: one\nunknown: two',
                       'metadata:\n  author: one\n  author: two'):
            with self.subTest(header=header), self.assertRaises(ValueError):
                parse_frontmatter('---\n' + header + '\n---\n')

    def test_rejects_malformed_ambiguous_or_unsupported_headers(self):
        headers = ['name demo', ': empty', 'name: "unterminated', 'name: [a, b]',
                   'name: &anchor demo', 'description: a: b', 'description: hello # comment',
                   'description: |\n  multiline', '\tname: demo', 'name: demo\n  - unexpected',
                   'metadata:\n  author: one\n    nested: two', 'skills:\n  - one\n  key: two',
                   'name: "bad\\escape"', 'name: demo\n  stray continuation']
        for header in headers:
            with self.subTest(header=header), self.assertRaises(ValueError):
                parse_frontmatter('---\n' + header + '\n---\n')
        for text in ('body', '---\nname: demo', ' ---\nname: demo\n---'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_frontmatter(text)

    def test_form_cannot_inject_fields_or_change_unknown_fields(self):
        parsed = parse_frontmatter('---\nname: demo\nunknown: retained\n---\nbody')
        for updates in ({'name': 'demo\ntools: Agent'}, {'unknown': 'changed'}, {'name': None}):
            with self.subTest(updates=updates), self.assertRaises(ValueError):
                parsed.with_updates(updates)

    def test_quoted_scalars_decode_semantics_before_security_checks(self):
        parsed = parse_frontmatter('---\ntools: "Read, \\u0041gent"\ndescription: \'Owner\'\'s text\'\n---\n')
        self.assertEqual(parsed.fields['tools'], 'Read, Agent')
        self.assertEqual(parsed.fields['description'], "Owner's text")
        parsed = parse_frontmatter('---\ntools:\n  - Read\n  - "\\u0041gent"\n---\n')
        self.assertEqual(parsed.fields['tools'], ' - Read - Agent')
        literal = r'literal \"text\"'
        parsed = parse_frontmatter("---\ndescription: '" + literal + "'\n---\n")
        self.assertEqual(parsed.fields['description'], literal)
        with self.assertRaises(ValueError):
            parse_frontmatter('---\ntools:\n  allow: "\\u0041gent"\n---\n')

    def test_existing_agents_and_skills_keep_values_with_correct_quote_semantics(self):
        paths = [*ROOT.joinpath('agents').rglob('*.md'), *ROOT.joinpath('skills').glob('*/SKILL.md')]
        count = 0
        for path in paths:
            text = path.read_text(encoding='utf-8')
            if not text.startswith('---'):
                continue
            legacy, key = {}, None
            for line in text.splitlines()[1:]:
                if line.strip() == '---':
                    break
                if line[:1] in (' ', '\t') or line.startswith('-'):
                    if key:
                        legacy[key] += ' ' + line.strip()
                    continue
                key, _, value = line.partition(':')
                key, value = key.strip(), value.strip()
                if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                    value = json.loads(value) if value[0] == '"' else value[1:-1].replace("''", "'")
                legacy[key] = value
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(parse_frontmatter(text).fields, legacy)
            count += 1
        self.assertGreaterEqual(count, 60)

    def test_app_bridge_loads_canonical_parser(self):
        bridge = ROOT.parent / 'applications/workshop-ai/server/resource_headers.py'
        spec = importlib.util.spec_from_file_location('_header_bridge_test', bridge)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        parsed = module.parse_frontmatter(ROOT.parent, '---\nname: demo\n---\nbody')
        self.assertEqual(parsed.body, 'body')
        self.assertEqual(Path(sys.modules[type(parsed).__module__].__file__), ROOT / 'scripts/resource_headers.py')


if __name__ == '__main__':
    unittest.main()
