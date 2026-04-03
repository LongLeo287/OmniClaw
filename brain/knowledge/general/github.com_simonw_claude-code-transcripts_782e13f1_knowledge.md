---
id: github.com-simonw-claude-code-transcripts-782e13f1
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.281567
---

# KNOWLEDGE EXTRACT: github.com_simonw_claude-code-transcripts_782e13f1
> **Extracted on:** 2026-04-01 10:00:26
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520551/github.com_simonw_claude-code-transcripts_782e13f1

---

## File: `.gitignore`
```
.DS_Store
__pycache__
uv.lock
.playwright-mcp/
```

## File: `AGENTS.md`
```markdown
Uses uv. Run tests like this:

    uv run pytest

Run the development version of the tool like this:

    uv run claude-code-transcripts --help

Always practice TDD: write a faliing test, watch it fail, then make it pass.

Commit early and often. Commits should bundle the test, implementation, and documentation changes together.

Run Black to format code before you commit:

    uv run black .
```

## File: `CLAUDE.md`
```markdown
@AGENTS.md
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
# claude-code-transcripts

[![PyPI](https://img.shields.io/pypi/v/claude-code-transcripts.svg)](https://pypi.org/project/claude-code-transcripts/)
[![Changelog](https://img.shields.io/github/v/release/simonw/claude-code-transcripts?include_prereleases&label=changelog)](https://github.com/simonw/claude-code-transcripts/releases)
[![Tests](https://github.com/simonw/claude-code-transcripts/workflows/Test/badge.svg)](https://github.com/simonw/claude-code-transcripts/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/claude-code-transcripts/blob/main/LICENSE)

Convert Claude Code session files (JSON or JSONL) to clean, mobile-friendly HTML pages with pagination.

[Example transcript](https://static.simonwillison.net/static/2025/claude-code-microjs/index.html) produced using this tool.

Read [A new way to extract detailed transcripts from Claude Code](https://simonwillison.net/2025/Dec/25/claude-code-transcripts/) for background on this project.

> [!WARNING]
>
> The `web` commands for both listing Claude Code for web sessions and converting those to a transcript are both broken right now due to changes to the unofficial and undocumented APIs that these commands were using. See [issue #77](https://github.com/simonw/claude-code-transcripts/issues/77) for details.

## Installation

Install this tool using `uv`:
```bash
uv tool install claude-code-transcripts
```
Or run it without installing:
```bash
uvx claude-code-transcripts --help
```

## Usage

This tool converts Claude Code session files into browseable multi-page HTML transcripts.

There are four commands available:

- `local` (default) - select from local Claude Code sessions stored in `~/.claude/projects`
- `web` - select from web sessions via the Claude API
- `json` - convert a specific JSON or JSONL session file
- `all` - convert all local sessions to a browsable HTML archive

The quickest way to view a recent local session:

```bash
claude-code-transcripts
```

This shows an interactive picker to select a session, generates HTML, and opens it in your default browser.

### Output options

All commands support these options:

- `-o, --output DIRECTORY` - output directory (default: writes to temp dir and opens browser)
- `-a, --output-auto` - auto-name output subdirectory based on session ID or filename
- `--repo OWNER/NAME` - GitHub repo for commit links (auto-detected if not specified). For `web` command, also filters the session list.
- `--open` - open the generated `index.html` in your default browser (default if no `-o` specified)
- `--gist` - upload the generated HTML files to a GitHub Gist and output a preview URL
- `--json` - include the original session file in the output directory

The generated output includes:
- `index.html` - an index page with a timeline of prompts and commits
- `page-001.html`, `page-002.html`, etc. - paginated transcript pages

### Local sessions

Local Claude Code sessions are stored as JSONL files in `~/.claude/projects`. Run with no arguments to select from recent sessions:

```bash
claude-code-transcripts
# or explicitly:
claude-code-transcripts local
```

Use `--limit` to control how many sessions are shown (default: 10):

```bash
claude-code-transcripts local --limit 20
```

### Web sessions

Import sessions directly from the Claude API:

```bash
# Interactive session picker
claude-code-transcripts web

# Import a specific session by ID
claude-code-transcripts web SESSION_ID

# Import and publish to gist
claude-code-transcripts web SESSION_ID --gist
```

The session picker displays sessions grouped by their associated GitHub repository:

```
simonw/datasette              2025-01-15T10:30:00  Fix the bug in query parser
simonw/llm                    2025-01-14T09:00:00  Add streaming support
(no repo)                     2025-01-13T14:22:00  General coding session
```

Use `--repo` to filter the session list to a specific repository:

```bash
claude-code-transcripts web --repo simonw/datasette
```

On macOS, API credentials are automatically retrieved from your keychain (requires being logged into Claude Code). On other platforms, provide `--token` and `--org-uuid` manually.

### Publishing to GitHub Gist

Use the `--gist` option to automatically upload your transcript to a GitHub Gist and get a shareable preview URL:

```bash
claude-code-transcripts --gist
claude-code-transcripts web --gist
claude-code-transcripts json session.json --gist
```

This will output something like:
```
Gist: https://gist.github.com/username/abc123def456
Preview: https://gisthost.github.io/?abc123def456/index.html
Files: /var/folders/.../session-id
```

The preview URL uses [gisthost.github.io](https://gisthost.github.io/) to render your HTML gist. The tool automatically injects JavaScript to fix relative links when served through gisthost.

Combine with `-o` to keep a local copy:

```bash
claude-code-transcripts json session.json -o ./my-transcript --gist
```

**Requirements:** The `--gist` option requires the [GitHub CLI](https://cli.github.com/) (`gh`) to be installed and authenticated (`gh auth login`).

### Auto-naming output directories

Use `-a/--output-auto` to automatically create a subdirectory named after the session:

```bash
# Creates ./session_ABC123/ subdirectory
claude-code-transcripts web SESSION_ABC123 -a

# Creates ./transcripts/session_ABC123/ subdirectory
claude-code-transcripts web SESSION_ABC123 -o ./transcripts -a
```

### Including the source file

Use the `--json` option to include the original session file in the output directory:

```bash
claude-code-transcripts json session.json -o ./my-transcript --json
```

This will output:
```
JSON: ./my-transcript/session_ABC.json (245.3 KB)
```

This is useful for archiving the source data alongside the HTML output.

### Converting from JSON/JSONL files

Convert a specific session file directly:

```bash
claude-code-transcripts json session.json -o output-directory/
claude-code-transcripts json session.jsonl --open
```
This works with both JSONL files in the `~/.claude/projects/` folder and JSON session files extracted from Claude Code for web.

The `json` command can take a URL to a JSON or JSONL file as an alternative to a path on disk.

### Converting all sessions

Convert all your local Claude Code sessions to a browsable HTML archive:

```bash
claude-code-transcripts all
```

This creates a directory structure with:
- A master index listing all projects
- Per-project pages listing sessions
- Individual session transcripts

Options:

- `-s, --source DIRECTORY` - source directory (default: `~/.claude/projects`)
- `-o, --output DIRECTORY` - output directory (default: `./claude-archive`)
- `--include-agents` - include agent session files (excluded by default)
- `--dry-run` - show what would be converted without creating files
- `--open` - open the generated archive in your default browser
- `-q, --quiet` - suppress all output except errors

Examples:

```bash
# Preview what would be converted
claude-code-transcripts all --dry-run

# Convert all sessions and open in browser
claude-code-transcripts all --open

# Convert to a specific directory
claude-code-transcripts all -o ./my-archive

# Include agent sessions
claude-code-transcripts all --include-agents
```

## Development

To contribute to this tool, first checkout the code. You can run the tests using `uv run`:
```bash
cd claude-code-transcripts
uv run pytest
```
And run your local development copy of the tool like this:
```bash
uv run claude-code-transcripts --help
```
```

## File: `pyproject.toml`
```
[project]
name = "claude-code-transcripts"
version = "0.6"
description = "Convert Claude Code session files to HTML transcripts"
readme = "README.md"
license = "Apache-2.0"
authors = [
    { name = "Simon Willison" }
]
requires-python = ">=3.10"
dependencies = [
    "click",
    "click-default-group",
    "httpx",
    "jinja2",
    "markdown",
    "questionary",
]

[project.urls]
Homepage = "https://github.com/simonw/claude-code-transcripts"
Changelog = "https://github.com/simonw/claude-code-transcripts/releases"
Issues = "https://github.com/simonw/claude-code-transcripts/issues"
CI = "https://github.com/simonw/claude-code-transcripts/actions"

[project.scripts]
claude-code-transcripts = "claude_code_transcripts:main"

[build-system]
requires = ["uv_build>=0.9.7,<0.10.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "pytest>=9.0.2",
    "pytest-httpx>=0.35.0",
    "syrupy>=5.0.0",
]
```

