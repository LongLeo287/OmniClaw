---
id: stitch
type: knowledge
owner: OA_Triage
---
# stitch
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Stitch Agent Skills

A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor.

## Installation & Discovery

Install any skill from this repository using the `skills` CLI. This command will automatically detect your active coding agents and place the skill in the appropriate directory.

```bash
# List all available skills in this repository
npx skills add google-labs-code/stitch-skills --list

# Install a specific skill
npx skills add google-labs-code/stitch-skills --skill react:components --global
```

## Available Skills

### stitch-design
Unified entry point for Stitch design work. Handles prompt enhancement (UI/UX keywords, atmosphere), design system synthesis (.stitch/DESIGN.md), and high-fidelity screen generation/editing via Stitch MCP.

```bash
npx skills add google-labs-code/stitch-skills --skill stitch-design --global
```

### stitch-loop
Generates a complete multi-page website from a single prompt using Stitch, with automated file organization and validation.

```bash
npx skills add google-labs-code/stitch-skills --skill stitch-loop --global
```

### design-md
Analyzes Stitch projects and generates comprehensive DESIGN.md files documenting design systems in natural, semantic language optimized for Stitch screen generation.

```bash
npx skills add google-labs-code/stitch-skills --skill design-md --global
```

### enhance-prompt
Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better generation results.

```bash
npx skills add google-labs-code/stitch-skills --skill enhance-prompt --global
```

### react-components
Converts Stitch screens to React component systems with automated validation and design token consistency.

```bash
npx skills add google-labs-code/stitch-skills --skill react:components --global
```

### remotion
Generates walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays to showcase app screens professionally.

```bash
npx skills add google-labs-code/stitch-skills --skill remotion --global
```

### shadcn-ui
Expert guidance for integrating and building applications with shadcn/ui components. Helps discover, install, customize, and optimize shadcn/ui components with best practices for React applications.

```bash
npx skills add google-labs-code/stitch-skills --skill shadcn-ui --global
```

## Repository Structure

Every directory within `skills/` or at the root level follows a standardized structure to ensure the AI agent has everything it needs to perform "few-shot" learning and automated quality checks.

```text
skills/[category]/
├── SKILL.md           — The "Mission Control" for the agent
├── scripts/           — Executable enforcers (Validation & Networking)
├── resources/         — The knowledge base (Checklists & Style Guides)
└── examples/          — The "Gold Standard" syntactically valid references
```

## Adding New Skills
All new skills need to follow the file structure above to implement the Agent Skills open standard.

### Great candidates for new skills
* **Validation**: Skills that convert Stitch HTML to other UI frameworks and validate the syntax.
* **Decoupling Data**: Skills that convert static design content into external mock data files.
* **Generate Designs**: Skills that generate new design screens in Stitch from a given set of data.

This is not an officially supported Google product. This project is not eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).

