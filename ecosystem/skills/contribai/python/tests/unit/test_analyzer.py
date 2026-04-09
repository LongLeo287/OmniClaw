"""Tests for the code analysis engine."""

import pytest

from contribai.analysis.analyzer import ANALYZABLE_EXTENSIONS, CodeAnalyzer
from contribai.core.config import AnalysisConfig
from contribai.core.models import (
    ContributionType,
    FileNode,
    Finding,
    RepoContext,
    Severity,
)


@pytest.fixture
def analyzer(mock_llm, mock_github):
    config = AnalysisConfig(
        enabled_analyzers=["security", "code_quality"],
        severity_threshold="medium",
    )
    return CodeAnalyzer(llm=mock_llm, github=mock_github, config=config)


@pytest.fixture
def sample_tree():
    return [
        FileNode(path="README.md", type="blob", size=1024, sha="a"),
        FileNode(path="src/main.py", type="blob", size=2048, sha="b"),
        FileNode(path="src/utils.py", type="blob", size=512, sha="c"),
        FileNode(path="src/app.min.js", type="blob", size=50000, sha="d"),
        FileNode(path="node_modules/pkg/index.js", type="blob", size=100, sha="e"),
        FileNode(path="images/logo.png", type="blob", size=5000, sha="f"),
        FileNode(path="src", type="tree", size=0, sha="g"),
    ]


class TestSelectFiles:
    def test_selects_analyzable_files(self, analyzer, sample_tree):
        selected = analyzer._select_files(sample_tree)
        paths = [f.path for f in selected]
        assert "src/main.py" in paths
        assert "src/utils.py" in paths
        assert "README.md" in paths

    def test_skips_minified(self, analyzer, sample_tree):
        selected = analyzer._select_files(sample_tree)
        paths = [f.path for f in selected]
        assert "src/app.min.js" not in paths

    def test_skips_node_modules(self, analyzer, sample_tree):
        selected = analyzer._select_files(sample_tree)
        paths = [f.path for f in selected]
        assert "node_modules/pkg/index.js" not in paths

    def test_skips_binary_files(self, analyzer, sample_tree):
        selected = analyzer._select_files(sample_tree)
        paths = [f.path for f in selected]
        assert "images/logo.png" not in paths

    def test_skips_tree_nodes(self, analyzer, sample_tree):
        selected = analyzer._select_files(sample_tree)
        paths = [f.path for f in selected]
        assert "src" not in paths

    def test_skips_oversized_files(self, analyzer):
        tree = [FileNode(path="big.py", type="blob", size=1_000_000, sha="x")]
        selected = analyzer._select_files(tree)
        assert len(selected) == 0


class TestPrioritizeFiles:
    def test_main_files_first(self, analyzer):
        files = [
            FileNode(path="utils.py", type="blob", size=100, sha="a"),
            FileNode(path="main.py", type="blob", size=100, sha="b"),
            FileNode(path="setup.py", type="blob", size=100, sha="c"),
        ]
        result = analyzer._prioritize_files(files)
        assert result[0].path == "main.py"

    def test_config_files_prioritized(self, analyzer):
        files = [
            FileNode(path="random.py", type="blob", size=100, sha="a"),
            FileNode(path="config.py", type="blob", size=100, sha="b"),
        ]
        result = analyzer._prioritize_files(files)
        assert result[0].path == "config.py"


class TestDeduplicate:
    def test_removes_duplicates(self, analyzer):
        findings = [
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="Hardcoded secret",
                description="Found API key",
                file_path="config.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="Hardcoded secret",
                description="Found API key duplicate",
                file_path="config.py",
            ),
        ]
        result = analyzer._deduplicate(findings)
        assert len(result) == 1

    def test_keeps_different_findings(self, analyzer):
        findings = [
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="Issue A",
                description="",
                file_path="a.py",
            ),
            Finding(
                type=ContributionType.CODE_QUALITY,
                severity=Severity.MEDIUM,
                title="Issue B",
                description="",
                file_path="b.py",
            ),
        ]
        result = analyzer._deduplicate(findings)
        assert len(result) == 2


class TestFilterSeverity:
    def test_filters_below_threshold(self, analyzer):
        findings = [
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.LOW,
                title="Low",
                description="",
                file_path="a.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.MEDIUM,
                title="Medium",
                description="",
                file_path="b.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="High",
                description="",
                file_path="c.py",
            ),
        ]
        result = analyzer._filter_severity(findings)
        assert len(result) == 2  # medium threshold: medium + high
        titles = [f.title for f in result]
        assert "Low" not in titles


class TestParseFindingsYAML:
    def test_parse_yaml_response(self, analyzer, sample_repo):
        response = """```yaml
findings:
  - title: Hardcoded secret
    severity: high
    file_path: config.py
    line_start: 42
    description: API key is hardcoded
    suggestion: Use env vars
```"""
        ctx = RepoContext(repo=sample_repo)
        findings = analyzer._parse_findings(response, "security", ctx)
        assert len(findings) == 1
        assert findings[0].title == "Hardcoded secret"
        assert findings[0].severity == Severity.HIGH

    def test_parse_empty_response(self, analyzer, sample_repo):
        ctx = RepoContext(repo=sample_repo)
        findings = analyzer._parse_findings("findings: []", "security", ctx)
        assert len(findings) == 0

    def test_parse_invalid_yaml(self, analyzer, sample_repo):
        ctx = RepoContext(repo=sample_repo)
        findings = analyzer._parse_findings("not valid yaml {{{", "security", ctx)
        assert len(findings) == 0


class TestAnalyzableExtensions:
    def test_python_is_analyzable(self):
        assert ".py" in ANALYZABLE_EXTENSIONS

    def test_javascript_is_analyzable(self):
        assert ".js" in ANALYZABLE_EXTENSIONS

    def test_png_is_not_analyzable(self):
        assert ".png" not in ANALYZABLE_EXTENSIONS