## File: `src/claude_code_transcripts/__init__.py`
```python
"""Convert Claude Code session JSON to a clean mobile-friendly HTML page with pagination."""

import json
import html
import os
import platform
import re
import shutil
import subprocess
import tempfile
import webbrowser
from datetime import datetime
from pathlib import Path

import click
from click_default_group import DefaultGroup
import httpx
from jinja2 import Environment, PackageLoader
import markdown
import questionary

# Set up Jinja2 environment
_jinja_env = Environment(
    loader=PackageLoader("claude_code_transcripts", "templates"),
    autoescape=True,
)

# Load macros template and expose macros
_macros_template = _jinja_env.get_template("macros.html")
_macros = _macros_template.module


def get_template(name):
    """Get a Jinja2 template by name."""
    return _jinja_env.get_template(name)


# Regex to match git commit output: [branch hash] message
COMMIT_PATTERN = re.compile(r"\[[\w\-/]+ ([a-f0-9]{7,})\] (.+?)(?:\n|$)")

# Regex to detect GitHub repo from git push output (e.g., github.com/owner/repo/pull/new/branch)
GITHUB_REPO_PATTERN = re.compile(
    r"github\.com/([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)/pull/new/"
)

PROMPTS_PER_PAGE = 5
LONG_TEXT_THRESHOLD = (
    300  # Characters - text blocks longer than this are shown in index
)


def extract_text_from_content(content):
    """Extract plain text from message content.

    Handles both string content (older format) and array content (newer format).

    Args:
        content: Either a string or a list of content blocks like
                 [{"type": "text", "text": "..."}, {"type": "image", ...}]

    Returns:
        The extracted text as a string, or empty string if no text found.
    """
    if isinstance(content, str):
        return content.strip()
    elif isinstance(content, list):
        # Extract text from content blocks of type "text"
        texts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text", "")
                if text:
                    texts.append(text)
        return " ".join(texts).strip()
    return ""


# Module-level variable for GitHub repo (set by generate_html)
_github_repo = None

# API constants
API_BASE_URL = "https://api.anthropic.com/v1"
ANTHROPIC_VERSION = "2023-06-01"


def get_session_summary(filepath, max_length=200):
    """Extract a human-readable summary from a session file.

    Supports both JSON and JSONL formats.
    Returns a summary string or "(no summary)" if none found.
    """
    filepath = Path(filepath)
    try:
        if filepath.suffix == ".jsonl":
            return _get_jsonl_summary(filepath, max_length)
        else:
            # For JSON files, try to get first user message
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            loglines = data.get("loglines", [])
            for entry in loglines:
                if entry.get("type") == "user":
                    msg = entry.get("message", {})
                    content = msg.get("content", "")
                    text = extract_text_from_content(content)
                    if text:
                        if len(text) > max_length:
                            return text[: max_length - 3] + "..."
                        return text
            return "(no summary)"
    except Exception:
        return "(no summary)"


def _get_jsonl_summary(filepath, max_length=200):
    """Extract summary from JSONL file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    # First priority: summary type entries
                    if obj.get("type") == "summary" and obj.get("summary"):
                        summary = obj["summary"]
                        if len(summary) > max_length:
                            return summary[: max_length - 3] + "..."
                        return summary
                except json.JSONDecodeError:
                    continue

        # Second pass: find first non-meta user message
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    if (
                        obj.get("type") == "user"
                        and not obj.get("isMeta")
                        and obj.get("message", {}).get("content")
                    ):
                        content = obj["message"]["content"]
                        text = extract_text_from_content(content)
                        if text and not text.startswith("<"):
                            if len(text) > max_length:
                                return text[: max_length - 3] + "..."
                            return text
                except json.JSONDecodeError:
                    continue
    except Exception:
        pass

    return "(no summary)"


def find_local_sessions(folder, limit=10):
    """Find recent JSONL session files in the given folder.

    Returns a list of (Path, summary) tuples sorted by modification time.
    Excludes agent files and warmup/empty sessions.
    """
    folder = Path(folder)
    if not folder.exists():
        return []

    results = []
    for f in folder.glob("**/*.jsonl"):
        if f.name.startswith("agent-"):
            continue
        summary = get_session_summary(f)
        # Skip boring/empty sessions
        if summary.lower() == "warmup" or summary == "(no summary)":
            continue
        results.append((f, summary))

    # Sort by modification time, most recent first
    results.sort(key=lambda x: x[0].stat().st_mtime, reverse=True)
    return results[:limit]


def get_project_display_name(folder_name):
    """Convert encoded folder name to readable project name.

    Claude Code stores projects in folders like:
    - -home-user-projects-myproject -> myproject
    - -mnt-c-Users-name-Projects-app -> app

    For nested paths under common roots (home, projects, code, Users, etc.),
    extracts the meaningful project portion.
    """
    # Common path prefixes to strip
    prefixes_to_strip = [
        "-home-",
        "-mnt-c-Users-",
        "-mnt-c-users-",
        "-Users-",
    ]

    name = folder_name
    for prefix in prefixes_to_strip:
        if name.lower().startswith(prefix.lower()):
            name = name[len(prefix) :]
            break

    # Split on dashes and find meaningful parts
    parts = name.split("-")

    # Common intermediate directories to skip
    skip_dirs = {"projects", "code", "repos", "src", "dev", "work", "documents"}

    # Find the first meaningful part (after skipping username and common dirs)
    meaningful_parts = []
    found_project = False

    for i, part in enumerate(parts):
        if not part:
            continue
        # Skip the first part if it looks like a username (before common dirs)
        if i == 0 and not found_project:
            # Check if next parts contain common dirs
            remaining = [p.lower() for p in parts[i + 1 :]]
            if any(d in remaining for d in skip_dirs):
                continue
        if part.lower() in skip_dirs:
            found_project = True
            continue
        meaningful_parts.append(part)
        found_project = True

    if meaningful_parts:
        return "-".join(meaningful_parts)

    # Fallback: return last non-empty part or original
    for part in reversed(parts):
        if part:
            return part
    return folder_name


def find_all_sessions(folder, include_agents=False):
    """Find all sessions in a Claude projects folder, grouped by project.

    Returns a list of project dicts, each containing:
    - name: display name for the project
    - path: Path to the project folder
    - sessions: list of session dicts with path, summary, mtime, size

    Sessions are sorted by modification time (most recent first) within each project.
    Projects are sorted by their most recent session.
    """
    folder = Path(folder)
    if not folder.exists():
        return []

    projects = {}

    for session_file in folder.glob("**/*.jsonl"):
        # Skip agent files unless requested
        if not include_agents and session_file.name.startswith("agent-"):
            continue

        # Get summary and skip boring sessions
        summary = get_session_summary(session_file)
        if summary.lower() == "warmup" or summary == "(no summary)":
            continue

        # Get project folder
        project_folder = session_file.parent
        project_key = project_folder.name

        if project_key not in projects:
            projects[project_key] = {
                "name": get_project_display_name(project_key),
                "path": project_folder,
                "sessions": [],
            }

        stat = session_file.stat()
        projects[project_key]["sessions"].append(
            {
                "path": session_file,
                "summary": summary,
                "mtime": stat.st_mtime,
                "size": stat.st_size,
            }
        )

    # Sort sessions within each project by mtime (most recent first)
    for project in projects.values():
        project["sessions"].sort(key=lambda s: s["mtime"], reverse=True)

    # Convert to list and sort projects by most recent session
    result = list(projects.values())
    result.sort(
        key=lambda p: p["sessions"][0]["mtime"] if p["sessions"] else 0, reverse=True
    )

    return result


def generate_batch_html(
    source_folder, output_dir, include_agents=False, progress_callback=None
):
    """Generate HTML archive for all sessions in a Claude projects folder.

    Creates:
    - Master index.html listing all projects
    - Per-project directories with index.html listing sessions
    - Per-session directories with transcript pages

    Args:
        source_folder: Path to the Claude projects folder
        output_dir: Path for output archive
        include_agents: Whether to include agent-* session files
        progress_callback: Optional callback(project_name, session_name, current, total)
            called after each session is processed

    Returns statistics dict with total_projects, total_sessions, failed_sessions, output_dir.
    """
    source_folder = Path(source_folder)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all sessions
    projects = find_all_sessions(source_folder, include_agents=include_agents)

    # Calculate total for progress tracking
    total_session_count = sum(len(p["sessions"]) for p in projects)
    processed_count = 0
    successful_sessions = 0
    failed_sessions = []

    # Process each project
    for project in projects:
        project_dir = output_dir / project["name"]
        project_dir.mkdir(exist_ok=True)

        # Process each session
        for session in project["sessions"]:
            session_name = session["path"].stem
            session_dir = project_dir / session_name

            # Generate transcript HTML with error handling
            try:
                generate_html(session["path"], session_dir)
                successful_sessions += 1
            except Exception as e:
                failed_sessions.append(
                    {
                        "project": project["name"],
                        "session": session_name,
                        "error": str(e),
                    }
                )

            processed_count += 1

            # Call progress callback if provided
            if progress_callback:
                progress_callback(
                    project["name"], session_name, processed_count, total_session_count
                )

        # Generate project index
        _generate_project_index(project, project_dir)

    # Generate master index
    _generate_master_index(projects, output_dir)

    return {
        "total_projects": len(projects),
        "total_sessions": successful_sessions,
        "failed_sessions": failed_sessions,
        "output_dir": output_dir,
    }


def _generate_project_index(project, output_dir):
    """Generate index.html for a single project."""
    template = get_template("project_index.html")

    # Format sessions for template
    sessions_data = []
    for session in project["sessions"]:
        mod_time = datetime.fromtimestamp(session["mtime"])
        sessions_data.append(
            {
                "name": session["path"].stem,
                "summary": session["summary"],
                "date": mod_time.strftime("%Y-%m-%d %H:%M"),
                "size_kb": session["size"] / 1024,
            }
        )

    html_content = template.render(
        project_name=project["name"],
        sessions=sessions_data,
        session_count=len(sessions_data),
        css=CSS,
        js=JS,
    )

    output_path = output_dir / "index.html"
    output_path.write_text(html_content, encoding="utf-8")


def _generate_master_index(projects, output_dir):
    """Generate master index.html listing all projects."""
    template = get_template("master_index.html")

    # Format projects for template
    projects_data = []
    total_sessions = 0

    for project in projects:
        session_count = len(project["sessions"])
        total_sessions += session_count

        # Get most recent session date
        if project["sessions"]:
            most_recent = datetime.fromtimestamp(project["sessions"][0]["mtime"])
            recent_date = most_recent.strftime("%Y-%m-%d")
        else:
            recent_date = "N/A"

        projects_data.append(
            {
                "name": project["name"],
                "session_count": session_count,
                "recent_date": recent_date,
            }
        )

    html_content = template.render(
        projects=projects_data,
        total_projects=len(projects),
        total_sessions=total_sessions,
        css=CSS,
        js=JS,
    )

    output_path = output_dir / "index.html"
    output_path.write_text(html_content, encoding="utf-8")


def parse_session_file(filepath):
    """Parse a session file and return normalized data.

    Supports both JSON and JSONL formats.
    Returns a dict with 'loglines' key containing the normalized entries.
    """
    filepath = Path(filepath)

    if filepath.suffix == ".jsonl":
        return _parse_jsonl_file(filepath)
    else:
        # Standard JSON format
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)


def _parse_jsonl_file(filepath):
    """Parse JSONL file and convert to standard format."""
    loglines = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                entry_type = obj.get("type")

                # Skip non-message entries
                if entry_type not in ("user", "assistant"):
                    continue

                # Convert to standard format
                entry = {
                    "type": entry_type,
                    "timestamp": obj.get("timestamp", ""),
                    "message": obj.get("message", {}),
                }

                # Preserve isCompactSummary if present
                if obj.get("isCompactSummary"):
                    entry["isCompactSummary"] = True

                loglines.append(entry)
            except json.JSONDecodeError:
                continue

    return {"loglines": loglines}


class CredentialsError(Exception):
    """Raised when credentials cannot be obtained."""

    pass


def get_access_token_from_keychain():
    """Get access token from macOS keychain.

    Returns the access token or None if not found.
    Raises CredentialsError with helpful message on failure.
    """
    if platform.system() != "Darwin":
        return None

    try:
        result = subprocess.run(
            [
                "security",
                "find-generic-password",
                "-a",
                os.environ.get("USER", ""),
                "-s",
                "Claude Code-credentials",
                "-w",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return None

        # Parse the JSON to get the access token
        creds = json.loads(result.stdout.strip())
        return creds.get("claudeAiOauth", {}).get("accessToken")
    except (json.JSONDecodeError, subprocess.SubprocessError):
        return None


def get_org_uuid_from_config():
    """Get organization UUID from ~/.claude.json.

    Returns the organization UUID or None if not found.
    """
    config_path = Path.home() / ".claude.json"
    if not config_path.exists():
        return None

    try:
        with open(config_path) as f:
            config = json.load(f)
        return config.get("oauthAccount", {}).get("organizationUuid")
    except (json.JSONDecodeError, IOError):
        return None


def get_api_headers(token, org_uuid):
    """Build API request headers."""
    return {
        "Authorization": f"Bearer {token}",
        "anthropic-version": ANTHROPIC_VERSION,
        "Content-Type": "application/json",
        "x-organization-uuid": org_uuid,
    }


def fetch_sessions(token, org_uuid):
    """Fetch list of sessions from the API.

    Returns the sessions data as a dict.
    Raises httpx.HTTPError on network/API errors.
    """
    headers = get_api_headers(token, org_uuid)
    response = httpx.get(f"{API_BASE_URL}/sessions", headers=headers, timeout=30.0)
    response.raise_for_status()
    return response.json()


def fetch_session(token, org_uuid, session_id):
    """Fetch a specific session from the API.

    Returns the session data as a dict.
    Raises httpx.HTTPError on network/API errors.
    """
    headers = get_api_headers(token, org_uuid)
    response = httpx.get(
        f"{API_BASE_URL}/session_ingress/session/{session_id}",
        headers=headers,
        timeout=60.0,
    )
    response.raise_for_status()
    return response.json()


def detect_github_repo(loglines):
    """
    Detect GitHub repo from git push output in tool results.

    Looks for patterns like:
    - github.com/owner/repo/pull/new/branch (from git push messages)

    Returns the first detected repo (owner/name) or None.
    """
    for entry in loglines:
        message = entry.get("message", {})
        content = message.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_result":
                result_content = block.get("content", "")
                if isinstance(result_content, str):
                    match = GITHUB_REPO_PATTERN.search(result_content)
                    if match:
                        return match.group(1)
    return None


def extract_repo_from_session(session):
    """Extract GitHub repo from session metadata.

    Looks in session_context.outcomes for git_info.repo,
    or parses from session_context.sources URL.

    Returns repo as "owner/name" or None.
    """
    context = session.get("session_context", {})

    # Try outcomes first (has clean repo format)
    outcomes = context.get("outcomes", [])
    for outcome in outcomes:
        if outcome.get("type") == "git_repository":
            git_info = outcome.get("git_info", {})
            repo = git_info.get("repo")
            if repo:
                return repo

    # Fall back to sources URL
    sources = context.get("sources", [])
    for source in sources:
        if source.get("type") == "git_repository":
            url = source.get("url", "")
            # Parse github.com/owner/repo from URL
            if "github.com/" in url:
                # Extract owner/repo from https://github.com/owner/repo
                match = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git)?$", url)
                if match:
                    return match.group(1)

    return None


def enrich_sessions_with_repos(sessions, token=None, org_uuid=None, fetch_fn=None):
    """Enrich sessions with repo information from session metadata.

    Args:
        sessions: List of session dicts from the API
        token: Unused (kept for backward compatibility)
        org_uuid: Unused (kept for backward compatibility)
        fetch_fn: Unused (kept for backward compatibility)

    Returns:
        List of session dicts with 'repo' key added
    """
    enriched = []
    for session in sessions:
        session_copy = dict(session)
        session_copy["repo"] = extract_repo_from_session(session)
        enriched.append(session_copy)
    return enriched


def filter_sessions_by_repo(sessions, repo):
    """Filter sessions by repo.

    Args:
        sessions: List of session dicts with 'repo' key
        repo: Repo to filter by (owner/name), or None to return all

    Returns:
        Filtered list of sessions
    """
    if repo is None:
        return sessions
    return [s for s in sessions if s.get("repo") == repo]


def format_json(obj):
    try:
        if isinstance(obj, str):
            obj = json.loads(obj)
        formatted = json.dumps(obj, indent=2, ensure_ascii=False)
        return f'<pre class="json">{html.escape(formatted)}</pre>'
    except (json.JSONDecodeError, TypeError):
        return f"<pre>{html.escape(str(obj))}</pre>"


def render_markdown_text(text):
    if not text:
        return ""
    return markdown.markdown(text, extensions=["fenced_code", "tables"])


def is_json_like(text):
    if not text or not isinstance(text, str):
        return False
    text = text.strip()
    return (text.startswith("{") and text.endswith("}")) or (
        text.startswith("[") and text.endswith("]")
    )


def render_todo_write(tool_input, tool_id):
    todos = tool_input.get("todos", [])
    if not todos:
        return ""
    return _macros.todo_list(todos, tool_id)


def render_write_tool(tool_input, tool_id):
    """Render Write tool calls with file path header and content preview."""
    file_path = tool_input.get("file_path", "Unknown file")
    content = tool_input.get("content", "")
    return _macros.write_tool(file_path, content, tool_id)


def render_edit_tool(tool_input, tool_id):
    """Render Edit tool calls with diff-like old/new display."""
    file_path = tool_input.get("file_path", "Unknown file")
    old_string = tool_input.get("old_string", "")
    new_string = tool_input.get("new_string", "")
    replace_all = tool_input.get("replace_all", False)
    return _macros.edit_tool(file_path, old_string, new_string, replace_all, tool_id)


def render_bash_tool(tool_input, tool_id):
    """Render Bash tool calls with command as plain text."""
    command = tool_input.get("command", "")
    description = tool_input.get("description", "")
    return _macros.bash_tool(command, description, tool_id)


def render_content_block(block):
    if not isinstance(block, dict):
        return f"<p>{html.escape(str(block))}</p>"
    block_type = block.get("type", "")
    if block_type == "image":
        source = block.get("source", {})
        media_type = source.get("media_type", "image/png")
        data = source.get("data", "")
        return _macros.image_block(media_type, data)
    elif block_type == "thinking":
        content_html = render_markdown_text(block.get("thinking", ""))
        return _macros.thinking(content_html)
    elif block_type == "text":
        content_html = render_markdown_text(block.get("text", ""))
        return _macros.assistant_text(content_html)
    elif block_type == "tool_use":
        tool_name = block.get("name", "Unknown tool")
        tool_input = block.get("input", {})
        tool_id = block.get("id", "")
        if tool_name == "TodoWrite":
            return render_todo_write(tool_input, tool_id)
        if tool_name == "Write":
            return render_write_tool(tool_input, tool_id)
        if tool_name == "Edit":
            return render_edit_tool(tool_input, tool_id)
        if tool_name == "Bash":
            return render_bash_tool(tool_input, tool_id)
        description = tool_input.get("description", "")
        display_input = {k: v for k, v in tool_input.items() if k != "description"}
        input_json = json.dumps(display_input, indent=2, ensure_ascii=False)
        return _macros.tool_use(tool_name, description, input_json, tool_id)
    elif block_type == "tool_result":
        content = block.get("content", "")
        is_error = block.get("is_error", False)
        has_images = False

        # Check for git commits and render with styled cards
        if isinstance(content, str):
            commits_found = list(COMMIT_PATTERN.finditer(content))
            if commits_found:
                # Build commit cards + remaining content
                parts = []
                last_end = 0
                for match in commits_found:
                    # Add any content before this commit
                    before = content[last_end : match.start()].strip()
                    if before:
                        parts.append(f"<pre>{html.escape(before)}</pre>")

                    commit_hash = match.group(1)
                    commit_msg = match.group(2)
                    parts.append(
                        _macros.commit_card(commit_hash, commit_msg, _github_repo)
                    )
                    last_end = match.end()

                # Add any remaining content after last commit
                after = content[last_end:].strip()
                if after:
                    parts.append(f"<pre>{html.escape(after)}</pre>")

                content_html = "".join(parts)
            else:
                content_html = f"<pre>{html.escape(content)}</pre>"
        elif isinstance(content, list):
            # Handle tool result content that contains multiple blocks (text, images, etc.)
            parts = []
            for item in content:
                if isinstance(item, dict):
                    item_type = item.get("type", "")
                    if item_type == "text":
                        text = item.get("text", "")
                        if text:
                            parts.append(f"<pre>{html.escape(text)}</pre>")
                    elif item_type == "image":
                        source = item.get("source", {})
                        media_type = source.get("media_type", "image/png")
                        data = source.get("data", "")
                        if data:
                            parts.append(_macros.image_block(media_type, data))
                            has_images = True
                    else:
                        # Unknown type, render as JSON
                        parts.append(format_json(item))
                else:
                    # Non-dict item, escape as text
                    parts.append(f"<pre>{html.escape(str(item))}</pre>")
            content_html = "".join(parts) if parts else format_json(content)
        elif is_json_like(content):
            content_html = format_json(content)
        else:
            content_html = format_json(content)
        return _macros.tool_result(content_html, is_error, has_images)
    else:
        return format_json(block)


def render_user_message_content(message_data):
    content = message_data.get("content", "")
    if isinstance(content, str):
        if is_json_like(content):
            return _macros.user_content(format_json(content))
        return _macros.user_content(render_markdown_text(content))
    elif isinstance(content, list):
        return "".join(render_content_block(block) for block in content)
    return f"<p>{html.escape(str(content))}</p>"


def render_assistant_message(message_data):
    content = message_data.get("content", [])
    if not isinstance(content, list):
        return f"<p>{html.escape(str(content))}</p>"
    return "".join(render_content_block(block) for block in content)


def make_msg_id(timestamp):
    return f"msg-{timestamp.replace(':', '-').replace('.', '-')}"


def analyze_conversation(messages):
    """Analyze messages in a conversation to extract stats and long texts."""
    tool_counts = {}  # tool_name -> count
    long_texts = []
    commits = []  # list of (hash, message, timestamp)

    for log_type, message_json, timestamp in messages:
        if not message_json:
            continue
        try:
            message_data = json.loads(message_json)
        except json.JSONDecodeError:
            continue

        content = message_data.get("content", [])
        if not isinstance(content, list):
            continue

        for block in content:
            if not isinstance(block, dict):
                continue
            block_type = block.get("type", "")

            if block_type == "tool_use":
                tool_name = block.get("name", "Unknown")
                tool_counts[tool_name] = tool_counts.get(tool_name, 0) + 1
            elif block_type == "tool_result":
                # Check for git commit output
                result_content = block.get("content", "")
                if isinstance(result_content, str):
                    for match in COMMIT_PATTERN.finditer(result_content):
                        commits.append((match.group(1), match.group(2), timestamp))
            elif block_type == "text":
                text = block.get("text", "")
                if len(text) >= LONG_TEXT_THRESHOLD:
                    long_texts.append(text)

    return {
        "tool_counts": tool_counts,
        "long_texts": long_texts,
        "commits": commits,
    }


def format_tool_stats(tool_counts):
    """Format tool counts into a concise summary string."""
    if not tool_counts:
        return ""

    # Abbreviate common tool names
    abbrev = {
        "Bash": "bash",
        "Read": "read",
        "Write": "write",
        "Edit": "edit",
        "Glob": "glob",
        "Grep": "grep",
        "Task": "task",
        "TodoWrite": "todo",
        "WebFetch": "fetch",
        "WebSearch": "search",
    }

    parts = []
    for name, count in sorted(tool_counts.items(), key=lambda x: -x[1]):
        short_name = abbrev.get(name, name.lower())
        parts.append(f"{count} {short_name}")

    return " · ".join(parts)


def is_tool_result_message(message_data):
    """Check if a message contains only tool_result blocks."""
    content = message_data.get("content", [])
    if not isinstance(content, list):
        return False
    if not content:
        return False
    return all(
        isinstance(block, dict) and block.get("type") == "tool_result"
        for block in content
    )


def render_message(log_type, message_json, timestamp):
    if not message_json:
        return ""
    try:
        message_data = json.loads(message_json)
    except json.JSONDecodeError:
        return ""
    if log_type == "user":
        content_html = render_user_message_content(message_data)
        # Check if this is a tool result message
        if is_tool_result_message(message_data):
            role_class, role_label = "tool-reply", "Tool reply"
        else:
            role_class, role_label = "user", "User"
    elif log_type == "assistant":
        content_html = render_assistant_message(message_data)
        role_class, role_label = "assistant", "Assistant"
    else:
        return ""
    if not content_html.strip():
        return ""
    msg_id = make_msg_id(timestamp)
    return _macros.message(role_class, role_label, msg_id, timestamp, content_html)


CSS = """
:root { --bg-color: #f5f5f5; --card-bg: #ffffff; --user-bg: #e3f2fd; --user-border: #1976d2; --assistant-bg: #f5f5f5; --assistant-border: #9e9e9e; --thinking-bg: #fff8e1; --thinking-border: #ffc107; --thinking-text: #666; --tool-bg: #f3e5f5; --tool-border: #9c27b0; --tool-result-bg: #e8f5e9; --tool-error-bg: #ffebee; --text-color: #212121; --text-muted: #757575; --code-bg: #263238; --code-text: #aed581; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 16px; line-height: 1.6; }
.container { max-width: 800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin-bottom: 24px; padding-bottom: 8px; border-bottom: 2px solid var(--user-border); }
.header-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-bottom: 2px solid var(--user-border); padding-bottom: 8px; margin-bottom: 24px; }
.header-row h1 { border-bottom: none; padding-bottom: 0; margin-bottom: 0; flex: 1; min-width: 200px; }
.message { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.message.user { background: var(--user-bg); border-left: 4px solid var(--user-border); }
.message.assistant { background: var(--card-bg); border-left: 4px solid var(--assistant-border); }
.message.tool-reply { background: #fff8e1; border-left: 4px solid #ff9800; }
.tool-reply .role-label { color: #e65100; }
.tool-reply .tool-result { background: transparent; padding: 0; margin: 0; }
.tool-reply .tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.message-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.role-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.user .role-label { color: var(--user-border); }
time { color: var(--text-muted); font-size: 0.8rem; }
.timestamp-link { color: inherit; text-decoration: none; }
.timestamp-link:hover { text-decoration: underline; }
.message:target { animation: highlight 2s ease-out; }
@keyframes highlight { 0% { background-color: rgba(25, 118, 210, 0.2); } 100% { background-color: transparent; } }
.message-content { padding: 16px; }
.message-content p { margin: 0 0 12px 0; }
.message-content p:last-child { margin-bottom: 0; }
.thinking { background: var(--thinking-bg); border: 1px solid var(--thinking-border); border-radius: 8px; padding: 12px; margin: 12px 0; font-size: 0.9rem; color: var(--thinking-text); }
.thinking-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: #f57c00; margin-bottom: 8px; }
.thinking p { margin: 8px 0; }
.assistant-text { margin: 8px 0; }
.tool-use { background: var(--tool-bg); border: 1px solid var(--tool-border); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-header { font-weight: 600; color: var(--tool-border); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.tool-icon { font-size: 1.1rem; }
.tool-description { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 8px; font-style: italic; }
.tool-result { background: var(--tool-result-bg); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-result.tool-error { background: var(--tool-error-bg); }
.file-tool { border-radius: 8px; padding: 12px; margin: 12px 0; }
.write-tool { background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%); border: 1px solid #4caf50; }
.edit-tool { background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%); border: 1px solid #ff9800; }
.file-tool-header { font-weight: 600; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.write-header { color: #2e7d32; }
.edit-header { color: #e65100; }
.file-tool-icon { font-size: 1rem; }
.file-tool-path { font-family: monospace; background: rgba(0,0,0,0.08); padding: 2px 8px; border-radius: 4px; }
.file-tool-fullpath { font-family: monospace; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; word-break: break-all; }
.file-content { margin: 0; }
.edit-section { display: flex; margin: 4px 0; border-radius: 4px; overflow: hidden; }
.edit-label { padding: 8px 12px; font-weight: bold; font-family: monospace; display: flex; align-items: flex-start; }
.edit-old { background: #fce4ec; }
.edit-old .edit-label { color: #b71c1c; background: #f8bbd9; }
.edit-old .edit-content { color: #880e4f; }
.edit-new { background: #e8f5e9; }
.edit-new .edit-label { color: #1b5e20; background: #a5d6a7; }
.edit-new .edit-content { color: #1b5e20; }
.edit-content { margin: 0; flex: 1; background: transparent; font-size: 0.85rem; }
.edit-replace-all { font-size: 0.75rem; font-weight: normal; color: var(--text-muted); }
.write-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #e6f4ea); }
.edit-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff0e5); }
.todo-list { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); border: 1px solid #81c784; border-radius: 8px; padding: 12px; margin: 12px 0; }
.todo-header { font-weight: 600; color: #2e7d32; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.todo-items { list-style: none; margin: 0; padding: 0; }
.todo-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(0,0,0,0.06); font-size: 0.9rem; }
.todo-item:last-child { border-bottom: none; }
.todo-icon { flex-shrink: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 50%; }
.todo-completed .todo-icon { color: #2e7d32; background: rgba(46, 125, 50, 0.15); }
.todo-completed .todo-content { color: #558b2f; text-decoration: line-through; }
.todo-in-progress .todo-icon { color: #f57c00; background: rgba(245, 124, 0, 0.15); }
.todo-in-progress .todo-content { color: #e65100; font-weight: 500; }
.todo-pending .todo-icon { color: #757575; background: rgba(0,0,0,0.05); }
.todo-pending .todo-content { color: #616161; }
pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }
pre.json { color: #e0e0e0; }
code { background: rgba(0,0,0,0.08); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre code { background: none; padding: 0; }
.user-content { margin: 0; }
.truncatable { position: relative; }
.truncatable.truncated .truncatable-content { max-height: 200px; overflow: hidden; }
.truncatable.truncated::after { content: ''; position: absolute; bottom: 32px; left: 0; right: 0; height: 60px; background: linear-gradient(to bottom, transparent, var(--card-bg)); pointer-events: none; }
.message.user .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--user-bg)); }
.message.tool-reply .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.tool-use .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-bg)); }
.tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-result-bg)); }
.expand-btn { display: none; width: 100%; padding: 8px 16px; margin-top: 4px; background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; cursor: pointer; font-size: 0.85rem; color: var(--text-muted); }
.expand-btn:hover { background: rgba(0,0,0,0.1); }
.truncatable.truncated .expand-btn, .truncatable.expanded .expand-btn { display: block; }
.pagination { display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; }
.pagination a, .pagination span { padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; }
.pagination a { background: var(--card-bg); color: var(--user-border); border: 1px solid var(--user-border); }
.pagination a:hover { background: var(--user-bg); }
.pagination .current { background: var(--user-border); color: white; }
.pagination .disabled { color: var(--text-muted); border: 1px solid #ddd; }
.pagination .index-link { background: var(--user-border); color: white; }
details.continuation { margin-bottom: 16px; }
details.continuation summary { cursor: pointer; padding: 12px 16px; background: var(--user-bg); border-left: 4px solid var(--user-border); border-radius: 12px; font-weight: 500; color: var(--text-muted); }
details.continuation summary:hover { background: rgba(25, 118, 210, 0.15); }
details.continuation[open] summary { border-radius: 12px 12px 0 0; margin-bottom: 0; }
.index-item { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: var(--user-bg); border-left: 4px solid var(--user-border); }
.index-item a { display: block; text-decoration: none; color: inherit; }
.index-item a:hover { background: rgba(25, 118, 210, 0.1); }
.index-item-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.index-item-number { font-weight: 600; color: var(--user-border); }
.index-item-content { padding: 16px; }
.index-item-stats { padding: 8px 16px 12px 32px; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.06); }
.index-item-commit { margin-top: 6px; padding: 4px 8px; background: #fff3e0; border-radius: 4px; font-size: 0.85rem; color: #e65100; }
.index-item-commit code { background: rgba(0,0,0,0.08); padding: 1px 4px; border-radius: 3px; font-size: 0.8rem; margin-right: 6px; }
.commit-card { margin: 8px 0; padding: 10px 14px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 6px; }
.commit-card a { text-decoration: none; color: #5d4037; display: block; }
.commit-card a:hover { color: #e65100; }
.commit-card-hash { font-family: monospace; color: #e65100; font-weight: 600; margin-right: 8px; }
.index-commit { margin-bottom: 12px; padding: 10px 16px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.index-commit a { display: block; text-decoration: none; color: inherit; }
.index-commit a:hover { background: rgba(255, 152, 0, 0.1); margin: -10px -16px; padding: 10px 16px; border-radius: 8px; }
.index-commit-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; margin-bottom: 4px; }
.index-commit-hash { font-family: monospace; color: #e65100; font-weight: 600; }
.index-commit-msg { color: #5d4037; }
.index-item-long-text { margin-top: 8px; padding: 12px; background: var(--card-bg); border-radius: 8px; border-left: 3px solid var(--assistant-border); }
.index-item-long-text .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--card-bg)); }
.index-item-long-text-content { color: var(--text-color); }
#search-box { display: none; align-items: center; gap: 8px; }
#search-box input { padding: 6px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; width: 180px; }
#search-box button, #modal-search-btn, #modal-close-btn { background: var(--user-border); color: white; border: none; border-radius: 6px; padding: 6px 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#search-box button:hover, #modal-search-btn:hover { background: #1565c0; }
#modal-close-btn { background: var(--text-muted); margin-left: 8px; }
#modal-close-btn:hover { background: #616161; }
#search-modal[open] { border: none; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.2); padding: 0; width: 90vw; max-width: 900px; height: 80vh; max-height: 80vh; display: flex; flex-direction: column; }
#search-modal::backdrop { background: rgba(0,0,0,0.5); }
.search-modal-header { display: flex; align-items: center; gap: 8px; padding: 16px; border-bottom: 1px solid var(--assistant-border); background: var(--bg-color); border-radius: 12px 12px 0 0; }
.search-modal-header input { flex: 1; padding: 8px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; }
#search-status { padding: 8px 16px; font-size: 0.85rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
#search-results { flex: 1; overflow-y: auto; padding: 16px; }
.search-result { margin-bottom: 16px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.search-result a { display: block; text-decoration: none; color: inherit; }
.search-result a:hover { background: rgba(25, 118, 210, 0.05); }
.search-result-page { padding: 6px 12px; background: rgba(0,0,0,0.03); font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
.search-result-content { padding: 12px; }
.search-result mark { background: #fff59d; padding: 1px 2px; border-radius: 2px; }
@media (max-width: 600px) { body { padding: 8px; } .message, .index-item { border-radius: 8px; } .message-content, .index-item-content { padding: 12px; } pre { font-size: 0.8rem; padding: 8px; } #search-box input { width: 120px; } #search-modal[open] { width: 95vw; height: 90vh; } }
"""

JS = """
document.querySelectorAll('time[data-timestamp]').forEach(function(el) {
    const timestamp = el.getAttribute('data-timestamp');
    const date = new Date(timestamp);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const timeStr = date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    if (isToday) { el.textContent = timeStr; }
    else { el.textContent = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' + timeStr; }
});
document.querySelectorAll('pre.json').forEach(function(el) {
    let text = el.textContent;
    text = text.replace(/"([^"]+)":/g, '<span style="color: #ce93d8">"$1"</span>:');
    text = text.replace(/: "([^"]*)"/g, ': <span style="color: #81d4fa">"$1"</span>');
    text = text.replace(/: (\\d+)/g, ': <span style="color: #ffcc80">$1</span>');
    text = text.replace(/: (true|false|null)/g, ': <span style="color: #f48fb1">$1</span>');
    el.innerHTML = text;
});
document.querySelectorAll('.truncatable').forEach(function(wrapper) {
    const content = wrapper.querySelector('.truncatable-content');
    const btn = wrapper.querySelector('.expand-btn');
    if (content.scrollHeight > 250) {
        wrapper.classList.add('truncated');
        btn.addEventListener('click', function() {
            if (wrapper.classList.contains('truncated')) { wrapper.classList.remove('truncated'); wrapper.classList.add('expanded'); btn.textContent = 'Show less'; }
            else { wrapper.classList.remove('expanded'); wrapper.classList.add('truncated'); btn.textContent = 'Show more'; }
        });
    }
});
"""

# JavaScript to fix relative URLs when served via gisthost.github.io or gistpreview.github.io
# Fixes issue #26: Pagination links broken on gisthost.github.io
GIST_PREVIEW_JS = r"""
(function() {
    var hostname = window.location.hostname;
    if (hostname !== 'gisthost.github.io' && hostname !== 'gistpreview.github.io') return;
    // URL format: https://gisthost.github.io/?GIST_ID/filename.html
    var match = window.location.search.match(/^\?([^/]+)/);
    if (!match) return;
    var gistId = match[1];

    function rewriteLinks(root) {
        (root || document).querySelectorAll('a[href]').forEach(function(link) {
            var href = link.getAttribute('href');
            // Skip already-rewritten links (issue #26 fix)
            if (href.startsWith('?')) return;
            // Skip external links and anchors
            if (href.startsWith('http') || href.startsWith('#') || href.startsWith('//')) return;
            // Handle anchor in relative URL (e.g., page-001.html#msg-123)
            var parts = href.split('#');
            var filename = parts[0];
            var anchor = parts.length > 1 ? '#' + parts[1] : '';
            link.setAttribute('href', '?' + gistId + '/' + filename + anchor);
        });
    }

    // Run immediately
    rewriteLinks();

    // Also run on DOMContentLoaded in case DOM isn't ready yet
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() { rewriteLinks(); });
    }

    // Use MutationObserver to catch dynamically added content
    // gistpreview.github.io may add content after initial load
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1) { // Element node
                    rewriteLinks(node);
                    // Also check if the node itself is a link
                    if (node.tagName === 'A' && node.getAttribute('href')) {
                        var href = node.getAttribute('href');
                        if (!href.startsWith('?') && !href.startsWith('http') &&
                            !href.startsWith('#') && !href.startsWith('//')) {
                            var parts = href.split('#');
                            var filename = parts[0];
                            var anchor = parts.length > 1 ? '#' + parts[1] : '';
                            node.setAttribute('href', '?' + gistId + '/' + filename + anchor);
                        }
                    }
                }
            });
        });
    });

    // Start observing once body exists
    function startObserving() {
        if (document.body) {
            observer.observe(document.body, { childList: true, subtree: true });
        } else {
            setTimeout(startObserving, 10);
        }
    }
    startObserving();

    // Handle fragment navigation after dynamic content loads
    // gisthost.github.io/gistpreview.github.io loads content dynamically, so the browser's
    // native fragment navigation fails because the element doesn't exist yet
    function scrollToFragment() {
        var hash = window.location.hash;
        if (!hash) return false;
        var targetId = hash.substring(1);
        var target = document.getElementById(targetId);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            return true;
        }
        return false;
    }

    // Try immediately in case content is already loaded
    if (!scrollToFragment()) {
        // Retry with increasing delays to handle dynamic content loading
        var delays = [100, 300, 500, 1000, 2000];
        delays.forEach(function(delay) {
            setTimeout(scrollToFragment, delay);
        });
    }
})();
"""


def inject_gist_preview_js(output_dir):
    """Inject gist preview JavaScript into all HTML files in the output directory."""
    output_dir = Path(output_dir)
    for html_file in output_dir.glob("*.html"):
        content = html_file.read_text(encoding="utf-8")
        # Insert the gist preview JS before the closing </body> tag
        if "</body>" in content:
            content = content.replace(
                "</body>", f"<script>{GIST_PREVIEW_JS}</script>\n</body>"
            )
            html_file.write_text(content, encoding="utf-8")


def create_gist(output_dir, public=False):
    """Create a GitHub gist from the HTML files in output_dir.

    Returns the gist ID on success, or raises click.ClickException on failure.
    """
    output_dir = Path(output_dir)
    html_files = list(output_dir.glob("*.html"))
    if not html_files:
        raise click.ClickException("No HTML files found to upload to gist.")

    # Build the gh gist create command
    # gh gist create file1 file2 ... --public/--private
    cmd = ["gh", "gist", "create"]
    cmd.extend(str(f) for f in sorted(html_files))
    if public:
        cmd.append("--public")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        # Output is the gist URL, e.g., https://gist.github.com/username/GIST_ID
        gist_url = result.stdout.strip()
        # Extract gist ID from URL
        gist_id = gist_url.rstrip("/").split("/")[-1]
        return gist_id, gist_url
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        raise click.ClickException(f"Failed to create gist: {error_msg}")
    except FileNotFoundError:
        raise click.ClickException(
            "gh CLI not found. Install it from https://cli.github.com/ and run 'gh auth login'."
        )


def generate_pagination_html(current_page, total_pages):
    return _macros.pagination(current_page, total_pages)


def generate_index_pagination_html(total_pages):
    """Generate pagination for index page where Index is current (first page)."""
    return _macros.index_pagination(total_pages)


def generate_html(json_path, output_dir, github_repo=None):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    # Load session file (supports both JSON and JSONL)
    data = parse_session_file(json_path)

    loglines = data.get("loglines", [])

    # Auto-detect GitHub repo if not provided
    if github_repo is None:
        github_repo = detect_github_repo(loglines)
        if github_repo:
            print(f"Auto-detected GitHub repo: {github_repo}")
        else:
            print(
                "Warning: Could not auto-detect GitHub repo. Commit links will be disabled."
            )

    # Set module-level variable for render functions
    global _github_repo
    _github_repo = github_repo

    conversations = []
    current_conv = None
    for entry in loglines:
        log_type = entry.get("type")
        timestamp = entry.get("timestamp", "")
        is_compact_summary = entry.get("isCompactSummary", False)
        message_data = entry.get("message", {})
        if not message_data:
            continue
        # Convert message dict to JSON string for compatibility with existing render functions
        message_json = json.dumps(message_data)
        is_user_prompt = False
        user_text = None
        if log_type == "user":
            content = message_data.get("content", "")
            text = extract_text_from_content(content)
            if text:
                is_user_prompt = True
                user_text = text
        if is_user_prompt:
            if current_conv:
                conversations.append(current_conv)
            current_conv = {
                "user_text": user_text,
                "timestamp": timestamp,
                "messages": [(log_type, message_json, timestamp)],
                "is_continuation": bool(is_compact_summary),
            }
        elif current_conv:
            current_conv["messages"].append((log_type, message_json, timestamp))
    if current_conv:
        conversations.append(current_conv)

    total_convs = len(conversations)
    total_pages = (total_convs + PROMPTS_PER_PAGE - 1) // PROMPTS_PER_PAGE

    for page_num in range(1, total_pages + 1):
        start_idx = (page_num - 1) * PROMPTS_PER_PAGE
        end_idx = min(start_idx + PROMPTS_PER_PAGE, total_convs)
        page_convs = conversations[start_idx:end_idx]
        messages_html = []
        for conv in page_convs:
            is_first = True
            for log_type, message_json, timestamp in conv["messages"]:
                msg_html = render_message(log_type, message_json, timestamp)
                if msg_html:
                    # Wrap continuation summaries in collapsed details
                    if is_first and conv.get("is_continuation"):
                        msg_html = f'<details class="continuation"><summary>Session continuation summary</summary>{msg_html}</details>'
                    messages_html.append(msg_html)
                is_first = False
        pagination_html = generate_pagination_html(page_num, total_pages)
        page_template = get_template("page.html")
        page_content = page_template.render(
            css=CSS,
            js=JS,
            page_num=page_num,
            total_pages=total_pages,
            pagination_html=pagination_html,
            messages_html="".join(messages_html),
        )
        (output_dir / f"page-{page_num:03d}.html").write_text(
            page_content, encoding="utf-8"
        )
        print(f"Generated page-{page_num:03d}.html")

    # Calculate overall stats and collect all commits for timeline
    total_tool_counts = {}
    total_messages = 0
    all_commits = []  # (timestamp, hash, message, page_num, conv_index)
    for i, conv in enumerate(conversations):
        total_messages += len(conv["messages"])
        stats = analyze_conversation(conv["messages"])
        for tool, count in stats["tool_counts"].items():
            total_tool_counts[tool] = total_tool_counts.get(tool, 0) + count
        page_num = (i // PROMPTS_PER_PAGE) + 1
        for commit_hash, commit_msg, commit_ts in stats["commits"]:
            all_commits.append((commit_ts, commit_hash, commit_msg, page_num, i))
    total_tool_calls = sum(total_tool_counts.values())
    total_commits = len(all_commits)

    # Build timeline items: prompts and commits merged by timestamp
    timeline_items = []

    # Add prompts
    prompt_num = 0
    for i, conv in enumerate(conversations):
        if conv.get("is_continuation"):
            continue
        if conv["user_text"].startswith("Stop hook feedback:"):
            continue
        prompt_num += 1
        page_num = (i // PROMPTS_PER_PAGE) + 1
        msg_id = make_msg_id(conv["timestamp"])
        link = f"page-{page_num:03d}.html#{msg_id}"
        rendered_content = render_markdown_text(conv["user_text"])

        # Collect all messages including from subsequent continuation conversations
        # This ensures long_texts from continuations appear with the original prompt
        all_messages = list(conv["messages"])
        for j in range(i + 1, len(conversations)):
            if not conversations[j].get("is_continuation"):
                break
            all_messages.extend(conversations[j]["messages"])

        # Analyze conversation for stats (excluding commits from inline display now)
        stats = analyze_conversation(all_messages)
        tool_stats_str = format_tool_stats(stats["tool_counts"])

        long_texts_html = ""
        for lt in stats["long_texts"]:
            rendered_lt = render_markdown_text(lt)
            long_texts_html += _macros.index_long_text(rendered_lt)

        stats_html = _macros.index_stats(tool_stats_str, long_texts_html)

        item_html = _macros.index_item(
            prompt_num, link, conv["timestamp"], rendered_content, stats_html
        )
        timeline_items.append((conv["timestamp"], "prompt", item_html))

    # Add commits as separate timeline items
    for commit_ts, commit_hash, commit_msg, page_num, conv_idx in all_commits:
        item_html = _macros.index_commit(
            commit_hash, commit_msg, commit_ts, _github_repo
        )
        timeline_items.append((commit_ts, "commit", item_html))

    # Sort by timestamp
    timeline_items.sort(key=lambda x: x[0])
    index_items = [item[2] for item in timeline_items]

    index_pagination = generate_index_pagination_html(total_pages)
    index_template = get_template("index.html")
    index_content = index_template.render(
        css=CSS,
        js=JS,
        pagination_html=index_pagination,
        prompt_num=prompt_num,
        total_messages=total_messages,
        total_tool_calls=total_tool_calls,
        total_commits=total_commits,
        total_pages=total_pages,
        index_items_html="".join(index_items),
    )
    index_path = output_dir / "index.html"
    index_path.write_text(index_content, encoding="utf-8")
    print(
        f"Generated {index_path.resolve()} ({total_convs} prompts, {total_pages} pages)"
    )


@click.group(cls=DefaultGroup, default="local", default_if_no_args=True)
@click.version_option(None, "-v", "--version", package_name="claude-code-transcripts")
def cli():
    """Convert Claude Code session JSON to mobile-friendly HTML pages."""
    pass


@cli.command("local")
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    help="Output directory. If not specified, writes to temp dir and opens in browser.",
)
@click.option(
    "-a",
    "--output-auto",
    is_flag=True,
    help="Auto-name output subdirectory based on session filename (uses -o as parent, or current dir).",
)
@click.option(
    "--repo",
    help="GitHub repo (owner/name) for commit links. Auto-detected from git push output if not specified.",
)
@click.option(
    "--gist",
    is_flag=True,
    help="Upload to GitHub Gist and output a gisthost.github.io URL.",
)
@click.option(
    "--json",
    "include_json",
    is_flag=True,
    help="Include the original JSONL session file in the output directory.",
)
@click.option(
    "--open",
    "open_browser",
    is_flag=True,
    help="Open the generated index.html in your default browser (default if no -o specified).",
)
@click.option(
    "--limit",
    default=10,
    help="Maximum number of sessions to show (default: 10)",
)
def local_cmd(output, output_auto, repo, gist, include_json, open_browser, limit):
    """Select and convert a local Claude Code session to HTML."""
    projects_folder = Path.home() / ".claude" / "projects"

    if not projects_folder.exists():
        click.echo(f"Projects folder not found: {projects_folder}")
        click.echo("No local Claude Code sessions available.")
        return

    click.echo("Loading local sessions...")
    results = find_local_sessions(projects_folder, limit=limit)

    if not results:
        click.echo("No local sessions found.")
        return

    # Build choices for questionary
    choices = []
    for filepath, summary in results:
        stat = filepath.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        size_kb = stat.st_size / 1024
        date_str = mod_time.strftime("%Y-%m-%d %H:%M")
        # Truncate summary if too long
        if len(summary) > 50:
            summary = summary[:47] + "..."
        display = f"{date_str}  {size_kb:5.0f} KB  {summary}"
        choices.append(questionary.Choice(title=display, value=filepath))

    selected = questionary.select(
        "Select a session to convert:",
        choices=choices,
    ).ask()

    if selected is None:
        click.echo("No session selected.")
        return

    session_file = selected

    # Determine output directory and whether to open browser
    # If no -o specified, use temp dir and open browser by default
    auto_open = output is None and not gist and not output_auto
    if output_auto:
        # Use -o as parent dir (or current dir), with auto-named subdirectory
        parent_dir = Path(output) if output else Path(".")
        output = parent_dir / session_file.stem
    elif output is None:
        output = Path(tempfile.gettempdir()) / f"claude-session-{session_file.stem}"

    output = Path(output)
    generate_html(session_file, output, github_repo=repo)

    # Show output directory
    click.echo(f"Output: {output.resolve()}")

    # Copy JSONL file to output directory if requested
    if include_json:
        output.mkdir(exist_ok=True)
        json_dest = output / session_file.name
        shutil.copy(session_file, json_dest)
        json_size_kb = json_dest.stat().st_size / 1024
        click.echo(f"JSONL: {json_dest} ({json_size_kb:.1f} KB)")

    if gist:
        # Inject gist preview JS and create gist
        inject_gist_preview_js(output)
        click.echo("Creating GitHub gist...")
        gist_id, gist_url = create_gist(output)
        preview_url = f"https://gisthost.github.io/?{gist_id}/index.html"
        click.echo(f"Gist: {gist_url}")
        click.echo(f"Preview: {preview_url}")

    if open_browser or auto_open:
        index_url = (output / "index.html").resolve().as_uri()
        webbrowser.open(index_url)


def is_url(path):
    """Check if a path is a URL (starts with http:// or https://)."""
    return path.startswith("http://") or path.startswith("https://")


def fetch_url_to_tempfile(url):
    """Fetch a URL and save to a temporary file.

    Returns the Path to the temporary file.
    Raises click.ClickException on network errors.
    """
    try:
        response = httpx.get(url, timeout=60.0, follow_redirects=True)
        response.raise_for_status()
    except httpx.RequestError as e:
        raise click.ClickException(f"Failed to fetch URL: {e}")
    except httpx.HTTPStatusError as e:
        raise click.ClickException(
            f"Failed to fetch URL: {e.response.status_code} {e.response.reason_phrase}"
        )

    # Determine file extension from URL
    url_path = url.split("?")[0]  # Remove query params
    if url_path.endswith(".jsonl"):
        suffix = ".jsonl"
    elif url_path.endswith(".json"):
        suffix = ".json"
    else:
        suffix = ".jsonl"  # Default to JSONL

    # Extract a name from the URL for the temp file
    url_name = Path(url_path).stem or "session"

    temp_dir = Path(tempfile.gettempdir())
    temp_file = temp_dir / f"claude-url-{url_name}{suffix}"
    temp_file.write_text(response.text, encoding="utf-8")
    return temp_file


@cli.command("json")
@click.argument("json_file", type=click.Path())
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    help="Output directory. If not specified, writes to temp dir and opens in browser.",
)
@click.option(
    "-a",
    "--output-auto",
    is_flag=True,
    help="Auto-name output subdirectory based on filename (uses -o as parent, or current dir).",
)
@click.option(
    "--repo",
    help="GitHub repo (owner/name) for commit links. Auto-detected from git push output if not specified.",
)
@click.option(
    "--gist",
    is_flag=True,
    help="Upload to GitHub Gist and output a gisthost.github.io URL.",
)
@click.option(
    "--json",
    "include_json",
    is_flag=True,
    help="Include the original JSON session file in the output directory.",
)
@click.option(
    "--open",
    "open_browser",
    is_flag=True,
    help="Open the generated index.html in your default browser (default if no -o specified).",
)
def json_cmd(json_file, output, output_auto, repo, gist, include_json, open_browser):
    """Convert a Claude Code session JSON/JSONL file or URL to HTML."""
    # Handle URL input
    if is_url(json_file):
        click.echo(f"Fetching {json_file}...")
        temp_file = fetch_url_to_tempfile(json_file)
        json_file_path = temp_file
        # Use URL path for naming
        url_name = Path(json_file.split("?")[0]).stem or "session"
    else:
        # Validate that local file exists
        json_file_path = Path(json_file)
        if not json_file_path.exists():
            raise click.ClickException(f"File not found: {json_file}")
        url_name = None

    # Determine output directory and whether to open browser
    # If no -o specified, use temp dir and open browser by default
    auto_open = output is None and not gist and not output_auto
    if output_auto:
        # Use -o as parent dir (or current dir), with auto-named subdirectory
        parent_dir = Path(output) if output else Path(".")
        output = parent_dir / (url_name or json_file_path.stem)
    elif output is None:
        output = (
            Path(tempfile.gettempdir())
            / f"claude-session-{url_name or json_file_path.stem}"
        )

    output = Path(output)
    generate_html(json_file_path, output, github_repo=repo)

    # Show output directory
    click.echo(f"Output: {output.resolve()}")

    # Copy JSON file to output directory if requested
    if include_json:
        output.mkdir(exist_ok=True)
        json_dest = output / json_file_path.name
        shutil.copy(json_file_path, json_dest)
        json_size_kb = json_dest.stat().st_size / 1024
        click.echo(f"JSON: {json_dest} ({json_size_kb:.1f} KB)")

    if gist:
        # Inject gist preview JS and create gist
        inject_gist_preview_js(output)
        click.echo("Creating GitHub gist...")
        gist_id, gist_url = create_gist(output)
        preview_url = f"https://gisthost.github.io/?{gist_id}/index.html"
        click.echo(f"Gist: {gist_url}")
        click.echo(f"Preview: {preview_url}")

    if open_browser or auto_open:
        index_url = (output / "index.html").resolve().as_uri()
        webbrowser.open(index_url)


def resolve_credentials(token, org_uuid):
    """Resolve token and org_uuid from arguments or auto-detect.

    Returns (token, org_uuid) tuple.
    Raises click.ClickException if credentials cannot be resolved.
    """
    # Get token
    if token is None:
        token = get_access_token_from_keychain()
        if token is None:
            if platform.system() == "Darwin":
                raise click.ClickException(
                    "Could not retrieve access token from macOS keychain. "
                    "Make sure you are logged into Claude Code, or provide --token."
                )
            else:
                raise click.ClickException(
                    "On non-macOS platforms, you must provide --token with your access token."
                )

    # Get org UUID
    if org_uuid is None:
        org_uuid = get_org_uuid_from_config()
        if org_uuid is None:
            raise click.ClickException(
                "Could not find organization UUID in ~/.claude.json. "
                "Provide --org-uuid with your organization UUID."
            )

    return token, org_uuid


def format_session_for_display(session_data):
    """Format a session for display in the list or picker.

    Shows repo first (if available), then date, then title.
    Returns a formatted string.
    """
    title = session_data.get("title", "Untitled")
    created_at = session_data.get("created_at", "")
    repo = session_data.get("repo")
    # Truncate title if too long
    if len(title) > 50:
        title = title[:47] + "..."
    # Format: repo (or placeholder)  date  title
    repo_display = repo if repo else "(no repo)"
    date_display = created_at[:19] if created_at else "N/A"
    return f"{repo_display:30}  {date_display:19}  {title}"


def generate_html_from_session_data(session_data, output_dir, github_repo=None):
    """Generate HTML from session data dict (instead of file path)."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    loglines = session_data.get("loglines", [])

    # Auto-detect GitHub repo if not provided
    if github_repo is None:
        github_repo = detect_github_repo(loglines)
        if github_repo:
            click.echo(f"Auto-detected GitHub repo: {github_repo}")

    # Set module-level variable for render functions
    global _github_repo
    _github_repo = github_repo

    conversations = []
    current_conv = None
    for entry in loglines:
        log_type = entry.get("type")
        timestamp = entry.get("timestamp", "")
        is_compact_summary = entry.get("isCompactSummary", False)
        message_data = entry.get("message", {})
        if not message_data:
            continue
        # Convert message dict to JSON string for compatibility with existing render functions
        message_json = json.dumps(message_data)
        is_user_prompt = False
        user_text = None
        if log_type == "user":
            content = message_data.get("content", "")
            text = extract_text_from_content(content)
            if text:
                is_user_prompt = True
                user_text = text
        if is_user_prompt:
            if current_conv:
                conversations.append(current_conv)
            current_conv = {
                "user_text": user_text,
                "timestamp": timestamp,
                "messages": [(log_type, message_json, timestamp)],
                "is_continuation": bool(is_compact_summary),
            }
        elif current_conv:
            current_conv["messages"].append((log_type, message_json, timestamp))
    if current_conv:
        conversations.append(current_conv)

    total_convs = len(conversations)
    total_pages = (total_convs + PROMPTS_PER_PAGE - 1) // PROMPTS_PER_PAGE

    for page_num in range(1, total_pages + 1):
        start_idx = (page_num - 1) * PROMPTS_PER_PAGE
        end_idx = min(start_idx + PROMPTS_PER_PAGE, total_convs)
        page_convs = conversations[start_idx:end_idx]
        messages_html = []
        for conv in page_convs:
            is_first = True
            for log_type, message_json, timestamp in conv["messages"]:
                msg_html = render_message(log_type, message_json, timestamp)
                if msg_html:
                    # Wrap continuation summaries in collapsed details
                    if is_first and conv.get("is_continuation"):
                        msg_html = f'<details class="continuation"><summary>Session continuation summary</summary>{msg_html}</details>'
                    messages_html.append(msg_html)
                is_first = False
        pagination_html = generate_pagination_html(page_num, total_pages)
        page_template = get_template("page.html")
        page_content = page_template.render(
            css=CSS,
            js=JS,
            page_num=page_num,
            total_pages=total_pages,
            pagination_html=pagination_html,
            messages_html="".join(messages_html),
        )
        (output_dir / f"page-{page_num:03d}.html").write_text(
            page_content, encoding="utf-8"
        )
        click.echo(f"Generated page-{page_num:03d}.html")

    # Calculate overall stats and collect all commits for timeline
    total_tool_counts = {}
    total_messages = 0
    all_commits = []  # (timestamp, hash, message, page_num, conv_index)
    for i, conv in enumerate(conversations):
        total_messages += len(conv["messages"])
        stats = analyze_conversation(conv["messages"])
        for tool, count in stats["tool_counts"].items():
            total_tool_counts[tool] = total_tool_counts.get(tool, 0) + count
        page_num = (i // PROMPTS_PER_PAGE) + 1
        for commit_hash, commit_msg, commit_ts in stats["commits"]:
            all_commits.append((commit_ts, commit_hash, commit_msg, page_num, i))
    total_tool_calls = sum(total_tool_counts.values())
    total_commits = len(all_commits)

    # Build timeline items: prompts and commits merged by timestamp
    timeline_items = []

    # Add prompts
    prompt_num = 0
    for i, conv in enumerate(conversations):
        if conv.get("is_continuation"):
            continue
        if conv["user_text"].startswith("Stop hook feedback:"):
            continue
        prompt_num += 1
        page_num = (i // PROMPTS_PER_PAGE) + 1
        msg_id = make_msg_id(conv["timestamp"])
        link = f"page-{page_num:03d}.html#{msg_id}"
        rendered_content = render_markdown_text(conv["user_text"])

        # Collect all messages including from subsequent continuation conversations
        # This ensures long_texts from continuations appear with the original prompt
        all_messages = list(conv["messages"])
        for j in range(i + 1, len(conversations)):
            if not conversations[j].get("is_continuation"):
                break
            all_messages.extend(conversations[j]["messages"])

        # Analyze conversation for stats (excluding commits from inline display now)
        stats = analyze_conversation(all_messages)
        tool_stats_str = format_tool_stats(stats["tool_counts"])

        long_texts_html = ""
        for lt in stats["long_texts"]:
            rendered_lt = render_markdown_text(lt)
            long_texts_html += _macros.index_long_text(rendered_lt)

        stats_html = _macros.index_stats(tool_stats_str, long_texts_html)

        item_html = _macros.index_item(
            prompt_num, link, conv["timestamp"], rendered_content, stats_html
        )
        timeline_items.append((conv["timestamp"], "prompt", item_html))

    # Add commits as separate timeline items
    for commit_ts, commit_hash, commit_msg, page_num, conv_idx in all_commits:
        item_html = _macros.index_commit(
            commit_hash, commit_msg, commit_ts, _github_repo
        )
        timeline_items.append((commit_ts, "commit", item_html))

    # Sort by timestamp
    timeline_items.sort(key=lambda x: x[0])
    index_items = [item[2] for item in timeline_items]

    index_pagination = generate_index_pagination_html(total_pages)
    index_template = get_template("index.html")
    index_content = index_template.render(
        css=CSS,
        js=JS,
        pagination_html=index_pagination,
        prompt_num=prompt_num,
        total_messages=total_messages,
        total_tool_calls=total_tool_calls,
        total_commits=total_commits,
        total_pages=total_pages,
        index_items_html="".join(index_items),
    )
    index_path = output_dir / "index.html"
    index_path.write_text(index_content, encoding="utf-8")
    click.echo(
        f"Generated {index_path.resolve()} ({total_convs} prompts, {total_pages} pages)"
    )


@cli.command("web")
@click.argument("session_id", required=False)
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    help="Output directory. If not specified, writes to temp dir and opens in browser.",
)
@click.option(
    "-a",
    "--output-auto",
    is_flag=True,
    help="Auto-name output subdirectory based on session ID (uses -o as parent, or current dir).",
)
@click.option("--token", help="API access token (auto-detected from keychain on macOS)")
@click.option(
    "--org-uuid", help="Organization UUID (auto-detected from ~/.claude.json)"
)
@click.option(
    "--repo",
    help="GitHub repo (owner/name). Filters session list and sets default for commit links.",
)
@click.option(
    "--gist",
    is_flag=True,
    help="Upload to GitHub Gist and output a gisthost.github.io URL.",
)
@click.option(
    "--json",
    "include_json",
    is_flag=True,
    help="Include the JSON session data in the output directory.",
)
@click.option(
    "--open",
    "open_browser",
    is_flag=True,
    help="Open the generated index.html in your default browser (default if no -o specified).",
)
def web_cmd(
    session_id,
    output,
    output_auto,
    token,
    org_uuid,
    repo,
    gist,
    include_json,
    open_browser,
):
    """Select and convert a web session from the Claude API to HTML.

    If SESSION_ID is not provided, displays an interactive picker to select a session.
    """
    try:
        token, org_uuid = resolve_credentials(token, org_uuid)
    except click.ClickException:
        raise

    # If no session ID provided, show interactive picker
    if session_id is None:
        try:
            sessions_data = fetch_sessions(token, org_uuid)
        except httpx.HTTPStatusError as e:
            raise click.ClickException(
                f"API request failed: {e.response.status_code} {e.response.text}"
            )
        except httpx.RequestError as e:
            raise click.ClickException(f"Network error: {e}")

        sessions = sessions_data.get("data", [])
        if not sessions:
            raise click.ClickException("No sessions found.")

        # Enrich sessions with repo information (extracted from session metadata)
        sessions = enrich_sessions_with_repos(sessions)

        # Filter by repo if specified
        if repo:
            sessions = filter_sessions_by_repo(sessions, repo)
            if not sessions:
                raise click.ClickException(f"No sessions found for repo: {repo}")

        # Build choices for questionary
        choices = []
        for s in sessions:
            sid = s.get("id", "unknown")
            display = format_session_for_display(s)
            choices.append(questionary.Choice(title=display, value=sid))

        selected = questionary.select(
            "Select a session to import:",
            choices=choices,
        ).ask()

        if selected is None:
            # User cancelled
            raise click.ClickException("No session selected.")

        session_id = selected

    # Fetch the session
    click.echo(f"Fetching session {session_id}...")
    try:
        session_data = fetch_session(token, org_uuid, session_id)
    except httpx.HTTPStatusError as e:
        raise click.ClickException(
            f"API request failed: {e.response.status_code} {e.response.text}"
        )
    except httpx.RequestError as e:
        raise click.ClickException(f"Network error: {e}")

    # Determine output directory and whether to open browser
    # If no -o specified, use temp dir and open browser by default
    auto_open = output is None and not gist and not output_auto
    if output_auto:
        # Use -o as parent dir (or current dir), with auto-named subdirectory
        parent_dir = Path(output) if output else Path(".")
        output = parent_dir / session_id
    elif output is None:
        output = Path(tempfile.gettempdir()) / f"claude-session-{session_id}"

    output = Path(output)
    click.echo(f"Generating HTML in {output}/...")
    generate_html_from_session_data(session_data, output, github_repo=repo)

    # Show output directory
    click.echo(f"Output: {output.resolve()}")

    # Save JSON session data if requested
    if include_json:
        output.mkdir(exist_ok=True)
        json_dest = output / f"{session_id}.json"
        with open(json_dest, "w") as f:
            json.dump(session_data, f, indent=2)
        json_size_kb = json_dest.stat().st_size / 1024
        click.echo(f"JSON: {json_dest} ({json_size_kb:.1f} KB)")

    if gist:
        # Inject gist preview JS and create gist
        inject_gist_preview_js(output)
        click.echo("Creating GitHub gist...")
        gist_id, gist_url = create_gist(output)
        preview_url = f"https://gisthost.github.io/?{gist_id}/index.html"
        click.echo(f"Gist: {gist_url}")
        click.echo(f"Preview: {preview_url}")

    if open_browser or auto_open:
        index_url = (output / "index.html").resolve().as_uri()
        webbrowser.open(index_url)


@cli.command("all")
@click.option(
    "-s",
    "--source",
    type=click.Path(exists=True),
    help="Source directory containing Claude projects (default: ~/.claude/projects).",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    default="./claude-archive",
    help="Output directory for the archive (default: ./claude-archive).",
)
@click.option(
    "--include-agents",
    is_flag=True,
    help="Include agent-* session files (excluded by default).",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be converted without creating files.",
)
@click.option(
    "--open",
    "open_browser",
    is_flag=True,
    help="Open the generated archive in your default browser.",
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Suppress all output except errors.",
)
def all_cmd(source, output, include_agents, dry_run, open_browser, quiet):
    """Convert all local Claude Code sessions to a browsable HTML archive.

    Creates a directory structure with:
    - Master index listing all projects
    - Per-project pages listing sessions
    - Individual session transcripts
    """
    # Default source folder
    if source is None:
        source = Path.home() / ".claude" / "projects"
    else:
        source = Path(source)

    if not source.exists():
        raise click.ClickException(f"Source directory not found: {source}")

    output = Path(output)

    if not quiet:
        click.echo(f"Scanning {source}...")

    projects = find_all_sessions(source, include_agents=include_agents)

    if not projects:
        if not quiet:
            click.echo("No sessions found.")
        return

    # Calculate totals
    total_sessions = sum(len(p["sessions"]) for p in projects)

    if not quiet:
        click.echo(f"Found {len(projects)} projects with {total_sessions} sessions")

    if dry_run:
        # Dry-run always outputs (it's the point of dry-run), but respects --quiet
        if not quiet:
            click.echo("\nDry run - would convert:")
            for project in projects:
                click.echo(
                    f"\n  {project['name']} ({len(project['sessions'])} sessions)"
                )
                for session in project["sessions"][:3]:  # Show first 3
                    mod_time = datetime.fromtimestamp(session["mtime"])
                    click.echo(
                        f"    - {session['path'].stem} ({mod_time.strftime('%Y-%m-%d')})"
                    )
                if len(project["sessions"]) > 3:
                    click.echo(f"    ... and {len(project['sessions']) - 3} more")
        return

    if not quiet:
        click.echo(f"\nGenerating archive in {output}...")

    # Progress callback for non-quiet mode
    def on_progress(project_name, session_name, current, total):
        if not quiet and current % 10 == 0:
            click.echo(f"  Processed {current}/{total} sessions...")

    # Generate the archive using the library function
    stats = generate_batch_html(
        source,
        output,
        include_agents=include_agents,
        progress_callback=on_progress,
    )

    # Report any failures
    if stats["failed_sessions"]:
        click.echo(f"\nWarning: {len(stats['failed_sessions'])} session(s) failed:")
        for failure in stats["failed_sessions"]:
            click.echo(
                f"  {failure['project']}/{failure['session']}: {failure['error']}"
            )

    if not quiet:
        click.echo(
            f"\nGenerated archive with {stats['total_projects']} projects, "
            f"{stats['total_sessions']} sessions"
        )
        click.echo(f"Output: {output.resolve()}")

    if open_browser:
        index_url = (output / "index.html").resolve().as_uri()
        webbrowser.open(index_url)


def main():
    cli()
```

