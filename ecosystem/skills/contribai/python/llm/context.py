"""Context management for LLM calls.

Handles token estimation, context window chunking, and
building effective prompts from repository content.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from contribai.core.models import FileNode, RepoContext

logger = logging.getLogger(__name__)

# Rough token estimates (chars per token varies by model/language)
CHARS_PER_TOKEN = 4


@dataclass
class ContextBudget:
    """Tracks token budget for context window."""

    max_tokens: int
    used_tokens: int = 0
    sections: dict[str, int] = field(default_factory=dict)

    @property
    def remaining(self) -> int:
        return max(0, self.max_tokens - self.used_tokens)

    def can_fit(self, text: str) -> bool:
        return estimate_tokens(text) <= self.remaining

    def add(self, section_name: str, text: str) -> bool:
        tokens = estimate_tokens(text)
        if tokens > self.remaining:
            return False
        self.used_tokens += tokens
        self.sections[section_name] = tokens
        return True


def estimate_tokens(text: str) -> int:
    """Rough token estimate based on character count."""
    return len(text) // CHARS_PER_TOKEN


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """Truncate text to fit within token budget."""
    max_chars = max_tokens * CHARS_PER_TOKEN
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n... [truncated]"


def build_repo_context_prompt(context: RepoContext, max_tokens: int = 6000) -> str:
    """Build a compact prompt summarizing the repository context.

    Prioritizes: README > file tree > contributing guide > relevant files.
    """
    budget = ContextBudget(max_tokens=max_tokens)
    parts: list[str] = []

    # 1. Repo metadata (always included)
    meta = (
        f"## Repository: {context.repo.full_name}\n"
        f"- Language: {context.repo.language}\n"
        f"- Stars: {context.repo.stars}\n"
        f"- Description: {context.repo.description or 'N/A'}\n"
    )
    budget.add("metadata", meta)
    parts.append(meta)

    # 2. README (high priority)
    if context.readme_content:
        readme = truncate_to_tokens(context.readme_content, min(2000, budget.remaining))
        if budget.add("readme", readme):
            parts.append(f"## README\n{readme}")

    # 3. File tree (medium priority)
    if context.file_tree:
        tree_text = format_file_tree(context.file_tree)
        tree_text = truncate_to_tokens(tree_text, min(1000, budget.remaining))
        if budget.add("file_tree", tree_text):
            parts.append(f"## File Structure\n```\n{tree_text}\n```")

    # 4. Contributing guide
    if context.contributing_guide:
        guide = truncate_to_tokens(context.contributing_guide, min(800, budget.remaining))
        if budget.add("contributing", guide):
            parts.append(f"## Contributing Guide\n{guide}")

    # 5. Relevant source files
    if context.relevant_files:
        parts.append("## Relevant Source Files")
        for path, content in context.relevant_files.items():
            truncated = truncate_to_tokens(content, min(500, budget.remaining))
            if budget.add(f"file:{path}", truncated):
                parts.append(f"### {path}\n```\n{truncated}\n```")
            else:
                break

    # 6. Coding style
    if context.coding_style and budget.can_fit(context.coding_style):
        budget.add("style", context.coding_style)
        parts.append(f"## Coding Conventions\n{context.coding_style}")

    logger.debug(
        "Context built: %d tokens across %d sections",
        budget.used_tokens,
        len(budget.sections),
    )
    return "\n\n".join(parts)


def format_file_tree(nodes: list[FileNode], max_depth: int = 3) -> str:
    """Format file tree nodes into a readable string."""
    lines: list[str] = []
    for node in sorted(nodes, key=lambda n: n.path):
        depth = node.path.count("/")
        if depth > max_depth:
            continue
        prefix = "📁 " if node.type == "tree" else "📄 "
        indent = "  " * depth
        lines.append(f"{indent}{prefix}{node.path.split('/')[-1]}")
    return "\n".join(lines[:100])  # cap output size
