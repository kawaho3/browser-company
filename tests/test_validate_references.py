"""Fast, offline tests for the M0 repository-index validator."""

import tempfile
from pathlib import Path
import unittest

from scripts.validate_references import REQUIRED_DOCUMENTS, check


class ReferenceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in REQUIRED_DOCUMENTS:
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text("# Placeholder\n", encoding="utf-8")
        self.urls = [f"https://github.com/example/repo-{i}" for i in range(1, 19)]
        self.urls[0] = "https://github.com/chromium/chromium"
        self.urls[1] = "https://github.com/brave/brave-core"
        self.write_index()

    def write_index(self):
        content = "\n".join(
            f"{n:02d}. Repo {n}\n    URL: {url}\n    Purpose: test"
            for n, url in enumerate(self.urls, 1)
        )
        (self.root / "REPOSITORIES_TO_STUDY.txt").write_text(content, encoding="utf-8")

    def test_valid_inventory(self):
        self.assertEqual(check(self.root), [])

    def test_duplicate_repository(self):
        self.urls[17] = self.urls[16]
        self.write_index()
        self.assertTrue(any("Duplicate" in s for s in check(self.root)))

    def test_missing_foundation(self):
        self.urls[1] = "https://github.com/example/not-brave"
        self.write_index()
        self.assertTrue(any("foundation" in s for s in check(self.root)))

    def test_missing_document(self):
        (self.root / "docs/DECISIONS.md").unlink()
        self.assertTrue(any("DECISIONS" in s for s in check(self.root)))

    def test_missing_index(self):
        (self.root / "REPOSITORIES_TO_STUDY.txt").unlink()
        self.assertTrue(any("Missing REPOSITORIES" in s for s in check(self.root)))

    def test_nonsequential_entries(self):
        content = (self.root / "REPOSITORIES_TO_STUDY.txt").read_text(encoding="utf-8")
        (self.root / "REPOSITORIES_TO_STUDY.txt").write_text(content.replace("03. Repo", "19. Repo"), encoding="utf-8")
        self.assertTrue(any("sequential" in s for s in check(self.root)))


if __name__ == "__main__":
    unittest.main()