## File: `src/claude_code_transcripts/templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Claude Code transcript{% endblock %}</title>
    <style>{{ css|safe }}</style>
</head>
<body>
    <div class="container">
{%- block content %}{% endblock %}
    </div>
    <script>{{ js|safe }}</script>
</body>
</html>
```

## File: `src/claude_code_transcripts/templates/index.html`
```html
{% extends "base.html" %}

{% block title %}Claude Code transcript - Index{% endblock %}

{% block content %}
        <div class="header-row">
            <h1>Claude Code transcript</h1>
            <div id="search-box">
                <input type="text" id="search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
            </div>
        </div>
        {{ pagination_html|safe }}
        <p style="color: var(--text-muted); margin-bottom: 24px;">{{ prompt_num }} prompts · {{ total_messages }} messages · {{ total_tool_calls }} tool calls · {{ total_commits }} commits · {{ total_pages }} pages</p>
        {{ index_items_html|safe }}
        {{ pagination_html|safe }}

        <dialog id="search-modal">
            <div class="search-modal-header">
                <input type="text" id="modal-search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="modal-search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
                <button id="modal-close-btn" type="button" aria-label="Close">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg>
                </button>
            </div>
            <div id="search-status"></div>
            <div id="search-results"></div>
        </dialog>
        <script>
{% include "search.js" %}
        </script>
{%- endblock %}
```

## File: `src/claude_code_transcripts/templates/macros.html`
```html
{# Pagination for regular pages #}
{% macro pagination(current_page, total_pages) %}
{% if total_pages <= 1 %}
<div class="pagination"><a href="index.html" class="index-link">Index</a></div>
{%- else %}
<div class="pagination">
<a href="index.html" class="index-link">Index</a>
{% if current_page > 1 -%}
<a href="page-{{ '%03d'|format(current_page - 1) }}.html">&larr; Prev</a>
{%- else -%}
<span class="disabled">&larr; Prev</span>
{%- endif %}
{% for page in range(1, total_pages + 1) -%}
{% if page == current_page -%}
<span class="current">{{ page }}</span>
{%- else -%}
<a href="page-{{ '%03d'|format(page) }}.html">{{ page }}</a>
{%- endif %}
{% endfor -%}
{% if current_page < total_pages -%}
<a href="page-{{ '%03d'|format(current_page + 1) }}.html">Next &rarr;</a>
{%- else -%}
<span class="disabled">Next &rarr;</span>
{%- endif %}
</div>
{%- endif %}
{% endmacro %}

{# Pagination for index page #}
{% macro index_pagination(total_pages) %}
{% if total_pages < 1 %}
<div class="pagination"><span class="current">Index</span></div>
{%- else %}
<div class="pagination">
<span class="current">Index</span>
<span class="disabled">&larr; Prev</span>
{% for page in range(1, total_pages + 1) -%}
<a href="page-{{ '%03d'|format(page) }}.html">{{ page }}</a>
{% endfor -%}
{% if total_pages >= 1 -%}
<a href="page-001.html">Next &rarr;</a>
{%- else -%}
<span class="disabled">Next &rarr;</span>
{%- endif %}
</div>
{%- endif %}
{% endmacro %}

{# Todo list #}
{% macro todo_list(todos, tool_id) %}
<div class="todo-list" data-tool-id="{{ tool_id }}"><div class="todo-header"><span class="todo-header-icon">☰</span> Task List</div><ul class="todo-items">
{%- for todo in todos -%}
{%- set status = todo.status|default('pending') -%}
{%- set content = todo.content|default('') -%}
{%- if status == 'completed' -%}
{%- set icon = '✓' -%}
{%- set status_class = 'todo-completed' -%}
{%- elif status == 'in_progress' -%}
{%- set icon = '→' -%}
{%- set status_class = 'todo-in-progress' -%}
{%- else -%}
{%- set icon = '○' -%}
{%- set status_class = 'todo-pending' -%}
{%- endif -%}
<li class="todo-item {{ status_class }}"><span class="todo-icon">{{ icon }}</span><span class="todo-content">{{ content }}</span></li>
{%- endfor -%}
</ul></div>
{%- endmacro %}

{# Write tool #}
{% macro write_tool(file_path, content, tool_id) %}
{%- set filename = file_path.split('/')[-1] if '/' in file_path else file_path -%}
<div class="file-tool write-tool" data-tool-id="{{ tool_id }}">
<div class="file-tool-header write-header"><span class="file-tool-icon">📝</span> Write <span class="file-tool-path">{{ filename }}</span></div>
<div class="file-tool-fullpath">{{ file_path }}</div>
<div class="truncatable"><div class="truncatable-content"><pre class="file-content">{{ content }}</pre></div><button class="expand-btn">Show more</button></div>
</div>
{%- endmacro %}

{# Edit tool #}
{% macro edit_tool(file_path, old_string, new_string, replace_all, tool_id) %}
{%- set filename = file_path.split('/')[-1] if '/' in file_path else file_path -%}
<div class="file-tool edit-tool" data-tool-id="{{ tool_id }}">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">{{ filename }}</span>{% if replace_all %} <span class="edit-replace-all">(replace all)</span>{% endif %}</div>
<div class="file-tool-fullpath">{{ file_path }}</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">{{ old_string }}</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">{{ new_string }}</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div>
{%- endmacro %}

{# Bash tool #}
{% macro bash_tool(command, description, tool_id) %}
<div class="tool-use bash-tool" data-tool-id="{{ tool_id }}">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
{%- if description %}
<div class="tool-description">{{ description }}</div>
{%- endif -%}
<div class="truncatable"><div class="truncatable-content"><pre class="bash-command">{{ command }}</pre></div><button class="expand-btn">Show more</button></div>
</div>
{%- endmacro %}

{# Generic tool use - input_json is pre-formatted so needs |safe #}
{% macro tool_use(tool_name, description, input_json, tool_id) %}
<div class="tool-use" data-tool-id="{{ tool_id }}"><div class="tool-header"><span class="tool-icon">⚙</span> {{ tool_name }}</div>
{%- if description -%}
<div class="tool-description">{{ description }}</div>
{%- endif -%}
<div class="truncatable"><div class="truncatable-content"><pre class="json">{{ input_json }}</pre></div><button class="expand-btn">Show more</button></div></div>
{%- endmacro %}

{# Tool result - content_html is pre-rendered so needs |safe #}
{# has_images=True disables truncation so images are always visible #}
{% macro tool_result(content_html, is_error, has_images=False) %}
{%- set error_class = ' tool-error' if is_error else '' -%}
{%- if has_images -%}
<div class="tool-result{{ error_class }}">{{ content_html|safe }}</div>
{%- else -%}
<div class="tool-result{{ error_class }}"><div class="truncatable"><div class="truncatable-content">{{ content_html|safe }}</div><button class="expand-btn">Show more</button></div></div>
{%- endif -%}
{%- endmacro %}

{# Thinking block - content_html is pre-rendered markdown so needs |safe #}
{% macro thinking(content_html) %}
<div class="thinking"><div class="thinking-label">Thinking</div>{{ content_html|safe }}</div>
{%- endmacro %}

{# Assistant text - content_html is pre-rendered markdown so needs |safe #}
{% macro assistant_text(content_html) %}
<div class="assistant-text">{{ content_html|safe }}</div>
{%- endmacro %}

{# User content - content_html is pre-rendered so needs |safe #}
{% macro user_content(content_html) %}
<div class="user-content">{{ content_html|safe }}</div>
{%- endmacro %}

{# Image block with base64 data URL #}
{% macro image_block(media_type, data) %}
<div class="image-block"><img src="data:{{ media_type }};base64,{{ data }}" style="max-width: 100%"></div>
{%- endmacro %}

{# Commit card (in tool results) #}
{% macro commit_card(commit_hash, commit_msg, github_repo) %}
{%- if github_repo -%}
{%- set github_link = 'https://github.com/' ~ github_repo ~ '/commit/' ~ commit_hash -%}
<div class="commit-card"><a href="{{ github_link }}"><span class="commit-card-hash">{{ commit_hash[:7] }}</span> {{ commit_msg }}</a></div>
{%- else -%}
<div class="commit-card"><span class="commit-card-hash">{{ commit_hash[:7] }}</span> {{ commit_msg }}</div>
{%- endif %}
{%- endmacro %}

{# Message wrapper - content_html is pre-rendered so needs |safe #}
{% macro message(role_class, role_label, msg_id, timestamp, content_html) %}
<div class="message {{ role_class }}" id="{{ msg_id }}"><div class="message-header"><span class="role-label">{{ role_label }}</span><a href="#{{ msg_id }}" class="timestamp-link"><time datetime="{{ timestamp }}" data-timestamp="{{ timestamp }}">{{ timestamp }}</time></a></div><div class="message-content">{{ content_html|safe }}</div></div>
{%- endmacro %}

{# Continuation wrapper - content_html is pre-rendered so needs |safe #}
{% macro continuation(content_html) %}
<details class="continuation"><summary>Session continuation summary</summary>{{ content_html|safe }}</details>
{%- endmacro %}

{# Index item (prompt) - rendered_content and stats_html are pre-rendered so need |safe #}
{% macro index_item(prompt_num, link, timestamp, rendered_content, stats_html) %}
<div class="index-item"><a href="{{ link }}"><div class="index-item-header"><span class="index-item-number">#{{ prompt_num }}</span><time datetime="{{ timestamp }}" data-timestamp="{{ timestamp }}">{{ timestamp }}</time></div><div class="index-item-content">{{ rendered_content|safe }}</div></a>{{ stats_html|safe }}</div>
{%- endmacro %}

{# Index commit #}
{% macro index_commit(commit_hash, commit_msg, timestamp, github_repo) %}
{%- if github_repo -%}
{%- set github_link = 'https://github.com/' ~ github_repo ~ '/commit/' ~ commit_hash -%}
<div class="index-commit"><a href="{{ github_link }}"><div class="index-commit-header"><span class="index-commit-hash">{{ commit_hash[:7] }}</span><time datetime="{{ timestamp }}" data-timestamp="{{ timestamp }}">{{ timestamp }}</time></div><div class="index-commit-msg">{{ commit_msg }}</div></a></div>
{%- else -%}
<div class="index-commit"><div class="index-commit-header"><span class="index-commit-hash">{{ commit_hash[:7] }}</span><time datetime="{{ timestamp }}" data-timestamp="{{ timestamp }}">{{ timestamp }}</time></div><div class="index-commit-msg">{{ commit_msg }}</div></div>
{%- endif %}
{%- endmacro %}

{# Index stats - tool_stats_str and long_texts_html are pre-rendered so need |safe #}
{% macro index_stats(tool_stats_str, long_texts_html) %}
{%- if tool_stats_str or long_texts_html -%}
<div class="index-item-stats">
{%- if tool_stats_str -%}<span>{{ tool_stats_str }}</span>{%- endif -%}
{{ long_texts_html|safe }}
</div>
{%- endif %}
{%- endmacro %}

{# Long text in index - rendered_content is pre-rendered markdown so needs |safe #}
{% macro index_long_text(rendered_content) %}
<div class="index-item-long-text"><div class="truncatable"><div class="truncatable-content"><div class="index-item-long-text-content">{{ rendered_content|safe }}</div></div><button class="expand-btn">Show more</button></div></div>
{%- endmacro %}
```

## File: `src/claude_code_transcripts/templates/master_index.html`
```html
{% extends "base.html" %}

{% block title %}Claude Code Archive{% endblock %}

{% block content %}
        <h1>Claude Code Archive</h1>
        <p style="color: var(--text-muted); margin-bottom: 24px;">{{ total_projects }} projects · {{ total_sessions }} sessions</p>

        {% for project in projects %}
        <div class="index-item">
            <a href="{{ project.name }}/index.html">
                <div class="index-item-header">
                    <span class="index-item-number">{{ project.name }}</span>
                    <time>{{ project.recent_date }}</time>
                </div>
                <div class="index-item-content">
                    <p style="margin: 0;">{{ project.session_count }} session{% if project.session_count != 1 %}s{% endif %}</p>
                </div>
            </a>
        </div>
        {% endfor %}
{%- endblock %}
```

## File: `src/claude_code_transcripts/templates/page.html`
```html
{% extends "base.html" %}

{% block title %}Claude Code transcript - page {{ page_num }}{% endblock %}

{% block content %}
        <h1><a href="index.html" style="color: inherit; text-decoration: none;">Claude Code transcript</a> - page {{ page_num }}/{{ total_pages }}</h1>
        {{ pagination_html|safe }}
        {{ messages_html|safe }}
        {{ pagination_html|safe }}
{%- endblock %}
```

## File: `src/claude_code_transcripts/templates/project_index.html`
```html
{% extends "base.html" %}

{% block title %}{{ project_name }} - Claude Code Archive{% endblock %}

{% block content %}
        <h1><a href="../index.html" style="color: inherit; text-decoration: none;">Claude Code Archive</a> / {{ project_name }}</h1>
        <p style="color: var(--text-muted); margin-bottom: 24px;">{{ session_count }} session{% if session_count != 1 %}s{% endif %}</p>

        {% for session in sessions %}
        <div class="index-item">
            <a href="{{ session.name }}/index.html">
                <div class="index-item-header">
                    <span class="index-item-number">{{ session.date }}</span>
                    <span style="color: var(--text-muted);">{{ "%.0f"|format(session.size_kb) }} KB</span>
                </div>
                <div class="index-item-content">
                    <p style="margin: 0;">{{ session.summary[:100] }}{% if session.summary|length > 100 %}...{% endif %}</p>
                </div>
            </a>
        </div>
        {% endfor %}

        <div style="margin-top: 24px;">
            <a href="../index.html" class="pagination" style="display: inline-block; padding: 8px 16px; background: var(--user-border); color: white; text-decoration: none; border-radius: 6px;">Back to Archive</a>
        </div>
{%- endblock %}
```

## File: `src/claude_code_transcripts/templates/search.js`
```javascript
(function() {
    var totalPages = {{ total_pages }};
    var searchBox = document.getElementById('search-box');
    var searchInput = document.getElementById('search-input');
    var searchBtn = document.getElementById('search-btn');
    var modal = document.getElementById('search-modal');
    var modalInput = document.getElementById('modal-search-input');
    var modalSearchBtn = document.getElementById('modal-search-btn');
    var modalCloseBtn = document.getElementById('modal-close-btn');
    var searchStatus = document.getElementById('search-status');
    var searchResults = document.getElementById('search-results');

    if (!searchBox || !modal) return;

    // Hide search on file:// protocol (doesn't work due to CORS restrictions)
    if (window.location.protocol === 'file:') return;

    // Show search box (progressive enhancement)
    searchBox.style.display = 'flex';

    // Gist preview support - detect if we're on gisthost.github.io or gistpreview.github.io
    var hostname = window.location.hostname;
    var isGistPreview = hostname === 'gisthost.github.io' || hostname === 'gistpreview.github.io';
    var gistId = null;
    var gistOwner = null;
    var gistInfoLoaded = false;

    if (isGistPreview) {
        // Extract gist ID from URL query string like ?78a436a8a9e7a2e603738b8193b95410/index.html
        var queryMatch = window.location.search.match(/^\?([a-f0-9]+)/i);
        if (queryMatch) {
            gistId = queryMatch[1];
        }
    }

    async function loadGistInfo() {
        if (!isGistPreview || !gistId || gistInfoLoaded) return;
        try {
            var response = await fetch('https://api.github.com/gists/' + gistId);
            if (response.ok) {
                var info = await response.json();
                gistOwner = info.owner.login;
                gistInfoLoaded = true;
            }
        } catch (e) {
            console.error('Failed to load gist info:', e);
        }
    }

    function getPageFetchUrl(pageFile) {
        if (isGistPreview && gistOwner && gistId) {
            // Use raw gist URL for fetching content
            return 'https://gist.githubusercontent.com/' + gistOwner + '/' + gistId + '/raw/' + pageFile;
        }
        return pageFile;
    }

    function getPageLinkUrl(pageFile) {
        if (isGistPreview && gistId) {
            // Use gistpreview URL format for navigation links
            return '?' + gistId + '/' + pageFile;
        }
        return pageFile;
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function openModal(query) {
        modalInput.value = query || '';
        searchResults.innerHTML = '';
        searchStatus.textContent = '';
        modal.showModal();
        modalInput.focus();
        if (query) {
            performSearch(query);
        }
    }

    function closeModal() {
        modal.close();
        // Update URL to remove search fragment, preserving path and query string
        if (window.location.hash.startsWith('#search=')) {
            history.replaceState(null, '', window.location.pathname + window.location.search);
        }
    }

    function updateUrlHash(query) {
        if (query) {
            // Preserve path and query string when adding hash
            history.replaceState(null, '', window.location.pathname + window.location.search + '#search=' + encodeURIComponent(query));
        }
    }

    function highlightTextNodes(element, searchTerm) {
        var walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
        var nodesToReplace = [];

        while (walker.nextNode()) {
            var node = walker.currentNode;
            if (node.nodeValue.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) {
                nodesToReplace.push(node);
            }
        }

        nodesToReplace.forEach(function(node) {
            var text = node.nodeValue;
            var regex = new RegExp('(' + escapeRegex(searchTerm) + ')', 'gi');
            var parts = text.split(regex);
            if (parts.length > 1) {
                var span = document.createElement('span');
                parts.forEach(function(part) {
                    if (part.toLowerCase() === searchTerm.toLowerCase()) {
                        var mark = document.createElement('mark');
                        mark.textContent = part;
                        span.appendChild(mark);
                    } else {
                        span.appendChild(document.createTextNode(part));
                    }
                });
                node.parentNode.replaceChild(span, node);
            }
        });
    }

    function fixInternalLinks(element, pageFile) {
        // Update all internal anchor links to include the page file
        var links = element.querySelectorAll('a[href^="#"]');
        links.forEach(function(link) {
            var href = link.getAttribute('href');
            link.setAttribute('href', pageFile + href);
        });
    }

    function processPage(pageFile, html, query) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var resultsFromPage = 0;

        // Find all message blocks
        var messages = doc.querySelectorAll('.message');
        messages.forEach(function(msg) {
            var text = msg.textContent || '';
            if (text.toLowerCase().indexOf(query.toLowerCase()) !== -1) {
                resultsFromPage++;

                // Get the message ID for linking
                var msgId = msg.id || '';
                var pageLinkUrl = getPageLinkUrl(pageFile);
                var link = pageLinkUrl + (msgId ? '#' + msgId : '');

                // Clone the message HTML and highlight matches
                var clone = msg.cloneNode(true);
                // Fix internal links to include the page file
                fixInternalLinks(clone, pageLinkUrl);
                highlightTextNodes(clone, query);

                var resultDiv = document.createElement('div');
                resultDiv.className = 'search-result';
                resultDiv.innerHTML = '<a href="' + link + '">' +
                    '<div class="search-result-page">' + escapeHtml(pageFile) + '</div>' +
                    '<div class="search-result-content">' + clone.innerHTML + '</div>' +
                    '</a>';
                searchResults.appendChild(resultDiv);
            }
        });

        return resultsFromPage;
    }

    async function performSearch(query) {
        if (!query.trim()) {
            searchStatus.textContent = 'Enter a search term';
            return;
        }

        updateUrlHash(query);
        searchResults.innerHTML = '';
        searchStatus.textContent = 'Searching...';

        // Load gist info if on gistpreview (needed for constructing URLs)
        if (isGistPreview && !gistInfoLoaded) {
            searchStatus.textContent = 'Loading gist info...';
            await loadGistInfo();
            if (!gistOwner) {
                searchStatus.textContent = 'Failed to load gist info. Search unavailable.';
                return;
            }
        }

        var resultsFound = 0;
        var pagesSearched = 0;

        // Build list of pages to fetch
        var pagesToFetch = [];
        for (var i = 1; i <= totalPages; i++) {
            pagesToFetch.push('page-' + String(i).padStart(3, '0') + '.html');
        }

        searchStatus.textContent = 'Searching...';

        // Process pages in batches of 3, but show results immediately as each completes
        var batchSize = 3;
        for (var i = 0; i < pagesToFetch.length; i += batchSize) {
            var batch = pagesToFetch.slice(i, i + batchSize);

            // Create promises that process results immediately when each fetch completes
            var promises = batch.map(function(pageFile) {
                return fetch(getPageFetchUrl(pageFile))
                    .then(function(response) {
                        if (!response.ok) throw new Error('Failed to fetch');
                        return response.text();
                    })
                    .then(function(html) {
                        // Process and display results immediately
                        var count = processPage(pageFile, html, query);
                        resultsFound += count;
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    })
                    .catch(function() {
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    });
            });

            // Wait for this batch to complete before starting the next
            await Promise.all(promises);
        }

        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + totalPages + ' pages';
    }

    // Event listeners
    searchBtn.addEventListener('click', function() {
        openModal(searchInput.value);
    });

    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            openModal(searchInput.value);
        }
    });

    modalSearchBtn.addEventListener('click', function() {
        performSearch(modalInput.value);
    });

    modalInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            performSearch(modalInput.value);
        }
    });

    modalCloseBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Check for #search= in URL on page load
    if (window.location.hash.startsWith('#search=')) {
        var query = decodeURIComponent(window.location.hash.substring(8));
        if (query) {
            searchInput.value = query;
            openModal(query);
        }
    }
})();
```

## File: `tests/conftest.py`
```python
"""Pytest configuration and fixtures for claude-code-transcripts tests."""

import pytest


@pytest.fixture(autouse=True)
def mock_webbrowser_open(monkeypatch):
    """Automatically mock webbrowser.open to prevent browsers opening during tests."""
    opened_urls = []

    def mock_open(url):
        opened_urls.append(url)
        return True

    monkeypatch.setattr("claude_code_transcripts.webbrowser.open", mock_open)
    return opened_urls
```

## File: `tests/sample_session.json`
```json
{
  "loglines": [
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:00.000Z",
      "message": {
        "content": "Create a simple Python function to add two numbers",
        "role": "user"
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:00:05.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "thinking",
            "thinking": "The user wants a simple addition function. I should:\n1. Create the function\n2. Add a basic test\n\nThis is straightforward."
          },
          {
            "type": "text",
            "text": "I'll create a simple Python function for you. Let me write it now."
          },
          {
            "type": "tool_use",
            "id": "toolu_write_001",
            "name": "Write",
            "input": {
              "file_path": "/project/math_utils.py",
              "content": "def add(a: int, b: int) -> int:\n    \"\"\"Add two numbers together.\"\"\"\n    return a + b\n"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:10.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_write_001",
            "content": "File written successfully",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:00:15.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "I've created the `add` function. Now let me run the tests."
          },
          {
            "type": "tool_use",
            "id": "toolu_bash_001",
            "name": "Bash",
            "input": {
              "command": "python -m pytest tests/",
              "description": "Run pytest on tests directory"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:20.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_bash_001",
            "content": "===== test session starts =====\ncollected 2 items\n\ntests/test_math.py ..  [100%]\n\n===== 2 passed in 0.05s =====",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:00:25.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "All tests pass. Let me update the todo list and make a commit."
          },
          {
            "type": "tool_use",
            "id": "toolu_todo_001",
            "name": "TodoWrite",
            "input": {
              "todos": [
                {"content": "Create add function", "status": "completed", "activeForm": "Creating add function"},
                {"content": "Write tests", "status": "completed", "activeForm": "Writing tests"},
                {"content": "Run tests", "status": "completed", "activeForm": "Running tests"},
                {"content": "Commit changes", "status": "in_progress", "activeForm": "Committing changes"},
                {"content": "Push to remote", "status": "pending", "activeForm": "Pushing to remote"}
              ]
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:30.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_todo_001",
            "content": "Todos updated",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:00:35.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_bash_002",
            "name": "Bash",
            "input": {
              "command": "git add . && git commit -m 'Add math_utils with add function'",
              "description": "Commit changes"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:40.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_bash_002",
            "content": "[main abc1234] Add math_utils with add function\n 1 file changed, 5 insertions(+)",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:00:45.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Committed! Now pushing to remote."
          },
          {
            "type": "tool_use",
            "id": "toolu_bash_003",
            "name": "Bash",
            "input": {
              "command": "git push -u origin main",
              "description": "Push to remote"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:00:50.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_bash_003",
            "content": "remote: \nremote: Create a pull request for 'main' on GitHub by visiting:\nremote:      https://github.com/example/project/pull/new/main\nremote: \nTo github.com:example/project.git\n   def5678..abc1234  main -> main",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:01:00.000Z",
      "message": {
        "content": "Now edit the file to add a subtract function",
        "role": "user"
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:01:05.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_glob_001",
            "name": "Glob",
            "input": {
              "pattern": "**/*.py",
              "path": "/project"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:01:10.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_glob_001",
            "content": "/project/math_utils.py\n/project/tests/test_math.py",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:01:15.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_edit_001",
            "name": "Edit",
            "input": {
              "file_path": "/project/math_utils.py",
              "old_string": "    return a + b\n",
              "new_string": "    return a + b\n\n\ndef subtract(a: int, b: int) -> int:\n    \"\"\"Subtract b from a.\"\"\"\n    return a - b\n"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:01:20.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_edit_001",
            "content": "File edited successfully",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:01:25.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Added the subtract function. Let me verify with grep."
          },
          {
            "type": "tool_use",
            "id": "toolu_grep_001",
            "name": "Grep",
            "input": {
              "pattern": "def subtract",
              "path": "/project",
              "output_mode": "content"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:01:30.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_grep_001",
            "content": "/project/math_utils.py:6:def subtract(a: int, b: int) -> int:",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:02:00.000Z",
      "message": {
        "content": "Run the tests again",
        "role": "user"
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:02:05.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_bash_004",
            "name": "Bash",
            "input": {
              "command": "python -m pytest tests/ -v",
              "description": "Run tests with verbose output"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:02:10.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_bash_004",
            "content": "Exit code 1\n===== FAILURES =====\ntest_subtract - AssertionError: expected 5 but got None",
            "is_error": true
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:02:15.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "There's a test failure. I need to check the test file and fix it.\n\nHere's some **markdown** content with:\n- A bullet list\n- `inline code`\n- A [link](https://example.com)\n\n```python\ndef example():\n    return 42\n```"
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:03:00.000Z",
      "message": {
        "content": "Fix the issue and commit",
        "role": "user"
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:03:05.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_edit_002",
            "name": "Edit",
            "input": {
              "file_path": "/project/tests/test_math.py",
              "old_string": "assert subtract(10, 5) == None",
              "new_string": "assert subtract(10, 5) == 5",
              "replace_all": true
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:03:10.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_edit_002",
            "content": "File edited successfully",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:03:15.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_bash_005",
            "name": "Bash",
            "input": {
              "command": "git add . && git commit -m 'Add subtract function and fix tests'",
              "description": "Commit the fix"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:03:20.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_bash_005",
            "content": "[main def5678] Add subtract function and fix tests\n 2 files changed, 10 insertions(+), 1 deletion(-)",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:03:25.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Done! The subtract function is now working and committed."
          }
        ]
      }
    },
    {
      "isCompactSummary": true,
      "type": "user",
      "timestamp": "2025-12-24T10:04:00.000Z",
      "message": {
        "content": "This is a session continuation summary from a previous context. The user was working on a math utilities library.",
        "role": "user"
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:05:00.000Z",
      "message": {
        "content": "Add a multiply function too",
        "role": "user"
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:05:05.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "tool_use",
            "id": "toolu_edit_003",
            "name": "Edit",
            "input": {
              "file_path": "/project/math_utils.py",
              "old_string": "    return a - b\n",
              "new_string": "    return a - b\n\n\ndef multiply(a: int, b: int) -> int:\n    \"\"\"Multiply two numbers.\"\"\"\n    return a * b\n"
            }
          }
        ]
      }
    },
    {
      "type": "user",
      "timestamp": "2025-12-24T10:05:10.000Z",
      "message": {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_edit_003",
            "content": "File edited successfully",
            "is_error": false
          }
        ]
      }
    },
    {
      "type": "assistant",
      "timestamp": "2025-12-24T10:05:15.000Z",
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Added multiply function!"
          }
        ]
      }
    }
  ]
}
```

## File: `tests/sample_session.jsonl`
```
{"type":"summary","summary":"Test session for JSONL parsing","leafUuid":"test-leaf-uuid"}
{"type":"user","timestamp":"2025-12-24T10:00:00.000Z","sessionId":"test-session-id","cwd":"/project","gitBranch":"main","message":{"role":"user","content":"Create a hello world function"},"uuid":"msg-001"}
{"type":"assistant","timestamp":"2025-12-24T10:00:05.000Z","sessionId":"test-session-id","message":{"role":"assistant","content":[{"type":"text","text":"I'll create that function for you."},{"type":"tool_use","id":"toolu_001","name":"Write","input":{"file_path":"/project/hello.py","content":"def hello():\n    return 'Hello, World!'\n"}}]},"uuid":"msg-002"}
{"type":"user","timestamp":"2025-12-24T10:00:10.000Z","sessionId":"test-session-id","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"toolu_001","content":"File written successfully"}]},"uuid":"msg-003"}
{"type":"assistant","timestamp":"2025-12-24T10:00:15.000Z","sessionId":"test-session-id","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_002","name":"Bash","input":{"command":"git add . && git commit -m 'Add hello function'","description":"Commit changes"}}]},"uuid":"msg-004"}
{"type":"user","timestamp":"2025-12-24T10:00:20.000Z","sessionId":"test-session-id","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"toolu_002","content":"[main abc1234] Add hello function\n 1 file changed"}]},"uuid":"msg-005"}
{"type":"user","timestamp":"2025-12-24T10:01:00.000Z","sessionId":"test-session-id","message":{"role":"user","content":"Now add a goodbye function"},"uuid":"msg-006"}
{"type":"assistant","timestamp":"2025-12-24T10:01:05.000Z","sessionId":"test-session-id","message":{"role":"assistant","content":[{"type":"text","text":"Done! The hello function is ready."}]},"uuid":"msg-007"}
```

## File: `tests/test_all.py`
```python
"""Tests for batch conversion functionality."""

import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from claude_code_transcripts import (
    cli,
    find_all_sessions,
    get_project_display_name,
    generate_batch_html,
)


@pytest.fixture
def mock_projects_dir():
    """Create a mock ~/.claude/projects structure with test sessions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        projects_dir = Path(tmpdir)

        # Create project-a with 2 sessions
        project_a = projects_dir / "-home-user-projects-project-a"
        project_a.mkdir(parents=True)

        session_a1 = project_a / "abc123.jsonl"
        session_a1.write_text(
            '{"type": "user", "timestamp": "2025-01-01T10:00:00.000Z", "message": {"role": "user", "content": "Hello from project A"}}\n'
            '{"type": "assistant", "timestamp": "2025-01-01T10:00:05.000Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Hi there!"}]}}\n'
        )

        session_a2 = project_a / "def456.jsonl"
        session_a2.write_text(
            '{"type": "user", "timestamp": "2025-01-02T10:00:00.000Z", "message": {"role": "user", "content": "Second session in project A"}}\n'
            '{"type": "assistant", "timestamp": "2025-01-02T10:00:05.000Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Got it!"}]}}\n'
        )

        # Create an agent file (should be skipped by default)
        agent_a = project_a / "agent-xyz789.jsonl"
        agent_a.write_text(
            '{"type": "user", "timestamp": "2025-01-03T10:00:00.000Z", "message": {"role": "user", "content": "Agent session"}}\n'
        )

        # Create project-b with 1 session
        project_b = projects_dir / "-home-user-projects-project-b"
        project_b.mkdir(parents=True)

        session_b1 = project_b / "ghi789.jsonl"
        session_b1.write_text(
            '{"type": "user", "timestamp": "2025-01-04T10:00:00.000Z", "message": {"role": "user", "content": "Hello from project B"}}\n'
            '{"type": "assistant", "timestamp": "2025-01-04T10:00:05.000Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Welcome!"}]}}\n'
        )

        # Create empty/warmup session (should be skipped)
        warmup = project_b / "warmup123.jsonl"
        warmup.write_text(
            '{"type": "user", "timestamp": "2025-01-05T10:00:00.000Z", "message": {"role": "user", "content": "warmup"}}\n'
        )

        yield projects_dir


@pytest.fixture
def output_dir():
    """Create a temporary output directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestGetProjectDisplayName:
    """Tests for get_project_display_name function."""

    def test_extracts_project_name_from_path(self):
        """Test extracting readable project name from encoded path."""
        assert get_project_display_name("-home-user-projects-myproject") == "myproject"

    def test_handles_nested_paths(self):
        """Test handling nested project paths."""
        assert get_project_display_name("-home-user-code-apps-webapp") == "apps-webapp"

    def test_handles_windows_style_paths(self):
        """Test handling Windows-style encoded paths."""
        assert get_project_display_name("-mnt-c-Users-name-Projects-app") == "app"

    def test_handles_simple_name(self):
        """Test handling already simple names."""
        assert get_project_display_name("simple-project") == "simple-project"


class TestFindAllSessions:
    """Tests for find_all_sessions function."""

    def test_finds_sessions_grouped_by_project(self, mock_projects_dir):
        """Test that sessions are found and grouped by project."""
        result = find_all_sessions(mock_projects_dir)

        # Should have 2 projects
        assert len(result) == 2

        # Check project names are extracted
        project_names = [p["name"] for p in result]
        assert "project-a" in project_names
        assert "project-b" in project_names

    def test_excludes_agent_files_by_default(self, mock_projects_dir):
        """Test that agent-* files are excluded by default."""
        result = find_all_sessions(mock_projects_dir)

        # Find project-a
        project_a = next(p for p in result if p["name"] == "project-a")

        # Should have 2 sessions (not 3, agent excluded)
        assert len(project_a["sessions"]) == 2

        # No session should be an agent file
        for session in project_a["sessions"]:
            assert not session["path"].name.startswith("agent-")

    def test_includes_agent_files_when_requested(self, mock_projects_dir):
        """Test that agent-* files can be included."""
        result = find_all_sessions(mock_projects_dir, include_agents=True)

        # Find project-a
        project_a = next(p for p in result if p["name"] == "project-a")

        # Should have 3 sessions (including agent)
        assert len(project_a["sessions"]) == 3

    def test_excludes_warmup_sessions(self, mock_projects_dir):
        """Test that warmup sessions are excluded."""
        result = find_all_sessions(mock_projects_dir)

        # Find project-b
        project_b = next(p for p in result if p["name"] == "project-b")

        # Should have 1 session (warmup excluded)
        assert len(project_b["sessions"]) == 1

    def test_sessions_sorted_by_date(self, mock_projects_dir):
        """Test that sessions within a project are sorted by modification time."""
        result = find_all_sessions(mock_projects_dir)

        for project in result:
            sessions = project["sessions"]
            if len(sessions) > 1:
                # Check descending order (most recent first)
                for i in range(len(sessions) - 1):
                    assert sessions[i]["mtime"] >= sessions[i + 1]["mtime"]

    def test_returns_empty_for_nonexistent_folder(self):
        """Test handling of non-existent folder."""
        result = find_all_sessions(Path("/nonexistent/path"))
        assert result == []

    def test_session_includes_summary(self, mock_projects_dir):
        """Test that sessions include summary text."""
        result = find_all_sessions(mock_projects_dir)

        project_a = next(p for p in result if p["name"] == "project-a")

        for session in project_a["sessions"]:
            assert "summary" in session
            assert session["summary"] != "(no summary)"


class TestGenerateBatchHtml:
    """Tests for generate_batch_html function."""

    def test_creates_output_directory(self, mock_projects_dir, output_dir):
        """Test that output directory is created."""
        generate_batch_html(mock_projects_dir, output_dir)
        assert output_dir.exists()

    def test_creates_master_index(self, mock_projects_dir, output_dir):
        """Test that master index.html is created."""
        generate_batch_html(mock_projects_dir, output_dir)
        assert (output_dir / "index.html").exists()

    def test_creates_project_directories(self, mock_projects_dir, output_dir):
        """Test that project directories are created."""
        generate_batch_html(mock_projects_dir, output_dir)

        assert (output_dir / "project-a").exists()
        assert (output_dir / "project-b").exists()

    def test_creates_project_indexes(self, mock_projects_dir, output_dir):
        """Test that project index.html files are created."""
        generate_batch_html(mock_projects_dir, output_dir)

        assert (output_dir / "project-a" / "index.html").exists()
        assert (output_dir / "project-b" / "index.html").exists()

    def test_creates_session_directories(self, mock_projects_dir, output_dir):
        """Test that session directories are created with transcripts."""
        generate_batch_html(mock_projects_dir, output_dir)

        # Check project-a has session directories
        project_a_dir = output_dir / "project-a"
        session_dirs = [d for d in project_a_dir.iterdir() if d.is_dir()]
        assert len(session_dirs) == 2

        # Each session directory should have an index.html
        for session_dir in session_dirs:
            assert (session_dir / "index.html").exists()

    def test_master_index_lists_all_projects(self, mock_projects_dir, output_dir):
        """Test that master index lists all projects."""
        generate_batch_html(mock_projects_dir, output_dir)

        index_html = (output_dir / "index.html").read_text()
        assert "project-a" in index_html
        assert "project-b" in index_html

    def test_master_index_shows_session_counts(self, mock_projects_dir, output_dir):
        """Test that master index shows session counts per project."""
        generate_batch_html(mock_projects_dir, output_dir)

        index_html = (output_dir / "index.html").read_text()
        # project-a has 2 sessions, project-b has 1
        assert "2 sessions" in index_html or "2 session" in index_html
        assert "1 session" in index_html

    def test_project_index_lists_sessions(self, mock_projects_dir, output_dir):
        """Test that project index lists all sessions."""
        generate_batch_html(mock_projects_dir, output_dir)

        project_a_index = (output_dir / "project-a" / "index.html").read_text()
        # Should contain links to session directories
        assert "abc123" in project_a_index
        assert "def456" in project_a_index

    def test_returns_statistics(self, mock_projects_dir, output_dir):
        """Test that batch generation returns statistics."""
        stats = generate_batch_html(mock_projects_dir, output_dir)

        assert stats["total_projects"] == 2
        assert stats["total_sessions"] == 3  # 2 + 1
        assert stats["failed_sessions"] == []
        assert "output_dir" in stats

    def test_progress_callback_called(self, mock_projects_dir, output_dir):
        """Test that progress callback is called for each session."""
        progress_calls = []

        def on_progress(project_name, session_name, current, total):
            progress_calls.append((project_name, session_name, current, total))

        generate_batch_html(
            mock_projects_dir, output_dir, progress_callback=on_progress
        )

        # Should be called for each session (3 total)
        assert len(progress_calls) == 3
        # Last call should have current == total
        assert progress_calls[-1][2] == progress_calls[-1][3]

    def test_handles_failed_session_gracefully(self, output_dir):
        """Test that failed session conversion doesn't crash the batch."""
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmpdir:
            projects_dir = Path(tmpdir)

            # Create a project with 2 sessions
            project = projects_dir / "-home-user-projects-test"
            project.mkdir(parents=True)

            # Session 1
            session1 = project / "session1.jsonl"
            session1.write_text(
                '{"type": "user", "timestamp": "2025-01-01T10:00:00.000Z", "message": {"role": "user", "content": "Hello from session 1"}}\n'
            )

            # Session 2
            session2 = project / "session2.jsonl"
            session2.write_text(
                '{"type": "user", "timestamp": "2025-01-02T10:00:00.000Z", "message": {"role": "user", "content": "Hello from session 2"}}\n'
            )

            # Patch generate_html to fail on one specific session
            original_generate_html = __import__("claude_code_transcripts").generate_html

            def mock_generate_html(json_path, output_dir, github_repo=None):
                if "session1" in str(json_path):
                    raise RuntimeError("Simulated failure")
                return original_generate_html(json_path, output_dir, github_repo)

            with patch(
                "claude_code_transcripts.generate_html", side_effect=mock_generate_html
            ):
                stats = generate_batch_html(projects_dir, output_dir)

            # Should have processed session2 successfully
            assert stats["total_sessions"] == 1
            # Should have recorded session1 as failed
            assert len(stats["failed_sessions"]) == 1
            assert "session1" in stats["failed_sessions"][0]["session"]
            assert "Simulated failure" in stats["failed_sessions"][0]["error"]


class TestAllCommand:
    """Tests for the all CLI command."""

    def test_all_command_exists(self):
        """Test that all command is registered."""
        runner = CliRunner()
        result = runner.invoke(cli, ["all", "--help"])
        assert result.exit_code == 0
        assert "all" in result.output.lower() or "convert" in result.output.lower()

    def test_all_dry_run(self, mock_projects_dir, output_dir):
        """Test dry-run mode shows what would be converted."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "all",
                "--source",
                str(mock_projects_dir),
                "--output",
                str(output_dir),
                "--dry-run",
            ],
        )

        assert result.exit_code == 0
        assert "project-a" in result.output
        assert "project-b" in result.output
        # Dry run should not create files
        assert not (output_dir / "index.html").exists()

    def test_all_creates_archive(self, mock_projects_dir, output_dir):
        """Test all command creates full archive."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "all",
                "--source",
                str(mock_projects_dir),
                "--output",
                str(output_dir),
            ],
        )

        assert result.exit_code == 0
        assert (output_dir / "index.html").exists()

    def test_all_include_agents_flag(self, mock_projects_dir, output_dir):
        """Test --include-agents flag includes agent sessions."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "all",
                "--source",
                str(mock_projects_dir),
                "--output",
                str(output_dir),
                "--include-agents",
            ],
        )

        assert result.exit_code == 0
        # Should have agent directory in project-a
        project_a_dir = output_dir / "project-a"
        session_dirs = [d for d in project_a_dir.iterdir() if d.is_dir()]
        assert len(session_dirs) == 3  # 2 regular + 1 agent

    def test_all_quiet_flag(self, mock_projects_dir, output_dir):
        """Test --quiet flag suppresses non-error output."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "all",
                "--source",
                str(mock_projects_dir),
                "--output",
                str(output_dir),
                "--quiet",
            ],
        )

        assert result.exit_code == 0
        # Should create the archive
        assert (output_dir / "index.html").exists()
        # Output should be minimal (no progress messages)
        assert "Scanning" not in result.output
        assert "Processed" not in result.output
        assert "Generating" not in result.output

    def test_all_quiet_with_dry_run(self, mock_projects_dir, output_dir):
        """Test --quiet flag works with --dry-run."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "all",
                "--source",
                str(mock_projects_dir),
                "--output",
                str(output_dir),
                "--dry-run",
                "--quiet",
            ],
        )

        assert result.exit_code == 0
        # Dry run with quiet should produce no output
        assert "Dry run" not in result.output
        assert "project-a" not in result.output
        # Should not create any files
        assert not (output_dir / "index.html").exists()


class TestJsonCommandWithUrl:
    """Tests for the json command with URL support."""

    def test_json_command_accepts_url(self, output_dir):
        """Test that json command can accept a URL starting with http:// or https://."""
        from unittest.mock import patch, MagicMock

        # Sample JSONL content
        jsonl_content = (
            '{"type": "user", "timestamp": "2025-01-01T10:00:00.000Z", "message": {"role": "user", "content": "Hello from URL"}}\n'
            '{"type": "assistant", "timestamp": "2025-01-01T10:00:05.000Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Hi there!"}]}}\n'
        )

        # Mock the httpx.get response
        mock_response = MagicMock()
        mock_response.text = jsonl_content
        mock_response.raise_for_status = MagicMock()

        runner = CliRunner()
        with patch(
            "claude_code_transcripts.httpx.get", return_value=mock_response
        ) as mock_get:
            result = runner.invoke(
                cli,
                [
                    "json",
                    "https://example.com/session.jsonl",
                    "-o",
                    str(output_dir),
                ],
            )

        # Check that the URL was fetched
        mock_get.assert_called_once()
        call_url = mock_get.call_args[0][0]
        assert call_url == "https://example.com/session.jsonl"

        # Check that HTML was generated
        assert result.exit_code == 0
        assert (output_dir / "index.html").exists()

    def test_json_command_accepts_http_url(self, output_dir):
        """Test that json command can accept http:// URLs."""
        from unittest.mock import patch, MagicMock

        jsonl_content = '{"type": "user", "timestamp": "2025-01-01T10:00:00.000Z", "message": {"role": "user", "content": "Hello"}}\n'

        mock_response = MagicMock()
        mock_response.text = jsonl_content
        mock_response.raise_for_status = MagicMock()

        runner = CliRunner()
        with patch(
            "claude_code_transcripts.httpx.get", return_value=mock_response
        ) as mock_get:
            result = runner.invoke(
                cli,
                [
                    "json",
                    "http://example.com/session.jsonl",
                    "-o",
                    str(output_dir),
                ],
            )

        mock_get.assert_called_once()
        assert result.exit_code == 0

    def test_json_command_url_fetch_error(self, output_dir):
        """Test that json command handles URL fetch errors gracefully."""
        from unittest.mock import patch
        import httpx

        runner = CliRunner()
        with patch(
            "claude_code_transcripts.httpx.get",
            side_effect=httpx.RequestError("Network error"),
        ):
            result = runner.invoke(
                cli,
                [
                    "json",
                    "https://example.com/session.jsonl",
                    "-o",
                    str(output_dir),
                ],
            )

        assert result.exit_code != 0
        assert "error" in result.output.lower() or "Error" in result.output

    def test_json_command_still_works_with_local_file(self, output_dir):
        """Test that json command still works with local file paths."""
        # Create a temp JSONL file
        jsonl_file = output_dir / "test.jsonl"
        jsonl_file.write_text(
            '{"type": "user", "timestamp": "2025-01-01T10:00:00.000Z", "message": {"role": "user", "content": "Hello local"}}\n'
            '{"type": "assistant", "timestamp": "2025-01-01T10:00:05.000Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Hi!"}]}}\n'
        )

        html_output = output_dir / "html_output"

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "json",
                str(jsonl_file),
                "-o",
                str(html_output),
            ],
        )

        assert result.exit_code == 0
        assert (html_output / "index.html").exists()


class TestWebCommandRepoFiltering:
    """Tests for the web command repo display and filtering."""

    def test_detect_github_repo_from_session(self):
        """Test that detect_github_repo extracts repo from session loglines."""
        from claude_code_transcripts import detect_github_repo

        loglines = [
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "tool_result",
                            "content": "remote: Create a pull request for 'my-branch' on GitHub by visiting:\nremote:      https://github.com/simonw/datasette/pull/new/my-branch",
                        }
                    ],
                },
            }
        ]
        repo = detect_github_repo(loglines)
        assert repo == "simonw/datasette"

    def test_detect_github_repo_returns_none_when_not_found(self):
        """Test that detect_github_repo returns None when no repo found."""
        from claude_code_transcripts import detect_github_repo

        loglines = [
            {
                "type": "user",
                "message": {"role": "user", "content": "Hello"},
            }
        ]
        repo = detect_github_repo(loglines)
        assert repo is None

    def test_enrich_sessions_with_repos(self):
        """Test enriching sessions with repo information from session metadata."""
        from claude_code_transcripts import enrich_sessions_with_repos

        # Mock sessions from the API list with session_context
        sessions = [
            {
                "id": "sess1",
                "title": "Session 1",
                "created_at": "2025-01-01T10:00:00Z",
                "session_context": {
                    "outcomes": [
                        {
                            "type": "git_repository",
                            "git_info": {"repo": "simonw/datasette", "type": "github"},
                        }
                    ]
                },
            },
            {
                "id": "sess2",
                "title": "Session 2",
                "created_at": "2025-01-02T10:00:00Z",
                "session_context": {},
            },
        ]

        enriched = enrich_sessions_with_repos(sessions)

        assert enriched[0]["repo"] == "simonw/datasette"
        assert enriched[1]["repo"] is None

    def test_extract_repo_from_session_outcomes(self):
        """Test extracting repo from session_context.outcomes."""
        from claude_code_transcripts import extract_repo_from_session

        session = {
            "session_context": {
                "outcomes": [
                    {
                        "type": "git_repository",
                        "git_info": {"repo": "simonw/llm", "type": "github"},
                    }
                ]
            }
        }
        assert extract_repo_from_session(session) == "simonw/llm"

    def test_extract_repo_from_session_sources_url(self):
        """Test extracting repo from session_context.sources URL."""
        from claude_code_transcripts import extract_repo_from_session

        session = {
            "session_context": {
                "sources": [
                    {
                        "type": "git_repository",
                        "url": "https://github.com/simonw/datasette",
                    }
                ]
            }
        }
        assert extract_repo_from_session(session) == "simonw/datasette"

    def test_extract_repo_from_session_no_context(self):
        """Test extracting repo when no session_context exists."""
        from claude_code_transcripts import extract_repo_from_session

        session = {"id": "sess1", "title": "No context"}
        assert extract_repo_from_session(session) is None

    def test_filter_sessions_by_repo(self):
        """Test filtering sessions by repo."""
        from claude_code_transcripts import filter_sessions_by_repo

        sessions = [
            {"id": "sess1", "title": "Session 1", "repo": "simonw/datasette"},
            {"id": "sess2", "title": "Session 2", "repo": "simonw/llm"},
            {"id": "sess3", "title": "Session 3", "repo": None},
        ]

        filtered = filter_sessions_by_repo(sessions, "simonw/datasette")
        assert len(filtered) == 1
        assert filtered[0]["id"] == "sess1"

    def test_filter_sessions_by_repo_none_returns_all(self):
        """Test that filtering with None repo returns all sessions."""
        from claude_code_transcripts import filter_sessions_by_repo

        sessions = [
            {"id": "sess1", "title": "Session 1", "repo": "simonw/datasette"},
            {"id": "sess2", "title": "Session 2", "repo": None},
        ]

        filtered = filter_sessions_by_repo(sessions, None)
        assert len(filtered) == 2

    def test_format_session_for_display_with_repo(self):
        """Test formatting session display with repo first."""
        from claude_code_transcripts import format_session_for_display

        session = {
            "id": "sess1",
            "title": "Fix the bug",
            "created_at": "2025-01-15T10:30:00.000Z",
            "repo": "simonw/datasette",
        }

        display = format_session_for_display(session)
        # Repo should appear first
        assert display.startswith("simonw/datasette")
        assert "2025-01-15T10:30:00" in display
        assert "Fix the bug" in display

    def test_format_session_for_display_without_repo(self):
        """Test formatting session display without repo."""
        from claude_code_transcripts import format_session_for_display

        session = {
            "id": "sess1",
            "title": "Fix the bug",
            "created_at": "2025-01-15T10:30:00.000Z",
            "repo": None,
        }

        display = format_session_for_display(session)
        # Should show (no repo) placeholder
        assert "(no repo)" in display
        assert "Fix the bug" in display
```

## File: `tests/test_generate_html.py`
```python
"""Tests for HTML generation from Claude Code session JSON."""

import json
import tempfile
from pathlib import Path

import pytest
from syrupy.extensions.single_file import SingleFileSnapshotExtension, WriteMode

from claude_code_transcripts import (
    generate_html,
    detect_github_repo,
    render_markdown_text,
    format_json,
    is_json_like,
    render_todo_write,
    render_write_tool,
    render_edit_tool,
    render_bash_tool,
    render_content_block,
    analyze_conversation,
    format_tool_stats,
    is_tool_result_message,
    inject_gist_preview_js,
    create_gist,
    GIST_PREVIEW_JS,
    parse_session_file,
    get_session_summary,
    find_local_sessions,
)


class HTMLSnapshotExtension(SingleFileSnapshotExtension):
    """Snapshot extension that saves HTML files."""

    _write_mode = WriteMode.TEXT
    file_extension = "html"


@pytest.fixture
def snapshot_html(snapshot):
    """Fixture for HTML file snapshots."""
    return snapshot.use_extension(HTMLSnapshotExtension)


@pytest.fixture
def sample_session():
    """Load the sample session fixture."""
    fixture_path = Path(__file__).parent / "sample_session.json"
    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def output_dir():
    """Create a temporary output directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestGenerateHtml:
    """Tests for the main generate_html function."""

    def test_generates_index_html(self, output_dir, snapshot_html):
        """Test index.html generation."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")
        assert index_html == snapshot_html

    def test_generates_page_001_html(self, output_dir, snapshot_html):
        """Test page-001.html generation."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        page_html = (output_dir / "page-001.html").read_text(encoding="utf-8")
        assert page_html == snapshot_html

    def test_generates_page_002_html(self, output_dir, snapshot_html):
        """Test page-002.html generation (continuation page)."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        page_html = (output_dir / "page-002.html").read_text(encoding="utf-8")
        assert page_html == snapshot_html

    def test_github_repo_autodetect(self, sample_session):
        """Test GitHub repo auto-detection from git push output."""
        loglines = sample_session["loglines"]
        repo = detect_github_repo(loglines)
        assert repo == "example/project"

    def test_handles_array_content_format(self, tmp_path):
        """Test that user messages with array content format are recognized.

        Claude Code v2.0.76+ uses array content format like:
        {"type": "user", "message": {"content": [{"type": "text", "text": "..."}]}}
        instead of the simpler string format:
        {"type": "user", "message": {"content": "..."}}
        """
        jsonl_file = tmp_path / "session.jsonl"
        jsonl_file.write_text(
            '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Hello from array format"}]}}\n'
            '{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Hi there!"}]}}\n'
        )

        output_dir = tmp_path / "output"
        output_dir.mkdir()

        generate_html(jsonl_file, output_dir)

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")
        # Should have 1 prompt, not 0
        assert "1 prompts" in index_html or "1 prompt" in index_html
        assert "0 prompts" not in index_html
        # The page file should exist
        assert (output_dir / "page-001.html").exists()


class TestRenderFunctions:
    """Tests for individual render functions."""

    def test_render_markdown_text(self, snapshot_html):
        """Test markdown rendering."""
        result = render_markdown_text("**bold** and `code`\n\n- item 1\n- item 2")
        assert result == snapshot_html

    def test_render_markdown_text_empty(self):
        """Test markdown rendering with empty input."""
        assert render_markdown_text("") == ""
        assert render_markdown_text(None) == ""

    def test_format_json(self, snapshot_html):
        """Test JSON formatting."""
        result = format_json({"key": "value", "number": 42, "nested": {"a": 1}})
        assert result == snapshot_html

    def test_is_json_like(self):
        """Test JSON-like string detection."""
        assert is_json_like('{"key": "value"}')
        assert is_json_like("[1, 2, 3]")
        assert not is_json_like("plain text")
        assert not is_json_like("")
        assert not is_json_like(None)

    def test_render_todo_write(self, snapshot_html):
        """Test TodoWrite rendering."""
        tool_input = {
            "todos": [
                {"content": "First task", "status": "completed", "activeForm": "First"},
                {
                    "content": "Second task",
                    "status": "in_progress",
                    "activeForm": "Second",
                },
                {"content": "Third task", "status": "pending", "activeForm": "Third"},
            ]
        }
        result = render_todo_write(tool_input, "tool-123")
        assert result == snapshot_html

    def test_render_todo_write_empty(self):
        """Test TodoWrite with no todos."""
        result = render_todo_write({"todos": []}, "tool-123")
        assert result == ""

    def test_render_write_tool(self, snapshot_html):
        """Test Write tool rendering."""
        tool_input = {
            "file_path": "/project/src/main.py",
            "content": "def hello():\n    print('hello world')\n",
        }
        result = render_write_tool(tool_input, "tool-123")
        assert result == snapshot_html

    def test_render_edit_tool(self, snapshot_html):
        """Test Edit tool rendering."""
        tool_input = {
            "file_path": "/project/file.py",
            "old_string": "old code here",
            "new_string": "new code here",
        }
        result = render_edit_tool(tool_input, "tool-123")
        assert result == snapshot_html

    def test_render_edit_tool_replace_all(self, snapshot_html):
        """Test Edit tool with replace_all flag."""
        tool_input = {
            "file_path": "/project/file.py",
            "old_string": "old",
            "new_string": "new",
            "replace_all": True,
        }
        result = render_edit_tool(tool_input, "tool-123")
        assert result == snapshot_html

    def test_render_bash_tool(self, snapshot_html):
        """Test Bash tool rendering."""
        tool_input = {
            "command": "pytest tests/ -v",
            "description": "Run tests with verbose output",
        }
        result = render_bash_tool(tool_input, "tool-123")
        assert result == snapshot_html


class TestRenderContentBlock:
    """Tests for render_content_block function."""

    def test_image_block(self, snapshot_html):
        """Test image block rendering with base64 data URL."""
        # 200x200 black GIF - minimal valid GIF with black pixels
        # Generated with: from PIL import Image; img = Image.new('RGB', (200, 200), (0, 0, 0)); img.save('black.gif')
        import base64
        import io

        # Create a minimal 200x200 black GIF using raw bytes
        # GIF89a header + logical screen descriptor + global color table + image data
        gif_data = (
            b"GIF89a"  # Header
            b"\xc8\x00\xc8\x00"  # Width 200, Height 200
            b"\x80"  # Global color table flag (1 color: 2^(0+1)=2 colors)
            b"\x00"  # Background color index
            b"\x00"  # Pixel aspect ratio
            b"\x00\x00\x00"  # Color 0: black
            b"\x00\x00\x00"  # Color 1: black (padding)
            b","  # Image separator
            b"\x00\x00\x00\x00"  # Left, Top
            b"\xc8\x00\xc8\x00"  # Width 200, Height 200
            b"\x00"  # No local color table
            b"\x08"  # LZW minimum code size
            b"\x02\x04\x01\x00"  # Compressed data (minimal)
            b";"  # GIF trailer
        )
        black_gif_base64 = base64.b64encode(gif_data).decode("ascii")

        block = {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/gif",
                "data": black_gif_base64,
            },
        }
        result = render_content_block(block)
        # The result should contain an img tag with data URL
        assert 'src="data:image/gif;base64,' in result
        assert "max-width: 100%" in result
        assert result == snapshot_html

    def test_thinking_block(self, snapshot_html):
        """Test thinking block rendering."""
        block = {
            "type": "thinking",
            "thinking": "Let me think about this...\n\n1. First consideration\n2. Second point",
        }
        result = render_content_block(block)
        assert result == snapshot_html

    def test_text_block(self, snapshot_html):
        """Test text block rendering."""
        block = {"type": "text", "text": "Here is my response with **markdown**."}
        result = render_content_block(block)
        assert result == snapshot_html

    def test_tool_result_block(self, snapshot_html):
        """Test tool result rendering."""
        block = {
            "type": "tool_result",
            "content": "Command completed successfully\nOutput line 1\nOutput line 2",
            "is_error": False,
        }
        result = render_content_block(block)
        assert result == snapshot_html

    def test_tool_result_error(self, snapshot_html):
        """Test tool result error rendering."""
        block = {
            "type": "tool_result",
            "content": "Error: file not found\nTraceback follows...",
            "is_error": True,
        }
        result = render_content_block(block)
        assert result == snapshot_html

    def test_tool_result_with_commit(self, snapshot_html):
        """Test tool result with git commit output."""
        # Need to set the global _github_repo for commit link rendering
        import claude_code_transcripts

        old_repo = claude_code_transcripts._github_repo
        claude_code_transcripts._github_repo = "example/repo"
        try:
            block = {
                "type": "tool_result",
                "content": "[main abc1234] Add new feature\n 2 files changed, 10 insertions(+)",
                "is_error": False,
            }
            result = render_content_block(block)
            assert result == snapshot_html
        finally:
            claude_code_transcripts._github_repo = old_repo

    def test_tool_result_with_image(self, snapshot_html):
        """Test tool result containing image blocks in content array.

        This tests the case where a tool (like a screenshot tool) returns
        both text and image content in the same tool_result.
        """
        import base64

        # Create a minimal GIF image
        gif_data = (
            b"GIF89a"  # Header
            b"\xc8\x00\xc8\x00"  # Width 200, Height 200
            b"\x80"  # Global color table flag
            b"\x00"  # Background color index
            b"\x00"  # Pixel aspect ratio
            b"\x00\x00\x00"  # Color 0: black
            b"\x00\x00\x00"  # Color 1: black
            b","  # Image separator
            b"\x00\x00\x00\x00"  # Left, Top
            b"\xc8\x00\xc8\x00"  # Width 200, Height 200
            b"\x00"  # No local color table
            b"\x08"  # LZW minimum code size
            b"\x02\x04\x01\x00"  # Compressed data
            b";"  # GIF trailer
        )
        gif_base64 = base64.b64encode(gif_data).decode("ascii")

        block = {
            "type": "tool_result",
            "content": [
                {
                    "type": "text",
                    "text": "Successfully captured screenshot (807x782, jpeg) - ID: ss_123",
                },
                {
                    "type": "text",
                    "text": "\n\nTab Context:\n- Executed on tabId: 12345",
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/gif",
                        "data": gif_base64,
                    },
                },
            ],
            "is_error": False,
        }
        result = render_content_block(block)

        # The result should contain the text content
        assert "Successfully captured screenshot" in result
        assert "Tab Context" in result

        # The result should contain an img tag with data URL for the image
        assert 'src="data:image/gif;base64,' in result
        assert "max-width: 100%" in result

        # Tool results with images should NOT be truncatable
        assert "truncatable" not in result

        assert result == snapshot_html


class TestAnalyzeConversation:
    """Tests for conversation analysis."""

    def test_counts_tools(self):
        """Test that tool usage is counted."""
        messages = [
            (
                "assistant",
                json.dumps(
                    {
                        "content": [
                            {
                                "type": "tool_use",
                                "name": "Bash",
                                "id": "1",
                                "input": {},
                            },
                            {
                                "type": "tool_use",
                                "name": "Bash",
                                "id": "2",
                                "input": {},
                            },
                            {
                                "type": "tool_use",
                                "name": "Write",
                                "id": "3",
                                "input": {},
                            },
                        ]
                    }
                ),
                "2025-01-01T00:00:00Z",
            ),
        ]
        result = analyze_conversation(messages)
        assert result["tool_counts"]["Bash"] == 2
        assert result["tool_counts"]["Write"] == 1

    def test_extracts_commits(self):
        """Test that git commits are extracted."""
        messages = [
            (
                "user",
                json.dumps(
                    {
                        "content": [
                            {
                                "type": "tool_result",
                                "content": "[main abc1234] Add new feature\n 1 file changed",
                            }
                        ]
                    }
                ),
                "2025-01-01T00:00:00Z",
            ),
        ]
        result = analyze_conversation(messages)
        assert len(result["commits"]) == 1
        assert result["commits"][0][0] == "abc1234"
        assert "Add new feature" in result["commits"][0][1]


class TestFormatToolStats:
    """Tests for tool stats formatting."""

    def test_formats_counts(self):
        """Test tool count formatting."""
        counts = {"Bash": 5, "Read": 3, "Write": 1}
        result = format_tool_stats(counts)
        assert "5 bash" in result
        assert "3 read" in result
        assert "1 write" in result

    def test_empty_counts(self):
        """Test empty tool counts."""
        assert format_tool_stats({}) == ""


class TestIsToolResultMessage:
    """Tests for tool result message detection."""

    def test_detects_tool_result_only(self):
        """Test detection of tool-result-only messages."""
        message = {"content": [{"type": "tool_result", "content": "result"}]}
        assert is_tool_result_message(message) is True

    def test_rejects_mixed_content(self):
        """Test rejection of mixed content messages."""
        message = {
            "content": [
                {"type": "text", "text": "hello"},
                {"type": "tool_result", "content": "result"},
            ]
        }
        assert is_tool_result_message(message) is False

    def test_rejects_empty(self):
        """Test rejection of empty content."""
        assert is_tool_result_message({"content": []}) is False
        assert is_tool_result_message({"content": "string"}) is False


class TestInjectGistPreviewJs:
    """Tests for the inject_gist_preview_js function."""

    def test_injects_js_into_html_files(self, output_dir):
        """Test that JS is injected before </body> tag."""
        # Create test HTML files
        (output_dir / "index.html").write_text(
            "<html><body><h1>Test</h1></body></html>", encoding="utf-8"
        )
        (output_dir / "page-001.html").write_text(
            "<html><body><p>Page 1</p></body></html>", encoding="utf-8"
        )

        inject_gist_preview_js(output_dir)

        index_content = (output_dir / "index.html").read_text(encoding="utf-8")
        page_content = (output_dir / "page-001.html").read_text(encoding="utf-8")

        # Check JS was injected
        assert GIST_PREVIEW_JS in index_content
        assert GIST_PREVIEW_JS in page_content

        # Check JS is before </body>
        assert index_content.endswith("</body></html>")
        assert "<script>" in index_content

    def test_gist_preview_js_handles_fragment_navigation(self):
        """Test that GIST_PREVIEW_JS includes fragment navigation handling.

        When accessing a gistpreview URL with a fragment like:
        https://gistpreview.github.io/?GIST_ID/page-001.html#msg-2025-12-26T15-30-45-910Z

        The content loads dynamically, so the browser's native fragment
        navigation fails because the element doesn't exist yet. The JS
        should scroll to the fragment element after content loads.
        """
        # The JS should check for fragment in URL
        assert (
            "location.hash" in GIST_PREVIEW_JS
            or "window.location.hash" in GIST_PREVIEW_JS
        )
        # The JS should scroll to the element
        assert "scrollIntoView" in GIST_PREVIEW_JS

    def test_skips_files_without_body(self, output_dir):
        """Test that files without </body> are not modified."""
        original_content = "<html><head><title>Test</title></head></html>"
        (output_dir / "fragment.html").write_text(original_content, encoding="utf-8")

        inject_gist_preview_js(output_dir)

        assert (output_dir / "fragment.html").read_text(
            encoding="utf-8"
        ) == original_content

    def test_handles_empty_directory(self, output_dir):
        """Test that empty directories don't cause errors."""
        inject_gist_preview_js(output_dir)
        # Should complete without error

    def test_gist_preview_js_skips_already_rewritten_links(self):
        """Test that GIST_PREVIEW_JS skips links that have already been rewritten.

        When navigating between pages on gistpreview.github.io, the JS may run
        multiple times. Links that have already been rewritten to the
        ?GIST_ID/filename.html format should be skipped to avoid double-rewriting.

        This fixes issue #26 where pagination links break on later pages.
        """
        # The JS should check if href already starts with '?'
        assert "href.startsWith('?')" in GIST_PREVIEW_JS

    def test_gist_preview_js_uses_mutation_observer(self):
        """Test that GIST_PREVIEW_JS uses MutationObserver for dynamic content.

        gistpreview.github.io loads content dynamically. When navigating between
        pages via SPA-style navigation, new content is inserted without a full
        page reload. The JS needs to use MutationObserver to detect and rewrite
        links in dynamically added content.

        This fixes issue #26 where pagination links break on later pages.
        """
        # The JS should use MutationObserver
        assert "MutationObserver" in GIST_PREVIEW_JS

    def test_gist_preview_js_runs_on_dom_content_loaded(self):
        """Test that GIST_PREVIEW_JS runs on DOMContentLoaded.

        The script is injected at the end of the body, but in some cases
        (especially on gistpreview.github.io), the DOM might not be fully ready
        when the script runs. We should also run on DOMContentLoaded as a fallback.

        This fixes issue #26 where pagination links break on later pages.
        """
        # The JS should listen for DOMContentLoaded
        assert "DOMContentLoaded" in GIST_PREVIEW_JS


class TestCreateGist:
    """Tests for the create_gist function."""

    def test_creates_gist_successfully(self, output_dir, monkeypatch):
        """Test successful gist creation."""
        import subprocess
        import click

        # Create test HTML files
        (output_dir / "index.html").write_text(
            "<html><body>Index</body></html>", encoding="utf-8"
        )
        (output_dir / "page-001.html").write_text(
            "<html><body>Page</body></html>", encoding="utf-8"
        )

        # Mock subprocess.run to simulate successful gh gist create
        mock_result = subprocess.CompletedProcess(
            args=["gh", "gist", "create"],
            returncode=0,
            stdout="https://gist.github.com/testuser/abc123def456\n",
            stderr="",
        )

        def mock_run(*args, **kwargs):
            return mock_result

        monkeypatch.setattr(subprocess, "run", mock_run)

        gist_id, gist_url = create_gist(output_dir)

        assert gist_id == "abc123def456"
        assert gist_url == "https://gist.github.com/testuser/abc123def456"

    def test_raises_on_no_html_files(self, output_dir):
        """Test that error is raised when no HTML files exist."""
        import click

        with pytest.raises(click.ClickException) as exc_info:
            create_gist(output_dir)

        assert "No HTML files found" in str(exc_info.value)

    def test_raises_on_gh_cli_error(self, output_dir, monkeypatch):
        """Test that error is raised when gh CLI fails."""
        import subprocess
        import click

        # Create test HTML file
        (output_dir / "index.html").write_text(
            "<html><body>Test</body></html>", encoding="utf-8"
        )

        # Mock subprocess.run to simulate gh error
        def mock_run(*args, **kwargs):
            raise subprocess.CalledProcessError(
                returncode=1,
                cmd=["gh", "gist", "create"],
                stderr="error: Not logged in",
            )

        monkeypatch.setattr(subprocess, "run", mock_run)

        with pytest.raises(click.ClickException) as exc_info:
            create_gist(output_dir)

        assert "Failed to create gist" in str(exc_info.value)

    def test_raises_on_gh_not_found(self, output_dir, monkeypatch):
        """Test that error is raised when gh CLI is not installed."""
        import subprocess
        import click

        # Create test HTML file
        (output_dir / "index.html").write_text(
            "<html><body>Test</body></html>", encoding="utf-8"
        )

        # Mock subprocess.run to simulate gh not found
        def mock_run(*args, **kwargs):
            raise FileNotFoundError()

        monkeypatch.setattr(subprocess, "run", mock_run)

        with pytest.raises(click.ClickException) as exc_info:
            create_gist(output_dir)

        assert "gh CLI not found" in str(exc_info.value)


class TestSessionGistOption:
    """Tests for the session command --gist option."""

    def test_session_gist_creates_gist(self, monkeypatch, tmp_path):
        """Test that session --gist creates a gist."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import subprocess

        # Create sample session file
        fixture_path = Path(__file__).parent / "sample_session.json"

        # Mock subprocess.run for gh gist create
        mock_result = subprocess.CompletedProcess(
            args=["gh", "gist", "create"],
            returncode=0,
            stdout="https://gist.github.com/testuser/abc123\n",
            stderr="",
        )

        def mock_run(*args, **kwargs):
            return mock_result

        monkeypatch.setattr(subprocess, "run", mock_run)

        # Mock tempfile.gettempdir to use our tmp_path
        monkeypatch.setattr(
            "claude_code_transcripts.tempfile.gettempdir", lambda: str(tmp_path)
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "--gist"],
        )

        assert result.exit_code == 0
        assert "Creating GitHub gist" in result.output
        assert "gist.github.com" in result.output
        assert "gisthost.github.io" in result.output

    def test_session_gist_with_output_dir(self, monkeypatch, output_dir):
        """Test that session --gist with -o uses specified directory."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import subprocess

        fixture_path = Path(__file__).parent / "sample_session.json"

        # Mock subprocess.run for gh gist create
        mock_result = subprocess.CompletedProcess(
            args=["gh", "gist", "create"],
            returncode=0,
            stdout="https://gist.github.com/testuser/abc123\n",
            stderr="",
        )

        def mock_run(*args, **kwargs):
            return mock_result

        monkeypatch.setattr(subprocess, "run", mock_run)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-o", str(output_dir), "--gist"],
        )

        assert result.exit_code == 0
        assert (output_dir / "index.html").exists()
        # Verify JS was injected (checks for both domains for backwards compatibility)
        index_content = (output_dir / "index.html").read_text(encoding="utf-8")
        assert "gisthost.github.io" in index_content


class TestContinuationLongTexts:
    """Tests for long text extraction from continuation conversations."""

    def test_long_text_in_continuation_appears_in_index(self, output_dir):
        """Test that long texts from continuation conversations appear in index.

        This is a regression test for a bug where conversations marked as
        continuations (isCompactSummary=True) were completely skipped when
        building the index, causing their long_texts to be lost.
        """
        # Create a session with:
        # 1. An initial user prompt
        # 2. Some messages
        # 3. A continuation prompt (isCompactSummary=True)
        # 4. An assistant message with a long text summary (>300 chars)
        session_data = {
            "loglines": [
                # Initial user prompt
                {
                    "type": "user",
                    "timestamp": "2025-01-01T10:00:00.000Z",
                    "message": {
                        "content": "Build a Redis JavaScript module",
                        "role": "user",
                    },
                },
                # Some assistant work
                {
                    "type": "assistant",
                    "timestamp": "2025-01-01T10:00:05.000Z",
                    "message": {
                        "role": "assistant",
                        "content": [
                            {"type": "text", "text": "I'll start working on this."}
                        ],
                    },
                },
                # Continuation prompt (context was summarized)
                {
                    "type": "user",
                    "timestamp": "2025-01-01T11:00:00.000Z",
                    "isCompactSummary": True,
                    "message": {
                        "content": "This session is being continued from a previous conversation...",
                        "role": "user",
                    },
                },
                # More assistant work after continuation
                {
                    "type": "assistant",
                    "timestamp": "2025-01-01T11:00:05.000Z",
                    "message": {
                        "role": "assistant",
                        "content": [{"type": "text", "text": "Continuing the work..."}],
                    },
                },
                # Final summary - this is a LONG text (>300 chars) that should appear in index
                {
                    "type": "assistant",
                    "timestamp": "2025-01-01T12:00:00.000Z",
                    "message": {
                        "role": "assistant",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    "All tasks completed successfully. Here's a summary of what was built:\n\n"
                                    "## Redis JavaScript Module\n\n"
                                    "A loadable Redis module providing JavaScript scripting via the mquickjs engine.\n\n"
                                    "### Commands Implemented\n"
                                    "- JS.EVAL - Execute JavaScript with KEYS/ARGV arrays\n"
                                    "- JS.LOAD / JS.CALL - Cache and call scripts by SHA1\n"
                                    "- JS.EXISTS / JS.FLUSH - Manage script cache\n\n"
                                    "All 41 tests pass. Changes pushed to branch."
                                ),
                            }
                        ],
                    },
                },
            ]
        }

        # Write the session to a temp file
        session_file = output_dir / "test_session.json"
        session_file.write_text(json.dumps(session_data), encoding="utf-8")

        # Generate HTML
        generate_html(session_file, output_dir)

        # Read the index.html
        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # The long text summary should appear in the index
        # This is the bug: currently it doesn't because the continuation
        # conversation is skipped entirely
        assert (
            "All tasks completed successfully" in index_html
        ), "Long text from continuation conversation should appear in index"
        assert "Redis JavaScript Module" in index_html


class TestSessionJsonOption:
    """Tests for the session command --json option."""

    def test_session_json_copies_file(self, output_dir):
        """Test that session --json copies the JSON file to output."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        fixture_path = Path(__file__).parent / "sample_session.json"

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-o", str(output_dir), "--json"],
        )

        assert result.exit_code == 0
        json_file = output_dir / "sample_session.json"
        assert json_file.exists()
        assert "JSON:" in result.output
        assert "KB" in result.output

    def test_session_json_preserves_original_name(self, output_dir):
        """Test that --json preserves the original filename."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        fixture_path = Path(__file__).parent / "sample_session.json"

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-o", str(output_dir), "--json"],
        )

        assert result.exit_code == 0
        # Should use original filename, not "session.json"
        assert (output_dir / "sample_session.json").exists()
        assert not (output_dir / "session.json").exists()


