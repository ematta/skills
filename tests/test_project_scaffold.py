"""Structural checks for the multi-skill repository scaffold."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectScaffoldTests(unittest.TestCase):
    def test_readme_explains_how_skills_are_organized(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file())
        content = readme.read_text(encoding="utf-8").lower()
        self.assertIn("skills/", content)
        self.assertIn("skill.md", content)

    def test_skills_collection_contains_reusable_template(self):
        template = ROOT / "skills" / "_template" / "SKILL.md"
        self.assertTrue(template.is_file())
        content = template.read_text(encoding="utf-8")
        self.assertIn("name:", content)
        self.assertIn("description:", content)
        self.assertIn("# ", content)

    def test_template_identifies_its_placeholder_content(self):
        content = (ROOT / "skills" / "_template" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("TODO", content)


if __name__ == "__main__":
    unittest.main()
