---
id: think
type: knowledge
owner: OA_Triage
---
# think
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<img src="docs/images/banner.png" alt="Think Better" width="100%">

# Think Better

**Your AI writes code fast but makes terrible decisions.**<br>
Think Better injects structured decision frameworks directly into your AI prompts.

[![Go 1.25](https://img.shields.io/badge/Go-1.25-00ADD8?style=flat-square&logo=go&logoColor=white)](https://golang.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![2 AI Skills](https://img.shields.io/badge/AI_Skills-2-blueviolet?style=flat-square)](.)
[![10+ Frameworks](https://img.shields.io/badge/Frameworks-10+-orange?style=flat-square)](.)  
[![15 Decomposition](https://img.shields.io/badge/Decomposition-15-teal?style=flat-square)](.)
[![12 Biases](https://img.shields.io/badge/Biases-12-red?style=flat-square)](.)
[![4 Depth Levels](https://img.shields.io/badge/Depth-4_Levels-ff69b4?style=flat-square)](.)

[Website](https://thinkbetter.dev/) · [Documentation](USER-GUIDE.md) · [Quick Reference](QUICK-REFERENCE.md) · [Contributing](CONTRIBUTING.md)

**Works with** Claude · GitHub Copilot · Antigravity

</div>

<br>

## The Problem

You ask your AI *"Should we migrate to microservices?"* and get a generic pros/cons list. No framework. No bias detection. No structured analysis. Just vibes.

**Think Better fixes this.** It gives your AI access to 10 decision frameworks, 15 decomposition methods, 12 cognitive bias detectors, and 160 knowledge records — turning surface-level responses into structured, rigorous analysis.

<br>

## Quick Start

```bash
# macOS / Linux
curl -sSL https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.ps1 | iex
```

Then install skills for your AI:

```bash
think-better init --ai claude        # Claude Code
think-better init --ai copilot       # GitHub Copilot
think-better init --ai antigravity   # Antigravity
```

> **Other install methods:** `go install github.com/HoangTheQuyen/think-better/cmd/make-decision@latest` or clone & `make build`

<br>

## How It Works

Just talk to your AI naturally. Think Better auto-activates when it detects a decision or problem:

```
You: "Should we migrate from React to Next.js for our main app?"

AI:  → Detects: Binary Choice
     → Framework: Reversibility Filter
     → Warns: Overconfidence Bias, Status Quo Bias, Sunk Cost
     → Generates: Weighted comparison matrix + action plan
```

```
You: "Revenue dropped 20% despite market growth"

AI:  → Detects: Opportunity Gap
     → Decomposition: Profitability Tree (MECE)
     → Analysis: Root Cause (5 Whys) + Fermi Estimation
     → Warns: Anchoring Bias, Confirmation Bias
```

<br>

## Two Skills

### `/decide` — For Choices

> *"choose", "compare", "should I", "pros and cons", "nên chọn cái nào", "phân vân"*

| | |
|---|---|
| **10 Frameworks** | Reversibility Filter, Weighted Matrix, Hypothesis-Driven, Pre-Mortem, Pros-Cons-Fixes... |
| **12 Bias Warnings** | Overconfidence, Anchoring, Sunk Cost, Status Quo, Confirmation... |
| **Comparison Matrix** | `--matrix "A vs B vs C"` with weighted scoring |
| **Decision Journal** | Track → Review → Improve calibration |

### `/solve` — For Problems

> *"solve", "debug", "root cause", "I'm stuck", "tại sao bị vậy", "không biết làm sao"*

| | |
|---|---|
| **7-Step Method** | Define → Decompose → Prioritize → Analyze → Synthesize → Communicate |
| **15 Decomposition Frameworks** | Issue Tree, MECE, Hypothesis Tree, Profitability Tree, Systems Map... |
| **12 Mental Models** | First Principles, Inversion, Bayesian Updating, Pareto... |
| **10 Communication Patterns** | Pyramid Principle, BLUF, SCR, Action Titles... |

<br>

## Depth Levels

Control analysis depth with slash commands:

| Command | Depth | Records | Best For |
|---------|-------|---------|----------|
| `/solve.quick` · `/decide.quick` | Quick | 0.5× | Fast scan, simple problems |
| `/solve` · `/decide` | Standard | 1.0× | Default for most situations |
| `/solve.deep` · `/decide.deep` | Deep | 1.7× | Complex, high-stakes decisions |
| `/solve.exec` · `/decide.exec` | Executive | 2.5× | Board reports, stakeholder briefings |

**Examples:**
```
/solve.quick API latency spiked after deploy
/decide.deep AWS vs Azure vs GCP for cloud migration
/solve.exec Revenue declined 20% quarter over quarter
```

<br>

## Architecture

```
YOU ─── "Revenue dropped 20%" ──────────────────────────────────┐
                                                                │
  ┌─────────────────────────────────────────────────────────────▼──┐
  │  AI ASSISTANT (Claude / Copilot / Antigravity)                 │
  │                                                                │
  │  ┌─ Auto-detect ──────────┐    ┌─ Slash Command ────────────┐ │
  │  │ SKILL.md triggers      │ OR │ /solve.deep → deep mode    │ │
  │  │ "solve" → problem-pro  │    │ /decide.quick → quick mode │ │
  │  └────────────┬───────────┘    └────────────┬───────────────┘ │
  │               └───────────┬────────────────┘                  │
  │                           ▼                                    │
  │  ┌────────────────────────────────────────────────────────┐   │
  │  │  🐍 BM25 Search Engine                                 │   │
  │  │  160 records × depth multiplier (0.5× → 2.5×)         │   │
  │  └────────────────────────┬───────────────────────────────┘   │
  │                           ▼                                    │
  │  ┌────────────────────────────────────────────────────────┐   │
  │  │  📋 Advisor Engine                                      │   │
  │  │  Classify → Framework → Bias Detection → Plan          │   │
  │  └────────────────────────┬───────────────────────────────┘   │
  │                           ▼                                    │
  │  📄 Structured Output + Next-step suggestions                 │
  └───────────────────────────────────────────────────────────────┘
```

<br>

## Step-by-Step Workspace

Add *"save step-by-step"* to any prompt to generate a full markdown workspace:

```
solving-plans/project/               decision-plans/project/
├── 00-OVERVIEW.md                   ├── 00-OVERVIEW.md
├── 01-PROBLEM-DEFINITION.md         ├── 01-DECISION-TYPE.md
├── 02-DECOMPOSITION.md              ├── 02-FRAMEWORK.md
├── 03-PRIORITIZATION.md             ├── 03-CRITERIA.md
├── 04-ANALYSIS-PLAN.md              ├── 04-ANALYSIS.md
├── 05-FINDINGS.md                   ├── 05-OPTIONS.md
├── 06-SYNTHESIS.md                  ├── 06-DECISION.md
├── 07-RECOMMENDATION.md             ├── BIAS-WARNINGS.md
├── BIAS-WARNINGS.md                 └── DECISION-LOG.md
└── DECISION-LOG.md
```

<br>

## CLI Commands

```bash
think-better init             # Install skills for your AI
think-better list             # Show installed skills
think-better check            # Verify prerequisites (Python 3)
think-better uninstall        # Remove skills
think-better version          # Show version
```

<br>

## Project Structure

```
think-better/
├── cmd/make-decision/           # CLI entry point (Go)
├── internal/                    # Core logic
│   ├── skills/                  # Skill registry + embedded data
│   ├── targets/                 # AI platform definitions
│   ├── installer/               # Install/uninstall logic
│   └── cli/                     # Command handlers
├── .agents/
│   ├── skills/
│   │   ├── make-decision/       # Decision skill (SKILL.md, scripts, CSVs)
│   │   └── problem-solving-pro/ # Problem-solving skill
│   └── workflows/               # Slash command definitions
└── specs/                       # Specifications
```

**Stats:** 13 Go files · 7 Python scripts · 16 CSVs (160 records) · 8 workflows

<br>

## Requirements

| Method | Requirements |
|--------|-------------|
| Binary download | None — just run |
| `go install` | Go 1.25+ |
| Build from source | Go 1.25+ |
| Running skills | Python 3 |

<br>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

<br>

---

<div align="center">

# 🇻🇳 Tiếng Việt

**Ngừng Đoán Mò. Bắt Đầu Tư Duy Có Cấu Trúc.**

AI viết code nhanh nhưng ra quyết định tệ.<br>
Think Better tiêm framework tư duy vào prompt — biến AI thành Staff Engineer.

</div>

### Cài Đặt

```bash
# macOS / Linux
curl -sSL https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.sh | bash

# Windows
irm https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.ps1 | iex

# Cài skill
think-better init --ai claude
```

### Cách Dùng

Nói chuyện với AI bình thường — Think Better tự kích hoạt:

| Bạn Nói | AI Làm |
|---------|--------|
| *"Nên chọn công ty lớn hay startup?"* | `make-decision` → Weighted Matrix, cảnh báo Status Quo Bias |
| *"So sánh React vs Vue vs Angular"* | Bảng so sánh với tiêu chí có trọng số |
| *"Tại sao doanh thu giảm?"* | `problem-solving-pro` → Issue Tree, Root Cause Analysis |
| *"Bị kẹt, không biết làm sao"* | 7 bước: Định nghĩa → Phân tách → Ưu tiên → Phân tích |

### 2 Skill

**`/decide`** — Chọn lựa
- 10 framework · 12 bias · So sánh đa tiêu chí · Nhật ký quyết định

**`/solve`** — Giải quyết vấn đề
- 7 bước McKinsey · 15 framework phân tách · 12 mô hình tư duy

### Slash Commands

| Lệnh | Khi Nào |
|------|---------|
| `/solve.quick` · `/decide.quick` | Scan nhanh |
| `/solve` · `/decide` | Phân tích chuẩn |
| `/solve.deep` · `/decide.deep` | Phức tạp, high-stakes |
| `/solve.exec` · `/decide.exec` | Báo cáo cho leadership |

```
/solve.quick API chậm sau deploy
/decide.deep Nên dùng AWS hay Azure hay GCP?
```

### Lưu Ý

- Knowledge base tiếng Anh — AI tự dịch keyword trước khi search
- Cần **Python 3** cho script phân tích
- Hỗ trợ **Claude, Copilot, Antigravity**

---

<div align="center">

**MIT License** · Built by [HoangTheQuyen](https://github.com/HoangTheQuyen)

**[⭐ Star](https://github.com/HoangTheQuyen/think-better)** if Think Better helped you think better.

</div>

```

### File: examples\README.md
```md
# Decision-Making Use Cases & Lessons Learned

Real-world examples demonstrating how to use the `make-decision` CLI tool and bundled skills for structured decision-making and problem-solving.

## 📚 Available Use Cases

| # | Use Case | Skill | Decision Type | Key Learning |
|---|----------|-------|---------------|--------------|
| [01](01-product-strategy.md) | **CLI Product Strategy** | make-decision | Binary Choice | Keep it minimal - fixable cons beat permanent ones |
| [02](02-cloud-migration.md) | **Cloud Provider Selection** | make-decision | Multi-Option | Use weighted criteria + sensitivity analysis |
| [03](03-hiring-decision.md) | **Senior Engineer Hiring** | make-decision | Multi-Option | Define criteria before seeing candidates to avoid bias |
| [04](04-budget-allocation.md) | **Resource Allocation** | make-decision | Resource Allocation | Iterative allocation reduces planning risk |
| [05](05-debugging-race-condition.md) | **API Race Condition** | problem-solving-pro | Debugging | Structured hypothesis testing finds root cause faster |
| [06](06-template.md) | **[Template for new use case]** | - | - | - |
| [07](07-template.md) | **[Template for new use case]** | - | - | - |
| [08](08-template.md) | **[Template for new use case]** | - | - | - |
| [09](09-template.md) | **[Template for new use case]** | - | - | - |
| [10](10-template.md) | **[Template for new use case]** | - | - | - |

## 📖 How to Use These Examples

1. **Read the scenario** — Understand the decision context and constraints
2. **Follow the commands** — Copy/paste the exact commands used
3. **Study the output** — See what the skill recommends and why
4. **Extract the lesson** — Apply the pattern to your own decisions

## 🎯 Decision Patterns by Type

### Binary Choices (2 options)
- Use: **Pros-Cons-Fixes Analysis**
- Examples: [01 - Product Strategy](01-product-strategy.md)
- Key: Ask "can this con be fixed?" to reveal hidden flexibility

### Multi-Option Selection (3+ options)
- Use: **Weighted Criteria Matrix**
- Examples: [02 - Cloud Migration](02-cloud-migration.md), [03 - Hiring](03-hiring-decision.md)
- Key: Define criteria *before* evaluating options to avoid anchoring

### Resource Allocation (limited budget/time)
- Use: **Iterative Allocation**
- Examples: [04 - Budget Allocation](04-budget-allocation.md)
- Key: Allocate in rounds, reassess after each round

### Problem Solving (debugging, root cause analysis)
- Use: **Hypothesis-Driven Investigation**
- Examples: [05 - Race Condition](05-debugging-race-condition.md)
- Key: Rank hypotheses by likelihood, test highest-probability first

## 🧠 Common Cognitive Biases to Watch

| Bias | What It Is | Remedy |
|------|-----------|---------|
| **Confirmation Bias** | You notice evidence supporting your first impression | Actively seek disconfirming evidence |
| **Anchoring** | First number you see influences all estimates | Generate independent estimates before comparing |
| **Sunk Cost Fallacy** | Past investment makes you continue failing projects | Evaluate as if starting fresh today |
| **Status Quo Bias** | You prefer current state even when change is better | Reframe as opportunity cost |
| **Overconfidence** | You're too certain about uncertain outcomes | Use pre-mortem, track calibration over time |

## 🔄 Suggested Workflow

```bash
# 1. Install the skill
make-decision init --ai copilot --skill make-decision

# 2. Generate decision plan (always start here)
cd .github/prompts/make-decision
python scripts/search.py "your decision question" --plan -p "Project Name"

# 3. Deep-dive into specific domains as needed
python scripts/search.py "relevant keywords" --domain frameworks

# 4. Create comparison matrix for options
python scripts/search.py --matrix "Option A vs Option B vs Option C" -c "criterion1,criterion2"

# 5. Document the decision
python scripts/search.py --journal "Decision title" -p "Project Name"

# 6. Update with actual outcome later
python scripts/search.py --journal --update "decision-slug" --outcome "What actually happened"
```

## 🤝 Contributing Your Own Use Case

Have a great example? Follow the template in [06-template.md](06-template.md) and submit a PR!

**What makes a good use case:**
- ✅ Real scenario (anonymized if needed)
- ✅ Shows actual commands and outputs
- ✅ Highlights key learning or insight
- ✅ Identifies biases that were mitigated
- ✅ Documents the outcome/retrospective

---

**Back to:** [Main README](../README.md)

```

### File: build.ps1
```ps1
# Think Better - Build Script (Windows)
# Equivalent of `make build` for Windows users

Write-Host "=== Think Better Build ===" -ForegroundColor Cyan

# Step 1: Prepare embedded skills
Write-Host "Preparing embedded skills..." -ForegroundColor Yellow
$skillsDir = "internal\skills\skills"
if (Test-Path $skillsDir) { Remove-Item -Recurse -Force $skillsDir }
New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
Copy-Item -Recurse ".agents\skills\make-decision" "$skillsDir\make-decision"
Copy-Item -Recurse ".agents\skills\problem-solving-pro" "$skillsDir\problem-solving-pro"
# Clean __pycache__
Get-ChildItem -Path $skillsDir -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "Done: skills ready for embedding" -ForegroundColor Green

# Step 1b: Prepare embedded workflows
Write-Host "Preparing embedded workflows..." -ForegroundColor Yellow
$workflowsDir = "internal\skills\workflows"
if (Test-Path $workflowsDir) { Remove-Item -Recurse -Force $workflowsDir }
New-Item -ItemType Directory -Path $workflowsDir -Force | Out-Null
Copy-Item ".agents\workflows\*.md" "$workflowsDir\"
Write-Host "Done: workflows ready for embedding" -ForegroundColor Green

# Step 2: Build
Write-Host "Building..." -ForegroundColor Yellow
$binDir = "bin"
if (-not (Test-Path $binDir)) { New-Item -ItemType Directory -Path $binDir -Force | Out-Null }
$env:CGO_ENABLED = "0"
go build -o "$binDir\think-better.exe" ./cmd/make-decision
if ($LASTEXITCODE -eq 0) {
    Write-Host "Built: $binDir\think-better.exe" -ForegroundColor Green
}
else {
    Write-Host "Build failed!" -ForegroundColor Red
    exit 1
}

```

### File: build.sh
```sh
#!/bin/bash
# Think Better - Build Script (Linux / macOS)
# Equivalent of `make build` for users without make

set -e

echo "=== Think Better Build ==="

# Step 1: Prepare embedded skills
echo "Preparing embedded skills..."
SKILLS_DIR="internal/skills/skills"
rm -rf "$SKILLS_DIR"
mkdir -p "$SKILLS_DIR"
cp -r .agents/skills/make-decision "$SKILLS_DIR/make-decision"
cp -r .agents/skills/problem-solving-pro "$SKILLS_DIR/problem-solving-pro"
find "$SKILLS_DIR" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo "Done: skills ready for embedding"

# Step 2: Build
echo "Building..."
mkdir -p bin
CGO_ENABLED=0 go build -o bin/think-better ./cmd/make-decision
echo "Built: bin/think-better"

```

### File: CONTRIBUTING.md
```md
# Contributing to Think Better

First off, thank you for considering contributing to **Think Better**! It's people like you that make the open-source community such a great place to learn, inspire, and create.

This document provides guidelines and instructions for contributing to this project.

## How Can I Contribute?

### Reporting Bugs & Requesting Features
- Use the [GitHub Issues](https://github.com/HoangTheQuyen/think-better/issues) tab.
- Check if the issue or feature request already exists before creating a new one.
- Describe the issue clearly, including steps to reproduce, what you expected to happen, and what actually happened.

### Contributing Code or New AI Skills

We welcome pull requests! Here is the standard workflow to contribute code:

#### 1. Fork and Clone
1. **Fork** the repository on GitHub by clicking the "Fork" button in the top right corner.
2. **Clone** your forked repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/think-better.git
   cd think-better
   ```

#### 2. Create a Branch
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

#### 3. Make Changes & Test
- Make your code changes. If you are adding a new AI skill, follow the structure in `.agents/skills/`.
- Run the tests to ensure everything is working correctly:
  ```bash
  go test ./...
  ```
- Before committing, make sure the embedded skills are prepared:
  ```bash
  make embed-prep
  ```

#### 4. Commit Your Changes
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification (e.g., `feat:`, `fix:`, `docs:`, `chore:`).
```bash
git add .
git commit -m "feat: add new decision framework for product launch"
```

#### 5. Push and Create a Pull Request (PR)
1. **Push** your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Go to the original `HoangTheQuyen/think-better` repository on GitHub.
3. Click the **"Compare & pull request"** button next to your recently pushed branch.
4. Fill out the PR template describing your changes, why they are needed, and how they were tested.
5. Submit the Pull Request!

## Development Setup

To work on `think-better` locally, you will need:
- **Go 1.25+**
- **Python 3** (for running the skill analysis checker scripts)

Thank you for your contributions! 🚀

```

### File: GITHUB-SETUP.md
```md
# GitHub Setup Guide for think-better

## Step-by-Step GitHub Creation

### 1. Create New Repository on GitHub

**URL:** https://github.com/new

**Fill in:**

| Field | Value |
|-------|-------|
| **Repository name** | `think-better` |
| **Description** | AI-powered decision-making framework & problem-solving toolkit. 10+ frameworks, cognitive bias detection, critical thinking skills for Claude AI & GitHub Copilot. Career, business, life decisions. |
| **Visibility** | Public |
| **Initialize with:** | ✅ Add .gitignore (Go) |
| **License** | MIT License |

---

### 2. Repository Settings

**General → About**
- ☑️ Add description: "AI-powered decision-making framework & problem-solving toolkit with cognitive bias detection for Claude AI & GitHub Copilot"
- ☑️ Add website: `https://htrbao.github.io/think-better`

**Manage access → Collaborators** (optional, for future contributors)
- Add fellow maintainers here

---

### 3. Repository Topics (for SEO/Discoverability)

Go to **Settings → General → Repository topics**

Add these topics:
```
decision-making
decision-making-framework
problem-solving
problem-solving-toolkit
critical-thinking
cognitive-bias
ai-assistant
ai-prompts
claude-ai
github-copilot
strategic-planning
career-development
business-strategy
thinking-tools
reasoning-framework
cli-tool
go-cli
cross-platform
open-source
```

---

### 4. Create GitHub Discussions (Optional, for Community)

**Settings → Features → Discussions** → ✅ Enable

Creates:
- Announcements
- General discussion
- Ideas
- Show and tell

---

### 5. Create GitHub Pages (Optional, for Docs Site)

**Settings → GitHub Pages → Source:** `main` branch

Then create `docs/` folder with Markdown files that auto-convert to HTML.

---

## Local Repository Setup

### 1. Clone Your New Repo

```bash
cd D:\
git clone https://github.com/htrbao/think-better.git
cd think-better
```

### 2. Move Files from Old to New

```bash
# Copy all files from decision-maker to think-better
# (You can skip this - just create new repo and push code to it)
```

---

## Repository Structure

```
think-better/
├── README.md                          # Main entry point
├── USER-GUIDE.md                      # Complete workflows
├── QUICK-REFERENCE.md                 # Cheat sheet
├── GITHUB-SETUP.md                    # This file
├── LICENSE                            # MIT
├── .gitignore                         # Go + OS stuff
│
├── cmd/
│   └── think-better/                  # CLI tool
│       └── main.go
│
├── internal/
│   ├── skills/
│   │   ├── registry.go
│   │   ├── embed.go
│   │   └── skills/                    # Embedded skill files
│   │       ├── make-decision/
│   │       └── problem-solving-pro/
│   │
│   ├── installer/
│   ├── targets/
│   ├── checker/
│   └── cli/
│
├── .github/
│   ├── prompts/
│   │   ├── make-decision/
│   │   └── problem-solving-pro/
│   │
│   └── workflows/                     # CI/CD (optional)
│       └── build.yml
│
├── examples/
│   ├── README.md
│   ├── 01-career-transition.md       # NEW: Career advice
│   ├── 02-business-strategy.md       # NEW: Business
│   ├── 03-hiring-decision.md         # Keep: Team
│   ├── 04-resource-allocation.md     # Keep: Resource
│   ├── 05-debugging-race-condition.md # NEW: Problem-solving
│   └── 06-10-template.md
│
├── go.mod                             # Module name
├── Makefile
└── docs/                              # (Optional) GitHub Pages
    └── index.md
```

---

## Files to Update for Brand Consistency

### Core Files (REQUIRED)

| File | What to Change |
|------|----------------|
| `README.md` | Header, taglines, description |
| `USER-GUIDE.md` | Intro, language |
| `QUICK-REFERENCE.md` | Header, context |
| `go.mod` | Module path: `github.com/htrbao/think-better` |
| `cmd/think-better/main.go` | Binary name, version string |
| `.gitignore` | Update paths for `think-better` |

### Documentation Files (OPTIONAL but recommended)

| File | Updates |
|------|---------|
| `examples/README.md` | Add career/business/life examples |
| `examples/01-*.md` | Rename/expand for universal appeal |
| Skip | Skill files in `.github/prompts/` (keep as-is) |
| Skip | Internal Go code (no need to change) |

---

## Module Path Change (Go)

### Current
```
module github.com/htrbao/think-better
```

### Should be
```
module github.com/htrbao/think-better
```

**Update in:**
- `go.mod`
- `go.sum` (auto-generated)
- Code imports (if any)

---

## Build & Release

### Build Command
```bash
make build-all
# Creates: bin/think-better-linux-amd64, etc.
```

### Create GitHub Release

1. Go to **Releases → Create a new release**
2. Tag: `v0.1.0`
3. Title: `Think Better v0.1.0 - Launch`
4. Description:
   ```markdown
   # 🎉 Think Better v0.1.0
   
   The operating system for clear thinking & better decisions.
   
   ## What's Included
   - 2 bundled skills (make-decision, problem-solving-pro)
   - 10+ decision frameworks
   - 12 cognitive bias warnings
   - 5 real-world case studies
   - Comprehensive user guide
   
   ## Download
   Pick your platform below and download the binary. No installation needed!
   
   ## Quick Start
   ```bash
   ./think-better init --ai claude
   ```
   
   Then open Claude in VS Code and type:
   ```
   @workspace /think-better Should I change jobs?
   ```
   ```

5. Upload binaries:
   - `bin/think-better-windows-amd64.exe`
   - `bin/think-better-windows-arm64.exe`
   - `bin/think-better-darwin-amd64`
   - `bin/think-better-darwin-arm64`
   - `bin/think-better-linux-amd64`
   - `bin/think-better-linux-arm64`

---

## Post-Launch Checklist

- [ ] Repo created on GitHub with correct name/description
- [ ] Topics added (13 topics for SEO)
- [ ] License set to MIT
- [ ] README.md updated with new branding
- [ ] All file references updated to `think-better`
- [ ] go.mod updated to new module path
- [ ] Build successful: `go build -o bin/think-better ./cmd/think-better`
- [ ] Release created with v0.1.0 tag
- [ ] Binaries uploaded to release
- [ ] Examples updated with universal appeal
- [ ] USER-GUIDE.md references updated
- [ ] QUICK-REFERENCE.md updated

---

## Marketing Checklist (Optional)

- [ ] Write "Show HN" post
- [ ] Tweet announcement
- [ ] Post to r/OpenSource, r/PromptEngineering
- [ ] Add to Awesome lists on GitHub
- [ ] Post to Product Hunt (optional)
- [ ] Create 1-2 minute demo video

---

## Your GitHub Username

**Replace `htrbao` with your actual GitHub username in:**
- Repository URL: `github.com/htrbao/think-better`
- Module path: `github.com/htrbao/think-better`
- URLs in docs

---

## Questions?

Common setup issues:

**Q: Clone failed?**  
A: Check you have Git installed, GitHub username correct

**Q: Permission denied on binary?**  
A: On Mac/Linux: `chmod +x bin/think-better-*`

**Q: Module import error?**  
A: Run `go mod tidy` to fix imports

---

**Ready? Let's rename everything! 🚀**

```

### File: install.ps1
```ps1
# Think Better — One-liner installer for Windows
# Usage: irm https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

$Repo = "HoangTheQuyen/think-better"
$Binary = "think-better"

# --- Detect architecture ---
$Arch = if ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture -eq "Arm64") { "arm64" } else { "amd64" }

$Asset = "${Binary}-windows-${Arch}.exe"
$InstallDir = Join-Path $env:LOCALAPPDATA "think-better"

Write-Host "🧠 Think Better Installer" -ForegroundColor Cyan
Write-Host "   Platform: windows/${Arch}"

# --- Download ---
$Url = "https://github.com/${Repo}/releases/latest/download/${Asset}"
Write-Host "   Downloading: ${Url}"

New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
$DestPath = Join-Path $InstallDir "${Binary}.exe"

try {
    Invoke-WebRequest -Uri $Url -OutFile $DestPath -UseBasicParsing
}
catch {
    Write-Host "❌ Download failed. Make sure there is a release at:" -ForegroundColor Red
    Write-Host "   $Url" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Installed to ${DestPath}" -ForegroundColor Green

# --- Add to PATH ---
$UserPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($UserPath -notlike "*$InstallDir*") {
    [Environment]::SetEnvironmentVariable("PATH", "$UserPath;$InstallDir", "User")
    $env:PATH = "$env:PATH;$InstallDir"
    Write-Host "✅ Added to PATH (restart terminal to take effect)" -ForegroundColor Green
}
else {
    Write-Host "   Already in PATH" -ForegroundColor Gray
}

# --- Verify ---
Write-Host ""
& $DestPath version
Write-Host ""
Write-Host "🚀 Ready! Run: think-better init --ai claude" -ForegroundColor Cyan

```

### File: install.sh
```sh
#!/bin/bash
# Think Better — One-liner installer for macOS / Linux
# Usage: curl -sSL https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.sh | bash
set -e

REPO="HoangTheQuyen/think-better"
BINARY="think-better"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"

# --- Detect platform ---
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

case "$OS" in
  linux)  OS="linux" ;;
  darwin) OS="darwin" ;;
  *)      echo "❌ Unsupported OS: $OS"; exit 1 ;;
esac

case "$ARCH" in
  x86_64|amd64)  ARCH="amd64" ;;
  aarch64|arm64) ARCH="arm64" ;;
  *)             echo "❌ Unsupported architecture: $ARCH"; exit 1 ;;
esac

ASSET="${BINARY}-${OS}-${ARCH}"
echo "🧠 Think Better Installer"
echo "   Platform: ${OS}/${ARCH}"

# --- Get latest release URL ---
LATEST_URL="https://github.com/${REPO}/releases/latest/download/${ASSET}"
echo "   Downloading: ${LATEST_URL}"

# --- Download ---
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

if command -v curl &>/dev/null; then
  curl -fsSL "$LATEST_URL" -o "${TMP_DIR}/${BINARY}"
elif command -v wget &>/dev/null; then
  wget -qO "${TMP_DIR}/${BINARY}" "$LATEST_URL"
else
  echo "❌ Neither curl nor wget found. Please install one."
  exit 1
fi

# --- Install ---
mkdir -p "$INSTALL_DIR"
mv "${TMP_DIR}/${BINARY}" "${INSTALL_DIR}/${BINARY}"
chmod +x "${INSTALL_DIR}/${BINARY}"

echo "✅ Installed to ${INSTALL_DIR}/${BINARY}"

# --- Check PATH ---
if ! echo "$PATH" | tr ':' '\n' | grep -qx "$INSTALL_DIR"; then
  echo ""
  echo "⚠️  ${INSTALL_DIR} is not in your PATH. Add it:"
  echo ""
  echo "   echo 'export PATH=\"${INSTALL_DIR}:\$PATH\"' >> ~/.bashrc"
  echo "   source ~/.bashrc"
  echo ""
fi

# --- Verify ---
if command -v "$BINARY" &>/dev/null; then
  echo ""
  "$BINARY" version
  echo ""
  echo "🚀 Ready! Run: think-better init --ai claude"
fi

```

### File: QUICK-REFERENCE.md
```md
# Quick Reference Card

## Installation & Setup

```bash
# Install binary
curl -sSL https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.sh | bash
# Or Windows: irm https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.ps1 | iex

# Install skills
think-better init --ai claude       # or: copilot, antigravity

# List installed skills
think-better list

# Verify setup
think-better check
```

---

## Decision Workflows (One-Pagers)

### Binary Choice (2 Options)
```bash
python scripts/search.py "your decision" --plan -p "Project"
python scripts/search.py --matrix "Option A vs Option B" -c "criterion1,criterion2"
python scripts/search.py "relevant keyword" --domain biases
python scripts/search.py --journal "Decision title" -p "Project"
```
**Framework:** Pros-Cons-Fixes Analysis  
**Key Q:** Which cons are fixable vs permanent?

---

### Multi-Option Selection (3+ Options)
```bash
# 1. Get decision plan
python scripts/search.py "choosing between A, B, C for [purpose]" --plan -p "Project"

# 2. Get criteria template
python scripts/search.py "[topic]" --domain criteria

# 3. Get analysis techniques
python scripts/search.py "comparison scoring sensitivity" --domain analysis

# 4. Create matrix
python scripts/search.py --matrix "A vs B vs C" -c "c1,c2,c3,c4,c5"

# 5. Check biases
python scripts/search.py "anchoring status quo first impression" --domain biases

# 6. Group facilitation (if team)
python scripts/search.py "anonymous voting structured" --domain facilitation

# 7. Document
python scripts/search.py --journal "Chose [WINNER] because..." -p "Project"
```
**Framework:** Weighted Criteria Matrix + Sensitivity Analysis  
**Key:** Define criteria BEFORE evaluating options

---

### Resource Allocation
```bash
python scripts/search.py "allocate resources across priorities" --plan -p "Project"
python scripts/search.py "iterative allocation" --domain frameworks
python scripts/search.py "opportunity cost" --domain analysis

# Remember: Allocate 50-70% in Round 1, measure velocity, reallocate
```
**Framework:** Iterative Allocation  
**Key:** Don't allocate 100% upfront; learn before committing

---

### Problem-Solving / Debugging
```bash
# In your AI assistant with problem-solving-pro skill:
/solve [Describe problem, environment, what you've tried]

# With depth control:
/solve.quick API latency spiked after deploy
/solve.deep Revenue declining despite growth
/solve.exec Board-level crisis analysis

# The skill guides you through:
# 1. Problem decomposition (break into layers)
# 2. Hypothesis ranking (by likelihood)
# 3. Evidence collection (specific tests)
# 4. Root cause (5 Whys)
# 5. Solution options (quick vs proper vs architectural)
# 6. Prevention (monitoring, alerts)
```
**Key:** Test hypotheses by likelihood × ease of testing

---

## Domain-Specific Searches

```bash
# Get decision-making frameworks (10 available)
python scripts/search.py "keywords" --domain frameworks

# Get decision type classifications (8 types)
python scripts/search.py "keywords" --domain types

# Get cognitive biases (12 with remedies)
python scripts/search.py "keywords" --domain biases

# Get analysis techniques (10 methods)
python scripts/search.py "keywords" --domain analysis

# Get evaluation criteria (8 templates)
python scripts/search.py "keywords" --domain criteria

# Get group facilitation techniques (8 methods)
python scripts/search.py "keywords" --domain facilitation
```

---

## Decision Journey

### Before Deciding
- ✅ Define problem precisely
- ✅ List all options/alternatives
- ✅ Define criteria BEFORE evaluating options
- ✅ Identify stakeholders
- ✅ Check relevant biases and apply remedies

### During Decision
- ✅ Get independent scores/estimates first
- ✅ Run sensitivity analysis (multi-option)
- ✅ Use structured group process (if team)
- ✅ Check references (vendors/hires)
- ✅ POCs for technical decisions

### After Decision
- ✅ Create journal entry with rationale
- ✅ Set review date (3-6 months or 12 months)
- ✅ Document implementation plan
- ✅ Identify known risks

### Retrospective
- ✅ Update journal with actual outcomes
- ✅ Extract lessons learned
- ✅ Improve future calibration

---

## High-Risk Biases (Always Watch)

| Bias | Watch For | Counter |
|------|-----------|---------|
| **Confirmation** | Noticing what supports first impression | Seek disconfirming evidence actively |
| **Anchoring** | First number/option influences rest | Independent estimates before comparing |
| **Sunk Cost** | Past investment justifying future | Evaluate as if starting fresh |
| **Overconfidence** | Too certain about uncertain outcomes | Pre-mortem, track calibration |
| **Status Quo** | Preference for current state | Reframe as opportunity cost |

### Domain-Specific
- **Hiring:** Affinity, Halo Effect, Resume-Driven
- **Tech:** Resume-Driven, Not Invented Here, Status Quo
- **Allocation:** Planning Fallacy, Overconfidence

---

## Pro Tips

### Decision-Making
1. **Pros-Cons-Fixes** for binary choices — Ask "is this fixable?"
2. **Sensitivity Analysis** for multi-option — What if weights change?
3. **Define Criteria First** — Prevents anchoring and post-hoc rationalization
4. **Use Anonymous Voting** — Surfaces minority views before group pressure
5. **Reference Checks** — Talk to customers/previous managers, not just sales pitch

### Problem-Solving
1. **Break Into Layers** — Decompose by system architecture
2. **Rank by Likelihood** — Test highest probability hypotheses first
3. **Measure Before Fixing** — Understand the problem before proposing solution
4. **5 Whys** — Work backward from symptom to root cause
5. **Prevention Matters** — Add monitoring to catch this in future

---

## Common Decision Types & Frameworks

| Situation | Framework | Time | Who |
|-----------|-----------|------|-----|
| 2 options | Pros-Cons-Fixes | 1-2 hrs | Individual/Team |
| 3+ options | Weighted Matrix | 2-4 hrs | Individual/Team |
| Uncertain | Scenario Planning | 2-4 hrs | Team |
| Sequential | Decision Tree | 1-2 hrs | Team |
| Resources | Iterative Allocation | 2-4 weeks | Team |
| Debugging | Hypothesis Testing | 1-4 hrs | Individual |
| Team aligned | Nominal Group | 2-3 hrs | Group |

---

## Quick Prompts for AI Assistant

```
## For Decision-Making

/decide Should we [option A] or [option B]?
/decide.deep Choosing between [A], [B], and [C] for [purpose].
/decide.exec Strategic analysis of [major decision] for board discussion

## For Problem-Solving

/solve [Describe symptom]. Happens in [environment].
Stack: [tech stack]. I've tried [what you've tried so far].

/solve.deep Why does [system] sometimes [fail condition]?
Recent changes: [recent deployments/config changes]
```

---

## Resources

- **Main Guide:** [USER-GUIDE.md](USER-GUIDE.md) — Full workflows with examples
- **Case Studies:** [examples/](examples/) — Real decisions with outcomes
- **Skill Reference:** `.agents/skills/make-decision/SKILL.md` — Full documentation
- **Templates:** [examples/06-template.md](examples/06-template.md) onwards — Adapt for your use cases

---

**Print this card and keep it at your desk!** 📇

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in **think-better**, please report it responsibly.

### How to Report

1. **DO NOT** open a public GitHub issue for security vulnerabilities.
2. Email your findings to: **hoangthequyen@gmail.com**
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment** within 48 hours of your report.
- **Assessment** of severity and impact within 1 week.
- **Fix and disclosure** coordinated with you before public release.

### Scope

This policy applies to:
- The `think-better` CLI binary
- Embedded skill and workflow files
- Build and release infrastructure (GitHub Actions)

### Out of Scope

- Third-party AI assistants (Claude, Copilot, etc.) — report vulnerabilities to their respective vendors.
- Social engineering attacks.

## Recognition

We appreciate security researchers who help keep think-better safe. Contributors who report valid vulnerabilities will be acknowledged in our release notes (with permission).

```

### File: USER-GUIDE.md
```md
# User Guide: How to Use Think Better

A step-by-step guide to installing and using the bundled skills for structured thinking, decision-making, and problem-solving with your AI assistant.

---

## 🚀 Quick Start (5 minutes)

### 1. Download and Install

```bash
# macOS / Linux
curl -sSL https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/HoangTheQuyen/think-better/main/install.ps1 | iex

# Or build from source:
git clone https://github.com/HoangTheQuyen/think-better.git && cd think-better
make build          # Linux/macOS
.\build.ps1         # Windows
```

### 2. Install a Skill

```bash
# For Claude Code
think-better init --ai claude

# For GitHub Copilot
think-better init --ai copilot

# For Antigravity
think-better init --ai antigravity
```

### 3. Open Your AI Assistant

- **Claude:** Open Claude Code or VS Code with Claude extension
- **Copilot:** Open VS Code and switch to Copilot Chat
- **Antigravity:** Open your Antigravity-powered editor

### 4. Start Using

Just describe your problem naturally, or use a slash command:
```
"Should we migrate to microservices?"
/decide.deep Should we migrate to microservices?
/solve.quick API latency spiked after deploy
```

---

## 📚 Bundled Skills

### Skill 1: make-decision

**What it does:** Guides you through structured decision-making with frameworks, bias detection, and facilitation techniques.

**Best for:**
- Strategic choices (keep it minimal vs scale up)
- Multi-option selection (choose between 3+ vendors/technologies)
- Resource allocation (budget distribution)
- Team decisions (need group consensus)

**How it works:**
```bash
# Inside the skill directory:
cd .agents/skills/make-decision

# Step 1: Generate decision plan (always start here!)
python scripts/search.py "your decision question here" --plan -p "Project Name"

# Step 2: Deep-dive into specific domains
python scripts/search.py "relevant keywords" --domain frameworks  # 10 frameworks
python scripts/search.py "relevant keywords" --domain biases     # 12 cognitive biases
python scripts/search.py "relevant keywords" --domain criteria   # Evaluation templates
python scripts/search.py "relevant keywords" --domain analysis   # 10 analysis techniques
python scripts/search.py "relevant keywords" --domain facilitation # Group decision tips

# Step 3: Create comparison matrix for options
python scripts/search.py --matrix "Option A vs Option B vs Option C" \
  -c "criterion1,criterion2,criterion3"

# Step 4: Document the decision
python scripts/search.py --journal "Decision title" -p "Project Name"

# Step 5: Update with actual outcome (later)
python scripts/search.py --journal --update "decision-slug" \
  --outcome "What actually happened and what you learned"
```

### Skill 2: problem-solving-pro

**What it does:** Guides you through structured problem-solving with hypothesis testing, root cause analysis, and systematic investigation.

**Best for:**
- Production incidents (bugs, performance issues)
- Debugging intermittent failures
- Root cause analysis
- Technical investigations
- Data quality issues

**How it works:**

In your AI assistant:
```
/solve My API sometimes returns stale data after updates. 
Happens intermittently (~2% of requests), no clear pattern by time or user.
Stack: Node.js + Express, PostgreSQL with read replica, Redis cache.

# Or with depth control:
/solve.deep My API sometimes returns stale data after updates...
/solve.exec Revenue declined 20% despite market growth
```

The skill will guide you through:
1. **Problem Decomposition** — Break system into layers
2. **Hypothesis Generation** — Rank potential causes by likelihood
3. **Evidence Collection** — Specific tests to validate each hypothesis
4. **Root Cause Identification** — 5 Whys analysis
5. **Solution Design** — Compare quick fix vs proper fix vs architectural fix
6. **Prevention** — Monitoring to catch this in future

---

## 🎯 Decision-Making Workflows

### Scenario A: Binary Choice (2 Options)

**Example:** "Keep frontend simple or add more features?"

**Workflow:**

```bash
# Step 1: Get decision plan
python scripts/search.py "binary choice: keep simple vs add features" --plan -p "Product Roadmap"

# Output should recommend: Pros-Cons-Fixes Analysis

# Step 2: Search for relevant frameworks
python scripts/search.py "binary simplicity complexity" --domain frameworks

# Step 3: Create comparison matrix
python scripts/search.py --matrix "Keep simple vs Add features" \
  -c "development_time,maintainability,user_value,technical_debt,learning_curve"

# Step 4: Check for biases specific to this decision
python scripts/search.py "feature creep perfectionism" --domain biases

# Step 5: Document with decision journal
python scripts/search.py --journal "Frontend complexity: simple vs feature-rich" \
  -p "Product Roadmap"
```

**Key Question to Ask:**
> "Which cons are fixable vs permanent?"

Fixable cons (can be solved with documentation, features, or process changes) are less important than permanent cons (fundamental trade-offs).

---

### Scenario B: Multi-Option Selection (3+ Options)

**Example:** "Which cloud provider: AWS, Azure, or GCP?"

**Workflow:**

```bash
# Step 1: Get decision plan (critical for multi-option!)
python scripts/search.py "choosing between AWS, Azure, and GCP for enterprise migration" \
  --plan -p "Cloud Strategy"

# Output should recommend: Weighted Criteria Matrix + Sensitivity Analysis

# Step 2: Get evaluation criteria template
python scripts/search.py "technology vendor cloud" --domain criteria

# Step 3: Get analysis technique for multi-option decisions
python scripts/search.py "decision tree scoring comparison" --domain analysis

# Step 4: Create detailed comparison matrix
python scripts/search.py --matrix "AWS vs Azure vs GCP" \
  -c "total_cost,team_expertise,service_coverage,support_quality,compliance,migration_tools"

# Step 5: Run sensitivity analysis
# (Ask yourself: if weight of X criterion changes, does the winner change?)
# (Test different scenarios: what if team expertise was less important?)

# Step 6: Check for anchoring & status quo biases
python scripts/search.py "anchoring status quo first impression" --domain biases

# Step 7: Use group facilitation technique if team decisions
python scripts/search.py "structured debate dot voting anonymous" --domain facilitation

# Step 8: Document the final decision
python scripts/search.py --journal "Cloud migration: chose [WINNER] over alternatives" \
  -p "Cloud Strategy"
```

**Critical Steps:**
1. ✅ **Define criteria BEFORE evaluating options** (prevents anchoring)
2. ✅ **Get independent estimates/scores** (before group discussion)
3. ✅ **Run sensitivity analysis** (identify swing factors)
4. ✅ **Check references** (for vendors/hires)

---

### Scenario C: Resource Allocation

**Example:** "Allocate 10 engineers across 5 projects"

**Workflow:**

```bash
# Step 1: Decision plan for allocation
python scripts/search.py "allocate resources across competing priorities with constraints" \
  --plan -p "Q2 Planning"

# Output should recommend: Iterative Allocation (don't allocate all at once!)

# Step 2: Get resource allocation framework
python scripts/search.py "iterative constraint priority" --domain frameworks

# Step 3: Use opportunity cost analysis
python scripts/search.py "opportunity cost what do we lose" --domain analysis

# Step 4: Identify decision type (production risk vs growth opportunity)
python scripts/search.py "prioritization scoring risk reward" --domain types

# Step 5: If team decision, use facilitation
python scripts/search.py "dot voting priority ranking" --domain facilitation

# Step 6-Plan: Allocate conservative portion (50-70%)
# Allocate Round 1 with 30% of resources held back

# Step 6-Execute: Measure actual velocity and blockers for 2-3 weeks

# Step 7-Reassess: Based on evidence, reallocate remaining resources
# Repeat until all resources allocated
```

**Key Principle:**
> "Iterative allocation beats perfect planning."

You can't predict the future accurately. Better to allocate conservatively, measure real velocity, then adjust.

---

### Scenario D: Hiring/Team Decisions

**Example:** "Choose between 3 senior engineer candidates"

**Workflow:**

```bash
# Step 1: Decision plan for hiring
python scripts/search.py "choosing senior engineer from 3 finalists" --plan -p "Q1 Hiring"

# Output should recommend: Weighted Criteria Matrix

# Step 2: Get hiring-specific criteria
python scripts/search.py "hiring technical fit culture team" --domain criteria

# Step 3: CRITICAL - Identify biases in hiring (most dangerous!)
python scripts/search.py "affinity halo confirmation resume driven" --domain biases -n 5

# Step 4: Get group facilitation technique
python scripts/search.py "anonymous voting structured interview blind review" --domain facilitation

# Step 5: Implement bias mitigation:
#   - Define criteria BEFORE seeing resumes (or profiles)
#   - Blind review first (remove names, companies, universities)
#   - Structured interview questions (same for all candidates)
#   - Anonymous scoring before group discussion
#   - Devil's advocate role for top choice
#   - Reference checks (talk to previous managers)

# Step 6: Create comparison matrix
python scripts/search.py --matrix "Candidate A vs Candidate B vs Candidate C" \
  -c "technical_skills,domain_expertise,culture_fit,growth_potential,team_complement,references"

# Step 7: Document the decision
python scripts/search.py --journal "Senior engineer hire: chose [NAME] based on [CRITERIA]" \
  -p "Q1 Hiring"
```

**Bias Watch:** Hiring decisions are prone to affinity bias, halo effect, and confirmation bias. The most important mitigation is **defining criteria before seeing candidates**.

---

## 🔍 Problem-Solving Workflows

### Common Production Issue

**Example:** "API intermittently returns stale data"

**Process:**

```bash
# In your AI assistant with problem-solving-pro skill:

/solve My API returns stale data ~2% of the time after updates.
No clear pattern by time, user, or endpoint. Stack: Node.js + Express,
PostgreSQL (primary + read replica), Redis cache.
```

**The skill will guide you:**

```
1. DECOMPOSITION
   - CDN cache layer (possibility: serving cached response)
   - Application cache layer (possibility: Redis invalidation bug)
   - Database layer (possibility: reading from stale replica)
   - Network/infrastructure layer (possibility: packet loss)

2. HYPOTHESIS RANKING
   Rank by likelihood:
   - Hypothesis 1 (60%): Redis cache not invalidated on write
   - Hypothesis 2 (25%): Reading from replica with replication lag
   - Hypothesis 3 (10%): CDN caching response
   - Hypothesis 4 (5%): Race condition in app

3. TESTING STRATEGY
   Test Hypothesis 1 first (highest likelihood × easiest to test)
   - Check: Is EXPIRE called after update? Is key really deleted?
   - Look at: Redis logs, application code, TTL values

4. ROOT CAUSE
   Found: Cache-aside pattern + read replica + replication lag
   - PATCH invalidates cache ✓
   - GET has cache miss
   - GET reads from REPLICA (has 2-5s lag still)
   - GET repopulates cache with STALE data
   - Subsequent GETs serve stale for 5 minutes (TTL)

5. SOLUTION OPTIONS
   Option 1 (Quick): Read from PRIMARY on cache miss (30 min)
   Option 2 (Proper): Write-through cache (2 hours)
   Option 3 (Architectural): Consistent cache invalidation (1 day)
   Choice: Implement Option 2 (best risk/reward)

6. PREVENTION
   - Add monitoring for cache hit rate drop
   - Alert on staleness detection
   - Document cache consistency guarantees
```

---

## 💡 Tips for Best Results

### Before You Decide/Debug

1. **📋 Define the problem precisely**
   - Not: "Cloud is too expensive"
   - But: "Need cloud infrastructure for 500K req/sec, 18-month migration window, HIPAA compliance"

2. **👥 Identify all stakeholders early**
   - Who decides? Who's affected? Who has relevant experience?
   - Include them in criteria definition, not just final vote

3. **⚖️ Define criteria BEFORE evaluating options**
   - Prevents anchoring (first option influences scoring of others)
   - Prevents post-hoc rationalization ("This option is good because it has feature X")

4. **🧠 Check your biases explicitly**
   - Run: `python scripts/search.py "relevant keywords" --domain biases`
   - Apply specific remedies for each bias

5. **📊 Use decision journal religiously**
   - Document not just the decision, but the rationale
   - 6-12 months later, update with actual outcomes
   - This improves your decision calibration over time

### During Decision-Making

6. **🔍 Run sensitivity analysis for multi-option decisions**
   - Ask: "If I weight criterion X differently, does the winner change?"
   - Identifies which criteria actually swing the decision

7. **👂 Use structured group processes**
   - Not: "What do people think?" (groupthink, halo effect)
   - But: "Anonymous vote first, discuss gaps, revote"

8. **🧪 Run POCs for technical decisions**
   - Prove assumptions with real data
   - Don't trust estimates

9. **📞 Check references**
   - For vendors: Talk to customers
   - For hires: Call previous managers
   - For technologies: Test in your environment

10. **⏱️ Use iterative allocation for resource decisions**
    - Don't allocate all 100% upfront
    - Allocate 50-70%, measure velocity, adjust

### After Decision

11. **📖 Document the decision**
    ```bash
    python scripts/search.py --journal "Decision title" -p "Project Name"
    ```
    Include:
    - Options considered
    - Criteria and weights
    - Winner and why
    - Implementation plan
    - Known risks

12. **📅 Set a review date**
    - 3-6 months for tactical decisions
    - 12 months for strategic decisions
    - Update journal with actual outcomes

13. **🎓 Extract lessons learned**
    - What worked in the process?
    - What surprised you?
    - What would you do differently?
    - Which criteria proved most important?

---

## 🎓 Decision Frameworks Reference

### When to Use Each Framework

| Decision Type | Best Framework | Example |
|---------------|----------------|---------|
| **2 options** | Pros-Cons-Fixes | Keep simple vs add features |
| **3+ options** | Weighted Matrix | AWS vs Azure vs GCP |
| **Uncertain future** | Scenario Planning | Enter new market or not |
| **Sequential choices** | Decision Tree | Hire now vs wait 6mo? |
| **Resource/budget** | Iterative Allocation | Which projects get engineers |
| **Group alignment** | Nominal Group Technique | Team decision on strategy |
| **Testing hypotheses** | Hypothesis-Driven | Debugging root cause |

---

## ⚠️ Cognitive Biases to Watch

### High-Risk Biases (Always Watch)

| Bias | What It Does | How to Counter |
|------|-------------|-----------------|
| **Confirmation Bias** | You notice what confirms your first impression | Actively seek disconfirming evidence |
| **Anchoring** | First number/option influences everything | Get independent e
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
