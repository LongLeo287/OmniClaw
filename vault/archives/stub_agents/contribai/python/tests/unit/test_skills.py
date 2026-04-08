"""Tests for contribai.analysis.skills — Progressive skill loading."""

from __future__ import annotations

from contribai.analysis.skills import (
    SKILLS,
    AnalysisSkill,
    detect_frameworks,
    select_skills,
)


class TestAnalysisSkill:
    """Tests for AnalysisSkill dataclass."""

    def test_create(self):
        skill = AnalysisSkill(
            name="test_skill",
            description="Find issues",
            languages=["python"],
            frameworks=[],
            priority=1,
        )
        assert skill.name == "test_skill"
        assert skill.description == "Find issues"
        assert skill.priority == 1

    def test_matches_language(self):
        skill = AnalysisSkill(
            name="py_skill",
            description="test",
            languages=["Python"],
            priority=5,
        )
        assert skill.matches("Python", set()) is True
        assert skill.matches("python", set()) is True  # case insensitive
        assert skill.matches("JavaScript", set()) is False

    def test_matches_framework(self):
        skill = AnalysisSkill(
            name="django_skill",
            description="test",
            frameworks=["django"],
            priority=2,
        )
        assert skill.matches("Python", {"django"}) is True
        assert skill.matches("Python", {"flask"}) is False

    def test_matches_universal(self):
        """Skills with no language/framework match everything."""
        skill = AnalysisSkill(
            name="universal",
            description="test",
            priority=1,
        )
        assert skill.matches("Python", set()) is True
        assert skill.matches("Go", {"gin"}) is True


class TestBuiltinSkills:
    """Tests for SKILLS registry."""

    def test_has_skills(self):
        assert isinstance(SKILLS, list)
        assert len(SKILLS) > 0

    def test_all_have_names(self):
        for skill in SKILLS:
            assert skill.name
            assert skill.description

    def test_has_security(self):
        names = [s.name for s in SKILLS]
        assert "security" in names

    def test_has_python_skill(self):
        py_skills = [
            s for s in SKILLS if "python" in [lang.lower() for lang in (s.languages or [])]
        ]
        assert len(py_skills) >= 1

    def test_has_django_skill(self):
        names = [s.name for s in SKILLS]
        assert "django_security" in names

    def test_priorities_are_set(self):
        for skill in SKILLS:
            assert 1 <= skill.priority <= 10


class TestDetectFrameworks:
    """Tests for framework detection."""

    def test_detect_django(self):
        files = ["manage.py", "settings.py", "urls.py", "views.py"]
        detected = detect_frameworks(files)
        assert "django" in detected

    def test_detect_flask(self):
        files = ["app.py", "requirements.txt"]
        contents = {"requirements.txt": "flask==2.0\ngunicorn"}
        detected = detect_frameworks(files, contents)
        assert "flask" in detected

    def test_detect_fastapi(self):
        files = ["main.py", "requirements.txt"]
        contents = {"requirements.txt": "fastapi\nuvicorn"}
        detected = detect_frameworks(files, contents)
        assert "fastapi" in detected

    def test_detect_react(self):
        files = ["package.json", "src/App.tsx", "src/index.tsx"]
        contents = {"package.json": '{"dependencies": {"react": "^18"}}'}
        detected = detect_frameworks(files, contents)
        assert "react" in detected

    def test_detect_express(self):
        files = ["package.json", "server.js"]
        contents = {"package.json": '{"dependencies": {"express": "^4"}}'}
        detected = detect_frameworks(files, contents)
        assert "express" in detected

    def test_empty_files(self):
        detected = detect_frameworks([])
        assert detected == set()

    def test_no_detection(self):
        files = ["README.md", "LICENSE"]
        detected = detect_frameworks(files)
        assert detected == set()

    def test_returns_set(self):
        detected = detect_frameworks(["manage.py"])
        assert isinstance(detected, set)


class TestSelectSkills:
    """Tests for select_skills."""

    def test_selects_for_python(self):
        selected = select_skills("Python", set())
        assert len(selected) > 0
        for s in selected:
            assert s.matches("Python", set())

    def test_selects_for_django(self):
        selected = select_skills("Python", {"django"})
        names = [s.name for s in selected]
        assert "django_security" in names

    def test_selects_for_javascript(self):
        selected = select_skills("JavaScript", set())
        assert len(selected) > 0

    def test_max_skills(self):
        selected = select_skills("Python", {"django", "flask", "fastapi"}, max_skills=3)
        assert len(selected) <= 3

    def test_sorted_by_priority(self):
        selected = select_skills("Python", set())
        priorities = [s.priority for s in selected]
        assert priorities == sorted(priorities)

    def test_universal_skills_always_included(self):
        """Security + code_quality are universal and should always appear."""
        selected = select_skills("Go", set(), max_skills=10)
        names = [s.name for s in selected]
        assert "security" in names
        assert "code_quality" in names