class TestImportJsonOption:
    """Tests for the import command --json option."""

    def test_import_json_saves_session_data(self, httpx_mock, output_dir):
        """Test that import --json saves the session JSON."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        # Load sample session to mock API response
        fixture_path = Path(__file__).parent / "sample_session.json"
        with open(fixture_path) as f:
            session_data = json.load(f)

        httpx_mock.add_response(
            url="https://api.anthropic.com/v1/session_ingress/session/test-session-id",
            json=session_data,
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "web",
                "test-session-id",
                "--token",
                "test-token",
                "--org-uuid",
                "test-org",
                "-o",
                str(output_dir),
                "--json",
            ],
        )

        assert result.exit_code == 0
        json_file = output_dir / "test-session-id.json"
        assert json_file.exists()
        assert "JSON:" in result.output
        assert "KB" in result.output

        # Verify JSON content is valid
        with open(json_file) as f:
            saved_data = json.load(f)
        assert saved_data == session_data


class TestImportGistOption:
    """Tests for the import command --gist option."""

    def test_import_gist_creates_gist(self, httpx_mock, monkeypatch, tmp_path):
        """Test that import --gist creates a gist."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import subprocess

        # Load sample session to mock API response
        fixture_path = Path(__file__).parent / "sample_session.json"
        with open(fixture_path) as f:
            session_data = json.load(f)

        httpx_mock.add_response(
            url="https://api.anthropic.com/v1/session_ingress/session/test-session-id",
            json=session_data,
        )

        # Mock subprocess.run for gh gist create
        mock_result = subprocess.CompletedProcess(
            args=["gh", "gist", "create"],
            returncode=0,
            stdout="https://gist.github.com/testuser/def456\n",
            stderr="",
        )

        def mock_run(*args, **kwargs):
            return mock_result

        monkeypatch.setattr(subprocess, "run", mock_run)

        # Mock tempfile.gettempdir
        monkeypatch.setattr(
            "claude_code_transcripts.tempfile.gettempdir", lambda: str(tmp_path)
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "web",
                "test-session-id",
                "--token",
                "test-token",
                "--org-uuid",
                "test-org",
                "--gist",
            ],
        )

        assert result.exit_code == 0
        assert "Creating GitHub gist" in result.output
        assert "gist.github.com" in result.output
        assert "gisthost.github.io" in result.output


