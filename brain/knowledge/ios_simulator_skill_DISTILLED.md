---
id: ios-simulator-skill
type: knowledge
owner: OA_Triage
---
# ios-simulator-skill
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/conorluddy/ios-simulator-skill)

# iOS Simulator Skill for Claude Code

Production-ready automation for iOS app testing and building. 21 scripts optimized for both human developers and AI agents.

This is basically a Skill version of my XCode MCP: [https://github.com/conorluddy/xc-mcp](https://github.com/conorluddy/xc-mcp)


> [!WARNING]
> You want to take the `ios-simulator-skill` directory from this repo and drop it into your skills directory - not this entire repo. I'll update this soon with an easier approach. Feel free to fork this and get Claude to adjust it to your specific needs.


MCPs load a lot of tokens into the context window when they're active, but also seem to work really well. Skills don't load in any context. I'll make a plugin next and try to find the balance...

Updated: The Plugin version lets you easily disable MCPs for different tool groups. Optimise your context window by only enabling the tools you're actively using, such as xcodebuild: [https://github.com/conorluddy/xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)

## What It Does

Instead of pixel-based navigation that breaks when UI changes:

```bash
# Fragile - breaks if UI changes
idb ui tap 320 400

# Robust - finds by meaning
python scripts/navigator.py --find-text "Login" --tap
```

Uses semantic navigation on accessibility APIs to interact with elements by their meaning, not coordinates. Works across different screen sizes and survives UI redesigns.

## Features

- **21 production scripts** for building, testing, and automation
- **Semantic navigation** - find elements by text, type, or ID
- **Token optimized** - 96% reduction vs raw tools (3-5 lines default)
- **Zero configuration** - works immediately on macOS with Xcode
- **Structured output** - JSON and formatted text, easy to parse
- **Auto-UDID detection** - no need to specify device each time
- **Batch operations** - boot, delete, erase multiple simulators at once
- **Comprehensive testing** - WCAG compliance, visual diffs, accessibility audits
- **CI/CD ready** - JSON output, exit codes, automated device lifecycle

## Installation

### As Claude Code Skill

```bash
# Personal installation
git clone https://github.com/conorluddy/ios-simulator-skill.git ~/.claude/skills/ios-simulator-skill

# Project installation
git clone https://github.com/conorluddy/ios-simulator-skill.git .claude/skills/ios-simulator-skill
```

Restart Claude Code. The skill loads automatically.

### From Release

```bash
# Download latest release
curl -L https://github.com/conorluddy/ios-simulator-skill/releases/download/vX.X.X/ios-simulator-skill-vX.X.X.zip -o skill.zip

# Extract
unzip skill.zip -d ~/.claude/skills/ios-simulator-skill
```

## Prerequisites

- macOS 12+
- Xcode Command Line Tools (`xcode-select --install`)
- Python 3
- IDB (optional, for interactive features: `brew tap facebook/fb && brew install idb-companion`)

## Quick Start

```bash
# 1. Check environment
bash ~/.claude/skills/ios-simulator-skill/scripts/sim_health_check.sh

# 2. Launch your app
python ~/.claude/skills/ios-simulator-skill/scripts/app_launcher.py --launch com.example.app

# 3. See what's on screen
python ~/.claude/skills/ios-simulator-skill/scripts/screen_mapper.py
# Output:
# Screen: LoginViewController (45 elements, 7 interactive)
# Buttons: "Login", "Cancel", "Forgot Password"
# TextFields: 2 (0 filled)

# 4. Tap login button
python ~/.claude/skills/ios-simulator-skill/scripts/navigator.py --find-text "Login" --tap

# 5. Enter text
python ~/.claude/skills/ios-simulator-skill/scripts/navigator.py --find-type TextField --enter-text "user@test.com"

# 6. Check accessibility
python ~/.claude/skills/ios-simulator-skill/scripts/accessibility_audit.py
```

## 21 Scripts Organized by Category

### Build & Development
- **build_and_test.py** - Build projects, run tests, parse results
- **log_monitor.py** - Real-time log monitoring

### Navigation & Interaction
- **screen_mapper.py** - Analyze current screen
- **navigator.py** - Find and interact with elements
- **gesture.py** - Swipes, scrolls, pinches
- **keyboard.py** - Text input and hardware buttons
- **app_launcher.py** - App lifecycle control

### Testing & Analysis
- **accessibility_audit.py** - WCAG compliance checking
- **visual_diff.py** - Screenshot comparison
- **test_recorder.py** - Automated test documentation
- **app_state_capture.py** - Debugging snapshots
- **sim_health_check.sh** - Environment verification

### Advanced Testing & Permissions
- **clipboard.py** - Clipboard management
- **status_bar.py** - Status bar control
- **push_notification.py** - Push notifications
- **privacy_manager.py** - Permission management

### Device Lifecycle
- **simctl_boot.py** - Boot simulator
- **simctl_shutdown.py** - Shutdown simulator
- **simctl_create.py** - Create simulator
- **simctl_delete.py** - Delete simulator
- **simctl_erase.py** - Factory reset

See **SKILL.md** for complete reference.

## How It Works with Claude Code

Claude Code automatically detects when to use this skill based on your request. You don't need to manually invoke it.

**Example conversation:**

```
You: "Set up my iOS app for testing"
Claude: [Uses simctl_boot.py and app_launcher.py automatically]

You: "Tap the login button"
Claude: [Uses navigator.py to find and tap]

You: "Check if the form is accessible"
Claude: [Uses accessibility_audit.py]
```

You can also run scripts manually when needed.

## Usage Examples

### Example 1: Login Flow

```bash
# Launch app
python scripts/app_launcher.py --launch com.example.app

# Map screen to find fields
python scripts/screen_mapper.py

# Enter credentials
python scripts/navigator.py --find-type TextField --index 0 --enter-text "user@test.com"
python scripts/navigator.py --find-type SecureTextField --enter-text "password"

# Tap login
python scripts/navigator.py --find-text "Login" --tap

# Verify accessibility
python scripts/accessibility_audit.py
```

### Example 2: Test Documentation

```bash
# Record test execution
python scripts/test_recorder.py --test-name "Login Flow" --output test-reports/

# Generates:
# - Screenshots per step
# - Accessibility trees
# - Markdown report with timing
```

### Example 3: Visual Testing

```bash
# Capture baseline
python scripts/app_state_capture.py --output baseline/

# Make changes...

# Compare
python scripts/visual_diff.py baseline/screenshot.png current/screenshot.png
```

### Example 4: Permission Testing

```bash
# Grant permissions
python scripts/privacy_manager.py --bundle-id com.example.app --grant camera,location

# Test app behavior with permissions...

# Revoke permissions
python scripts/privacy_manager.py --bundle-id com.example.app --revoke camera,location
```

### Example 5: Device Lifecycle in CI/CD

```bash
# Create test device
DEVICE_ID=$(python scripts/simctl_create.py --device "iPhone 16 Pro" --json | jq -r '.new_udid')

# Run tests
python scripts/build_and_test.py --project MyApp.xcodeproj

# Clean up
python scripts/simctl_delete.py --udid $DEVICE_ID --yes
```

## Design Principles

**Semantic Navigation**: Find elements by meaning (text, type, ID) not pixel coordinates. Survives UI changes and works across device sizes.

**Token Efficiency**: Default output is 3-5 lines. Use `--verbose` for details or `--json` for machine parsing. 96% reduction vs raw tools.

**Accessibility-First**: Built on iOS accessibility APIs for reliability. Better for users with accessibility needs and more robust for automation.

**Zero Configuration**: Works immediately on any macOS with Xcode. No complex setup, no configuration files.

**Structured Data**: Scripts output JSON or formatted text, not raw logs. Easy to parse, integrate, and understand.

**Auto-Learning**: Build system learns your device preference and remembers it for next time.

## Requirements

**System:**
- macOS 12 or later
- Xcode Command Line Tools
- Python 3

**Optional:**
- IDB (for interactive features)
- Pillow (for visual_diff.py: `pip3 install pillow`)

## Documentation

- **SKILL.md** - Complete script reference and table of contents
- **CLAUDE.md** - Architecture and developer guide
- **references/** - Deep documentation on specific topics
- **examples/** - Complete automation workflows

## Output Efficiency

All scripts minimize output by default:

| Task | Raw Tools | This Skill | Savings |
|------|-----------|-----------|---------|
| Screen analysis | 200+ lines | 5 lines | 97.5% |
| Find & tap button | 100+ lines | 1 line | 99% |
| Enter text | 50+ lines | 1 line | 98% |
| Login flow | 400+ lines | 15 lines | 96% |

This efficiency keeps AI agent conversations focused and cost-effective.

## Evaluation

This skill is tested using [Claude Code evals](https://docs.claude.com/en/docs/claude-code/evals) — automated benchmarks that compare agent performance with and without the skill installed.

### Results (Iteration 1)

| Condition | Pass Rate |
|-----------|-----------|
| With skill | **100%** (3/3) |
| Without skill | **46%** (≈1.4/3) |

### What's Tested

Three eval scenarios cover the skill's core capabilities:

1. **Environment & Discovery** — Health check, list simulators, identify booted device
2. **Build & Navigate** — Build an app, launch it, map the screen, tap a button
3. **Test & Capture** — Accessibility audit, app state snapshot, status bar override

Each eval checks that the agent uses skill scripts (not raw `xcrun simctl`), follows progressive disclosure, and completes all requested steps.

### Running Evals

```bash
# From repo root
claude evals run evals/evals.json --skill ios-simulator-skill
```

Eval definitions live in `evals/evals.json`.

## Troubleshooting

### Environment Issues

```bash
# Run health check
bash ~/.claude/skills/ios-simulator-skill/scripts/sim_health_check.sh

# Checks: macOS, Xcode, simctl, IDB, Python, simulators, packages
```

### Script Help

```bash
# All scripts support --help
python scripts/navigator.py --help
python scripts/accessibility_audit.py --help
```

### Not Finding Elements

```bash
# Use verbose mode to see all elements
python scripts/screen_mapper.py --verbose

# Check for exact text match
python scripts/navigator.py --find-text "Exact Button Text" --tap
```

## Contributing

> [!WARNING]
> I appreciate contributions, but please note that this repo and my other public repos are far down in the priority queue of what I'm working on, so I'll be slow to review anything. Your best bet is really just to fork the repo and customise it to your own needs.

Contributions should:
- Maintain token efficiency (minimal default output)
- Follow accessibility-first design
- Support `--help` documentation
- Support `--json` for CI/CD
- Pass Black formatter and Ruff linter
- Include type hints
- Update SKILL.md

## License

MIT License - Allows commercial use and distribution.

## Support

- **Issues**: Create GitHub issue with reproduction steps
- **Documentation**: See SKILL.md and references/
- **Examples**: Check examples/ directory
- **Skills Docs**: https://docs.claude.com/en/docs/claude-code/skills

---

**Built for AI agents. Optimized for developers.**

```

### File: .pre-commit-config.yaml
```yaml
# Pre-commit hooks for ios-simulator-skill
# Install: pre-commit install
# Run manually: pre-commit run --all-files

repos:
  # Black - Code formatter
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black
        name: Format Python code with Black
        language_version: python3.12
        files: ^skill/scripts/.*\.py$

  # Ruff - Fast linter (replaces Flake8, isort, etc)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
        name: Lint with Ruff
        args: [--fix, --exit-non-zero-on-fix]
        files: ^skill/scripts/.*\.py$

  # General file checks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
        name: Trim trailing whitespace
      - id: end-of-file-fixer
        name: Fix end of files
      - id: check-yaml
        name: Check YAML syntax
      - id: check-added-large-files
        name: Check for large files
        args: ['--maxkb=500']
      - id: mixed-line-ending
        name: Fix mixed line endings
        args: ['--fix=lf']

```

### File: CLAUDE.md
```md
# CLAUDE.md - Developer Guide

This file provides guidance to Claude Code and developers working with this repository.

## Project Overview

iOS Simulator Skill is a production-ready Agent Skill providing 21 scripts for iOS app building, testing, and automation. It wraps Apple's `xcrun simctl` and Facebook's `idb` tools with semantic interfaces designed for AI agents and developers.

**Key Statistics:**
- 21 production scripts (~8,500 lines)
- 5 script categories (Build, Navigation, Testing, Permissions, Lifecycle)
- 6 shared utility modules (~1,400 lines)
- 100% token-optimized default output
- Full test coverage on all new features

## Project Structure

```
ios-simulator-skill/            # Repository root
├── ios-simulator-skill/        # Distributable package
│   ├── SKILL.md               # Entry point (table of contents)
│   └── scripts/               # 21 production scripts
│       ├── build_and_test.py
│       ├── xcode/             # Xcode integration module
│       ├── log_monitor.py
│       ├── screen_mapper.py
│       ├── navigator.py
│       ├── gesture.py
│       ├── keyboard.py
│       ├── app_launcher.py
│       ├── accessibility_audit.py
│       ├── visual_diff.py
│       ├── test_recorder.py
│       ├── app_state_capture.py
│       ├── clipboard.py
│       ├── status_bar.py
│       ├── push_notification.py
│       ├── privacy_manager.py
│       ├── simctl_boot.py
│       ├── simctl_shutdown.py
│       ├── simctl_create.py
│       ├── simctl_delete.py
│       ├── simctl_erase.py
│       ├── sim_health_check.sh
│       └── common/            # Shared utilities
├── .github/workflows/
├── pyproject.toml
└── README.md
```

## Architecture Patterns

### Pattern 1: Class-Based Script Design

All scripts use class-based architecture for testability:

```python
class DeviceManager:
    def __init__(self, udid: str | None = None):
        self.udid = udid

    def execute(self, **kwargs) -> tuple[bool, str]:
        # Return (success, message) tuple
        pass

def main():
    parser = argparse.ArgumentParser()
    manager = DeviceManager(args.udid)
    success, message = manager.execute()
    print(message)
    sys.exit(0 if success else 1)
```

### Pattern 2: Auto-UDID Detection

All scripts support optional `--udid` with auto-detection:

```python
try:
    udid = resolve_device_identifier(args.udid)  # May be None
except RuntimeError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
```

### Pattern 3: Output Formatting

Consistent format across all scripts:

```
# Default (3-5 lines)
Device booted: iPhone 16 Pro (ABC123) [2.1s]

# --verbose (50+ lines)
Device booted successfully.
Device UDID: ABC123DEF456...
Boot time: 2.1 seconds

# --json (20-30 lines)
{"action": "boot", "udid": "ABC123", "success": true}
```

### Pattern 4: Batch Operations

Most scripts support batch operations:

```bash
python scripts/simctl_boot.py --all
python scripts/simctl_boot.py --type iPhone
```

## Script Categories

### Build & Development (2)
- **build_and_test.py**: Build with progressive disclosure
- **log_monitor.py**: Real-time log monitoring

### Navigation & Interaction (5)
- **screen_mapper.py**: Analyze screen
- **navigator.py**: Semantic element finding
- **gesture.py**: Touch simulation
- **keyboard.py**: Text input and keys
- **app_launcher.py**: App lifecycle

### Testing & Analysis (5)
- **accessibility_audit.py**: WCAG compliance
- **visual_diff.py**: Screenshot comparison
- **test_recorder.py**: Test documentation
- **app_state_capture.py**: Debugging snapshots
- **sim_health_check.sh**: Environment verification

### Advanced Testing & Permissions (4)
- **clipboard.py**: Clipboard management
- **status_bar.py**: Status bar control
- **push_notification.py**: Push notifications
- **privacy_manager.py**: Permission management

### Device Lifecycle Management (5)
- **simctl_boot.py**: Boot device
- **simctl_shutdown.py**: Shutdown device
- **simctl_create.py**: Create device
- **simctl_delete.py**: Delete device
- **simctl_erase.py**: Reset device

## Shared Utilities

### device_utils.py (~450 lines)
- `resolve_device_identifier()`: UDID/name/booted resolution
- `list_simulators()`: List with state filtering
- `_extract_device_type()`: Parse device type from name

### screenshot_utils.py (~346 lines)
- `capture_screenshot()`: File or inline mode
- `generate_screenshot_name()`: Semantic naming
- `resize_screenshot()`: Token optimization

### cache_utils.py (~258 lines)
- `ProgressiveCache`: Large output caching with TTL

## Quality Standards

1. Type hints (modern Python syntax)
2. Docstrings on all functions
3. Specific exception handling
4. --help support on all scripts
5. Black formatter compliance
6. Ruff linter (0 errors)
7. Never use shell=True

## Token Efficiency

96% reduction in typical output:

- Default: 3-5 lines (5-10 tokens)
- Verbose: 50+ lines (400+ tokens)
- JSON: 20-30 lines (20-30 tokens)

This keeps AI agent conversations focused and cost-effective.

## Contributing

New scripts should:
- Use class-based design for > 50 lines of logic
- Support --udid and auto-detection
- Support --json output
- Provide --help documentation
- Follow Black and Ruff standards
- Update SKILL.md table of contents
- Work with real simulators before submission

## Release Process

1. Update version in SKILL.md frontmatter, pyproject.toml
2. Verify CI passes (Black, Ruff)
3. Create GitHub release with vX.X.X tag
4. Attach zipped ios-simulator-skill/ directory

## Design Philosophy

**Semantic**: Find elements by meaning, not pixels.

**Progressive**: Minimal output by default, details on demand.

**Accessible**: Built on standard iOS accessibility APIs.

**Zero-Config**: Works immediately with no setup.

**Structured**: JSON and formatted text, not raw logs.

**Reusable**: Common patterns across all scripts.

This design works for both developers and AI agents.

```

### File: DEV.md
```md
# iOS Simulator Skill - Development Repository

This is the **development repository** for the iOS Simulator Skill. Users should download the packaged skill from [GitHub Releases](https://github.com/YOUR_USERNAME/ios-simulator-skill/releases).

## What is This?

A production-ready Claude Code skill providing 21+ scripts for iOS simulator testing and automation with:
- 🏗️ **Ultra token-efficient build automation** with progressive disclosure
- 🔍 **Real-time log monitoring** with intelligent filtering
- 🎯 **Accessibility-driven navigation** (semantic, not pixel-based)
- ♿ **WCAG accessibility auditing**
- 📸 **Visual regression testing**
- 🎬 **Test recording and documentation**

**Total:** ~10,000 lines of production Python code

## For Users: Installation

Download the latest release and extract to your Claude skills directory:

```bash
# Download from releases
curl -L https://github.com/YOUR_USERNAME/ios-simulator-skill/releases/latest/download/ios-simulator-skill-v1.0.0.zip -o skill.zip

# Extract to Claude Code skills directory
unzip skill.zip -d ~/.claude/skills/ios-simulator-skill

# Restart Claude Code
```

See [`ios-simulator-skill/SKILL.md`](ios-simulator-skill/SKILL.md) for usage documentation.

## For Contributors: Development Setup

### Prerequisites

- macOS 11+ (required for iOS simulator)
- Xcode Command Line Tools: `xcode-select --install`
- Python 3.12+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ios-simulator-skill.git
cd ios-simulator-skill

# Install development dependencies
pip3 install black ruff mypy pre-commit

# Install pre-commit hooks
pre-commit install

# Verify setup
pre-commit run --all-files
```

### Development Workflow

```bash
# Make changes to ios-simulator-skill/scripts/
vim ios-simulator-skill/scripts/build_and_test.py

# Hooks run automatically on commit (Black, Ruff, mypy)
git add ios-simulator-skill/scripts/build_and_test.py
git commit -m "feat: improve build error reporting"

# Push and create PR
git push origin feature-branch
# Open PR on GitHub - lint workflow runs automatically
```

### Linting Tools

All code in `ios-simulator-skill/scripts/` is checked with **STRICT** configuration:

- **Black** - Auto-formats to consistent style (line length: 100)
- **Ruff** - Fast linter catching bugs, style issues, unused imports
- **mypy** - Strict type checking (all type hints required)

Configuration in [`pyproject.toml`](pyproject.toml).

### Running Linters Manually

```bash
# Format code
black ios-simulator-skill/scripts/

# Lint code (with auto-fix)
ruff check --fix ios-simulator-skill/scripts/

# Type check
mypy ios-simulator-skill/scripts/

# Or run all checks
pre-commit run --all-files
```

### Repository Structure

```
ios-simulator-skill/                   # Repository root
├── ios-simulator-skill/               # Distributable package (packaged in releases)
│   ├── SKILL.md                      # Entry point with YAML frontmatter
│   └── scripts/                      # 21+ production scripts (~10,000 lines)
│
├── .github/workflows/                 # CI/CD automation
│   ├── release.yml                   # Auto-package on release
│   ├── lint.yml                      # Run linters on PRs
│   └── validate-version.yml          # Ensure version consistency
│
├── pyproject.toml                     # Linting configuration
├── .pre-commit-config.yaml            # Git hooks
└── README.md                          # This file (dev guide)
```

### Creating a Release

```bash
# 1. Update version in pyproject.toml
vim pyproject.toml  # Update version = "1.1.0"

# 2. Commit version bump
git add pyproject.toml
git commit -m "chore: bump version to 1.1.0"
git push origin main

# 3. Create and push tag
git tag v1.1.0
git push origin v1.1.0

# 4. Create GitHub release
# Go to: https://github.com/YOUR_USERNAME/ios-simulator-skill/releases/new
# - Tag: v1.1.0
# - Title: "Release v1.1.0"
# - Description: (auto-generated or write your own)
# - Publish release

# 5. GitHub Actions automatically:
#    - Validates version consistency
#    - Packages skill/ directory
#    - Attaches ios-simulator-skill-v1.1.0.zip to release
```

### Testing

```bash
# Test scripts locally with booted simulator
open -a Simulator

# Run health check
bash ios-simulator-skill/scripts/sim_health_check.sh

# Test individual scripts
python ios-simulator-skill/scripts/build_and_test.py --help
python ios-simulator-skill/scripts/screen_mapper.py

# Test skill installation
mkdir -p ~/.claude/skills/ios-simulator-skill-test
cp -r ios-simulator-skill/* ~/.claude/skills/ios-simulator-skill-test/
# Restart Claude Code and verify
```

## Code Style Guidelines

From [`CLAUDE.md`](CLAUDE.md):

- **Jackson's Law**: Minimal code to solve the problem
- **Guard clauses**: Validate inputs first, happy path last
- **Functions < 50 lines**: Keep functions focused
- **Files < 300 lines**: Keep modules understandable
- **Actionable errors**: Always explain what failed and how to fix
- **Type hints**: All functions use type annotations (enforced by mypy --strict)
- **Security**: Never `shell=True`, always validate paths

## GitHub Actions Workflows

### release.yml
- **Trigger:** When release is published
- **Actions:** Validate structure → Zip ios-simulator-skill/ → Upload to release

### lint.yml
- **Trigger:** On PR to main (for Python files)
- **Actions:** Run Black, Ruff, mypy → Block merge if fails

### validate-version.yml
- **Trigger:** On release published
- **Actions:** Check pyproject.toml version matches git tag

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes (hooks will run on commit)
4. Push and create a PR
5. Wait for lint workflow to pass
6. Request review

## License

MIT License - see [LICENSE.md](LICENSE.md)

## Questions?

- **Usage questions**: See [ios-simulator-skill/SKILL.md](ios-simulator-skill/SKILL.md)
- **Bug reports**: [Open an issue](https://github.com/YOUR_USERNAME/ios-simulator-skill/issues)
- **Development questions**: [Open a discussion](https://github.com/YOUR_USERNAME/ios-simulator-skill/discussions)

```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2025 Conor Luddy

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

