"""Structural checks for the job description review skill."""

from pathlib import Path
import unittest


SKILL = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "job-description-review"
    / "SKILL.md"
)


class JobDescriptionReviewSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL.read_text(encoding="utf-8")
        cls.lower_content = cls.content.lower()

    def test_skill_has_required_metadata_and_a_clear_trigger_description(self):
        self.assertIn("---", self.content)
        self.assertIn("name: job-description-review", self.content)
        self.assertIn("description:", self.content)
        self.assertIn("job description", self.lower_content)
        self.assertIn("resume", self.lower_content)

    def test_workflow_uses_the_resume_and_covers_role_fit(self):
        self.assertIn("@src/data/resume.json", self.content)
        self.assertIn("specialized", self.lower_content)
        self.assertIn("qualified", self.lower_content)
        self.assertIn("evidence", self.lower_content)

    def test_qualified_candidate_gets_a_bounded_cover_letter(self):
        self.assertIn("coverletters", self.lower_content)
        self.assertIn("300 words", self.lower_content)

    def test_browser_workflow_uses_playwright_and_closes_the_browser(self):
        self.assertIn("playwright", self.lower_content)
        self.assertIn("close the browser", self.lower_content)


if __name__ == "__main__":
    unittest.main()
