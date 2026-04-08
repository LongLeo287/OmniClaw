---
id: repo-fetched-baoyu-skills-060115-060151
type: knowledge
owner: OA
registered_at: 2026-04-05T03:48:55.289314
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_baoyu-skills_060115_060151

## Assimilation Report
Auto-cloned repository: FETCHED_baoyu-skills_060115_060151

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# baoyu-skills

English | [中文](./README.zh.md)

Skills shared by Baoyu for improving daily work efficiency with Claude Code.

## Prerequisites

- Node.js environment installed
- Ability to run `npx bun` commands

## Installation

### Quick Install (Recommended)

```bash
npx skills add jimliu/baoyu-skills
```

### Publish to ClawHub / OpenClaw

This repository now supports publishing each `skills/baoyu-*` directory as an individual ClawHub skill.

```bash
# Preview what would be published
./scripts/sync-clawhub.sh --dry-run

# Publish all changed skills from ./skills
./scripts/sync-clawhub.sh --all
```

ClawHub installs skills individually, not as one marketplace bundle. After publishing, users can install specific skills such as:

```bash
clawhub install baoyu-imagine
clawhub install baoyu-markdown-to-html
```

Publishing to ClawHub releases the published skill under `MIT-0`, per ClawHub's registry rules.

### Register as Plugin Marketplace

Run the following command in Claude Code:

```bash
/plugin marketplace add JimLiu/baoyu-skills
```

### Install Skills

**Option 1: Via Browse UI**

1. Select **Browse and install plugins**
2. Select **baoyu-skills**
3. Select the **baoyu-skills** plugin
4. Select **Install now**

**Option 2: Direct Install**

```bash
# Install the marketplace's single plugin
/plugin install baoyu-skills@baoyu-skills
```

**Option 3: Ask the Agent**

Simply tell Claude Code:

> Please install Skills from github.com/JimLiu/baoyu-skills

### Available Plugin

The marketplace now exposes a single plugin so each skill is registered exactly once.

| Plugin | Description | Includes |
|--------|-------------|----------|
| **baoyu-skills** | Content generation, AI backends, and utility tools for daily work efficiency | All skills in this repository, organized below as Content Skills, AI Generation Skills, and Utility Skills |

## Update Skills

To update skills to the latest version:

1. Run `/plugin` in Claude Code
2. Switch to **Marketplaces** tab (use arrow keys or Tab)
3. Select **baoyu-skills**
4. Choose **Update marketplace**

You can also **Enable auto-update** to get the latest versions automatically.

![Update Skills](./screenshots/update-plugins.png)

## Available Skills

Skills are organized into three categories:

### Content Skills

Content generation and publishing skills.

#### baoyu-xhs-images

Xiaohongshu (RedNote) infographic series generator. Breaks down content into 1-10 cartoon-style infographics with **Style × Layout** two-dimensional system.

```bash
# Auto-select style and layout
/baoyu-xhs-images posts/ai-future/article.md

# Specify style
/baoyu-xhs-images posts/ai-future/article.md --style notion

# Specify layout
/baoyu-xhs-images posts/ai-future/article.md --layout dense

# Combine style and layout
/baoyu-xhs-images posts/ai-future/article.md --style tech --layout list

# Direct content input
/baoyu-xhs-images 今日星座运势
```

**Styles** (visual aesthetics): `cute` (default), `fresh`, `warm`, `bold`, `minimal`, `retro`, `pop`, `notion`, `chalkboard`

**Style Previews**:

| | | |
|:---:|:---:|:---:|
| ![cute](./screenshots/xhs-images-styles/cute.webp) | ![fresh](./screenshots/xhs-images-styles/fresh.webp) | ![warm](./screenshots/xhs-images-styles/warm.webp) |
| cute | fresh | warm |
| ![bold](./screenshots/xhs-images-styles/bold.webp) | ![minimal](./screenshots/xhs-images-styles/minimal.webp) | ![retro](./screenshots/xhs-images-styles/retro.webp) |
| bold | minimal | retro |
| ![pop](./screenshots/xhs-images-styles/pop.webp) | ![notion](./screenshots/xhs-images-styles/notion.webp) | ![chalkboard](./screenshots/xhs-images-styles/chalkboard.webp) |
| pop | notion | chalkboard |

**Layouts** (information density):
| Layout | Density | Best for |
|--------|---------|----------|
| `sparse` | 1-2 pts | Covers, quotes |
| `balanced` | 3-4 pts | Regular content |
| `dense` | 5-8 pts | Knowledge cards, cheat sheets |
| `list` | 4-7 items | Checklists, rankings |
| `comparison` | 2 sides | Before/after, pros/cons |
| `flow` | 3-6 steps | Processes, timelines |

**Layout Previews**:

| | | |
|:---:|:---:|:---:|
| ![sparse](./screenshots/xhs-images-layouts/sparse.webp) | ![balanced](./screenshots/xhs-images-layouts/balanced.webp) | ![dense](./screenshots/xhs-images-layouts/dense.webp) |
| sparse | balanced | dense |
| ![list](./screenshots/xhs-images-layouts/list.webp) | ![comparison](./screenshots/xhs-images-layouts/comparison.webp) | ![flow](./screenshots/xhs-images-layouts/flow.webp) |
| list | comparison | flow |

#### baoyu-infographic

Generate professional infographics with 20 layout types and 17 visual styles. Analyzes content, recommends layout×style combinations, and generates publication-ready infographics.

```bash
# Auto-recommend combinations based on content
/baoyu-infographic path/to/content.md

# Specify layout
/baoyu-infographic path/to/content.md --layout pyramid

# Specify style (default: craft-handmade)
/baoyu-infographic path/to/content.md --style technical-schematic

# Specify both
/baoyu-infographic path/to/content.md --layout funnel --style corporate-memphis

# With aspect ratio (named preset or custom W:H)
/baoyu-infographic path/to/content.md --aspect portrait
/baoyu-infographic path/to/content.md --aspect 3:4
```

**Options**:
| Option | Description |
|--------|-------------|
| `--layout <name>` | Information layout (20 options) |
| `--style <name>` | Visual style (17 options, default: craft-handmade) |
| `--aspect <ratio>` | Named: landscape (16:9), portrait (9:16), square (1:1). Custom: any W:H ratio (e.g., 3:4, 4:3, 2.35:1) |
| `--lang <code>` | Output language (en, zh, ja, etc.) |

**Layouts** (information structure):

| Layout | Best For |
|--------|----------|
| `bridge` | Problem-solution, gap-crossing |
| `circular-flow` | Cycles, recurring processes |
| `comparison-table` | Multi-factor comparisons |
| `do-dont` | Correct vs incorrect practices |
| `equation` | Formula breakdown, input-output |
| `feature-list` | Product features, bullet points |
| `fishbone` | Root cause analysis |
| `funnel` | Conversion processes, filtering |
| `grid-cards` | Multiple topics, overview |
| `iceberg` | Surface vs hidden aspects |
| `journey-path` | Customer journey, milestones |
| `layers-stack` | Technology stack, layers |
| `mind-map` | Brainstorming, idea mapping |
| `nested-circles` | Levels of influence, scope |
| `priority-quadrants` | Eisenhower matrix, 2x2 |
| `pyramid` | Hierarchy, Maslow's needs |
| `scale-balance` | Pros vs cons, weighing |
| `timeline-horizontal` | History, chronological events |
| `tree-hierarchy` | Org charts, taxonomy |
| `venn` | Overlapping concepts |

**Layout Previews**:

| | | |
|:---:|:---:|:---:|
| ![bridge](./screenshots/infographic-layouts/bridge.webp) | ![circular-flow](./screenshots/infographic-layouts/circular-flow.webp) | ![comparison-table](./screenshots/infographic-layouts/comparison-table.webp) |
| bridge | circular-flow | comparison-table |
| ![do-dont](./screenshots/infographic-layouts/do-dont.webp) | ![equation](./screenshots/infographic-layouts/equation.webp) | ![feature-list](./screenshots/infographic-layouts/feature-list.webp) |
| do-dont | equation | feature-list |
| ![fishbone](./screenshots/infographic-layouts/fishbone.webp) | ![funnel](./screenshots/infographic-layouts/funnel.webp) | ![grid-cards](./screenshots/infographic-layouts/grid-cards.webp) |
| fishbone | funnel | grid-cards |
| ![iceberg](./screenshots/infographic-layouts/iceberg.webp) | ![journey-path](./screenshots/infographic-layouts/journey-path.webp) | ![layers-stack](./screenshots/infographic-layouts/layers-stack.webp) |
| iceberg | journey-path | layers-stack |
| ![mind-map](./screenshots/infographic-layouts/mind-map.webp) | ![nested-circles](./screenshots/infographic-layouts/nested-circles.webp) | ![priority-quadrants](./screenshots/infographic-layouts/priority-quadrants.webp) |
| mind-map | nested-circles | priority-quadrants |
| ![pyramid](./screenshots/infographic-layouts/pyramid.webp) | ![scale-balance](./screenshots/infographic-layouts/scale-balance.webp) | ![timeline-horizontal](./screenshots/infographic-layouts/timeline-horizontal.webp) |
| pyramid | scale-balance | timeline-horizontal |
| ![tree-hierarchy](./screenshots/infographic-layouts/tree-hierarchy.webp) | ![venn](./screenshots/infographic-layouts/venn.webp) | |
| tree-hierarchy | venn | |

**Styles** (visual aesthetics):

| Style | Description |
|-------|-------------|
| `craft-handmade` (Default) | Hand-drawn illustration, paper craft aesthetic |
| `claymation` | 3D clay figures, playful stop-motion |
| `kawaii` | Japanese cute, big eyes, pastel colors |
| `storybook-watercolor` | Soft painted illustrations, whimsical |
| `chalkboard` | Colorful chalk on black board |
| `cyberpunk-neon` | Neon glow on dark, futuristic |
| `bold-graphic` | Comic style, halftone dots, high contrast |
| `aged-academia` | Vintage science, sepia sketches |
| `corporate-memphis` | Flat vector people, vibrant fills |
| `technical-schematic` | Blueprint, isometric 3D, engineering |
| `origami` | Folded paper forms, geometric |
| `pixel-art` | Retro 8-bit, nostalgic gaming |
| `ui-wireframe` | Grayscale boxes, interface mockup |
| `subway-map` | Transit diagram, colored lines |
| `ikea-manual` | Minimal line art, assembly style |
| `knolling` | Organized flat-lay, top-down |
| `lego-brick` | Toy brick construction, playful |

**Style Previews**:

