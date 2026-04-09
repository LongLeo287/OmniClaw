"""Tests for framework detection strategies."""

import pytest

from contribai.analysis.strategies import (
    DjangoStrategy,
    ExpressStrategy,
    FastAPIStrategy,
    FlaskStrategy,
    ReactStrategy,
    detect_frameworks,
)
from contribai.core.models import FileNode, RepoContext, Repository


@pytest.fixture
def base_repo():
    return Repository(owner="x", name="y", full_name="x/y", language="python")


class TestDjangoDetection:
    def test_detects_manage_py(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            file_tree=[FileNode(path="manage.py", type="blob", size=100, sha="a")],
        )
        strategy = DjangoStrategy()
        info = strategy.detect(ctx)
        assert info is not None
        assert info.name == "Django"

    def test_detects_from_requirements(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"requirements.txt": "Django==4.2\ncelery==5.3"},
        )
        info = DjangoStrategy().detect(ctx)
        assert info is not None

    def test_no_detection(self, base_repo):
        ctx = RepoContext(repo=base_repo)
        assert DjangoStrategy().detect(ctx) is None

    def test_critical_files(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            file_tree=[
                FileNode(path="app/views.py", type="blob", size=100, sha="a"),
                FileNode(path="app/models.py", type="blob", size=100, sha="b"),
                FileNode(path="README.md", type="blob", size=100, sha="c"),
            ],
        )
        files = DjangoStrategy().get_critical_files(ctx)
        assert "app/views.py" in files
        assert "app/models.py" in files
        assert "README.md" not in files


class TestFlaskDetection:
    def test_detects_import(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"app.py": "from flask import Flask\napp = Flask(__name__)"},
        )
        assert FlaskStrategy().detect(ctx) is not None

    def test_detects_from_requirements(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"requirements.txt": "flask==3.0\nflask-sqlalchemy"},
        )
        assert FlaskStrategy().detect(ctx) is not None


class TestFastAPIDetection:
    def test_detects_import(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"main.py": "from fastapi import FastAPI\napp = FastAPI()"},
        )
        assert FastAPIStrategy().detect(ctx) is not None


class TestReactDetection:
    def test_detects_from_package_json(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"package.json": '{"dependencies": {"react": "^18.0.0"}}'},
        )
        info = ReactStrategy().detect(ctx)
        assert info is not None
        assert info.name == "React"

    def test_detects_nextjs(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"package.json": '{"dependencies": {"next": "^14.0.0"}}'},
        )
        info = ReactStrategy().detect(ctx)
        assert info is not None
        assert info.name == "Next.js"

    def test_detects_tsx_files(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            file_tree=[FileNode(path="src/App.tsx", type="blob", size=100, sha="a")],
        )
        assert ReactStrategy().detect(ctx) is not None


class TestExpressDetection:
    def test_detects_from_package_json(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            relevant_files={"package.json": '{"dependencies": {"express": "^4.18"}}'},
        )
        assert ExpressStrategy().detect(ctx) is not None


class TestDetectFrameworks:
    def test_detects_multiple(self, base_repo):
        ctx = RepoContext(
            repo=base_repo,
            file_tree=[FileNode(path="manage.py", type="blob", size=100, sha="a")],
            relevant_files={"requirements.txt": "Django==4.2\nDjango-rest-framework"},
        )
        detected = detect_frameworks(ctx)
        assert len(detected) >= 1
        names = [info.name for _, info in detected]
        assert "Django" in names

    def test_empty_repo_no_detection(self, base_repo):
        ctx = RepoContext(repo=base_repo)
        detected = detect_frameworks(ctx)
        assert len(detected) == 0
