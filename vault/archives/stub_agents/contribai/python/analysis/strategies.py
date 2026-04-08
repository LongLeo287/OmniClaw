"""Framework-specific analysis strategies.

Detects the framework used in a repository and applies
targeted analysis rules beyond general code analysis.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

from contribai.core.models import RepoContext

logger = logging.getLogger(__name__)


@dataclass
class FrameworkInfo:
    """Detected framework metadata."""

    name: str
    version: str | None = None
    config_file: str | None = None


class FrameworkStrategy(ABC):
    """Base class for framework-specific analysis."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Framework name."""

    @abstractmethod
    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        """Detect if this framework is used in the repo.

        Args:
            context: Repository context with file tree and contents.

        Returns:
            FrameworkInfo if detected, None otherwise.
        """

    @abstractmethod
    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        """Get framework-specific analysis prompt.

        Args:
            context: Repository context.
            info: Detected framework info.

        Returns:
            LLM prompt string for framework-specific analysis.
        """

    @abstractmethod
    def get_critical_files(self, context: RepoContext) -> list[str]:
        """Get framework-specific files that should be analyzed.

        Args:
            context: Repository context.

        Returns:
            List of file paths to prioritize for analysis.
        """


# ── Python Frameworks ──────────────────────────────────────────────────────


class DjangoStrategy(FrameworkStrategy):
    """Django web framework analysis."""

    @property
    def name(self) -> str:
        return "Django"

    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        for f in context.file_tree:
            if f.path.endswith("manage.py") or f.path.endswith("settings.py"):
                return FrameworkInfo(name="Django", config_file=f.path)
        # Check dependencies
        for path, content in context.relevant_files.items():
            if (
                "requirements" in path.lower() or path == "pyproject.toml"
            ) and "django" in content.lower():
                return FrameworkInfo(name="Django", config_file=path)
        return None

    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        return """Analyze this Django project for:
1. **Security**: CSRF protection, SQL injection in raw queries, DEBUG=True in production,
   SECRET_KEY exposure, missing ALLOWED_HOSTS, unsafe template rendering
2. **Best Practices**: Missing migrations, N+1 queries in views,
   missing `select_related`/`prefetch_related`,
   fat views (logic should be in models/services), hardcoded URLs instead of `reverse()`
3. **Common Issues**: Missing `__str__` on models, no admin registration, missing form validation,
   no error handling in views, missing pagination on list views
4. **Performance**: Unbounded querysets, missing database indexes, no caching on repeated queries"""

    def get_critical_files(self, context: RepoContext) -> list[str]:
        patterns = [
            "settings.py",
            "urls.py",
            "views.py",
            "models.py",
            "forms.py",
            "admin.py",
            "serializers.py",
        ]
        return [f.path for f in context.file_tree if any(f.path.endswith(p) for p in patterns)]


class FlaskStrategy(FrameworkStrategy):
    """Flask web framework analysis."""

    @property
    def name(self) -> str:
        return "Flask"

    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        for path, content in context.relevant_files.items():
            if "from flask" in content or "import flask" in content:
                return FrameworkInfo(name="Flask", config_file=path)
        for path, content in context.relevant_files.items():
            if "requirements" in path.lower() and "flask" in content.lower():
                return FrameworkInfo(name="Flask", config_file=path)
        return None

    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        return """Analyze this Flask project for:
1. **Security**: Missing CSRF protection, no input validation, SQL injection in raw queries,
   debug mode in production, SECRET_KEY exposure, missing rate limiting
2. **Best Practices**: Missing error handlers (404, 500), no blueprints for organization,
   no application factory pattern, hardcoded config values, no logging setup
3. **Common Issues**: Missing request validation, no JSON error responses for API routes,
   synchronous blocking calls, missing CORS configuration
4. **Performance**: No connection pooling, missing caching, large file uploads without streaming"""

    def get_critical_files(self, context: RepoContext) -> list[str]:
        patterns = ["app.py", "wsgi.py", "config.py", "routes.py", "__init__.py"]
        return [f.path for f in context.file_tree if any(f.path.endswith(p) for p in patterns)]


