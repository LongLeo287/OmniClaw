"""Progressive skill loading for analysis.

Inspired by DeerFlow: skills (analyzer prompts) are loaded on-demand
based on detected language/framework, not all at once.
Keeps context window lean and improves analysis quality.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class AnalysisSkill:
    """A single analysis skill/prompt."""

    name: str
    description: str
    languages: list[str] = field(default_factory=list)  # e.g., ["python", "javascript"]
    frameworks: list[str] = field(default_factory=list)  # e.g., ["django", "flask"]
    file_patterns: list[str] = field(default_factory=list)  # e.g., ["*.py", "*.js"]
    priority: int = 5  # 1=highest, 10=lowest

    def matches(self, language: str, frameworks_detected: set[str]) -> bool:
        """Check if this skill is relevant for given language/frameworks."""
        # Universal skills always match
        if not self.languages and not self.frameworks:
            return True

        # Language match
        if self.languages and language.lower() in [lang.lower() for lang in self.languages]:
            return True

        # Framework match
        if self.frameworks:
            return bool(frameworks_detected & {f.lower() for f in self.frameworks})

        return False


# ── Built-in Skill Registry ──────────────────────────────────────────────

SKILLS: list[AnalysisSkill] = [
    # Universal skills (always loaded)
    AnalysisSkill(
        name="security",
        description="Detect hardcoded secrets, SQL injection, XSS, command injection",
        priority=1,
    ),
    AnalysisSkill(
        name="code_quality",
        description="Find dead code, missing error handling, complexity issues",
        priority=2,
    ),
    # Language-specific skills
    AnalysisSkill(
        name="python_specific",
        description="Python antipatterns: mutable defaults, bare except, f-string issues",
        languages=["python"],
        priority=3,
    ),
    AnalysisSkill(
        name="javascript_specific",
        description="JS/TS issues: callback hell, promise misuse, prototype pollution",
        languages=["javascript", "typescript"],
        priority=3,
    ),
    AnalysisSkill(
        name="go_specific",
        description="Go issues: goroutine leaks, unchecked errors, defer in loops",
        languages=["go"],
        priority=3,
    ),
    AnalysisSkill(
        name="rust_specific",
        description="Rust: unwrap abuse, unnecessary clones, unsafe misuse",
        languages=["rust"],
        priority=3,
    ),
    AnalysisSkill(
        name="java_specific",
        description="Java: resource leaks, null handling, serialization issues",
        languages=["java", "kotlin"],
        priority=3,
    ),
    # Framework-specific skills
    AnalysisSkill(
        name="django_security",
        description="Django: CSRF, ORM injection, settings exposure, debug mode",
        languages=["python"],
        frameworks=["django"],
        priority=4,
    ),
    AnalysisSkill(
        name="flask_security",
        description="Flask: template injection, secret key exposure, debug mode",
        languages=["python"],
        frameworks=["flask"],
        priority=4,
    ),
    AnalysisSkill(
        name="fastapi_patterns",
        description="FastAPI: missing validation, sync in async, dependency injection",
        languages=["python"],
        frameworks=["fastapi"],
        priority=4,
    ),
    AnalysisSkill(
        name="react_patterns",
        description="React: key prop issues, effect dependencies, state management",
        languages=["javascript", "typescript"],
        frameworks=["react", "next"],
        priority=4,
    ),
    AnalysisSkill(
        name="express_security",
        description="Express: middleware ordering, CORS, helmet, rate limiting",
        languages=["javascript", "typescript"],
        frameworks=["express"],
        priority=4,
    ),
    # Low-priority skills (loaded only when relevant)
    AnalysisSkill(
        name="docs",
        description="Missing docstrings, incomplete READMEs, stale comments",
        priority=6,
    ),
    AnalysisSkill(
        name="ui_ux",
        description="Accessibility issues, responsive design gaps, WCAG violations",
        languages=["javascript", "typescript"],
        frameworks=["react", "vue", "svelte", "angular"],
        priority=7,
    ),
    AnalysisSkill(
        name="performance",
        description="String allocation, blocking calls, N+1 queries, memory leaks",
        priority=5,
    ),
    AnalysisSkill(
        name="refactor",
        description="Unused imports, non-null assertions, encoding issues",
        priority=8,
    ),
]


# ── Framework Detection ──────────────────────────────────────────────────

FRAMEWORK_INDICATORS: dict[str, list[str]] = {
    "django": ["settings.py", "urls.py", "manage.py", "wsgi.py", "asgi.py"],
    "flask": ["flask", "Flask(__name__)", "from flask"],
    "fastapi": ["fastapi", "FastAPI()", "from fastapi"],
    "express": ["express", "require('express')", "from 'express'"],
    "react": ["react", "React.", "jsx", "tsx", "package.json"],
    "next": ["next.config", "pages/", "app/", "next/"],
    "vue": [".vue", "Vue.", "createApp"],
    "svelte": [".svelte", "svelte.config"],
    "angular": ["angular.json", "@angular/"],
    "spring": ["pom.xml", "build.gradle", "@SpringBoot"],
    "rails": ["Gemfile", "config/routes.rb", "app/controllers"],
}


def detect_frameworks(
    file_paths: list[str], file_contents: dict[str, str] | None = None
) -> set[str]:
    """Detect frameworks from file tree and optionally file contents."""
    detected: set[str] = set()
    paths_lower = [p.lower() for p in file_paths]

    for framework, indicators in FRAMEWORK_INDICATORS.items():
        for indicator in indicators:
            ind_lower = indicator.lower()
            # Check file paths
            if any(ind_lower in p for p in paths_lower):
                detected.add(framework)
                break
            # Check file contents
            if file_contents:
                for content in file_contents.values():
                    if ind_lower in content.lower():
                        detected.add(framework)
                        break
                if framework in detected:
                    break

    return detected


def select_skills(
    language: str,
    frameworks: set[str],
    max_skills: int = 5,
) -> list[AnalysisSkill]:
    """Select relevant skills for the given language and frameworks.

    Returns at most `max_skills` skills, sorted by priority.
    """
    relevant = [s for s in SKILLS if s.matches(language, frameworks)]
    relevant.sort(key=lambda s: s.priority)
    selected = relevant[:max_skills]

    logger.info(
        "Selected %d/%d skills for %s (frameworks: %s): %s",
        len(selected),
        len(SKILLS),
        language,
        ", ".join(frameworks) or "none",
        ", ".join(s.name for s in selected),
    )
    return selected
