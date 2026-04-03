---
id: github.com-takechanman1228-claude-ecom-7e538721-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:25.293723
---

# KNOWLEDGE EXTRACT: github.com_takechanman1228_claude-ecom_7e538721
> **Extracted on:** 2026-04-01 16:18:25
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525025/github.com_takechanman1228_claude-ecom_7e538721

---

## File: `.gitignore`
```
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.pytest_cache/
.ruff_cache/
.mypy_cache/
htmlcov/
.coverage
*.parquet
.venv/
.env
.claude-ecom/
.DS_Store
/review.json
/review_*.json
/REVIEW.md
/REVIEW_*.md
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-03-06

Initial release.

- Single `ecom review` command for full-store health review
- Multi-period architecture: 30d / 90d / 365d trailing windows with automatic data coverage detection
- ~30 health checks across Revenue (40%), Customer (30%), Product (30%)
- Each check returns pass / watch / fail
- KPI tree with growth drivers (AOV / volume / mix effects)
- review.json output with top issues and action candidates
- Claude Code skill (`/ecom review`) with full review and focused query modes
- Shopify CSV and generic CSV format support with fuzzy column mapping
- Install script for bash and PowerShell
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

## Project: claude-ecom

Ecommerce data analytics toolkit -- review and improve online stores.

## Architecture: Hybrid (Python Compute + LLM Interpretation)

```
Order CSV Data
    |
    v
Python CLI (ecom review)    <-- Deterministic: KPI calc, scoring, check evaluation
    |
    v
review.json / review_{period}.json   <-- Machine-readable structured data
    |
    v
Claude (SKILL.md)           <-- LLM: reads review.json + reference files, generates
    |                            natural language report with business interpretation
    v
REVIEW.md / REVIEW_{PERIOD}.md       <-- Human-readable: narrative insights, not just numbers
```

**Key principle:** Python computes the numbers. Claude interprets them.

## Structure

```
claude_ecom/          # Python package (pip install -e .)
  cli.py              # Click CLI: ecom review | validate
  loader.py           # CSV/Parquet data loading
  checks.py           # Check result types, impact estimation, action builders
  report.py           # Report generation (generate_review_json)
  review_engine.py    # Unified period-based review builder (30d/90d/365d)
  periods.py          # Trailing window + data coverage utilities
  scoring.py          # Health scoring, top issues, action candidates
skills/ecom/          # Claude Code skill (SKILL.md + references/)
  SKILL.md            # LLM instructions for interpreting review.json
  references/         # 6 reference files loaded on-demand for interpretation
tests/                # pytest test suite
```

## Commands

```bash
pip install -e ".[dev]"       # Install for development
pytest tests/ -v              # Run tests
ecom review orders.csv        # Run review (generates review.json)
ecom review orders.csv --period 90d  # Focus on specific period
```

## Conventions

- Package name: `claude-ecom` (pip), `claude_ecom` (import)
- CLI entry point: `ecom` (defined in pyproject.toml)
- Check IDs are semantic snake_case keys (e.g., `monthly_revenue_trend`, `repeat_purchase_rate`, `multi_item_order_rate`)
- 3 categories: Revenue, Customer, Product
- Each check returns pass / watch / fail (no numeric scores)
- Python handles computation; Claude handles interpretation
- Reference files (references/*.md) are the knowledge base for LLM interpretation
- Reports output to current directory by default (--output flag)
- Never present raw numbers without business context and actionable recommendations
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

Thanks for your interest in contributing to claude-ecom!

## Getting Started

```bash
git clone <your-fork-url>
cd claude-ecom
pip install -e ".[dev]"
pytest tests/ -v
```

## Adding New Checks

Each check produces a `CheckResult` with these fields:

```python
CheckResult(
    check_id="new_check_name",  # semantic snake_case key
    category="revenue",       # revenue | customer | product
    severity="high",          # critical | high | medium | low
    result="fail",            # pass | watch | warning | fail | na
    message="MoM revenue growth: -10.0%",
    current_value=-0.10,
    threshold=0.0,
)
```

**Severity guidelines:**

| Severity | When to use | Multiplier |
|----------|-------------|-----------|
| Critical | Direct revenue loss, data integrity | 5.0x |
| High | Significant missed opportunity | 3.0x |
| Medium | Improvement opportunity | 1.5x |
| Low | Nice-to-have optimization | 0.5x |

**Steps:**

1. Add the check function in the appropriate module (`claude_ecom/metrics.py`, `decomposition.py`, etc.)
2. Add the check definition to the matching reference file in `skills/ecom/references/`
3. Add the check to `_build_checks()` in `claude_ecom/review_engine.py`
4. Add a test in `tests/`
5. Run `pytest tests/ -v` to verify

## Pull Request Process

1. **Branch naming:** `feature/<description>`, `fix/<description>`, or `docs/<description>`
2. **Tests required:** All PRs must pass `pytest tests/ -v`
3. **Skill validation:** Run `bash validate-skills.sh` if skills were modified
4. **One concern per PR:** Keep PRs focused on a single change

## Skill Quality Checklist

Before submitting, verify:

- [ ] `name` in frontmatter matches directory name
- [ ] `description` includes trigger phrases for agent routing
- [ ] Check thresholds are backed by industry benchmarks or documented reasoning
- [ ] No hardcoded paths or credentials
- [ ] Tests cover the new/changed functionality
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Hajime Takeda

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

## File: `README.md`
```markdown


<p align="center">
  <img src="assets/banner.png" alt="Claude Ecom" width="100%">
</p>

# claude-ecom

Turn order/sales CSV into a business review — KPI decomposition, prioritized findings, and concrete next actions. One command.

<p align="center">
  <img src="assets/claude_ecom_demo.gif" alt="claude-ecom demo" width="100%">
</p>

---

## Who This Is For

- Data Analysts / Marketers who write monthly business reviews from scratch every time
- D2C brand owners, retail managers, or ecommerce managers without an analyst on staff
- Anyone who knows revenue dropped but can't explain why

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/takechanman1228/claude-ecom/v0.1.3/install.sh | bash

# Drop your orders CSV, Start Claude Code, and run:
/ecom review
```

Requires: Claude Code CLI, Python 3.10+, and git

### Alternative: Install as a Claude Code plugin

```
/plugin marketplace add takechanman1228/claude-ecom
/plugin install claude-ecom@claude-ecom
/reload-plugins
```

Restart Claude Code. The Python backend installs automatically on session start.
The command becomes `/claude-ecom:ecom review` when installed as a plugin.

## What You Get

A single `REVIEW.md` that reads like a consultant wrote it:


```
# Business Review
> Revenue reached $9.37M for the year, essentially flat YoY (-1.7%), despite strong
> short-term momentum — the last 90 days surged 84% and November posted +28.5%,
> both driven by Q4 seasonal demand rather than structural growth. The flat annual...
```

```
           30d Pulse       90d Momentum     365d Structure
Revenue    $1.47M (+ 28%)  $3.73M (+ 84%)   $9.37M (= -2%)
Orders     3,499 (+ 26%)   8,814 (+ 60%)    24,812 (- 11%)
AOV        $419 (+ 2%)     $424 (+ 15%)     $378 (+ 10%)
Customers  1,676 (+ 11%)   2,918 (+ 51%)    4,296 (= flat)
...
```
```
Revenue $9.37M (YoY: -1.7%)
├── 🔴 New Customer Revenue $1.45M (15.5%)
│   ├── New Customers: 1,559 (-57.8%)
│   └── New Customer AOV: $305
└── 🟢 Existing Customer Revenue $7.92M (84.5%)
    ├── Returning Customers: 2,737 (+345%)
    ├── Returning AOV: $395
    └── Repeat Purchase Rate: 75.4%
```
Executive summary → Multi-horizon dashboard → KPI trees with 🔴/🟢 signals → Findings with "what / why / what to do" → Prioritized action plan with deadlines, success metrics, and guardrails.
[See a full example output →](REVIEW.md)


## Commands

| Command | Description |
|---------|-------------|
| `/ecom review` | Full business review — auto-selects 30d / 90d / 365d |
| `/ecom review 30d` / `90d` / `365d` | Focus on a specific period |
| `/ecom review How's retention?` | Ask a question instead of a full report |

## Input

Any e-commerce/retail orders CSV works. 

Required columns: order ID, order date, customer ID or email, revenue (after discounts, before tax/shipping).
Optional (enables deeper analysis): quantity, SKU or product name, discount amount. In many cases, column names don't need to match exactly.


## How It Works

```
Orders CSV → Python engine → review.json → Claude → REVIEW.md
```

Python computes every KPI and runs health checks. Claude reads the structured output and writes the business narrative. Numbers are precise because Python owns them. Interpretation is sharp because Claude owns that.



## Example

Tested on [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (UCI, CC BY 4.0) — a real UK retailer with ~1M transactions over 2 years.

[See the full report →](REVIEW.md) | [Try it yourself →](examples/online-retail-ii/)

## Roadmap

- [ ] Shopify API integration (skip CSV export)
- [ ] Weekly digest mode
- [ ] Multi-store comparison

## Acknowledgements

Inspired by [claude-ads](https://github.com/AgriciDaniel/claude-ads) by [@AgriciDaniel](https://github.com/AgriciDaniel).

## License

MIT
```

## File: `install.ps1`
```powershell
#Requires -Version 5.1
<#
.SYNOPSIS
    claude-ecom Installer for Windows
.DESCRIPTION
    Installs claude-ecom skill files and Python CLI into ~/.claude/skills/ecom/
    Creates a private venv — no global packages are modified.
.EXAMPLE
    .\install.ps1
#>

$ErrorActionPreference = "Stop"

# ── Configuration ──────────────────────────────────────────────
$SkillDir   = Join-Path $env:USERPROFILE ".claude\skills\ecom"
$VenvDir    = Join-Path $SkillDir ".venv"
$RepoUrl    = "https://github.com/takechanman1228/claude-ecom"

# ── Banner ─────────────────────────────────────────────────────
Write-Host ""
Write-Host ([char]0x2550 * 40)
Write-Host "   claude-ecom - Installer"
Write-Host "   Ecom Data Analytics Skill"
Write-Host ([char]0x2550 * 40)
Write-Host ""

# ── Prerequisites ──────────────────────────────────────────────
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Error: git is required but not installed." -ForegroundColor Red
    exit 1
}
Write-Host "[ok] Git detected"

# Check Python 3
$pythonCmd = $null
foreach ($cmd in @("python3", "python")) {
    if (Get-Command $cmd -ErrorAction SilentlyContinue) {
        $ver = & $cmd -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
        if ($ver -and [version]$ver -ge [version]"3.10") {
            $pythonCmd = $cmd
            break
        }
    }
}
if (-not $pythonCmd) {
    Write-Host "Error: Python 3.10+ is required but not found." -ForegroundColor Red
    Write-Host "  Install from https://python.org" -ForegroundColor Red
    exit 1
}
Write-Host "[ok] Python $ver ($pythonCmd)"

# Check venv module
& $pythonCmd -c "import venv" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Python venv module is required but not available." -ForegroundColor Red
    exit 1
}

# ── Create directories ─────────────────────────────────────────
New-Item -ItemType Directory -Path (Join-Path $SkillDir "references") -Force | Out-Null

# ── Clone to temp dir ──────────────────────────────────────────
$TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("claude-ecom-" + [guid]::NewGuid().ToString("N").Substring(0, 8))

Write-Host "[..] Downloading claude-ecom..."
try {
    git clone --depth 1 $RepoUrl "$TempDir\claude-ecom" 2>$null
    if ($LASTEXITCODE -ne 0) { throw "clone failed" }
} catch {
    Write-Host "Error: Failed to clone from $RepoUrl" -ForegroundColor Red
    Write-Host "  If the repository hasn't been created yet, update REPO_URL in this script." -ForegroundColor Red
    exit 1
} finally {
    $cleanupBlock = {
        if (Test-Path $TempDir) {
            Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
        }
    }
    Register-EngineEvent -SourceIdentifier PowerShell.Exiting -Action $cleanupBlock | Out-Null
}

$CloneRoot = Join-Path $TempDir "claude-ecom"

# ── Copy skill + references ───────────────────────────────────
Write-Host "[..] Installing skill files..."
Copy-Item (Join-Path $CloneRoot "skills\ecom\SKILL.md") -Destination (Join-Path $SkillDir "SKILL.md") -Force
Copy-Item (Join-Path $CloneRoot "skills\ecom\references\*.md") -Destination (Join-Path $SkillDir "references") -Force

# ── Create private venv and install Python CLI ─────────────────
Write-Host "[..] Creating Python environment..."
& $pythonCmd -m venv $VenvDir

$VenvPip = Join-Path $VenvDir "Scripts\pip.exe"

Write-Host "[..] Installing Python CLI (this may take a minute)..."
& $VenvPip install --upgrade pip --quiet 2>$null
& $VenvPip install $CloneRoot --quiet

# ── Create wrapper script ──────────────────────────────────────
$BinDir = Join-Path $SkillDir "bin"
New-Item -ItemType Directory -Path $BinDir -Force | Out-Null

$WrapperPath = Join-Path $BinDir "ecom.cmd"
$VenvPython = Join-Path $VenvDir "Scripts\python.exe"
Set-Content -Path $WrapperPath -Value "@echo off`r`n`"$VenvPython`" -m claude_ecom.cli %*"

# Also create a bash wrapper for Git Bash / WSL
$BashWrapperPath = Join-Path $BinDir "ecom"
Set-Content -Path $BashWrapperPath -Value "#!/usr/bin/env bash`nexec `"`$(dirname `"`$0`")/../.venv/Scripts/python.exe`" -m claude_ecom.cli `"`$@`""

# ── Cleanup temp dir now ───────────────────────────────────────
if (Test-Path $TempDir) {
    Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
}

# ── Summary ────────────────────────────────────────────────────
Write-Host ""
Write-Host "[ok] claude-ecom installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "  Installed:"
Write-Host "    - 1 skill (ecom)"
Write-Host "    - 6 reference files"
Write-Host "    - Python CLI (in private venv)"
Write-Host ""
Write-Host "  Usage:"
Write-Host "    1. Start Claude Code:  claude"
Write-Host "    2. Run command:        /ecom review"
Write-Host ""
Write-Host "  CLI: ~\.claude\skills\ecom\bin\ecom.cmd review orders.csv"
Write-Host ""
Write-Host "  To uninstall: .\uninstall.ps1"
```

## File: `install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# claude-ecom Installer
# Wraps in main() to prevent partial execution on network failure

main() {
    VERSION="0.1.3"
    SKILL_DIR="${HOME}/.claude/skills/ecom"
    VENV_DIR="${SKILL_DIR}/.venv"
    REPO_URL="https://github.com/takechanman1228/claude-ecom"
    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

    echo "════════════════════════════════════════"
    echo "║   claude-ecom - Installer            ║"
    echo "║   Ecom Data Analytics Skill          ║"
    echo "════════════════════════════════════════"
    echo ""

    # Check prerequisites
    command -v git >/dev/null 2>&1 || { echo "Error: git is required but not installed."; exit 1; }
    echo "[ok] Git detected"

    command -v python3 >/dev/null 2>&1 || {
        echo "Error: Python 3 is required but not installed."
        echo "  Install from https://python.org or via your package manager."
        echo "  macOS: brew install python@3.12"
        exit 1
    }
    echo "[ok] Python 3 detected"

    python3 -c "import sys; assert sys.version_info >= (3,10), f'Python 3.10+ required, found {sys.version}'" 2>/dev/null || {
        echo "Error: Python 3.10+ is required. Found: $(python3 --version)"
        echo "  Upgrade from https://python.org or via your package manager."
        echo "  macOS: brew install python@3.12"
        exit 1
    }
    echo "[ok] Python $(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

    python3 -c "import venv" 2>/dev/null || {
        echo "Error: Python venv module is required but not available."
        echo "  Debian/Ubuntu: sudo apt install python3-venv"
        echo "  Fedora: sudo dnf install python3-venv"
        exit 1
    }

    # Create directories
    mkdir -p "${SKILL_DIR}/references"

    # Determine install mode: dev (local source) vs stable (PyPI)
    # When piped via curl|bash, $0 is "bash" — not "install.sh"
    if [ "$(basename "$0")" = "install.sh" ] && [ -f "${SCRIPT_DIR}/pyproject.toml" ]; then
        # Dev mode: running from cloned repo — install from local source
        echo "[..] Installing from local source (dev mode)..."

        # Copy skill + references
        echo "[..] Installing skill files..."
        cp "${SCRIPT_DIR}/skills/ecom/SKILL.md" "${SKILL_DIR}/SKILL.md"
        cp "${SCRIPT_DIR}/skills/ecom/references/"*.md "${SKILL_DIR}/references/"

        # Create private venv and install Python CLI from source
        echo "[..] Creating Python environment..."
        python3 -m venv "${VENV_DIR}"

        echo "[..] Installing Python CLI (this may take a minute)..."
        "${VENV_DIR}/bin/pip" install --upgrade pip --quiet 2>/dev/null
        "${VENV_DIR}/bin/pip" install "${SCRIPT_DIR}" --quiet
    else
        # Stable mode: downloaded via curl — install from tagged release + PyPI
        echo "[..] Installing claude-ecom v${VERSION}..."

        TEMP_DIR=$(mktemp -d)
        trap "rm -rf ${TEMP_DIR}" EXIT

        echo "[..] Downloading tagged release v${VERSION}..."
        if ! git clone --depth 1 --branch "v${VERSION}" "${REPO_URL}" "${TEMP_DIR}/claude-ecom" 2>/dev/null; then
            echo "Error: Failed to download v${VERSION} from ${REPO_URL}"
            exit 1
        fi

        # Copy skill + references from tagged release
        echo "[..] Installing skill files..."
        cp "${TEMP_DIR}/claude-ecom/skills/ecom/SKILL.md" "${SKILL_DIR}/SKILL.md"
        cp "${TEMP_DIR}/claude-ecom/skills/ecom/references/"*.md "${SKILL_DIR}/references/"

        # Create private venv and install Python CLI from PyPI
        echo "[..] Creating Python environment..."
        python3 -m venv "${VENV_DIR}"

        echo "[..] Installing Python CLI (this may take a minute)..."
        "${VENV_DIR}/bin/pip" install --upgrade pip --quiet 2>/dev/null
        "${VENV_DIR}/bin/pip" install "claude-ecom==${VERSION}" --quiet
    fi

    # Create wrapper script
    mkdir -p "${SKILL_DIR}/bin"
    cat > "${SKILL_DIR}/bin/ecom" << 'WRAPPER'
#!/usr/bin/env bash
exec "$(dirname "$0")/../.venv/bin/python" -m claude_ecom.cli "$@"
WRAPPER
    chmod +x "${SKILL_DIR}/bin/ecom"

    echo ""
    echo "[ok] claude-ecom installed successfully!"
    echo ""
    echo "  Installed:"
    echo "    - 1 skill (ecom)"
    echo "    - 6 reference files"
    echo "    - Python CLI (in private venv)"
    echo ""
    echo "  Usage:"
    echo "    1. Start Claude Code:  claude"
    echo "    2. Run command:        /ecom review"
    echo ""
    echo "  CLI: ~/.claude/skills/ecom/bin/ecom review orders.csv"
    echo ""
    echo "  To uninstall: bash uninstall.sh"
}

main "$@"
```

## File: `pyproject.toml`
```
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "claude-ecom"
version = "0.1.3"
description = "Claude-powered ecommerce business review toolkit — run /ecom review to get a full-store business review with prioritized fixes"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
authors = [
    {name = "Hajime Takeda"},
]
keywords = ["ecommerce", "analytics", "shopify", "data-science", "claude"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Office/Business",
]
dependencies = [
    "pandas>=2.0",
    "click>=8.0",
    "numpy>=1.24",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
]
parquet = ["pyarrow>=14.0"]

[project.urls]
Homepage = "https://github.com/takechanman1228/claude-ecom"
Repository = "https://github.com/takechanman1228/claude-ecom"
Issues = "https://github.com/takechanman1228/claude-ecom/issues"

[project.scripts]
ecom = "claude_ecom.cli:cli"

[tool.setuptools.packages.find]
include = ["claude_ecom*"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
target-version = "py310"
line-length = 120

[tool.ruff.lint]
select = ["E", "F", "I", "W"]
```

## File: `uninstall.ps1`
```powershell
#Requires -Version 5.1
<#
.SYNOPSIS
    claude-ecom Uninstaller for Windows
.DESCRIPTION
    Removes claude-ecom skill files from ~/.claude/skills/
.EXAMPLE
    .\uninstall.ps1
#>

$ErrorActionPreference = "Stop"

$SkillDir = Join-Path $env:USERPROFILE ".claude\skills\ecom"

Write-Host "This will remove claude-ecom skill from ~\.claude\skills\"
Write-Host ""
Write-Host "  Directory to remove:"
Write-Host "    - $SkillDir"
Write-Host ""

$confirm = Read-Host "Continue? [y/N]"
if ($confirm -notmatch "^[Yy]$") {
    Write-Host "Cancelled."
    exit 0
}

if (Test-Path $SkillDir) {
    Remove-Item -Recurse -Force $SkillDir
}

Write-Host ""
Write-Host "[ok] claude-ecom uninstalled." -ForegroundColor Green
```

## File: `uninstall.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="${HOME}/.claude/skills/ecom"

echo "This will remove claude-ecom skill from ~/.claude/skills/"
echo ""
echo "  Directory to remove:"
echo "    - ${SKILL_DIR}"
echo ""

read -rp "Continue? [y/N] " confirm
if [[ ! "${confirm}" =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

rm -rf "${SKILL_DIR}"

echo ""
echo "[ok] claude-ecom uninstalled."
```

## File: `validate-skills.sh`
```bash
#!/usr/bin/env bash
# validate-skills.sh — Validate SKILL.md frontmatter for claude-ecom skill

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"
ERRORS=0
CHECKED=0

echo "=== SKILL.md Validation ==="
echo ""

for skill_md in "$SKILLS_DIR"/*/SKILL.md; do
    dir_name="$(basename "$(dirname "$skill_md")")"
    CHECKED=$((CHECKED + 1))

    # Check frontmatter exists
    if ! head -1 "$skill_md" | grep -q '^---$'; then
        echo "FAIL  $dir_name: Missing YAML frontmatter (no opening ---)"
        ERRORS=$((ERRORS + 1))
        continue
    fi

    # Extract frontmatter (between first and second ---)
    frontmatter=$(awk '/^---$/{n++; next} n==1{print} n>=2{exit}' "$skill_md")

    # Check name field
    name=$(echo "$frontmatter" | grep '^name:' | head -1 | sed 's/^name:[[:space:]]*//')
    if [ -z "$name" ]; then
        echo "FAIL  $dir_name: Missing 'name' field"
        ERRORS=$((ERRORS + 1))
    elif [ "$name" != "$dir_name" ]; then
        echo "FAIL  $dir_name: name '$name' does not match directory '$dir_name'"
        ERRORS=$((ERRORS + 1))
    else
        echo "PASS  $dir_name: name='$name'"
    fi

    # Check description field
    if ! echo "$frontmatter" | grep -q '^description:'; then
        echo "FAIL  $dir_name: Missing 'description' field"
        ERRORS=$((ERRORS + 1))
    fi

    # Check argument-hint and allowed-tools
    if ! echo "$frontmatter" | grep -q '^argument-hint:'; then
        echo "FAIL  $dir_name: Missing 'argument-hint'"
        ERRORS=$((ERRORS + 1))
    fi
    if ! echo "$frontmatter" | grep -q '^allowed-tools:'; then
        echo "FAIL  $dir_name: Missing 'allowed-tools'"
        ERRORS=$((ERRORS + 1))
    fi
done

# --- Reference file existence check ---
echo ""
echo "=== Reference File Validation ==="
echo ""
ref_dir="$SKILLS_DIR/ecom/references"

if [ ! -d "$ref_dir" ]; then
    echo "FAIL  Reference directory not found: $ref_dir"
    ERRORS=$((ERRORS + 1))
else
    ref_count=$(ls "$ref_dir"/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo "PASS  Found $ref_count reference files in $ref_dir"
fi

echo ""
echo "=== Results ==="
echo "Checked: $CHECKED SKILL.md files"
echo "Errors:  $ERRORS"

if [ "$ERRORS" -gt 0 ]; then
    echo "FAILED"
    exit 1
else
    echo "ALL PASSED"
    exit 0
fi
```

## File: `claude_ecom/__init__.py`
```python
"""claude-ecom: Ecommerce data analytics toolkit."""

__version__ = "0.1.3"
```

## File: `claude_ecom/checks.py`
```python
"""Check result types, impact estimation, and action builders."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CheckResult:
    """A single check evaluation."""

    check_id: str
    category: str
    severity: str  # critical, high, medium, low
    result: str  # pass, watch, fail, na
    message: str = ""
    current_value: float | str | None = None
    threshold: float | str | None = None
    recommended_action: str = ""


def _check_specific_impact(c: CheckResult, annual_revenue: float) -> float | None:
    """Compute check-specific revenue impact when current_value is available.

    Returns None if no formula exists for this check or data is missing.
    """
    if c.current_value is None:
        return None
    try:
        val = float(c.current_value)
    except (ValueError, TypeError):
        return None

    formulas: dict[str, tuple[float, object]] = {
        # Discount rate: margin recovery from reducing discounts
        "avg_discount_rate_trend": (0.12, lambda v, rev: rev * max(0, v - 0.12) * 0.5),
    }

    entry = formulas.get(c.check_id)
    if entry is None:
        return None
    _, fn = entry
    result = fn(val, annual_revenue)
    if result is None or result < 0:
        return None
    return result


def estimate_revenue_impact(check_results: list[CheckResult], annual_revenue: float) -> dict:
    """Estimate revenue impact of fixing FAIL/WARNING checks.

    Uses check-specific formulas when available, falling back to
    severity-based heuristics.
    """
    if annual_revenue <= 0:
        return {}

    severity_pct = {
        "critical": 0.03,
        "high": 0.015,
        "medium": 0.005,
        "low": 0.001,
    }

    impacts: dict[str, dict] = {}
    for c in check_results:
        if c.result.lower() in ("pass", "na"):
            continue

        # Try check-specific formula first
        specific = _check_specific_impact(c, annual_revenue)
        if specific is not None:
            est = specific
            confidence = "high"
        else:
            # Fallback: severity-based estimate
            pct = severity_pct.get(c.severity.lower(), 0.005)
            if c.result.lower() == "warning":
                pct *= 0.5
            est = annual_revenue * pct
            confidence = (
                "high" if c.severity.lower() == "critical" else ("medium" if c.severity.lower() == "high" else "low")
            )

        impacts[c.check_id] = {
            "annual_revenue_impact": round(est, 0),
            "confidence": confidence,
            "severity": c.severity,
            "result": c.result,
        }

    return impacts


# ---------------------------------------------------------------------------
# Builders for unified review model
# ---------------------------------------------------------------------------

_SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def build_top_issues(checks: list[CheckResult], annual_revenue: float, max_issues: int = 10) -> list[dict]:
    """Build pre-sorted top issues from non-pass checks.

    Sorted by severity * impact. Each entry contains id, category, severity,
    result, message, and estimated_annual_impact.
    """
    impacts = estimate_revenue_impact(checks, annual_revenue)
    issues = []
    for c in checks:
        if c.result.lower() in ("pass", "na"):
            continue
        imp = impacts.get(c.check_id, {})
        issues.append(
            {
                "id": c.check_id,
                "category": c.category,
                "severity": c.severity,
                "result": c.result,
                "message": c.message,
                "estimated_annual_impact": imp.get("annual_revenue_impact", 0),
            }
        )
    issues.sort(
        key=lambda x: (
            _SEVERITY_ORDER.get(x["severity"].lower(), 9),
            x["result"].lower() != "fail",
            -x["estimated_annual_impact"],
        )
    )
    return issues[:max_issues]


_SEVERITY_TIMELINE = {
    "critical": "this_week",
    "high": "this_month",
    "medium": "this_quarter",
    "low": "this_quarter",
}

# Action suggestion templates keyed by check_id
_ACTION_TEMPLATES: dict[str, str] = {
    "monthly_revenue_trend": "Audit acquisition channels for spend or efficiency changes",
    "aov_trend": "Analyze category mix shift and review promotional calendar",
    "order_count_trend": "Review traffic sources and conversion funnel for volume drops",
    "repeat_customer_revenue_share": "Launch tiered loyalty program and post-purchase email automation",
    "revenue_concentration_top10": "Diversify customer acquisition channels to reduce concentration",
    "avg_discount_rate_trend": "Cap discount depth and shift to value-added incentives",
    "daily_revenue_volatility": "Shift promotional budget from flash sales to always-on acquisition",
    "large_order_dependency": "Analyze large-order dependency and diversify revenue sources",
    "discounted_order_ratio": "Restrict promo code distribution to targeted segments",
    "discount_depth_trend": "Freeze discount escalation and introduce non-discount incentives",
    "category_margin_variance": "Review pricing for negative-margin categories",
    "free_shipping_threshold_effectiveness": "Adjust free-shipping threshold to 1.2x median AOV",
    "repeat_purchase_rate": "Deploy post-purchase engagement sequence to improve repeat purchase conversion",
    "champions_loyal_share": "Build VIP program for top customers to grow Champions segment",
    "at_risk_segment_share": "Launch win-back campaigns for At-Risk customer segment",
    "lost_segment_share": "Implement automated reactivation flows for Lost customers",
    "days_to_second_purchase": "Shorten second-purchase window with replenishment reminders",
    "top20_revenue_concentration": "Create discovery merchandising for mid-tier products",
    "converting_sku_rate": "Conduct SKU rationalization for non-converting products",
    "multi_item_order_rate": "Introduce product bundles to increase multi-item orders",
    "cross_sell_pair_lift": "Build cross-sell recommendations from high-lift product pairs",
    "lifecycle_stage_distribution": "Accelerate new product launches to replace declining SKUs",
    "price_tier_distribution": "Expand price tier coverage with entry-level or premium options",
}


def build_action_candidates(top_issues: list[dict], max_actions: int = 10) -> list[dict]:
    """Build action candidates from top issues with severity-based timelines.

    Each entry contains action, source_check, severity, estimated_annual_impact,
    and timeline.
    """
    actions = []
    seen_checks: set[str] = set()
    for issue in top_issues:
        if len(actions) >= max_actions:
            break
        cid = issue["id"]
        if cid in seen_checks:
            continue
        seen_checks.add(cid)
        action_text = _ACTION_TEMPLATES.get(cid, f"Address {issue['message']}")
        actions.append(
            {
                "action": action_text,
                "source_check": cid,
                "severity": issue["severity"],
                "estimated_annual_impact": issue["estimated_annual_impact"],
                "timeline": _SEVERITY_TIMELINE.get(issue["severity"].lower(), "this_quarter"),
            }
        )
    return actions
```

## File: `claude_ecom/cli.py`
```python
"""CLI entry point for claude-ecom."""

from __future__ import annotations

import click
import pandas as pd

from claude_ecom import __version__
from claude_ecom.loader import (
    GENERIC_ORDER_REQUIRED,
    _auto_map_columns,
    _fuzzy_map_columns,
    load_orders,
)
from claude_ecom.report import generate_review_json, review_json_filename


@click.group()
@click.version_option(version=__version__)
def cli():
    """claude-ecom: Ecommerce data analytics toolkit."""
    pass


# ---------------------------------------------------------------------------
# review command (single unified command)
# ---------------------------------------------------------------------------


@cli.command()
@click.argument("orders_path")
@click.option(
    "--period",
    type=click.Choice(["30d", "90d", "365d"]),
    default=None,
    help="Focus on a specific period (default: auto-select all)",
)
@click.option("--output", default="./", help="Output directory for reports")
@click.option("--format", "fmt", default="auto", help="CSV format (shopify|generic|auto)")
@click.option("--nrows", default=None, type=int, help="Limit rows to read (for large files)")
def review(orders_path, period, output, fmt, nrows):
    """Run a business review and generate review.json."""
    from claude_ecom.review_engine import build_review_data

    click.echo("Loading data...")
    orders = load_orders(orders_path, fmt=fmt, nrows=nrows)
    if nrows:
        click.echo(f"  (limited to {nrows:,} rows)")

    click.echo("Building review...")
    review_data = build_review_data(orders, period=period)

    # Display coverage
    cov = review_data["data_coverage"]
    covered = [p for p, v in cov.items() if v]
    click.echo(f"  Data coverage: {', '.join(covered) if covered else 'insufficient data'}")

    click.echo(f"\nGenerating {review_json_filename(period)} to {output} ...")
    path = generate_review_json(review_data, output_dir=output, period=period)
    click.echo(f"Done. Output: {path}")


# ---------------------------------------------------------------------------
# validate command
# ---------------------------------------------------------------------------


@cli.command()
@click.argument("orders_path")
@click.option("--format", "fmt", default="auto", help="CSV format (shopify|generic|auto)")
def validate(orders_path, fmt):
    """Show column mapping diagnostics for order data."""
    df = pd.read_csv(orders_path, nrows=100, low_memory=False)
    click.echo(f"Columns found: {list(df.columns)}\n")

    # Tier 1: exact alias match
    df1, tier1_map = _auto_map_columns(df.copy())
    if tier1_map:
        click.echo("Tier 1 (exact alias match):")
        for orig, canonical in tier1_map.items():
            click.echo(f"  {orig} -> {canonical}")
    else:
        click.echo("Tier 1: no exact alias matches")

    # Tier 2: fuzzy match
    missing_after_t1 = GENERIC_ORDER_REQUIRED - set(df1.columns)
    if missing_after_t1:
        df2, tier2_map = _fuzzy_map_columns(df1.copy())
        if tier2_map:
            click.echo("\nTier 2 (fuzzy token + type inference):")
            for orig, canonical in tier2_map.items():
                click.echo(f"  {orig} -> {canonical}")
        else:
            click.echo("\nTier 2: no fuzzy matches found")
        still_missing = GENERIC_ORDER_REQUIRED - set(df2.columns)
    else:
        still_missing = set()

    click.echo(f"\nRequired columns: {GENERIC_ORDER_REQUIRED}")
    if still_missing:
        click.echo(f"Still missing: {still_missing}")
    else:
        click.echo("All required columns resolved.")


if __name__ == "__main__":
    cli()
```

## File: `claude_ecom/cohort.py`
```python
"""Cohort analysis and RFM segmentation."""

from __future__ import annotations

import pandas as pd


def rfm_segmentation(orders: pd.DataFrame, n_segments: int = 5) -> pd.DataFrame:
    """Compute RFM scores and assign customer segments.

    Returns a DataFrame with columns: customer_id, recency_days,
    frequency, monetary, r_score, f_score, m_score, segment.
    """
    now = orders["order_date"].max()
    rfm = orders.groupby("customer_id").agg(
        recency_days=("order_date", lambda x: (now - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("amount", "sum"),
    )

    # Quintile scoring (1=worst, 5=best for F and M; inverted for R)
    rfm["r_score"] = pd.qcut(rfm["recency_days"], n_segments, labels=False, duplicates="drop")
    rfm["r_score"] = n_segments - rfm["r_score"]  # lower recency = better
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), n_segments, labels=False, duplicates="drop") + 1
    rfm["m_score"] = pd.qcut(rfm["monetary"].rank(method="first"), n_segments, labels=False, duplicates="drop") + 1

    rfm["rfm_sum"] = rfm["r_score"] + rfm["f_score"] + rfm["m_score"]

    def _label(row: pd.Series) -> str:
        r, f = row["r_score"], row["f_score"]
        if r >= 4 and f >= 4:
            return "Champions"
        if r >= 3 and f >= 3:
            return "Loyal"
        if r >= 4 and f <= 2:
            return "New Customers"
        if r <= 2 and f >= 3:
            return "At Risk"
        if r <= 2 and f <= 2:
            return "Lost"
        return "Potential"

    rfm["segment"] = rfm.apply(_label, axis=1)
    return rfm.reset_index()
```

## File: `claude_ecom/loader.py`
```python
"""CSV data loading and validation for ecommerce datasets."""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

# ---------------------------------------------------------------------------
# Column mappings — Shopify export → internal canonical names
# ---------------------------------------------------------------------------

SHOPIFY_ORDER_COLUMNS = {
    "Name": "order_id",
    "Created at": "order_date",
    "Total": "amount",
    "Email": "customer_id",
    "Discount Amount": "discount",
    "Financial Status": "financial_status",
    "Shipping": "shipping",
    "Billing City": "city",
    "Lineitem name": "product_name",
    "Lineitem quantity": "quantity",
    "Lineitem price": "item_price",
    "Lineitem sku": "sku",
}

SHOPIFY_PRODUCT_COLUMNS = {
    "Handle": "product_id",
    "Title": "name",
    "Variant Price": "price",
    "Variant SKU": "sku",
    "Vendor": "vendor",
    "Type": "category",
    "Tags": "tags",
    "Variant Inventory Qty": "stock_quantity",
}

GENERIC_ORDER_REQUIRED = {"order_id", "order_date", "amount", "customer_id"}
GENERIC_PRODUCT_REQUIRED = {"product_id", "name", "price", "category"}
GENERIC_INVENTORY_REQUIRED = {"sku", "quantity_on_hand"}

# ---------------------------------------------------------------------------
# Column alias auto-mapping for arbitrary CSV formats
# ---------------------------------------------------------------------------

_ORDER_COLUMN_ALIASES: dict[str, list[str]] = {
    "order_id": [
        "order_id",
        "order id",
        "order_number",
        "order number",
        "invoice",
        "invoice number",
        "invoice/item number",
        "transaction_id",
        "transaction id",
    ],
    "order_date": [
        "order_date",
        "order date",
        "date",
        "created_at",
        "created at",
        "purchase_date",
        "purchase date",
        "transaction_date",
        "transaction date",
        "day",
        "invoicedate",
        "invoice_date",
        "invoice date",
    ],
    "amount": [
        "amount",
        "total",
        "sale (dollars)",
        "sale_amount",
        "sale amount",
        "total_amount",
        "total amount",
        "revenue",
        "grand_total",
        "grand total",
        "total sales",
        "net sales",
    ],
    "customer_id": [
        "customer_id",
        "customer id",
        "email",
        "customer_email",
        "buyer_id",
        "store number",
        "store_number",
        "store name",
        "user_id",
        "client_id",
    ],
}

_ORDER_COLUMN_OPTIONAL_ALIASES: dict[str, list[str]] = {
    "product_name": [
        "product_name",
        "product name",
        "item description",
        "item_description",
        "product",
        "item",
        "lineitem name",
        "product title",
        "description",
        "item_name",
        "item name",
    ],
    "quantity": [
        "quantity",
        "bottles sold",
        "qty",
        "units",
        "items",
        "lineitem quantity",
    ],
    "sku": [
        "sku",
        "item number",
        "item_number",
        "variant_id",
        "lineitem sku",
        "stockcode",
        "stock_code",
        "stock code",
        "product_code",
        "product code",
    ],
    "discount": [
        "discount",
        "discount_amount",
        "discount amount",
        "discounts",
    ],
    "category": [
        "category",
        "category name",
        "category_name",
        "product_type",
        "product type",
    ],
    "city": [
        "city",
        "billing city",
        "shipping city",
    ],
    "item_price": [
        "item_price",
        "item price",
        "unit_price",
        "unit price",
        "lineitem price",
        "price",
    ],
}


def _auto_map_columns(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, str]]:
    """Try to auto-map columns to canonical names using aliases.

    Returns the renamed DataFrame and a dict of applied mappings.
    """
    col_lower_map = {c.lower().strip(): c for c in df.columns}
    rename_map: dict[str, str] = {}

    for canonical, aliases in {**_ORDER_COLUMN_ALIASES, **_ORDER_COLUMN_OPTIONAL_ALIASES}.items():
        if canonical in df.columns:
            continue  # already present
        for alias in aliases:
            if alias in col_lower_map:
                rename_map[col_lower_map[alias]] = canonical
                break

    if rename_map:
        df = df.rename(columns=rename_map)
    return df, rename_map


def _token_similarity(a: str, b: str) -> float:
    """Jaccard similarity on word tokens of two strings."""
    tokens_a = set(a.lower().replace("_", " ").split())
    tokens_b = set(b.lower().replace("_", " ").split())
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    return len(intersection) / len(union)


def _infer_column_type(series: pd.Series) -> str:
    """Detect column type from sample values: date, currency, id, or unknown."""
    sample = series.dropna().head(20)
    if sample.empty:
        return "unknown"
    # Date-like
    try:
        pd.to_datetime(sample, format="mixed")
        return "date"
    except (ValueError, TypeError):
        pass
    # Currency-like (numeric with possible $ , .)
    str_vals = sample.astype(str)
    numeric_count = (
        str_vals.str.replace(r"[$,\s]", "", regex=True)
        .apply(lambda v: v.replace(".", "", 1).replace("-", "", 1).isdigit())
        .sum()
    )
    if numeric_count / len(sample) > 0.8:
        return "currency"
    # ID-like (mostly unique values)
    if series.nunique() / max(len(series), 1) > 0.8:
        return "id"
    return "unknown"


def _fuzzy_map_columns(
    df: pd.DataFrame, already_mapped: dict[str, str] | None = None
) -> tuple[pd.DataFrame, dict[str, str]]:
    """Tier 2: Token + value-type inference for unmapped required columns.

    Only maps columns that are still missing after exact alias matching.
    """
    all_aliases = {**_ORDER_COLUMN_ALIASES, **_ORDER_COLUMN_OPTIONAL_ALIASES}
    rename_map: dict[str, str] = {}
    used_cols: set[str] = set()
    if already_mapped:
        # already_mapped is {original_col: canonical_name}.
        # After Tier 1 rename, canonical names are now the df column names.
        # Protect them from being re-consumed as fuzzy source columns.
        used_cols.update(already_mapped.values())

    # Type hints for canonical columns
    expected_types = {
        "order_id": "id",
        "order_date": "date",
        "amount": "currency",
        "customer_id": "id",
        "discount": "currency",
        "quantity": "currency",
    }

    for canonical, aliases in all_aliases.items():
        if canonical in df.columns:
            continue
        best_score = 0.0
        best_col = None
        # All alias tokens for similarity
        alias_tokens = " ".join(aliases)
        for col in df.columns:
            if col in used_cols or col in rename_map:
                continue
            sim = max(_token_similarity(col, alias_tokens), _token_similarity(col, canonical))
            # Boost if value type matches
            if canonical in expected_types:
                col_type = _infer_column_type(df[col])
                if col_type == expected_types[canonical]:
                    sim += 0.2
            if sim > best_score:
                best_score = sim
                best_col = col
        if best_col and best_score >= 0.5:
            rename_map[best_col] = canonical
            used_cols.add(best_col)

    if rename_map:
        df = df.rename(columns=rename_map)
    return df, rename_map


@dataclass
class ValidationResult:
    """Result of schema validation."""

    valid: bool
    missing_columns: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Format detection
# ---------------------------------------------------------------------------


def detect_format(path: str) -> str:
    """Detect CSV format by inspecting column names.

    Returns ``"shopify"`` or ``"generic"``.
    """
    df_head = pd.read_csv(path, nrows=5)
    cols = set(df_head.columns)
    shopify_markers = {"Name", "Created at", "Financial Status"}
    if shopify_markers.issubset(cols):
        return "shopify"
    return "generic"


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------


def validate_schema(df: pd.DataFrame, schema: str) -> ValidationResult:
    """Validate that *df* contains the columns required by *schema*.

    Parameters
    ----------
    schema : str
        One of ``"orders"``, ``"products"``, ``"inventory"``.
    """
    required_map = {
        "orders": GENERIC_ORDER_REQUIRED,
        "products": GENERIC_PRODUCT_REQUIRED,
        "inventory": GENERIC_INVENTORY_REQUIRED,
    }
    required = required_map.get(schema, set())
    present = set(df.columns)
    missing = sorted(required - present)
    warnings: list[str] = []
    if schema == "orders" and "discount" not in present:
        warnings.append("'discount' column missing — discount analysis will be skipped")
    return ValidationResult(valid=len(missing) == 0, missing_columns=missing, warnings=warnings)


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def _normalise_shopify_orders(df: pd.DataFrame) -> pd.DataFrame:
    rename = {k: v for k, v in SHOPIFY_ORDER_COLUMNS.items() if k in df.columns}
    df = df.rename(columns=rename)
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], utc=True)
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    if "discount" in df.columns:
        df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0)
    return df


def _normalise_generic_orders(df: pd.DataFrame) -> pd.DataFrame:
    # Tier 1: Auto-map column names from common aliases
    df, mapped = _auto_map_columns(df)
    if mapped:
        import logging

        logging.getLogger(__name__).info("Auto-mapped columns: %s", mapped)
    # Tier 2: Fuzzy matching for still-missing required columns
    missing = GENERIC_ORDER_REQUIRED - set(df.columns)
    if missing:
        df, fuzzy_mapped = _fuzzy_map_columns(df, already_mapped=mapped)
        if fuzzy_mapped:
            import logging

            logging.getLogger(__name__).info("Fuzzy-mapped columns: %s", fuzzy_mapped)
            mapped.update(fuzzy_mapped)
    # Derive amount from quantity * item_price when amount is missing
    if "amount" not in df.columns and "quantity" in df.columns and "item_price" in df.columns:
        df["item_price"] = pd.to_numeric(df["item_price"], errors="coerce")
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
        df["amount"] = df["quantity"] * df["item_price"]
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    if "discount" in df.columns:
        df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0)
    return df


def load_orders(path: str, fmt: str = "auto", nrows: int | None = None) -> pd.DataFrame:
    """Load and normalise an orders CSV.

    Parameters
    ----------
    fmt : str
        ``"shopify"``, ``"generic"``, or ``"auto"`` (detect automatically).
    nrows : int | None
        If set, only read this many rows (useful for large files).
    """
    if fmt == "auto":
        fmt = detect_format(path)
    df = pd.read_csv(path, nrows=nrows, low_memory=False)
    if fmt == "shopify":
        df = _normalise_shopify_orders(df)
    else:
        df = _normalise_generic_orders(df)
    validation = validate_schema(df, "orders")
    if not validation.valid:
        raise ValueError(f"Orders CSV missing required columns: {validation.missing_columns}")
    return df


def load_products(path: str) -> pd.DataFrame:
    """Load and normalise a products CSV."""
    df = pd.read_csv(path)
    # Try Shopify mapping first
    shopify_markers = {"Handle", "Title", "Variant Price"}
    if shopify_markers.issubset(set(df.columns)):
        rename = {k: v for k, v in SHOPIFY_PRODUCT_COLUMNS.items() if k in df.columns}
        df = df.rename(columns=rename)
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
    validation = validate_schema(df, "products")
    if not validation.valid:
        raise ValueError(f"Products CSV missing required columns: {validation.missing_columns}")
    return df


def load_inventory(path: str) -> pd.DataFrame:
    """Load and normalise an inventory CSV."""
    df = pd.read_csv(path)
    if "quantity_on_hand" in df.columns:
        df["quantity_on_hand"] = pd.to_numeric(df["quantity_on_hand"], errors="coerce")
    validation = validate_schema(df, "inventory")
    if not validation.valid:
        raise ValueError(f"Inventory CSV missing required columns: {validation.missing_columns}")
    return df
```

## File: `claude_ecom/metrics.py`
```python
"""KPI calculation engine for ecommerce datasets."""

from __future__ import annotations

import calendar
import math

import pandas as pd


def _safe_float(val: float) -> float:
    """Return NaN if val is NaN or inf, otherwise float(val)."""
    if math.isnan(val) or math.isinf(val):
        return float("nan")
    return float(val)


def compute_revenue_kpis(orders: pd.DataFrame) -> dict:
    """Compute revenue-related KPIs from an orders DataFrame.

    Expected columns: ``order_date``, ``amount``, ``order_id``, ``customer_id``.
    Optional: ``discount``.
    """
    orders = orders.copy()
    orders["month"] = orders["order_date"].dt.to_period("M")

    monthly = orders.groupby("month").agg(
        revenue=("amount", "sum"),
        order_count=("order_id", "nunique"),
    )
    monthly["aov"] = monthly["revenue"] / monthly["order_count"]
    monthly["mom_growth"] = monthly["revenue"].pct_change()

    total_revenue = orders["amount"].sum()
    total_orders = orders["order_id"].nunique()
    avg_aov = total_revenue / total_orders if total_orders else 0

    # New vs repeat
    first_order = orders.groupby("customer_id")["order_date"].min().rename("first_order")
    orders = orders.merge(first_order, on="customer_id", how="left")
    # Normalize both sides to date-only to avoid tz/time mismatches
    orders["is_new"] = orders["order_date"].dt.normalize() == orders["first_order"].dt.normalize()
    repeat_revenue_share = orders.loc[~orders["is_new"], "amount"].sum() / total_revenue if total_revenue else 0

    # Discount
    avg_discount_rate = 0.0
    if "discount" in orders.columns:
        gross = orders["amount"] + orders["discount"]
        avg_discount_rate = (orders["discount"].sum() / gross.sum()) if gross.sum() else 0

    # Revenue concentration (top 10% customers)
    cust_rev = orders.groupby("customer_id")["amount"].sum().sort_values(ascending=False)
    top10_pct = int(max(1, len(cust_rev) * 0.1))
    top10_share = cust_rev.iloc[:top10_pct].sum() / total_revenue if total_revenue else 0

    # Daily CV
    daily = orders.groupby(orders["order_date"].dt.date)["amount"].sum()
    if len(daily) > 1 and daily.mean():
        daily_cv = daily.std() / daily.mean()
        daily_cv = _safe_float(daily_cv)
    else:
        daily_cv = float("nan")

    # Partial last month detection
    last_period = monthly.index[-1] if len(monthly) else None
    partial_last_month = False
    partial_last_month_days = 0
    partial_last_month_label = ""
    if last_period is not None:
        lp_year = last_period.start_time.year
        lp_month = last_period.start_time.month
        days_in_month = calendar.monthrange(lp_year, lp_month)[1]
        # Count actual days with data in the last month
        last_month_dates = orders.loc[orders["month"] == last_period, "order_date"].dt.date.nunique()
        partial_last_month_days = int(last_month_dates)
        partial_last_month_label = f"{lp_year}-{lp_month:02d}"
        if last_month_dates < days_in_month / 2:
            partial_last_month = True

    # MoM growth — guard NaN/inf; skip partial last month
    if partial_last_month and len(monthly) > 2:
        # Use the two most recent complete months
        raw_mom = monthly["mom_growth"].iloc[-2]
        mom_growth_latest = _safe_float(raw_mom)
    elif not partial_last_month and len(monthly) > 1:
        raw_mom = monthly["mom_growth"].iloc[-1]
        mom_growth_latest = _safe_float(raw_mom)
    else:
        mom_growth_latest = float("nan")

    return {
        "total_revenue": float(total_revenue),
        "total_orders": int(total_orders),
        "aov": float(avg_aov),
        "mom_growth_latest": float(mom_growth_latest),
        "repeat_revenue_share": float(repeat_revenue_share),
        "avg_discount_rate": float(avg_discount_rate),
        "top10_customer_share": float(top10_share),
        "daily_revenue_cv": float(daily_cv),
        "monthly_revenue": monthly["revenue"].to_dict(),
        "monthly_aov": monthly["aov"].to_dict(),
        "monthly_orders": monthly["order_count"].to_dict(),
        "partial_last_month": partial_last_month,
        "partial_last_month_days": partial_last_month_days,
        "partial_last_month_label": partial_last_month_label,
    }


def compute_product_kpis(orders: pd.DataFrame, products: pd.DataFrame) -> dict:
    """Compute product-level KPIs.

    ``orders`` should have per-line-item rows with ``sku`` or ``product_name``.
    """
    total_revenue = orders["amount"].sum()

    # Product revenue ranking
    if "sku" in orders.columns:
        prod_rev = orders.groupby("sku")["amount"].sum().sort_values(ascending=False)
    elif "product_name" in orders.columns:
        prod_rev = orders.groupby("product_name")["amount"].sum().sort_values(ascending=False)
    else:
        prod_rev = pd.Series(dtype=float)

    # Pareto — top 20% share
    top20_n = int(max(1, len(prod_rev) * 0.2))
    top20_share = prod_rev.iloc[:top20_n].sum() / total_revenue if total_revenue else 0

    # Multi-item order rate
    items_per_order = orders.groupby("order_id").size()
    multi_item_rate = (items_per_order > 1).mean() if len(items_per_order) else 0

    total_skus = int(products["product_id"].nunique()) if "product_id" in products.columns else 0

    return {
        "total_skus": total_skus,
        "top20_revenue_share": float(top20_share),
        "multi_item_order_rate": float(multi_item_rate),
    }


def compute_cohort_kpis(orders: pd.DataFrame) -> dict:
    """Compute retention / cohort KPIs from orders."""
    orders = orders.copy()
    orders["order_month"] = orders["order_date"].dt.to_period("M")

    first_month = orders.groupby("customer_id")["order_month"].min().rename("cohort_month")
    orders = orders.merge(first_month, on="customer_id", how="left")

    total_customers = orders["customer_id"].nunique()

    # Repeat purchase rate: customers who ordered at least twice
    order_counts = orders.groupby("customer_id")["order_id"].nunique()
    repeat_purchase_rate = (order_counts >= 2).mean() if len(order_counts) else 0

    # Average purchase interval
    cust_dates = orders.groupby("customer_id")["order_date"].apply(lambda s: s.sort_values().diff().dt.days.mean())
    avg_purchase_interval = float(cust_dates.mean()) if not cust_dates.isna().all() else float("nan")

    return {
        "total_customers": int(total_customers),
        "repeat_purchase_rate": float(repeat_purchase_rate),
        "avg_purchase_interval_days": avg_purchase_interval,
    }


def compute_inventory_kpis(inventory: pd.DataFrame, orders: pd.DataFrame) -> dict:
    """Compute inventory-level KPIs."""
    total_skus = int(inventory["sku"].nunique())

    # Stockout SKUs
    stockout_skus = int((inventory["quantity_on_hand"] <= 0).sum())
    stockout_rate = stockout_skus / total_skus if total_skus else 0

    # Overstock (90+ days)
    if "days_on_hand" in inventory.columns:
        overstock_skus = int((inventory["days_on_hand"] > 90).sum())
    else:
        overstock_skus = 0

    # Inventory value
    if "cost" in inventory.columns:
        total_inventory_value = float((inventory["quantity_on_hand"] * inventory["cost"]).sum())
    else:
        total_inventory_value = float("nan")

    return {
        "total_skus": total_skus,
        "stockout_skus": stockout_skus,
        "stockout_rate": float(stockout_rate),
        "overstock_skus": overstock_skus,
        "total_inventory_value": total_inventory_value,
    }
```

## File: `claude_ecom/periods.py`
```python
"""Calendar period utilities for business reviews."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd


@dataclass
class PeriodRange:
    """A labelled date range representing a business period."""

    label: str  # e.g. "February 2026", "Q1 2026", "2025"
    start: date
    end: date


def trailing_window(ref: date, days: int) -> PeriodRange:
    """Trailing N-day window ending at ref (inclusive)."""
    from datetime import timedelta

    start = ref - timedelta(days=days - 1)
    return PeriodRange(
        label=f"Past {days} Days",
        start=start,
        end=ref,
    )


# ---------------------------------------------------------------------------
# Data coverage & prior trailing window (new for unified review model)
# ---------------------------------------------------------------------------

COVERAGE_THRESHOLDS = {"30d": 45, "90d": 120, "365d": 400}


def compute_data_coverage(orders: pd.DataFrame) -> dict[str, bool]:
    """Check which trailing periods have enough data.

    Returns ``{"30d": bool, "90d": bool, "365d": bool}`` based on
    whether the data span (in days) meets the threshold for each period.
    """
    span_days = (orders["order_date"].max() - orders["order_date"].min()).days
    return {k: span_days >= v for k, v in COVERAGE_THRESHOLDS.items()}


def prior_trailing_window(ref: date, days: int) -> PeriodRange:
    """Prior N-day window ending the day before the current window starts.

    If the current trailing window is ``[ref - days + 1, ref]``, the prior
    window is ``[ref - 2*days + 1, ref - days]``.
    """
    from datetime import timedelta

    current_start = ref - timedelta(days=days - 1)
    prior_end = current_start - timedelta(days=1)
    prior_start = prior_end - timedelta(days=days - 1)
    return PeriodRange(
        label=f"Prior {days} Days",
        start=prior_start,
        end=prior_end,
    )
```

## File: `claude_ecom/pricing.py`
```python
"""Price and discount analysis."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class DiscountResult:
    """Discount dependency analysis output."""

    avg_discount_rate: float
    discounted_order_ratio: float
    discount_rate_trend: str  # "increasing", "stable", "decreasing"
    monthly_discount_rates: dict


@dataclass
class MarginResult:
    """Margin analysis output."""

    overall_margin: float
    margin_by_category: dict
    negative_margin_categories: list[str]


@dataclass
class ThresholdResult:
    """Free-shipping threshold analysis output."""

    current_aov: float
    suggested_threshold: float
    orders_below_threshold_pct: float
    potential_aov_lift: float


def discount_dependency(orders: pd.DataFrame) -> DiscountResult:
    """Analyse discount dependency across orders."""
    if "discount" not in orders.columns:
        return DiscountResult(
            avg_discount_rate=0.0,
            discounted_order_ratio=0.0,
            discount_rate_trend="stable",
            monthly_discount_rates={},
        )

    orders = orders.copy()
    gross = orders["amount"] + orders["discount"]
    overall_rate = orders["discount"].sum() / gross.sum() if gross.sum() else 0

    discounted = orders["discount"] > 0
    ratio = discounted.mean()

    # Monthly trend
    orders["month"] = orders["order_date"].dt.to_period("M")
    monthly = orders.groupby("month").apply(
        lambda g: (
            g["discount"].sum() / (g["amount"] + g["discount"]).sum() if (g["amount"] + g["discount"]).sum() else 0
        )
    )

    if len(monthly) >= 3:
        slope = np.polyfit(range(len(monthly)), monthly.values, 1)[0]
        trend = "increasing" if slope > 0.005 else ("decreasing" if slope < -0.005 else "stable")
    else:
        trend = "stable"

    return DiscountResult(
        avg_discount_rate=float(overall_rate),
        discounted_order_ratio=float(ratio),
        discount_rate_trend=trend,
        monthly_discount_rates={str(k): float(v) for k, v in monthly.items()},
    )


def margin_analysis(orders: pd.DataFrame, cost_col: str = "cost") -> MarginResult:
    """Compute gross margin overall and by category."""
    if cost_col not in orders.columns:
        return MarginResult(overall_margin=float("nan"), margin_by_category={}, negative_margin_categories=[])

    revenue = orders["amount"].sum()
    cost = orders[cost_col].sum()
    overall = (revenue - cost) / revenue if revenue else 0

    margin_by_cat: dict[str, float] = {}
    negative_cats: list[str] = []
    if "category" in orders.columns:
        for cat, grp in orders.groupby("category"):
            r = grp["amount"].sum()
            c = grp[cost_col].sum()
            m = (r - c) / r if r else 0
            margin_by_cat[str(cat)] = float(m)
            if m < 0:
                negative_cats.append(str(cat))

    return MarginResult(
        overall_margin=float(overall),
        margin_by_category=margin_by_cat,
        negative_margin_categories=negative_cats,
    )


def free_shipping_threshold(orders: pd.DataFrame) -> ThresholdResult:
    """Suggest an optimal free-shipping threshold based on AOV distribution."""
    aov_per_order = orders.groupby("order_id")["amount"].sum()
    current_aov = float(aov_per_order.mean())

    # Suggest threshold at ~120% of median to encourage upsell
    median_val = float(aov_per_order.median())
    suggested = round(median_val * 1.2, -2)  # round to nearest 100

    below = (aov_per_order < suggested).mean()

    # Potential AOV lift: orders just below threshold would increase
    near_threshold = aov_per_order[(aov_per_order >= suggested * 0.8) & (aov_per_order < suggested)]
    if len(near_threshold):
        lift = (suggested - near_threshold.mean()) / current_aov
    else:
        lift = 0.0

    return ThresholdResult(
        current_aov=current_aov,
        suggested_threshold=float(suggested),
        orders_below_threshold_pct=float(below),
        potential_aov_lift=float(lift),
    )
```

## File: `claude_ecom/product.py`
```python
"""Product analysis — ABC classification, cross-sell, lifecycle."""

from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd


def abc_analysis(orders: pd.DataFrame, metric: str = "revenue") -> pd.DataFrame:
    """Classify products into A/B/C tiers by cumulative revenue share.

    A = top 80%, B = next 15%, C = remaining 5%.
    """
    key = "sku" if "sku" in orders.columns else "product_name"
    if metric == "revenue":
        prod = orders.groupby(key)["amount"].sum().sort_values(ascending=False)
    else:
        prod = orders.groupby(key).size().sort_values(ascending=False)

    prod = prod.reset_index()
    prod.columns = [key, metric]
    total = prod[metric].sum()
    prod["cumulative_share"] = prod[metric].cumsum() / total

    def _rank(share: float) -> str:
        if share <= 0.80:
            return "A"
        if share <= 0.95:
            return "B"
        return "C"

    prod["abc_rank"] = prod["cumulative_share"].apply(_rank)
    prod["revenue_share"] = prod[metric] / total
    return prod


def cross_sell_matrix(orders: pd.DataFrame, min_support: float = 0.01) -> pd.DataFrame:
    """Find co-purchased product pairs with lift > 1.

    Returns a DataFrame with columns: product_a, product_b, support, lift.
    """
    key = "sku" if "sku" in orders.columns else "product_name"
    basket = orders.groupby("order_id")[key].apply(set)
    n_orders = len(basket)
    min_count = max(2, int(n_orders * min_support))

    # Single item frequencies
    from collections import Counter

    item_counts: Counter[str] = Counter()
    pair_counts: Counter[tuple[str, str]] = Counter()

    for items in basket:
        items = {i for i in items if i is not None and isinstance(i, str)}
        for item in items:
            item_counts[item] += 1
        for pair in combinations(sorted(items), 2):
            pair_counts[pair] += 1

    rows = []
    for (a, b), count in pair_counts.items():
        if count < min_count:
            continue
        support = count / n_orders
        pa = item_counts[a] / n_orders
        pb = item_counts[b] / n_orders
        lift = support / (pa * pb) if (pa * pb) else 0
        rows.append({"product_a": a, "product_b": b, "support": support, "lift": lift, "count": count})

    df = pd.DataFrame(rows)
    if len(df):
        df = df.sort_values("lift", ascending=False).reset_index(drop=True)
    return df


def product_lifecycle(orders: pd.DataFrame, products: pd.DataFrame | None = None) -> pd.DataFrame:
    """Assign lifecycle stage (Launch / Growth / Mature / Decline) per product.

    Uses 3-month trailing revenue trend.
    """
    key = "sku" if "sku" in orders.columns else "product_name"
    orders = orders.copy()
    orders["month"] = orders["order_date"].dt.to_period("M")

    monthly = orders.groupby([key, "month"])["amount"].sum().reset_index()
    monthly = monthly.sort_values(["month"])

    results = []
    for prod_id, grp in monthly.groupby(key):
        if len(grp) < 2:
            stage = "Launch"
        else:
            recent = grp.tail(3)["amount"].values
            if len(recent) < 2:
                stage = "Launch"
            else:
                slope = np.polyfit(range(len(recent)), recent, 1)[0]
                mean_val = recent.mean()
                rel_slope = slope / mean_val if mean_val else 0
                if rel_slope > 0.10:
                    stage = "Growth"
                elif rel_slope < -0.10:
                    stage = "Decline"
                else:
                    stage = "Mature"
        results.append(
            {
                key: prod_id,
                "total_revenue": float(grp["amount"].sum()),
                "months_active": int(grp["month"].nunique()),
                "lifecycle_stage": stage,
            }
        )
    return pd.DataFrame(results)


def category_performance(orders: pd.DataFrame) -> pd.DataFrame:
    """Revenue and order stats by product category."""
    if "category" not in orders.columns:
        return pd.DataFrame()
    agg = orders.groupby("category").agg(
        revenue=("amount", "sum"),
        orders=("order_id", "nunique"),
        avg_price=("amount", "mean"),
    )
    total = agg["revenue"].sum()
    agg["revenue_share"] = agg["revenue"] / total if total else 0
    return agg.sort_values("revenue", ascending=False).reset_index()
```

## File: `claude_ecom/report.py`
```python
"""Report generation (review.json) and finding clusters."""

from __future__ import annotations

import json as json_mod
from pathlib import Path

from .checks import CheckResult

# Severity ordering for cluster sorting
_SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

# Finding cluster definitions: name → (check_ids, hypothesis_template, approach)
# 4 clusters: B (Discount), C (Assortment), F (Customer), G (Concentration)
_FINDING_CLUSTERS = [
    {
        "name": "Discount Dependency",
        "checks": {
            "avg_discount_rate_trend",
            "discounted_order_ratio",
            "discount_depth_trend",
            "free_shipping_threshold_effectiveness",
            "monthly_revenue_trend",
        },
        "hypothesis": (
            "{n} discount/pricing checks flagged, indicating the store "
            "may be conditioning customers to wait for sales. "
            "{worst} is the key concern."
        ),
        "approach": ("Shift from blanket discounts to value-added incentives; cap discount depth and frequency."),
    },
    {
        "name": "Assortment & Merchandising Misfit",
        "checks": {
            "top20_revenue_concentration",
            "converting_sku_rate",
            "multi_item_order_rate",
            "cross_sell_pair_lift",
            "lifecycle_stage_distribution",
            "price_tier_distribution",
            "category_margin_variance",
        },
        "hypothesis": (
            "{n} assortment/merchandising checks flagged, suggesting the catalog "
            "is misaligned to demand and value positioning. "
            "{worst} is most critical."
        ),
        "approach": (
            "Do SKU rationalization with clear roles (hero/core/seasonal); "
            "improve merchandising and align price ladders."
        ),
    },
    {
        "name": "Customer & LTV Engine Weakness",
        "checks": {
            "repeat_purchase_rate",
            "champions_loyal_share",
            "at_risk_segment_share",
            "lost_segment_share",
            "days_to_second_purchase",
            "repeat_customer_revenue_share",
            "large_order_dependency",
        },
        "hypothesis": (
            "{n} customer and value checks flagged — the store is failing to "
            "convert first-time buyers into repeat buyers at profitable frequency. "
            "{worst} is most severe."
        ),
        "approach": (
            "Build a retention engine: post-purchase onboarding, replenishment triggers, "
            "lifecycle marketing, and loyalty economics."
        ),
    },
    {
        "name": "Revenue Concentration Risk",
        "checks": {"order_count_trend", "revenue_concentration_top10", "top20_revenue_concentration"},
        "hypothesis": (
            "{n} concentration-related checks show risk — revenue depends on "
            "a narrow set of customers or SKUs. "
            "{worst} is the primary concern."
        ),
        "approach": ("Diversify customer acquisition channels; expand product assortment into adjacent categories."),
    },
]


def _get_version() -> str:
    """Get package version, with fallback to pyproject.toml."""
    try:
        from importlib.metadata import version

        return version("claude-ecom")
    except Exception:
        try:
            import tomllib
        except ModuleNotFoundError:
            import tomli as tomllib  # type: ignore[no-redef]
        try:
            pyproject = Path(__file__).parent.parent / "pyproject.toml"
            with open(pyproject, "rb") as f:
                data = tomllib.load(f)
            return data["project"]["version"]
        except Exception:
            return "0.1.3"


def _build_clusters(check_results: list[CheckResult]) -> list[dict]:
    """Build activated finding clusters from check results."""
    non_pass = {c.check_id: c for c in check_results if c.result.lower() not in ("pass", "na")}
    clusters = []
    for cluster in _FINDING_CLUSTERS:
        matched = [non_pass[cid] for cid in cluster["checks"] if cid in non_pass]
        if len(matched) < 2:
            continue
        matched.sort(
            key=lambda c: (
                _SEVERITY_ORDER.get(c.severity.lower(), 9),
                c.result.lower() != "fail",
            )
        )
        worst = matched[0]
        clusters.append(
            {
                "name": cluster["name"],
                "count": len(matched),
                "related_issues": ", ".join(c.message for c in matched),
                "hypothesis": cluster["hypothesis"].format(n=len(matched), worst=worst.message),
                "approach": cluster["approach"],
            }
        )
    return clusters


def _sanitize_for_json(obj):
    """Replace NaN/Infinity with None for JSON serialization."""
    import math

    if isinstance(obj, dict):
        return {k: _sanitize_for_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_sanitize_for_json(v) for v in obj]
    elif isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    return obj


def review_json_filename(period: str | None = None) -> str:
    """Return the JSON output filename for a given period."""
    suffix = f"_{period}" if period else ""
    return f"review{suffix}.json"


def review_md_filename(period: str | None = None) -> str:
    """Return the Markdown output filename for a given period."""
    suffix = f"_{period.upper()}" if period else ""
    return f"REVIEW{suffix}.md"


def generate_review_json(
    review_data: dict,
    output_dir: str = ".",
    period: str | None = None,
) -> str:
    """Write review.json (or review_{period}.json) from review engine output.

    Returns the output file path.
    """
    sanitized = _sanitize_for_json(review_data)
    out = Path(output_dir) / review_json_filename(period)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json_mod.dumps(sanitized, indent=2, default=str), encoding="utf-8")
    return str(out)
```

## File: `claude_ecom/review_engine.py`
```python
"""Business review engine — unified period-based model.

Produces review.json with multi-period analysis (30d/90d/365d),
health checks, top issues, and action candidates.
"""

from __future__ import annotations

import math
from datetime import date, datetime

import pandas as pd

from .checks import (
    CheckResult,
    build_action_candidates,
    build_top_issues,
)
from .periods import (
    PeriodRange,
    compute_data_coverage,
    prior_trailing_window,
    trailing_window,
)

# ---------------------------------------------------------------------------
# Period summary (kept from original, extended)
# ---------------------------------------------------------------------------


def compute_period_summary(orders: pd.DataFrame, period: PeriodRange) -> dict:
    """Compute KPIs for a calendar period.

    Filters orders to [period.start, period.end] then computes core metrics.
    """
    mask = (orders["order_date"].dt.date >= period.start) & (orders["order_date"].dt.date <= period.end)
    filtered = orders[mask]

    if filtered.empty:
        return {
            "revenue": 0.0,
            "orders": 0,
            "aov": 0.0,
            "customers": 0,
            "new_customers": 0,
            "returning_customers": 0,
            "new_customer_revenue": 0.0,
            "returning_customer_revenue": 0.0,
            "new_customer_aov": 0.0,
            "returning_customer_aov": 0.0,
            "avg_discount_rate": 0.0,
        }

    revenue = float(filtered["amount"].sum())
    n_orders = int(filtered["order_id"].nunique())
    aov = revenue / n_orders if n_orders else 0.0
    customers = int(filtered["customer_id"].nunique())

    # Determine new vs returning based on full order history
    first_order = orders.groupby("customer_id")["order_date"].min()
    period_customers = filtered["customer_id"].unique()
    new_custs = [
        c
        for c in period_customers
        if c in first_order.index and first_order[c].date() >= period.start and first_order[c].date() <= period.end
    ]
    new_customers = len(new_custs)
    returning_customers = customers - new_customers

    new_mask = filtered["customer_id"].isin(new_custs)
    new_customer_revenue = float(filtered.loc[new_mask, "amount"].sum())
    returning_customer_revenue = float(filtered.loc[~new_mask, "amount"].sum())

    # Per-segment AOV
    new_orders = int(filtered.loc[new_mask, "order_id"].nunique()) if new_mask.any() else 0
    ret_orders = int(filtered.loc[~new_mask, "order_id"].nunique()) if (~new_mask).any() else 0
    new_customer_aov = new_customer_revenue / new_orders if new_orders else 0.0
    returning_customer_aov = returning_customer_revenue / ret_orders if ret_orders else 0.0

    avg_discount_rate = 0.0
    if "discount" in filtered.columns:
        gross = filtered["amount"] + filtered["discount"]
        gross_sum = gross.sum()
        avg_discount_rate = float(filtered["discount"].sum() / gross_sum) if gross_sum else 0.0

    return {
        "revenue": revenue,
        "orders": n_orders,
        "aov": aov,
        "customers": customers,
        "new_customers": new_customers,
        "returning_customers": returning_customers,
        "new_customer_revenue": new_customer_revenue,
        "returning_customer_revenue": returning_customer_revenue,
        "new_customer_aov": new_customer_aov,
        "returning_customer_aov": returning_customer_aov,
        "avg_discount_rate": avg_discount_rate,
    }


def compute_period_comparison(current: dict, previous: dict) -> dict:
    """Compute % change for each KPI between two periods."""
    result = {}
    for key in current:
        cur = current[key]
        prev = previous.get(key, 0)
        if isinstance(cur, (int, float)) and isinstance(prev, (int, float)):
            if prev != 0:
                result[key] = (cur - prev) / abs(prev)
            else:
                result[key] = 0.0 if cur == 0 else float("inf")
        else:
            result[key] = 0.0
    return result


# ---------------------------------------------------------------------------
# Period block computation
# ---------------------------------------------------------------------------


def _compute_period_block(orders: pd.DataFrame, ref_date: date, days: int) -> dict:
    """Compute a single period block: summary + kpi_tree + drivers."""
    current_window = trailing_window(ref_date, days)
    prior_window = prior_trailing_window(ref_date, days)

    current_summary = compute_period_summary(orders, current_window)
    prior_summary = compute_period_summary(orders, prior_window)
    changes = compute_period_comparison(current_summary, prior_summary)

    summary = {
        "revenue": current_summary["revenue"],
        "revenue_change": changes.get("revenue", 0.0),
        "orders": current_summary["orders"],
        "orders_change": changes.get("orders", 0.0),
        "aov": current_summary["aov"],
        "aov_change": changes.get("aov", 0.0),
        "customers": current_summary["customers"],
        "customers_change": changes.get("customers", 0.0),
    }

    rev = current_summary["revenue"]
    kpi_tree = {
        "new_customer_revenue": current_summary["new_customer_revenue"],
        "new_customer_revenue_share": (current_summary["new_customer_revenue"] / rev if rev else 0.0),
        "new_customers": current_summary["new_customers"],
        "new_customers_change": changes.get("new_customers", 0.0),
        "new_customer_aov": current_summary["new_customer_aov"],
        "returning_customer_revenue": current_summary["returning_customer_revenue"],
        "returning_customer_revenue_share": (current_summary["returning_customer_revenue"] / rev if rev else 0.0),
        "returning_customers": current_summary["returning_customers"],
        "returning_customers_change": changes.get("returning_customers", 0.0),
        "returning_customer_aov": current_summary["returning_customer_aov"],
    }

    drivers = _compute_drivers(current_summary, prior_summary)

    return {
        "summary": summary,
        "kpi_tree": kpi_tree,
        "drivers": drivers,
    }


def _compute_drivers(current: dict, prior: dict) -> dict:
    """Decompose revenue change into AOV, volume, and mix effects."""
    cur_rev = current.get("revenue", 0)
    prev_rev = prior.get("revenue", 0)
    if prev_rev == 0:
        return {"aov_effect": 0, "volume_effect": 0, "mix_effect": 0}

    cur_orders = current.get("orders", 0)
    prev_orders = prior.get("orders", 0)
    cur_aov = current.get("aov", 0)
    prev_aov = prior.get("aov", 0)

    # Volume effect: change in orders at prior AOV
    volume_effect = (cur_orders - prev_orders) * prev_aov
    # AOV effect: change in AOV at current orders
    aov_effect = (cur_aov - prev_aov) * cur_orders
    # Mix effect: residual
    total_change = cur_rev - prev_rev
    mix_effect = total_change - volume_effect - aov_effect

    return {
        "aov_effect": round(aov_effect, 2),
        "volume_effect": round(volume_effect, 2),
        "mix_effect": round(mix_effect, 2),
    }


# ---------------------------------------------------------------------------
# Monthly trend (for 365d block)
# ---------------------------------------------------------------------------


def _compute_monthly_trend(orders: pd.DataFrame, ref: date, days: int = 365) -> list[dict]:
    """Compute monthly KPI series for the trailing window.

    Only includes months that actually contain data within
    [ref - days + 1, ref]. Each entry includes ``partial`` and
    ``days_with_data`` when the month has data for less than half its days.

    Returns list of dicts with keys: month, revenue, orders, aov,
    customers, new_customers, returning_customers, partial, days_with_data.
    """
    import calendar
    from datetime import timedelta

    window_start = ref - timedelta(days=days - 1)
    window_end = ref

    # Determine the range of months that overlap with the window
    start_year, start_month = window_start.year, window_start.month
    end_year, end_month = window_end.year, window_end.month

    trend = []
    y, m = start_year, start_month
    while (y, m) <= (end_year, end_month):
        month_first = date(y, m, 1)
        month_last_day = calendar.monthrange(y, m)[1]
        month_last = date(y, m, month_last_day)

        # Clip to window bounds
        period_start = max(month_first, window_start)
        period_end = min(month_last, window_end)

        period = PeriodRange(
            label=f"{y}-{m:02d}",
            start=period_start,
            end=period_end,
        )
        summary = compute_period_summary(orders, period)

        # Skip months with zero data
        if summary["orders"] == 0 and summary["revenue"] == 0.0:
            # Advance month
            m += 1
            if m > 12:
                m = 1
                y += 1
            continue

        # Count actual days with data
        mask = (orders["order_date"].dt.date >= period_start) & (orders["order_date"].dt.date <= period_end)
        days_with_data = int(orders.loc[mask, "order_date"].dt.date.nunique())
        is_partial = days_with_data < month_last_day / 2

        entry = {
            "month": f"{y}-{m:02d}",
            "revenue": summary["revenue"],
            "orders": summary["orders"],
            "aov": summary["aov"],
            "customers": summary["customers"],
            "new_customers": summary["new_customers"],
            "returning_customers": summary["returning_customers"],
            "days_with_data": days_with_data,
        }
        if is_partial:
            entry["partial"] = True
        trend.append(entry)

        # Advance month
        m += 1
        if m > 12:
            m = 1
            y += 1

    return trend


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------


def _build_metadata(orders: pd.DataFrame) -> dict:
    """Build metadata block from orders data."""
    total_revenue = float(orders["amount"].sum())
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "data_start": str(orders["order_date"].min().date()),
        "data_end": str(orders["order_date"].max().date()),
        "total_orders": int(orders["order_id"].nunique()),
        "total_customers": int(orders["customer_id"].nunique()),
        "total_revenue": total_revenue,
        "currency": "USD",
        "revenue_definition": "Net sales after discounts, before tax and shipping",
    }


# ---------------------------------------------------------------------------
# Health checks (moved from cli.py, adapted for 3-category model)
# ---------------------------------------------------------------------------


def _build_checks(
    rev_kpis: dict,
    cohort_kpis: dict,
    orders: pd.DataFrame,
) -> list[CheckResult]:
    """Build check results from computed KPIs.

    3 categories: revenue, customer, product.
    Orders-only input (no products/inventory params).
    """
    checks: list[CheckResult] = []

    # ===== Revenue checks =====
    partial_last = rev_kpis.get("partial_last_month", False)

    mom = rev_kpis.get("mom_growth_latest", float("nan"))
    try:
        mom = float(mom)
    except (ValueError, TypeError):
        mom = float("nan")
    if math.isnan(mom):
        checks.append(
            CheckResult(
                "monthly_revenue_trend",
                "revenue",
                "high",
                "na",
                "Insufficient data for MoM growth (<2 months)",
                None,
                0.0,
            )
        )
    else:
        suffix = " (partial month excluded)" if partial_last else ""
        checks.append(
            CheckResult(
                "monthly_revenue_trend",
                "revenue",
                "high",
                "pass" if mom > 0 else ("watch" if mom > -0.05 else "fail"),
                f"MoM revenue growth: {mom:.1%}{suffix}",
                mom,
                0.0,
            )
        )

    # aov_trend — AOV Trend (skip partial last month)
    monthly_aov = rev_kpis.get("monthly_aov", {})
    aov_vals = list(monthly_aov.values())
    if partial_last and len(aov_vals) >= 3:
        aov_change = (aov_vals[-2] - aov_vals[-3]) / aov_vals[-3] if aov_vals[-3] else 0
        checks.append(
            CheckResult(
                "aov_trend",
                "revenue",
                "high",
                "pass" if aov_change > -0.05 else ("watch" if aov_change > -0.1 else "fail"),
                f"AOV MoM change: {aov_change:.1%} (partial month excluded)",
                aov_change,
                -0.05,
            )
        )
    elif not partial_last and len(aov_vals) >= 2:
        aov_change = (aov_vals[-1] - aov_vals[-2]) / aov_vals[-2] if aov_vals[-2] else 0
        checks.append(
            CheckResult(
                "aov_trend",
                "revenue",
                "high",
                "pass" if aov_change > -0.05 else ("watch" if aov_change > -0.1 else "fail"),
                f"AOV MoM change: {aov_change:.1%}",
                aov_change,
                -0.05,
            )
        )

    # order_count_trend — Order Count Trend (skip partial last month)
    monthly_orders = rev_kpis.get("monthly_orders", {})
    ord_vals = list(monthly_orders.values())
    if partial_last and len(ord_vals) >= 3:
        ord_change = (ord_vals[-2] - ord_vals[-3]) / ord_vals[-3] if ord_vals[-3] else 0
        checks.append(
            CheckResult(
                "order_count_trend",
                "revenue",
                "high",
                "pass" if ord_change > -0.05 else ("watch" if ord_change > -0.1 else "fail"),
                f"MoM order count change: {ord_change:.1%} (partial month excluded)",
                ord_change,
                -0.05,
            )
        )
    elif not partial_last and len(ord_vals) >= 2:
        ord_change = (ord_vals[-1] - ord_vals[-2]) / ord_vals[-2] if ord_vals[-2] else 0
        checks.append(
            CheckResult(
                "order_count_trend",
                "revenue",
                "high",
                "pass" if ord_change > -0.05 else ("watch" if ord_change > -0.1 else "fail"),
                f"MoM order count change: {ord_change:.1%}",
                ord_change,
                -0.05,
            )
        )

    # repeat_customer_revenue_share — Repeat Customer Revenue Share
    repeat_share = rev_kpis.get("repeat_revenue_share", 0)
    rpr_for_cross_check = cohort_kpis.get("repeat_purchase_rate", 0)
    if repeat_share == 0 and rpr_for_cross_check > 0.3:
        checks.append(
            CheckResult(
                "repeat_customer_revenue_share",
                "revenue",
                "critical",
                "watch",
                f"Repeat customer revenue share: {repeat_share:.1%} "
                f"(data quality issue: repeat purchase rate={rpr_for_cross_check:.1%})",
                repeat_share,
                0.3,
            )
        )
    else:
        checks.append(
            CheckResult(
                "repeat_customer_revenue_share",
                "revenue",
                "critical",
                "pass" if repeat_share >= 0.3 else ("watch" if repeat_share >= 0.2 else "fail"),
                f"Repeat customer revenue share: {repeat_share:.1%}",
                repeat_share,
                0.3,
            )
        )

    # revenue_concentration_top10 — Revenue Concentration (Top 10% Customers)
    top10 = rev_kpis.get("top10_customer_share", 0)
    if rev_kpis.get("total_revenue", 0) == 0:
        checks.append(
            CheckResult(
                "revenue_concentration_top10",
                "revenue",
                "medium",
                "na",
                "No revenue data for concentration analysis",
                None,
                0.6,
            )
        )
    else:
        checks.append(
            CheckResult(
                "revenue_concentration_top10",
                "revenue",
                "medium",
                "pass" if top10 < 0.6 else ("watch" if top10 < 0.8 else "fail"),
                f"Top 10% customer revenue share: {top10:.1%}",
                top10,
                0.6,
            )
        )

    # avg_discount_rate_trend — Average Discount Rate (subsumes old PR01)
    discount_rate = rev_kpis.get("avg_discount_rate", 0)
    if "discount" not in orders.columns and discount_rate == 0:
        checks.append(
            CheckResult(
                "avg_discount_rate_trend",
                "revenue",
                "high",
                "na",
                "No discount data available",
                None,
                0.15,
            )
        )
    else:
        checks.append(
            CheckResult(
                "avg_discount_rate_trend",
                "revenue",
                "high",
                "pass" if discount_rate < 0.15 else ("watch" if discount_rate < 0.25 else "fail"),
                f"Average discount rate: {discount_rate:.1%}",
                discount_rate,
                0.15,
            )
        )

    # daily_revenue_volatility — Daily Revenue Volatility (CV)
    daily_cv = rev_kpis.get("daily_revenue_cv", 0)
    if isinstance(daily_cv, float) and math.isnan(daily_cv):
        checks.append(
            CheckResult(
                "daily_revenue_volatility",
                "revenue",
                "medium",
                "na",
                "Insufficient daily data for CV calculation",
                None,
                0.5,
            )
        )
    elif rev_kpis.get("total_revenue", 0) == 0:
        checks.append(
            CheckResult(
                "daily_revenue_volatility",
                "revenue",
                "medium",
                "na",
                "No revenue data for CV calculation",
                None,
                0.5,
            )
        )
    else:
        checks.append(
            CheckResult(
                "daily_revenue_volatility",
                "revenue",
                "medium",
                "pass" if daily_cv < 0.5 else ("watch" if daily_cv < 0.8 else "fail"),
                f"Daily revenue coefficient of variation: {daily_cv:.2f}",
                daily_cv,
                0.5,
            )
        )

    # large_order_dependency — Large Order Dependency
    if rev_kpis.get("total_revenue", 0) > 0:
        order_amounts = orders.groupby("order_id")["amount"].sum()
        largest_share = order_amounts.max() / rev_kpis["total_revenue"]
        checks.append(
            CheckResult(
                "large_order_dependency",
                "revenue",
                "medium",
                "pass" if largest_share < 0.05 else ("watch" if largest_share < 0.1 else "fail"),
                f"Largest order share of revenue: {largest_share:.1%}",
                largest_share,
                0.05,
            )
        )

    # ===== Pricing checks (now under revenue) =====
    if "discount" in orders.columns:
        from .pricing import discount_dependency as dd_fn

        dd = dd_fn(orders)
        checks.append(
            CheckResult(
                "discounted_order_ratio",
                "revenue",
                "high",
                "pass" if dd.discounted_order_ratio < 0.4 else ("watch" if dd.discounted_order_ratio < 0.6 else "fail"),
                f"Discounted order ratio: {dd.discounted_order_ratio:.1%}",
                dd.discounted_order_ratio,
                0.4,
            )
        )
        trend = dd.discount_rate_trend
        checks.append(
            CheckResult(
                "discount_depth_trend",
                "revenue",
                "critical",
                "pass" if trend in ("stable", "decreasing") else "watch",
                f"Discount depth trend: {trend}",
                trend,
                "stable",
            )
        )

    # category_margin_variance — Category Margin Variance (if cost data available)
    if "cost" in orders.columns:
        from .pricing import margin_analysis

        ma = margin_analysis(orders)
        neg_cats = len(ma.negative_margin_categories)
        checks.append(
            CheckResult(
                "category_margin_variance",
                "revenue",
                "medium",
                "pass" if neg_cats == 0 else ("watch" if neg_cats == 1 else "fail"),
                f"Categories with negative margin: {neg_cats}",
                neg_cats,
                0,
            )
        )

    # free_shipping_threshold_effectiveness — Free-Shipping Threshold
    from .pricing import free_shipping_threshold

    fst = free_shipping_threshold(orders)
    if fst.suggested_threshold == 0 or fst.current_aov == 0:
        checks.append(
            CheckResult(
                "free_shipping_threshold_effectiveness",
                "revenue",
                "high",
                "na",
                "Insufficient order data for free-shipping threshold analysis",
                None,
                0.1,
            )
        )
    else:
        checks.append(
            CheckResult(
                "free_shipping_threshold_effectiveness",
                "revenue",
                "high",
                "pass" if fst.potential_aov_lift >= 0.1 else ("watch" if fst.potential_aov_lift >= 0.05 else "fail"),
                f"Free-shipping threshold AOV lift potential: {fst.potential_aov_lift:.1%} "
                f"(suggested: {fst.suggested_threshold:,.0f})",
                fst.potential_aov_lift,
                0.1,
            )
        )

    # ===== Customer checks =====
    rpr = cohort_kpis.get("repeat_purchase_rate", 0)
    checks.append(
        CheckResult(
            "repeat_purchase_rate",
            "customer",
            "critical",
            "pass" if rpr >= 0.25 else ("watch" if rpr >= 0.15 else "fail"),
            f"Repeat purchase rate: {rpr:.1%}",
            rpr,
            0.25,
        )
    )

    avg_interval = cohort_kpis.get("avg_purchase_interval_days", float("nan"))
    if isinstance(avg_interval, float) and math.isnan(avg_interval):
        checks.append(
            CheckResult(
                "days_to_second_purchase",
                "customer",
                "high",
                "na",
                "Insufficient data for purchase interval calculation",
                None,
                60,
            )
        )
    else:
        checks.append(
            CheckResult(
                "days_to_second_purchase",
                "customer",
                "high",
                "pass" if avg_interval < 60 else ("watch" if avg_interval < 90 else "fail"),
                f"Avg days to 2nd purchase: {avg_interval:.0f}",
                avg_interval,
                60,
            )
        )

    # C08/C09/C10 — RFM Segment Distribution
    order_counts = orders.groupby("customer_id")["order_id"].nunique()
    total_cust = len(order_counts)
    if total_cust > 0:
        from .cohort import rfm_segmentation

        try:
            rfm = rfm_segmentation(orders)
            seg_dist = rfm["segment"].value_counts(normalize=True)

            champions_loyal = seg_dist.get("Champions", 0) + seg_dist.get("Loyal", 0)
            checks.append(
                CheckResult(
                    "champions_loyal_share",
                    "customer",
                    "medium",
                    "pass" if champions_loyal >= 0.2 else ("watch" if champions_loyal >= 0.1 else "fail"),
                    f"Champions + Loyal segment share: {champions_loyal:.1%}",
                    champions_loyal,
                    0.2,
                )
            )

            at_risk = seg_dist.get("At Risk", 0)
            checks.append(
                CheckResult(
                    "at_risk_segment_share",
                    "customer",
                    "high",
                    "pass" if at_risk < 0.25 else ("watch" if at_risk < 0.35 else "fail"),
                    f"At-Risk segment share: {at_risk:.1%}",
                    at_risk,
                    0.25,
                )
            )

            lost = seg_dist.get("Lost", 0)
            checks.append(
                CheckResult(
                    "lost_segment_share",
                    "customer",
                    "medium",
                    "pass" if lost < 0.3 else ("watch" if lost < 0.45 else "fail"),
                    f"Lost segment share: {lost:.1%}",
                    lost,
                    0.3,
                )
            )
        except Exception:
            pass

    # ===== Product checks =====
    key = "sku" if "sku" in orders.columns else "product_name" if "product_name" in orders.columns else None

    # top20_revenue_concentration — Top-20% Revenue Concentration (orders-only approximation)
    if key:
        product_rev = orders.groupby(key)["amount"].sum().sort_values(ascending=False)
        total_rev = product_rev.sum()
        if total_rev > 0 and len(product_rev) > 0:
            top20_count = max(1, int(len(product_rev) * 0.2))
            top20_share = product_rev.head(top20_count).sum() / total_rev
            checks.append(
                CheckResult(
                    "top20_revenue_concentration",
                    "product",
                    "medium",
                    "pass" if 0.5 <= top20_share <= 0.8 else ("watch" if top20_share <= 0.9 else "fail"),
                    f"Top 20% SKU revenue concentration: {top20_share:.1%}",
                    top20_share,
                    0.8,
                )
            )

    # converting_sku_rate — Converting SKU Rate
    if key:
        total_active = orders[key].nunique()
        selling = orders.groupby(key)["amount"].sum()
        converting = (selling > 0).sum()
        convert_rate = converting / total_active if total_active else 0
        if total_active == 0:
            checks.append(
                CheckResult(
                    "converting_sku_rate",
                    "product",
                    "high",
                    "na",
                    "No SKU/product data available for conversion analysis",
                    None,
                    0.7,
                )
            )
        else:
            checks.append(
                CheckResult(
                    "converting_sku_rate",
                    "product",
                    "high",
                    "pass" if convert_rate >= 0.7 else ("watch" if convert_rate >= 0.5 else "fail"),
                    f"Converting SKU rate: {convert_rate:.1%} ({converting}/{total_active})",
                    convert_rate,
                    0.7,
                )
            )

    # multi_item_order_rate — Multi-Item Order Rate
    if key:
        items_per_order = orders.groupby("order_id")[key].nunique()
        multi_item = (items_per_order > 1).mean() if len(items_per_order) else 0
        checks.append(
            CheckResult(
                "multi_item_order_rate",
                "product",
                "medium",
                "pass" if multi_item >= 0.25 else ("watch" if multi_item >= 0.15 else "fail"),
                f"Multi-item order rate: {multi_item:.1%}",
                multi_item,
                0.25,
            )
        )

    # cross_sell_pair_lift — Cross-Sell Pair Lift
    if key:
        from .product import cross_sell_matrix

        xs = cross_sell_matrix(orders)
        high_lift = len(xs[xs["lift"] > 2.0]) if len(xs) else 0
        checks.append(
            CheckResult(
                "cross_sell_pair_lift",
                "product",
                "medium",
                "pass" if high_lift >= 3 else ("watch" if high_lift >= 1 else "fail"),
                f"Cross-sell pairs with lift > 2.0: {high_lift}",
                high_lift,
                3,
            )
        )

    # lifecycle_stage_distribution — Lifecycle Stage Distribution
    if key:
        from .product import product_lifecycle

        lifecycle = product_lifecycle(orders)
        if len(lifecycle):
            decline_pct = (lifecycle["lifecycle_stage"] == "Decline").mean()
            checks.append(
                CheckResult(
                    "lifecycle_stage_distribution",
                    "product",
                    "medium",
                    "pass" if decline_pct < 0.3 else ("watch" if decline_pct < 0.5 else "fail"),
                    f"Decline-stage products: {decline_pct:.1%}",
                    decline_pct,
                    0.3,
                )
            )

    # price_tier_distribution — Price Tier Distribution
    if key:
        prices = orders.groupby(key)["amount"].mean()
        if len(prices) == 0:
            checks.append(
                CheckResult(
                    "price_tier_distribution",
                    "product",
                    "medium",
                    "na",
                    "No price data available for tier analysis",
                    None,
                    3,
                )
            )
        else:
            try:
                n_tiers = len(pd.qcut(prices, q=min(4, len(prices)), duplicates="drop").cat.categories)
            except (ValueError, TypeError):
                n_tiers = 1
            checks.append(
                CheckResult(
                    "price_tier_distribution",
                    "product",
                    "medium",
                    "pass" if n_tiers >= 3 else ("watch" if n_tiers >= 2 else "fail"),
                    f"Distinct price tiers: {n_tiers}",
                    n_tiers,
                    3,
                )
            )

    return checks


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def build_review_data(
    orders: pd.DataFrame,
    period: str | None = None,
    ref_date: date | None = None,
) -> dict:
    """Build the full review.json data structure.

    Parameters
    ----------
    orders : DataFrame
        Order transaction data with columns: order_id, order_date, customer_id, amount.
    period : str, optional
        One of ``"30d"``, ``"90d"``, ``"365d"``, or ``None`` (auto-select all covered).
    ref_date : date, optional
        Reference date for trailing windows. Defaults to max order date.
    """
    from .metrics import compute_cohort_kpis, compute_revenue_kpis

    ref = ref_date or orders["order_date"].max().date()

    # 1. Metadata
    metadata = _build_metadata(orders)

    # 2. Data coverage
    data_coverage = compute_data_coverage(orders)

    # 3. Determine which periods to compute
    if period:
        periods_to_compute = [period] if data_coverage.get(period, False) else []
    else:
        periods_to_compute = [p for p in ("30d", "90d", "365d") if data_coverage[p]]

    # 4. Compute period blocks
    period_days = {"30d": 30, "90d": 90, "365d": 365}
    periods_data: dict[str, dict] = {}
    for p in periods_to_compute:
        block = _compute_period_block(orders, ref, period_days[p])
        periods_data[p] = block

    # 5. Monthly trend + repeat purchase rate for 365d
    if "365d" in periods_data:
        periods_data["365d"]["monthly_trend"] = _compute_monthly_trend(orders, ref, days=365)

    # 6. Health checks on longest available period's data
    rev_kpis = compute_revenue_kpis(orders)
    cohort_kpis = compute_cohort_kpis(orders)
    checks = _build_checks(rev_kpis, cohort_kpis, orders)

    # 6a. Add repeat_purchase_rate to 365d block (computed from all data)
    if "365d" in periods_data:
        periods_data["365d"]["repeat_purchase_rate"] = cohort_kpis.get("repeat_purchase_rate", 0.0)

    # 6b. Data quality warnings
    data_quality: list[dict] = []
    data_span_days = (orders["order_date"].max() - orders["order_date"].min()).days

    if rev_kpis.get("partial_last_month"):
        data_quality.append(
            {
                "type": "partial_period",
                "period": rev_kpis["partial_last_month_label"],
                "days_with_data": rev_kpis["partial_last_month_days"],
                "message": (
                    f"Latest month ({rev_kpis['partial_last_month_label']}) has only "
                    f"{rev_kpis['partial_last_month_days']} days of data. "
                    "MoM comparisons use prior complete months."
                ),
            }
        )

    if data_span_days < 90:
        data_quality.append(
            {
                "type": "short_data_span",
                "days": data_span_days,
                "message": (
                    f"Data spans only {data_span_days} days. "
                    "90d and 365d analyses are unavailable; interpret results with caution."
                ),
            }
        )
    elif data_span_days < 365:
        data_quality.append(
            {
                "type": "limited_data_span",
                "days": data_span_days,
                "message": (
                    f"Data spans {data_span_days} days (<1 year). "
                    "365d analysis may be unavailable; year-over-year comparisons are limited."
                ),
            }
        )

    # Annualize revenue
    total_revenue = rev_kpis["total_revenue"]
    if 0 < data_span_days < 365:
        annual_revenue = total_revenue * (365 / data_span_days)
    else:
        annual_revenue = total_revenue
    if annual_revenue <= 0:
        annual_revenue = 0.0

    # 8. Top issues + action candidates
    top_issues = build_top_issues(checks, annual_revenue)
    action_candidates = build_action_candidates(top_issues)

    # 9. Assemble review.json
    from . import __version__

    review_data = {
        "version": __version__,
        "metadata": metadata,
        "data_quality": data_quality,
        "data_coverage": data_coverage,
        "periods": periods_data,
        "health": {
            "checks": [
                {
                    "id": c.check_id,
                    "category": c.category,
                    "severity": c.severity,
                    "result": c.result,
                    "message": c.message,
                    "value": c.current_value,
                    "threshold": c.threshold,
                }
                for c in checks
            ],
            "top_issues": top_issues,
        },
        "action_candidates": action_candidates,
    }

    return review_data
```

## File: `examples/online-retail-ii/README.md`
```markdown
# Example: Online Retail II (UCI)

## Dataset

UK-based online retailer, Dec 2009 - Dec 2011. ~1M transactions, ~5.9K customers.

- **Original source:** [UCI Machine Learning Repository - Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (CC BY 4.0)
- **CSV mirror:** [Kaggle - Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)

## Reproduce

1. Download `online_retail_II.csv` from Kaggle (or convert the UCI xlsx)
2. Run: `/ecom review` with the CSV in your working directory
3. Output: `REVIEW.md` in current directory

## Output

See [REVIEW.md](./REVIEW.md) for the full generated report.
```

## File: `examples/online-retail-ii/REVIEW.md`
```markdown
# Business Review

> Revenue reached $9.37M for the year, essentially flat YoY (-1.7%), despite strong
> short-term momentum — the last 90 days surged 84% and November posted +28.5%,
> both driven by Q4 seasonal demand rather than structural growth. The flat annual
> result masks a composition shift: order volume declined 10.5% while AOV grew 9.9%,
> meaning the business is selling fewer units at higher prices. New customer acquisition
> collapsed 57.8% YoY, leaving 84.5% of revenue dependent on returning buyers.
> Launch a dedicated acquisition campaign this month to reverse the new customer
> decline while the retention engine (75.4% repeat rate) sustains existing revenue.

```
           30d Pulse       90d Momentum     365d Structure
Revenue    $1.47M (+ 28%)  $3.73M (+ 84%)   $9.37M (= -2%)
Orders     3,499 (+ 26%)   8,814 (+ 60%)    24,812 (- 11%)
AOV        $419 (+ 2%)     $424 (+ 15%)     $378 (+ 10%)
Customers  1,676 (+ 11%)   2,918 (+ 51%)    4,296 (= flat)
```

---

## 30d Pulse: Peak season lifts all metrics, but new customer decline persists

**KPI Tree:**

```
Revenue $1.47M (vs prior 30d: +28.5%)
|-- 🔴 New Customer Revenue $80K (5.5% of total)
|   |-- New Customers: 153 (-24.3%)
|   |-- New Customer AOV: $365
|-- 🟢 Existing Customer Revenue $1.39M (94.5% of total)
    |-- Returning Customers: 1,523 (+16.7%)
    |-- Returning AOV: $423
```

A strong November driven entirely by returning customers. Even during peak season, new customer count fell 24.3%, confirming the structural acquisition weakness identified at the annual level.

---

## 90d Momentum: Q4 seasonal surge delivers 84% growth, volume-led

**KPI Tree:**

```
Revenue $3.73M (vs prior 90d: +83.7%)
|-- 🟢 New Customer Revenue $385K (10.3% of total)
|   |-- New Customers: 596 (+96.1%)
|   |-- New Customer AOV: $316
|-- 🟢 Existing Customer Revenue $3.35M (89.7% of total)
    |-- Returning Customers: 2,322 (+42.3%)
    |-- Returning AOV: $441
```

**Growth Drivers:** The 90d surge was 72% volume-driven ($1.22M from order count increase) and 28% price-driven ($478K from AOV lift). This reflects classic Q4 seasonal acceleration — monthly revenue jumped from a $560K–$690K range in Q1–Q2 to $1.02M–$1.46M in Sep–Nov.

### Seasonal Concentration Risk

**What is:** Sep–Nov revenue totaled $3.55M, accounting for 38% of the full year in just 3 months.

**Why it matters:** However, the Q1–Q2 monthly average was $608K — roughly half the Sep–Nov average of $1.18M. Revenue outside the peak season is flat and undifferentiated, meaning any Q4 shortfall (supply chain disruption, competitive pressure) would directly threaten the annual target with no buffer from other quarters.

**What to do:** Build a spring/summer campaign calendar with dedicated product launches to reduce Q4 dependency.

---

## 365d Structure: Flat revenue masks a volume-to-price shift and acquisition collapse

**KPI Tree:**

```
Revenue $9.37M (YoY: -1.7%)
|-- 🔴 New Customer Revenue $1.45M (15.5% of total)
|   |-- New Customers: 1,559 (-57.8%)
|   |-- New Customer AOV: $305
|-- 🟢 Existing Customer Revenue $7.92M (84.5% of total)
    |-- Returning Customers: 2,737 (+345%)
    |-- Returning AOV: $395
    |-- Repeat Purchase Rate: 75.4%
```

**Growth Drivers:** AOV gains contributed $843K to revenue, but order volume decline dragged it down by $1.00M, netting a $160K loss. The business preserved revenue by extracting more per order from a shrinking customer base — not by growing demand.

### New Customer Acquisition Collapse

**What is:** New customer count dropped 57.8% YoY, with new customer revenue share falling to 15.5%.

**Why it matters:** Despite an exceptionally strong retention engine (75.4% repeat rate, 5-day median time to second purchase, 45.9% Champions+Loyal segment share), the business cannot sustain indefinitely on existing customers alone. The +345% returning customer growth reflects the cumulative base of prior acquisitions, not new inflow. Without replenishment, the returning customer pool will plateau and eventually contract.

**What to do:** Diagnose which acquisition channels deteriorated and reallocate budget to rebuild new customer volume toward at least 25% revenue share.

### Product Lifecycle Risk

**What is:** 59% of SKUs are in decline stage.

**Why it matters:** Despite a 92.2% converting SKU rate (most products still sell), the majority are declining in velocity. The top 20% of SKUs drive 83% of revenue — if these hero products shift into decline, the revenue impact would be immediate and concentrated with limited replacement depth.

**What to do:** Audit the top 50 SKUs by revenue, identify which are entering decline, and accelerate the new product pipeline to fill gaps before hero products lose momentum.

### Volume Decline Offset by AOV

**What is:** Annual order count declined 10.5% while AOV grew 9.9%, resulting in flat revenue.

**Why it matters:** AOV increases have a natural ceiling — existing customers can only increase basket size so far. However, the latest 30 days show AOV growth already slowing to +1.9%, while order volume growth (+26%) is entirely seasonal. If AOV gains stall outside Q4, revenue will contract.

**What to do:** Shift focus from AOV optimization to volume recovery through new customer acquisition and lapsed customer reactivation.

---

## Action Plan

**Immediate**

1. **Audit acquisition channels to identify where new customer volume dropped**
   Why: New customers declined 57.8% YoY and 24.3% in the latest 30 days, even during peak season
   When: This week
   Success metric: Root cause identified for top 3 acquisition channels by prior-year contribution

**This Month**

2. **Set free-shipping threshold at $200 to capture AOV lift**
   Why: Health check identified 5.7% AOV lift potential, worth an estimated $289K annually
   When: By end of March
   Success metric: AOV increases 3%+ within 60 days of implementation

3. **Launch a new customer acquisition campaign across 2–3 channels**
   Why: New customer revenue share at 15.5% creates existential dependency on returning buyers
   When: By end of March
   Success metric: New customer count reaches 200+/month within 90 days (vs 153 currently)

**This Quarter**

4. **Conduct SKU rationalization on decline-stage products**
   Why: 59% of SKUs are in decline stage; top 20% account for 83% of revenue with limited replacement depth
   When: By end of Q2
   Success metric: Decline-stage share drops below 40%; new/growth-stage SKUs cover at least 10% of revenue

5. **Build a non-Q4 revenue strategy with spring/summer campaign calendar**
   Why: Sep–Nov accounts for 38% of annual revenue; Q1–Q2 monthly average is half the peak
   When: By end of Q2
   Success metric: Q2 revenue increases 15% vs prior Q2

> **Guardrails:** AOV must stay above $370 (currently $378) | Repeat purchase rate must not drop below 70% (currently 75.4%) | Returning customer AOV must not decline while scaling acquisition spend

---

## Data Notes

Revenue defined as net sales after discounts, before tax and shipping. Data covers Dec 2009 – Dec 2011 (53,628 orders across 5,942 customers). All three periods included (30d, 90d, 365d). December 2011 is partial (8 days of data); MoM comparisons use prior complete months.
```

## File: `hooks/hooks.json`
```json
{
  "description": "Installs the claude-ecom Python backend on session start",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh",
            "timeout": 300
          }
        ]
      }
    ]
  }
}
```

## File: `scripts/setup.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILL_DIR="${HOME}/.claude/skills/ecom"
VENV_DIR="${SKILL_DIR}/.venv"

# Fast path: already installed
if [ -x "${SKILL_DIR}/bin/ecom" ] && "${VENV_DIR}/bin/python" -c "import claude_ecom" 2>/dev/null; then
    exit 0
fi

# Check Python 3.10+
if ! command -v python3 &>/dev/null; then
    echo "claude-ecom: Python 3.10+ required. Install from https://python.org" >&2
    exit 0  # Don't block session
fi

python3 -c "import sys; assert sys.version_info >= (3,10)" 2>/dev/null || {
    echo "claude-ecom: Python 3.10+ required. Found: $(python3 --version)" >&2
    exit 0
}

# Create venv + install
mkdir -p "${SKILL_DIR}/bin"
if [ ! -d "${VENV_DIR}" ]; then
    python3 -m venv "${VENV_DIR}"
fi

"${VENV_DIR}/bin/pip" install --upgrade pip --quiet 2>/dev/null
"${VENV_DIR}/bin/pip" install "${REPO_DIR}" --quiet

# Create wrapper
cat > "${SKILL_DIR}/bin/ecom" << 'WRAPPER'
#!/usr/bin/env bash
exec "$(dirname "$0")/../.venv/bin/python" -m claude_ecom.cli "$@"
WRAPPER
chmod +x "${SKILL_DIR}/bin/ecom"

echo "claude-ecom: installed successfully"
```

## File: `skills/ecom/SKILL.md`
```markdown
---
name: ecom
version: 0.1.0
description: >
  Claude-powered ecommerce business review toolkit for D2C stores.
  Single command: review. Analyzes order transaction data across multiple
  time periods (30d/90d/365d), produces KPI trees with health signals,
  structured findings, and concrete action plans.
  Triggers on: "ecommerce review", "store review", "store health",
  "revenue analysis", "customer analysis", "product analysis",
  "business review".
argument-hint: "review [30d|90d|365d]"
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Write
---

# ecom -- Ecommerce Business Review Toolkit

D2C ecommerce analytics system. The Python backend computes KPIs, runs
health checks, and scores performance from order transaction data;
**you** (Claude) interpret the numbers and write the human-readable report.

**Input:** Order transaction data only (CSV).

## Quick Reference

| Command | What it does | Output |
|---------|-------------|--------|
| /ecom review | Full business review (auto-selects periods from data) | REVIEW.md |
| /ecom review 30d | Focused on the last 30 days | REVIEW_30D.md |
| /ecom review 90d | Focused on the last 90 days | REVIEW_90D.md |
| /ecom review 365d | Focused on the last 365 days | REVIEW_365D.md |
| /ecom review [question] | Answers a specific question from the data | Inline response |

One command. Two modes: full report or focused answer.

---

## Response Modes

### Mode 1: Full Review (default)

Triggered when: no natural-language question in the user's input.
Output: REVIEW.md (or REVIEW_{PERIOD}.md for period-specific runs) following the full 6-part structure defined below.

Examples: `/ecom review`, `/ecom review 30d`, `/ecom review 365d`

### Mode 2: Focused Query

Triggered when: user's input includes a natural-language question or topic.
Output: inline conversational response (no file creation).

Examples:
- "how was last month?" → extract from monthly_trend
- "how was last year?" → 365d data
- "how was Q4 last year?" → extract from monthly_trend
- "how's retention looking?" → customer metrics focus

#### Query-to-Period Mapping

| Query pattern | Data source |
|---|---|
| last 30 days | `--period 30d` |
| last 3 months / last 90 days | `--period 90d` |
| last year / this year | `--period 365d` |
| last month / specific month name | full run, extract from monthly_trend |
| Q1-Q4 / specific quarter | full run, extract from monthly_trend |

Calendar-month questions ("last month", "January") use the 365d monthly_trend, NOT a 30d trailing window. Use `--period 30d` only when the user explicitly asks for "last 30 days".

**Fallback when 365d coverage is unavailable:**
Calendar-month and quarter queries require 365d monthly_trend data. If 365d coverage is missing (data < 400 days):
- Answer from the best available trailing window data
- State that exact calendar-month/quarter breakdown is not available
- Suggest running a full review for deeper analysis

**monthly_trend limitation: no year-over-year comparison by month/quarter**
monthly_trend covers only the most recent 12 months. Comparing "Q4 this year vs Q4 last year" is not possible.
Instead:
- Present absolute values (revenue, orders) for the requested period
- Calculate its share of annual revenue (seasonality concentration)
- Compare against Q1-Q3 average for relative scale
- Add 365d overall YoY growth rate as context
- Do not mention the absence of YoY comparison (follow Handling Incomplete Data rules — omit what you can't measure)

If the query doesn't map to a clear period, run full (no --period flag) and answer from the most relevant data.

#### Focused Query Response Format

1. **Direct answer** (2-3 sentences with key numbers from review.json)
2. **Supporting context** (1-2 observations that add nuance — tensions, comparisons)
3. **One actionable takeaway** (if warranted by the data)

Total: 10-30 lines. Headings, KPI tree, and Finding format are NOT required. Use whatever structure best fits the answer.
For example, "what's the new vs returning split?" is clearest as a partial KPI tree.
Apply the same data rules: all numbers from review.json only, match user's language.
Do NOT create a REVIEW.md file.

---

## Data Input

Order transaction data (CSV). Each row = one order or line item.

Required columns:
- Order ID, Order date, Customer ID (or email)
- Revenue (after discounts, before tax/shipping)
- Quantity, SKU/Product ID
- Discount amount (if available)

```bash
~/.claude/skills/ecom/bin/ecom review orders.csv --output <output-dir>
~/.claude/skills/ecom/bin/ecom review orders.csv --period 90d --output <output-dir>
```

---

## Workflow

### Phase 1: Compute (Python)

```bash
~/.claude/skills/ecom/bin/ecom review orders.csv --output <output-dir>
```

The engine internally:

1. **Period analysis** -- computes KPIs for each time period (30d, 90d, 365d)
   with prior-period comparisons, decompositions, and trend detection.
2. **Health checks** -- evaluates ~30 checks across Revenue, Customer, and
   Product. Each check produces a pass/watch/fail signal with severity
   weighting. These power the 🟢/🟡/🔴 markers in the KPI tree.

Output: `review.json` (or `review_{period}.json` for period-specific runs). See Schema section below.

### Phase 2: Interpret (You -- Claude)

1. **Read `review.json`** (or `review_{period}.json` for period-specific runs)
2. **Load reference files on demand** (see Reference Files below)
3. **Write REVIEW.md** (or `REVIEW_{PERIOD}.md`) following the Output Format below

**Your job is to weave trends and diagnostics into one coherent story.**
Period analysis tells you *where things are heading*. Health checks tell you
*what's broken right now*. The report combines both.

---

## review.json Schema

This is the data contract between Python and Claude. Every field below is
guaranteed to exist in the output. Claude reads this structure; Claude does
NOT invent data that isn't here.

```jsonc
{
  "version": "0.1.0",

  // --- Metadata ---
  "metadata": {
    "generated_at": "2026-03-05T18:00:00Z",
    "data_start": "2025-01-01",
    "data_end": "2025-12-31",
    "total_orders": 5784,
    "total_customers": 2765,
    "total_revenue": 1383651,
    "currency": "USD",
    "revenue_definition": "Net sales after discounts, before tax and shipping"
  },

  // --- Data quality warnings (empty array = no issues) ---
  "data_quality": [
    // Example entries (only present when issues detected):
    // { "type": "partial_period", "period": "2026-02", "days_with_data": 3,
    //   "message": "Latest month (2026-02) has only 3 days of data. MoM comparisons use prior complete months." }
    // { "type": "short_data_span", "days": 45, "message": "Data spans only 45 days..." }
    // { "type": "limited_data_span", "days": 200, "message": "Data spans 200 days (<1 year)..." }
  ],

  // --- Data coverage: which periods are available ---
  "data_coverage": {
    "30d": true,       // true if >=45 days of data exist
    "90d": true,       // true if >=120 days of data exist
    "365d": true       // true if >=400 days of data exist
  },

  // --- Period metrics (one block per available period) ---
  "periods": {
    "30d": {
      "summary": {
        "revenue": 98000,
        "revenue_change": -0.003,       // vs prior 30d
        "orders": 412,
        "orders_change": -0.03,
        "aov": 238,
        "aov_change": -0.001,
        "customers": 287,
        "customers_change": -0.05
      },
      "kpi_tree": {
        "new_customer_revenue": 38000,
        "new_customer_revenue_share": 0.388,
        "new_customers": 95,
        "new_customers_change": -0.08,
        "new_customer_aov": 400,
        "returning_customer_revenue": 60000,
        "returning_customer_revenue_share": 0.612,
        "returning_customers": 192,
        "returning_customers_change": -0.03,
        "returning_customer_aov": 312
      },
      "drivers": {
        "aov_effect": 1200,            // revenue change attributable to AOV
        "volume_effect": -1500,         // revenue change attributable to order count
        "mix_effect": 0                 // revenue change attributable to new/returning mix shift
      }
    },
    "90d": { /* same structure */ },
    "365d": {
      /* same structure as 30d (summary, kpi_tree, drivers) plus: */
      "repeat_purchase_rate": 0.38,   // only in 365d block
      "monthly_trend": [
        { "month": "2025-01", "revenue": 95000, "orders": 420, "aov": 226, "customers": 310, "new_customers": 180, "returning_customers": 130, "days_with_data": 31 },
        // ... only months with actual data (no zero-fill for future months)
        { "month": "2025-12", "revenue": 12000, "orders": 45, "aov": 267, "customers": 38, "new_customers": 10, "returning_customers": 28, "days_with_data": 3, "partial": true }
      ]
    }
  },

  // --- Health checks (powers 🟢/🟡/🔴 markers) ---
  "health": {
    "checks": [
      {
        "id": "monthly_revenue_trend",   // internal only, never expose
        "category": "revenue",
        "severity": "high",
        "result": "watch",              // pass | watch | fail
        "message": "MoM revenue growth: -3.8%",
        "value": -0.038,
        "threshold": 0.0
      }
      // ... more checks
    ],
    "top_issues": [
      // Pre-sorted by severity * impact. Max 10.
      {
        "id": "multi_item_order_rate",
        "category": "product",
        "severity": "high",
        "result": "fail",
        "message": "Multi-item order rate: 0.0%",
        "estimated_annual_impact": 77573
      }
      // ...
    ]
  },

  // --- Pre-computed action candidates ---
  "action_candidates": [
    {
      "action": "Introduce product bundles to increase multi-item orders",
      "source_check": "multi_item_order_rate",  // internal reference
      "severity": "high",
      "estimated_annual_impact": 77573,
      "timeline": "this_month"
    }
    // ... max 10 candidates, sorted by impact
  ]
}
```

### Schema Rules

- `periods` only contains keys for periods where `data_coverage` is `true`
- All `_change` fields are proportional change vs prior period (e.g., 0.08 = +8%)
- `health.checks` contains every check result; `health.top_issues` is a
  filtered/sorted subset (fail and watch only, max 10, sorted by severity × impact)
- `action_candidates` are suggestions from Python; Claude refines, merges, and
  rewrites them in business language for the report
- `monthly_trend` contains only months with actual order data (no zero-fill for future months)
- `monthly_trend` entries with `"partial": true` have less than half the month's days with data
- When `data_quality` is non-empty, mention relevant warnings in Data Notes

---

## Reference Files

Load on-demand -- do NOT load all at startup.

> **Path:** `references/`

- `review-narratives.md` -- Narrative templates by health level and growth trajectory, finding templates, period-specific guidance. **Always load.**
- `finding-clusters.md` -- Cluster model for grouping related issues into themes. **Load to identify themes.**
- `recommended-actions.md` -- Actionable recommendations per check with timeline and impact range. **Load for watch/fail checks.**
- `impact-formulas.md` -- Revenue impact formulas with worked examples. **Load when estimating impact.**
- `health-checks.md` -- Check definitions (R/C/P) with thresholds and interpretation.
- `benchmarks.md` -- D2C ecommerce KPI benchmarks.

---

## Output Format: REVIEW.md / REVIEW_{PERIOD}.md

The following structure applies to Full Review mode only. See Response Modes for Focused Query.

One report. Three parts. **Target: ~150 lines.** Tighter is better.

### Report Construction Checklist (MANDATORY)

Before writing, verify your report contains ALL sections in this exact order.
Missing or reordered sections are a format violation.

1. [ ] Executive Summary -- narrative blockquote (4-6 lines) + Scoreboard table
2. [ ] 30d Pulse section (if data available) -- KPI tree + max 1 finding
3. [ ] 90d Momentum section (if data available) -- KPI tree + drivers + max 2 findings
4. [ ] 365d Structure section (if data available) -- KPI tree + drivers + max 3 findings
5. [ ] Action Plan -- max 5 items grouped by time horizon + Guardrails
6. [ ] Data Notes -- 2-4 lines

Structural rules:
- Sections MUST appear in this order. Do NOT reorganize by theme.
- Period sections MUST use the KPI tree format with emoji markers.
- Do NOT create standalone sections like "What's Working Well" or "Issues to Address".
- Positive signals belong in Executive Summary narrative and KPI tree markers.

---

### Part 1: Executive Summary

#### Narrative (4-6 lines, blockquote)

Synthesize across all available periods. Structure:

```
[North Star result + trend across periods]
[What's working: 1-2 strengths confirmed by data -- 80/20 rule]
[What needs attention: the key tension/risk, with data]
[Most important action, with timeline]
```

**Example:**
> Revenue reached $1.38M for the year (+25.7% YoY), but growth is decelerating --
> the last 90 days grew only 8% vs prior 90 days, and last month was flat (+0.3%).
> Growth depends on existing customer AOV increases (+14.8%), while new customer
> acquisition has stalled (share: 42.3%, unchanged). Reallocate 20% of retention
> budget to acquisition channels by end of this month, targeting CPA below $XX.

#### Scoreboard

```
          30d Pulse     90d Momentum    365d Structure
Revenue   $98K (= flat) $340K (+ 8%)    $1.38M (+ 26%)
Orders    412 (- 3%)    1,280 (+ 5%)    5,784 (+ 10%)
AOV       $238 (= flat) $266 (+ 12%)    $239 (+ 15%)
Customers 287 (- 5%)    812 (+ 3%)      2,765 (+ 10%)
```

`+` improving, `-` deteriorating, `=` stable.
Only show periods that data supports.

---

### Part 2: Period Sections

**CRITICAL: Each period gets its own heading and its own KPI tree. Do NOT merge periods into thematic sections.**

All periods use the same skeleton. **But they are not equal length:**

| Period | Depth | Findings cap | Role |
|--------|-------|-------------|------|
| 30d Pulse | Shallow -- KPI tree + 1-2 sentences + max 1 finding | 1 | Flag fires only |
| 90d Momentum | Medium -- KPI tree + drivers + max 2 findings | 2 | Main analytical body |
| 365d Structure | Deep -- KPI tree + drivers + max 3 findings | 3 | Strategic narrative |

If only one period is available, give it the full depth (3 findings).

**The total across all periods must not exceed 5-7 findings.** If a theme
appears in multiple periods, state it once at the most structural level and
reference supporting signals from shorter periods.

#### Skeleton

##### [Period Name]: [One-line headline -- the "so what"]

**KPI Tree:**

```
Revenue $X (vs prior period: +X%)
|-- 🟢 New Customer Revenue $X (X% of total)
|   |-- New Customers: X (+X%)
|   |-- New Customer AOV: $X (+X%)
|-- 🟡 Existing Customer Revenue $X (X% of total)
    |-- Returning Customers: X (+X%)
    |-- Returning AOV: $X (+X%)
    |-- Repeat Purchase Rate: X% -- first-to-second purchase conversion (365d only)
```

🟢 healthy / 🟡 watch / 🔴 problem (driven by health check results).

**Growth Drivers** (1-2 sentences, 90d and 365d only):

Was the change volume-driven or price-driven? Connect to KPI tree nodes.

**Findings** (within period cap):

Each follows Finding Quality Standards. Findings should weave trend data and
health check diagnostics together, not present them separately. Use this format:

### [Finding title]

**What is:** [1 sentence, quantitative fact]

**Why it matters:** [Data-backed tension with "however"/"despite"/"but"]

**What to do:** [Direction only — 1 sentence. Details go in Action Plan.]

---

### Part 3: Action Plan (unified, max 5 items)

**Hard cap: 5 action items. Exceeding 5 is a format violation.**

Action Plan is the single source of truth for deadlines and success metrics.
Findings point to the problem and direction; Action Plan specifies the execution.

One list synthesizing across all periods. Group by time horizon:

```
Immediate (from 30d signals)
1. ...

This Month (from 90d findings)
2. ...

This Quarter (from 365d insights)
3. ...
```

For each item:
- **What** (one concrete sentence)
- **Why** (reference specific data)
- **When** (specific deadline)
- **Success metric** (measurable)

End with (REQUIRED -- omitting Guardrails is a format violation):
> **Guardrails:** [2-3 metrics that must not deteriorate while executing above actions]
>
> Example: AOV must stay above $X | Repeat purchase rate must not drop below X% | Discount rate must stay under X%

---

### Data Notes (2-4 lines)

Always include:
- Revenue definition (from `metadata.revenue_definition`)
- Data period and order count
- Periods included/omitted

---

## Period Interaction Rules

- **Confirm or contradict across periods.** Don't let periods exist in isolation.
- **Zoom in:** If 90d shows a break, check 30d for continuation.
- **Never repeat a finding across periods.** State once at the structural level.
- **Executive Summary synthesizes**, does not summarize sequentially.

---

## Finding Quality Standards

**Every finding follows: What is → Why it matters → What to do**

- **What is:** 1 sentence. Quantitative fact. No interpretation.
- **Why it matters:** Data-backed tension. Must show contrast ("despite", "however").
  Abstract concerns like "growth must be validated" are PROHIBITED.
- **What to do:** Direction and rationale only — 1 sentence. Deadlines and
  success metrics belong in the Action Plan. "Consider", "improve", "optimize",
  "explore" are PROHIBITED.

**Good:**
```
What is:       Annual revenue grew 25.7% YoY.
Why it matters: However, despite a 25.4% reduction in discount rate, new customer
               revenue share remains at 42.3% -- growth depends entirely on
               existing customer AOV increases (+14.8%).
What to do:    Reallocate retention budget toward acquisition channels to diversify growth sources.
```

**Bad (PROHIBITED):**
```
What is:       Revenue grew 25.7%.
Why it matters: Rapid growth must be validated. <-- no data, no tension
What to do:    Consider improving acquisition. <-- banned verb, no deadline
```

---

## Handling Incomplete Data

- Omit what you can't measure. No N/A, no empty sections.
- Don't apologize. Never say "unfortunately..."
- Shorter data = shorter report.
- All gaps noted in Data Notes only.

---

## Language and Data Scope Rules

### Language
- Write entire report in ONE language (match user's prompt/store language)
- Data Notes follows same language as body

### Data Scope: review.json Only
- All numbers MUST come from review.json or be derived from its values
- Do NOT reference external sources (Shopify Analytics, GA, etc.)
- If additional data would help, note as recommended investigation in "What to do"
- PROHIBITED: "CVR from Shopify shows 2.1%" (CVR not in review.json)
- ALLOWED: "Investigate CVR in Shopify Analytics to determine root cause"

### data_quality Warnings
- When `data_quality` array is non-empty, mention relevant warnings in Data Notes
- Do NOT present partial-month MoM as real performance signals

---

## Quality Gates

- Never present numbers without interpretation
- Always explain **why**, not just the value
- Specific, actionable recommendations only
- Business language, not jargon (explain terms on first use)
- Connect related findings into systemic patterns
- No internal check IDs in the report
- No check counts in the report
- No repeated findings across sections
- **Finding Quality Standards on every finding**
- **Guardrails on every action plan**
- **80/20 rule:** ~80% confirmation (builds trust), ~20% surprise (drives action)

---

## Internal: Health Check Engine

> Each check returns pass / watch / fail. These power the 🟢🟡🔴 KPI tree markers.
> Check definitions in `references/health-checks.md`.
> Do NOT use numeric scores, letter grades, or percentage-based health ratings.

---

## Runtime

The skill uses a local Python runtime installed in `~/.claude/skills/ecom/.venv/`.
Use the wrapper command:

```bash
~/.claude/skills/ecom/bin/ecom review orders.csv --output <output-dir>
~/.claude/skills/ecom/bin/ecom review orders.csv --period 90d --output <output-dir>
```

Modules: `loader`, `metrics`, `decomposition`, `cohort`, `product`,
`checks`, `report`, `review_engine`, `config`, `normalize`, `periods`.
```

## File: `skills/ecom/references/benchmarks.md`
```markdown
# Vertical-Specific Benchmarks

This file contains pass/watch/fail thresholds, benchmark ranges, seasonal calendars, structural challenges, and strategy playbooks for six ecommerce verticals. Use the KPI tables to contextualize review findings by swapping in vertical-appropriate expectations for four high-variance metrics: Repeat Purchase Rate (repeat_purchase_rate), AOV, Discount rate (avg_discount_rate_trend), and Gross margin. Thresholds assume a typical ecommerce operator in a competitive market; apply additional modifiers for subscription, marketplace, dropship, luxury, or B2B business models. Modifier values are not yet codified and should be calibrated per engagement.

**Scope note:** This file covers four high-variance KPIs only. Customer acquisition cost (CAC) and LTV:CAC ratio are intentionally excluded; a store with low Repeat Purchase Rate but high per-order LTV (e.g., high-AOV electronics) may still be healthy when evaluated on a full-funnel basis. Do not use these thresholds as the sole basis for a pass/fail judgment without considering acquisition economics.

**Margin assumption:** Gross margin ranges for Fashion & Apparel and Beauty & Cosmetics assume brand-owned DTC operations, where the brand captures manufacturing-to-consumer margin. Multi-brand retailers, resellers, and marketplace sellers typically operate 10--20 pp lower; adjust thresholds accordingly.

**Discount rate methodology:** The discount rate KPI (avg_discount_rate_trend) measures the store's average realized discount rate across all orders in the review period -- not peak promotional markdown depth during events. Rationale sections reference peak event depths (e.g., holiday, BFCM) for context on consumer expectations, but these peaks are distinct from the year-round average that triggers pass/watch/fail.

---

## Fashion & Apparel

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 25% | 15%--24.9% | < 15% |
| AOV | >= $160 | $120--$159 | < $120 |
| Discount rate (avg_discount_rate_trend) | <= 20% | 20.1%--30% | > 30% |
| Gross margin | >= 50% | 40%--49.9% | < 40% |

### Rationale

Fashion has structurally higher gross margins than electronics or grocery, supporting a higher fail threshold. The discount rate pass threshold (<=20%) targets the year-round average realized discount; peak seasonal markdown depths run higher (mid-20% range for apparel during major deal events, with consumers trained to expect 30%+ during Black Friday), but a store whose annual average exceeds 20% is likely running always-on promotions rather than event-led discounting.

### Seasonal Calendar

- **Peak months:** Aug--Sep (back-to-school), Nov--Dec (holiday), plus smaller spikes around mid-summer mega-sale events.
- **Pre-season prep timeline:** Begin merchandising, inventory positioning, and creative production 8--12 weeks ahead of peak, as consumers start shopping earlier and the peak holiday window is short.
- **Markdown windows:** Late Nov--early Dec (BFCM/Cyber Week), late Dec--Jan (post-holiday clearance), and mid-summer eventing (July) used to reset seasonal inventory and drive cash conversion.

### Top Structural Challenges

- Seasonal inventory risk: wrong depth/size curves show up as stockouts in winners and long-tail overstock in losers, forcing deeper markdowns in clearance windows.
- Discount dependency and "promo-trained" customers: heavy reliance on sitewide promotions compresses gross margin and can still fail to move aged units if merchandising is weak.

### Recommended Strategy Playbook

- Use **assortment discipline + lifecycle merchandising**: plan hero SKUs, chase winners early, and separate "core continuity" from "seasonal risk" so markdowns are targeted rather than blanket.
- Replace always-on discounts with a **promo architecture**: fewer, clearer moments; tiered thresholds; and clearance segmentation, aligned to consumer expectations for deep-event periods without training constant waiting.
- Increase repeat purchase rate by designing a **second-order path**: post-purchase styling flows, "complete the look" bundles, and customer-specific recommendations to pull second purchase inside your attribution window.

### Benchmark Ranges

| Metric | Typical range for Fashion & Apparel |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~15%--30% |
| AOV | ~$150--$220 |
| Discount rate (avg_discount_rate_trend) | ~10%--25% (event peaks higher) |
| Gross margin | ~45%--60% |

---

## Beauty & Cosmetics

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 30% | 20%--29.9% | < 20% |
| AOV | >= $120 | $80--$119 | < $80 |
| Discount rate (avg_discount_rate_trend) | <= 15% | 15.1%--25% | > 25% |
| Gross margin | >= 65% | 55%--64.9% | < 55% |

### Rationale

Beauty converts strongly and product margins are structurally high (often ~55%--80%), supporting an aggressive gross margin floor. Loyalty fragility in a crowded market makes personalization and CRM flows disproportionately important to lift repeat purchase rate.

### Seasonal Calendar

- **Peak months:** Nov--Dec (holiday gifting) and Jul (major marketplace promo events that pull forward demand); replenishment categories remain steadier year-round than fashion.
- **Pre-season prep timeline:** 6--10 weeks before peak, ensure giftability (bundles, sets, minis), sampling strategy, and landing pages are ready because shoppers start earlier and concentrate purchases into a short holiday window.
- **Markdown windows:** BFCM/Cyber Week, then targeted post-holiday offers for self-care/routine resets, plus mid-summer deal events that increasingly resemble "Black Friday in summer."

### Top Structural Challenges

- Loyalty fragility in a crowded market (high switching), making personalization, routine-building, and CRM flows disproportionately important to lift repeat purchase rate.
- Shade/formula mismatch risk: incorrect product selection (especially in color cosmetics and skincare) drives returns and erodes trust, making guided selling and education a conversion prerequisite.

### Recommended Strategy Playbook

- Implement **guided selling** (shade finders, skin-type quizzes, regimen builders) and emphasize education on PDP/PLP to reduce mismatch and increase confidence.
- Drive AOV via **routine bundles** (AM/PM kits), "complete the routine" cross-sells, and free-sample thresholds instead of deeper discounts.
- Build for repeat purchases with **replenishment timing** (reorder reminders calibrated to product lifespan) and subscription/auto-ship options where appropriate.
- Protect margin by using promotions strategically during peak deal windows and shifting value to gifts-with-purchase, exclusives, or bundles when possible.

### Benchmark Ranges

| Metric | Typical range for Beauty & Cosmetics |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~20%--40% |
| AOV | ~$80--$170 |
| Discount rate (avg_discount_rate_trend) | ~10%--20% (event peaks higher) |
| Gross margin | ~55%--75% |

---

## Food & Beverage

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 40% | 25%--39.9% | < 25% |
| AOV | >= $65 | $50--$64 | < $50 |
| Discount rate (avg_discount_rate_trend) | <= 10% | 10.1%--15% | > 15% |
| Gross margin | >= 25% | 18%--24.9% | < 18% |

### Rationale

Grocery/food retail margin is structurally low (mid-20s gross margin, large grocers often in the low-20s), which means discounting and shipping subsidies quickly become existential. Basket sizes are generally lower than categories like home goods, with industry snapshots showing ~$69 AOV in Q1. The AOV pass threshold is set at $65 to avoid penalizing typical operators in a structurally low-basket category.

### Seasonal Calendar

- **Peak months:** Nov (holiday food events), Dec (gifting/entertaining), and early Feb (Super Bowl snacks/party food).
- **Pre-season prep timeline:** 4--8 weeks before each peak, lock supply, packaging materials, and fulfillment capacity; short peak windows plus higher shipping sensitivity makes operational readiness a conversion lever.
- **Markdown windows:** Concentrate promo depth around BFCM/Cyber Week and major event weeks; otherwise bias toward bundles/thresholds rather than deep percent-off, because margins are thin.

### Top Structural Challenges

- Shipping economics vs. low AOV: free shipping thresholds that are too low (or hidden fees) produce margin leakage.
- Underutilized retention mechanics (reorder/subscription): many stores perform fine on acquisition but fail to capture the natural repeat cycle inherent to consumables.

### Recommended Strategy Playbook

- Make **subscription-first** where appropriate (staples, coffee/tea, supplements-adjacent consumables) with low-friction skip/pause; pair with reorder reminders for non-subscription buyers.
- Push AOV through **bundles and thresholds** (variety packs, "build-a-box," subscribe-and-save) to reduce shipping as % of revenue instead of relying on discounts.
- Treat event weeks as mini-seasons (holiday, Super Bowl): pre-build landing pages and email/SMS flows, and coordinate inventory + promo so you don't discount items you can't fulfill.

### Benchmark Ranges

| Metric | Typical range for Food & Beverage |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~25%--45% |
| AOV | ~$55--$90 |
| Discount rate (avg_discount_rate_trend) | ~5%--15% |
| Gross margin | ~18%--35% |

---

## Electronics & Gadgets

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 12% | 8%--11.9% | < 8% |
| AOV | >= $180 | $120--$179 | < $120 |
| Discount rate (avg_discount_rate_trend) | <= 15% | 15.1%--25% | > 25% |
| Gross margin | >= 25% | 15%--24.9% | < 15% |

### Rationale

Electronics is structurally margin-thin compared to beauty and apparel; large electronics retailers commonly operate with gross margins in the low-20% range, so gross margin should not be audited against beauty-like expectations. Repeat purchase rates are structurally low due to long replacement cycles; the pass threshold is set at 12% (rather than the top of the typical range) to avoid flagging healthy stores whose customers simply don't need to buy again soon. The discount rate pass threshold (<=15%) targets the year-round average realized discount; peak event markdown depths for electronics are considerably higher (~30% during holiday deal events), but persistent high average discount depth outside deal windows signals price-matching stress and weak differentiation.

### Seasonal Calendar

- **Peak months:** Jul (major deal events often tied to back-to-school shopping) and Nov--Dec (holiday).
- **Pre-season prep timeline:** 6--10 weeks ahead -- ensure pricing strategy, supplier availability, and fulfillment SLAs are locked because consumers compare prices heavily and the peak window is short.
- **Markdown windows:** Highest discount depths cluster around Prime-like summer events and BFCM/Cyber Week, with category peak discounts reported around ~30% for electronics during holiday.

### Top Structural Challenges

- Low gross margins + price transparency drive a "race to the bottom," so shipping leakage or heavy discounting quickly breaks contribution margin.
- Long replacement cycles and low natural repeat: most electronics purchases are one-off or multi-year, making accessory attach and ecosystem lock-in critical to lifetime value.

### Recommended Strategy Playbook

- Make PDPs "decision-complete": rich specs, compatibility matrices, side-by-side comparisons, and transparent warranty/return terms to reduce uncertainty-driven abandonment.
- Shift value from discounts to **bundles and services** (warranty extensions, setup, accessories kits) to lift AOV while protecting gross margin.
- Treat promo as event-led (summer deal weeks + BFCM) and avoid constant markdowns; persistent deep discounts are often unsustainable in low-margin categories.

### Benchmark Ranges

| Metric | Typical range for Electronics & Gadgets |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~8%--15% |
| AOV | ~$120--$250+ |
| Discount rate (avg_discount_rate_trend) | ~10%--25% (event peaks higher) |
| Gross margin | ~15%--30% |

---

## Home & Living

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 15% | 10%--14.9% | < 10% |
| AOV | >= $250 | $150--$249 | < $150 |
| Discount rate (avg_discount_rate_trend) | <= 15% | 15.1%--25% | > 25% |
| Gross margin | >= 35% | 25%--34.9% | < 25% |

### Rationale

Home & furniture categories have structurally high AOV (~$266 in one benchmark snapshot), making merchandising clarity more valuable than chasing visits. Gross margins for large home-focused ecommerce retailers are commonly around ~30%, supporting a mid-30s pass goal but a lower fail floor than beauty/apparel.

### Seasonal Calendar

- **Peak months:** Jul--Sep (move-in / dorm / home refresh) and Nov--Dec (holiday). Back-to-school shopping starts early for many consumers (early July), which matters for dorm basics and small home goods.
- **Pre-season prep timeline:** 8--12 weeks ahead -- ensure catalog hygiene, delivery promises, and inventory visibility are correct because purchases are high-consideration and shoppers start earlier.
- **Markdown windows:** BFCM/Cyber Week (giftable home goods + decor), plus targeted clearance on seasonal decor and end-of-line SKUs; avoid blanket promos that destroy margin with bulky-ship items.

### Top Structural Challenges

- "Ops is the product": delivery fees, lead times, damage risk, and poor post-purchase comms become conversion drivers.
- Low purchase frequency and long consideration cycles: customers may buy furniture once every few years, making LTV-building through cross-category expansion (decor, textiles, accessories) and post-purchase nurture essential.

### Recommended Strategy Playbook

- Upgrade "confidence merchandising": dimension clarity, material details, room photography, and UGC; treat PDP completeness as a conversion lever.
- Show **transparent delivery economics** early (shipping costs, thresholds, white-glove options) to prevent late-stage abandonment from unexpected fees.
- Lift AOV without margin collapse via **bundled rooms/collections**, accessories attach, and financing where relevant, rather than deeper discounts.
- Segment promos: use event promotions for giftable items but protect bulky/low-margin SKUs with targeted markdowns and controlled clearance.

### Benchmark Ranges

| Metric | Typical range for Home & Living |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~10%--20% |
| AOV | ~$200--$350+ |
| Discount rate (avg_discount_rate_trend) | ~10%--20% (event peaks higher) |
| Gross margin | ~25%--35% |

---

## Health & Wellness

### KPI Pass / Watch / Fail Thresholds

| KPI | Pass | Watch | Fail |
|---|---:|---:|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | >= 30% | 18%--29.9% | < 18% |
| AOV | >= $75 | $55--$74 | < $55 |
| Discount rate (avg_discount_rate_trend) | <= 15% | 15.1%--25% | > 25% |
| Gross margin | >= 50% | 40%--49.9% | < 40% |

### Rationale

Health & wellness is a blended vertical: consumable products (supplements, routine items) behave like high-repeat DTC, while durable goods (equipment) behave more like electronics/home. Regulatory/compliance and trust are unusually material -- misleading health claims can trigger enforcement actions and reputational damage, making claims hygiene a structural concern. Seasonality is pronounced around behavior-change moments, with a meaningful share of annual new gym memberships occurring in January (~12%), correlating with demand spikes for fitness/wellness products.

### Seasonal Calendar

- **Peak months:** Jan (New Year behavior change / resolution spike), Sep (back-to-routine after summer), and Nov--Dec (holiday gifting and deal season).
- **Pre-season prep timeline:** 6--10 weeks before Jan and holiday: validate claims/labeling, refresh educational content, and make subscription/refill mechanics prominent to capture routine-building intent.
- **Markdown windows:** BFCM/Cyber Week plus New Year promotions; keep routine products focused on subscription/refill value rather than deep markdown dependence.

### Top Structural Challenges

- Claims and compliance risk: supplement and health-related stores often overreach on marketing claims, creating failures that matter beyond performance.
- Trust deficit and anxiety purchasing: consumers want proof (testing, certifications, clear ingredients), so weak credibility signals depress purchase rates.
- Retention is available but not captured: routine products can generate strong repeat, yet many stores lack reorder/subscription UX and lifecycle communications to convert first-time buyers into ongoing customers.

### Recommended Strategy Playbook

- Build a **trust stack**: transparent ingredients, third-party testing and disclaimers where appropriate, and rigorous claim language review; treat this as a KPI precondition.
- Prioritize **subscription + adherence UX** (skip/pause, reminders, reorder in 1--2 clicks) for consumables to lift repeat purchase rate without discounting away margin.
- Use education as conversion: condition-specific guides, dosage FAQs, and "what to expect" timelines reduce uncertainty and preventable returns.
- Plan around **January**: preload landing pages and lifecycle flows for the resolution spike, similar to how retailers plan early for compressed peak seasons.

### Benchmark Ranges

| Metric | Typical range for Health & Wellness |
|---|---:|
| Repeat Purchase Rate (repeat_purchase_rate) | ~18%--40% (higher for consumables) |
| AOV | ~$55--$90 (routine products) |
| Discount rate (avg_discount_rate_trend) | ~5%--20% |
| Gross margin | ~40%--60% |
```

## File: `skills/ecom/references/finding-clusters.md`
```markdown
# Finding Clusters for Ecommerce Review


## Purpose and design assumptions

"Finding clusters" are a layer above individual checks: they group multiple related non-pass results (watch/fail) into executive-level themes that are more likely to represent **systemic** problems than isolated metric noise. Many of the biggest ecommerce performance drags show up as *patterns* across merchandising, pricing, and customer behavior rather than as single-metric anomalies.

Retention economics are well-established: improving retention rates can have outsized profit effects, which is why "repeat + churn + LTV" clusters should be treated as board-level issues when multiple sub-signals fire together.

---

## Finding cluster catalog

The check descriptions below use only **implemented checks** (those the Python backend evaluates). The cluster logic is designed so that **multiple** non-pass checks activate a theme, which reduces false alarms and elevates "structural" patterns.

---

### Cluster B -- Promo-Led Growth and Margin Compression

**Member checks (cross-category):**

| Check ID | Brief description (what "non-pass" typically implies) |
|---|---|
| discounted_order_ratio | Promo penetration is high (% of orders with discounts/codes). |
| discount_depth_trend | Discount depth trend is escalating (deeper discounts over time). |
| free_shipping_threshold_effectiveness | Free-shipping threshold is not driving AOV increase effectively. |
| monthly_revenue_trend | Revenue growth appears driven by discounting rather than underlying demand. |
| avg_discount_rate_trend | Average discount rate is rising, eroding margins (subsumes former PR01). |

**Activation rule:** Activate when **>= 2** checks are non-pass, **including at least one** discount intensity check (discounted_order_ratio/discount_depth_trend) **and** at least one revenue or margin signal (monthly_revenue_trend/avg_discount_rate_trend/free_shipping_threshold_effectiveness).

**Root cause hypothesis template:**

> "{n} pricing and margin checks flagged {severity_level}, indicating growth is being purchased through discount depth/frequency and is compressing unit economics. {worst_check} is most critical; validate whether discounting is incremental or cannibalizing full-price demand."

**Recommended approach:** Rebuild pricing/promo governance: segment promos by goal (acquisition vs reactivation vs inventory liquidation), tighten code eligibility, and introduce markdown optimization rather than blanket discounts.

---

### Cluster C -- Assortment and Merchandising Misfit

**Member checks (cross-category):**

| Check ID | Brief description (what "non-pass" typically implies) |
|---|---|
| top20_revenue_concentration | Assortment breadth misfit: too many or too few SKUs for demand (dilution or lack of choice). |
| converting_sku_rate | Converting SKU rate is low: many SKUs are inactive/low-velocity. |
| multi_item_order_rate | Multi-item order rate is low (weak cross-sell / product adjacency). |
| cross_sell_pair_lift | Cross-sell pair lift is weak (no strong product affinities found). |
| lifecycle_stage_distribution | Lifecycle imbalance: too many decline-stage products vs core winners. |
| price_tier_distribution | Price tier distribution is too narrow (limited market reach). |
| category_margin_variance | Category margin variance signals: negative-margin categories drag down profitability. |

**Activation rule:** Activate when **>= 3** checks are non-pass, including at least **two** Product checks and at least **one** of category_margin_variance to ensure this is cross-functional (assortment *and* commercial architecture).

**Root cause hypothesis template:**

> "{n} assortment/merchandising checks flagged {severity_level}, suggesting the catalog is misaligned to demand and value positioning (too much tail, weak launches, or unclear tiers). {worst_check} is most critical; validate whether the issue is breadth (too many SKUs) or depth (missing winners) and whether pricing architecture reinforces or confuses choices."

**Recommended approach:** Do SKU and category rationalization with clear roles (hero/core/seasonal/experimental), improve category-level merchandising (sorting, bundling, cross-sell adjacency), and align internal price ladders to clear "good-better-best" tiers.

---

### Cluster F -- Customer and LTV Engine Weakness

**Member checks (cross-category):**

| Check ID | Brief description (what "non-pass" typically implies) |
|---|---|
| repeat_purchase_rate | Repeat purchase rate is low for the business model/category. |
| champions_loyal_share | Champions + Loyal segment share is low (not enough high-value customers). |
| at_risk_segment_share | At-Risk segment share is high (engaged customers drifting away). |
| lost_segment_share | Lost segment share is high (chronic retention failure). |
| days_to_second_purchase | Days to second purchase is too long (slow second-order conversion). |
| repeat_customer_revenue_share | New vs returning revenue mix is skewed toward new (repeat base not contributing). |
| large_order_dependency | Large order dependency suggests fragile, non-recurring revenue. |

**Activation rule:** Activate when **>= 3** checks are non-pass, including at least one RFM segment check (champions_loyal_share/at_risk_segment_share/lost_segment_share) and at least one value check (repeat_purchase_rate/days_to_second_purchase/repeat_customer_revenue_share).

**Root cause hypothesis template:**

> "{n} customer and value checks flagged {severity_level}, indicating the store is failing to convert first-time buyers into repeat buyers at profitable frequency/velocity. {worst_check} is most critical; diagnose whether the primary break is early repeat (time-to-2nd) or long-run churn, and identify the weakest cohort ({worst_cohort})."

**Recommended approach:** Build a customer "engine" (post-purchase onboarding, replenishment triggers, lifecycle marketing, loyalty economics, and category expansion) and tie it tightly to margin and product strategy.

---

### Cluster G -- Revenue Concentration and Growth Sustainability Risk

**Member checks (cross-category):**

| Check ID | Brief description (what "non-pass" typically implies) |
|---|---|
| order_count_trend | Order count trend declining (demand concentration risk). |
| revenue_concentration_top10 | Revenue concentration: top 10% of customers drive too much revenue. |
| top20_revenue_concentration | Product concentration: top 20% of SKUs overly dominant. |

**Activation rule:** Activate when **>= 2** checks are non-pass, including at least one concentration check (revenue_concentration_top10/top20_revenue_concentration).

**Root cause hypothesis template:**

> "{n} concentration-related checks flagged {severity_level}, suggesting structural fragility: revenue depends on a narrow set of customers/SKUs. {worst_check} is most critical; quantify downside if the top dependency is disrupted and define the diversification path."

**Recommended approach:** Quantify concentration (top-N share) and pursue deliberate diversification (bench products behind hero SKUs, broaden customer base through customer programs).

---

## Standalone checks

These checks are intentionally **not included in cluster activation logic** because they are either single-point-of-failure incidents or highly data-dependent:

| Check ID | Why it is standalone | Brief description |
|---|---|---|
| category_margin_variance | Model-dependent | Category margin variance signal is category-specific; cluster activation would be noise. |
| daily_revenue_volatility | Can be incident-like | Daily revenue volatility may reflect one-off events rather than structural issues. |

---

## Deduplication and overlap rules

1. **Single primary owner.** A check can appear in multiple clusters as **supporting evidence**, but it should have exactly one **Primary Cluster** for activation counting.

2. **Closest actionable root cause.** If two clusters could plausibly own a check, assign ownership based on **closest actionable root cause** (not the symptom). Discount intensity belongs to Cluster B; customer segment drift belongs to Cluster F.

3. **Worst-check selection.** When selecting `{worst_check}` in hypothesis templates, pick the non-pass check with the highest severity (Fail = 2 points, Watch = 1 point; tie-break by estimated $ impact).

---

## Priority ordering when multiple clusters activate simultaneously

1. **B -- Promo-Led Growth and Margin Compression** -- Discount dependency creates a treadmill where revenue requires margin sacrifice.
2. **C -- Assortment and Merchandising Misfit** -- Catalog structure influences both conversion and margin.
3. **F -- Customer and LTV Engine Weakness** -- Customer programs are a compounding engine; failure means growth only through acquisition spend.
4. **G -- Revenue Concentration and Growth Sustainability Risk** -- Concentration is the "second-order" strategic risk.

---

## Practical implementation notes

Implement clusters as deterministic rules over your existing check statuses: each check emits `{pass, watch, fail, n/a}`. Activate a cluster when its rule is met, then generate the executive narrative using the template placeholders (`{n}`, `{worst_check}`, etc.).

To keep clusters robust across seasonality and promo calendars, consider evaluating checks on two windows:

- **Short window** (e.g., trailing 28 days) for incident detection.
- **Long window** (e.g., trailing 90 days) for structural confirmation.

Treat a finding as "structural" only when the cluster activates in both windows or repeatedly across weeks.
```

## File: `skills/ecom/references/health-checks.md`
```markdown
# Health Checks Reference

Only checks that the Python backend actively evaluates are listed here.
Three categories: Revenue, Customer, Product.

---

## Revenue Checks (12 implemented)

### monthly_revenue_trend -- Monthly Revenue Trend
- **Severity:** High (3.0x)
- **Thresholds:** PASS: 3 consecutive months MoM growth > 0% | WATCH: latest MoM between -5% and 0% | FAIL: MoM decline > 5% or 3+ consecutive decline months
- **Interpretation:** Measures revenue momentum. Declining MoM signals weakening demand, loss of market share, or seasonal patterns not being leveraged.

### aov_trend -- AOV Trend
- **Severity:** High (3.0x)
- **Thresholds:** PASS: AOV decline < 5%/month | WATCH: 5-10% | FAIL: > 10%
- **Interpretation:** Falling AOV may indicate product mix shifts toward lower-priced items, deeper discounting, or loss of premium customers.

### order_count_trend -- Order Count Trend
- **Severity:** High (3.0x)
- **Thresholds:** PASS: MoM order count > -5% | WATCH: -10% to -5% | FAIL: < -10%
- **Interpretation:** Directly measures demand volume. Combine with AOV trend to determine whether revenue changes are volume-driven or value-driven.

### repeat_customer_revenue_share -- Repeat Customer Revenue Share
- **Severity:** Critical (5.0x)
- **Thresholds:** PASS: repeat revenue > 30% | WATCH: 20-30% | FAIL: < 20%
- **Interpretation:** Low repeat share signals unsustainable acquisition dependency. Healthy ecommerce stores derive 30-45% of revenue from returning customers; top consumable brands reach 60%+.

### revenue_concentration_top10 -- Revenue Concentration (Top 10% Customers)
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: top 10% customers < 60% of revenue | WATCH: 60-80% | FAIL: > 80%
- **Interpretation:** Extreme customer concentration creates fragility -- losing a few key accounts would materially impact revenue.

### avg_discount_rate_trend -- Average Discount Rate Trend
- **Severity:** High (3.0x)
- **Thresholds:** PASS: avg rate < 15% and no upward trend > 2pt/month | WATCH: 15-25% or 1-2pt/month trend | FAIL: > 25% or > 2pt/month trend
- **Interpretation:** Rising discount rates erode margins and train customers to wait for sales, creating a dangerous dependency cycle. This check subsumes the former PR01 (average discount rate) -- both the level and trend are evaluated here.

### daily_revenue_volatility -- Daily Revenue Volatility (CV)
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: coefficient of variation < 0.5 | WATCH: 0.5-0.8 | FAIL: > 0.8
- **Interpretation:** High daily volatility makes forecasting unreliable and often indicates over-reliance on promotional spikes rather than steady organic demand.

### large_order_dependency -- Large Order Dependency
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: largest single order < 5% of period revenue | WATCH: 5-10% | FAIL: > 10%
- **Interpretation:** Large individual orders distort trend metrics and create revenue fragility if those customers don't repeat.

### discounted_order_ratio -- Discounted Order Ratio
- **Severity:** High (3.0x)
- **Thresholds:** PASS: < 40% of orders discounted | WATCH: 40-60% | FAIL: > 60%
- **Interpretation:** High ratios condition customers to expect discounts and undermine full-price conversion. Indicates structural over-reliance on promotions.

### discount_depth_trend -- Discount Depth Trend
- **Severity:** Critical (5.0x)
- **Thresholds:** PASS: monthly avg increase < 1pt | WATCH: 1-2pt/month | FAIL: > 2pt/month
- **Interpretation:** Escalating discount depth signals a dangerous cycle where each promotion must go deeper to maintain conversion, steadily eroding margins and brand value.

### category_margin_variance -- Category Margin Variance
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: no category with negative gross margin | WATCH: 1 category at break-even | FAIL: any category with negative margin
- **Interpretation:** Negative-margin categories drag down blended profitability. May indicate mispricing, excessive COGS, or promotional over-investment in specific categories.

### free_shipping_threshold_effectiveness -- Free-Shipping Threshold Effectiveness
- **Severity:** High (3.0x)
- **Thresholds:** PASS: > 10% AOV bump for orders near threshold | WATCH: 5-10% | FAIL: < 5%
- **Interpretation:** An effective threshold drives meaningful AOV increases. Weak signal suggests the threshold is set too high (unreachable) or poorly communicated. Optimal threshold is typically 1.2x median AOV.

---

## Customer Checks (5 implemented)

### repeat_purchase_rate -- Repeat Purchase Rate
- **Severity:** Critical (5.0x)
- **Thresholds:** PASS: > 25% of first-time buyers make a second purchase | WATCH: 15-25% | FAIL: < 15%
- **Interpretation:** The single most important retention metric. Repeat purchase conversion is the foundation of all customer lifetime value -- customers who buy a second time have a 45% chance of buying a third.

### champions_loyal_share -- Champions + Loyal Segment Share
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: > 20% of customers in Champions or Loyal RFM segments | WATCH: 10-20% | FAIL: < 10%
- **Interpretation:** Measures the proportion of high-value engaged customers. Low share indicates retention programs are not cultivating loyalty effectively.

### at_risk_segment_share -- At-Risk Segment Share
- **Severity:** High (3.0x)
- **Thresholds:** PASS: < 25% of customers in At-Risk segment | WATCH: 25-35% | FAIL: > 35%
- **Interpretation:** A large at-risk segment means previously engaged customers are drifting away. Reactivation campaigns are urgent before they become lost.

### lost_segment_share -- Lost Segment Share
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: < 30% of customers in Lost segment | WATCH: 30-45% | FAIL: > 45%
- **Interpretation:** High lost-customer share is a lagging indicator of chronic retention failure. These customers are unlikely to return without significant win-back investment.

### days_to_second_purchase -- Days to Second Purchase
- **Severity:** High (3.0x)
- **Thresholds:** PASS: median < 60 days | WATCH: 60-90 days | FAIL: > 90 days
- **Interpretation:** Longer gaps to second purchase correlate with lower F2 rates. Post-purchase engagement (email, recommendations) should aim to shorten this window.

---

## Product Checks (6 implemented)

### top20_revenue_concentration -- Top-20% Revenue Concentration
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: 60-80% of revenue from top 20% products | WATCH: 80-90% or < 50% | FAIL: > 90% or < 40%
- **Interpretation:** A healthy Pareto distribution supports focused inventory and marketing. Extreme concentration means the catalog is too narrow; extreme diffusion means no clear winners.

### converting_sku_rate -- Converting SKU Rate
- **Severity:** High (3.0x)
- **Thresholds:** PASS: > 70% of active SKUs have at least 1 sale | WATCH: 50-70% | FAIL: < 50%
- **Interpretation:** Low converting rate signals catalog bloat -- dead SKUs increase carrying costs, dilute marketing, and degrade customer browsing experience.

### multi_item_order_rate -- Multi-Item Order Rate
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: > 25% of orders contain 2+ items | WATCH: 15-25% | FAIL: < 15%
- **Interpretation:** Low multi-item rate suggests missed cross-sell opportunities. Improving product adjacency and recommendation logic can lift AOV.

### cross_sell_pair_lift -- Cross-Sell Pair Lift
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: 3+ product pairs with lift > 2.0 | WATCH: 1-2 pairs | FAIL: no pairs > 1.5
- **Interpretation:** Strong cross-sell pairs indicate actionable affinities for bundling and recommendation strategies that can increase basket size.

### lifecycle_stage_distribution -- Lifecycle Stage Distribution
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: decline-stage products < 30% of catalog | WATCH: 30-50% | FAIL: > 50%
- **Interpretation:** An aging catalog dominated by declining products signals lack of product innovation and future revenue risk.

### price_tier_distribution -- Price Tier Distribution
- **Severity:** Medium (1.5x)
- **Thresholds:** PASS: products span 3+ distinct price tiers | WATCH: 2 tiers | FAIL: single tier
- **Interpretation:** Multiple price tiers broaden market reach and enable upselling from entry to premium. A single tier limits customer segmentation.

---

## RFM Segment Definitions

Used by champions_loyal_share, at_risk_segment_share, lost_segment_share checks:

| Segment | R Score | F Score | Description |
|---------|---------|---------|-------------|
| Champions | 4-5 | 4-5 | Recent, frequent, high-spend |
| Loyal | 3-4 | 3-4 | Regular purchasers |
| New Customers | 4-5 | 1-2 | Recent first-time buyers |
| Potential | 3 | 2-3 | Could become loyal with engagement |
| At Risk | 1-2 | 3-5 | Were frequent, now inactive |
| Lost | 1-2 | 1-2 | Long inactive, low frequency |

---

## Check → KPI Tree Mapping

Each health check maps to one or more KPI tree nodes. The node's marker
(🟢/🟡/🔴) is determined by the **worst** result among its mapped checks:

- 🟢 = all mapped checks pass
- 🟡 = any mapped check is watch (and none fail)
- 🔴 = any mapped check is fail

### Revenue (root node)

| Check | What it signals |
|-------|----------------|
| monthly_revenue_trend | Overall revenue momentum |
| aov_trend | AOV trend health |
| order_count_trend | Order volume trend |
| daily_revenue_volatility | Revenue stability / predictability |
| large_order_dependency | Large-order dependency risk |
| category_margin_variance | Category margin health |

### New Customer Revenue (branch)

| Check | What it signals |
|-------|----------------|
| repeat_customer_revenue_share | New vs returning revenue balance (inverse: low repeat = high new dependency) |
| revenue_concentration_top10 | Customer concentration risk |

### Existing Customer Revenue (branch)

| Check | What it signals |
|-------|----------------|
| repeat_purchase_rate | Repeat purchase rate -- foundation of repeat revenue |
| champions_loyal_share | High-value customer segment strength |
| at_risk_segment_share | At-risk customer erosion |
| lost_segment_share | Lost customer accumulation |
| days_to_second_purchase | Speed of second purchase |
| repeat_customer_revenue_share | Repeat customer revenue share |

### Discount / Pricing (cross-cutting, affects root)

| Check | What it signals |
|-------|----------------|
| avg_discount_rate_trend | Discount rate level and trend |
| discounted_order_ratio | Breadth of discounting |
| discount_depth_trend | Discount depth escalation |
| free_shipping_threshold_effectiveness | Free-shipping threshold effectiveness |

### Product Mix (cross-cutting, affects AOV branches)

| Check | What it signals |
|-------|----------------|
| top20_revenue_concentration | SKU revenue concentration |
| converting_sku_rate | Catalog utilization |
| multi_item_order_rate | Cross-sell / basket composition |
| cross_sell_pair_lift | Product affinity strength |
| lifecycle_stage_distribution | Product lifecycle balance |
| price_tier_distribution | Price tier coverage |
```

## File: `skills/ecom/references/impact-formulas.md`
```markdown
# Ecom Health Check — Revenue Impact Calculation Formulas

## Quick Reference Table

| Check ID | Metric | Formula (per period) | Typical Improvement | Annualised Impact Example ($10M revenue) |
|----------|--------|---------------------|---------------------|------------------------------------------|
| repeat_purchase_rate | Repeat Purchase Rate | `New_Customers * RPR_Improvement_pp/100 * LTV_Repeat` | +3-5 pp | $150K-$500K |
| repeat_customer_revenue_share | Repeat revenue share | `Total_Revenue * Improvement_pp/100 * (1 - Churn_Volatility)` | +3-5 pp | $75K-$200K |
| avg_discount_rate_trend | Avg discount rate | `Discounted_Revenue * Reduction_pp / 100` | -1-2 pp | $50K-$150K |
| large_order_dependency | Large order dependency | Severity-based estimate (no specific formula) | varies | varies |

**Note:** "pp" = percentage points. All examples assume a $10M annual revenue baseline. Actual impact varies by category, AOV, and traffic volume.

---

## repeat_purchase_rate — Repeat Purchase Rate

### What it measures
The share of customers who make a second purchase (repeat purchase rate), and the broader returning customer ratio. Repeat customers drive disproportionate revenue and have dramatically higher conversion rates (60-70%) compared to new prospects (5-20%).

### Calculation Formula

```
Returning_Customer_Ratio = Repeat_Customers / Total_Customers * 100

Repeat_Purchase_Rate = Customers_With_2+_Orders / Total_Customers * 100

LTV_Uplift_Per_1pp_RPR = New_Customers * 0.01 * (LTV_Repeat - LTV_OneTime)

Revenue_Impact = LTV_Uplift_Per_1pp_RPR * (1 + Downstream_Acceleration)
```

**Worked example (per 1 pp repeat purchase rate improvement):**
- Annual new customers: 50,000
- LTV of one-time buyer: $215
- LTV of 2+ purchase buyer: $538 (2.5x multiplier)
- Revenue uplift = 50,000 * 0.01 * ($538 - $215) = **$161,500/year**
- With downstream acceleration (repeat buyers convert to 3rd purchase at 38.8%): effective uplift is higher

### Key LTV Multipliers by Purchase Count

| Purchase Count | Relative LTV | F(n) to F(n+1) Conversion |
|---------------|-------------|--------------------------|
| 1 (one-time) | 1.0x | ~18.8% make a repeat purchase |
| 2 | 2.5x | ~38.8% convert to F3 |
| 3 | 3.8x | ~50%+ convert to F4 |
| 5+ | 7.3x | High retention zone |

### Industry Benchmarks

| Category | Repeat Customer Rate | Repeat Revenue Share |
|----------|---------------------|---------------------|
| Overall ecommerce | 15-30% | 25-45% |
| Consumables (top) | 39-44% | 62-67% |
| Health & supplements | 29% | 45-55% |
| Beauty & cosmetics | 25.9% | 35-45% |
| Fashion & apparel | 15-26% | 13-25% |
| Home & furniture | 14.7% | 12-18% |
| Pet supplies | 30%+ | 45-55% |
| Grocery & food delivery | 30-40%+ | 50-65% |
| Durables / high-ticket | 11-17% | 12-18% |

### Typical Improvement Rates
- Loyalty / VIP tier programme: +5-10 pp repeat rate, 15-25% annual revenue lift
- Post-purchase email sequence (3-5 emails): +3-5 pp repeat purchase rate
- Personalised product recommendations: +2-4 pp
- Subscription / auto-replenish models: +10-15 pp for consumables
- 5% increase in retention -> 25-95% increase in profits (Bain & Company)
- Existing customers spend 67% more after 30+ months (Bain & Company)
- Probability of selling to existing customer: 60-70% vs 5-20% for new

### Sources
- BS&Co — Repeat Purchase Rate Benchmarks: 18.8% across 156K DTC customers (2026)
- BS&Co — LTV by Purchase Count: DTC Benchmarks from 162K customers
- Rivo — VIP Customer Repeat Rate Statistics (27 stats)
- Geckoboard — Repeat Customer Rate KPI (25-30% benchmark)
- Bain & Company — customer retention and LTV research

---

## repeat_customer_revenue_share — Repeat Revenue Share

### What it measures
The proportion of total revenue generated by repeat (returning) customers. Higher repeat revenue share indicates more predictable, stable revenue with lower acquisition cost dependency.

### Calculation Formula

```
Repeat_Revenue_Share = Revenue_From_Repeat_Customers / Total_Revenue * 100

Revenue_Stability_Score = Repeat_Revenue_Share * (1 - Monthly_Revenue_CV)
  where CV = coefficient of variation of monthly revenue

Impact_Per_1pp_Improvement = Total_Revenue * 0.01 * (1 - Blended_CAC_Rate)
  (repeat revenue has near-zero marginal CAC vs 15-30% for new customer revenue)
```

**Worked example (per 1 pp shift from new to repeat revenue):**
- Annual revenue: $10M
- Current repeat revenue share: 35%
- CAC as % of new customer revenue: 25%
- Effective savings = $10M * 0.01 * 0.25 = **$25,000/year in CAC savings**
- Plus: reduced revenue volatility and improved forecasting accuracy

### Industry Benchmarks

| Category | Repeat Revenue Share |
|----------|---------------------|
| Overall ecommerce | 25-45% |
| Consumables (top performers) | 62-67% |
| Consumables (mid-tier) | 55-64% |
| Fashion & apparel | 13-25% |
| Durables / high-ticket | 12-18% |
| Subscription-based | 65-80% |

### Key Insight: Over-indexing
- Consumable brands: repeat customers generate 1.5x their share of revenue (e.g., 44% of customers drive 67% of revenue)
- Fashion / durables: repeat customers generate ~1:1 their share (no over-index)
- Implication: repeat revenue improvement strategies have highest ROI for consumable categories

### Typical Improvement Rates
- Loyalty programme implementation: +5-10 pp repeat revenue share over 12 months
- Subscription model introduction (consumables): +15-25 pp
- Email lifecycle marketing (post-purchase flows): +3-5 pp
- Personalisation engine: +2-4 pp
- Healthy target: 40%+ repeat revenue share for most ecommerce

### Sources
- BS&Co — Repeat Purchase Rate Benchmarks (2026): 156K DTC customer analysis
- Finaloop — Ecommerce Profit Benchmarks (2024-2025 P&L data)
- Rivo — VIP Customer Repeat Rate Statistics

---

## avg_discount_rate_trend — Average Discount Rate (Margin Erosion)

### What it measures
The average discount percentage applied across all discounted transactions. avg_discount_rate_trend measures how deep discounts are when they are applied.

### Calculation Formula

```
Avg_Discount_Rate = Total_Discount_Amount / Gross_Revenue_Before_Discounts * 100

Margin_Recovery_Per_1pp = Discounted_Revenue * 0.01

Effective_Margin_Impact = Margin_Recovery / (Revenue * Gross_Margin_Rate)
  (percentage of margin recovered relative to total margin pool)
```

**Worked example (per 1 pp reduction in average discount depth):**
- Annual gross revenue (before discounts): $12M
- Discounted portion: $4M (33% of revenue is discounted)
- Current average discount: 20%
- Margin recovered per 1 pp = $4M * 0.01 = **$40,000/year**
- If gross margin is 55%: this represents 0.6% of total margin pool recovered

### Benchmarks

| Discount Depth Tier | Range | Typical Context |
|---------------------|-------|-----------------|
| Light discounting | 5-10% | Loyalty perks, first-purchase incentive |
| Moderate discounting | 10-20% | Standard promotions, seasonal sales |
| Heavy discounting | 20-30% | Clearance, competitive pricing |
| Aggressive discounting | 30%+ | End-of-life, Black Friday, distressed inventory |

### Margin Erosion Math
| Gross Margin | 10% Discount Impact | 20% Discount Impact | 30% Discount Impact |
|-------------|---------------------|---------------------|---------------------|
| 30% | Gives away 33% of profit | Gives away 67% of profit | Sells at cost |
| 40% | Gives away 25% of profit | Gives away 50% of profit | Gives away 75% |
| 50% | Gives away 20% of profit | Gives away 40% of profit | Gives away 60% |
| 60% | Gives away 17% of profit | Gives away 33% of profit | Gives away 50% |

### Typical Improvement Rates
- Replacing flat discounts with tiered spend thresholds: -2 to -3 pp depth
- Gift-with-purchase instead of % off: equivalent conversion lift at 0% discount depth
- Personalised discount depth (ML-based willingness-to-pay): -3 to -5 pp
- Reducing discount frequency (fewer sale events): -1 to -2 pp average depth

### Sources
- Opensend — Average Discount Rate Statistics for eCommerce (2025)
- SalesSo — Discounting Statistics in Sales (2025)
- Finaloop — Ecommerce Profit Benchmarks: P&L metrics (2024-2025)

---

## Cross-Metric Impact Chains

Many of these metrics are interconnected. Improving one often creates cascading effects on others.

```
Repeat Purchase Rate Improvement (repeat_purchase_rate)
  --> Higher repeat revenue share (repeat_customer_revenue_share)
       --> Lower blended CAC
            --> Revenue stability + margin improvement

Discount Reduction (avg_discount_rate_trend)
  --> Direct margin recovery
       --> Better brand perception
            --> Higher full-price conversion
```

### Priority Matrix: Effort vs Impact

| Priority | Check | Typical Effort | Typical Impact | Time to Realise |
|----------|-------|---------------|----------------|-----------------|
| 1 | repeat_purchase_rate | Medium | Very High (LTV) | 4-12 weeks |
| 2 | avg_discount_rate_trend | Low | Medium-High | Immediate |
| 3 | repeat_customer_revenue_share | Medium | Medium | 8-24 weeks |

---

## Per-Check Impact Models

Formal models using the $10M store baseline.

### repeat_purchase_rate — Repeat Purchase Rate (Formal)

\(\Delta LTV_{12} = (p_{RPR} \cdot u)(O_{rep} - 1) \cdot AOV_{rep}\), \(\Delta R_{annual} = N_{new} \cdot \Delta LTV_{12}\)

```python
def ltv_uplift_from_rpr(p_rpr, uplift_rel, o_rep, aov_repeat):
    return p_rpr * uplift_rel * (o_rep - 1.0) * aov_repeat

def annual_revenue_uplift_from_rpr(new_customers, p_rpr, uplift_rel, o_rep, aov_repeat):
    return new_customers * ltv_uplift_from_rpr(p_rpr, uplift_rel, o_rep, aov_repeat)
```

**Example.** \(N_{new}=60K\), \(p_{RPR}=25\%\), 5% relative lift, \(O_{rep}=3\), \(AOV_{rep}=\$110\): \(\Delta LTV_{12}=\$2.75\), annual = **$165K**. **Confidence: Medium-Low.** Caveat: +5pp absolute vs +5% relative yields ~4x difference.

### repeat_customer_revenue_share — Repeat Revenue Share (Formal)

\(\Delta R_{shift} = R(s_{tgt}-s_{cur})\), \(\text{Net savings} = (\Delta R_{shift}/AOV_{new}) \cdot (CAC - \text{retention\_cost})\)

```python
def repeat_share_shift_savings(annual_revenue, s_cur, s_tgt, aov_new, cac_new, retention_cost=0.0):
    delta_rev = annual_revenue * (s_tgt - s_cur)
    fewer_new = delta_rev / aov_new
    return {"delta_repeat_revenue": delta_rev, "fewer_new_orders": fewer_new,
            "net_savings": fewer_new * cac_new - fewer_new * retention_cost}
```

**Example.** 35% to 44%, CAC=$40, retention=$5: **$315K net savings**. **Confidence: Medium.** Caveat: constant total revenue is simplifying.

### avg_discount_rate_trend — Discount Reduction (Formal)

\(P'=P_0(1-d+\Delta d)\), \(Q' \approx Q(1+\epsilon \cdot \Delta d/(1-d))\), \(\Delta GP = (P'-c)Q' - (P-c)Q\). Revenue quality: \(\Delta R_{\text{const vol}} = R/(1-d) \cdot \Delta d\).

```python
def discount_margin_recovery(list_price, cogs, d_current, d_reduction_pp, elasticity, annual_orders):
    p, p_new = list_price*(1-d_current), list_price*(1-d_current+d_reduction_pp)
    q_new = annual_orders * (1 + elasticity * ((p_new/p) - 1.0))
    return {"delta_revenue": p_new*q_new - p*annual_orders,
            "delta_gross_profit": (p_new-cogs)*q_new - (p-cogs)*annual_orders}
```

**Example.** \(P_0=\$125\), d=20%, c=$55, Q=100K, 1pp reduction, \(\epsilon=-1.5\): **GP +$38K** (revenue -$65K). Constant-volume: $125K. **Confidence: Medium.** Caveat: elasticity is the key unknown.
```

## File: `skills/ecom/references/recommended-actions.md`
```markdown
# Recommended Actions Reference

This file provides specific, actionable improvement recommendations for each diagnostic check
in the claude-ecom skill. Each check includes 2-3 prioritized actions with estimated
implementation time and expected improvement range based on industry research and benchmarks.

---

## monthly_revenue_trend: MoM Revenue Growth (Low)

When month-over-month revenue growth is stagnant or declining, the root cause is typically
a combination of weakening acquisition, poor retention, or seasonal patterns not being leveraged.

### Actions

1. **Launch a win-back email campaign targeting lapsed customers**
   - Time: 3-5 days
   - Impact: 5-15% incremental revenue from reactivated customers
   - Details: Segment customers who purchased 60-120 days ago but have not returned.
     Send a 3-email sequence with a personalized incentive (e.g., 10% off their most-browsed
     category). Shopify data shows win-back flows recover 2-5% of lapsed customers.

2. **Implement a monthly promotional calendar aligned to micro-seasons**
   - Time: 2-3 days to plan; ongoing execution
   - Impact: 8-20% revenue lift during promoted periods
   - Details: Map out monthly themes, product highlights, and limited-time offers tied to
     cultural moments, seasonal demand, or new product launches. Consistent promotional
     cadence smooths MoM volatility. Aim for 10-20% MoM growth in early-stage ecommerce
     and 3-5% for mature stores.

3. **Optimize high-traffic landing pages for conversion**
   - Time: 1-2 weeks
   - Impact: 10-30% conversion lift on targeted pages
   - Details: Identify the top 5-10 landing pages by traffic volume. A/B test headlines,
     CTAs, hero images, and social proof placement. Even small CVR improvements on
     high-traffic pages compound into meaningful revenue growth.

### Sources
- Alexander Jarvis, "MoM Growth in Ecommerce" (alexanderjarvis.com)
- Amplitude, "Month-Over-Month Growth Rates" (amplitude.com/blog)
- Shopify, "Win-Back Email Best Practices"

---

## repeat_customer_revenue_share: Repeat Customer Revenue Share (Low)

A low share of revenue from repeat customers (typically below 30%) signals over-reliance
on new customer acquisition, which is 5-7x more expensive than retention.

### Actions

1. **Launch a tiered loyalty/rewards program**
   - Time: 1-2 weeks (using platforms like Smile.io, Yotpo, or Rivo)
   - Impact: 15-25% increase in repeat purchase rate; loyalty members spend 3.1x more
   - Details: Implement a points-based system with 2-3 tiers. Tiered programs achieve
     1.8x higher ROI than flat programs. VIP customers generate 73% higher AOV ($435 vs $291)
     and purchase 3.6x more frequently. Start simple: earn points on purchase, redeem for
     discounts.

2. **Build a post-purchase email automation sequence**
   - Time: 3-5 days
   - Impact: 10-20% increase in second-purchase rate
   - Details: After first purchase, send a sequence: order confirmation with cross-sell,
     product education/tips at day 3, review request at day 7, replenishment or
     complementary product suggestion at day 14-30. Customers who return for a second
     purchase have a 45% chance of buying a third time (Shopify data).

3. **Introduce subscription or auto-replenishment options for consumable products**
   - Time: 1-2 weeks
   - Impact: 20-40% improvement in retention over 6 months
   - Details: Subscription merchants see 45% retention at 6 months vs 20% for standard
     ecommerce (Recharge data). Offer a 5-10% discount for subscribe-and-save to
     incentivize enrollment.

### Sources
- Rivo, "27 VIP Customer Repeat Rate Statistics" (rivo.io)
- Shopify, "Repeat Purchase Rate Benchmarks"
- Recharge, "State of Subscriptions Report"
- The Seventh Sense, "12 Strategies to Increase Repeat Purchase Rate"
- Envive AI, "36 Customer Retention Statistics in eCommerce 2026"

---

## avg_discount_rate_trend: Average Discount Rate (High)

An excessively high average discount rate (typically above 15-20%) erodes margins,
trains customers to wait for sales, and devalues the brand.

### Actions

1. **Shift from percentage discounts to value-added incentives**
   - Time: 1-2 days to plan; ongoing
   - Impact: 5-10 percentage point reduction in average discount rate while maintaining conversion
   - Details: Replace blanket percentage discounts with free shipping thresholds, gift-with-purchase,
     bundle deals, or extended warranties. These preserve perceived value while costing less
     than equivalent percentage discounts. 81% of abandoned cart emails offer percentage discounts;
     differentiate by offering non-discount value.

2. **Implement tiered discount rules with maximum caps**
   - Time: 1-3 days
   - Impact: 3-8 percentage point reduction in average discount depth
   - Details: Set maximum discount caps (e.g., never exceed 20%), prohibit discount stacking,
     and use tiered thresholds (e.g., "Spend $100 get $10 off, spend $200 get $25 off")
     that increase AOV. Track gross margin per promotion, not just conversion.

3. **Create urgency through scarcity rather than discounts**
   - Time: 2-5 days
   - Impact: Maintain conversion rates while reducing discount dependency by 15-30%
   - Details: Use limited-edition products, countdown timers on flash sales, low-stock
     indicators, and early-access for loyalty members. These psychological triggers drive
     conversion without margin erosion. Reserve deep discounts for clearance of end-of-life SKUs only.

### Sources
- ReferralCandy, "The Complete Ecommerce Discount Strategy Guide for 2026"
- Email Vendor Selection, "Cart Abandonment Rate Statistics 2026"
- Pitney Bowes, "6 Ideas for Improving eCommerce Profit Margins"

---

## large_order_dependency: Large Order Dependency (High)

When a small number of large orders account for a disproportionate share of revenue
(>5-10%), the business faces fragility risk — losing those customers or orders
would materially impact performance.

### Actions

1. **Analyze large-order customers and diversify revenue sources**
   - Time: 1-3 days for analysis; ongoing for execution
   - Impact: Reduce single-order concentration below 5% of period revenue
   - Details: Identify orders exceeding 5% of period revenue. Determine if they are
     recurring (B2B accounts, wholesale) or one-off. For recurring large accounts,
     build relationship management but also actively grow the mid-tier customer base.
     For one-off spikes, discount them from trend analysis to avoid false signals.

2. **Grow the mid-tier customer base to reduce concentration**
   - Time: 2-4 weeks
   - Impact: 10-20% increase in order count from diversified sources
   - Details: Shift acquisition spend toward channels that attract higher volumes of
     mid-value customers rather than fewer high-value ones. Introduce tiered pricing
     or product bundles that appeal to a broader audience. A healthy revenue
     distribution has no single order exceeding 5% of monthly revenue.

3. **Implement revenue monitoring alerts for concentration risk**
   - Time: 1-2 days
   - Impact: Early warning when dependency thresholds are breached
   - Details: Set up automated alerts when any single order exceeds 5% of trailing-30d
     revenue, or when the top 3 orders exceed 15%. This enables proactive response
     before concentration becomes structural.

### Sources
- Revenue concentration risk management best practices
- Customer diversification strategies for D2C ecommerce

---

## top20_revenue_concentration: Top 20% SKU Revenue Concentration (Too High)

When the top 20% of SKUs account for >80% of revenue (extreme Pareto), the business
is overly dependent on a narrow product range, creating risk and limiting growth.

### Actions

1. **Create discovery merchandising for mid-tier products**
   - Time: 3-7 days
   - Impact: 10-20% revenue shift toward the mid-tier over 3-6 months
   - Details: Feature "hidden gems," "staff picks," or "rising products" collections
     on the homepage and in email campaigns. Use product recommendations to cross-sell
     mid-tier items alongside bestsellers. Bundle top sellers with lesser-known products
     to introduce them to customers.

2. **Invest in content marketing and SEO for long-tail product categories**
   - Time: 2-4 weeks; ongoing
   - Impact: 15-30% increase in organic traffic to non-hero product pages
   - Details: Create buying guides, comparison articles, and how-to content targeting
     long-tail keywords related to underperforming categories. Each piece of content
     acts as a new entry point to the catalog. Internal linking from top-selling
     product pages to related mid-tier products distributes link equity.

3. **Review and optimize pricing/positioning of mid-tier products**
   - Time: 3-5 days for analysis; ongoing for testing
   - Impact: 5-15% conversion improvement on repositioned products
   - Details: Analyze why mid-tier products underperform. Common issues: poor product
     photography, weak descriptions, uncompetitive pricing, or low review counts.
     Prioritize the top 20 mid-tier products with the best margin potential and
     systematically fix their product pages.

### Sources
- IBSW, "SKU Rationalization in E-Commerce: Strategic Approach to Growth"
- ThoughtSpot, "How to Use Data to Optimize Your SKU Rationalization Process"
- Onramp Funds, "9 Ways to Improve eCommerce Profit Margins"

---

## converting_sku_rate: Converting SKU Rate (Low)

A low converting SKU rate (below 50-70%) indicates catalog bloat — too many SKUs
with zero or negligible sales. This increases carrying costs, dilutes marketing
resources, and degrades the customer browsing experience.

### Actions

1. **Conduct SKU rationalization: discontinue or archive non-converting SKUs**
   - Time: 1-2 weeks for analysis and decision; ongoing
   - Impact: 5-15% reduction in inventory carrying costs; improved site navigation
   - Details: Flag all SKUs with zero sales in the past 90 days. Categorize as:
     (a) new launches (keep, promote), (b) seasonal (archive until season),
     (c) truly dead stock (clearance or discontinue). Removing dead SKUs reduces
     storage costs, simplifies operations, and makes the catalog easier to browse.
     SKU rationalization typically improves profit margins by focusing resources
     on high-performers.

2. **Bundle or promote non-converting SKUs with bestsellers before discontinuing**
   - Time: 3-5 days
   - Impact: Recover 10-30% of dead stock investment
   - Details: Create "complete the set" bundles pairing slow movers with popular
     items. Run a targeted clearance campaign with email and social promotion.
     Offer non-converting items as gifts-with-purchase above a spend threshold.
     If products still do not sell after a 30-day promotional push, proceed with
     discontinuation.

3. **Implement a new product launch checklist to prevent future non-converting additions**
   - Time: 2-3 days to create process
   - Impact: 20-40% fewer non-converting SKUs added over time
   - Details: Before adding a new SKU, require: demand signal validation (search
     data, customer requests), minimum viable product page (6+ images, complete
     description, competitive price analysis), and a 30-day launch marketing plan.
     Set a 60-day review gate: if a new SKU has zero sales by day 60, trigger
     a mandatory review.

### Sources
- Toolio, "SKU Rationalization: What It Is and How to Optimize It"
- Brightpearl, "How to Perform SKU Rationalization to Improve Product Management"
- ThoughtSpot, "How to Use Data to Optimize Your SKU Rationalization Process"
- IBSW, "SKU Rationalization in E-Commerce: Strategic Approach to Growth"

---

## repeat_purchase_rate: Repeat Purchase Rate (Low)

A low returning customer ratio (below 20-30%) means most revenue comes from one-time
buyers, indicating weak post-purchase engagement and retention.

### Actions

1. **Deploy a post-purchase engagement sequence across email and SMS**
   - Time: 3-5 days
   - Impact: 10-20% increase in second-purchase rate within 90 days
   - Details: Send targeted communications: thank-you + order tracking (day 0),
     product tips/care guide (day 3), review request (day 7), cross-sell recommendation
     based on purchase (day 14), replenishment reminder or new arrival alert (day 30).
     56% of shoppers become repeat buyers following personalized experiences.

2. **Implement a referral program with dual incentives**
   - Time: 3-7 days (using tools like ReferralCandy, Yotpo, or native platform features)
   - Impact: 5-10% increase in returning customer rate; referred customers have 16% higher LTV
   - Details: Offer rewards to both the referrer and the new customer (e.g., "$10 off
     for you and your friend"). Referral programs create a re-engagement touchpoint for
     existing customers while acquiring high-quality new customers who are pre-disposed
     to loyalty.

3. **Create a VIP or membership program for top customers**
   - Time: 1-2 weeks
   - Impact: 15-25% increase in purchase frequency among enrolled customers
   - Details: The top 5% of customers generate 35% of ecommerce revenue.
     Identify these customers and offer exclusive benefits: early access to sales,
     free shipping, birthday rewards, or members-only products. VIP customers show
     73% higher AOV and 3.6x purchase frequency. Even simple recognition (handwritten
     notes, surprise gifts) drives emotional loyalty.

### Sources
- Envive AI, "36 Customer Retention Statistics in eCommerce 2026"
- Amplience, "5 Proven Ecommerce Customer Retention Strategies"
- Recharge, "6 Ecommerce Retention Strategies to Maximize Repeat Business"
- Rivo, "VIP Customer Repeat Rate Statistics"

---

## Cross-Cutting Recommendations

Several actions reinforce multiple metrics simultaneously:

| Action | Checks Improved |
|--------|----------------|
| Loyalty/rewards program | repeat_customer_revenue_share, repeat_purchase_rate, monthly_revenue_trend |
| Post-purchase email automation | repeat_customer_revenue_share, repeat_purchase_rate, monthly_revenue_trend |
| SKU rationalization | top20_revenue_concentration, converting_sku_rate |
| Shift from % discounts to value-added incentives | avg_discount_rate_trend |

---

## Implementation Priority Framework

When multiple checks are flagged, prioritize actions by:

1. **Quick wins** (< 3 days, high impact): Post-purchase email sequences,
   free-shipping threshold adjustment, discount cap rules
2. **Medium effort** (1-2 weeks, high impact): Loyalty program launch,
   SKU rationalization, product page optimization
3. **Strategic initiatives** (2-8 weeks, transformational): Private-label
   development, supplier renegotiation, subscription model

Focus on the highest-impact items first, typically retention automation (repeat_customer_revenue_share, repeat_purchase_rate)
and discount governance (avg_discount_rate_trend), as these have the fastest payback period.

---

## Vertical-Specific Strategy Playbooks

When the business vertical is identified, apply the corresponding strategy playbook
from [`benchmarks.md`](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/ai_research/distributed_training_megatron_core/references/benchmarks.md) to prioritize actions.

| Vertical | Top Priority Action | Reference |
|----------|--------------------|-----------|
| Fashion & Apparel | Build fit-confidence layer to reduce preventable returns | `benchmarks.md` |
| Beauty & Cosmetics | Implement guided selling (shade finders, quizzes) | `benchmarks.md` |
| Food & Beverage | Make subscription-first for consumable staples | `benchmarks.md` |
| Electronics & Gadgets | Make PDPs decision-complete (specs, compatibility) | `benchmarks.md` |
| Home & Living | Upgrade confidence merchandising (dimensions, UGC) | `benchmarks.md` |
| Health & Wellness | Build trust stack (certifications, claim review) | `benchmarks.md` |

See also: [`finding-clusters.md`](finding-clusters.md) for how clusters inform action prioritization.
```

## File: `skills/ecom/references/review-narratives.md`
```markdown
# Review Narrative Templates

Reference file for interpreting business review reports (REVIEW.md).
Use these templates to write natural language interpretation.　Single unified review with multi-period architecture
(30d Pulse / 90d Momentum / 365d Structure).

---

## 1. Performance Narrative Templates

Select the template matching the growth trajectory. Used in the Executive
Summary narrative and as a starting point for period-level headlines.

### Strong Growth (revenue > +10% vs prior period)

> {Period} delivered strong revenue growth of {delta}%, driven primarily by
> {primary_driver: new customers / returning customers / AOV increase}.
> {secondary_observation}. The key question is whether this momentum is
> sustainable or driven by one-time factors.

### Stable Performance (-5% to +10% vs prior period)

> {Period} showed stable performance with revenue {direction} {delta}%,
> largely in line with expectations. {strength_callout}. The focus should
> shift to incremental optimization rather than diagnosing problems.

### Declining Performance (revenue < -5% vs prior period)

> {Period} saw a {delta}% revenue decline, primarily driven by
> {primary_driver: fewer orders / lower AOV / customer churn}.
> {urgency_statement}. Immediate investigation is needed to determine
> whether this is cyclical or structural.

### Mixed Signals

> {Period} presents a mixed picture: {positive_signal} but offset by
> {negative_signal}. The {metric} improvement of {value} is encouraging,
> but the {concerning_metric} decline of {value} warrants monitoring.

---

## 2. Executive Summary Template

The Executive Summary is a 4-6 line narrative that synthesizes across all
available periods. It is NOT a KPI list.

### Structure

```
[North Star + trend across periods]
[What's driving it -- connect 365d structure to 90d momentum to 30d signal]
[Most important action, with timeline]
```

### Worked Example

> Revenue reached $1.38M for the year (+25.7% YoY), but growth is decelerating --
> the last 90 days grew only 8% vs prior 90 days, and last month was flat (+0.3%).
> Growth depends on existing customer AOV increases (+14.8%), while new customer
> acquisition has stalled (share: 42.3%, unchanged). Reallocate 20% of retention
> budget to acquisition channels by end of this month, targeting CPA below $XX.

### Anti-patterns (PROHIBITED)

- "Revenue $1.38M, Orders 5,784, AOV $239, Customers 2,765..." -- number dump
- "The store performed well across most metrics" -- no specifics
- "Several areas show room for improvement" -- no direction
- "In the last 30 days X. In the last 90 days Y. In the last year Z." -- sequential summary instead of synthesis

---

## 3. KPI Tree Template

The KPI Tree replaces flat KPI tables. Revenue is the root, decomposed into
branches. Each node shows metric value + change vs prior period + health marker.

Markers are driven by internal health check results:
- 🟢 healthy (all associated checks pass)
- 🟡 watch (any associated check in warning)
- 🔴 problem (any associated check failing)

### Template

```
Revenue {value} (vs prior period: {change}%)
|-- {marker} New Customer Revenue {value} ({share}% of total)
|   |-- New Customers: {n} ({change}%)
|   |-- New Customer AOV: ${value} ({change}%)
|-- {marker} Existing Customer Revenue {value} ({share}% of total)
    |-- Returning Customers: {n} ({change}%)
    |-- Returning AOV: ${value} ({change}%)
    |-- Repeat Purchase Rate: {pct}% -- first-to-second purchase conversion (365d only)
```

### Worked Example (365d)

```
Revenue $1.38M (YoY +25.7%)
|-- 🟡 New Customer Revenue $584K (42.3% of total)
|   |-- New Customers: 1,812 (+10.3%)
|   |-- New Customer AOV: $323 (+4.1%)
|-- 🟢 Existing Customer Revenue $799K (57.7% of total)
    |-- Returning Customers: 953 (+10.3%)
    |-- Returning AOV: $838 (+18.2%)
    |-- Repeat Purchase Rate: 38%
```

### Worked Example (30d)

Keep 30d trees compact -- same structure, but no extra commentary:

```
Revenue $98K (MoM: = flat)
|-- 🟡 New Customer Revenue $38K (38.8%)
|   |-- New Customers: 95 (-8%)
|   |-- New Customer AOV: $400 (+3%)
|-- 🟢 Existing Customer Revenue $60K (61.2%)
    |-- Returning Customers: 192 (-3%)
    |-- Returning AOV: $312 (+1%)
    |-- Repeat Purchase Rate: 96%
```

### Marker Decision Rules

| Condition | Marker | When to use |
|-----------|--------|-------------|
| 🟢 | All checks pass | Metric is healthy, on track |
| 🟡 | Any check in warning | Emerging concern, worth noting |
| 🔴 | Any check failing | Active problem, must appear in findings |

---

## 4. Finding Templates

Every finding in the report follows: **What is → Why it matters → What to do**

See SKILL.md Finding Quality Standards for the rules. This section provides
worked examples for common D2C patterns.

### Growth Dependency

```
What is:       Annual revenue grew 25.7% YoY.
Why it matters: However, despite a 25.4% reduction in discount rate, new customer
               revenue share remains at 42.3% -- growth depends entirely on
               existing customer AOV increases (+14.8%). If existing customer
               purchase frequency slows, growth stops.
What to do:    Reallocate retention budget toward acquisition channels to diversify growth sources.
```

### Retention Cliff

```
What is:       Repeat purchase rate (first-to-second purchase conversion) is 38%, near top quartile.
Why it matters: However, F3 rate drops to 18% -- a 53% falloff between second and
               third purchase. More than half of second-time buyers never come back,
               creating a ceiling on customer lifetime value.
What to do:    Launch a post-second-purchase re-engagement sequence to close the F2-to-F3 gap.
```

### Seasonality Dependency

```
What is:       Q4 (Oct-Dec) accounts for 41% of annual revenue.
Why it matters: Q4 dependency rose 5 percentage points from prior year (was 36%).
               Q1-Q3 quarterly average is $197K and flat -- any Q4 shortfall now
               threatens the full-year target with no buffer.
What to do:    Build a non-Q4 revenue lever (e.g., summer campaign) to reduce seasonal dependency.
```

### Product Concentration

```
What is:       Top 5 SKUs account for 62% of total revenue.
Why it matters: Two of these SKUs are 18+ months old with YoY growth declining 8%.
               No replacement SKUs are in the pipeline. If these two slow further,
               total revenue declines directly.
What to do:    Accelerate new SKU pipeline to reduce top-5 revenue concentration.
```

### Revenue Volatility

```
What is:       Daily revenue coefficient of variation is 0.77 over the last 90 days.
Why it matters: D2C benchmark is below 0.5. High volatility means revenue depends on
               spike days (promotions, viral moments) rather than consistent demand.
               This makes forecasting unreliable and inventory planning difficult.
What to do:    Shift promotional budget from flash sales toward always-on acquisition to stabilize daily revenue.
```

### Discount Creep

```
What is:       Average discount rate is 6.6%, within healthy range.
Why it matters: However, 55% of orders include a discount -- up from 42% last quarter.
               The rate per order is low, but the breadth of discounting is expanding.
               If unchecked, customers begin to expect discounts on every purchase.
What to do:    Restrict promo code distribution to targeted segments to cap discounted order ratio.
```

### Customer Acquisition Stall

```
What is:       New customer count grew 10.3% YoY.
Why it matters: Despite this, new customer revenue share has not improved (42.3%,
               unchanged). New customer AOV is 2.6x lower than returning customer AOV,
               meaning acquisition growth isn't translating to revenue share gains.
What to do:    Test an upsell flow for first-time buyers to lift new customer AOV.
```

---

## 5. Period-Specific Guidance

Each period has a different role. The narrative tone and finding emphasis
should match.

### 30d Pulse

**Tone:** Direct, concise. Flag fires only.

**KPI Tree:** Show the full tree but keep it compact. No growth drivers section.

**Findings:** Max 1. Only surface findings if something anomalous happened --
a sudden drop, a spike, a metric crossing a threshold. If the month was
unremarkable, say so in one sentence and move on.

**Headline examples:**
- "30d Pulse: New customer acquisition dropped 15% -- investigate channel performance"
- "30d Pulse: Steady month, no anomalies detected"
- "30d Pulse: AOV spike of +12% driven by a single high-value cohort"

### 90d Momentum

**Tone:** Analytical. This is the main body of the review.

**KPI Tree:** Full tree with growth drivers (2-3 sentences on volume vs price).

**Findings:** Max 2. Focus on whether trends are improving or deteriorating,
and whether recent initiatives are working. Compare to prior 90 days.

**Headline examples:**
- "90d Momentum: Growth is decelerating -- AOV gains slowing while volume is flat"
- "90d Momentum: Retention improvements are paying off -- repeat purchase rate up 4pp"
- "90d Momentum: Mixed signals -- orders up but AOV declining, net revenue flat"

### 365d Structure

**Tone:** Strategic. This is the "big picture" section.

**KPI Tree:** Full tree with growth drivers (2-3 sentences on structural changes).

**Findings:** Max 3. Focus on structural issues: concentration risk, dependency
patterns, customer mix evolution, product lifecycle shifts. These findings
should drive the quarterly actions in the Action Plan.

**Headline examples:**
- "365d Structure: Revenue doubled, but growth is entirely AOV-driven -- volume engine needs building"
- "365d Structure: Healthy diversification -- no single product exceeds 15% share"
- "365d Structure: Customer base is aging -- 40% of revenue comes from cohorts acquired 18+ months ago"

---

## 6. Risk Assessment Rubric

Risks surface as findings (using the standard "What is / Why it matters / What to do"
format). Use this rubric to determine severity when a health check or trend
suggests structural risk.

### Severity Determination

| Risk Factor | High (must appear in findings) | Medium (mention if space) | Low (omit) |
|-------------|-------------------------------|--------------------------|------------|
| Revenue Concentration | Top product >50% share | Top product 30-50% | <30% |
| Acquisition Dependency | Returning share <30% | Returning share 30-40% | >40% |
| Discount Dependency | Avg discount >25% or rising trend | 15-25% | <15% stable |
| Product Lifecycle | Decline stage >50% of SKUs | 30-50% | <30% |
| Growth Sustainability | Revenue AND customers declining | One declining | Both growing |
| Revenue Volatility | Daily CV >0.8 | 0.5-0.8 | <0.5 |

High-severity risks MUST appear as findings. Medium risks appear only if the
finding cap for that period allows. Low risks are omitted from the report.

---

## 7. Action Plan Templates by Time Horizon

Actions in the unified Action Plan are grouped by time horizon. Each horizon
maps to the period that surfaced the finding.

### Immediate (from 30d Pulse signals)

Actions should be:
- Executable this week or next
- Measurable within 30 days
- Focused on stopping bleeding or capturing quick wins

Template:
```
1. {Specific action, one sentence}
   Why: {Data reference from 30d finding}
   When: {This week / Next week / By [date]}
   Success metric: {Measurable outcome}
```

### This Month (from 90d Momentum findings)

Actions should be:
- Executable within 30 days
- Connected to trend reversal or acceleration
- Include a clear test/learn component

Template:
```
2. {Specific action, one sentence}
   Why: {Data reference from 90d finding}
   When: By end of {month}
   Success metric: {Measurable outcome within 90 days}
```

### This Quarter (from 365d Structure insights)

Actions should be:
- Structural or foundational changes
- May require cross-team coordination
- Impact measured over 3-6 months

Template:
```
4. {Specific action, one sentence}
   Why: {Data reference from 365d finding}
   When: {Q2 / By end of June / etc.}
   Success metric: {Measurable outcome within 6 months}
```

### Guardrails

Every Action Plan ends with guardrails. These are metrics NOT being optimized
but that must be monitored for unintended side effects.

Template:
```
Guardrails:
- {Metric} must stay {above/below} {threshold} (currently {value})
- {Metric} must stay {above/below} {threshold} (currently {value})
```

Common guardrail pairs:
| If optimizing... | Monitor as guardrail |
|-----------------|---------------------|
| Revenue growth | Discount rate, gross margin |
| New customer acquisition | Customer acquisition cost |
| AOV increase | Conversion rate, order volume |
| Discount reduction | Revenue, order volume |
| Email open rate | Unsubscribe rate |
```

## File: `tests/test_checks.py`
```python
"""Tests for claude_ecom.checks."""

from claude_ecom.checks import (
    CheckResult,
    build_action_candidates,
    build_top_issues,
    estimate_revenue_impact,
)


class TestEstimateImpact:
    def test_pass_excluded(self):
        checks = [CheckResult("monthly_revenue_trend", "revenue", "high", "pass")]
        impacts = estimate_revenue_impact(checks, 1_000_000)
        assert len(impacts) == 0

    def test_fail_has_impact(self):
        checks = [CheckResult("monthly_revenue_trend", "revenue", "critical", "fail")]
        impacts = estimate_revenue_impact(checks, 1_000_000)
        assert "monthly_revenue_trend" in impacts
        assert impacts["monthly_revenue_trend"]["annual_revenue_impact"] > 0
        assert impacts["monthly_revenue_trend"]["confidence"] == "high"


class TestBuildTopIssues:
    def test_excludes_pass(self):
        checks = [
            CheckResult("monthly_revenue_trend", "revenue", "high", "pass"),
            CheckResult("repeat_customer_revenue_share", "revenue", "critical", "fail", "test", 0.1, 0.3),
        ]
        issues = build_top_issues(checks, 1_000_000)
        assert len(issues) == 1
        assert issues[0]["id"] == "repeat_customer_revenue_share"

    def test_sorted_by_severity(self):
        checks = [
            CheckResult("daily_revenue_volatility", "revenue", "medium", "watch", "low sev"),
            CheckResult("repeat_customer_revenue_share", "revenue", "critical", "fail", "high sev"),
        ]
        issues = build_top_issues(checks, 1_000_000)
        assert issues[0]["id"] == "repeat_customer_revenue_share"

    def test_max_issues(self):
        checks = [CheckResult(f"test_check_{i}", "revenue", "medium", "fail") for i in range(20)]
        issues = build_top_issues(checks, 1_000_000, max_issues=5)
        assert len(issues) <= 5

    def test_has_estimated_impact(self):
        checks = [CheckResult("repeat_customer_revenue_share", "revenue", "critical", "fail", "test", 0.1, 0.3)]
        issues = build_top_issues(checks, 1_000_000)
        assert "estimated_annual_impact" in issues[0]


class TestBuildActionCandidates:
    def test_generates_actions(self):
        issues = [
            {
                "id": "multi_item_order_rate",
                "category": "product",
                "severity": "high",
                "result": "fail",
                "message": "test",
                "estimated_annual_impact": 50000,
            },
        ]
        actions = build_action_candidates(issues)
        assert len(actions) >= 1
        assert actions[0]["source_check"] == "multi_item_order_rate"
        assert actions[0]["timeline"] == "this_month"

    def test_max_actions(self):
        issues = [
            {
                "id": f"test_check_{i}",
                "category": "revenue",
                "severity": "medium",
                "result": "fail",
                "message": "test",
                "estimated_annual_impact": 1000,
            }
            for i in range(20)
        ]
        actions = build_action_candidates(issues, max_actions=5)
        assert len(actions) <= 5

    def test_severity_timeline_mapping(self):
        issues = [
            {
                "id": "repeat_customer_revenue_share",
                "category": "revenue",
                "severity": "critical",
                "result": "fail",
                "message": "test",
                "estimated_annual_impact": 100000,
            },
        ]
        actions = build_action_candidates(issues)
        assert actions[0]["timeline"] == "this_week"
```

## File: `tests/test_cli_review.py`
```python
"""Tests for the unified review CLI command."""

import json
import os

from click.testing import CliRunner

from claude_ecom.cli import cli

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES_DIR, "sample_orders.csv")


class TestReviewCommand:
    def test_produces_review_json(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        assert result.exit_code == 0, result.output
        review_path = tmp_path / "review.json"
        assert review_path.exists()

    def test_review_json_valid(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        assert result.exit_code == 0
        with open(tmp_path / "review.json") as f:
            data = json.load(f)
        assert "version" in data
        assert "metadata" in data
        assert "health" in data

    def test_period_filter(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--period", "30d", "--output", str(tmp_path)])
        assert result.exit_code == 0, result.output
        assert (tmp_path / "review_30d.json").exists()

    def test_nrows_option(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--nrows", "50", "--output", str(tmp_path)])
        assert result.exit_code == 0

    def test_shows_coverage(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        assert result.exit_code == 0
        assert "Data coverage" in result.output
```

## File: `tests/test_clusters.py`
```python
"""Tests for finding cluster activation logic in report.py.

Clusters group related check failures into systemic themes.
They are critical for the LLM interpretation layer -- if clusters
don't activate correctly, the report misses key business insights.

4 clusters: B (Discount), C (Assortment), F (Customer), G (Concentration).
"""

from claude_ecom.checks import CheckResult
from claude_ecom.report import _build_clusters


def _make_check(check_id, category, severity, result):
    return CheckResult(
        check_id=check_id,
        category=category,
        severity=severity,
        result=result,
        message=f"{check_id} test message",
    )


class TestClusterActivation:
    """Clusters should activate when 2+ member checks are non-pass."""

    def test_no_clusters_when_all_pass(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "pass"),
            _make_check("discounted_order_ratio", "revenue", "high", "pass"),
            _make_check("repeat_purchase_rate", "customer", "critical", "pass"),
        ]
        clusters = _build_clusters(checks)
        assert len(clusters) == 0

    def test_no_cluster_with_single_fail(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "fail"),
            _make_check("discounted_order_ratio", "revenue", "high", "pass"),
        ]
        clusters = _build_clusters(checks)
        discount_clusters = [c for c in clusters if c["name"] == "Discount Dependency"]
        assert len(discount_clusters) == 0

    def test_discount_dependency_activates(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "fail"),
            _make_check("discounted_order_ratio", "revenue", "high", "fail"),
        ]
        clusters = _build_clusters(checks)
        names = [c["name"] for c in clusters]
        assert "Discount Dependency" in names

    def test_customer_ltv_activates(self):
        checks = [
            _make_check("repeat_customer_revenue_share", "revenue", "critical", "fail"),
            _make_check("repeat_purchase_rate", "customer", "critical", "fail"),
            _make_check("at_risk_segment_share", "customer", "high", "watch"),
        ]
        clusters = _build_clusters(checks)
        names = [c["name"] for c in clusters]
        assert "Customer & LTV Engine Weakness" in names

    def test_revenue_concentration_activates(self):
        checks = [
            _make_check("revenue_concentration_top10", "revenue", "medium", "watch"),
            _make_check("top20_revenue_concentration", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        names = [c["name"] for c in clusters]
        assert "Revenue Concentration Risk" in names

    def test_assortment_activates(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        names = [c["name"] for c in clusters]
        assert "Assortment & Merchandising Misfit" in names


class TestClusterContent:
    """Each cluster should have useful content for the LLM."""

    def test_cluster_has_name(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        assert clusters[0]["name"]

    def test_cluster_has_count(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        assert clusters[0]["count"] == 2

    def test_cluster_has_hypothesis(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        assert len(clusters[0]["hypothesis"]) > 10

    def test_cluster_has_approach(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        assert len(clusters[0]["approach"]) > 10

    def test_cluster_has_related_issues(self):
        checks = [
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        assert "related_issues" in clusters[0]
        assert len(clusters[0]["related_issues"]) > 0


class TestClusterWorstCheck:
    """The worst check should be the most severe."""

    def test_critical_fail_is_worst(self):
        checks = [
            _make_check("repeat_customer_revenue_share", "revenue", "critical", "fail"),
            _make_check("repeat_purchase_rate", "customer", "critical", "watch"),
            _make_check("champions_loyal_share", "customer", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        customer_cluster = [c for c in clusters if c["name"] == "Customer & LTV Engine Weakness"]
        if customer_cluster:
            assert (
                "repeat_customer_revenue_share" in customer_cluster[0]["hypothesis"]
                or "repeat_purchase_rate" in customer_cluster[0]["hypothesis"]
            )

    def test_fail_beats_watch_at_same_severity(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "watch"),
            _make_check("discounted_order_ratio", "revenue", "high", "fail"),
        ]
        clusters = _build_clusters(checks)
        discount_cluster = [c for c in clusters if c["name"] == "Discount Dependency"]
        if discount_cluster:
            assert "discounted_order_ratio" in discount_cluster[0]["hypothesis"]


class TestMultipleClusters:
    """Multiple clusters can activate simultaneously."""

    def test_two_clusters_activate(self):
        checks = [
            # Discount Dependency
            _make_check("avg_discount_rate_trend", "revenue", "high", "fail"),
            _make_check("discounted_order_ratio", "revenue", "high", "fail"),
            # Assortment
            _make_check("converting_sku_rate", "product", "high", "fail"),
            _make_check("multi_item_order_rate", "product", "medium", "fail"),
        ]
        clusters = _build_clusters(checks)
        names = [c["name"] for c in clusters]
        assert "Discount Dependency" in names
        assert "Assortment & Merchandising Misfit" in names

    def test_na_checks_do_not_activate_clusters(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "na"),
            _make_check("discounted_order_ratio", "revenue", "high", "na"),
        ]
        clusters = _build_clusters(checks)
        assert len(clusters) == 0

    def test_pass_checks_do_not_activate_clusters(self):
        checks = [
            _make_check("avg_discount_rate_trend", "revenue", "high", "pass"),
            _make_check("discounted_order_ratio", "revenue", "high", "fail"),
        ]
        clusters = _build_clusters(checks)
        discount_clusters = [c for c in clusters if c["name"] == "Discount Dependency"]
        assert len(discount_clusters) == 0
```

## File: `tests/test_loader.py`
```python
"""Tests for claude_ecom.loader."""

import os

import pandas as pd

from claude_ecom.loader import (
    _auto_map_columns,
    _fuzzy_map_columns,
    _normalise_generic_orders,
    detect_format,
    load_orders,
    validate_schema,
)

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES, "sample_orders.csv")
ONLINE_RETAIL_CSV = os.path.join(FIXTURES, "online_retail_sample.csv")


class TestDetectFormat:
    def test_generic_format(self):
        assert detect_format(ORDERS_CSV) == "generic"


class TestLoadOrders:
    def test_load_returns_dataframe(self):
        df = load_orders(ORDERS_CSV)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 500

    def test_required_columns_present(self):
        df = load_orders(ORDERS_CSV)
        for col in ("order_id", "order_date", "amount", "customer_id"):
            assert col in df.columns

    def test_order_date_is_datetime(self):
        df = load_orders(ORDERS_CSV)
        assert pd.api.types.is_datetime64_any_dtype(df["order_date"])

    def test_amount_is_numeric(self):
        df = load_orders(ORDERS_CSV)
        assert pd.api.types.is_numeric_dtype(df["amount"])


class TestValidateSchema:
    def test_valid_orders(self):
        df = load_orders(ORDERS_CSV)
        result = validate_schema(df, "orders")
        assert result.valid is True
        assert result.missing_columns == []

    def test_missing_columns(self):
        df = pd.DataFrame({"foo": [1]})
        result = validate_schema(df, "orders")
        assert result.valid is False
        assert len(result.missing_columns) > 0


class TestOnlineRetailFormat:
    def test_load_returns_dataframe(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 5

    def test_required_columns_present(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        for col in ("order_id", "order_date", "amount", "customer_id"):
            assert col in df.columns

    def test_optional_columns_mapped(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        for col in ("sku", "product_name", "quantity"):
            assert col in df.columns

    def test_amount_derived(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        # First row: 12 * 6.95 = 83.4
        assert abs(df["amount"].iloc[0] - 83.4) < 0.01

    def test_negative_quantity_amount(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        # Row 4 (index 3): -2 * 4.95 = -9.9
        assert abs(df["amount"].iloc[3] - (-9.9)) < 0.01

    def test_order_date_is_datetime(self):
        df = load_orders(ONLINE_RETAIL_CSV)
        assert pd.api.types.is_datetime64_any_dtype(df["order_date"])

    def test_amount_not_overwritten(self):
        """When amount already present in CSV, derivation is skipped."""
        df = pd.DataFrame(
            {
                "order_id": ["A1"],
                "order_date": ["2024-01-01"],
                "amount": [100.0],
                "customer_id": ["C1"],
                "quantity": [10],
                "item_price": [5.0],
            }
        )
        df = _normalise_generic_orders(df)
        assert df["amount"].iloc[0] == 100.0

    def test_fuzzy_does_not_overwrite_tier1(self):
        """Tier 1 mapped columns should not be re-consumed by fuzzy mapper."""
        df = pd.DataFrame(
            {
                "Invoice": ["A1"],
                "order_date": ["2024-01-01"],
                "amount": [50.0],
                "customer_id": ["C1"],
            }
        )
        df, mapped = _auto_map_columns(df)
        assert mapped.get("Invoice") == "order_id"
        # Fuzzy should not remap order_id to something else
        df2, fuzzy_mapped = _fuzzy_map_columns(df, already_mapped=mapped)
        assert "order_id" in df2.columns
```

## File: `tests/test_metrics.py`
```python
"""Tests for claude_ecom.metrics."""

import os

import pandas as pd
import pytest

from claude_ecom.loader import load_orders
from claude_ecom.metrics import (
    compute_cohort_kpis,
    compute_revenue_kpis,
)

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES, "sample_orders.csv")


@pytest.fixture
def orders():
    return load_orders(ORDERS_CSV)


class TestRevenueKPIs:
    def test_returns_dict(self, orders):
        kpis = compute_revenue_kpis(orders)
        assert isinstance(kpis, dict)

    def test_total_revenue_positive(self, orders):
        kpis = compute_revenue_kpis(orders)
        assert kpis["total_revenue"] > 0

    def test_aov_positive(self, orders):
        kpis = compute_revenue_kpis(orders)
        assert kpis["aov"] > 0

    def test_repeat_revenue_share_bounded(self, orders):
        kpis = compute_revenue_kpis(orders)
        assert 0 <= kpis["repeat_revenue_share"] <= 1

    def test_discount_rate_bounded(self, orders):
        kpis = compute_revenue_kpis(orders)
        assert 0 <= kpis["avg_discount_rate"] <= 1


class TestCohortKPIs:
    def test_returns_dict(self, orders):
        kpis = compute_cohort_kpis(orders)
        assert isinstance(kpis, dict)

    def test_repeat_purchase_rate_bounded(self, orders):
        kpis = compute_cohort_kpis(orders)
        assert 0 <= kpis["repeat_purchase_rate"] <= 1

    def test_total_customers_positive(self, orders):
        kpis = compute_cohort_kpis(orders)
        assert kpis["total_customers"] > 0


class TestPartialMonthMetrics:
    """Tests for partial last month detection in compute_revenue_kpis."""

    def _make_full_month_orders(self, year, month, days_count, daily_amount=1000.0):
        rows = []
        for i in range(days_count):
            d = pd.Timestamp(year, month, 1) + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-{year}{month:02d}-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i}",
                    "amount": daily_amount,
                }
            )
        return rows

    def test_detects_partial_last_month(self):
        """3 days in January should be flagged as partial."""
        rows = self._make_full_month_orders(2025, 11, 30)
        rows += self._make_full_month_orders(2025, 12, 31)
        # Only 3 days in Jan
        for i in range(3):
            d = pd.Timestamp("2026-01-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-jan-{i}",
                    "order_date": d,
                    "customer_id": f"C-jan-{i}",
                    "amount": 100.0,
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        kpis = compute_revenue_kpis(df)
        assert kpis["partial_last_month"] is True
        assert kpis["partial_last_month_days"] == 3
        assert kpis["partial_last_month_label"] == "2026-01"

    def test_full_month_not_partial(self):
        """A full month should not be flagged as partial."""
        rows = self._make_full_month_orders(2025, 11, 30)
        rows += self._make_full_month_orders(2025, 12, 31)
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        kpis = compute_revenue_kpis(df)
        assert kpis["partial_last_month"] is False

    def test_mom_uses_complete_months(self):
        """MoM should be computed from complete months when last is partial."""
        rows = self._make_full_month_orders(2025, 11, 30, daily_amount=1000.0)
        rows += self._make_full_month_orders(2025, 12, 31, daily_amount=1100.0)
        # 3 days in Jan (partial)
        for i in range(3):
            d = pd.Timestamp("2026-01-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-jan-{i}",
                    "order_date": d,
                    "customer_id": f"C-jan-{i}",
                    "amount": 50.0,
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        kpis = compute_revenue_kpis(df)
        # MoM should be Dec vs Nov (~10% growth), not Jan(150) vs Dec(34100)
        mom = kpis["mom_growth_latest"]
        assert mom > 0, "MoM should be positive (Dec > Nov)"
        assert mom < 0.5, f"MoM {mom:.1%} is too high, likely comparing wrong months"
```

## File: `tests/test_na_handling.py`
```python
"""Tests for N/A handling across scoring, metrics, and checks."""

import math

import pandas as pd

from claude_ecom.checks import (
    CheckResult,
    estimate_revenue_impact,
)


class TestNAImpactEstimation:
    def test_na_checks_skipped_in_impact(self):
        checks = [
            CheckResult("monthly_revenue_trend", "revenue", "high", "na"),
            CheckResult("test_check_r02", "revenue", "critical", "fail"),
        ]
        impacts = estimate_revenue_impact(checks, 1_000_000)
        assert "monthly_revenue_trend" not in impacts
        assert "test_check_r02" in impacts

    def test_zero_revenue_returns_empty(self):
        checks = [
            CheckResult("monthly_revenue_trend", "revenue", "critical", "fail"),
        ]
        impacts = estimate_revenue_impact(checks, 0)
        assert len(impacts) == 0

    def test_negative_revenue_returns_empty(self):
        checks = [
            CheckResult("monthly_revenue_trend", "revenue", "critical", "fail"),
        ]
        impacts = estimate_revenue_impact(checks, -100)
        assert len(impacts) == 0


class TestNAMetrics:
    def _make_orders(self, months=1):
        """Create minimal order DataFrame spanning given months."""
        dates = []
        for m in range(months):
            dates.extend(
                [
                    f"2024-{m + 1:02d}-01",
                    f"2024-{m + 1:02d}-15",
                ]
            )
        n = len(dates)
        return pd.DataFrame(
            {
                "order_id": [f"ORD-{i}" for i in range(n)],
                "order_date": pd.to_datetime(dates),
                "amount": [100.0] * n,
                "customer_id": [f"CUST-{i}" for i in range(n)],
            }
        )

    def test_single_month_mom_is_nan(self):
        from claude_ecom.metrics import compute_revenue_kpis

        orders = self._make_orders(months=1)
        kpis = compute_revenue_kpis(orders)
        assert math.isnan(kpis["mom_growth_latest"])

    def test_two_months_mom_is_valid(self):
        """With sparse data (2 days per month), the last month is partial.

        Need 3 months so partial-month logic can compare the two earlier
        (both sparse but complete-enough relative to each other).
        """
        from claude_ecom.metrics import compute_revenue_kpis

        orders = self._make_orders(months=3)
        kpis = compute_revenue_kpis(orders)
        assert not math.isnan(kpis["mom_growth_latest"])


class TestNAChecks:
    def _make_orders(self, months=1, with_discount=False):
        dates = []
        for m in range(months):
            dates.extend(
                [
                    f"2024-{m + 1:02d}-01",
                    f"2024-{m + 1:02d}-15",
                ]
            )
        n = len(dates)
        data = {
            "order_id": [f"ORD-{i}" for i in range(n)],
            "order_date": pd.to_datetime(dates),
            "amount": [100.0] * n,
            "customer_id": [f"CUST-{i % max(1, n // 2)}" for i in range(n)],
            "product_name": [f"PROD-{i % 3}" for i in range(n)],
        }
        if with_discount:
            data["discount"] = [5.0] * n
        return pd.DataFrame(data)

    def test_single_month_r01_is_na(self):
        from claude_ecom.metrics import compute_cohort_kpis, compute_revenue_kpis

        orders = self._make_orders(months=1)
        rev_kpis = compute_revenue_kpis(orders)
        cohort_kpis = compute_cohort_kpis(orders)

        from claude_ecom.review_engine import _build_checks

        checks = _build_checks(rev_kpis, cohort_kpis, orders)
        r01 = next(c for c in checks if c.check_id == "monthly_revenue_trend")
        assert r01.result == "na"

    def test_no_discount_r08_is_na(self):
        from claude_ecom.metrics import compute_cohort_kpis, compute_revenue_kpis

        orders = self._make_orders(months=2, with_discount=False)
        rev_kpis = compute_revenue_kpis(orders)
        cohort_kpis = compute_cohort_kpis(orders)

        from claude_ecom.review_engine import _build_checks

        checks = _build_checks(rev_kpis, cohort_kpis, orders)
        r08 = next(c for c in checks if c.check_id == "avg_discount_rate_trend")
        assert r08.result == "na"


class TestNumpyNaNRegression:
    """Regression test: numpy NaN types must not slip through isinstance(float) checks."""

    def test_numpy_nan_mom_gives_na_result(self):
        import numpy as np

        from claude_ecom.metrics import compute_cohort_kpis, compute_revenue_kpis
        from claude_ecom.review_engine import _build_checks

        orders = pd.DataFrame(
            {
                "order_id": ["ORD-1", "ORD-2"],
                "order_date": pd.to_datetime(["2024-01-01", "2024-01-15"]),
                "amount": [100.0, 200.0],
                "customer_id": ["C1", "C2"],
            }
        )
        rev_kpis = compute_revenue_kpis(orders)
        # Inject numpy NaN (the bug scenario)
        rev_kpis["mom_growth_latest"] = np.nan
        cohort_kpis = compute_cohort_kpis(orders)

        checks = _build_checks(rev_kpis, cohort_kpis, orders)
        r01 = next(c for c in checks if c.check_id == "monthly_revenue_trend")
        assert r01.result == "na", f"Expected 'na' but got '{r01.result}'"


class TestFuzzyColumnMapping:
    def test_token_similarity(self):
        from claude_ecom.loader import _token_similarity

        assert _token_similarity("order_id", "order id") == 1.0
        assert _token_similarity("order_id", "something else") == 0.0
        assert _token_similarity("purchase date", "date") > 0

    def test_fuzzy_map_finds_similar_columns(self):
        from claude_ecom.loader import _fuzzy_map_columns

        df = pd.DataFrame(
            {
                "Order Number": ["1", "2"],
                "Purchase Date": ["2024-01-01", "2024-01-02"],
                "Total Amount": [100, 200],
                "Buyer ID": ["A", "B"],
            }
        )
        # First apply exact mapping (which should find some)
        from claude_ecom.loader import _auto_map_columns

        df, exact = _auto_map_columns(df)
        # Then try fuzzy for remaining
        df, fuzzy = _fuzzy_map_columns(df)
        # After both tiers, required columns should be present
        mapped_cols = set(df.columns)
        # At least some of the required columns should be mapped
        assert "order_id" in mapped_cols or "order_date" in mapped_cols or len(exact) + len(fuzzy) > 0
```

## File: `tests/test_periods.py`
```python
"""Tests for calendar period utilities."""

from datetime import date

import pandas as pd

from claude_ecom.periods import (
    compute_data_coverage,
    prior_trailing_window,
    trailing_window,
)


class TestTrailingWindow:
    def test_30_day(self):
        p = trailing_window(date(2026, 3, 15), 30)
        assert p.start == date(2026, 2, 14)
        assert p.end == date(2026, 3, 15)
        assert p.label == "Past 30 Days"

    def test_90_day(self):
        p = trailing_window(date(2026, 3, 15), 90)
        assert p.start == date(2025, 12, 16)
        assert p.end == date(2026, 3, 15)
        assert p.label == "Past 90 Days"


class TestComputeDataCoverage:
    def test_short_data_only_30d(self):
        df = pd.DataFrame(
            {
                "order_date": pd.to_datetime(["2025-06-01", "2025-08-01"]),
            }
        )
        cov = compute_data_coverage(df)
        assert cov["30d"] is True  # 61 days >= 45
        assert cov["90d"] is False  # 61 days < 120
        assert cov["365d"] is False

    def test_medium_data_30d_90d(self):
        df = pd.DataFrame(
            {
                "order_date": pd.to_datetime(["2025-01-01", "2025-06-01"]),
            }
        )
        cov = compute_data_coverage(df)
        assert cov["30d"] is True
        assert cov["90d"] is True  # 151 days >= 120
        assert cov["365d"] is False

    def test_long_data_all_periods(self):
        df = pd.DataFrame(
            {
                "order_date": pd.to_datetime(["2024-01-01", "2025-06-01"]),
            }
        )
        cov = compute_data_coverage(df)
        assert cov["30d"] is True
        assert cov["90d"] is True
        assert cov["365d"] is True  # 517 days >= 400

    def test_very_short_data_none(self):
        df = pd.DataFrame(
            {
                "order_date": pd.to_datetime(["2025-06-01", "2025-06-30"]),
            }
        )
        cov = compute_data_coverage(df)
        assert cov["30d"] is False  # 29 days < 45
        assert cov["90d"] is False
        assert cov["365d"] is False


class TestPriorTrailingWindow:
    def test_30_day_prior(self):
        p = prior_trailing_window(date(2026, 3, 15), 30)
        # Current window: [2026-02-14, 2026-03-15]
        # Prior window: [2026-01-15, 2026-02-13]
        assert p.end == date(2026, 2, 13)
        assert p.start == date(2026, 1, 15)
        assert p.label == "Prior 30 Days"

    def test_90_day_prior(self):
        p = prior_trailing_window(date(2026, 3, 15), 90)
        # Current window: [2025-12-16, 2026-03-15]
        # Prior window: [2025-09-17, 2025-12-15]
        assert p.end == date(2025, 12, 15)
        assert p.start == date(2025, 9, 17)
        assert p.label == "Prior 90 Days"

    def test_windows_dont_overlap(self):
        ref = date(2026, 3, 15)
        current = trailing_window(ref, 30)
        prior = prior_trailing_window(ref, 30)
        assert prior.end < current.start
```

## File: `tests/test_report.py`
```python
"""Tests for report generation."""

import json
import os

import pytest

from claude_ecom.loader import load_orders
from claude_ecom.report import (
    _sanitize_for_json,
    generate_review_json,
    review_json_filename,
    review_md_filename,
)
from claude_ecom.review_engine import build_review_data

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES_DIR, "sample_orders.csv")


@pytest.fixture
def orders():
    return load_orders(ORDERS_CSV)


@pytest.mark.parametrize(
    "period,expected",
    [
        (None, "review.json"),
        ("30d", "review_30d.json"),
        ("90d", "review_90d.json"),
        ("365d", "review_365d.json"),
    ],
)
def test_review_json_filename(period, expected):
    assert review_json_filename(period) == expected


@pytest.mark.parametrize(
    "period,expected",
    [
        (None, "REVIEW.md"),
        ("30d", "REVIEW_30D.md"),
        ("90d", "REVIEW_90D.md"),
        ("365d", "REVIEW_365D.md"),
    ],
)
def test_review_md_filename(period, expected):
    assert review_md_filename(period) == expected


class TestGenerateReviewJson:
    def test_creates_file(self, orders, tmp_path):
        data = build_review_data(orders)
        path = generate_review_json(data, output_dir=str(tmp_path))
        assert os.path.exists(path)
        assert path.endswith("review.json")

    def test_valid_json(self, orders, tmp_path):
        data = build_review_data(orders)
        path = generate_review_json(data, output_dir=str(tmp_path))
        with open(path) as f:
            parsed = json.load(f)
        assert "version" in parsed
        assert "metadata" in parsed
        assert "data_coverage" in parsed
        assert "periods" in parsed
        assert "health" in parsed
        assert "action_candidates" in parsed

    def test_health_structure(self, orders, tmp_path):
        data = build_review_data(orders)
        path = generate_review_json(data, output_dir=str(tmp_path))
        with open(path) as f:
            parsed = json.load(f)
        health = parsed["health"]
        assert "checks" in health
        assert "top_issues" in health

    def test_no_nan_in_output(self, orders, tmp_path):
        data = build_review_data(orders)
        path = generate_review_json(data, output_dir=str(tmp_path))
        content = open(path).read()
        assert "NaN" not in content
        assert "Infinity" not in content

    @pytest.mark.parametrize(
        "period,expected",
        [
            (None, "review.json"),
            ("30d", "review_30d.json"),
            ("90d", "review_90d.json"),
            ("365d", "review_365d.json"),
        ],
    )
    def test_filename_by_period(self, orders, tmp_path, period, expected):
        from pathlib import Path

        data = build_review_data(orders)
        path = generate_review_json(data, output_dir=str(tmp_path), period=period)
        assert Path(path).name == expected
        assert os.path.exists(path)


class TestSanitizeForJson:
    def test_replaces_nan(self):
        result = _sanitize_for_json({"a": float("nan")})
        assert result["a"] is None

    def test_replaces_infinity(self):
        result = _sanitize_for_json({"a": float("inf")})
        assert result["a"] is None

    def test_preserves_normal_values(self):
        result = _sanitize_for_json({"a": 42, "b": "hello", "c": 3.14})
        assert result == {"a": 42, "b": "hello", "c": 3.14}

    def test_handles_nested(self):
        result = _sanitize_for_json({"a": {"b": float("nan")}, "c": [float("inf"), 1]})
        assert result["a"]["b"] is None
        assert result["c"][0] is None
        assert result["c"][1] == 1
```

## File: `tests/test_review_e2e.py`
```python
"""End-to-end tests for the review CLI pipeline.

Verifies: CSV input -> KPI computation -> scoring -> review.json generation.
"""

import json
import os

from click.testing import CliRunner

from claude_ecom.cli import cli

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES_DIR, "sample_orders.csv")


class TestReviewBasic:
    """Basic review with orders-only CSV."""

    def test_exit_code_zero(self, tmp_path):
        runner = CliRunner()
        result = runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        assert result.exit_code == 0, f"Review failed:\n{result.output}"

    def test_generates_review_json(self, tmp_path):
        runner = CliRunner()
        runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        assert (tmp_path / "review.json").exists(), "Missing review.json"

    def test_review_json_is_valid(self, tmp_path):
        runner = CliRunner()
        runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        data = json.loads((tmp_path / "review.json").read_text())
        assert "health" in data
        assert "checks" in data["health"]
        assert isinstance(data["health"]["checks"], list)


class TestReviewNoData:
    """Edge case: missing required arg."""

    def test_no_orders_path_errors(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["review"])
        assert result.exit_code != 0


class TestReviewJsonNoNaN:
    """Ensure review.json never contains NaN -- breaks JSON parsing."""

    def test_no_nan_with_minimal_data(self, tmp_path):
        runner = CliRunner()
        runner.invoke(cli, ["review", ORDERS_CSV, "--output", str(tmp_path)])
        content = (tmp_path / "review.json").read_text()
        assert "NaN" not in content
        assert "Infinity" not in content
```

## File: `tests/test_review_engine.py`
```python
"""Tests for the unified business review engine."""

import os
from datetime import date

import pandas as pd
import pytest

from claude_ecom.loader import load_orders
from claude_ecom.periods import PeriodRange
from claude_ecom.review_engine import (
    _compute_drivers,
    _compute_monthly_trend,
    build_review_data,
    compute_period_comparison,
    compute_period_summary,
)

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES_DIR, "sample_orders.csv")


@pytest.fixture
def orders():
    return load_orders(ORDERS_CSV)


class TestComputePeriodSummary:
    def test_returns_expected_keys(self, orders):
        period = PeriodRange("June 2025", date(2025, 6, 1), date(2025, 6, 30))
        result = compute_period_summary(orders, period)
        expected_keys = {
            "revenue",
            "orders",
            "aov",
            "customers",
            "new_customers",
            "returning_customers",
            "new_customer_revenue",
            "returning_customer_revenue",
            "new_customer_aov",
            "returning_customer_aov",
            "avg_discount_rate",
        }
        assert expected_keys == set(result.keys())

    def test_filters_to_period(self, orders):
        period = PeriodRange("June 2025", date(2025, 6, 1), date(2025, 6, 30))
        result = compute_period_summary(orders, period)
        assert result["revenue"] >= 0
        assert result["orders"] >= 0

    def test_new_vs_returning_split(self, orders):
        period = PeriodRange("June 2025", date(2025, 6, 1), date(2025, 6, 30))
        result = compute_period_summary(orders, period)
        assert result["new_customers"] + result["returning_customers"] == result["customers"]
        assert abs(result["new_customer_revenue"] + result["returning_customer_revenue"] - result["revenue"]) < 0.01

    def test_empty_period_returns_zeros(self, orders):
        period = PeriodRange("Jan 2020", date(2020, 1, 1), date(2020, 1, 31))
        result = compute_period_summary(orders, period)
        assert result["revenue"] == 0.0
        assert result["orders"] == 0
        assert result["customers"] == 0

    def test_has_segment_aov(self, orders):
        period = PeriodRange("June 2025", date(2025, 6, 1), date(2025, 6, 30))
        result = compute_period_summary(orders, period)
        assert "new_customer_aov" in result
        assert "returning_customer_aov" in result


class TestComputePeriodComparison:
    def test_positive_change(self):
        current = {"revenue": 120.0, "orders": 12}
        previous = {"revenue": 100.0, "orders": 10}
        delta = compute_period_comparison(current, previous)
        assert abs(delta["revenue"] - 0.20) < 0.001
        assert abs(delta["orders"] - 0.20) < 0.001

    def test_negative_change(self):
        current = {"revenue": 80.0}
        previous = {"revenue": 100.0}
        delta = compute_period_comparison(current, previous)
        assert abs(delta["revenue"] - (-0.20)) < 0.001

    def test_zero_previous(self):
        current = {"revenue": 100.0}
        previous = {"revenue": 0.0}
        delta = compute_period_comparison(current, previous)
        assert delta["revenue"] == float("inf")


class TestBuildReviewData:
    def test_has_required_top_level_keys(self, orders):
        data = build_review_data(orders)
        assert "version" in data
        assert "metadata" in data
        assert "data_coverage" in data
        assert "periods" in data
        assert "health" in data
        assert "action_candidates" in data

    def test_metadata_fields(self, orders):
        data = build_review_data(orders)
        md = data["metadata"]
        assert "generated_at" in md
        assert "data_start" in md
        assert "data_end" in md
        assert "total_orders" in md
        assert "total_customers" in md
        assert "total_revenue" in md

    def test_data_coverage_has_three_periods(self, orders):
        data = build_review_data(orders)
        cov = data["data_coverage"]
        assert "30d" in cov
        assert "90d" in cov
        assert "365d" in cov

    def test_period_blocks_have_expected_structure(self, orders):
        data = build_review_data(orders)
        for period_key, block in data["periods"].items():
            assert "summary" in block
            assert "kpi_tree" in block
            assert "drivers" in block
            summary = block["summary"]
            assert "revenue" in summary
            assert "revenue_change" in summary
            assert "orders" in summary
            assert "aov" in summary

    def test_health_has_checks(self, orders):
        data = build_review_data(orders)
        health = data["health"]
        assert "checks" in health
        assert "top_issues" in health
        assert isinstance(health["checks"], list)
        assert len(health["checks"]) > 0

    def test_specific_period_filter(self, orders):
        data = build_review_data(orders, period="30d")
        cov = data["data_coverage"]
        if cov["30d"]:
            assert "30d" in data["periods"]
            # Should not have other periods when specific period requested
            assert len(data["periods"]) <= 1

    def test_action_candidates_structure(self, orders):
        data = build_review_data(orders)
        for action in data["action_candidates"]:
            assert "action" in action
            assert "source_check" in action
            assert "severity" in action
            assert "timeline" in action

    def test_top_issues_max_10(self, orders):
        data = build_review_data(orders)
        assert len(data["health"]["top_issues"]) <= 10


class TestComputeDrivers:
    def test_basic_decomposition(self):
        current = {"revenue": 1200, "orders": 12, "aov": 100}
        prior = {"revenue": 1000, "orders": 10, "aov": 100}
        drivers = _compute_drivers(current, prior)
        assert drivers["volume_effect"] == 200.0  # 2 extra orders * 100 AOV
        assert drivers["aov_effect"] == 0.0

    def test_zero_prior_revenue(self):
        current = {"revenue": 1000, "orders": 10, "aov": 100}
        prior = {"revenue": 0, "orders": 0, "aov": 0}
        drivers = _compute_drivers(current, prior)
        assert drivers["volume_effect"] == 0
        assert drivers["aov_effect"] == 0
        assert drivers["mix_effect"] == 0


class TestMonthlyTrend:
    def test_returns_only_data_months(self, orders):
        ref = orders["order_date"].max().date()
        trend = _compute_monthly_trend(orders, ref, days=365)
        # Should not have months with zero data
        for entry in trend:
            assert entry["orders"] > 0 or entry["revenue"] > 0

    def test_no_future_months_with_zero(self, orders):
        ref = orders["order_date"].max().date()
        trend = _compute_monthly_trend(orders, ref, days=365)
        for entry in trend:
            assert entry["revenue"] > 0 or entry["orders"] > 0, f"Month {entry['month']} has zero data but was included"

    def test_trailing_window_bounds(self, orders):
        ref = orders["order_date"].max().date()
        trend = _compute_monthly_trend(orders, ref, days=365)
        from datetime import timedelta

        window_start = ref - timedelta(days=364)
        for entry in trend:
            year, month = map(int, entry["month"].split("-"))
            # Month must overlap with [window_start, ref]
            assert date(year, month, 1) <= ref
            import calendar

            last_day = calendar.monthrange(year, month)[1]
            assert date(year, month, last_day) >= window_start

    def test_each_entry_has_keys(self, orders):
        ref = orders["order_date"].max().date()
        trend = _compute_monthly_trend(orders, ref, days=365)
        for entry in trend:
            assert "month" in entry
            assert "revenue" in entry
            assert "orders" in entry
            assert "aov" in entry
            assert "customers" in entry
            assert "new_customers" in entry
            assert "returning_customers" in entry
            assert "days_with_data" in entry

    def test_partial_flag_on_short_month(self):
        """A month with only 3 days of data should have partial=True."""
        dates = pd.date_range("2025-12-01", "2025-12-31", freq="D")
        rows = []
        for i, d in enumerate(dates):
            rows.append(
                {
                    "order_id": f"O-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i}",
                    "amount": 100.0,
                }
            )
        # Add 3 days in Jan 2026
        for i in range(3):
            d = pd.Timestamp("2026-01-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-jan-{i}",
                    "order_date": d,
                    "customer_id": f"C-jan-{i}",
                    "amount": 100.0,
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])

        trend = _compute_monthly_trend(df, date(2026, 1, 3), days=365)
        jan_entry = [e for e in trend if e["month"] == "2026-01"]
        assert len(jan_entry) == 1
        assert jan_entry[0].get("partial") is True
        assert jan_entry[0]["days_with_data"] == 3


class TestPartialMonth:
    """Tests that partial last month does not cause false-positive MoM checks."""

    def _make_orders_with_partial_month(self):
        """Create orders: full Dec + 3 days of Jan."""
        rows = []
        # Full December
        for i in range(31):
            d = pd.Timestamp("2025-12-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-dec-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i}",
                    "amount": 1000.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        # Full November
        for i in range(30):
            d = pd.Timestamp("2025-11-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-nov-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i}",
                    "amount": 1000.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        # 3 days of January (partial)
        for i in range(3):
            d = pd.Timestamp("2026-01-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-jan-{i}",
                    "order_date": d,
                    "customer_id": f"C-jan-{i}",
                    "amount": 100.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        return df

    def test_mom_not_false_negative(self):
        """MoM should not report -87.8% from 3 days vs full month."""
        from claude_ecom.metrics import compute_revenue_kpis

        orders = self._make_orders_with_partial_month()
        kpis = compute_revenue_kpis(orders)
        assert kpis["partial_last_month"] is True
        # MoM should compare Nov vs Dec (both full), not Jan(partial) vs Dec
        mom = kpis["mom_growth_latest"]
        # Nov and Dec have similar revenue, so MoM should be close to 0
        assert abs(mom) < 0.2, f"MoM {mom:.1%} looks like a partial-month false positive"

    def test_r01_check_has_partial_note(self):
        """R01 check message should note partial month exclusion."""
        from claude_ecom.metrics import compute_cohort_kpis, compute_revenue_kpis

        orders = self._make_orders_with_partial_month()
        rev_kpis = compute_revenue_kpis(orders)
        cohort_kpis = compute_cohort_kpis(orders)
        from claude_ecom.review_engine import _build_checks

        checks = _build_checks(rev_kpis, cohort_kpis, orders)
        r01 = [c for c in checks if c.check_id == "monthly_revenue_trend"][0]
        assert "partial month excluded" in r01.message


class TestDataQuality:
    def test_data_quality_in_review_json(self, orders):
        data = build_review_data(orders)
        assert "data_quality" in data
        assert isinstance(data["data_quality"], list)

    def test_short_data_warns(self):
        """Fewer than 90 days of data should produce a short_data_span warning."""
        rows = []
        for i in range(30):
            d = pd.Timestamp("2025-12-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i}",
                    "amount": 100.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        data = build_review_data(df)
        types = [w["type"] for w in data["data_quality"]]
        assert "short_data_span" in types

    def test_partial_month_warning(self):
        """Partial last month should produce a partial_period warning."""
        rows = []
        # Full November + December
        for i in range(61):
            d = pd.Timestamp("2025-11-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-{i}",
                    "order_date": d,
                    "customer_id": f"C-{i % 20}",
                    "amount": 100.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        # 3 days of January (partial)
        for i in range(3):
            d = pd.Timestamp("2026-01-01") + pd.Timedelta(days=i)
            rows.append(
                {
                    "order_id": f"O-jan-{i}",
                    "order_date": d,
                    "customer_id": f"C-jan-{i}",
                    "amount": 100.0,
                    "sku": "SKU-1",
                    "product_name": "P1",
                }
            )
        df = pd.DataFrame(rows)
        df["order_date"] = pd.to_datetime(df["order_date"])
        data = build_review_data(df)
        types = [w["type"] for w in data["data_quality"]]
        assert "partial_period" in types


class TestMonthlyTrendIn365dBlock:
    def test_365d_has_monthly_trend(self, orders):
        data = build_review_data(orders)
        if data["data_coverage"]["365d"] and "365d" in data["periods"]:
            assert "monthly_trend" in data["periods"]["365d"]
            trend = data["periods"]["365d"]["monthly_trend"]
            # All entries should have data
            for entry in trend:
                assert entry["orders"] > 0 or entry["revenue"] > 0
```

## File: `tests/test_review_json_schema.py`
```python
"""Tests for review.json schema stability.

review.json is the contract between the Python compute engine and the LLM
interpretation layer. If the schema breaks, the LLM cannot interpret results.
"""

import json
import math
import os

import pytest

from claude_ecom.loader import load_orders
from claude_ecom.review_engine import build_review_data

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
ORDERS_CSV = os.path.join(FIXTURES_DIR, "sample_orders.csv")


@pytest.fixture
def review_data():
    orders = load_orders(ORDERS_CSV)
    return build_review_data(orders)


class TestReviewJsonTopLevel:
    """Top-level fields that the LLM reads first."""

    def test_has_required_top_level_fields(self, review_data):
        required = {"version", "metadata", "data_coverage", "periods", "health", "action_candidates"}
        assert required.issubset(set(review_data.keys()))


class TestReviewJsonHealth:
    """Health section schema."""

    def test_checks_is_list(self, review_data):
        checks = review_data["health"]["checks"]
        assert isinstance(checks, list)
        assert len(checks) > 0

    def test_each_check_has_required_fields(self, review_data):
        required = {"id", "category", "severity", "result", "message"}
        for check in review_data["health"]["checks"]:
            missing = required - set(check.keys())
            assert not missing, f"Check {check.get('id', '?')} missing: {missing}"

    def test_result_values_include_watch(self, review_data):
        valid_results = {"pass", "watch", "warning", "fail", "na"}
        for check in review_data["health"]["checks"]:
            assert check["result"] in valid_results, f"{check['id']} invalid result: {check['result']}"


class TestReviewJsonNoNaN:
    """Ensure review data never contains NaN -- breaks JSON parsing."""

    def _check_no_nan(self, obj, path=""):
        if isinstance(obj, float):
            assert not math.isnan(obj), f"NaN at {path}"
            assert not math.isinf(obj), f"Infinity at {path}"
        elif isinstance(obj, dict):
            for k, v in obj.items():
                self._check_no_nan(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                self._check_no_nan(v, f"{path}[{i}]")

    def test_no_nan_or_infinity(self, review_data):
        from claude_ecom.report import _sanitize_for_json

        sanitized = _sanitize_for_json(review_data)
        self._check_no_nan(sanitized)

    def test_json_serializable(self, review_data):
        from claude_ecom.report import _sanitize_for_json

        sanitized = _sanitize_for_json(review_data)
        content = json.dumps(sanitized, default=str)
        assert "NaN" not in content
        assert "Infinity" not in content
```

## File: `tests/fixtures/online_retail_sample.csv`
```
Invoice,StockCode,Description,Quantity,InvoiceDate,Price,Customer ID,Country
489434,85048,15CM CHRISTMAS GLASS BALL 20 LIGHTS,12,12/1/2009 7:45,6.95,13085,United Kingdom
489434,79323P,PINK CHERRY LIGHTS,12,12/1/2009 7:45,6.75,13085,United Kingdom
489434,79323W,WHITE CHERRY LIGHTS,12,12/1/2009 7:45,6.75,13085,United Kingdom
C489435,22180,RETROSPOT LAMP,-2,12/1/2009 8:00,4.95,13085,United Kingdom
489436,22633,HAND WARMER UNION JACK,6,12/1/2009 8:15,1.85,17850,United Kingdom
```

## File: `tests/fixtures/sample_orders.csv`
```
order_id,order_date,customer_id,sku,product_name,category,quantity,item_price,amount,discount,cost,channel,device,city
ORD-00001,2025-01-13,cust_0082,SKU-008,Product SKU-008,Home,1,22376.0,22376.0,0.0,7649.0,organic,tablet,Sapporo
ORD-00002,2025-08-05,cust_0012,SKU-038,Product SKU-038,Home,1,1438.0,1438.0,0.0,532.0,direct,mobile,Sapporo
ORD-00003,2025-11-29,cust_0026,SKU-046,Product SKU-046,Fashion,2,21189.0,42378.0,0.0,18424.0,email,mobile,Osaka
ORD-00004,2025-06-24,cust_0090,SKU-028,Product SKU-028,Home,1,8697.0,8697.0,1739.0,3487.0,organic,desktop,Tokyo
ORD-00005,2025-11-06,cust_0046,SKU-023,Product SKU-023,Home,1,8303.0,8303.0,1245.0,3635.0,organic,desktop,Tokyo
ORD-00006,2025-11-18,cust_0071,SKU-019,Product SKU-019,Food,2,18746.0,37492.0,3749.0,13410.0,organic,mobile,Osaka
ORD-00007,2025-02-10,cust_0099,SKU-019,Product SKU-019,Food,1,25732.0,25732.0,1287.0,9865.0,email,mobile,Nagoya
ORD-00008,2025-12-10,cust_0046,SKU-014,Product SKU-014,Food,3,8376.0,25128.0,3769.0,8076.0,paid_search,tablet,Osaka
ORD-00009,2025-07-14,cust_0021,SKU-030,Product SKU-030,Electronics,3,8463.0,25389.0,3808.0,11859.0,email,mobile,Osaka
ORD-00010,2025-07-25,cust_0005,SKU-021,Product SKU-021,Fashion,1,8398.0,8398.0,840.0,4727.0,email,mobile,Fukuoka
ORD-00011,2025-08-23,cust_0051,SKU-042,Product SKU-042,Beauty,1,4715.0,4715.0,0.0,2468.0,direct,desktop,Sapporo
ORD-00012,2025-07-24,cust_0055,SKU-038,Product SKU-038,Home,1,11179.0,11179.0,1118.0,5009.0,organic,mobile,Osaka
ORD-00013,2025-12-15,cust_0081,SKU-011,Product SKU-011,Fashion,1,12954.0,12954.0,648.0,5369.0,social,tablet,Nagoya
ORD-00014,2025-12-15,cust_0071,SKU-001,Product SKU-001,Fashion,3,21761.0,65283.0,6528.0,34290.0,email,mobile,Nagoya
ORD-00015,2025-08-21,cust_0056,SKU-011,Product SKU-011,Fashion,3,596.0,1788.0,268.0,678.0,direct,mobile,Sapporo
ORD-00016,2025-06-02,cust_0014,SKU-041,Product SKU-041,Fashion,3,25329.0,75987.0,7599.0,27330.0,email,mobile,Sapporo
ORD-00017,2025-01-01,cust_0100,SKU-034,Product SKU-034,Food,2,18169.0,36338.0,0.0,12120.0,email,desktop,Osaka
ORD-00018,2025-10-18,cust_0008,SKU-016,Product SKU-016,Fashion,1,28435.0,28435.0,4265.0,12676.0,organic,tablet,Osaka
ORD-00019,2025-09-01,cust_0017,SKU-043,Product SKU-043,Home,1,28432.0,28432.0,0.0,13030.0,direct,desktop,Osaka
ORD-00020,2025-12-20,cust_0070,SKU-049,Product SKU-049,Food,2,6434.0,12868.0,643.0,7702.0,email,desktop,Sapporo
ORD-00021,2025-05-07,cust_0058,SKU-008,Product SKU-008,Home,2,7129.0,14258.0,0.0,6794.0,paid_search,tablet,Osaka
ORD-00022,2025-12-29,cust_0001,SKU-005,Product SKU-005,Electronics,1,19118.0,19118.0,0.0,10928.0,email,mobile,Sapporo
ORD-00023,2025-12-09,cust_0031,SKU-018,Product SKU-018,Home,3,14820.0,44460.0,0.0,22986.0,direct,tablet,Fukuoka
ORD-00024,2025-07-28,cust_0032,SKU-031,Product SKU-031,Fashion,1,6117.0,6117.0,918.0,2626.0,social,desktop,Fukuoka
ORD-00025,2025-12-11,cust_0094,SKU-004,Product SKU-004,Food,3,19777.0,59331.0,0.0,18879.0,email,mobile,Osaka
ORD-00026,2025-10-02,cust_0025,SKU-013,Product SKU-013,Home,2,13734.0,27468.0,0.0,10536.0,paid_search,mobile,Fukuoka
ORD-00027,2025-01-26,cust_0071,SKU-007,Product SKU-007,Beauty,3,19738.0,59214.0,11843.0,18027.0,organic,mobile,Osaka
ORD-00028,2025-09-04,cust_0053,SKU-032,Product SKU-032,Beauty,2,6806.0,13612.0,0.0,4756.0,organic,desktop,Nagoya
ORD-00029,2025-08-05,cust_0059,SKU-019,Product SKU-019,Food,3,21049.0,63147.0,12629.0,29472.0,social,mobile,Osaka
ORD-00030,2025-01-30,cust_0038,SKU-014,Product SKU-014,Food,3,17586.0,52758.0,0.0,27666.0,organic,mobile,Sapporo
ORD-00031,2025-09-29,cust_0062,SKU-033,Product SKU-033,Home,3,5144.0,15432.0,0.0,8571.0,organic,tablet,Tokyo
ORD-00032,2025-07-26,cust_0087,SKU-016,Product SKU-016,Fashion,3,4037.0,12111.0,0.0,5736.0,organic,tablet,Tokyo
ORD-00033,2025-10-26,cust_0054,SKU-043,Product SKU-043,Home,2,17174.0,34348.0,0.0,12410.0,email,mobile,Nagoya
ORD-00034,2025-12-10,cust_0051,SKU-009,Product SKU-009,Food,2,19542.0,39084.0,0.0,22618.0,organic,mobile,Fukuoka
ORD-00035,2025-02-21,cust_0080,SKU-037,Product SKU-037,Beauty,1,2661.0,2661.0,266.0,1010.0,email,mobile,Osaka
ORD-00036,2025-03-22,cust_0048,SKU-019,Product SKU-019,Food,3,13426.0,40278.0,6042.0,15738.0,direct,mobile,Sapporo
ORD-00037,2025-02-23,cust_0039,SKU-043,Product SKU-043,Home,1,28198.0,28198.0,0.0,9436.0,organic,tablet,Sapporo
ORD-00038,2025-05-25,cust_0020,SKU-018,Product SKU-018,Home,3,18342.0,55026.0,0.0,19869.0,email,tablet,Fukuoka
ORD-00039,2025-02-17,cust_0033,SKU-004,Product SKU-004,Food,2,19211.0,38422.0,0.0,11568.0,paid_search,tablet,Nagoya
ORD-00040,2025-08-15,cust_0021,SKU-048,Product SKU-048,Home,2,16775.0,33550.0,3355.0,10162.0,organic,tablet,Osaka
ORD-00041,2025-07-09,cust_0070,SKU-003,Product SKU-003,Home,1,17684.0,17684.0,884.0,5981.0,email,desktop,Tokyo
ORD-00042,2025-12-16,cust_0046,SKU-014,Product SKU-014,Food,1,7861.0,7861.0,0.0,4198.0,social,tablet,Osaka
ORD-00043,2025-04-01,cust_0031,SKU-011,Product SKU-011,Fashion,1,26502.0,26502.0,0.0,13807.0,email,desktop,Osaka
ORD-00044,2025-12-26,cust_0035,SKU-011,Product SKU-011,Fashion,1,3689.0,3689.0,738.0,1628.0,paid_search,desktop,Nagoya
ORD-00045,2025-04-25,cust_0040,SKU-015,Product SKU-015,Electronics,1,1198.0,1198.0,60.0,477.0,organic,desktop,Nagoya
ORD-00046,2025-07-24,cust_0083,SKU-033,Product SKU-033,Home,3,20546.0,61638.0,0.0,35859.0,organic,desktop,Osaka
ORD-00047,2025-01-20,cust_0075,SKU-017,Product SKU-017,Beauty,2,3698.0,7396.0,0.0,3836.0,email,desktop,Sapporo
ORD-00048,2025-07-17,cust_0066,SKU-008,Product SKU-008,Home,1,27035.0,27035.0,0.0,8470.0,social,mobile,Sapporo
ORD-00049,2025-12-10,cust_0069,SKU-044,Product SKU-044,Food,2,6313.0,12626.0,0.0,7382.0,email,tablet,Nagoya
ORD-00050,2025-06-03,cust_0085,SKU-008,Product SKU-008,Home,3,15460.0,46380.0,2319.0,18453.0,email,tablet,Osaka
ORD-00051,2025-12-07,cust_0025,SKU-027,Product SKU-027,Beauty,3,28241.0,84723.0,12708.0,48363.0,direct,tablet,Nagoya
ORD-00052,2025-01-01,cust_0052,SKU-036,Product SKU-036,Fashion,1,9464.0,9464.0,473.0,5070.0,direct,tablet,Nagoya
ORD-00053,2025-08-15,cust_0060,SKU-029,Product SKU-029,Food,3,20431.0,61293.0,3065.0,32982.0,paid_search,tablet,Tokyo
ORD-00054,2025-12-06,cust_0037,SKU-033,Product SKU-033,Home,2,19172.0,38344.0,0.0,20918.0,paid_search,tablet,Nagoya
ORD-00055,2025-03-17,cust_0029,SKU-013,Product SKU-013,Home,1,1221.0,1221.0,61.0,590.0,organic,desktop,Fukuoka
ORD-00056,2025-04-10,cust_0081,SKU-037,Product SKU-037,Beauty,2,21691.0,43382.0,2169.0,18216.0,paid_search,tablet,Tokyo
ORD-00057,2025-02-24,cust_0097,SKU-050,Product SKU-050,Electronics,1,23463.0,23463.0,0.0,12699.0,direct,desktop,Tokyo
ORD-00058,2025-03-04,cust_0072,SKU-016,Product SKU-016,Fashion,2,13966.0,27932.0,4190.0,12830.0,direct,tablet,Nagoya
ORD-00059,2025-11-10,cust_0097,SKU-029,Product SKU-029,Food,3,24543.0,73629.0,3681.0,40434.0,direct,desktop,Osaka
ORD-00060,2025-08-19,cust_0096,SKU-031,Product SKU-031,Fashion,1,8146.0,8146.0,1629.0,4002.0,direct,desktop,Osaka
ORD-00061,2025-02-09,cust_0036,SKU-029,Product SKU-029,Food,1,21550.0,21550.0,0.0,8636.0,direct,mobile,Osaka
ORD-00062,2025-07-16,cust_0020,SKU-015,Product SKU-015,Electronics,3,20972.0,62916.0,0.0,20088.0,social,desktop,Sapporo
ORD-00063,2025-02-01,cust_0060,SKU-027,Product SKU-027,Beauty,2,6602.0,13204.0,660.0,7546.0,direct,tablet,Tokyo
ORD-00064,2025-07-14,cust_0098,SKU-037,Product SKU-037,Beauty,2,14571.0,29142.0,0.0,15330.0,social,tablet,Sapporo
ORD-00065,2025-09-07,cust_0078,SKU-015,Product SKU-015,Electronics,2,6973.0,13946.0,697.0,4306.0,email,tablet,Fukuoka
ORD-00066,2025-08-28,cust_0093,SKU-011,Product SKU-011,Fashion,3,27626.0,82878.0,8288.0,25533.0,social,tablet,Sapporo
ORD-00067,2025-02-12,cust_0085,SKU-002,Product SKU-002,Beauty,1,19461.0,19461.0,3892.0,8534.0,organic,desktop,Fukuoka
ORD-00068,2025-08-21,cust_0042,SKU-014,Product SKU-014,Food,2,10142.0,20284.0,0.0,10662.0,social,desktop,Tokyo
ORD-00069,2025-10-04,cust_0061,SKU-002,Product SKU-002,Beauty,2,2037.0,4074.0,0.0,2016.0,organic,mobile,Osaka
ORD-00070,2025-11-15,cust_0026,SKU-002,Product SKU-002,Beauty,1,4995.0,4995.0,250.0,2502.0,direct,mobile,Fukuoka
ORD-00071,2025-07-08,cust_0090,SKU-017,Product SKU-017,Beauty,3,5450.0,16350.0,2452.0,8430.0,paid_search,desktop,Tokyo
ORD-00072,2025-06-09,cust_0075,SKU-002,Product SKU-002,Beauty,2,17486.0,34972.0,1749.0,20370.0,paid_search,mobile,Sapporo
ORD-00073,2025-05-05,cust_0089,SKU-041,Product SKU-041,Fashion,2,3506.0,7012.0,1402.0,3544.0,organic,tablet,Tokyo
ORD-00074,2025-08-08,cust_0045,SKU-035,Product SKU-035,Electronics,1,20015.0,20015.0,2002.0,9893.0,organic,desktop,Fukuoka
ORD-00075,2025-07-05,cust_0014,SKU-028,Product SKU-028,Home,2,19250.0,38500.0,5775.0,13318.0,paid_search,tablet,Sapporo
ORD-00076,2025-11-12,cust_0084,SKU-018,Product SKU-018,Home,3,24342.0,73026.0,14605.0,32499.0,social,tablet,Sapporo
ORD-00077,2025-05-06,cust_0035,SKU-021,Product SKU-021,Fashion,1,25007.0,25007.0,0.0,14116.0,paid_search,desktop,Sapporo
ORD-00078,2025-07-14,cust_0079,SKU-043,Product SKU-043,Home,2,10424.0,20848.0,4170.0,8288.0,social,mobile,Nagoya
ORD-00079,2025-05-24,cust_0034,SKU-022,Product SKU-022,Beauty,3,26469.0,79407.0,0.0,37062.0,direct,mobile,Tokyo
ORD-00080,2025-07-28,cust_0031,SKU-047,Product SKU-047,Beauty,1,14913.0,14913.0,2237.0,6604.0,social,desktop,Tokyo
ORD-00081,2025-04-24,cust_0012,SKU-019,Product SKU-019,Food,1,12430.0,12430.0,0.0,6205.0,email,desktop,Sapporo
ORD-00082,2025-08-06,cust_0068,SKU-023,Product SKU-023,Home,3,29901.0,89703.0,0.0,36378.0,social,desktop,Nagoya
ORD-00083,2025-03-03,cust_0033,SKU-015,Product SKU-015,Electronics,2,21778.0,43556.0,0.0,22774.0,paid_search,mobile,Osaka
ORD-00084,2025-05-22,cust_0095,SKU-031,Product SKU-031,Fashion,3,21875.0,65625.0,6562.0,25260.0,organic,mobile,Nagoya
ORD-00085,2025-04-02,cust_0030,SKU-024,Product SKU-024,Food,3,9417.0,28251.0,2825.0,9549.0,organic,mobile,Sapporo
ORD-00086,2025-03-06,cust_0038,SKU-045,Product SKU-045,Electronics,2,19317.0,38634.0,0.0,21706.0,direct,desktop,Fukuoka
ORD-00087,2025-06-24,cust_0062,SKU-029,Product SKU-029,Food,1,5939.0,5939.0,0.0,3458.0,social,mobile,Tokyo
ORD-00088,2025-02-07,cust_0052,SKU-032,Product SKU-032,Beauty,3,17522.0,52566.0,0.0,18162.0,direct,desktop,Tokyo
ORD-00089,2025-10-13,cust_0032,SKU-008,Product SKU-008,Home,3,23051.0,69153.0,6915.0,37152.0,paid_search,tablet,Fukuoka
ORD-00090,2025-06-02,cust_0058,SKU-029,Product SKU-029,Food,2,25875.0,51750.0,0.0,24352.0,organic,tablet,Tokyo
ORD-00091,2025-11-17,cust_0098,SKU-014,Product SKU-014,Food,3,6725.0,20175.0,0.0,7002.0,paid_search,tablet,Tokyo
ORD-00092,2025-07-29,cust_0021,SKU-001,Product SKU-001,Fashion,3,13790.0,41370.0,2068.0,16026.0,paid_search,desktop,Nagoya
ORD-00093,2025-02-06,cust_0090,SKU-030,Product SKU-030,Electronics,2,20778.0,41556.0,8311.0,22332.0,direct,tablet,Osaka
ORD-00094,2025-10-06,cust_0055,SKU-008,Product SKU-008,Home,1,7132.0,7132.0,0.0,3908.0,organic,mobile,Osaka
ORD-00095,2025-10-19,cust_0040,SKU-039,Product SKU-039,Food,2,27675.0,55350.0,0.0,24388.0,email,tablet,Fukuoka
ORD-00096,2025-10-04,cust_0035,SKU-033,Product SKU-033,Home,1,15067.0,15067.0,1507.0,4700.0,social,tablet,Nagoya
ORD-00097,2025-01-14,cust_0078,SKU-017,Product SKU-017,Beauty,3,3194.0,9582.0,1916.0,5349.0,direct,mobile,Nagoya
ORD-00098,2025-03-31,cust_0074,SKU-003,Product SKU-003,Home,3,14380.0,43140.0,2157.0,24798.0,paid_search,tablet,Fukuoka
ORD-00099,2025-02-16,cust_0082,SKU-032,Product SKU-032,Beauty,2,14365.0,28730.0,0.0,11386.0,organic,mobile,Nagoya
ORD-00100,2025-09-11,cust_0053,SKU-045,Product SKU-045,Electronics,2,9002.0,18004.0,3601.0,9508.0,organic,desktop,Tokyo
ORD-00101,2025-06-15,cust_0041,SKU-017,Product SKU-017,Beauty,2,3920.0,7840.0,1568.0,3562.0,organic,tablet,Sapporo
ORD-00102,2025-01-28,cust_0060,SKU-027,Product SKU-027,Beauty,2,6034.0,12068.0,1207.0,6360.0,social,mobile,Osaka
ORD-00103,2025-03-09,cust_0035,SKU-036,Product SKU-036,Fashion,2,27866.0,55732.0,8360.0,24824.0,organic,tablet,Sapporo
ORD-00104,2025-03-23,cust_0031,SKU-046,Product SKU-046,Fashion,1,9667.0,9667.0,967.0,4083.0,paid_search,mobile,Fukuoka
ORD-00105,2025-03-20,cust_0016,SKU-042,Product SKU-042,Beauty,3,15202.0,45606.0,0.0,20643.0,email,desktop,Fukuoka
ORD-00106,2025-08-22,cust_0061,SKU-016,Product SKU-016,Fashion,2,16762.0,33524.0,0.0,19328.0,direct,tablet,Osaka
ORD-00107,2025-08-01,cust_0009,SKU-018,Product SKU-018,Home,3,10526.0,31578.0,0.0,17247.0,email,tablet,Nagoya
ORD-00108,2025-12-04,cust_0076,SKU-038,Product SKU-038,Home,1,14944.0,14944.0,747.0,6898.0,email,desktop,Sapporo
ORD-00109,2025-07-13,cust_0098,SKU-035,Product SKU-035,Electronics,2,13933.0,27866.0,5573.0,9936.0,paid_search,tablet,Fukuoka
ORD-00110,2025-07-30,cust_0030,SKU-050,Product SKU-050,Electronics,3,1788.0,5364.0,268.0,2745.0,social,desktop,Osaka
ORD-00111,2025-03-06,cust_0064,SKU-003,Product SKU-003,Home,3,15318.0,45954.0,0.0,25776.0,social,mobile,Sapporo
ORD-00112,2025-03-15,cust_0059,SKU-001,Product SKU-001,Fashion,3,12594.0,37782.0,0.0,12183.0,email,desktop,Sapporo
ORD-00113,2025-11-29,cust_0089,SKU-026,Product SKU-026,Fashion,2,2869.0,5738.0,1148.0,2882.0,direct,desktop,Nagoya
ORD-00114,2025-09-07,cust_0081,SKU-046,Product SKU-046,Fashion,1,26235.0,26235.0,2624.0,8409.0,email,mobile,Tokyo
ORD-00115,2025-11-21,cust_0056,SKU-007,Product SKU-007,Beauty,1,21265.0,21265.0,1063.0,7441.0,email,mobile,Tokyo
ORD-00116,2025-05-31,cust_0042,SKU-004,Product SKU-004,Food,2,11075.0,22150.0,0.0,8268.0,social,tablet,Osaka
ORD-00117,2025-02-10,cust_0022,SKU-012,Product SKU-012,Beauty,2,18480.0,36960.0,3696.0,18662.0,social,tablet,Osaka
ORD-00118,2025-11-23,cust_0030,SKU-030,Product SKU-030,Electronics,2,7992.0,15984.0,2398.0,4840.0,social,desktop,Sapporo
ORD-00119,2025-08-15,cust_0021,SKU-005,Product SKU-005,Electronics,3,28384.0,85152.0,0.0,41868.0,social,tablet,Nagoya
ORD-00120,2025-04-12,cust_0059,SKU-020,Product SKU-020,Electronics,2,29982.0,59964.0,0.0,22256.0,direct,desktop,Sapporo
ORD-00121,2025-06-01,cust_0038,SKU-045,Product SKU-045,Electronics,3,1147.0,3441.0,172.0,1317.0,direct,tablet,Tokyo
ORD-00122,2025-09-12,cust_0078,SKU-048,Product SKU-048,Home,2,25069.0,50138.0,10028.0,27058.0,direct,desktop,Osaka
ORD-00123,2025-11-14,cust_0082,SKU-013,Product SKU-013,Home,3,7893.0,23679.0,4736.0,11787.0,paid_search,tablet,Tokyo
ORD-00124,2025-01-21,cust_0081,SKU-042,Product SKU-042,Beauty,2,9614.0,19228.0,0.0,9112.0,paid_search,mobile,Nagoya
ORD-00125,2025-08-01,cust_0042,SKU-048,Product SKU-048,Home,1,5681.0,5681.0,1136.0,2624.0,email,tablet,Sapporo
ORD-00126,2025-05-12,cust_0035,SKU-011,Product SKU-011,Fashion,2,27464.0,54928.0,10986.0,21342.0,email,mobile,Fukuoka
ORD-00127,2025-04-26,cust_0010,SKU-010,Product SKU-010,Electronics,3,25874.0,77622.0,11643.0,46107.0,direct,desktop,Tokyo
ORD-00128,2025-05-16,cust_0051,SKU-001,Product SKU-001,Fashion,2,16329.0,32658.0,0.0,16390.0,email,tablet,Fukuoka
ORD-00129,2025-02-25,cust_0082,SKU-024,Product SKU-024,Food,2,20408.0,40816.0,0.0,19832.0,direct,desktop,Sapporo
ORD-00130,2025-02-02,cust_0029,SKU-042,Product SKU-042,Beauty,2,19244.0,38488.0,5773.0,15036.0,social,mobile,Osaka
ORD-00131,2025-06-05,cust_0006,SKU-003,Product SKU-003,Home,1,29880.0,29880.0,0.0,11069.0,direct,mobile,Fukuoka
ORD-00132,2025-12-10,cust_0059,SKU-024,Product SKU-024,Food,3,28507.0,85521.0,8552.0,36411.0,paid_search,desktop,Tokyo
ORD-00133,2025-07-28,cust_0063,SKU-040,Product SKU-040,Electronics,2,28202.0,56404.0,0.0,28602.0,paid_search,desktop,Fukuoka
ORD-00134,2025-02-20,cust_0031,SKU-024,Product SKU-024,Food,2,29437.0,58874.0,5887.0,33588.0,email,mobile,Fukuoka
ORD-00135,2025-03-04,cust_0036,SKU-013,Product SKU-013,Home,2,28496.0,56992.0,0.0,28430.0,direct,mobile,Tokyo
ORD-00136,2025-03-06,cust_0043,SKU-016,Product SKU-016,Fashion,1,23716.0,23716.0,0.0,13019.0,direct,mobile,Sapporo
ORD-00137,2025-06-18,cust_0028,SKU-015,Product SKU-015,Electronics,3,23344.0,70032.0,0.0,26835.0,paid_search,mobile,Sapporo
ORD-00138,2025-02-26,cust_0033,SKU-012,Product SKU-012,Beauty,1,20001.0,20001.0,0.0,6089.0,paid_search,tablet,Nagoya
ORD-00139,2025-05-16,cust_0003,SKU-012,Product SKU-012,Beauty,3,2046.0,6138.0,307.0,2811.0,organic,desktop,Fukuoka
ORD-00140,2025-09-20,cust_0100,SKU-024,Product SKU-024,Food,2,18013.0,36026.0,3603.0,13202.0,direct,mobile,Sapporo
ORD-00141,2025-11-26,cust_0039,SKU-030,Product SKU-030,Electronics,1,28939.0,28939.0,1447.0,16038.0,social,tablet,Tokyo
ORD-00142,2025-08-16,cust_0063,SKU-046,Product SKU-046,Fashion,1,2668.0,2668.0,0.0,1287.0,organic,mobile,Nagoya
ORD-00143,2025-10-27,cust_0080,SKU-041,Product SKU-041,Fashion,2,16677.0,33354.0,1668.0,19958.0,direct,desktop,Fukuoka
ORD-00144,2025-08-09,cust_0065,SKU-039,Product SKU-039,Food,3,3426.0,10278.0,0.0,5712.0,direct,tablet,Osaka
ORD-00145,2025-04-27,cust_0056,SKU-029,Product SKU-029,Food,2,12708.0,25416.0,1271.0,10796.0,organic,desktop,Fukuoka
ORD-00146,2025-05-11,cust_0041,SKU-043,Product SKU-043,Home,1,11542.0,11542.0,1731.0,6659.0,organic,mobile,Tokyo
ORD-00147,2025-02-19,cust_0012,SKU-028,Product SKU-028,Home,2,22465.0,44930.0,8986.0,15232.0,organic,tablet,Sapporo
ORD-00148,2025-12-10,cust_0072,SKU-022,Product SKU-022,Beauty,2,4106.0,8212.0,1642.0,4102.0,social,tablet,Tokyo
ORD-00149,2025-06-09,cust_0037,SKU-039,Product SKU-039,Food,3,10874.0,32622.0,3262.0,11868.0,social,mobile,Tokyo
ORD-00150,2025-07-08,cust_0045,SKU-036,Product SKU-036,Fashion,2,3889.0,7778.0,778.0,2862.0,social,tablet,Sapporo
ORD-00151,2025-11-26,cust_0079,SKU-044,Product SKU-044,Food,3,16924.0,50772.0,7616.0,27867.0,email,mobile,Osaka
ORD-00152,2025-06-08,cust_0035,SKU-045,Product SKU-045,Electronics,2,27685.0,55370.0,0.0,19624.0,paid_search,tablet,Fukuoka
ORD-00153,2025-11-21,cust_0009,SKU-010,Product SKU-010,Electronics,1,29168.0,29168.0,4375.0,13392.0,social,desktop,Fukuoka
ORD-00154,2025-07-09,cust_0044,SKU-011,Product SKU-011,Fashion,2,9693.0,19386.0,3877.0,11290.0,direct,mobile,Tokyo
ORD-00155,2025-11-13,cust_0020,SKU-011,Product SKU-011,Fashion,1,1968.0,1968.0,0.0,852.0,social,desktop,Sapporo
ORD-00156,2025-05-20,cust_0057,SKU-027,Product SKU-027,Beauty,3,6859.0,20577.0,0.0,8304.0,organic,desktop,Sapporo
ORD-00157,2025-12-08,cust_0063,SKU-034,Product SKU-034,Food,1,9598.0,9598.0,480.0,5714.0,organic,mobile,Osaka
ORD-00158,2025-03-12,cust_0039,SKU-014,Product SKU-014,Food,2,23043.0,46086.0,0.0,15484.0,social,tablet,Fukuoka
ORD-00159,2025-07-14,cust_0023,SKU-009,Product SKU-009,Food,1,16211.0,16211.0,1621.0,7581.0,email,mobile,Fukuoka
ORD-00160,2025-08-12,cust_0095,SKU-003,Product SKU-003,Home,1,1053.0,1053.0,211.0,415.0,social,tablet,Fukuoka
ORD-00161,2025-08-02,cust_0091,SKU-041,Product SKU-041,Fashion,2,9041.0,18082.0,0.0,10666.0,paid_search,tablet,Fukuoka
ORD-00162,2025-02-15,cust_0089,SKU-024,Product SKU-024,Food,1,13383.0,13383.0,0.0,5764.0,social,tablet,Tokyo
ORD-00163,2025-06-23,cust_0051,SKU-020,Product SKU-020,Electronics,1,7036.0,7036.0,0.0,3188.0,organic,tablet,Sapporo
ORD-00164,2025-06-28,cust_0025,SKU-050,Product SKU-050,Electronics,3,10857.0,32571.0,6514.0,11214.0,organic,mobile,Nagoya
ORD-00165,2025-11-05,cust_0026,SKU-012,Product SKU-012,Beauty,3,5010.0,15030.0,0.0,5307.0,social,desktop,Sapporo
ORD-00166,2025-08-18,cust_0098,SKU-038,Product SKU-038,Home,3,20593.0,61779.0,9267.0,30309.0,direct,desktop,Nagoya
ORD-00167,2025-02-04,cust_0020,SKU-029,Product SKU-029,Food,3,14333.0,42999.0,0.0,23172.0,direct,mobile,Nagoya
ORD-00168,2025-06-08,cust_0065,SKU-005,Product SKU-005,Electronics,1,14121.0,14121.0,0.0,5798.0,email,mobile,Tokyo
ORD-00169,2025-09-17,cust_0079,SKU-039,Product SKU-039,Food,3,11842.0,35526.0,3553.0,20829.0,organic,desktop,Sapporo
ORD-00170,2025-06-14,cust_0084,SKU-013,Product SKU-013,Home,3,18348.0,55044.0,0.0,32328.0,social,mobile,Nagoya
ORD-00171,2025-09-16,cust_0092,SKU-006,Product SKU-006,Fashion,1,19561.0,19561.0,0.0,10021.0,social,tablet,Sapporo
ORD-00172,2025-07-06,cust_0079,SKU-011,Product SKU-011,Fashion,2,11499.0,22998.0,1150.0,9720.0,email,tablet,Sapporo
ORD-00173,2025-11-28,cust_0007,SKU-041,Product SKU-041,Fashion,2,10372.0,20744.0,0.0,9696.0,social,desktop,Nagoya
ORD-00174,2025-11-05,cust_0093,SKU-043,Product SKU-043,Home,2,26262.0,52524.0,0.0,24940.0,paid_search,desktop,Nagoya
ORD-00175,2025-12-06,cust_0084,SKU-045,Product SKU-045,Electronics,3,12063.0,36189.0,5428.0,21039.0,email,tablet,Fukuoka
ORD-00176,2025-03-07,cust_0083,SKU-022,Product SKU-022,Beauty,3,20268.0,60804.0,9121.0,34884.0,organic,tablet,Fukuoka
ORD-00177,2025-01-10,cust_0066,SKU-024,Product SKU-024,Food,1,11197.0,11197.0,0.0,4507.0,social,mobile,Osaka
ORD-00178,2025-02-09,cust_0018,SKU-010,Product SKU-010,Electronics,1,9226.0,9226.0,923.0,4901.0,direct,mobile,Nagoya
ORD-00179,2025-03-09,cust_0099,SKU-040,Product SKU-040,Electronics,1,18119.0,18119.0,0.0,6419.0,direct,mobile,Fukuoka
ORD-00180,2025-07-06,cust_0006,SKU-027,Product SKU-027,Beauty,1,20453.0,20453.0,1023.0,9882.0,social,mobile,Sapporo
ORD-00181,2025-08-29,cust_0031,SKU-020,Product SKU-020,Electronics,1,27167.0,27167.0,0.0,13678.0,direct,desktop,Fukuoka
ORD-00182,2025-07-15,cust_0099,SKU-019,Product SKU-019,Food,2,15336.0,30672.0,0.0,16718.0,direct,mobile,Nagoya
ORD-00183,2025-09-04,cust_0007,SKU-042,Product SKU-042,Beauty,3,26286.0,78858.0,0.0,40488.0,direct,mobile,Nagoya
ORD-00184,2025-03-24,cust_0011,SKU-049,Product SKU-049,Food,3,8547.0,25641.0,0.0,14085.0,organic,mobile,Fukuoka
ORD-00185,2025-08-01,cust_0045,SKU-002,Product SKU-002,Beauty,3,2071.0,6213.0,0.0,2304.0,organic,desktop,Osaka
ORD-00186,2025-02-20,cust_0004,SKU-021,Product SKU-021,Fashion,3,25256.0,75768.0,0.0,40719.0,paid_search,mobile,Nagoya
ORD-00187,2025-03-13,cust_0061,SKU-045,Product SKU-045,Electronics,2,22886.0,45772.0,2289.0,22182.0,organic,mobile,Nagoya
ORD-00188,2025-10-08,cust_0028,SKU-010,Product SKU-010,Electronics,3,28237.0,84711.0,8471.0,36171.0,email,mobile,Nagoya
ORD-00189,2025-05-03,cust_0016,SKU-004,Product SKU-004,Food,3,12885.0,38655.0,1933.0,12324.0,social,tablet,Sapporo
ORD-00190,2025-09-21,cust_0003,SKU-041,Product SKU-041,Fashion,3,17464.0,52392.0,0.0,20295.0,organic,tablet,Nagoya
ORD-00191,2025-08-02,cust_0031,SKU-037,Product SKU-037,Beauty,3,6026.0,18078.0,0.0,8262.0,email,mobile,Sapporo
ORD-00192,2025-09-17,cust_0070,SKU-033,Product SKU-033,Home,2,16847.0,33694.0,6739.0,14860.0,social,desktop,Nagoya
ORD-00193,2025-07-02,cust_0096,SKU-002,Product SKU-002,Beauty,2,23761.0,47522.0,0.0,24706.0,organic,tablet,Nagoya
ORD-00194,2025-06-30,cust_0018,SKU-003,Product SKU-003,Home,3,16607.0,49821.0,0.0,27357.0,social,tablet,Fukuoka
ORD-00195,2025-03-11,cust_0081,SKU-012,Product SKU-012,Beauty,2,2361.0,4722.0,0.0,1832.0,organic,mobile,Tokyo
ORD-00196,2025-09-21,cust_0041,SKU-020,Product SKU-020,Electronics,3,12248.0,36744.0,1837.0,13815.0,paid_search,desktop,Nagoya
ORD-00197,2025-12-02,cust_0100,SKU-004,Product SKU-004,Food,1,10292.0,10292.0,2058.0,4224.0,social,tablet,Fukuoka
ORD-00198,2025-04-06,cust_0050,SKU-022,Product SKU-022,Beauty,2,15138.0,30276.0,0.0,17478.0,direct,desktop,Tokyo
ORD-00199,2025-02-10,cust_0094,SKU-028,Product SKU-028,Home,1,13203.0,13203.0,1320.0,5124.0,organic,mobile,Nagoya
ORD-00200,2025-06-06,cust_0085,SKU-019,Product SKU-019,Food,3,13655.0,40965.0,2048.0,14337.0,social,desktop,Fukuoka
ORD-00201,2025-06-30,cust_0006,SKU-047,Product SKU-047,Beauty,2,18638.0,37276.0,0.0,18334.0,organic,mobile,Fukuoka
ORD-00202,2025-12-14,cust_0047,SKU-033,Product SKU-033,Home,1,5220.0,5220.0,0.0,2895.0,social,mobile,Osaka
ORD-00203,2025-11-27,cust_0009,SKU-016,Product SKU-016,Fashion,2,11307.0,22614.0,2261.0,7004.0,paid_search,tablet,Fukuoka
ORD-00204,2025-08-16,cust_0048,SKU-024,Product SKU-024,Food,3,23011.0,69033.0,0.0,31674.0,social,desktop,Nagoya
ORD-00205,2025-01-14,cust_0032,SKU-008,Product SKU-008,Home,2,22202.0,44404.0,4440.0,18476.0,direct,mobile,Nagoya
ORD-00206,2025-12-27,cust_0100,SKU-017,Product SKU-017,Beauty,3,13665.0,40995.0,0.0,20832.0,social,mobile,Tokyo
ORD-00207,2025-08-20,cust_0018,SKU-005,Product SKU-005,Electronics,3,5593.0,16779.0,839.0,10053.0,email,tablet,Nagoya
ORD-00208,2025-10-09,cust_0091,SKU-005,Product SKU-005,Electronics,2,16494.0,32988.0,6598.0,11456.0,paid_search,desktop,Sapporo
ORD-00209,2025-04-13,cust_0029,SKU-008,Product SKU-008,Home,1,23866.0,23866.0,4773.0,10697.0,email,tablet,Sapporo
ORD-00210,2025-10-10,cust_0048,SKU-030,Product SKU-030,Electronics,1,4328.0,4328.0,0.0,1700.0,social,tablet,Fukuoka
ORD-00211,2025-10-22,cust_0099,SKU-027,Product SKU-027,Beauty,2,2676.0,5352.0,803.0,1724.0,social,tablet,Sapporo
ORD-00212,2025-10-10,cust_0045,SKU-009,Product SKU-009,Food,1,19374.0,19374.0,3875.0,11428.0,social,tablet,Tokyo
ORD-00213,2025-03-20,cust_0016,SKU-034,Product SKU-034,Food,1,9472.0,9472.0,0.0,5498.0,paid_search,desktop,Sapporo
ORD-00214,2025-05-09,cust_0037,SKU-006,Product SKU-006,Fashion,3,6291.0,18873.0,0.0,6372.0,email,tablet,Sapporo
ORD-00215,2025-11-25,cust_0012,SKU-033,Product SKU-033,Home,3,5475.0,16425.0,0.0,5772.0,direct,tablet,Sapporo
ORD-00216,2025-01-22,cust_0044,SKU-037,Product SKU-037,Beauty,1,24844.0,24844.0,0.0,7792.0,direct,desktop,Osaka
ORD-00217,2025-08-02,cust_0099,SKU-037,Product SKU-037,Beauty,1,18734.0,18734.0,937.0,10617.0,direct,desktop,Nagoya
ORD-00218,2025-12-17,cust_0062,SKU-016,Product SKU-016,Fashion,2,12480.0,24960.0,0.0,12644.0,paid_search,desktop,Fukuoka
ORD-00219,2025-04-15,cust_0062,SKU-030,Product SKU-030,Electronics,1,10536.0,10536.0,0.0,5884.0,email,tablet,Nagoya
ORD-00220,2025-07-09,cust_0052,SKU-009,Product SKU-009,Food,1,15692.0,15692.0,0.0,5846.0,organic,desktop,Fukuoka
ORD-00221,2025-02-19,cust_0032,SKU-010,Product SKU-010,Electronics,2,1993.0,3986.0,797.0,1932.0,paid_search,mobile,Nagoya
ORD-00222,2025-06-10,cust_0074,SKU-047,Product SKU-047,Beauty,1,6100.0,6100.0,305.0,3653.0,social,desktop,Nagoya
ORD-00223,2025-02-16,cust_0064,SKU-002,Product SKU-002,Beauty,3,28384.0,85152.0,4258.0,50241.0,paid_search,tablet,Nagoya
ORD-00224,2025-05-25,cust_0007,SKU-004,Product SKU-004,Food,3,15099.0,45297.0,6795.0,19983.0,direct,mobile,Tokyo
ORD-00225,2025-05-16,cust_0056,SKU-009,Product SKU-009,Food,2,21961.0,43922.0,0.0,13772.0,organic,tablet,Sapporo
ORD-00226,2025-10-11,cust_0025,SKU-024,Product SKU-024,Food,2,9014.0,18028.0,1803.0,7844.0,direct,desktop,Sapporo
ORD-00227,2025-03-02,cust_0088,SKU-040,Product SKU-040,Electronics,1,4296.0,4296.0,215.0,1770.0,email,tablet,Nagoya
ORD-00228,2025-04-12,cust_0097,SKU-010,Product SKU-010,Electronics,2,18273.0,36546.0,3655.0,11406.0,organic,mobile,Nagoya
ORD-00229,2025-08-22,cust_0061,SKU-034,Product SKU-034,Food,3,4894.0,14682.0,0.0,5850.0,direct,desktop,Osaka
ORD-00230,2025-06-03,cust_0051,SKU-040,Product SKU-040,Electronics,3,18015.0,54045.0,10809.0,24477.0,social,tablet,Sapporo
ORD-00231,2025-01-09,cust_0039,SKU-031,Product SKU-031,Fashion,3,11367.0,34101.0,0.0,20256.0,direct,desktop,Tokyo
ORD-00232,2025-05-16,cust_0077,SKU-031,Product SKU-031,Fashion,3,29029.0,87087.0,8709.0,32070.0,organic,tablet,Fukuoka
ORD-00233,2025-11-19,cust_0022,SKU-034,Product SKU-034,Food,2,21775.0,43550.0,0.0,23800.0,paid_search,mobile,Sapporo
ORD-00234,2025-04-08,cust_0090,SKU-008,Product SKU-008,Home,2,1059.0,2118.0,106.0,732.0,paid_search,desktop,Sapporo
ORD-00235,2025-08-30,cust_0100,SKU-040,Product SKU-040,Electronics,3,26248.0,78744.0,11812.0,25095.0,paid_search,tablet,Osaka
ORD-00236,2025-12-06,cust_0072,SKU-021,Product SKU-021,Fashion,2,14612.0,29224.0,0.0,17154.0,social,tablet,Nagoya
ORD-00237,2025-12-13,cust_0070,SKU-023,Product SKU-023,Home,3,23274.0,69822.0,10473.0,34422.0,email,tablet,Fukuoka
ORD-00238,2025-05-23,cust_0025,SKU-016,Product SKU-016,Fashion,1,16964.0,16964.0,0.0,9014.0,paid_search,tablet,Fukuoka
ORD-00239,2025-06-28,cust_0041,SKU-031,Product SKU-031,Fashion,3,17034.0,51102.0,0.0,19743.0,direct,tablet,Sapporo
ORD-00240,2025-06-26,cust_0049,SKU-026,Product SKU-026,Fashion,1,28661.0,28661.0,0.0,8960.0,organic,desktop,Fukuoka
ORD-00241,2025-09-03,cust_0084,SKU-017,Product SKU-017,Beauty,3,6813.0,20439.0,0.0,11853.0,email,mobile,Tokyo
ORD-00242,2025-10-28,cust_0079,SKU-048,Product SKU-048,Home,1,7559.0,7559.0,1134.0,4320.0,paid_search,tablet,Osaka
ORD-00243,2025-07-31,cust_0007,SKU-007,Product SKU-007,Beauty,2,10244.0,20488.0,0.0,10334.0,paid_search,mobile,Sapporo
ORD-00244,2025-12-01,cust_0021,SKU-027,Product SKU-027,Beauty,2,28083.0,56166.0,2808.0,27812.0,email,desktop,Nagoya
ORD-00245,2025-02-15,cust_0083,SKU-004,Product SKU-004,Food,1,19743.0,19743.0,1974.0,10298.0,organic,mobile,Fukuoka
ORD-00246,2025-07-23,cust_0023,SKU-003,Product SKU-003,Home,1,23745.0,23745.0,3562.0,13977.0,email,mobile,Tokyo
ORD-00247,2025-11-05,cust_0039,SKU-037,Product SKU-037,Beauty,2,3665.0,7330.0,0.0,3198.0,direct,tablet,Fukuoka
ORD-00248,2025-08-28,cust_0018,SKU-033,Product SKU-033,Home,1,8549.0,8549.0,0.0,2981.0,social,tablet,Nagoya
ORD-00249,2025-01-08,cust_0092,SKU-012,Product SKU-012,Beauty,2,22230.0,44460.0,4446.0,22334.0,paid_search,mobile,Sapporo
ORD-00250,2025-08-07,cust_0082,SKU-026,Product SKU-026,Fashion,1,15701.0,15701.0,785.0,7863.0,paid_search,mobile,Fukuoka
ORD-00251,2025-01-04,cust_0042,SKU-016,Product SKU-016,Fashion,1,8193.0,8193.0,410.0,4311.0,email,desktop,Sapporo
ORD-00252,2025-01-06,cust_0093,SKU-037,Product SKU-037,Beauty,2,8216.0,16432.0,2465.0,6094.0,organic,desktop,Nagoya
ORD-00253,2025-12-18,cust_0021,SKU-026,Product SKU-026,Fashion,3,15324.0,45972.0,9194.0,18081.0,organic,tablet,Nagoya
ORD-00254,2025-04-24,cust_0048,SKU-040,Product SKU-040,Electronics,1,6964.0,6964.0,348.0,2409.0,direct,desktop,Fukuoka
ORD-00255,2025-08-30,cust_0090,SKU-036,Product SKU-036,Fashion,3,22842.0,68526.0,13705.0,25047.0,paid_search,tablet,Sapporo
ORD-00256,2025-08-17,cust_0011,SKU-034,Product SKU-034,Food,2,16081.0,32162.0,0.0,18498.0,organic,mobile,Sapporo
ORD-00257,2025-10-21,cust_0065,SKU-013,Product SKU-013,Home,1,16331.0,16331.0,0.0,9086.0,social,mobile,Osaka
ORD-00258,2025-09-08,cust_0092,SKU-038,Product SKU-038,Home,3,3183.0,9549.0,477.0,5181.0,social,mobile,Sapporo
ORD-00259,2025-10-16,cust_0054,SKU-030,Product SKU-030,Electronics,2,2203.0,4406.0,661.0,2388.0,organic,desktop,Nagoya
ORD-00260,2025-04-22,cust_0001,SKU-048,Product SKU-048,Home,1,17560.0,17560.0,878.0,7083.0,organic,tablet,Tokyo
ORD-00261,2025-01-17,cust_0009,SKU-031,Product SKU-031,Fashion,1,8969.0,8969.0,1794.0,3055.0,social,desktop,Fukuoka
ORD-00262,2025-07-12,cust_0058,SKU-025,Product SKU-025,Electronics,3,2867.0,8601.0,1720.0,3972.0,email,mobile,Osaka
ORD-00263,2025-09-28,cust_0069,SKU-026,Product SKU-026,Fashion,1,4257.0,4257.0,851.0,1282.0,organic,desktop,Fukuoka
ORD-00264,2025-10-06,cust_0087,SKU-047,Product SKU-047,Beauty,2,13012.0,26024.0,5205.0,9600.0,social,desktop,Osaka
ORD-00265,2025-02-27,cust_0036,SKU-013,Product SKU-013,Home,3,1450.0,4350.0,218.0,2106.0,organic,mobile,Osaka
ORD-00266,2025-11-01,cust_0009,SKU-007,Product SKU-007,Beauty,3,1491.0,4473.0,671.0,2286.0,organic,mobile,Tokyo
ORD-00267,2025-04-30,cust_0052,SKU-029,Product SKU-029,Food,1,16423.0,16423.0,0.0,7410.0,email,mobile,Sapporo
ORD-00268,2025-11-03,cust_0041,SKU-037,Product SKU-037,Beauty,2,23290.0,46580.0,0.0,18190.0,paid_search,tablet,Sapporo
ORD-00269,2025-06-03,cust_0029,SKU-027,Product SKU-027,Beauty,3,8617.0,25851.0,2585.0,14577.0,paid_search,tablet,Fukuoka
ORD-00270,2025-01-25,cust_0072,SKU-032,Product SKU-032,Beauty,3,29183.0,87549.0,13132.0,36276.0,direct,desktop,Fukuoka
ORD-00271,2025-06-03,cust_0053,SKU-010,Product SKU-010,Electronics,3,11606.0,34818.0,1741.0,12963.0,paid_search,desktop,Osaka
ORD-00272,2025-10-15,cust_0060,SKU-004,Product SKU-004,Food,2,12674.0,25348.0,2535.0,11634.0,social,mobile,Nagoya
ORD-00273,2025-11-28,cust_0027,SKU-022,Product SKU-022,Beauty,2,2833.0,5666.0,1133.0,2330.0,direct,tablet,Osaka
ORD-00274,2025-07-13,cust_0007,SKU-018,Product SKU-018,Home,3,20373.0,61119.0,0.0,34353.0,paid_search,tablet,Sapporo
ORD-00275,2025-04-17,cust_0028,SKU-031,Product SKU-031,Fashion,2,26149.0,52298.0,0.0,30704.0,organic,mobile,Osaka
ORD-00276,2025-09-03,cust_0095,SKU-008,Product SKU-008,Home,3,27476.0,82428.0,8243.0,42132.0,social,mobile,Sapporo
ORD-00277,2025-05-25,cust_0042,SKU-050,Product SKU-050,Electronics,3,11730.0,35190.0,5278.0,14349.0,email,desktop,Sapporo
ORD-00278,2025-02-20,cust_0064,SKU-030,Product SKU-030,Electronics,3,24183.0,72549.0,3627.0,38340.0,email,mobile,Nagoya
ORD-00279,2025-01-24,cust_0041,SKU-027,Product SKU-027,Beauty,1,17094.0,17094.0,2564.0,5877.0,email,tablet,Sapporo
ORD-00280,2025-08-02,cust_0075,SKU-047,Product SKU-047,Beauty,1,9208.0,9208.0,0.0,3398.0,direct,mobile,Fukuoka
ORD-00281,2025-12-17,cust_0071,SKU-042,Product SKU-042,Beauty,2,10458.0,20916.0,3137.0,10302.0,social,desktop,Osaka
ORD-00282,2025-03-28,cust_0094,SKU-023,Product SKU-023,Home,3,4629.0,13887.0,694.0,4932.0,direct,tablet,Tokyo
ORD-00283,2025-02-08,cust_0068,SKU-003,Product SKU-003,Home,3,28383.0,85149.0,0.0,45069.0,social,mobile,Osaka
ORD-00284,2025-03-19,cust_0009,SKU-046,Product SKU-046,Fashion,3,770.0,2310.0,116.0,951.0,direct,tablet,Sapporo
ORD-00285,2025-09-07,cust_0062,SKU-043,Product SKU-043,Home,3,964.0,2892.0,289.0,1224.0,organic,tablet,Nagoya
ORD-00286,2025-01-09,cust_0069,SKU-019,Product SKU-019,Food,3,15315.0,45945.0,6892.0,19719.0,paid_search,mobile,Tokyo
ORD-00287,2025-05-04,cust_0068,SKU-010,Product SKU-010,Electronics,3,6162.0,18486.0,0.0,10068.0,email,desktop,Tokyo
ORD-00288,2025-08-24,cust_0048,SKU-026,Product SKU-026,Fashion,3,17168.0,51504.0,0.0,20085.0,organic,tablet,Tokyo
ORD-00289,2025-07-14,cust_0012,SKU-026,Product SKU-026,Fashion,2,11627.0,23254.0,0.0,11418.0,paid_search,mobile,Fukuoka
ORD-00290,2025-06-19,cust_0056,SKU-042,Product SKU-042,Beauty,1,17193.0,17193.0,1719.0,9899.0,paid_search,mobile,Sapporo
ORD-00291,2025-01-24,cust_0061,SKU-018,Product SKU-018,Home,3,27763.0,83289.0,0.0,47457.0,direct,tablet,Tokyo
ORD-00292,2025-01-09,cust_0023,SKU-021,Product SKU-021,Fashion,3,28863.0,86589.0,0.0,45519.0,social,mobile,Nagoya
ORD-00293,2025-05-04,cust_0021,SKU-037,Product SKU-037,Beauty,2,17218.0,34436.0,5165.0,19592.0,email,desktop,Osaka
ORD-00294,2025-02-10,cust_0089,SKU-047,Product SKU-047,Beauty,2,15273.0,30546.0,0.0,10058.0,paid_search,mobile,Nagoya
ORD-00295,2025-11-11,cust_0078,SKU-050,Product SKU-050,Electronics,2,28668.0,57336.0,11467.0,22814.0,email,desktop,Fukuoka
ORD-00296,2025-10-11,cust_0030,SKU-023,Product SKU-023,Home,2,28264.0,56528.0,0.0,28484.0,social,mobile,Sapporo
ORD-00297,2025-02-07,cust_0038,SKU-016,Product SKU-016,Fashion,1,2920.0,2920.0,146.0,1499.0,paid_search,tablet,Fukuoka
ORD-00298,2025-02-24,cust_0041,SKU-024,Product SKU-024,Food,2,3200.0,6400.0,320.0,2612.0,email,mobile,Osaka
ORD-00299,2025-08-09,cust_0012,SKU-012,Product SKU-012,Beauty,3,13741.0,41223.0,4122.0,17412.0,organic,mobile,Nagoya
ORD-00300,2025-11-02,cust_0071,SKU-006,Product SKU-006,Fashion,2,18142.0,36284.0,7257.0,15078.0,email,desktop,Fukuoka
ORD-00301,2025-10-14,cust_0100,SKU-006,Product SKU-006,Fashion,1,27204.0,27204.0,2720.0,12414.0,social,mobile,Osaka
ORD-00302,2025-05-18,cust_0035,SKU-020,Product SKU-020,Electronics,1,15047.0,15047.0,0.0,6476.0,social,desktop,Fukuoka
ORD-00303,2025-05-09,cust_0010,SKU-024,Product SKU-024,Food,3,28355.0,85065.0,12760.0,38172.0,direct,mobile,Fukuoka
ORD-00304,2025-06-05,cust_0014,SKU-009,Product SKU-009,Food,2,700.0,1400.0,0.0,774.0,social,desktop,Fukuoka
ORD-00305,2025-11-30,cust_0043,SKU-028,Product SKU-028,Home,1,29240.0,29240.0,0.0,11585.0,paid_search,desktop,Nagoya
ORD-00306,2025-06-13,cust_0023,SKU-026,Product SKU-026,Fashion,3,9098.0,27294.0,4094.0,12210.0,direct,mobile,Nagoya
ORD-00307,2025-07-21,cust_0049,SKU-018,Product SKU-018,Home,3,11268.0,33804.0,0.0,16146.0,direct,mobile,Sapporo
ORD-00308,2025-08-25,cust_0004,SKU-047,Product SKU-047,Beauty,1,28318.0,28318.0,1416.0,15272.0,organic,desktop,Fukuoka
ORD-00309,2025-06-05,cust_0018,SKU-041,Product SKU-041,Fashion,3,7640.0,22920.0,0.0,11793.0,social,mobile,Fukuoka
ORD-00310,2025-10-26,cust_0077,SKU-031,Product SKU-031,Fashion,3,12324.0,36972.0,7394.0,18765.0,direct,mobile,Nagoya
ORD-00311,2025-11-01,cust_0090,SKU-035,Product SKU-035,Electronics,1,19326.0,19326.0,0.0,10256.0,email,mobile,Sapporo
ORD-00312,2025-11-27,cust_0006,SKU-037,Product SKU-037,Beauty,2,20485.0,40970.0,8194.0,16366.0,social,mobile,Tokyo
ORD-00313,2025-04-24,cust_0013,SKU-017,Product SKU-017,Beauty,3,15565.0,46695.0,4670.0,22140.0,direct,mobile,Fukuoka
ORD-00314,2025-08-26,cust_0048,SKU-026,Product SKU-026,Fashion,3,23284.0,69852.0,10478.0,31443.0,email,mobile,Fukuoka
ORD-00315,2025-08-01,cust_0014,SKU-019,Product SKU-019,Food,1,27656.0,27656.0,0.0,15194.0,paid_search,desktop,Nagoya
ORD-00316,2025-04-16,cust_0044,SKU-030,Product SKU-030,Electronics,2,15873.0,31746.0,1587.0,10454.0,social,desktop,Tokyo
ORD-00317,2025-12-30,cust_0039,SKU-003,Product SKU-003,Home,2,3895.0,7790.0,1168.0,2592.0,paid_search,tablet,Osaka
ORD-00318,2025-10-10,cust_0067,SKU-012,Product SKU-012,Beauty,3,5224.0,15672.0,784.0,9207.0,paid_search,desktop,Osaka
ORD-00319,2025-12-03,cust_0024,SKU-041,Product SKU-041,Fashion,1,13248.0,13248.0,1987.0,6415.0,paid_search,desktop,Sapporo
ORD-00320,2025-01-03,cust_0055,SKU-025,Product SKU-025,Electronics,1,21290.0,21290.0,0.0,11192.0,organic,tablet,Tokyo
ORD-00321,2025-07-07,cust_0069,SKU-012,Product SKU-012,Beauty,2,10117.0,20234.0,0.0,7662.0,social,tablet,Nagoya
ORD-00322,2025-11-09,cust_0077,SKU-025,Product SKU-025,Electronics,1,12080.0,12080.0,0.0,4900.0,social,tablet,Osaka
ORD-00323,2025-06-02,cust_0087,SKU-046,Product SKU-046,Fashion,3,27601.0,82803.0,0.0,41538.0,email,mobile,Osaka
ORD-00324,2025-04-04,cust_0040,SKU-008,Product SKU-008,Home,1,11513.0,11513.0,1151.0,4796.0,direct,mobile,Sapporo
ORD-00325,2025-04-06,cust_0050,SKU-028,Product SKU-028,Home,3,14857.0,44571.0,6686.0,25662.0,paid_search,tablet,Osaka
ORD-00326,2025-03-13,cust_0063,SKU-019,Product SKU-019,Food,2,6019.0,12038.0,1204.0,3806.0,email,mobile,Fukuoka
ORD-00327,2025-07-16,cust_0018,SKU-013,Product SKU-013,Home,3,28933.0,86799.0,13020.0,38928.0,social,desktop,Fukuoka
ORD-00328,2025-02-12,cust_0063,SKU-011,Product SKU-011,Fashion,1,17179.0,17179.0,0.0,5322.0,paid_search,tablet,Nagoya
ORD-00329,2025-08-23,cust_0022,SKU-050,Product SKU-050,Electronics,2,17187.0,34374.0,3437.0,15580.0,direct,mobile,Nagoya
ORD-00330,2025-07-07,cust_0100,SKU-035,Product SKU-035,Electronics,1,16490.0,16490.0,3298.0,8504.0,direct,mobile,Fukuoka
ORD-00331,2025-12-01,cust_0014,SKU-048,Product SKU-048,Home,2,22665.0,45330.0,9066.0,27188.0,social,desktop,Nagoya
ORD-00332,2025-03-02,cust_0012,SKU-029,Product SKU-029,Food,1,23381.0,23381.0,0.0,12701.0,direct,tablet,Nagoya
ORD-00333,2025-11-20,cust_0091,SKU-040,Product SKU-040,Electronics,3,13131.0,39393.0,0.0,21093.0,paid_search,mobile,Sapporo
ORD-00334,2025-05-24,cust_0045,SKU-035,Product SKU-035,Electronics,1,18107.0,18107.0,0.0,10750.0,email,desktop,Sapporo
ORD-00335,2025-12-14,cust_0035,SKU-033,Product SKU-033,Home,1,24548.0,24548.0,4910.0,13151.0,organic,desktop,Osaka
ORD-00336,2025-05-08,cust_0090,SKU-009,Product SKU-009,Food,2,4814.0,9628.0,1926.0,3604.0,social,desktop,Osaka
ORD-00337,2025-05-18,cust_0074,SKU-041,Product SKU-041,Fashion,2,19020.0,38040.0,1902.0,12274.0,organic,desktop,Sapporo
ORD-00338,2025-12-22,cust_0096,SKU-018,Product SKU-018,Home,2,28122.0,56244.0,2812.0,32908.0,email,tablet,Tokyo
ORD-00339,2025-02-17,cust_0100,SKU-047,Product SKU-047,Beauty,2,22062.0,44124.0,6619.0,22028.0,email,mobile,Sapporo
ORD-00340,2025-08-08,cust_0051,SKU-014,Product SKU-014,Food,2,24833.0,49666.0,0.0,19710.0,email,desktop,Sapporo
ORD-00341,2025-10-17,cust_0074,SKU-009,Product SKU-009,Food,2,25646.0,51292.0,7694.0,27116.0,organic,mobile,Fukuoka
ORD-00342,2025-03-22,cust_0003,SKU-008,Product SKU-008,Home,1,13518.0,13518.0,676.0,4876.0,paid_search,tablet,Nagoya
ORD-00343,2025-02-17,cust_0021,SKU-018,Product SKU-018,Home,2,19810.0,39620.0,0.0,16306.0,paid_search,mobile,Fukuoka
ORD-00344,2025-12-25,cust_0081,SKU-020,Product SKU-020,Electronics,2,22779.0,45558.0,6834.0,14914.0,organic,mobile,Osaka
ORD-00345,2025-03-09,cust_0062,SKU-005,Product SKU-005,Electronics,3,18014.0,54042.0,8106.0,23427.0,organic,tablet,Nagoya
ORD-00346,2025-12-22,cust_0016,SKU-028,Product SKU-028,Home,1,4399.0,4399.0,0.0,1825.0,organic,mobile,Nagoya
ORD-00347,2025-03-12,cust_0048,SKU-020,Product SKU-020,Electronics,1,11790.0,11790.0,1768.0,7049.0,paid_search,mobile,Sapporo
ORD-00348,2025-11-09,cust_0073,SKU-001,Product SKU-001,Fashion,2,19676.0,39352.0,0.0,20334.0,paid_search,desktop,Sapporo
ORD-00349,2025-04-22,cust_0088,SKU-029,Product SKU-029,Food,1,3057.0,3057.0,0.0,1607.0,direct,tablet,Fukuoka
ORD-00350,2025-06-11,cust_0045,SKU-028,Product SKU-028,Home,1,23837.0,23837.0,0.0,11761.0,paid_search,tablet,Sapporo
ORD-00351,2025-11-08,cust_0077,SKU-047,Product SKU-047,Beauty,3,8905.0,26715.0,0.0,14811.0,email,mobile,Sapporo
ORD-00352,2025-04-07,cust_0078,SKU-033,Product SKU-033,Home,2,22561.0,45122.0,6768.0,14276.0,paid_search,desktop,Fukuoka
ORD-00353,2025-09-13,cust_0015,SKU-016,Product SKU-016,Fashion,1,19323.0,19323.0,1932.0,10949.0,organic,desktop,Nagoya
ORD-00354,2025-10-19,cust_0017,SKU-025,Product SKU-025,Electronics,3,12915.0,38745.0,5812.0,13632.0,social,mobile,Tokyo
ORD-00355,2025-01-08,cust_0076,SKU-005,Product SKU-005,Electronics,1,8234.0,8234.0,0.0,4814.0,social,tablet,Nagoya
ORD-00356,2025-09-14,cust_0081,SKU-046,Product SKU-046,Fashion,2,23130.0,46260.0,6939.0,19460.0,direct,tablet,Sapporo
ORD-00357,2025-02-12,cust_0020,SKU-018,Product SKU-018,Home,3,9642.0,28926.0,0.0,17133.0,paid_search,tablet,Nagoya
ORD-00358,2025-11-21,cust_0051,SKU-038,Product SKU-038,Home,3,23015.0,69045.0,10357.0,34035.0,email,tablet,Fukuoka
ORD-00359,2025-01-30,cust_0094,SKU-016,Product SKU-016,Fashion,2,7712.0,15424.0,0.0,6726.0,direct,mobile,Nagoya
ORD-00360,2025-12-03,cust_0086,SKU-048,Product SKU-048,Home,1,22349.0,22349.0,0.0,11451.0,organic,mobile,Fukuoka
ORD-00361,2025-09-22,cust_0045,SKU-034,Product SKU-034,Food,3,23598.0,70794.0,0.0,24783.0,paid_search,tablet,Nagoya
ORD-00362,2025-01-16,cust_0094,SKU-008,Product SKU-008,Home,2,10383.0,20766.0,0.0,9494.0,email,tablet,Sapporo
ORD-00363,2025-09-12,cust_0081,SKU-005,Product SKU-005,Electronics,2,13928.0,27856.0,0.0,12532.0,direct,mobile,Nagoya
ORD-00364,2025-02-22,cust_0021,SKU-017,Product SKU-017,Beauty,3,26881.0,80643.0,12096.0,26982.0,direct,mobile,Tokyo
ORD-00365,2025-01-24,cust_0002,SKU-016,Product SKU-016,Fashion,2,14417.0,28834.0,0.0,10198.0,organic,tablet,Fukuoka
ORD-00366,2025-05-08,cust_0029,SKU-021,Product SKU-021,Fashion,3,12780.0,38340.0,0.0,14622.0,organic,tablet,Nagoya
ORD-00367,2025-12-11,cust_0016,SKU-033,Product SKU-033,Home,1,27107.0,27107.0,0.0,14673.0,organic,desktop,Tokyo
ORD-00368,2025-06-09,cust_0060,SKU-019,Product SKU-019,Food,3,10155.0,30465.0,1523.0,9213.0,paid_search,desktop,Sapporo
ORD-00369,2025-11-15,cust_0039,SKU-048,Product SKU-048,Home,2,7656.0,15312.0,1531.0,9058.0,paid_search,tablet,Sapporo
ORD-00370,2025-03-19,cust_0098,SKU-016,Product SKU-016,Fashion,2,688.0,1376.0,0.0,508.0,email,tablet,Tokyo
ORD-00371,2025-12-03,cust_0043,SKU-001,Product SKU-001,Fashion,3,11600.0,34800.0,5220.0,13650.0,paid_search,tablet,Osaka
ORD-00372,2025-01-31,cust_0054,SKU-032,Product SKU-032,Beauty,1,29190.0,29190.0,4378.0,11207.0,organic,mobile,Sapporo
ORD-00373,2025-07-10,cust_0053,SKU-045,Product SKU-045,Electronics,3,14025.0,42075.0,0.0,19953.0,direct,mobile,Fukuoka
ORD-00374,2025-10-18,cust_0010,SKU-038,Product SKU-038,Home,3,2337.0,7011.0,0.0,2601.0,email,desktop,Fukuoka
ORD-00375,2025-06-17,cust_0090,SKU-048,Product SKU-048,Home,2,9883.0,19766.0,0.0,6372.0,paid_search,mobile,Sapporo
ORD-00376,2025-02-24,cust_0014,SKU-010,Product SKU-010,Electronics,2,5349.0,10698.0,0.0,4514.0,direct,desktop,Osaka
ORD-00377,2025-08-26,cust_0058,SKU-020,Product SKU-020,Electronics,1,8318.0,8318.0,0.0,2889.0,email,tablet,Sapporo
ORD-00378,2025-06-17,cust_0006,SKU-014,Product SKU-014,Food,3,4876.0,14628.0,0.0,8637.0,social,tablet,Tokyo
ORD-00379,2025-05-14,cust_0087,SKU-020,Product SKU-020,Electronics,1,24693.0,24693.0,0.0,14461.0,social,tablet,Sapporo
ORD-00380,2025-08-25,cust_0032,SKU-007,Product SKU-007,Beauty,1,3506.0,3506.0,0.0,1064.0,paid_search,mobile,Osaka
ORD-00381,2025-12-18,cust_0052,SKU-024,Product SKU-024,Food,3,19094.0,57282.0,0.0,27192.0,email,mobile,Tokyo
ORD-00382,2025-11-27,cust_0009,SKU-013,Product SKU-013,Home,1,13581.0,13581.0,0.0,7762.0,email,mobile,Tokyo
ORD-00383,2025-03-28,cust_0060,SKU-004,Product SKU-004,Food,2,27762.0,55524.0,11105.0,28724.0,social,mobile,Fukuoka
ORD-00384,2025-03-30,cust_0088,SKU-028,Product SKU-028,Home,1,10941.0,10941.0,0.0,4201.0,paid_search,mobile,Sapporo
ORD-00385,2025-05-06,cust_0080,SKU-040,Product SKU-040,Electronics,2,19595.0,39190.0,1960.0,22136.0,social,mobile,Tokyo
ORD-00386,2025-03-12,cust_0036,SKU-025,Product SKU-025,Electronics,3,12867.0,38601.0,7720.0,17670.0,direct,mobile,Fukuoka
ORD-00387,2025-09-03,cust_0092,SKU-023,Product SKU-023,Home,2,16563.0,33126.0,0.0,19008.0,direct,desktop,Fukuoka
ORD-00388,2025-01-14,cust_0035,SKU-012,Product SKU-012,Beauty,1,9907.0,9907.0,0.0,5634.0,email,mobile,Fukuoka
ORD-00389,2025-10-27,cust_0068,SKU-023,Product SKU-023,Home,1,29988.0,29988.0,0.0,11226.0,paid_search,desktop,Sapporo
ORD-00390,2025-04-23,cust_0095,SKU-004,Product SKU-004,Food,2,17483.0,34966.0,0.0,20300.0,paid_search,mobile,Osaka
ORD-00391,2025-12-24,cust_0076,SKU-021,Product SKU-021,Fashion,3,11084.0,33252.0,0.0,16992.0,email,tablet,Sapporo
ORD-00392,2025-04-07,cust_0019,SKU-037,Product SKU-037,Beauty,2,25183.0,50366.0,5037.0,19780.0,social,mobile,Tokyo
ORD-00393,2025-11-05,cust_0008,SKU-015,Product SKU-015,Electronics,3,6955.0,20865.0,1043.0,6264.0,direct,mobile,Osaka
ORD-00394,2025-04-01,cust_0044,SKU-046,Product SKU-046,Fashion,2,27604.0,55208.0,0.0,16926.0,direct,tablet,Osaka
ORD-00395,2025-09-27,cust_0100,SKU-008,Product SKU-008,Home,1,25890.0,25890.0,0.0,13239.0,social,tablet,Tokyo
ORD-00396,2025-06-15,cust_0044,SKU-020,Product SKU-020,Electronics,1,4525.0,4525.0,679.0,2645.0,social,tablet,Nagoya
ORD-00397,2025-10-15,cust_0023,SKU-046,Product SKU-046,Fashion,3,20960.0,62880.0,12576.0,25596.0,direct,mobile,Fukuoka
ORD-00398,2025-12-19,cust_0040,SKU-047,Product SKU-047,Beauty,1,9188.0,9188.0,1378.0,2761.0,direct,desktop,Sapporo
ORD-00399,2025-11-05,cust_0005,SKU-012,Product SKU-012,Beauty,3,9887.0,29661.0,0.0,14589.0,organic,desktop,Osaka
ORD-00400,2025-02-09,cust_0043,SKU-048,Product SKU-048,Home,2,7521.0,15042.0,0.0,7384.0,organic,tablet,Nagoya
ORD-00401,2025-05-16,cust_0058,SKU-001,Product SKU-001,Fashion,3,6686.0,20058.0,0.0,8127.0,organic,tablet,Tokyo
ORD-00402,2025-08-13,cust_0007,SKU-025,Product SKU-025,Electronics,1,22111.0,22111.0,1106.0,9904.0,social,desktop,Sapporo
ORD-00403,2025-09-03,cust_0049,SKU-007,Product SKU-007,Beauty,3,23768.0,71304.0,10696.0,37611.0,paid_search,mobile,Fukuoka
ORD-00404,2025-05-31,cust_0010,SKU-003,Product SKU-003,Home,2,1092.0,2184.0,0.0,704.0,paid_search,desktop,Osaka
ORD-00405,2025-10-08,cust_0094,SKU-005,Product SKU-005,Electronics,1,28284.0,28284.0,0.0,13526.0,direct,desktop,Tokyo
ORD-00406,2025-03-26,cust_0056,SKU-042,Product SKU-042,Beauty,2,18416.0,36832.0,0.0,11642.0,email,mobile,Osaka
ORD-00407,2025-10-11,cust_0053,SKU-045,Product SKU-045,Electronics,3,21800.0,65400.0,6540.0,24825.0,email,desktop,Osaka
ORD-00408,2025-07-21,cust_0013,SKU-004,Product SKU-004,Food,2,17367.0,34734.0,0.0,10988.0,organic,desktop,Tokyo
ORD-00409,2025-11-17,cust_0038,SKU-043,Product SKU-043,Home,1,18206.0,18206.0,0.0,5602.0,paid_search,tablet,Nagoya
ORD-00410,2025-03-01,cust_0011,SKU-031,Product SKU-031,Fashion,2,9596.0,19192.0,960.0,8574.0,email,mobile,Sapporo
ORD-00411,2025-07-09,cust_0050,SKU-012,Product SKU-012,Beauty,2,26622.0,53244.0,0.0,23094.0,email,desktop,Fukuoka
ORD-00412,2025-05-18,cust_0034,SKU-015,Product SKU-015,Electronics,1,17145.0,17145.0,3429.0,8726.0,organic,mobile,Nagoya
ORD-00413,2025-10-29,cust_0070,SKU-027,Product SKU-027,Beauty,1,7212.0,7212.0,1442.0,3001.0,direct,desktop,Sapporo
ORD-00414,2025-10-21,cust_0088,SKU-031,Product SKU-031,Fashion,2,26509.0,53018.0,0.0,17162.0,organic,tablet,Sapporo
ORD-00415,2025-12-13,cust_0067,SKU-037,Product SKU-037,Beauty,1,29491.0,29491.0,0.0,17246.0,social,mobile,Osaka
ORD-00416,2025-03-06,cust_0028,SKU-013,Product SKU-013,Home,1,1759.0,1759.0,264.0,757.0,paid_search,tablet,Nagoya
ORD-00417,2025-02-04,cust_0041,SKU-047,Product SKU-047,Beauty,3,3067.0,9201.0,460.0,4284.0,email,tablet,Fukuoka
ORD-00418,2025-11-16,cust_0002,SKU-045,Product SKU-045,Electronics,2,17833.0,35666.0,0.0,15134.0,paid_search,tablet,Sapporo
ORD-00419,2025-02-21,cust_0075,SKU-049,Product SKU-049,Food,3,27785.0,83355.0,16671.0,27531.0,email,tablet,Nagoya
ORD-00420,2025-07-16,cust_0053,SKU-017,Product SKU-017,Beauty,3,19816.0,59448.0,5945.0,26271.0,paid_search,desktop,Fukuoka
ORD-00421,2025-11-08,cust_0019,SKU-040,Product SKU-040,Electronics,2,20584.0,41168.0,0.0,17238.0,email,tablet,Osaka
ORD-00422,2025-09-01,cust_0007,SKU-048,Product SKU-048,Home,2,27665.0,55330.0,0.0,22208.0,email,desktop,Nagoya
ORD-00423,2025-12-17,cust_0063,SKU-045,Product SKU-045,Electronics,1,3397.0,3397.0,0.0,1325.0,social,desktop,Nagoya
ORD-00424,2025-11-06,cust_0094,SKU-027,Product SKU-027,Beauty,1,19544.0,19544.0,977.0,7103.0,social,tablet,Fukuoka
ORD-00425,2025-07-11,cust_0098,SKU-034,Product SKU-034,Food,3,24720.0,74160.0,14832.0,25785.0,email,tablet,Sapporo
ORD-00426,2025-09-26,cust_0052,SKU-009,Product SKU-009,Food,1,26440.0,26440.0,0.0,9461.0,paid_search,mobile,Osaka
ORD-00427,2025-01-26,cust_0005,SKU-030,Product SKU-030,Electronics,3,27582.0,82746.0,0.0,31626.0,social,tablet,Fukuoka
ORD-00428,2025-12-15,cust_0082,SKU-008,Product SKU-008,Home,2,1402.0,2804.0,140.0,1340.0,paid_search,desktop,Sapporo
ORD-00429,2025-06-26,cust_0071,SKU-023,Product SKU-023,Home,2,5324.0,10648.0,1597.0,5848.0,organic,desktop,Tokyo
ORD-00430,2025-03-25,cust_0050,SKU-004,Product SKU-004,Food,1,25688.0,25688.0,5138.0,9412.0,paid_search,tablet,Osaka
ORD-00431,2025-07-29,cust_0035,SKU-042,Product SKU-042,Beauty,3,15642.0,46926.0,0.0,20751.0,paid_search,tablet,Osaka
ORD-00432,2025-04-25,cust_0077,SKU-001,Product SKU-001,Fashion,2,7946.0,15892.0,2384.0,9378.0,email,desktop,Fukuoka
ORD-00433,2025-05-10,cust_0045,SKU-030,Product SKU-030,Electronics,2,6937.0,13874.0,2081.0,6330.0,direct,desktop,Sapporo
ORD-00434,2025-09-19,cust_0014,SKU-001,Product SKU-001,Fashion,2,29983.0,59966.0,5997.0,29636.0,direct,desktop,Nagoya
ORD-00435,2025-09-04,cust_0088,SKU-007,Product SKU-007,Beauty,2,2383.0,4766.0,715.0,1894.0,email,desktop,Nagoya
ORD-00436,2025-09-22,cust_0025,SKU-010,Product SKU-010,Electronics,1,23081.0,23081.0,4616.0,12861.0,direct,desktop,Nagoya
ORD-00437,2025-01-14,cust_0088,SKU-009,Product SKU-009,Food,2,19834.0,39668.0,0.0,22694.0,social,desktop,Tokyo
ORD-00438,2025-10-20,cust_0075,SKU-046,Product SKU-046,Fashion,2,24572.0,49144.0,7372.0,25260.0,direct,tablet,Fukuoka
ORD-00439,2025-09-17,cust_0086,SKU-023,Product SKU-023,Home,1,9356.0,9356.0,1871.0,4653.0,direct,mobile,Nagoya
ORD-00440,2025-03-07,cust_0013,SKU-031,Product SKU-031,Fashion,3,22357.0,67071.0,13414.0,31371.0,paid_search,tablet,Nagoya
ORD-00441,2025-04-24,cust_0084,SKU-006,Product SKU-006,Fashion,3,10981.0,32943.0,6589.0,12918.0,email,desktop,Nagoya
ORD-00442,2025-08-26,cust_0075,SKU-019,Product SKU-019,Food,2,25611.0,51222.0,0.0,28680.0,direct,tablet,Sapporo
ORD-00443,2025-04-10,cust_0010,SKU-031,Product SKU-031,Fashion,3,15264.0,45792.0,2290.0,21015.0,social,mobile,Osaka
ORD-00444,2025-06-25,cust_0018,SKU-013,Product SKU-013,Home,3,12571.0,37713.0,1886.0,12933.0,paid_search,mobile,Fukuoka
ORD-00445,2025-04-01,cust_0043,SKU-041,Product SKU-041,Fashion,1,9746.0,9746.0,0.0,4246.0,paid_search,mobile,Sapporo
ORD-00446,2025-09-08,cust_0098,SKU-011,Product SKU-011,Fashion,1,23664.0,23664.0,0.0,11462.0,social,desktop,Fukuoka
ORD-00447,2025-01-03,cust_0062,SKU-025,Product SKU-025,Electronics,1,1613.0,1613.0,242.0,664.0,organic,desktop,Sapporo
ORD-00448,2025-12-13,cust_0025,SKU-002,Product SKU-002,Beauty,3,622.0,1866.0,0.0,687.0,email,desktop,Osaka
ORD-00449,2025-09-15,cust_0014,SKU-025,Product SKU-025,Electronics,1,17866.0,17866.0,0.0,9775.0,email,desktop,Fukuoka
ORD-00450,2025-11-02,cust_0094,SKU-034,Product SKU-034,Food,2,15961.0,31922.0,4788.0,19110.0,email,desktop,Nagoya
ORD-00451,2025-03-26,cust_0097,SKU-013,Product SKU-013,Home,2,28468.0,56936.0,0.0,20982.0,paid_search,mobile,Tokyo
ORD-00452,2025-03-28,cust_0076,SKU-033,Product SKU-033,Home,3,4133.0,12399.0,1860.0,6666.0,social,tablet,Nagoya
ORD-00453,2025-11-16,cust_0099,SKU-035,Product SKU-035,Electronics,1,1933.0,1933.0,290.0,643.0,organic,mobile,Tokyo
ORD-00454,2025-07-14,cust_0054,SKU-029,Product SKU-029,Food,2,4146.0,8292.0,415.0,4234.0,paid_search,tablet,Tokyo
ORD-00455,2025-12-05,cust_0039,SKU-027,Product SKU-027,Beauty,3,3479.0,10437.0,0.0,5082.0,paid_search,desktop,Tokyo
ORD-00456,2025-11-13,cust_0066,SKU-047,Product SKU-047,Beauty,1,3973.0,3973.0,795.0,1319.0,paid_search,tablet,Osaka
ORD-00457,2025-09-25,cust_0100,SKU-017,Product SKU-017,Beauty,2,29207.0,58414.0,8762.0,24704.0,paid_search,mobile,Sapporo
ORD-00458,2025-12-19,cust_0064,SKU-014,Product SKU-014,Food,2,28027.0,56054.0,0.0,16862.0,organic,mobile,Sapporo
ORD-00459,2025-03-18,cust_0086,SKU-032,Product SKU-032,Beauty,3,28509.0,85527.0,0.0,44223.0,organic,desktop,Osaka
ORD-00460,2025-05-16,cust_0059,SKU-019,Product SKU-019,Food,1,14196.0,14196.0,2839.0,5003.0,organic,desktop,Nagoya
ORD-00461,2025-08-07,cust_0087,SKU-021,Product SKU-021,Fashion,1,22287.0,22287.0,4457.0,11756.0,organic,mobile,Osaka
ORD-00462,2025-03-29,cust_0085,SKU-042,Product SKU-042,Beauty,2,10195.0,20390.0,2039.0,7758.0,organic,desktop,Nagoya
ORD-00463,2025-07-25,cust_0024,SKU-008,Product SKU-008,Home,2,12307.0,24614.0,0.0,13556.0,social,desktop,Osaka
ORD-00464,2025-12-23,cust_0015,SKU-009,Product SKU-009,Food,1,21929.0,21929.0,0.0,9316.0,direct,desktop,Sapporo
ORD-00465,2025-04-03,cust_0087,SKU-029,Product SKU-029,Food,2,18534.0,37068.0,3707.0,11440.0,paid_search,desktop,Fukuoka
ORD-00466,2025-08-14,cust_0015,SKU-027,Product SKU-027,Beauty,2,1856.0,3712.0,557.0,1464.0,direct,tablet,Sapporo
ORD-00467,2025-04-25,cust_0093,SKU-037,Product SKU-037,Beauty,3,29348.0,88044.0,17609.0,35349.0,direct,tablet,Sapporo
ORD-00468,2025-12-05,cust_0013,SKU-028,Product SKU-028,Home,2,21936.0,43872.0,0.0,21898.0,social,mobile,Sapporo
ORD-00469,2025-01-06,cust_0079,SKU-004,Product SKU-004,Food,1,19480.0,19480.0,1948.0,10805.0,social,mobile,Tokyo
ORD-00470,2025-06-14,cust_0097,SKU-032,Product SKU-032,Beauty,2,7606.0,15212.0,0.0,6878.0,direct,tablet,Fukuoka
ORD-00471,2025-02-10,cust_0052,SKU-016,Product SKU-016,Fashion,3,14043.0,42129.0,2106.0,13752.0,social,desktop,Nagoya
ORD-00472,2025-12-01,cust_0016,SKU-032,Product SKU-032,Beauty,2,1024.0,2048.0,102.0,636.0,direct,mobile,Tokyo
ORD-00473,2025-11-23,cust_0078,SKU-040,Product SKU-040,Electronics,3,9486.0,28458.0,2846.0,10302.0,social,desktop,Nagoya
ORD-00474,2025-08-21,cust_0007,SKU-015,Product SKU-015,Electronics,3,10293.0,30879.0,3088.0,13647.0,email,tablet,Fukuoka
ORD-00475,2025-12-04,cust_0015,SKU-007,Product SKU-007,Beauty,2,7042.0,14084.0,0.0,7732.0,email,tablet,Sapporo
ORD-00476,2025-02-24,cust_0048,SKU-045,Product SKU-045,Electronics,1,1850.0,1850.0,92.0,633.0,social,mobile,Nagoya
ORD-00477,2025-04-07,cust_0079,SKU-013,Product SKU-013,Home,2,4062.0,8124.0,0.0,3552.0,paid_search,tablet,Nagoya
ORD-00478,2025-08-01,cust_0014,SKU-049,Product SKU-049,Food,3,1872.0,5616.0,1123.0,2817.0,organic,desktop,Fukuoka
ORD-00479,2025-09-16,cust_0085,SKU-038,Product SKU-038,Home,2,4472.0,8944.0,0.0,4106.0,organic,tablet,Fukuoka
ORD-00480,2025-09-18,cust_0075,SKU-031,Product SKU-031,Fashion,1,23542.0,23542.0,3531.0,11149.0,paid_search,mobile,Fukuoka
ORD-00481,2025-11-07,cust_0085,SKU-039,Product SKU-039,Food,3,26540.0,79620.0,3981.0,33885.0,direct,tablet,Osaka
ORD-00482,2025-06-25,cust_0036,SKU-026,Product SKU-026,Fashion,2,29130.0,58260.0,11652.0,19810.0,social,tablet,Sapporo
ORD-00483,2025-10-08,cust_0039,SKU-045,Product SKU-045,Electronics,3,25891.0,77673.0,11651.0,45102.0,paid_search,mobile,Osaka
ORD-00484,2025-05-29,cust_0080,SKU-046,Product SKU-046,Fashion,3,20755.0,62265.0,0.0,37011.0,paid_search,tablet,Sapporo
ORD-00485,2025-06-15,cust_0089,SKU-041,Product SKU-041,Fashion,2,21455.0,42910.0,4291.0,19056.0,direct,tablet,Fukuoka
ORD-00486,2025-10-01,cust_0087,SKU-048,Product SKU-048,Home,2,8935.0,17870.0,3574.0,5430.0,organic,mobile,Fukuoka
ORD-00487,2025-12-10,cust_0019,SKU-004,Product SKU-004,Food,2,2170.0,4340.0,868.0,2324.0,email,tablet,Nagoya
ORD-00488,2025-12-20,cust_0019,SKU-004,Product SKU-004,Food,1,23639.0,23639.0,4728.0,10930.0,email,desktop,Tokyo
ORD-00489,2025-10-15,cust_0079,SKU-044,Product SKU-044,Food,3,26013.0,78039.0,11706.0,36552.0,paid_search,tablet,Nagoya
ORD-00490,2025-01-25,cust_0089,SKU-043,Product SKU-043,Home,2,27831.0,55662.0,2783.0,32674.0,email,tablet,Tokyo
ORD-00491,2025-05-09,cust_0002,SKU-048,Product SKU-048,Home,2,6491.0,12982.0,2596.0,4774.0,email,tablet,Sapporo
ORD-00492,2025-04-11,cust_0095,SKU-039,Product SKU-039,Food,1,23396.0,23396.0,0.0,10169.0,organic,mobile,Osaka
ORD-00493,2025-03-03,cust_0095,SKU-033,Product SKU-033,Home,2,11627.0,23254.0,0.0,10860.0,paid_search,mobile,Sapporo
ORD-00494,2025-06-19,cust_0033,SKU-001,Product SKU-001,Fashion,1,14257.0,14257.0,0.0,4935.0,email,tablet,Tokyo
ORD-00495,2025-11-12,cust_0100,SKU-041,Product SKU-041,Fashion,2,25373.0,50746.0,2537.0,27250.0,direct,desktop,Tokyo
ORD-00496,2025-09-27,cust_0091,SKU-021,Product SKU-021,Fashion,1,6989.0,6989.0,699.0,2240.0,direct,mobile,Fukuoka
ORD-00497,2025-07-26,cust_0070,SKU-035,Product SKU-035,Electronics,1,3212.0,3212.0,0.0,1603.0,email,desktop,Nagoya
ORD-00498,2025-11-13,cust_0028,SKU-049,Product SKU-049,Food,3,16150.0,48450.0,9690.0,25467.0,organic,mobile,Nagoya
ORD-00499,2025-11-25,cust_0058,SKU-016,Product SKU-016,Fashion,3,18604.0,55812.0,0.0,32799.0,email,desktop,Tokyo
ORD-00500,2025-10-04,cust_0050,SKU-017,Product SKU-017,Beauty,1,21857.0,21857.0,2186.0,11948.0,email,tablet,Sapporo
```