class TestVersionOption:
    """Tests for the --version option."""

    def test_version_long_flag(self):
        """Test that --version shows version info."""
        import importlib.metadata
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        runner = CliRunner()
        result = runner.invoke(cli, ["--version"])

        expected_version = importlib.metadata.version("claude-code-transcripts")
        assert result.exit_code == 0
        assert expected_version in result.output

    def test_version_short_flag(self):
        """Test that -v shows version info."""
        import importlib.metadata
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        runner = CliRunner()
        result = runner.invoke(cli, ["-v"])

        expected_version = importlib.metadata.version("claude-code-transcripts")
        assert result.exit_code == 0
        assert expected_version in result.output


class TestOpenOption:
    """Tests for the --open option."""

    def test_session_open_calls_webbrowser(self, output_dir, monkeypatch):
        """Test that session --open opens the browser."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        fixture_path = Path(__file__).parent / "sample_session.json"

        # Track webbrowser.open calls
        opened_urls = []

        def mock_open(url):
            opened_urls.append(url)
            return True

        monkeypatch.setattr("claude_code_transcripts.webbrowser.open", mock_open)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-o", str(output_dir), "--open"],
        )

        assert result.exit_code == 0
        assert len(opened_urls) == 1
        assert "index.html" in opened_urls[0]
        assert opened_urls[0].startswith("file://")

    def test_import_open_calls_webbrowser(self, httpx_mock, output_dir, monkeypatch):
        """Test that import --open opens the browser."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        # Load sample session to mock API response
        fixture_path = Path(__file__).parent / "sample_session.json"
        with open(fixture_path) as f:
            session_data = json.load(f)

        httpx_mock.add_response(
            url="https://api.anthropic.com/v1/session_ingress/session/test-session-id",
            json=session_data,
        )

        # Track webbrowser.open calls
        opened_urls = []

        def mock_open(url):
            opened_urls.append(url)
            return True

        monkeypatch.setattr("claude_code_transcripts.webbrowser.open", mock_open)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "web",
                "test-session-id",
                "--token",
                "test-token",
                "--org-uuid",
                "test-org",
                "-o",
                str(output_dir),
                "--open",
            ],
        )

        assert result.exit_code == 0
        assert len(opened_urls) == 1
        assert "index.html" in opened_urls[0]
        assert opened_urls[0].startswith("file://")


class TestParseSessionFile:
    """Tests for parse_session_file which abstracts both JSON and JSONL formats."""

    def test_parses_json_format(self):
        """Test that standard JSON format is parsed correctly."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        result = parse_session_file(fixture_path)

        assert "loglines" in result
        assert len(result["loglines"]) > 0
        # Check first entry
        first = result["loglines"][0]
        assert first["type"] == "user"
        assert "timestamp" in first
        assert "message" in first

    def test_parses_jsonl_format(self):
        """Test that JSONL format is parsed and converted to standard format."""
        fixture_path = Path(__file__).parent / "sample_session.jsonl"
        result = parse_session_file(fixture_path)

        assert "loglines" in result
        assert len(result["loglines"]) > 0
        # Check structure matches JSON format
        for entry in result["loglines"]:
            assert "type" in entry
            # Skip summary entries which don't have message
            if entry["type"] in ("user", "assistant"):
                assert "timestamp" in entry
                assert "message" in entry

    def test_jsonl_skips_non_message_entries(self):
        """Test that summary and file-history-snapshot entries are skipped."""
        fixture_path = Path(__file__).parent / "sample_session.jsonl"
        result = parse_session_file(fixture_path)

        # None of the loglines should be summary or file-history-snapshot
        for entry in result["loglines"]:
            assert entry["type"] in ("user", "assistant")

    def test_jsonl_preserves_message_content(self):
        """Test that message content is preserved correctly."""
        fixture_path = Path(__file__).parent / "sample_session.jsonl"
        result = parse_session_file(fixture_path)

        # Find the first user message
        user_msg = next(e for e in result["loglines"] if e["type"] == "user")
        assert user_msg["message"]["content"] == "Create a hello world function"

    def test_jsonl_generates_html(self, output_dir, snapshot_html):
        """Test that JSONL files can be converted to HTML."""
        fixture_path = Path(__file__).parent / "sample_session.jsonl"
        generate_html(fixture_path, output_dir)

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")
        assert "hello world" in index_html.lower()
        assert index_html == snapshot_html


class TestGetSessionSummary:
    """Tests for get_session_summary which extracts summary from session files."""

    def test_gets_summary_from_jsonl(self):
        """Test extracting summary from JSONL file."""
        fixture_path = Path(__file__).parent / "sample_session.jsonl"
        summary = get_session_summary(fixture_path)
        assert summary == "Test session for JSONL parsing"

    def test_gets_first_user_message_if_no_summary(self, tmp_path):
        """Test falling back to first user message when no summary entry."""
        jsonl_file = tmp_path / "test.jsonl"
        jsonl_file.write_text(
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello world test"}}\n'
        )
        summary = get_session_summary(jsonl_file)
        assert summary == "Hello world test"

    def test_returns_no_summary_for_empty_file(self, tmp_path):
        """Test handling empty or invalid files."""
        jsonl_file = tmp_path / "empty.jsonl"
        jsonl_file.write_text("", encoding="utf-8")
        summary = get_session_summary(jsonl_file)
        assert summary == "(no summary)"

    def test_truncates_long_summaries(self, tmp_path):
        """Test that long summaries are truncated."""
        jsonl_file = tmp_path / "long.jsonl"
        long_text = "x" * 300
        jsonl_file.write_text(f'{{"type":"summary","summary":"{long_text}"}}\n')
        summary = get_session_summary(jsonl_file, max_length=100)
        assert len(summary) <= 100
        assert summary.endswith("...")


class TestFindLocalSessions:
    """Tests for find_local_sessions which discovers local JSONL files."""

    def test_finds_jsonl_files(self, tmp_path):
        """Test finding JSONL files in projects directory."""
        # Create mock .claude/projects structure
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        # Create a session file
        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Test session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        results = find_local_sessions(tmp_path / ".claude" / "projects", limit=10)
        assert len(results) == 1
        assert results[0][0] == session_file
        assert results[0][1] == "Test session"

    def test_excludes_agent_files(self, tmp_path):
        """Test that agent- prefixed files are excluded."""
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        # Create agent file (should be excluded)
        agent_file = projects_dir / "agent-123.jsonl"
        agent_file.write_text('{"type":"user","message":{"content":"test"}}\n')

        # Create regular file (should be included)
        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Real session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        results = find_local_sessions(tmp_path / ".claude" / "projects", limit=10)
        assert len(results) == 1
        assert "agent-" not in results[0][0].name

    def test_excludes_warmup_sessions(self, tmp_path):
        """Test that warmup sessions are excluded."""
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        # Create warmup file (should be excluded)
        warmup_file = projects_dir / "warmup-session.jsonl"
        warmup_file.write_text('{"type":"summary","summary":"warmup"}\n')

        # Create regular file
        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Real session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        results = find_local_sessions(tmp_path / ".claude" / "projects", limit=10)
        assert len(results) == 1
        assert results[0][1] == "Real session"

    def test_sorts_by_modification_time(self, tmp_path):
        """Test that results are sorted by modification time, newest first."""
        import time

        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        # Create files with different mtimes
        file1 = projects_dir / "older.jsonl"
        file1.write_text(
            '{"type":"summary","summary":"Older"}\n{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"test"}}\n'
        )

        time.sleep(0.1)  # Ensure different mtime

        file2 = projects_dir / "newer.jsonl"
        file2.write_text(
            '{"type":"summary","summary":"Newer"}\n{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"test"}}\n'
        )

        results = find_local_sessions(tmp_path / ".claude" / "projects", limit=10)
        assert len(results) == 2
        assert results[0][1] == "Newer"  # Most recent first
        assert results[1][1] == "Older"

    def test_respects_limit(self, tmp_path):
        """Test that limit parameter is respected."""
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        # Create 5 files
        for i in range(5):
            f = projects_dir / f"session-{i}.jsonl"
            f.write_text(
                f'{{"type":"summary","summary":"Session {i}"}}\n{{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{{"role":"user","content":"test"}}}}\n'
            )

        results = find_local_sessions(tmp_path / ".claude" / "projects", limit=3)
        assert len(results) == 3


class TestLocalSessionCLI:
    """Tests for CLI behavior with local sessions."""

    def test_local_shows_sessions_and_converts(self, tmp_path, monkeypatch):
        """Test that 'local' command shows sessions and converts selected one."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import questionary

        # Create mock .claude/projects structure
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Test local session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        # Mock Path.home() to return our tmp_path
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        # Mock questionary.select to return the session file
        class MockSelect:
            def __init__(self, *args, **kwargs):
                pass

            def ask(self):
                return session_file

        monkeypatch.setattr(questionary, "select", MockSelect)

        runner = CliRunner()
        result = runner.invoke(cli, ["local"])

        assert result.exit_code == 0
        assert "Loading local sessions" in result.output
        assert "Generated" in result.output

    def test_no_args_runs_local_command(self, tmp_path, monkeypatch):
        """Test that running with no arguments runs local command."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import questionary

        # Create mock .claude/projects structure
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Test default session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        # Mock Path.home() to return our tmp_path
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        # Mock questionary.select to return the session file
        class MockSelect:
            def __init__(self, *args, **kwargs):
                pass

            def ask(self):
                return session_file

        monkeypatch.setattr(questionary, "select", MockSelect)

        runner = CliRunner()
        result = runner.invoke(cli, [])

        assert result.exit_code == 0
        assert "Loading local sessions" in result.output

    def test_local_handles_cancelled_selection(self, tmp_path, monkeypatch):
        """Test that local command handles cancelled selection gracefully."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import questionary

        # Create mock .claude/projects structure
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        session_file = projects_dir / "session-123.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Test session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        # Mock Path.home() to return our tmp_path
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        # Mock questionary.select to return None (cancelled)
        class MockSelect:
            def __init__(self, *args, **kwargs):
                pass

            def ask(self):
                return None

        monkeypatch.setattr(questionary, "select", MockSelect)

        runner = CliRunner()
        result = runner.invoke(cli, ["local"])

        assert result.exit_code == 0
        assert "No session selected" in result.output


