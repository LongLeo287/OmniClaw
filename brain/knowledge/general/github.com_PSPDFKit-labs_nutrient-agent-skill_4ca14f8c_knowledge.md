---
id: github.com-pspdfkit-labs-nutrient-agent-skill-4ca1
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:15.564462
---

# KNOWLEDGE EXTRACT: github.com_PSPDFKit-labs_nutrient-agent-skill_4ca14f8c
> **Extracted on:** 2026-04-01 13:29:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522481/github.com_PSPDFKit-labs_nutrient-agent-skill_4ca14f8c

---

## File: `.gitignore`
```
__pycache__/
*.pyc
.recording-tmp/
```

## File: `README.md`
```markdown
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

- **[SKILL.md](../bmad_repo/SKILL.md)** — Agent instructions with setup and operation examples
- **[Reference Index](../claude_bp_repo/reference.md)** — Modular cookbook for generation, conversion, extraction, security, compliance, and workflow sequencing
- **[Testing Guide](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/backend-dev-guidelines/resources/testing-guide.md)** — Manual test procedures
- **[Custom Workflow Template](nutrient-document-processing/assets/templates/custom-workflow-template.py)** — Runtime pipeline starting point
- **[Codex App Metadata](nutrient-document-processing/agents/openai.yaml)** — Optional manifest for Codex App packaging
- **[API Playground](https://dashboard.nutrient.io/processor-api/playground/)** — Interactive API testing
- **[Official API Docs](https://www.nutrient.io/guides/dws-processor/)** — Nutrient documentation

## About

Built by [Nutrient](https://www.nutrient.io/) (formerly PSPDFKit) — document SDKs trusted by thousands of companies worldwide.

## License

[Apache-2.0](nutrient-document-processing/LICENSE.txt)
```

## File: `record-gifs.sh`
```bash
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

## File: `nutrient-document-processing/LICENSE.txt`
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
      submitted to the Licensor for inclusion in the Work by the copyright owner
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
      on behalf of whom a Contribution has been received by the Licensor and
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
          within such NOTICE file, excluding any notices that do not
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

   Copyright 2025 Nutrient GmbH

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

## File: `nutrient-document-processing/SKILL.md`
```markdown
---
name: nutrient-document-processing
description: >-
  Process documents with Nutrient DWS. Use when the user wants to generate PDFs from HTML or URLs,
  convert Office/images/PDFs, assemble or split packets, OCR scans, extract text/tables/key-value
  pairs, redact PII, watermark, sign, fill forms, optimize PDFs, or produce compliance outputs like
  PDF/A or PDF/UA. Triggers include convert to PDF, merge these PDFs, OCR this scan, extract tables,
  redact PII, sign this PDF, make this PDF/A, or linearize for web delivery.
license: Apache-2.0
metadata:
  author: nutrient-sdk
  version: "1.0"
  homepage: "https://www.nutrient.io/api/"
  repository: "https://github.com/PSPDFKit-labs/nutrient-agent-skill"
  compatibility: "Requires Python 3.10+, uv, and internet. Works with Claude Code, Codex CLI, Gemini CLI, OpenCode, Cursor, Windsurf, GitHub Copilot, Amp, or any Agent Skills-compatible product."
  short-description: "Generate, convert, assemble, OCR, redact, sign, archive, and optimize documents"
---

# Nutrient Document Processing

Use Nutrient DWS for managed document workflows where fidelity, compliance, or multi-step processing matters more than local-tool convenience.

## Setup
- Get a Nutrient DWS API key at <https://dashboard.nutrient.io/sign_up/?product=processor>.
- Direct API calls use `Authorization: Bearer $NUTRIENT_API_KEY`.
  ```bash
  export NUTRIENT_API_KEY="nutr_sk_..."
  ```
- MCP setups commonly use `@nutrient-sdk/dws-mcp-server` with `NUTRIENT_DWS_API_KEY`.
- Scripts live in `scripts/` relative to this SKILL.md. Use the directory containing this SKILL.md as the working directory:
  ```bash
  cd <directory containing this SKILL.md> && uv run scripts/<script>.py --help
  ```
- Page ranges use `start:end` with 0-based indexes and end-exclusive semantics. Negative indexes count from the end.

## When to use
- Generate PDFs from HTML templates, uploaded assets, or remote URLs.
- Convert Office, HTML, image, and PDF files between supported formats.
- OCR scans and extract text, tables, or key-value pairs.
- Redact PII, watermark, sign, fill forms, merge, split, rotate, flatten, or encrypt PDFs.
- Produce delivery targets like PDF/A, PDF/UA, optimized PDFs, or linearized PDFs.
- Check credits before large, batch, or AI-heavy runs.

## Tool preference
1. Prefer `scripts/*.py` for covered single-operation workflows.
2. Use `assets/templates/custom-workflow-template.py` for multi-step jobs that should still run through the Python client.
3. Use the modular `references/` docs and direct API payloads for capabilities that do not yet have a dedicated helper script, especially HTML/URL generation and compliance tuning.
4. Use local PDF utilities only for lightweight inspection. Use Nutrient when output fidelity or compliance matters.

## Single-operation scripts
- `convert.py` -> convert between `pdf`, `pdfa`, `pdfua`, `docx`, `xlsx`, `pptx`, `png`, `jpeg`, `webp`, `html`, and `markdown`
- `merge.py` -> merge multiple files into one PDF
- `split.py` -> split one PDF into multiple PDFs by page ranges
- `add-pages.py` -> append blank pages
- `delete-pages.py` -> remove specific pages
- `duplicate-pages.py` -> reorder or duplicate pages into a new PDF
- `rotate.py` -> rotate selected pages
- `ocr.py` -> OCR scanned PDFs or images
- `extract-text.py` -> extract text to JSON
- `extract-table.py` -> extract tables
- `extract-key-value-pairs.py` -> extract key-value pairs
- `watermark-text.py` -> apply a text watermark
- `redact-ai.py` -> detect and apply AI-powered redactions
- `sign.py` -> digitally sign a local PDF
- `password-protect.py` -> write encrypted output PDFs
- `optimize.py` -> apply optimization and linearization-style options via JSON

## Multi-Step Workflow Rule
Do not add new committed pipeline scripts under `scripts/`.

When the user asks for multiple operations in one run:
1. Copy `assets/templates/custom-workflow-template.py` to a temporary location such as `/tmp/ndp-workflow-<task>.py`.
2. Implement the combined workflow in that temporary script.
3. Run it with `uv run /tmp/ndp-workflow-<task>.py ...`.
4. Return generated output files.
5. Delete the temporary script unless the user explicitly asks to keep it.

## PDF Requirements
- `split.py` requires a multi-page PDF and cannot extract ranges from a single-page document.
- `delete-pages.py` must retain at least one page and cannot delete the entire document.
- `sign.py` only accepts local file paths for the main PDF.

## Decision rules
- Prefer a helper script when one already covers the requested operation cleanly.
- If you control the source markup, prefer HTML generation over browser print workflows.
- Use remote `file.url` inputs when the source already lives at a stable URL and you want to avoid local uploads.
- Use `output.type` for conversion and finalization targets. Use `actions` for transformations when building direct API payloads.
- OCR before text extraction, key-value extraction, or semantic redaction on scans.
- Prefer preset or regex redaction when the target is explicit. Use AI redaction only for contextual or natural-language requests.
- Use the PDF manipulation reference for merge, split, rotate, flatten, and page-range workflows instead of inferring those payloads from conversion examples.
- Treat PDF/A and PDF/UA as compliance targets, not cosmetic export formats. Choose the target up front and validate final artifacts when requirements are contractual.
- For PDF/UA, clean born-digital inputs and structured HTML usually tag better than rasterized or flattened source PDFs.
- For delivery optimization, linearize or optimize unsigned output artifacts instead of mutating already signed files.
- When the user asks for multiple steps, keep destructive or final steps late in the sequence. Use the workflow recipes when ordering is ambiguous.

