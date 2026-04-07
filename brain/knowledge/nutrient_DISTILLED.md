---
id: nutrient
type: knowledge
owner: OA_Triage
---
# nutrient
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Nutrient Document Processing — Agent Skill

<p align="center">
  <a href="https://www.nutrient.io/api/"><img src="https://img.shields.io/badge/Nutrient-DWS%20API-blue" alt="Nutrient DWS API"></a>
  <a href="https://www.npmjs.com/package/@nutrient-sdk/dws-mcp-server"><img src="https://img.shields.io/npm/v/@nutrient-sdk/dws-mcp-server" alt="npm version"></a>
  <a href="nutrient-document-processing/LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache--2.0-green" alt="License"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-purple" alt="Agent Skills"></a>
</p>

<p align="center">
  <strong>Give your AI agent PDF superpowers — in one command.</strong><br>
  Generate, convert, extract, OCR, redact, sign, archive, and optimize documents from any coding agent.
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Demo: Ask your agent to redact PII from a PDF" width="720">
</p>

<p align="center">
  <a href="#30-second-quickstart">Quickstart</a> •
  <a href="#real-world-workflows">Workflows</a> •
  <a href="#features">Features</a> •
  <a href="#supported-agents">40+ Agents</a>
</p>

---

## 30-Second Quickstart

**1. Get a free API key** → **<https://dashboard.nutrient.io/sign_up/?product=processor>**

**2. Install & configure:**

```bash
# Install the skill (works with 40+ agents)
npx skills add PSPDFKit-labs/nutrient-agent-skill

# Set your API key
export NUTRIENT_API_KEY="pdf_live_..."
```

**3. Ask your agent:**

> *"Extract the text from invoice.pdf"*

That's it. Your agent now has full document processing capabilities.

---

## Requirements

- Python 3.10+
- `uv` installed: <https://docs.astral.sh/uv/>
- Nutrient API key

---

## Supported Agents

Works out of the box with **40+ AI coding agents**:

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-black?logo=anthropic&logoColor=white" alt="Claude Code" height="28">
  <img src="https://img.shields.io/badge/Codex_CLI-black?logo=openai&logoColor=white" alt="Codex CLI" height="28">
  <img src="https://img.shields.io/badge/Gemini_CLI-4285F4?logo=google&logoColor=white" alt="Gemini CLI" height="28">
  <img src="https://img.shields.io/badge/Cursor-000?logo=cursor&logoColor=white" alt="Cursor" height="28">
  <img src="https://img.shields.io/badge/GitHub_Copilot-000?logo=githubcopilot&logoColor=white" alt="GitHub Copilot" height="28">
  <img src="https://img.shields.io/badge/Windsurf-06B6D4?logoColor=white" alt="Windsurf" height="28">
  <img src="https://img.shields.io/badge/OpenCode-333?logoColor=white" alt="OpenCode" height="28">
  <img src="https://img.shields.io/badge/Amp-7C3AED?logoColor=white" alt="Amp" height="28">
  <img src="https://img.shields.io/badge/Roo_Code-FF6B35?logoColor=white" alt="Roo Code" height="28">
  <img src="https://img.shields.io/badge/OpenClaw-1a1a2e?logoColor=white" alt="OpenClaw" height="28">
  <img src="https://img.shields.io/badge/+30_more-gray" alt="and 30 more" height="28">
</p>

