---
id: github.com-jacob-bd-notebooklm-cli-4e6ef6ea-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:10.507746
---

# KNOWLEDGE EXTRACT: github.com_jacob-bd_notebooklm-cli_4e6ef6ea
> **Extracted on:** 2026-04-01 09:39:33
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520353/github.com_jacob-bd_notebooklm-cli_4e6ef6ea

---

## File: `.gitignore`
```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# Environment variables
.env

# Mac
.DS_Store

# User specific
.gemini/

# Auto Claude data directory
.auto-claude/

# Auto Claude generated files
.auto-claude-security.json
.auto-claude-status
.claude_settings.json
.worktrees/
.security-key
logs/security/
todo.md

# MCP reference folder (local only)
mcp-reference/
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [0.1.12] - 2026-01-18

### Added
- **Demo Video**: Added ~12 minute demo video to README

## [0.1.11] - 2026-01-18

### Added
- **AI Skill**: New `nlm-cli-skill/` folder containing a comprehensive skill for AI coding assistants (Claude Code, Gemini CLI/Antigravity, OpenAI Codex, and any tool supporting SKILL.md format).
- **AI Docs**: Enhanced `nlm --ai` output with 12 tips for AI assistants including:
  - Always ask user confirmation before delete operations
  - Check existing aliases before creating new ones
  - Do not launch REPL (`nlm chat start`) - use `nlm notebook query` instead
  - Use `--json` for structured output parsing

## [0.1.8] - 2026-01-17

### Added
- **Documentation**: New `docs/TROUBLESHOOTING.md` with common issues and solutions.
  - Includes OpenAI Codex sandbox network access configuration.
- **Source Types**: Added support for `uploaded_file`, `image`, and `word_doc` source types.

### Fixed
- **URL Parsing**: Fixed URL extraction for different source types in `source list`:
  - YouTube videos now correctly extract URL from metadata index 5.
  - Web pages correctly extract URL from metadata index 7.
  - Drive documents now generate proper Drive URLs from document IDs.

## [0.1.7] - 2026-01-16

### Added
- **Performance**: Added `--skip-freshness/-S` flag to `nlm source list --drive`.
  - Skips N+1 HTTP requests for freshness checks, significantly faster for notebooks with many Drive sources.
- **Export**: Added `--output/-o` flag to `nlm source content` to export source text directly to file.
- **Developer Docs**: Added `CONTRIBUTING.md` with development setup, code style, testing, and PR guidelines.
- **Shell Completion**: Documented `nlm --install-completion` for tab completion setup.

### Changed
- **UX**: Generation commands now show progress spinners during API calls (audio, report, quiz, flashcards, mindmap, slides, infographic, video, data-table).
- **UX**: Artifact status table now uses Unicode symbols (✓, ●, ✗) for faster visual scanning.

## [0.1.6] - 2026-01-16

### Fixed
- **Chrome Port Conflict**: `nlm login` now works when port 9222 is already in use (Issue #5).
  - Automatically finds an available port in range 9222-9231.
  - Reconnects to existing NLM auth Chrome if already running.
  - Improved error messages for stale profile locks.

## [0.1.5] - 2026-01-15

### Added
- **Config CLI**: New `nlm config` command group to view and edit configuration.
  - `nlm config show`: Display current config (TOML/JSON).
  - `nlm config get <key>`: specific setting.
  - `nlm config set <key> <value>`: Update setting.
- **Interactive Chat REPL**: New `nlm chat start <notebook-id>` for multi-turn conversations.
  - Maintains conversation context across turns
  - Slash commands: `/exit`, `/clear`, `/sources`, `/help`
  - Rich Markdown rendering for AI responses

### Fixed
- **Citation Display**: Fixed incorrect source titles in REPL citation legend.
  - Citations now correctly map to source UUIDs via backend metadata.
  - Multiple citations referencing the same source are grouped together.

## [0.1.4] - 2026-01-15

### Added
- **Auto-Authentication**: Ported robust 3-layer authentication recovery from `notebooklm-mcp`.
  - Layer 1: Automatic CSRF/Session ID refresh.
  - Layer 2: Automatic reload of tokens from disk if updated externally.
  - Layer 3: Headless Chrome authentication if profile has saved login.
- Added `auth_refresh.py` module for handling headless auth.

### Changed
- Refactored `client.py` to use `CodeMapper` pattern and centralized `constants.py` for better maintainability (Issue #3).


The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2026-01-15

### 🐛 Fixed
- Extended timeout for Drive source operations from 30s to 120s (fixes #4).
  - Large Google Slides presentations (100+ slides) no longer timeout during upload.

## [0.1.2] - 2026-01-10

### 🚀 Added
- Added `--url` flag to `nlm source list` for a simplified "ID: URL" output format.
- Added `url` field to JSON source output (now always present).

### 💅 Changed
- Improved `nlm source list --full` table layout:
    - Expanded URL column width to 80 chars and enabled wrapping.
    - Tightened Title column to 30 chars with ellipsis.
- Updated documentation (`README.md` and `nlm --ai`) to reflect new source list features.

## [0.1.1] - 2026-01-10

### 🚀 Added
- Auto-detection of alias types when setting aliases (`nlm alias set`).
- Type icons/emojis in `nlm alias list` output.
- Support for `notebook`, `source`, `artifact`, `task` types in alias storage.

### 🧹 Changed
- Removed manual `detect-types` command (superseded by auto-detection on creation).
- Updated documentation to reflect alias system improvements.

## [0.1.0] - 2026-01-09

### 🎉 Initial Release
- Core commands: `notebook`, `source`, `studio`, `auth`, `research`.
- Chrome DevTools Protocol authentication.
- `--ai` flag for AI-friendly documentation.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to NotebookLM CLI

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/jacob-bd/notebooklm-cli.git
cd notebooklm-cli

# Install with development dependencies
uv pip install -e ".[dev]"

# Verify setup
uv run pytest
```

## Project Structure

```
src/nlm/
├── cli/         # Typer command definitions (one file per command group)
├── core/        # Business logic: client.py (API), auth.py, exceptions.py
├── output/      # Formatters for table/JSON/quiet output
├── utils/       # Helpers: config.py, cdp.py (Chrome DevTools)
└── ai_docs.py   # Content for `nlm --ai` flag
```

**Where to add features:**
- New commands → `cli/` (create new file, register in `cli/main.py`)
- API methods → `core/client.py`
- Output formatting → `output/formatters.py`

## Code Style

We use **Ruff** for linting and formatting. Configuration is in `pyproject.toml`.

```bash
# Check for issues
uv run ruff check src/

# Auto-fix issues
uv run ruff check --fix src/

# Format code
uv run ruff format src/
```

**Key conventions:**
- Line length: 100 characters
- Target Python: 3.10+
- Imports: sorted by Ruff (isort-compatible)

## Testing

### Unit Tests
```bash
uv run pytest
```

### End-to-End Tests
```bash
# Requires valid authentication
uv run python tests/run_e2e_tests.py
```

**Testing requirements:**
- New features should include unit tests
- API-dependent tests should be in `tests/run_e2e_tests.py`
- Tests must pass before PR merge

## Pull Request Process

1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/my-feature`)
3. **Make your changes** with descriptive commits
4. **Run tests** (`uv run pytest`)
5. **Run linter** (`uv run ruff check src/`)
6. **Open a PR** with a clear description

**Commit message format:**
```
<type>: <short description>

<optional body with details>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Example: `feat: add --skip-freshness flag to source list`

## Release Process (Maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with new version section
3. Commit: `chore: bump version to X.Y.Z`
4. Tag: `git tag vX.Y.Z && git push --tags`
5. GitHub Actions will publish to PyPI

## Questions?

Open an issue or start a discussion on GitHub. We're happy to help!
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2024 Jacob

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `MCP_REFERENCE.md`
```markdown
# MCP Reference

For the NotebookLM MCP server implementation that this CLI is based on, see:

**Repository:** https://github.com/jacob-bd/notebooklm-mcp

The MCP server provides similar functionality through the Model Context Protocol.
```

## File: `README.md`
```markdown
<div align="center">

> [!CAUTION]
> ## 🚨 Project Deprecated
> **This project has been merged into [NotebookLM MCP CLI](https://github.com/jacob-bd/notebooklm-mcp-cli).**
> 
> No further updates will be made to this repository.
> The new package includes both the CLI (`nlm`) and MCP server (`notebooklm-mcp`) in a single installation.

</div>

---

<div align="center">
  <img src="assets/logo.jpeg" alt="NotebookLM CLI Logo">
  <h1>NLM - NotebookLM CLI</h1>
  <p><strong>A powerful command-line interface for Google NotebookLM</strong></p>

  [![PyPI version](https://img.shields.io/pypi/v/notebooklm-cli.svg)](https://pypi.org/project/notebooklm-cli/)
  [![Python](https://img.shields.io/pypi/pyversions/notebooklm-cli.svg)](https://pypi.org/project/notebooklm-cli/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
</div>

> ‼️⚠️ **Important Disclaimer**: This CLI uses **internal APIs** that are undocumented and may change without notice. Not affiliated with or endorsed by Google. Use at your own risk for personal/experimental purposes. See also: [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) for the unified CLI + MCP server.

---

## 🎬 Demo

Watch a ~12 minute overview of the CLI in action:

<a href="https://youtu.be/XyXVuALWZkE" target="_blank">
  <img src="https://img.youtube.com/vi/XyXVuALWZkE/maxresdefault.jpg?v=2" alt="NotebookLM CLI Demo" width="600">
</a>

---

## ✨ Features

- **Full NotebookLM API Coverage** — Notebooks, sources, audio podcasts, reports, quizzes, flashcards, mind maps, slides, infographics, videos, and data tables
- **Seamless Authentication** — Uses Chrome DevTools Protocol for reliable, automatic cookie extraction
- **AI-Teachable** — Run `nlm --ai` to output comprehensive documentation that AI assistants can consume
- **Alias System** — Create memorable shortcuts for long UUIDs (e.g., `myproject` instead of `abc123-def456-...`)
- **Multiple Output Formats** — Rich tables, JSON, quiet (IDs only), or full details
- **Profile Support** — Manage multiple Google accounts with named profiles
- **Research Integration** — Deep web search or Google Drive search to discover and import sources

---

## 📦 Installation

Install from PyPI using your preferred package manager:

```bash
# Using pip
pip install notebooklm-cli

# Using pipx (recommended for CLI tools)
pipx install notebooklm-cli

# Using uv
uv tool install notebooklm-cli
```

**Requirements:**
- Python 3.10+
- Google Chrome (for authentication)

---

## 🚀 Quick Start

### 1. Authenticate

```bash
nlm login
```

This launches Chrome, navigates to NotebookLM, and automatically extracts your session cookies. You'll need to log in to your Google account if not already signed in.

### 2. List Your Notebooks

```bash
nlm notebook list
```

### 3. Create a Notebook and Add Sources

```bash
# Create a new notebook
nlm notebook create "My Research"
# Output: Created notebook: abc123-def456-...

# Add a URL source
nlm source add abc123-def456 --url "https://example.com/article"

# Add a YouTube video
nlm source add abc123-def456 --url "https://youtube.com/watch?v=..."

# Add pasted text
nlm source add abc123-def456 --text "Your content here" --title "My Notes"
```

### 4. Generate a Podcast

```bash
nlm audio create abc123-def456 --confirm
```

### 5. Check Generation Status

```bash
nlm studio status abc123-def456
```

---

## 🏷️ Aliases (UUID Shortcuts)

Tired of typing long UUIDs? Create aliases:

```bash
# Set an alias
nlm alias set myproject abc123-def456-... # Types are auto-detected!

# Now use the alias anywhere
nlm notebook get myproject
nlm source list myproject
nlm audio create myproject --confirm

# Manage aliases
nlm alias list              # List all aliases
nlm alias get myproject     # Resolve to UUID
nlm alias delete myproject  # Remove alias
```

---

## 🤖 AI Integration

### Option 1: Quick Context (`nlm --ai`)

The `--ai` flag outputs comprehensive, structured documentation designed for AI assistants:

```bash
nlm --ai
```

This prints a 400+ line guide covering all commands with exact syntax, authentication flow, error handling, complete task sequences, and 12 tips for AI automation.

**Use case:** Paste the output of `nlm --ai` into your AI assistant's context to teach it how to use the CLI.

### Option 2: AI Skill (`nlm-cli-skill`)

For AI coding assistants that support skills (Claude Code, Gemini CLI/Antigravity, etc.), we provide a pre-packaged skill.

1. **Download**: [Click here to download nlm-cli-skill.zip](assets/nlm-cli-skill.zip) (hosted in this repo).
2. **Install**: Extract the zip file into your AI tool's skills directory (e.g., `~/.gemini/antigravity/skills/`, `~/.claude/skills`, etc.).

**Structure:**
```
nlm-cli-skill/
├── SKILL.md              # Main skill file with 10 critical rules
└── references/
    ├── command_reference.md   # Complete command signatures
    ├── troubleshooting.md     # Error diagnosis & solutions
    └── workflows.md           # End-to-end task sequences
```

---

## 📚 Command Reference

### Core Commands

| Command | Description |
|---------|-------------|
| `nlm login` | Authenticate with NotebookLM (opens Chrome) |
| `nlm auth status` | Check if current session is valid |
| `nlm notebook list` | List all notebooks |
| `nlm notebook create "Title"` | Create a new notebook |
| `nlm notebook get <id>` | Get notebook details |
| `nlm notebook describe <id>` | Get AI-generated summary |
| `nlm notebook query <id> "question"` | Chat with your sources |
| `nlm notebook delete <id> --confirm` | Delete a notebook |

### Source Management

| Command | Description |
|---------|-------------|
| `nlm source list <notebook-id>` | List sources in a notebook |
| `nlm source list <notebook-id> --drive` | Show Drive sources with freshness |
| `nlm source list <notebook-id> --drive -S` | Faster listing, skip freshness checks |
| `nlm source add <id> --url "..."` | Add URL or YouTube source |
| `nlm source add <id> --text "..." --title "..."` | Add pasted text |
| `nlm source add <id> --drive <doc-id>` | Add Google Drive document |
| `nlm source describe <source-id>` | Get AI summary of source |
| `nlm source content <source-id>` | Get raw text content |
| `nlm source stale <notebook-id>` | List outdated Drive sources |
| `nlm source sync <notebook-id> --confirm` | Sync Drive sources |

### Research (Discover New Sources)

| Command | Description |
|---------|-------------|
| `nlm research start "query" --notebook-id <id>` | Start web search (~30s) |
| `nlm research start "query" --notebook-id <id> --mode deep` | Deep research (~5min) |
| `nlm research start "query" --notebook-id <id> --source drive` | Search Google Drive |
| `nlm research status <notebook-id>` | Check research progress |
| `nlm research import <notebook-id> <task-id>` | Import discovered sources |

### Content Generation

All generation commands require `--confirm` (or `-y`) to execute:

| Command | Description |
|---------|-------------|
| `nlm audio create <id> --confirm` | Generate podcast/audio overview |
| `nlm report create <id> --confirm` | Generate briefing doc or study guide |
| `nlm quiz create <id> --confirm` | Generate quiz questions |
| `nlm flashcards create <id> --confirm` | Generate flashcards |
| `nlm mindmap create <id> --confirm` | Generate mind map |
| `nlm slides create <id> --confirm` | Generate slide deck |
| `nlm infographic create <id> --confirm` | Generate infographic |
| `nlm video create <id> --confirm` | Generate video overview |
| `nlm data-table create <id> "description" --confirm` | Extract data as table |

### Studio (Artifact Management)

| Command | Description |
|---------|-------------|
| `nlm studio status <notebook-id>` | List all generated artifacts |
| `nlm studio delete <notebook-id> <artifact-id> --confirm` | Delete an artifact |

### Chat (Interactive Q&A)

| Command | Description |
|---------|-------------|
| `nlm chat start <notebook-id>` | Start interactive REPL session |
| `nlm chat configure <notebook-id>` | Configure chat goal and response style |
| `nlm notebook query <id> "question"` | One-shot question (no session) |

**Chat REPL commands:** `/sources`, `/clear`, `/help`, `/exit`

### Configuration

| Command | Description |
|---------|-------------|
| `nlm config show` | Show current configuration |
| `nlm config get <key>` | Get a specific setting |
| `nlm config set <key> <value>` | Update a setting |

### Authentication

| Command | Description |
|---------|-------------|
| `nlm login` | Authenticate with Chrome |
| `nlm login --check` | Verify current credentials |
| `nlm auth status` | Check session validity |
| `nlm auth list` | List all profiles |
| `nlm auth delete <profile> --confirm` | Delete a profile |

## 🎛️ Output Formats

Most list commands support multiple output formats:

```bash
nlm notebook list              # Rich table (default)
nlm notebook list --json       # JSON output
nlm notebook list --quiet      # IDs only (for scripting)
nlm notebook list --title      # "ID: Title" format
nlm source list --url          # "ID: URL" format
nlm notebook list --full       # All columns
```

---

## 👤 Profiles (Multiple Accounts)

Manage multiple Google accounts with named profiles:

```bash
# Login to a specific profile
nlm login --profile work
nlm login --profile personal

# Use a profile for commands
nlm notebook list --profile work

# List all profiles
nlm auth list

# Delete a profile
nlm auth delete work --confirm
```

---

## ⌨️ Shell Completion

Enable tab completion for faster command entry:

```bash
# Auto-install for your current shell
nlm --install-completion

# Or show the completion script to install manually
nlm --show-completion
```

---

## ⚠️ Session Lifetime

NotebookLM sessions typically last **~20 minutes**. If commands start failing with authentication errors, simply re-run:

```bash
nlm login
```

---

## 🔧 Troubleshooting

Having issues? See the [Troubleshooting Guide](troubleshooting.md) for solutions to common problems including authentication, network issues, and OpenAI Codex sandbox configuration.

---

## 📖 Documentation

For detailed technical documentation on the internal API and advanced usage, see the [`docs/`](docs/) folder:

- [Troubleshooting](troubleshooting.md) — Common issues and solutions
- [CLI Test Plan](docs/CLI_TEST_PLAN.md) — End-to-end testing procedures
- [Technical Deep Dive](docs/TECHNICAL_DEEP_DIVE.md) — Internal API details

For AI assistants, run `nlm --ai` to get the full command reference.

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Quick start for contributors
git clone https://github.com/jacob-bd/notebooklm-cli.git
cd notebooklm-cli
uv pip install -e ".[dev]"
uv run pytest
```

---

## ⚠️ Limitations

- **Rate limits**: Free tier has ~50 queries/day
- **No official support**: API may change without notice
- **Cookie expiration**: Need to re-authenticate every few weeks

---

## 🎨 Vibe Coding Alert

Full transparency: this project was built by a non-developer using AI coding assistants. If you're an experienced Python developer, you might look at this codebase and wince. That's okay.

The goal here was to scratch an itch—programmatic access to NotebookLM—and learn along the way. The code works, but it's likely missing patterns, optimizations, or elegance that only years of experience can provide.

**This is where you come in.** If you see something that makes you cringe, please consider contributing rather than just closing the tab. PRs and issues are welcome.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
```

## File: `bump_version.sh`
```bash
#!/bin/bash
# Version bump script for nlm
# Usage: ./bump_version.sh <new_version>
# Example: ./bump_version.sh 0.2.0

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <new_version>"
    echo "Example: $0 0.2.0"
    exit 1
fi

NEW_VERSION=$1

echo "Bumping version to $NEW_VERSION..."

# Update pyproject.toml
sed -i '' "s/^version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

# Update __init__.py
sed -i '' "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" src/nlm/__init__.py

echo "Updated files:"
grep "version" pyproject.toml | head -1
grep "__version__" src/nlm/__init__.py

echo ""
echo "To publish:"
echo "  git add pyproject.toml src/nlm/__init__.py"
echo "  git commit -m 'chore: bump version to $NEW_VERSION'"
echo "  git tag v$NEW_VERSION"
echo "  git push origin main --tags"
```

## File: `pyproject.toml`
```
[project]
name = "notebooklm-cli"
version = "0.1.12"
description = "Command-line interface for Google NotebookLM"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
authors = [
    {name = "Jacob", email = "jacob@example.com"}
]
keywords = ["notebooklm", "cli", "google", "ai", "notebook"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Utilities",
]

dependencies = [
    "typer>=0.9.0",
    "httpx>=0.25.0",
    "rich>=13.0.0",
    "pydantic>=2.0.0",
    "platformdirs>=4.0.0",
    "websocket-client>=1.6.0",  # For CDP cookie extraction
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]

[project.scripts]
nlm = "nlm.cli.main:app"

[project.urls]
Homepage = "https://github.com/jacob-bd/notebooklm-cli"
Repository = "https://github.com/jacob-bd/notebooklm-cli"
Issues = "https://github.com/jacob-bd/notebooklm-cli/issues"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/nlm"]

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.10"
strict = true
warn_return_any = true
warn_unused_ignores = true

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10"

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "backports-asyncio-runner"
version = "1.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8e/ff/70dca7d7cb1cbc0edb2c6cc0c38b65cba36cccc491eca64cabd5fe7f8670/backports_asyncio_runner-1.2.0.tar.gz", hash = "sha256:a5aa7b2b7d8f8bfcaa2b57313f70792df84e32a2a746f585213373f900b42162", size = 69893, upload-time = "2025-07-02T02:27:15.685Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/59/76ab57e3fe74484f48a53f8e337171b4a2349e506eabe136d7e01d059086/backports_asyncio_runner-1.2.0-py3-none-any.whl", hash = "sha256:0da0a936a8aeb554eccb426dc55af3ba63bcdc69fa1a600b5bb305413a4477b5", size = 12313, upload-time = "2025-07-02T02:27:14.263Z" },
]

[[package]]
name = "certifi"
version = "2026.1.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e0/2d/a891ca51311197f6ad14a7ef42e2399f36cf2f9bd44752b3dc4eab60fdc5/certifi-2026.1.4.tar.gz", hash = "sha256:ac726dd470482006e014ad384921ed6438c457018f4b3d204aea4281258b2120", size = 154268, upload-time = "2026-01-04T02:42:41.825Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e6/ad/3cc14f097111b4de0040c83a525973216457bbeeb63739ef1ed275c1c021/certifi-2026.1.4-py3-none-any.whl", hash = "sha256:9943707519e4add1115f44c2bc244f782c0249876bf51b6599fee1ffbedd685c", size = 152900, upload-time = "2026-01-04T02:42:40.15Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371, upload-time = "2025-11-21T23:01:54.787Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740, upload-time = "2025-11-21T23:01:53.443Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
]

[[package]]
name = "librt"
version = "0.7.7"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b7/29/47f29026ca17f35cf299290292d5f8331f5077364974b7675a353179afa2/librt-0.7.7.tar.gz", hash = "sha256:81d957b069fed1890953c3b9c3895c7689960f233eea9a1d9607f71ce7f00b2c", size = 145910, upload-time = "2026-01-01T23:52:22.87Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/84/2cfb1f3b9b60bab52e16a220c931223fc8e963d0d7bb9132bef012aafc3f/librt-0.7.7-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:e4836c5645f40fbdc275e5670819bde5ab5f2e882290d304e3c6ddab1576a6d0", size = 54709, upload-time = "2026-01-01T23:50:48.326Z" },
    { url = "https://files.pythonhosted.org/packages/19/a1/3127b277e9d3784a8040a54e8396d9ae5c64d6684dc6db4b4089b0eedcfb/librt-0.7.7-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:6ae8aec43117a645a31e5f60e9e3a0797492e747823b9bda6972d521b436b4e8", size = 56658, upload-time = "2026-01-01T23:50:49.74Z" },
    { url = "https://files.pythonhosted.org/packages/3a/e9/b91b093a5c42eb218120445f3fef82e0b977fa2225f4d6fc133d25cdf86a/librt-0.7.7-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:aea05f701ccd2a76b34f0daf47ca5068176ff553510b614770c90d76ac88df06", size = 161026, upload-time = "2026-01-01T23:50:50.853Z" },
    { url = "https://files.pythonhosted.org/packages/c7/cb/1ded77d5976a79d7057af4a010d577ce4f473ff280984e68f4974a3281e5/librt-0.7.7-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7b16ccaeff0ed4355dfb76fe1ea7a5d6d03b5ad27f295f77ee0557bc20a72495", size = 169529, upload-time = "2026-01-01T23:50:52.24Z" },
    { url = "https://files.pythonhosted.org/packages/da/6e/6ca5bdaa701e15f05000ac1a4c5d1475c422d3484bd3d1ca9e8c2f5be167/librt-0.7.7-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c48c7e150c095d5e3cea7452347ba26094be905d6099d24f9319a8b475fcd3e0", size = 183271, upload-time = "2026-01-01T23:50:55.287Z" },
    { url = "https://files.pythonhosted.org/packages/e7/2d/55c0e38073997b4bbb5ddff25b6d1bbba8c2f76f50afe5bb9c844b702f34/librt-0.7.7-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:4dcee2f921a8632636d1c37f1bbdb8841d15666d119aa61e5399c5268e7ce02e", size = 179039, upload-time = "2026-01-01T23:50:56.807Z" },
    { url = "https://files.pythonhosted.org/packages/33/4e/3662a41ae8bb81b226f3968426293517b271d34d4e9fd4b59fc511f1ae40/librt-0.7.7-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:14ef0f4ac3728ffd85bfc58e2f2f48fb4ef4fa871876f13a73a7381d10a9f77c", size = 173505, upload-time = "2026-01-01T23:50:58.291Z" },
    { url = "https://files.pythonhosted.org/packages/f8/5d/cf768deb8bdcbac5f8c21fcb32dd483d038d88c529fd351bbe50590b945d/librt-0.7.7-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:e4ab69fa37f8090f2d971a5d2bc606c7401170dbdae083c393d6cbf439cb45b8", size = 193570, upload-time = "2026-01-01T23:50:59.546Z" },
    { url = "https://files.pythonhosted.org/packages/a1/ea/ee70effd13f1d651976d83a2812391f6203971740705e3c0900db75d4bce/librt-0.7.7-cp310-cp310-win32.whl", hash = "sha256:4bf3cc46d553693382d2abf5f5bd493d71bb0f50a7c0beab18aa13a5545c8900", size = 42600, upload-time = "2026-01-01T23:51:00.694Z" },
    { url = "https://files.pythonhosted.org/packages/f0/eb/dc098730f281cba76c279b71783f5de2edcba3b880c1ab84a093ef826062/librt-0.7.7-cp310-cp310-win_amd64.whl", hash = "sha256:f0c8fe5aeadd8a0e5b0598f8a6ee3533135ca50fd3f20f130f9d72baf5c6ac58", size = 48977, upload-time = "2026-01-01T23:51:01.726Z" },
    { url = "https://files.pythonhosted.org/packages/f0/56/30b5c342518005546df78841cb0820ae85a17e7d07d521c10ef367306d0d/librt-0.7.7-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a487b71fbf8a9edb72a8c7a456dda0184642d99cd007bc819c0b7ab93676a8ee", size = 54709, upload-time = "2026-01-01T23:51:02.774Z" },
    { url = "https://files.pythonhosted.org/packages/72/78/9f120e3920b22504d4f3835e28b55acc2cc47c9586d2e1b6ba04c3c1bf01/librt-0.7.7-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:f4d4efb218264ecf0f8516196c9e2d1a0679d9fb3bb15df1155a35220062eba8", size = 56663, upload-time = "2026-01-01T23:51:03.838Z" },
    { url = "https://files.pythonhosted.org/packages/1c/ea/7d7a1ee7dfc1151836028eba25629afcf45b56bbc721293e41aa2e9b8934/librt-0.7.7-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:b8bb331aad734b059c4b450cd0a225652f16889e286b2345af5e2c3c625c3d85", size = 161705, upload-time = "2026-01-01T23:51:04.917Z" },
    { url = "https://files.pythonhosted.org/packages/45/a5/952bc840ac8917fbcefd6bc5f51ad02b89721729814f3e2bfcc1337a76d6/librt-0.7.7-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:467dbd7443bda08338fc8ad701ed38cef48194017554f4c798b0a237904b3f99", size = 171029, upload-time = "2026-01-01T23:51:06.09Z" },
    { url = "https://files.pythonhosted.org/packages/fa/bf/c017ff7da82dc9192cf40d5e802a48a25d00e7639b6465cfdcee5893a22c/librt-0.7.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:50d1d1ee813d2d1a3baf2873634ba506b263032418d16287c92ec1cc9c1a00cb", size = 184704, upload-time = "2026-01-01T23:51:07.549Z" },
    { url = "https://files.pythonhosted.org/packages/77/ec/72f3dd39d2cdfd6402ab10836dc9cbf854d145226062a185b419c4f1624a/librt-0.7.7-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c7e5070cf3ec92d98f57574da0224f8c73faf1ddd6d8afa0b8c9f6e86997bc74", size = 180719, upload-time = "2026-01-01T23:51:09.062Z" },
    { url = "https://files.pythonhosted.org/packages/78/86/06e7a1a81b246f3313bf515dd9613a1c81583e6fd7843a9f4d625c4e926d/librt-0.7.7-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:bdb9f3d865b2dafe7f9ad7f30ef563c80d0ddd2fdc8cc9b8e4f242f475e34d75", size = 174537, upload-time = "2026-01-01T23:51:10.611Z" },
    { url = "https://files.pythonhosted.org/packages/83/08/f9fb2edc9c7a76e95b2924ce81d545673f5b034e8c5dd92159d1c7dae0c6/librt-0.7.7-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:8185c8497d45164e256376f9da5aed2bb26ff636c798c9dabe313b90e9f25b28", size = 195238, upload-time = "2026-01-01T23:51:11.762Z" },
    { url = "https://files.pythonhosted.org/packages/ba/56/ea2d2489d3ea1f47b301120e03a099e22de7b32c93df9a211e6ff4f9bf38/librt-0.7.7-cp311-cp311-win32.whl", hash = "sha256:44d63ce643f34a903f09ff7ca355aae019a3730c7afd6a3c037d569beeb5d151", size = 42939, upload-time = "2026-01-01T23:51:13.192Z" },
    { url = "https://files.pythonhosted.org/packages/58/7b/c288f417e42ba2a037f1c0753219e277b33090ed4f72f292fb6fe175db4c/librt-0.7.7-cp311-cp311-win_amd64.whl", hash = "sha256:7d13cc340b3b82134f8038a2bfe7137093693dcad8ba5773da18f95ad6b77a8a", size = 49240, upload-time = "2026-01-01T23:51:14.264Z" },
    { url = "https://files.pythonhosted.org/packages/7c/24/738eb33a6c1516fdb2dfd2a35db6e5300f7616679b573585be0409bc6890/librt-0.7.7-cp311-cp311-win_arm64.whl", hash = "sha256:983de36b5a83fe9222f4f7dcd071f9b1ac6f3f17c0af0238dadfb8229588f890", size = 42613, upload-time = "2026-01-01T23:51:15.268Z" },
    { url = "https://files.pythonhosted.org/packages/56/72/1cd9d752070011641e8aee046c851912d5f196ecd726fffa7aed2070f3e0/librt-0.7.7-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:2a85a1fc4ed11ea0eb0a632459ce004a2d14afc085a50ae3463cd3dfe1ce43fc", size = 55687, upload-time = "2026-01-01T23:51:16.291Z" },
    { url = "https://files.pythonhosted.org/packages/50/aa/d5a1d4221c4fe7e76ae1459d24d6037783cb83c7645164c07d7daf1576ec/librt-0.7.7-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:c87654e29a35938baead1c4559858f346f4a2a7588574a14d784f300ffba0efd", size = 57136, upload-time = "2026-01-01T23:51:17.363Z" },
    { url = "https://files.pythonhosted.org/packages/23/6f/0c86b5cb5e7ef63208c8cc22534df10ecc5278efc0d47fb8815577f3ca2f/librt-0.7.7-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:c9faaebb1c6212c20afd8043cd6ed9de0a47d77f91a6b5b48f4e46ed470703fe", size = 165320, upload-time = "2026-01-01T23:51:18.455Z" },
    { url = "https://files.pythonhosted.org/packages/16/37/df4652690c29f645ffe405b58285a4109e9fe855c5bb56e817e3e75840b3/librt-0.7.7-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1908c3e5a5ef86b23391448b47759298f87f997c3bd153a770828f58c2bb4630", size = 174216, upload-time = "2026-01-01T23:51:19.599Z" },
    { url = "https://files.pythonhosted.org/packages/9a/d6/d3afe071910a43133ec9c0f3e4ce99ee6df0d4e44e4bddf4b9e1c6ed41cc/librt-0.7.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dbc4900e95a98fc0729523be9d93a8fedebb026f32ed9ffc08acd82e3e181503", size = 189005, upload-time = "2026-01-01T23:51:21.052Z" },
    { url = "https://files.pythonhosted.org/packages/d5/18/74060a870fe2d9fd9f47824eba6717ce7ce03124a0d1e85498e0e7efc1b2/librt-0.7.7-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a7ea4e1fbd253e5c68ea0fe63d08577f9d288a73f17d82f652ebc61fa48d878d", size = 183961, upload-time = "2026-01-01T23:51:22.493Z" },
    { url = "https://files.pythonhosted.org/packages/7c/5e/918a86c66304af66a3c1d46d54df1b2d0b8894babc42a14fb6f25511497f/librt-0.7.7-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:ef7699b7a5a244b1119f85c5bbc13f152cd38240cbb2baa19b769433bae98e50", size = 177610, upload-time = "2026-01-01T23:51:23.874Z" },
    { url = "https://files.pythonhosted.org/packages/b2/d7/b5e58dc2d570f162e99201b8c0151acf40a03a39c32ab824dd4febf12736/librt-0.7.7-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:955c62571de0b181d9e9e0a0303c8bc90d47670a5eff54cf71bf5da61d1899cf", size = 199272, upload-time = "2026-01-01T23:51:25.341Z" },
    { url = "https://files.pythonhosted.org/packages/18/87/8202c9bd0968bdddc188ec3811985f47f58ed161b3749299f2c0dd0f63fb/librt-0.7.7-cp312-cp312-win32.whl", hash = "sha256:1bcd79be209313b270b0e1a51c67ae1af28adad0e0c7e84c3ad4b5cb57aaa75b", size = 43189, upload-time = "2026-01-01T23:51:26.799Z" },
    { url = "https://files.pythonhosted.org/packages/61/8d/80244b267b585e7aa79ffdac19f66c4861effc3a24598e77909ecdd0850e/librt-0.7.7-cp312-cp312-win_amd64.whl", hash = "sha256:4353ee891a1834567e0302d4bd5e60f531912179578c36f3d0430f8c5e16b456", size = 49462, upload-time = "2026-01-01T23:51:27.813Z" },
    { url = "https://files.pythonhosted.org/packages/2d/1f/75db802d6a4992d95e8a889682601af9b49d5a13bbfa246d414eede1b56c/librt-0.7.7-cp312-cp312-win_arm64.whl", hash = "sha256:a76f1d679beccccdf8c1958e732a1dfcd6e749f8821ee59d7bec009ac308c029", size = 42828, upload-time = "2026-01-01T23:51:28.804Z" },
    { url = "https://files.pythonhosted.org/packages/8d/5e/d979ccb0a81407ec47c14ea68fb217ff4315521730033e1dd9faa4f3e2c1/librt-0.7.7-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8f4a0b0a3c86ba9193a8e23bb18f100d647bf192390ae195d84dfa0a10fb6244", size = 55746, upload-time = "2026-01-01T23:51:29.828Z" },
    { url = "https://files.pythonhosted.org/packages/f5/2c/3b65861fb32f802c3783d6ac66fc5589564d07452a47a8cf9980d531cad3/librt-0.7.7-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:5335890fea9f9e6c4fdf8683061b9ccdcbe47c6dc03ab8e9b68c10acf78be78d", size = 57174, upload-time = "2026-01-01T23:51:31.226Z" },
    { url = "https://files.pythonhosted.org/packages/50/df/030b50614b29e443607220097ebaf438531ea218c7a9a3e21ea862a919cd/librt-0.7.7-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:9b4346b1225be26def3ccc6c965751c74868f0578cbcba293c8ae9168483d811", size = 165834, upload-time = "2026-01-01T23:51:32.278Z" },
    { url = "https://files.pythonhosted.org/packages/5d/e1/bd8d1eacacb24be26a47f157719553bbd1b3fe812c30dddf121c0436fd0b/librt-0.7.7-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a10b8eebdaca6e9fdbaf88b5aefc0e324b763a5f40b1266532590d5afb268a4c", size = 174819, upload-time = "2026-01-01T23:51:33.461Z" },
    { url = "https://files.pythonhosted.org/packages/46/7d/91d6c3372acf54a019c1ad8da4c9ecf4fc27d039708880bf95f48dbe426a/librt-0.7.7-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:067be973d90d9e319e6eb4ee2a9b9307f0ecd648b8a9002fa237289a4a07a9e7", size = 189607, upload-time = "2026-01-01T23:51:34.604Z" },
    { url = "https://files.pythonhosted.org/packages/fa/ac/44604d6d3886f791fbd1c6ae12d5a782a8f4aca927484731979f5e92c200/librt-0.7.7-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:23d2299ed007812cccc1ecef018db7d922733382561230de1f3954db28433977", size = 184586, upload-time = "2026-01-01T23:51:35.845Z" },
    { url = "https://files.pythonhosted.org/packages/5c/26/d8a6e4c17117b7f9b83301319d9a9de862ae56b133efb4bad8b3aa0808c9/librt-0.7.7-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:6b6f8ea465524aa4c7420c7cc4ca7d46fe00981de8debc67b1cc2e9957bb5b9d", size = 178251, upload-time = "2026-01-01T23:51:37.018Z" },
    { url = "https://files.pythonhosted.org/packages/99/ab/98d857e254376f8e2f668e807daccc1f445e4b4fc2f6f9c1cc08866b0227/librt-0.7.7-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f8df32a99cc46eb0ee90afd9ada113ae2cafe7e8d673686cf03ec53e49635439", size = 199853, upload-time = "2026-01-01T23:51:38.195Z" },
    { url = "https://files.pythonhosted.org/packages/7c/55/4523210d6ae5134a5da959900be43ad8bab2e4206687b6620befddb5b5fd/librt-0.7.7-cp313-cp313-win32.whl", hash = "sha256:86f86b3b785487c7760247bcdac0b11aa8bf13245a13ed05206286135877564b", size = 43247, upload-time = "2026-01-01T23:51:39.629Z" },
    { url = "https://files.pythonhosted.org/packages/25/40/3ec0fed5e8e9297b1cf1a3836fb589d3de55f9930e3aba988d379e8ef67c/librt-0.7.7-cp313-cp313-win_amd64.whl", hash = "sha256:4862cb2c702b1f905c0503b72d9d4daf65a7fdf5a9e84560e563471e57a56949", size = 49419, upload-time = "2026-01-01T23:51:40.674Z" },
    { url = "https://files.pythonhosted.org/packages/1c/7a/aab5f0fb122822e2acbc776addf8b9abfb4944a9056c00c393e46e543177/librt-0.7.7-cp313-cp313-win_arm64.whl", hash = "sha256:0996c83b1cb43c00e8c87835a284f9057bc647abd42b5871e5f941d30010c832", size = 42828, upload-time = "2026-01-01T23:51:41.731Z" },
    { url = "https://files.pythonhosted.org/packages/69/9c/228a5c1224bd23809a635490a162e9cbdc68d99f0eeb4a696f07886b8206/librt-0.7.7-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:23daa1ab0512bafdd677eb1bfc9611d8ffbe2e328895671e64cb34166bc1b8c8", size = 55188, upload-time = "2026-01-01T23:51:43.14Z" },
    { url = "https://files.pythonhosted.org/packages/ba/c2/0e7c6067e2b32a156308205e5728f4ed6478c501947e9142f525afbc6bd2/librt-0.7.7-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:558a9e5a6f3cc1e20b3168fb1dc802d0d8fa40731f6e9932dcc52bbcfbd37111", size = 56895, upload-time = "2026-01-01T23:51:44.534Z" },
    { url = "https://files.pythonhosted.org/packages/0e/77/de50ff70c80855eb79d1d74035ef06f664dd073fb7fb9d9fb4429651b8eb/librt-0.7.7-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:2567cb48dc03e5b246927ab35cbb343376e24501260a9b5e30b8e255dca0d1d2", size = 163724, upload-time = "2026-01-01T23:51:45.571Z" },
    { url = "https://files.pythonhosted.org/packages/6e/19/f8e4bf537899bdef9e0bb9f0e4b18912c2d0f858ad02091b6019864c9a6d/librt-0.7.7-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6066c638cdf85ff92fc6f932d2d73c93a0e03492cdfa8778e6d58c489a3d7259", size = 172470, upload-time = "2026-01-01T23:51:46.823Z" },
    { url = "https://files.pythonhosted.org/packages/42/4c/dcc575b69d99076768e8dd6141d9aecd4234cba7f0e09217937f52edb6ed/librt-0.7.7-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a609849aca463074c17de9cda173c276eb8fee9e441053529e7b9e249dc8b8ee", size = 186806, upload-time = "2026-01-01T23:51:48.009Z" },
    { url = "https://files.pythonhosted.org/packages/fe/f8/4094a2b7816c88de81239a83ede6e87f1138477d7ee956c30f136009eb29/librt-0.7.7-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:add4e0a000858fe9bb39ed55f31085506a5c38363e6eb4a1e5943a10c2bfc3d1", size = 181809, upload-time = "2026-01-01T23:51:49.35Z" },
    { url = "https://files.pythonhosted.org/packages/1b/ac/821b7c0ab1b5a6cd9aee7ace8309c91545a2607185101827f79122219a7e/librt-0.7.7-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:a3bfe73a32bd0bdb9a87d586b05a23c0a1729205d79df66dee65bb2e40d671ba", size = 175597, upload-time = "2026-01-01T23:51:50.636Z" },
    { url = "https://files.pythonhosted.org/packages/71/f9/27f6bfbcc764805864c04211c6ed636fe1d58f57a7b68d1f4ae5ed74e0e0/librt-0.7.7-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:0ecce0544d3db91a40f8b57ae26928c02130a997b540f908cefd4d279d6c5848", size = 196506, upload-time = "2026-01-01T23:51:52.535Z" },
    { url = "https://files.pythonhosted.org/packages/46/ba/c9b9c6fc931dd7ea856c573174ccaf48714905b1a7499904db2552e3bbaf/librt-0.7.7-cp314-cp314-win32.whl", hash = "sha256:8f7a74cf3a80f0c3b0ec75b0c650b2f0a894a2cec57ef75f6f72c1e82cdac61d", size = 39747, upload-time = "2026-01-01T23:51:53.683Z" },
    { url = "https://files.pythonhosted.org/packages/c5/69/cd1269337c4cde3ee70176ee611ab0058aa42fc8ce5c9dce55f48facfcd8/librt-0.7.7-cp314-cp314-win_amd64.whl", hash = "sha256:3d1fe2e8df3268dd6734dba33ededae72ad5c3a859b9577bc00b715759c5aaab", size = 45971, upload-time = "2026-01-01T23:51:54.697Z" },
    { url = "https://files.pythonhosted.org/packages/79/fd/e0844794423f5583108c5991313c15e2b400995f44f6ec6871f8aaf8243c/librt-0.7.7-cp314-cp314-win_arm64.whl", hash = "sha256:2987cf827011907d3dfd109f1be0d61e173d68b1270107bb0e89f2fca7f2ed6b", size = 39075, upload-time = "2026-01-01T23:51:55.726Z" },
    { url = "https://files.pythonhosted.org/packages/42/02/211fd8f7c381e7b2a11d0fdfcd410f409e89967be2e705983f7c6342209a/librt-0.7.7-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:8e92c8de62b40bfce91d5e12c6e8b15434da268979b1af1a6589463549d491e6", size = 57368, upload-time = "2026-01-01T23:51:56.706Z" },
    { url = "https://files.pythonhosted.org/packages/4c/b6/aca257affae73ece26041ae76032153266d110453173f67d7603058e708c/librt-0.7.7-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:f683dcd49e2494a7535e30f779aa1ad6e3732a019d80abe1309ea91ccd3230e3", size = 59238, upload-time = "2026-01-01T23:51:58.066Z" },
    { url = "https://files.pythonhosted.org/packages/96/47/7383a507d8e0c11c78ca34c9d36eab9000db5989d446a2f05dc40e76c64f/librt-0.7.7-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:9b15e5d17812d4d629ff576699954f74e2cc24a02a4fc401882dd94f81daba45", size = 183870, upload-time = "2026-01-01T23:51:59.204Z" },
    { url = "https://files.pythonhosted.org/packages/a4/b8/50f3d8eec8efdaf79443963624175c92cec0ba84827a66b7fcfa78598e51/librt-0.7.7-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c084841b879c4d9b9fa34e5d5263994f21aea7fd9c6add29194dbb41a6210536", size = 194608, upload-time = "2026-01-01T23:52:00.419Z" },
    { url = "https://files.pythonhosted.org/packages/23/d9/1b6520793aadb59d891e3b98ee057a75de7f737e4a8b4b37fdbecb10d60f/librt-0.7.7-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:10c8fb9966f84737115513fecbaf257f9553d067a7dd45a69c2c7e5339e6a8dc", size = 206776, upload-time = "2026-01-01T23:52:01.705Z" },
    { url = "https://files.pythonhosted.org/packages/ff/db/331edc3bba929d2756fa335bfcf736f36eff4efcb4f2600b545a35c2ae58/librt-0.7.7-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:9b5fb1ecb2c35362eab2dbd354fd1efa5a8440d3e73a68be11921042a0edc0ff", size = 203206, upload-time = "2026-01-01T23:52:03.315Z" },
    { url = "https://files.pythonhosted.org/packages/b2/e1/6af79ec77204e85f6f2294fc171a30a91bb0e35d78493532ed680f5d98be/librt-0.7.7-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:d1454899909d63cc9199a89fcc4f81bdd9004aef577d4ffc022e600c412d57f3", size = 196697, upload-time = "2026-01-01T23:52:04.857Z" },
    { url = "https://files.pythonhosted.org/packages/f3/46/de55ecce4b2796d6d243295c221082ca3a944dc2fb3a52dcc8660ce7727d/librt-0.7.7-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:7ef28f2e7a016b29792fe0a2dd04dec75725b32a1264e390c366103f834a9c3a", size = 217193, upload-time = "2026-01-01T23:52:06.159Z" },
    { url = "https://files.pythonhosted.org/packages/41/61/33063e271949787a2f8dd33c5260357e3d512a114fc82ca7890b65a76e2d/librt-0.7.7-cp314-cp314t-win32.whl", hash = "sha256:5e419e0db70991b6ba037b70c1d5bbe92b20ddf82f31ad01d77a347ed9781398", size = 40277, upload-time = "2026-01-01T23:52:07.625Z" },
    { url = "https://files.pythonhosted.org/packages/06/21/1abd972349f83a696ea73159ac964e63e2d14086fdd9bc7ca878c25fced4/librt-0.7.7-cp314-cp314t-win_amd64.whl", hash = "sha256:d6b7d93657332c817b8d674ef6bf1ab7796b4f7ce05e420fd45bd258a72ac804", size = 46765, upload-time = "2026-01-01T23:52:08.647Z" },
    { url = "https://files.pythonhosted.org/packages/51/0e/b756c7708143a63fca65a51ca07990fa647db2cc8fcd65177b9e96680255/librt-0.7.7-cp314-cp314t-win_arm64.whl", hash = "sha256:142c2cd91794b79fd0ce113bd658993b7ede0fe93057668c2f98a45ca00b7e91", size = 39724, upload-time = "2026-01-01T23:52:09.745Z" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "mypy"
version = "1.19.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "librt", marker = "platform_python_implementation != 'PyPy'" },
    { name = "mypy-extensions" },
    { name = "pathspec" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f5/db/4efed9504bc01309ab9c2da7e352cc223569f05478012b5d9ece38fd44d2/mypy-1.19.1.tar.gz", hash = "sha256:19d88bb05303fe63f71dd2c6270daca27cb9401c4ca8255fe50d1d920e0eb9ba", size = 3582404, upload-time = "2025-12-15T05:03:48.42Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2f/63/e499890d8e39b1ff2df4c0c6ce5d371b6844ee22b8250687a99fd2f657a8/mypy-1.19.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:5f05aa3d375b385734388e844bc01733bd33c644ab48e9684faa54e5389775ec", size = 13101333, upload-time = "2025-12-15T05:03:03.28Z" },
    { url = "https://files.pythonhosted.org/packages/72/4b/095626fc136fba96effc4fd4a82b41d688ab92124f8c4f7564bffe5cf1b0/mypy-1.19.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:022ea7279374af1a5d78dfcab853fe6a536eebfda4b59deab53cd21f6cd9f00b", size = 12164102, upload-time = "2025-12-15T05:02:33.611Z" },
    { url = "https://files.pythonhosted.org/packages/0c/5b/952928dd081bf88a83a5ccd49aaecfcd18fd0d2710c7ff07b8fb6f7032b9/mypy-1.19.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee4c11e460685c3e0c64a4c5de82ae143622410950d6be863303a1c4ba0e36d6", size = 12765799, upload-time = "2025-12-15T05:03:28.44Z" },
    { url = "https://files.pythonhosted.org/packages/2a/0d/93c2e4a287f74ef11a66fb6d49c7a9f05e47b0a4399040e6719b57f500d2/mypy-1.19.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:de759aafbae8763283b2ee5869c7255391fbc4de3ff171f8f030b5ec48381b74", size = 13522149, upload-time = "2025-12-15T05:02:36.011Z" },
    { url = "https://files.pythonhosted.org/packages/7b/0e/33a294b56aaad2b338d203e3a1d8b453637ac36cb278b45005e0901cf148/mypy-1.19.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ab43590f9cd5108f41aacf9fca31841142c786827a74ab7cc8a2eacb634e09a1", size = 13810105, upload-time = "2025-12-15T05:02:40.327Z" },
    { url = "https://files.pythonhosted.org/packages/0e/fd/3e82603a0cb66b67c5e7abababce6bf1a929ddf67bf445e652684af5c5a0/mypy-1.19.1-cp310-cp310-win_amd64.whl", hash = "sha256:2899753e2f61e571b3971747e302d5f420c3fd09650e1951e99f823bc3089dac", size = 10057200, upload-time = "2025-12-15T05:02:51.012Z" },
    { url = "https://files.pythonhosted.org/packages/ef/47/6b3ebabd5474d9cdc170d1342fbf9dddc1b0ec13ec90bf9004ee6f391c31/mypy-1.19.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d8dfc6ab58ca7dda47d9237349157500468e404b17213d44fc1cb77bce532288", size = 13028539, upload-time = "2025-12-15T05:03:44.129Z" },
    { url = "https://files.pythonhosted.org/packages/5c/a6/ac7c7a88a3c9c54334f53a941b765e6ec6c4ebd65d3fe8cdcfbe0d0fd7db/mypy-1.19.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:e3f276d8493c3c97930e354b2595a44a21348b320d859fb4a2b9f66da9ed27ab", size = 12083163, upload-time = "2025-12-15T05:03:37.679Z" },
    { url = "https://files.pythonhosted.org/packages/67/af/3afa9cf880aa4a2c803798ac24f1d11ef72a0c8079689fac5cfd815e2830/mypy-1.19.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2abb24cf3f17864770d18d673c85235ba52456b36a06b6afc1e07c1fdcd3d0e6", size = 12687629, upload-time = "2025-12-15T05:02:31.526Z" },
    { url = "https://files.pythonhosted.org/packages/2d/46/20f8a7114a56484ab268b0ab372461cb3a8f7deed31ea96b83a4e4cfcfca/mypy-1.19.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a009ffa5a621762d0c926a078c2d639104becab69e79538a494bcccb62cc0331", size = 13436933, upload-time = "2025-12-15T05:03:15.606Z" },
    { url = "https://files.pythonhosted.org/packages/5b/f8/33b291ea85050a21f15da910002460f1f445f8007adb29230f0adea279cb/mypy-1.19.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f7cee03c9a2e2ee26ec07479f38ea9c884e301d42c6d43a19d20fb014e3ba925", size = 13661754, upload-time = "2025-12-15T05:02:26.731Z" },
    { url = "https://files.pythonhosted.org/packages/fd/a3/47cbd4e85bec4335a9cd80cf67dbc02be21b5d4c9c23ad6b95d6c5196bac/mypy-1.19.1-cp311-cp311-win_amd64.whl", hash = "sha256:4b84a7a18f41e167f7995200a1d07a4a6810e89d29859df936f1c3923d263042", size = 10055772, upload-time = "2025-12-15T05:03:26.179Z" },
    { url = "https://files.pythonhosted.org/packages/06/8a/19bfae96f6615aa8a0604915512e0289b1fad33d5909bf7244f02935d33a/mypy-1.19.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:a8174a03289288c1f6c46d55cef02379b478bfbc8e358e02047487cad44c6ca1", size = 13206053, upload-time = "2025-12-15T05:03:46.622Z" },
    { url = "https://files.pythonhosted.org/packages/a5/34/3e63879ab041602154ba2a9f99817bb0c85c4df19a23a1443c8986e4d565/mypy-1.19.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ffcebe56eb09ff0c0885e750036a095e23793ba6c2e894e7e63f6d89ad51f22e", size = 12219134, upload-time = "2025-12-15T05:03:24.367Z" },
    { url = "https://files.pythonhosted.org/packages/89/cc/2db6f0e95366b630364e09845672dbee0cbf0bbe753a204b29a944967cd9/mypy-1.19.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b64d987153888790bcdb03a6473d321820597ab8dd9243b27a92153c4fa50fd2", size = 12731616, upload-time = "2025-12-15T05:02:44.725Z" },
    { url = "https://files.pythonhosted.org/packages/00/be/dd56c1fd4807bc1eba1cf18b2a850d0de7bacb55e158755eb79f77c41f8e/mypy-1.19.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c35d298c2c4bba75feb2195655dfea8124d855dfd7343bf8b8c055421eaf0cf8", size = 13620847, upload-time = "2025-12-15T05:03:39.633Z" },
    { url = "https://files.pythonhosted.org/packages/6d/42/332951aae42b79329f743bf1da088cd75d8d4d9acc18fbcbd84f26c1af4e/mypy-1.19.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:34c81968774648ab5ac09c29a375fdede03ba253f8f8287847bd480782f73a6a", size = 13834976, upload-time = "2025-12-15T05:03:08.786Z" },
    { url = "https://files.pythonhosted.org/packages/6f/63/e7493e5f90e1e085c562bb06e2eb32cae27c5057b9653348d38b47daaecc/mypy-1.19.1-cp312-cp312-win_amd64.whl", hash = "sha256:b10e7c2cd7870ba4ad9b2d8a6102eb5ffc1f16ca35e3de6bfa390c1113029d13", size = 10118104, upload-time = "2025-12-15T05:03:10.834Z" },
    { url = "https://files.pythonhosted.org/packages/de/9f/a6abae693f7a0c697dbb435aac52e958dc8da44e92e08ba88d2e42326176/mypy-1.19.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e3157c7594ff2ef1634ee058aafc56a82db665c9438fd41b390f3bde1ab12250", size = 13201927, upload-time = "2025-12-15T05:02:29.138Z" },
    { url = "https://files.pythonhosted.org/packages/9a/a4/45c35ccf6e1c65afc23a069f50e2c66f46bd3798cbe0d680c12d12935caa/mypy-1.19.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:bdb12f69bcc02700c2b47e070238f42cb87f18c0bc1fc4cdb4fb2bc5fd7a3b8b", size = 12206730, upload-time = "2025-12-15T05:03:01.325Z" },
    { url = "https://files.pythonhosted.org/packages/05/bb/cdcf89678e26b187650512620eec8368fded4cfd99cfcb431e4cdfd19dec/mypy-1.19.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f859fb09d9583a985be9a493d5cfc5515b56b08f7447759a0c5deaf68d80506e", size = 12724581, upload-time = "2025-12-15T05:03:20.087Z" },
    { url = "https://files.pythonhosted.org/packages/d1/32/dd260d52babf67bad8e6770f8e1102021877ce0edea106e72df5626bb0ec/mypy-1.19.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c9a6538e0415310aad77cb94004ca6482330fece18036b5f360b62c45814c4ef", size = 13616252, upload-time = "2025-12-15T05:02:49.036Z" },
    { url = "https://files.pythonhosted.org/packages/71/d0/5e60a9d2e3bd48432ae2b454b7ef2b62a960ab51292b1eda2a95edd78198/mypy-1.19.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:da4869fc5e7f62a88f3fe0b5c919d1d9f7ea3cef92d3689de2823fd27e40aa75", size = 13840848, upload-time = "2025-12-15T05:02:55.95Z" },
    { url = "https://files.pythonhosted.org/packages/98/76/d32051fa65ecf6cc8c6610956473abdc9b4c43301107476ac03559507843/mypy-1.19.1-cp313-cp313-win_amd64.whl", hash = "sha256:016f2246209095e8eda7538944daa1d60e1e8134d98983b9fc1e92c1fc0cb8dd", size = 10135510, upload-time = "2025-12-15T05:02:58.438Z" },
    { url = "https://files.pythonhosted.org/packages/de/eb/b83e75f4c820c4247a58580ef86fcd35165028f191e7e1ba57128c52782d/mypy-1.19.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:06e6170bd5836770e8104c8fdd58e5e725cfeb309f0a6c681a811f557e97eac1", size = 13199744, upload-time = "2025-12-15T05:03:30.823Z" },
    { url = "https://files.pythonhosted.org/packages/94/28/52785ab7bfa165f87fcbb61547a93f98bb20e7f82f90f165a1f69bce7b3d/mypy-1.19.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:804bd67b8054a85447c8954215a906d6eff9cabeabe493fb6334b24f4bfff718", size = 12215815, upload-time = "2025-12-15T05:02:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/0a/c6/bdd60774a0dbfb05122e3e925f2e9e846c009e479dcec4821dad881f5b52/mypy-1.19.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:21761006a7f497cb0d4de3d8ef4ca70532256688b0523eee02baf9eec895e27b", size = 12740047, upload-time = "2025-12-15T05:03:33.168Z" },
    { url = "https://files.pythonhosted.org/packages/32/2a/66ba933fe6c76bd40d1fe916a83f04fed253152f451a877520b3c4a5e41e/mypy-1.19.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:28902ee51f12e0f19e1e16fbe2f8f06b6637f482c459dd393efddd0ec7f82045", size = 13601998, upload-time = "2025-12-15T05:03:13.056Z" },
    { url = "https://files.pythonhosted.org/packages/e3/da/5055c63e377c5c2418760411fd6a63ee2b96cf95397259038756c042574f/mypy-1.19.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:481daf36a4c443332e2ae9c137dfee878fcea781a2e3f895d54bd3002a900957", size = 13807476, upload-time = "2025-12-15T05:03:17.977Z" },
    { url = "https://files.pythonhosted.org/packages/cd/09/4ebd873390a063176f06b0dbf1f7783dd87bd120eae7727fa4ae4179b685/mypy-1.19.1-cp314-cp314-win_amd64.whl", hash = "sha256:8bb5c6f6d043655e055be9b542aa5f3bdd30e4f3589163e85f93f3640060509f", size = 10281872, upload-time = "2025-12-15T05:03:05.549Z" },
    { url = "https://files.pythonhosted.org/packages/8d/f4/4ce9a05ce5ded1de3ec1c1d96cf9f9504a04e54ce0ed55cfa38619a32b8d/mypy-1.19.1-py3-none-any.whl", hash = "sha256:f1235f5ea01b7db5468d53ece6aaddf1ad0b88d9e7462b86ef96fe04995d7247", size = 2471239, upload-time = "2025-12-15T05:03:07.248Z" },
]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/6e/371856a3fb9d31ca8dac321cda606860fa4548858c0cc45d9d1d4ca2628b/mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558", size = 6343, upload-time = "2025-04-22T14:54:24.164Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/79/7b/2c79738432f5c924bef5071f933bcc9efd0473bac3b4aa584a6f7c1c8df8/mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505", size = 4963, upload-time = "2025-04-22T14:54:22.983Z" },
]

[[package]]
name = "notebooklm-cli"
version = "0.1.7"
source = { editable = "." }
dependencies = [
    { name = "httpx" },
    { name = "platformdirs" },
    { name = "pydantic" },
    { name = "rich" },
    { name = "typer" },
    { name = "websocket-client" },
]

[package.optional-dependencies]
dev = [
    { name = "mypy" },
    { name = "pytest" },
    { name = "pytest-asyncio" },
    { name = "ruff" },
]

[package.metadata]
requires-dist = [
    { name = "httpx", specifier = ">=0.25.0" },
    { name = "mypy", marker = "extra == 'dev'", specifier = ">=1.0.0" },
    { name = "platformdirs", specifier = ">=4.0.0" },
    { name = "pydantic", specifier = ">=2.0.0" },
    { name = "pytest", marker = "extra == 'dev'", specifier = ">=7.0.0" },
    { name = "pytest-asyncio", marker = "extra == 'dev'", specifier = ">=0.21.0" },
    { name = "rich", specifier = ">=13.0.0" },
    { name = "ruff", marker = "extra == 'dev'", specifier = ">=0.1.0" },
    { name = "typer", specifier = ">=0.9.0" },
    { name = "websocket-client", specifier = ">=1.6.0" },
]
provides-extras = ["dev"]

[[package]]
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
]

[[package]]
name = "pathspec"
version = "1.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/4c/b2/bb8e495d5262bfec41ab5cb18f522f1012933347fb5d9e62452d446baca2/pathspec-1.0.3.tar.gz", hash = "sha256:bac5cf97ae2c2876e2d25ebb15078eb04d76e4b98921ee31c6f85ade8b59444d", size = 130841, upload-time = "2026-01-09T15:46:46.009Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/32/2b/121e912bd60eebd623f873fd090de0e84f322972ab25a7f9044c056804ed/pathspec-1.0.3-py3-none-any.whl", hash = "sha256:e80767021c1cc524aa3fb14bedda9c34406591343cc42797b386ce7b9354fb6c", size = 55021, upload-time = "2026-01-09T15:46:44.652Z" },
]

[[package]]
name = "platformdirs"
version = "4.5.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cf/86/0248f086a84f01b37aaec0fa567b397df1a119f73c16f6c7a9aac73ea309/platformdirs-4.5.1.tar.gz", hash = "sha256:61d5cdcc6065745cdd94f0f878977f8de9437be93de97c1c12f853c9c0cdcbda", size = 21715, upload-time = "2025-12-05T13:52:58.638Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/28/3bfe2fa5a7b9c46fe7e13c97bda14c895fb10fa2ebf1d0abb90e0cea7ee1/platformdirs-4.5.1-py3-none-any.whl", hash = "sha256:d03afa3963c806a9bed9d5125c8f4cb2fdaf74a55ab60e5d59b3fde758104d31", size = 18731, upload-time = "2025-12-05T13:52:56.823Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/90/32c9941e728d564b411d574d8ee0cf09b12ec978cb22b294995bae5549a5/pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146", size = 2107298, upload-time = "2025-11-04T13:39:04.116Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a8/61c96a77fe28993d9a6fb0f4127e05430a267b235a124545d79fea46dd65/pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2", size = 1901475, upload-time = "2025-11-04T13:39:06.055Z" },
    { url = "https://files.pythonhosted.org/packages/5d/b6/338abf60225acc18cdc08b4faef592d0310923d19a87fba1faf05af5346e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97", size = 1918815, upload-time = "2025-11-04T13:39:10.41Z" },
    { url = "https://files.pythonhosted.org/packages/d1/1c/2ed0433e682983d8e8cba9c8d8ef274d4791ec6a6f24c58935b90e780e0a/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9", size = 2065567, upload-time = "2025-11-04T13:39:12.244Z" },
    { url = "https://files.pythonhosted.org/packages/b3/24/cf84974ee7d6eae06b9e63289b7b8f6549d416b5c199ca2d7ce13bbcf619/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52", size = 2230442, upload-time = "2025-11-04T13:39:13.962Z" },
    { url = "https://files.pythonhosted.org/packages/fd/21/4e287865504b3edc0136c89c9c09431be326168b1eb7841911cbc877a995/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941", size = 2350956, upload-time = "2025-11-04T13:39:15.889Z" },
    { url = "https://files.pythonhosted.org/packages/a8/76/7727ef2ffa4b62fcab916686a68a0426b9b790139720e1934e8ba797e238/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a", size = 2068253, upload-time = "2025-11-04T13:39:17.403Z" },
    { url = "https://files.pythonhosted.org/packages/d5/8c/a4abfc79604bcb4c748e18975c44f94f756f08fb04218d5cb87eb0d3a63e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c", size = 2177050, upload-time = "2025-11-04T13:39:19.351Z" },
    { url = "https://files.pythonhosted.org/packages/67/b1/de2e9a9a79b480f9cb0b6e8b6ba4c50b18d4e89852426364c66aa82bb7b3/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2", size = 2147178, upload-time = "2025-11-04T13:39:21Z" },
    { url = "https://files.pythonhosted.org/packages/16/c1/dfb33f837a47b20417500efaa0378adc6635b3c79e8369ff7a03c494b4ac/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556", size = 2341833, upload-time = "2025-11-04T13:39:22.606Z" },
    { url = "https://files.pythonhosted.org/packages/47/36/00f398642a0f4b815a9a558c4f1dca1b4020a7d49562807d7bc9ff279a6c/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49", size = 2321156, upload-time = "2025-11-04T13:39:25.843Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/cad3acd89fde2010807354d978725ae111ddf6d0ea46d1ea1775b5c1bd0c/pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba", size = 1989378, upload-time = "2025-11-04T13:39:27.92Z" },
    { url = "https://files.pythonhosted.org/packages/76/92/d338652464c6c367e5608e4488201702cd1cbb0f33f7b6a85a60fe5f3720/pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9", size = 2013622, upload-time = "2025-11-04T13:39:29.848Z" },
    { url = "https://files.pythonhosted.org/packages/e8/72/74a989dd9f2084b3d9530b0915fdda64ac48831c30dbf7c72a41a5232db8/pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6", size = 2105873, upload-time = "2025-11-04T13:39:31.373Z" },
    { url = "https://files.pythonhosted.org/packages/12/44/37e403fd9455708b3b942949e1d7febc02167662bf1a7da5b78ee1ea2842/pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b", size = 1899826, upload-time = "2025-11-04T13:39:32.897Z" },
    { url = "https://files.pythonhosted.org/packages/33/7f/1d5cab3ccf44c1935a359d51a8a2a9e1a654b744b5e7f80d41b88d501eec/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a", size = 1917869, upload-time = "2025-11-04T13:39:34.469Z" },
    { url = "https://files.pythonhosted.org/packages/6e/6a/30d94a9674a7fe4f4744052ed6c5e083424510be1e93da5bc47569d11810/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8", size = 2063890, upload-time = "2025-11-04T13:39:36.053Z" },
    { url = "https://files.pythonhosted.org/packages/50/be/76e5d46203fcb2750e542f32e6c371ffa9b8ad17364cf94bb0818dbfb50c/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e", size = 2229740, upload-time = "2025-11-04T13:39:37.753Z" },
    { url = "https://files.pythonhosted.org/packages/d3/ee/fed784df0144793489f87db310a6bbf8118d7b630ed07aa180d6067e653a/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1", size = 2350021, upload-time = "2025-11-04T13:39:40.94Z" },
    { url = "https://files.pythonhosted.org/packages/c8/be/8fed28dd0a180dca19e72c233cbf58efa36df055e5b9d90d64fd1740b828/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b", size = 2066378, upload-time = "2025-11-04T13:39:42.523Z" },
    { url = "https://files.pythonhosted.org/packages/b0/3b/698cf8ae1d536a010e05121b4958b1257f0b5522085e335360e53a6b1c8b/pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b", size = 2175761, upload-time = "2025-11-04T13:39:44.553Z" },
    { url = "https://files.pythonhosted.org/packages/b8/ba/15d537423939553116dea94ce02f9c31be0fa9d0b806d427e0308ec17145/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284", size = 2146303, upload-time = "2025-11-04T13:39:46.238Z" },
    { url = "https://files.pythonhosted.org/packages/58/7f/0de669bf37d206723795f9c90c82966726a2ab06c336deba4735b55af431/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594", size = 2340355, upload-time = "2025-11-04T13:39:48.002Z" },
    { url = "https://files.pythonhosted.org/packages/e5/de/e7482c435b83d7e3c3ee5ee4451f6e8973cff0eb6007d2872ce6383f6398/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e", size = 2319875, upload-time = "2025-11-04T13:39:49.705Z" },
    { url = "https://files.pythonhosted.org/packages/fe/e6/8c9e81bb6dd7560e33b9053351c29f30c8194b72f2d6932888581f503482/pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b", size = 1987549, upload-time = "2025-11-04T13:39:51.842Z" },
    { url = "https://files.pythonhosted.org/packages/11/66/f14d1d978ea94d1bc21fc98fcf570f9542fe55bfcc40269d4e1a21c19bf7/pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe", size = 2011305, upload-time = "2025-11-04T13:39:53.485Z" },
    { url = "https://files.pythonhosted.org/packages/56/d8/0e271434e8efd03186c5386671328154ee349ff0354d83c74f5caaf096ed/pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f", size = 1972902, upload-time = "2025-11-04T13:39:56.488Z" },
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/11/72/90fda5ee3b97e51c494938a4a44c3a35a9c96c19bba12372fb9c634d6f57/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034", size = 2115441, upload-time = "2025-11-04T13:42:39.557Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/8942f884fa33f50794f119012dc6a1a02ac43a56407adaac20463df8e98f/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c", size = 1930291, upload-time = "2025-11-04T13:42:42.169Z" },
    { url = "https://files.pythonhosted.org/packages/79/c8/ecb9ed9cd942bce09fc888ee960b52654fbdbede4ba6c2d6e0d3b1d8b49c/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2", size = 1948632, upload-time = "2025-11-04T13:42:44.564Z" },
    { url = "https://files.pythonhosted.org/packages/2e/1b/687711069de7efa6af934e74f601e2a4307365e8fdc404703afc453eab26/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad", size = 2138905, upload-time = "2025-11-04T13:42:47.156Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b0/1a2aa41e3b5a4ba11420aba2d091b2d17959c8d1519ece3627c371951e73/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8", size = 2103351, upload-time = "2025-11-04T13:43:02.058Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ee/31b1f0020baaf6d091c87900ae05c6aeae101fa4e188e1613c80e4f1ea31/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a", size = 1925363, upload-time = "2025-11-04T13:43:05.159Z" },
    { url = "https://files.pythonhosted.org/packages/e1/89/ab8e86208467e467a80deaca4e434adac37b10a9d134cd2f99b28a01e483/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b", size = 2135615, upload-time = "2025-11-04T13:43:08.116Z" },
    { url = "https://files.pythonhosted.org/packages/99/0a/99a53d06dd0348b2008f2f30884b34719c323f16c3be4e6cc1203b74a91d/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2", size = 2175369, upload-time = "2025-11-04T13:43:12.49Z" },
    { url = "https://files.pythonhosted.org/packages/6d/94/30ca3b73c6d485b9bb0bc66e611cff4a7138ff9736b7e66bcf0852151636/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093", size = 2144218, upload-time = "2025-11-04T13:43:15.431Z" },
    { url = "https://files.pythonhosted.org/packages/87/57/31b4f8e12680b739a91f472b5671294236b82586889ef764b5fbc6669238/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a", size = 2329951, upload-time = "2025-11-04T13:43:18.062Z" },
    { url = "https://files.pythonhosted.org/packages/7d/73/3c2c8edef77b8f7310e6fb012dbc4b8551386ed575b9eb6fb2506e28a7eb/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963", size = 2318428, upload-time = "2025-11-04T13:43:20.679Z" },
    { url = "https://files.pythonhosted.org/packages/2f/02/8559b1f26ee0d502c74f9cca5c0d2fd97e967e083e006bbbb4e97f3a043a/pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a", size = 2147009, upload-time = "2025-11-04T13:43:23.286Z" },
    { url = "https://files.pythonhosted.org/packages/5f/9b/1b3f0e9f9305839d7e84912f9e8bfbd191ed1b1ef48083609f0dabde978c/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26", size = 2101980, upload-time = "2025-11-04T13:43:25.97Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ed/d71fefcb4263df0da6a85b5d8a7508360f2f2e9b3bf5814be9c8bccdccc1/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808", size = 1923865, upload-time = "2025-11-04T13:43:28.763Z" },
    { url = "https://files.pythonhosted.org/packages/ce/3a/626b38db460d675f873e4444b4bb030453bbe7b4ba55df821d026a0493c4/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc", size = 2134256, upload-time = "2025-11-04T13:43:31.71Z" },
    { url = "https://files.pythonhosted.org/packages/83/d9/8412d7f06f616bbc053d30cb4e5f76786af3221462ad5eee1f202021eb4e/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1", size = 2174762, upload-time = "2025-11-04T13:43:34.744Z" },
    { url = "https://files.pythonhosted.org/packages/55/4c/162d906b8e3ba3a99354e20faa1b49a85206c47de97a639510a0e673f5da/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84", size = 2143141, upload-time = "2025-11-04T13:43:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f2/f11dd73284122713f5f89fc940f370d035fa8e1e078d446b3313955157fe/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770", size = 2330317, upload-time = "2025-11-04T13:43:40.406Z" },
    { url = "https://files.pythonhosted.org/packages/88/9d/b06ca6acfe4abb296110fb1273a4d848a0bfb2ff65f3ee92127b3244e16b/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f", size = 2316992, upload-time = "2025-11-04T13:43:43.602Z" },
    { url = "https://files.pythonhosted.org/packages/36/c7/cfc8e811f061c841d7990b0201912c3556bfeb99cdcb7ed24adc8d6f8704/pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51", size = 2145302, upload-time = "2025-11-04T13:43:46.64Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pytest"
version = "9.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d1/db/7ef3487e0fb0049ddb5ce41d3a49c235bf9ad299b6a25d5780a89f19230f/pytest-9.0.2.tar.gz", hash = "sha256:75186651a92bd89611d1d9fc20f0b4345fd827c41ccd5c299a868a05d70edf11", size = 1568901, upload-time = "2025-12-06T21:30:51.014Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3b/ab/b3226f0bd7cdcf710fbede2b3548584366da3b19b5021e74f5bde2a8fa3f/pytest-9.0.2-py3-none-any.whl", hash = "sha256:711ffd45bf766d5264d487b917733b453d917afd2b0ad65223959f59089f875b", size = 374801, upload-time = "2025-12-06T21:30:49.154Z" },
]

[[package]]
name = "pytest-asyncio"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "backports-asyncio-runner", marker = "python_full_version < '3.11'" },
    { name = "pytest" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/90/2c/8af215c0f776415f3590cac4f9086ccefd6fd463befeae41cd4d3f193e5a/pytest_asyncio-1.3.0.tar.gz", hash = "sha256:d7f52f36d231b80ee124cd216ffb19369aa168fc10095013c6b014a34d3ee9e5", size = 50087, upload-time = "2025-11-10T16:07:47.256Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e5/35/f8b19922b6a25bc0880171a2f1a003eaeb93657475193ab516fd87cac9da/pytest_asyncio-1.3.0-py3-none-any.whl", hash = "sha256:611e26147c7f77640e6d0a92a38ed17c3e9848063698d5c93d5aa7aa11cebff5", size = 15075, upload-time = "2025-11-10T16:07:45.537Z" },
]

[[package]]
name = "rich"
version = "14.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fb/d2/8920e102050a0de7bfabeb4c4614a49248cf8d5d7a8d01885fbb24dc767a/rich-14.2.0.tar.gz", hash = "sha256:73ff50c7c0c1c77c8243079283f4edb376f0f6442433aecb8ce7e6d0b92d1fe4", size = 219990, upload-time = "2025-10-09T14:16:53.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/25/7a/b0178788f8dc6cafce37a212c99565fa1fe7872c70c6c9c1e1a372d9d88f/rich-14.2.0-py3-none-any.whl", hash = "sha256:76bc51fe2e57d2b1be1f96c524b890b816e334ab4c1e45888799bfaab0021edd", size = 243393, upload-time = "2025-10-09T14:16:51.245Z" },
]

[[package]]
name = "ruff"
version = "0.14.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d4/77/9a7fe084d268f8855d493e5031ea03fa0af8cc05887f638bf1c4e3363eb8/ruff-0.14.11.tar.gz", hash = "sha256:f6dc463bfa5c07a59b1ff2c3b9767373e541346ea105503b4c0369c520a66958", size = 5993417, upload-time = "2026-01-08T19:11:58.322Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f0/a6/a4c40a5aaa7e331f245d2dc1ac8ece306681f52b636b40ef87c88b9f7afd/ruff-0.14.11-py3-none-linux_armv6l.whl", hash = "sha256:f6ff2d95cbd335841a7217bdfd9c1d2e44eac2c584197ab1385579d55ff8830e", size = 12951208, upload-time = "2026-01-08T19:12:09.218Z" },
    { url = "https://files.pythonhosted.org/packages/5c/5c/360a35cb7204b328b685d3129c08aca24765ff92b5a7efedbdd6c150d555/ruff-0.14.11-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:6f6eb5c1c8033680f4172ea9c8d3706c156223010b8b97b05e82c59bdc774ee6", size = 13330075, upload-time = "2026-01-08T19:12:02.549Z" },
    { url = "https://files.pythonhosted.org/packages/1b/9e/0cc2f1be7a7d33cae541824cf3f95b4ff40d03557b575912b5b70273c9ec/ruff-0.14.11-py3-none-macosx_11_0_arm64.whl", hash = "sha256:f2fc34cc896f90080fca01259f96c566f74069a04b25b6205d55379d12a6855e", size = 12257809, upload-time = "2026-01-08T19:12:00.366Z" },
    { url = "https://files.pythonhosted.org/packages/a7/e5/5faab97c15bb75228d9f74637e775d26ac703cc2b4898564c01ab3637c02/ruff-0.14.11-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:53386375001773ae812b43205d6064dae49ff0968774e6befe16a994fc233caa", size = 12678447, upload-time = "2026-01-08T19:12:13.899Z" },
    { url = "https://files.pythonhosted.org/packages/1b/33/e9767f60a2bef779fb5855cab0af76c488e0ce90f7bb7b8a45c8a2ba4178/ruff-0.14.11-py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:a697737dce1ca97a0a55b5ff0434ee7205943d4874d638fe3ae66166ff46edbe", size = 12758560, upload-time = "2026-01-08T19:11:42.55Z" },
    { url = "https://files.pythonhosted.org/packages/eb/84/4c6cf627a21462bb5102f7be2a320b084228ff26e105510cd2255ea868e5/ruff-0.14.11-py3-none-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6845ca1da8ab81ab1dce755a32ad13f1db72e7fba27c486d5d90d65e04d17b8f", size = 13599296, upload-time = "2026-01-08T19:11:30.371Z" },
    { url = "https://files.pythonhosted.org/packages/88/e1/92b5ed7ea66d849f6157e695dc23d5d6d982bd6aa8d077895652c38a7cae/ruff-0.14.11-py3-none-manylinux_2_17_ppc64.manylinux2014_ppc64.whl", hash = "sha256:e36ce2fd31b54065ec6f76cb08d60159e1b32bdf08507862e32f47e6dde8bcbf", size = 15048981, upload-time = "2026-01-08T19:12:04.742Z" },
    { url = "https://files.pythonhosted.org/packages/61/df/c1bd30992615ac17c2fb64b8a7376ca22c04a70555b5d05b8f717163cf9f/ruff-0.14.11-py3-none-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:590bcc0e2097ecf74e62a5c10a6b71f008ad82eb97b0a0079e85defe19fe74d9", size = 14633183, upload-time = "2026-01-08T19:11:40.069Z" },
    { url = "https://files.pythonhosted.org/packages/04/e9/fe552902f25013dd28a5428a42347d9ad20c4b534834a325a28305747d64/ruff-0.14.11-py3-none-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:53fe71125fc158210d57fe4da26e622c9c294022988d08d9347ec1cf782adafe", size = 14050453, upload-time = "2026-01-08T19:11:37.555Z" },
    { url = "https://files.pythonhosted.org/packages/ae/93/f36d89fa021543187f98991609ce6e47e24f35f008dfe1af01379d248a41/ruff-0.14.11-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a35c9da08562f1598ded8470fcfef2afb5cf881996e6c0a502ceb61f4bc9c8a3", size = 13757889, upload-time = "2026-01-08T19:12:07.094Z" },
    { url = "https://files.pythonhosted.org/packages/b7/9f/c7fb6ecf554f28709a6a1f2a7f74750d400979e8cd47ed29feeaa1bd4db8/ruff-0.14.11-py3-none-manylinux_2_31_riscv64.whl", hash = "sha256:0f3727189a52179393ecf92ec7057c2210203e6af2676f08d92140d3e1ee72c1", size = 13955832, upload-time = "2026-01-08T19:11:55.064Z" },
    { url = "https://files.pythonhosted.org/packages/db/a0/153315310f250f76900a98278cf878c64dfb6d044e184491dd3289796734/ruff-0.14.11-py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:eb09f849bd37147a789b85995ff734a6c4a095bed5fd1608c4f56afc3634cde2", size = 12586522, upload-time = "2026-01-08T19:11:35.356Z" },
    { url = "https://files.pythonhosted.org/packages/2f/2b/a73a2b6e6d2df1d74bf2b78098be1572191e54bec0e59e29382d13c3adc5/ruff-0.14.11-py3-none-musllinux_1_2_armv7l.whl", hash = "sha256:c61782543c1231bf71041461c1f28c64b961d457d0f238ac388e2ab173d7ecb7", size = 12724637, upload-time = "2026-01-08T19:11:47.796Z" },
    { url = "https://files.pythonhosted.org/packages/f0/41/09100590320394401cd3c48fc718a8ba71c7ddb1ffd07e0ad6576b3a3df2/ruff-0.14.11-py3-none-musllinux_1_2_i686.whl", hash = "sha256:82ff352ea68fb6766140381748e1f67f83c39860b6446966cff48a315c3e2491", size = 13145837, upload-time = "2026-01-08T19:11:32.87Z" },
    { url = "https://files.pythonhosted.org/packages/3b/d8/e035db859d1d3edf909381eb8ff3e89a672d6572e9454093538fe6f164b0/ruff-0.14.11-py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:728e56879df4ca5b62a9dde2dd0eb0edda2a55160c0ea28c4025f18c03f86984", size = 13850469, upload-time = "2026-01-08T19:12:11.694Z" },
    { url = "https://files.pythonhosted.org/packages/4e/02/bb3ff8b6e6d02ce9e3740f4c17dfbbfb55f34c789c139e9cd91985f356c7/ruff-0.14.11-py3-none-win32.whl", hash = "sha256:337c5dd11f16ee52ae217757d9b82a26400be7efac883e9e852646f1557ed841", size = 12851094, upload-time = "2026-01-08T19:11:45.163Z" },
    { url = "https://files.pythonhosted.org/packages/58/f1/90ddc533918d3a2ad628bc3044cdfc094949e6d4b929220c3f0eb8a1c998/ruff-0.14.11-py3-none-win_amd64.whl", hash = "sha256:f981cea63d08456b2c070e64b79cb62f951aa1305282974d4d5216e6e0178ae6", size = 14001379, upload-time = "2026-01-08T19:11:52.591Z" },
    { url = "https://files.pythonhosted.org/packages/c4/1c/1dbe51782c0e1e9cfce1d1004752672d2d4629ea46945d19d731ad772b3b/ruff-0.14.11-py3-none-win_arm64.whl", hash = "sha256:649fb6c9edd7f751db276ef42df1f3df41c38d67d199570ae2a7bd6cbc3590f0", size = 12938644, upload-time = "2026-01-08T19:11:50.027Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "tomli"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/52/ed/3f73f72945444548f33eba9a87fc7a6e969915e7b1acc8260b30e1f76a2f/tomli-2.3.0.tar.gz", hash = "sha256:64be704a875d2a59753d80ee8a533c3fe183e3f06807ff7dc2232938ccb01549", size = 17392, upload-time = "2025-10-08T22:01:47.119Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/2e/299f62b401438d5fe1624119c723f5d877acc86a4c2492da405626665f12/tomli-2.3.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:88bd15eb972f3664f5ed4b57c1634a97153b4bac4479dcb6a495f41921eb7f45", size = 153236, upload-time = "2025-10-08T22:01:00.137Z" },
    { url = "https://files.pythonhosted.org/packages/86/7f/d8fffe6a7aefdb61bced88fcb5e280cfd71e08939da5894161bd71bea022/tomli-2.3.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:883b1c0d6398a6a9d29b508c331fa56adbcdff647f6ace4dfca0f50e90dfd0ba", size = 148084, upload-time = "2025-10-08T22:01:01.63Z" },
    { url = "https://files.pythonhosted.org/packages/47/5c/24935fb6a2ee63e86d80e4d3b58b222dafaf438c416752c8b58537c8b89a/tomli-2.3.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d1381caf13ab9f300e30dd8feadb3de072aeb86f1d34a8569453ff32a7dea4bf", size = 234832, upload-time = "2025-10-08T22:01:02.543Z" },
    { url = "https://files.pythonhosted.org/packages/89/da/75dfd804fc11e6612846758a23f13271b76d577e299592b4371a4ca4cd09/tomli-2.3.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a0e285d2649b78c0d9027570d4da3425bdb49830a6156121360b3f8511ea3441", size = 242052, upload-time = "2025-10-08T22:01:03.836Z" },
    { url = "https://files.pythonhosted.org/packages/70/8c/f48ac899f7b3ca7eb13af73bacbc93aec37f9c954df3c08ad96991c8c373/tomli-2.3.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0a154a9ae14bfcf5d8917a59b51ffd5a3ac1fd149b71b47a3a104ca4edcfa845", size = 239555, upload-time = "2025-10-08T22:01:04.834Z" },
    { url = "https://files.pythonhosted.org/packages/ba/28/72f8afd73f1d0e7829bfc093f4cb98ce0a40ffc0cc997009ee1ed94ba705/tomli-2.3.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:74bf8464ff93e413514fefd2be591c3b0b23231a77f901db1eb30d6f712fc42c", size = 245128, upload-time = "2025-10-08T22:01:05.84Z" },
    { url = "https://files.pythonhosted.org/packages/b6/eb/a7679c8ac85208706d27436e8d421dfa39d4c914dcf5fa8083a9305f58d9/tomli-2.3.0-cp311-cp311-win32.whl", hash = "sha256:00b5f5d95bbfc7d12f91ad8c593a1659b6387b43f054104cda404be6bda62456", size = 96445, upload-time = "2025-10-08T22:01:06.896Z" },
    { url = "https://files.pythonhosted.org/packages/0a/fe/3d3420c4cb1ad9cb462fb52967080575f15898da97e21cb6f1361d505383/tomli-2.3.0-cp311-cp311-win_amd64.whl", hash = "sha256:4dc4ce8483a5d429ab602f111a93a6ab1ed425eae3122032db7e9acf449451be", size = 107165, upload-time = "2025-10-08T22:01:08.107Z" },
    { url = "https://files.pythonhosted.org/packages/ff/b7/40f36368fcabc518bb11c8f06379a0fd631985046c038aca08c6d6a43c6e/tomli-2.3.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d7d86942e56ded512a594786a5ba0a5e521d02529b3826e7761a05138341a2ac", size = 154891, upload-time = "2025-10-08T22:01:09.082Z" },
    { url = "https://files.pythonhosted.org/packages/f9/3f/d9dd692199e3b3aab2e4e4dd948abd0f790d9ded8cd10cbaae276a898434/tomli-2.3.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:73ee0b47d4dad1c5e996e3cd33b8a76a50167ae5f96a2607cbe8cc773506ab22", size = 148796, upload-time = "2025-10-08T22:01:10.266Z" },
    { url = "https://files.pythonhosted.org/packages/60/83/59bff4996c2cf9f9387a0f5a3394629c7efa5ef16142076a23a90f1955fa/tomli-2.3.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:792262b94d5d0a466afb5bc63c7daa9d75520110971ee269152083270998316f", size = 242121, upload-time = "2025-10-08T22:01:11.332Z" },
    { url = "https://files.pythonhosted.org/packages/45/e5/7c5119ff39de8693d6baab6c0b6dcb556d192c165596e9fc231ea1052041/tomli-2.3.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4f195fe57ecceac95a66a75ac24d9d5fbc98ef0962e09b2eddec5d39375aae52", size = 250070, upload-time = "2025-10-08T22:01:12.498Z" },
    { url = "https://files.pythonhosted.org/packages/45/12/ad5126d3a278f27e6701abde51d342aa78d06e27ce2bb596a01f7709a5a2/tomli-2.3.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:e31d432427dcbf4d86958c184b9bfd1e96b5b71f8eb17e6d02531f434fd335b8", size = 245859, upload-time = "2025-10-08T22:01:13.551Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a1/4d6865da6a71c603cfe6ad0e6556c73c76548557a8d658f9e3b142df245f/tomli-2.3.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b0882799624980785240ab732537fcfc372601015c00f7fc367c55308c186f6", size = 250296, upload-time = "2025-10-08T22:01:14.614Z" },
    { url = "https://files.pythonhosted.org/packages/a0/b7/a7a7042715d55c9ba6e8b196d65d2cb662578b4d8cd17d882d45322b0d78/tomli-2.3.0-cp312-cp312-win32.whl", hash = "sha256:ff72b71b5d10d22ecb084d345fc26f42b5143c5533db5e2eaba7d2d335358876", size = 97124, upload-time = "2025-10-08T22:01:15.629Z" },
    { url = "https://files.pythonhosted.org/packages/06/1e/f22f100db15a68b520664eb3328fb0ae4e90530887928558112c8d1f4515/tomli-2.3.0-cp312-cp312-win_amd64.whl", hash = "sha256:1cb4ed918939151a03f33d4242ccd0aa5f11b3547d0cf30f7c74a408a5b99878", size = 107698, upload-time = "2025-10-08T22:01:16.51Z" },
    { url = "https://files.pythonhosted.org/packages/89/48/06ee6eabe4fdd9ecd48bf488f4ac783844fd777f547b8d1b61c11939974e/tomli-2.3.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5192f562738228945d7b13d4930baffda67b69425a7f0da96d360b0a3888136b", size = 154819, upload-time = "2025-10-08T22:01:17.964Z" },
    { url = "https://files.pythonhosted.org/packages/f1/01/88793757d54d8937015c75dcdfb673c65471945f6be98e6a0410fba167ed/tomli-2.3.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:be71c93a63d738597996be9528f4abe628d1adf5e6eb11607bc8fe1a510b5dae", size = 148766, upload-time = "2025-10-08T22:01:18.959Z" },
    { url = "https://files.pythonhosted.org/packages/42/17/5e2c956f0144b812e7e107f94f1cc54af734eb17b5191c0bbfb72de5e93e/tomli-2.3.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c4665508bcbac83a31ff8ab08f424b665200c0e1e645d2bd9ab3d3e557b6185b", size = 240771, upload-time = "2025-10-08T22:01:20.106Z" },
    { url = "https://files.pythonhosted.org/packages/d5/f4/0fbd014909748706c01d16824eadb0307115f9562a15cbb012cd9b3512c5/tomli-2.3.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4021923f97266babc6ccab9f5068642a0095faa0a51a246a6a02fccbb3514eaf", size = 248586, upload-time = "2025-10-08T22:01:21.164Z" },
    { url = "https://files.pythonhosted.org/packages/30/77/fed85e114bde5e81ecf9bc5da0cc69f2914b38f4708c80ae67d0c10180c5/tomli-2.3.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4ea38c40145a357d513bffad0ed869f13c1773716cf71ccaa83b0fa0cc4e42f", size = 244792, upload-time = "2025-10-08T22:01:22.417Z" },
    { url = "https://files.pythonhosted.org/packages/55/92/afed3d497f7c186dc71e6ee6d4fcb0acfa5f7d0a1a2878f8beae379ae0cc/tomli-2.3.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ad805ea85eda330dbad64c7ea7a4556259665bdf9d2672f5dccc740eb9d3ca05", size = 248909, upload-time = "2025-10-08T22:01:23.859Z" },
    { url = "https://files.pythonhosted.org/packages/f8/84/ef50c51b5a9472e7265ce1ffc7f24cd4023d289e109f669bdb1553f6a7c2/tomli-2.3.0-cp313-cp313-win32.whl", hash = "sha256:97d5eec30149fd3294270e889b4234023f2c69747e555a27bd708828353ab606", size = 96946, upload-time = "2025-10-08T22:01:24.893Z" },
    { url = "https://files.pythonhosted.org/packages/b2/b7/718cd1da0884f281f95ccfa3a6cc572d30053cba64603f79d431d3c9b61b/tomli-2.3.0-cp313-cp313-win_amd64.whl", hash = "sha256:0c95ca56fbe89e065c6ead5b593ee64b84a26fca063b5d71a1122bf26e533999", size = 107705, upload-time = "2025-10-08T22:01:26.153Z" },
    { url = "https://files.pythonhosted.org/packages/19/94/aeafa14a52e16163008060506fcb6aa1949d13548d13752171a755c65611/tomli-2.3.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:cebc6fe843e0733ee827a282aca4999b596241195f43b4cc371d64fc6639da9e", size = 154244, upload-time = "2025-10-08T22:01:27.06Z" },
    { url = "https://files.pythonhosted.org/packages/db/e4/1e58409aa78eefa47ccd19779fc6f36787edbe7d4cd330eeeedb33a4515b/tomli-2.3.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4c2ef0244c75aba9355561272009d934953817c49f47d768070c3c94355c2aa3", size = 148637, upload-time = "2025-10-08T22:01:28.059Z" },
    { url = "https://files.pythonhosted.org/packages/26/b6/d1eccb62f665e44359226811064596dd6a366ea1f985839c566cd61525ae/tomli-2.3.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c22a8bf253bacc0cf11f35ad9808b6cb75ada2631c2d97c971122583b129afbc", size = 241925, upload-time = "2025-10-08T22:01:29.066Z" },
    { url = "https://files.pythonhosted.org/packages/70/91/7cdab9a03e6d3d2bb11beae108da5bdc1c34bdeb06e21163482544ddcc90/tomli-2.3.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0eea8cc5c5e9f89c9b90c4896a8deefc74f518db5927d0e0e8d4a80953d774d0", size = 249045, upload-time = "2025-10-08T22:01:31.98Z" },
    { url = "https://files.pythonhosted.org/packages/15/1b/8c26874ed1f6e4f1fcfeb868db8a794cbe9f227299402db58cfcc858766c/tomli-2.3.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b74a0e59ec5d15127acdabd75ea17726ac4c5178ae51b85bfe39c4f8a278e879", size = 245835, upload-time = "2025-10-08T22:01:32.989Z" },
    { url = "https://files.pythonhosted.org/packages/fd/42/8e3c6a9a4b1a1360c1a2a39f0b972cef2cc9ebd56025168c4137192a9321/tomli-2.3.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b5870b50c9db823c595983571d1296a6ff3e1b88f734a4c8f6fc6188397de005", size = 253109, upload-time = "2025-10-08T22:01:34.052Z" },
    { url = "https://files.pythonhosted.org/packages/22/0c/b4da635000a71b5f80130937eeac12e686eefb376b8dee113b4a582bba42/tomli-2.3.0-cp314-cp314-win32.whl", hash = "sha256:feb0dacc61170ed7ab602d3d972a58f14ee3ee60494292d384649a3dc38ef463", size = 97930, upload-time = "2025-10-08T22:01:35.082Z" },
    { url = "https://files.pythonhosted.org/packages/b9/74/cb1abc870a418ae99cd5c9547d6bce30701a954e0e721821df483ef7223c/tomli-2.3.0-cp314-cp314-win_amd64.whl", hash = "sha256:b273fcbd7fc64dc3600c098e39136522650c49bca95df2d11cf3b626422392c8", size = 107964, upload-time = "2025-10-08T22:01:36.057Z" },
    { url = "https://files.pythonhosted.org/packages/54/78/5c46fff6432a712af9f792944f4fcd7067d8823157949f4e40c56b8b3c83/tomli-2.3.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:940d56ee0410fa17ee1f12b817b37a4d4e4dc4d27340863cc67236c74f582e77", size = 163065, upload-time = "2025-10-08T22:01:37.27Z" },
    { url = "https://files.pythonhosted.org/packages/39/67/f85d9bd23182f45eca8939cd2bc7050e1f90c41f4a2ecbbd5963a1d1c486/tomli-2.3.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:f85209946d1fe94416debbb88d00eb92ce9cd5266775424ff81bc959e001acaf", size = 159088, upload-time = "2025-10-08T22:01:38.235Z" },
    { url = "https://files.pythonhosted.org/packages/26/5a/4b546a0405b9cc0659b399f12b6adb750757baf04250b148d3c5059fc4eb/tomli-2.3.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a56212bdcce682e56b0aaf79e869ba5d15a6163f88d5451cbde388d48b13f530", size = 268193, upload-time = "2025-10-08T22:01:39.712Z" },
    { url = "https://files.pythonhosted.org/packages/42/4f/2c12a72ae22cf7b59a7fe75b3465b7aba40ea9145d026ba41cb382075b0e/tomli-2.3.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c5f3ffd1e098dfc032d4d3af5c0ac64f6d286d98bc148698356847b80fa4de1b", size = 275488, upload-time = "2025-10-08T22:01:40.773Z" },
    { url = "https://files.pythonhosted.org/packages/92/04/a038d65dbe160c3aa5a624e93ad98111090f6804027d474ba9c37c8ae186/tomli-2.3.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5e01decd096b1530d97d5d85cb4dff4af2d8347bd35686654a004f8dea20fc67", size = 272669, upload-time = "2025-10-08T22:01:41.824Z" },
    { url = "https://files.pythonhosted.org/packages/be/2f/8b7c60a9d1612a7cbc39ffcca4f21a73bf368a80fc25bccf8253e2563267/tomli-2.3.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:8a35dd0e643bb2610f156cca8db95d213a90015c11fee76c946aa62b7ae7e02f", size = 279709, upload-time = "2025-10-08T22:01:43.177Z" },
    { url = "https://files.pythonhosted.org/packages/7e/46/cc36c679f09f27ded940281c38607716c86cf8ba4a518d524e349c8b4874/tomli-2.3.0-cp314-cp314t-win32.whl", hash = "sha256:a1f7f282fe248311650081faafa5f4732bdbfef5d45fe3f2e702fbc6f2d496e0", size = 107563, upload-time = "2025-10-08T22:01:44.233Z" },
    { url = "https://files.pythonhosted.org/packages/84/ff/426ca8683cf7b753614480484f6437f568fd2fda2edbdf57a2d3d8b27a0b/tomli-2.3.0-cp314-cp314t-win_amd64.whl", hash = "sha256:70a251f8d4ba2d9ac2542eecf008b3c8a9fc5c3f9f02c56a9d7952612be2fdba", size = 119756, upload-time = "2025-10-08T22:01:45.234Z" },
    { url = "https://files.pythonhosted.org/packages/77/b8/0135fadc89e73be292b473cb820b4f5a08197779206b33191e801feeae40/tomli-2.3.0-py3-none-any.whl", hash = "sha256:e95b1af3c5b07d9e643909b5abbec77cd9f1217e6d0bca72b0234736b9fb1f1b", size = 14408, upload-time = "2025-10-08T22:01:46.04Z" },
]

[[package]]
name = "typer"
version = "0.21.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/36/bf/8825b5929afd84d0dabd606c67cd57b8388cb3ec385f7ef19c5cc2202069/typer-0.21.1.tar.gz", hash = "sha256:ea835607cd752343b6b2b7ce676893e5a0324082268b48f27aa058bdb7d2145d", size = 110371, upload-time = "2026-01-06T11:21:10.989Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/1d/d9257dd49ff2ca23ea5f132edf1281a0c4f9de8a762b9ae399b670a59235/typer-0.21.1-py3-none-any.whl", hash = "sha256:7985e89081c636b88d172c2ee0cfe33c253160994d47bdfdc302defd7d1f1d01", size = 47381, upload-time = "2026-01-06T11:21:09.824Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "websocket-client"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2c/41/aa4bf9664e4cda14c3b39865b12251e8e7d239f4cd0e3cc1b6c2ccde25c1/websocket_client-1.9.0.tar.gz", hash = "sha256:9e813624b6eb619999a97dc7958469217c3176312b3a16a4bd1bc7e08a46ec98", size = 70576, upload-time = "2025-10-07T21:16:36.495Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/34/db/b10e48aa8fff7407e67470363eac595018441cf32d5e1001567a7aeba5d2/websocket_client-1.9.0-py3-none-any.whl", hash = "sha256:af248a825037ef591efbf6ed20cc5faa03d3b47b9e5a2230a529eeee1c1fc3ef", size = 82616, upload-time = "2025-10-07T21:16:34.951Z" },
]
```

## File: `docs/CLI_TEST_PLAN.md`
```markdown
# NotebookLM CLI - Comprehensive Test Plan

**Purpose:** Verify all CLI commands work correctly before GA release.  
**Version:** v0.1.0  
**Last Updated:** 2026-01-09

---

## Prerequisites

```bash
# Install CLI
cd /path/to/notebooklm-cli
pip install -e .

# Verify installation
nlm --version

# Authenticate (required before running tests)
nlm login
nlm login --check  # Should show "Notebooks found: N"
```

---

## Test Configuration

```bash
# Hardcoded test resources
export TEST_YOUTUBE_URL="https://www.youtube.com/watch?v=d-PZDQlO4m4"
export TEST_URL="https://en.wikipedia.org/wiki/Artificial_intelligence"

# Rate limiting (wait between API calls to avoid hitting limits)
export TEST_THROTTLE_MS="${TEST_THROTTLE_MS:-2000}"  # 2 seconds between calls
```

---

## Pre-Test Setup (Interactive)

Before running tests, you'll need to provide a Google Drive document that you can edit.

### Step 1: Provide Your Drive Document

**Why?** The staleness/sync test requires modifying a document to verify the CLI detects changes.

```
Please provide a Google Drive document or slide deck URL that you can edit:
Example: https://docs.google.com/document/d/1KQH3eW0hMBp7WKukQ1oURhnW-SdOT1qq-kEZaVLWGB8/edit
```

Extract the document ID from the URL and set it:
```bash
export TEST_DRIVE_DOC_ID="<your-doc-id>"
export TEST_DRIVE_DOC_TITLE="My Test Document"
export TEST_DRIVE_DOC_TYPE="doc"  # Options: doc, slides, sheets, pdf
```

### Step 2: Remember the Freshness Test

> **⚠️ IMPORTANT:** Later in the test (Group 10), you will be asked to:
> 1. Make a small edit to your Drive document
> 2. Verify the CLI detects it as "stale"
> 3. Sync the document
> 4. Verify it's now "fresh"
>
> Keep your Drive document open in another tab!

---

## Test Execution Flow

The tests are ordered for optimal execution:

1. **Setup** - Auth verification, create test notebook
2. **Early Background Tasks** - Start deep research (takes 3-5 min)
3. **Source Tests** - Add URL, text, YouTube, Drive sources
4. **Query Tests** - Chat and query functionality
5. **Generation Tests** - Audio, video, reports, etc.
6. **Research Tests** - Check deep research status, import
7. **Drive Sync** - Interactive staleness check
8. **Cleanup** - Delete test notebook

---

## Test Group 1: Authentication

### Test 1.1 - Help: Login
```bash
nlm login --help
```

**Expected output includes:**
- `--legacy / -l` - browser-cookie3 fallback
- `--browser / -b` - browser selection for legacy mode
- `--manual / -m` - import from file
- `--check` - validate current auth
- `--profile / -p` - profile name
- `--file / -f` - cookie file path

---

### Test 1.2 - Functionality: CDP Login
```bash
nlm login
```

**Expected:**
- Chrome browser launches
- Message: "Using Chrome DevTools Protocol"
- No keychain prompt on macOS
- Success: "Cookies: N extracted"
- Success: "CSRF Token: Yes"

---

### Test 1.3 - Functionality: Check Valid Auth
```bash
nlm login --check
```

**Expected:**
- Makes real API call (not just file check)
- Shows: "Authentication valid!"
- Shows: "Notebooks found: N" (N > 0)

---

### Test 1.4 - Functionality: Check Invalid Auth
**Setup:** Corrupt or delete credentials

```bash
rm -rf ~/Library/Application\ Support/nlm/profiles/test-invalid
nlm login --check -p test-invalid
```

**Expected:**
- Exit code: 2
- Error about missing profile or auth failure
- Hint to run `nlm login`

---

## Test Group 2: Setup (Create Test Notebook)

### Test 2.1 - Create Test Notebook
```bash
nlm notebook create "NLM CLI Test - $(date +%Y%m%d-%H%M%S)"
```

**Expected:**
- Success message with title
- Shows notebook ID

**Capture:** `NOTEBOOK_ID=<id>`

---

### Test 2.2 - Verify Notebook Creation
```bash
nlm notebook get $NOTEBOOK_ID
```

**Expected:** Shows notebook with 0 sources

---

## Test Group 3: Start Deep Research (Background Task)

> **IMPORTANT:** Deep research takes 3-5 minutes. We start it early and check results later.

### Test 3.1 - Start Deep Research
```bash
nlm research start "artificial intelligence applications" --mode deep --notebook-id $NOTEBOOK_ID
```

**Expected:**
- Research started
- Shows task ID
- Message about ~5 minute duration

**Capture:** `DEEP_TASK_ID=<task_id>` (we'll check this in Test Group 9)

---

## Test Group 4: Source Management

### Test 4.1 - Add URL Source
```bash
nlm source add $NOTEBOOK_ID --url $TEST_URL
```

**Expected:** Source added, shows title

**Throttle:** `sleep 2`

---

### Test 4.2 - Add YouTube Source
```bash
nlm source add $NOTEBOOK_ID --url $TEST_YOUTUBE_URL
```

**Expected:** YouTube source added

**Throttle:** `sleep 2`

---

### Test 4.3 - Add Text Source
```bash
nlm source add $NOTEBOOK_ID --text "This is a test document about machine learning and neural networks." --title "Test Text Document"
```

**Expected:** Text source added with custom title

**Throttle:** `sleep 2`

---

### Test 4.4 - Add Drive Document Source
```bash
nlm source add $NOTEBOOK_ID --drive $TEST_DRIVE_DOC_ID --title "$TEST_DRIVE_DOC_TITLE" --type doc
```

**Expected:** Drive source added

**Note:** For staleness testing later, users need an editable document.

**Throttle:** `sleep 2`

---

### Test 4.5 - List Sources
```bash
nlm source list $NOTEBOOK_ID
```

**Expected:**
- Table with 4 sources
- Columns: ID, Title, Type

**Capture:** `SOURCE_ID=<first_source_id>` for later tests

---

### Test 4.6 - List Sources JSON
```bash
nlm source list $NOTEBOOK_ID --json
```

**Expected:** Valid JSON array with 4 items

---

### Test 4.7 - List Sources Quiet
```bash
nlm source list $NOTEBOOK_ID --quiet
```

**Expected:** 4 lines, each with just a UUID

---

### Test 4.8 - Get Source Details
```bash
nlm source get $SOURCE_ID
```

**Expected:** Source details with title, type

---

### Test 4.9 - Describe Source (AI Summary)
```bash
nlm source describe $SOURCE_ID
```

**Expected:**
- AI-generated summary
- Keywords list

---

### Test 4.10 - Get Source Content
```bash
nlm source content $SOURCE_ID
```

**Expected:** Raw text content (no AI processing)

---

## Test Group 5: Notebook Operations

### Test 5.1 - Notebook List Variations
```bash
# Default
nlm notebook list

# JSON
nlm notebook list --json

# Quiet (IDs only)
nlm notebook list --quiet

# Title format
nlm notebook list --title

# Full columns
nlm notebook list --full
```

**Expected:** Each format works correctly

---

### Test 5.2 - Describe Notebook
```bash
nlm notebook describe $NOTEBOOK_ID
```

**Expected:**
- AI-generated summary of sources
- Suggested topics

---

### Test 5.3 - Rename Notebook
```bash
nlm notebook rename $NOTEBOOK_ID "NLM CLI Test - Renamed"
```

**Expected:** Success message with new title

---

## Test Group 6: Query & Chat

### Test 6.1 - Basic Query
```bash
nlm notebook query $NOTEBOOK_ID "What topics are covered in these sources?"
```

**Expected:**
- AI response
- Shows conversation ID

**Capture:** `CONVERSATION_ID=<conv_id>`

---

### Test 6.2 - Follow-up Query
```bash
nlm notebook query $NOTEBOOK_ID "Tell me more about AI" --conversation-id $CONVERSATION_ID
```

**Expected:** Response uses conversation context

---

### Test 6.3 - Chat Configuration
```bash
# Learning guide mode
nlm chat configure $NOTEBOOK_ID --goal learning_guide

# Custom prompt
nlm chat configure $NOTEBOOK_ID --goal custom --prompt "Answer in bullet points"

# Response length
nlm chat configure $NOTEBOOK_ID --response-length shorter
```

**Expected:** Each configuration succeeds

---

### Test 6.4 - Chat Error Case
```bash
nlm chat configure $NOTEBOOK_ID --goal custom
```

**Expected:** Error: "--prompt is required when goal is 'custom'"

---

## Test Group 7: Content Generation

> **Throttling Reminder:** Wait 2-5 seconds between generation calls to avoid rate limits.

### Test 7.1 - Create Audio (Brief)
```bash
nlm audio create $NOTEBOOK_ID --format brief --length short --confirm
```

**Expected:** Audio generation started

**Throttle:** `sleep 5`

---

### Test 7.2 - Create Report
```bash
nlm report create $NOTEBOOK_ID --format "Briefing Doc" --confirm
```

**Expected:** Report generation started

**Throttle:** `sleep 5`

---

### Test 7.3 - Create Quiz
```bash
nlm quiz create $NOTEBOOK_ID --count 2 --difficulty 2 --confirm
```

**Expected:** Quiz generation started

**Throttle:** `sleep 3`

---

### Test 7.4 - Create Flashcards
```bash
nlm flashcards create $NOTEBOOK_ID --difficulty medium --confirm
```

**Expected:** Flashcards generation started

**Throttle:** `sleep 3`

---

### Test 7.5 - Create Mind Map
```bash
nlm mindmap create $NOTEBOOK_ID --title "Test Mind Map" --confirm
```

**Expected:** Mind map created

---

### Test 7.6 - List Mind Maps
```bash
nlm mindmap list $NOTEBOOK_ID
```

**Expected:** Shows created mind map

---

### Test 7.7 - Check Studio Status
```bash
nlm studio status $NOTEBOOK_ID
```

**Expected:** Lists all generated artifacts with status

---

## Test Group 8: Fast Research (Complete Cycle)

### Test 8.1 - Start Fast Research
```bash
nlm research start "machine learning basics" --mode fast --notebook-id $NOTEBOOK_ID
```

**Expected:**
- Research started
- Estimated time: ~30 seconds

**Capture:** `FAST_TASK_ID=<task_id>`

---

### Test 8.2 - Check Fast Research Status
```bash
nlm research status $NOTEBOOK_ID --max-wait 60
```

**Expected:**
- Status: completed
- Sources found: ~10

---

### Test 8.3 - Import Fast Research Sources
```bash
nlm research import $NOTEBOOK_ID $FAST_TASK_ID --indices 0,1,2
```

**Expected:** 3 sources imported

---

## Test Group 9: Deep Research (Check Background Task)

### Test 9.1 - Check Deep Research Status
```bash
# By now, deep research from Test 3.1 should be complete
nlm research status $NOTEBOOK_ID --max-wait 120
```

**Expected:**
- Status: completed
- Sources found: ~40+
- Report available

---

### Test 9.2 - Import Deep Research Sources
```bash
nlm research import $NOTEBOOK_ID $DEEP_TASK_ID
```

**Expected:** All sources imported

---

## Test Group 10: Drive Sync (Interactive)

> **⚠️ USER INTERACTION REQUIRED**
>
> This test requires you to modify the test Drive document to trigger staleness detection.

### Test 10.1 - Check Initial Freshness
```bash
nlm source stale $NOTEBOOK_ID
```

**Expected:** Shows Drive sources with freshness status (likely all fresh)

---

### Test 10.2 - Modify Drive Document

**⏸️ PAUSE: Please modify your test Drive document now:**
1. Open: https://docs.google.com/document/d/$TEST_DRIVE_DOC_ID
2. Add or change some text
3. Wait 10 seconds
4. Continue with Test 10.3

---

### Test 10.3 - Check Staleness After Edit
```bash
nlm source stale $NOTEBOOK_ID
```

**Expected:** Modified source shows as stale

---

### Test 10.4 - Sync Stale Sources
```bash
nlm source sync $NOTEBOOK_ID --confirm
```

**Expected:** Stale sources synced

---

### Test 10.5 - Verify Sync
```bash
nlm source stale $NOTEBOOK_ID
```

**Expected:** All sources now fresh

---

## Test Group 11: Delete Source (Mid-Test)

### Test 11.1 - Delete One Source
```bash
nlm source delete $SOURCE_ID --confirm
```

**Expected:** Source deleted

---

## Test Group 12: Cleanup (LAST)

### Test 12.1 - Delete Test Notebook
```bash
nlm notebook delete $NOTEBOOK_ID --confirm
```

**Expected:** Notebook and all contents permanently deleted

---

## Quick Copy-Paste Test Script

```bash
#!/bin/bash
# NLM CLI Test Script
set -e

# Config
TEST_YOUTUBE_URL="https://www.youtube.com/watch?v=d-PZDQlO4m4"
TEST_DRIVE_DOC_ID="1KQH3eW0hMBp7WKukQ1oURhnW-SdOT1qq-kEZaVLWGB8"
TEST_URL="https://en.wikipedia.org/wiki/Artificial_intelligence"
THROTTLE=2

echo "=== NLM CLI Test Suite ==="
echo ""

# Auth check
echo "1. Checking auth..."
nlm login --check
sleep $THROTTLE

# Create notebook
echo "2. Creating test notebook..."
RESULT=$(nlm notebook create "CLI Test $(date +%H%M%S)" 2>&1)
echo "$RESULT"
NOTEBOOK_ID=$(echo "$RESULT" | grep -oE '[0-9a-f-]{36}' | head -1)
echo "NOTEBOOK_ID=$NOTEBOOK_ID"
sleep $THROTTLE

# Start deep research early
echo "3. Starting deep research (background)..."
nlm research start "AI trends 2025" --mode deep --notebook-id $NOTEBOOK_ID
sleep $THROTTLE

# Add sources
echo "4. Adding sources..."
nlm source add $NOTEBOOK_ID --url "$TEST_URL"
sleep $THROTTLE
nlm source add $NOTEBOOK_ID --url "$TEST_YOUTUBE_URL"
sleep $THROTTLE
nlm source add $NOTEBOOK_ID --text "Test content" --title "Test Doc"
sleep $THROTTLE
nlm source add $NOTEBOOK_ID --drive "$TEST_DRIVE_DOC_ID" --title "Test Drive Doc" --type doc
sleep $THROTTLE

# List sources
echo "5. Listing sources..."
nlm source list $NOTEBOOK_ID

# Query
echo "6. Querying notebook..."
nlm notebook query $NOTEBOOK_ID "Summarize these sources"
sleep $THROTTLE

# Generate content
echo "7. Generating audio..."
nlm audio create $NOTEBOOK_ID --format brief --length short --confirm
sleep 5

# Check studio
echo "8. Checking studio status..."
nlm studio status $NOTEBOOK_ID

# Fast research
echo "9. Fast research..."
nlm research start "machine learning" --mode fast --notebook-id $NOTEBOOK_ID
sleep $THROTTLE
nlm research status $NOTEBOOK_ID --max-wait 60

# Check deep research
echo "10. Checking deep research..."
nlm research status $NOTEBOOK_ID --max-wait 120

# Cleanup
echo ""
read -p "Press Enter to delete test notebook or Ctrl+C to keep it..."
nlm notebook delete $NOTEBOOK_ID --confirm

echo "=== Tests Complete ==="
```

---

## Summary Checklist

After completing all tests, verify:

- [ ] Authentication works (CDP login, --check validates)
- [ ] All `--help` commands show correct options
- [ ] All CRUD operations work (create, read, update, delete)
- [ ] All output formats work (table, JSON, quiet, title, full)
- [ ] All source types work (URL, YouTube, text, Drive)
- [ ] Query and chat configuration work
- [ ] All content generation works (audio, report, quiz, flashcards, mindmap)
- [ ] Research works (fast and deep modes)
- [ ] Drive sync detects staleness and syncs
- [ ] Confirmation prompts work as expected
- [ ] Error messages are clear and helpful
- [ ] Rate limiting doesn't cause failures (with throttling)

---

## Rate Limiting Guidelines

To avoid API rate limits during testing:

| Operation Type | Recommended Delay |
|---------------|-------------------|
| Source operations | 2 seconds |
| Content generation | 5 seconds |
| Research operations | 2 seconds |
| Query operations | 2 seconds |

For automated testing, implement exponential backoff on 429 errors.
```

## File: `docs/TECHNICAL_DEEP_DIVE.md`
```markdown
# NotebookLM Technical Deep Dive: Research & Mind Map Protocols

This document captures technical discoveries made during the development of the NotebookLM CLI and MCP server, specifically regarding undocumented RPC behaviors and status codes.

## 1. Research Protocol (RPC: `e3bVqc`)

When polling for research status, NotebookLM returns a complex nested array. The status of a research task is indicated by a specific integer code at index `task_info[4]`.

### Status Code Mapping
- **`2`**: `IN_PROGRESS`. The task is active, but results are not yet finalized.
- **`6`**: `COMPLETED`. The research session has finished, and all discovered sources are available for import.
- **`NO_RESEARCH`**: Indicated by an empty response or `null` task identifiers.

### Task Structure Discovery
The response structure for `poll_research` (RPC `e3bVqc`) is:
```json
[
  "task_id",
  [
    "notebook_id",
    ["query", 1],
    1,
    [
      [
        ["url", "title", "snippet", type_code, ...]
      ],
      "overall_summary"
    ],
    status_code
  ]
]
```
- **Note**: `type_code` in the source list determines if a source is Web (`1`), Drive (`2`, `3`, `8`), or an internal Deep Report (`5`).

---

## 2. Mind Map Protocol

Mind Maps behave differently from other Studio artifacts (Audio/Video). They require a two-step synchronization process for mutations and have a unique storage mechanism.

### Mutation: Deletion Sequence
To fully delete a Mind Map and prevent "ghost" entries in the backend list, two RPCs must be called in order:

1. **`AH0mwd` (Logical Delete)**:
   - **Payload**: `[notebook_id, null, [mind_map_id], [2]]`
   - This marks the artifact as deleted but doesn't immediately remove it from the persistent list (`cFji9`).

2. **`cFji9` (Commit/Sync)**:
   - **Payload**: `[notebook_id, null, [seconds, microseconds], [2]]`
   - **Crucial**: The `[seconds, microseconds]` timestamp MUST be the artifact's specific creation timestamp, retrieved from a previous `LIST_MIND_MAPS` call.
   - Calling this "commits" the state change.

### Tombstone Behavior in `LIST_MIND_MAPS` (RPC: `cFji9`)
Even after deletion, the backend often returns a "tombstone" entry in the list to maintain synchronization history.
- **Active Entry**: `["uuid", [metadata...]]`
- **Deleted Entry (Tombstone)**: `["uuid", null, 2]`
- **Action**: Clients must filter out entries where the second index (`metadata`) is `null`.

---

## 3. General Implementation Notes

### Build Label (`bl`)
The `bl` query parameter in `batchexecute` requests is critical for mutations. 
- **Effect**: If the `bl` is significantly outdated (e.g., several weeks old), mutations like research starts or artifact deletions may fail silently or return `400 Bad Request`.
- **Recommendation**: Periodically update the hardcoded default `bl` to match the latest web client version. Current observed working `bl`: `boq_labs-tailwind-frontend_20260108.06_p0`.

### Batch Import (RPC: `LBwxtb`)
When importing research sources, use the batch import RPC rather than adding sources individually. This handles MIME types correctly and is much more efficient.
- **Payload**: `[None, [1], task_id, notebook_id, source_array]`
- **Source Format**: Web sources use `[None, None, [url, title], ..., 2]`. Drive sources use `[[doc_id, mime_type, 1, title], ..., 2]`.

---

## 4. Chat/Query Response Structure

When querying a notebook, the response contains answer text with embedded citation markers (e.g., `[1]`, `[2, 3]`, `[5-7]`). These citation numbers are **indices into an internal citation list**, not direct indices into the notebook's source list.

### Response Structure (Query RPC)

Each response chunk is a `wrb.fr` payload containing JSON with the following top-level structure:

```
parsed[0]  - Answer metadata
  [0] - Answer text (string)
  [2] - Master list of source UUIDs used (not indexed by citation number)
  [4] - Annotations (text ranges with citation indices)

parsed[1]  - Citation list (array of citation entries)
  Each entry at index `i` corresponds to citation number `[i+1]`
  
parsed[2]  - Offset mapping (text range → citation indices)
```

### Citation Entry Structure

Each entry in `parsed[1]` (the citation list) at index `i` corresponds to citation `[i+1]`:

```json
[
  null,                    // [0]
  null,                    // [1]
  0.6925...,              // [2] Relevance score
  [[null, 13479, 14020]], // [3] Text offset range
  [...],                  // [4] Passage text and formatting
  [                       // [5] Source ID container
    [
      ["22e391d8-ddf4-..."]  // [5][0][0][0] = Source UUID
    ],
    "a0d8d307-..."
  ],
  ["b5ef2a72-..."]        // [6] Citation instance ID
]
```

**Key Path**: `citation_entry[5][0][0][0]` contains the Source UUID.

### Multiple Citations → Same Source

The backend creates a new citation entry for each **passage** cited, not each source. This means:
- Citation `[1]` might reference Source A, passage 1
- Citation `[2]` might reference Source A, passage 2
- Citation `[3]` might reference Source B

This explains why responses may contain `[18]` even when only 9 sources exist—there are 18 unique cited passages.

### Client Implementation

To display correct source titles:
1. Extract the citation list from `parsed[1]`
2. For each cited number in the answer text, look up `citation_list[num-1][5][0][0][0]` to get the Source UUID
3. Map the Source UUID to the source title using the notebook's source list

```

## File: `docs/TROUBLESHOOTING.md`
```markdown
# Troubleshooting

Common issues and solutions for the NotebookLM CLI.

## Quick Reference

| Error | Solution |
|-------|----------|
| "Cookies have expired" | Run `nlm login` |
| "Notebook not found" | Check ID with `nlm notebook list` |
| "Research already in progress" | Use `--force` flag or import existing results |
| Chrome doesn't launch | Ensure Chrome is installed and in your PATH |
| "nodename nor servname provided" | Network access blocked (see [Codex Users](#openai-codex-users)) |

---

## Authentication Issues

### Cookies Expired

**Error:** `Cookies have expired` or `Authentication failed`

**Solution:** Re-authenticate by running:
```bash
nlm login
```

NotebookLM sessions typically last ~20 minutes. If you're scripting or automating, you may need to re-authenticate periodically.

### Chrome Doesn't Launch

**Error:** Chrome doesn't open during `nlm login`

**Solutions:**
1. Ensure Google Chrome is installed
2. Check Chrome is in your PATH
3. Close any existing Chrome instances that may conflict
4. Try running with verbose output: `nlm login --debug` (if available)

---

## Network Issues

### OpenAI Codex Users

If you're using `nlm` from [OpenAI Codex CLI](https://github.com/openai/codex) and get DNS errors like:

```
Error: Request failed: [Errno 8] nodename nor servname provided, or not known
Hint: Check your internet connection.
```

**Cause:** Codex runs commands in a sandboxed environment that **blocks network access by default**.

**Solution:** Add the following to `~/.codex/config.toml`:

```toml
[sandbox_workspace_write]
network_access = true
```

Alternatively, run individual commands with full network access:
```bash
codex exec --sandbox danger-full-access "nlm notebook list"
```

---

## Source Issues

### Research Already in Progress

**Error:** `Research already in progress`

**Solutions:**
1. Wait for the current research to complete: `nlm research status <notebook-id>`
2. Import existing results: `nlm research import <notebook-id> <task-id>`
3. Force a new research: `nlm research start "query" --notebook-id <id> --force`

### Source Not Found

**Error:** `Source not found`

**Solutions:**
1. Verify the source ID: `nlm source list <notebook-id>`
2. Check if you're using the correct notebook
3. Ensure the source wasn't deleted

---

## Content Generation Issues

### Artifact Still Generating

**Error:** Status shows "in_progress" for a long time

**Solution:** Check studio status periodically:
```bash
nlm studio status <notebook-id>
```

Generation times vary:
- Audio podcasts: 2-5 minutes
- Reports/flashcards: 30-60 seconds
- Deep research: 4-5 minutes

### Generation Failed

**Error:** Artifact status shows "failed"

**Solutions:**
1. Ensure you have at least one source in the notebook
2. Check if NotebookLM service is available
3. Try regenerating the content

---

## Getting Help

If your issue isn't listed here:

1. Check the [GitHub Issues](https://github.com/jacob-bd/notebooklm-cli/issues)
2. Run `nlm --ai` to see the full command reference
3. Open a new issue with details about your error
```

## File: `nlm-cli-skill/SKILL.md`
```markdown
---
name: nlm-cli-skill
description: "Expert guide for the NotebookLM CLI (`nlm`) - a command-line interface for Google NotebookLM. Use this skill when users want to interact with NotebookLM programmatically, including: creating/managing notebooks, adding sources (URLs, YouTube, text, Google Drive), generating content (podcasts, reports, quizzes, flashcards, mind maps, slides, infographics, videos, data tables), conducting research, chatting with sources, or automating NotebookLM workflows. Triggers on mentions of \"nlm\", \"notebooklm\", \"notebook lm\", \"podcast generation\", \"audio overview\", or any NotebookLM-related automation task."
---

# NotebookLM CLI Expert

This skill provides comprehensive guidance for using the `nlm` CLI to automate Google NotebookLM workflows.

## Quick Reference

```bash
nlm --help              # List all commands
nlm <command> --help    # Help for specific command
nlm --ai                # Full AI-optimized documentation
nlm --version           # Check installed version
```

## Critical Rules (Read First!)

1. **Always authenticate first**: Run `nlm login` before any operations
2. **Sessions expire in ~20 minutes**: Re-run `nlm login` if commands start failing
3. **`--confirm` is REQUIRED**: All generation and delete commands need `--confirm` or `-y`
4. **Research requires `--notebook-id`**: The flag is mandatory, not positional
5. **Capture IDs from output**: Create/start commands return IDs needed for subsequent operations
6. **Use aliases**: Simplify long UUIDs with `nlm alias set <name> <uuid>`
7. **⚠️ ALWAYS ASK USER BEFORE DELETE**: Before executing ANY delete command, ask the user for explicit confirmation. Deletions are **irreversible**. Show what will be deleted and warn about permanent data loss.
8. **Check aliases before creating**: Run `nlm alias list` before creating a new alias to avoid conflicts with existing names.
9. **DO NOT launch REPL**: Never use `nlm chat start` - it opens an interactive REPL that AI tools cannot control. Use `nlm notebook query` for one-shot Q&A instead.
10. **Choose output format wisely**: Default output (no flags) is compact and token-efficient—use it for status checks. Use `--quiet` to capture IDs for piping. Only use `--json` when you need to parse specific fields programmatically.

## Workflow Decision Tree

Use this to determine the right sequence of commands:

```
User wants to...
│
├─► Work with NotebookLM for the first time
│   └─► nlm login → nlm notebook create "Title"
│
├─► Add content to a notebook
│   ├─► From a URL/webpage → nlm source add <nb-id> --url "https://..."
│   ├─► From YouTube → nlm source add <nb-id> --url "https://youtube.com/..."
│   ├─► From pasted text → nlm source add <nb-id> --text "content" --title "Title"
│   ├─► From Google Drive → nlm source add <nb-id> --drive <doc-id> --type doc
│   └─► Discover new sources → nlm research start "query" --notebook-id <nb-id>
│
├─► Generate content from sources
│   ├─► Podcast/Audio → nlm audio create <nb-id> --confirm
│   ├─► Written summary → nlm report create <nb-id> --confirm
│   ├─► Study materials → nlm quiz/flashcards create <nb-id> --confirm
│   ├─► Visual content → nlm mindmap/slides/infographic create <nb-id> --confirm
│   ├─► Video → nlm video create <nb-id> --confirm
│   └─► Extract data → nlm data-table create <nb-id> "description" --confirm
│
├─► Ask questions about sources
│   └─► nlm notebook query <nb-id> "question"
│       (Use --conversation-id for follow-ups)
│       ⚠️ Do NOT use `nlm chat start` - it's a REPL for humans only
│
├─► Check generation status
│   └─► nlm studio status <nb-id>
│
└─► Manage/cleanup
    ├─► List notebooks → nlm notebook list
    ├─► List sources → nlm source list <nb-id>
    ├─► Delete source → nlm source delete <source-id> --confirm
    └─► Delete notebook → nlm notebook delete <nb-id> --confirm
```

## Command Categories

### 1. Authentication

```bash
nlm login                    # Launch Chrome, extract cookies (primary method)
nlm login --check            # Validate current session
nlm login --profile work     # Use named profile for multiple accounts
nlm auth status              # Check if authenticated
nlm auth list                # List all profiles
```

**Session lifetime**: ~20 minutes. Re-authenticate when commands fail with auth errors.

### 2. Notebook Management

```bash
nlm notebook list                      # List all notebooks
nlm notebook list --json               # JSON output for parsing
nlm notebook list --quiet              # IDs only (for scripting)
nlm notebook create "Title"            # Create notebook, returns ID
nlm notebook get <id>                  # Get notebook details
nlm notebook describe <id>             # AI-generated summary + suggested topics
nlm notebook query <id> "question"     # One-shot Q&A with sources
nlm notebook rename <id> "New Title"   # Rename notebook
nlm notebook delete <id> --confirm     # PERMANENT deletion
```

### 3. Source Management

```bash
# Adding sources
nlm source add <nb-id> --url "https://..."           # Web page
nlm source add <nb-id> --url "https://youtube.com/..." # YouTube video
nlm source add <nb-id> --text "content" --title "X"  # Pasted text
nlm source add <nb-id> --drive <doc-id>              # Drive doc (auto-detect type)
nlm source add <nb-id> --drive <doc-id> --type slides # Explicit type

# Listing and viewing
nlm source list <nb-id>                # Table of sources
nlm source list <nb-id> --drive        # Show Drive sources with freshness
nlm source list <nb-id> --drive -S     # Skip freshness checks (faster)
nlm source get <source-id>             # Source metadata
nlm source describe <source-id>        # AI summary + keywords
nlm source content <source-id>         # Raw text content
nlm source content <source-id> -o file.txt  # Export to file

# Drive sync (for stale sources)
nlm source stale <nb-id>               # List outdated Drive sources
nlm source sync <nb-id> --confirm      # Sync all stale sources
nlm source sync <nb-id> --source-ids <ids> --confirm  # Sync specific

# Deletion
nlm source delete <source-id> --confirm
```

**Drive types**: `doc`, `slides`, `sheets`, `pdf`

### 4. Research (Source Discovery)

Research finds NEW sources from the web or Google Drive:

```bash
# Start research (--notebook-id is REQUIRED)
nlm research start "query" --notebook-id <id>              # Fast web (~30s)
nlm research start "query" --notebook-id <id> --mode deep  # Deep web (~5min)
nlm research start "query" --notebook-id <id> --source drive  # Drive search

# Check progress
nlm research status <nb-id>                   # Poll until done (5min max)
nlm research status <nb-id> --max-wait 0      # Single check, no waiting
nlm research status <nb-id> --task-id <tid>   # Check specific task
nlm research status <nb-id> --full            # Full details

# Import discovered sources
nlm research import <nb-id> <task-id>            # Import all
nlm research import <nb-id> <task-id> --indices 0,2,5  # Import specific
```

**Modes**: `fast` (~30s, ~10 sources) | `deep` (~5min, ~40+ sources, web only)

### 5. Content Generation (Studio)

All generation commands share these flags:
- `--confirm` or `-y`: **REQUIRED** to execute
- `--source-ids <id1,id2>`: Limit to specific sources
- `--language <code>`: BCP-47 code (en, es, fr, de, ja)

```bash
# Audio (Podcast)
nlm audio create <id> --confirm
nlm audio create <id> --format deep_dive --length default --confirm
nlm audio create <id> --format brief --focus "key topic" --confirm
# Formats: deep_dive, brief, critique, debate
# Lengths: short, default, long

# Report
nlm report create <id> --confirm
nlm report create <id> --format "Study Guide" --confirm
nlm report create <id> --format "Create Your Own" --prompt "Custom..." --confirm
# Formats: "Briefing Doc", "Study Guide", "Blog Post", "Create Your Own"

# Quiz
nlm quiz create <id> --confirm
nlm quiz create <id> --count 5 --difficulty 3 --confirm
# Count: number of questions (default: 2)
# Difficulty: 1-5 (1=easy, 5=hard)

# Flashcards
nlm flashcards create <id> --confirm
nlm flashcards create <id> --difficulty hard --confirm
# Difficulty: easy, medium, hard

# Mind Map
nlm mindmap create <id> --confirm
nlm mindmap create <id> --title "Topic Overview" --confirm
nlm mindmap list <id>  # List existing mind maps

# Slides
nlm slides create <id> --confirm
nlm slides create <id> --format presenter --length short --confirm
# Formats: detailed, presenter | Lengths: short, default

# Infographic
nlm infographic create <id> --confirm
nlm infographic create <id> --orientation portrait --detail detailed --confirm
# Orientations: landscape, portrait, square
# Detail: concise, standard, detailed

# Video
nlm video create <id> --confirm
nlm video create <id> --format brief --style whiteboard --confirm
# Formats: explainer, brief
# Styles: auto_select, classic, whiteboard, kawaii, anime, watercolor, retro_print, heritage, paper_craft

# Data Table
nlm data-table create <id> "Extract all dates and events" --confirm
# DESCRIPTION is required as second argument
```

### 6. Studio (Artifact Management)

Check and manage generated content:

```bash
nlm studio status <nb-id>                          # List all artifacts
nlm studio status <nb-id> --json                   # JSON output
nlm studio delete <nb-id> <artifact-id> --confirm  # Delete artifact
```

**Status values**: `completed` (✓), `in_progress` (●), `failed` (✗)

### 7. Interactive Chat (Human Users Only)

> ⚠️ **AI TOOLS: DO NOT USE `nlm chat start`** - It launches an interactive REPL that cannot be controlled programmatically. Use `nlm notebook query` for one-shot Q&A instead.

For human users at a terminal:

```bash
nlm chat start <nb-id>  # Launch interactive REPL
```

**REPL Commands**:
- `/sources` - List available sources
- `/clear` - Reset conversation context
- `/help` - Show commands
- `/exit` - Exit REPL

**Configure chat behavior** (works for both REPL and query):
```bash
nlm chat configure <id> --goal default
nlm chat configure <id> --goal learning_guide
nlm chat configure <id> --goal custom --prompt "Act as a tutor..."
nlm chat configure <id> --response-length longer  # longer, default, shorter
```

### 8. Aliases (UUID Shortcuts)

Simplify long UUIDs:

```bash
nlm alias set myproject abc123-def456...  # Create alias (auto-detects type)
nlm alias get myproject                    # Resolve to UUID
nlm alias list                             # List all aliases
nlm alias delete myproject                 # Remove alias

# Use aliases anywhere
nlm notebook get myproject
nlm source list myproject
nlm audio create myproject --confirm
```

### 9. Configuration

```bash
nlm config show              # Show current config
nlm config get <key>         # Get specific setting
nlm config set <key> <value> # Update setting
```

## Output Formats

Most list commands support multiple formats:

| Flag | Description |
|------|-------------|
| (none) | Rich table (human-readable) |
| `--json` | JSON output (for parsing) |
| `--quiet` | IDs only (for piping) |
| `--title` | "ID: Title" format |
| `--url` | "ID: URL" format (sources only) |
| `--full` | All columns/details |

## Common Patterns

### Pattern 1: Research → Podcast Pipeline

```bash
nlm notebook create "AI Research 2026"   # Capture ID
nlm alias set ai <notebook-id>
nlm research start "agentic AI trends" --notebook-id ai --mode deep
nlm research status ai --max-wait 300    # Wait up to 5 min
nlm research import ai <task-id>         # Import all sources
nlm audio create ai --format deep_dive --confirm
nlm studio status ai                     # Check generation progress
```

### Pattern 2: Quick Content Ingestion

```bash
nlm source add <id> --url "https://example1.com"
nlm source add <id> --url "https://example2.com"
nlm source add <id> --text "My notes..." --title "Notes"
nlm source list <id>
```

### Pattern 3: Study Materials Generation

```bash
nlm report create <id> --format "Study Guide" --confirm
nlm quiz create <id> --count 10 --difficulty 3 --confirm
nlm flashcards create <id> --difficulty medium --confirm
```

### Pattern 4: Drive Document Workflow

```bash
nlm source add <id> --drive 1KQH3eW0hMBp7WK... --type slides
# ... time passes, document is edited ...
nlm source stale <id>                    # Check freshness
nlm source sync <id> --confirm           # Sync if stale
```

## Error Recovery

| Error | Cause | Solution |
|-------|-------|----------|
| "Cookies have expired" | Session timeout | `nlm login` |
| "authentication may have expired" | Session timeout | `nlm login` |
| "Notebook not found" | Invalid ID | `nlm notebook list` |
| "Source not found" | Invalid ID | `nlm source list <nb-id>` |
| "Rate limit exceeded" | Too many calls | Wait 30s, retry |
| "Research already in progress" | Pending research | Use `--force` or import first |
| Chrome doesn't launch | Port conflict | Close Chrome, retry |

## Rate Limiting

Wait between operations to avoid rate limits:
- Source operations: 2 seconds
- Content generation: 5 seconds
- Research operations: 2 seconds
- Query operations: 2 seconds

## Advanced Reference

For detailed information, see:
- **[references/command_reference.md](command_reference.md)**: Complete command signatures
- **[references/troubleshooting.md](troubleshooting.md)**: Detailed error handling
- **[references/workflows.md](workflows.md)**: End-to-end task sequences
```

## File: `nlm-cli-skill/references/command_reference.md`
```markdown
# NotebookLM CLI - Complete Command Reference

This document contains the complete command signatures and all available options for every `nlm` command.

## Table of Contents

1. [Global Options](#global-options)
2. [Authentication](#authentication)
3. [Notebook Commands](#notebook-commands)
4. [Source Commands](#source-commands)
5. [Research Commands](#research-commands)
6. [Generation Commands](#generation-commands)
7. [Studio Commands](#studio-commands)
8. [Chat Commands](#chat-commands)
9. [Alias Commands](#alias-commands)
10. [Config Commands](#config-commands)

---

## Global Options

```bash
nlm --version, -v      # Show version and exit
nlm --ai               # Output AI-friendly documentation
nlm --install-completion  # Install shell completion
nlm --show-completion  # Show completion script
nlm --help             # Show help and exit
```

---

## Authentication

### nlm login

Authenticate with NotebookLM using Chrome DevTools Protocol.

```bash
nlm login [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Profile name for multiple accounts |
| `--check` | | Validate current credentials without re-authenticating |
| `--legacy` | `-l` | Use browser-cookie3 fallback (not recommended) |
| `--browser` | `-b` | Browser for legacy mode (chrome, firefox, edge) |
| `--manual` | `-m` | Import cookies from file |
| `--file` | `-f` | Cookie file path for manual mode |

### nlm auth status

Check current authentication status.

```bash
nlm auth status [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Profile to check |

### nlm auth list

List all authentication profiles.

```bash
nlm auth list
```

### nlm auth delete

Delete an authentication profile.

```bash
nlm auth delete <profile> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--confirm` | Required to confirm deletion |

---

## Notebook Commands

### nlm notebook list

List all notebooks.

```bash
nlm notebook list [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--json` | | Output as JSON |
| `--quiet` | `-q` | Output IDs only |
| `--title` | | Output as "ID: Title" |
| `--full` | | Show all columns |
| `--profile` | `-p` | Use specific profile |

### nlm notebook create

Create a new notebook.

```bash
nlm notebook create <title> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm notebook get

Get notebook details.

```bash
nlm notebook get <notebook-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm notebook describe

Get AI-generated notebook summary with suggested topics.

```bash
nlm notebook describe <notebook-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm notebook query

Ask a question about notebook sources.

```bash
nlm notebook query <notebook-id> <question> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--source-ids` | | Limit to specific sources (comma-separated) |
| `--conversation-id` | | Continue existing conversation |
| `--profile` | `-p` | Use specific profile |

### nlm notebook rename

Rename a notebook.

```bash
nlm notebook rename <notebook-id> <new-title> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm notebook delete

Delete a notebook permanently.

```bash
nlm notebook delete <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--confirm` | **Required** to confirm deletion |
| `--profile` | Use specific profile |

---

## Source Commands

### nlm source list

List sources in a notebook.

```bash
nlm source list <notebook-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--json` | | Output as JSON |
| `--quiet` | `-q` | Output IDs only |
| `--title` | | Output as "ID: Title" |
| `--url` | | Output as "ID: URL" |
| `--full` | | Show all columns (wider URL display) |
| `--drive` | | Show Drive sources with freshness status |
| `--skip-freshness` | `-S` | Skip freshness checks (faster with --drive) |
| `--profile` | `-p` | Use specific profile |

### nlm source add

Add a source to a notebook.

```bash
nlm source add <notebook-id> [OPTIONS]
```

**URL Source:**
| Option | Description |
|--------|-------------|
| `--url` | URL to add (web page or YouTube) |

**Text Source:**
| Option | Description |
|--------|-------------|
| `--text` | Text content to add |
| `--title` | Title for text source |

**Drive Source:**
| Option | Description |
|--------|-------------|
| `--drive` | Google Drive document ID |
| `--type` | Drive doc type: `doc`, `slides`, `sheets`, `pdf` |
| `--title` | Display title |

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm source get

Get source metadata.

```bash
nlm source get <source-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm source describe

Get AI-generated source summary with keywords.

```bash
nlm source describe <source-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm source content

Get raw text content of a source.

```bash
nlm source content <source-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--output` | `-o` | Export to file path |
| `--profile` | `-p` | Use specific profile |

### nlm source stale

List stale (outdated) Drive sources.

```bash
nlm source stale <notebook-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

### nlm source sync

Sync Drive sources with latest content.

```bash
nlm source sync <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--confirm` | **Required** to execute sync |
| `--source-ids` | Specific source IDs to sync (comma-separated) |
| `--profile` | Use specific profile |

### nlm source delete

Delete a source permanently.

```bash
nlm source delete <source-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--confirm` | **Required** to confirm deletion |
| `--profile` | Use specific profile |

---

## Research Commands

### nlm research start

Start a research task to discover new sources.

```bash
nlm research start <query> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--notebook-id` | **Required** - Target notebook ID |
| `--mode` | `fast` (default, ~30s) or `deep` (~5min, web only) |
| `--source` | `web` (default) or `drive` |
| `--force` | Override pending research |
| `--profile` | Use specific profile |

### nlm research status

Check research task progress.

```bash
nlm research status <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--task-id` | Check specific task (auto-detected if omitted) |
| `--max-wait` | Max seconds to wait (default: 300, 0=single check) |
| `--full` | Show full details |
| `--profile` | Use specific profile |

### nlm research import

Import discovered sources into notebook.

```bash
nlm research import <notebook-id> <task-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--indices` | Comma-separated indices of sources to import (default: all) |
| `--profile` | Use specific profile |

---

## Generation Commands

All generation commands share these common options:

| Option | Short | Description |
|--------|-------|-------------|
| `--confirm` | `-y` | **Required** to execute generation |
| `--source-ids` | | Limit to specific sources (comma-separated) |
| `--language` | | BCP-47 language code (en, es, fr, de, ja) |
| `--profile` | `-p` | Use specific profile |

### nlm audio create

Generate audio overview (podcast).

```bash
nlm audio create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--format` | `deep_dive`, `brief`, `critique`, `debate` | `deep_dive` |
| `--length` | `short`, `default`, `long` | `default` |
| `--focus` | Focus text/topic | |

### nlm report create

Generate written report.

```bash
nlm report create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--format` | `"Briefing Doc"`, `"Study Guide"`, `"Blog Post"`, `"Create Your Own"` | `"Briefing Doc"` |
| `--prompt` | Custom prompt (required for "Create Your Own") | |

### nlm quiz create

Generate quiz questions.

```bash
nlm quiz create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--count` | Number of questions | 2 |
| `--difficulty` | 1-5 (1=easy, 5=hard) | 2 |

### nlm flashcards create

Generate flashcards.

```bash
nlm flashcards create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--difficulty` | `easy`, `medium`, `hard` | `medium` |

### nlm mindmap create

Generate mind map.

```bash
nlm mindmap create <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--title` | Display title for the mind map |

### nlm mindmap list

List existing mind maps.

```bash
nlm mindmap list <notebook-id> [OPTIONS]
```

### nlm slides create

Generate slide deck.

```bash
nlm slides create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--format` | `detailed`, `presenter` | `detailed` |
| `--length` | `short`, `default` | `default` |
| `--focus` | Focus text/topic | |

### nlm infographic create

Generate infographic.

```bash
nlm infographic create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--orientation` | `landscape`, `portrait`, `square` | `landscape` |
| `--detail` | `concise`, `standard`, `detailed` | `standard` |
| `--focus` | Focus text/topic | |

### nlm video create

Generate video overview.

```bash
nlm video create <notebook-id> [OPTIONS]
```

| Option | Values | Default |
|--------|--------|---------|
| `--format` | `explainer`, `brief` | `explainer` |
| `--style` | `auto_select`, `classic`, `whiteboard`, `kawaii`, `anime`, `watercolor`, `retro_print`, `heritage`, `paper_craft` | `auto_select` |
| `--focus` | Focus text/topic | |

### nlm data-table create

Extract structured data as a table.

```bash
nlm data-table create <notebook-id> <description> [OPTIONS]
```

**Note**: `<description>` is a **required positional argument** describing what data to extract.

---

## Studio Commands

### nlm studio status

List all generated artifacts in a notebook.

```bash
nlm studio status <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--json` | Output as JSON |
| `--full` | Show all details |
| `--profile` | Use specific profile |

### nlm studio delete

Delete a generated artifact.

```bash
nlm studio delete <notebook-id> <artifact-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--confirm` | **Required** to confirm deletion |
| `--profile` | Use specific profile |

---

## Chat Commands

### nlm chat start

Start interactive chat REPL session.

```bash
nlm chat start <notebook-id> [OPTIONS]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--profile` | `-p` | Use specific profile |

**REPL Commands:**
- `/sources` - List available sources
- `/clear` - Reset conversation context
- `/help` - Show available commands
- `/exit` - Exit the REPL

### nlm chat configure

Configure chat behavior for a notebook.

```bash
nlm chat configure <notebook-id> [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--goal` | `default`, `learning_guide`, `custom` |
| `--prompt` | Custom system prompt (required when goal is `custom`) |
| `--response-length` | `default`, `longer`, `shorter` |
| `--profile` | Use specific profile |

---

## Alias Commands

### nlm alias set

Create or update an alias for a UUID.

```bash
nlm alias set <name> <uuid>
```

Type is auto-detected (notebook, source, artifact, task).

### nlm alias get

Resolve an alias to its UUID.

```bash
nlm alias get <name>
```

### nlm alias list

List all aliases.

```bash
nlm alias list
```

### nlm alias delete

Delete an alias.

```bash
nlm alias delete <name>
```

---

## Config Commands

### nlm config show

Display current configuration.

```bash
nlm config show [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--json` | Output as JSON instead of TOML |

### nlm config get

Get a specific configuration value.

```bash
nlm config get <key>
```

### nlm config set

Set a configuration value.

```bash
nlm config set <key> <value>
```
```

## File: `nlm-cli-skill/references/troubleshooting.md`
```markdown
# NotebookLM CLI - Troubleshooting Guide

This document provides detailed solutions for common issues when using the `nlm` CLI.

## Quick Diagnosis

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| "Cookies have expired" | Session timeout | `nlm login` |
| "Notebook not found" | Invalid/stale ID | `nlm notebook list` |
| "Source not found" | Invalid source ID | `nlm source list <nb-id>` |
| Chrome doesn't open | Port conflict | Close existing Chrome, retry |
| "Research already in progress" | Pending task | `--force` or import existing |
| "nodename nor servname" | Network blocked | See [Sandbox Users](#sandbox-environments) |
| Commands hang forever | Network/auth issue | Ctrl+C, `nlm login` |

---

## Authentication Issues

### Session Expired

**Symptoms:**
```
Error: Cookies have expired. Please run 'nlm login' to re-authenticate.
Error: authentication may have expired
```

**Cause:** NotebookLM sessions last approximately 20 minutes.

**Solution:**
```bash
nlm login
```

**Prevention:** For long-running scripts, implement periodic re-authentication:
```bash
# Check auth before critical operations
nlm login --check || nlm login
```

### Chrome Doesn't Launch

**Symptoms:**
- `nlm login` hangs with no browser window
- Error about Chrome not found

**Solutions:**

1. **Ensure Chrome is installed and in PATH:**
   ```bash
   which google-chrome || which chromium
   # On macOS, Chrome is at /Applications/Google Chrome.app
   ```

2. **Close existing Chrome instances:**
   ```bash
   pkill -f "Chrome"
   # Wait a moment, then retry
   nlm login
   ```

3. **Port conflict (port 9222 in use):**
   The CLI automatically tries ports 9222-9231, but if all are blocked:
   ```bash
   lsof -i :9222
   # Kill the process using the port
   kill -9 <PID>
   ```

### Profile Issues

**Symptom:** "Profile not found" or wrong account being used.

**Solutions:**

1. **List existing profiles:**
   ```bash
   nlm auth list
   ```

2. **Create a new profile:**
   ```bash
   nlm login --profile work
   ```

3. **Delete corrupted profile:**
   ```bash
   nlm auth delete <profile-name> --confirm
   nlm login --profile <profile-name>
   ```

4. **Check which profile is active:**
   ```bash
   nlm auth status
   ```

---

## Network Issues

### Sandbox Environments

**Symptom:**
```
Error: Request failed: [Errno 8] nodename nor servname provided, or not known
Hint: Check your internet connection.
```

**Cause:** Running inside a sandboxed environment (OpenAI Codex, containers) that blocks network access.

**Solution for OpenAI Codex:**

Add to `~/.codex/config.toml`:
```toml
[sandbox_workspace_write]
network_access = true
```

Or run with full network access:
```bash
codex exec --sandbox danger-full-access "nlm notebook list"
```

**Solution for Docker/Containers:**
Ensure the container has network access and can reach `notebooklm.google.com`.

### Rate Limiting

**Symptom:**
```
Error: Rate limit exceeded
```

**Cause:** Too many API calls in a short period. Free tier: ~50 queries/day.

**Solutions:**

1. **Wait and retry:**
   ```bash
   sleep 30
   # Retry command
   ```

2. **Implement throttling in scripts:**
   ```bash
   # Wait 2 seconds between operations
   nlm source add $ID --url "..." && sleep 2
   nlm source add $ID --url "..." && sleep 2
   ```

3. **Use batch operations where possible:**
   - Use `nlm research import` to import multiple sources at once
   - Use `nlm source sync` to sync all stale sources at once

---

## Source Issues

### Source Not Found

**Symptom:**
```
Error: Source not found
```

**Solutions:**

1. **Verify source exists:**
   ```bash
   nlm source list <notebook-id>
   ```

2. **Check correct notebook:**
   Sources are scoped to notebooks. Ensure you're using the right notebook ID.

3. **Source may have been deleted:**
   If the source was recently deleted, it no longer exists.

### Drive Source Issues

**Symptom:** Drive document fails to add or shows wrong content.

**Solutions:**

1. **Verify document ID:**
   Extract from URL: `https://docs.google.com/document/d/[DOC_ID]/edit`

2. **Specify correct type:**
   ```bash
   nlm source add <nb-id> --drive <doc-id> --type slides  # for Slides
   nlm source add <nb-id> --drive <doc-id> --type sheets  # for Sheets
   nlm source add <nb-id> --drive <doc-id> --type pdf     # for PDF
   ```

3. **Check permissions:**
   Ensure your Google account has access to the Drive document.

4. **Large documents timeout:**
   Very large documents (100+ slides) may take longer. The CLI has a 120-second timeout.

### Stale Drive Sources

**Symptom:** Drive source content is outdated.

**Solution:**
```bash
# Check which sources are stale
nlm source stale <notebook-id>

# Sync all stale sources
nlm source sync <notebook-id> --confirm

# Sync specific sources
nlm source sync <notebook-id> --source-ids <id1>,<id2> --confirm
```

---

## Research Issues

### Research Already in Progress

**Symptom:**
```
Error: Research already in progress
```

**Solutions:**

1. **Wait for completion:**
   ```bash
   nlm research status <notebook-id>
   ```

2. **Import existing results:**
   ```bash
   nlm research status <notebook-id> --full  # Get task ID
   nlm research import <notebook-id> <task-id>
   ```

3. **Force new research:**
   ```bash
   nlm research start "query" --notebook-id <id> --force
   ```

### Research Takes Too Long

**Expected durations:**
- Fast mode: ~30 seconds
- Deep mode: ~5 minutes

**If exceeding these times:**

1. **Check status without waiting:**
   ```bash
   nlm research status <notebook-id> --max-wait 0
   ```

2. **Try a more specific query:**
   Broader queries take longer. Narrow down the search terms.

---

## Generation Issues

### Artifact Still Generating

**Symptom:** `nlm studio status` shows "in_progress" for extended time.

**Expected generation times:**
- Reports, quizzes, flashcards: 30-60 seconds
- Audio podcasts: 2-5 minutes
- Videos: 3-7 minutes
- Deep research: 4-5 minutes

**Solution:** Keep polling:
```bash
nlm studio status <notebook-id>
```

### Generation Failed

**Symptom:** Artifact status shows "failed" or (✗).

**Possible causes and solutions:**

1. **No sources in notebook:**
   ```bash
   nlm source list <notebook-id>
   # If empty, add sources first
   ```

2. **Sources too short:**
   Add more substantial content to your sources.

3. **Retry generation:**
   ```bash
   # Delete failed artifact
   nlm studio delete <notebook-id> <artifact-id> --confirm
   # Regenerate
   nlm audio create <notebook-id> --confirm
   ```

### Missing --confirm Flag

**Symptom:**
```
Error: Missing required flag: --confirm
```

**Cause:** All generation and delete commands require explicit confirmation.

**Solution:** Add `--confirm` or `-y`:
```bash
nlm audio create <notebook-id> --confirm
# or
nlm audio create <notebook-id> -y
```

---

## Command Syntax Issues

### Wrong Argument Order

**Common mistakes:**

```bash
# WRONG: research start without --notebook-id
nlm research start "query" <notebook-id>

# CORRECT: --notebook-id is a required flag
nlm research start "query" --notebook-id <notebook-id>
```

```bash
# WRONG: data-table without description
nlm data-table create <notebook-id> --confirm

# CORRECT: description is required positional argument
nlm data-table create <notebook-id> "Extract all dates" --confirm
```

### Custom Chat Prompt Without --goal

**Symptom:**
```
Error: --prompt is required when goal is 'custom'
```

**Solution:**
```bash
# CORRECT: specify both --goal custom AND --prompt
nlm chat configure <id> --goal custom --prompt "Act as a tutor..."
```

---

## Getting More Help

1. **Check command help:**
   ```bash
   nlm <command> --help
   ```

2. **Get full AI documentation:**
   ```bash
   nlm --ai
   ```

3. **Check version:**
   ```bash
   nlm --version
   ```

4. **GitHub Issues:**
   https://github.com/jacob-bd/notebooklm-cli/issues
```

## File: `nlm-cli-skill/references/workflows.md`
```markdown
# NotebookLM CLI - Complete Workflow Sequences

This document provides end-to-end workflow sequences for common tasks with the `nlm` CLI.

## Critical AI Behavior Rules

### Always Confirm Destructive Operations

**Before executing ANY delete operation, ALWAYS ask the user for explicit confirmation.** Deletions are irreversible.

Commands requiring user confirmation before AI execution:
- `nlm notebook delete <id> --confirm`
- `nlm source delete <id> --confirm`
- `nlm studio delete <notebook-id> <artifact-id> --confirm`
- `nlm auth delete <profile> --confirm`

**Example AI behavior:**
```
User: "Delete that notebook"

AI: "I found notebook 'AI Research' (ID: abc123...). 
⚠️ This will PERMANENTLY delete the notebook and all its sources, generated content, and history. 
This action cannot be undone.

Do you want me to proceed with deletion?"

[Wait for user confirmation before running: nlm notebook delete abc123... --confirm]
```

---

## Workflow 1: First-Time Setup

### Goal: Authenticate and create first notebook

```bash
# Step 1: Authenticate (opens Chrome)
nlm login

# Step 2: Verify authentication
nlm login --check
# Expected: "Authentication valid! Notebooks found: N"

# Step 3: Create a notebook
nlm notebook create "My First Notebook"
# Output: Created notebook: <notebook-id>

# Step 4: Set alias for convenience
nlm alias set first <notebook-id>

# Step 5: Verify
nlm notebook get first
```

---

## Workflow 2: Content Ingestion

### Goal: Add multiple sources to a notebook

```bash
# Prerequisites: Authenticated, have notebook ID

# Add web pages
nlm source add <notebook-id> --url "https://example.com/article1"
sleep 2  # Throttle to avoid rate limits

nlm source add <notebook-id> --url "https://example.com/article2"
sleep 2

# Add YouTube video
nlm source add <notebook-id> --url "https://youtube.com/watch?v=VIDEO_ID"
sleep 2

# Add pasted text/notes
nlm source add <notebook-id> --text "My personal notes and observations about this topic..." --title "My Notes"
sleep 2

# Add Google Drive document
nlm source add <notebook-id> --drive 1KQH3eW0hMBp7WKukQ1oURhnW-SdOT1qq --type doc
sleep 2

# Verify all sources added
nlm source list <notebook-id>
```

---

## Workflow 3: Research → Podcast Pipeline

### Goal: Discover sources via research and generate a podcast

```bash
# Step 1: Create dedicated notebook
nlm notebook create "AI Trends Research 2026"
# Capture: NOTEBOOK_ID=<id>

# Step 2: Set alias
nlm alias set research <notebook-id>

# Step 3: Start deep research (takes ~5 minutes)
nlm research start "agentic AI and autonomous systems trends 2026" --notebook-id research --mode deep
# Capture: TASK_ID=<task_id>

# Step 4: Monitor progress (polls until complete or timeout)
nlm research status research --max-wait 300

# Step 5: View discovered sources
nlm research status research --full

# Step 6: Import all discovered sources
nlm research import research <task-id>
# Or import specific sources:
# nlm research import research <task-id> --indices 0,2,5,7

# Step 7: Generate podcast
nlm audio create research --format deep_dive --length default --confirm

# Step 8: Check generation status (podcast takes 2-5 minutes)
nlm studio status research
# Repeat until status shows "completed"

# Step 9: Get podcast URL from studio status output
```

---

## Workflow 4: Study Materials Generation

### Goal: Create comprehensive study materials from sources

```bash
# Prerequisites: Notebook with sources already added

# Step 1: Verify sources exist
nlm source list <notebook-id>

# Step 2: Generate study guide report
nlm report create <notebook-id> --format "Study Guide" --confirm
sleep 5

# Step 3: Generate quiz (10 questions, medium difficulty)
nlm quiz create <notebook-id> --count 10 --difficulty 3 --confirm
sleep 3

# Step 4: Generate flashcards
nlm flashcards create <notebook-id> --difficulty medium --confirm
sleep 3

# Step 5: Generate mind map for visual overview
nlm mindmap create <notebook-id> --title "Topic Overview" --confirm

# Step 6: Check all generated artifacts
nlm studio status <notebook-id>
```

---

## Workflow 5: Quick Q&A Session

### Goal: Ask questions about sources

```bash
# Option A: One-shot questions
nlm notebook query <notebook-id> "What are the main themes across these sources?"
# Capture: CONVERSATION_ID from output

# Follow-up (maintains context)
nlm notebook query <notebook-id> "Can you elaborate on the first theme?" --conversation-id <conv-id>

# Option B: Interactive chat session
nlm chat start <notebook-id>
# In REPL:
#   Type questions naturally
#   /sources - see available sources
#   /clear - reset conversation
#   /exit - exit REPL
```

---

## Workflow 6: Drive Document Sync

### Goal: Keep Drive sources up-to-date

```bash
# Step 1: Check current freshness status
nlm source list <notebook-id> --drive
# Shows: Source ID, Title, Type, Fresh status

# Step 2: Quick check (skip freshness API calls)
nlm source list <notebook-id> --drive -S

# Step 3: Find stale sources
nlm source stale <notebook-id>
# Lists sources that have been modified in Drive since import

# Step 4: Sync all stale sources
nlm source sync <notebook-id> --confirm

# Step 5: Sync specific sources only
nlm source sync <notebook-id> --source-ids <id1>,<id2> --confirm

# Step 6: Verify all fresh
nlm source stale <notebook-id>
# Should show no stale sources
```

---

## Workflow 7: Multi-Account Management

### Goal: Work with multiple Google accounts

```bash
# Step 1: Login to work account
nlm login --profile work

# Step 2: Login to personal account
nlm login --profile personal

# Step 3: List all profiles
nlm auth list

# Step 4: Use specific profile for commands
nlm notebook list --profile work
nlm notebook list --profile personal

# Step 5: Create notebook in specific account
nlm notebook create "Work Project" --profile work
```

---

## Workflow 8: Content Export

### Goal: Extract and export source content

```bash
# Step 1: List sources
nlm source list <notebook-id>

# Step 2: Get AI summary of a source
nlm source describe <source-id>

# Step 3: Get raw text content
nlm source content <source-id>

# Step 4: Export to file
nlm source content <source-id> --output ./export/source_content.txt

# Step 5: Export multiple sources (script pattern)
for id in $(nlm source list <notebook-id> --quiet); do
    nlm source content $id --output "./export/${id}.txt"
    sleep 1
done
```

---

## Workflow 9: Presentation Preparation

### Goal: Generate presentation materials

```bash
# Step 1: Create focused notebook
nlm notebook create "Q4 Presentation Prep"
nlm alias set pres <notebook-id>

# Step 2: Add relevant sources
nlm source add pres --url "https://company.com/q4-results"
nlm source add pres --drive <slides-doc-id> --type slides
nlm source add pres --text "Key talking points: ..." --title "Talking Points"

# Step 3: Generate slide deck
nlm slides create pres --format detailed --confirm
sleep 5

# Step 4: Generate briefing doc
nlm report create pres --format "Briefing Doc" --confirm
sleep 5

# Step 5: Generate infographic for visual summary
nlm infographic create pres --orientation landscape --detail standard --confirm

# Step 6: Check outputs
nlm studio status pres
```

---

## Workflow 10: Cleanup and Deletion

### Goal: Clean up notebooks and artifacts

**⚠️ IMPORTANT: Always confirm with user before executing delete commands!**

```bash
# Step 1: List existing notebooks
nlm notebook list

# Step 2: Get notebook details before deletion
nlm notebook get <notebook-id>
nlm source list <notebook-id>
nlm studio status <notebook-id>

# Step 3: Delete specific artifact (after user confirms)
# AI: "Are you sure you want to delete artifact X from notebook Y?"
nlm studio delete <notebook-id> <artifact-id> --confirm

# Step 4: Delete specific source (after user confirms)
# AI: "Are you sure you want to delete source X?"
nlm source delete <source-id> --confirm

# Step 5: Delete entire notebook (after user confirms)
# AI: "This will permanently delete notebook X and ALL its contents. Proceed?"
nlm notebook delete <notebook-id> --confirm

# Step 6: Clean up aliases
nlm alias delete <alias-name>
```

---

## Workflow 11: Scripting and Automation

### Goal: Automate repetitive tasks

```bash
#!/bin/bash
# Example: Daily research automation

# Configuration
NOTEBOOK_ID="abc123..."
QUERY="latest AI news $(date +%Y-%m-%d)"

# Ensure authenticated
nlm login --check || nlm login

# Start fast research
nlm research start "$QUERY" --notebook-id $NOTEBOOK_ID --mode fast

# Wait for completion
nlm research status $NOTEBOOK_ID --max-wait 60

# Get task ID from status
TASK_ID=$(nlm research status $NOTEBOOK_ID --max-wait 0 2>&1 | grep -oE 'task_id=[^ ]+' | cut -d= -f2)

# Import all sources
nlm research import $NOTEBOOK_ID $TASK_ID

# Generate brief audio summary
nlm audio create $NOTEBOOK_ID --format brief --length short --confirm

# Check status
nlm studio status $NOTEBOOK_ID
```

---

## Rate Limiting Guidelines

To avoid hitting API rate limits:

| Operation Type | Recommended Delay |
|---------------|-------------------|
| Source add | 2 seconds |
| Content generation | 5 seconds |
| Research operations | 2 seconds |
| Query operations | 2 seconds |
| Batch operations | 10 seconds |

**Daily limits (free tier):** ~50 queries/operations per day.

---

## Error Recovery Patterns

### Pattern: Re-authentication on failure

```bash
# Try command, re-auth if fails
nlm notebook list || (nlm login && nlm notebook list)
```

### Pattern: Retry with backoff

```bash
retry_command() {
    local max=3 delay=5
    for ((i=1; i<=max; i++)); do
        "$@" && return 0
        sleep $delay
        delay=$((delay * 2))
    done
    return 1
}

retry_command nlm audio create $NOTEBOOK_ID --confirm
```

### Pattern: Check before generate

```bash
# Ensure sources exist before generating
SOURCE_COUNT=$(nlm source list $NOTEBOOK_ID --quiet | wc -l)
if [ "$SOURCE_COUNT" -gt 0 ]; then
    nlm audio create $NOTEBOOK_ID --confirm
else
    echo "Error: No sources in notebook"
fi
```
```

## File: `src/nlm/__init__.py`
```python
"""NLM - NotebookLM CLI."""

__version__ = "0.1.12"
```

## File: `src/nlm/__main__.py`
```python
"""Entry point for running nlm as a module."""

from nlm.cli.main import app

if __name__ == "__main__":
    app()
```

## File: `src/nlm/ai_docs.py`
```python
"""AI-friendly documentation output for the --ai flag."""

from nlm import __version__

AI_DOCS = """# NLM CLI - AI Assistant Guide

You are interacting with `nlm`, a command-line interface for Google NotebookLM.
This documentation teaches you how to use the tool effectively.

## Version

nlm version {version}

---

## CRITICAL: Authentication

**Sessions last approximately 20 minutes.** Before ANY operation, you MUST ensure the user is authenticated.

### First-Time Setup / Re-Authentication
```bash
nlm login
```
This opens NotebookLM in Chrome and extracts cookies automatically.
Output on success: `✓ Successfully authenticated!`

### Check If Already Authenticated
```bash
nlm auth status
```
Validates credentials by making a real API call (lists notebooks).
Shows: `✓ Authenticated` with notebook count, or error if expired.

### Auto-Authentication Recovery (Automatic)
The CLI includes 3-layer automatic recovery:
1. **CSRF/Session Refresh**: Automatically refreshes tokens on 401 errors
2. **Token Reload**: Reloads tokens from disk if updated externally (e.g., by another session)
3. **Headless Auth**: If Chrome profile has saved login, attempts headless authentication

This means most session expirations are handled automatically. You only need to manually run `nlm login` if all recovery layers fail.

### Session Expired?
If ANY command returns:
- "Cookies have expired"
- "authentication may have expired"

Run:
```bash
nlm login
```

---

## Quick Reference

```
nlm <command> [subcommand] [options]
```

### All Top-Level Commands

| Command | Description |
|---------|-------------|
| `nlm login` | Authenticate with NotebookLM (**START HERE**) |
| `nlm auth` | Check authentication status (status, list, delete) |
| `nlm config` | View/edit configuration (show, get, set) |
| `nlm notebook` | Manage notebooks (list, create, get, describe, rename, delete, query) |
| `nlm source` | Manage sources (list, add, get, describe, content, delete, stale, sync) |
| `nlm chat` | Chat with notebooks (start, configure) |
| `nlm studio` | Manage artifacts (status, delete) |
| `nlm research` | Research and discover sources (start, status, import) |
| `nlm alias` | Manage ID shortcuts (set, get, list, delete) |
| `nlm audio` | Create audio overviews/podcasts (create) |
| `nlm report` | Create reports (create) |
| `nlm quiz` | Create quizzes (create) |
| `nlm flashcards` | Create flashcards (create) |
| `nlm mindmap` | Create mind maps (create) |
| `nlm slides` | Create slide decks (create) |
| `nlm infographic` | Create infographics (create) |
| `nlm video` | Create video overviews (create) |
| `nlm data-table` | Create data tables (create) |

---

## Alias System (Shortcuts for UUIDs)

Create memorable names for long UUIDs:

```bash
# IMPORTANT: Always check existing aliases before creating new ones
nlm alias list

# Set an alias (type is auto-detected)
nlm alias set myproject abc123-def456-...

# Use aliases anywhere an ID is expected
nlm notebook get myproject
nlm source list myproject  
nlm audio create myproject --confirm

# Manage aliases
nlm alias list                    # List all
nlm alias get myproject           # Resolve to UUID
nlm alias delete myproject        # Remove
```

---

## Complete Command Reference

### Login & Auth

```bash
nlm login                              # Authenticate (opens browser)
nlm login --profile work               # Named profile
nlm login --manual --file <path>       # Import cookies from file
nlm login --check                      # Only check if auth valid

nlm auth status                        # Check current auth
nlm auth status --profile work         # Check specific profile
nlm auth list                          # List all profiles
nlm auth delete work --confirm         # Delete a profile
```

### Config Commands

```bash
nlm config show                        # Display current config (TOML)
nlm config show --json                 # Display as JSON
nlm config get <key>                   # Get specific setting
nlm config set <key> <value>           # Update setting
```

### Notebook Commands

```bash
nlm notebook list                      # List all notebooks
nlm notebook list --json               # JSON output
nlm notebook list --quiet              # IDs only
nlm notebook list --title              # "ID: Title" format
nlm notebook list --full               # All columns

nlm notebook create "Title"            # Create new notebook

nlm notebook get <id>                  # Get notebook details

nlm notebook describe <id>             # AI summary with topics

nlm notebook rename <id> "New Title"   # Rename notebook

nlm notebook delete <id> --confirm     # Delete permanently

nlm notebook query <id> "question"     # Chat with sources
nlm notebook query <id> "follow up" --conversation-id <cid>
nlm notebook query <id> "question" --source-ids <id1,id2>
```

### Source Commands

```bash
nlm source list <notebook-id>          # List sources
nlm source list <notebook-id> --full   # Full details
nlm source list <notebook-id> --url    # "ID: URL" format
nlm source list <notebook-id> --drive  # Show Drive sources with freshness
nlm source list <notebook-id> --drive --skip-freshness  # Faster, skip freshness checks

nlm source add <notebook-id> --url "https://..."           # Add URL
nlm source add <notebook-id> --url "https://youtube.com/..." # Add YouTube
nlm source add <notebook-id> --text "content" --title "Title"  # Add text
nlm source add <notebook-id> --drive <doc-id>              # Add Drive doc
nlm source add <notebook-id> --drive <doc-id> --type slides  # Add Drive slides
# Types: doc, slides, sheets, pdf

nlm source get <source-id>             # Get source metadata

nlm source describe <source-id>        # AI summary + keywords

nlm source content <source-id>         # Raw text content
nlm source content <source-id> --output file.txt  # Export to file

nlm source delete <source-id> --confirm  # Delete source

nlm source stale <notebook-id>         # List stale Drive sources
nlm source sync <notebook-id> --confirm  # Sync all stale
nlm source sync <notebook-id> --source-ids <ids> --confirm  # Sync specific
```

### Chat Commands

```bash
# Interactive REPL (multi-turn conversation)
nlm chat start <notebook-id>           # Start interactive session
# In REPL:
#   /sources - List sources
#   /clear   - Reset conversation
#   /help    - Show commands
#   /exit    - Exit

# Configure chat behavior
nlm chat configure <notebook-id> --goal default
nlm chat configure <notebook-id> --goal learning_guide
nlm chat configure <notebook-id> --goal custom --prompt "Act as a tutor..."
nlm chat configure <notebook-id> --response-length longer   # longer, default, shorter
```

### Research Commands

```bash
# Start research (--notebook-id is REQUIRED)
nlm research start "query" --notebook-id <id>                    # Fast web (default)
nlm research start "query" --notebook-id <id> --mode deep        # Deep web (~5min)
nlm research start "query" --notebook-id <id> --source drive     # Fast drive
nlm research start "query" --notebook-id <id> --force            # Override pending

# Check progress
nlm research status <notebook-id>                    # Poll until done (5min max)
nlm research status <notebook-id> --max-wait 0       # Single check
nlm research status <notebook-id> --task-id <tid>    # Specific task
nlm research status <notebook-id> --full             # Full details

# Import discovered sources
nlm research import <notebook-id> <task-id>              # Import all
nlm research import <notebook-id> <task-id> --indices 0,2,5  # Import specific
```

**Research Modes:**
- `fast`: ~30 seconds, ~10 sources (web or drive)
- `deep`: ~5 minutes, ~40-80 sources (web only)

### Generation Commands (Studio)

**All generation commands support:**
- `--confirm` or `-y`: Skip confirmation (REQUIRED for automation)
- `--source-ids <id1,id2>`: Limit to specific sources
- `--language <code>`: BCP-47 code (en, es, fr, de, ja)
- `--profile <name>`: Use specific auth profile

#### Audio (Podcast)
```bash
nlm audio create <notebook-id> --confirm
nlm audio create <notebook-id> --format deep_dive --length default --confirm
nlm audio create <notebook-id> --format brief --focus "key topic" --confirm
# Formats: deep_dive, brief, critique, debate
# Lengths: short, default, long
```

#### Report
```bash
nlm report create <notebook-id> --confirm
nlm report create <notebook-id> --format "Study Guide" --confirm
nlm report create <notebook-id> --format "Create Your Own" --prompt "Summary..." --confirm
# Formats: "Briefing Doc", "Study Guide", "Blog Post", "Create Your Own"
```

#### Quiz
```bash
nlm quiz create <notebook-id> --confirm
nlm quiz create <notebook-id> --count 5 --difficulty 3 --confirm
# Count: number of questions (default: 2)
# Difficulty: 1-5 (1=easy, 5=hard, default: 2)
```

#### Flashcards
```bash
nlm flashcards create <notebook-id> --confirm
nlm flashcards create <notebook-id> --difficulty hard --confirm
# Difficulty: easy, medium, hard (default: medium)
```

#### Mind Map
```bash
nlm mindmap create <notebook-id> --confirm
nlm mindmap create <notebook-id> --title "Topic Overview" --confirm
```

#### Slides
```bash
nlm slides create <notebook-id> --confirm
nlm slides create <notebook-id> --format presenter --length short --confirm
# Formats: detailed, presenter (default: detailed)
# Lengths: short, default
```

#### Infographic
```bash
nlm infographic create <notebook-id> --confirm
nlm infographic create <notebook-id> --orientation portrait --detail detailed --confirm
# Orientations: landscape, portrait, square (default: landscape)
# Detail: concise, standard, detailed (default: standard)
```

#### Video
```bash
nlm video create <notebook-id> --confirm
nlm video create <notebook-id> --format brief --style whiteboard --confirm
# Formats: explainer, brief (default: explainer)
# Styles: auto_select, classic, whiteboard, kawaii, anime, watercolor, retro_print, heritage, paper_craft
```

#### Data Table
```bash
nlm data-table create <notebook-id> "Extract all dates and events" --confirm
# DESCRIPTION is REQUIRED as second argument
```

### Studio Commands (Artifact Management)

```bash
nlm studio status <notebook-id>                    # List all artifacts + status
nlm studio status <notebook-id> --json             # JSON output
nlm studio status <notebook-id> --full             # All details

nlm studio delete <notebook-id> <artifact-id> --confirm  # Delete artifact
```

### Alias Commands

```bash
nlm alias set <name> <uuid>     # Create/update alias (auto-detects type)
nlm alias get <name>            # Get UUID for alias
nlm alias list                  # List all aliases
nlm alias delete <name>         # Remove (no --confirm needed)
```

---

## Output Formats

List commands support multiple formats:

| Flag | Description |
|------|-------------|
| (none) | Rich table (human-readable) |
| `--json` | JSON output (for parsing) |
| `--quiet` | IDs only (for piping) |
| `--title` | "ID: Title" format |
| `--url` | "ID: URL" format (sources only) |
| `--full` | All columns/details |

---

## Error Handling

| Error Message | Cause | Solution |
|--------------|-------|----------|
| "Cookies have expired" | Session expired | Run `nlm login` |
| "authentication may have expired" | Session expired | Run `nlm login` |
| "Notebook not found" | Invalid ID | Run `nlm notebook list` |
| "Source not found" | Invalid ID | Run `nlm source list <notebook-id>` |
| "Rate limit exceeded" | Too many API calls | Wait 30 seconds, retry |
| "Research already in progress" | Pending research | Use `--force` or import first |

---

## Complete Task Sequences

### Sequence 1: Research → Podcast

```bash
# 1. Authenticate
nlm login

# 2. Create notebook
nlm notebook create "AI Research 2026"
# ID: abc123...

# 3. Set alias for convenience
nlm alias set ai abc123...

# 4. Start deep research
nlm research start "agentic AI trends 2026" --notebook-id ai --mode deep
# Task ID: task456...

# 5. Wait for completion
nlm research status ai --max-wait 300

# 6. Import all sources
nlm research import ai task456...

# 7. Generate podcast
nlm audio create ai --format deep_dive --confirm

# 8. Check status until completed
nlm studio status ai
```

### Sequence 2: Quick Source Ingestion

```bash
# Add multiple URLs
nlm source add <notebook-id> --url "https://example1.com"
nlm source add <notebook-id> --url "https://example2.com"
nlm source add <notebook-id> --text "My notes here" --title "Notes"
nlm source list <notebook-id>
```

### Sequence 3: Generate Study Materials

```bash
nlm quiz create <notebook-id> --count 10 --difficulty 3 --confirm
nlm flashcards create <notebook-id> --difficulty hard --confirm
nlm report create <notebook-id> --format "Study Guide" --confirm
```

---

## Tips for AI Assistants

1. **Always run `nlm login` first** if any auth error occurs
2. **Use `--confirm` for all generation/delete commands** to avoid blocking prompts
3. **Capture IDs from create outputs** - you'll need them for subsequent operations
4. **Use aliases** for frequently-used notebooks to simplify commands
5. **Poll for long operations** - audio/video takes 1-5 minutes; use `nlm studio status`
6. **Research requires `--notebook-id`** - the flag is mandatory
7. **Session lifetime is ~20 minutes** - re-login if operations start failing
8. **Use `--max-wait 0`** for single status poll instead of blocking
9. **⚠️ ALWAYS ask user before delete** - Before running ANY delete command, ask the user for explicit confirmation. Deletions are IRREVERSIBLE. Show what will be deleted and warn about permanent data loss.
10. **Check aliases before creating** - Run `nlm alias list` before creating a new alias to avoid conflicts with existing names.
11. **DO NOT launch REPL** - Never use `nlm chat start` - it opens an interactive REPL that AI tools cannot control. Use `nlm notebook query` for one-shot Q&A instead.
12. **Choose output format wisely** - Default output (no flags) is compact and token-efficient—use it for status checks. Use `--quiet` to capture IDs for piping. Only use `--json` when you need to parse specific fields programmatically.
"""


def print_ai_docs() -> None:
    """Print the AI-friendly documentation."""
    print(AI_DOCS.format(version=__version__))
```

## File: `src/nlm/cli/__init__.py`
```python
"""CLI package for NLM."""
```

## File: `src/nlm/cli/alias.py`
```python
"""Alias CLI commands."""

import typer
from rich.console import Console
from rich.table import Table

from nlm.core.alias import get_alias_manager, detect_id_type

console = Console()
app = typer.Typer(
    help="Manage ID aliases",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


@app.command("set")
def set_alias(
    name: str = typer.Argument(..., help="Alias name (e.g. 'my-notebook')"),
    value: str = typer.Argument(..., help="ID value (e.g. valid UUID)"),
    alias_type: str = typer.Option(
        None, "--type", "-t",
        help="Type: notebook, source, artifact, task (auto-detected if not specified)",
    ),
    profile: str = typer.Option(None, "--profile", "-p", help="Profile to use for detection"),
) -> None:
    """Create or update an alias for an ID."""
    manager = get_alias_manager()
    
    # Auto-detect type if not provided
    if not alias_type:
        with console.status("[dim]Detecting ID type...[/dim]"):
            alias_type = detect_id_type(value, profile)
    
    manager.set_alias(name, value, alias_type)
    
    type_display = f"[dim]({alias_type})[/dim]" if alias_type != "unknown" else ""
    console.print(f"[green]✓[/green] Alias set: [bold]{name}[/bold] -> {value} {type_display}")


@app.command("get")
def get_alias(
    name: str = typer.Argument(..., help="Alias name"),
) -> None:
    """Get the value of an alias."""
    manager = get_alias_manager()
    entry = manager.get_entry(name)
    
    if entry:
        console.print(entry.value)
    else:
        console.print(f"[red]Error:[/red] Alias '{name}' not found")
        raise typer.Exit(1)


@app.command("list")
def list_aliases() -> None:
    """List all aliases."""
    manager = get_alias_manager()
    aliases = manager.list_aliases()
    
    if not aliases:
        console.print("No aliases defined.")
        return

    table = Table(title="Aliases")
    table.add_column("Name", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Value", style="green")
    
    # Type icons for visual distinction
    type_icons = {
        "notebook": "📓",
        "source": "📄",
        "artifact": "🎨",
        "task": "🔍",
        "unknown": "❓",
    }
    
    for name, entry in sorted(aliases.items()):
        icon = type_icons.get(entry.type, "❓")
        table.add_row(name, f"{icon} {entry.type}", entry.value)
    
    console.print(table)


@app.command("delete")
def delete_alias(
    name: str = typer.Argument(..., help="Alias name"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
) -> None:
    """Delete an alias."""
    if not confirm:
        typer.confirm(f"Are you sure you want to delete alias '{name}'?", abort=True)
        
    manager = get_alias_manager()
    if manager.delete_alias(name):
        console.print(f"[green]✓[/green] Deleted alias: {name}")
    else:
        console.print(f"[yellow]⚠[/yellow] Alias '{name}' not found")
        raise typer.Exit(1)



```

## File: `src/nlm/cli/auth.py`
```python
"""Authentication CLI commands."""

import typer
from rich.console import Console

from nlm.core.auth import AuthManager
from nlm.core.exceptions import NLMError

console = Console()
app = typer.Typer(
    help="Authentication commands",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


@app.command("status")
def status(
    profile: str = typer.Option(
        "default", "--profile", "-p",
        help="Profile to check",
    ),
) -> None:
    """Show authentication status and profile information.
    
    Validates credentials by making a real API call to list notebooks.
    """
    from nlm.core.client import NotebookLMClient
    
    auth = AuthManager(profile)
    
    try:
        p = auth.load_profile()
    except NLMError as e:
        console.print(f"[red]✗[/red] Not authenticated")
        console.print(f"  {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(2)
    
    # Actually validate by making a real API call
    console.print(f"[dim]Validating credentials for profile: {p.name}...[/dim]")
    
    try:
        with NotebookLMClient(profile=profile) as client:
            notebooks = client.list_notebooks()
        
        # Update last_validated timestamp
        auth.save_profile(
            cookies=p.cookies,
            csrf_token=p.csrf_token,
            session_id=p.session_id,
            email=p.email,
        )
        
        console.print(f"[green]✓[/green] Authenticated")
        console.print(f"  Email: {p.email or 'Unknown'}")
        console.print(f"  Profile: {p.name}")
        console.print(f"  Notebooks accessible: {len(notebooks)}")
        console.print(f"  Credentials path: {auth.profile_dir}")
        
    except NLMError as e:
        console.print(f"[red]✗[/red] Authentication expired or invalid")
        console.print(f"  {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        console.print(f"\n[dim]Run 'nlm login' to re-authenticate.[/dim]")
        raise typer.Exit(2)


@app.command("list")
def list_profiles() -> None:
    """List all available profiles."""
    profiles = AuthManager.list_profiles()
    
    if not profiles:
        console.print("[dim]No profiles found.[/dim]")
        console.print("\nRun 'nlm login' to create a profile.")
        return
    
    console.print("[bold]Available profiles:[/bold]")
    for name in profiles:
        try:
            auth = AuthManager(name)
            p = auth.load_profile()
            email = p.email or "Unknown"
            console.print(f"  [cyan]{name}[/cyan]: {email}")
        except Exception:
            console.print(f"  [cyan]{name}[/cyan]: [dim](invalid)[/dim]")


@app.command("delete")
def delete_profile(
    profile: str = typer.Argument(..., help="Profile name to delete"),
    confirm: bool = typer.Option(
        False, "--confirm", "-y",
        help="Skip confirmation prompt",
    ),
) -> None:
    """Delete a profile and its credentials."""
    auth = AuthManager(profile)
    
    if not auth.profile_exists():
        console.print(f"[red]Error:[/red] Profile '{profile}' not found")
        raise typer.Exit(1)
    
    if not confirm:
        typer.confirm(
            f"Are you sure you want to delete profile '{profile}'?",
            abort=True,
        )
    
    auth.delete_profile()
    console.print(f"[green]✓[/green] Deleted profile: {profile}")
```

## File: `src/nlm/cli/chat.py`
```python
"""Chat configuration CLI commands."""

from typing import Optional

import typer
from rich.console import Console

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError

console = Console()
app = typer.Typer(
    help="Configure chat settings",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def get_client(profile: str | None = None) -> NotebookLMClient:
    """Get a client instance."""
    return NotebookLMClient(profile=profile)


@app.command("configure")
def configure_chat(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    goal: str = typer.Option(
        "default", "--goal", "-g",
        help="Chat goal: default, learning_guide, or custom",
    ),
    prompt: Optional[str] = typer.Option(
        None, "--prompt",
        help="Custom prompt (required when goal=custom, max 10000 chars)",
    ),
    response_length: str = typer.Option(
        "default", "--response-length", "-r",
        help="Response length: default, longer, or shorter",
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """
    Configure how AI responds in notebook chat.
    
    Goals:
    - default: Standard helpful responses
    - learning_guide: Educational, step-by-step explanations
    - custom: Use your own prompt to guide the AI
    """
    notebook_id = get_alias_manager().resolve(notebook_id)

    # Validate goal
    valid_goals = ["default", "learning_guide", "custom"]
    if goal not in valid_goals:
        console.print(f"[red]Error:[/red] Invalid goal. Must be one of: {', '.join(valid_goals)}")
        raise typer.Exit(1)
    
    # Validate custom prompt requirement
    if goal == "custom" and not prompt:
        console.print("[red]Error:[/red] --prompt is required when goal is 'custom'")
        raise typer.Exit(1)
    
    # Validate prompt length
    if prompt and len(prompt) > 10000:
        console.print("[red]Error:[/red] Custom prompt must be 10000 characters or less")
        raise typer.Exit(1)
    
    # Validate response length
    valid_lengths = ["default", "longer", "shorter"]
    if response_length not in valid_lengths:
        console.print(f"[red]Error:[/red] Invalid response length. Must be one of: {', '.join(valid_lengths)}")
        raise typer.Exit(1)
    
    try:
        with get_client(profile) as client:
            config = client.configure_chat(
                notebook_id,
                goal=goal,
                custom_prompt=prompt,
                response_length=response_length,
            )
        
        console.print("[green]✓[/green] Chat configuration updated")
        console.print(f"  Goal: {config.get('goal', goal)}")
        if config.get('custom_prompt'):
            cp = config['custom_prompt']
            preview = cp[:50] + "..." if len(cp) > 50 else cp
            console.print(f"  Prompt: {preview}")
        console.print(f"  Response length: {config.get('response_length', response_length)}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("start")
def start_chat(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """
    Start interactive chat session with a notebook.
    
    Enter a REPL where you can have multi-turn conversations.
    Use /help for commands, /exit to quit.
    """
    from nlm.cli.repl import run_chat_repl
    run_chat_repl(notebook_id, profile)

```

## File: `src/nlm/cli/config.py`
```python
"""Configuration CLI commands."""

import typer
from rich.console import Console
from rich.syntax import Syntax

from nlm.utils.config import get_config, save_config, _config_to_toml

console = Console()
app = typer.Typer(
    help="Manage configuration settings",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


@app.command("show")
def show_config(
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
) -> None:
    """Show current configuration."""
    config = get_config()
    
    if json_output:
        import json
        console.print_json(json.dumps(config.model_dump(), indent=2))
    else:
        # Print as TOML syntax highlighted
        toml_str = _config_to_toml(config)
        syntax = Syntax(toml_str, "toml", theme="monokai", line_numbers=False)
        console.print(syntax)


@app.command("get")
def get_config_value(
    key: str = typer.Argument(..., help="Configuration key (e.g. output.format)"),
) -> None:
    """Get a specific configuration value."""
    config = get_config()
    conf_dict = config.model_dump()
    
    parts = key.split(".")
    current = conf_dict
    
    try:
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                console.print(f"[red]Error:[/red] Key '{key}' not found.")
                raise typer.Exit(1)
        
        # Format output based on type
        if isinstance(current, bool):
            val_str = str(current).lower()
            color = "green" if current else "red"
            console.print(f"[{color}]{val_str}[/{color}]")
        else:
            console.print(str(current))
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)


@app.command("set")
def set_config_value(
    key: str = typer.Argument(..., help="Configuration key (e.g. output.format)"),
    value: str = typer.Argument(..., help="Value to set"),
) -> None:
    """Set a configuration value."""
    config = get_config()
    
    parts = key.split(".")
    if len(parts) != 2:
        console.print("[red]Error:[/red] Invalid key format. Use section.key (e.g. output.format)")
        raise typer.Exit(1)
        
    section, field = parts
    
    # Validate section
    if not hasattr(config, section):
        console.print(f"[red]Error:[/red] Unknown section '{section}'")
        raise typer.Exit(1)
        
    section_obj = getattr(config, section)
    
    # Validate field
    if not hasattr(section_obj, field):
        console.print(f"[red]Error:[/red] Unknown field '{field}' in section '{section}'")
        raise typer.Exit(1)
        
    # Get field info for type conversion
    # Pydantic v2 uses model_fields
    field_info = section_obj.model_fields.get(field)
    target_type = field_info.annotation
    
    try:
        # Handle boolean conversion explicitly
        if target_type is bool:
            if value.lower() in ("true", "1", "yes", "on"):
                converted_val = True
            elif value.lower() in ("false", "0", "no", "off"):
                converted_val = False
            else:
                raise ValueError("Value must be true/false")
        else:
            # Basic casting for other types (int, float, str)
            # This is simplified; Pydantic model usage handles validation but we need native type for assignment
            if target_type is int:
                converted_val = int(value)
            elif target_type is float:
                converted_val = float(value)
            else:
                converted_val = value  # Default to string
        
        # Update the model
        setattr(section_obj, field, converted_val)
        
        # Save changes
        save_config(config)
        console.print(f"[green]✓[/green] Set {key} = {converted_val}")
        
    except ValueError as e:
        console.print(f"[red]Error:[/red] Invalid value for {key}: {str(e)}")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error:[/red] Failed to update config: {str(e)}")
        raise typer.Exit(1)
```

## File: `src/nlm/cli/main.py`
```python
"""Main CLI application for NLM."""

from typing import Optional

import typer
from rich.console import Console

from nlm import __version__
from nlm.cli.auth import app as auth_app
from nlm.cli.chat import app as chat_app
from nlm.cli.notebook import app as notebook_app
from nlm.cli.research import app as research_app
from nlm.cli.source import app as source_app
from nlm.cli.alias import app as alias_app
from nlm.cli.config import app as config_app
from nlm.cli.studio import (
    app as studio_app,
    audio_app,
    data_table_app,
    flashcards_app,
    infographic_app,
    mindmap_app,
    quiz_app,
    report_app,
    slides_app,
    video_app,
)

console = Console()

# Main application
app = typer.Typer(
    name="nlm",
    help="NotebookLM CLI - Command-line interface for Google NotebookLM",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

# Register subcommands
app.add_typer(notebook_app, name="notebook", help="Manage notebooks")
app.add_typer(source_app, name="source", help="Manage sources")
app.add_typer(chat_app, name="chat", help="Configure chat settings")
app.add_typer(studio_app, name="studio", help="Manage studio artifacts")
app.add_typer(research_app, name="research", help="Research and discover sources")
app.add_typer(alias_app, name="alias", help="Manage ID aliases")
app.add_typer(config_app, name="config", help="Manage configuration")

# Generation commands as top-level
app.add_typer(audio_app, name="audio", help="Create audio overviews")
app.add_typer(report_app, name="report", help="Create reports")
app.add_typer(quiz_app, name="quiz", help="Create quizzes")
app.add_typer(flashcards_app, name="flashcards", help="Create flashcards")
app.add_typer(mindmap_app, name="mindmap", help="Create and manage mind maps")
app.add_typer(slides_app, name="slides", help="Create slide decks")
app.add_typer(infographic_app, name="infographic", help="Create infographics")
app.add_typer(video_app, name="video", help="Create video overviews")
app.add_typer(data_table_app, name="data-table", help="Create data tables")

# Auth commands at top level
app.add_typer(auth_app, name="auth", help="Authentication status")


@app.command("login")
def login(
    manual: bool = typer.Option(
        False, "--manual", "-m",
        help="Manually provide cookies from a file",
    ),
    check: bool = typer.Option(
        False, "--check",
        help="Only check if current auth is valid",
    ),
    profile: str = typer.Option(
        "default", "--profile", "-p",
        help="Profile name to save credentials to",
    ),
    cookie_file: Optional[str] = typer.Option(
        None, "--file", "-f",
        help="Path to file containing cookies (for manual mode)",
    ),
) -> None:
    """
    Authenticate with NotebookLM.
    
    Default: Uses Chrome DevTools Protocol to extract cookies automatically.
    Use --manual to import cookies from a file.
    """
    from nlm.core.auth import AuthManager
    from nlm.core.exceptions import NLMError
    
    auth = AuthManager(profile)
    
    if check:
        # Check existing auth by making a real API call
        try:
            from nlm.core.client import NotebookLMClient
            
            p = auth.load_profile()
            console.print(f"[dim]Checking credentials for profile: {p.name}...[/dim]")
            
            # Actually test the API
            with NotebookLMClient(profile=profile) as client:
                notebooks = client.list_notebooks()
            
            # Success! Update last validated
            auth.save_profile(
                cookies=p.cookies,
                csrf_token=p.csrf_token,
                session_id=p.session_id,
                email=p.email,
            )
            
            console.print(f"[green]✓[/green] Authentication valid!")
            console.print(f"  Profile: {p.name}")
            console.print(f"  Notebooks found: {len(notebooks)}")
            if p.email:
                console.print(f"  Account: {p.email}")
        except NLMError as e:
            console.print(f"[red]✗[/red] Authentication failed: {e.message}")
            if e.hint:
                console.print(f"[dim]{e.hint}[/dim]")
            raise typer.Exit(2)
        return
    
    if manual:
        # Manual mode - read from file
        if not cookie_file:
            cookie_file = typer.prompt(
                "Enter path to file containing cookies",
                default="~/.nlm/cookies.txt",
            )
        try:
            profile_obj = auth.login_with_file(cookie_file)
            console.print(f"[green]✓[/green] Successfully authenticated!")
            console.print(f"  Profile saved: {profile}")
            console.print(f"  Credentials saved to: {auth.profile_dir}")
        except NLMError as e:
            console.print(f"[red]Error:[/red] {e.message}")
            if e.hint:
                console.print(f"\n[dim]Hint: {e.hint}[/dim]")
            raise typer.Exit(1)
        return
    
    # Default: CDP mode - Chrome DevTools Protocol
    console.print("[bold]Launching Chrome for authentication...[/bold]")
    console.print("[dim]Using Chrome DevTools Protocol[/dim]\n")
    
    try:
        from nlm.utils.cdp import extract_cookies_via_cdp, extract_csrf_token, extract_session_id, get_page_html, terminate_chrome
        
        console.print("Starting Chrome...")
        result = extract_cookies_via_cdp(
            auto_launch=True,
            wait_for_login=True,
            login_timeout=300,
        )
        
        cookies = result["cookies"]
        csrf_token = result.get("csrf_token", "")
        session_id = result.get("session_id", "")
        
        # Save to profile
        auth.save_profile(
            cookies=cookies,
            csrf_token=csrf_token,
            session_id=session_id,
        )
        
        # Close Chrome to release profile lock (enables headless auth later)
        console.print("[dim]Closing Chrome...[/dim]")
        terminate_chrome()
        
        console.print(f"\n[green]✓[/green] Successfully authenticated!")
        console.print(f"  Profile: {profile}")
        console.print(f"  Cookies: {len(cookies)} extracted")
        console.print(f"  CSRF Token: {'Yes' if csrf_token else 'No (will be auto-extracted)'}")
        console.print(f"  Credentials saved to: {auth.profile_dir}")
        
    except NLMError as e:
        console.print(f"\n[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False, "--version", "-v",
        help="Show version and exit",
    ),
    ai: bool = typer.Option(
        False, "--ai",
        help="Output AI-friendly documentation for this CLI",
    ),
) -> None:
    """
    NLM - Command-line interface for Google NotebookLM.
    
    Use 'nlm <command> --help' for help on specific commands.
    """
    if version:
        console.print(f"nlm version {__version__}")
        raise typer.Exit()
    
    if ai:
        from nlm.ai_docs import print_ai_docs
        print_ai_docs()
        raise typer.Exit()
    
    # Show help if no command provided
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())


if __name__ == "__main__":
    app()
```

## File: `src/nlm/cli/notebook.py`
```python
"""Notebook CLI commands."""

from typing import Optional

import typer
from rich.console import Console

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError
from nlm.output.formatters import detect_output_format, get_formatter

console = Console()
app = typer.Typer(
    help="Manage notebooks",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def get_client(profile: str | None = None) -> NotebookLMClient:
    """Get a client instance."""
    return NotebookLMClient(profile=profile)


@app.command("list")
def list_notebooks(
    full: bool = typer.Option(False, "--full", "-a", help="Show all columns"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Output IDs only"),
    title: bool = typer.Option(False, "--title", "-t", help="Show ID: Title format"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List all notebooks."""
    try:
        with get_client(profile) as client:
            notebooks = client.list_notebooks()
        
        fmt = detect_output_format(json_output, quiet, title)
        formatter = get_formatter(fmt, console)
        formatter.format_notebooks(notebooks, full=full, title_only=title)
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("create")
def create_notebook(
    title: str = typer.Argument("", help="Notebook title"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a new notebook."""
    try:
        with get_client(profile) as client:
            notebook = client.create_notebook(title)
        
        if not notebook:
            console.print("[red]Error:[/red] Failed to create notebook. The API returned an empty or invalid response.")
            raise typer.Exit(1)
            
        console.print(f"[green]✓[/green] Created notebook: {notebook.title}")
        console.print(f"  ID: {notebook.id}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("get")
def get_notebook(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get notebook details."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            notebook = client.get_notebook(notebook_id)
        
        fmt = detect_output_format(json_output)
        formatter = get_formatter(fmt, console)
        formatter.format_item(notebook, title="Notebook Details")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("describe")
def describe_notebook(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get AI-generated notebook summary with suggested topics."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            result = client.get_notebook_summary(notebook_id)
        
        console.print("[bold]Summary:[/bold]")
        console.print(result.get("summary", "No summary available."))
        
        topics = result.get("suggested_topics", [])
        if topics:
            console.print("\n[bold]Suggested Topics:[/bold]")
            for topic in topics:
                if isinstance(topic, dict):
                    console.print(f"  • {topic.get('question', topic)}")
                else:
                    console.print(f"  • {topic}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("rename")
def rename_notebook(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    new_title: str = typer.Argument(..., help="New title"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Rename a notebook."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            success = client.rename_notebook(notebook_id, new_title)
        
        if success:
            console.print(f"[green]✓[/green] Renamed notebook to: {new_title}")
        else:
            console.print("[yellow]⚠[/yellow] Rename may have failed")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("delete")
def delete_notebook(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Delete a notebook permanently."""
    notebook_id = get_alias_manager().resolve(notebook_id)
    
    if not confirm:
        typer.confirm(
            f"Are you sure you want to delete notebook {notebook_id}?",
            abort=True,
        )
    
    try:
        with get_client(profile) as client:
            client.delete_notebook(notebook_id)
        
        console.print(f"[green]✓[/green] Deleted notebook: {notebook_id}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("query")
def query_notebook(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    question: str = typer.Argument(..., help="Question to ask"),
    conversation_id: Optional[str] = typer.Option(
        None, "--conversation-id", "-c",
        help="Conversation ID for follow-up questions",
    ),
    source_ids: Optional[str] = typer.Option(
        None, "--source-ids", "-s",
        help="Comma-separated source IDs to query (default: all)",
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Chat with notebook sources."""
    try:
        sources = source_ids.split(",") if source_ids else None
        
        notebook_id = get_alias_manager().resolve(notebook_id)
        
        with get_client(profile) as client:
            response = client.query(
                notebook_id,
                question,
                source_ids=sources,
                conversation_id=conversation_id,
            )
        
        if response:
            console.print(response.get("answer", "No response"))
            
            # Print citations footer
            sources = response.get("sources", [])
            if sources:
                console.print("\n[bold]Sources:[/bold]")
                for i, src in enumerate(sources, 1):
                    title = src.get("title", "Untitled")
                    # Try to be smart about alignment if list is long, but simple is fine for now
                    console.print(f"  [dim][{i}] {title}[/dim]")
            
            conv_id = response.get("conversation_id")
            if conv_id:
                console.print(f"\n[dim]Conversation ID: {conv_id}[/dim]")
                console.print("[dim]Use --conversation-id for follow-up questions[/dim]")
        else:
            console.print("[yellow]No response received[/yellow]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)
```

## File: `src/nlm/cli/repl.py`
```python
"""Interactive REPL for notebook chat."""

import re

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError

console = Console()

HELP_TEXT = """
[bold]Available Commands:[/bold]
  /exit, /quit  Exit the chat
  /clear        Start new conversation
  /sources      List notebook sources
  /help         Show this help
"""


def _parse_citations(text: str) -> set[int]:
    """Extract citation numbers from response text.
    
    Handles formats: [1], [1, 2], [11-13], [1, 2, 5-7]
    """
    citations = set()
    
    # Find all bracketed citation groups
    pattern = r'\[(\d+(?:\s*[-,]\s*\d+)*)\]'
    matches = re.findall(pattern, text)
    
    for match in matches:
        # Split by comma first
        parts = match.split(',')
        for part in parts:
            part = part.strip()
            if '-' in part:
                # Handle ranges like "11-13"
                try:
                    start, end = part.split('-')
                    for num in range(int(start.strip()), int(end.strip()) + 1):
                        citations.add(num)
                except ValueError:
                    pass
            else:
                # Single number
                try:
                    citations.add(int(part))
                except ValueError:
                    pass
    
    return citations


def run_chat_repl(notebook_id: str, profile: str | None = None) -> None:
    """Run interactive chat session with a notebook."""
    notebook_id = get_alias_manager().resolve(notebook_id)
    
    try:
        with NotebookLMClient(profile=profile) as client:
            # Get notebook info for welcome banner
            notebook = client.get_notebook(notebook_id)
            if not notebook:
                console.print("[red]Error:[/red] Notebook not found.")
                raise typer.Exit(1)
            
            notebook_title = notebook.title or "Notebook"
            source_count = len(notebook.sources) if notebook.sources else 0
            sources_list = notebook.sources or []
            
            # Welcome banner
            console.print(Panel(
                f"[bold]{notebook_title}[/bold]\n"
                f"[dim]{source_count} source(s) loaded[/dim]\n\n"
                f"Type your question and press Enter.\n"
                f"Use [bold]/help[/bold] for commands, [bold]/exit[/bold] to quit.",
                title="NotebookLM Chat",
                border_style="blue",
            ))
            console.print()
            
            conversation_id: str | None = None
            turn_number = 0
            
            while True:
                try:
                    # Get user input
                    user_input = console.input("[bold cyan]You:[/bold cyan] ").strip()
                    
                    # Handle empty input
                    if not user_input:
                        continue
                    
                    # Handle slash commands
                    if user_input.startswith("/"):
                        cmd = user_input.lower()
                        
                        if cmd in ("/exit", "/quit"):
                            console.print("\n[dim]Goodbye![/dim]")
                            break
                        
                        elif cmd == "/clear":
                            conversation_id = None
                            turn_number = 0
                            console.print("[green]✓[/green] Conversation cleared.\n")
                            continue
                        
                        elif cmd == "/sources":
                            if sources_list:
                                console.print("\n[bold]Sources:[/bold]")
                                for i, src in enumerate(sources_list, 1):
                                    title = src.get("title", "Untitled")
                                    stype = src.get("type", "unknown")
                                    console.print(f"  [{i}] {title} [dim]({stype})[/dim]")
                                console.print()
                            else:
                                console.print("[dim]No sources in this notebook.[/dim]\n")
                            continue
                        
                        elif cmd == "/help":
                            console.print(HELP_TEXT)
                            continue
                        
                        else:
                            console.print(f"[yellow]Unknown command:[/yellow] {user_input}")
                            console.print("[dim]Type /help for available commands.[/dim]\n")
                            continue
                    
                    # Query the notebook
                    turn_number += 1
                    
                    with console.status("[dim]Thinking...[/dim]", spinner="dots"):
                        result = client.query(
                            notebook_id,
                            query_text=user_input,
                            conversation_id=conversation_id,
                        )
                    
                    if result:
                        conversation_id = result.get("conversation_id")
                        answer = result.get("answer", "No response.")
                        
                        # Render response with notebook title as label
                        console.print()
                        console.print(f"[bold green]{notebook_title}:[/bold green]")
                        console.print(Markdown(answer))
                        
                        # Parse and display citation legend
                        cited_nums = _parse_citations(answer)
                        citations_map = result.get("citations", {})
                        
                        if cited_nums and sources_list:
                            # Build UUID -> title lookup
                            uuid_to_title = {
                                src.get("id"): src.get("title", "Untitled")
                                for src in sources_list
                            }
                            
                            # Collect unique sources cited
                            cited_sources: dict[str, list[int]] = {}
                            for num in sorted(cited_nums):
                                source_uuid = citations_map.get(num)
                                if source_uuid:
                                    if source_uuid not in cited_sources:
                                        cited_sources[source_uuid] = []
                                    cited_sources[source_uuid].append(num)
                            
                            if cited_sources:
                                console.print()
                                console.print("[dim]" + "─" * 40 + "[/dim]")
                                console.print("[dim]Sources cited:[/dim]")
                                for uuid, nums in cited_sources.items():
                                    title = uuid_to_title.get(uuid, uuid[:8] + "...")
                                    nums_str = ", ".join(f"[{n}]" for n in nums)
                                    console.print(f"[dim]  {nums_str} {title}[/dim]")
                        
                        console.print()
                    else:
                        console.print("[red]No response from AI.[/red]\n")
                
                except KeyboardInterrupt:
                    console.print("\n\n[dim]Interrupted. Type /exit to quit.[/dim]\n")
                    continue
                
                except NLMError as e:
                    console.print(f"\n[red]Error:[/red] {e.message}")
                    if e.hint:
                        console.print(f"[dim]{e.hint}[/dim]")
                    console.print()
                    continue
    
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"[dim]{e.hint}[/dim]")
        raise typer.Exit(1)
    
    except KeyboardInterrupt:
        console.print("\n[dim]Goodbye![/dim]")

```

## File: `src/nlm/cli/research.py`
```python
"""Research CLI commands."""

from typing import Optional

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError

console = Console()
app = typer.Typer(
    help="Research and discover sources",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def get_client(profile: str | None = None) -> NotebookLMClient:
    """Get a client instance."""
    return NotebookLMClient(profile=profile)


@app.command("start")
def start_research(
    query: str = typer.Argument(..., help="What to search for"),
    source: str = typer.Option(
        "web", "--source", "-s",
        help="Where to search: web or drive",
    ),
    mode: str = typer.Option(
        "fast", "--mode", "-m",
        help="Research mode: fast (~30s, ~10 sources) or deep (~5min, ~40 sources, web only)",
    ),
    notebook_id: Optional[str] = typer.Option(
        None, "--notebook-id", "-n",
        help="Add to existing notebook",
    ),
    title: Optional[str] = typer.Option(
        None, "--title", "-t",
        help="Title for new notebook",
    ),
    force: bool = typer.Option(
        False, "--force", "-f",
        help="Start new research even if one is already pending",
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """
    Start a research task to find new sources.
    
    This searches the web or Google Drive to discover relevant sources
    for your research topic. Use 'nlm research status' to check progress
    and 'nlm research import' to add discovered sources to your notebook.
    """
    # Validate source
    if source not in ["web", "drive"]:
        console.print("[red]Error:[/red] Source must be 'web' or 'drive'")
        raise typer.Exit(1)
    
    # Validate mode
    if mode not in ["fast", "deep"]:
        console.print("[red]Error:[/red] Mode must be 'fast' or 'deep'")
        raise typer.Exit(1)
    
    # Validate deep mode restriction
    if mode == "deep" and source != "web":
        console.print("[red]Error:[/red] Deep research mode is only available for web sources")
        console.print("[dim]Use --mode fast for Drive search, or --source web for deep research.[/dim]")
        raise typer.Exit(1)
    
    try:
        # notebook_id is required for research
        if not notebook_id:
            console.print("[red]Error:[/red] --notebook-id is required for research")
            raise typer.Exit(1)
            
        notebook_id = get_alias_manager().resolve(notebook_id)
        
        with get_client(profile) as client:
            # Check for existing research before starting new one
            if not force:
                existing = client.poll_research(notebook_id)
                if existing and existing.get("status") == "in_progress":
                    console.print("[yellow]Warning:[/yellow] Research already in progress for this notebook.")
                    console.print(f"  Task ID: {existing.get('task_id', 'unknown')}")
                    console.print(f"  Sources found so far: {existing.get('source_count', 0)}")
                    console.print("\n[dim]Use --force to start a new research anyway (will overwrite pending results).[/dim]")
                    console.print("[dim]Or run 'nlm research status' to check progress / 'nlm research import' to save results.[/dim]")
                    raise typer.Exit(1)
                elif existing and existing.get("status") == "completed" and existing.get("source_count", 0) > 0:
                    console.print("[yellow]Warning:[/yellow] Previous research completed with sources not yet imported.")
                    console.print(f"  Task ID: {existing.get('task_id', 'unknown')}")
                    console.print(f"  Sources available: {existing.get('source_count', 0)}")
                    console.print("\n[dim]Use --force to start a new research (will discard existing results).[/dim]")
                    console.print("[dim]Or run 'nlm research import' to save the existing results first.[/dim]")
                    raise typer.Exit(1)
            
            task = client.start_research(
                notebook_id=notebook_id,
                query=query,
                source=source,
                mode=mode,
            )
        
        if not task:
            console.print("[red]Error:[/red] Failed to start research")
            raise typer.Exit(1)
        
        console.print("[green]✓[/green] Research started")
        console.print(f"  Query: {query}")
        console.print(f"  Source: {source}")
        console.print(f"  Mode: {mode}")
        console.print(f"  Notebook ID: {notebook_id}")
        console.print(f"  Task ID: {task.get('task_id', 'unknown')}")
        
        estimate = "~30 seconds" if mode == "fast" else "~5 minutes"
        console.print(f"\n[dim]Estimated time: {estimate}[/dim]")
        console.print(f"[dim]Run 'nlm research status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("status")
def research_status(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    task_id: Optional[str] = typer.Option(None, "--task-id", "-t", help="Specific task ID to check"),
    compact: bool = typer.Option(
        True, "--compact/--full",
        help="Show compact or full details",
    ),
    poll_interval: int = typer.Option(
        30, "--poll-interval",
        help="Seconds between status checks",
    ),
    max_wait: int = typer.Option(
        300, "--max-wait",
        help="Maximum seconds to wait (0 for single check)",
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """
    Check research task progress.
    
    By default, polls until the task completes or times out.
    Use --max-wait 0 for a single status check.
    """
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        if task_id:
            task_id = get_alias_manager().resolve(task_id)

        if max_wait > 0:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                progress.add_task("Waiting for research to complete...", total=None)
                
                with get_client(profile) as client:
                    task = client.get_research_status(
                        notebook_id,
                        poll_interval=poll_interval,
                        max_wait=max_wait,
                        compact=compact,
                        task_id=task_id,
                    )
        else:
            with get_client(profile) as client:
                task = client.get_research_status(
                    notebook_id,
                    poll_interval=poll_interval,
                    max_wait=0,
                    compact=compact,
                    task_id=task_id,
                )
        
        # Handle dict response from client
        if isinstance(task, dict):
            status = task.get('status', 'unknown')
            sources_found = task.get('sources_found', task.get('source_count', 0))
            report = task.get('report', '')
            sources = task.get('sources', [])
            all_tasks = task.get('tasks', [])
        else:
            status = getattr(task, 'status', 'unknown')
            sources_found = getattr(task, 'sources_found', 0)
            report = getattr(task, 'report', '')
            sources = getattr(task, 'sources', [])
            all_tasks = []
        
        status_style = {
            "completed": "green",
            "pending": "yellow",
            "running": "yellow",
            "in_progress": "yellow",
            "no_research": "dim",
            "failed": "red",
        }.get(status, "")
        
        console.print(f"\n[bold]Research Status:[/bold]")
        
        # Display all tasks if multiple exist
        if len(all_tasks) > 1:
            console.print(f"  Tasks found: {len(all_tasks)}")
            console.print(f"  Overall status: [{status_style}]{status}[/{status_style}]" if status_style else f"  Overall status: {status}")
            console.print()
            for i, t in enumerate(all_tasks):
                t_status = t.get("status", "unknown")
                t_style = {"completed": "green", "in_progress": "yellow"}.get(t_status, "")
                task_id_str = t.get('task_id', 'unknown')
                console.print(f"  [{i+1}] Task ID: [cyan]{task_id_str}[/cyan]")
                console.print(f"      Status: [{t_style}]{t_status}[/{t_style}]" if t_style else f"      Status: {t_status}")
                console.print(f"      Sources: {t.get('source_count', 0)}")
        else:
            # Show task ID for single task too
            task_id_val = task.get('task_id', '')
            if status_style:
                console.print(f"  Status: [{status_style}]{status}[/{status_style}]")
            if task_id_val:
                console.print(f"  Task ID: [cyan]{task_id_val}[/cyan]")
            else:
                console.print(f"  Status: {status}")
                if task_id_val:
                    console.print(f"  Task ID: [cyan]{task_id_val}[/cyan]")
            console.print(f"  Sources found: {sources_found}")
        
        if report and not compact:
            console.print(f"\n[bold]Report:[/bold]")
            console.print(report)
        
        if sources and not compact:
            console.print(f"\n[bold]Discovered Sources:[/bold]")
            for i, src in enumerate(sources):
                if isinstance(src, dict):
                    title = src.get("title", "Untitled")
                    url = src.get("url", "")
                else:
                    title = getattr(src, 'title', 'Untitled')
                    url = getattr(src, 'url', '')
                console.print(f"  [{i}] {title}")
                if url:
                    console.print(f"      [dim]{url}[/dim]")
        
        if status == "completed":
            console.print(f"\n[dim]Run 'nlm research import {notebook_id} <task-id>' to import sources.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("import")
def import_research(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    task_id: Optional[str] = typer.Argument(None, help="Research task ID (auto-detects if not provided)"),
    indices: Optional[str] = typer.Option(
        None, "--indices", "-i",
        help="Comma-separated indices of sources to import (default: all)",
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """
    Import discovered sources from a completed research task.
    
    If TASK_ID is not provided, automatically imports from the first
    available completed or in-progress research task.
    """
    try:
        source_indices = None
        if indices:
            source_indices = [int(i.strip()) for i in indices.split(",")]
        
        notebook_id = get_alias_manager().resolve(notebook_id)
        
        with get_client(profile) as client:
            # Auto-detect task ID if not provided
            if not task_id:
                research = client.poll_research(notebook_id)
                if not research or research.get("status") == "no_research":
                    console.print("[red]Error:[/red] No research tasks found for this notebook.")
                    console.print("[dim]Start a research task first with 'nlm research start'.[/dim]")
                    raise typer.Exit(1)
                
                # Get task ID from first task
                task_id = research.get("task_id")
                if not task_id:
                    tasks = research.get("tasks", [])
                    if tasks:
                        task_id = tasks[0].get("task_id")
                
                if not task_id:
                    console.print("[red]Error:[/red] Could not determine task ID.")
                    raise typer.Exit(1)
                
                console.print(f"[dim]Using task: {task_id}[/dim]")
            else:
                task_id = get_alias_manager().resolve(task_id)
            
            sources = client.import_research(notebook_id, task_id, source_indices)
        
        console.print(f"[green]✓[/green] Imported {len(sources) if sources else 0} source(s)")
        if sources:
            for src in sources:
                if isinstance(src, dict):
                    console.print(f"  • {src.get('title', 'Unknown')}")
                else:
                    console.print(f"  • {getattr(src, 'title', 'Unknown')}")
    except ValueError as e:
        console.print(f"[red]Error:[/red] Invalid indices. Use comma-separated numbers like: 0,2,5")
        raise typer.Exit(1)
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)
```

## File: `src/nlm/cli/source.py`
```python
"""Source CLI commands."""

from typing import Optional

import typer
from rich.console import Console

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError
from nlm.output.formatters import detect_output_format, get_formatter

console = Console()
app = typer.Typer(
    help="Manage sources",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def get_client(profile: str | None = None) -> NotebookLMClient:
    """Get a client instance."""
    return NotebookLMClient(profile=profile)


@app.command("list")
def list_sources(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    full: bool = typer.Option(False, "--full", "-a", help="Show all columns"),
    drive: bool = typer.Option(False, "--drive", "-d", help="Show Drive sources with freshness status"),
    skip_freshness: bool = typer.Option(False, "--skip-freshness", "-S", help="Skip freshness checks (faster, use with --drive)"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Output IDs only"),
    url: bool = typer.Option(False, "--url", "-u", help="Output as ID: URL"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List sources in a notebook."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            if drive:
                sources = client.list_drive_sources(notebook_id, check_freshness=not skip_freshness)
            else:
                sources = client.list_sources(notebook_id)
        
        fmt = detect_output_format(json_output, quiet, url_flag=url)
        formatter = get_formatter(fmt, console)
        formatter.format_sources(sources, full=full or drive, url_only=url)
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("add")
def add_source(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    url: Optional[str] = typer.Option(None, "--url", "-u", help="URL to add (website or YouTube)"),
    text: Optional[str] = typer.Option(None, "--text", "-t", help="Text content to add"),
    drive: Optional[str] = typer.Option(None, "--drive", "-d", help="Google Drive document ID"),
    youtube: Optional[str] = typer.Option(None, "--youtube", "-y", help="YouTube URL"),
    title: str = typer.Option("", "--title", help="Title for the source"),
    doc_type: str = typer.Option("doc", "--type", help="Drive doc type: doc, slides, sheets, pdf"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Add a source to a notebook."""
    notebook_id = get_alias_manager().resolve(notebook_id)
    
    # Validate that exactly one source type is provided
    source_count = sum(1 for x in [url, text, drive, youtube] if x)
    if source_count == 0:
        console.print("[red]Error:[/red] Please specify a source: --url, --text, --drive, or --youtube")
        raise typer.Exit(1)
    if source_count > 1:
        console.print("[red]Error:[/red] Please specify only one source type at a time")
        raise typer.Exit(1)
    
    try:
        with get_client(profile) as client:
            if url:
                result = client.add_source_url(notebook_id, url)
                source_desc = url
            elif youtube:
                result = client.add_source_url(notebook_id, youtube)
                source_desc = youtube
            elif text:
                result = client.add_source_text(notebook_id, text, title=title or "Pasted Text")
                source_desc = title or "Pasted Text"
            elif drive:
                if not title:
                    title = f"Drive Document ({drive[:8]}...)"
                result = client.add_source_drive(notebook_id, drive, title, doc_type)
                source_desc = title
            else:
                raise typer.Exit(1)  # Should never reach here
        
        # API returns raw result, not a Source object
        if result is not None:
            console.print(f"[green]✓[/green] Added source: {source_desc}")
        else:
            console.print(f"[yellow]⚠[/yellow] Source may have been added (no confirmation from API)")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("get")
def get_source(
    source_id: str = typer.Argument(..., help="Source ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get source details."""
    try:
        source_id = get_alias_manager().resolve(source_id)
        with get_client(profile) as client:
            source = client.get_source(source_id)
        
        fmt = detect_output_format(json_output)
        formatter = get_formatter(fmt, console)
        formatter.format_item(source, title="Source Details")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("describe")
def describe_source(
    source_id: str = typer.Argument(..., help="Source ID"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get AI-generated source summary with keywords."""
    try:
        source_id = get_alias_manager().resolve(source_id)
        with get_client(profile) as client:
            summary = client.describe_source(source_id)
        
        console.print("[bold]Summary:[/bold]")
        console.print(summary.summary)
        
        if summary.keywords:
            console.print("\n[bold]Keywords:[/bold]")
            console.print(", ".join(summary.keywords))
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("content")
def get_source_content(
    source_id: str = typer.Argument(..., help="Source ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Write content to file"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get raw source content (no AI processing)."""
    try:
        source_id = get_alias_manager().resolve(source_id)
        with get_client(profile) as client:
            content = client.get_source_content(source_id)
        
        if output:
            # Write raw content to file
            from pathlib import Path
            Path(output).write_text(content.content)
            console.print(f"[green]✓[/green] Wrote {content.char_count:,} characters to {output}")
        else:
            # Display to console
            console.print(f"[bold]Title:[/bold] {content.title}")
            console.print(f"[bold]Type:[/bold] {content.source_type}")
            console.print(f"[bold]Characters:[/bold] {content.char_count:,}")
            console.print("\n[bold]Content:[/bold]")
            console.print(content.content)
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("delete")
def delete_source(
    source_id: str = typer.Argument(..., help="Source ID"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Delete a source permanently."""
    source_id = get_alias_manager().resolve(source_id)
    
    if not confirm:
        typer.confirm(
            f"Are you sure you want to delete source {source_id}?",
            abort=True,
        )
    
    try:
        with get_client(profile) as client:
            client.delete_source(source_id)
        
        console.print(f"[green]✓[/green] Deleted source: {source_id}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("stale")
def list_stale_sources(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List Drive sources that need syncing."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            sources = client.list_drive_sources(notebook_id)
        
        stale_sources = [s for s in sources if s.is_stale]
        
        if not stale_sources:
            console.print("[green]✓[/green] All Drive sources are up to date.")
            return
        
        console.print(f"[yellow]⚠[/yellow] {len(stale_sources)} source(s) need syncing:")
        
        fmt = detect_output_format(json_output)
        formatter = get_formatter(fmt, console)
        formatter.format_sources(stale_sources, full=True)
        
        console.print("\n[dim]Run 'nlm source sync <notebook-id>' to sync all stale sources.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("sync")
def sync_sources(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    source_ids: Optional[str] = typer.Option(
        None, "--source-ids", "-s",
        help="Comma-separated source IDs to sync (default: all stale)",
    ),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Sync Drive sources with latest content."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        
        with get_client(profile) as client:
            if source_ids:
                ids_to_sync = [get_alias_manager().resolve(sid.strip()) for sid in source_ids.split(",")]
            else:
                # Get all stale sources
                sources = client.list_drive_sources(notebook_id)
                ids_to_sync = [s.id for s in sources if s.is_stale]
        
        if not ids_to_sync:
            console.print("[green]✓[/green] No sources need syncing.")
            return
        
        if not confirm:
            typer.confirm(
                f"Sync {len(ids_to_sync)} source(s)?",
                abort=True,
            )
        
        with get_client(profile) as client:
            client.sync_sources(ids_to_sync)
        
        console.print(f"[green]✓[/green] Synced {len(ids_to_sync)} source(s)")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)
```

## File: `src/nlm/cli/studio.py`
```python
"""Studio CLI commands for generation (audio, report, quiz, etc.)."""

from typing import Optional

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from nlm.core.alias import get_alias_manager
from nlm.core.client import NotebookLMClient
from nlm.core.exceptions import NLMError
from nlm.output.formatters import detect_output_format, get_formatter

console = Console()

# Main studio app for status/delete
app = typer.Typer(
    help="Manage studio artifacts",
    rich_markup_mode="rich",
    no_args_is_help=True,
)

# Individual generation apps
audio_app = typer.Typer(
    help="Create audio overviews",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
report_app = typer.Typer(
    help="Create reports",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
quiz_app = typer.Typer(
    help="Create quizzes",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
flashcards_app = typer.Typer(
    help="Create flashcards",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
mindmap_app = typer.Typer(
    help="Create and manage mind maps",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
slides_app = typer.Typer(
    help="Create slide decks",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
infographic_app = typer.Typer(
    help="Create infographics",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
video_app = typer.Typer(
    help="Create video overviews",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
data_table_app = typer.Typer(
    help="Create data tables",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


def get_client(profile: str | None = None) -> NotebookLMClient:
    """Get a client instance."""
    return NotebookLMClient(profile=profile)


def parse_source_ids(source_ids: str | None) -> list[str] | None:
    """Parse comma-separated source IDs."""
    if source_ids:
        return [get_alias_manager().resolve(s.strip()) for s in source_ids.split(",")]
    return None


# ========== Studio Status/Delete ==========

@app.command("status")
def studio_status(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    full: bool = typer.Option(False, "--full", "-a", help="Show all details"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List all studio artifacts and their status."""
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with get_client(profile) as client:
            artifacts = client.get_studio_status(notebook_id)
        
        fmt = detect_output_format(json_output)
        formatter = get_formatter(fmt, console)
        formatter.format_artifacts(artifacts, full=full)
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


@app.command("delete")
def studio_delete(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    artifact_id: str = typer.Argument(..., help="Artifact ID to delete"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Delete a studio artifact permanently."""
    notebook_id = get_alias_manager().resolve(notebook_id)
    artifact_id = get_alias_manager().resolve(artifact_id)

    if not confirm:
        typer.confirm(f"Are you sure you want to delete artifact {artifact_id}?", abort=True)
    
    try:
        with get_client(profile) as client:
            client.delete_artifact(notebook_id, artifact_id)
        
        console.print(f"[green]✓[/green] Deleted artifact: {artifact_id}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Audio ==========

@audio_app.command("create")
def create_audio(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    format: str = typer.Option(
        "deep_dive", "--format", "-f",
        help="Overview format (deep_dive, brief, critique, debate)",
    ),
    length: str = typer.Option(
        "default", "--length", "-l",
        help="Length (short, default, long)",
    ),
    language: str = typer.Option(
        "en", "--language",
        help="BCP-47 language code (en, es, fr, de, ja)",
    ),
    focus: Optional[str] = typer.Option(
        None, "--focus",
        help="Optional focus topic",
    ),
    source_ids: Optional[str] = typer.Option(
        None, "--source-ids", "-s",
        help="Comma-separated source IDs",
    ),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create an audio overview (podcast) from notebook sources."""
    if not confirm:
        typer.confirm(f"Create {format} audio overview?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating audio...", total=None)
            with get_client(profile) as client:
                result = client.create_audio(
                    notebook_id,
                    format=format,
                    length=length,
                    language=language,
                    focus_prompt=focus,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Audio generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"  Format: {format}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Report ==========

@report_app.command("create")
def create_report(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    format: str = typer.Option(
        "Briefing Doc", "--format", "-f",
        help="Format: 'Briefing Doc', 'Study Guide', 'Blog Post', 'Create Your Own'",
    ),
    prompt: str = typer.Option("", "--prompt", help="Custom prompt (required for 'Create Your Own')"),
    language: str = typer.Option("en", "--language", help="BCP-47 language code"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a report from notebook sources."""
    if format == "Create Your Own" and not prompt:
        console.print("[red]Error:[/red] --prompt is required when format is 'Create Your Own'")
        raise typer.Exit(1)
    
    if not confirm:
        typer.confirm(f"Create '{format}' report?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating report...", total=None)
            with get_client(profile) as client:
                result = client.create_report(
                    notebook_id,
                    report_format=format,
                    custom_prompt=prompt,
                    language=language,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Report generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Quiz ==========

@quiz_app.command("create")
def create_quiz(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    count: int = typer.Option(2, "--count", "-c", help="Number of questions"),
    difficulty: int = typer.Option(2, "--difficulty", "-d", help="Difficulty 1-5 (1=easy, 5=hard)"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a quiz from notebook sources."""
    if not confirm:
        typer.confirm(f"Create quiz with {count} questions?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating quiz...", total=None)
            with get_client(profile) as client:
                result = client.create_quiz(
                    notebook_id,
                    question_count=count,
                    difficulty=difficulty,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Quiz generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Flashcards ==========

@flashcards_app.command("create")
def create_flashcards(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    difficulty: str = typer.Option("medium", "--difficulty", "-d", help="Difficulty: easy, medium, hard"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create flashcards from notebook sources."""
    if not confirm:
        typer.confirm("Create flashcards?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating flashcards...", total=None)
            with get_client(profile) as client:
                result = client.create_flashcards(
                    notebook_id,
                    difficulty=difficulty,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Flashcards generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Mind Map ==========

@mindmap_app.command("create")
def create_mindmap(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    title: str = typer.Option("Mind Map", "--title", "-t", help="Mind map title"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a mind map from notebook sources."""
    if not confirm:
        typer.confirm("Create mind map?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating mind map...", total=None)
            with get_client(profile) as client:
                result = client.create_mindmap(
                    notebook_id,
                    title=title,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Mind map created")
        if result:
            console.print(f"  ID: {result.get('mind_map_id', result.get('artifact_id', 'unknown'))}")
            console.print(f"  Title: {title}")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# Note: mindmap list removed - use 'studio status' which now includes mindmaps


# ========== Slides ==========

@slides_app.command("create")
def create_slides(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    format: str = typer.Option("detailed", "--format", "-f", help="Format: detailed, presenter"),
    length: str = typer.Option("default", "--length", "-l", help="Length: short, default"),
    language: str = typer.Option("en", "--language", help="BCP-47 language code"),
    focus: str = typer.Option("", "--focus", help="Optional focus topic"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a slide deck from notebook sources."""
    if not confirm:
        typer.confirm("Create slide deck?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating slides...", total=None)
            with get_client(profile) as client:
                result = client.create_slides(
                    notebook_id,
                    format=format,
                    length=length,
                    language=language,
                    focus_prompt=focus,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Slide deck generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Infographic ==========

@infographic_app.command("create")
def create_infographic(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    orientation: str = typer.Option("landscape", "--orientation", "-o", help="Orientation: landscape, portrait, square"),
    detail: str = typer.Option("standard", "--detail", "-d", help="Detail level: concise, standard, detailed"),
    language: str = typer.Option("en", "--language", help="BCP-47 language code"),
    focus: str = typer.Option("", "--focus", help="Optional focus topic"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create an infographic from notebook sources."""
    if not confirm:
        typer.confirm("Create infographic?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating infographic...", total=None)
            with get_client(profile) as client:
                result = client.create_infographic(
                    notebook_id,
                    orientation=orientation,
                    detail_level=detail,
                    language=language,
                    focus_prompt=focus,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Infographic generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Video ==========

@video_app.command("create")
def create_video(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    format: str = typer.Option("explainer", "--format", "-f", help="Format: explainer, brief"),
    style: str = typer.Option(
        "auto_select", "--style", "-s",
        help="Visual style: auto_select, classic, whiteboard, kawaii, anime, watercolor, retro_print, heritage, paper_craft",
    ),
    language: str = typer.Option("en", "--language", help="BCP-47 language code"),
    focus: str = typer.Option("", "--focus", help="Optional focus topic"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a video overview from notebook sources."""
    if not confirm:
        typer.confirm("Create video overview?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating video...", total=None)
            with get_client(profile) as client:
                result = client.create_video(
                    notebook_id,
                    format=format,
                    visual_style=style,
                    language=language,
                    focus_prompt=focus,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Video generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)


# ========== Data Table ==========

@data_table_app.command("create")
def create_data_table(
    notebook_id: str = typer.Argument(..., help="Notebook ID"),
    description: str = typer.Argument(..., help="Description of the data table to create"),
    language: str = typer.Option("en", "--language", help="BCP-47 language code"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Create a data table from notebook sources."""
    if not confirm:
        typer.confirm("Create data table?", abort=True)
    
    try:
        notebook_id = get_alias_manager().resolve(notebook_id)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Creating data table...", total=None)
            with get_client(profile) as client:
                result = client.create_data_table(
                    notebook_id,
                    description=description,
                    language=language,
                    source_ids=parse_source_ids(source_ids),
                )
        
        console.print(f"[green]✓[/green] Data table generation started")
        if result:
            console.print(f"  Artifact ID: {result.get('artifact_id', 'unknown')}")
        console.print(f"\n[dim]Run 'nlm studio status {notebook_id}' to check progress.[/dim]")
    except NLMError as e:
        console.print(f"[red]Error:[/red] {e.message}")
        if e.hint:
            console.print(f"\n[dim]Hint: {e.hint}[/dim]")
        raise typer.Exit(1)
```

## File: `src/nlm/core/__init__.py`
```python
"""Core package for NLM."""
```

## File: `src/nlm/core/alias.py`
```python
"""Alias management for NotebookLM CLI."""

import json
from pathlib import Path
from typing import Any

from nlm.utils.config import get_config_dir


class AliasEntry:
    """Represents an alias with its value and type."""
    
    def __init__(self, value: str, alias_type: str = "unknown") -> None:
        self.value = value
        self.type = alias_type
    
    def to_dict(self) -> dict[str, str]:
        return {"value": self.value, "type": self.type}
    
    @classmethod
    def from_dict(cls, data: dict[str, Any] | str) -> "AliasEntry":
        """Create from dict or legacy string format."""
        if isinstance(data, str):
            # Legacy format: just the value
            return cls(value=data, alias_type="unknown")
        return cls(value=data.get("value", ""), alias_type=data.get("type", "unknown"))


class AliasManager:
    """Manages user-defined aliases for IDs."""

    def __init__(self) -> None:
        self.config_dir = get_config_dir()
        self.aliases_file = self.config_dir / "aliases.json"
        self._aliases: dict[str, AliasEntry] = {}
        self._load()

    def _load(self) -> None:
        """Load aliases from disk."""
        if not self.aliases_file.exists():
            return
        
        try:
            content = self.aliases_file.read_text()
            if content:
                raw_data = json.loads(content)
                # Convert to AliasEntry objects (handles legacy format)
                self._aliases = {
                    name: AliasEntry.from_dict(data) 
                    for name, data in raw_data.items()
                }
        except Exception:
            # On error, start with empty map
            self._aliases = {}

    def _save(self) -> None:
        """Save aliases to disk."""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        data = {name: entry.to_dict() for name, entry in self._aliases.items()}
        self.aliases_file.write_text(json.dumps(data, indent=2))

    def set_alias(self, name: str, value: str, alias_type: str = "unknown") -> None:
        """Set an alias with optional type."""
        self._aliases[name] = AliasEntry(value=value, alias_type=alias_type)
        self._save()

    def get_alias(self, name: str) -> str | None:
        """Get an alias value."""
        entry = self._aliases.get(name)
        return entry.value if entry else None
    
    def get_entry(self, name: str) -> AliasEntry | None:
        """Get the full alias entry including type."""
        return self._aliases.get(name)

    def delete_alias(self, name: str) -> bool:
        """Delete an alias. Returns True if deleted."""
        if name in self._aliases:
            del self._aliases[name]
            self._save()
            return True
        return False

    def list_aliases(self) -> dict[str, AliasEntry]:
        """List all aliases with their types."""
        return self._aliases.copy()

    def resolve(self, id_or_alias: str) -> str:
        """
        Resolve an ID or alias to its value.
        If the input matches a known alias, return the aliased value.
        Otherwise return the input as-is.
        """
        entry = self._aliases.get(id_or_alias)
        return entry.value if entry else id_or_alias


# Global instance
_alias_manager: AliasManager | None = None


def get_alias_manager() -> AliasManager:
    """Get the global alias manager instance."""
    global _alias_manager
    if _alias_manager is None:
        _alias_manager = AliasManager()
    return _alias_manager


def detect_id_type(value: str, profile: str | None = None) -> str:
    """
    Detect the type of an ID by trying API calls.
    
    Returns: "notebook", "source", or "unknown"
    """
    from nlm.core.client import NotebookLMClient
    from nlm.core.exceptions import NLMError
    
    try:
        with NotebookLMClient(profile=profile) as client:
            # Try as notebook ID first (most common)
            try:
                notebook = client.get_notebook(value)
                if notebook:
                    return "notebook"
            except NLMError:
                pass
            
            # Try as source ID
            try:
                # Sources need a notebook context, but we can try to get source content
                content = client.get_source_content(value)
                if content:
                    return "source"
            except NLMError:
                pass
            
    except NLMError:
        pass
    
    return "unknown"
```

## File: `src/nlm/core/auth.py`
```python
"""Authentication management for NLM CLI."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from nlm.core.exceptions import AuthenticationError, ProfileNotFoundError
from nlm.utils.browser import (
    cookies_to_header,
    parse_cookies_from_file,
    validate_notebooklm_cookies,
)
from nlm.utils.config import get_profile_dir, get_profiles_dir


class Profile:
    """Represents an authentication profile."""

    def __init__(
        self,
        name: str,
        cookies: dict[str, str],
        csrf_token: str | None = None,
        session_id: str | None = None,
        email: str | None = None,
        last_validated: datetime | None = None,
    ) -> None:
        self.name = name
        self.cookies = cookies
        self.csrf_token = csrf_token
        self.session_id = session_id
        self.email = email
        self.last_validated = last_validated

    def to_dict(self) -> dict[str, Any]:
        """Convert profile to dictionary for serialization."""
        return {
            "name": self.name,
            "cookies": self.cookies,
            "csrf_token": self.csrf_token,
            "session_id": self.session_id,
            "email": self.email,
            "last_validated": self.last_validated.isoformat() if self.last_validated else None,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Profile":
        """Create profile from dictionary."""
        last_validated = None
        if data.get("last_validated"):
            try:
                last_validated = datetime.fromisoformat(data["last_validated"])
            except (ValueError, TypeError):
                pass
        
        return cls(
            name=data.get("name", "default"),
            cookies=data.get("cookies", {}),
            csrf_token=data.get("csrf_token"),
            session_id=data.get("session_id"),
            email=data.get("email"),
            last_validated=last_validated,
        )


class AuthManager:
    """Manages authentication profiles and credentials."""

    def __init__(self, profile_name: str = "default") -> None:
        self.profile_name = profile_name
        self._profile: Profile | None = None

    @property
    def profile_dir(self) -> Path:
        """Get the directory for the current profile."""
        return get_profile_dir(self.profile_name)

    @property
    def cookies_file(self) -> Path:
        """Get the cookies file path."""
        return self.profile_dir / "cookies.json"

    @property
    def metadata_file(self) -> Path:
        """Get the metadata file path."""
        return self.profile_dir / "metadata.json"

    def profile_exists(self) -> bool:
        """Check if the profile exists."""
        return self.cookies_file.exists()

    def load_profile(self, force_reload: bool = False) -> Profile:
        """Load the current profile from disk."""
        if self._profile is not None and not force_reload:
            return self._profile
        
        if not self.profile_exists():
            raise ProfileNotFoundError(self.profile_name)
        
        try:
            cookies = json.loads(self.cookies_file.read_text())
            metadata = {}
            if self.metadata_file.exists():
                metadata = json.loads(self.metadata_file.read_text())
            
            self._profile = Profile(
                name=self.profile_name,
                cookies=cookies,
                csrf_token=metadata.get("csrf_token"),
                session_id=metadata.get("session_id"),
                email=metadata.get("email"),
                last_validated=datetime.fromisoformat(metadata["last_validated"])
                if metadata.get("last_validated") else None,
            )
            return self._profile
        except Exception as e:
            raise AuthenticationError(
                message=f"Failed to load profile '{self.profile_name}': {e}",
                hint="The profile may be corrupted. Try 'nlm login' to re-authenticate.",
            ) from e

    def save_profile(
        self,
        cookies: dict[str, str],
        csrf_token: str | None = None,
        session_id: str | None = None,
        email: str | None = None,
    ) -> Profile:
        """Save credentials to the current profile."""
        self.profile_dir.mkdir(parents=True, exist_ok=True)
        
        # Set restrictive permissions on the directory
        self.profile_dir.chmod(0o700)
        
        # Save cookies
        self.cookies_file.write_text(json.dumps(cookies, indent=2))
        self.cookies_file.chmod(0o600)
        
        # Save metadata
        metadata = {
            "csrf_token": csrf_token,
            "session_id": session_id,
            "email": email,
            "last_validated": datetime.now().isoformat(),
        }
        self.metadata_file.write_text(json.dumps(metadata, indent=2))
        self.metadata_file.chmod(0o600)
        
        self._profile = Profile(
            name=self.profile_name,
            cookies=cookies,
            csrf_token=csrf_token,
            session_id=session_id,
            email=email,
            last_validated=datetime.now(),
        )
        return self._profile

    def delete_profile(self) -> None:
        """Delete the current profile."""
        if self.profile_dir.exists():
            import shutil
            shutil.rmtree(self.profile_dir)
        self._profile = None

    def get_cookies(self) -> dict[str, str]:
        """Get cookies for the current profile."""
        profile = self.load_profile()
        return profile.cookies

    def get_cookie_header(self) -> str:
        """Get Cookie header value for HTTP requests."""
        return cookies_to_header(self.get_cookies())

    def get_headers(self) -> dict[str, str]:
        """Get headers for NotebookLM API requests."""
        profile = self.load_profile()
        headers = {
            "Cookie": cookies_to_header(profile.cookies),
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://notebooklm.google.com",
            "Referer": "https://notebooklm.google.com/",
        }
        if profile.csrf_token:
            headers["X-Goog-Csrf-Token"] = profile.csrf_token
        return headers

    @staticmethod
    def list_profiles() -> list[str]:
        """List all available profiles."""
        profiles_dir = get_profiles_dir()
        if not profiles_dir.exists():
            return []
        return [d.name for d in profiles_dir.iterdir() if d.is_dir()]

    def login_with_file(self, file_path: str | Path) -> Profile:
        """
        Parse cookies from file and save to profile.
        
        Args:
            file_path: Path to file containing cookies.
        
        Returns:
            The saved profile.
        """
        cookies = parse_cookies_from_file(file_path)
        
        if not validate_notebooklm_cookies(cookies):
            raise AuthenticationError(
                message="Parsed cookies don't appear to be valid for NotebookLM",
                hint="Make sure the file contains cookies from a NotebookLM session.",
            )
        
        return self.save_profile(cookies)


def get_auth_manager(profile: str | None = None) -> AuthManager:
    """Get an AuthManager for the specified or default profile."""
    from nlm.utils.config import get_config
    
    if profile is None:
        profile = get_config().auth.default_profile
    
    return AuthManager(profile)
```

## File: `src/nlm/core/auth_refresh.py`
```python
"""Authentication refresh and recovery logic.

Implements a 3-layer recovery strategy for handling expired tokens:
1. Layer 1: Refresh CSRF/session tokens (handled in client.py)
2. Layer 2: Reload cookies from disk (handled here)
3. Layer 3: Headless Chrome auth (handled here)
"""

import time
import subprocess
from pathlib import Path
from typing import Any

from nlm.core.auth import AuthManager, Profile
from nlm.utils.cdp import (
    CDP_DEFAULT_PORT,
    NOTEBOOKLM_URL,
    find_or_create_notebooklm_page,
    get_current_url,
    get_debugger_url,
    get_page_cookies,
    get_page_html,
    is_logged_in,
    is_profile_locked,
    launch_chrome,
    launch_chrome_process,
    extract_csrf_token,
    extract_session_id,
    navigate_to_url,
    get_chrome_path,
)


def has_fresher_tokens_on_disk(profile: Profile, max_age_seconds: int = 300) -> Profile | None:
    """Check if tokens on disk are significantly fresher than the current profile.
    
    This handles the case where the user re-authenticated in another terminal
    running 'nlm login' or the MCP re-authenticated.
    
    Args:
        profile: The in-memory profile currently in use
        max_age_seconds: Threshold to consider on-disk tokens as "fresh" (default 5 mins)
        
    Returns:
        The updated Profile loaded from disk if fresher, otherwise None.
    """
    if not profile or not profile.name:
        return None
        
    auth_manager = AuthManager(profile.name)
    if not auth_manager.profile_exists():
        return None
        
    try:
        disk_profile = auth_manager.load_profile()
        
        # If disk profile has no validation time, we can't compare
        if not disk_profile.last_validated:
            return None
            
        # If current profile has no validation time, disk is fresher
        if not profile.last_validated:
            return disk_profile
            
        # Calculate age difference
        disk_ts = disk_profile.last_validated.timestamp()
        current_ts = profile.last_validated.timestamp()
        
        # If disk is newer by at least 1 second
        if disk_ts > current_ts:
            return disk_profile
            
        # Also check if disk tokens are absolutely "fresh" (less than max_age_seconds old)
        # This helps in cases where we don't have a good base comparison
        if (time.time() - disk_ts) < max_age_seconds:
            return disk_profile
            
    except Exception:
        pass
        
    return None


def run_headless_auth(port: int = 9223, timeout: int = 30) -> dict[str, Any] | None:
    """Run authentication in headless mode (no user interaction).
    
    This only works if the Chrome profile already has saved Google login.
    The Chrome process is automatically terminated after token extraction.
    
    Args:
        port: Chrome DevTools port (use diff port than interactive to avoid conflicts)
        timeout: Maximum time to wait for auth extraction
        
    Returns:
        Dict with keys: cookies, csrf_token, session_id
        Or None if failed
    """
    # 1. Check prerequisites: Chrome exists, profile not locked
    if is_profile_locked():
        # Profile in use interactively - can't use it headlessly
        return None
        
    if not get_chrome_path():
        return None
        
    chrome_process = None
    
    try:
        # 2. Launch headless Chrome
        # We need a subprocess handle to kill it later, but launch_chrome returns bool.
        # So we'll reimplement specific launch logic here for fine-grained control
        # or rely on launch_chrome's behavior and find process by port (less reliable).
        
        # BETTER: Let's reuse launch_chrome but we need to ensure we can kill it.
        # The cdp.launch_chrome uses Popen but doesn't return the process object.
        # We should modify cdp.launch_chrome or create a local version.
        # For now, we'll create a local version that returns the process.
        
        chrome_process = launch_chrome_process(port, headless=True)
        if not chrome_process:
            return None
            
        # 3. Connect and extract
        # Wait for debugger
        debugger_url = None
        for _ in range(5):
            debugger_url = get_debugger_url(port)
            if debugger_url:
                break
            time.sleep(1)
            
        if not debugger_url:
            return None
            
        page = find_or_create_notebooklm_page(port)
        if not page:
            return None
            
        ws_url = page.get("webSocketDebuggerUrl")
        if not ws_url:
            return None
            
        # Navigate if needed
        current_url = page.get("url", "")
        if "notebooklm.google.com" not in current_url:
            navigate_to_url(ws_url, NOTEBOOKLM_URL)
            
        # Check login status
        current_url = get_current_url(ws_url)
        if not is_logged_in(current_url):
            # Not logged in - headless can't do anything
            return None
            
        # Extract everything
        cookies = get_page_cookies(ws_url)
        html = get_page_html(ws_url)
        csrf_token = extract_csrf_token(html)
        session_id = extract_session_id(html)
        
        if not cookies:
            return None
            
        return {
            "cookies": cookies,
            "csrf_token": csrf_token,
            "session_id": session_id
        }
        
    except Exception:
        return None
        
    finally:
        # 4. Clean up: Terminate Chrome
        if chrome_process:
            try:
                chrome_process.terminate()
                chrome_process.wait(timeout=5)
            except Exception:
                try:
                    chrome_process.kill()
                except Exception:
                    pass



```

## File: `src/nlm/core/client.py`
```python
"""NotebookLM API client.

This client uses Google's batchexecute RPC protocol to interact with NotebookLM.
Ported from notebooklm-mcp with matching signatures for easy maintenance.
"""

import json
import os
import re
import time
import urllib.parse
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import httpx

from nlm.core.auth import AuthManager, get_auth_manager
from nlm.core.exceptions import (
    AuthenticationError,
    NetworkError,
    NotFoundError,
    NLMError,
)
from nlm.core.auth_refresh import has_fresher_tokens_on_disk, run_headless_auth
from nlm.core import constants


# ============================================================================
# Constants (ported from MCP)
# ============================================================================

BASE_URL = "https://notebooklm.google.com"
BATCHEXECUTE_URL = f"{BASE_URL}/_/LabsTailwindUi/data/batchexecute"

# Timeout constants
SOURCE_ADD_TIMEOUT = 120.0  # Extended timeout for adding sources (URLs, Drive, etc.)

# Ownership constants
OWNERSHIP_MINE = 1
OWNERSHIP_SHARED = 2


# ============================================================================
# RPC IDs (ported from MCP)
# ============================================================================

class RPC:
    """Known RPC IDs for NotebookLM batchexecute API."""
    
    # Notebook operations
    LIST_NOTEBOOKS = "wXbhsf"
    GET_NOTEBOOK = "rLM1Ne"
    CREATE_NOTEBOOK = "CCqFvf"
    RENAME_NOTEBOOK = "s0tc2d"  # Also used for chat configuration
    DELETE_NOTEBOOK = "WWINqb"
    
    # Source operations
    ADD_SOURCE = "izAoDd"  # URL, text, and Drive sources
    GET_SOURCE = "hizoJc"
    CHECK_FRESHNESS = "yR9Yof"
    SYNC_DRIVE = "FLmJqe"
    DELETE_SOURCE = "tGMBJ"
    
    # Summary operations
    GET_SUMMARY = "VfAZjd"  # Notebook summary
    GET_SOURCE_GUIDE = "tr032e"  # Source summary + keywords
    
    # Research operations
    START_FAST_RESEARCH = "Ljjv0c"
    START_DEEP_RESEARCH = "QA9ei"
    POLL_RESEARCH = "e3bVqc"
    IMPORT_RESEARCH = "LBwxtb"
    
    # Studio operations
    CREATE_STUDIO = "R7cb6c"
    POLL_STUDIO = "gArtLc"
    DELETE_STUDIO = "V5N4be"
    
    # Mind map operations
    GENERATE_MIND_MAP = "yyryJe"
    SAVE_MIND_MAP = "CYK0Xb"
    LIST_MIND_MAPS = "cFji9"
    DELETE_MIND_MAP = "AH0mwd"


@dataclass
class ConversationTurn:
    """Represents a single turn in a conversation (query + response)."""
    query: str
    answer: str
    turn_number: int


@dataclass
class Notebook:
    """Represents a NotebookLM notebook."""
    id: str
    title: str
    source_count: int = 0
    sources: list[dict] | None = None
    is_owned: bool = True
    is_shared: bool = False
    created_at: str | None = None
    modified_at: str | None = None
    
    @property
    def url(self) -> str:
        return f"https://notebooklm.google.com/notebook/{self.id}"
    
    @property
    def ownership(self) -> str:
        return "owned" if self.is_owned else "shared_with_me"


@dataclass
class SourceContent:
    """Represents raw source content data."""
    title: str
    source_type: str
    content: str
    char_count: int


@dataclass
class SourceGuide:
    """Represents AI-generated source guide (summary + keywords)."""
    summary: str
    keywords: list[str]


@dataclass
class DriveSource:
    """Represents a Drive source with sync status."""
    id: str
    title: str
    is_stale: bool
    type: str = "drive"
    original_type: str | None = None



def _parse_timestamp(ts_array: list | None) -> str | None:
    """Convert [seconds, nanoseconds] timestamp array to ISO format string."""
    if not ts_array or not isinstance(ts_array, list) or len(ts_array) < 1:
        return None
    try:
        seconds = ts_array[0]
        if not isinstance(seconds, (int, float)):
            return None
        dt = datetime.fromtimestamp(seconds, tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, OSError, OverflowError):
        return None


def _parse_notebook_data(nb_data: list) -> Notebook | None:
    """Parse raw notebook data array into a Notebook object."""
    if not isinstance(nb_data, list) or len(nb_data) < 3:
        return None
    
    title = nb_data[0] if isinstance(nb_data[0], str) else "Untitled"
    sources_data = nb_data[1] if len(nb_data) > 1 else []
    notebook_id = nb_data[2] if len(nb_data) > 2 else None
    
    if not notebook_id:
        return None
    
    is_owned = True
    is_shared = False
    created_at = None
    modified_at = None
    
    if len(nb_data) > 5 and isinstance(nb_data[5], list) and len(nb_data[5]) > 0:
        metadata = nb_data[5]
        is_owned = metadata[0] == constants.OWNERSHIP_MINE
        if len(metadata) > 1:
            is_shared = bool(metadata[1])
        if len(metadata) > 5:
            modified_at = _parse_timestamp(metadata[5])
        if len(metadata) > 8:
            created_at = _parse_timestamp(metadata[8])
    
    sources = []
    if isinstance(sources_data, list):
        for src in sources_data:
            if isinstance(src, list) and len(src) >= 2:
                src_ids = src[0] if src[0] else []
                src_title = src[1] if len(src) > 1 else "Untitled"
                src_id = src_ids[0] if isinstance(src_ids, list) and src_ids else src_ids
                
                # Extract source type and URL from metadata
                source_type = "unknown"
                url = ""
                
                if len(src) > 2 and isinstance(src[2], list):
                    metadata = src[2]
                    type_code = None
                    if len(metadata) > 4:
                        type_code = metadata[4]
                        source_type = constants.SOURCE_TYPES.get_name(type_code)
                    
                    # Extract URL based on source type
                    # YouTube (type 9): URL at metadata[5][0]
                    # Web pages (type 5): URL at metadata[7][0]
                    # Drive docs (types 1,2,14): Drive ID at metadata[9][0]
                    if type_code == constants.SOURCE_TYPE_YOUTUBE:
                        if len(metadata) > 5 and isinstance(metadata[5], list) and len(metadata[5]) > 0:
                            potential_url = metadata[5][0]
                            if isinstance(potential_url, str):
                                url = potential_url
                    elif type_code == constants.SOURCE_TYPE_WEB_PAGE:
                        if len(metadata) > 7 and isinstance(metadata[7], list) and len(metadata[7]) > 0:
                            potential_url = metadata[7][0]
                            if isinstance(potential_url, str):
                                url = potential_url
                    elif type_code in (constants.SOURCE_TYPE_GOOGLE_DOCS, constants.SOURCE_TYPE_GOOGLE_OTHER, constants.SOURCE_TYPE_WORD_DOC):
                        # Drive document ID is at metadata[9][0]
                        if len(metadata) > 9 and isinstance(metadata[9], list) and len(metadata[9]) > 0:
                            drive_id = metadata[9][0]
                            if isinstance(drive_id, str):
                                url = f"https://drive.google.com/file/d/{drive_id}/view"
                
                sources.append({
                    "id": src_id, 
                    "title": src_title, 
                    "type": source_type,
                    "url": url
                })
    
    return Notebook(
        id=notebook_id,
        title=title,
        source_count=len(sources),
        sources=sources,
        is_owned=is_owned,
        is_shared=is_shared,
        created_at=created_at,
        modified_at=modified_at,
    )


# ============================================================================
# Client class (matching MCP signatures)
# ============================================================================


class NotebookLMClient:
    """Client for interacting with the NotebookLM API.
    
    Uses Google's batchexecute RPC protocol. Method signatures match
    notebooklm-mcp for easy maintenance.
    """
    
    # Query endpoint (different from batchexecute - streaming gRPC-style)
    QUERY_ENDPOINT = "/_/LabsTailwindUi/data/google.internal.labs.tailwind.orchestration.v1.LabsTailwindOrchestrationService/GenerateFreeFormStreamed"
    
    # Headers for page fetch
    _PAGE_FETCH_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
    }
    
    def __init__(
        self,
        auth_manager: AuthManager | None = None,
        profile: str | None = None,
        cookies: dict[str, str] | None = None,
        csrf_token: str = "",
        session_id: str = "",
    ) -> None:
        """
        Initialize the client.
        
        Args:
            auth_manager: AuthManager instance (preferred).
            profile: Profile name to use (creates AuthManager if auth_manager not provided).
            cookies: Dict of cookies (alternative to auth_manager, for MCP compatibility).
            csrf_token: CSRF token (optional - auto-extracted if not provided).
            session_id: Session ID (optional - auto-extracted if not provided).
        """
        # Support both AuthManager and direct cookies (for MCP compatibility)
        if auth_manager:
            self.auth = auth_manager
            self.cookies = auth_manager.get_cookies()
            self.csrf_token = csrf_token or (auth_manager.load_profile().csrf_token or "")
            self._session_id = session_id or (auth_manager.load_profile().session_id or "")
        elif cookies:
            self.auth = None
            self.cookies = cookies
            self.csrf_token = csrf_token
            self._session_id = session_id
        else:
            self.auth = get_auth_manager(profile)
            self.cookies = self.auth.get_cookies()
            profile_obj = self.auth.load_profile()
            self.csrf_token = csrf_token or (profile_obj.csrf_token or "")
            self._session_id = session_id or (profile_obj.session_id or "")
        
        self._client: httpx.Client | None = None
        
        # Conversation cache for follow-up queries
        self._conversation_cache: dict[str, list[ConversationTurn]] = {}
        
        # Request counter for query endpoint
        import random
        self._reqid_counter = random.randint(100000, 999999)
        
        # Refresh CSRF token if not provided
        if not self.csrf_token:
            self._refresh_auth_tokens()
    
    def close(self) -> None:
        """Close the HTTP client."""
        if self._client is not None:
            self._client.close()
            self._client = None
    
    def __enter__(self) -> "NotebookLMClient":
        return self
    
    def __exit__(self, *args: Any) -> None:
        self.close()
    
    # =========================================================================
    # Core RPC Infrastructure (ported from MCP)
    # =========================================================================
    
    def _refresh_auth_tokens(self) -> None:
        """Refresh CSRF token and session ID by fetching NotebookLM page."""
        cookie_header = "; ".join(f"{k}={v}" for k, v in self.cookies.items())
        headers = {**self._PAGE_FETCH_HEADERS, "Cookie": cookie_header}
        
        with httpx.Client(headers=headers, follow_redirects=True, timeout=15.0) as client:
            response = client.get(f"{BASE_URL}/")
            
            if "accounts.google.com" in str(response.url):
                raise AuthenticationError(
                    message="Cookies have expired",
                    hint="Run 'nlm login' to re-authenticate.",
                )
            
            if response.status_code != 200:
                raise NetworkError(
                    message=f"Failed to fetch NotebookLM page: HTTP {response.status_code}",
                    hint="Check your internet connection.",
                )
            
            html = response.text
            
            # Extract CSRF token (SNlM0e)
            csrf_match = re.search(r'"SNlM0e":"([^"]+)"', html)
            if csrf_match:
                self.csrf_token = csrf_match.group(1)
            
            # Extract session ID (FdrFJe)
            sid_match = re.search(r'"FdrFJe":"([^"]+)"', html)
            if sid_match:
                self._session_id = sid_match.group(1)
            
            # Update profile if we have auth manager
            if self.auth and self.csrf_token:
                try:
                    self.auth.save_profile(
                        cookies=self.cookies,
                        csrf_token=self.csrf_token,
                        session_id=self._session_id,
                    )
                except Exception:
                    pass  # Caching is optional
    
    def _get_client(self) -> httpx.Client:
        """Get or create HTTP client."""
        if self._client is None:
            cookie_str = "; ".join(f"{k}={v}" for k, v in self.cookies.items())
            self._client = httpx.Client(
                headers={
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Origin": BASE_URL,
                    "Referer": f"{BASE_URL}/",
                    "Cookie": cookie_str,
                    "X-Same-Domain": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                },
                timeout=30.0,
            )
        return self._client
    
    def _build_request_body(self, rpc_id: str, params: Any) -> str:
        """Build the batchexecute request body."""
        params_json = json.dumps(params, separators=(',', ':'))
        f_req = [[[rpc_id, params_json, None, "generic"]]]
        f_req_json = json.dumps(f_req, separators=(',', ':'))
        
        body_parts = [f"f.req={urllib.parse.quote(f_req_json, safe='')}"]
        if self.csrf_token:
            body_parts.append(f"at={urllib.parse.quote(self.csrf_token, safe='')}")
        
        return "&".join(body_parts) + "&"
    
    def _build_url(self, rpc_id: str, source_path: str = "/") -> str:
        """Build the batchexecute URL with query params."""
        params = {
            "rpcids": rpc_id,
            "source-path": source_path,
            "bl": os.environ.get("NOTEBOOKLM_BL", "boq_labs-tailwind-frontend_20260108.06_p0"),
            "hl": "en",
            "rt": "c",
        }
        if self._session_id:
            params["f.sid"] = self._session_id
        
        query = urllib.parse.urlencode(params)
        return f"{BATCHEXECUTE_URL}?{query}"
    
    def _parse_response(self, response_text: str) -> list:
        """Parse the batchexecute response."""
        # Remove anti-XSSI prefix
        if response_text.startswith(")]}'"):
            response_text = response_text[4:]
        
        lines = response_text.strip().split("\n")
        results = []
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            
            try:
                int(line)  # byte count
                i += 1
                if i < len(lines):
                    try:
                        data = json.loads(lines[i])
                        results.append(data)
                    except json.JSONDecodeError:
                        pass
                i += 1
            except ValueError:
                try:
                    data = json.loads(line)
                    results.append(data)
                except json.JSONDecodeError:
                    pass
                i += 1
        
        return results
    
    def _extract_rpc_result(self, parsed_response: list, rpc_id: str) -> Any:
        """Extract the result for a specific RPC ID from parsed response."""
        for chunk in parsed_response:
            if isinstance(chunk, list):
                for item in chunk:
                    if isinstance(item, list) and len(item) >= 3:
                        if item[0] == "wrb.fr" and item[1] == rpc_id:
                            # Check for generic error signature (e.g. auth expired)
                            # Signature: ["wrb.fr", "RPC_ID", null, null, null, [16], "generic"]
                            if len(item) > 6 and item[6] == "generic" and isinstance(item[5], list) and 16 in item[5]:
                                from nlm.core.exceptions import AuthenticationError
                                raise AuthenticationError(
                                    message="Unable to fetch data - authentication may have expired (Code 16)",
                                    hint="Run 'nlm login' to re-authenticate."
                                )

                            result_str = item[2]
                            if isinstance(result_str, str):
                                try:
                                    return json.loads(result_str)
                                except json.JSONDecodeError:
                                    return result_str
                            return result_str
        return None
    
    def _call_rpc(
        self,
        rpc_id: str,
        params: Any,
        path: str = "/",
        timeout: float | None = None,
        _retry: bool = False,
        _deep_retry: bool = False,
    ) -> Any:
        """Execute an RPC call and return the extracted result.
        
        Includes automatic retry on auth failures with three-layer recovery:
        1. Refresh CSRF/session tokens (fast, handles token expiry)
        2. Reload cookies from disk (handles external re-authentication)
        3. Run headless auth (auto-refresh if Chrome profile has saved login)
        """
        from nlm.core.exceptions import AuthenticationError
        
        client = self._get_client()
        body = self._build_request_body(rpc_id, params)
        url = self._build_url(rpc_id, path)
        
        try:
            if timeout:
                response = client.post(url, content=body, timeout=timeout)
            else:
                response = client.post(url, content=body)
            
            response.raise_for_status()
            
            # Parse and extract RPC result (may raise AuthenticationError on Code 16)
            parsed = self._parse_response(response.text)
            result = self._extract_rpc_result(parsed, rpc_id)
            
            # Check for null result on list_notebooks (another auth failure symptom)
            if result is None and rpc_id == RPC.LIST_NOTEBOOKS:
                raise AuthenticationError(
                    message="Unable to fetch notebooks - authentication may have expired",
                    hint="Run 'nlm login' to re-authenticate.",
                )
            
            return result
            
        except (httpx.HTTPStatusError, AuthenticationError) as e:
            # Check for auth failures (401/403 HTTP or RPC Error 16)
            is_http_auth = isinstance(e, httpx.HTTPStatusError) and e.response.status_code in (401, 403)
            is_rpc_auth = isinstance(e, AuthenticationError)
            
            if not (is_http_auth or is_rpc_auth):
                if isinstance(e, httpx.RequestError):
                    raise NetworkError(
                        message=f"Request failed: {e}",
                        hint="Check your internet connection.",
                    ) from e
                raise

            # Layer 1: Refresh CSRF/session tokens (first retry only)
            if not _retry:
                try:
                    self._refresh_auth_tokens()
                    self._client = None
                    return self._call_rpc(rpc_id, params, path, timeout, _retry=True)
                except Exception:
                    # CSRF refresh failed (cookies expired) - continue to layer 2
                    pass
            
            # Layer 2 & 3: Reload from disk or run headless auth (deep retry)
            if not _deep_retry and self.auth:
                if self._try_reload_or_headless_auth():
                    self._client = None
                    # Update internal auth state from profile
                    profile = self.auth.load_profile(force_reload=True)
                    self.cookies = profile.cookies
                    self.csrf_token = profile.csrf_token
                    self._session_id = profile.session_id
                    
                    return self._call_rpc(
                        rpc_id, params, path, timeout, _retry=True, _deep_retry=True
                    )
            
            # Re-raise if already retried or recovery failed
            if is_http_auth:
                raise AuthenticationError(
                    message="Authentication failed or session expired",
                    hint="Your session has expired. Run 'nlm login' to re-authenticate.",
                ) from e
            raise
            
        except httpx.RequestError as e:
            raise NetworkError(
                message=f"Request failed: {e}",
                hint="Check your internet connection.",
            ) from e

    def _try_reload_or_headless_auth(self) -> bool:
        """Try to recover authentication by reloading from disk or running headless auth.
        
        Returns:
             True if new valid tokens were obtained and saved to profile.
        """
        if not self.auth:
            return False
            
        # Layer 2: Check if disk has fresher tokens
        try:
            current_profile = self.auth.load_profile()
            fresher = has_fresher_tokens_on_disk(current_profile)
            if fresher:
                # AuthManager handles the loading, so we just need to report success
                # The caller will reload the profile from disk
                return True
        except Exception:
            pass
            
        # Layer 3: Headless Chrome Auth
        try:
            tokens = run_headless_auth()
            if tokens:
                # Save new tokens to profile
                self.auth.save_profile(
                    cookies=tokens["cookies"],
                    csrf_token=tokens["csrf_token"],
                    session_id=tokens["session_id"],
                )
                return True
        except Exception:
            pass
            
        return False
    
    # =========================================================================
    # Notebook Operations (matching MCP signatures)
    # =========================================================================
    
    def list_notebooks(self, debug: bool = False) -> list[Notebook]:
        """List all notebooks."""
        params = [None, 1, None, [2]]
        result = self._call_rpc(RPC.LIST_NOTEBOOKS, params)
        
        notebooks = []
        if result and isinstance(result, list):
            notebook_list = result[0] if result and isinstance(result[0], list) else result
            
            for nb_data in notebook_list:
                notebook = _parse_notebook_data(nb_data)
                if notebook:
                    notebooks.append(notebook)
        
        return notebooks
    
    def get_notebook(self, notebook_id: str) -> Notebook | None:
        """Get notebook details."""
        result = self._call_rpc(
            RPC.GET_NOTEBOOK,
            [notebook_id, None, [2], None, 0],
            f"/notebook/{notebook_id}",
        )
        
        # Result is [[notebook_data]] - extract the inner list
        if result and isinstance(result, list) and len(result) > 0:
            nb_data = result[0]
            return _parse_notebook_data(nb_data)
        return None
    
    def create_notebook(self, title: str = "") -> Notebook | None:
        """Create a new notebook."""
        params = [title, None, None, [2], [1, None, None, None, None, None, None, None, None, None, [1]]]
        result = self._call_rpc(RPC.CREATE_NOTEBOOK, params)
        
        if result and isinstance(result, list) and len(result) >= 3:
            notebook_id = result[2]
            if notebook_id:
                return Notebook(
                    id=notebook_id,
                    title=title or "Untitled notebook",
                    source_count=0,
                    sources=[],
                )
        return None
    
    def rename_notebook(self, notebook_id: str, new_title: str) -> bool:
        """Rename a notebook."""
        params = [notebook_id, [[None, None, None, [None, new_title]]]]
        result = self._call_rpc(RPC.RENAME_NOTEBOOK, params, f"/notebook/{notebook_id}")
        return result is not None
    
    def delete_notebook(self, notebook_id: str) -> bool:
        """Delete a notebook."""
        params = [[notebook_id], [2]]
        result = self._call_rpc(RPC.DELETE_NOTEBOOK, params)
        return result is not None
    
    def get_notebook_summary(self, notebook_id: str) -> dict[str, Any]:
        """Get AI-generated summary and suggested topics for a notebook."""
        result = self._call_rpc(RPC.GET_SUMMARY, [notebook_id, [2]], f"/notebook/{notebook_id}")
        
        summary = ""
        suggested_topics = []
        
        if result and isinstance(result, list):
            if len(result) > 0 and isinstance(result[0], list) and len(result[0]) > 0:
                summary = result[0][0]
            
            if len(result) > 1 and result[1]:
                topics_data = result[1][0] if isinstance(result[1], list) and len(result[1]) > 0 else []
                for topic in topics_data:
                    if isinstance(topic, list) and len(topic) >= 2:
                        suggested_topics.append({
                            "question": topic[0],
                            "prompt": topic[1],
                        })
        
        return {
            "summary": summary,
            "suggested_topics": suggested_topics,
        }
    
    # =========================================================================
    # Source Operations (matching MCP signatures)
    # =========================================================================
    
    def list_sources(self, notebook_id: str) -> list[dict]:
        """List all sources in a notebook."""
        notebook = self.get_notebook(notebook_id)
        
        if notebook and notebook.sources:
            # Add 'type' field if missing (sources from Notebook don't have type)
            sources = []
            for src in notebook.sources:
                sources.append({
                    "id": src.get("id", ""),
                    "title": src.get("title", "Untitled"),
                    "type": src.get("type", "unknown"),
                    "url": src.get("url", ""),
                })
            return sources
        
        return []
    
    def add_source_url(self, notebook_id: str, url: str, timeout: float | None = None) -> dict | None:
        """Add a URL source to a notebook.
        
        Uses extended timeout (120s) by default for slow-loading URLs.
        """
        if timeout is None:
            timeout = SOURCE_ADD_TIMEOUT
        
        # YouTube URLs use different position than regular URLs
        is_youtube = "youtube.com" in url or "youtu.be" in url
        
        if is_youtube:
            source_data = [None, None, None, None, None, None, None, [url], None, None, 1]
        else:
            source_data = [None, None, [url], None, None, None, None, None, None, None, 1]
        
        params = [[source_data], notebook_id, [2], [1, None, None, None, None, None, None, None, None, None, [1]]]
        return self._call_rpc(RPC.ADD_SOURCE, params, f"/notebook/{notebook_id}", timeout=timeout)
    
    def add_source_text(self, notebook_id: str, text: str, title: str = "Pasted Text", timeout: float | None = None) -> dict | None:
        """Add a text source to a notebook.
        
        Uses extended timeout (120s) by default for large text sources.
        """
        if timeout is None:
            timeout = SOURCE_ADD_TIMEOUT
        
        source_data = [None, [title, text], None, 2, None, None, None, None, None, None, 1]
        params = [[source_data], notebook_id, [2], [1, None, None, None, None, None, None, None, None, None, [1]]]
        return self._call_rpc(RPC.ADD_SOURCE, params, f"/notebook/{notebook_id}", timeout=timeout)
    
    def add_source_drive(
        self,
        notebook_id: str,
        document_id: str,
        title: str,
        doc_type: str = "doc",
        timeout: float | None = None,
    ) -> dict | None:
        """Add a Google Drive document as a source.
        
        Uses extended timeout (120s) by default for large files like presentations.
        """
        # Use extended timeout for Drive sources (large files can take 60s+)
        if timeout is None:
            timeout = SOURCE_ADD_TIMEOUT
        mime_types = {
            "doc": "application/vnd.google-apps.document",
            "slides": "application/vnd.google-apps.presentation",
            "sheets": "application/vnd.google-apps.spreadsheet",
            "pdf": "application/pdf",
        }
        mime_type = mime_types.get(doc_type, mime_types["doc"])
        
        source_data = [[document_id, mime_type, 1, title], None, None, None, None, None, None, None, None, None, 1]
        params = [[source_data], notebook_id, [2], [1, None, None, None, None, None, None, None, None, None, [1]]]
        return self._call_rpc(RPC.ADD_SOURCE, params, f"/notebook/{notebook_id}", timeout=timeout)
    
    def get_source(self, source_id: str) -> dict | None:
        """Get source details."""
        params = [[source_id], [2], [2]]
        return self._call_rpc(RPC.GET_SOURCE, params)
    
    def get_source_guide(self, source_id: str) -> "SourceGuide":
        """Get AI-generated summary and keywords for a source."""
        result = self._call_rpc(RPC.GET_SOURCE_GUIDE, [[[[source_id]]]])
        
        summary = ""
        keywords = []
        
        if result and isinstance(result, list):
            if len(result) > 0 and isinstance(result[0], list):
                if len(result[0]) > 0 and isinstance(result[0][0], list):
                    inner = result[0][0]
                    if len(inner) > 1 and isinstance(inner[1], list) and len(inner[1]) > 0:
                        summary = inner[1][0]
                    if len(inner) > 2 and isinstance(inner[2], list) and len(inner[2]) > 0:
                        keywords = inner[2][0] if isinstance(inner[2][0], list) else []
        
        return SourceGuide(summary=summary, keywords=keywords)
    
    def describe_source(self, source_id: str) -> "SourceGuide":
        """Alias for get_source_guide (for CLI compatibility)."""
        return self.get_source_guide(source_id)
    
    def get_source_content(self, source_id: str) -> "SourceContent":
        """Get raw text content of a source (no AI processing).
        
        Returns the original indexed text from PDFs, web pages, pasted text,
        or YouTube transcripts.
        """
        params = [[source_id], [2], [2]]
        result = self._call_rpc(RPC.GET_SOURCE, params, "/")
        
        content = ""
        title = ""
        source_type = ""
        url = None
        
        if result and isinstance(result, list):
            # Extract from result[0] which contains source metadata
            if len(result) > 0 and isinstance(result[0], list):
                source_meta = result[0]
                
                # Title is at position 1
                if len(source_meta) > 1 and isinstance(source_meta[1], str):
                    title = source_meta[1]
                
                # Metadata is at position 2
                if len(source_meta) > 2 and isinstance(source_meta[2], list):
                    metadata = source_meta[2]
                    # Source type code is at position 4
                    if len(metadata) > 4:
                        type_code = metadata[4]
                        source_type = constants.SOURCE_TYPES.get_name(type_code)
                    
                    # URL might be at position 7 for web sources
                    if len(metadata) > 7 and isinstance(metadata[7], list):
                        url_info = metadata[7]
                        if len(url_info) > 0 and isinstance(url_info[0], str):
                            url = url_info[0]
            
            # Extract content from result[3][0] - array of content blocks
            if len(result) > 3 and isinstance(result[3], list):
                content_wrapper = result[3]
                if len(content_wrapper) > 0 and isinstance(content_wrapper[0], list):
                    content_blocks = content_wrapper[0]
                    # Collect all text from content blocks
                    text_parts = []
                    for block in content_blocks:
                        if isinstance(block, list):
                            texts = self._extract_all_text(block)
                            text_parts.extend(texts)
                    content = "\n\n".join(text_parts)
        
        return SourceContent(
            title=title,
            source_type=source_type,
            content=content,
            char_count=len(content),
        )
    
    def _extract_all_text(self, data: list) -> list[str]:
        """Recursively extract all text strings from nested arrays."""
        texts = []
        for item in data:
            if isinstance(item, str) and len(item) > 0:
                texts.append(item)
            elif isinstance(item, list):
                texts.extend(self._extract_all_text(item))
        return texts
    
    def delete_source(self, source_id: str) -> bool:
        """Delete a source."""
        params = [[[source_id]], [2]]
        result = self._call_rpc(RPC.DELETE_SOURCE, params)
        return result is not None
    
    def list_drive_sources(self, notebook_id: str, check_freshness: bool = True) -> list[DriveSource]:
        """List all Drive sources and their freshness status.
        
        Args:
            notebook_id: The notebook to list Drive sources from.
            check_freshness: If True (default), check freshness for each source.
                           If False, skip freshness checks for faster listing.
        """
        sources = self.list_sources(notebook_id)
        drive_sources = []
        
        for s in sources:
            # Check freshness for potential Drive sources
            # Only check explicit 'drive' type per user request
            stype = s.get("type", "unknown")
            valid_drive_types = ["google_docs", "google_slides_sheets", "pdf", "drive"]
            if stype not in valid_drive_types:
                continue
            
            # Determine staleness
            if check_freshness:
                # check_source_freshness returns True if fresh (not stale)
                is_fresh = self.check_source_freshness(s["id"])
                # If explicit False, it's stale. If None/True, assume fresh.
                is_stale = (is_fresh is False)
            else:
                # Skip freshness check - assume unknown (not stale)
                is_stale = False
            
            drive_sources.append(DriveSource(
                id=s["id"],
                title=s.get("title", "Untitled"),
                is_stale=is_stale,
                type=stype,
            ))
            
        return drive_sources

    def sync_sources(self, source_ids: list[str]) -> int:
        """Sync multiple sources. Returns number of successful syncs."""
        count = 0
        for sid in source_ids:
            if self.sync_drive_source(sid):
                count += 1
        return count

    def check_source_freshness(self, source_id: str) -> bool:
        """Check if a Drive source is fresh (True) or stale (False)."""
        params = [None, [source_id], [2]]
        result = self._call_rpc(RPC.CHECK_FRESHNESS, params)
        
        # Result is like [[None, True, ['id']]]
        if result and isinstance(result, list) and len(result) > 0:
            inner = result[0]
            if isinstance(inner, list) and len(inner) > 1:
                return inner[1] is True
                
        # If parsing fails, conservatively assume fresh to avoid false positives
        return True
    
    def sync_drive_source(self, source_id: str) -> bool:
        """Sync a Drive source with latest content."""
        params = [None, [source_id], [2]]
        result = self._call_rpc(RPC.SYNC_DRIVE, params)
        return result is not None
    
    # =========================================================================
    # Chat Configuration (matching MCP signatures)
    # =========================================================================
    
    def configure_chat(
        self,
        notebook_id: str,
        goal: str = "default",
        custom_prompt: str | None = None,
        response_length: str = "default",
    ) -> dict[str, Any]:
        """Configure notebook chat settings."""
        goal_code = constants.CHAT_GOALS.get_code(goal)
        length_code = constants.CHAT_RESPONSE_LENGTHS.get_code(response_length)
        
        if goal == "custom" and custom_prompt:
            goal_setting = [goal_code, custom_prompt]
        else:
            goal_setting = [goal_code]
        
        params = [notebook_id, [[None, None, None, None, None, None, None, [goal_setting, [length_code]]]]]
        result = self._call_rpc(RPC.RENAME_NOTEBOOK, params, f"/notebook/{notebook_id}")
        
        return {
            "goal": goal,
            "custom_prompt": custom_prompt,
            "response_length": response_length,
            "success": result is not None,
        }
    
    # =========================================================================
    # Studio Operations (matching MCP signatures)
    # =========================================================================
    
    def create_audio(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        format: str = "deep_dive",
        length: str = "default",
        format_code: int | None = None,
        length_code: int | None = None,
        language: str = "en",
        focus_prompt: str = "",
    ) -> dict | None:
        """Create an Audio Overview from notebook sources.
        
        Accepts either string format/length or integer codes.
        If source_ids not provided, uses all sources from notebook.
        """
        # Get source IDs if not provided
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating audio.")
        
        # Convert string format to code
        # Convert string format to code
        if format_code is None:
            format_code = constants.AUDIO_FORMATS.get_code(format)
        
        # Convert string length to code
        if length_code is None:
            length_code = constants.AUDIO_LENGTHS.get_code(length)
        
        sources_nested = [[[sid]] for sid in source_ids]
        sources_simple = [[sid] for sid in source_ids]  # For audio_options
        
        # Audio options structure from reference MCP
        audio_options = [
            None,
            [
                focus_prompt,
                length_code,
                None,
                sources_simple,
                language,
                None,
                format_code
            ]
        ]
        
        params = [
            [2],
            notebook_id,
            [None, None, constants.STUDIO_TYPE_AUDIO, sources_nested, None, None, audio_options]
        ]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "audio",
                "status": "in_progress",
            }
        return None
    
    def create_video(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        format: str = "explainer",
        visual_style: str = "auto_select",
        format_code: int | None = None,
        visual_style_code: int | None = None,
        language: str = "en",
        focus_prompt: str = "",
    ) -> dict | None:
        """Create a Video Overview from notebook sources."""
        # Get source IDs if not provided
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating video.")
        
        # Convert string format to code
        # Convert string format to code
        if format_code is None:
            format_code = constants.VIDEO_FORMATS.get_code(format)
        
        if visual_style_code is None:
            visual_style_code = constants.VIDEO_STYLES.get_code(visual_style)
        
        sources_nested = [[[sid]] for sid in source_ids]
        sources_simple = [[sid] for sid in source_ids]  # For video_options
        
        # Video options structure from reference MCP
        video_options = [
            None, None,
            [
                sources_simple,
                language,
                focus_prompt,
                None,
                format_code,
                visual_style_code
            ]
        ]
        
        params = [
            [2],
            notebook_id,
            [None, None, constants.STUDIO_TYPE_VIDEO, sources_nested, None, None, None, None, video_options]
        ]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "video",
                "status": "in_progress",
            }
        return None
    
    def create_report(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        report_format: str = "Briefing Doc",
        custom_prompt: str = "",
        language: str = "en",
    ) -> dict | None:
        """Create a Report from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating report.")
        
        sources_nested = [[[sid]] for sid in source_ids]
        sources_simple = [[sid] for sid in source_ids]  # For report_options
        
        # Format configs from reference MCP
        format_configs = {
            "Briefing Doc": {
                "title": "Briefing Doc",
                "description": "Key insights and important quotes",
                "prompt": "Create a comprehensive briefing document that includes an Executive Summary, detailed analysis of key themes, important quotes with context, and actionable insights.",
            },
            "Study Guide": {
                "title": "Study Guide",
                "description": "Short-answer quiz, essay questions, glossary",
                "prompt": "Create a comprehensive study guide that includes key concepts, short-answer practice questions, essay prompts for deeper exploration, and a glossary of important terms.",
            },
            "Blog Post": {
                "title": "Blog Post",
                "description": "Insightful takeaways in readable article format",
                "prompt": "Write an engaging blog post that presents the key insights in an accessible, reader-friendly format.",
            },
            "Create Your Own": {
                "title": "Custom Report",
                "description": "Custom format",
                "prompt": custom_prompt or "Create a report based on the provided sources.",
            },
        }
        
        config = format_configs.get(report_format, format_configs["Briefing Doc"])
        
        # Report options structure from reference MCP
        report_options = [
            None,
            [
                config["title"],
                config["description"],
                None,
                sources_simple,
                language,
                config["prompt"],
                None,
                True
            ]
        ]
        
        params = [
            [2],
            notebook_id,
            [None, None, constants.STUDIO_TYPE_REPORT, sources_nested, None, None, None, report_options]
        ]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "report",
                "status": "in_progress",
            }
        return None
    
    def create_quiz(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        question_count: int = 2,
        difficulty: int = 2,
    ) -> dict | None:
        """Create a quiz from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating quiz.")
        
        sources_nested = [[[sid]] for sid in source_ids]
        
        # Quiz options from reference MCP - uses FLASHCARDS type (4) with quiz variant
        quiz_options = [
            None,
            [
                2,  # Format/variant code for quiz
                None, None, None, None, None, None,
                [question_count, difficulty]
            ]
        ]
        
        content = [
            None, None,
            constants.STUDIO_TYPE_FLASHCARDS,  # Type 4 (shared with flashcards)
            sources_nested,
            None, None, None, None, None,
            quiz_options  # position 9
        ]
        
        params = [[2], notebook_id, content]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "quiz",
                "status": "in_progress",
            }
        return None
    
    def create_flashcards(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        difficulty: str = "medium",
    ) -> dict | None:
        """Create flashcards from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating flashcards.")
        
        diff_code = constants.FLASHCARD_DIFFICULTIES.get_code(difficulty)
        
        sources_nested = [[[sid]] for sid in source_ids]
        
        # Flashcard options from reference MCP
        flashcard_options = [
            None,
            [
                1,  # Default count base
                None, None, None, None, None,
                [diff_code, 2]  # [difficulty_code, count_code]
            ]
        ]
        
        content = [
            None, None,
            constants.STUDIO_TYPE_FLASHCARDS,
            sources_nested,
            None, None, None, None, None,  # 5 nulls (positions 4-8)
            flashcard_options  # position 9
        ]
        
        params = [[2], notebook_id, content]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "flashcards",
                "status": "in_progress",
            }
        return None
    
    def create_mindmap(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        title: str = "Mind Map",
    ) -> dict | None:
        """Create and save a mind map from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating mind map.")
        
        # Step 1: Generate mind map - from reference MCP
        sources_nested = [[[sid]] for sid in source_ids]
        
        gen_params = [
            sources_nested,
            None, None, None, None,
            ["interactive_mindmap", [["[CONTEXT]", ""]], ""],
            None,
            [2, None, [1]]
        ]
        
        result = self._call_rpc(RPC.GENERATE_MIND_MAP, gen_params)
        
        if not result or not isinstance(result, list) or len(result) == 0:
            return None
        
        # Parse generation result
        inner = result[0] if isinstance(result[0], list) else result
        mind_map_json = inner[0] if isinstance(inner[0], str) else None
        
        if not mind_map_json:
            return None
        
        # Step 2: Save mind map - from reference MCP
        sources_simple = [[sid] for sid in source_ids]
        metadata = [2, None, None, 5, sources_simple]
        
        save_params = [
            notebook_id,
            mind_map_json,
            metadata,
            None,
            title
        ]
        
        save_result = self._call_rpc(RPC.SAVE_MIND_MAP, save_params, f"/notebook/{notebook_id}")
        
        if save_result and isinstance(save_result, list) and len(save_result) > 0:
            inner = save_result[0] if isinstance(save_result[0], list) else save_result
            mind_map_id = inner[0] if len(inner) > 0 else None
            
            return {
                "mind_map_id": mind_map_id,
                "notebook_id": notebook_id,
                "title": title,
                "status": "completed",
            }
        return None
    
    def list_mindmaps(self, notebook_id: str) -> list[dict]:
        """List mind maps in a notebook. Skips deleted/tombstone entries."""
        params = [notebook_id]
        result = self._call_rpc(RPC.LIST_MIND_MAPS, params, f"/notebook/{notebook_id}")
        
        mindmaps = []
        if result and isinstance(result, list) and len(result) > 0:
            # Structure: [[mindmap_data, ...], timestamp]
            mm_list = result[0] if isinstance(result[0], list) else []
            for mm_entry in mm_list:
                # Check if it's a valid non-deleted entry: [uuid, [data...]]
                # Deleted entries look like: [uuid, null, 2]
                if isinstance(mm_entry, list) and len(mm_entry) >= 2 and mm_entry[1] is not None:
                    mm_id = str(mm_entry[0])
                    mm_title = "Untitled Mind Map"
                    
                    inner = mm_entry[1]
                    if isinstance(inner, list) and len(inner) > 4 and isinstance(inner[4], str):
                        mm_title = inner[4]
                        
                    mindmaps.append({
                        "id": mm_id,
                        "title": mm_title,
                    })
        return mindmaps
    
    def create_slides(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        format: str = "detailed",
        length: str = "default",
        language: str = "en",
        focus_prompt: str = "",
    ) -> dict | None:
        """Create a slide deck from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating slides.")
        
        format_code = constants.SLIDE_DECK_FORMATS.get_code(format)
        length_code = constants.SLIDE_DECK_LENGTHS.get_code(length)
        
        sources_nested = [[[sid]] for sid in source_ids]
        
        # Options at position 16: [[focus_prompt, language, format, length]] from reference MCP
        slide_deck_options = [[focus_prompt or None, language, format_code, length_code]]
        
        content = [
            None, None,
            constants.STUDIO_TYPE_SLIDE_DECK,
            sources_nested,
            None, None, None, None, None, None, None, None, None, None, None, None,  # 12 nulls (positions 4-15)
            slide_deck_options  # position 16
        ]
        
        params = [[2], notebook_id, content]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "slide_deck",
                "status": "in_progress",
            }
        return None
    
    def create_infographic(
        self,
        notebook_id: str,
        source_ids: list[str] | None = None,
        orientation: str = "landscape",
        detail_level: str = "standard",
        language: str = "en",
        focus_prompt: str = "",
    ) -> dict | None:
        """Create an infographic from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating infographic.")
        
        orient_code = constants.INFOGRAPHIC_ORIENTATIONS.get_code(orientation)
        detail_code = constants.INFOGRAPHIC_DETAILS.get_code(detail_level)
        
        sources_nested = [[[sid]] for sid in source_ids]
        
        # Options at position 14: [[focus_prompt, language, null, orientation, detail_level]] from reference MCP
        infographic_options = [[focus_prompt or None, language, None, orient_code, detail_code]]
        
        content = [
            None, None,
            constants.STUDIO_TYPE_INFOGRAPHIC,
            sources_nested,
            None, None, None, None, None, None, None, None, None, None,  # 10 nulls (positions 4-13)
            infographic_options  # position 14
        ]
        
        params = [[2], notebook_id, content]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "infographic",
                "status": "in_progress",
            }
        return None
    
    def create_data_table(
        self,
        notebook_id: str,
        description: str,
        source_ids: list[str] | None = None,
        language: str = "en",
    ) -> dict | None:
        """Create a data table from notebook sources."""
        if source_ids is None:
            sources = self.list_sources(notebook_id)
            source_ids = [s["id"] for s in sources]
        
        if not source_ids:
            from nlm.core.exceptions import NLMError
            raise NLMError("No sources in notebook. Add sources before creating data table.")
        
        sources_nested = [[[sid]] for sid in source_ids]
        
        # Data Table options from reference MCP - at position 18
        datatable_options = [None, [description, language]]
        
        content = [
            None, None,
            constants.STUDIO_TYPE_DATA_TABLE,  # Type 9
            sources_nested,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None,  # 14 nulls (positions 4-17)
            datatable_options  # position 18
        ]
        
        params = [[2], notebook_id, content]
        
        result = self._call_rpc(RPC.CREATE_STUDIO, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            artifact_data = result[0]
            artifact_id = artifact_data[0] if isinstance(artifact_data, list) else None
            return {
                "artifact_id": artifact_id,
                "notebook_id": notebook_id,
                "type": "data_table",
                "status": "in_progress",
            }
        return None
    
    def get_studio_status(self, notebook_id: str) -> list[dict]:
        """Get studio artifacts status including mind maps."""
        artifacts = self.poll_studio_status(notebook_id)
        
        # Also include mind maps for unified view
        try:
            mindmaps = self.list_mindmaps(notebook_id)
            for mm in mindmaps:
                artifacts.append({
                    "artifact_id": mm.get("id", ""),
                    "title": mm.get("title", "Untitled Mind Map"),
                    "type": "mindmap",
                    "status": "completed",  # Mind maps are always complete once saved
                })
        except Exception:
            pass  # Silently skip if mindmaps fail
        
        return artifacts
    
    def poll_studio_status(self, notebook_id: str) -> list[dict]:
        """Poll for studio content status."""
        params = [[2], notebook_id, 'NOT artifact.status = "ARTIFACT_STATUS_SUGGESTED"']
        result = self._call_rpc(RPC.POLL_STUDIO, params, f"/notebook/{notebook_id}")
        
        artifacts = []
        if result and isinstance(result, list) and len(result) > 0:
            artifact_list = result[0] if isinstance(result[0], list) else result
            
            for artifact_data in artifact_list:
                if not isinstance(artifact_data, list) or len(artifact_data) < 5:
                    continue
                
                artifact_id = artifact_data[0]
                title = artifact_data[1] if len(artifact_data) > 1 else ""
                type_code = artifact_data[2] if len(artifact_data) > 2 else None
                status_code = artifact_data[4] if len(artifact_data) > 4 else None
                
                type_map = {
                    constants.STUDIO_TYPE_AUDIO: "audio",
                    constants.STUDIO_TYPE_REPORT: "report",
                    constants.STUDIO_TYPE_VIDEO: "video",
                    constants.STUDIO_TYPE_FLASHCARDS: "flashcards",
                    constants.STUDIO_TYPE_INFOGRAPHIC: "infographic",
                    constants.STUDIO_TYPE_SLIDE_DECK: "slide_deck",
                    constants.STUDIO_TYPE_DATA_TABLE: "data_table",
                }
                
                artifacts.append({
                    "artifact_id": artifact_id,
                    "title": title,
                    "type": type_map.get(type_code, "unknown"),
                    "status": "in_progress" if status_code == 1 else "completed" if status_code == 3 else "unknown",
                })
        
        return artifacts

    def delete_studio_artifact(self, artifact_id: str, notebook_id: str | None = None) -> bool:
        """Delete a studio artifact.
        
        Args:
            artifact_id: ID of the artifact to delete.
            notebook_id: Optional notebook ID. Required for deleting Mind Maps.
        """
        # 1. Try standard deletion (Audio, Video, etc.)
        try:
            params = [[2], artifact_id]
            result = self._call_rpc(RPC.DELETE_STUDIO, params)
            if result is not None:
                return True
        except Exception:
            # Continue to fallback if standard delete fails
            pass
            
        # 2. Fallback: Try Mind Map deletion if we have a notebook ID
        # Mind maps require a different RPC (AH0mwd) and payload structure
        if notebook_id:
            return self.delete_mind_map(notebook_id, artifact_id)
            
        return False
    
    def delete_mind_map(self, notebook_id: str, mind_map_id: str) -> bool:
        """Delete a Mind Map artifact using the observed two-step RPC sequence.
        
        Args:
            notebook_id: The notebook UUID.
            mind_map_id: The Mind Map artifact UUID.
        """
        # 1. We need the artifact-specific timestamp from LIST_MIND_MAPS
        params = [notebook_id]
        list_result = self._call_rpc(RPC.LIST_MIND_MAPS, params, f"/notebook/{notebook_id}")
        
        timestamp = None
        if list_result and isinstance(list_result, list) and len(list_result) > 0:
            mm_list = list_result[0] if isinstance(list_result[0], list) else []
            for mm_entry in mm_list:
                if isinstance(mm_entry, list) and mm_entry[0] == mind_map_id:
                    # Based on debug output: item[1][2][2] contains [seconds, micros]
                    try:
                        timestamp = mm_entry[1][2][2]
                    except (IndexError, TypeError):
                        pass
                    break
        
        # 2. Step 1: UUID-based deletion (AH0mwd)
        params_v2 = [notebook_id, None, [mind_map_id], [2]]
        self._call_rpc(RPC.DELETE_MIND_MAP, params_v2, f"/notebook/{notebook_id}")
        
        # 3. Step 2: Timestamp-based sync/deletion (cFji9)
        # This is required to fully remove it from the list and avoid "ghosts"
        if timestamp:
            params_v1 = [notebook_id, None, timestamp, [2]]
            self._call_rpc(RPC.LIST_MIND_MAPS, params_v1, f"/notebook/{notebook_id}")
            
        return True

    def delete_artifact(self, notebook_id: str, artifact_id: str) -> bool:
        """Delete a studio artifact. Alias for delete_studio_artifact."""
        return self.delete_studio_artifact(artifact_id, notebook_id)
    
    # =========================================================================
    # Research Operations (matching MCP signatures)
    # =========================================================================
    
    def start_research(
        self,
        notebook_id: str,
        query: str,
        source: str = "web",
        mode: str = "fast",
    ) -> dict | None:
        """Start a research session to discover sources."""
        source_code = constants.RESEARCH_SOURCES.get_code(source)
        mode_code = constants.RESEARCH_MODES.get_code(mode)
        
        if mode_code == constants.RESEARCH_MODE_FAST:
            params = [[query, source_code], None, constants.RESEARCH_MODE_FAST, notebook_id]
            rpc_id = RPC.START_FAST_RESEARCH
        else:
            params = [None, [1], [query, source_code], constants.RESEARCH_MODE_DEEP, notebook_id]
            rpc_id = RPC.START_DEEP_RESEARCH
        
        result = self._call_rpc(rpc_id, params, f"/notebook/{notebook_id}")
        
        if result and isinstance(result, list) and len(result) > 0:
            return {
                "task_id": result[0],
                "report_id": result[1] if len(result) > 1 else None,
                "notebook_id": notebook_id,
                "query": query,
                "source": source.lower(),
                "mode": mode.lower(),
            }
        return None
    
    def poll_research(self, notebook_id: str, target_task_id: str | None = None) -> dict | None:
        """Poll for research results.
        
        Returns dict with:
        - tasks: list of all research tasks found
        - status: overall status (completed if any completed, in_progress if any running, no_research otherwise)
        
        Each task has: task_id, status, sources, source_count
        """
        params = [None, None, notebook_id]
        result = self._call_rpc(RPC.POLL_RESEARCH, params, f"/notebook/{notebook_id}")
        
        if not result or not isinstance(result, list):
            return {"status": "no_research", "message": "No active research found", "tasks": []}
        
        # Parse research results (simplified)
        if isinstance(result[0], list) and len(result[0]) > 0:
            result = result[0]
        
        all_tasks = []
        
        for task_data in result:
            if not isinstance(task_data, list) or len(task_data) < 2:
                continue
            
            task_id = task_data[0]
            if not isinstance(task_id, str):
                continue
            
            # If looking for specific task, skip others
            if target_task_id and task_id != target_task_id:
                continue
            
            task_info = task_data[1]
            if not task_info or not isinstance(task_info, list):
                continue
            
            status_code = task_info[4] if len(task_info) > 4 else None
            sources_data = task_info[3][0] if len(task_info) > 3 and isinstance(task_info[3], list) else []
            
            sources = []
            for idx, src in enumerate(sources_data):
                if isinstance(src, list) and len(src) >= 2:
                    sources.append({
                        "index": idx,
                        "url": src[0] if isinstance(src[0], str) else "",
                        "title": src[1] if len(src) > 1 else "",
                        "type_code": src[3] if len(src) > 3 and isinstance(src[3], int) else None,
                    })
            
            # Status codes from API:
            # 1 = in_progress (researching)
            # 2 = completed (ready for import)  
            # 6 = imported (sources added to notebook)
            task_status = "completed" if status_code in (2, 6) else "in_progress"
            
            task_dict = {
                "task_id": task_id,
                "status": task_status,
                "status_code": status_code,
                "sources": sources,
                "source_count": len(sources),
            }
            
            # If we found our specific task, return it directly (backward compat)
            if target_task_id:
                return task_dict
            
            all_tasks.append(task_dict)
        
        if target_task_id:
            return {"status": "no_research", "message": f"Task {target_task_id} not found", "tasks": []}
        
        if not all_tasks:
            return {"status": "no_research", "message": "No active research found", "tasks": []}
        
        # Determine overall status
        has_completed = any(t["status"] == "completed" for t in all_tasks)
        has_in_progress = any(t["status"] == "in_progress" for t in all_tasks)
        
        overall_status = "completed" if has_completed else ("in_progress" if has_in_progress else "no_research")
        
        # For backward compat, also include top-level fields from first task
        first_task = all_tasks[0]
        return {
            "status": overall_status,
            "tasks": all_tasks,
            "task_id": first_task["task_id"],
            "sources": first_task["sources"],
            "source_count": first_task["source_count"],
        }
    
    def import_research_sources(
        self,
        notebook_id: str,
        task_id: str,
        sources: list[dict],
    ) -> list[dict]:
        """Import research sources into the notebook.
        
        Uses the native research import RPC which handles source types correctly
        and avoids duplicates/ghost entries.
        """
        if not sources:
            return []

        # Build source array for import using the specific format required by RPC_IMPORT_RESEARCH
        # This matches the implementation in notebooklm-mcp/api_client.py
        source_array = []
        
        for src in sources:
            url = src.get("url", "")
            title = src.get("title", "Untitled")
            
            # Use type_code from research results (3rd index in raw list, mapped in poll_research)
            # Default to 1 (Web) if missing
            result_type = src.get("type_code", 1)
            
            # Skip deep_report sources (type 5) and empty URLs
            if result_type == 5 or not url:
                continue

            if result_type == 1:
                # Web source structure: [None, None, [url, title], None, None, None, None, None, None, None, 2]
                source_data = [None, None, [url, title], None, None, None, None, None, None, None, 2]
            else:
                # Drive source - extract document ID from URL
                # URL format: https://drive.google.com/open?id=<doc_id> or similar
                doc_id = None
                if "id=" in url:
                    doc_id = url.split("id=")[-1].split("&")[0]
                
                if doc_id:
                    # Determine MIME type from result_type (type_code)
                    mime_types = {
                        2: "application/vnd.google-apps.document",     # Doc
                        3: "application/vnd.google-apps.presentation", # Slide (Presentation)
                        8: "application/vnd.google-apps.spreadsheet",  # Sheet
                    }
                    mime_type = mime_types.get(result_type, "application/vnd.google-apps.document")
                    
                    # Drive source structure: [[doc_id, mime_type, 1, title], None x9, 2]
                    # The 1 at position 2 and trailing 2 are required
                    source_data = [[doc_id, mime_type, 1, title], None, None, None, None, None, None, None, None, None, 2]
                else:
                    # Fallback to web-style import if no ID found
                    source_data = [None, None, [url, title], None, None, None, None, None, None, None, 2]
            
            source_array.append(source_data)

        if not source_array:
            return []

        # Call RPC_IMPORT_RESEARCH with the batch
        # Params: [None, [1], task_id, notebook_id, source_array]
        params = [None, [1], task_id, notebook_id, source_array]
        
        try:
            # Import can take a long time when fetching multiple sources
            # Use 120s timeout instead of the default 30s
            # Note: _call_rpc returns the extracted result structure directly
            result = self._call_rpc(RPC.IMPORT_RESEARCH, params, f"/notebook/{notebook_id}", timeout=120.0)
            
            imported_sources = []
            if result and isinstance(result, list):
                # Unwrap nested list if present (common in batch execute)
                if (len(result) > 0 and isinstance(result[0], list) and 
                    len(result[0]) > 0 and isinstance(result[0][0], list)):
                    result = result[0]
                
                for src_data in result:
                    if isinstance(src_data, list) and len(src_data) >= 2:
                        # Extract source ID and Title
                        src_id = src_data[0][0] if src_data[0] and isinstance(src_data[0], list) else None
                        src_title = src_data[1] if len(src_data) > 1 else "Untitled"
                        if src_id:
                            imported_sources.append({"id": src_id, "title": src_title})
            
            return imported_sources

        except Exception as e:
            # If batch import fails, re-raise or handle
            print(f"Error importing sources batch: {e}")
            raise e
    
    def get_research_status(
        self,
        notebook_id: str,
        poll_interval: int = 5,  # 5 seconds for responsive polling
        max_wait: int = 300,
        compact: bool = True,
        task_id: str | None = None,
    ) -> dict:
        """Get research status with polling support.
        
        Args:
            notebook_id: Notebook UUID
            poll_interval: Seconds between status checks (default 5)
            max_wait: Maximum seconds to wait for completion (0 for single check)
            compact: Whether to return compact results
            task_id: Optional specific task ID to check
            
        Returns:
            Research status dict with status, sources_found, etc.
        """
        import time
        
        start_time = time.time()
        
        while True:
            result = self.poll_research(notebook_id, target_task_id=task_id)
            
            # Add sources_found for CLI compatibility
            if result and "source_count" in result:
                result["sources_found"] = result["source_count"]
            
            # Check if we should stop polling
            status = result.get("status", "no_research") if result else "no_research"
            
            # Stop if: completed (status_code 2 or 6), failed, no_research, or not waiting
            if status in ("completed", "failed", "no_research") or max_wait == 0:
                return result
            
            # Check timeout
            elapsed = time.time() - start_time
            if elapsed >= max_wait:
                return result
            
            # Wait before next poll
            remaining = max_wait - elapsed
            wait_time = min(poll_interval, remaining)
            if wait_time > 0:
                time.sleep(wait_time)
    
    def import_research(
        self,
        notebook_id: str,
        task_id: str,
        source_indices: list[int] | None = None,
    ) -> list[dict]:
        """Import research sources. CLI-compatible wrapper for import_research_sources."""
        # First get the research status to get source list (targeting specific task)
        research = self.poll_research(notebook_id, target_task_id=task_id)
        if not research or research.get("status") == "no_research":
            return []
        
        sources = research.get("sources", [])
        if not sources:
            return []
        
        # Filter by indices if specified
        if source_indices is not None:
            sources = [sources[i] for i in source_indices if i < len(sources)]
        
        return self.import_research_sources(notebook_id, task_id, sources)
    
    # =========================================================================
    # Query Operations (matching MCP signatures)
    # =========================================================================
    
    def query(
        self,
        notebook_id: str,
        query_text: str,
        source_ids: list[str] | None = None,
        conversation_id: str | None = None,
    ) -> dict | None:
        """Query the notebook with a question."""
        import uuid
        
        client = self._get_client()
        
        # Get source IDs if not provided
        # Get source metadata for citations
        used_sources = []
        notebook = self.get_notebook(notebook_id)
        
        if source_ids is None:
            if notebook and notebook.sources:
                source_ids = [s["id"] for s in notebook.sources]
                used_sources = notebook.sources
            else:
                source_ids = []
        else:
            # Resolve titles for requested source IDs
            if notebook and notebook.sources:
                lookup = {s["id"]: s for s in notebook.sources}
                used_sources = [lookup[sid] for sid in source_ids if sid in lookup]
        
        # Handle conversation
        is_new = conversation_id is None
        if is_new:
            conversation_id = str(uuid.uuid4())
            history = None
        else:
            history = self._build_conversation_history(conversation_id)
        
        sources_array = [[[sid]] for sid in source_ids] if source_ids else []
        
        params = [
            sources_array,
            query_text,
            history,
            [2, None, [1]],
            conversation_id,
        ]
        
        params_json = json.dumps(params, separators=(",", ":"))
        f_req = [None, params_json]
        f_req_json = json.dumps(f_req, separators=(",", ":"))
        
        body_parts = [f"f.req={urllib.parse.quote(f_req_json, safe='')}"]
        if self.csrf_token:
            body_parts.append(f"at={urllib.parse.quote(self.csrf_token, safe='')}")
        body = "&".join(body_parts) + "&"
        
        self._reqid_counter += 100000
        url_params = {
            "bl": os.environ.get("NOTEBOOKLM_BL", "boq_labs-tailwind-frontend_20251221.14_p0"),
            "hl": "en",
            "_reqid": str(self._reqid_counter),
            "rt": "c",
        }
        if self._session_id:
            url_params["f.sid"] = self._session_id
        
        query_string = urllib.parse.urlencode(url_params)
        url = f"{BASE_URL}{self.QUERY_ENDPOINT}?{query_string}"
        
        try:
            response = client.post(url, content=body)
            response.raise_for_status()
        except httpx.RequestError as e:
            raise NetworkError(
                message=f"Query failed: {e}",
                hint="Check your internet connection.",
            ) from e
        
        answer, citations = self._parse_query_response(response.text)
        
        if answer:
            self._cache_conversation_turn(conversation_id, query_text, answer)
        
        turns = self._conversation_cache.get(conversation_id, [])
        
        return {
            "answer": answer,
            "conversation_id": conversation_id,
            "turn_number": len(turns),
            "is_follow_up": not is_new,
            "sources": used_sources,
            "citations": citations,
        }
    
    def _extract_source_ids(self, notebook_data: Any) -> list[str]:
        """Extract source IDs from notebook data."""
        source_ids = []
        
        # Handle Notebook object
        if hasattr(notebook_data, "sources") and notebook_data.sources:
            return [s["id"] for s in notebook_data.sources]
            
        # Handle raw list data (fallback)
        if notebook_data and isinstance(notebook_data, list):
            try:
                if len(notebook_data) > 0 and isinstance(notebook_data[0], list):
                    notebook_info = notebook_data[0]
                    if len(notebook_info) > 1 and isinstance(notebook_info[1], list):
                        for source in notebook_info[1]:
                            if isinstance(source, list) and len(source) > 0:
                                src_wrapper = source[0]
                                if isinstance(src_wrapper, list) and len(src_wrapper) > 0:
                                    source_ids.append(src_wrapper[0])
            except (IndexError, TypeError):
                pass
        return source_ids
    
    def _parse_query_response(self, response_text: str) -> tuple[str, dict[int, str]]:
        """Parse streaming query response and extract answer with citations.
        
        Returns:
            tuple: (answer_text, citations_dict) where citations_dict maps
                   1-indexed citation numbers to source UUIDs.
        """
        if response_text.startswith(")]}'"):
            response_text = response_text[4:]
        
        answer_parts = []
        citations: dict[int, str] = {}
        lines = response_text.strip().split("\n")
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            
            try:
                int(line)
                i += 1
                if i < len(lines):
                    try:
                        data = json.loads(lines[i])
                        text, is_answer, chunk_citations = self._extract_answer_text(data)
                        if text and is_answer:
                            answer_parts.append(text)
                        if chunk_citations:
                            citations.update(chunk_citations)
                    except json.JSONDecodeError:
                        pass
                i += 1
            except ValueError:
                try:
                    data = json.loads(line)
                    text, is_answer, chunk_citations = self._extract_answer_text(data)
                    if text and is_answer:
                        answer_parts.append(text)
                    if chunk_citations:
                        citations.update(chunk_citations)
                except json.JSONDecodeError:
                    pass
                i += 1
        
        return answer_parts[-1] if answer_parts else "", citations
    
    def _extract_answer_text(self, data: Any) -> tuple[str, bool, dict[int, str]]:
        """Extract answer text and citation mappings from query response chunk.
        
        Returns:
            tuple: (text, is_answer, citations_dict) where citations_dict maps
                   1-indexed citation numbers to source UUIDs.
        """
        if not isinstance(data, list):
            return "", False, {}
        
        for chunk in data:
            if isinstance(chunk, list) and len(chunk) >= 3:
                if chunk[0] == "wrb.fr":
                    inner = chunk[2]
                    if isinstance(inner, str):
                        try:
                            parsed = json.loads(inner)
                            if isinstance(parsed, list) and len(parsed) > 0:
                                first = parsed[0]
                                if isinstance(first, list) and len(first) > 0:
                                    text = first[0]
                                    if isinstance(text, str) and len(text) > 20:
                                        # Check if answer (type 1) vs thinking (type 2)
                                        is_answer = True
                                        if len(first) > 4 and isinstance(first[4], list):
                                            type_info = first[4]
                                            if len(type_info) > 0 and isinstance(type_info[-1], int):
                                                is_answer = type_info[-1] == 1
                                        
                                        # Extract citation mappings from parsed[1]
                                        citations: dict[int, str] = {}
                                        if len(parsed) > 1 and isinstance(parsed[1], list):
                                            citation_list = parsed[1]
                                            for idx, cite_item in enumerate(citation_list):
                                                try:
                                                    # Path: cite_item[5][0][0][0] = source UUID
                                                    source_uuid = cite_item[5][0][0][0]
                                                    if isinstance(source_uuid, str):
                                                        citations[idx + 1] = source_uuid
                                                except (IndexError, TypeError):
                                                    pass
                                        
                                        return text, is_answer, citations
                        except json.JSONDecodeError:
                            pass
        return "", False, {}
    
    def _build_conversation_history(self, conversation_id: str) -> list | None:
        """Build conversation history for follow-up queries."""
        turns = self._conversation_cache.get(conversation_id, [])
        if not turns:
            return None
        
        history = []
        for turn in reversed(turns):
            history.append([turn.answer, None, 2])
            history.append([turn.query, None, 1])
        
        return history
    
    def _cache_conversation_turn(self, conversation_id: str, query: str, answer: str) -> None:
        """Cache a conversation turn for follow-ups."""
        if conversation_id not in self._conversation_cache:
            self._conversation_cache[conversation_id] = []
        
        turns = self._conversation_cache[conversation_id]
        turns.append(ConversationTurn(
            query=query,
            answer=answer,
            turn_number=len(turns) + 1,
        ))

```

## File: `src/nlm/core/constants.py`
```python
"""
Constants and mappings for NotebookLM API.

This module acts as the Single Source of Truth for all API constants, code mappings,
and validation logic. It decouples data definitions from the client logic and
presentation layer.
"""

from typing import Any, Generic, TypeVar

T = TypeVar("T")


class CodeMapper:
    """
    Bidirectional mapping for API codes.
    
    Handles strict validation, normalization (case-insensitivity), and 
    human-readable error messages.
    """

    def __init__(self, mapping: dict[str, int], unknown_label: str = "unknown"):
        # Store as lower-case keys for case-insensitive lookup
        self._name_to_code: dict[str, int] = {k.lower(): v for k, v in mapping.items()}
        # Reverse mapping for code -> name lookup
        self._code_to_name: dict[int, str] = {v: k for k, v in mapping.items()}
        self._unknown_label = unknown_label
        # Keep original display names (keys) sorted for error messages
        self._display_names = sorted(list(mapping.keys()))

    def get_code(self, name: str) -> int:
        """
        Get integer code for a string name.
        
        Args:
            name: The string name (case-insensitive).
            
        Returns:
            The corresponding integer code.
            
        Raises:
            ValueError: If the name is unknown.
        """
        if not name:
            raise ValueError(f"Invalid name: '{name}'. Must be one of: {self.options_str}")
            
        code = self._name_to_code.get(name.lower())
        if code is None:
            raise ValueError(f"Unknown name '{name}'. Must be one of: {self.options_str}")
        return code

    def get_name(self, code: int | None) -> str:
        """
        Get string name for an integer code.
        
        Args:
            code: The integer code.
            
        Returns:
            The corresponding string name, or the 'unknown_label' if not found.
        """
        if code is None:
            return self._unknown_label
        return self._code_to_name.get(code, self._unknown_label)

    @property
    def options_str(self) -> str:
        """Return comma-separated list of valid options."""
        return ", ".join(self._display_names)

    @property
    def names(self) -> list[str]:
        """Return list of valid option names."""
        return self._display_names


# =============================================================================
# Ownership Constants
# =============================================================================
OWNERSHIP_MINE = 1
OWNERSHIP_SHARED = 2

# =============================================================================
# Chat Configuration
# =============================================================================
CHAT_GOAL_DEFAULT = 1
CHAT_GOAL_CUSTOM = 2
CHAT_GOAL_LEARNING_GUIDE = 3

CHAT_GOALS = CodeMapper({
    "default": CHAT_GOAL_DEFAULT,
    "custom": CHAT_GOAL_CUSTOM,
    "learning_guide": CHAT_GOAL_LEARNING_GUIDE,
})

CHAT_RESPONSE_DEFAULT = 1
CHAT_RESPONSE_LONGER = 4
CHAT_RESPONSE_SHORTER = 5

CHAT_RESPONSE_LENGTHS = CodeMapper({
    "default": CHAT_RESPONSE_DEFAULT,
    "longer": CHAT_RESPONSE_LONGER,
    "shorter": CHAT_RESPONSE_SHORTER,
})

# =============================================================================
# Research / Source Discovery
# =============================================================================
RESEARCH_SOURCE_WEB = 1
RESEARCH_SOURCE_DRIVE = 2

RESEARCH_SOURCES = CodeMapper({
    "web": RESEARCH_SOURCE_WEB,
    "drive": RESEARCH_SOURCE_DRIVE,
})

RESEARCH_MODE_FAST = 1
RESEARCH_MODE_DEEP = 5

RESEARCH_MODES = CodeMapper({
    "fast": RESEARCH_MODE_FAST,
    "deep": RESEARCH_MODE_DEEP,
})

RESULT_TYPE_WEB = 1
RESULT_TYPE_GOOGLE_DOC = 2
RESULT_TYPE_GOOGLE_SLIDES = 3
RESULT_TYPE_DEEP_REPORT = 5
RESULT_TYPE_GOOGLE_SHEETS = 8

RESULT_TYPES = CodeMapper({
    "web": RESULT_TYPE_WEB,
    "google_doc": RESULT_TYPE_GOOGLE_DOC,
    "google_slides": RESULT_TYPE_GOOGLE_SLIDES,
    "deep_report": RESULT_TYPE_DEEP_REPORT,
    "google_sheets": RESULT_TYPE_GOOGLE_SHEETS,
})

# =============================================================================
# Source Types (Notebook Content)
# =============================================================================
SOURCE_TYPE_GOOGLE_DOCS = 1
SOURCE_TYPE_GOOGLE_OTHER = 2
SOURCE_TYPE_PDF = 3
SOURCE_TYPE_PASTED_TEXT = 4
SOURCE_TYPE_WEB_PAGE = 5
SOURCE_TYPE_GENERATED_TEXT = 8
SOURCE_TYPE_YOUTUBE = 9
SOURCE_TYPE_UPLOADED_FILE = 11
SOURCE_TYPE_IMAGE = 13
SOURCE_TYPE_WORD_DOC = 14

SOURCE_TYPES = CodeMapper({
    "google_docs": SOURCE_TYPE_GOOGLE_DOCS,
    "google_slides_sheets": SOURCE_TYPE_GOOGLE_OTHER,
    "pdf": SOURCE_TYPE_PDF,
    "pasted_text": SOURCE_TYPE_PASTED_TEXT,
    "web_page": SOURCE_TYPE_WEB_PAGE,
    "generated_text": SOURCE_TYPE_GENERATED_TEXT,
    "youtube": SOURCE_TYPE_YOUTUBE,
    "uploaded_file": SOURCE_TYPE_UPLOADED_FILE,
    "image": SOURCE_TYPE_IMAGE,
    "word_doc": SOURCE_TYPE_WORD_DOC,
})

# =============================================================================
# Studio Types
# =============================================================================
STUDIO_TYPE_AUDIO = 1
STUDIO_TYPE_REPORT = 2
STUDIO_TYPE_VIDEO = 3
STUDIO_TYPE_FLASHCARDS = 4  # Also Quiz
STUDIO_TYPE_INFOGRAPHIC = 7
STUDIO_TYPE_SLIDE_DECK = 8
STUDIO_TYPE_DATA_TABLE = 9

STUDIO_TYPES = CodeMapper({
    "audio": STUDIO_TYPE_AUDIO,
    "report": STUDIO_TYPE_REPORT,
    "video": STUDIO_TYPE_VIDEO,
    "flashcards": STUDIO_TYPE_FLASHCARDS,
    "infographic": STUDIO_TYPE_INFOGRAPHIC,
    "slide_deck": STUDIO_TYPE_SLIDE_DECK,
    "data_table": STUDIO_TYPE_DATA_TABLE,
})

# =============================================================================
# Audio Overview
# =============================================================================
AUDIO_FORMAT_DEEP_DIVE = 1
AUDIO_FORMAT_BRIEF = 2
AUDIO_FORMAT_CRITIQUE = 3
AUDIO_FORMAT_DEBATE = 4

AUDIO_FORMATS = CodeMapper({
    "deep_dive": AUDIO_FORMAT_DEEP_DIVE,
    "brief": AUDIO_FORMAT_BRIEF,
    "critique": AUDIO_FORMAT_CRITIQUE,
    "debate": AUDIO_FORMAT_DEBATE,
})

AUDIO_LENGTH_SHORT = 1
AUDIO_LENGTH_DEFAULT = 2
AUDIO_LENGTH_LONG = 3

AUDIO_LENGTHS = CodeMapper({
    "short": AUDIO_LENGTH_SHORT,
    "default": AUDIO_LENGTH_DEFAULT,
    "long": AUDIO_LENGTH_LONG,
})

# =============================================================================
# Video Overview
# =============================================================================
VIDEO_FORMAT_EXPLAINER = 1
VIDEO_FORMAT_BRIEF = 2

VIDEO_FORMATS = CodeMapper({
    "explainer": VIDEO_FORMAT_EXPLAINER,
    "brief": VIDEO_FORMAT_BRIEF,
})

VIDEO_STYLE_AUTO_SELECT = 1
VIDEO_STYLE_CUSTOM = 2
VIDEO_STYLE_CLASSIC = 3
VIDEO_STYLE_WHITEBOARD = 4
VIDEO_STYLE_KAWAII = 5
VIDEO_STYLE_ANIME = 6
VIDEO_STYLE_WATERCOLOR = 7
VIDEO_STYLE_RETRO_PRINT = 8
VIDEO_STYLE_HERITAGE = 9
VIDEO_STYLE_PAPER_CRAFT = 10

VIDEO_STYLES = CodeMapper({
    "auto_select": VIDEO_STYLE_AUTO_SELECT,
    "custom": VIDEO_STYLE_CUSTOM,
    "classic": VIDEO_STYLE_CLASSIC,
    "whiteboard": VIDEO_STYLE_WHITEBOARD,
    "kawaii": VIDEO_STYLE_KAWAII,
    "anime": VIDEO_STYLE_ANIME,
    "watercolor": VIDEO_STYLE_WATERCOLOR,
    "retro_print": VIDEO_STYLE_RETRO_PRINT,
    "heritage": VIDEO_STYLE_HERITAGE,
    "paper_craft": VIDEO_STYLE_PAPER_CRAFT,
})

# =============================================================================
# Infographic
# =============================================================================
INFOGRAPHIC_ORIENTATION_LANDSCAPE = 1
INFOGRAPHIC_ORIENTATION_PORTRAIT = 2
INFOGRAPHIC_ORIENTATION_SQUARE = 3

INFOGRAPHIC_ORIENTATIONS = CodeMapper({
    "landscape": INFOGRAPHIC_ORIENTATION_LANDSCAPE,
    "portrait": INFOGRAPHIC_ORIENTATION_PORTRAIT,
    "square": INFOGRAPHIC_ORIENTATION_SQUARE,
})

INFOGRAPHIC_DETAIL_CONCISE = 1
INFOGRAPHIC_DETAIL_STANDARD = 2
INFOGRAPHIC_DETAIL_DETAILED = 3

INFOGRAPHIC_DETAILS = CodeMapper({
    "concise": INFOGRAPHIC_DETAIL_CONCISE,
    "standard": INFOGRAPHIC_DETAIL_STANDARD,
    "detailed": INFOGRAPHIC_DETAIL_DETAILED,
})

# =============================================================================
# Slide Deck
# =============================================================================
SLIDE_DECK_FORMAT_DETAILED = 1
SLIDE_DECK_FORMAT_PRESENTER = 2

SLIDE_DECK_FORMATS = CodeMapper({
    "detailed_deck": SLIDE_DECK_FORMAT_DETAILED,
    "detailed": SLIDE_DECK_FORMAT_DETAILED,
    "presenter_slides": SLIDE_DECK_FORMAT_PRESENTER,
    "presenter": SLIDE_DECK_FORMAT_PRESENTER,
})

SLIDE_DECK_LENGTH_SHORT = 1
SLIDE_DECK_LENGTH_DEFAULT = 3

SLIDE_DECK_LENGTHS = CodeMapper({
    "short": SLIDE_DECK_LENGTH_SHORT,
    "default": SLIDE_DECK_LENGTH_DEFAULT,
})

# =============================================================================
# Flashcards / Quiz
# =============================================================================
FLASHCARD_DIFFICULTY_EASY = 1
FLASHCARD_DIFFICULTY_MEDIUM = 2
FLASHCARD_DIFFICULTY_HARD = 3

FLASHCARD_DIFFICULTIES = CodeMapper({
    "easy": FLASHCARD_DIFFICULTY_EASY,
    "medium": FLASHCARD_DIFFICULTY_MEDIUM,
    "hard": FLASHCARD_DIFFICULTY_HARD,
})

FLASHCARD_COUNT_DEFAULT = 2

# =============================================================================
# Reports
# =============================================================================
REPORT_FORMAT_BRIEFING_DOC = "Briefing Doc"
REPORT_FORMAT_STUDY_GUIDE = "Study Guide"
REPORT_FORMAT_BLOG_POST = "Blog Post"
REPORT_FORMAT_CUSTOM = "Create Your Own"
```

## File: `src/nlm/core/exceptions.py`
```python
"""Custom exceptions for NLM CLI."""

from typing import Any


class NLMError(Exception):
    """Base exception for all NLM errors."""

    def __init__(self, message: str, hint: str | None = None) -> None:
        self.message = message
        self.hint = hint
        super().__init__(message)

    def __str__(self) -> str:
        if self.hint:
            return f"{self.message}\n\nHint: {self.hint}"
        return self.message


class AuthenticationError(NLMError):
    """Raised when authentication fails or credentials are invalid."""

    def __init__(
        self,
        message: str = "Authentication failed",
        hint: str = "Run 'nlm login' to authenticate.",
    ) -> None:
        super().__init__(message, hint)


class NotFoundError(NLMError):
    """Raised when a requested resource is not found."""

    def __init__(
        self,
        resource_type: str,
        resource_id: str,
        hint: str | None = None,
    ) -> None:
        message = f"{resource_type} not found: {resource_id}"
        if hint is None:
            hint = f"Run 'nlm {resource_type.lower()} list' to see available {resource_type.lower()}s."
        super().__init__(message, hint)
        self.resource_type = resource_type
        self.resource_id = resource_id


class ValidationError(NLMError):
    """Raised when input validation fails."""

    def __init__(
        self,
        message: str,
        field: str | None = None,
        hint: str | None = None,
    ) -> None:
        if field:
            message = f"Invalid {field}: {message}"
        super().__init__(message, hint)
        self.field = field


class NetworkError(NLMError):
    """Raised when a network request fails."""

    def __init__(
        self,
        message: str = "Network request failed",
        hint: str = "Check your internet connection and try again.",
        status_code: int | None = None,
    ) -> None:
        super().__init__(message, hint)
        self.status_code = status_code


class RateLimitError(NLMError):
    """Raised when rate limit is exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        hint: str = "Please wait a moment and try again.",
        retry_after: int | None = None,
    ) -> None:
        super().__init__(message, hint)
        self.retry_after = retry_after


class ConfigError(NLMError):
    """Raised when configuration is invalid."""

    def __init__(
        self,
        message: str,
        hint: str = "Check your configuration at ~/.nlm/config.toml",
    ) -> None:
        super().__init__(message, hint)


class ProfileNotFoundError(NLMError):
    """Raised when a profile is not found."""

    def __init__(self, profile_name: str) -> None:
        message = f"Profile not found: {profile_name}"
        hint = "Run 'nlm login' to create a profile, or use '--profile <name>' to specify a different profile."
        super().__init__(message, hint)
        self.profile_name = profile_name


def handle_api_error(status_code: int, response_data: dict[str, Any] | None = None) -> NLMError:
    """Convert API error response to appropriate exception."""
    if status_code == 401:
        return AuthenticationError()
    if status_code == 403:
        return AuthenticationError(
            message="Access denied",
            hint="Your session may have expired. Run 'nlm login' to re-authenticate.",
        )
    if status_code == 404:
        return NotFoundError("Resource", "unknown")
    if status_code == 429:
        return RateLimitError()
    if status_code >= 500:
        return NetworkError(
            message="NotebookLM server error",
            hint="The NotebookLM service may be temporarily unavailable. Try again later.",
            status_code=status_code,
        )
    return NetworkError(
        message=f"Request failed with status {status_code}",
        status_code=status_code,
    )
```

## File: `src/nlm/core/models.py`
```python
"""Pydantic models for NotebookLM data structures."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class Notebook(BaseModel):
    """Represents a NotebookLM notebook."""

    id: str = Field(description="Unique notebook identifier")
    title: str = Field(default="Untitled", description="Notebook title")
    sources_count: int = Field(default=0, description="Number of sources")
    created_at: datetime | None = Field(default=None, description="Creation timestamp")
    updated_at: datetime | None = Field(default=None, description="Last update timestamp")

    @property
    def short_id(self) -> str:
        """Return abbreviated ID for display."""
        if len(self.id) > 12:
            return f"{self.id[:8]}..."
        return self.id


class Source(BaseModel):
    """Represents a source within a notebook."""

    id: str = Field(description="Unique source identifier")
    title: str = Field(default="Untitled", description="Source title")
    type: str = Field(default="unknown", description="Source type (url, text, drive, youtube)")
    url: str | None = Field(default=None, description="Source URL if applicable")
    is_stale: bool = Field(default=False, description="Whether Drive source needs sync")

    @property
    def short_id(self) -> str:
        """Return abbreviated ID for display."""
        if len(self.id) > 12:
            return f"{self.id[:8]}..."
        return self.id


class SourceContent(BaseModel):
    """Raw content of a source."""

    content: str = Field(description="Raw text content")
    title: str = Field(default="", description="Source title")
    source_type: str = Field(default="", description="Type of source")
    char_count: int = Field(default=0, description="Character count")


class SourceSummary(BaseModel):
    """AI-generated summary of a source."""

    summary: str = Field(description="Markdown summary with bold keywords")
    keywords: list[str] = Field(default_factory=list, description="Extracted keywords")


class NotebookSummary(BaseModel):
    """AI-generated summary of a notebook."""

    summary: str = Field(description="Markdown summary")
    suggested_topics: list[str] = Field(default_factory=list, description="Suggested topics")


class ChatConfig(BaseModel):
    """Chat configuration for a notebook."""

    goal: str = Field(default="default", description="Chat goal: default, learning_guide, custom")
    custom_prompt: str | None = Field(default=None, description="Custom prompt when goal=custom")
    response_length: str = Field(default="default", description="Response length: default, longer, shorter")


class QueryResponse(BaseModel):
    """Response from a notebook query."""

    response: str = Field(description="AI response text")
    conversation_id: str | None = Field(default=None, description="Conversation ID for follow-ups")
    citations: list[dict[str, Any]] = Field(default_factory=list, description="Source citations")


class AudioOverview(BaseModel):
    """Audio overview (podcast) artifact."""

    id: str = Field(description="Artifact ID")
    status: str = Field(description="Generation status")
    format: str = Field(default="deep_dive", description="Audio format")
    url: str | None = Field(default=None, description="Download URL when ready")
    duration: int | None = Field(default=None, description="Duration in seconds")


class StudioArtifact(BaseModel):
    """Generic studio artifact (report, quiz, etc.)."""

    id: str = Field(description="Artifact ID")
    type: str = Field(description="Artifact type")
    status: str = Field(description="Generation status")
    url: str | None = Field(default=None, description="Download/view URL")
    title: str | None = Field(default=None, description="Artifact title")
    created_at: datetime | None = Field(default=None, description="Creation timestamp")

    @property
    def short_id(self) -> str:
        """Return abbreviated ID for display."""
        if len(self.id) > 12:
            return f"{self.id[:8]}..."
        return self.id


class ResearchTask(BaseModel):
    """Research task status."""

    task_id: str = Field(description="Research task ID")
    status: str = Field(description="Task status: pending, running, completed, failed")
    sources_found: int = Field(default=0, description="Number of sources discovered")
    report: str | None = Field(default=None, description="Research report when complete")
    sources: list[dict[str, Any]] = Field(default_factory=list, description="Discovered sources")


class MindMap(BaseModel):
    """Mind map artifact."""

    id: str = Field(description="Mind map ID")
    title: str = Field(default="Mind Map", description="Mind map title")
    data: dict[str, Any] = Field(default_factory=dict, description="Mind map data structure")
```

## File: `src/nlm/output/__init__.py`
```python
"""Output formatting package for NLM."""
```

## File: `src/nlm/output/formatters.py`
```python
"""Output formatting utilities for NLM CLI."""

import json
import sys
from enum import Enum
from typing import Any

from rich.console import Console
from rich.table import Table


class OutputFormat(str, Enum):
    """Output format options."""

    TABLE = "table"
    JSON = "json"
    COMPACT = "compact"


def detect_output_format(
    json_flag: bool = False,
    quiet_flag: bool = False,
    title_flag: bool = False,
    url_flag: bool = False,
) -> OutputFormat:
    """
    Detect the appropriate output format based on flags and TTY.
    
    Args:
        json_flag: User explicitly requested JSON output.
        quiet_flag: User requested quiet/compact output.
        title_flag: User requested title output (for notebooks).
        url_flag: User requested URL output (for sources).
    
    Returns:
        The output format to use.
    """
    if json_flag:
        return OutputFormat.JSON
    if quiet_flag or title_flag or url_flag:
        return OutputFormat.COMPACT
    
    # Auto-detect based on TTY
    if not sys.stdout.isatty():
        return OutputFormat.JSON
    
    return OutputFormat.TABLE


class Formatter:
    """Base class for output formatters."""

    def __init__(self, console: Console | None = None) -> None:
        self.console = console or Console()

    def format_notebooks(
        self,
        notebooks: list[Any],
        full: bool = False,
        title_only: bool = False,
    ) -> None:
        """Format notebook list output."""
        raise NotImplementedError

    def format_sources(
        self,
        sources: list[Any],
        full: bool = False,
        url_only: bool = False,
    ) -> None:
        """Format source list output."""
        raise NotImplementedError

    def format_artifacts(
        self,
        artifacts: list[Any],
        full: bool = False,
    ) -> None:
        """Format studio artifacts output."""
        raise NotImplementedError

    def format_item(self, item: Any, title: str = "") -> None:
        """Format a single item."""
        raise NotImplementedError

    def format_message(self, message: str, style: str = "") -> None:
        """Format a simple message."""
        self.console.print(message, style=style)

    def format_error(self, message: str, hint: str | None = None) -> None:
        """Format an error message."""
        self.console.print(f"[red]Error:[/red] {message}")
        if hint:
            self.console.print(f"\n[dim]Hint: {hint}[/dim]")

    def format_success(self, message: str) -> None:
        """Format a success message."""
        self.console.print(f"[green]✓[/green] {message}")


class TableFormatter(Formatter):
    """Format output as rich tables."""

    def format_notebooks(
        self,
        notebooks: list[Any],
        full: bool = False,
        title_only: bool = False,
    ) -> None:
        if not notebooks:
            self.console.print("[dim]No notebooks found.[/dim]")
            return

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="cyan", min_width=36, no_wrap=True)
        table.add_column("Title", overflow="ellipsis", max_width=50)
        table.add_column("Src", justify="right", width=4)
        table.add_column("Updated", no_wrap=True, width=10)
        
        if full:
            table.add_column("Created", no_wrap=True, width=10)

        for nb in notebooks:
            # Handle both source_count and sources_count for compatibility
            src_count = getattr(nb, 'source_count', None) or getattr(nb, 'sources_count', 0)
            # Handle both modified_at and updated_at - format as short date
            updated = getattr(nb, 'modified_at', None) or getattr(nb, 'updated_at', None)
            if updated:
                if isinstance(updated, str):
                    updated_str = updated[:10]  # Just the date part
                else:
                    updated_str = updated.strftime("%Y-%m-%d")
            else:
                updated_str = "-"
            
            row = [
                str(nb.id),  # Full ID for copy/paste
                nb.title,
                str(src_count),
                updated_str,
            ]
            if full:
                created = getattr(nb, 'created_at', None)
                if created:
                    created_str = created[:10] if isinstance(created, str) else created.strftime("%Y-%m-%d")
                else:
                    created_str = "-"
                row.append(created_str)
            table.add_row(*row)

        self.console.print(table)

    def format_sources(
        self,
        sources: list[Any],
        full: bool = False,
        url_only: bool = False,
    ) -> None:
        if not sources:
            self.console.print("[dim]No sources found.[/dim]")
            return

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="cyan", min_width=36, no_wrap=True)
        table.add_column("Title", max_width=30, overflow="ellipsis")
        table.add_column("Type")
        
        if full:
            table.add_column("URL", overflow="fold", max_width=80)
            table.add_column("Stale", justify="center")

        for src in sources:
            # Handle both dict and object
            if isinstance(src, dict):
                src_id = src.get('id', '')
                src_title = src.get('title', 'Untitled')
                src_type = src.get('type', 'unknown')
                src_url = src.get('url', '')
                is_stale = src.get('is_stale', False)
            else:
                src_id = str(src.id)
                src_title = src.title
                src_type = src.type
                src_url = getattr(src, 'url', '') or ''
                is_stale = getattr(src, 'is_stale', False)
            
            row = [
                src_id,
                src_title,
                src_type,
            ]
            if full:
                row.extend([src_url or '-', '⚠️' if is_stale else ''])
            table.add_row(*row)

        self.console.print(table)

    def format_artifacts(
        self,
        artifacts: list[Any],
        full: bool = False,
    ) -> None:
        if not artifacts:
            self.console.print("[dim]No artifacts found.[/dim]")
            return

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="cyan", min_width=36, no_wrap=True)
        table.add_column("Title", max_width=40)
        table.add_column("Type")
        table.add_column("Status")
        
        if full:
            table.add_column("URL")

        for art in artifacts:
            # Handle both dict and object
            if isinstance(art, dict):
                art_id = art.get('artifact_id', art.get('id', ''))
                art_type = art.get('type', 'unknown')
                art_status = art.get('status', 'unknown')
                art_title = art.get('title', '')
                art_url = art.get('url', '')
            else:
                art_id = str(art.id)
                art_type = art.type
                art_status = art.status
                art_title = getattr(art, 'title', '')
                art_url = getattr(art, 'url', '')
            
            # Status with color and Unicode symbol for quick scanning
            status_config = {
                'completed': ('green', '✓'),
                'pending': ('yellow', '●'),
                'in_progress': ('yellow', '●'),
                'failed': ('red', '✗'),
            }
            
            if art_status in status_config:
                style, symbol = status_config[art_status]
                status_display = f'[{style}]{symbol} {art_status}[/{style}]'
            else:
                status_display = art_status
            
            row = [
                art_id,
                art_title or '-',
                art_type,
                status_display,
            ]
            if full:
                row.append(art_url or '-')
            table.add_row(*row)

        self.console.print(table)

    def format_item(self, item: Any, title: str = "") -> None:
        if title:
            self.console.print(f"[bold]{title}[/bold]")
        
        if hasattr(item, "model_dump"):
            data = item.model_dump(exclude_none=True)
        elif hasattr(item, "__dict__"):
            data = {k: v for k, v in item.__dict__.items() if not k.startswith("_")}
        else:
            data = {"value": item}
        
        for key, value in data.items():
            # Special handling for sources list
            if key == "sources" and isinstance(value, list):
                self.console.print(f"  [cyan]{key}:[/cyan]")
                for src in value:
                    if isinstance(src, dict):
                        self.console.print(f"    • {src.get('title', 'Untitled')} [dim]({src.get('id', '')})[/dim]")
                    else:
                        self.console.print(f"    • {src}")
            else:
                self.console.print(f"  [cyan]{key}:[/cyan] {value}")


class JsonFormatter(Formatter):
    """Format output as JSON."""

    def format_notebooks(
        self,
        notebooks: list[Any],
        full: bool = False,
        title_only: bool = False,
    ) -> None:
        data = []
        for nb in notebooks:
            src_count = getattr(nb, 'source_count', None) or getattr(nb, 'sources_count', 0)
            item = {"id": nb.id, "title": nb.title, "source_count": src_count}
            updated = getattr(nb, 'modified_at', None) or getattr(nb, 'updated_at', None)
            if updated:
                item["updated_at"] = updated if isinstance(updated, str) else updated.isoformat()
            created = getattr(nb, 'created_at', None)
            if full and created:
                item["created_at"] = created if isinstance(created, str) else created.isoformat()
            data.append(item)
        print(json.dumps(data, indent=2))

    def format_sources(
        self,
        sources: list[Any],
        full: bool = False,
        url_only: bool = False,
    ) -> None:
        data = []
        for src in sources:
            if isinstance(src, dict):
                item = {
                    'id': src.get('id', ''),
                    'title': src.get('title', ''),
                    'type': src.get('type', ''),
                    'url': src.get('url', ''),
                }
                if full:
                    item['is_stale'] = src.get('is_stale', False)
            else:
                item = {
                    'id': src.id,
                    'title': src.title,
                    'type': src.type,
                    'url': getattr(src, 'url', '') or '',
                }
                if full:
                    item['is_stale'] = getattr(src, 'is_stale', False)
            data.append(item)
        print(json.dumps(data, indent=2))

    def format_artifacts(
        self,
        artifacts: list[Any],
        full: bool = False,
    ) -> None:
        data = []
        for art in artifacts:
            if isinstance(art, dict):
                item = {'id': art.get('artifact_id', art.get('id', '')), 'type': art.get('type', ''), 'status': art.get('status', '')}
                if full:
                    item['title'] = art.get('title', '')
                    item['url'] = art.get('url', '')
            else:
                item = {'id': art.id, 'type': art.type, 'status': art.status}
                if full:
                    item['title'] = getattr(art, 'title', '')
                    item['url'] = getattr(art, 'url', '')
            data.append(item)
        print(json.dumps(data, indent=2))

    def format_item(self, item: Any, title: str = "") -> None:
        if hasattr(item, "model_dump"):
            data = item.model_dump(exclude_none=True)
        elif hasattr(item, "__dict__"):
            data = {k: v for k, v in item.__dict__.items() if not k.startswith("_")}
        else:
            data = {"value": item}
        print(json.dumps(data, indent=2))


class CompactFormatter(Formatter):
    """Format output as compact text (for piping)."""

    def format_notebooks(
        self,
        notebooks: list[Any],
        full: bool = False,
        title_only: bool = False,
    ) -> None:
        for nb in notebooks:
            if title_only:
                print(f"{nb.id}: {nb.title}")
            else:
                print(nb.id)

    def format_sources(
        self,
        sources: list[Any],
        full: bool = False,
        url_only: bool = False,
    ) -> None:
        for src in sources:
            if isinstance(src, dict):
                src_id = src.get('id', '')
                src_url = src.get('url', '')
            else:
                src_id = str(src.id)
                src_url = getattr(src, 'url', '') or ''
            
            if url_only:
                if src_url:
                    print(f"{src_id}: {src_url}")
            else:
                print(src_id)

    def format_artifacts(
        self,
        artifacts: list[Any],
        full: bool = False,
    ) -> None:
        for art in artifacts:
            if isinstance(art, dict):
                print(art.get('artifact_id', art.get('id', '')))
            else:
                print(art.id)

    def format_item(self, item: Any, title: str = "") -> None:
        if hasattr(item, "id"):
            print(item.id)
        else:
            print(str(item))


def get_formatter(format: OutputFormat, console: Console | None = None) -> Formatter:
    """Get the appropriate formatter for the output format."""
    formatters = {
        OutputFormat.TABLE: TableFormatter,
        OutputFormat.JSON: JsonFormatter,
        OutputFormat.COMPACT: CompactFormatter,
    }
    return formatters[format](console)
```

## File: `src/nlm/utils/__init__.py`
```python
"""Utility functions for NLM."""
```

## File: `src/nlm/utils/browser.py`
```python
"""Browser cookie utilities."""

import json
import re
from pathlib import Path

from nlm.core.exceptions import AuthenticationError


# NotebookLM domain for cookie filtering
NOTEBOOKLM_DOMAIN = ".google.com"
NOTEBOOKLM_URL = "https://notebooklm.google.com"


def parse_cookies_from_file(file_path: str | Path) -> dict[str, str]:
    """
    Parse cookies from a file.
    
    The file can contain:
    - Raw cookie header string (Cookie: name=value; name2=value2)
    - cURL command (copy as cURL from DevTools)
    - JSON object with cookies
    
    Args:
        file_path: Path to the file containing cookies.
    
    Returns:
        Dictionary of cookie name -> value.
    
    Raises:
        AuthenticationError: If file cannot be parsed.
    """
    path = Path(file_path).expanduser()
    
    if not path.exists():
        raise AuthenticationError(
            message=f"Cookie file not found: {path}",
            hint="Create the file with cookies copied from browser DevTools.",
        )
    
    content = path.read_text().strip()
    
    # Try to parse as JSON first
    try:
        data = json.loads(content)
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
        if isinstance(data, list):
            # List of cookie objects
            cookies = {}
            for item in data:
                if isinstance(item, dict) and "name" in item and "value" in item:
                    cookies[item["name"]] = item["value"]
            if cookies:
                return cookies
    except json.JSONDecodeError:
        pass
    
    # Try to extract from cURL command
    curl_match = re.search(r"-H\s+['\"]Cookie:\s*([^'\"]+)['\"]", content, re.IGNORECASE)
    if curl_match:
        content = curl_match.group(1)
    
    # Try to extract Cookie header value
    if content.lower().startswith("cookie:"):
        content = content[7:].strip()
    
    # Parse cookie string (name=value; name2=value2)
    cookies: dict[str, str] = {}
    for part in content.split(";"):
        part = part.strip()
        if "=" in part:
            name, _, value = part.partition("=")
            name = name.strip()
            value = value.strip()
            if name and value:
                cookies[name] = value
    
    if not cookies:
        raise AuthenticationError(
            message="Could not parse cookies from file",
            hint="The file should contain a Cookie header value or cURL command.",
        )
    
    return cookies


def cookies_to_header(cookies: dict[str, str]) -> str:
    """Convert cookies dict to Cookie header value."""
    return "; ".join(f"{name}={value}" for name, value in cookies.items())


def validate_notebooklm_cookies(cookies: dict[str, str]) -> bool:
    """
    Check if cookies appear to be valid for NotebookLM.
    
    This is a basic check - actual validation requires making an API call.
    """
    # Check for essential Google auth cookies
    essential_patterns = ["SID", "HSID", "SSID", "APISID", "SAPISID"]
    found = sum(1 for pattern in essential_patterns if any(pattern in name for name in cookies))
    return found >= 2  # At least 2 essential cookies should be present
```

## File: `src/nlm/utils/cdp.py`
```python
"""Chrome DevTools Protocol (CDP) utilities for cookie extraction.

This module provides a keychain-free way to extract cookies from Chrome
by using the Chrome DevTools Protocol over WebSocket.

Usage:
    1. Chrome is launched with --remote-debugging-port
    2. We connect via WebSocket and use Network.getCookies
    3. No keychain access required!
"""

import json
import platform
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any

import httpx

from nlm.core.exceptions import AuthenticationError


CDP_DEFAULT_PORT = 9222
CDP_PORT_RANGE = range(9222, 9232)  # Ports to scan for existing/available
NOTEBOOKLM_URL = "https://notebooklm.google.com/"


def find_available_port(starting_from: int = 9222, max_attempts: int = 10) -> int:
    """Find an available port for Chrome debugging.
    
    Args:
        starting_from: Port to start scanning from
        max_attempts: Number of ports to try
    
    Returns:
        An available port number
    
    Raises:
        RuntimeError: If no available ports found
    """
    import socket
    for offset in range(max_attempts):
        port = starting_from + offset
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    raise RuntimeError(
        f"No available ports in range {starting_from}-{starting_from + max_attempts - 1}. "
        "Close some applications and try again."
    )


def get_chrome_path() -> str | None:
    """Get the Chrome executable path for the current platform."""
    system = platform.system()
    
    if system == "Darwin":
        path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        return path if Path(path).exists() else None
    elif system == "Linux":
        candidates = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]
        for candidate in candidates:
            if shutil.which(candidate):
                return candidate
        return None
    elif system == "Windows":
        path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        return path if Path(path).exists() else None
    
    return None


def get_chrome_profile_dir() -> Path:
    """Get the CLI's Chrome profile directory.
    
    We use a separate profile at ~/.nlm/chrome-profile so we can run
    alongside the user's main Chrome browser without conflicts.
    """
    return Path.home() / ".nlm" / "chrome-profile"


def is_profile_locked() -> bool:
    """Check if the Chrome profile is locked (Chrome is using it)."""
    lock_file = get_chrome_profile_dir() / "SingletonLock"
    return lock_file.exists()


def find_existing_nlm_chrome(port_range: range = CDP_PORT_RANGE) -> int | None:
    """Find an existing NLM Chrome instance on any port in range.
    
    Scans the port range looking for a Chrome DevTools endpoint.
    This allows reconnecting to an existing auth Chrome window.
    
    Returns:
        The port number if found, None otherwise
    """
    for port in port_range:
        try:
            response = httpx.get(f"http://localhost:{port}/json/version", timeout=2)
            if response.status_code == 200:
                # Found a Chrome DevTools endpoint
                return port
        except Exception:
            continue
    return None


def launch_chrome_process(port: int = CDP_DEFAULT_PORT, headless: bool = False) -> subprocess.Popen | None:
    """Launch Chrome and return process handle."""
    chrome_path = get_chrome_path()
    if not chrome_path:
        return None
    
    profile_dir = get_chrome_profile_dir()
    profile_dir.mkdir(parents=True, exist_ok=True)
    
    args = [
        chrome_path,
        f"--remote-debugging-port={port}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        f"--user-data-dir={profile_dir}",
        "--remote-allow-origins=*",
    ]
    
    if headless:
        args.append("--headless=new")
    
    try:
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Wait for Chrome to start
        time.sleep(3)
        return process
    except Exception:
        return None


# Module-level Chrome state for termination and reconnection
_chrome_process: subprocess.Popen | None = None
_chrome_port: int | None = None


def launch_chrome(port: int = CDP_DEFAULT_PORT, headless: bool = False) -> bool:
    """Launch Chrome with remote debugging enabled."""
    global _chrome_process, _chrome_port
    _chrome_process = launch_chrome_process(port, headless)
    _chrome_port = port if _chrome_process else None
    return _chrome_process is not None


def terminate_chrome() -> bool:
    """Terminate the Chrome process launched by this module.
    
    This releases the profile lock so headless auth can work later.
    
    Returns:
        True if Chrome was terminated, False if no process to terminate.
    """
    global _chrome_process
    if _chrome_process is None:
        return False
    
    try:
        _chrome_process.terminate()
        _chrome_process.wait(timeout=5)
    except Exception:
        try:
            _chrome_process.kill()
        except Exception:
            pass
    
    _chrome_process = None
    return True


def get_debugger_url(port: int = CDP_DEFAULT_PORT) -> str | None:
    """Get the WebSocket debugger URL for Chrome."""
    try:
        response = httpx.get(f"http://localhost:{port}/json/version", timeout=5)
        data = response.json()
        return data.get("webSocketDebuggerUrl")
    except Exception:
        return None


def get_pages(port: int = CDP_DEFAULT_PORT) -> list[dict]:
    """Get list of open pages in Chrome."""
    try:
        response = httpx.get(f"http://localhost:{port}/json", timeout=5)
        return response.json()
    except Exception:
        return []


def find_or_create_notebooklm_page(port: int = CDP_DEFAULT_PORT) -> dict | None:
    """Find an existing NotebookLM page or create a new one."""
    from urllib.parse import quote
    
    pages = get_pages(port)
    
    # Look for existing NotebookLM page
    for page in pages:
        url = page.get("url", "")
        if "notebooklm.google.com" in url:
            return page
    
    # Create a new page
    try:
        encoded_url = quote(NOTEBOOKLM_URL, safe="")
        response = httpx.put(
            f"http://localhost:{port}/json/new?{encoded_url}",
            timeout=15
        )
        if response.status_code == 200 and response.text.strip():
            return response.json()
        
        # Fallback: create blank page then navigate
        response = httpx.put(f"http://localhost:{port}/json/new", timeout=10)
        if response.status_code == 200 and response.text.strip():
            page = response.json()
            ws_url = page.get("webSocketDebuggerUrl")
            if ws_url:
                navigate_to_url(ws_url, NOTEBOOKLM_URL)
            return page
        
        return None
    except Exception:
        return None


def execute_cdp_command(ws_url: str, method: str, params: dict | None = None) -> dict:
    """Execute a CDP command via WebSocket.
    
    Args:
        ws_url: WebSocket URL for the page
        method: CDP method name (e.g., "Network.getCookies")
        params: Optional parameters for the command
    
    Returns:
        The result of the CDP command
    """
    try:
        import websocket
    except ImportError:
        raise AuthenticationError(
            message="websocket-client package not installed",
            hint="Run 'pip install websocket-client' to install it.",
        )
    
    ws = websocket.create_connection(ws_url, timeout=30)
    try:
        command = {
            "id": 1,
            "method": method,
            "params": params or {}
        }
        ws.send(json.dumps(command))
        
        # Wait for response with matching ID
        while True:
            response = json.loads(ws.recv())
            if response.get("id") == 1:
                return response.get("result", {})
    finally:
        ws.close()


def get_page_cookies(ws_url: str) -> dict[str, str]:
    """Get all cookies for the page via CDP.
    
    This is the key function that avoids keychain access!
    Uses Network.getCookies CDP command instead of decrypting cookies.
    """
    result = execute_cdp_command(ws_url, "Network.getCookies")
    cookies_list = result.get("cookies", [])
    return {c["name"]: c["value"] for c in cookies_list}


def get_page_html(ws_url: str) -> str:
    """Get the page HTML to extract CSRF token."""
    execute_cdp_command(ws_url, "Runtime.enable")
    result = execute_cdp_command(
        ws_url,
        "Runtime.evaluate",
        {"expression": "document.documentElement.outerHTML"}
    )
    return result.get("result", {}).get("value", "")


def get_current_url(ws_url: str) -> str:
    """Get the current page URL."""
    execute_cdp_command(ws_url, "Runtime.enable")
    result = execute_cdp_command(
        ws_url,
        "Runtime.evaluate",
        {"expression": "window.location.href"}
    )
    return result.get("result", {}).get("value", "")


def navigate_to_url(ws_url: str, url: str) -> None:
    """Navigate the page to a URL."""
    execute_cdp_command(ws_url, "Page.enable")
    execute_cdp_command(ws_url, "Page.navigate", {"url": url})
    time.sleep(3)  # Wait for page to load


def is_logged_in(url: str) -> bool:
    """Check login status by URL.
    
    If NotebookLM redirects to accounts.google.com, user is not logged in.
    """
    if "accounts.google.com" in url:
        return False
    if "notebooklm.google.com" in url:
        return True
    return False


def extract_csrf_token(html: str) -> str:
    """Extract CSRF token from page HTML."""
    match = re.search(r'"SNlM0e":"([^"]+)"', html)
    return match.group(1) if match else ""


def extract_session_id(html: str) -> str:
    """Extract session ID from page HTML."""
    patterns = [
        r'"FdrFJe":"(\d+)"',
        r'f\.sid["\s:=]+["\']?(\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(1)
    return ""


def extract_cookies_via_cdp(
    port: int = CDP_DEFAULT_PORT,
    auto_launch: bool = True,
    wait_for_login: bool = True,
    login_timeout: int = 300,
) -> dict[str, Any]:
    """Extract cookies and tokens from Chrome via CDP.
    
    This is the main entry point for CDP-based authentication.
    
    Args:
        port: Chrome DevTools port
        auto_launch: If True, launch Chrome if not running
        wait_for_login: If True, wait for user to log in
        login_timeout: Max seconds to wait for login
    
    Returns:
        Dict with cookies, csrf_token, and session_id
    
    Raises:
        AuthenticationError: If extraction fails
    """
    # Check if Chrome is running with debugging
    # First, try to find an existing instance on any port in our range
    existing_port = find_existing_nlm_chrome()
    if existing_port:
        port = existing_port
        debugger_url = get_debugger_url(port)
    else:
        debugger_url = None
    
    if not debugger_url and auto_launch:
        if is_profile_locked():
            # Profile locked but no Chrome found on known ports - stale lock?
            raise AuthenticationError(
                message="The NLM auth profile is locked but no Chrome instance found",
                hint="Close any stuck Chrome processes or delete ~/.nlm/chrome-profile/SingletonLock",
            )
        
        if not get_chrome_path():
            raise AuthenticationError(
                message="Chrome not found",
                hint="Install Google Chrome or use 'nlm login --manual' to import cookies from a file.",
            )
        
        # Find an available port
        try:
            port = find_available_port()
        except RuntimeError as e:
            raise AuthenticationError(
                message=str(e),
                hint="Close some Chrome instances and try again.",
            )
        
        if not launch_chrome(port):
            raise AuthenticationError(
                message="Failed to launch Chrome",
                hint="Try 'nlm login --manual' to import cookies from a file.",
            )
        
        debugger_url = get_debugger_url(port)
    
    if not debugger_url:
        raise AuthenticationError(
            message=f"Cannot connect to Chrome on port {port}",
            hint="Use 'nlm login --manual' to import cookies from a file.",
        )
    
    # Find or create NotebookLM page
    page = find_or_create_notebooklm_page(port)
    if not page:
        raise AuthenticationError(
            message="Failed to open NotebookLM page",
            hint="Try manually navigating to notebooklm.google.com in Chrome.",
        )
    
    ws_url = page.get("webSocketDebuggerUrl")
    if not ws_url:
        raise AuthenticationError(
            message="No WebSocket URL for page",
            hint="Chrome may need to be restarted.",
        )
    
    # Navigate to NotebookLM if needed
    current_url = page.get("url", "")
    if "notebooklm.google.com" not in current_url:
        navigate_to_url(ws_url, NOTEBOOKLM_URL)
    
    # Check login status
    current_url = get_current_url(ws_url)
    
    if not is_logged_in(current_url) and wait_for_login:
        # Wait for login
        start_time = time.time()
        while time.time() - start_time < login_timeout:
            time.sleep(5)
            try:
                current_url = get_current_url(ws_url)
                if is_logged_in(current_url):
                    break
            except Exception:
                pass
        
        if not is_logged_in(current_url):
            raise AuthenticationError(
                message="Login timeout",
                hint="Please log in to NotebookLM in the Chrome window.",
            )
    
    # Extract cookies
    cookies = get_page_cookies(ws_url)
    
    if not cookies:
        raise AuthenticationError(
            message="No cookies extracted",
            hint="Make sure you're fully logged in.",
        )
    
    # Get page HTML for CSRF and session ID
    html = get_page_html(ws_url)
    csrf_token = extract_csrf_token(html)
    session_id = extract_session_id(html)
    
    return {
        "cookies": cookies,
        "csrf_token": csrf_token,
        "session_id": session_id,
    }
```

## File: `src/nlm/utils/config.py`
```python
"""Configuration management for NLM CLI."""

import os
from pathlib import Path
from typing import Any

from platformdirs import user_config_dir, user_data_dir
from pydantic import BaseModel, Field


class OutputConfig(BaseModel):
    """Output formatting configuration."""

    format: str = Field(default="table", description="Default output format: table, json, compact")
    color: bool = Field(default=True, description="Enable colored output")
    short_ids: bool = Field(default=True, description="Show abbreviated IDs by default")


class AuthConfig(BaseModel):
    """Authentication configuration."""

    browser: str = Field(default="auto", description="Browser for auth: auto, chrome, firefox, safari, edge, brave")
    default_profile: str = Field(default="default", description="Default profile name")


class Config(BaseModel):
    """Main configuration model."""

    output: OutputConfig = Field(default_factory=OutputConfig)
    auth: AuthConfig = Field(default_factory=AuthConfig)


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    # Check for environment override
    if env_path := os.environ.get("NLM_CONFIG_PATH"):
        return Path(env_path)
    # Use platformdirs for cross-platform support
    return Path(user_config_dir("nlm", ensure_exists=True))


def get_data_dir() -> Path:
    """Get the data directory path (for profiles/credentials)."""
    if env_path := os.environ.get("NLM_PROFILE_PATH"):
        return Path(env_path)
    return Path(user_data_dir("nlm", ensure_exists=True))


def get_profiles_dir() -> Path:
    """Get the profiles directory path."""
    return get_data_dir() / "profiles"


def get_profile_dir(profile_name: str = "default") -> Path:
    """Get directory for a specific profile."""
    return get_profiles_dir() / profile_name


def get_config_file() -> Path:
    """Get the config file path."""
    return get_config_dir() / "config.toml"


def load_config() -> Config:
    """Load configuration from file and environment."""
    config_file = get_config_file()
    config_data: dict[str, Any] = {}
    
    # Load from file if exists
    if config_file.exists():
        try:
            import tomllib
            with open(config_file, "rb") as f:
                config_data = tomllib.load(f)
        except Exception:
            pass  # Use defaults on error
    
    # Apply environment overrides
    if output_format := os.environ.get("NLM_OUTPUT_FORMAT"):
        config_data.setdefault("output", {})["format"] = output_format
    
    if os.environ.get("NLM_NO_COLOR"):
        config_data.setdefault("output", {})["color"] = False
    
    if browser := os.environ.get("NLM_BROWSER"):
        config_data.setdefault("auth", {})["browser"] = browser
    
    if profile := os.environ.get("NLM_PROFILE"):
        config_data.setdefault("auth", {})["default_profile"] = profile
    
    return Config(**config_data)


def save_config(config: Config) -> None:
    """Save configuration to file."""
    config_file = get_config_file()
    config_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert to TOML format
    toml_content = _config_to_toml(config)
    config_file.write_text(toml_content)


def _config_to_toml(config: Config) -> str:
    """Convert config model to TOML string."""
    lines = []
    
    lines.append("[output]")
    lines.append(f'format = "{config.output.format}"')
    lines.append(f'color = {"true" if config.output.color else "false"}')
    lines.append(f'short_ids = {"true" if config.output.short_ids else "false"}')
    lines.append("")
    
    lines.append("[auth]")
    lines.append(f'browser = "{config.auth.browser}"')
    lines.append(f'default_profile = "{config.auth.default_profile}"')
    lines.append("")
    
    return "\n".join(lines)


# Global config instance (lazy loaded)
_config: Config | None = None


def get_config() -> Config:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = load_config()
    return _config


def reset_config() -> None:
    """Reset the global configuration (for testing)."""
    global _config
    _config = None
```

## File: `tests/__init__.py`
```python
"""Tests package for NLM."""
```

## File: `tests/run_e2e_tests.py`
```python
#!/usr/bin/env python3
"""
NotebookLM CLI - End-to-End Test Runner

This script runs comprehensive tests against the NLM CLI to verify all
functionality works correctly before GA release.

Usage:
    python tests/run_e2e_tests.py
    python tests/run_e2e_tests.py --skip-interactive  # Skip Drive sync tests
    python tests/run_e2e_tests.py --keep-notebook     # Don't delete test notebook
"""

import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class TestStatus(Enum):
    PASSED = "✓"
    FAILED = "✗"
    SKIPPED = "○"
    WARNING = "⚠"


@dataclass
class TestResult:
    name: str
    status: TestStatus
    duration: float = 0.0
    output: str = ""
    error: str = ""


@dataclass
class TestContext:
    """Shared context across tests."""
    notebook_id: str = ""
    source_ids: list = field(default_factory=list)
    conversation_id: str = ""
    deep_task_id: str = ""
    fast_task_id: str = ""
    drive_doc_id: str = ""
    drive_doc_title: str = ""
    drive_doc_type: str = "doc"


class TestRunner:
    """E2E test runner for NLM CLI."""
    
    # Hardcoded test resources
    TEST_YOUTUBE_URL = "https://www.youtube.com/watch?v=d-PZDQlO4m4"
    TEST_URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    # Public read-only Google Doc for automated testing (source add only, not sync)
    TEST_DRIVE_DOC_ID = "1KcEFkycep4QZTuZ7OkLVWkNZ2sIeqCKULfz9EhWLCw8"
    TEST_DRIVE_DOC_TITLE = "NLM CLI Test Document"
    
    def __init__(
        self,
        throttle_seconds: float = 2.0,
        skip_interactive: bool = False,
        keep_notebook: bool = False,
    ):
        self.throttle = throttle_seconds
        self.skip_interactive = skip_interactive
        self.keep_notebook = keep_notebook
        self.results: list[TestResult] = []
        self.ctx = TestContext()
        self.start_time = None
    
    def run_command(self, cmd: str, timeout: int = 120) -> tuple[int, str, str]:
        """Run a shell command and return (exit_code, stdout, stderr)."""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return -1, "", f"Command timed out after {timeout}s"
        except Exception as e:
            return -1, "", str(e)
    
    def run_nlm(self, args: str, timeout: int = 120) -> tuple[int, str, str]:
        """Run nlm command with args."""
        return self.run_command(f"nlm {args}", timeout)
    
    def throttle_wait(self):
        """Wait between API calls to avoid rate limits."""
        time.sleep(self.throttle)
    
    def print_header(self, text: str):
        """Print a section header."""
        print(f"\n{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}\n")
    
    def print_result(self, result: TestResult):
        """Print a single test result."""
        status_color = {
            TestStatus.PASSED: "\033[92m",  # Green
            TestStatus.FAILED: "\033[91m",  # Red
            TestStatus.SKIPPED: "\033[93m", # Yellow
            TestStatus.WARNING: "\033[93m", # Yellow
        }
        reset = "\033[0m"
        
        color = status_color.get(result.status, "")
        print(f"  {color}{result.status.value}{reset} {result.name} ({result.duration:.2f}s)")
        
        if result.status == TestStatus.FAILED and result.error:
            for line in result.error.strip().split("\n")[:3]:
                print(f"      {line}")
    
    def run_test(self, name: str, cmd: str, check_fn=None, timeout: int = 120) -> TestResult:
        """Run a single test."""
        start = time.time()
        exit_code, stdout, stderr = self.run_nlm(cmd, timeout)
        duration = time.time() - start
        
        # Default check: exit code 0
        if check_fn:
            try:
                passed = check_fn(exit_code, stdout, stderr)
            except Exception as e:
                passed = False
                stderr = f"Check function error: {e}\n{stderr}"
        else:
            passed = exit_code == 0
        
        result = TestResult(
            name=name,
            status=TestStatus.PASSED if passed else TestStatus.FAILED,
            duration=duration,
            output=stdout,
            error=stderr if not passed else "",
        )
        
        self.results.append(result)
        self.print_result(result)
        self.throttle_wait()
        
        return result
    
    def skip_test(self, name: str, reason: str = "") -> TestResult:
        """Mark a test as skipped."""
        result = TestResult(
            name=name,
            status=TestStatus.SKIPPED,
            error=reason,
        )
        self.results.append(result)
        self.print_result(result)
        return result
    
    def extract_uuid(self, text: str) -> str | None:
        """Extract a UUID from text."""
        match = re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', text)
        return match.group(0) if match else None
    
    def prompt_user(self, message: str) -> str:
        """Prompt user for input."""
        print(f"\n>>> {message}")
        return input(">>> ").strip()
    
    def pause_for_user(self, message: str):
        """Pause and wait for user to press Enter."""
        print(f"\n⏸️  {message}")
        input("   Press Enter to continue...")
    
    # =========================================================================
    # Pre-Test Setup
    # =========================================================================
    
    def setup(self) -> bool:
        """Interactive setup before running tests."""
        self.print_header("NLM CLI End-to-End Test Suite")
        
        print("This script will test all CLI commands against your NotebookLM account.")
        print("It will create a test notebook, add sources, and clean up afterward.\n")
        
        # Check auth
        print("Checking authentication...")
        exit_code, stdout, stderr = self.run_nlm("login --check")
        if exit_code != 0:
            print(f"\n❌ Authentication failed. Please run 'nlm login' first.")
            print(f"   Error: {stderr or stdout}")
            return False
        print(f"✓ {stdout.strip()}\n")
        
        # Prompt for Drive document
        print("-" * 50)
        print("DRIVE DOCUMENT SETUP")
        print("-" * 50)
        print("\nFor the staleness/sync test, you need a Google Drive document you can edit.")
        print("Example URL: https://docs.google.com/document/d/YOUR_DOC_ID/edit")
        print(f"\nDefault (read-only, for source add test only): {self.TEST_DRIVE_DOC_ID[:20]}...\n")
        
        drive_url = self.prompt_user("Enter your Drive document URL (or press Enter to use default):")
        
        if drive_url:
            # Extract doc ID from URL
            match = re.search(r'/d/([a-zA-Z0-9_-]+)', drive_url)
            if match:
                self.ctx.drive_doc_id = match.group(1)
                self.ctx.drive_doc_title = self.prompt_user("Enter a title for this document:") or "Test Drive Doc"
                
                # Detect type
                if "slides" in drive_url:
                    self.ctx.drive_doc_type = "slides"
                elif "sheets" in drive_url:
                    self.ctx.drive_doc_type = "sheets"
                else:
                    self.ctx.drive_doc_type = "doc"
                
                print(f"\n✓ Drive doc configured: {self.ctx.drive_doc_id[:20]}...")
                print(f"\n⚠️  REMEMBER: Later you'll be asked to edit this document for the freshness test.")
                print("   Keep it open in another browser tab!")
            else:
                print("⚠️  Could not extract doc ID from URL. Using default read-only doc.")
                self.ctx.drive_doc_id = self.TEST_DRIVE_DOC_ID
                self.ctx.drive_doc_title = self.TEST_DRIVE_DOC_TITLE
                self.ctx.drive_doc_type = "doc"
        else:
            # Use default public doc
            print("✓ Using default public test document (read-only, sync tests will be skipped).")
            self.ctx.drive_doc_id = self.TEST_DRIVE_DOC_ID
            self.ctx.drive_doc_title = self.TEST_DRIVE_DOC_TITLE
            self.ctx.drive_doc_type = "doc"
        
        print("\n" + "-" * 50)
        confirm = self.prompt_user("Ready to start tests? (y/n):").lower()
        return confirm in ("y", "yes", "")
    
    # =========================================================================
    # Test Groups
    # =========================================================================
    
    def test_group_1_auth(self):
        """Test Group 1: Authentication."""
        self.print_header("Test Group 1: Authentication")
        
        # Help
        self.run_test(
            "login --help",
            "login --help",
            lambda c, o, e: "--manual" in o and "--check" in o,
        )
        
        # Check valid auth
        self.run_test(
            "login --check (valid)",
            "login --check",
            lambda c, o, e: "Authentication valid" in o or "Notebooks found" in o,
        )
    
    def test_group_2_create_notebook(self):
        """Test Group 2: Create test notebook."""
        self.print_header("Test Group 2: Setup - Create Test Notebook")
        
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        title = f"NLM CLI Test {timestamp}"
        
        result = self.run_test(
            "notebook create",
            f'notebook create "{title}"',
            lambda c, o, e: c == 0 and ("Created" in o or self.extract_uuid(o)),
        )
        
        # Extract notebook ID
        self.ctx.notebook_id = self.extract_uuid(result.output)
        if self.ctx.notebook_id:
            print(f"\n   📓 Test Notebook ID: {self.ctx.notebook_id}")
        else:
            print("\n   ❌ Failed to extract notebook ID!")
            return False
        
        # Verify
        self.run_test(
            "notebook get",
            f"notebook get {self.ctx.notebook_id}",
        )
        
        return True
    
    def test_group_3_fast_research(self):
        """Test Group 3: Fast research (complete cycle - runs first to avoid conflicts)."""
        self.print_header("Test Group 3: Fast Research (Complete Cycle)")
        
        print("   Running fast research first (~30s)...\n")
        
        result = self.run_test(
            "research start (fast)",
            f'research start "machine learning basics" --mode fast --notebook-id {self.ctx.notebook_id}',
            timeout=30,
        )
        
        # Extract task ID
        task_match = re.search(r'Task ID: ([a-zA-Z0-9_-]+)', result.output)
        if task_match:
            self.ctx.fast_task_id = task_match.group(1)
            print(f"   ⚡ Fast Research Task ID: {self.ctx.fast_task_id}")
        
        # Wait for completion - verify it actually says "completed"
        self.run_test(
            "research status (fast)",
            f"research status {self.ctx.notebook_id} --max-wait 45",
            lambda c, o, e: c == 0 and ("completed" in o.lower() or "sources found" in o.lower()),
            timeout=120,
        )
        
        # Import sources - verify at least 1 source was imported
        self.run_test(
            "research import (fast)",
            f"research import {self.ctx.notebook_id}",
            lambda c, o, e: c == 0 and "Imported" in o and "0 source" not in o,
        )
    
    def test_group_4_sources(self):
        """Test Group 4: Source management."""
        self.print_header("Test Group 4: Source Management")
        
        # Add URL source
        self.run_test(
            "source add (URL)",
            f"source add {self.ctx.notebook_id} --url {self.TEST_URL}",
        )
        
        # Add YouTube source
        self.run_test(
            "source add (YouTube)",
            f"source add {self.ctx.notebook_id} --url {self.TEST_YOUTUBE_URL}",
        )
        
        # Add text source
        self.run_test(
            "source add (text)",
            f'source add {self.ctx.notebook_id} --text "Test content about machine learning and AI." --title "Test Text Doc"',
        )
        
        # Add Drive source if available
        if self.ctx.drive_doc_id:
            self.run_test(
                "source add (Drive)",
                f'source add {self.ctx.notebook_id} --drive {self.ctx.drive_doc_id} --title "{self.ctx.drive_doc_title}" --type {self.ctx.drive_doc_type}',
            )
        else:
            self.skip_test("source add (Drive)", "No Drive document provided")
        
        # List sources
        result = self.run_test(
            "source list",
            f"source list {self.ctx.notebook_id}",
        )
        
        # Extract source IDs
        for uuid in re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', result.output):
            if uuid not in self.ctx.source_ids:
                self.ctx.source_ids.append(uuid)
        
        if self.ctx.source_ids:
            print(f"\n   📎 Found {len(self.ctx.source_ids)} source(s)")
        
        # Test variations
        self.run_test("source list --json", f"source list {self.ctx.notebook_id} --json")
        self.run_test("source list --quiet", f"source list {self.ctx.notebook_id} --quiet")
        self.run_test("source list --drive", f"source list {self.ctx.notebook_id} --drive")
        self.run_test("source list --drive --skip-freshness", f"source list {self.ctx.notebook_id} --drive --skip-freshness")
        
        # Source operations on first source
        if self.ctx.source_ids:
            src_id = self.ctx.source_ids[0]
            self.run_test("source get", f"source get {src_id}")
            self.run_test("source describe", f"source describe {src_id}")
            self.run_test("source content", f"source content {src_id}")
            self.run_test("source content --output", f"source content {src_id} --output /tmp/nlm_test_content.txt")
    
    def test_group_5_notebook_operations(self):
        """Test Group 5: Notebook operations."""
        self.print_header("Test Group 5: Notebook Operations")
        
        # List variations
        self.run_test("notebook list", "notebook list")
        self.run_test("notebook list --json", "notebook list --json")
        self.run_test("notebook list --quiet", "notebook list --quiet")
        self.run_test("notebook list --title", "notebook list --title")
        self.run_test("notebook list --full", "notebook list --full")
        
        # Describe
        self.run_test(
            "notebook describe",
            f"notebook describe {self.ctx.notebook_id}",
        )
        
        # Rename
        self.run_test(
            "notebook rename",
            f'notebook rename {self.ctx.notebook_id} "NLM CLI Test - Renamed"',
        )
    
    def test_group_5b_config(self):
        """Test Group 5b: Configuration commands."""
        self.print_header("Test Group 5b: Configuration")
        
        self.run_test("config show", "config show")
        self.run_test("config show --json", "config show --json")
        self.run_test("config get auth.default_profile", "config get auth.default_profile")
    
    def test_group_6_query_chat(self):
        """Test Group 6: Query and chat configuration."""
        self.print_header("Test Group 6: Query & Chat")
        
        # Basic query
        result = self.run_test(
            "notebook query",
            f'notebook query {self.ctx.notebook_id} "What topics are covered in these sources?"',
            timeout=60,
        )
        
        # Extract conversation ID
        conv_match = re.search(r'Conversation ID: ([a-zA-Z0-9_-]+)', result.output)
        if conv_match:
            self.ctx.conversation_id = conv_match.group(1)
        
        # Follow-up query
        if self.ctx.conversation_id:
            self.run_test(
                "notebook query (follow-up)",
                f'notebook query {self.ctx.notebook_id} "Tell me more" --conversation-id {self.ctx.conversation_id}',
                timeout=60,
            )
        
        # Chat configuration
        self.run_test(
            "chat configure (learning_guide)",
            f"chat configure {self.ctx.notebook_id} --goal learning_guide",
        )
        
        self.run_test(
            "chat configure (custom prompt)",
            f'chat configure {self.ctx.notebook_id} --goal custom --prompt "Be concise"',
        )
        
        self.run_test(
            "chat configure (response length)",
            f"chat configure {self.ctx.notebook_id} --response-length shorter",
        )
    
    def test_group_7_content_generation(self):
        """Test Group 7: Content generation."""
        self.print_header("Test Group 7: Content Generation")
        
        print("   Generating content... (this may take a moment)\n")
        
        # Audio
        self.run_test(
            "audio create",
            f"audio create {self.ctx.notebook_id} --format brief --length short --confirm",
            timeout=60,
        )
        time.sleep(3)  # Extra throttle for generation
        
        # Report
        self.run_test(
            "report create",
            f'report create {self.ctx.notebook_id} --format "Briefing Doc" --confirm',
            timeout=60,
        )
        time.sleep(3)
        
        # Quiz
        self.run_test(
            "quiz create",
            f"quiz create {self.ctx.notebook_id} --count 2 --difficulty 2 --confirm",
            timeout=60,
        )
        
        # Flashcards
        self.run_test(
            "flashcards create",
            f"flashcards create {self.ctx.notebook_id} --difficulty medium --confirm",
            timeout=60,
        )
        
        # Mind map
        self.run_test(
            "mindmap create",
            f'mindmap create {self.ctx.notebook_id} --title "Test Mind Map" --confirm',
            timeout=60,
        )
        
        # Note: mindmap list is deprecated - use studio status which includes mindmaps
        
        # Studio status (includes all artifacts + mindmaps)
        self.run_test(
            "studio status",
            f"studio status {self.ctx.notebook_id}",
        )
        
        self.run_test(
            "studio status --full",
            f"studio status {self.ctx.notebook_id} --full",
        )
    
    def test_group_8_start_deep_research(self):
        """Test Group 8: Start deep research (background task - after fast research completes)."""
        self.print_header("Test Group 8: Start Deep Research (Background)")
        
        print("   Starting deep research - this runs in background while we do other tests...\n")
        
        result = self.run_test(
            "research start (deep)",
            f'research start "artificial intelligence applications" --mode deep --notebook-id {self.ctx.notebook_id} --force',
            timeout=30,
        )
        
        # Extract task ID if available
        task_match = re.search(r'Task ID: ([a-zA-Z0-9_-]+)', result.output)
        if task_match:
            self.ctx.deep_task_id = task_match.group(1)
            print(f"   🔬 Deep Research Task ID: {self.ctx.deep_task_id}")
    
    def test_group_9_deep_research(self):
        """Test Group 9: Check deep research (should be done by now)."""
        self.print_header("Test Group 9: Deep Research Check")
        
        if not self.ctx.deep_task_id:
            self.skip_test("research status (deep)", "No deep research task started")
            return
        
        print("   Checking deep research status (may need to wait up to 5 min)...\n")
        
        # Wait for completion - verify it actually says "completed"
        self.run_test(
            "research status (deep)",
            f"research status {self.ctx.notebook_id} --max-wait 300",
            lambda c, o, e: c == 0 and ("completed" in o.lower() or "sources found" in o.lower()),
            timeout=360,
        )
        
        # Import sources - verify at least 1 source was imported
        self.run_test(
            "research import (deep)",
            f"research import {self.ctx.notebook_id}",
            lambda c, o, e: c == 0 and "Imported" in o and "0 source" not in o,
        )
    
    def test_group_10_drive_sync(self):
        """Test Group 10: Drive sync (interactive)."""
        self.print_header("Test Group 10: Drive Sync (Interactive)")
        
        # Skip if no drive doc, or skip_interactive, or using default read-only doc
        using_default_doc = self.ctx.drive_doc_id == self.TEST_DRIVE_DOC_ID
        
        if not self.ctx.drive_doc_id:
            self.skip_test("source stale", "No Drive document configured")
            self.skip_test("source sync", "No Drive document configured")
            return
        
        if self.skip_interactive or using_default_doc:
            reason = "Using read-only default doc" if using_default_doc else "Running in non-interactive mode"
            self.skip_test("source stale", reason)
            self.skip_test("source sync", reason)
            return
        
        # Initial freshness check
        self.run_test(
            "source stale (initial)",
            f"source stale {self.ctx.notebook_id}",
        )
        
        # Pause for user to edit document
        self.pause_for_user(
            "Please make a small edit to your Drive document now.\n"
            "   (Add a line of text, change a word, etc.)\n"
            "   Then press Enter to continue..."
        )
        
        time.sleep(5)  # Wait for Drive to sync
        
        # Check staleness
        self.run_test(
            "source stale (after edit)",
            f"source stale {self.ctx.notebook_id}",
        )
        
        # Sync
        self.run_test(
            "source sync",
            f"source sync {self.ctx.notebook_id} --confirm",
        )
        
        # Verify fresh
        self.run_test(
            "source stale (after sync)",
            f"source stale {self.ctx.notebook_id}",
        )
    
    def test_group_11_cleanup(self):
        """Test Group 11: Cleanup."""
        self.print_header("Test Group 11: Cleanup")
        
        if self.keep_notebook:
            print(f"   📓 Keeping test notebook: {self.ctx.notebook_id}")
            self.skip_test("notebook delete", "--keep-notebook flag set")
            return
        
        if not self.ctx.notebook_id:
            self.skip_test("notebook delete", "No notebook to delete")
            return
        
        self.run_test(
            "notebook delete",
            f"notebook delete {self.ctx.notebook_id} --confirm",
        )
    
    # =========================================================================
    # Main Runner
    # =========================================================================
    
    def run_all(self) -> int:
        """Run all test groups."""
        self.start_time = time.time()
        
        if not self.setup():
            print("\n❌ Setup cancelled or failed.")
            return 1
        
        try:
            self.test_group_1_auth()
            
            if not self.test_group_2_create_notebook():
                print("\n❌ Failed to create test notebook. Aborting.")
                return 1
            
            self.test_group_3_fast_research()  # Fast research first (complete cycle)
            self.test_group_4_sources()
            self.test_group_5_notebook_operations()
            self.test_group_5b_config()
            self.test_group_6_query_chat()
            self.test_group_7_content_generation()
            self.test_group_8_start_deep_research()  # Deep research starts here (runs in background)
            self.test_group_9_deep_research()  # Check deep research completion
            self.test_group_10_drive_sync()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Tests interrupted!")
        finally:
            self.test_group_11_cleanup()
        
        self.print_summary()
        
        # Return exit code based on failures
        failed = sum(1 for r in self.results if r.status == TestStatus.FAILED)
        return 1 if failed > 0 else 0
    
    def print_summary(self):
        """Print test summary."""
        total_time = time.time() - self.start_time
        
        passed = sum(1 for r in self.results if r.status == TestStatus.PASSED)
        failed = sum(1 for r in self.results if r.status == TestStatus.FAILED)
        skipped = sum(1 for r in self.results if r.status == TestStatus.SKIPPED)
        total = len(self.results)
        
        self.print_header("Test Summary")
        
        print(f"   Total:   {total}")
        print(f"   Passed:  \033[92m{passed}\033[0m")
        print(f"   Failed:  \033[91m{failed}\033[0m")
        print(f"   Skipped: \033[93m{skipped}\033[0m")
        print(f"   Time:    {total_time:.1f}s")
        
        if failed > 0:
            print("\n   Failed tests:")
            for r in self.results:
                if r.status == TestStatus.FAILED:
                    print(f"     - {r.name}")
        
        print()
        if failed == 0:
            print("   🎉 All tests passed! Ready for GA.")
        else:
            print(f"   ⚠️  {failed} test(s) failed. Please review and fix.")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="NLM CLI End-to-End Tests")
    parser.add_argument(
        "--skip-interactive",
        action="store_true",
        help="Skip tests that require user interaction (Drive sync)",
    )
    parser.add_argument(
        "--keep-notebook",
        action="store_true",
        help="Don't delete the test notebook after tests",
    )
    parser.add_argument(
        "--throttle",
        type=float,
        default=2.0,
        help="Seconds to wait between API calls (default: 2.0)",
    )
    
    args = parser.parse_args()
    
    runner = TestRunner(
        throttle_seconds=args.throttle,
        skip_interactive=args.skip_interactive,
        keep_notebook=args.keep_notebook,
    )
    
    exit_code = runner.run_all()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
```