## Anti-patterns
- Do not OCR born-digital PDFs just because the task mentions extraction. Extract first and OCR only if the text layer is missing.
- Do not flatten forms or annotations until the user confirms the artifact no longer needs to stay editable.
- Do not sign, archive, or linearize intermediate working files. Keep those as final-delivery steps.
- Do not promise PDF/A or PDF/UA compliance without a validation step when the requirement is contractual.
- Do not commit temporary workflow scripts under `scripts/`.

## Reference map
Read only what you need:

- `references/request-basics.md` -> endpoint model, auth, multipart vs JSON, credits, limits, and errors
- `references/generation-and-conversion.md` -> HTML/URL generation and format conversion
- `references/pdf-manipulation.md` -> merge, split, page-range, rotate, and flatten workflows
- `references/extraction-and-ocr.md` -> OCR, text extraction, tables, and key-value workflows
- `references/security-signing-and-forms.md` -> redaction, watermarking, signatures, forms, and passwords
- `references/compliance-and-optimization.md` -> PDF/A, PDF/UA, optimization, and linearization
- `references/workflow-recipes.md` -> end-to-end sequencing patterns for common business document workflows

## Rules
- Fail fast when required arguments are missing.
- Write outputs to explicit paths and print created files.
- Do not log secrets.
- All client methods are async and should run via `asyncio.run(main())`.
- If import fails, install dependency with `uv add nutrient-dws`.

## Security Hardening Addendum

- Prefer a pinned, preinstalled MCP server binary over runtime package fetches.
  - Preferred: `npm i -g @nutrient-sdk/dws-mcp-server@<pinned-version>`
  - Avoid unpinned runtime fetch in production paths.
- Never store `NUTRIENT_DWS_API_KEY` in committed JSON config files.
  - Use process env injection at runtime (shell/export, secrets manager, or host env).
- Restrict file access with `SANDBOX_PATH` to the minimum required working directory.
- Before enabling MCP mode in production, verify package provenance and lock version.

```

## File: `nutrient-document-processing/agents/openai.yaml`
```yaml
interface:
  display_name: "Nutrient Document Processing"
  short_description: "Generate, convert, assemble, OCR, redact, sign, archive, and optimize documents"
  icon_small: "./assets/nutrient.svg"
  icon_large: "./assets/nutrient.svg"
  default_prompt: "Use $nutrient-document-processing to generate, convert, assemble, OCR, extract, redact, sign, fill, archive, optimize, or linearize this document, then return the output files and a concise summary."
```

## File: `nutrient-document-processing/assets/templates/custom-workflow-template.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

from nutrient_dws.builder.constant import BuildActions

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
from lib.common import create_client, write_workflow_output, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(description="Template for multi-step custom workflows.")
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args()

    client = create_client()

    # Customize this action list for the requested pipeline.
    actions = [
        BuildActions.ocr("english"),
        BuildActions.watermark_text("DRAFT", {"opacity": 0.25, "rotation": 45}),
    ]

    result = await (
        client.workflow()
        .add_file_part(args.input, actions=actions)
        .output_pdf()
        .execute()
    )
    write_workflow_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/references/REFERENCE.md`
```markdown
# Nutrient DWS Reference Index

Use this folder as a modular cookbook. Keep `SKILL.md` loaded as the router and open only the reference file that matches the task at hand.

## Reference map

- [request-basics.md](request-basics.md)
  Endpoint model, authentication, multipart vs JSON requests, credits, limits, and common errors.

- [generation-and-conversion.md](generation-and-conversion.md)
  PDF generation from HTML or URLs, Office/image conversion, and output-format selection.

- [pdf-manipulation.md](pdf-manipulation.md)
  Merge, split, reorder, rotate, and flatten PDF workflows.

- [extraction-and-ocr.md](extraction-and-ocr.md)
  OCR, text extraction, table extraction, and key-value workflows.

- [security-signing-and-forms.md](security-signing-and-forms.md)
  Redaction, watermarking, signing, form fill, and password-protected PDFs.

- [compliance-and-optimization.md](compliance-and-optimization.md)
  PDF/A archival output, PDF/UA auto-tagging, PDF optimization, and linearization.

- [workflow-recipes.md](workflow-recipes.md)
  Sequencing guidance for common multi-step business document workflows.

## Official docs

- [Processor API overview](https://www.nutrient.io/api/processor-api/)
- [General documentation](https://www.nutrient.io/api/documentation/)
- [Tools and APIs](https://www.nutrient.io/api/documentation/tools-and-api/)
- [API playground](https://dashboard.nutrient.io/processor-api/playground/)
```

## File: `nutrient-document-processing/references/compliance-and-optimization.md`
```markdown
# Compliance and Optimization

Use these patterns when the required output is archival, accessible, or tuned for delivery performance.

## PDF/A archival conversion

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document=@document.pdf \
  -F 'instructions={
    "parts": [
      {
        "file": "document"
      }
    ],
    "output": {
      "type": "pdfa",
      "conformance": "pdfa-2a",
      "vectorization": true,
      "rasterization": true
    }
  }' \
  -o result.pdf
```

Supported PDF/A targets include:

- `pdfa-1a`, `pdfa-1b`
- `pdfa-2a`, `pdfa-2u`, `pdfa-2b`
- `pdfa-3a`, `pdfa-3u`, `pdfa-3b`
- `pdfa-4`, `pdfa-4e`, `pdfa-4f`

### PDF/A caveat

To achieve conformance, conversion may vectorize or rasterize content. That can remove live text and font information, so later OCR may be needed.

## PDF/UA auto-tagging

Dedicated endpoint:

```bash
curl -X POST https://api.nutrient.io/processor/pdfua \
  -H "Content-Type: application/pdf" \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  --data-binary @document.pdf \
  -o result.pdf
```

Equivalent `/build` workflow:

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document=@document.pdf \
  -F 'instructions={
    "parts": [
      {
        "file": "document"
      }
    ],
    "output": {
      "type": "pdfua"
    }
  }' \
  -o result.pdf
```

### PDF/UA rules

- PDF/UA is an accessibility target, not just a format conversion.
- Clean born-digital PDFs generally tag better than rasterized or flattened inputs.
- Structured HTML sources also tend to produce better accessibility outcomes than image-only content.
- Validate final outputs with your required checker when accessibility compliance is contractual.

## PDF optimization and linearization

Linearize a PDF for fast web viewing:

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document=@document.pdf \
  -F 'instructions={
    "parts": [
      {
        "file": "document"
      }
    ],
    "output": {
      "type": "pdf",
      "optimize": {
        "linearize": true
      }
    }
  }' \
  -o result.pdf
```

Optimization with compression controls:

```json
{
  "parts": [{ "file": "document" }],
  "output": {
    "type": "pdf",
    "optimize": {
      "disableImages": false,
      "mrcCompression": true,
      "imageOptimizationQuality": 2,
      "linearize": true
    }
  }
}
```

### Optimization rules

- Linearize only for delivery PDFs meant for network viewing.
- Optimize before signatures when possible. Treat signed PDFs as immutable delivery artifacts.
- Compression changes should be validated visually when image quality matters.

## Official docs

- [PDF to PDF/A API](https://www.nutrient.io/api/pdf-to-pdfa-api/)
- [PDF/UA auto-tagging API](https://www.nutrient.io/api/pdfua-auto-tagging-api/)
- [Optimization API](https://www.nutrient.io/api/document-optimization-api/)
- [PDF linearization API](https://www.nutrient.io/api/pdf-linearization-api/)
```

## File: `nutrient-document-processing/references/extraction-and-ocr.md`
```markdown
# Extraction and OCR

Use these patterns when the goal is to pull machine-readable data from PDFs or scans.

## Extract plain text

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"output":{"type":"text"}}' \
  -o extracted.txt
```

## Extract tables

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"extraction","strategy":"tables"}],"output":{"type":"xlsx"}}' \
  -o tables.xlsx