class TestOutputAutoOption:
    """Tests for the -a/--output-auto flag."""

    def test_json_output_auto_creates_subdirectory(self, tmp_path):
        """Test that json -a creates output subdirectory named after file stem."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        fixture_path = Path(__file__).parent / "sample_session.json"

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-a", "-o", str(tmp_path)],
        )

        assert result.exit_code == 0
        # Output should be in tmp_path/sample_session/
        expected_dir = tmp_path / "sample_session"
        assert expected_dir.exists()
        assert (expected_dir / "index.html").exists()

    def test_json_output_auto_uses_cwd_when_no_output(self, tmp_path, monkeypatch):
        """Test that json -a uses current directory when -o not specified."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import os

        fixture_path = Path(__file__).parent / "sample_session.json"

        # Change to tmp_path
        monkeypatch.chdir(tmp_path)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-a"],
        )

        assert result.exit_code == 0
        # Output should be in ./sample_session/
        expected_dir = tmp_path / "sample_session"
        assert expected_dir.exists()
        assert (expected_dir / "index.html").exists()

    def test_json_output_auto_no_browser_open(self, tmp_path, monkeypatch):
        """Test that json -a does not auto-open browser."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        fixture_path = Path(__file__).parent / "sample_session.json"

        # Track webbrowser.open calls
        opened_urls = []

        def mock_open(url):
            opened_urls.append(url)
            return True

        monkeypatch.setattr("claude_code_transcripts.webbrowser.open", mock_open)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-a", "-o", str(tmp_path)],
        )

        assert result.exit_code == 0
        assert len(opened_urls) == 0  # No browser opened

    def test_local_output_auto_creates_subdirectory(self, tmp_path, monkeypatch):
        """Test that local -a creates output subdirectory named after file stem."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli
        import questionary

        # Create mock .claude/projects structure
        projects_dir = tmp_path / ".claude" / "projects" / "test-project"
        projects_dir.mkdir(parents=True)

        session_file = projects_dir / "my-session-file.jsonl"
        session_file.write_text(
            '{"type":"summary","summary":"Test local session"}\n'
            '{"type":"user","timestamp":"2025-01-01T00:00:00Z","message":{"role":"user","content":"Hello"}}\n'
        )

        output_parent = tmp_path / "output"
        output_parent.mkdir()

        # Mock Path.home() to return our tmp_path
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        # Mock questionary.select to return the session file
        class MockSelect:
            def __init__(self, *args, **kwargs):
                pass

            def ask(self):
                return session_file

        monkeypatch.setattr(questionary, "select", MockSelect)

        runner = CliRunner()
        result = runner.invoke(cli, ["local", "-a", "-o", str(output_parent)])

        assert result.exit_code == 0
        # Output should be in output_parent/my-session-file/
        expected_dir = output_parent / "my-session-file"
        assert expected_dir.exists()
        assert (expected_dir / "index.html").exists()

    def test_web_output_auto_creates_subdirectory(self, httpx_mock, tmp_path):
        """Test that web -a creates output subdirectory named after session ID."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        # Load sample session to mock API response
        fixture_path = Path(__file__).parent / "sample_session.json"
        with open(fixture_path) as f:
            session_data = json.load(f)

        httpx_mock.add_response(
            url="https://api.anthropic.com/v1/session_ingress/session/my-web-session-id",
            json=session_data,
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "web",
                "my-web-session-id",
                "--token",
                "test-token",
                "--org-uuid",
                "test-org",
                "-a",
                "-o",
                str(tmp_path),
            ],
        )

        assert result.exit_code == 0
        # Output should be in tmp_path/my-web-session-id/
        expected_dir = tmp_path / "my-web-session-id"
        assert expected_dir.exists()
        assert (expected_dir / "index.html").exists()

    def test_output_auto_with_jsonl_uses_stem(self, tmp_path, monkeypatch):
        """Test that -a with JSONL file uses file stem (without .jsonl extension)."""
        from click.testing import CliRunner
        from claude_code_transcripts import cli

        # Create a JSONL file
        fixture_path = Path(__file__).parent / "sample_session.jsonl"

        monkeypatch.chdir(tmp_path)

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["json", str(fixture_path), "-a"],
        )

        assert result.exit_code == 0
        # Output should be in ./sample_session/ (not ./sample_session.jsonl/)
        expected_dir = tmp_path / "sample_session"
        assert expected_dir.exists()
        assert (expected_dir / "index.html").exists()


class TestSearchFeature:
    """Tests for the search feature on index.html pages."""

    def test_search_box_in_index_html(self, output_dir):
        """Test that search box is present in index.html."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # Search box should be present with id="search-box"
        assert 'id="search-box"' in index_html
        # Search input should be present
        assert 'id="search-input"' in index_html
        # Search button should be present
        assert 'id="search-btn"' in index_html

    def test_search_modal_in_index_html(self, output_dir):
        """Test that search modal dialog is present in index.html."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # Search modal should be present
        assert 'id="search-modal"' in index_html
        # Results container should be present
        assert 'id="search-results"' in index_html

    def test_search_javascript_present(self, output_dir):
        """Test that search JavaScript functionality is present."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # JavaScript should handle DOMParser for parsing fetched pages
        assert "DOMParser" in index_html
        # JavaScript should handle fetch for getting pages
        assert "fetch(" in index_html
        # JavaScript should handle #search= URL fragment
        assert "#search=" in index_html or "search=" in index_html

    def test_search_css_present(self, output_dir):
        """Test that search CSS styles are present."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # CSS should style the search box
        assert "#search-box" in index_html or ".search-box" in index_html
        # CSS should style the search modal
        assert "#search-modal" in index_html or ".search-modal" in index_html

    def test_search_box_hidden_by_default_in_css(self, output_dir):
        """Test that search box is hidden by default (for progressive enhancement)."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # Search box should be hidden by default in CSS
        # JavaScript will show it when loaded
        assert "search-box" in index_html
        # The JS should show the search box
        assert "style.display" in index_html or "classList" in index_html

    def test_search_total_pages_available(self, output_dir):
        """Test that total_pages is available to JavaScript for fetching."""
        fixture_path = Path(__file__).parent / "sample_session.json"
        generate_html(fixture_path, output_dir, github_repo="example/project")

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")

        # Total pages should be embedded for JS to know how many pages to fetch
        assert "totalPages" in index_html or "total_pages" in index_html
```

## File: `tests/__snapshots__/test_generate_html/TestGenerateHtml.test_generates_index_html.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Code transcript - Index</title>
    <style>
