"""Main code analysis orchestrator.

Runs multiple analyzers (security, code quality, docs, UI/UX) in parallel
using LLM-powered analysis. Each analyzer examines the repo through
a different lens and returns findings.
"""

from __future__ import annotations

import asyncio
import contextlib
import logging
import time
import uuid
from fnmatch import fnmatch

from contribai.analysis.context_compressor import ContextCompressor
from contribai.core.config import AnalysisConfig
from contribai.core.models import (
    AnalysisResult,
    ContributionType,
    FileNode,
    Finding,
    RepoContext,
    Repository,
    Severity,
)
from contribai.github.client import GitHubClient
from contribai.llm.provider import LLMProvider

logger = logging.getLogger(__name__)

# File extensions we can meaningfully analyze
ANALYZABLE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".go",
    ".rs",
    ".rb",
    ".php",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".swift",
    ".kt",
    ".html",
    ".css",
    ".scss",
    ".vue",
    ".svelte",
    ".md",
    ".rst",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
}


class CodeAnalyzer:
    """Orchestrates multiple code analyzers using LLM."""

    def __init__(
        self,
        llm: LLMProvider,
        github: GitHubClient,
        config: AnalysisConfig,
    ):
        self._llm = llm
        self._github = github
        self._config = config
        self._compressor = ContextCompressor(
            max_context_tokens=getattr(config, "max_context_tokens", 30_000)
        )

    async def analyze(self, repo: Repository) -> AnalysisResult:
        """Run full analysis on a repository.

        1. Fetch file tree
        2. Select files to analyze
        3. Run enabled analyzers in parallel
        4. Aggregate and deduplicate findings
        """
        start = time.monotonic()

        # Fetch file tree
        file_tree = await self._github.get_file_tree(repo.owner, repo.name)
        analyzable = self._select_files(file_tree)

        logger.info(
            "Analyzing %s: %d/%d files selected",
            repo.full_name,
            len(analyzable),
            len(file_tree),
        )

        # Build repo context
        context = await self._build_context(repo, file_tree, analyzable)

        # Run enabled analyzers
        all_findings: list[Finding] = []
        analyzer_tasks = []

        for analyzer_name in self._config.enabled_analyzers:
            analyzer_tasks.append(self._run_analyzer(analyzer_name, context))

        results = await asyncio.gather(*analyzer_tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                logger.error("Analyzer failed: %s", result)
            elif isinstance(result, list):
                all_findings.extend(result)

        # Deduplicate
        findings = self._deduplicate(all_findings)

        # Filter by severity threshold
        findings = self._filter_severity(findings)

        # Build context summary for downstream consumers
        context_summary = self.summarize_findings(findings)
        logger.info(
            "Analysis of %s complete — %d findings. Summary: %s",
            repo.full_name,
            len(findings),
            context_summary[:100],
        )

        duration = time.monotonic() - start
        return AnalysisResult(
            repo=repo,
            findings=findings,
            analyzed_files=len(analyzable),
            skipped_files=len(file_tree) - len(analyzable),
            analysis_duration_sec=round(duration, 2),
        )

    @staticmethod
    def summarize_findings(findings: list[Finding]) -> str:
        """Compress findings into a concise summary.

        Inspired by DeerFlow's context engineering: summarize completed
        sub-tasks to preserve context window for subsequent processing.

        Returns a compact string suitable for injection into LLM prompts.
        """
        if not findings:
            return "No issues found."

        # Group by type
        by_type: dict[str, list[str]] = {}
        for f in findings:
            key = f.type.value if hasattr(f.type, "value") else str(f.type)
            by_type.setdefault(key, []).append(f.title)

        parts = []
        for ftype, titles in by_type.items():
            if len(titles) <= 2:
                parts.append(f"- {ftype}: {'; '.join(titles)}")
            else:
                parts.append(f"- {ftype}: {titles[0]}; {titles[1]}; +{len(titles) - 2} more")

        severity_counts = {}
        for f in findings:
            sev = f.severity.value if hasattr(f.severity, "value") else str(f.severity)
            severity_counts[sev] = severity_counts.get(sev, 0) + 1

        sev_str = ", ".join(f"{s}: {c}" for s, c in sorted(severity_counts.items()))
        return f"{len(findings)} findings ({sev_str}):\n" + "\n".join(parts)

    def _select_files(self, tree: list[FileNode]) -> list[FileNode]:
        """Select files suitable for analysis."""
        selected: list[FileNode] = []
        for node in tree:
            if node.type != "blob":
                continue

            # Check extension
            ext = "." + node.path.rsplit(".", 1)[-1] if "." in node.path else ""
            if ext.lower() not in ANALYZABLE_EXTENSIONS:
                continue

            # Check skip patterns
            if any(fnmatch(node.path, pat) for pat in self._config.skip_patterns):
                continue

            # Check file size
            if node.size > self._config.max_file_size_kb * 1024:
                continue

            selected.append(node)

        return selected

    async def _build_context(
        self,
        repo: Repository,
        tree: list[FileNode],
        analyzable: list[FileNode],
    ) -> RepoContext:
        """Build repository context for LLM analysis."""
        # Fetch key files
        readme = None
        contributing = None
        relevant_files: dict[str, str] = {}

        with contextlib.suppress(Exception):
            readme = await self._github.get_file_content(repo.owner, repo.name, "README.md")

        with contextlib.suppress(Exception):
            contributing = await self._github.get_contributing_guide(repo.owner, repo.name)

        # Fetch a sample of source files (up to 15 most important)
        priority_files = self._prioritize_files(analyzable, tree)[:15]
        for node in priority_files:
            try:
                content = await self._github.get_file_content(repo.owner, repo.name, node.path)
                relevant_files[node.path] = content
            except Exception as e:
                logger.debug("Failed to fetch %s: %s", node.path, e)

        # Detect project profile and style
        profile = self._detect_project_profile(repo, tree, readme)
        style_guide = self._build_style_guide(relevant_files)
        coding_style = f"PROJECT PROFILE:\n{profile}\n\nSTYLE GUIDE:\n{style_guide}"

        # Compress files to fit within token budget
        compressed_files = self._compressor.compress_files(relevant_files)
        if len(compressed_files) < len(relevant_files):
            logger.info(
                "📦 Compressed context: %d → %d files",
                len(relevant_files),
                len(compressed_files),
            )

        return RepoContext(
            repo=repo,
            file_tree=tree,
            readme_content=readme,
            contributing_guide=contributing,
            relevant_files=compressed_files,
            coding_style=coding_style,
        )

    def _detect_project_profile(
        self,
        repo: Repository,
        tree: list[FileNode],
        readme: str | None,
    ) -> str:
        """Detect project type, tech stack, and conventions from file tree.

        Returns a concise profile string that helps LLM understand the codebase.
        """
        paths = {n.path.lower() for n in tree}
        names = {n.path.rsplit("/", 1)[-1].lower() for n in tree}

        # Detect project type
        project_type = "library"
        if any(f in names for f in ("manage.py", "wsgi.py", "asgi.py")):
            project_type = "web_app"
        elif any(f in names for f in ("server.py", "api.py", "routes.py", "app.py")):
            project_type = "api_server"
        elif any(f in names for f in ("main.py", "__main__.py", "cli.py")):
            if any("click" in p or "argparse" in p or "typer" in p for p in paths):
                project_type = "cli_tool"
        elif any(f in names for f in ("pipeline.py", "dag.py", "etl.py")):
            project_type = "data_pipeline"

        # Detect tech stack
        stack: list[str] = []
        stack_markers = {
            "django": ["manage.py", "settings.py", "urls.py"],
            "flask": ["flask"],
            "fastapi": ["fastapi"],
            "sqlalchemy": ["models.py", "alembic"],
            "react": ["package.json", "jsx", "tsx"],
            "pytest": ["conftest.py", "pytest.ini"],
            "celery": ["celery.py", "tasks.py"],
            "docker": ["dockerfile", "docker-compose.yml"],
        }
        for tech, markers in stack_markers.items():
            if any(m in p for p in paths for m in markers):
                stack.append(tech)

        # Detect conventions
        has_tests = any("test" in p for p in paths)
        has_ci = any(
            f in p for p in paths for f in (".github/workflows", ".gitlab-ci", "Jenkinsfile")
        )
        has_types = any("py.typed" in p or "types" in p for p in paths)
        has_docs = any(f in p for p in paths for f in ("docs/", "doc/", "sphinx"))

        return (
            f"Type: {project_type}\n"
            f"Language: {repo.language or 'unknown'}\n"
            f"Stack: {', '.join(stack) if stack else 'minimal'}\n"
            f"Tests: {'yes' if has_tests else 'no'}\n"
            f"CI: {'yes' if has_ci else 'no'}\n"
            f"Type hints: {'yes' if has_types else 'unknown'}\n"
            f"Docs: {'yes' if has_docs else 'minimal'}"
        )

    def _build_style_guide(self, files: dict[str, str]) -> str:
        """Extract coding conventions from sample files.

        Examines actual code to detect naming, error handling, and import patterns.
        Returns a concise style guide string.
        """
        if not files:
            return "No source files available for style detection."

        # Sample up to 3 Python files for style detection
        py_files = [(p, c) for p, c in files.items() if p.endswith(".py") and len(c) > 100][:3]
        if not py_files:
            # Try other languages
            code_files = [
                (p, c)
                for p, c in files.items()
                if any(p.endswith(e) for e in (".js", ".ts", ".go", ".rs")) and len(c) > 100
            ][:3]
            if not code_files:
                return "Could not detect style — no substantial source files."
            py_files = code_files

        # Analyze patterns
        conventions: list[str] = []
        all_code = "\n".join(c for _, c in py_files)

        # Naming convention
        if "snake_case" not in all_code and "camelCase" not in all_code:
            import re

            func_names = re.findall(r"def (\w+)", all_code)
            if func_names:
                snake = sum(1 for n in func_names if "_" in n)
                camel = sum(1 for n in func_names if n != n.lower() and "_" not in n)
                conventions.append(f"Naming: {'snake_case' if snake > camel else 'camelCase'}")

        # Error handling style
        if "raise" in all_code and "except" in all_code:
            conventions.append("Errors: try/except with raise")
        elif "Result" in all_code or "Ok(" in all_code:
            conventions.append("Errors: Result type pattern")

        # Docstring format
        if '"""' in all_code:
            if "Args:" in all_code:
                conventions.append("Docstrings: Google style")
            elif "Parameters" in all_code and "---" in all_code:
                conventions.append("Docstrings: NumPy style")
            elif ":param" in all_code:
                conventions.append("Docstrings: Sphinx style")
            else:
                conventions.append("Docstrings: simple/minimal")
        else:
            conventions.append("Docstrings: rare/none")

        # Import style
        import re

        abs_imports = len(re.findall(r"^from \w+\.\w+", all_code, re.MULTILINE))
        rel_imports = len(re.findall(r"^from \.", all_code, re.MULTILINE))
        if abs_imports + rel_imports > 0:
            conventions.append(
                f"Imports: {'absolute' if abs_imports > rel_imports else 'relative'}"
            )

        # Logging
        if "logger" in all_code or "logging" in all_code:
            conventions.append("Logging: stdlib logging")
        elif "print(" in all_code:
            conventions.append("Logging: print statements")

        return "\n".join(conventions) if conventions else "Standard conventions"

    def _prioritize_files(
        self,
        files: list[FileNode],
        tree: list[FileNode] | None = None,
    ) -> list[FileNode]:
        """Prioritize files for analysis by contribution value.

        Scores files based on:
        - Core logic (not tests, vendored, generated, or configs)
        - Size (medium-sized files are most useful)
        - Location (shallow = more important)
        """
        # Dirs/patterns that indicate low-value files
        skip_prefixes = (
            "test",
            "tests",
            "spec",
            "__pycache__",
            "node_modules",
            "vendor",
            "dist",
            "build",
            ".git",
            "migrations",
            "generated",
            "proto",
            "stubs",
        )

        def file_score(node: FileNode) -> float:
            path = node.path.lower()
            name = path.rsplit("/", 1)[-1]
            score = 50.0  # base score

            # Boost entry points and core files
            if name in ("main.py", "app.py", "server.py", "cli.py", "__main__.py"):
                score += 40
            elif name in ("api.py", "routes.py", "views.py", "handlers.py"):
                score += 35
            elif any(k in name for k in ("auth", "security", "middleware", "utils")):
                score += 30
            elif name in ("models.py", "schema.py", "types.py"):
                score += 25
            elif any(k in name for k in ("config", "settings")):
                score += 20

            # Penalize low-value files
            parts = path.split("/")
            if any(p.startswith(s) for p in parts for s in skip_prefixes):
                score -= 60
            if name.startswith("test_") or name.endswith("_test.py"):
                score -= 50
            if name in ("__init__.py", "conftest.py", "setup.py"):
                score -= 20

            # Prefer medium-sized files (200-2000 bytes = sweet spot)
            if 200 <= node.size <= 2000:
                score += 10
            elif node.size > 10000:
                score -= 5  # very large files are harder to analyze

            # Prefer shallow paths (core modules, not deeply nested)
            depth = len(parts)
            if depth <= 2:
                score += 15
            elif depth >= 5:
                score -= 10

            return score

        return sorted(files, key=file_score, reverse=True)

    async def _run_analyzer(self, name: str, context: RepoContext) -> list[Finding]:
        """Run a single LLM-powered analyzer."""
        prompts = {
            "security": self._security_prompt,
            "code_quality": self._code_quality_prompt,
            "docs": self._docs_prompt,
            "ui_ux": self._ui_ux_prompt,
            "performance": self._performance_prompt,
            "refactor": self._refactor_prompt,
            "testing": self._testing_prompt,
        }

        prompt_fn = prompts.get(name)
        if not prompt_fn:
            logger.warning("Unknown analyzer: %s", name)
            return []

        prompt = prompt_fn(context)

        # Build context-aware system prompt with project profile
        profile_ctx = ""
        if context.coding_style:
            profile_ctx = (
                f"\n\nCODEBASE CONTEXT (use this to calibrate your analysis):\n"
                f"{context.coding_style}\n\n"
                f"IMPORTANT: Only report issues relevant to this type of project. "
                f"Skip issues that don't apply to the detected stack/type.\n"
            )

        # v4.0: Inject repo intelligence + PR history if available
        repo_intel_ctx = getattr(context, "_repo_intel_context", "")
        if repo_intel_ctx:
            profile_ctx += f"\n{repo_intel_ctx}\n"

        system = (
            "You are a senior software engineer performing a focused code review. "
            "You have deep expertise in real-world codebases and know which issues "
            "actually matter vs which are noise.\n\n"
            "For each finding, provide:\n"
            "- title: short descriptive title (be specific, not generic)\n"
            "- severity: low|medium|high|critical\n"
            "- file_path: path to the affected file\n"
            "- line_start: approximate line number (or 0 if unknown)\n"
            "- description: explain WHY this is a problem with concrete impact\n"
            "- suggestion: exact code-level fix (not vague advice)\n\n"
            "Return findings as a YAML list. If no issues found, return 'findings: []'.\n\n"
            f"{profile_ctx}"
            "ANTI-FALSE-POSITIVE RULES (mandatory checks before reporting):\n"
            "1. ALREADY HANDLED — Is the code already protected by try/except, "
            "guards, or fallback patterns? If yes, do NOT report.\n"
            "2. BY DESIGN — Is the pattern intentional? (e.g., bare except in a "
            "daemon, hardcoded values in test fixtures). If yes, do NOT report.\n"
            "3. BOUNDED CONTEXT — Does the call chain guarantee safety? "
            "(e.g., dict access after `if key in dict`). If yes, do NOT report.\n"
            "4. TRIVIAL FIX — Would the fix add complexity without real benefit? "
            "(e.g., adding type hints to a 10-line script). If yes, do NOT report.\n"
            "5. COSMETIC — Is this purely stylistic with no functional impact? "
            "(e.g., prefer f-strings over .format()). If yes, do NOT report.\n\n"
            "Report ONLY issues that a senior developer would actually fix in a PR review. "
            "Quality over quantity — 1 genuine finding beats 5 false positives.\n"
            "Maximum 3 findings per analyzer."
        )

        try:
            response = await self._llm.complete(prompt, system=system, temperature=0.2)
            return self._parse_findings(response, name, context)
        except Exception as e:
            logger.error("Analyzer %s failed: %s", name, e)
            return []

    def _security_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for SECURITY vulnerabilities:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"{files_text}\n\n"
            "Focus on vulnerabilities with REAL exploitability:\n"
            "1. Hardcoded secrets/credentials (NOT test fixtures or placeholders)\n"
            "2. SQL injection (only if raw queries are used, NOT ORM calls)\n"
            "3. Command injection via unsanitized user input\n"
            "4. Path traversal in file operations\n"
            "5. Insecure deserialization (pickle, yaml.load without SafeLoader)\n"
            "6. Missing authentication on sensitive endpoints\n\n"
            "DO NOT report:\n"
            "- Hardcoded values in test/fixture files\n"
            "- Missing CSRF if the framework handles it (Django, etc.)\n"
            "- Generic 'missing input validation' without a concrete attack vector\n"
            "- Theoretical vulnerabilities that require physical access\n"
        )

    def _code_quality_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for CODE QUALITY bugs:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"{files_text}\n\n"
            "Focus on issues that cause BUGS or CRASHES in production:\n"
            "1. Unhandled None/null that will crash at runtime\n"
            "2. Resource leaks (unclosed files, connections, cursors)\n"
            "3. Race conditions in concurrent code\n"
            "4. Off-by-one errors in loops or slices\n"
            "5. Silent data corruption (wrong type coercion, truncation)\n"
            "6. Missing error propagation (swallowed exceptions hiding failures)\n\n"
            "DO NOT report:\n"
            "- Missing type hints (unless the project uses them everywhere else)\n"
            "- Code style preferences (naming, formatting)\n"
            "- 'Could be refactored' without a concrete bug\n"
            "- Missing logging (unless an error path silently fails)\n"
        )

    def _docs_prompt(self, ctx: RepoContext) -> str:
        readme = ctx.readme_content or "No README found"
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for DOCUMENTATION gaps:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"README:\n{readme[:2000]}\n\n"
            f"{files_text}\n\n"
            "Look for:\n"
            "1. Missing or incomplete README sections (install, usage, API docs)\n"
            "2. Undocumented public functions/classes/modules\n"
            "3. Outdated or incorrect code examples\n"
            "4. Missing docstrings\n"
            "5. Missing CHANGELOG entries\n"
            "6. Missing or incomplete API documentation\n"
            "7. Broken links in documentation\n"
            "8. Missing contributing guidelines\n"
        )

    def _ui_ux_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this repository for UI/UX issues:\n\n"
            f"Repository: {ctx.repo.full_name} ({ctx.repo.language})\n\n"
            f"{files_text}\n\n"
            "Look for:\n"
            "1. Accessibility (a11y) issues (missing ARIA labels, alt text)\n"
            "2. Missing loading/skeleton states\n"
            "3. Missing error boundaries/states\n"
            "4. Responsiveness issues\n"
            "5. Color contrast problems\n"
            "6. Missing keyboard navigation\n"
            "7. Missing form validation feedback\n"
            "8. Poor empty states\n"
            "NOTE: Only analyze if the repo contains frontend code (HTML/CSS/JS/React/Vue/etc). "
            "If no frontend code found, return 'findings: []'.\n"
        )

    def _performance_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for PERFORMANCE issues:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"{files_text}\n\n"
            "Focus on issues with MEASURABLE impact (>10% improvement):\n"
            "1. N+1 queries — database/API calls inside loops\n"
            "2. Blocking I/O in async code — sync calls in event loop\n"
            "3. O(n²) algorithms where O(n) or O(n log n) is possible\n"
            "4. Memory leaks — growing collections without bounds\n"
            "5. Repeated expensive computation that should be cached\n\n"
            "DO NOT report:\n"
            "- Micro-optimizations (f-string vs .format(), list comp vs loop)\n"
            "- Theoretical perf issues in code that runs once at startup\n"
            "- 'Could use caching' without evidence the operation is expensive\n"
            "- String concatenation unless it's in a tight loop with large data\n"
        )

    def _refactor_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for REFACTORING opportunities:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"{files_text}\n\n"
            "Look for:\n"
            "1. Functions/methods that are too long (>50 lines) and should be split\n"
            "2. DRY violations (duplicated logic across multiple files)\n"
            "3. God classes/modules that do too many things\n"
            "4. Deeply nested conditionals (>3 levels) that need extraction\n"
            "5. Inappropriate use of inheritance vs composition\n"
            "6. Magic numbers/strings that should be named constants\n"
            "7. Complex boolean expressions that need helper methods\n"
            "8. Mixed abstraction levels within a single function\n"
            "9. Feature envy (methods that use other class's data more than their own)\n"
            "10. Dead code or unused imports/variables\n\n"
            "Focus on refactorings that improve readability and maintainability. "
            "Each finding should be a single, self-contained refactoring.\n"
        )

    def _testing_prompt(self, ctx: RepoContext) -> str:
        files_text = self._format_files(ctx)
        return (
            f"Analyze this {ctx.repo.language} repository for TESTING gaps:\n\n"
            f"Repository: {ctx.repo.full_name}\n\n"
            f"{files_text}\n\n"
            "Look for:\n"
            "1. Public functions/methods with NO unit tests\n"
            "2. Critical business logic without test coverage\n"
            "3. Edge cases not covered by existing tests\n"
            "4. Error handling paths without tests\n"
            "5. Missing integration tests for API endpoints\n"
            "6. Untested configuration validation\n"
            "7. Missing tests for data transformations/serialization\n"
            "8. Race conditions or concurrency that needs testing\n\n"
            "For each finding, suggest a specific test that should be written. "
            "Focus on the most impactful missing tests — those covering critical "
            "code paths or frequently modified code.\n"
            "NOTE: If the repo has no test directory/framework at all, suggest "
            "setting up a test framework as one finding and specific tests as others.\n"
        )

    def _format_files(self, ctx: RepoContext) -> str:
        """Format relevant files for the prompt."""
        parts = []
        for path, content in ctx.relevant_files.items():
            truncated = content[:3000] if len(content) > 3000 else content
            parts.append(f"### {path}\n```\n{truncated}\n```")
        return "\n\n".join(parts) if parts else "No source files available."

    def _parse_findings(self, response: str, analyzer_name: str, ctx: RepoContext) -> list[Finding]:
        """Parse LLM response into Finding objects."""
        import yaml

        findings: list[Finding] = []

        type_map = {
            "security": ContributionType.SECURITY_FIX,
            "code_quality": ContributionType.CODE_QUALITY,
            "docs": ContributionType.DOCS_IMPROVE,
            "ui_ux": ContributionType.UI_UX_FIX,
            "performance": ContributionType.PERFORMANCE_OPT,
            "refactor": ContributionType.REFACTOR,
            "testing": ContributionType.CODE_QUALITY,
        }
        contrib_type = type_map.get(analyzer_name, ContributionType.CODE_QUALITY)

        try:
            # Try to extract YAML from the response
            yaml_text = response
            if "```yaml" in response:
                yaml_text = response.split("```yaml")[1].split("```")[0]
            elif "```" in response:
                yaml_text = response.split("```")[1].split("```")[0]

            parsed = yaml.safe_load(yaml_text)
            if not parsed:
                return []

            items = parsed if isinstance(parsed, list) else parsed.get("findings", [])

            for item in items:
                if not isinstance(item, dict):
                    continue

                severity_str = str(item.get("severity", "medium")).lower()
                try:
                    severity = Severity(severity_str)
                except ValueError:
                    severity = Severity.MEDIUM

                findings.append(
                    Finding(
                        id=str(uuid.uuid4())[:8],
                        type=contrib_type,
                        severity=severity,
                        title=str(item.get("title", "Untitled finding")),
                        description=str(item.get("description", "")),
                        file_path=str(item.get("file_path", "")),
                        line_start=item.get("line_start"),
                        line_end=item.get("line_end"),
                        suggestion=item.get("suggestion"),
                    )
                )
        except Exception as e:
            logger.warning("Failed to parse %s findings: %s", analyzer_name, e)

        logger.info("Analyzer %s found %d issues", analyzer_name, len(findings))
        return findings

    def _deduplicate(self, findings: list[Finding]) -> list[Finding]:
        """Remove duplicate findings."""
        seen: set[str] = set()
        unique: list[Finding] = []
        for f in findings:
            key = f"{f.file_path}:{f.title}:{f.severity}"
            if key not in seen:
                seen.add(key)
                unique.append(f)
        return unique

    def _filter_severity(self, findings: list[Finding]) -> list[Finding]:
        """Filter findings by minimum severity threshold."""
        order = [Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]
        try:
            threshold = Severity(self._config.severity_threshold)
        except ValueError:
            threshold = Severity.MEDIUM
        min_idx = order.index(threshold)
        return [f for f in findings if order.index(f.severity) >= min_idx]