```

Common structured outputs: `xlsx`, `json`, `xml`, `csv`

## Extract key-value pairs

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"extraction","strategy":"key-values"}],"output":{"type":"json"}}' \
  -o pairs.json
```

## Basic OCR

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F scanned.pdf=@scanned.pdf \
  -F 'instructions={"parts":[{"file":"scanned.pdf"}],"actions":[{"type":"ocr","language":"english"}]}' \
  -o searchable.pdf
```

## Multi-language OCR

```json
{
  "parts": [{ "file": "scanned.pdf" }],
  "actions": [{ "type": "ocr", "language": ["english", "german", "french"] }]
}
```

## OCR on images

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F scan.jpg=@scan.jpg \
  -F 'instructions={"parts":[{"file":"scan.jpg"}],"actions":[{"type":"ocr","language":"english"}]}' \
  -o searchable.pdf
```

## OCR languages

Common OCR languages include:

- `english`
- `german`
- `french`
- `spanish`
- `italian`
- `portuguese`
- `dutch`
- `swedish`
- `polish`
- `czech`
- `turkish`
- `japanese`
- `korean`
- `chinese-simplified`
- `chinese-traditional`
- `arabic`
- `hebrew`
- `hindi`
- `russian`

## OCR and extraction rules

- OCR before extraction when text is image-only, unselectable, or suspiciously sparse.
- Tables and key-values benefit from cleaner scans and correct page orientation.
- For multilingual inputs, pass an array of languages rather than guessing a single language.
- If OCR quality is poor, fix source orientation and scan quality before retrying.

## Official docs

- [Data extraction overview](https://www.nutrient.io/api/data-extraction-api/)
- [Processor API overview](https://www.nutrient.io/api/processor-api/)
```

## File: `nutrient-document-processing/references/generation-and-conversion.md`
```markdown
# Generation and Conversion

Use these patterns when the main task is to generate a new document or convert an existing one into another format.

## HTML to PDF generation

Upload the HTML file and reference it through `parts[].html`.

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F index.html=@index.html \
  -F 'instructions={"parts":[{"html":"index.html"}]}' \
  -o result.pdf
```

With layout options:

```json
{
  "parts": [{ "html": "index.html" }],
  "output": {
    "type": "pdf",
    "layout": {
      "orientation": "landscape",
      "size": "A4",
      "margin": { "top": 20, "bottom": 20, "left": 15, "right": 15 }
    }
  }
}
```

## Remote URL generation or conversion

When the input already lives at a stable remote URL, send a JSON request and use `file.url`:

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -d '{
    "parts": [
      {
        "file": {
          "url": "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"
        }
      }
    ]
  }' \
  -o result.pdf
```

Use this pattern when you want server-side fetches and do not need to upload a local file first.

## Office to PDF

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.docx=@document.docx \
  -F 'instructions={"parts":[{"file":"document.docx"}]}' \
  -o result.pdf
```

Supported common inputs: `docx`, `xlsx`, `pptx`, `doc`, `xls`, `ppt`, `odt`, `ods`, `odp`, `rtf`

## Image to PDF

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F photo.jpg=@photo.jpg \
  -F 'instructions={"parts":[{"file":"photo.jpg"}]}' \
  -o result.pdf
```

Supported common images: `jpg`, `jpeg`, `png`, `gif`, `webp`, `tiff`, `bmp`

## PDF to Office

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"output":{"type":"docx"}}' \
  -o result.docx
```

Supported common outputs: `docx`, `xlsx`, `pptx`

## PDF to image

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf","pages":{"start":0,"end":0}}],"output":{"type":"png","dpi":150}}' \
  -o page.png
```

Useful output options:

| Option | Meaning |
|--------|---------|
| `type` | `png`, `jpeg`, or `webp` |
| `dpi` | Resolution target |
| `width` / `height` | Explicit pixel size |

## Generation and conversion rules

- Use HTML generation when you control the markup and need stable, reproducible output.
- Use remote URL requests when the source already exists online and you want to avoid local uploads.
- Use `output.type` for direct conversions. Do not create unnecessary `actions` for simple format changes.
- For paginated image output, render only the pages you need.

## Official docs

- [PDF generator / converter overview](https://www.nutrient.io/api/pdf-converter-api/)
- [URL to PDF API](https://www.nutrient.io/api/url-to-pdf-api/)
```

## File: `nutrient-document-processing/references/pdf-manipulation.md`
```markdown
# PDF Manipulation

Use these patterns when the task is about assembling, slicing, or normalizing PDFs before final delivery operations.

## Merge PDFs

Part order controls merge order:

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F cover=@cover.pdf \
  -F body=@body.pdf \
  -F appendix=@appendix.pdf \
  -F 'instructions={
    "parts": [
      { "file": "cover" },
      { "file": "body" },
      { "file": "appendix" }
    ]
  }' \
  -o packet.pdf
```

## Split or extract page ranges

Use `pages` on a part to carve out a subset:

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document=@document.pdf \
  -F 'instructions={
    "parts": [
      {
        "file": "document",
        "pages": { "start": 0, "end": 4 }
      }
    ]
  }' \
  -o first-five-pages.pdf
```

## Reorder or assemble a packet from ranges

Reuse the same source part with different page ranges to build a new packet:

```json
{
  "parts": [
    { "file": "document", "pages": { "start": 5, "end": 9 } },
    { "file": "document", "pages": { "start": 0, "end": 4 } }
  ]
}
```

## Rotate pages

Use a rotation action when page orientation is wrong:

```json
{
  "parts": [{ "file": "document.pdf" }],
  "actions": [
    {
      "type": "rotate",
      "rotation": 90,
      "pages": [0, 1, 2]
    }
  ]
}
```

## Flatten forms or annotations

Flatten only when the output should stop being interactive:

```json
{
  "parts": [{ "file": "document.pdf" }],
  "actions": [{ "type": "flatten" }]
}
```

## Rules

- Page indexes are zero-based. `end: -1` means the last page.
- Assemble the full packet before watermarking, signing, optimizing, or linearizing.
- Rotate before rasterizing or signing if the source orientation is incorrect.
- Flatten late. It removes editability from forms and many annotation workflows.
- Keep passwords on the affected `part` when slicing or merging encrypted inputs.

## Official docs

- [Processor API overview](https://www.nutrient.io/api/processor-api/)
- [Tools and APIs](https://www.nutrient.io/api/documentation/tools-and-api/)
```

## File: `nutrient-document-processing/references/request-basics.md`
```markdown
# Request Basics

Most Nutrient DWS workflows use:

```text
POST https://api.nutrient.io/build
Authorization: Bearer YOUR_API_KEY
```

Use multipart when you are uploading local files. Use JSON when every input is a remote URL.

## Multipart pattern

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document=@document.pdf \
  -F 'instructions={"parts":[{"file":"document"}]}' \
  -o result.pdf
```

## JSON pattern for remote URLs

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -d '{
    "parts": [
      {
        "file": {
          "url": "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"
        }
      }
    ]
  }' \
  -o result.pdf
```

## Instructions model

```json
{
  "parts": [
    {
      "file": "document.pdf",
      "pages": { "start": 0, "end": -1 },
      "password": "optional-password"
    }
  ],
  "actions": [
    { "type": "action_type" }
  ],
  "output": {
    "type": "pdf"
  }
}
```

## Core rules

- Multipart field names must match the filenames or symbolic names referenced in `parts`.
- `parts` preserves order. Multiple parts become a merged output unless the selected output type says otherwise.
- `actions` execute in order and mutate the in-flight document.
- `output.type` selects the final artifact type such as `pdf`, `text`, `docx`, `xlsx`, `pptx`, `png`, `pdfa`, or `pdfua`.
- Password-protected inputs need `password` on the relevant part.

## Credits

Check balance:

```bash
curl -X GET https://api.nutrient.io/credits \
  -H "Authorization: Bearer $NUTRIENT_API_KEY"
```

Check usage:

```bash
curl -X GET "https://api.nutrient.io/credits/usage?period=month" \
  -H "Authorization: Bearer $NUTRIENT_API_KEY"
```

## Limits and common errors

### HTTP status codes

| Code | Meaning |
|------|---------|
| `200` | Success |
| `400` | Invalid instructions or missing required fields |
| `401` | Invalid or missing API key |
| `402` | Insufficient credits |
| `413` | Payload too large |
| `415` | Unsupported media type |
| `422` | Valid request but unsupported or unprocessable content |
| `429` | Rate limited |
| `500` | Server error |

### Common problems

| Problem | Cause | Fix |
|---------|-------|-----|
| `file_not_found` | The symbolic file name in `parts` does not match an uploaded field | Align multipart names and `parts` references |
| Empty extraction | The file is scanned or rasterized | OCR first |
| `password_required` | The PDF is encrypted | Add the password on the part |
| `insufficient_credits` | Batch or AI-heavy workflow exceeded credits | Check balance before the run |

### File limits

- Maximum input file: 100 MB
- Maximum total upload: 500 MB per request
- For faster runs, prefer files below 50 MB when possible

## Official docs

- [API overview](https://www.nutrient.io/api/documentation/developer-guides/api-overview/)
- [Processor API overview](https://www.nutrient.io/api/processor-api/)
```

## File: `nutrient-document-processing/references/security-signing-and-forms.md`
```markdown
# Security, Signing, and Forms

Use these patterns when the task is about redaction, watermarking, signatures, form fill, or document protection.

## Preset redaction

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"redaction","strategy":"preset","preset":"email-address"}]}' \
  -o redacted.pdf
```

Common presets:

- `social-security-number`
- `credit-card-number`
- `email-address`
- `north-american-phone-number`
- `international-phone-number`
- `date`
- `url`
- `ipv4`
- `ipv6`
- `mac-address`
- `us-zip-code`
- `vin`
- `time`

## Regex redaction

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"redaction","strategy":"regex","regex":"\\b\\d{3}-\\d{2}-\\d{4}\\b","caseSensitive":false}]}' \
  -o redacted.pdf
```

## AI redaction

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"ai_redaction","criteria":"All personally identifiable information"}]}' \
  -o redacted.pdf