class FastAPIStrategy(FrameworkStrategy):
    """FastAPI framework analysis."""

    @property
    def name(self) -> str:
        return "FastAPI"

    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        for path, content in context.relevant_files.items():
            if "from fastapi" in content or "import fastapi" in content:
                return FrameworkInfo(name="FastAPI", config_file=path)
        return None

    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        return """Analyze this FastAPI project for:
1. **Security**: Missing authentication dependencies, no input validation beyond Pydantic,
   CORS misconfiguration, missing rate limiting, exposed debug endpoints
2. **Best Practices**: Missing response models, no dependency injection pattern,
   sync endpoints that should be async, missing OpenAPI metadata,
   no error handler middleware, hardcoded status codes
3. **Common Issues**: Missing Depends() for shared logic, no background tasks for heavy work,
   missing health check endpoint, no request/response logging middleware
4. **Performance**: Missing async database driver, no connection pooling,
   blocking I/O in async endpoints, missing response caching"""

    def get_critical_files(self, context: RepoContext) -> list[str]:
        patterns = ["main.py", "app.py", "routers/", "dependencies.py", "schemas.py", "models.py"]
        return [f.path for f in context.file_tree if any(p in f.path for p in patterns)]


# ── JavaScript Frameworks ──────────────────────────────────────────────────


class ReactStrategy(FrameworkStrategy):
    """React/Next.js framework analysis."""

    @property
    def name(self) -> str:
        return "React"

    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        for path, content in context.relevant_files.items():
            if path == "package.json" and ('"react"' in content or '"next"' in content):
                name = "Next.js" if '"next"' in content else "React"
                return FrameworkInfo(name=name, config_file=path)
        for f in context.file_tree:
            if f.path.endswith(".jsx") or f.path.endswith(".tsx"):
                return FrameworkInfo(name="React")
        return None

    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        extra = ""
        if info.name == "Next.js":
            extra = """
5. **Next.js Specific**: Missing metadata/SEO, no loading.tsx for suspense,
   'use client' on server-renderable components, no error.tsx,
   fetching in useEffect instead of server components"""

        return f"""Analyze this {info.name} project for:
1. **Security**: XSS via dangerouslySetInnerHTML, missing input sanitization,
   exposed API keys in client code, insecure localStorage usage
2. **Performance**: Missing React.memo on heavy components, no useMemo/useCallback,
   prop drilling instead of context, missing lazy loading, no code splitting
3. **Accessibility**: Missing alt text, no ARIA labels, missing keyboard navigation,
   no semantic HTML, missing skip-to-content link
4. **Best Practices**: Missing PropTypes/TypeScript types, no error boundaries,
   unstable keys in lists, state management anti-patterns{extra}"""

    def get_critical_files(self, context: RepoContext) -> list[str]:
        patterns = [".jsx", ".tsx", "App.", "index.", "layout.", "page.", "package.json"]
        return [f.path for f in context.file_tree if any(p in f.path for p in patterns)][:20]


class ExpressStrategy(FrameworkStrategy):
    """Express.js framework analysis."""

    @property
    def name(self) -> str:
        return "Express"

    def detect(self, context: RepoContext) -> FrameworkInfo | None:
        for path, content in context.relevant_files.items():
            if path == "package.json" and '"express"' in content:
                return FrameworkInfo(name="Express", config_file=path)
            if "require('express')" in content or 'from "express"' in content:
                return FrameworkInfo(name="Express", config_file=path)
        return None

    def get_analysis_prompt(self, context: RepoContext, info: FrameworkInfo) -> str:
        return """Analyze this Express.js project for:
1. **Security**: Missing helmet middleware, no rate limiting, CORS misconfiguration,
   SQL/NoSQL injection in user inputs, missing input validation, no CSRF protection
2. **Best Practices**: No error handling middleware, missing async/await error handling,
   hardcoded port numbers, no environment variable validation, missing health endpoint
3. **Common Issues**: Callback hell, no request validation (use Joi/Zod), missing logging,
   no graceful shutdown handler, unhandled promise rejections
4. **Performance**: No compression middleware, missing caching headers,
   synchronous file operations, no connection pooling for database"""

    def get_critical_files(self, context: RepoContext) -> list[str]:
        patterns = ["app.js", "server.js", "index.js", "routes/", "middleware/", "package.json"]
        return [f.path for f in context.file_tree if any(p in f.path for p in patterns)][:15]


# ── Strategy Registry ──────────────────────────────────────────────────────

ALL_STRATEGIES: list[type[FrameworkStrategy]] = [
    DjangoStrategy,
    FlaskStrategy,
    FastAPIStrategy,
    ReactStrategy,
    ExpressStrategy,
]


def detect_frameworks(context: RepoContext) -> list[tuple[FrameworkStrategy, FrameworkInfo]]:
    """Detect all frameworks used in a repository.

    Args:
        context: Repository context with file tree and contents.

    Returns:
        List of (strategy, info) tuples for detected frameworks.
    """
    detected = []
    for strategy_cls in ALL_STRATEGIES:
        strategy = strategy_cls()
        info = strategy.detect(context)
        if info:
            logger.info("Detected framework: %s", info.name)
            detected.append((strategy, info))
    return detected
