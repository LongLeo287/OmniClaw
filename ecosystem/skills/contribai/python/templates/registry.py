"""Template registry for common contribution patterns.

Templates are YAML-defined patterns that describe common
fixes the agent can apply without full LLM generation.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

BUILTIN_DIR = Path(__file__).parent / "builtin"


@dataclass
class Template:
    """A contribution template definition."""

    name: str
    description: str
    type: str  # ContributionType value
    pattern: str  # what to look for
    fix_template: str  # how to fix it
    severity: str = "medium"
    languages: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


class TemplateRegistry:
    """Manages contribution templates."""

    def __init__(self):
        self._templates: dict[str, Template] = {}
        self._load_builtins()

    def _load_builtins(self):
        """Load built-in templates from the builtin/ dir."""
        if not BUILTIN_DIR.exists():
            return
        for path in sorted(BUILTIN_DIR.glob("*.yaml")):
            try:
                self._load_file(path)
            except Exception:
                logger.warning("Failed to load template: %s", path.name)

    def _load_file(self, path: Path):
        """Load a single template YAML file."""
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not raw or not isinstance(raw, dict):
            return
        tpl = Template(
            name=raw.get("name", path.stem),
            description=raw.get("description", ""),
            type=raw.get("type", "code_quality"),
            pattern=raw.get("pattern", ""),
            fix_template=raw.get("fix_template", ""),
            severity=raw.get("severity", "medium"),
            languages=raw.get("languages", []),
            tags=raw.get("tags", []),
        )
        self._templates[tpl.name] = tpl

    def load_directory(self, directory: str | Path):
        """Load additional templates from a directory."""
        d = Path(directory)
        if not d.exists():
            return
        for path in sorted(d.glob("*.yaml")):
            self._load_file(path)

    def get(self, name: str) -> Template | None:
        """Get a template by name."""
        return self._templates.get(name)

    def list_all(self) -> list[Template]:
        """List all loaded templates."""
        return list(self._templates.values())

    def filter_by_type(self, contrib_type: str) -> list[Template]:
        """Filter templates by contribution type."""
        return [t for t in self._templates.values() if t.type == contrib_type]

    def filter_by_language(self, language: str) -> list[Template]:
        """Filter templates applicable to a language."""
        lang_lower = language.lower()
        return [
            t
            for t in self._templates.values()
            if not t.languages or lang_lower in [la.lower() for la in t.languages]
        ]