```

Use AI redaction for contextual asks. Use preset or regex redaction for explicit patterns.

## Text watermark

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"watermark","watermarkType":"text","text":"DRAFT","fontSize":72,"fontColor":"#FF0000","opacity":0.3,"rotation":45,"width":"50%","height":"50%"}]}' \
  -o watermarked.pdf
```

## Image watermark

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F logo.png=@logo.png \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"watermark","watermarkType":"image","imagePath":"logo.png","width":"25%","height":"25%","opacity":0.5}]}' \
  -o watermarked.pdf
```

## CMS signature

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"sign","signatureType":"cms","signerName":"John Doe","reason":"Document approval","location":"San Francisco"}]}' \
  -o signed.pdf
```

## CAdES signature

```bash
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F document.pdf=@document.pdf \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"sign","signatureType":"cades","cadesLevel":"b-lt","signerName":"Jane Smith"}]}' \
  -o signed.pdf
```

## Fill form fields

```json
{
  "parts": [{ "file": "form.pdf" }],
  "actions": [{
    "type": "fillForm",
    "fields": [
      { "name": "firstName", "value": "John" },
      { "name": "lastName", "value": "Doe" },
      { "name": "email", "value": "john@example.com" },
      { "name": "agree", "value": true }
    ]
  }]
}
```

## Encrypt output

```json
{
  "parts": [{ "file": "document.pdf" }],
  "output": {
    "type": "pdf",
    "owner_password": "owner123",
    "user_password": "user456"
  }
}
```

## Open a password-protected input

```json
{
  "parts": [{ "file": "protected.pdf", "password": "user456" }]
}
```

## Rules

- Redact before signing. Signed documents should be treated as final artifacts.
- Deterministic redaction is easier to verify than AI redaction.
- Confirm real signing requirements before promising a legally sufficient workflow.
- Use real field names for form fill. Do not guess from visible labels.

## Official docs

