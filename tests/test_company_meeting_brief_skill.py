"""Structural checks for the company meeting brief skill."""

from pathlib import Path
import unittest


SKILL = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "company-meeting-brief"
    / "SKILL.md"
)


class CompanyMeetingBriefSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL.read_text(encoding="utf-8")
        cls.lower_content = cls.content.lower()

    def test_skill_has_required_metadata_and_company_research_trigger(self):
        self.assertIn("name: company-meeting-brief", self.content)
        self.assertIn("description:", self.content)
        self.assertIn("company", self.lower_content)
        self.assertIn("meeting", self.lower_content)

    def test_plan_gathers_and_checks_information_before_build(self):
        self.assertIn("plan", self.lower_content)
        self.assertIn("build", self.lower_content)
        self.assertIn("url", self.lower_content)
        self.assertIn("verify", self.lower_content)
        self.assertIn("do not create the html report", self.lower_content)

    def test_report_covers_company_products_and_meeting_context(self):
        self.assertIn("product", self.lower_content)
        self.assertIn("who they are", self.lower_content)
        self.assertIn("meeting", self.lower_content)

    def test_build_saves_cited_html_report_under_interviews(self):
        self.assertIn("interviews/", self.lower_content)
        self.assertIn("html", self.lower_content)
        self.assertIn("source", self.lower_content)

    def test_existing_interview_reports_are_used_as_patterns(self):
        self.assertIn("existing", self.lower_content)
        self.assertIn("pattern", self.lower_content)


if __name__ == "__main__":
    unittest.main()