:root { --bg-color: #f5f5f5; --card-bg: #ffffff; --user-bg: #e3f2fd; --user-border: #1976d2; --assistant-bg: #f5f5f5; --assistant-border: #9e9e9e; --thinking-bg: #fff8e1; --thinking-border: #ffc107; --thinking-text: #666; --tool-bg: #f3e5f5; --tool-border: #9c27b0; --tool-result-bg: #e8f5e9; --tool-error-bg: #ffebee; --text-color: #212121; --text-muted: #757575; --code-bg: #263238; --code-text: #aed581; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 16px; line-height: 1.6; }
.container { max-width: 800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin-bottom: 24px; padding-bottom: 8px; border-bottom: 2px solid var(--user-border); }
.header-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-bottom: 2px solid var(--user-border); padding-bottom: 8px; margin-bottom: 24px; }
.header-row h1 { border-bottom: none; padding-bottom: 0; margin-bottom: 0; flex: 1; min-width: 200px; }
.message { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.message.user { background: var(--user-bg); border-left: 4px solid var(--user-border); }
.message.assistant { background: var(--card-bg); border-left: 4px solid var(--assistant-border); }
.message.tool-reply { background: #fff8e1; border-left: 4px solid #ff9800; }
.tool-reply .role-label { color: #e65100; }
.tool-reply .tool-result { background: transparent; padding: 0; margin: 0; }
.tool-reply .tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.message-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.role-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.user .role-label { color: var(--user-border); }
time { color: var(--text-muted); font-size: 0.8rem; }
.timestamp-link { color: inherit; text-decoration: none; }
.timestamp-link:hover { text-decoration: underline; }
.message:target { animation: highlight 2s ease-out; }
@keyframes highlight { 0% { background-color: rgba(25, 118, 210, 0.2); } 100% { background-color: transparent; } }
.message-content { padding: 16px; }
.message-content p { margin: 0 0 12px 0; }
.message-content p:last-child { margin-bottom: 0; }
.thinking { background: var(--thinking-bg); border: 1px solid var(--thinking-border); border-radius: 8px; padding: 12px; margin: 12px 0; font-size: 0.9rem; color: var(--thinking-text); }
.thinking-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: #f57c00; margin-bottom: 8px; }
.thinking p { margin: 8px 0; }
.assistant-text { margin: 8px 0; }
.tool-use { background: var(--tool-bg); border: 1px solid var(--tool-border); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-header { font-weight: 600; color: var(--tool-border); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.tool-icon { font-size: 1.1rem; }
.tool-description { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 8px; font-style: italic; }
.tool-result { background: var(--tool-result-bg); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-result.tool-error { background: var(--tool-error-bg); }
.file-tool { border-radius: 8px; padding: 12px; margin: 12px 0; }
.write-tool { background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%); border: 1px solid #4caf50; }
.edit-tool { background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%); border: 1px solid #ff9800; }
.file-tool-header { font-weight: 600; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.write-header { color: #2e7d32; }
.edit-header { color: #e65100; }
.file-tool-icon { font-size: 1rem; }
.file-tool-path { font-family: monospace; background: rgba(0,0,0,0.08); padding: 2px 8px; border-radius: 4px; }
.file-tool-fullpath { font-family: monospace; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; word-break: break-all; }
.file-content { margin: 0; }
.edit-section { display: flex; margin: 4px 0; border-radius: 4px; overflow: hidden; }
.edit-label { padding: 8px 12px; font-weight: bold; font-family: monospace; display: flex; align-items: flex-start; }
.edit-old { background: #fce4ec; }
.edit-old .edit-label { color: #b71c1c; background: #f8bbd9; }
.edit-old .edit-content { color: #880e4f; }
.edit-new { background: #e8f5e9; }
.edit-new .edit-label { color: #1b5e20; background: #a5d6a7; }
.edit-new .edit-content { color: #1b5e20; }
.edit-content { margin: 0; flex: 1; background: transparent; font-size: 0.85rem; }
.edit-replace-all { font-size: 0.75rem; font-weight: normal; color: var(--text-muted); }
.write-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #e6f4ea); }
.edit-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff0e5); }
.todo-list { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); border: 1px solid #81c784; border-radius: 8px; padding: 12px; margin: 12px 0; }
.todo-header { font-weight: 600; color: #2e7d32; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.todo-items { list-style: none; margin: 0; padding: 0; }
.todo-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(0,0,0,0.06); font-size: 0.9rem; }
.todo-item:last-child { border-bottom: none; }
.todo-icon { flex-shrink: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 50%; }
.todo-completed .todo-icon { color: #2e7d32; background: rgba(46, 125, 50, 0.15); }
.todo-completed .todo-content { color: #558b2f; text-decoration: line-through; }
.todo-in-progress .todo-icon { color: #f57c00; background: rgba(245, 124, 0, 0.15); }
.todo-in-progress .todo-content { color: #e65100; font-weight: 500; }
.todo-pending .todo-icon { color: #757575; background: rgba(0,0,0,0.05); }
.todo-pending .todo-content { color: #616161; }
pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }
pre.json { color: #e0e0e0; }
code { background: rgba(0,0,0,0.08); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre code { background: none; padding: 0; }
.user-content { margin: 0; }
.truncatable { position: relative; }
.truncatable.truncated .truncatable-content { max-height: 200px; overflow: hidden; }
.truncatable.truncated::after { content: ''; position: absolute; bottom: 32px; left: 0; right: 0; height: 60px; background: linear-gradient(to bottom, transparent, var(--card-bg)); pointer-events: none; }
.message.user .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--user-bg)); }
.message.tool-reply .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.tool-use .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-bg)); }
.tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-result-bg)); }
.expand-btn { display: none; width: 100%; padding: 8px 16px; margin-top: 4px; background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; cursor: pointer; font-size: 0.85rem; color: var(--text-muted); }
.expand-btn:hover { background: rgba(0,0,0,0.1); }
.truncatable.truncated .expand-btn, .truncatable.expanded .expand-btn { display: block; }
.pagination { display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; }
.pagination a, .pagination span { padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; }
.pagination a { background: var(--card-bg); color: var(--user-border); border: 1px solid var(--user-border); }
.pagination a:hover { background: var(--user-bg); }
.pagination .current { background: var(--user-border); color: white; }
.pagination .disabled { color: var(--text-muted); border: 1px solid #ddd; }
.pagination .index-link { background: var(--user-border); color: white; }
details.continuation { margin-bottom: 16px; }
details.continuation summary { cursor: pointer; padding: 12px 16px; background: var(--user-bg); border-left: 4px solid var(--user-border); border-radius: 12px; font-weight: 500; color: var(--text-muted); }
details.continuation summary:hover { background: rgba(25, 118, 210, 0.15); }
details.continuation[open] summary { border-radius: 12px 12px 0 0; margin-bottom: 0; }
.index-item { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: var(--user-bg); border-left: 4px solid var(--user-border); }
.index-item a { display: block; text-decoration: none; color: inherit; }
.index-item a:hover { background: rgba(25, 118, 210, 0.1); }
.index-item-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.index-item-number { font-weight: 600; color: var(--user-border); }
.index-item-content { padding: 16px; }
.index-item-stats { padding: 8px 16px 12px 32px; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.06); }
.index-item-commit { margin-top: 6px; padding: 4px 8px; background: #fff3e0; border-radius: 4px; font-size: 0.85rem; color: #e65100; }
.index-item-commit code { background: rgba(0,0,0,0.08); padding: 1px 4px; border-radius: 3px; font-size: 0.8rem; margin-right: 6px; }
.commit-card { margin: 8px 0; padding: 10px 14px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 6px; }
.commit-card a { text-decoration: none; color: #5d4037; display: block; }
.commit-card a:hover { color: #e65100; }
.commit-card-hash { font-family: monospace; color: #e65100; font-weight: 600; margin-right: 8px; }
.index-commit { margin-bottom: 12px; padding: 10px 16px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.index-commit a { display: block; text-decoration: none; color: inherit; }
.index-commit a:hover { background: rgba(255, 152, 0, 0.1); margin: -10px -16px; padding: 10px 16px; border-radius: 8px; }
.index-commit-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; margin-bottom: 4px; }
.index-commit-hash { font-family: monospace; color: #e65100; font-weight: 600; }
.index-commit-msg { color: #5d4037; }
.index-item-long-text { margin-top: 8px; padding: 12px; background: var(--card-bg); border-radius: 8px; border-left: 3px solid var(--assistant-border); }
.index-item-long-text .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--card-bg)); }
.index-item-long-text-content { color: var(--text-color); }
#search-box { display: none; align-items: center; gap: 8px; }
#search-box input { padding: 6px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; width: 180px; }
#search-box button, #modal-search-btn, #modal-close-btn { background: var(--user-border); color: white; border: none; border-radius: 6px; padding: 6px 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#search-box button:hover, #modal-search-btn:hover { background: #1565c0; }
#modal-close-btn { background: var(--text-muted); margin-left: 8px; }
#modal-close-btn:hover { background: #616161; }
#search-modal[open] { border: none; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.2); padding: 0; width: 90vw; max-width: 900px; height: 80vh; max-height: 80vh; display: flex; flex-direction: column; }
#search-modal::backdrop { background: rgba(0,0,0,0.5); }
.search-modal-header { display: flex; align-items: center; gap: 8px; padding: 16px; border-bottom: 1px solid var(--assistant-border); background: var(--bg-color); border-radius: 12px 12px 0 0; }
.search-modal-header input { flex: 1; padding: 8px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; }
#search-status { padding: 8px 16px; font-size: 0.85rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
#search-results { flex: 1; overflow-y: auto; padding: 16px; }
.search-result { margin-bottom: 16px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.search-result a { display: block; text-decoration: none; color: inherit; }
.search-result a:hover { background: rgba(25, 118, 210, 0.05); }
.search-result-page { padding: 6px 12px; background: rgba(0,0,0,0.03); font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
.search-result-content { padding: 12px; }
.search-result mark { background: #fff59d; padding: 1px 2px; border-radius: 2px; }
@media (max-width: 600px) { body { padding: 8px; } .message, .index-item { border-radius: 8px; } .message-content, .index-item-content { padding: 12px; } pre { font-size: 0.8rem; padding: 8px; } #search-box input { width: 120px; } #search-modal[open] { width: 95vw; height: 90vh; } }
</style>
</head>
<body>
    <div class="container">
        <div class="header-row">
            <h1>Claude Code transcript</h1>
            <div id="search-box">
                <input type="text" id="search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
            </div>
        </div>
        

<div class="pagination">
<span class="current">Index</span>
<span class="disabled">&larr; Prev</span>
<a href="page-001.html">1</a>
<a href="page-002.html">2</a>
<a href="page-001.html">Next &rarr;</a>
</div>

        <p style="color: var(--text-muted); margin-bottom: 24px;">5 prompts · 33 messages · 12 tool calls · 2 commits · 2 pages</p>
        
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-00-00-000Z"><div class="index-item-header"><span class="index-item-number">#1</span><time datetime="2025-12-24T10:00:00.000Z" data-timestamp="2025-12-24T10:00:00.000Z">2025-12-24T10:00:00.000Z</time></div><div class="index-item-content"><p>Create a simple Python function to add two numbers</p></div></a><div class="index-item-stats"><span>3 bash · 1 write · 1 todo</span>
</div></div><div class="index-commit"><a href="https://github.com/example/project/commit/abc1234"><div class="index-commit-header"><span class="index-commit-hash">abc1234</span><time datetime="2025-12-24T10:00:40.000Z" data-timestamp="2025-12-24T10:00:40.000Z">2025-12-24T10:00:40.000Z</time></div><div class="index-commit-msg">Add math_utils with add function</div></a></div>
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-01-00-000Z"><div class="index-item-header"><span class="index-item-number">#2</span><time datetime="2025-12-24T10:01:00.000Z" data-timestamp="2025-12-24T10:01:00.000Z">2025-12-24T10:01:00.000Z</time></div><div class="index-item-content"><p>Now edit the file to add a subtract function</p></div></a><div class="index-item-stats"><span>1 glob · 1 edit · 1 grep</span>
</div></div>
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-02-00-000Z"><div class="index-item-header"><span class="index-item-number">#3</span><time datetime="2025-12-24T10:02:00.000Z" data-timestamp="2025-12-24T10:02:00.000Z">2025-12-24T10:02:00.000Z</time></div><div class="index-item-content"><p>Run the tests again</p></div></a><div class="index-item-stats"><span>1 bash</span>
</div></div>
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-03-00-000Z"><div class="index-item-header"><span class="index-item-number">#4</span><time datetime="2025-12-24T10:03:00.000Z" data-timestamp="2025-12-24T10:03:00.000Z">2025-12-24T10:03:00.000Z</time></div><div class="index-item-content"><p>Fix the issue and commit</p></div></a><div class="index-item-stats"><span>1 edit · 1 bash</span>
</div></div><div class="index-commit"><a href="https://github.com/example/project/commit/def5678"><div class="index-commit-header"><span class="index-commit-hash">def5678</span><time datetime="2025-12-24T10:03:20.000Z" data-timestamp="2025-12-24T10:03:20.000Z">2025-12-24T10:03:20.000Z</time></div><div class="index-commit-msg">Add subtract function and fix tests</div></a></div>
<div class="index-item"><a href="page-002.html#msg-2025-12-24T10-05-00-000Z"><div class="index-item-header"><span class="index-item-number">#5</span><time datetime="2025-12-24T10:05:00.000Z" data-timestamp="2025-12-24T10:05:00.000Z">2025-12-24T10:05:00.000Z</time></div><div class="index-item-content"><p>Add a multiply function too</p></div></a><div class="index-item-stats"><span>1 edit</span>
</div></div>
        

<div class="pagination">
<span class="current">Index</span>
<span class="disabled">&larr; Prev</span>
<a href="page-001.html">1</a>
<a href="page-002.html">2</a>
<a href="page-001.html">Next &rarr;</a>
</div>


        <dialog id="search-modal">
            <div class="search-modal-header">
                <input type="text" id="modal-search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="modal-search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
                <button id="modal-close-btn" type="button" aria-label="Close">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg>
                </button>
            </div>
            <div id="search-status"></div>
            <div id="search-results"></div>
        </dialog>
        <script>
(function() {
    var totalPages = 2;
    var searchBox = document.getElementById('search-box');
    var searchInput = document.getElementById('search-input');
    var searchBtn = document.getElementById('search-btn');
    var modal = document.getElementById('search-modal');
    var modalInput = document.getElementById('modal-search-input');
    var modalSearchBtn = document.getElementById('modal-search-btn');
    var modalCloseBtn = document.getElementById('modal-close-btn');
    var searchStatus = document.getElementById('search-status');
    var searchResults = document.getElementById('search-results');

    if (!searchBox || !modal) return;

    // Hide search on file:// protocol (doesn't work due to CORS restrictions)
    if (window.location.protocol === 'file:') return;

    // Show search box (progressive enhancement)
    searchBox.style.display = 'flex';

    // Gist preview support - detect if we're on gisthost.github.io or gistpreview.github.io
    var hostname = window.location.hostname;
    var isGistPreview = hostname === 'gisthost.github.io' || hostname === 'gistpreview.github.io';
    var gistId = null;
    var gistOwner = null;
    var gistInfoLoaded = false;

    if (isGistPreview) {
        // Extract gist ID from URL query string like ?78a436a8a9e7a2e603738b8193b95410/index.html
        var queryMatch = window.location.search.match(/^\?([a-f0-9]+)/i);
        if (queryMatch) {
            gistId = queryMatch[1];
        }
    }

    async function loadGistInfo() {
        if (!isGistPreview || !gistId || gistInfoLoaded) return;
        try {
            var response = await fetch('https://api.github.com/gists/' + gistId);
            if (response.ok) {
                var info = await response.json();
                gistOwner = info.owner.login;
                gistInfoLoaded = true;
            }
        } catch (e) {
            console.error('Failed to load gist info:', e);
        }
    }

    function getPageFetchUrl(pageFile) {
        if (isGistPreview && gistOwner && gistId) {
            // Use raw gist URL for fetching content
            return 'https://gist.githubusercontent.com/' + gistOwner + '/' + gistId + '/raw/' + pageFile;
        }
        return pageFile;
    }

    function getPageLinkUrl(pageFile) {
        if (isGistPreview && gistId) {
            // Use gistpreview URL format for navigation links
            return '?' + gistId + '/' + pageFile;
        }
        return pageFile;
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function openModal(query) {
        modalInput.value = query || '';
        searchResults.innerHTML = '';
        searchStatus.textContent = '';
        modal.showModal();
        modalInput.focus();
        if (query) {
            performSearch(query);
        }
    }

    function closeModal() {
        modal.close();
        // Update URL to remove search fragment, preserving path and query string
        if (window.location.hash.startsWith('#search=')) {
            history.replaceState(null, '', window.location.pathname + window.location.search);
        }
    }

    function updateUrlHash(query) {
        if (query) {
            // Preserve path and query string when adding hash
            history.replaceState(null, '', window.location.pathname + window.location.search + '#search=' + encodeURIComponent(query));
        }
    }

    function highlightTextNodes(element, searchTerm) {
        var walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
        var nodesToReplace = [];

        while (walker.nextNode()) {
            var node = walker.currentNode;
            if (node.nodeValue.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) {
                nodesToReplace.push(node);
            }
        }

        nodesToReplace.forEach(function(node) {
            var text = node.nodeValue;
            var regex = new RegExp('(' + escapeRegex(searchTerm) + ')', 'gi');
            var parts = text.split(regex);
            if (parts.length > 1) {
                var span = document.createElement('span');
                parts.forEach(function(part) {
                    if (part.toLowerCase() === searchTerm.toLowerCase()) {
                        var mark = document.createElement('mark');
                        mark.textContent = part;
                        span.appendChild(mark);
                    } else {
                        span.appendChild(document.createTextNode(part));
                    }
                });
                node.parentNode.replaceChild(span, node);
            }
        });
    }

    function fixInternalLinks(element, pageFile) {
        // Update all internal anchor links to include the page file
        var links = element.querySelectorAll('a[href^="#"]');
        links.forEach(function(link) {
            var href = link.getAttribute('href');
            link.setAttribute('href', pageFile + href);
        });
    }

    function processPage(pageFile, html, query) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var resultsFromPage = 0;

        // Find all message blocks
        var messages = doc.querySelectorAll('.message');
        messages.forEach(function(msg) {
            var text = msg.textContent || '';
            if (text.toLowerCase().indexOf(query.toLowerCase()) !== -1) {
                resultsFromPage++;

                // Get the message ID for linking
                var msgId = msg.id || '';
                var pageLinkUrl = getPageLinkUrl(pageFile);
                var link = pageLinkUrl + (msgId ? '#' + msgId : '');

                // Clone the message HTML and highlight matches
                var clone = msg.cloneNode(true);
                // Fix internal links to include the page file
                fixInternalLinks(clone, pageLinkUrl);
                highlightTextNodes(clone, query);

                var resultDiv = document.createElement('div');
                resultDiv.className = 'search-result';
                resultDiv.innerHTML = '<a href="' + link + '">' +
                    '<div class="search-result-page">' + escapeHtml(pageFile) + '</div>' +
                    '<div class="search-result-content">' + clone.innerHTML + '</div>' +
                    '</a>';
                searchResults.appendChild(resultDiv);
            }
        });

        return resultsFromPage;
    }

    async function performSearch(query) {
        if (!query.trim()) {
            searchStatus.textContent = 'Enter a search term';
            return;
        }

        updateUrlHash(query);
        searchResults.innerHTML = '';
        searchStatus.textContent = 'Searching...';

        // Load gist info if on gistpreview (needed for constructing URLs)
        if (isGistPreview && !gistInfoLoaded) {
            searchStatus.textContent = 'Loading gist info...';
            await loadGistInfo();
            if (!gistOwner) {
                searchStatus.textContent = 'Failed to load gist info. Search unavailable.';
                return;
            }
        }

        var resultsFound = 0;
        var pagesSearched = 0;

        // Build list of pages to fetch
        var pagesToFetch = [];
        for (var i = 1; i <= totalPages; i++) {
            pagesToFetch.push('page-' + String(i).padStart(3, '0') + '.html');
        }

        searchStatus.textContent = 'Searching...';

        // Process pages in batches of 3, but show results immediately as each completes
        var batchSize = 3;
        for (var i = 0; i < pagesToFetch.length; i += batchSize) {
            var batch = pagesToFetch.slice(i, i + batchSize);

            // Create promises that process results immediately when each fetch completes
            var promises = batch.map(function(pageFile) {
                return fetch(getPageFetchUrl(pageFile))
                    .then(function(response) {
                        if (!response.ok) throw new Error('Failed to fetch');
                        return response.text();
                    })
                    .then(function(html) {
                        // Process and display results immediately
                        var count = processPage(pageFile, html, query);
                        resultsFound += count;
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    })
                    .catch(function() {
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    });
            });

            // Wait for this batch to complete before starting the next
            await Promise.all(promises);
        }

        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + totalPages + ' pages';
    }

    // Event listeners
    searchBtn.addEventListener('click', function() {
        openModal(searchInput.value);
    });

    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            openModal(searchInput.value);
        }
    });

    modalSearchBtn.addEventListener('click', function() {
        performSearch(modalInput.value);
    });

    modalInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            performSearch(modalInput.value);
        }
    });

    modalCloseBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Check for #search= in URL on page load
    if (window.location.hash.startsWith('#search=')) {
        var query = decodeURIComponent(window.location.hash.substring(8));
        if (query) {
            searchInput.value = query;
            openModal(query);
        }
    }
})();
        </script>
    </div>
    <script>
document.querySelectorAll('time[data-timestamp]').forEach(function(el) {
    const timestamp = el.getAttribute('data-timestamp');
    const date = new Date(timestamp);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const timeStr = date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    if (isToday) { el.textContent = timeStr; }
    else { el.textContent = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' + timeStr; }
});
document.querySelectorAll('pre.json').forEach(function(el) {
    let text = el.textContent;
    text = text.replace(/"([^"]+)":/g, '<span style="color: #ce93d8">"$1"</span>:');
    text = text.replace(/: "([^"]*)"/g, ': <span style="color: #81d4fa">"$1"</span>');
    text = text.replace(/: (\d+)/g, ': <span style="color: #ffcc80">$1</span>');
    text = text.replace(/: (true|false|null)/g, ': <span style="color: #f48fb1">$1</span>');
    el.innerHTML = text;
});
document.querySelectorAll('.truncatable').forEach(function(wrapper) {
    const content = wrapper.querySelector('.truncatable-content');
    const btn = wrapper.querySelector('.expand-btn');
    if (content.scrollHeight > 250) {
        wrapper.classList.add('truncated');
        btn.addEventListener('click', function() {
            if (wrapper.classList.contains('truncated')) { wrapper.classList.remove('truncated'); wrapper.classList.add('expanded'); btn.textContent = 'Show less'; }
            else { wrapper.classList.remove('expanded'); wrapper.classList.add('truncated'); btn.textContent = 'Show more'; }
        });
    }
});
</script>
</body>
</html>
```

## File: `tests/__snapshots__/test_generate_html/TestGenerateHtml.test_generates_page_001_html.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Code transcript - page 1</title>
    <style>
:root { --bg-color: #f5f5f5; --card-bg: #ffffff; --user-bg: #e3f2fd; --user-border: #1976d2; --assistant-bg: #f5f5f5; --assistant-border: #9e9e9e; --thinking-bg: #fff8e1; --thinking-border: #ffc107; --thinking-text: #666; --tool-bg: #f3e5f5; --tool-border: #9c27b0; --tool-result-bg: #e8f5e9; --tool-error-bg: #ffebee; --text-color: #212121; --text-muted: #757575; --code-bg: #263238; --code-text: #aed581; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 16px; line-height: 1.6; }
.container { max-width: 800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin-bottom: 24px; padding-bottom: 8px; border-bottom: 2px solid var(--user-border); }
.header-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-bottom: 2px solid var(--user-border); padding-bottom: 8px; margin-bottom: 24px; }
.header-row h1 { border-bottom: none; padding-bottom: 0; margin-bottom: 0; flex: 1; min-width: 200px; }
.message { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.message.user { background: var(--user-bg); border-left: 4px solid var(--user-border); }
.message.assistant { background: var(--card-bg); border-left: 4px solid var(--assistant-border); }
.message.tool-reply { background: #fff8e1; border-left: 4px solid #ff9800; }
.tool-reply .role-label { color: #e65100; }
.tool-reply .tool-result { background: transparent; padding: 0; margin: 0; }
.tool-reply .tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.message-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.role-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.user .role-label { color: var(--user-border); }
time { color: var(--text-muted); font-size: 0.8rem; }
.timestamp-link { color: inherit; text-decoration: none; }
.timestamp-link:hover { text-decoration: underline; }
.message:target { animation: highlight 2s ease-out; }
@keyframes highlight { 0% { background-color: rgba(25, 118, 210, 0.2); } 100% { background-color: transparent; } }
.message-content { padding: 16px; }
.message-content p { margin: 0 0 12px 0; }
.message-content p:last-child { margin-bottom: 0; }
.thinking { background: var(--thinking-bg); border: 1px solid var(--thinking-border); border-radius: 8px; padding: 12px; margin: 12px 0; font-size: 0.9rem; color: var(--thinking-text); }
.thinking-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: #f57c00; margin-bottom: 8px; }
.thinking p { margin: 8px 0; }
.assistant-text { margin: 8px 0; }
.tool-use { background: var(--tool-bg); border: 1px solid var(--tool-border); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-header { font-weight: 600; color: var(--tool-border); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.tool-icon { font-size: 1.1rem; }
.tool-description { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 8px; font-style: italic; }
.tool-result { background: var(--tool-result-bg); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-result.tool-error { background: var(--tool-error-bg); }
.file-tool { border-radius: 8px; padding: 12px; margin: 12px 0; }
.write-tool { background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%); border: 1px solid #4caf50; }
.edit-tool { background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%); border: 1px solid #ff9800; }
.file-tool-header { font-weight: 600; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.write-header { color: #2e7d32; }
.edit-header { color: #e65100; }
.file-tool-icon { font-size: 1rem; }
.file-tool-path { font-family: monospace; background: rgba(0,0,0,0.08); padding: 2px 8px; border-radius: 4px; }
.file-tool-fullpath { font-family: monospace; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; word-break: break-all; }
.file-content { margin: 0; }
.edit-section { display: flex; margin: 4px 0; border-radius: 4px; overflow: hidden; }
.edit-label { padding: 8px 12px; font-weight: bold; font-family: monospace; display: flex; align-items: flex-start; }
.edit-old { background: #fce4ec; }
.edit-old .edit-label { color: #b71c1c; background: #f8bbd9; }
.edit-old .edit-content { color: #880e4f; }
.edit-new { background: #e8f5e9; }
.edit-new .edit-label { color: #1b5e20; background: #a5d6a7; }
.edit-new .edit-content { color: #1b5e20; }
.edit-content { margin: 0; flex: 1; background: transparent; font-size: 0.85rem; }
.edit-replace-all { font-size: 0.75rem; font-weight: normal; color: var(--text-muted); }
.write-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #e6f4ea); }
.edit-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff0e5); }
.todo-list { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); border: 1px solid #81c784; border-radius: 8px; padding: 12px; margin: 12px 0; }
.todo-header { font-weight: 600; color: #2e7d32; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.todo-items { list-style: none; margin: 0; padding: 0; }
.todo-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(0,0,0,0.06); font-size: 0.9rem; }
.todo-item:last-child { border-bottom: none; }
.todo-icon { flex-shrink: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 50%; }
.todo-completed .todo-icon { color: #2e7d32; background: rgba(46, 125, 50, 0.15); }
.todo-completed .todo-content { color: #558b2f; text-decoration: line-through; }
.todo-in-progress .todo-icon { color: #f57c00; background: rgba(245, 124, 0, 0.15); }
.todo-in-progress .todo-content { color: #e65100; font-weight: 500; }
.todo-pending .todo-icon { color: #757575; background: rgba(0,0,0,0.05); }
.todo-pending .todo-content { color: #616161; }
pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }
pre.json { color: #e0e0e0; }
code { background: rgba(0,0,0,0.08); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre code { background: none; padding: 0; }
.user-content { margin: 0; }
.truncatable { position: relative; }
.truncatable.truncated .truncatable-content { max-height: 200px; overflow: hidden; }
.truncatable.truncated::after { content: ''; position: absolute; bottom: 32px; left: 0; right: 0; height: 60px; background: linear-gradient(to bottom, transparent, var(--card-bg)); pointer-events: none; }
.message.user .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--user-bg)); }
.message.tool-reply .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.tool-use .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-bg)); }
.tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-result-bg)); }
.expand-btn { display: none; width: 100%; padding: 8px 16px; margin-top: 4px; background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; cursor: pointer; font-size: 0.85rem; color: var(--text-muted); }
.expand-btn:hover { background: rgba(0,0,0,0.1); }
.truncatable.truncated .expand-btn, .truncatable.expanded .expand-btn { display: block; }
.pagination { display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; }
.pagination a, .pagination span { padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; }
.pagination a { background: var(--card-bg); color: var(--user-border); border: 1px solid var(--user-border); }
.pagination a:hover { background: var(--user-bg); }
.pagination .current { background: var(--user-border); color: white; }
.pagination .disabled { color: var(--text-muted); border: 1px solid #ddd; }
.pagination .index-link { background: var(--user-border); color: white; }
details.continuation { margin-bottom: 16px; }
details.continuation summary { cursor: pointer; padding: 12px 16px; background: var(--user-bg); border-left: 4px solid var(--user-border); border-radius: 12px; font-weight: 500; color: var(--text-muted); }
details.continuation summary:hover { background: rgba(25, 118, 210, 0.15); }
details.continuation[open] summary { border-radius: 12px 12px 0 0; margin-bottom: 0; }
.index-item { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: var(--user-bg); border-left: 4px solid var(--user-border); }
.index-item a { display: block; text-decoration: none; color: inherit; }
.index-item a:hover { background: rgba(25, 118, 210, 0.1); }
.index-item-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.index-item-number { font-weight: 600; color: var(--user-border); }
.index-item-content { padding: 16px; }
.index-item-stats { padding: 8px 16px 12px 32px; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.06); }
.index-item-commit { margin-top: 6px; padding: 4px 8px; background: #fff3e0; border-radius: 4px; font-size: 0.85rem; color: #e65100; }
.index-item-commit code { background: rgba(0,0,0,0.08); padding: 1px 4px; border-radius: 3px; font-size: 0.8rem; margin-right: 6px; }
.commit-card { margin: 8px 0; padding: 10px 14px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 6px; }
.commit-card a { text-decoration: none; color: #5d4037; display: block; }
.commit-card a:hover { color: #e65100; }
.commit-card-hash { font-family: monospace; color: #e65100; font-weight: 600; margin-right: 8px; }
.index-commit { margin-bottom: 12px; padding: 10px 16px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.index-commit a { display: block; text-decoration: none; color: inherit; }
.index-commit a:hover { background: rgba(255, 152, 0, 0.1); margin: -10px -16px; padding: 10px 16px; border-radius: 8px; }
.index-commit-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; margin-bottom: 4px; }
.index-commit-hash { font-family: monospace; color: #e65100; font-weight: 600; }
.index-commit-msg { color: #5d4037; }
.index-item-long-text { margin-top: 8px; padding: 12px; background: var(--card-bg); border-radius: 8px; border-left: 3px solid var(--assistant-border); }
.index-item-long-text .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--card-bg)); }
.index-item-long-text-content { color: var(--text-color); }
#search-box { display: none; align-items: center; gap: 8px; }
#search-box input { padding: 6px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; width: 180px; }
#search-box button, #modal-search-btn, #modal-close-btn { background: var(--user-border); color: white; border: none; border-radius: 6px; padding: 6px 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#search-box button:hover, #modal-search-btn:hover { background: #1565c0; }
#modal-close-btn { background: var(--text-muted); margin-left: 8px; }
#modal-close-btn:hover { background: #616161; }
#search-modal[open] { border: none; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.2); padding: 0; width: 90vw; max-width: 900px; height: 80vh; max-height: 80vh; display: flex; flex-direction: column; }
#search-modal::backdrop { background: rgba(0,0,0,0.5); }
.search-modal-header { display: flex; align-items: center; gap: 8px; padding: 16px; border-bottom: 1px solid var(--assistant-border); background: var(--bg-color); border-radius: 12px 12px 0 0; }
.search-modal-header input { flex: 1; padding: 8px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; }
#search-status { padding: 8px 16px; font-size: 0.85rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
#search-results { flex: 1; overflow-y: auto; padding: 16px; }
.search-result { margin-bottom: 16px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.search-result a { display: block; text-decoration: none; color: inherit; }
.search-result a:hover { background: rgba(25, 118, 210, 0.05); }
.search-result-page { padding: 6px 12px; background: rgba(0,0,0,0.03); font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
.search-result-content { padding: 12px; }
.search-result mark { background: #fff59d; padding: 1px 2px; border-radius: 2px; }
@media (max-width: 600px) { body { padding: 8px; } .message, .index-item { border-radius: 8px; } .message-content, .index-item-content { padding: 12px; } pre { font-size: 0.8rem; padding: 8px; } #search-box input { width: 120px; } #search-modal[open] { width: 95vw; height: 90vh; } }
</style>
</head>
<body>
    <div class="container">
        <h1><a href="index.html" style="color: inherit; text-decoration: none;">Claude Code transcript</a> - page 1/2</h1>
        

<div class="pagination">
<a href="index.html" class="index-link">Index</a>
<span class="disabled">&larr; Prev</span>
<span class="current">1</span>
<a href="page-002.html">2</a>
<a href="page-002.html">Next &rarr;</a>
</div>

        
<div class="message user" id="msg-2025-12-24T10-00-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-00-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:00.000Z" data-timestamp="2025-12-24T10:00:00.000Z">2025-12-24T10:00:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>Create a simple Python function to add two numbers</p></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-00-05-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-00-05-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:05.000Z" data-timestamp="2025-12-24T10:00:05.000Z">2025-12-24T10:00:05.000Z</time></a></div><div class="message-content">
<div class="thinking"><div class="thinking-label">Thinking</div><p>The user wants a simple addition function. I should:
1. Create the function
2. Add a basic test</p>
<p>This is straightforward.</p></div>
<div class="assistant-text"><p>I'll create a simple Python function for you. Let me write it now.</p></div><div class="file-tool write-tool" data-tool-id="toolu_write_001">
<div class="file-tool-header write-header"><span class="file-tool-icon">📝</span> Write <span class="file-tool-path">math_utils.py</span></div>
<div class="file-tool-fullpath">/project/math_utils.py</div>
<div class="truncatable"><div class="truncatable-content"><pre class="file-content">def add(a: int, b: int) -&gt; int:
    &#34;&#34;&#34;Add two numbers together.&#34;&#34;&#34;
    return a + b
</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-00-10-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-00-10-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:10.000Z" data-timestamp="2025-12-24T10:00:10.000Z">2025-12-24T10:00:10.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>File written successfully</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-00-15-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-00-15-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:15.000Z" data-timestamp="2025-12-24T10:00:15.000Z">2025-12-24T10:00:15.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>I've created the <code>add</code> function. Now let me run the tests.</p></div>
<div class="tool-use bash-tool" data-tool-id="toolu_bash_001">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Run pytest on tests directory</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">python -m pytest tests/</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-00-20-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-00-20-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:20.000Z" data-timestamp="2025-12-24T10:00:20.000Z">2025-12-24T10:00:20.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>===== test session starts =====
collected 2 items

tests/test_math.py ..  [100%]

===== 2 passed in 0.05s =====</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-00-25-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-00-25-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:25.000Z" data-timestamp="2025-12-24T10:00:25.000Z">2025-12-24T10:00:25.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>All tests pass. Let me update the todo list and make a commit.</p></div>
<div class="todo-list" data-tool-id="toolu_todo_001"><div class="todo-header"><span class="todo-header-icon">☰</span> Task List</div><ul class="todo-items"><li class="todo-item todo-completed"><span class="todo-icon">✓</span><span class="todo-content">Create add function</span></li><li class="todo-item todo-completed"><span class="todo-icon">✓</span><span class="todo-content">Write tests</span></li><li class="todo-item todo-completed"><span class="todo-icon">✓</span><span class="todo-content">Run tests</span></li><li class="todo-item todo-in-progress"><span class="todo-icon">→</span><span class="todo-content">Commit changes</span></li><li class="todo-item todo-pending"><span class="todo-icon">○</span><span class="todo-content">Push to remote</span></li></ul></div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-00-30-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-00-30-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:30.000Z" data-timestamp="2025-12-24T10:00:30.000Z">2025-12-24T10:00:30.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>Todos updated</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-00-35-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-00-35-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:35.000Z" data-timestamp="2025-12-24T10:00:35.000Z">2025-12-24T10:00:35.000Z</time></a></div><div class="message-content">
<div class="tool-use bash-tool" data-tool-id="toolu_bash_002">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Commit changes</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">git add . &amp;&amp; git commit -m &#39;Add math_utils with add function&#39;</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-00-40-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-00-40-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:40.000Z" data-timestamp="2025-12-24T10:00:40.000Z">2025-12-24T10:00:40.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><div class="commit-card"><a href="https://github.com/example/project/commit/abc1234"><span class="commit-card-hash">abc1234</span> Add math_utils with add function</a></div><pre>1 file changed, 5 insertions(+)</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-00-45-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-00-45-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:45.000Z" data-timestamp="2025-12-24T10:00:45.000Z">2025-12-24T10:00:45.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>Committed! Now pushing to remote.</p></div>
<div class="tool-use bash-tool" data-tool-id="toolu_bash_003">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Push to remote</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">git push -u origin main</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-00-50-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-00-50-000Z" class="timestamp-link"><time datetime="2025-12-24T10:00:50.000Z" data-timestamp="2025-12-24T10:00:50.000Z">2025-12-24T10:00:50.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>remote: 
remote: Create a pull request for &#x27;main&#x27; on GitHub by visiting:
remote:      https://github.com/example/project/pull/new/main
remote: 
To github.com:example/project.git
   def5678..abc1234  main -&gt; main</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message user" id="msg-2025-12-24T10-01-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-01-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:00.000Z" data-timestamp="2025-12-24T10:01:00.000Z">2025-12-24T10:01:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>Now edit the file to add a subtract function</p></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-01-05-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-01-05-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:05.000Z" data-timestamp="2025-12-24T10:01:05.000Z">2025-12-24T10:01:05.000Z</time></a></div><div class="message-content">
<div class="tool-use" data-tool-id="toolu_glob_001"><div class="tool-header"><span class="tool-icon">⚙</span> Glob</div><div class="truncatable"><div class="truncatable-content"><pre class="json">{
  &#34;pattern&#34;: &#34;**/*.py&#34;,
  &#34;path&#34;: &#34;/project&#34;
}</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-01-10-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-01-10-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:10.000Z" data-timestamp="2025-12-24T10:01:10.000Z">2025-12-24T10:01:10.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>/project/math_utils.py
/project/tests/test_math.py</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-01-15-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-01-15-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:15.000Z" data-timestamp="2025-12-24T10:01:15.000Z">2025-12-24T10:01:15.000Z</time></a></div><div class="message-content"><div class="file-tool edit-tool" data-tool-id="toolu_edit_001">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">math_utils.py</span></div>
<div class="file-tool-fullpath">/project/math_utils.py</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">    return a + b
</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">    return a + b


def subtract(a: int, b: int) -&gt; int:
    &#34;&#34;&#34;Subtract b from a.&#34;&#34;&#34;
    return a - b
</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-01-20-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-01-20-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:20.000Z" data-timestamp="2025-12-24T10:01:20.000Z">2025-12-24T10:01:20.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>File edited successfully</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-01-25-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-01-25-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:25.000Z" data-timestamp="2025-12-24T10:01:25.000Z">2025-12-24T10:01:25.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>Added the subtract function. Let me verify with grep.</p></div>
<div class="tool-use" data-tool-id="toolu_grep_001"><div class="tool-header"><span class="tool-icon">⚙</span> Grep</div><div class="truncatable"><div class="truncatable-content"><pre class="json">{
  &#34;pattern&#34;: &#34;def subtract&#34;,
  &#34;path&#34;: &#34;/project&#34;,
  &#34;output_mode&#34;: &#34;content&#34;
}</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-01-30-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-01-30-000Z" class="timestamp-link"><time datetime="2025-12-24T10:01:30.000Z" data-timestamp="2025-12-24T10:01:30.000Z">2025-12-24T10:01:30.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>/project/math_utils.py:6:def subtract(a: int, b: int) -&gt; int:</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message user" id="msg-2025-12-24T10-02-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-02-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:02:00.000Z" data-timestamp="2025-12-24T10:02:00.000Z">2025-12-24T10:02:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>Run the tests again</p></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-02-05-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-02-05-000Z" class="timestamp-link"><time datetime="2025-12-24T10:02:05.000Z" data-timestamp="2025-12-24T10:02:05.000Z">2025-12-24T10:02:05.000Z</time></a></div><div class="message-content">
<div class="tool-use bash-tool" data-tool-id="toolu_bash_004">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Run tests with verbose output</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">python -m pytest tests/ -v</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-02-10-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-02-10-000Z" class="timestamp-link"><time datetime="2025-12-24T10:02:10.000Z" data-timestamp="2025-12-24T10:02:10.000Z">2025-12-24T10:02:10.000Z</time></a></div><div class="message-content"><div class="tool-result tool-error"><div class="truncatable"><div class="truncatable-content"><pre>Exit code 1
===== FAILURES =====
test_subtract - AssertionError: expected 5 but got None</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-02-15-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-02-15-000Z" class="timestamp-link"><time datetime="2025-12-24T10:02:15.000Z" data-timestamp="2025-12-24T10:02:15.000Z">2025-12-24T10:02:15.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>There's a test failure. I need to check the test file and fix it.</p>
<p>Here's some <strong>markdown</strong> content with:
- A bullet list
- <code>inline code</code>
- A <a href="https://example.com">link</a></p>
<pre><code class="language-python">def example():
    return 42
</code></pre></div></div></div>
<div class="message user" id="msg-2025-12-24T10-03-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-03-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:00.000Z" data-timestamp="2025-12-24T10:03:00.000Z">2025-12-24T10:03:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>Fix the issue and commit</p></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-03-05-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-03-05-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:05.000Z" data-timestamp="2025-12-24T10:03:05.000Z">2025-12-24T10:03:05.000Z</time></a></div><div class="message-content"><div class="file-tool edit-tool" data-tool-id="toolu_edit_002">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">test_math.py</span> <span class="edit-replace-all">(replace all)</span></div>
<div class="file-tool-fullpath">/project/tests/test_math.py</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">assert subtract(10, 5) == None</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">assert subtract(10, 5) == 5</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-03-10-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-03-10-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:10.000Z" data-timestamp="2025-12-24T10:03:10.000Z">2025-12-24T10:03:10.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>File edited successfully</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-03-15-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-03-15-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:15.000Z" data-timestamp="2025-12-24T10:03:15.000Z">2025-12-24T10:03:15.000Z</time></a></div><div class="message-content">
<div class="tool-use bash-tool" data-tool-id="toolu_bash_005">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Commit the fix</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">git add . &amp;&amp; git commit -m &#39;Add subtract function and fix tests&#39;</pre></div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-03-20-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-03-20-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:20.000Z" data-timestamp="2025-12-24T10:03:20.000Z">2025-12-24T10:03:20.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><div class="commit-card"><a href="https://github.com/example/project/commit/def5678"><span class="commit-card-hash">def5678</span> Add subtract function and fix tests</a></div><pre>2 files changed, 10 insertions(+), 1 deletion(-)</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-03-25-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-03-25-000Z" class="timestamp-link"><time datetime="2025-12-24T10:03:25.000Z" data-timestamp="2025-12-24T10:03:25.000Z">2025-12-24T10:03:25.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>Done! The subtract function is now working and committed.</p></div></div></div><details class="continuation"><summary>Session continuation summary</summary>
<div class="message user" id="msg-2025-12-24T10-04-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-04-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:04:00.000Z" data-timestamp="2025-12-24T10:04:00.000Z">2025-12-24T10:04:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>This is a session continuation summary from a previous context. The user was working on a math utilities library.</p></div></div></div></details>
        

<div class="pagination">
<a href="index.html" class="index-link">Index</a>
<span class="disabled">&larr; Prev</span>
<span class="current">1</span>
<a href="page-002.html">2</a>
<a href="page-002.html">Next &rarr;</a>
</div>

    </div>
    <script>
document.querySelectorAll('time[data-timestamp]').forEach(function(el) {
    const timestamp = el.getAttribute('data-timestamp');
    const date = new Date(timestamp);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const timeStr = date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    if (isToday) { el.textContent = timeStr; }
    else { el.textContent = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' + timeStr; }
});
document.querySelectorAll('pre.json').forEach(function(el) {
    let text = el.textContent;
    text = text.replace(/"([^"]+)":/g, '<span style="color: #ce93d8">"$1"</span>:');
    text = text.replace(/: "([^"]*)"/g, ': <span style="color: #81d4fa">"$1"</span>');
    text = text.replace(/: (\d+)/g, ': <span style="color: #ffcc80">$1</span>');
    text = text.replace(/: (true|false|null)/g, ': <span style="color: #f48fb1">$1</span>');
    el.innerHTML = text;
});
document.querySelectorAll('.truncatable').forEach(function(wrapper) {
    const content = wrapper.querySelector('.truncatable-content');
    const btn = wrapper.querySelector('.expand-btn');
    if (content.scrollHeight > 250) {
        wrapper.classList.add('truncated');
        btn.addEventListener('click', function() {
            if (wrapper.classList.contains('truncated')) { wrapper.classList.remove('truncated'); wrapper.classList.add('expanded'); btn.textContent = 'Show less'; }
            else { wrapper.classList.remove('expanded'); wrapper.classList.add('truncated'); btn.textContent = 'Show more'; }
        });
    }
});
</script>
</body>
</html>
```

## File: `tests/__snapshots__/test_generate_html/TestGenerateHtml.test_generates_page_002_html.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Code transcript - page 2</title>
    <style>
:root { --bg-color: #f5f5f5; --card-bg: #ffffff; --user-bg: #e3f2fd; --user-border: #1976d2; --assistant-bg: #f5f5f5; --assistant-border: #9e9e9e; --thinking-bg: #fff8e1; --thinking-border: #ffc107; --thinking-text: #666; --tool-bg: #f3e5f5; --tool-border: #9c27b0; --tool-result-bg: #e8f5e9; --tool-error-bg: #ffebee; --text-color: #212121; --text-muted: #757575; --code-bg: #263238; --code-text: #aed581; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 16px; line-height: 1.6; }
.container { max-width: 800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin-bottom: 24px; padding-bottom: 8px; border-bottom: 2px solid var(--user-border); }
.header-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-bottom: 2px solid var(--user-border); padding-bottom: 8px; margin-bottom: 24px; }
.header-row h1 { border-bottom: none; padding-bottom: 0; margin-bottom: 0; flex: 1; min-width: 200px; }
.message { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.message.user { background: var(--user-bg); border-left: 4px solid var(--user-border); }
.message.assistant { background: var(--card-bg); border-left: 4px solid var(--assistant-border); }
.message.tool-reply { background: #fff8e1; border-left: 4px solid #ff9800; }
.tool-reply .role-label { color: #e65100; }
.tool-reply .tool-result { background: transparent; padding: 0; margin: 0; }
.tool-reply .tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.message-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.role-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.user .role-label { color: var(--user-border); }
time { color: var(--text-muted); font-size: 0.8rem; }
.timestamp-link { color: inherit; text-decoration: none; }
.timestamp-link:hover { text-decoration: underline; }
.message:target { animation: highlight 2s ease-out; }
@keyframes highlight { 0% { background-color: rgba(25, 118, 210, 0.2); } 100% { background-color: transparent; } }
.message-content { padding: 16px; }
.message-content p { margin: 0 0 12px 0; }
.message-content p:last-child { margin-bottom: 0; }
.thinking { background: var(--thinking-bg); border: 1px solid var(--thinking-border); border-radius: 8px; padding: 12px; margin: 12px 0; font-size: 0.9rem; color: var(--thinking-text); }
.thinking-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: #f57c00; margin-bottom: 8px; }
.thinking p { margin: 8px 0; }
.assistant-text { margin: 8px 0; }
.tool-use { background: var(--tool-bg); border: 1px solid var(--tool-border); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-header { font-weight: 600; color: var(--tool-border); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.tool-icon { font-size: 1.1rem; }
.tool-description { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 8px; font-style: italic; }
.tool-result { background: var(--tool-result-bg); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-result.tool-error { background: var(--tool-error-bg); }
.file-tool { border-radius: 8px; padding: 12px; margin: 12px 0; }
.write-tool { background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%); border: 1px solid #4caf50; }
.edit-tool { background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%); border: 1px solid #ff9800; }
.file-tool-header { font-weight: 600; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.write-header { color: #2e7d32; }
.edit-header { color: #e65100; }
.file-tool-icon { font-size: 1rem; }
.file-tool-path { font-family: monospace; background: rgba(0,0,0,0.08); padding: 2px 8px; border-radius: 4px; }
.file-tool-fullpath { font-family: monospace; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; word-break: break-all; }
.file-content { margin: 0; }
.edit-section { display: flex; margin: 4px 0; border-radius: 4px; overflow: hidden; }
.edit-label { padding: 8px 12px; font-weight: bold; font-family: monospace; display: flex; align-items: flex-start; }
.edit-old { background: #fce4ec; }
.edit-old .edit-label { color: #b71c1c; background: #f8bbd9; }
.edit-old .edit-content { color: #880e4f; }
.edit-new { background: #e8f5e9; }
.edit-new .edit-label { color: #1b5e20; background: #a5d6a7; }
.edit-new .edit-content { color: #1b5e20; }
.edit-content { margin: 0; flex: 1; background: transparent; font-size: 0.85rem; }
.edit-replace-all { font-size: 0.75rem; font-weight: normal; color: var(--text-muted); }
.write-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #e6f4ea); }
.edit-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff0e5); }
.todo-list { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); border: 1px solid #81c784; border-radius: 8px; padding: 12px; margin: 12px 0; }
.todo-header { font-weight: 600; color: #2e7d32; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.todo-items { list-style: none; margin: 0; padding: 0; }
.todo-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(0,0,0,0.06); font-size: 0.9rem; }
.todo-item:last-child { border-bottom: none; }
.todo-icon { flex-shrink: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 50%; }
.todo-completed .todo-icon { color: #2e7d32; background: rgba(46, 125, 50, 0.15); }
.todo-completed .todo-content { color: #558b2f; text-decoration: line-through; }
.todo-in-progress .todo-icon { color: #f57c00; background: rgba(245, 124, 0, 0.15); }
.todo-in-progress .todo-content { color: #e65100; font-weight: 500; }
.todo-pending .todo-icon { color: #757575; background: rgba(0,0,0,0.05); }
.todo-pending .todo-content { color: #616161; }
pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }
pre.json { color: #e0e0e0; }
code { background: rgba(0,0,0,0.08); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre code { background: none; padding: 0; }
.user-content { margin: 0; }
.truncatable { position: relative; }
.truncatable.truncated .truncatable-content { max-height: 200px; overflow: hidden; }
.truncatable.truncated::after { content: ''; position: absolute; bottom: 32px; left: 0; right: 0; height: 60px; background: linear-gradient(to bottom, transparent, var(--card-bg)); pointer-events: none; }
.message.user .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--user-bg)); }
.message.tool-reply .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.tool-use .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-bg)); }
.tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-result-bg)); }
.expand-btn { display: none; width: 100%; padding: 8px 16px; margin-top: 4px; background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; cursor: pointer; font-size: 0.85rem; color: var(--text-muted); }
.expand-btn:hover { background: rgba(0,0,0,0.1); }
.truncatable.truncated .expand-btn, .truncatable.expanded .expand-btn { display: block; }
.pagination { display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; }
.pagination a, .pagination span { padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; }
.pagination a { background: var(--card-bg); color: var(--user-border); border: 1px solid var(--user-border); }
.pagination a:hover { background: var(--user-bg); }
.pagination .current { background: var(--user-border); color: white; }
.pagination .disabled { color: var(--text-muted); border: 1px solid #ddd; }
.pagination .index-link { background: var(--user-border); color: white; }
details.continuation { margin-bottom: 16px; }
details.continuation summary { cursor: pointer; padding: 12px 16px; background: var(--user-bg); border-left: 4px solid var(--user-border); border-radius: 12px; font-weight: 500; color: var(--text-muted); }
details.continuation summary:hover { background: rgba(25, 118, 210, 0.15); }
details.continuation[open] summary { border-radius: 12px 12px 0 0; margin-bottom: 0; }
.index-item { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: var(--user-bg); border-left: 4px solid var(--user-border); }
.index-item a { display: block; text-decoration: none; color: inherit; }
.index-item a:hover { background: rgba(25, 118, 210, 0.1); }
.index-item-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.index-item-number { font-weight: 600; color: var(--user-border); }
.index-item-content { padding: 16px; }
.index-item-stats { padding: 8px 16px 12px 32px; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.06); }
.index-item-commit { margin-top: 6px; padding: 4px 8px; background: #fff3e0; border-radius: 4px; font-size: 0.85rem; color: #e65100; }
.index-item-commit code { background: rgba(0,0,0,0.08); padding: 1px 4px; border-radius: 3px; font-size: 0.8rem; margin-right: 6px; }
.commit-card { margin: 8px 0; padding: 10px 14px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 6px; }
.commit-card a { text-decoration: none; color: #5d4037; display: block; }
.commit-card a:hover { color: #e65100; }
.commit-card-hash { font-family: monospace; color: #e65100; font-weight: 600; margin-right: 8px; }
.index-commit { margin-bottom: 12px; padding: 10px 16px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.index-commit a { display: block; text-decoration: none; color: inherit; }
.index-commit a:hover { background: rgba(255, 152, 0, 0.1); margin: -10px -16px; padding: 10px 16px; border-radius: 8px; }
.index-commit-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; margin-bottom: 4px; }
.index-commit-hash { font-family: monospace; color: #e65100; font-weight: 600; }
.index-commit-msg { color: #5d4037; }
.index-item-long-text { margin-top: 8px; padding: 12px; background: var(--card-bg); border-radius: 8px; border-left: 3px solid var(--assistant-border); }
.index-item-long-text .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--card-bg)); }
.index-item-long-text-content { color: var(--text-color); }
#search-box { display: none; align-items: center; gap: 8px; }
#search-box input { padding: 6px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; width: 180px; }
#search-box button, #modal-search-btn, #modal-close-btn { background: var(--user-border); color: white; border: none; border-radius: 6px; padding: 6px 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#search-box button:hover, #modal-search-btn:hover { background: #1565c0; }
#modal-close-btn { background: var(--text-muted); margin-left: 8px; }
#modal-close-btn:hover { background: #616161; }
#search-modal[open] { border: none; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.2); padding: 0; width: 90vw; max-width: 900px; height: 80vh; max-height: 80vh; display: flex; flex-direction: column; }
#search-modal::backdrop { background: rgba(0,0,0,0.5); }
.search-modal-header { display: flex; align-items: center; gap: 8px; padding: 16px; border-bottom: 1px solid var(--assistant-border); background: var(--bg-color); border-radius: 12px 12px 0 0; }
.search-modal-header input { flex: 1; padding: 8px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; }
#search-status { padding: 8px 16px; font-size: 0.85rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
#search-results { flex: 1; overflow-y: auto; padding: 16px; }
.search-result { margin-bottom: 16px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.search-result a { display: block; text-decoration: none; color: inherit; }
.search-result a:hover { background: rgba(25, 118, 210, 0.05); }
.search-result-page { padding: 6px 12px; background: rgba(0,0,0,0.03); font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
.search-result-content { padding: 12px; }
.search-result mark { background: #fff59d; padding: 1px 2px; border-radius: 2px; }
@media (max-width: 600px) { body { padding: 8px; } .message, .index-item { border-radius: 8px; } .message-content, .index-item-content { padding: 12px; } pre { font-size: 0.8rem; padding: 8px; } #search-box input { width: 120px; } #search-modal[open] { width: 95vw; height: 90vh; } }
</style>
</head>
<body>
    <div class="container">
        <h1><a href="index.html" style="color: inherit; text-decoration: none;">Claude Code transcript</a> - page 2/2</h1>
        

<div class="pagination">
<a href="index.html" class="index-link">Index</a>
<a href="page-001.html">&larr; Prev</a>
<a href="page-001.html">1</a>
<span class="current">2</span>
<span class="disabled">Next &rarr;</span>
</div>

        
<div class="message user" id="msg-2025-12-24T10-05-00-000Z"><div class="message-header"><span class="role-label">User</span><a href="#msg-2025-12-24T10-05-00-000Z" class="timestamp-link"><time datetime="2025-12-24T10:05:00.000Z" data-timestamp="2025-12-24T10:05:00.000Z">2025-12-24T10:05:00.000Z</time></a></div><div class="message-content">
<div class="user-content"><p>Add a multiply function too</p></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-05-05-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-05-05-000Z" class="timestamp-link"><time datetime="2025-12-24T10:05:05.000Z" data-timestamp="2025-12-24T10:05:05.000Z">2025-12-24T10:05:05.000Z</time></a></div><div class="message-content"><div class="file-tool edit-tool" data-tool-id="toolu_edit_003">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">math_utils.py</span></div>
<div class="file-tool-fullpath">/project/math_utils.py</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">    return a - b
</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">    return a - b


def multiply(a: int, b: int) -&gt; int:
    &#34;&#34;&#34;Multiply two numbers.&#34;&#34;&#34;
    return a * b
</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div></div></div>
<div class="message tool-reply" id="msg-2025-12-24T10-05-10-000Z"><div class="message-header"><span class="role-label">Tool reply</span><a href="#msg-2025-12-24T10-05-10-000Z" class="timestamp-link"><time datetime="2025-12-24T10:05:10.000Z" data-timestamp="2025-12-24T10:05:10.000Z">2025-12-24T10:05:10.000Z</time></a></div><div class="message-content"><div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>File edited successfully</pre></div><button class="expand-btn">Show more</button></div></div></div></div>
<div class="message assistant" id="msg-2025-12-24T10-05-15-000Z"><div class="message-header"><span class="role-label">Assistant</span><a href="#msg-2025-12-24T10-05-15-000Z" class="timestamp-link"><time datetime="2025-12-24T10:05:15.000Z" data-timestamp="2025-12-24T10:05:15.000Z">2025-12-24T10:05:15.000Z</time></a></div><div class="message-content">
<div class="assistant-text"><p>Added multiply function!</p></div></div></div>
        

<div class="pagination">
<a href="index.html" class="index-link">Index</a>
<a href="page-001.html">&larr; Prev</a>
<a href="page-001.html">1</a>
<span class="current">2</span>
<span class="disabled">Next &rarr;</span>
</div>

    </div>
    <script>
document.querySelectorAll('time[data-timestamp]').forEach(function(el) {
    const timestamp = el.getAttribute('data-timestamp');
    const date = new Date(timestamp);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const timeStr = date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    if (isToday) { el.textContent = timeStr; }
    else { el.textContent = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' + timeStr; }
});
document.querySelectorAll('pre.json').forEach(function(el) {
    let text = el.textContent;
    text = text.replace(/"([^"]+)":/g, '<span style="color: #ce93d8">"$1"</span>:');
    text = text.replace(/: "([^"]*)"/g, ': <span style="color: #81d4fa">"$1"</span>');
    text = text.replace(/: (\d+)/g, ': <span style="color: #ffcc80">$1</span>');
    text = text.replace(/: (true|false|null)/g, ': <span style="color: #f48fb1">$1</span>');
    el.innerHTML = text;
});
document.querySelectorAll('.truncatable').forEach(function(wrapper) {
    const content = wrapper.querySelector('.truncatable-content');
    const btn = wrapper.querySelector('.expand-btn');
    if (content.scrollHeight > 250) {
        wrapper.classList.add('truncated');
        btn.addEventListener('click', function() {
            if (wrapper.classList.contains('truncated')) { wrapper.classList.remove('truncated'); wrapper.classList.add('expanded'); btn.textContent = 'Show less'; }
            else { wrapper.classList.remove('expanded'); wrapper.classList.add('truncated'); btn.textContent = 'Show more'; }
        });
    }
});
</script>
</body>
</html>
```

## File: `tests/__snapshots__/test_generate_html/TestParseSessionFile.test_jsonl_generates_html.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Code transcript - Index</title>
    <style>
:root { --bg-color: #f5f5f5; --card-bg: #ffffff; --user-bg: #e3f2fd; --user-border: #1976d2; --assistant-bg: #f5f5f5; --assistant-border: #9e9e9e; --thinking-bg: #fff8e1; --thinking-border: #ffc107; --thinking-text: #666; --tool-bg: #f3e5f5; --tool-border: #9c27b0; --tool-result-bg: #e8f5e9; --tool-error-bg: #ffebee; --text-color: #212121; --text-muted: #757575; --code-bg: #263238; --code-text: #aed581; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 16px; line-height: 1.6; }
.container { max-width: 800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin-bottom: 24px; padding-bottom: 8px; border-bottom: 2px solid var(--user-border); }
.header-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-bottom: 2px solid var(--user-border); padding-bottom: 8px; margin-bottom: 24px; }
.header-row h1 { border-bottom: none; padding-bottom: 0; margin-bottom: 0; flex: 1; min-width: 200px; }
.message { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.message.user { background: var(--user-bg); border-left: 4px solid var(--user-border); }
.message.assistant { background: var(--card-bg); border-left: 4px solid var(--assistant-border); }
.message.tool-reply { background: #fff8e1; border-left: 4px solid #ff9800; }
.tool-reply .role-label { color: #e65100; }
.tool-reply .tool-result { background: transparent; padding: 0; margin: 0; }
.tool-reply .tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.message-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.role-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.user .role-label { color: var(--user-border); }
time { color: var(--text-muted); font-size: 0.8rem; }
.timestamp-link { color: inherit; text-decoration: none; }
.timestamp-link:hover { text-decoration: underline; }
.message:target { animation: highlight 2s ease-out; }
@keyframes highlight { 0% { background-color: rgba(25, 118, 210, 0.2); } 100% { background-color: transparent; } }
.message-content { padding: 16px; }
.message-content p { margin: 0 0 12px 0; }
.message-content p:last-child { margin-bottom: 0; }
.thinking { background: var(--thinking-bg); border: 1px solid var(--thinking-border); border-radius: 8px; padding: 12px; margin: 12px 0; font-size: 0.9rem; color: var(--thinking-text); }
.thinking-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: #f57c00; margin-bottom: 8px; }
.thinking p { margin: 8px 0; }
.assistant-text { margin: 8px 0; }
.tool-use { background: var(--tool-bg); border: 1px solid var(--tool-border); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-header { font-weight: 600; color: var(--tool-border); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.tool-icon { font-size: 1.1rem; }
.tool-description { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 8px; font-style: italic; }
.tool-result { background: var(--tool-result-bg); border-radius: 8px; padding: 12px; margin: 12px 0; }
.tool-result.tool-error { background: var(--tool-error-bg); }
.file-tool { border-radius: 8px; padding: 12px; margin: 12px 0; }
.write-tool { background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%); border: 1px solid #4caf50; }
.edit-tool { background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%); border: 1px solid #ff9800; }
.file-tool-header { font-weight: 600; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.write-header { color: #2e7d32; }
.edit-header { color: #e65100; }
.file-tool-icon { font-size: 1rem; }
.file-tool-path { font-family: monospace; background: rgba(0,0,0,0.08); padding: 2px 8px; border-radius: 4px; }
.file-tool-fullpath { font-family: monospace; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; word-break: break-all; }
.file-content { margin: 0; }
.edit-section { display: flex; margin: 4px 0; border-radius: 4px; overflow: hidden; }
.edit-label { padding: 8px 12px; font-weight: bold; font-family: monospace; display: flex; align-items: flex-start; }
.edit-old { background: #fce4ec; }
.edit-old .edit-label { color: #b71c1c; background: #f8bbd9; }
.edit-old .edit-content { color: #880e4f; }
.edit-new { background: #e8f5e9; }
.edit-new .edit-label { color: #1b5e20; background: #a5d6a7; }
.edit-new .edit-content { color: #1b5e20; }
.edit-content { margin: 0; flex: 1; background: transparent; font-size: 0.85rem; }
.edit-replace-all { font-size: 0.75rem; font-weight: normal; color: var(--text-muted); }
.write-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #e6f4ea); }
.edit-tool .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff0e5); }
.todo-list { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); border: 1px solid #81c784; border-radius: 8px; padding: 12px; margin: 12px 0; }
.todo-header { font-weight: 600; color: #2e7d32; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.todo-items { list-style: none; margin: 0; padding: 0; }
.todo-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(0,0,0,0.06); font-size: 0.9rem; }
.todo-item:last-child { border-bottom: none; }
.todo-icon { flex-shrink: 0; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 50%; }
.todo-completed .todo-icon { color: #2e7d32; background: rgba(46, 125, 50, 0.15); }
.todo-completed .todo-content { color: #558b2f; text-decoration: line-through; }
.todo-in-progress .todo-icon { color: #f57c00; background: rgba(245, 124, 0, 0.15); }
.todo-in-progress .todo-content { color: #e65100; font-weight: 500; }
.todo-pending .todo-icon { color: #757575; background: rgba(0,0,0,0.05); }
.todo-pending .todo-content { color: #616161; }
pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }
pre.json { color: #e0e0e0; }
code { background: rgba(0,0,0,0.08); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre code { background: none; padding: 0; }
.user-content { margin: 0; }
.truncatable { position: relative; }
.truncatable.truncated .truncatable-content { max-height: 200px; overflow: hidden; }
.truncatable.truncated::after { content: ''; position: absolute; bottom: 32px; left: 0; right: 0; height: 60px; background: linear-gradient(to bottom, transparent, var(--card-bg)); pointer-events: none; }
.message.user .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--user-bg)); }
.message.tool-reply .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, #fff8e1); }
.tool-use .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-bg)); }
.tool-result .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--tool-result-bg)); }
.expand-btn { display: none; width: 100%; padding: 8px 16px; margin-top: 4px; background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; cursor: pointer; font-size: 0.85rem; color: var(--text-muted); }
.expand-btn:hover { background: rgba(0,0,0,0.1); }
.truncatable.truncated .expand-btn, .truncatable.expanded .expand-btn { display: block; }
.pagination { display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; }
.pagination a, .pagination span { padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; }
.pagination a { background: var(--card-bg); color: var(--user-border); border: 1px solid var(--user-border); }
.pagination a:hover { background: var(--user-bg); }
.pagination .current { background: var(--user-border); color: white; }
.pagination .disabled { color: var(--text-muted); border: 1px solid #ddd; }
.pagination .index-link { background: var(--user-border); color: white; }
details.continuation { margin-bottom: 16px; }
details.continuation summary { cursor: pointer; padding: 12px 16px; background: var(--user-bg); border-left: 4px solid var(--user-border); border-radius: 12px; font-weight: 500; color: var(--text-muted); }
details.continuation summary:hover { background: rgba(25, 118, 210, 0.15); }
details.continuation[open] summary { border-radius: 12px 12px 0 0; margin-bottom: 0; }
.index-item { margin-bottom: 16px; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: var(--user-bg); border-left: 4px solid var(--user-border); }
.index-item a { display: block; text-decoration: none; color: inherit; }
.index-item a:hover { background: rgba(25, 118, 210, 0.1); }
.index-item-header { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; background: rgba(0,0,0,0.03); font-size: 0.85rem; }
.index-item-number { font-weight: 600; color: var(--user-border); }
.index-item-content { padding: 16px; }
.index-item-stats { padding: 8px 16px 12px 32px; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.06); }
.index-item-commit { margin-top: 6px; padding: 4px 8px; background: #fff3e0; border-radius: 4px; font-size: 0.85rem; color: #e65100; }
.index-item-commit code { background: rgba(0,0,0,0.08); padding: 1px 4px; border-radius: 3px; font-size: 0.8rem; margin-right: 6px; }
.commit-card { margin: 8px 0; padding: 10px 14px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 6px; }
.commit-card a { text-decoration: none; color: #5d4037; display: block; }
.commit-card a:hover { color: #e65100; }
.commit-card-hash { font-family: monospace; color: #e65100; font-weight: 600; margin-right: 8px; }
.index-commit { margin-bottom: 12px; padding: 10px 16px; background: #fff3e0; border-left: 4px solid #ff9800; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.index-commit a { display: block; text-decoration: none; color: inherit; }
.index-commit a:hover { background: rgba(255, 152, 0, 0.1); margin: -10px -16px; padding: 10px 16px; border-radius: 8px; }
.index-commit-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; margin-bottom: 4px; }
.index-commit-hash { font-family: monospace; color: #e65100; font-weight: 600; }
.index-commit-msg { color: #5d4037; }
.index-item-long-text { margin-top: 8px; padding: 12px; background: var(--card-bg); border-radius: 8px; border-left: 3px solid var(--assistant-border); }
.index-item-long-text .truncatable.truncated::after { background: linear-gradient(to bottom, transparent, var(--card-bg)); }
.index-item-long-text-content { color: var(--text-color); }
#search-box { display: none; align-items: center; gap: 8px; }
#search-box input { padding: 6px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; width: 180px; }
#search-box button, #modal-search-btn, #modal-close-btn { background: var(--user-border); color: white; border: none; border-radius: 6px; padding: 6px 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#search-box button:hover, #modal-search-btn:hover { background: #1565c0; }
#modal-close-btn { background: var(--text-muted); margin-left: 8px; }
#modal-close-btn:hover { background: #616161; }
#search-modal[open] { border: none; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.2); padding: 0; width: 90vw; max-width: 900px; height: 80vh; max-height: 80vh; display: flex; flex-direction: column; }
#search-modal::backdrop { background: rgba(0,0,0,0.5); }
.search-modal-header { display: flex; align-items: center; gap: 8px; padding: 16px; border-bottom: 1px solid var(--assistant-border); background: var(--bg-color); border-radius: 12px 12px 0 0; }
.search-modal-header input { flex: 1; padding: 8px 12px; border: 1px solid var(--assistant-border); border-radius: 6px; font-size: 16px; }
#search-status { padding: 8px 16px; font-size: 0.85rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
#search-results { flex: 1; overflow-y: auto; padding: 16px; }
.search-result { margin-bottom: 16px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.search-result a { display: block; text-decoration: none; color: inherit; }
.search-result a:hover { background: rgba(25, 118, 210, 0.05); }
.search-result-page { padding: 6px 12px; background: rgba(0,0,0,0.03); font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid rgba(0,0,0,0.06); }
.search-result-content { padding: 12px; }
.search-result mark { background: #fff59d; padding: 1px 2px; border-radius: 2px; }
@media (max-width: 600px) { body { padding: 8px; } .message, .index-item { border-radius: 8px; } .message-content, .index-item-content { padding: 12px; } pre { font-size: 0.8rem; padding: 8px; } #search-box input { width: 120px; } #search-modal[open] { width: 95vw; height: 90vh; } }
</style>
</head>
<body>
    <div class="container">
        <div class="header-row">
            <h1>Claude Code transcript</h1>
            <div id="search-box">
                <input type="text" id="search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
            </div>
        </div>
        

<div class="pagination">
<span class="current">Index</span>
<span class="disabled">&larr; Prev</span>
<a href="page-001.html">1</a>
<a href="page-001.html">Next &rarr;</a>
</div>

        <p style="color: var(--text-muted); margin-bottom: 24px;">2 prompts · 7 messages · 2 tool calls · 1 commits · 1 pages</p>
        
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-00-00-000Z"><div class="index-item-header"><span class="index-item-number">#1</span><time datetime="2025-12-24T10:00:00.000Z" data-timestamp="2025-12-24T10:00:00.000Z">2025-12-24T10:00:00.000Z</time></div><div class="index-item-content"><p>Create a hello world function</p></div></a><div class="index-item-stats"><span>1 write · 1 bash</span>
</div></div><div class="index-commit"><div class="index-commit-header"><span class="index-commit-hash">abc1234</span><time datetime="2025-12-24T10:00:20.000Z" data-timestamp="2025-12-24T10:00:20.000Z">2025-12-24T10:00:20.000Z</time></div><div class="index-commit-msg">Add hello function</div></div>
<div class="index-item"><a href="page-001.html#msg-2025-12-24T10-01-00-000Z"><div class="index-item-header"><span class="index-item-number">#2</span><time datetime="2025-12-24T10:01:00.000Z" data-timestamp="2025-12-24T10:01:00.000Z">2025-12-24T10:01:00.000Z</time></div><div class="index-item-content"><p>Now add a goodbye function</p></div></a></div>
        

<div class="pagination">
<span class="current">Index</span>
<span class="disabled">&larr; Prev</span>
<a href="page-001.html">1</a>
<a href="page-001.html">Next &rarr;</a>
</div>


        <dialog id="search-modal">
            <div class="search-modal-header">
                <input type="text" id="modal-search-input" placeholder="Search..." aria-label="Search transcripts">
                <button id="modal-search-btn" type="button" aria-label="Search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
                </button>
                <button id="modal-close-btn" type="button" aria-label="Close">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg>
                </button>
            </div>
            <div id="search-status"></div>
            <div id="search-results"></div>
        </dialog>
        <script>
(function() {
    var totalPages = 1;
    var searchBox = document.getElementById('search-box');
    var searchInput = document.getElementById('search-input');
    var searchBtn = document.getElementById('search-btn');
    var modal = document.getElementById('search-modal');
    var modalInput = document.getElementById('modal-search-input');
    var modalSearchBtn = document.getElementById('modal-search-btn');
    var modalCloseBtn = document.getElementById('modal-close-btn');
    var searchStatus = document.getElementById('search-status');
    var searchResults = document.getElementById('search-results');

    if (!searchBox || !modal) return;

    // Hide search on file:// protocol (doesn't work due to CORS restrictions)
    if (window.location.protocol === 'file:') return;

    // Show search box (progressive enhancement)
    searchBox.style.display = 'flex';

    // Gist preview support - detect if we're on gisthost.github.io or gistpreview.github.io
    var hostname = window.location.hostname;
    var isGistPreview = hostname === 'gisthost.github.io' || hostname === 'gistpreview.github.io';
    var gistId = null;
    var gistOwner = null;
    var gistInfoLoaded = false;

    if (isGistPreview) {
        // Extract gist ID from URL query string like ?78a436a8a9e7a2e603738b8193b95410/index.html
        var queryMatch = window.location.search.match(/^\?([a-f0-9]+)/i);
        if (queryMatch) {
            gistId = queryMatch[1];
        }
    }

    async function loadGistInfo() {
        if (!isGistPreview || !gistId || gistInfoLoaded) return;
        try {
            var response = await fetch('https://api.github.com/gists/' + gistId);
            if (response.ok) {
                var info = await response.json();
                gistOwner = info.owner.login;
                gistInfoLoaded = true;
            }
        } catch (e) {
            console.error('Failed to load gist info:', e);
        }
    }

    function getPageFetchUrl(pageFile) {
        if (isGistPreview && gistOwner && gistId) {
            // Use raw gist URL for fetching content
            return 'https://gist.githubusercontent.com/' + gistOwner + '/' + gistId + '/raw/' + pageFile;
        }
        return pageFile;
    }

    function getPageLinkUrl(pageFile) {
        if (isGistPreview && gistId) {
            // Use gistpreview URL format for navigation links
            return '?' + gistId + '/' + pageFile;
        }
        return pageFile;
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function openModal(query) {
        modalInput.value = query || '';
        searchResults.innerHTML = '';
        searchStatus.textContent = '';
        modal.showModal();
        modalInput.focus();
        if (query) {
            performSearch(query);
        }
    }

    function closeModal() {
        modal.close();
        // Update URL to remove search fragment, preserving path and query string
        if (window.location.hash.startsWith('#search=')) {
            history.replaceState(null, '', window.location.pathname + window.location.search);
        }
    }

    function updateUrlHash(query) {
        if (query) {
            // Preserve path and query string when adding hash
            history.replaceState(null, '', window.location.pathname + window.location.search + '#search=' + encodeURIComponent(query));
        }
    }

    function highlightTextNodes(element, searchTerm) {
        var walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
        var nodesToReplace = [];

        while (walker.nextNode()) {
            var node = walker.currentNode;
            if (node.nodeValue.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) {
                nodesToReplace.push(node);
            }
        }

        nodesToReplace.forEach(function(node) {
            var text = node.nodeValue;
            var regex = new RegExp('(' + escapeRegex(searchTerm) + ')', 'gi');
            var parts = text.split(regex);
            if (parts.length > 1) {
                var span = document.createElement('span');
                parts.forEach(function(part) {
                    if (part.toLowerCase() === searchTerm.toLowerCase()) {
                        var mark = document.createElement('mark');
                        mark.textContent = part;
                        span.appendChild(mark);
                    } else {
                        span.appendChild(document.createTextNode(part));
                    }
                });
                node.parentNode.replaceChild(span, node);
            }
        });
    }

    function fixInternalLinks(element, pageFile) {
        // Update all internal anchor links to include the page file
        var links = element.querySelectorAll('a[href^="#"]');
        links.forEach(function(link) {
            var href = link.getAttribute('href');
            link.setAttribute('href', pageFile + href);
        });
    }

    function processPage(pageFile, html, query) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var resultsFromPage = 0;

        // Find all message blocks
        var messages = doc.querySelectorAll('.message');
        messages.forEach(function(msg) {
            var text = msg.textContent || '';
            if (text.toLowerCase().indexOf(query.toLowerCase()) !== -1) {
                resultsFromPage++;

                // Get the message ID for linking
                var msgId = msg.id || '';
                var pageLinkUrl = getPageLinkUrl(pageFile);
                var link = pageLinkUrl + (msgId ? '#' + msgId : '');

                // Clone the message HTML and highlight matches
                var clone = msg.cloneNode(true);
                // Fix internal links to include the page file
                fixInternalLinks(clone, pageLinkUrl);
                highlightTextNodes(clone, query);

                var resultDiv = document.createElement('div');
                resultDiv.className = 'search-result';
                resultDiv.innerHTML = '<a href="' + link + '">' +
                    '<div class="search-result-page">' + escapeHtml(pageFile) + '</div>' +
                    '<div class="search-result-content">' + clone.innerHTML + '</div>' +
                    '</a>';
                searchResults.appendChild(resultDiv);
            }
        });

        return resultsFromPage;
    }

    async function performSearch(query) {
        if (!query.trim()) {
            searchStatus.textContent = 'Enter a search term';
            return;
        }

        updateUrlHash(query);
        searchResults.innerHTML = '';
        searchStatus.textContent = 'Searching...';

        // Load gist info if on gistpreview (needed for constructing URLs)
        if (isGistPreview && !gistInfoLoaded) {
            searchStatus.textContent = 'Loading gist info...';
            await loadGistInfo();
            if (!gistOwner) {
                searchStatus.textContent = 'Failed to load gist info. Search unavailable.';
                return;
            }
        }

        var resultsFound = 0;
        var pagesSearched = 0;

        // Build list of pages to fetch
        var pagesToFetch = [];
        for (var i = 1; i <= totalPages; i++) {
            pagesToFetch.push('page-' + String(i).padStart(3, '0') + '.html');
        }

        searchStatus.textContent = 'Searching...';

        // Process pages in batches of 3, but show results immediately as each completes
        var batchSize = 3;
        for (var i = 0; i < pagesToFetch.length; i += batchSize) {
            var batch = pagesToFetch.slice(i, i + batchSize);

            // Create promises that process results immediately when each fetch completes
            var promises = batch.map(function(pageFile) {
                return fetch(getPageFetchUrl(pageFile))
                    .then(function(response) {
                        if (!response.ok) throw new Error('Failed to fetch');
                        return response.text();
                    })
                    .then(function(html) {
                        // Process and display results immediately
                        var count = processPage(pageFile, html, query);
                        resultsFound += count;
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    })
                    .catch(function() {
                        pagesSearched++;
                        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + pagesSearched + '/' + totalPages + ' pages...';
                    });
            });

            // Wait for this batch to complete before starting the next
            await Promise.all(promises);
        }

        searchStatus.textContent = 'Found ' + resultsFound + ' result(s) in ' + totalPages + ' pages';
    }

    // Event listeners
    searchBtn.addEventListener('click', function() {
        openModal(searchInput.value);
    });

    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            openModal(searchInput.value);
        }
    });

    modalSearchBtn.addEventListener('click', function() {
        performSearch(modalInput.value);
    });

    modalInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            performSearch(modalInput.value);
        }
    });

    modalCloseBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Check for #search= in URL on page load
    if (window.location.hash.startsWith('#search=')) {
        var query = decodeURIComponent(window.location.hash.substring(8));
        if (query) {
            searchInput.value = query;
            openModal(query);
        }
    }
})();
        </script>
    </div>
    <script>
document.querySelectorAll('time[data-timestamp]').forEach(function(el) {
    const timestamp = el.getAttribute('data-timestamp');
    const date = new Date(timestamp);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const timeStr = date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    if (isToday) { el.textContent = timeStr; }
    else { el.textContent = date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' + timeStr; }
});
document.querySelectorAll('pre.json').forEach(function(el) {
    let text = el.textContent;
    text = text.replace(/"([^"]+)":/g, '<span style="color: #ce93d8">"$1"</span>:');
    text = text.replace(/: "([^"]*)"/g, ': <span style="color: #81d4fa">"$1"</span>');
    text = text.replace(/: (\d+)/g, ': <span style="color: #ffcc80">$1</span>');
    text = text.replace(/: (true|false|null)/g, ': <span style="color: #f48fb1">$1</span>');
    el.innerHTML = text;
});
document.querySelectorAll('.truncatable').forEach(function(wrapper) {
    const content = wrapper.querySelector('.truncatable-content');
    const btn = wrapper.querySelector('.expand-btn');
    if (content.scrollHeight > 250) {
        wrapper.classList.add('truncated');
        btn.addEventListener('click', function() {
            if (wrapper.classList.contains('truncated')) { wrapper.classList.remove('truncated'); wrapper.classList.add('expanded'); btn.textContent = 'Show less'; }
            else { wrapper.classList.remove('expanded'); wrapper.classList.add('truncated'); btn.textContent = 'Show more'; }
        });
    }
});
</script>
</body>
</html>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_image_block.html`
```html

<div class="image-block"><img src="data:image/gif;base64,R0lGODlhyADIAIAAAAAAAAAAACwAAAAAyADIAAAIAgQBADs=" style="max-width: 100%"></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_text_block.html`
```html

<div class="assistant-text"><p>Here is my response with <strong>markdown</strong>.</p></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_thinking_block.html`
```html

<div class="thinking"><div class="thinking-label">Thinking</div><p>Let me think about this...</p>
<ol>
<li>First consideration</li>
<li>Second point</li>
</ol></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_tool_result_block.html`
```html
<div class="tool-result"><div class="truncatable"><div class="truncatable-content"><pre>Command completed successfully
Output line 1
Output line 2</pre></div><button class="expand-btn">Show more</button></div></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_tool_result_error.html`
```html
<div class="tool-result tool-error"><div class="truncatable"><div class="truncatable-content"><pre>Error: file not found
Traceback follows...</pre></div><button class="expand-btn">Show more</button></div></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_tool_result_with_commit.html`
```html
<div class="tool-result"><div class="truncatable"><div class="truncatable-content"><div class="commit-card"><a href="https://github.com/example/repo/commit/abc1234"><span class="commit-card-hash">abc1234</span> Add new feature</a></div><pre>2 files changed, 10 insertions(+)</pre></div><button class="expand-btn">Show more</button></div></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderContentBlock.test_tool_result_with_image.html`
```html
<div class="tool-result"><pre>Successfully captured screenshot (807x782, jpeg) - ID: ss_123</pre><pre>

Tab Context:
- Executed on tabId: 12345</pre>
<div class="image-block"><img src="data:image/gif;base64,R0lGODlhyADIAIAAAAAAAAAAACwAAAAAyADIAAAIAgQBADs=" style="max-width: 100%"></div></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_format_json.html`
```html
<pre class="json">{
  &quot;key&quot;: &quot;value&quot;,
  &quot;number&quot;: 42,
  &quot;nested&quot;: {
    &quot;a&quot;: 1
  }
}</pre>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_bash_tool.html`
```html

<div class="tool-use bash-tool" data-tool-id="tool-123">
<div class="tool-header"><span class="tool-icon">$</span> Bash</div>
<div class="tool-description">Run tests with verbose output</div><div class="truncatable"><div class="truncatable-content"><pre class="bash-command">pytest tests/ -v</pre></div><button class="expand-btn">Show more</button></div>
</div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_edit_tool.html`
```html
<div class="file-tool edit-tool" data-tool-id="tool-123">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">file.py</span></div>
<div class="file-tool-fullpath">/project/file.py</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">old code here</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">new code here</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_edit_tool_replace_all.html`
```html
<div class="file-tool edit-tool" data-tool-id="tool-123">
<div class="file-tool-header edit-header"><span class="file-tool-icon">✏️</span> Edit <span class="file-tool-path">file.py</span> <span class="edit-replace-all">(replace all)</span></div>
<div class="file-tool-fullpath">/project/file.py</div>
<div class="truncatable"><div class="truncatable-content">
<div class="edit-section edit-old"><div class="edit-label">−</div><pre class="edit-content">old</pre></div>
<div class="edit-section edit-new"><div class="edit-label">+</div><pre class="edit-content">new</pre></div>
</div><button class="expand-btn">Show more</button></div>
</div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_markdown_text.html`
```html
<p><strong>bold</strong> and <code>code</code></p>
<ul>
<li>item 1</li>
<li>item 2</li>
</ul>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_todo_write.html`
```html

<div class="todo-list" data-tool-id="tool-123"><div class="todo-header"><span class="todo-header-icon">☰</span> Task List</div><ul class="todo-items"><li class="todo-item todo-completed"><span class="todo-icon">✓</span><span class="todo-content">First task</span></li><li class="todo-item todo-in-progress"><span class="todo-icon">→</span><span class="todo-content">Second task</span></li><li class="todo-item todo-pending"><span class="todo-icon">○</span><span class="todo-content">Third task</span></li></ul></div>
```

## File: `tests/__snapshots__/test_generate_html/TestRenderFunctions.test_render_write_tool.html`
```html
<div class="file-tool write-tool" data-tool-id="tool-123">
<div class="file-tool-header write-header"><span class="file-tool-icon">📝</span> Write <span class="file-tool-path">main.py</span></div>
<div class="file-tool-fullpath">/project/src/main.py</div>
<div class="truncatable"><div class="truncatable-content"><pre class="file-content">def hello():
    print(&#39;hello world&#39;)
</pre></div><button class="expand-btn">Show more</button></div>
</div>
```