- [Tools and APIs](https://www.nutrient.io/api/documentation/tools-and-api/)
```

## File: `nutrient-document-processing/references/workflow-recipes.md`
```markdown
# Workflow Recipes

Use these patterns when the task spans more than one DWS feature and ordering matters.

## 1. Scan to searchable text

Goal: take an image-only PDF and produce both a searchable PDF and extracted text.

Recommended sequence:

1. OCR the source PDF into a searchable PDF.
2. Extract text from the searchable result.

Reasoning: OCR improves extraction quality and gives you a reusable intermediate artifact.

## 2. Scan to redacted delivery PDF

Goal: redact a scanned document and deliver a shareable PDF.

Recommended sequence:

1. OCR
2. Preset or regex redaction
3. Optional watermark
4. Optional optimization or linearization
5. Signature last, if required

Reasoning: OCR enables reliable matching, and signatures should only happen after all content mutations are complete.

## 3. HTML report to archival PDF

Goal: generate a PDF from structured content and archive it.

Recommended sequence:

1. Generate PDF from HTML
2. Convert the result to PDF/A
3. Validate the archival output in your downstream compliance workflow if required

Reasoning: HTML generation gives you better structure control than post-hoc browser printing, and PDF/A should be treated as a final archival artifact.

## 4. Existing PDF to accessible PDF/UA

Goal: turn a born-digital PDF into a screen-reader-ready artifact.

Recommended sequence:

1. Start from the cleanest available PDF
2. Run PDF/UA auto-tagging
3. Validate the result with your required accessibility checker

Reasoning: flattened, rasterized, or noisy inputs reduce tagging quality.

## 5. Form packet to signed output

Goal: fill a form, remove interactivity if needed, and sign it.

Recommended sequence:

1. Fill form fields
2. Optional flattening
3. Signature last

Reasoning: signing too early forces a second mutation pass and can invalidate the signed artifact.

## 6. Web delivery PDF

Goal: publish a PDF that streams quickly in viewers.

Recommended sequence:

1. Final content edits
2. Optional compression
3. Linearization
4. Publish to a server that supports byte-range requests

Reasoning: linearization is a delivery concern, not an authoring concern.

## 7. Packet assembly before signing

Goal: merge multiple PDFs, fix page orientation, and produce a final packet for signing or distribution.

Recommended sequence:

1. Merge or reorder the required parts
2. Extract or omit page ranges as needed
3. Optional page rotation
4. Optional flattening
5. Watermark, sign, optimize, or linearize last

Reasoning: assembly and page normalization are still content mutations. Final-artifact operations should happen only after the packet shape is stable.

## Recipe heuristics

- Keep OCR early.
- Keep compliance targets intentional.
- Keep signatures last.
- Treat optimization as a delivery-stage step unless the workflow explicitly needs it earlier.
```

## File: `nutrient-document-processing/scripts/add-pages.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(description="Add blank pages to a PDF.")
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--count", required=True, type=int, help="Number of blank pages to add."
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument("--index", type=int, help="Insertion index (0-based; default: end).")
    args = parser.parse_args(fix_negative_args())

    if args.count <= 0:
        parser.error("--count must be a positive integer.")

    client = create_client()
    result = await client.add_page(args.input, args.count, args.index)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/convert.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a document to another format.")
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument(
        "--format",
        required=True,
        help="Target format: pdf, pdfa, pdfua, docx, xlsx, pptx, png, jpeg, jpg, webp, html, markdown",
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args()

    client = create_client()
    result = await client.convert(args.input, args.format)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/delete-pages.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_integer_csv, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Delete specific pages from a PDF.",
        epilog="Example: uv run scripts/delete-pages.py --input doc.pdf --pages 0,2,-1 --out doc-without-pages.pdf",
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--pages", required=True, help="Comma-separated 0-based page indices to delete."
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args(fix_negative_args())

    page_indices = parse_integer_csv(args.pages)
    if not page_indices:
        parser.error("--pages must include at least one index.")

    client = create_client()
    result = await client.delete_pages(args.input, page_indices)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/duplicate-pages.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_integer_csv, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a new PDF from specific page indices (supports duplicates/reordering).",
        epilog="Example: uv run scripts/duplicate-pages.py --input doc.pdf --pages 2,0,1,1 --out reordered.pdf",
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--pages", required=True, help="Comma-separated 0-based page indices to include."
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args(fix_negative_args())

    page_indices = parse_integer_csv(args.pages)
    if not page_indices:
        parser.error("--pages must include at least one index.")

    client = create_client()
    result = await client.duplicate_pages(args.input, page_indices)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/extract-key-value-pairs.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_json_output, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract key-value pairs from forms or structured documents."
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--out", required=True, help="Output JSON file path.")
    parser.add_argument("--pages", help="Page range in start:end format.")
    args = parser.parse_args(fix_negative_args())

    pages = parse_page_range(args.pages) if args.pages else None

    client = create_client()
    result = await client.extract_key_value_pairs(args.input, pages)
    write_json_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/extract-table.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_json_output, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(description="Extract table data from a document.")
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--out", required=True, help="Output JSON file path.")
    parser.add_argument("--pages", help="Page range in start:end format.")
    args = parser.parse_args(fix_negative_args())

    pages = parse_page_range(args.pages) if args.pages else None

    client = create_client()
    result = await client.extract_table(args.input, pages)
    write_json_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/extract-text.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_json_output, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract text from a document as JSON, with optional plain-text export."
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--out", required=True, help="Output JSON file path.")
    parser.add_argument("--pages", help="Page range in start:end format.")
    parser.add_argument("--plain-out", dest="plain_out", help="Optional plain-text output file.")
    args = parser.parse_args(fix_negative_args())

    pages = parse_page_range(args.pages) if args.pages else None

    client = create_client()
    result = await client.extract_text(args.input, pages)
    write_json_output(result, args.out)

    if args.plain_out:
        text = "\n\n".join(
            page.get("plainText", "")
            for page in result["data"].get("pages", [])
            if page.get("plainText")
        )
        plain_path = Path(args.plain_out)
        plain_path.parent.mkdir(parents=True, exist_ok=True)
        plain_path.write_text(text, encoding="utf-8")
        print(f"Wrote {args.plain_out}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/merge.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(description="Merge multiple documents into one PDF.")
    parser.add_argument(
        "--inputs",
        required=True,
        help="Comma-separated list of input file paths or URLs (at least 2).",
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args()

    inputs = [f.strip() for f in args.inputs.split(",") if f.strip()]
    if len(inputs) < 2:
        parser.error("--inputs must contain at least 2 files.")

    client = create_client()
    result = await client.merge(inputs)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/ocr.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_csv, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run OCR on a document.",
        epilog="Example: uv run scripts/ocr.py --input scan.pdf --languages english --out scan-ocr.pdf",
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument(
        "--languages", required=True, help="Comma-separated language(s) for OCR (e.g. english,german)."
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    args = parser.parse_args()

    languages = parse_csv(args.languages)
    language_arg = languages[0] if len(languages) == 1 else languages

    client = create_client()
    result = await client.ocr(args.input, language_arg)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/optimize.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, read_json_file, parse_json_string, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Optimize PDF size and quality.",
        epilog="Example: uv run scripts/optimize.py --input large.pdf --out optimized.pdf --options-json '{\"mrcCompression\":true}'",
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument(
        "--options-json-file",
        dest="options_json_file",
        help="Path to JSON file with optimization options.",
    )
    parser.add_argument(
        "--options-json", dest="options_json", help="JSON string with optimization options."
    )
    args = parser.parse_args()

    options = None
    if args.options_json_file:
        options = read_json_file(args.options_json_file)
    if args.options_json:
        options = parse_json_string(args.options_json)

    client = create_client()
    result = await client.optimize(args.input, options)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/password-protect.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_csv, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(description="Protect a PDF with user/owner passwords.")
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--user-password", dest="user_password", required=True, help="User password."
    )
    parser.add_argument(
        "--owner-password", dest="owner_password", required=True, help="Owner password."
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument("--permissions", help="Comma-separated list of permissions.")
    args = parser.parse_args()

    permissions = parse_csv(args.permissions) if args.permissions else None

    client = create_client()
    result = await client.password_protect(
        args.input, args.user_password, args.owner_password, permissions
    )
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/redact-ai.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create AI redactions and optionally apply them.",
        epilog='Example: uv run scripts/redact-ai.py --input policy.pdf --criteria "Remove all emails" --mode apply --out redacted.pdf',
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--criteria", required=True, help="Natural-language redaction criteria.")
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument(
        "--mode",
        default="stage",
        choices=["stage", "apply"],
        help="Redaction mode: stage (default) or apply.",
    )
    parser.add_argument("--pages", help="Page range in start:end format.")
    args = parser.parse_args(fix_negative_args())

    pages = parse_page_range(args.pages) if args.pages else None

    client = create_client()
    result = await client.create_redactions_ai(args.input, args.criteria, args.mode, pages)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/rotate.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(description="Rotate pages in a PDF.")
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--angle",
        required=True,
        type=int,
        choices=[90, 180, 270],
        help="Rotation angle in degrees (90, 180, or 270).",
    )
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument("--pages", help="Page range in start:end format.")
    args = parser.parse_args(fix_negative_args())

    pages = parse_page_range(args.pages) if args.pages else None

    client = create_client()
    result = await client.rotate(args.input, args.angle, pages)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/sign.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import (
    create_client,
    write_binary_output,
    assert_local_file,
    read_json_file,
    parse_json_string,
    handle_error,
)


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Digitally sign a PDF.",
        epilog="Note: sign() only supports local file inputs for the main PDF.",
    )
    parser.add_argument("--input", required=True, help="Local path to the input PDF.")
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument(
        "--signature-json-file",
        dest="signature_json_file",
        help="Path to JSON file with signature data.",
    )
    parser.add_argument(
        "--signature-json", dest="signature_json", help="JSON string with signature data."
    )
    parser.add_argument("--image", help="Local path to a signature image.")
    parser.add_argument(
        "--graphic-image", dest="graphic_image", help="Local path to a graphic image."
    )
    args = parser.parse_args()

    input_path = assert_local_file(args.input, "input")

    signature_data = None
    if args.signature_json_file:
        signature_data = read_json_file(args.signature_json_file)
    if args.signature_json:
        signature_data = parse_json_string(args.signature_json)

    options: dict = {}
    if args.image:
        options["image"] = assert_local_file(args.image, "image")
    if args.graphic_image:
        options["graphicImage"] = assert_local_file(args.graphic_image, "graphic-image")

    client = create_client()
    result = await client.sign(input_path, signature_data, options or None)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/split.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, parse_csv, parse_page_range, handle_error, fix_negative_args


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split one PDF into multiple PDFs by page ranges.",
        epilog="Example: uv run scripts/split.py --input report.pdf --ranges 0:2,3:5,-2:-1 --out-dir out --prefix section",
    )
    parser.add_argument("--input", required=True, help="Path or URL to the input PDF.")
    parser.add_argument(
        "--ranges", required=True, help="Comma-separated page ranges in start:end format."
    )
    parser.add_argument("--out-dir", dest="out_dir", required=True, help="Output directory.")
    parser.add_argument(
        "--prefix", default="split", help="Filename prefix for output files (default: split)."
    )
    args = parser.parse_args(fix_negative_args())

    ranges_raw = parse_csv(args.ranges)
    if not ranges_raw:
        parser.error("--ranges requires at least one range in start:end format.")
    ranges = [parse_page_range(r) for r in ranges_raw]

    client = create_client()
    results = await client.split(args.input, ranges)

    for i, result in enumerate(results):
        output_path = str(Path(args.out_dir) / f"{args.prefix}-{str(i + 1).zfill(2)}.pdf")
        write_binary_output(result, output_path)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/watermark-text.py`
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["nutrient-dws"]
# ///

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.common import create_client, write_binary_output, handle_error


async def main() -> None:
    parser = argparse.ArgumentParser(description="Add a text watermark to a document.")
    parser.add_argument("--input", required=True, help="Path or URL to the input document.")
    parser.add_argument("--text", required=True, help="Watermark text.")
    parser.add_argument("--out", required=True, help="Output file path.")
    parser.add_argument("--opacity", type=float, help="Watermark opacity (0.0–1.0).")
    parser.add_argument("--font-size", dest="font_size", type=int, help="Font size in points.")
    parser.add_argument("--rotation", type=int, help="Rotation angle in degrees (integer).")
    args = parser.parse_args()

    options: dict = {}
    if args.opacity is not None:
        options["opacity"] = args.opacity
    if args.font_size is not None:
        options["fontSize"] = args.font_size
    if args.rotation is not None:
        options["rotation"] = args.rotation

    client = create_client()
    result = await client.watermark_text(args.input, args.text, options or None)
    write_binary_output(result, args.out)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        handle_error(e)
```

## File: `nutrient-document-processing/scripts/lib/common.py`
```python
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, NoReturn

_NEGATIVE_VALUE_RE = re.compile(r"^-\d")


def create_client():
    """Create and return a NutrientClient using the NUTRIENT_API_KEY env var."""
    api_key = os.environ.get("NUTRIENT_API_KEY")
    if not api_key:
        raise RuntimeError(
            "NUTRIENT_API_KEY is not set. Export it before running these scripts."
        )
    try:
        from nutrient_dws import NutrientClient
    except ImportError as e:
        raise RuntimeError(
            "Unable to import nutrient_dws. Install with: uv add nutrient-dws\n"
            f"Original error: {e}"
        ) from e
    return NutrientClient(api_key=api_key)


def write_binary_output(result: dict, path: str) -> None:
    """Write a BufferOutput result to disk."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(result["buffer"])
    mime = result.get("mimeType", "application/octet-stream")
    print(f"Wrote {path} ({mime})")


def write_json_output(result: dict, path: str) -> None:
    """Write a JsonContentOutput result to disk (only the data portion)."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result["data"], f, indent=2)
    print(f"Wrote {path}")


def write_workflow_output(result: dict, path: str) -> None:
    """Write a WorkflowResult to disk, raising on failure."""
    if not result.get("success") or not result.get("output"):
        errors = result.get("errors") or []
        msgs = "; ".join(
            str(e.get("error", e)) for e in errors
        )
        raise RuntimeError(f"Workflow failed: {msgs or 'unknown error'}")
    write_binary_output(result["output"], path)


def parse_page_range(value: str) -> dict:
    """Parse 'start:end' into {'start': int, 'end': int}."""
    parts = str(value).split(":")
    if len(parts) != 2:
        raise ValueError(
            f"Invalid page range '{value}'. Use start:end (e.g. 0:4 or -3:-1)."
        )
    result = {}
    if parts[0] != "":
        try:
            result["start"] = int(parts[0])
        except ValueError:
            raise ValueError(f"Invalid start in page range '{value}'.")
    if parts[1] != "":
        try:
            result["end"] = int(parts[1])
        except ValueError:
            raise ValueError(f"Invalid end in page range '{value}'.")
    if not result:
        raise ValueError(
            f"Invalid page range '{value}'. Use start:end (e.g. 0:4 or -3:-1)."
        )
    return result


def parse_csv(value: str) -> list[str]:
    """Split a comma-separated string into a list of trimmed, non-empty strings."""
    if not value:
        return []
    return [item.strip() for item in str(value).split(",") if item.strip()]


def parse_integer_csv(value: str) -> list[int]:
    """Split a comma-separated string into a list of integers."""
    result = []
    for item in parse_csv(value):
        try:
            result.append(int(item))
        except ValueError:
            raise ValueError(f"Invalid integer value: '{item}'")
    return result


def assert_local_file(value: str, arg: str) -> str:
    """Raise if value looks like a URL; otherwise return the path."""
    v = str(value).strip()
    if v.startswith("http://") or v.startswith("https://"):
        raise ValueError(f"--{arg} must be a local file path for this operation.")
    return v


def read_json_file(path: str) -> Any:
    """Read and parse a JSON file."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file ({path}): {e}") from e


def parse_json_string(s: str) -> Any:
    """Parse a JSON string."""
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}") from e


def fix_negative_args() -> list[str]:
    """Return sys.argv[1:] with negative numeric values joined to their flag.

    argparse treats values like ``-1`` or ``-1:3`` as unknown option flags when
    passed as a separate token. This helper reattaches them using ``=`` so that
    ``--pages -1`` becomes ``--pages=-1`` before argparse sees the arguments.
    """
    argv = sys.argv[1:]
    result = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if (
            arg.startswith("--")
            and "=" not in arg
            and i + 1 < len(argv)
            and _NEGATIVE_VALUE_RE.match(argv[i + 1])
        ):
            result.append(f"{arg}={argv[i + 1]}")
            i += 2
        else:
            result.append(arg)
            i += 1
    return result


def handle_error(e: Exception) -> NoReturn:
    """Print the error message and exit with code 1."""
    print(str(e), file=sys.stderr)
    sys.exit(1)
```

## File: `nutrient-document-processing/tests/testing-guide.md`
```markdown
# Testing Guide

## Requirements

- Python 3.10+
- `uv` on `PATH`
- `NUTRIENT_API_KEY` set
- **Multi-page PDF input** (3+ pages recommended for comprehensive testing)

```bash
export NUTRIENT_API_KEY="nutr_sk_..."
# NOTE: Use a multi-page PDF (3+ pages required for split.py and delete-pages.py)
PDF=/path/to/your/input.pdf
OUT=/tmp/ndp-test
mkdir -p "$OUT"
```

Run commands from repository root.

## 1. Smoke tests

All scripts should print help and exit 0:

```bash
uv run nutrient-document-processing/scripts/convert.py --help
uv run nutrient-document-processing/scripts/merge.py --help
uv run nutrient-document-processing/scripts/split.py --help
uv run nutrient-document-processing/scripts/ocr.py --help
uv run nutrient-document-processing/scripts/extract-text.py --help
uv run nutrient-document-processing/scripts/extract-table.py --help
uv run nutrient-document-processing/scripts/extract-key-value-pairs.py --help
uv run nutrient-document-processing/scripts/watermark-text.py --help
uv run nutrient-document-processing/scripts/redact-ai.py --help
uv run nutrient-document-processing/scripts/rotate.py --help
uv run nutrient-document-processing/scripts/sign.py --help
uv run nutrient-document-processing/scripts/optimize.py --help
uv run nutrient-document-processing/scripts/password-protect.py --help
uv run nutrient-document-processing/scripts/add-pages.py --help
uv run nutrient-document-processing/scripts/delete-pages.py --help
uv run nutrient-document-processing/scripts/duplicate-pages.py --help
```

## 2. Single-operation happy-path checks

```bash
uv run nutrient-document-processing/scripts/convert.py --input "$PDF" --format docx --out "$OUT/convert.docx"
uv run nutrient-document-processing/scripts/merge.py --inputs "$PDF,$PDF" --out "$OUT/merge.pdf"
uv run nutrient-document-processing/scripts/split.py --input "$PDF" --ranges "0:1" --out-dir "$OUT/split" --prefix part
uv run nutrient-document-processing/scripts/ocr.py --input "$PDF" --languages english --out "$OUT/ocr.pdf"
uv run nutrient-document-processing/scripts/extract-text.py --input "$PDF" --out "$OUT/text.json"
uv run nutrient-document-processing/scripts/extract-table.py --input "$PDF" --out "$OUT/tables.json"
uv run nutrient-document-processing/scripts/extract-key-value-pairs.py --input "$PDF" --out "$OUT/kvp.json"
uv run nutrient-document-processing/scripts/watermark-text.py --input "$PDF" --text CONFIDENTIAL --out "$OUT/watermark.pdf"
uv run nutrient-document-processing/scripts/redact-ai.py --input "$PDF" --criteria "Remove all SSNs" --mode stage --out "$OUT/redact-stage.pdf"
uv run nutrient-document-processing/scripts/rotate.py --input "$PDF" --angle 90 --out "$OUT/rotate.pdf"
uv run nutrient-document-processing/scripts/sign.py --input "$PDF" --out "$OUT/sign.pdf"
uv run nutrient-document-processing/scripts/optimize.py --input "$PDF" --out "$OUT/optimize.pdf"
uv run nutrient-document-processing/scripts/password-protect.py --input "$PDF" --user-password upass --owner-password opass --out "$OUT/protected.pdf"
uv run nutrient-document-processing/scripts/add-pages.py --input "$PDF" --count 1 --out "$OUT/add-pages.pdf"
uv run nutrient-document-processing/scripts/delete-pages.py --input "$PDF" --pages 0 --out "$OUT/delete-pages.pdf"
uv run nutrient-document-processing/scripts/duplicate-pages.py --input "$PDF" --pages 1,0,1 --out "$OUT/duplicate-pages.pdf"
```

## 3. Multi-step workflow behavior

No multi-step script should exist in `scripts/`.

Build runtime pipelines in a temporary file using the template:

```bash
TMP_SCRIPT=/tmp/ndp-runtime-pipeline.py
cp nutrient-document-processing/assets/templates/custom-workflow-template.py "$TMP_SCRIPT"
# edit $TMP_SCRIPT for the requested pipeline
uv run "$TMP_SCRIPT" --input "$PDF" --out "$OUT/pipeline.pdf"
rm -f "$TMP_SCRIPT"
```

## 4. Pass criteria

- All `--help` commands succeed.
- Single-operation scripts produce output files (using a multi-page PDF).
- Multi-step workflows are run from temporary scripts only.
- No committed pipeline scripts exist in `nutrient-document-processing/scripts/`.

**Note:** Single-page PDFs will cause failures in `split.py` and `delete-pages.py`. Use a multi-page PDF (3+ pages) for complete test coverage.
```

## File: `tapes/demo.tape`
```
# Demo GIF: Redact PII from a PDF
# Runs a simulated Claude Code UI — does NOT launch real claude

Output assets/demo.gif
Set Width 840
Set Height 480
Set FontSize 14
Set FontFamily "JetBrains Mono"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 0
Set Padding 20
Set Framerate 15

Hide
Type "bash tapes/helpers/demo-full.sh"
Enter
Show
Sleep 15s
```

## File: `tapes/workflow-fill-sign.tape`
```
# Workflow GIF: Fill form + digital signature
# Runs a simulated Claude Code UI

Output assets/workflow-fill-sign.gif
Set Width 840
Set Height 560
Set FontSize 14
Set FontFamily "JetBrains Mono"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 0
Set Padding 20
Set Framerate 15

Hide
Type "bash tapes/helpers/fill-sign-full.sh"
Enter
Show
Sleep 18s
```

## File: `tapes/workflow-ocr.tape`
```
# Workflow GIF: OCR + text extraction
# Runs a simulated Claude Code UI

Output assets/workflow-ocr.gif
Set Width 840
Set Height 520
Set FontSize 14
Set FontFamily "JetBrains Mono"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 0
Set Padding 20
Set Framerate 15

Hide
Type "bash tapes/helpers/ocr-full.sh"
Enter
Show
Sleep 18s
```

## File: `tapes/helpers/demo-full.sh`
```bash
#!/bin/bash
# Full simulated Claude Code session — redact PII from a PDF
# Renders the entire UI frame by frame with realistic delays

# Colors matching Claude Code's TUI
BOLD='\033[1m'
DIM='\033[2m'
ITALIC='\033[3m'
RESET='\033[0m'
WHITE='\033[97m'
GRAY='\033[90m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
MAGENTA='\033[35m'
BLUE='\033[34m'
BG_DARK='\033[48;5;236m'
ORANGE='\033[38;5;208m'

clear

# ── Claude Code header ──
echo -e "${BOLD}${ORANGE}╭────────────────────────────────────────────────────────────────────╮${RESET}"
echo -e "${BOLD}${ORANGE}│${RESET}  ${BOLD}${WHITE}◆ Claude Code${RESET}  ${DIM}v1.0.26${RESET}                                          ${BOLD}${ORANGE}│${RESET}"
echo -e "${BOLD}${ORANGE}╰────────────────────────────────────────────────────────────────────╯${RESET}"
echo
echo -e "  ${DIM}cwd: ~/projects/patient-data${RESET}"
echo
sleep 0.8

# ── User prompt ──
echo -e "${BOLD}${BLUE}❯${RESET} ${WHITE}Redact all SSNs and email addresses from patient-records.pdf${RESET}"
echo
sleep 1.2

# ── Thinking indicator ──
echo -ne "  ${DIM}${MAGENTA}⟡ Thinking…${RESET}"
sleep 1.5
echo -e "\r  ${DIM}${MAGENTA}⟡ Thinking… done${RESET}                    "
echo

# ── Skill activation ──
echo -e "  ${DIM}Using skill: ${CYAN}nutrient-document-processing${RESET}"
echo
sleep 0.6

# ── Tool call ──
echo -e "  ${YELLOW}⬡ Tool: nutrient_redact${RESET}"
echo -e "  ${DIM}┌──────────────────────────────────────────────────────────────┐${RESET}"
echo -e "  ${DIM}│${RESET}  input:    ${WHITE}patient-records.pdf${RESET}                                ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  output:   ${WHITE}patient-records-redacted.pdf${RESET}                        ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  patterns: ${CYAN}[social-security-number, email-address]${RESET}              ${DIM}│${RESET}"
echo -e "  ${DIM}└──────────────────────────────────────────────────────────────┘${RESET}"
echo
sleep 0.8

# ── Processing animation ──
for i in 1 2 3; do
    echo -ne "\r  ${YELLOW}⏳ Calling Nutrient DWS API"
    for j in $(seq 1 $i); do echo -ne "."; done
    echo -ne "${RESET}      "
    sleep 0.5
done
echo -e "\r  ${GREEN}✓${RESET} ${WHITE}API call complete${RESET} ${DIM}(1.2s, 2 credits used)${RESET}          "
echo
sleep 0.5

# ── Results ──
echo -e "  ${GREEN}${BOLD}Redaction complete:${RESET}"
echo -e "    ${WHITE}•${RESET} ${BOLD}4${RESET} Social Security Numbers redacted"
echo -e "    ${WHITE}•${RESET} ${BOLD}7${RESET} email addresses redacted"
echo -e "    ${WHITE}•${RESET} ${BOLD}11${RESET} total redaction annotations applied"
echo
sleep 0.5

echo -e "  ${GREEN}📄 Created:${RESET} ${BOLD}${WHITE}patient-records-redacted.pdf${RESET} ${DIM}(248 KB)${RESET}"
echo
echo -e "  ${DIM}All matched patterns have been permanently removed from the document.${RESET}"
echo -e "  ${DIM}The redacted areas are filled with black boxes and the underlying${RESET}"
echo -e "  ${DIM}text has been irreversibly deleted.${RESET}"
echo

# Hold the final frame
sleep 5
```

## File: `tapes/helpers/fill-sign-full.sh`
```bash
#!/bin/bash
# Full simulated Claude Code session — fill form + digital signature

BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'
WHITE='\033[97m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
MAGENTA='\033[35m'
BLUE='\033[34m'
ORANGE='\033[38;5;208m'

clear

# ── Claude Code header ──
echo -e "${BOLD}${ORANGE}╭────────────────────────────────────────────────────────────────────╮${RESET}"
echo -e "${BOLD}${ORANGE}│${RESET}  ${BOLD}${WHITE}◆ Claude Code${RESET}  ${DIM}v1.0.26${RESET}                                          ${BOLD}${ORANGE}│${RESET}"
echo -e "${BOLD}${ORANGE}╰────────────────────────────────────────────────────────────────────╯${RESET}"
echo
echo -e "  ${DIM}cwd: ~/projects/hr-onboarding${RESET}"
echo
sleep 0.8

# ── User prompt ──
echo -e "${BOLD}${BLUE}❯${RESET} ${WHITE}Fill employee-onboarding.pdf with name 'Jane Smith', start date${RESET}"
echo -e "  ${WHITE}'2026-03-01', department 'Engineering', then sign it${RESET}"
echo
sleep 1.2

# ── Thinking ──
echo -ne "  ${DIM}${MAGENTA}⟡ Thinking…${RESET}"
sleep 1.2
echo -e "\r  ${DIM}${MAGENTA}⟡ Thinking… done${RESET}                    "
echo

echo -e "  ${DIM}Using skill: ${CYAN}nutrient-document-processing${RESET}"
echo
sleep 0.5

# ── Step 1: Fill form ──
echo -e "  ${YELLOW}⬡ Step 1: nutrient_fill_form${RESET}"
echo -e "  ${DIM}┌──────────────────────────────────────────────────────────────┐${RESET}"
echo -e "  ${DIM}│${RESET}  input:  ${WHITE}employee-onboarding.pdf${RESET}                                ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  fields:                                                      ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}    ${CYAN}employee_name${RESET}:  ${WHITE}\"Jane Smith\"${RESET}                              ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}    ${CYAN}start_date${RESET}:     ${WHITE}\"2026-03-01\"${RESET}                             ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}    ${CYAN}department${RESET}:     ${WHITE}\"Engineering\"${RESET}                            ${DIM}│${RESET}"
echo -e "  ${DIM}└──────────────────────────────────────────────────────────────┘${RESET}"
echo
sleep 0.6

echo -ne "  ${YELLOW}⏳ Filling form fields...${RESET}"
sleep 1
echo -e "\r  ${GREEN}✓${RESET} ${WHITE}Form filled${RESET} ${DIM}(0.8s, 1 credit used)${RESET}               "
echo
sleep 0.4

# ── Step 2: Sign ──
echo -e "  ${YELLOW}⬡ Step 2: nutrient_sign${RESET}"
echo -e "  ${DIM}┌──────────────────────────────────────────────────────────────┐${RESET}"
echo -e "  ${DIM}│${RESET}  input:         ${WHITE}employee-onboarding-filled.pdf${RESET}                  ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  output:        ${WHITE}employee-onboarding-signed.pdf${RESET}                  ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  signatureType: ${CYAN}cms${RESET}                                             ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  signerName:    ${WHITE}\"Jane Smith\"${RESET}                                   ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  reason:        ${WHITE}\"Employee onboarding\"${RESET}                          ${DIM}│${RESET}"
echo -e "  ${DIM}└──────────────────────────────────────────────────────────────┘${RESET}"
echo
sleep 0.6

echo -ne "  ${YELLOW}⏳ Applying digital signature...${RESET}"
sleep 1.2
echo -e "\r  ${GREEN}✓${RESET} ${WHITE}Document signed${RESET} ${DIM}(1.1s, 1 credit used)${RESET}          "
echo
sleep 0.4

# ── Results ──
echo -e "  ${GREEN}${BOLD}Done:${RESET}"
echo -e "    ${WHITE}•${RESET} 3 form fields filled"
echo -e "    ${WHITE}•${RESET} CMS digital signature applied"
echo -e "    ${WHITE}•${RESET} Total: 2 credits used"
echo
echo -e "  ${GREEN}📄 Created:${RESET} ${BOLD}${WHITE}employee-onboarding-signed.pdf${RESET} ${DIM}(342 KB)${RESET}"
echo

sleep 5
```

## File: `tapes/helpers/ocr-full.sh`
```bash
#!/bin/bash
# Full simulated Claude Code session — OCR + text extraction

BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'
WHITE='\033[97m'
GRAY='\033[90m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
MAGENTA='\033[35m'
BLUE='\033[34m'
ORANGE='\033[38;5;208m'

clear

# ── Claude Code header ──
echo -e "${BOLD}${ORANGE}╭────────────────────────────────────────────────────────────────────╮${RESET}"
echo -e "${BOLD}${ORANGE}│${RESET}  ${BOLD}${WHITE}◆ Claude Code${RESET}  ${DIM}v1.0.26${RESET}                                          ${BOLD}${ORANGE}│${RESET}"
echo -e "${BOLD}${ORANGE}╰────────────────────────────────────────────────────────────────────╯${RESET}"
echo
echo -e "  ${DIM}cwd: ~/projects/legal-docs${RESET}"
echo
sleep 0.8

# ── User prompt ──
echo -e "${BOLD}${BLUE}❯${RESET} ${WHITE}OCR scanned-contract.pdf in English and extract the text to contract.txt${RESET}"
echo
sleep 1.2

# ── Thinking ──
echo -ne "  ${DIM}${MAGENTA}⟡ Thinking…${RESET}"
sleep 1.2
echo -e "\r  ${DIM}${MAGENTA}⟡ Thinking… done${RESET}                    "
echo

echo -e "  ${DIM}Using skill: ${CYAN}nutrient-document-processing${RESET}"
echo
sleep 0.5

# ── Step 1: OCR ──
echo -e "  ${YELLOW}⬡ Step 1: nutrient_ocr${RESET}"
echo -e "  ${DIM}┌──────────────────────────────────────────────────────────────┐${RESET}"
echo -e "  ${DIM}│${RESET}  input:    ${WHITE}scanned-contract.pdf${RESET}                               ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  output:   ${WHITE}scanned-contract-ocr.pdf${RESET}                           ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  language: ${CYAN}english${RESET}                                             ${DIM}│${RESET}"
echo -e "  ${DIM}└──────────────────────────────────────────────────────────────┘${RESET}"
echo
sleep 0.6

for i in 1 2 3; do
    echo -ne "\r  ${YELLOW}⏳ Running OCR"
    for j in $(seq 1 $i); do echo -ne "."; done
    echo -ne "${RESET}      "
    sleep 0.5
done
echo -e "\r  ${GREEN}✓${RESET} ${WHITE}OCR complete${RESET} ${DIM}(2.8s, 4 credits used)${RESET}              "
echo
sleep 0.4

# ── Step 2: Extract ──
echo -e "  ${YELLOW}⬡ Step 2: nutrient_extract_text${RESET}"
echo -e "  ${DIM}┌──────────────────────────────────────────────────────────────┐${RESET}"
echo -e "  ${DIM}│${RESET}  input:    ${WHITE}scanned-contract-ocr.pdf${RESET}                           ${DIM}│${RESET}"
echo -e "  ${DIM}│${RESET}  mode:     ${CYAN}text${RESET}                                                ${DIM}│${RESET}"
echo -e "  ${DIM}└──────────────────────────────────────────────────────────────┘${RESET}"
echo
sleep 0.5

echo -ne "  ${YELLOW}⏳ Extracting text...${RESET}"
sleep 1
echo -e "\r  ${GREEN}✓${RESET} ${WHITE}Text extracted${RESET} ${DIM}(0.4s, 1 credit used)${RESET}            "
echo
sleep 0.4

# ── Results ──
echo -e "  ${GREEN}${BOLD}Done:${RESET}"
echo -e "    ${WHITE}•${RESET} OCR applied — 12 pages processed, 98.4% confidence"
echo -e "    ${WHITE}•${RESET} Text extracted — 4,231 words"
echo -e "    ${WHITE}•${RESET} Saved to ${BOLD}contract.txt${RESET}"
echo
echo -e "  ${GREEN}📄 Created:${RESET} ${BOLD}${WHITE}scanned-contract-ocr.pdf${RESET} ${DIM}(searchable PDF, 1.2 MB)${RESET}"
echo -e "  ${GREEN}📝 Created:${RESET} ${BOLD}${WHITE}contract.txt${RESET} ${DIM}(plain text, 28 KB)${RESET}"
echo

sleep 5
```

## File: `tools/validate-repo.py`
```python
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

