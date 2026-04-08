"""Named contribution profiles for quick configuration.

Profiles are pre-built config presets that adjust analysis
focus, contribution types, and behavior for different goals.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

PROFILE_DIRS = [
    Path.home() / ".contribai" / "profiles",
    Path("profiles"),
    Path(".contribai") / "profiles",
]


class ContribProfile(BaseModel):
    """A named contribution profile."""

    name: str
    description: str = ""
    analyzers: list[str] = Field(default_factory=list)
    contribution_types: list[str] = Field(default_factory=list)
    severity_threshold: str = "medium"
    max_prs_per_day: int = 10
    max_repos_per_run: int = 5
    dry_run: bool = False


# Built-in profiles
BUILTIN_PROFILES: dict[str, ContribProfile] = {
    "security-focused": ContribProfile(
        name="security-focused",
        description=("Focus on security vulnerabilities and fixes"),
        analyzers=["security"],
        contribution_types=[
            "security_fix",
            "code_quality",
        ],
        severity_threshold="high",
        max_prs_per_day=5,
    ),
    "docs-focused": ContribProfile(
        name="docs-focused",
        description=("Focus on documentation improvements"),
        analyzers=["docs"],
        contribution_types=[
            "docs_improve",
        ],
        severity_threshold="low",
        max_prs_per_day=10,
    ),
    "full-scan": ContribProfile(
        name="full-scan",
        description="Run all analyzers with low threshold",
        analyzers=[
            "security",
            "code_quality",
            "docs",
            "ui_ux",
        ],
        contribution_types=[
            "security_fix",
            "docs_improve",
            "code_quality",
            "feature_add",
            "ui_ux_fix",
            "performance_opt",
            "refactor",
        ],
        severity_threshold="low",
        max_repos_per_run=10,
    ),
    "gentle": ContribProfile(
        name="gentle",
        description=("Low-impact mode: small fixes, dry run by default"),
        analyzers=["docs", "code_quality"],
        contribution_types=[
            "docs_improve",
            "code_quality",
        ],
        severity_threshold="high",
        max_prs_per_day=3,
        max_repos_per_run=2,
        dry_run=True,
    ),
}


def get_profile(name: str) -> ContribProfile | None:
    """Get a profile by name (built-in or custom)."""
    # Check built-in first
    if name in BUILTIN_PROFILES:
        return BUILTIN_PROFILES[name]

    # Search custom profile directories
    for d in PROFILE_DIRS:
        path = d / f"{name}.yaml"
        if path.exists():
            return _load_profile(path)
    return None


def list_profiles() -> list[ContribProfile]:
    """List all available profiles (built-in + custom)."""
    profiles = dict(BUILTIN_PROFILES)

    # Load custom profiles
    for d in PROFILE_DIRS:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.yaml")):
            try:
                p = _load_profile(path)
                if p:
                    profiles[p.name] = p
            except Exception:
                logger.warning("Failed to load profile: %s", path)

    return list(profiles.values())


def apply_profile(
    config_data: dict[str, Any],
    profile: ContribProfile,
) -> dict[str, Any]:
    """Apply a profile's settings to config data."""
    if profile.analyzers:
        config_data.setdefault("analysis", {})["enabled_analyzers"] = profile.analyzers
    if profile.contribution_types:
        config_data.setdefault("contribution", {})["enabled_types"] = profile.contribution_types
    config_data.setdefault("analysis", {})["severity_threshold"] = profile.severity_threshold
    config_data.setdefault("github", {})["max_prs_per_day"] = profile.max_prs_per_day
    config_data.setdefault("github", {})["max_repos_per_run"] = profile.max_repos_per_run
    return config_data


def _load_profile(path: Path) -> ContribProfile | None:
    """Load a profile from a YAML file."""
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not raw or not isinstance(raw, dict):
        return None
    return ContribProfile(**raw)
