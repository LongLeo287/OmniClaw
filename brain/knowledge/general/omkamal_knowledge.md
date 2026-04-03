---
id: omkamal-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:14.698576
---

# KNOWLEDGE EXTRACT: omkamal
> **Extracted on:** 2026-03-30 17:49:54
> **Source:** omkamal

---

## File: `pypict-claude-skill.md`
```markdown
# 📦 omkamal/pypict-claude-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/omkamal/pypict-claude-skill


## Meta
- **Stars:** ⭐ 58 | **Forks:** 🍴 8
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A claude skill that generate test cases using N-wise test cases using the pypict library

## README (trích đầu)
```
# PICT Test Designer - Claude Skill

A Claude skill for designing comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing). This skill enables systematic test case design with minimal test cases while maintaining high coverage through pairwise combinatorial testing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Claude-Skill-blue.svg)](https://claude.ai)

## 🎯 What is PICT?

PICT (Pairwise Independent Combinatorial Testing) is a combinatorial testing tool developed by Microsoft. It generates test cases that efficiently cover all pairwise combinations of parameters while drastically reducing the total number of tests compared to exhaustive testing.

**Example:** Testing a system with 8 parameters and 3-5 values each:
- Exhaustive testing: **25,920 test cases**
- PICT pairwise testing: **~30 test cases** (99.88% reduction!)

## 🚀 Features

- **Automated Test Case Generation**: Converts requirements into structured PICT models
- **Constraint-Based Testing**: Applies business rules to eliminate invalid combinations
- **Expected Output Generation**: Automatically determines expected results for each test case
- **Comprehensive Coverage**: Ensures all pairwise parameter interactions are tested
- **Multiple Domains**: Works for software functions, APIs, web forms, configurations, and more

## 📋 Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing in Claude Code CLI](#installing-in-claude-code-cli)
  - [Installing in Claude Code Desktop](#installing-in-claude-code-desktop)
- [Quick Start](#quick-start)
- [Example: ATM System Testing](#example-atm-system-testing)
- [How It Works](#how-it-works)
- [Use Cases](#use-cases)
- [Credits](#credits)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Claude Code CLI or Claude Code Desktop
- (Optional) Python 3.7+ with `pypict` for advanced usage

### Installation Methods

Claude Code skills can be installed via the plugin marketplace or manually by placing them in the `.claude/skills/` directory.

### Method 1: Install via Claude Code Plugin Marketplace (Easiest) 🌟

Install directly through Claude Code's plugin system:

```bash
# Add the marketplace
/plugin marketplace add omkamal/pypict-claude-skill

# Install the plugin
/plugin install pict-test-designer@pypict-claude-skill
```

This automatically installs the skill and keeps it updated. The skill will be available across all your projects.

### Method 2: Install from GitHub (Manual)

**For Personal Use (All Projects):**

```bash
# Clone the repository to your personal skills directory
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer

# Restart Claude Code to load the skill
# The skill will now be available in all your projects
```

**For Project-Specific Use:**

```bash
# From your project director
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