Any agent that supports the [Agent Skills](https://agentskills.io) standard works automatically.

---

## Real-World Workflows

### 🔍 Workflow 1: OCR a scanned document and extract text

You have a scanned PDF — no selectable text. Ask your agent:

> *"OCR scanned-contract.pdf in English and extract the text to a file"*

**What happens:**
```
scanned-contract.pdf (image-only)
  → OCR (English) → searchable-contract.pdf (selectable text)
  → Extract text → contract-text.txt
```

<img src="assets/workflow-ocr.gif" alt="OCR workflow" width="720">

### 📋 Workflow 2: Fill a PDF form and sign it

You have an onboarding form to complete. Ask your agent:

> *"Fill employee-onboarding.pdf with name 'Jane Smith', start date '2026-03-01', and department 'Engineering', then digitally sign it"*

**What happens:**
```
employee-onboarding.pdf (blank form)
  → Fill fields (name, date, department)
  → Digital signature (CMS)
  → employee-onboarding-signed.pdf ✅
```

<img src="assets/workflow-fill-sign.gif" alt="Fill form and sign workflow" width="720">

### 🔒 Workflow 3: Redact PII before sharing

You need to share a document but it contains sensitive data. Ask your agent:

> *"Redact all social security numbers, email addresses, and credit card numbers from patient-records.pdf"*

**What happens:**
```
patient-records.pdf (contains PII)
  → Detect SSNs, emails, credit cards
  → Apply black redaction boxes (irreversible)
  → patient-records-redacted.pdf 🔒
```

> **Tip:** For smarter redaction, try: *"Use AI redaction to find and remove all personally identifiable information from contract.pdf"* — this uses contextual AI analysis instead of pattern matching.

---

## Features

| Capability | Description | Example prompt |
|------------|-------------|----------------|
| ✨ **Generate** | Create PDFs from HTML templates, uploaded assets, or remote URLs | *"Generate a PDF proposal from this HTML template"* |
| 📄 **Convert** | PDF ↔ DOCX/XLSX/PPTX, HTML → PDF, images → PDF | *"Convert report.docx to PDF"* |
| 🧩 **Assemble** | Merge, split, reorder, rotate, and flatten PDF packets before delivery | *"Merge these PDFs, rotate the landscape pages, and keep only pages 1-5"* |
| 📝 **Extract** | Text, tables, and key-value pairs from PDFs | *"Extract all tables from invoice.pdf as Excel"* |
| 🔍 **OCR** | Multi-language OCR for scanned documents | *"OCR this German scan and extract the text"* |
| 🔒 **Redact** | Pattern-based + AI-powered PII redaction | *"Redact all SSNs and emails from records.pdf"* |
| 💧 **Watermark** | Text or image watermarks with full styling | *"Add a DRAFT watermark to proposal.pdf"* |
| ✍️ **Sign** | CMS and CAdES digital signatures | *"Digitally sign contract.pdf"* |
| 📋 **Fill Forms** | Programmatic PDF form filling | *"Fill the tax form with these values…"* |
| 🗂️ **Compliance** | Convert PDFs for archival or accessibility targets like PDF/A and PDF/UA | *"Convert this PDF to PDF/A-2a"* |
| ⚡ **Optimize** | Optimize and linearize PDFs for web delivery and download performance | *"Linearize this PDF for fast web viewing"* |
| 📊 **Credits** | Monitor API usage and balance | *"How many API credits do I have left?"* |

---

## Installation

### Using `npx skills` (Recommended)

```bash
# Install to all detected agents
npx skills add PSPDFKit-labs/nutrient-agent-skill

# Install to specific agents only
npx skills add PSPDFKit-labs/nutrient-agent-skill -a claude-code -a codex -a cursor

# Install globally (available across all projects)
npx skills add PSPDFKit-labs/nutrient-agent-skill -g
```

### Manual Installation

Copy the `nutrient-document-processing/` folder to your agent's skills directory:

| Agent | Project Path | Global Path |
|-------|-------------|-------------|
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Codex CLI** | `.codex/skills/` | `~/.codex/skills/` |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` |
| **OpenCode** | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| **Amp** | `.agents/skills/` | `~/.config/agents/skills/` |
| **OpenClaw** | `skills/` | `~/.moltbot/skills/` |
| **Roo Code** | `.roo/skills/` | `~/.roo/skills/` |

Example for Claude Code:

```bash
git clone https://github.com/PSPDFKit-labs/nutrient-agent-skill.git
cp -r nutrient-agent-skill/nutrient-document-processing ~/.claude/skills/
```

---

## Skill Structure

```
nutrient-document-processing/
├── SKILL.md                          # Main instructions (loaded by agents)
├── agents/
│   └── openai.yaml                   # Optional Codex App metadata
├── references/
│   ├── REFERENCE.md                  # Reference index
│   └── *.md                          # Focused cookbooks by workflow type
├── scripts/
│   ├── *.py                          # Single-operation scripts
│   └── lib/common.py                 # Shared utilities
├── assets/
│   ├── nutrient.svg                  # Skill icon
│   └── templates/
│       └── custom-workflow-template.py  # Runtime pipeline template
├── tests/
│   └── testing-guide.md
└── LICENSE.txt                       # Apache-2.0
```

### Script Model

- `scripts/*.py` are single-operation scripts only.
- Multi-step workflows are generated at runtime in a temporary script from `assets/templates/custom-workflow-template.py`.
- Do not commit runtime pipeline scripts.
- Use `references/` for HTML/URL generation, compliance outputs, and other workflows that are easier to express as direct API payloads or temporary pipelines.

## Documentation

- **[SKILL.md](nutrient-document-processing/SKILL.md)** — Agent instructions with setup and operation examples
- **[Reference Index](nutrient-document-processing/references/REFERENCE.md)** — Modular cookbook for generation, conversion, extraction, security, compliance, and workflow sequencing
- **[Testing Guide](nutrient-document-processing/tests/testing-guide.md)** — Manual test procedures
- **[Custom Workflow Template](nutrient-document-processing/assets/templates/custom-workflow-template.py)** — Runtime pipeline starting point
- **[Codex App Metadata](nutrient-document-processing/agents/openai.yaml)** — Optional manifest for Codex App packaging
- **[API Playground](https://dashboard.nutrient.io/processor-api/playground/)** — Interactive API testing
- **[Official API Docs](https://www.nutrient.io/guides/dws-processor/)** — Nutrient documentation

## About

Built by [Nutrient](https://www.nutrient.io/) (formerly PSPDFKit) — document SDKs trusted by thousands of companies worldwide.

## License

[Apache-2.0](nutrient-document-processing/LICENSE.txt)

```

### File: record-gifs.sh
```sh
#!/bin/bash
# Record demo GIFs using screencapture + real macOS Terminal
# Usage: ./record-gifs.sh [demo|ocr|fill-sign|all]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ASSETS_DIR="$SCRIPT_DIR/assets"
TAPES_DIR="$SCRIPT_DIR/tapes/helpers"
TEMP_DIR="$SCRIPT_DIR/.recording-tmp"

mkdir -p "$ASSETS_DIR" "$TEMP_DIR"

WIN_WIDTH=880
WIN_HEIGHT=520
FPS=6

capture_frames() {
    local win_id="$1"
    local frames_dir="$2"
    local duration="$3"
    local interval
    interval=$(python3 -c "print(1.0/$FPS)")
    local total_frames=$((duration * FPS))
    local frame=0

    while [[ $frame -lt $total_frames ]]; do
        printf "%04d" $frame | xargs -I{} screencapture -l "$win_id" -x "$frames_dir/frame-{}.png" 2>/dev/null &
        sleep "$interval"
        frame=$((frame + 1))
    done
    wait
}

record_gif() {
    local name="$1"
    local script="$2"
    local height="${3:-$WIN_HEIGHT}"
    local duration="${4:-18}"
    local gif="$ASSETS_DIR/${name}.gif"
    local frames_dir="$TEMP_DIR/${name}-frames"

    rm -rf "$frames_dir"
    mkdir -p "$frames_dir"

    echo "🎬 Recording: $name (${duration}s @ ${FPS}fps)"

    # Close stale demo windows
    osascript -e '
        tell application "Terminal"
            repeat with w in windows
                try
                    if (item 1 of bounds of w) is 80 then close w
                end try
            end repeat
        end tell
    ' 2>/dev/null || true
    sleep 0.3

    # Open fresh Terminal with Pro theme
    osascript -e "
        tell application \"Terminal\"
            activate
            do script \"export PS1='> '; clear; sleep 1.5; bash '${script}'\"
            delay 0.5
            set current settings of front window to settings set \"Pro\"
            set bounds of front window to {80, 80, $((80 + WIN_WIDTH)), $((80 + height))}
        end tell
    " 2>/dev/null
    sleep 0.5

    # Get window ID
    local cg_win_id
    cg_win_id=$(osascript -e 'tell application "Terminal" to get id of front window' 2>/dev/null || echo "")
    if [[ -z "$cg_win_id" ]]; then echo "   ❌ No window ID"; return 1; fi
    echo "   Window ID: $cg_win_id"

    # Capture frames
    echo "   ⏺  Capturing..."
    capture_frames "$cg_win_id" "$frames_dir" "$duration"

    local frame_count
    frame_count=$(ls "$frames_dir"/frame-*.png 2>/dev/null | wc -l | tr -d ' ')
    echo "   ✅ $frame_count frames"

    # Convert to GIF (single-pass palette)
    echo "   🔄 Encoding GIF..."
    ffmpeg -y -framerate "$FPS" -i "$frames_dir/frame-%04d.png" \
        -vf "scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3" \
        -loop 0 \
        "$gif" \
        -loglevel error 2>/dev/null

    echo "   📦 $(du -h "$gif" | cut -f1) → $gif"

    # Close window
    osascript -e '
        tell application "Terminal"
            repeat with w in windows
                try
                    if (item 1 of bounds of w) is 80 then close w
                end try
            end repeat
        end tell
    ' 2>/dev/null || true

    echo ""
}

target="${1:-all}"

case "$target" in
    demo)      record_gif "demo" "$TAPES_DIR/demo-full.sh" 520 16 ;;
    ocr)       record_gif "workflow-ocr" "$TAPES_DIR/ocr-full.sh" 580 20 ;;
    fill-sign) record_gif "workflow-fill-sign" "$TAPES_DIR/fill-sign-full.sh" 600 20 ;;
    all)
        record_gif "demo" "$TAPES_DIR/demo-full.sh" 520 16
        sleep 1
        record_gif "workflow-ocr" "$TAPES_DIR/ocr-full.sh" 580 20
        sleep 1
        record_gif "workflow-fill-sign" "$TAPES_DIR/fill-sign-full.sh" 600 20
        ;;
    *) echo "Usage: $0 [demo|ocr|fill-sign|all]"; exit 1 ;;
esac

echo "🎉 Done!"
ls -lh "$ASSETS_DIR"/*.gif
rm -rf "$TEMP_DIR"

```

### File: tools\validate-repo.py
```py
#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "nutrient-document-processing"
CONFLICT_MARKERS = ("<" * 7, "=" * 7, ">" * 7)
TEXT_SUFFIXES = {".md", ".txt", ".py", ".yaml", ".yml", ".svg", ".gitignore"}


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def check_required_paths() -> None:
    required = [
        REPO_ROOT / "README.md",
        SKILL_DIR / "SKILL.md",
        SKILL_DIR / "LICENSE.txt",
        SKILL_DIR / "references" / "REFERENCE.md",
        SKILL_DIR / "scripts" / "lib" / "common.py",
        SKILL_DIR / "tests" / "testing-guide.md",
    ]
    missing = [str(path.relative_to(REPO_ROOT)) for path in required if not path.exists()]
    if missing:
        fail("Missing required files:\n- " + "\n- ".join(missing))


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in TEXT_SUFFIXES:
            files.append(path)
    return files


def check_conflict_markers() -> None:
    offenders: list[str] = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(marker in text for marker in CONFLICT_MARKERS):
            offenders.append(str(path.relative_to(REPO_ROOT)))
    if offenders:
        fail("Unresolved merge markers found:\n- " + "\n- ".join(sorted(offenders)))


def check_skill_frontmatter() -> None:
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md is missing a frontmatter block.")
    frontmatter = match.group(1)
    for field in ("name:", "description:", "license:"):
        if field not in frontmatter:
            fail(f"SKILL.md frontmatter is missing `{field[:-1]}`.")


def check_readme_links() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    if 'href="nutrient-document-processing/LICENSE.txt"' not in readme:
        fail("README.md does not point its license badge at nutrient-document-processing/LICENSE.txt.")
    if "[Apache-2.0](nutrient-document-processing/LICENSE.txt)" not in readme:
        fail("README.md does not point its license section at nutrient-document-processing/LICENSE.txt.")


def check_reference_links() -> None:
    reference_path = SKILL_DIR / "references" / "REFERENCE.md"
    text = reference_path.read_text(encoding="utf-8")
    links = re.findall(r"\(([^)]+)\)", text)
    missing: list[str] = []
    for link in links:
        if "://" in link or link.startswith("#"):
            continue
        target = (reference_path.parent / link).resolve()
        if not target.exists():
            missing.append(link)
    if missing:
        fail("REFERENCE.md contains missing relative links:\n- " + "\n- ".join(sorted(missing)))


def main() -> None:
    check_required_paths()
    check_conflict_markers()
    check_skill_frontmatter()
    check_readme_links()
    check_reference_links()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()

```

