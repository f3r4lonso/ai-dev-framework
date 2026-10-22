"""Ownership and containment tests for the first-party resource copier."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("resource_sync", Path(__file__).with_name("sync-resources.py"))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class ResourceOwnershipTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.relative = ".agents/skills/sample/SKILL.md"
        self.first = {self.relative: b"reviewed source\n"}

    def apply(self, expected):
        writes, deletes = sync.plan_sync(self.root, expected)
        for path, data in writes:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for path in deletes:
            path.unlink()

    def test_repeat_install_has_no_writes(self):
        self.apply(self.first)
        self.assertEqual(sync.plan_sync(self.root, self.first), ([], []))

    def test_modified_managed_copy_is_preserved(self):
        self.apply(self.first)
        target = self.root / self.relative
        target.write_bytes(b"owner modification\n")
        with self.assertRaisesRegex(ValueError, "preserved"):
            sync.plan_sync(self.root, {self.relative: b"updated upstream\n"})
        self.assertEqual(target.read_bytes(), b"owner modification\n")

    def test_unowned_collision_is_preserved(self):
        target = self.root / self.relative
        target.parent.mkdir(parents=True)
        target.write_bytes(b"another skill\n")
        with self.assertRaisesRegex(ValueError, "preserved"):
            sync.plan_sync(self.root, self.first)
        self.assertFalse((self.root / sync.MANIFEST).exists())
        self.assertEqual(target.read_bytes(), b"another skill\n")

    def test_keep_existing_agents_does_not_claim_or_replace_them(self):
        relative = '.codex/agents/atlas.toml'
        target = self.root / relative
        target.parent.mkdir(parents=True)
        target.write_bytes(b'owner version')
        preserved = []
        expected = {**self.first, relative: b'canonical version'}
        writes, deletes = sync.plan_sync(self.root, expected, keep_existing_agents=True, preserved=preserved)
        self.assertEqual(preserved, [relative])
        self.assertNotIn(target, [path for path, _ in writes])
        metadata = json.loads(next(data for path, data in writes if path.name == 'resources.json'))
        self.assertNotIn(relative, metadata['files'])
        self.assertEqual(metadata['preserved_agents'], [relative])
        self.assertEqual(target.read_bytes(), b'owner version')
        self.assertEqual(deletes, [])

    def test_keep_existing_agents_still_stops_on_skill_collision(self):
        target = self.root / self.relative
        target.parent.mkdir(parents=True)
        target.write_bytes(b'owner skill')
        with self.assertRaisesRegex(ValueError, 'preserved'):
            sync.plan_sync(self.root, self.first, keep_existing_agents=True)

    def test_identical_existing_copy_can_be_adopted(self):
        target = self.root / self.relative
        target.parent.mkdir(parents=True)
        target.write_bytes(self.first[self.relative])
        writes, deletes = sync.plan_sync(self.root, self.first)
        self.assertEqual([p.name for p, _ in writes], ["resources.json"])
        self.assertEqual(deletes, [])

    def test_only_exact_known_legacy_profile_can_migrate(self):
        target = self.root / self.relative
        target.parent.mkdir(parents=True)
        target.write_bytes(b"known legacy output")
        writes, _ = sync.plan_sync(self.root, self.first, {self.relative: b"known legacy output"})
        self.assertIn(target, [path for path, _ in writes])
        target.write_bytes(b"GENERATED but modified")
        with self.assertRaisesRegex(ValueError, "preserved"):
            sync.plan_sync(self.root, self.first, {self.relative: b"known legacy output"})

    def test_retirement_only_removes_owned_unchanged_file(self):
        self.apply(self.first)
        other = self.root / ".agents/skills/personal/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_bytes(b"not managed")
        self.apply({})
        self.assertFalse((self.root / self.relative).exists())
        self.assertEqual(other.read_bytes(), b"not managed")

    def test_retirement_preserves_owner_changes(self):
        self.apply(self.first)
        target = self.root / self.relative
        target.write_bytes(b"owner change")
        with self.assertRaisesRegex(ValueError, "preserved"):
            sync.plan_sync(self.root, {})
        self.assertEqual(target.read_bytes(), b"owner change")

    def test_manifest_cannot_escape_or_target_other_files(self):
        for relative in (".agents/skills/../../outside.md", "AGENTS.md", ".codex/auth.json"):
            with self.subTest(relative=relative), self.assertRaises(ValueError):
                sync.safe_target(self.root, relative)

    def test_destination_link_is_refused(self):
        outside = self.root / "outside"
        outside.mkdir()
        try:
            (self.root / ".agents").symlink_to(outside, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"OS does not permit creating a test symlink: {error}")
        with self.assertRaisesRegex(ValueError, "linked destination"):
            sync.plan_sync(self.root, self.first)

    def test_manifest_cannot_claim_itself_for_retirement(self):
        target = self.root / sync.MANIFEST
        target.parent.mkdir()
        target.write_text(json.dumps({"schema": 1, "files": {sync.MANIFEST: "invalid"}}))
        with self.assertRaises(ValueError):
            sync.plan_sync(self.root, {})


if __name__ == "__main__":
    unittest.main()