| | | |
|:---:|:---:|:---:|
| ![craft-handmade](./screenshots/infographic-styles/craft-handmade.webp) | ![claymation](./screenshots/infographic-styles/claymation.webp) | ![kawaii](./screenshots/infographic-styles/kawaii.webp) |
| craft-handmade | claymation | kawaii |
| ![storybook-watercolor](./screenshots/infographic-styles/storybook-watercolor.webp) | ![chalkboard](./screenshots/infographic-styles/chalkboard.webp) | ![cyberpunk-neon](./screenshots/infographic-styles/cyberpunk-neon.webp) |
| storybook-watercolor | chalkboard | cyberpunk-neon |
| ![bold-graphic](./screenshots/infographic-styles/bold-graphic.webp) | ![aged-academia](./screenshots/infographic-styles/aged-academia.webp) | ![corporate-memphis](./screenshots/infographic-styles/corporate-memphis.webp) |
| bold-graphic | aged-academia | corporate-memphis |
| ![technical-schematic](./screenshots/infographic-styles/technical-schematic.webp) | ![origami](./screenshots/infographic-styles/origami.webp) | ![pixel-art](./screenshots/infographic-styles/pixel-art.webp) |
| technical-schematic | origami | pixel-art |
| ![ui-wireframe](./screenshots/infographic-styles/ui-wireframe.webp) | ![subway-map](./screenshots/infographic-styles/subway-map.webp) | ![ikea-manual](./screenshots/infographic-styles/ikea-manual.webp) |
| ui-wireframe | subway-map | ikea-manual |
| ![knolling](./screenshots/infographic-styles/knolling.webp) | ![lego-brick](./screenshots/infographic-styles/lego-brick.webp) | |
| knolling | lego-brick | |

#### baoyu-cover-image

Generate cover images for articles with 5 dimensions: Type × Palette × Rendering × Text × Mood. Combines 9 color palettes with 6 rendering styles for 54 unique combinations.

```bash
# Auto-select all dimensions based on content
/baoyu-cover-image path/to/article.md

# Quick mode: skip confirmation, use auto-selection
/baoyu-cover-image path/to/article.md --quick

# Specify dimensions (5D system)
/baoyu-cover-image path/to/article.md --type conceptual --palette cool --rendering digital
/baoyu-cover-image path/to/article.md --text title-subtitle --mood bold

# Style presets (backward-compatible shorthand)
/baoyu-cover-image path/to/article.md --style blueprint

# Specify aspect ratio (default: 16:9)
/baoyu-cover-image path/to/article.md --aspect 2.35:1

# Visual only (no title text)
/baoyu-cover-image path/to/article.md --no-title
```

**Five Dimensions**:
- **Type**: `hero`, `conceptual`, `typography`, `metaphor`, `scene`, `minimal`
- **Palette**: `warm`, `elegant`, `cool`, `dark`, `earth`, `vivid`, `pastel`, `mono`, `retro`
- **Rendering**: `flat-vector`, `hand-drawn`, `painterly`, `digital`, `pixel`, `chalk`
- **Text**: `none`, `title-only` (default), `title-subtitle`, `text-rich`
- **Mood**: `subtle`, `balanced` (default), `bold`

#### baoyu-slide-deck

Generate professional slide deck images from content. Creates comprehensive outlines with style instructions, then generates individual slide images.

```bash
# From markdown file
/baoyu-slide-deck path/to/article.md

# With style and audience
/baoyu-slide-deck path/to/article.md --style corporate
/baoyu-slide-deck path/to/article.md --audience executives

# Target slide count
/baoyu-slide-deck path/to/article.md --slides 15

# Outline only (no image generation)
/baoyu-slide-deck path/to/article.md --outline-only

# With language
/baoyu-slide-deck path/to/article.md --lang zh
```

**Options**:

| Option | Description |
|--------|-------------|
| `--style <name>` | Visual style: preset name or `custom` |
| `--audience <type>` | Target: beginners, intermediate, experts, executives, general |
| `--lang <code>` | Output language (en, zh, ja, etc.) |
| `--slides <number>` | Target slide count (8-25 recommended, max 30) |
| `--outline-only` | Generate outline only, skip images |
| `--prompts-only` | Generate outline + prompts, skip images |
| `--images-only` | Generate images from existing prompts |
| `--regenerate <N>` | Regenerate specific slide(s): `3` or `2,5,8` |

**Style System**:

Styles are built from 4 dimensions: **Texture** × **Mood** × **Typography** × **Density**

| Dimension | Options |
|-----------|---------|
| Texture | clean, grid, organic, pixel, paper |
| Mood | professional, warm, cool, vibrant, dark, neutral |
| Typography | geometric, humanist, handwritten, editorial, technical |
| Density | minimal, balanced, dense |

**Presets** (pre-configured dimension combinations):

| Preset | Dimensions | Best For |
|--------|------------|----------|
| `blueprint` (default) | grid + cool + technical + balanced | Architecture, system design |
| `chalkboard` | organic + warm + handwritten + balanced | Education, tutorials |
| `corporate` | clean + professional + geometric + balanced | Investor decks, proposals |
| `minimal` | clean + neutral + geometric + minimal | Executive briefings |
| `sketch-notes` | organic + warm + handwritten + balanced | Educational, tutorials |
| `watercolor` | organic + warm + humanist + minimal | Lifestyle, wellness |
| `dark-atmospheric` | clean + dark + editorial + balanced | Entertainment, gaming |
| `notion` | clean + neutral + geometric + dense | Product demos, SaaS |
| `bold-editorial` | clean + vibrant + editorial + balanced | Product launches, keynotes |
| `editorial-infographic` | clean + cool + editorial + dense | Tech explainers, research |
| `fantasy-animation` | organic + vibrant + handwritten + minimal | Educational storytelling |
| `intuition-machine` | clean + cool + technical + dense | Technical docs, academic |
| `pixel-art` | pixel + vibrant + technical + balanced | Ga
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

English | [中文](./CHANGELOG.zh.md)

## 1.89.1 - 2026-04-01

### Features
- `baoyu-chrome-cdp`: add `gracefulKillChrome` that waits for Chrome to exit and release its port; fix `killChrome` to use `exitCode`/`signalCode` instead of `.killed` for reliable process state detection
- `baoyu-fetch`: auto-detect login state before extraction in interaction wait mode

### Maintenance
- Sync vendor baoyu-chrome-cdp across CDP skills
- `baoyu-url-to-markdown`: sync vendor baoyu-fetch with login auto-detect

## 1.89.0 - 2026-03-31

### Features
- `baoyu-fetch`: add X session cookie sidecar to persist login across runs, graceful Chrome shutdown via Browser.close, and stale profile lock auto-recovery
- `baoyu-article-illustrator`: add warm palette variant for vector-illustration style with new `warm-knowledge` preset
- `baoyu-post-to-x`: add X session persistence after login, Chrome lock recovery, and graceful shutdown

### Documentation
- `baoyu-post-to-weibo`: add post type auto-selection rules and safer CDP kill instructions

### Refactor
- `baoyu-danger-gemini-web`: use graceful Chrome shutdown instead of hard kill
- `baoyu-danger-x-to-markdown`: use graceful Chrome shutdown instead of hard kill

### Fixes
- Sync npm lockfile and root node tests

### Maintenance
- `baoyu-url-to-markdown`: sync vendor baoyu-fetch with session and lifecycle changes
- Update bun.lock files

## 1.88.0 - 2026-03-27

### Features
- `baoyu-fetch`: new URL reader CLI package with Chrome CDP and site-specific adapters (X/Twitter, YouTube, Hacker News, generic)

### Refactor
- `baoyu-url-to-markdown`: replace custom CDP/converter pipeline with `baoyu-fetch` CLI
- `shared-skill-packages`: add `package.json` `files` allowlist support and filter test files, changelogs, and `.changeset` dirs during vendor sync

### Fixes
- `baoyu-md`: rename test image paths from `images/` to `imgs/`

## 1.87.2 - 2026-03-26

### Refactor
- `baoyu-translate`: simplify translation prompts from 15+ verbose principles to 7 concise ones, consolidate analysis and review steps in workflow references

## 1.87.1 - 2026-03-26

### Maintenance
- Add deprecation notice to `baoyu-image-gen` SKILL.md redirecting users to `baoyu-imagine`
- Document deprecated skills policy in CLAUDE.md

## 1.87.0 - 2026-03-26

### Maintenance
- Remove deprecated `baoyu-image-gen` redirect skill and plugin manifest entry — migration to `baoyu-imagine` is complete

## 1.86.0 - 2026-03-25

### Features
- `baoyu-translate`: enrich translation prompt with full analysis context — source voice assessment, structured figurative language mapping, comprehension challenge reasoning, structural/creative challenges, and chunk position context for subagents

## 1.85.0 - 2026-03-25

### Features
- `baoyu-imagine`: auto-migrate legacy `baoyu-image-gen` EXTEND.md config path at runtime
- Add `baoyu-image-gen` deprecation redirect skill to guide users to install `baoyu-imagine` and remove the old skill

## 1.84.0 - 2026-03-25

### Features
- Rename `baoyu-image-gen` skill to `baoyu-imagine` — shorter command name, all references updated across docs, configs, and dependent skills

## 1.83.0 - 2026-03-25

### Features
- `baoyu-image-gen`: add MiniMax provider (`image-01` / `image-01-live`) with subject_reference for character/portrait consistency, custom sizes, and aspect ratio support

## 1.82.0 - 2026-03-24

### Features
- `baoyu-url-to-markdown`: add browser fallback strategy — headless first, automatic retry in visible Chrome on technical failure; new `--browser auto|headless|headed` flag with `--headless`/`--headed` shortcuts
- `baoyu-url-to-markdown`: add content cleaner module for HTML preprocessing before extraction (remove ads, base64 images, scripts, styles)
- `baoyu-url-to-markdown`: support base64 data URI images in media localizer alongside remote URLs
- `baoyu-url-to-markdown`: capture final URL from browser to track redirects for output path generation
- `baoyu-url-to-markdown`: add agent quality gate documentation for post-capture content validation

### Dependencies
- `baoyu-url-to-markdown`: upgrade defuddle ^0.12.0 → ^0.14.0

### Tests
- `baoyu-url-to-markdown`: add unit tests for content-cleaner, html-to-markdown, legacy-converter, media-localizer

## 1.81.0 - 2026-03-24

### Features
- `baoyu-youtube-transcript`: add yt-dlp fallback when YouTube blocks direct InnerTube API, with alternate client identity retry and cookie support via `YOUTUBE_TRANSCRIPT_COOKIES_FROM_BROWSER` env var

### Refactor
- `baoyu-youtube-transcript`: split monolithic script into typed modules (youtube, transcript, storage, shared, types) and add unit tests

## 1.80.1 - 2026-03-24

