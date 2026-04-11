#!/usr/bin/env python3
"""
[OER] Sub-Agent Context Compiler
======================================================
Mission: 
  1. Deep compile 5 layers of systemic context constraints.
  2. Render into an immutable markdown roadmap for CLI Agents (Pillar 2).
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT = REPO_ROOT / ".omniclaw_context"
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json"}


@dataclass(frozen=True)
class LayerSource:
    layer_name: str
    path: Path


def _collect_files(base: Path, *, limit: int = 10) -> list[Path]:
    if not base.is_absolute():
        base = (REPO_ROOT / base).resolve()
    if not base.exists():
        return []
    if base.is_file():
        return [base]

    collected: list[Path] = []
    for candidate in sorted(base.rglob("*")):
        if len(collected) >= limit:
            break
        if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES and candidate.name != ".omniclaw_context":
            collected.append(candidate)
    return collected


def discover_sources(task_files: list[Path], dept: str | None, agent_path: Path | None) -> list[LayerSource]:
    sources: list[LayerSource] = []

    company_candidates = [
        REPO_ROOT / "brain" / "rules",
        REPO_ROOT / ".clauderules",
        REPO_ROOT / ".cursorrules",
    ]
    project_candidates = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "README-vn.md",
        REPO_ROOT / "brain" / "registry" / "OMA_SYSTEM_MAP.json",
    ]

    for candidate in company_candidates:
        for path in _collect_files(candidate):
            sources.append(LayerSource("Company", path))

    for candidate in project_candidates:
        for path in _collect_files(candidate):
            sources.append(LayerSource("Project", path))

    if dept:
        dept_dir = REPO_ROOT / "ecosystem" / "workforce" / "departments" / dept
        for path in _collect_files(dept_dir, limit=12):
            sources.append(LayerSource("Department", path))

    if agent_path:
        for path in _collect_files(agent_path, limit=12):
            sources.append(LayerSource("Agent", path))
    else:
        for fallback in [REPO_ROOT / "AGENT.md", REPO_ROOT / "agent.md"]:
            for path in _collect_files(fallback):
                sources.append(LayerSource("Agent", path))

    for task_file in task_files:
        for path in _collect_files(task_file):
            sources.append(LayerSource("Task", path))

    return sources


def compile_context(task_files: list[Path], dept: str | None = None, agent_path: Path | None = None) -> str:
    sources = discover_sources(task_files, dept, agent_path)
    lines: list[str] = [
        "# OmniClaw Compiled Context",
        "",
        "Later layers override earlier layers when instructions conflict.",
        "",
    ]

    for source in sources:
        rel_path = source.path.relative_to(REPO_ROOT).as_posix()
        lines.extend([
            f"## {source.layer_name}: `{rel_path}`",
            "",
            source.path.read_text(encoding="utf-8", errors="ignore").strip(),
            "",
        ])

    return "\n".join(lines).strip() + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile OmniClaw multi-layer system context into one markdown file.")
    parser.add_argument("--task-file", action="append", default=[], help="Task file(s) to include as the final layer.")
    parser.add_argument("--dept", default=None, help="Department folder under ecosystem/workforce/departments.")
    parser.add_argument("--agent-path", default=None, help="Agent file or directory to include.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output markdown file path.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    task_files = [Path(path) for path in args.task_file]
    compiled = compile_context(
        task_files=task_files,
        dept=args.dept,
        agent_path=Path(args.agent_path) if args.agent_path else None,
    )
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = (REPO_ROOT / output_path).resolve()
    output_path.write_text(compiled, encoding="utf-8")
    print(f"Context compiler complete: wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
