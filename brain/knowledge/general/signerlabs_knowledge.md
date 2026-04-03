---
id: signerlabs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.688952
---

# KNOWLEDGE EXTRACT: signerlabs
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** signerlabs

---

## File: `ShipSwift.md`
```markdown
# 📦 signerlabs/ShipSwift [🔖 PENDING/APPROVE]
🔗 https://github.com/signerlabs/ShipSwift
🌐 https://shipswift.app

## Meta
- **Stars:** ⭐ 1296 | **Forks:** 🍴 81
- **Language:** Swift | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

## README (trích đầu)
```
# ShipSwift

<div align="center">

![ShipSwift Banner](assets/banner.jpg)

**AI-native SwiftUI component library — production-ready code that LLMs can use to build real apps.**

[![Website](https://img.shields.io/badge/Website-shipswift.app-blue.svg)](https://www.shipswift.app/)
[![App Store](https://img.shields.io/badge/App_Store-Demo_App-black.svg)](https://apps.apple.com/us/app/shipswift-mcp-codebase/id6759209764)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Swift](https://img.shields.io/badge/Swift-5.0+-F05138.svg)](https://swift.org)
[![iOS](https://img.shields.io/badge/iOS-18.0+-000000.svg)](https://developer.apple.com/ios/)
[![Skills](https://img.shields.io/badge/Skills-Powered-8A2BE2.svg)](https://github.com/signerlabs/shipswift-skills)
[![ShipSwift MCP server](https://glama.ai/mcp/servers/signerlabs/ShipSwift/badges/score.svg)](https://glama.ai/mcp/servers/signerlabs/ShipSwift)

[Quick Start](#quick-start) · [Components](#components) · [Directory Structure](#directory-structure) · [Recipes](#recipes) · [Contributing](#contributing)

</div>

---

## What is ShipSwift?

One command gives your AI everything it needs — production-ready SwiftUI components, full-stack recipes, and the context to build real apps without guessing. Check more [MCP recipes](https://www.shipswift.app/).

Download the [Showcase App](https://apps.apple.com/us/app/shipswift-mcp-codebase/id6759209764) to preview every component on your device.

---

## Quick Start

### Option 1: Skills + Recipe Server (Recommended)

**Step 1** — Install ShipSwift Skills:

```bash
npx skills add signerlabs/shipswift-skills
```

**Step 2** — Connect the recipe server so your AI can fetch recipes:

```bash
# Claude Code
claude mcp add --transport http shipswift https://api.shipswift.app/mcp

# Gemini CLI
gemini mcp add --transport http shipswift https://api.shipswift.app/mcp
```

For Cursor, VS Code Copilot, Windsurf, and other tools, see the [Skills repo](https://github.com/signerlabs/shipswift-skills) for MCP setup.

**Step 3** — Ask your AI:
- "Add a shimmer loading animation"
- "Build an authentication flow with Cognito"
- "Show me all chart components"

### Option 2: Local Skills (No MCP Required)

Install skills that read source files directly from this repo — works offline, no server needed:

```bash
npx skills add signerlabs/ShipSwift
```

Your AI can then browse the component catalog and read source code locally. Try:
- "Explore ShipSwift recipes"
- "Add a shimmer animation"
- "Build a chat feature"

> **Tip**: If you also connect the MCP server (Option 1), your AI gets access to additional Pro recipes (backend guides, compliance templates, pitfall docs).

### Option 3: File Copy

1. Clone this repository
2. Copy the files you need from `ShipSwift/SWPackage/` into your Xcode project
3. Each component in `SWAnimation/`, `SWChart/`, and `SWComponent/` is self-contained — just copy the file and `SWUtil/` if needed

##
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