### Fixes
- `baoyu-image-gen`: use correct `prompt` field name for Jimeng API request

## 1.80.0 - 2026-03-24

### Features
- `baoyu-image-gen`: add Azure OpenAI as independent image generation provider with flexible endpoint parsing, deployment-name resolution, quality mapping, and reference image validation

## 1.79.2 - 2026-03-23

### Fixes
- `baoyu-cover-image`: simplify reference image handling — use `--ref` when model supports it, only create description files for models without reference image support
- `baoyu-post-to-weibo`: add no-theme rule for article markdown-to-HTML conversion

### Tests
- Fix Node-compatible parser tests and add parser test dependencies

## 1.79.1 - 2026-03-23

### Fixes
- Consolidate to single plugin to prevent duplicate skill registration (by @TyrealQ)
- `baoyu-article-illustrator`: remove opacity parameter from watermark prompt
- `baoyu-comic`: fix Doraemon naming spacing and remove opacity from watermark prompt
- `baoyu-xhs-images`: remove opacity from watermark prompt and fix CJK spacing

### Documentation
- Update project documentation to reflect single-plugin architecture

## 1.79.0 - 2026-03-22

### Features
- `baoyu-post-to-wechat`: improve credential loading with multi-source resolution, priority ordering, and diagnostics for skipped incomplete sources

## 1.78.0 - 2026-03-22

### Features
- `baoyu-url-to-markdown`: add URL-specific parser layer for X/Twitter and archive.ph sites
- `baoyu-url-to-markdown`: improved slug generation with stop words removal and subdirectory output structure

### Fixes
- `baoyu-url-to-markdown`: preserve anchor elements containing media in legacy converter
- `baoyu-url-to-markdown`: smarter title deduplication to avoid redundant headings

## 1.77.0 - 2026-03-22

### Features
- `baoyu-youtube-transcript`: add end times to chapter data (by @jzOcb)

### Fixes
- `sync-clawhub`: skip failed skills instead of aborting

## 1.76.1 - 2026-03-21

### Documentation
- `baoyu-youtube-transcript`: fix zsh glob issue — always single-quote YouTube URLs when running the script

## 1.76.0 - 2026-03-21

### Features
- `baoyu-youtube-transcript`: add title heading, description summary, and cover image to markdown output

### Fixes
- `baoyu-markdown-to-html`: use process.execPath and tsx import in test runner

## 1.75.0 - 2026-03-21

### Features
- `baoyu-youtube-transcript`: new skill — download YouTube video transcripts/subtitles and cover images with multi-language, chapters, and speaker identification support

## 1.74.1 - 2026-03-21

### Fixes
- `baoyu-image-gen`: align OpenRouter image generation with current API, harden image support, and narrow Gemini aspect ratios (by @cwandev)
- `baoyu-image-gen`: broaden OpenRouter model detection and aspect ratio validation

## 1.74.0 - 2026-03-20

### Features
- `baoyu-markdown-to-html`: CLI now supports all rendering options — color, font-family, font-size, code-theme, mac-code-block, line-number, count, legend

### Fixes
- `baoyu-markdown-to-html`: fix CSS custom property regex to handle quoted values; grace/simple themes now layer default CSS

## 1.73.3 - 2026-03-20

### Fixes
- `baoyu-post-to-wechat`: fix placeholder replacement to avoid shorter placeholders matching longer numbered variants

## 1.73.2 - 2026-03-20

### Fixes
- `baoyu-post-to-wechat`: fix body image upload to correctly use media/uploadimg API with format and size validation (by @AICreator-Wind)

### Refactor
- `baoyu-post-to-wechat`: extract image processor module for local format conversion (WebP/BMP/GIF → JPEG/PNG) instead of material API fallback

## 1.73.1 - 2026-03-18

### Refactor
- `baoyu-danger-x-to-markdown`: migrate tests from bun:test to node:test

## 1.73.0 - 2026-03-18

### Features
- `baoyu-danger-x-to-markdown`: add video media support for X articles with poster image and video link rendering

## 1.72.0 - 2026-03-18

### Features
- `baoyu-danger-x-to-markdown`: add MARKDOWN entity support for rendering embedded markdown/code blocks in X articles

## 1.71.0 - 2026-03-17

### Features
- `baoyu-image-gen`: add Seedream reference image support for 5.0/4.5/4.0 models with model-specific size validation

## 1.70.0 - 2026-03-17

### Features
- `baoyu-format-markdown`: optimize title generation with formula-based recommendations and straightforward alternatives
- `baoyu-format-markdown`: auto-generate dual summaries (`summary` + `description`) in frontmatter

## 1.69.1 - 2026-03-16

### Fixes
- `baoyu-chrome-cdp`: tighten chrome auto-connect logic to reduce false positives

## 1.69.0 - 2026-03-16

### Features
- `baoyu-chrome-cdp`: support connecting to existing Chrome session (by @bviews)

### Fixes
- `baoyu-chrome-cdp`: support Chrome 146 native remote debugging in approval mode (by @bviews)
- `baoyu-chrome-cdp`: keep HTTP validation in findExistingChromeDebugPort (by @bviews)
- `baoyu-danger-gemini-web`: reuse openPageSession and fix orphaned tab leak (by @bviews)
- `baoyu-danger-gemini-web`: respect explicit profile config over auto-discovery (by @bviews)
- `baoyu-danger-gemini-web`: respect BAOYU_CHROME_PROFILE_DIR in auto-discovery skip (by @bviews)
- `baoyu-post-to-wechat`: improve browser publishing reliability (by @cfh-7598)

### Documentation
- `baoyu-cover-image`: clarify people reference image workflow and interactive confirmation

## 1.68.0 - 2026-03-14

### Features
- `baoyu-article-illustrator`: add configurable output directory (`default_output_dir`) with 4 options — `imgs-subdir`, `same-dir`, `illustrations-subdir`, `independent`
- `baoyu-cover-image`: add character preservation from reference images — use `usage: direct` to pass people references to model for stylized likeness

## 1.67.0 - 2026-03-13

### Features
- `baoyu-image-gen`: add qwen-image-2.0-pro model support for DashScope provider with free-form sizes and text rendering (by @JianJang2017)

## 1.66.1 - 2026-03-13

### Tests
- Migrate test files from centralized `tests/` directory to colocate with source code
- Convert tests from `.mjs` to TypeScript (`.test.ts`) with `tsx` runner
- Add npm workspaces configuration and npm cache to CI workflow

## 1.66.0 - 2026-03-13

### Features
- `baoyu-image-gen`: add Jimeng (即梦) and Seedream (豆包) image generation providers (by @lindaifeng)

### Fixes
- `baoyu-image-gen`: tighten Jimeng provider behavior

### Refactor
- `baoyu-image-gen`: export functions for testability and add module entry guard

### Documentation
- `baoyu-image-gen`: add Jimeng and Seedream provider documentation to SKILL.md and READMEs

### Tests
- Add test infrastructure with CI workflow and image-gen unit tests

## 1.65.1 - 2026-03-13

### Refactor
- `baoyu-translate`: replace remark/unified with markdown-it for chunk parsing, add main.ts CLI entry point

## 1.65.0 - 2026-03-13

### Features
- `baoyu-post-to-wechat`: add placeholder image upload support with deduplication for markdown-embedded images

### Fixes
- `baoyu-post-to-wechat`: fix frontmatter parsing to allow leading whitespace and optional trailing newline

### Refactor
- `baoyu-post-to-wechat`: replace `renderMarkdownToHtml` with `renderMarkdownWithPlaceholders` for structured output

## 1.64.0 - 2026-03-13

### Features
- `baoyu-image-gen`: add OpenRouter provider with support for image generation, reference images, and configurable models

## 1.63.0 - 2026-03-13

### Features
- `baoyu-url-to-markdown`: add hosted `defuddle.md` API fallback when local browser capture fails
- `baoyu-url-to-markdown`: extract YouTube transcript/caption text into markdown output
- `baoyu-url-to-markdown`: materialize shadow DOM content for better web-component page conversion
- `baoyu-url-to-markdown`: include language hint in markdown front matter when available

### Refactor
- `baoyu-url-to-markdown`: split monolithic converter into defuddle, legacy, and shared modules

### Documentation
- Fix Claude Code marketplace repo casing in READMEs

## 1.62.0 - 2026-03-12

### Features
- `baoyu-infographic`: support flexible aspect ratios with custom W:H values (e.g., 3:4, 4:3, 2.35:1) in addition to named presets

### Fixes
- Set strict mode on plugins to prevent duplicated slash commands

### Documentation
- `baoyu-post-to-wechat`: replace credential-like placeholders

## 1.61.0 - 2026-03-11

### Features
- `baoyu-post-to-wechat`: add multi-account support with `--account` CLI arg, EXTEND.md accounts block, isolated Chrome profiles, and credential resolution chain

### Fixes
- Exclude `out/dist/build` dirs and `bun.lockb` from skill release files
- Use proper MIME types in skill publish to fix ClawhHub rejection

## 1.60.0 - 2026-03-11

### Features
- `baoyu-url-to-markdown`: support reusing existing Chrome CDP instances and fix port detection order

### Fixes
- `baoyu-post-to-x`: add missing `fs` import in x-article

### Refactor
- Unify all CDP skills to use shared `baoyu-chrome-cdp` package with vendored copies
- Simplify CLAUDE.md, move detailed documentation to `docs/` directory
- Publish skills directly from synced vendor, removing separate artifact preparation step

## 1.59.1 - 2026-03-11

### Fixes
- `baoyu-translate`: improve short text annotation density rule and add explicit style preset passing to 02-prompt.md
- `baoyu-post-to-x`: remove `--disable-blink-features=AutomationControlled` Chrome flag

### Refactor
- `baoyu-post-to-weibo`: add entry point guard to md-to-html.ts for module import compatibility
- Replace clawhub CLI with local sync-clawhub.mjs script

### Documentation
- Update CLAUDE.md to reflect v1.59.0 codebase state (by @jackL1020)

## 1.59.0 - 2026-03-09

### Features
- `baoyu-image-gen`: add batch parallel image generation and provider-level throttling (by @SeamoonAO)

### Fixes
- `baoyu-image-gen`: restore Google as default provider when multiple keys available

### Documentation
- Improve skill documentation clarity (by @SeamoonAO)

## 1.58.0 - 2026-03-08

### Features
- Add XDG config path support for EXTEND.md (by @liby)

### Fixes
- `baoyu-post-to-wechat`: surface agent-browser startup errors
- `baoyu-post-to-wechat`: harden agent-browser command and eval handling (by @luojiyin1987)
- `baoyu-image-gen`: use execFileSync for google curl requests (by @luojiyin1987)
- `baoyu-format-markdown`: use spawnSync for autocorrect command (by @luojiyin1987)