```

### File: skills\react_components\package.json
```json
{
  "name": "react-components",
  "version": "1.0.0",
  "description": "Design-to-code prompt to React components for Stitch MCP",
  "type": "module",
  "scripts": {
    "validate": "node scripts/validate.js",
    "fetch": "bash scripts/fetch-stitch.sh"
  },
  "dependencies": {
    "@swc/core": "^1.3.100"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

### File: skills\react_components\README.md
```md
# Stitch to React Components Skill

## Install

```bash
npx skills add google-labs-code/stitch-skills --skill react:components --global
```

## Example Prompt

```text
Convert my Landing Page screen in my Podcast Stitch Project to a React component system.
```

## Skill Structure

This repository follows the **Agent Skills** open standard. Each skill is self-contained with its own logic, validation scripts, and design tokens.

```text
skills/react-components/
├── SKILL.md           — Core instructions & workflow
├── package.json       — Validator dependencies
├── scripts/           — Networking & AST validation
├── resources/         — Style guides & API references
└── examples/          — Gold-standard code samples
```

## How it Works

When activated, the agent follows a high-fidelity engineering pipeline:

1. **Retrieval**: Uses a system-level `curl` script to bypass TLS/SNI issues on Google Cloud Storage.
2. **Mapping**: Cross-references Stitch metadata with the local `style-guide.json` to ensure token consistency.
3. **Generation**: Scaffolds components using a strict Atomic Design pattern.
4. **Validation**: Runs an automated AST check using `@swc/core` to prevent hardcoded hex values or missing interfaces.
5. **Audit**: Performs a final self-correction check against a 20-point architecture checklist.

```

### File: skills\stitch_design\README.md
```md
# Stitch Design Skill

Teaches agents to generate high-fidelity, consistent UI designs and maintain project-level design systems using Stitch.

## Install

```bash
npx skills add google-labs-code/stitch-skills --skill stitch-design --global
```

## What It Does

Enables professional-grade UI/UX design workflows through Stitch MCP:

1. **Prompt Enhancement**: Transforms rough intent into structured, high-fidelity prompts with professional terminology and design system context.
2. **Design System Synthesis**: Analyzes existing Stitch projects to create and maintain a `.stitch/DESIGN.md` "source of truth".
3. **Iterative Generation**: Selects the best generation or editing workflow (`edit_screens`, `generate_variants`) based on user intent.
4. **Asset Management**: Synchronizes remote designs by downloading HTML and screenshots to the project's `.stitch/designs` directory.

## Prerequisites

- Stitch MCP Server access
- A project `projectId` (can be discovered via `list_projects`)

## Example Prompt

```text
Design a premium landing page for a mountain resort with a focus on serene luxury and glassmorphism.
```

## Skill Structure

```
stitch-design/
├── SKILL.md           — Core instructions & Prompt Pipeline
├── README.md          — This file
├── workflows/         — Specialized pipelines (Text-to-UI, Edit, MD)
├── references/        — UI/UX keywords & Technical Mappings
└── examples/          — Gold-standard references (Solace Mindfulness)
```

## Works With

- **`react:components` skill**: Hand-off generated designs for frontend implementation.
- **`stitch-loop` skill**: Provides the `DESIGN.md` context for autonomous building loops.
- **Multi-agent workflows**: Refines prompts before passing design tasks to specialized agents.

## Learn More

See [SKILL.md](./SKILL.md) for complete instructions.

```

### File: CONTRIBUTING.md
```md
# How to Contribute

We'd love to accept your patches and contributions to this project. There are just a few small guidelines you need to follow.

## Before you begin

### Sign our Contributor License Agreement

Contributions to this project must be accompanied by a [Contributor License Agreement](https://cla.developers.google.com/about) (CLA). You (or your employer) retain the copyright to your contribution; this simply gives us permission to use and redistribute your contributions as part of the project.

If you or your current employer have already signed the Google CLA (even if it was for a different project), you probably don't need to do it again.

Visit <https://cla.developers.google.com/> to see your current agreements or to sign a new one.

### Review our community guidelines

This project follows [Google's Open Source Community Guidelines](https://opensource.google/conduct/).

## Contribution process

1.  Fork the repository
2.  Create a feature branch
3.  Commit your changes
4.  Push to the branch
5.  Create a new Pull Request

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

To report a security vulnerability, please use the [GitHub Security Advisory "Report a Vulnerability" tab](https://github.com/google-labs-code/jules-sdk/security/advisories/new).

> **Note:** This is not an officially supported Google product. This project is not eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).
```

### File: skills\design_md\SKILL.md
```md
---
name: design-md
description: Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
  - "web_fetch"
---

# Stitch DESIGN.md Skill

You are an expert Design Systems Lead. Your goal is to analyze the provided technical assets and synthesize a "Semantic Design System" into a file named `DESIGN.md`.

## Overview

This skill helps you create `DESIGN.md` files that serve as the "source of truth" for prompting Stitch to generate new screens that align perfectly with existing design language. Stitch interprets design through "Visual Descriptions" supported by specific color values.

## Prerequisites

- Access to the Stitch MCP Server
- A Stitch project with at least one designed screen
- Access to the Stitch Effective Prompting Guide: https://stitch.withgoogle.com/docs/learn/prompting/

## The Goal

The `DESIGN.md` file will serve as the "source of truth" for prompting Stitch to generate new screens that align perfectly with the existing design language. Stitch interprets design through "Visual Descriptions" supported by specific color values.

## Retrieval and Networking

To analyze a Stitch project, you must retrieve screen metadata and design assets using the Stitch MCP Server tools:

1. **Namespace discovery**: Run `list_tools` to find the Stitch MCP prefix. Use this prefix (e.g., `mcp_stitch:`) for all subsequent calls.

2. **Project lookup** (if Project ID is not provided):
   - Call `[prefix]:list_projects` with `filter: "view=owned"` to retrieve all user projects
   - Identify the target project by title or URL pattern
   - Extract the Project ID from the `name` field (e.g., `projects/13534454087919359824`)

3. **Screen lookup** (if Screen ID is not provided):
   - Call `[prefix]:list_screens` with the `projectId` (just the numeric ID, not the full path)
   - Review screen titles to identify the target screen (e.g., "Home", "Landing Page")
   - Extract the Screen ID from the screen's `name` field

4. **Metadata fetch**: 
   - Call `[prefix]:get_screen` with both `projectId` and `screenId` (both as numeric IDs only)
   - This returns the complete screen object including:
     - `screenshot.downloadUrl` - Visual reference of the design
     - `htmlCode.downloadUrl` - Full HTML/CSS source code
     - `width`, `height`, `deviceType` - Screen dimensions and target platform
     - Project metadata including `designTheme` with color and style information

5. **Asset download**:
   - Use `web_fetch` or `read_url_content` to download the HTML code from `htmlCode.downloadUrl`
   - Optionally download the screenshot from `screenshot.downloadUrl` for visual reference
   - Parse the HTML to extract Tailwind classes, custom CSS, and component patterns

6. **Project metadata extraction**:
   - Call `[prefix]:get_project` with the project `name` (full path: `projects/{id}`) to get:
     - `designTheme` object with color mode, fonts, roundness, custom colors
     - Project-level design guidelines and descriptions
     - Device type preferences and layout principles

## Analysis & Synthesis Instructions

### 1. Extract Project Identity (JSON)
- Locate the Project Title
- Locate the specific Project ID (e.g., from the `name` field in the JSON)

### 2. Define the Atmosphere (Image/HTML)
Evaluate the screenshot and HTML structure to capture the overall "vibe." Use evocative adjectives to describe the mood (e.g., "Airy," "Dense," "Minimalist," "Utilitarian").

### 3. Map the Color Palette (Tailwind Config/JSON)
Identify the key colors in the system. For each color, provide:
- A descriptive, natural language name that conveys its character (e.g., "Deep Muted Teal-Navy")
- The specific hex code in parentheses for precision (e.g., "#294056")
- Its specific functional role (e.g., "Used for primary actions")

### 4. Translate Geometry & Shape (CSS/Tailwind)
Convert technical `border-radius` and layout values into physical descriptions:
- Describe `rounded-full` as "Pill-shaped"
- Describe `rounded-lg` as "Subtly rounded corners"
- Describe `rounded-none` as "Sharp, squared-off edges"

### 5. Describe Depth & Elevation
Explain how the UI handles layers. Describe the presence and quality of shadows (e.g., "Flat," "Whisper-soft diffused shadows," or "Heavy, high-contrast drop shadows").

## Output Guidelines

- **Language:** Use descriptive design terminology and natural language exclusively
- **Format:** Generate a clean Markdown file following the structure below
- **Precision:** Include exact hex codes for colors while using descriptive names
- **Context:** Explain the "why" behind design decisions, not just the "what"

## Output Format (DESIGN.md Structure)

```markdown
# Design System: [Project Title]
**Project ID:** [Insert Project ID Here]

## 1. Visual Theme & Atmosphere
(Description of the mood, density, and aesthetic philosophy.)

## 2. Color Palette & Roles
(List colors by Descriptive Name + Hex Code + Functional Role.)

## 3. Typography Rules
(Description of font family, weight usage for headers vs. body, and letter-spacing character.)

## 4. Component Stylings
* **Buttons:** (Shape description, color assignment, behavior).
* **Cards/Containers:** (Corner roundness description, background color, shadow depth).
* **Inputs/Forms:** (Stroke style, background).

## 5. Layout Principles
(Description of whitespace strategy, margins, and grid alignment.)
```

## Usage Example

To use this skill for the Furniture Collection project:

1. **Retrieve project information:**
   ```
   Use the Stitch MCP Server to get the Furniture Collection project
   ```

2. **Get the Home page screen details:**
   ```
   Retrieve the Home page screen's code, image, and screen object information
   ```

3. **Reference best practices:**
   ```
   Review the Stitch Effective Prompting Guide at:
   https://stitch.withgoogle.com/docs/learn/prompting/
   ```

4. **Analyze and synthesize:**
   - Extract all relevant design tokens from the screen
   - Translate technical values into descriptive language
   - Organize information according to the DESIGN.md structure

5. **Generate the file:**
   - Create `DESIGN.md` in the project directory
   - Follow the prescribed format exactly
   - Ensure all color codes are accurate
   - Use evocative, designer-friendly language

## Best Practices

- **Be Descriptive:** Avoid generic terms like "blue" or "rounded." Use "Ocean-deep Cerulean (#0077B6)" or "Gently curved edges"
- **Be Functional:** Always explain what each design element is used for
- **Be Consistent:** Use the same terminology throughout the document
- **Be Visual:** Help readers visualize the design through your descriptions
- **Be Precise:** Include exact values (hex codes, pixel values) in parentheses after natural language descriptions

## Tips for Success

1. **Start with the big picture:** Understand the overall aesthetic before diving into details
2. **Look for patterns:** Identify consistent spacing, sizing, and styling patterns
3. **Think semantically:** Name colors by their purpose, not just their appearance
4. **Consider hierarchy:** Document how visual weight and importance are communicated
5. **Reference the guide:** Use language and patterns from the Stitch Effective Prompting Guide

## Common Pitfalls to Avoid

- ❌ Using technical jargon without translation (e.g., "rounded-xl" instead of "generously rounded corners")
- ❌ Omitting color codes or using only descriptive names
- ❌ Forgetting to explain functional roles of design elements
- ❌ Being too vague in atmosphere descriptions
- ❌ Ignoring subtle design details like shadows or spacing patterns

```

### File: skills\enhance_prompt\SKILL.md
```md
---
name: enhance-prompt
description: Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better generation results.
allowed-tools:
  - "Read"
  - "Write"
---

# Enhance Prompt for Stitch

You are a **Stitch Prompt Engineer**. Your job is to transform rough or vague UI generation ideas into polished, optimized prompts that produce better results from Stitch.

## Prerequisites

Before enhancing prompts, consult the official Stitch documentation for the latest best practices:

- **Stitch Effective Prompting Guide**: https://stitch.withgoogle.com/docs/learn/prompting/

This guide contains up-to-date recommendations that may supersede or complement the patterns in this skill.

## When to Use This Skill

Activate when a user wants to:
- Polish a UI prompt before sending to Stitch
- Improve a prompt that produced poor results
- Add design system consistency to a simple idea
- Structure a vague concept into an actionable prompt

## Enhancement Pipeline

Follow these steps to enhance any prompt:

### Step 1: Assess the Input

Evaluate what's missing from the user's prompt:

| Element | Check for | If missing... |
|---------|-----------|---------------|
| **Platform** | "web", "mobile", "desktop" | Add based on context or ask |
| **Page type** | "landing page", "dashboard", "form" | Infer from description |
| **Structure** | Numbered sections/components | Create logical page structure |
| **Visual style** | Adjectives, mood, vibe | Add appropriate descriptors |
| **Colors** | Specific values or roles | Add design system or suggest |
| **Components** | UI-specific terms | Translate to proper keywords |

### Step 2: Check for DESIGN.md

Look for a `DESIGN.md` file in the current project:

**If DESIGN.md exists:**
1. Read the file to extract the design system block
2. Include the color palette, typography, and component styles
3. Format as a "DESIGN SYSTEM (REQUIRED)" section in the output

**If DESIGN.md does not exist:**
1. Add this note at the end of the enhanced prompt:

```
---
💡 **Tip:** For consistent designs across multiple screens, create a DESIGN.md 
file using the `design-md` skill. This ensures all generated pages share the 
same visual language.
```

### Step 3: Apply Enhancements

Transform the input using these techniques:

#### A. Add UI/UX Keywords

Replace vague terms with specific component names:

| Vague | Enhanced |
|-------|----------|
| "menu at the top" | "navigation bar with logo and menu items" |
| "button" | "primary call-to-action button" |
| "list of items" | "card grid layout" or "vertical list with thumbnails" |
| "form" | "form with labeled input fields and submit button" |
| "picture area" | "hero section with full-width image" |

#### B. Amplify the Vibe

Add descriptive adjectives to set the mood:

| Basic | Enhanced |
|-------|----------|
| "modern" | "clean, minimal, with generous whitespace" |
| "professional" | "sophisticated, trustworthy, with subtle shadows" |
| "fun" | "vibrant, playful, with rounded corners and bold colors" |
| "dark mode" | "dark theme with high-contrast accents on deep backgrounds" |

#### C. Structure the Page

Organize content into numbered sections:

```markdown
**Page Structure:**
1. **Header:** Navigation with logo and menu items
2. **Hero Section:** Headline, subtext, and primary CTA
3. **Content Area:** [Describe the main content]
4. **Footer:** Links, social icons, copyright
```

#### D. Format Colors Properly

When colors are mentioned, format them as:
```
Descriptive Name (#hexcode) for functional role
```

Examples:
- "Deep Ocean Blue (#1a365d) for primary buttons and links"
- "Warm Cream (#faf5f0) for page background"
- "Soft Gray (#6b7280) for secondary text"

### Step 4: Format the Output

Structure the enhanced prompt in this order:

```markdown
[One-line description of the page purpose and vibe]

**DESIGN SYSTEM (REQUIRED):**
- Platform: [Web/Mobile], [Desktop/Mobile]-first
- Theme: [Light/Dark], [style descriptors]
- Background: [Color description] (#hex)
- Primary Accent: [Color description] (#hex) for [role]
- Text Primary: [Color description] (#hex)
- [Additional design tokens...]

**Page Structure:**
1. **[Section]:** [Description]
2. **[Section]:** [Description]
...
```

## Output Options

**Default:** Return the enhanced prompt as text for the user to copy.

**Optional file output:** If the user requests, write to a file:
- `next-prompt.md` — for use with the `stitch-loop` skill
- Custom filename specified by user

## Examples

### Example 1: Vague Input → Structured Prompt

**User input:**
> "make me a login page"

**Enhanced output:**
```markdown
A clean, trustworthy login page with a centered form and subtle branding.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first
- Theme: Light, minimal, professional
- Background: Clean White (#ffffff)
- Surface: Soft Gray (#f9fafb) for form card
- Primary Accent: Deep Blue (#2563eb) for submit button and links
- Text Primary: Near Black (#111827) for headings
- Text Secondary: Medium Gray (#6b7280) for labels
- Buttons: Subtly rounded (8px), full-width on form
- Cards: Gently rounded (12px), soft shadow for elevation

**Page Structure:**
1. **Header:** Minimal logo, centered
2. **Login Card:** Centered form with email, password fields, "Forgot password?" link
3. **Submit Button:** Primary blue "Sign In" button
4. **Footer:** "Don't have an account? Sign up" link

---
💡 **Tip:** For consistent designs across multiple screens, create a DESIGN.md 
file using the `design-md` skill.
```

### Example 2: Feature Request → Targeted Edit

**User input:**
> "add a search bar"

**Enhanced output:**
```markdown
Add a search bar to the header navigation.

**Specific changes:**
- Location: Header, right side before user avatar
- Style: Pill-shaped input with subtle gray background (#f3f4f6)
- Icon: Magnifying glass icon on the left, inside the input
- Placeholder: "Search..." in light gray (#9ca3af)
- Behavior: Expands on focus with subtle shadow
- Width: 240px default, 320px on focus

**Context:** This is a targeted edit. Make only this change while preserving all existing elements.
```

## Tips for Best Results

1. **Be specific early** — Vague inputs need more enhancement
2. **Match the user's intent** — Don't over-design if they want simple
3. **Keep it structured** — Numbered sections help Stitch understand hierarchy
4. **Include the design system** — Consistency is key for multi-page projects
5. **One change at a time for edits** — Don't bundle unrelated changes

```

### File: skills\react_components\package_lock.json
```json
{
  "name": "stitch-to-react-pro",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "stitch-to-react-pro",
      "version": "1.0.0",
      "dependencies": {
        "@swc/core": "^1.3.100"
      },
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/@swc/core": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core/-/core-1.15.8.tgz",
      "integrity": "sha512-T8keoJjXaSUoVBCIjgL6wAnhADIb09GOELzKg10CjNg+vLX48P93SME6jTfte9MZIm5m+Il57H3rTSk/0kzDUw==",
      "hasInstallScript": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@swc/counter": "^0.1.3",
        "@swc/types": "^0.1.25"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/swc"
      },
      "optionalDependencies": {
        "@swc/core-darwin-arm64": "1.15.8",
        "@swc/core-darwin-x64": "1.15.8",
        "@swc/core-linux-arm-gnueabihf": "1.15.8",
        "@swc/core-linux-arm64-gnu": "1.15.8",
        "@swc/core-linux-arm64-musl": "1.15.8",
        "@swc/core-linux-x64-gnu": "1.15.8",
        "@swc/core-linux-x64-musl": "1.15.8",
        "@swc/core-win32-arm64-msvc": "1.15.8",
        "@swc/core-win32-ia32-msvc": "1.15.8",
        "@swc/core-win32-x64-msvc": "1.15.8"
      },
      "peerDependencies": {
        "@swc/helpers": ">=0.5.17"
      },
      "peerDependenciesMeta": {
        "@swc/helpers": {
          "optional": true
        }
      }
    },
    "node_modules/@swc/core-darwin-arm64": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-darwin-arm64/-/core-darwin-arm64-1.15.8.tgz",
      "integrity": "sha512-M9cK5GwyWWRkRGwwCbREuj6r8jKdES/haCZ3Xckgkl8MUQJZA3XB7IXXK1IXRNeLjg6m7cnoMICpXv1v1hlJOg==",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-darwin-x64": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-darwin-x64/-/core-darwin-x64-1.15.8.tgz",
      "integrity": "sha512-j47DasuOvXl80sKJHSi2X25l44CMc3VDhlJwA7oewC1nV1VsSzwX+KOwE5tLnfORvVJJyeiXgJORNYg4jeIjYQ==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-linux-arm-gnueabihf": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-linux-arm-gnueabihf/-/core-linux-arm-gnueabihf-1.15.8.tgz",
      "integrity": "sha512-siAzDENu2rUbwr9+fayWa26r5A9fol1iORG53HWxQL1J8ym4k7xt9eME0dMPXlYZDytK5r9sW8zEA10F2U3Xwg==",
      "cpu": [
        "arm"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-linux-arm64-gnu": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-linux-arm64-gnu/-/core-linux-arm64-gnu-1.15.8.tgz",
      "integrity": "sha512-o+1y5u6k2FfPYbTRUPvurwzNt5qd0NTumCTFscCNuBksycloXY16J8L+SMW5QRX59n4Hp9EmFa3vpvNHRVv1+Q==",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-linux-arm64-musl": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-linux-arm64-musl/-/core-linux-arm64-musl-1.15.8.tgz",
      "integrity": "sha512-koiCqL09EwOP1S2RShCI7NbsQuG6r2brTqUYE7pV7kZm9O17wZ0LSz22m6gVibpwEnw8jI3IE1yYsQTVpluALw==",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-linux-x64-gnu": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-linux-x64-gnu/-/core-linux-x64-gnu-1.15.8.tgz",
      "integrity": "sha512-4p6lOMU3bC+Vd5ARtKJ/FxpIC5G8v3XLoPEZ5s7mLR8h7411HWC/LmTXDHcrSXRC55zvAVia1eldy6zDLz8iFQ==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-linux-x64-musl": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-linux-x64-musl/-/core-linux-x64-musl-1.15.8.tgz",
      "integrity": "sha512-z3XBnbrZAL+6xDGAhJoN4lOueIxC/8rGrJ9tg+fEaeqLEuAtHSW2QHDHxDwkxZMjuF/pZ6MUTjHjbp8wLbuRLA==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-win32-arm64-msvc": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-win32-arm64-msvc/-/core-win32-arm64-msvc-1.15.8.tgz",
      "integrity": "sha512-djQPJ9Rh9vP8GTS/Df3hcc6XP6xnG5c8qsngWId/BLA9oX6C7UzCPAn74BG/wGb9a6j4w3RINuoaieJB3t+7iQ==",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-win32-ia32-msvc": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-win32-ia32-msvc/-/core-win32-ia32-msvc-1.15.8.tgz",
      "integrity": "sha512-/wfAgxORg2VBaUoFdytcVBVCgf1isWZIEXB9MZEUty4wwK93M/PxAkjifOho9RN3WrM3inPLabICRCEgdHpKKQ==",
      "cpu": [
        "ia32"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/core-win32-x64-msvc": {
      "version": "1.15.8",
      "resolved": "https://registry.npmjs.org/@swc/core-win32-x64-msvc/-/core-win32-x64-msvc-1.15.8.tgz",
      "integrity": "sha512-GpMePrh9Sl4d61o4KAHOOv5is5+zt6BEXCOCgs/H0FLGeii7j9bWDE8ExvKFy2GRRZVNR1ugsnzaGWHKM6kuzA==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0 AND MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@swc/counter": {
      "version": "0.1.3",
      "resolved": "https://registry.npmjs.org/@swc/counter/-/counter-0.1.3.tgz",
      "integrity": "sha512-e2BR4lsJkkRlKZ/qCHPw9ZaSxc0MVUd7gtbtaB7aMvHeJVYe8sOB8DBZkP2DtISHGSku9sCK6T6cnY0CtXrOCQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@swc/types": {
      "version": "0.1.25",
      "resolved": "https://registry.npmjs.org/@swc/types/-/types-0.1.25.tgz",
      "integrity": "sha512-iAoY/qRhNH8a/hBvm3zKj9qQ4oc2+3w1unPJa2XvTK3XjeLXtzcCingVPw/9e5mn1+0yPqxcBGp9Jf0pkfMb1g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@swc/counter": "^0.1.3"
      }
    }
  }
}

```

### File: skills\react_components\SKILL.md
```md
---
name: react:components
description: Converts Stitch designs into modular Vite and React components using system-level networking and AST-based validation.
allowed-tools:
  - "stitch*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
---

# Stitch to React Components

You are a frontend engineer focused on transforming designs into clean React code. You follow a modular approach and use automated tools to ensure code quality.

## Retrieval and networking
1. **Namespace discovery**: Run `list_tools` to find the Stitch MCP prefix. Use this prefix (e.g., `stitch:`) for all subsequent calls.
2. **Metadata fetch**: Call `[prefix]:get_screen` to retrieve the design JSON.
3. **Check for existing designs**: Before downloading, check if `.stitch/designs/{page}.html` and `.stitch/designs/{page}.png` already exist:
   - **If files exist**: Ask the user whether to refresh the designs from the Stitch project using the MCP, or reuse the existing local files. Only re-download if the user confirms.
   - **If files do not exist**: Proceed to step 4.
4. **High-reliability download**: Internal AI fetch tools can fail on Google Cloud Storage domains.
   - **HTML**: `bash scripts/fetch-stitch.sh "[htmlCode.downloadUrl]" ".stitch/designs/{page}.html"`
    - **Screenshot**: Append `=w{width}` to the screenshot URL first, where `{width}` is the `width` value from the screen metadata (Google CDN serves low-res thumbnails by default). Then run: `bash scripts/fetch-stitch.sh "[screenshot.downloadUrl]=w{width}" ".stitch/designs/{page}.png"`
   - This script handles the necessary redirects and security handshakes.
5. **Visual audit**: Review the downloaded screenshot (`.stitch/designs/{page}.png`) to confirm design intent and layout details.

## Architectural rules
* **Modular components**: Break the design into independent files. Avoid large, single-file outputs.
* **Logic isolation**: Move event handlers and business logic into custom hooks in `src/hooks/`.
* **Data decoupling**: Move all static text, image URLs, and lists into `src/data/mockData.ts`.
* **Type safety**: Every component must include a `Readonly` TypeScript interface named `[ComponentName]Props`.
* **Project specific**: Focus on the target project's needs and constraints. Leave Google license headers out of the generated React components.
* **Style mapping**:
    * Extract the `tailwind.config` from the HTML `<head>`.
    * Sync these values with `resources/style-guide.json`.
    * Use theme-mapped Tailwind classes instead of arbitrary hex codes.

## Execution steps
1. **Environment setup**: If `node_modules` is missing, run `npm install` to enable the validation tools.
2. **Data layer**: Create `src/data/mockData.ts` based on the design content.
3. **Component drafting**: Use `resources/component-template.tsx` as a base. Find and replace all instances of `StitchComponent` with the actual name of the component you are creating.
4. **Application wiring**: Update the project entry point (like `App.tsx`) to render the new components.
5. **Quality check**:
    * Run `npm run validate <file_path>` for each component.
    * Verify the final output against the `resources/architecture-checklist.md`.
    * Start the dev server with `npm run dev` to verify the live result.

## Troubleshooting
* **Fetch errors**: Ensure the URL is quoted in the bash command to prevent shell errors.
* **Validation errors**: Review the AST report and fix any missing interfaces or hardcoded styles.
```

### File: skills\remotion\SKILL.md
```md
---
name: remotion
description: Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays
allowed-tools:
  - "stitch*:*"
  - "remotion*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
---

# Stitch to Remotion Walkthrough Videos

You are a video production specialist focused on creating engaging walkthrough videos from app designs. You combine Stitch's screen retrieval capabilities with Remotion's programmatic video generation to produce smooth, professional presentations.

## Overview

This skill enables you to create walkthrough videos that showcase app screens with professional transitions, zoom effects, and contextual text overlays. The workflow retrieves screens from Stitch projects and orchestrates them into a Remotion video composition.

## Prerequisites

**Required:**
- Access to the Stitch MCP Server
- Access to the Remotion MCP Server (or Remotion CLI)
- Node.js and npm installed
- A Stitch project with designed screens

**Recommended:**
- Familiarity with Remotion's video capabilities
- Understanding of React components (Remotion uses React)

## Retrieval and Networking

### Step 1: Discover Available MCP Servers

Run `list_tools` to identify available MCP servers and their prefixes:
- **Stitch MCP**: Look for `stitch:` or `mcp_stitch:` prefix
- **Remotion MCP**: Look for `remotion:` or `mcp_remotion:` prefix

### Step 2: Retrieve Stitch Project Information

1. **Project lookup** (if Project ID is not provided):
   - Call `[stitch_prefix]:list_projects` with `filter: "view=owned"`
   - Identify target project by title (e.g., "Calculator App")
   - Extract Project ID from `name` field (e.g., `projects/13534454087919359824`)

2. **Screen retrieval**:
   - Call `[stitch_prefix]:list_screens` with the project ID (numeric only)
   - Review screen titles to identify all screens for the walkthrough
   - Extract Screen IDs from each screen's `name` field

3. **Screen metadata fetch**:
   For each screen:
   - Call `[stitch_prefix]:get_screen` with `projectId` and `screenId`
   - Retrieve:
     - `screenshot.downloadUrl` — Visual asset for the video
     - `htmlCode.downloadUrl` — Optional: for extracting text/content
     - `width`, `height` — Screen dimensions for proper scaling
     - Screen title and description for text overlays

4. **Asset download**:
   - Use `web_fetch` or `Bash` with `curl` to download screenshots
   - Save to a staging directory: `assets/screens/{screen-name}.png`
   - Organize assets in order of the intended walkthrough flow

### Step 3: Set Up Remotion Project

1. **Check for existing Remotion project**:
   - Look for `remotion.config.ts` or `package.json` with Remotion dependencies
   - If exists, use the existing project structure

2. **Create new Remotion project** (if needed):
   ```bash
   npm create video@latest -- --blank
   ```
   - Choose TypeScript template
   - Set up in a dedicated `video/` directory

3. **Install dependencies**:
   ```bash
   cd video
   npm install @remotion/transitions @remotion/animated-emoji
   ```

## Video Composition Strategy

### Architecture

Create a modular Remotion composition with these components:

1. **`ScreenSlide.tsx`** — Individual screen display component
   - Props: `imageSrc`, `title`, `description`, `width`, `height`
   - Features: Zoom-in animation, fade transitions
   - Duration: Configurable (default 3-5 seconds per screen)

2. **`WalkthroughComposition.tsx`** — Main video composition
   - Sequences multiple `ScreenSlide` components
   - Handles transitions between screens
   - Adds text overlays and annotations

3. **`config.ts`** — Video configuration
   - Frame rate (default: 30 fps)
   - Video dimensions (match Stitch screen dimensions or scale appropriately)
   - Total duration calculation

### Transition Effects

Use Remotion's `@remotion/transitions` for professional effects:

- **Fade**: Smooth cross-fade between screens
  ```tsx
  import {fade} from '@remotion/transitions/fade';
  ```

- **Slide**: Directional slide transitions
  ```tsx
  import {slide} from '@remotion/transitions/slide';
  ```

- **Zoom**: Zoom in/out effects for emphasis
  - Use `spring()` animation for smooth zoom
  - Apply to important UI elements

### Text Overlays

Add contextual information using Remotion's text rendering:

1. **Screen titles**: Display at the top or bottom of each frame
2. **Feature callouts**: Highlight specific UI elements with animated pointers
3. **Descriptions**: Fade in descriptive text for each screen
4. **Progress indicator**: Show current screen position in walkthrough

## Execution Steps

### Step 1: Gather Screen Assets

1. Identify target Stitch project
2. List all screens in the project
3. Download screenshots for each screen
4. Organize in order of walkthrough flow
5. Create a manifest file (`screens.json`):

```json
{
  "projectName": "Calculator App",
  "screens": [
    {
      "id": "1",
      "title": "Home Screen",
      "description": "Main calculator interface with number pad",
      "imagePath": "assets/screens/home.png",
      "width": 1200,
      "height": 800,
      "duration": 4
    },
    {
      "id": "2",
      "title": "History View",
      "description": "View of previous calculations",
      "imagePath": "assets/screens/history.png",
      "width": 1200,
      "height": 800,
      "duration": 3
    }
  ]
}
```

### Step 2: Generate Remotion Components

Create the video components following Remotion best practices:

1. **Create `ScreenSlide.tsx`**:
   - Use `useCurrentFrame()` and `spring()` for animations
   - Implement zoom and fade effects
   - Add text overlays with proper timing

2. **Create `WalkthroughComposition.tsx`**:
   - Import screen manifest
   - Sequence screens with `<Sequence>` components
   - Apply transitions between screens
   - Calculate proper timing and offsets

3. **Update `remotion.config.ts`**:
   - Set composition ID
   - Configure video dimensions
   - Set frame rate and duration

**Reference Resources:**
- Use `resources/screen-slide-template.tsx` as starting point
- Follow `resources/composition-checklist.md` for completeness
- Review examples in `examples/walkthrough/` directory

### Step 3: Preview and Refine

1. **Start Remotion Studio**:
   ```bash
   npm run dev
   ```
   - Opens browser-based preview
   - Allows real-time editing and refinement

2. **Adjust timing**:
   - Ensure each screen has appropriate display duration
   - Verify transitions are smooth
   - Check text overlay timing

3. **Fine-tune animations**:
   - Adjust spring configurations for zoom effects
   - Modify easing functions for transitions
   - Ensure text is readable at all times

### Step 4: Render Video

1. **Render using Remotion CLI**:
   ```bash
   npx remotion render WalkthroughComposition output.mp4
   ```

2. **Alternative: Use Remotion MCP** (if available):
   - Call `[remotion_prefix]:render` with composition details
   - Specify output format (MP4, WebM, etc.)

3. **Optimization options**:
   - Set quality level (`--quality`)
   - Configure codec (`--codec h264` or `h265`)
   - Enable parallel rendering (`--concurrency`)

## Advanced Features

### Interactive Hotspots

Highlight clickable elements or important features:

```tsx
import {interpolate, useCurrentFrame} from 'remotion';

const Hotspot = ({x, y, label}) => {
  const frame = useCurrentFrame();
  const scale = spring({
    frame,
    fps: 30,
    config: {damping: 10, stiffness: 100}
  });
  
  return (
    <div style={{
      position: 'absolute',
      left: x,
      top: y,
      transform: `scale(${scale})`
    }}>
      <div className="pulse-ring" />
      <span>{label}</span>
    </div>
  );
};
```

### Voiceover Integration

Add narration to the walkthrough:

1. Generate voiceover script from screen descriptions
2. Use text-to-speech or record audio
3. Import audio into Remotion with `<Audio>` component
4. Sync screen timing with voiceover pacing

### Dynamic Text Extraction

Extract text from Stitch HTML code for automatic annotations:

1. Download `htmlCode.downloadUrl` for each screen
2. Parse HTML to extract key text elements (headings, buttons, labels)
3. Generate automatic callouts for important UI elements
4. Add to composition as timed text overlays

## File Structure

```
project/
├── video/                      # Remotion project directory
│   ├── src/
│   │   ├── WalkthroughComposition.tsx
│   │   ├── ScreenSlide.tsx
│   │   ├── components/
│   │   │   ├── Hotspot.tsx
│   │   │   └── TextOverlay.tsx
│   │   └── Root.tsx
│   ├── public/
│   │   └── assets/
│   │       └── screens/        # Downloaded Stitch screenshots
│   │           ├── home.png
│   │           └── history.png
│   ├── remotion.config.ts
│   └── package.json
├── screens.json                # Screen manifest
└── output.mp4                  # Rendered video
```

## Integration with Remotion Skills

Remotion maintains its own Agent Skills that define best practices. Review these for advanced techniques:

- **Repository**: https://github.com/remotion-dev/remotion/tree/main/packages/skills
- **Installation**: `npx skills add remotion-dev/skills`

Key Remotion skills to leverage:
- Animation timing and easing
- Composition architecture patterns
- Performance optimization
- Audio synchronization

## Common Patterns

### Pattern 1: Simple Slide Show

Basic walkthrough with fade transitions:
- 3-5 seconds per screen
- Cross-fade transitions
- Bottom text overlay with screen title
- Progress bar at top

### Pattern 2: Feature Highlight

Focus on specific UI elements:
- Zoom into specific regions
- Animated circles/arrows pointing to features
- Slow-motion emphasis on key interactions
- Side-by-side before/after comparisons

### Pattern 3: User Flow

Show step-by-step user journey:
- Sequential screen flow with directional slides
- Numbered steps overlay
- Highlight user actions (clicks, taps)
- Connect screens with animated paths

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Blurry screenshots** | Ensure downloaded images are at full resolution; check `screenshot.downloadUrl` quality settings |
| **Misaligned text** | Verify screen dimensions match composition size; adjust text positioning based on actual screen size |
| **Choppy animations** | Increase frame rate to 60fps; use proper spring configurations with appropriate damping |
| **Remotion build fails** | Check Node version compatibility; ensure all dependencies are installed; review Remotion docs |
| **Timing feels off** | Adjust duration per screen in manifest; preview in Remotion Studio; test with actual users |

## Best Practices

1. **Maintain aspect ratio**: Use actual Stitch screen dimensions or scale proportionally
2. **Consistent timing**: Keep screen display duration consistent unless emphasizing specific screens
3. **Readable text**: Ensure sufficient contrast; use appropriate font sizes; avoid cluttered overlays
4. **Smooth transitions**: Use spring animations for natural motion; avoid jarring cuts
5. **Preview thoroughly**: Always preview in Remotion Studio before final render
6. **Optimize assets**: Compress images appropriately; use efficient formats (PNG for UI, JPG for photos)

## Example Usage

**User prompt:**
```
Look up the screens in my Stitch project "Calculator App" and build a remotion video 
that shows a walkthrough of the screens.
```

**Agent workflow:**
1. List Stitch projects → Find "Calculator App" → Extract project ID
2. List screens in project → Identify all screens (Home, History, Settings)
3. Download screenshots for each screen → Save to `assets/screens/`
4. Create `screens.json` manifest with screen metadata
5. Generate Remotion components (`ScreenSlide.tsx`, `WalkthroughComposition.tsx`)
6. Preview in Remotion Studio → Refine timing and transitions
7. Render final video → `calculator-walkthrough.mp4`
8. Report completion with video preview link

## Tips for Success

- **Start simple**: Begin with basic fade transitions before adding complex animations
- **Follow Remotion patterns**: Leverage Remotion's official skills and documentation
- **Use manifest files**: Keep screen data organized in JSON for easy updates
- **Preview frequently**: Use Remotion Studio to catch issues early
- **Consider accessibility**: Add captions; ensure text is readable; use clear visuals
- **Optimize for platform**: Match video dimensions to target platform (YouTube, social media, etc.)

## References

- **Stitch Documentation**: https://stitch.withgoogle.com/docs/
- **Remotion Documentation**: https://www.remotion.dev/docs/
- **Remotion Skills**: https://www.remotion.dev/docs/ai/skills
- **Remotion MCP**: https://www.remotion.dev/docs/ai/mcp
- **Remotion Transitions**: https://www.remotion.dev/docs/transitions

```

### File: skills\shadcn_ui\SKILL.md
```md
---
name: shadcn-ui
description: Expert guidance for integrating and building applications with shadcn/ui components, including component discovery, installation, customization, and best practices.
allowed-tools:
  - "shadcn*:*"
  - "mcp_shadcn*"
  - "Read"
  - "Write"
  - "Bash"
  - "web_fetch"
---

# shadcn/ui Component Integration

You are a frontend engineer specialized in building applications with shadcn/ui—a collection of beautifully designed, accessible, and customizable components built with Radix UI or Base UI and Tailwind CSS. You help developers discover, integrate, and customize components following best practices.

## Core Principles

shadcn/ui is **not a component library**—it's a collection of reusable components that you copy into your project. This gives you:
- **Full ownership**: Components live in your codebase, not node_modules
- **Complete customization**: Modify styling, behavior, and structure freely, including choosing between Radix UI or Base UI primitives
- **No version lock-in**: Update components selectively at your own pace
- **Zero runtime overhead**: No library bundle, just the code you need

## Component Discovery and Installation

### 1. Browse Available Components

Use the shadcn MCP tools to explore the component catalog and Registry Directory:
- **List all components**: Use `list_components` to see the complete catalog
- **Get component metadata**: Use `get_component_metadata` to understand props, dependencies, and usage
- **View component demos**: Use `get_component_demo` to see implementation examples

### 2. Component Installation

There are two approaches to adding components:

**A. Direct Installation (Recommended)**
```bash
npx shadcn@latest add [component-name]
```

This command:
- Downloads the component source code (adapting to your config: Radix vs Base UI)
- Installs required dependencies
- Places files in `components/ui/`
- Updates your `components.json` config

**B. Manual Integration**
1. Use `get_component` to retrieve the source code
2. Create the file in `components/ui/[component-name].tsx`
3. Install peer dependencies manually
4. Adjust imports if needed

### 3. Registry and Custom Registries

If working with a custom registry (defined in `components.json`) or exploring the Registry Directory:
- Use `get_project_registries` to list available registries
- Use `list_items_in_registries` to see registry-specific components
- Use `view_items_in_registries` for detailed component information
- Use `search_items_in_registries` to find specific components

## Project Setup

### Initial Configuration

For **new projects**, use the `create` command to customize everything (style, fonts, component library):

```bash
npx shadcn@latest create
```

For **existing projects**, initialize configuration:

```bash
npx shadcn@latest init
```

This creates `components.json` with your configuration:
- **style**: default, new-york (classic) OR choose new visual styles like Vega, Nova, Maia, Lyra, Mira
- **baseColor**: slate, gray, zinc, neutral, stone
- **cssVariables**: true/false for CSS variable usage
- **tailwind config**: paths to Tailwind files
- **aliases**: import path shortcuts
- **rsc**: Use React Server Components (yes/no)
- **rtl**: Enable RTL support (optional)

### Required Dependencies

shadcn/ui components require:
- **React** (18+)
- **Tailwind CSS** (3.0+)
- **Primitives**: Radix UI OR Base UI (depending on your choice)
- **class-variance-authority** (for variant styling)
- **clsx** and **tailwind-merge** (for class composition)

## Component Architecture

### File Structure
```
src/
├── components/
│   ├── ui/              # shadcn components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   └── dialog.tsx
│   └── [custom]/        # your composed components
│       └── user-card.tsx
├── lib/
│   └── utils.ts         # cn() utility
└── app/
    └── page.tsx
```

### The `cn()` Utility

All shadcn components use the `cn()` helper for class merging:

```typescript
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

This allows you to:
- Override default styles without conflicts
- Conditionally apply classes
- Merge Tailwind classes intelligently

## Customization Best Practices

### 1. Theme Customization

Edit your Tailwind config and CSS variables in `app/globals.css`:

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    /* ... more variables */
  }
  
  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    /* ... dark mode overrides */
  }
}
```

### 2. Component Variants

Use `class-variance-authority` (cva) for variant logic:

```typescript
import { cva } from "class-variance-authority"

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground",
        outline: "border border-input",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)
```

### 3. Extending Components

Create wrapper components in `components/` (not `components/ui/`):

```typescript
// components/custom-button.tsx
import { Button } from "@/components/ui/button"
import { Loader2 } from "lucide-react"

export function LoadingButton({ 
  loading, 
  children, 
  ...props 
}: ButtonProps & { loading?: boolean }) {
  return (
    <Button disabled={loading} {...props}>
      {loading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
      {children}
    </Button>
  )
}
```

## Blocks and Complex Components

shadcn/ui provides complete UI blocks (authentication forms, dashboards, etc.):

1. **List available blocks**: Use `list_blocks` with optional category filter
2. **Get block source**: Use `get_block` with the block name
3. **Install blocks**: Many blocks include multiple component files

Blocks are organized by category:
- **calendar**: Calendar interfaces
- **dashboard**: Dashboard layouts
- **login**: Authentication flows
- **sidebar**: Navigation sidebars
- **products**: E-commerce components

## Accessibility

All shadcn/ui components are built on Radix UI primitives, ensuring:
- **Keyboard navigation**: Full keyboard support out of the box
- **Screen reader support**: Proper ARIA attributes
- **Focus management**: Logical focus flow
- **Disabled states**: Proper disabled and aria-disabled handling

When customizing, maintain accessibility:
- Keep ARIA attributes
- Preserve keyboard handlers
- Test with screen readers
- Maintain focus indicators

## Common Patterns

### Form Building
```typescript
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

// Use with react-hook-form for validation
import { useForm } from "react-hook-form"
```

### Dialog/Modal Patterns
```typescript
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

### Data Display
```typescript
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

## Troubleshooting

### Import Errors
- Check `components.json` for correct alias configuration
- Verify `tsconfig.json` includes the `@` path alias:
  ```json
  {
    "compilerOptions": {
      "paths": {
        "@/*": ["./src/*"]
      }
    }
  }
  ```

### Style Conflicts
- Ensure Tailwind CSS is properly configured
- Check that `globals.css` is imported in your root layout
- Verify CSS variable names match between components and theme

### Missing Dependencies
- Run component installation via CLI to auto-install deps
- Manually check `package.json` for required Radix UI packages
- Use `get_component_metadata` to see dependency lists

### Version Compatibility
- shadcn/ui v4 requires React 18+ and Next.js 13+ (if using Next.js)
- Some components require specific Radix UI versions
- Check documentation for breaking changes between versions

## Validation and Quality

Before committing components:
1. **Type check**: Run `tsc --noEmit` to verify TypeScript
2. **Lint**: Run your linter to catch style issues
3. **Test accessibility**: Use tools like axe DevTools
4. **Visual QA**: Test in light and dark modes
5. **Responsive check**: Verify behavior at different breakpoints

## Resources

Refer to the following resource files for detailed guidance:
- `resources/setup-guide.md` - Step-by-step project initialization
- `resources/component-catalog.md` - Complete component reference
- `resources/customization-guide.md` - Theming and variant patterns
- `resources/migration-guide.md` - Upgrading from other UI libraries

## Examples

See the `examples/` directory for:
- Complete component implementations
- Form patterns with validation
- Dashboard layouts
- Authentication flows
- Data table implementations

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
