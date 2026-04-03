---
id: simonw-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.786082
---

# KNOWLEDGE EXTRACT: simonw
> **Extracted on:** 2026-03-30 17:53:21
> **Source:** simonw

---

## File: `claude-code-transcripts.md`
```markdown
# 📦 simonw/claude-code-transcripts [🔖 PENDING/APPROVE]
🔗 https://github.com/simonw/claude-code-transcripts


## Meta
- **Stars:** ⭐ 1213 | **Forks:** 🍴 139
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Tools for publishing transcripts for Claude Code sessions

## README (trích đầu)
```
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

Local Claude Code sessions are stored a
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `llm.md`
```markdown
# 📦 simonw/llm [🔖 PENDING/APPROVE]
🔗 https://github.com/simonw/llm
🌐 https://llm.datasette.io

## Meta
- **Stars:** ⭐ 11442 | **Forks:** 🍴 779
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Access large language models from the command-line

## README (trích đầu)
```
<!-- [[[cog
# README.md is generated from docs/index.md using sphinx_markdown_builder
import tempfile
import subprocess
from pathlib import Path

readme_markdown = ''

with tempfile.TemporaryDirectory() as tmpdir:
    tmp_path = Path(tmpdir)
    # Run: sphinx-build -M markdown ./docs ./tmpdir
    subprocess.run([
        "sphinx-build",
        "-M", "markdown",
        "./docs",
        str(tmp_path)
    ], check=True)
    index_file = tmp_path / "markdown" / "index.md"
    readme_markdown = index_file.read_text(encoding="utf-8")

cog.out(readme_markdown)
]]] -->
# LLM

[![GitHub repo](https://img.shields.io/badge/github-repo-green)](https://github.com/simonw/llm)
[![PyPI](https://img.shields.io/pypi/v/llm.svg)](https://pypi.org/project/llm/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm?include_prereleases&label=changelog)](https://llm.datasette.io/en/stable/changelog.html)
[![Tests](https://github.com/simonw/llm/workflows/Test/badge.svg)](https://github.com/simonw/llm/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/823971286308356157?label=discord)](https://datasette.io/discord-llm)
[![Homebrew](https://img.shields.io/homebrew/installs/dy/llm?color=yellow&label=homebrew&logo=homebrew)](https://formulae.brew.sh/formula/llm)

A CLI tool and Python library for interacting with **OpenAI**, **Anthropic’s Claude**, **Google’s Gemini**, **Meta’s Llama** and dozens of other Large Language Models, both via remote APIs and with models that can be installed and run on your own machine.

Watch **[Language models on the command-line](https://www.youtube.com/watch?v=QUXQNi6jQ30)** on YouTube for a demo or [read the accompanying detailed notes](https://simonwillison.net/2024/Jun/17/cli-language-models/).

With LLM you can:

- [Run prompts from the command-line](https://llm.datasette.io/en/stable/usage.html#usage-executing-prompts)
- [Store prompts and responses in SQLite](https://llm.datasette.io/en/stable/logging.html#logging)
- [Generate and store embeddings](https://llm.datasette.io/en/stable/embeddings/index.html#embeddings)
- [Extract structured content from text and images](https://llm.datasette.io/en/stable/schemas.html#schemas)
- [Grant models the ability to execute tools](https://llm.datasette.io/en/stable/tools.html#tools)
- … and much, much more

## Quick start

First, install LLM using `pip` or Homebrew or `pipx` or `uv`:

```bash
pip install llm
```

Or with Homebrew (see [warning note](https://llm.datasette.io/en/stable/setup.html#homebrew-warning)):

```bash
brew install llm
```

Or with [pipx](https://pypa.github.io/pipx/):

```bash
pipx install llm
```

Or with [uv](https://docs.astral.sh/uv/guides/tools/)

```bash
uv tool install llm
```

If you have an [OpenAI API key](https://platform.openai.com/api-keys) key you can run this:

```bash
# Paste your OpenAI API key into this
l
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