### Documentation
- Fix CLAUDE dependency statement (by @
... [TRUNCATED]
```

### File: CHANGELOG.zh.md
```md
# Changelog

[English](./CHANGELOG.md) | 中文

## 1.89.1 - 2026-04-01

### 新功能
- `baoyu-chrome-cdp`：新增 `gracefulKillChrome`，等待 Chrome 进程退出并释放端口；修复 `killChrome` 使用 `exitCode`/`signalCode` 替代 `.killed` 以更可靠地检测进程状态
- `baoyu-fetch`：在交互等待模式下自动检测登录状态，未登录时提示用户先登录再提取内容

### 维护
- 同步 vendor baoyu-chrome-cdp 至所有 CDP 技能
- `baoyu-url-to-markdown`：同步 vendor baoyu-fetch 的登录自动检测功能

## 1.89.0 - 2026-03-31

### 新功能
- `baoyu-fetch`：新增 X 会话 Cookie 旁路文件，跨运行持久化登录状态；通过 Browser.close 优雅关闭 Chrome；自动检测并清理过期的 Chrome 配置锁文件
- `baoyu-article-illustrator`：新增暖色调矢量插画配色方案，含 `warm-knowledge` 预设
- `baoyu-post-to-x`：新增登录后 X 会话持久化、Chrome 锁文件恢复和优雅关闭

### 文档
- `baoyu-post-to-weibo`：新增发帖类型自动选择规则，优化 CDP Chrome 终止指令

### 重构
- `baoyu-danger-gemini-web`：使用优雅 Chrome 关闭替代强制终止
- `baoyu-danger-x-to-markdown`：使用优雅 Chrome 关闭替代强制终止

### 修复
- 同步 npm lockfile 及修复根目录 Node 测试

### 维护
- `baoyu-url-to-markdown`：同步 vendor baoyu-fetch 的会话和生命周期改进
- 更新 bun.lock 文件

## 1.88.0 - 2026-03-27

### 新功能
- `baoyu-fetch`：新增 URL 阅读器 CLI 包，支持 Chrome CDP 和站点适配器（X/Twitter、YouTube、Hacker News、通用页面）

### 重构
- `baoyu-url-to-markdown`：用 `baoyu-fetch` CLI 替换自定义 CDP/转换管道
- `shared-skill-packages`：支持 `package.json` 的 `files` 白名单，vendor 同步时过滤测试文件、CHANGELOG 和 `.changeset` 目录

### 修复
- `baoyu-md`：修正测试中图片路径 `images/` 为 `imgs/`

## 1.87.2 - 2026-03-26

### 重构
- `baoyu-translate`：精简翻译提示词，将 15+ 条冗长原则压缩为 7 条，合并分析和审校步骤

## 1.87.1 - 2026-03-26

### 维护
- 在 `baoyu-image-gen` SKILL.md 中添加废弃提示，引导用户使用 `baoyu-imagine`
- 在 CLAUDE.md 中记录废弃技能策略

## 1.87.0 - 2026-03-26

### 维护
- 移除已废弃的 `baoyu-image-gen` 重定向技能及插件清单条目 — 向 `baoyu-imagine` 的迁移已完成

## 1.86.0 - 2026-03-25

### 新功能
- `baoyu-translate`：丰富翻译提示词的分析上下文 — 加入原文语气评估、结构化比喻映射表、理解难点推理、结构性/创造性翻译挑战，以及分块翻译的位置上下文

## 1.85.0 - 2026-03-25

### 新功能
- `baoyu-imagine`：运行时自动迁移旧版 `baoyu-image-gen` 的 EXTEND.md 配置路径
- 新增 `baoyu-image-gen` 废弃重定向技能，引导用户安装 `baoyu-imagine` 并移除旧技能

## 1.84.0 - 2026-03-25

### 新功能
- 将 `baoyu-image-gen` 技能重命名为 `baoyu-imagine` — 更简短的命令名，所有文档、配置和依赖技能中的引用已同步更新

## 1.83.0 - 2026-03-25

### 新功能
- `baoyu-image-gen`：新增 MiniMax 服务商（`image-01` / `image-01-live`），支持 subject_reference 角色/肖像一致性、自定义尺寸和宽高比

## 1.82.0 - 2026-03-24

### 新功能
- `baoyu-url-to-markdown`：新增浏览器回退策略 — 默认无头模式优先，技术故障时自动重试有头 Chrome；新增 `--browser auto|headless|headed` 参数及 `--headless`/`--headed` 快捷方式
- `baoyu-url-to-markdown`：新增内容清理模块，提取前预处理 HTML（移除广告、base64 图片、脚本、样式）
- `baoyu-url-to-markdown`：媒体本地化支持 base64 data URI 图片
- `baoyu-url-to-markdown`：从浏览器捕获最终 URL 以跟踪重定向，用于输出路径生成
- `baoyu-url-to-markdown`：新增 Agent 质量门控文档，规范捕获后的内容验证流程

### 依赖
- `baoyu-url-to-markdown`：升级 defuddle ^0.12.0 → ^0.14.0

### 测试
- `baoyu-url-to-markdown`：新增 content-cleaner、html-to-markdown、legacy-converter、media-localizer 单元测试

## 1.81.0 - 2026-03-24

### 新功能
- `baoyu-youtube-transcript`：YouTube 封锁直连 InnerTube API 时自动回退到 yt-dlp，支持备用客户端身份重试及通过 `YOUTUBE_TRANSCRIPT_COOKIES_FROM_BROWSER` 环境变量传递浏览器 Cookie

### 重构
- `baoyu-youtube-transcript`：将单体脚本拆分为类型化模块（youtube、transcript、storage、shared、types）并添加单元测试

## 1.80.1 - 2026-03-24

### 修复
- `baoyu-image-gen`：修正即梦 API 请求中的 `prompt` 字段名

## 1.80.0 - 2026-03-24

### 新功能
- `baoyu-image-gen`：新增 Azure OpenAI 作为独立图像生成服务商，支持灵活的端点解析、部署名称推断、质量映射及参考图片格式校验

## 1.79.2 - 2026-03-23

### 修复
- `baoyu-cover-image`：简化参考图片处理流程 — 模型支持 `--ref` 时直接传递，仅在模型不支持参考图时创建描述文件
- `baoyu-post-to-weibo`：文章 Markdown 转 HTML 时不传递 --theme 参数

### 测试
- 修复 Node 兼容的解析器测试，添加解析器测试依赖

## 1.79.1 - 2026-03-23

### 修复
- 合并为单一插件，防止 skill 重复注册 (by @TyrealQ)
- `baoyu-article-illustrator`：移除水印提示词中的不透明度参数
- `baoyu-comic`：修正哆啦 A 梦命名间距，移除水印不透明度参数
- `baoyu-xhs-images`：移除水印不透明度参数，修正中英文间距

### 文档
- 更新项目文档以反映单一插件架构

## 1.79.0 - 2026-03-22

### 新功能
- `baoyu-post-to-wechat`：改进凭据加载机制，支持多来源优先级解析，并提供不完整凭据来源的诊断信息

## 1.78.0 - 2026-03-22

### 新功能
- `baoyu-url-to-markdown`：新增 URL 专用解析层，支持 X/Twitter 和 archive.ph 站点的定制化 HTML 提取
- `baoyu-url-to-markdown`：改进 slug 生成算法，去除停用词并采用子目录输出结构

### 修复
- `baoyu-url-to-markdown`：旧版转换器保留包含媒体元素的锚标签
- `baoyu-url-to-markdown`：更智能的标题去重，避免重复添加标题

## 1.77.0 - 2026-03-22

### 新功能
- `baoyu-youtube-transcript`：为章节数据添加结束时间 (by @jzOcb)

### 修复
- `sync-clawhub`：跳过失败的技能而不是中止同步

## 1.76.1 - 2026-03-21

### 文档
- `baoyu-youtube-transcript`：修复 zsh glob 问题 — 运行脚本时始终对 YouTube URL 使用单引号

## 1.76.0 - 2026-03-21

### 新功能
- `baoyu-youtube-transcript`：Markdown 输出中新增标题、描述摘要和封面图片

### 修复
- `baoyu-markdown-to-html`：测试运行器改用 process.execPath 和 tsx import

## 1.75.0 - 2026-03-21

### 新功能
- `baoyu-youtube-transcript`：新技能 — 下载 YouTube 视频字幕/转录文本和封面图片，支持多语言、章节分段和说话人识别

## 1.74.1 - 2026-03-21

### 修复
- `baoyu-image-gen`：对齐 OpenRouter 图像生成与当前 API，增强图像支持，收窄 Gemini 宽高比范围 (by @cwandev)
- `baoyu-image-gen`：扩展 OpenRouter 模型检测和宽高比验证

## 1.74.0 - 2026-03-20

### 新功能
- `baoyu-markdown-to-html`：CLI 支持全部渲染选项 — color、font-family、font-size、code-theme、mac-code-block、line-number、count、legend

### 修复
- `baoyu-markdown-to-html`：修复 CSS 自定义属性正则无法处理带引号值的问题；grace/simple 主题现在会叠加 default 主题 CSS

## 1.73.3 - 2026-03-20

### 修复
- `baoyu-post-to-wechat`：修复占位符替换时短占位符错误匹配更长编号变体的问题

## 1.73.2 - 2026-03-20

### 修复
- `baoyu-post-to-wechat`：修复正文图片上传，正确使用 media/uploadimg 接口并处理格式和大小限制 (by @AICreator-Wind)

### 重构
- `baoyu-post-to-wechat`：提取图片处理模块，本地转换不支持的格式（WebP/BMP/GIF → JPEG/PNG）而非回退到 material 接口

## 1.73.1 - 2026-03-18

### 重构
- `baoyu-danger-x-to-markdown`：测试从 bun:test 迁移至 node:test

## 1.73.0 - 2026-03-18

### 新功能
- `baoyu-danger-x-to-markdown`：支持 X 文章中的视频媒体，渲染封面图和视频链接

## 1.72.0 - 2026-03-18

### 新功能
- `baoyu-danger-x-to-markdown`：支持渲染 X 文章中嵌入的 MARKDOWN 实体（代码块等）

## 1.71.0 - 2026-03-17

### 新功能
- `baoyu-image-gen`：为 Seedream 5.0/4.5/4.0 模型添加参考图支持，并增加模型特定的尺寸校验

## 1.70.0 - 2026-03-17

### 新功能
- `baoyu-format-markdown`：优化标题生成，基于公式智能推荐并提供平实风格备选
- `baoyu-format-markdown`：自动生成双版本摘要（`summary` + `description`），写入 frontmatter

## 1.69.1 - 2026-03-16

### 修复
- `baoyu-chrome-cdp`：收紧 Chrome 自动连接逻辑，减少误连接

## 1.69.0 - 2026-03-16

### 新功能
- `baoyu-chrome-cdp`：支持连接到已有的 Chrome 会话 (by @bviews)

### 修复
- `baoyu-chrome-cdp`：支持 Chrome 146 原生远程调试（审批模式）(by @bviews)
- `baoyu-chrome-cdp`：保留 findExistingChromeDebugPort 中的 HTTP 验证 (by @bviews)
- `baoyu-danger-gemini-web`：复用 openPageSession 并修复孤立标签页泄漏 (by @bviews)
- `baoyu-danger-gemini-web`：显式配置优先于自动发现 (by @bviews)
- `baoyu-danger-gemini-web`：自动发现跳过时也遵循 BAOYU_CHROME_PROFILE_DIR (by @bviews)
- `baoyu-post-to-wechat`：提升浏览器发布可靠性 (by @cfh-7598)

### 文档
- `baoyu-cover-image`：完善人物参考图片工作流和交互式确认说明

## 1.68.0 - 2026-03-14

### 新功能
- `baoyu-article-illustrator`：新增可配置输出目录（`default_output_dir`），支持 4 种选项——`imgs-subdir`、`same-dir`、`illustrations-subdir`、`independent`
- `baoyu-cover-image`：新增参考图片人物保留功能——当参考图包含人物时使用 `usage: direct` 传递给模型，风格化保留人物特征

## 1.67.0 - 2026-03-13

### 新功能
- `baoyu-image-gen`：新增 DashScope qwen-image-2.0-pro 模型支持，支持自由尺寸和文字渲染 (by @JianJang2017)

## 1.66.1 - 2026-03-13

### 测试
- 将测试文件从集中式 `tests/` 目录迁移至与源码同级
- 将测试从 `.mjs` 转换为 TypeScript（`.test.ts`），使用 `tsx` 运行器
- 新增 npm workspaces 配置，CI 工作流添加 npm 缓存

## 1.66.0 - 2026-03-13

### 新功能
- `baoyu-image-gen`：新增即梦（Jimeng）和豆包（Seedream）图像生成服务商 (by @lindaifeng)

### 修复
- `baoyu-image-gen`：收紧即梦服务商行为

### 重构
- `baoyu-image-gen`：导出函数以支持测试，新增模块入口守卫

### 文档
- `baoyu-image-gen`：在 SKILL.md 和 README 中添加即梦和豆包服务商文档

### 测试
- 新增测试基础设施，包含 CI 工作流和 image-gen 单元测试

## 1.65.1 - 2026-03-13

### 重构
- `baoyu-translate`：将 chunk 解析从 remark/unified 替换为 markdown-it，新增 main.ts CLI 入口

## 1.65.0 - 2026-03-13

### 新功能
- `baoyu-post-to-wechat`：新增占位符图片上传支持，自动去重 Markdown 内嵌图片

### 修复
- `baoyu-post-to-wechat`：修复 frontmatter 解析，允许前导空白和可选的尾随换行

### 重构
- `baoyu-post-to-wechat`：将 `renderMarkdownToHtml` 重构为 `renderMarkdownWithPlaceholders`，输出结构化结果

## 1.64.0 - 2026-03-13

### 新功能
- `baoyu-image-gen`：新增 OpenRouter 服务商，支持图像生成、参考图和可配置模型

## 1.63.0 - 2026-03-13

### 新功能
- `baoyu-url-to-markdown`：本地浏览器抓取失败时自动回退到 `defuddle.md` 托管 API
- `baoyu-url-to-markdown`：将 YouTube 字幕/文字记录提取到 Markdown 输出中
- `baoyu-url-to-markdown`：转换前展开 Shadow DOM 内容，提升 Web Component 页面的转换质量
- `baoyu-url-to-markdown`：Markdown front matter 中包含语言标识（如有）

### 重构
- `baoyu-url-to-markdown`：将单体转换器拆分为 defuddle、legacy 和 shared 三个模块

### 文档
- 修复 README 中 Claude Code marketplace 仓库名大小写

## 1.62.0 - 2026-03-12

### 新功能
- `baoyu-infographic`：支持灵活宽高比，可使用自定义 W:H 值（如 3:4、4:3、2.35:1），同时保留预设名称

### 修复
- 设置插件严格模式，防止重复注册斜杠命令

### 文档
- `baoyu-post-to-wechat`：替换类似凭证的占位符

## 1.61.0 - 2026-03-11

### 新功能
- `baoyu-post-to-wechat`：新增多账号支持，通过 `--account` 参数选择账号，EXTEND.md 支持 accounts 配置块，每个账号独立 Chrome 配置目录和凭证解析链

### 修复
- 排除 `out/dist/build` 目录和 `bun.lockb` 文件，避免打包到技能发布文件中
- 修复技能发布时 MIME 类型不正确导致 ClawhHub 拒绝的问题

## 1.60.0 - 2026-03-11

### 新功能
- `baoyu-url-to-markdown`：支持复用已有 Chrome CDP 实例，修复端口检测顺序问题

### 修复
- `baoyu-post-to-x`：补充 x-article 缺失的 `fs` 导入

### 重构
- 统一所有 CDP 技能使用共享 `baoyu-chrome-cdp` 包，各技能内置 vendor 副本
- 精简 CLAUDE.md，将详细文档移至 `docs/` 目录
- 从 synced vendor 直接发布技能，移除单独的 artifact 准备步骤

## 1.59.1 - 2026-03-11

### 修复
- `baoyu-translate`：改进短文本注释密度规则，补充风格预设到 02-prompt.md 的显式传递
- `baoyu-post-to-x`：移除 `--disable-blink-features=AutomationControlled` Chrome 启动参数

### 重构
- `baoyu-post-to-weibo`：为 md-to-html.ts 添加入口守卫，支持模块导入
- 使用本地 sync-clawhub.mjs 脚本替代 clawhub CLI

### 文档
- 更新 CLAUDE.md 以反映 v1.59.0 代码库状态 (by @jackL1020)

## 1.59.0 - 2026-03-09

### 新功能
- `baoyu-image-gen`：新增批量并行图片生成和提供商级别限流 (by @SeamoonAO)

### 修复
- `baoyu-image-gen`：修复多个 API key 可用时恢复 Google 为默认提供商

### 文档
- 改进技能文档清晰度 (by @SeamoonAO)

## 1.58.0 - 2026-03-08

### 新功能
- 新增 EXTEND.md 的 XDG 配置路径支持 (by @liby)

### 修复
- `baoyu-post-to-wechat`：暴露 agent-browser 启动错误信息
- `baoyu-post-to-wechat`：加固 agent-browser 命令和 eval 处理 (by @luojiyin1987)
- `baoyu-image-gen`：使用 execFileSync 替代 shell 执行 Google curl 请求 (by @luojiyin1987)
- `baoyu-format-markdown`：使用 spawnSync 替代 shell 执行 autocorrect 命令 (by @luojiyin1987)

### 文档
- 修正 CLAUDE 依赖说明 (by @luojiyin1987)
- 将 markdown-to-html 添加到 README 工具技能列表 (by @luojiyin1987)

## 1.57.0 - 2026-03-08

### 新功能
- 新增 ClawHub/OpenClaw 发布支持，包含同步脚本和 README 文档

### 重构
- 为所有 skill 前言添加 openclaw 元数据，兼容 ClawHub 注册表
- 全部 skill 中将 `SKILL_DIR` 统一重命名为 `baseDir`
- `baoyu-danger-gemini-web`、`baoyu-danger-x-to-markdown`：使用动态脚本路径显示用法
- `baoyu-comic`、`baoyu-xhs-images`：通过 skill 接口调用图片生成，不再直接调用脚本

## 1.56.1 - 2026-03-08

### 修复
- `baoyu-post-to-weibo`：简化头条文章图片插入逻辑，使用 Backspace 按键替代复杂的 deleteContents 方案，兼容 ProseMirror 编辑器

## 1.56.0 - 2026-03-08

### 新功能
- `baoyu-article-illustrator`：预设优先选择流程，按内容类型分类的风格预设
- `baoyu-xhs-images`：精简工作流从 6 步到 4 步，新增智能确认（快速/自定义/详细三种路径）

### 修复
- `baoyu-post-to-wechat`：通过文件选择器拦截改进图片上传可靠性

## 1.55.0 - 2026-03-08

### 新功能
- `baoyu-article-illustrator`：新增 screen-print 风格和 `--preset` 快捷预设（如 tech-explainer、opinion-piece）
- `baoyu-cover-image`：新增 screen-print 渲染风格和 duotone 调色板，包含 5 个新预设（poster-art、mondo 等）
- `baoyu-xhs-images`：新增 screen-print 风格和 `--preset` 快捷预设，内置 23 个场景预设

### 文档
- 为中英文 README 新增致谢章节，致敬相关开源项目

## 1.54.1 - 2026-03-07

### 修复
- `baoyu-post-to-x`：保持已填充的发帖窗口处于打开状态，方便用户手动检查并发布

### 文档
- `baoyu-post-to-x`：补充默认帖子类型选择规则和手动发布流程说明
- `README`：为中英文 README 新增 Star History 图表

## 1.54.0 - 2026-03-06

### 新功能
- `baoyu-format-markdown`：优化标题和摘要生成，支持多风格候选（颠覆型、方案型、悬念型、数字型），新增禁用模式和钩子优先原则
- `baoyu-markdown-to-html`：新增 `--cite` 选项，将普通外链转换为底部编号引用
- `baoyu-post-to-wechat`：Markdown 输入默认启用底部引用，新增 `--no-cite` 标志可关闭
- `baoyu-translate`：EXTEND.md 支持 `glossary_files` 加载外部术语表文件（Markdown 表格或 YAML 格式）
- `baoyu-translate`：新增 frontmatter 转换规则，翻译时将源文章元数据字段添加 `source` 前缀

## 1.53.0 - 2026-03-06

### 新功能
- `baoyu-url-to-markdown`：将渲染后的 HTML 快照保存为 `-captured.html`，与 Markdown 文件并列输出
- `baoyu-url-to-markdown`：优先使用 Defuddle 转换，失败时自动回退到旧版 Readability/选择器提取器

## 1.52.0 - 2026-03-06

### 新功能
- `baoyu-post-to-weibo`：新增 `--video` 视频上传支持（图片+视频最多 18 个文件）
- `baoyu-post-to-weibo`：上传方式从剪贴板粘贴改为 `DOM.setFileInputFiles`，提升上传可靠性

### 修复
- `baoyu-post-to-weibo`：新增 Chrome 健康检查，无响应时自动重启
- `baoyu-post-to-weibo`：发布前检查页面是否在微博首页，避免在错误页面操作

## 1.51.2 - 2026-03-06

### 修复
- `release-skills`：将显式语言文件名模式（如 `CHANGELOG.de.md`）替换为通用模式，避免 Gen Agent Trust Hub URL 扫描器误报
- `baoyu-infographic`：新增凭证/密钥剥离指令，解决 Snyk W007 不安全凭证处理审计问题

## 1.51.1 - 2026-03-06

### 重构
- 统一 Chrome CDP profile 路径——所有 skill 共享 `baoyu-skills/chrome-profile`，不再各自独立目录
- 修复 `baoyu-post-to-weibo` 错误复用 `x-browser-profile` 路径的问题

### 修复
- 移除所有安装说明中的 `curl | bash` 远程代码执行模式
- `md-to-html` 脚本强制仅允许 HTTPS 下载远程图片
- 添加重定向次数限制（最多 5 次），防止无限重定向
- 在 CLAUDE.md 中新增安全准则章节

## 1.51.0 - 2026-03-06

### 新功能
- `baoyu-post-to-weibo`：新增微博发布技能——支持带图文本发布和头条文章，通过 Chrome CDP 自动化操作
- `baoyu-format-markdown`：新增标题/摘要多候选项选择——生成 3 个候选供用户选择，支持 EXTEND.md 中的 `auto_select` 配置

## 1.50.0 - 2026-03-06

### 新功能
- `baoyu-translate`：翻译风格预设从 4 种扩展到 9 种——新增学术、商务、幽默、口语化和优雅风格
- `baoyu-translate`：新增 `--style` 命令行参数，支持按次指定翻译风格
- `baoyu-translate`：将风格指令集成到子代理提示词模板

## 1.49.0 - 2026-03-06

### 新功能
- `baoyu-format-markdown`：新增读者视角内容分析阶段——在应用格式之前先分析要点、结构和格式问题
- `baoyu-format-markdown`：重构工作流从 8 步精简为 7 步，新增明确的格式化原则和完成报告模板
- `baoyu-translate`：将步骤 2 的工作流机制提取到独立参考文件，精简 SKILL.md
- `baoyu-translate`：扩展触发关键词（改成中文、快翻、本地化等），提升技能激活准确度
- `baoyu-translate`：快速翻译模式下对长内容主动提示切换建议
- `baoyu-translate`：分块时将 frontmatter 保存到 `chunks/frontmatter.md`

## 1.48.2 - 2026-03-06

### 新功能
- `baoyu-translate`：在精翻工作流的审查和修订阶段新增比喻语言与情感忠实度检查
- `baoyu-translate`：增强快速翻译模式，强制执行比喻语言的意义优先翻译原则

## 1.48.1 - 2026-03-05

### 新功能
- `baoyu-translate`：在分析阶段新增比喻语言与隐喻映射——翻译前先解读隐喻、习语和隐含意义，避免字面直译
- `baoyu-translate`：新增"意义优先于字面"、"比喻语言解读"、"情感忠实度"三项翻译原则，同步更新 SKILL.md、精翻工作流和子代理提示词模板

## 1.48.0 - 2026-03-05

### 新功能
- `baoyu-translate`：为 chunk.ts 新增 `--output-dir` 选项——分块文件现在写入翻译输出目录而非源文件目录
- `baoyu-translate`：优化精翻工作流——将审校拆分为批判性审查 + 修订（5→6 步），新增中日韩目标语言的欧化表达诊断

## 1.47.0 - 2026-03-05

### 新功能
- 新增 `baoyu-translate` 翻译技能——支持快速/标准/精翻三种模式，自定义术语表、面向受众翻译、长文档自动分块并行翻译
- 为所有技能的 EXTEND.md 偏好检测添加 PowerShell 跨平台支持

## 1.46.0 - 2026-03-05

### 新功能
- 为 url-to-markdown 新增 `--output-dir` 选项，支持自定义输出目录并自动生成文件名

## 1.45.1 - 2026-03-05

### 重构
- 将所有技能中硬编码的 `npx -y bun` 替换为 `${BUN_X}` 运行时变量——优先使用原生 `bun`，回退到 `npx -y bun`
- 在 CLAUDE.md 中新增运行时检测章节，在所有 SKILL.md 的脚本目录说明中添加运行时解析步骤

## 1.45.0 - 2026-03-05

### 新功能
- `baoyu-post-to-x`：X 文章发布后自动验证——检查残留占位符和图片数量是否正确
- `baoyu-post-to-x`：增加 CDP 超时至 60 秒，图片插入间隔增加 3 秒 DOM 稳定等待，改善长文章发布稳定性

## 1.44.0 - 2026-03-05

### 新功能
- `baoyu-url-to-markdown`：新增 `--download-media` 参数，支持下载图片和视频到本地目录，并将 Markdown 中的链接改写为本地路径
- `baoyu-url-to-markdown`：从页面 meta 信息（og:image）提取封面图，写入 YAML front matter 的 `coverImage` 字段
- `baoyu-url-to-markdown`：支持 `data-src` 懒加载图片提取（兼容微信公众号等站点）
- `baoyu-url-to-markdown`：新增 EXTEND.md 偏好设置，支持首次使用引导配置媒体下载行为

## 1.43.2 - 2026-03-05

### 重构
- `baoyu-url-to-markdown`：使用 defuddle 库替换自定义 HTML 提取逻辑（linkedom + Readability + Turndown），简化内容提取和 Markdown 转换

## 1.43.1 - 2026-03-02

### 新功能
- `baoyu-post-to-x`：自动检测 WSL 环境，将 Chrome profile 路径解析为 Windows 本地路径，解决登录态丢失问题
- `baoyu-post-to-wechat`：自动检测 WSL 环境，将 Chrome profile 路径解析为 Windows 本地路径，解决登录态丢失问题
- `baoyu-danger-gemini-web`：WSL 自动检测 Chrome profile 路径；新增 `GEMINI_WEB_DEBUG_PORT` 环境变量支持固定调试端口
- `baoyu-danger-x-to-markdown`：WSL 自动检测 Chrome profile 路径；新增 `X_DEBUG_PORT` 环境变量支持固定调试端口

## 1.43.0 - 2026-03-02

### 新功能
- `baoyu-post-to-wechat`：支持通过环境变量覆盖浏览器调试端口（`WECHAT_BROWSER_DEBUG_PORT`）和配置目录（`WECHAT_BROWSER_PROFILE_DIR`）
- `baoyu-post-to-x`：支持通过环境变量覆盖浏览器调试端口（`X_BROWSER_DEBUG_PORT`）和配置目录（`X_BROWSER_PROFILE_DIR`）

## 1.42.3 - 2026-03-02

### 修复
- `baoyu-
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

Claude Code marketplace plugin providing AI-powered content generation skills. Version: **1.89.1**.

## Architecture

Skills are exposed through the single `baoyu-skills` plugin in `.claude-plugin/marketplace.json` (which defines plugin metadata, version, and skill paths). The repo docs still group them into three logical areas:

| Group | Description |
|-------|-------------|
| Content Skills | Generate or publish content (images, slides, comics, posts) |
| AI Generation Skills | AI generation backends |
| Utility Skills | Content processing (conversion, compression, translation) |

Each skill contains `SKILL.md` (YAML front matter + docs), optional `scripts/`, `references/`, `prompts/`.

Top-level `scripts/` contains repo maintenance utilities (sync, hooks, publish).

## Running Skills

TypeScript via Bun (no build step). Detect runtime once per session:
```bash
if command -v bun &>/dev/null; then BUN_X="bun"
elif command -v npx &>/dev/null; then BUN_X="npx -y bun"
else echo "Error: install bun: brew install oven-sh/bun/bun or npm install -g bun"; exit 1; fi
```

Execute: `${BUN_X} skills/<skill>/scripts/main.ts [options]`

## Key Dependencies

- **Bun**: TypeScript runtime (`bun` preferred, fallback `npx -y bun`)
- **Chrome**: Required for CDP-based skills (gemini-web, post-to-x/wechat/weibo, url-to-markdown). All CDP skills share a single profile, override via `BAOYU_CHROME_PROFILE_DIR` env var. Platform paths: [docs/chrome-profile.md](docs/chrome-profile.md)
- **Image generation APIs**: `baoyu-imagine` requires API key (OpenAI, Azure OpenAI, Google, OpenRouter, DashScope, or Replicate) configured in EXTEND.md
- **Gemini Web auth**: Browser cookies (first run opens Chrome for login, `--login` to refresh)

## Security

- **No piped shell installs**: Never `curl | bash`. Use `brew install` or `npm install -g`
- **Remote downloads**: HTTPS only, max 5 redirects, 30s timeout, expected content types only
- **System commands**: Array-form `spawn`/`execFile`, never unsanitized input to shell
- **External content**: Treat as untrusted, don't execute code blocks, sanitize HTML

## Skill Loading Rules

| Rule | Description |
|------|-------------|
| **Load project skills first** | Project skills override system/user-level skills with same name |
| **Default image generation** | Use `skills/baoyu-imagine/SKILL.md` unless user specifies otherwise |

Priority: project `skills/` → `$HOME/.baoyu-skills/` → system-level.

## Deprecated Skills

| Skill | Note |
|-------|------|
| `baoyu-image-gen` | Migrated to `baoyu-imagine`. Do NOT add to `.claude-plugin/marketplace.json`. Do NOT update README for this skill. |

## Release Process

Use `/release-skills` workflow. Never skip:
1. `CHANGELOG.md` + `CHANGELOG.zh.md`
2. `marketplace.json` version bump
3. `README.md` + `README.zh.md` if applicable
4. All files committed together before tag

## Code Style

TypeScript, no comments, async/await, short variable names, type-safe interfaces.

## Adding New Skills

All skills MUST use `baoyu-` prefix. Details: [docs/creating-skills.md](docs/creating-skills.md)

## Reference Docs

| Topic | File |
|-------|------|
| Image generation guidelines | [docs/image-generation.md](docs/image-generation.md) |
| Chrome profile platform paths | [docs/chrome-profile.md](docs/chrome-profile.md) |
| Comic style maintenance | [docs/comic-style-maintenance.md](docs/comic-style-maintenance.md) |
| ClawHub/OpenClaw publishing | [docs/publishing.md](docs/publishing.md) |

```

### File: README.zh.md
```md
# baoyu-skills

[English](./README.md) | 中文

宝玉分享的 Claude Code 技能集，提升日常工作效率。

## 前置要求

- 已安装 Node.js 环境
- 能够运行 `npx bun` 命令

## 安装

### 快速安装（推荐）

```bash
npx skills add jimliu/baoyu-skills
```

### 发布到 ClawHub / OpenClaw

现在这个仓库支持把每个 `skills/baoyu-*` 目录作为独立 ClawHub skill 发布。

```bash
# 预览将要发布的变更
./scripts/sync-clawhub.sh --dry-run

# 发布 ./skills 下所有已变更的 skill
./scripts/sync-clawhub.sh --all
```

ClawHub 按“单个 skill”安装，不是把整个 marketplace 一次性装进去。发布后，用户可以按需安装：

```bash
clawhub install baoyu-imagine
clawhub install baoyu-markdown-to-html
```

根据 ClawHub 的 registry 规则，发布到 ClawHub 的 skill 会以 `MIT-0` 许可分发。

### 注册插件市场

在 Claude Code 中运行：

```bash
/plugin marketplace add JimLiu/baoyu-skills
```

### 安装技能

**方式一：通过浏览界面**

1. 选择 **Browse and install plugins**
2. 选择 **baoyu-skills**
3. 选择 **baoyu-skills** 插件
4. 选择 **Install now**

**方式二：直接安装**

```bash
# 安装 marketplace 中唯一的插件
/plugin install baoyu-skills@baoyu-skills
```

**方式三：告诉 Agent**

直接告诉 Claude Code：

> 请帮我安装 github.com/JimLiu/baoyu-skills 中的 Skills

### 可用插件

现在 marketplace 只暴露一个插件，这样每个 skill 只会注册一次。

| 插件 | 说明 | 包含内容 |
|------|------|----------|
| **baoyu-skills** | 提供内容生成、AI 后端和日常效率工具技能 | 仓库中的全部 skills，仍按下方的内容技能、AI 生成技能、工具技能三个分类展示 |

## 更新技能

更新技能到最新版本：

1. 在 Claude Code 中运行 `/plugin`
2. 切换到 **Marketplaces** 标签页（使用方向键或 Tab）
3. 选择 **baoyu-skills**
4. 选择 **Update marketplace**

也可以选择 **Enable auto-update** 启用自动更新，每次启动时自动获取最新版本。

![更新技能](./screenshots/update-plugins.png)

## 可用技能

技能分为三大类：

### 内容技能 (Content Skills)

内容生成和发布技能。

#### baoyu-xhs-images

小红书信息图系列生成器。将内容拆解为 1-10 张卡通风格信息图，支持 **风格 × 布局** 二维系统。

```bash
# 自动选择风格和布局
/baoyu-xhs-images posts/ai-future/article.md

# 指定风格
/baoyu-xhs-images posts/ai-future/article.md --style notion

# 指定布局
/baoyu-xhs-images posts/ai-future/article.md --layout dense

# 组合风格和布局
/baoyu-xhs-images posts/ai-future/article.md --style tech --layout list

# 直接输入内容
/baoyu-xhs-images 今日星座运势
```

**风格**（视觉美学）：`cute`（默认）、`fresh`、`warm`、`bold`、`minimal`、`retro`、`pop`、`notion`、`chalkboard`

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![cute](./screenshots/xhs-images-styles/cute.webp) | ![fresh](./screenshots/xhs-images-styles/fresh.webp) | ![warm](./screenshots/xhs-images-styles/warm.webp) |
| cute | fresh | warm |
| ![bold](./screenshots/xhs-images-styles/bold.webp) | ![minimal](./screenshots/xhs-images-styles/minimal.webp) | ![retro](./screenshots/xhs-images-styles/retro.webp) |
| bold | minimal | retro |
| ![pop](./screenshots/xhs-images-styles/pop.webp) | ![notion](./screenshots/xhs-images-styles/notion.webp) | ![chalkboard](./screenshots/xhs-images-styles/chalkboard.webp) |
| pop | notion | chalkboard |

**布局**（信息密度）：
| 布局 | 密度 | 适用场景 |
|------|------|----------|
| `sparse` | 1-2 点 | 封面、金句 |
| `balanced` | 3-4 点 | 常规内容 |
| `dense` | 5-8 点 | 知识卡片、干货总结 |
| `list` | 4-7 项 | 清单、排行 |
| `comparison` | 双栏 | 对比、优劣 |
| `flow` | 3-6 步 | 流程、时间线 |

**布局预览**：

| | | |
|:---:|:---:|:---:|
| ![sparse](./screenshots/xhs-images-layouts/sparse.webp) | ![balanced](./screenshots/xhs-images-layouts/balanced.webp) | ![dense](./screenshots/xhs-images-layouts/dense.webp) |
| sparse | balanced | dense |
| ![list](./screenshots/xhs-images-layouts/list.webp) | ![comparison](./screenshots/xhs-images-layouts/comparison.webp) | ![flow](./screenshots/xhs-images-layouts/flow.webp) |
| list | comparison | flow |

#### baoyu-infographic

专业信息图生成器，支持 20 种布局和 17 种视觉风格。分析内容后推荐布局×风格组合，生成可发布的信息图。

```bash
# 根据内容自动推荐组合
/baoyu-infographic path/to/content.md

# 指定布局
/baoyu-infographic path/to/content.md --layout pyramid

# 指定风格（默认：craft-handmade）
/baoyu-infographic path/to/content.md --style technical-schematic

# 同时指定布局和风格
/baoyu-infographic path/to/content.md --layout funnel --style corporate-memphis

# 指定比例（预设名称或自定义 W:H）
/baoyu-infographic path/to/content.md --aspect portrait
/baoyu-infographic path/to/content.md --aspect 3:4
```

**选项**：
| 选项 | 说明 |
|------|------|
| `--layout <name>` | 信息布局（20 种选项） |
| `--style <name>` | 视觉风格（17 种选项，默认：craft-handmade） |
| `--aspect <ratio>` | 预设：landscape (16:9)、portrait (9:16)、square (1:1)。自定义：任意 W:H 比例（如 3:4、4:3、2.35:1） |
| `--lang <code>` | 输出语言（en、zh、ja 等） |

**布局**（信息结构）：

| 布局 | 适用场景 |
|------|----------|
| `bridge` | 问题→解决方案、跨越鸿沟 |
| `circular-flow` | 循环、周期性流程 |
| `comparison-table` | 多因素对比 |
| `do-dont` | 正确 vs 错误做法 |
| `equation` | 公式分解、输入→输出 |
| `feature-list` | 产品功能、要点列表 |
| `fishbone` | 根因分析、鱼骨图 |
| `funnel` | 转化漏斗、筛选过程 |
| `grid-cards` | 多主题概览、卡片网格 |
| `iceberg` | 表面 vs 隐藏层面 |
| `journey-path` | 用户旅程、里程碑 |
| `layers-stack` | 技术栈、分层结构 |
| `mind-map` | 头脑风暴、思维导图 |
| `nested-circles` | 影响层级、范围圈 |
| `priority-quadrants` | 四象限矩阵、优先级 |
| `pyramid` | 层级金字塔、马斯洛需求 |
| `scale-balance` | 利弊权衡、天平对比 |
| `timeline-horizontal` | 历史、时间线事件 |
| `tree-hierarchy` | 组织架构、分类树 |
| `venn` | 重叠概念、韦恩图 |

**布局预览**：

| | | |
|:---:|:---:|:---:|
| ![bridge](./screenshots/infographic-layouts/bridge.webp) | ![circular-flow](./screenshots/infographic-layouts/circular-flow.webp) | ![comparison-table](./screenshots/infographic-layouts/comparison-table.webp) |
| bridge | circular-flow | comparison-table |
| ![do-dont](./screenshots/infographic-layouts/do-dont.webp) | ![equation](./screenshots/infographic-layouts/equation.webp) | ![feature-list](./screenshots/infographic-layouts/feature-list.webp) |
| do-dont | equation | feature-list |
| ![fishbone](./screenshots/infographic-layouts/fishbone.webp) | ![funnel](./screenshots/infographic-layouts/funnel.webp) | ![grid-cards](./screenshots/infographic-layouts/grid-cards.webp) |
| fishbone | funnel | grid-cards |
| ![iceberg](./screenshots/infographic-layouts/iceberg.webp) | ![journey-path](./screenshots/infographic-layouts/journey-path.webp) | ![layers-stack](./screenshots/infographic-layouts/layers-stack.webp) |
| iceberg | journey-path | layers-stack |
| ![mind-map](./screenshots/infographic-layouts/mind-map.webp) | ![nested-circles](./screenshots/infographic-layouts/nested-circles.webp) | ![priority-quadrants](./screenshots/infographic-layouts/priority-quadrants.webp) |
| mind-map | nested-circles | priority-quadrants |
| ![pyramid](./screenshots/infographic-layouts/pyramid.webp) | ![scale-balance](./screenshots/infographic-layouts/scale-balance.webp) | ![timeline-horizontal](./screenshots/infographic-layouts/timeline-horizontal.webp) |
| pyramid | scale-balance | timeline-horizontal |
| ![tree-hierarchy](./screenshots/infographic-layouts/tree-hierarchy.webp) | ![venn](./screenshots/infographic-layouts/venn.webp) | |
| tree-hierarchy | venn | |

**风格**（视觉美学）：

| 风格 | 描述 |
|------|------|
| `craft-handmade`（默认） | 手绘插画、纸艺风格 |
| `claymation` | 3D 黏土人物、定格动画感 |
| `kawaii` | 日系可爱、大眼睛、粉彩色 |
| `storybook-watercolor` | 柔和水彩、童话绘本 |
| `chalkboard` | 彩色粉笔、黑板风格 |
| `cyberpunk-neon` | 霓虹灯光、暗色未来感 |
| `bold-graphic` | 漫画风格、网点、高对比 |
| `aged-academia` | 复古科学、泛黄素描 |
| `corporate-memphis` | 扁平矢量人物、鲜艳填充 |
| `technical-schematic` | 蓝图、等距 3D、工程图 |
| `origami` | 折纸形态、几何感 |
| `pixel-art` | 复古 8-bit、怀旧游戏 |
| `ui-wireframe` | 灰度框图、界面原型 |
| `subway-map` | 地铁图、彩色线路 |
| `ikea-manual` | 极简线条、组装说明风 |
| `knolling` | 整齐平铺、俯视图 |
| `lego-brick` | 乐高积木、童趣拼搭 |

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![craft-handmade](./screenshots/infographic-styles/craft-handmade.webp) | ![claymation](./screenshots/infographic-styles/claymation.webp) | ![kawaii](./screenshots/infographic-styles/kawaii.webp) |
| craft-handmade | claymation | kawaii |
| ![storybook-watercolor](./screenshots/infographic-styles/storybook-watercolor.webp) | ![chalkboard](./screenshots/infographic-styles/chalkboard.webp) | ![cyberpunk-neon](./screenshots/infographic-styles/cyberpunk-neon.webp) |
| storybook-watercolor | chalkboard | cyberpunk-neon |
| ![bold-graphic](./screenshots/infographic-styles/bold-graphic.webp) | ![aged-academia](./screenshots/infographic-styles/aged-academia.webp) | ![corporate-memphis](./screenshots/infographic-styles/corporate-memphis.webp) |
| bold-graphic | aged-academia | corporate-memphis |
| ![technical-schematic](./screenshots/infographic-styles/technical-schematic.webp) | ![origami](./screenshots/infographic-styles/origami.webp) | ![pixel-art](./screenshots/infographic-styles/pixel-art.webp) |
| technical-schematic | origami | pixel-art |
| ![ui-wireframe](./screenshots/infographic-styles/ui-wireframe.webp) | ![subway-map](./screenshots/infographic-styles/subway-map.webp) | ![ikea-manual](./screenshots/infographic-styles/ikea-manual.webp) |
| ui-wireframe | subway-map | ikea-manual |
| ![knolling](./screenshots/infographic-styles/knolling.webp) | ![lego-brick](./screenshots/infographic-styles/lego-brick.webp) | |
| knolling | lego-brick | |

#### baoyu-cover-image

为文章生成封面图，支持五维定制系统：类型 × 配色 × 渲染 × 文字 × 氛围。9 种配色方案与 6 种渲染风格组合，提供 54 种独特效果。

```bash
# 根据内容自动选择所有维度
/baoyu-cover-image path/to/article.md

# 快速模式：跳过确认，使用自动选择
/baoyu-cover-image path/to/article.md --quick

# 指定维度（5D 系统）
/baoyu-cover-image path/to/article.md --type conceptual --palette cool --rendering digital
/baoyu-cover-image path/to/article.md --text title-subtitle --mood bold

# 风格预设（向后兼容的简写方式）
/baoyu-cover-image path/to/article.md --style blueprint

# 指定宽高比（默认：16:9）
/baoyu-cover-image path/to/article.md --aspect 2.35:1

# 纯视觉（不含标题文字）
/baoyu-cover-image path/to/article.md --no-title
```

**五个维度**：
- **类型 (Type)**：`hero`、`conceptual`、`typography`、`metaphor`、`scene`、`minimal`
- **配色 (Palette)**：`warm`、`elegant`、`cool`、`dark`、`earth`、`vivid`、`pastel`、`mono`、`retro`
- **渲染 (Rendering)**：`flat-vector`、`hand-drawn`、`painterly`、`digital`、`pixel`、`chalk`
- **文字 (Text)**：`none`、`title-only`（默认）、`title-subtitle`、`text-rich`
- **氛围 (Mood)**：`subtle`、`balanced`（默认）、`bold`

#### baoyu-slide-deck

从内容生成专业的幻灯片图片。先创建包含样式说明的完整大纲，然后逐页生成幻灯片图片。

```bash
# 从 markdown 文件生成
/baoyu-slide-deck path/to/article.md

# 指定风格和受众
/baoyu-slide-deck path/to/article.md --style corporate
/baoyu-slide-deck path/to/article.md --audience executives

# 指定页数
/baoyu-slide-deck path/to/article.md --slides 15

# 仅生成大纲（不生成图片）
/baoyu-slide-deck path/to/article.md --outline-only

# 指定语言
/baoyu-slide-deck path/to/article.md --lang zh
```

**选项**：

| 选项 | 说明 |
|------|------|
| `--style <name>` | 视觉风格：预设名称或 `custom` |
| `--audience <type>` | 目标受众：beginners、intermediate、experts、executives、general |
| `--lang <code>` | 输出语言（en、zh、ja 等） |
| `--slides <number>` | 目标页数（推荐 8-25，最多 30） |
| `--outline-only` | 仅生成大纲，跳过图片 |
| `--prompts-only` | 生成大纲 + 提示词，跳过图片 |
| `--images-only` | 从现有提示词生成图片 |
| `--regenerate <N>` | 重新生成指定页：`3` 或 `2,5,8` |

**风格系统**：

风格由 4 个维度组合而成：**纹理** × **氛围** × **字体** × **密度**

| 维度 | 选项 |
|------|------|
| 纹理 | clean 纯净、grid 网格、organic 有机、pixel 像素、paper 纸张 |
| 氛围 | professional 专业、warm 温暖、cool 冷静、vibrant 鲜艳、dark 暗色、neutral 中性 |
| 字体 | geometric 几何、humanist 人文、handwritten 手写、editorial 编辑、technical 技术 |
| 密度 | minimal 极简、balanced 均衡、dense 密集 |

**预设**（预配置的维度组合）：

| 预设 | 维度组合 | 适用场景 |
|------|----------|----------|
| `blueprint`（默认） | grid + cool + technical + balanced | 架构设计、系统设计 |
| `chalkboard` | organic + warm + handwritten + balanced | 教育、教程 |
| `corporate` | clean + professional + geometric + balanced | 投资者演示、提案 |
| `minimal` | clean + neutral + geometric + minimal | 高管简报 |
| `sketch-notes` | organic + warm + handwritten + balanced | 教育、教程 |
| `watercolor` | organic + warm + humanist + minimal | 生活方式、健康 |
| `dark-atmospheric` | clean + dark + editorial + balanced | 娱乐、游戏 |
| `notion` | clean + neutral + geometric + dense | 产品演示、SaaS |
| `bold-editorial` | clean + vibrant + editorial + balanced | 产品发布、主题演讲 |
| `editorial-infographic` | clean + cool + editorial + dense | 科技解说、研究 |
| `fantasy-animation` | organic + vibrant + handwritten + minimal | 教育故事 |
| `intuition-machine` | clean + cool + technical + dense | 技术文档、学术 |
| `pixel-art` | pixel + vibrant + technical + balanced | 游戏、开发者 |
| `scientific` | clean + cool + technical + dense | 生物、化学、医学 |
| `vector-illustration` | clean + vibrant + humanist + balanced | 创意、儿童内容 |
| `vintage` | paper + warm + editorial + balanced | 历史、传记 |

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![blueprint](./screenshots/slide-deck-styles/blueprint.webp) | ![chalkboard](./screenshots/slide-deck-styles/chalkboard.webp) | ![bold-editorial](./screenshots/slide-deck-styles/bold-editorial.webp) |
| blueprint | chalkboard | bold-editorial |
| ![corporate](./screenshots/slide-deck-styles/corporate.webp) | ![dark-atmospheric](./screenshots/slide-deck-styles/dark-atmospheric.webp) | ![editorial-infographic](./screenshots/slide-deck-styles/editorial-infographic.webp) |
| corporate | dark-atmospheric | editorial-infographic |
| ![fantasy-animation](./screenshots/slide-deck-styles/fantasy-animation.webp) | ![intuition-machine](./screenshots/slide-deck-styles/intuition-machine.webp) | ![minimal](./screenshots/slide-deck-styles/minimal.webp) |
| fantasy-animation | intuition-machine | minimal |
| ![notion](./screenshots/slide-deck-styles/notion.webp) | ![pixel-art](./screenshots/slide-deck-styles/pixel-art.webp) | ![scientific](./screenshots/slide-deck-styles/scientific.webp) |
| notion | pixel-art | scientific |
| ![sketch-notes](./screenshots/slide-deck-styles/sketch-notes.webp) | ![vector-illustration](./screenshots/slide-deck-styles/vector-illustration.webp) | ![vintage](./screenshots/slide-deck-styles/vintage.webp) |
| sketch-notes | vector-illustration | vintage |
| ![watercolor](./screenshots/slide-deck-styles/watercolor.webp) | | |
| watercolor | | |

生成完成后，所有幻灯片会自动合并为 `.pptx` 和 `.pdf` 文件，方便分享。

#### baoyu-comic

知识漫画创作器，支持画风 × 基调灵活组合。创作带有详细分镜布局的原创教育漫画，逐页生成图片。

```bash
# 从素材文件生成（自动选择画风 + 基调）
/baoyu-comic posts/turing-story/source.md

# 指定画风和基调
/baoyu-comic posts/turing-story/source.md --art manga --tone warm
/baoyu-comic posts/turing-story/source.md --art ink-brush --tone dramatic

# 使用预设（包含特殊规则）
/baoyu-comic posts/turing-story/source.md --style ohmsha
/baoyu-comic posts/turing-story/source.md --style wuxia

# 指定布局和比例
/baoyu-comic posts/turing-story/source.md --layout cinematic
/baoyu-comic posts/turing-story/source.md --aspect 16:9

# 指定语言
/baoyu-comic posts/turing-story/source.md --lang zh

# 直接输入内容
/baoyu-comic "图灵的故事与计算机科学的诞生"
```

**选项**：
| 选项 | 取值 |
|------|------|
| `--art` | `ligne-claire`（默认）、`manga`、`realistic`、`ink-brush`、`chalk` |
| `--tone` | `neutral`（默认）、`warm`、`dramatic`、`romantic`、`energetic`、`vintage`、`action` |
| `--style` | `ohmsha`、`wuxia`、`shoujo`（预设，含特殊规则） |
| `--layout` | `standard`（默认）、`cinematic`、`dense`、`splash`、`mixed`、`webtoon` |
| `--aspect` | `3:4`（默认，竖版）、`4:3`（横版）、`16:9`（宽屏） |
| `--lang` | `auto`（默认）、`zh`、`en`、`ja` 等 |

**画风**（渲染技法）：

| 画风 | 描述 |
|------|------|
| `ligne-claire` | 统一线条、平涂色彩，欧洲漫画传统（丁丁、Logicomix） |
| `manga` | 大眼睛、日漫风格、表情丰富 |
| `realistic` | 数字绘画、写实比例、精致细腻 |
| `ink-brush` | 中国水墨笔触、水墨晕染效果 |
| `chalk` | 黑板粉笔风格、手绘温暖感 |

**基调**（氛围/情绪）：

| 基调 | 描述 |
|------|------|
| `neutral` | 平衡、理性、教育性 |
| `warm` | 怀旧、个人化、温馨 |
| `dramatic` | 高对比、紧张、有力 |
| `romantic` | 柔和、唯美、装饰性元素 |
| `energetic` | 明亮、动感、活力 |
| `vintage` | 历史感、做旧、时代真实性 |
| `action` | 速度线、冲击效果、战斗 |

**预设**（画风 + 基调 + 特殊规则）：

| 预设 | 等价于 | 特殊规则 |
|------|--------|----------|
| `ohmsha` | manga + neutral | 视觉比喻、禁止大头对话、道
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
