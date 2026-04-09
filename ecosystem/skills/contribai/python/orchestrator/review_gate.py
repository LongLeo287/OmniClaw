"""Human-in-the-loop review gate before PR creation.

Inspired by AgentScope's Human-in-the-loop pattern — pauses the
pipeline to show the generated contribution for human approval.
"""

from __future__ import annotations

import logging

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

logger = logging.getLogger(__name__)
console = Console()


class ReviewDecision:
    """Result of a human review decision."""

    APPROVE = "approve"
    REJECT = "reject"
    SKIP = "skip"

    def __init__(self, action: str, reason: str = ""):
        self.action = action
        self.reason = reason

    @property
    def approved(self) -> bool:
        return self.action == self.APPROVE

    @property
    def rejected(self) -> bool:
        return self.action == self.REJECT

    @property
    def skipped(self) -> bool:
        return self.action == self.SKIP


class HumanReviewer:
    """Interactive review gate that displays contributions for human approval.

    Shows finding details, generated code changes, and commit message
    in a Rich-formatted terminal UI, then prompts for approval.
    """

    def __init__(self, *, auto_approve: bool = False):
        self._auto_approve = auto_approve

    async def review(self, contribution, finding, repo_name: str) -> ReviewDecision:
        """Present a contribution for human review.

        Args:
            contribution: Generated Contribution object.
            finding: Original Finding that triggered the fix.
            repo_name: Full repo name (owner/repo).

        Returns:
            ReviewDecision with the user's choice.
        """
        if self._auto_approve:
            return ReviewDecision(ReviewDecision.APPROVE)

        self._display_review(contribution, finding, repo_name)
        return self._prompt_decision()

    def _display_review(self, contribution, finding, repo_name: str) -> None:
        """Display the contribution details in Rich panels."""
        console.print()
        console.rule("[bold cyan]🔍 Human Review Required[/bold cyan]")
        console.print()

        # Finding info
        info_table = Table(show_header=False, box=None, padding=(0, 2))
        info_table.add_column("Key", style="bold")
        info_table.add_column("Value")
        info_table.add_row("Repo", repo_name)
        info_table.add_row("Title", contribution.title)
        info_table.add_row(
            "Type",
            contribution.contribution_type.value
            if hasattr(contribution.contribution_type, "value")
            else str(contribution.contribution_type),
        )
        info_table.add_row(
            "Severity",
            finding.severity.value if hasattr(finding.severity, "value") else str(finding.severity),
        )
        info_table.add_row("File", finding.file_path or "N/A")
        info_table.add_row("Commit", contribution.commit_message)
        console.print(Panel(info_table, title="[bold]📋 Contribution Details", border_style="blue"))

        # Description
        console.print(
            Panel(
                contribution.description or "No description",
                title="[bold]📝 Description",
                border_style="dim",
            )
        )

        # Code changes
        if contribution.changes:
            for change in contribution.changes[:3]:  # cap at 3 files
                path = getattr(change, "path", "unknown")
                new_content = getattr(change, "new_content", "")
                if new_content:
                    # Detect language from extension
                    ext = path.rsplit(".", 1)[-1] if "." in path else "text"
                    lang_map = {
                        "py": "python",
                        "js": "javascript",
                        "ts": "typescript",
                        "go": "go",
                        "rs": "rust",
                        "java": "java",
                        "rb": "ruby",
                    }
                    lang = lang_map.get(ext, ext)

                    # Truncate very long content
                    display_content = new_content
                    if len(new_content) > 2000:
                        display_content = (
                            new_content[:1500]
                            + f"\n\n... ({len(new_content) - 1500} chars truncated) ..."
                        )

                    syntax = Syntax(
                        display_content,
                        lang,
                        theme="monokai",
                        line_numbers=True,
                    )
                    console.print(Panel(syntax, title=f"[bold]📄 {path}", border_style="green"))

            if len(contribution.changes) > 3:
                console.print(f"  [dim]... and {len(contribution.changes) - 3} more files[/dim]")
        console.print()

    @staticmethod
    def _prompt_decision() -> ReviewDecision:
        """Prompt user for approval decision."""
        choices = Text()
        choices.append("[y]", style="bold green")
        choices.append("es  ")
        choices.append("[n]", style="bold red")
        choices.append("o  ")
        choices.append("[s]", style="bold yellow")
        choices.append("kip  ")

        console.print(Panel(choices, title="[bold]Create this PR?", border_style="cyan"))

        while True:
            try:
                response = console.input("[bold cyan]→ [/bold cyan]").strip().lower()
            except (EOFError, KeyboardInterrupt):
                console.print("\n[yellow]⏭️ Skipped (interrupted)[/yellow]")
                return ReviewDecision(ReviewDecision.SKIP, "interrupted")

            if response in ("y", "yes"):
                console.print("[green]✅ Approved — creating PR...[/green]")
                return ReviewDecision(ReviewDecision.APPROVE)
            if response in ("n", "no"):
                console.print("[red]❌ Rejected — skipping this contribution[/red]")
                return ReviewDecision(ReviewDecision.REJECT)
            if response in ("s", "skip"):
                console.print("[yellow]⏭️ Skipped[/yellow]")
                return ReviewDecision(ReviewDecision.SKIP)

            console.print("[dim]Please enter y, n, or s[/dim]")
