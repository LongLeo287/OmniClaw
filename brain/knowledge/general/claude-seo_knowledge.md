---
id: claude-seo-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.220233
---

# KNOWLEDGE EXTRACT: claude-seo
> **Extracted on:** 2026-03-29 23:46:06
> **Source:** claude-seo

---

## File: `.gitattributes`
```
# Linguist overrides for accurate GitHub language bar
*.md linguist-documentation
*.json linguist-data
brain/knowledge/docs_legacy/** linguist-documentation
schema/** linguist-data
*.sh linguist-detectable=false
*.ps1 linguist-detectable=false
```

## File: `.gitignore`
```
# Generated output
output/
.planning/
*.tmp
*.bak
*.swp

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.sublime-*

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.mypy_cache/
*.egg-info/
dist/
build/
.eggs/

# Virtual environments
venv/
.venv/
env/
.env/

# Secrets and credentials (NEVER commit these)
.env
.env.*
*.env
**/.env
**/client_secret*.json
**/service_account*.json
**/oauth-token.json
**/.google-token.json

# Node (if any)
node_modules/

# Logs
*.log

# Archives (don't commit zips)
*.zip
*.tar.gz

# Screenshots (generated during analysis)
screenshots/

# Temporary analysis files
*-AUDIT-REPORT.md
*-ACTION-PLAN.md
FULL-AUDIT-REPORT.md
ACTION-PLAN.md
GEO-ANALYSIS.md
SCHEMA-REPORT.md
SITEMAP-REPORT*.md
VALIDATION-REPORT.md

# Generated artifacts from audits
charts/
*.pdf
report.html
generated-schema.json
rankenstein-schema-audit.md
capture_closeups.py
capture_desktop.py
generate_charts.py
generate_pdf.py

# Debug logs
firebase-debug.log
firebase-debug.*.log

# Generated / site-specific scripts (not part of the generic tool)
scripts/mobile_analysis.py

# Audit reports with alternate naming conventions
sitemap-validation-report.md
*-validation-report.md

# Temporary download directories
claude-ads-main/
claude-seo-main/

# Root-level duplicate media files (originals live in screenshots/)
Cover Image.jpeg
seo audit demo.gif
seo command demo.gif
.github-audit/

# Generated Google SEO reports
Google-SEO-Report-*.html
Google-SEO-Report-*.pdf

# Site-specific analysis outputs
LOCAL-SEO-ANALYSIS-*.md
LOCAL-SEO-ANALYSIS-*.html
GEO-ANALYSIS-*.md
MAPS-ANALYSIS-*.md
RELEASE-*.md
dirigo-seo-images-review.html

# Site-specific scripts
indexnow-submit.sh

# Generated site builds
site/
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.0] - 2026-03-28

### Added
- **Google SEO APIs skill**: `skills/seo-google/SKILL.md` with 21 commands across 4 credential tiers
- **Google subagent**: `agents/seo-google.md` for enriched audit data (CWV field data, indexation status, organic traffic)
- **11 Python scripts**: google_auth.py, gsc_query.py, gsc_inspect.py, pagespeed_check.py, crux_history.py, indexing_notify.py, ga4_report.py, google_report.py, youtube_search.py, nlp_analyze.py, keyword_planner.py
- **10 reference files**: auth-setup.md, search-console-api.md, pagespeed-crux-api.md, indexing-api.md, ga4-data-api.md, youtube-api.md, nlp-api.md, keyword-planner-api.md, supplementary-apis.md, rate-limits-quotas.md
- **PDF report generator**: `scripts/google_report.py` with enterprise A4 template, WeasyPrint + matplotlib charts, post-generation quality review
- **OAuth web credential flow**: Browser-based auth with localhost:8085 callback, token refresh, manual code exchange fallback
- **4-tier credential system**: Tier 0 (API key: PSI/CrUX), Tier 1 (+OAuth/SA: GSC/Indexing), Tier 2 (+GA4), Tier 3 (+Ads Keyword Planner)
- **Python dependencies**: google-api-python-client, google-auth, google-auth-oauthlib, google-auth-httplib2, google-analytics-data, matplotlib, weasyprint

### Security
- SSRF protection: `validate_url()` blocks private IPs, loopback, and GCP metadata endpoints in all Google API scripts
- `.gitignore` hardened with 8 credential patterns: `.env`, `client_secret*.json`, `oauth-token.json`, `service_account*.json`
- OAuth tokens no longer store `client_secret` (reads from client_secret.json file only)
- Removed hardcoded user paths from all scripts (mobile_analysis.py, capture scripts)

### Changed
- Sub-skill count: 14 -> 15 core (+ 2 extensions)
- Subagent count: 9 -> 10 core (+ 2 extension) with conditional Google API spawning
- seo-audit spawns seo-google agent when Google API credentials detected
- seo-technical and seo-performance can use CrUX field data when available
- Report Generation Rules added to CLAUDE.md with color palette, dependency, and cross-skill enforcement
- README updated with Google APIs, local SEO, maps, and PDF report features

---

## [1.6.1] - 2026-03-27

### Added
- **Marketplace distribution**: Created `.claude-plugin/marketplace.json` for plugin marketplace submission. Users can now install via `/plugin marketplace add AgriciDaniel/claude-seo`
- **Agent model and turn limits**: All 11 subagents now specify `model: sonnet` and `maxTurns` (15-25) for predictable cost and behavior
- **Plugin keywords**: Added 12 discovery keywords to `plugin.json` for marketplace searchability

### Changed
- **Standard directory structure**: Moved `seo/` orchestrator to `skills/seo/` for auto-discovery compliance. Extension skills (seo-dataforseo, seo-image-gen) and agents copied to standard `skills/` and `agents/` directories
- **plugin.json rewrite**: Removed non-standard `entry_point` field and individual file-path arrays for `skills`/`agents`. All 17 skills and 11 agents now rely on directory auto-discovery per Anthropic plugin spec
- **allowed-tools format**: Converted from YAML arrays to comma-separated strings across all 17 SKILL.md files
- **Metadata standardized**: Added `license: MIT` and `metadata:` block (author, version, category) to all SKILL.md frontmatters
- **Cross-references**: Updated all agent and skill files referencing `seo/references/` to `skills/seo/references/`
- **CLAUDE.md**: Architecture tree updated to reflect new structure

### Fixed
- **Plugin validation**: `claude plugin validate .` now passes cleanly (previously would fail on non-standard fields)

---

## [1.6.0] - 2026-03-23

### Added
- **Local SEO skill**: `skills/seo-local/SKILL.md` for GBP, NAP, citations, reviews, and map pack analysis
- **Maps intelligence skill**: `skills/seo-maps/SKILL.md` for geo-grid rank tracking, GBP auditing, review intelligence, competitor radius mapping
- **Maps subagent**: `agents/seo-maps.md` for parallel maps analysis during audits
- **Local subagent**: `agents/seo-local.md` for parallel local SEO analysis
- **Maps reference files**: 4 new reference files (maps-geo-grid.md, maps-gbp-checklist.md, maps-api-endpoints.md, maps-free-apis.md)
- **Local reference files**: 2 new reference files (local-seo-signals.md, local-schema-types.md)
- **Installer fixes**: Cross-platform install script improvements

### Changed
- Subagent count: 7 -> 9 core (+ 2 extension) with conditional local/maps spawning
- Sub-skill count: 12 -> 14 core (+ 2 extension)

---

## [1.5.0] - 2026-03-19

### Added
- **Frontmatter fields**: `user-invokable`, `argument-hint`, and `allowed-tools` added to all SKILL.md files per Anthropic best practices
- **Error handling sections**: Added to all SKILL.md files with skill-specific guidance
- **Plugin manifest**: `.claude-plugin/plugin.json` updated with all skills and agents registered
- **Version tracking**: `pyproject.toml` with project metadata

### Fixed
- **Em dash elimination**: Replaced em dashes (U+2014) across files with appropriate punctuation (colons, commas, semicolons, periods) to reduce AI detection signals
- **HTML comments before frontmatter**: Removed `<!-- Updated: ... -->` comments from SKILL.md files that preceded the YAML frontmatter delimiter
- **Anthropic compliance audit**: Full audit against official skill-building guidelines, all checks now pass

### Changed
- **Technical SEO**: Updated from "8 categories" to "9 categories" in description (IndexNow added in prior update)

---

## [1.4.0] - 2026-03-12

### Security
- **Install script supply chain fix**: Replaced `irm | iex` Windows PowerShell one-liner with `git clone + powershell -File` as primary install method. Claude Code's own security guardrails flagged the old pattern as a supply chain risk (reported by community member). Added collapsible "review before running" section for Unix curl method.
- **Version pinning**: `install.sh` and `install.ps1` now clone a specific release tag (`v1.3.0`) by default rather than `main`, preventing silent updates. Override with `CLAUDE_SEO_TAG=main`.
- **PowerShell Invoke-External hardening**: Comprehensive `PSNativeCommandUseErrorActionPreference` handling in `Invoke-External` wrapper (fixes Windows git clone stderr false-positive termination, from PR #13 + PR #15).

### Added
- **GEO agent deployed**: `agents/seo-geo.md` created -- `/seo audit` now spawns 7 parallel agents (was 6). GEO analysis covers AI crawler access, llms.txt, passage-level citability, brand mention signals, platform-specific scoring (Google AI Overviews, ChatGPT, Perplexity, Bing Copilot).
- **`--googlebot` flag in `fetch_page.py`**: Detect prerender/dynamic rendering services by comparing response size with default UA vs Googlebot UA. First phase of SPA/CSR support (Issue #11).

### Fixed
- **URL normalization**: `capture_screenshot.py` and `analyze_visual.py` now accept bare domains (`example.com` -> `https://example.com`) via shared `normalize_url()` helper (from PR #16 by @shuofengzhang).
- **GEO weight**: AI Search Readiness weight increased from 5% to 10% in overall SEO Health Score. Technical SEO adjusted to 22%, Content Quality to 23%.
- **FAQPage guidance**: Blanket "remove FAQPage on commercial sites" updated to nuanced guidance -- existing FAQPage -> Info priority (not Critical), noting AI/LLM citation benefit. Adding new FAQPage -> not recommended for Google, note AI benefit. Updated in `seo/SKILL.md`, `agents/seo-schema.md`, `seo/references/schema-types.md`.
- **Uninstall agents list**: Added `seo-geo` to `uninstall.sh` and `uninstall.ps1` removal lists.
- **Python requirement**: Corrected from `3.8+` to `3.10+` in `README.md` and `brain/knowledge/docs_legacy/INSTALLATION.md`.

### Changed
- Subagent count: 6 -> 7 (added seo-geo to core audit pipeline)
- `.gitignore`: Added generated audit artifacts (charts/, PDFs, report.html, firebase-debug.log, generated-schema.json)

---

## [1.3.0] - 2026-03-06

### Added
- **Extension system**: `extensions/` directory convention for self-contained add-ons with install/uninstall scripts
- **DataForSEO extension**: 22 commands across 9 API modules (SERP, keywords, backlinks, on-page, content, business listings, AI visibility, LLM mentions). Install: `./extensions/dataforseo/install.sh`
- **DataForSEO integration**: seo-audit, seo-content, seo-geo, seo-page, seo-plan, seo-technical auto-detect DataForSEO MCP tools for enriched analysis
- **Plugin manifest**: `.claude-plugin/plugin.json` for official plugin directory submission
- **Documentation**: Extensions architecture in ARCHITECTURE.md, 22 new commands in COMMANDS.md, updated MCP integration guide

### Fixed
- **Title tag threshold**: Pre-commit hook now uses 60-char max, aligned with quality-gates.md and echo message
- **SSRF prevention**: Added to `capture_screenshot.py` (defense-in-depth, matching `fetch_page.py`)
- **Frontmatter cleanup**: Removed non-standard `allowed-tools` from main SKILL.md

### Changed
- Sub-skill count: 12 + 1 extension (added seo-dataforseo via DataForSEO extension)
- Subagent count: 6 + 1 optional (added seo-dataforseo agent via extension)
- DataForSEO promoted from "Community" to "Official extension" in MCP docs

---

## [1.2.1] - 2026-02-28

### Fixed
- **User-Agent header**: Changed default from bot-style `ClaudeSEO/1.0` to Chrome-like string with `ClaudeSEO/1.2` suffix. SSR frameworks (Next.js, Nuxt, Angular) now pre-render properly instead of serving empty client-side shells (#9)
- **Custom User-Agent support**: Added `--user-agent` flag to `fetch_page.py` for configurable UA strings

### Added
- **install.cat support**: Added alternative install method via `curl install.cat/AgriciDaniel/claude-seo | bash` to README (#10)

---

## [1.2.0] - 2026-02-19

### Security
- **SSRF prevention**: Added private IP blocking to `fetch_page.py` and `analyze_visual.py`
- **Path traversal prevention**: Added output path sanitization to `capture_screenshot.py` and file validation to `parse_html.py`
- **Install hardening**: Removed `--break-system-packages`, switched to venv-based pip install
- **requirements.txt**: Now persisted to `~/.claude/skills/seo/` for user retry

### Fixed
- **YAML frontmatter parsing**: Removed HTML comments before `---` delimiter in 8 files (skills: seo-content, seo-images, seo-programmatic, seo-schema, seo-technical; agents: seo-content, seo-performance, seo-technical). Thanks @kylewhirl for identifying this in the codex-seo fork.
- **Windows installer**: Merged @kfrancis improvements -- `python -m pip`, `py -3` launcher fallback, requirements.txt persistence, non-fatal subagent copy, better error diagnostics (PR #6)
- **requirements.txt missing after install**: Now copied to skill directory so users can retry (#1)

### Changed
- Python dependencies now installed in a venv at `~/.claude/skills/seo/.venv/` with `--user` fallback (#2)
- Playwright marked as explicitly optional in install output
- Windows installer uses `Resolve-Python` helper for robust Python detection (#5)

---

## [1.1.0] - 2026-02-07

### Security (CRITICAL)
- **urllib3 >=2.6.3**: Fixes CVE-2026-21441 (CVSS 8.9) - decompression bypass vulnerability
- **lxml >=6.0.2**: Updated from 5.3.2 for additional libxml2 security patches
- **Pillow >=12.1.0**: Fixes CVE-2025-48379
- **playwright >=1.55.1**: Fixes CVE-2025-59288 (macOS)
- **requests >=2.32.4**: Fixes CVE-2024-47081, CVE-2024-35195

### Added
- **GEO (Generative Engine Optimization) major enhancement**:
  - Brand mention analysis (3x more important than backlinks for AI visibility)
  - AI crawler detection (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, etc.)
  - llms.txt standard detection and recommendations
  - RSL 1.0 (Really Simple Licensing) detection
  - Passage-level citability scoring (optimal 134-167 words)
  - Platform-specific optimization (Google AI Overviews vs ChatGPT vs Perplexity)
  - Server-side rendering checks for AI crawler accessibility
- **LCP Subparts analysis**: TTFB, resource load delay, resource load time, render delay
- **Soft Navigations API detection** for SPA CWV measurement limitations
- **Schema.org v29.4 additions**: ConferenceEvent, PerformingArtsEvent, LoyaltyProgram
- **E-commerce schema updates**: returnPolicyCountry now required, organization-level policies

### Changed
- **E-E-A-T framework**: Updated for December 2025 core update - now applies to ALL competitive queries, not just YMYL
- **SKILL.md description**: Expanded to leverage new 1024-character limit
- **Schema deprecations expanded**: Added ClaimReview, VehicleListing (June 2025)
- **WebApplication schema**: Added as correct type for browser-based SaaS (vs SoftwareApplication)

### Fixed
- Schema-types.md now correctly distinguishes SoftwareApplication (apps) vs WebApplication (SaaS)

---

## [1.0.0] - 2026-02-07

### Added
- Initial release of Claude SEO
- 9 specialized skills: audit, page, sitemap, schema, images, technical, content, geo, plan
- 6 subagents for parallel analysis: seo-technical, seo-content, seo-schema, seo-sitemap, seo-performance, seo-visual
- Industry templates: SaaS, local service, e-commerce, publisher, agency, generic
- Schema library with deprecation tracking:
  - HowTo schema marked deprecated (September 2023)
  - FAQ schema restricted to government/healthcare sites only (August 2023)
  - SpecialAnnouncement schema marked deprecated (July 31, 2025)
- AI Overviews / GEO optimization skill (seo-geo) - new for 2026
- Core Web Vitals analysis using current metrics:
  - LCP (Largest Contentful Paint): <2.5s
  - INP (Interaction to Next Paint): <200ms - replaced FID on March 12, 2024
  - CLS (Cumulative Layout Shift): <0.1
- E-E-A-T framework updated to September 2025 Quality Rater Guidelines
- Quality gates for thin content and doorway page prevention:
  - Warning at 30+ location pages
  - Hard stop at 50+ location pages
- Pre-commit and post-edit automation hooks
- One-command install and uninstall scripts (Unix and Windows)
- Bounded Python dependency pinning with CVE-aware minimums (lxml >= 5.3.2)

### Architecture
- Follows Anthropic's official Claude Code skill specification (February 2026)
- Standard directory layout: `scripts/`, `references/`, `assets/`
- Valid hook matchers (tool name only, no argument patterns)
- Correct subagent frontmatter fields (name, description, tools)
- CLI command is `claude` (not `claude-code`)
```

## File: `CITATION.cff`
```
cff-version: 1.2.0
title: Claude SEO
message: >-
  If you use this software, please cite it using the metadata from this file.
type: software
authors:
  - alias: AgriciDaniel
repository-code: 'https://github.com/AgriciDaniel/claude-seo'
url: 'https://github.com/AgriciDaniel/claude-seo'
license: MIT
version: 1.4.0
date-released: '2026-03-12'
keywords:
  - seo
  - claude-code
  - ai-tools
  - schema-markup
  - e-e-a-t
  - geo
```

## File: `CLAUDE.md`
```markdown
# Claude SEO: Universal SEO Analysis Skill

## Project Overview

This repository contains **Claude SEO**, a Tier 4 Claude Code skill for comprehensive
SEO analysis across all industries. It follows the Agent Skills open standard and the
3-layer architecture (directive, orchestration, execution). 15 core sub-skills (+ 2
extensions), 10 core subagents (+ 2 extension agents), and an extensible reference
system cover technical SEO, content quality,
schema markup, image optimization, sitemap architecture, AI search optimization,
local SEO (GBP, citations, reviews, map pack), and maps intelligence (geo-grid
rank tracking, GBP auditing, review intelligence, competitor radius mapping).

## Architecture

```
claude-seo/
  CLAUDE.md                          # Project instructions (this file)
  .claude-plugin/
    plugin.json                    # Plugin manifest (v1.7.0)
    marketplace.json               # Marketplace catalog for distribution
  skills/                            # 17 skills (auto-discovered)
    seo/                           # Main orchestrator skill
      SKILL.md                     # Entry point, routing table, core rules
      references/                  # On-demand knowledge files (10 files)
    seo-audit/SKILL.md            # Full site audit with parallel agents
    seo-page/SKILL.md            # Deep single-page analysis
    seo-technical/SKILL.md       # Technical SEO (9 categories)
    seo-content/SKILL.md         # E-E-A-T and content quality
    seo-schema/SKILL.md          # Schema.org markup detection/generation
    seo-sitemap/SKILL.md         # XML sitemap analysis/generation
    seo-images/SKILL.md          # Image optimization analysis
    seo-geo/SKILL.md             # AI search / GEO optimization
    seo-local/SKILL.md           # Local SEO (GBP, citations, reviews, map pack)
    seo-maps/SKILL.md            # Maps intelligence (geo-grid, GBP audit, reviews, competitors)
    seo-plan/SKILL.md            # Strategic SEO planning
    seo-programmatic/SKILL.md    # Programmatic SEO at scale
    seo-competitor-pages/SKILL.md # Competitor comparison pages
    seo-hreflang/SKILL.md       # International SEO / hreflang
    seo-google/                  # Google SEO APIs
      SKILL.md
      references/                # API reference files (7 files)
    seo-dataforseo/SKILL.md     # Live SEO data via DataForSEO MCP
    seo-image-gen/              # AI image generation for SEO assets
      SKILL.md
      references/                # Image gen reference files (7 files)
  agents/                          # 12 subagents (auto-discovered)
    seo-technical.md             # Crawlability, indexability, security
    seo-content.md               # E-E-A-T, readability, thin content
    seo-schema.md                # Structured data validation
    seo-sitemap.md               # Sitemap quality gates
    seo-performance.md           # Core Web Vitals, page speed
    seo-visual.md                # Screenshots, mobile rendering
    seo-geo.md                   # AI crawler access, GEO, citability
    seo-local.md                 # GBP, NAP, citations, reviews, local schema
    seo-maps.md                  # Geo-grid, GBP audit, reviews, competitor radius
    seo-google.md                # Google API analyst (CrUX, GSC, GA4)
    seo-dataforseo.md            # DataForSEO data analyst
    seo-image-gen.md             # SEO image audit analyst
  hooks/                           # Quality gate hooks
    hooks.json                   # PostToolUse schema validation
  scripts/                         # Python execution scripts
  schema/                          # Schema.org JSON-LD templates
  extensions/                      # Optional add-on install helpers
    dataforseo/                  # DataForSEO MCP install scripts
    banana/                      # Banana MCP install scripts
  brain/knowledge/docs_legacy/                            # Extended documentation
```

## Commands

| Command | Purpose |
|---------|---------|
| `/seo audit <url>` | Full site audit with 10 parallel subagents |
| `/seo page <url>` | Deep single-page analysis |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo schema <url>` | Schema.org detection, validation, generation |
| `/seo sitemap <url>` | XML sitemap analysis or generation |
| `/seo images <url>` | Image optimization analysis |
| `/seo geo <url>` | AI search / Generative Engine Optimization |
| `/seo plan <type>` | Strategic SEO planning by industry |
| `/seo programmatic` | Programmatic SEO analysis and planning |
| `/seo competitor-pages` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command] [args]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang <url>` | International SEO / hreflang audit |
| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |
| `/seo image-gen [use-case] <desc>` | AI image generation for SEO assets (extension) |

## Development Rules

- Keep SKILL.md files under 500 lines / 5000 tokens
- Reference files should be focused and under 200 lines
- Scripts must have docstrings, CLI interface, and JSON output
- Follow kebab-case naming for all skill directories
- Agents invoked via Agent tool, never via Bash
- Python dependencies install into `~/.claude/skills/seo/.venv/`
- Test with `python -m pytest tests/` after changes (if applicable)

## Report Generation Rules

- **All SEO reports must use `scripts/google_report.py`** as the canonical report generator
- **Dependencies**: `matplotlib>=3.8.0` (charts) + `weasyprint>=61.0` (HTML-to-PDF), both in `requirements.txt`
- **Format**: A4 PDF via WeasyPrint + matplotlib charts at 200 DPI
- **Style**: Clean white title page with navy (#1e3a5f) accent, Times New Roman body font
- **Color palette**: Navy #1e3a5f (headers), dark gold #b8860b (accents), forest green #2d6a4f (pass), warm amber #d4740e (warnings), deep red #c53030 (fail), warm cream #faf9f7 (backgrounds)
- **Structure**: Title page → TOC with scores → Executive Summary → Data sections → Recommendations → Methodology
- **Charts**: 85% width, max-height 120mm, figure captions on every chart, saved to `charts/` at 200 DPI
- **No `page-break-inside: avoid`** on any element (causes white gaps in WeasyPrint)
- **Post-generation review**: `_review_pdf()` runs automatically, checking for empty images, thin sections, duplicates
- **Before presenting any PDF to the user**: verify the review passes (`"status": "PASS"`)
- **Cross-skill enforcement**: After completing ANY analysis command (audit, page, technical, content, schema, geo, local, maps), offer: "Generate a PDF report? Use `/seo google report`"
- **Google logo** appears on title page when using Google API data ("Powered by Google APIs")

## Ecosystem

Part of the Claude Code skill family:
- [Claude Banana](https://github.com/AgriciDaniel/banana-claude) -- standalone image gen (bundled as extension here)
- [Claude Blog](https://github.com/AgriciDaniel/claude-blog) -- companion blog engine, consumes SEO findings

## Key Principles

1. **Progressive Disclosure**: Metadata always loaded, instructions on activation, resources on demand
2. **Industry Detection**: Auto-detect SaaS, e-commerce, local, publisher, agency
3. **Parallel Execution**: Full audits spawn up to 11 subagents simultaneously
4. **Extension System**: DataForSEO MCP for live data, Banana MCP for AI image generation
```

## File: `CODEOWNERS`
```
# Default owner for everything
* @AgriciDaniel
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

## Our Standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior:

- The use of sexualized language or imagery, and sexual attention or advances
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by [opening an issue](https://github.com/AgriciDaniel/claude-seo/issues) on this repository.

All complaints will be reviewed and investigated promptly and fairly.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/),
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html).
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to claude-seo

Thanks for your interest in contributing! Here's how to get involved.

## Reporting Bugs

Open a [GitHub Issue](https://github.com/AgriciDaniel/claude-seo/issues) with:

- Your OS and Python version
- The full error output (copy from terminal)
- The command or step that failed
- The URL you were analyzing (if applicable)

## Suggesting Features

Use [GitHub Discussions](https://github.com/AgriciDaniel/claude-seo/discussions) for feature ideas and questions.

## Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Test with a sample URL before submitting
5. Submit a PR with a clear description of what changed and why

### Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/claude-seo.git
cd claude-seo
bash install.sh
```

### Guidelines

- All Python scripts should output JSON for Claude Code to parse
- Shell scripts should use `set -euo pipefail` for safety
- SKILL.md files must stay under 500 lines
- Reference files should be focused and under 200 lines
- Follow kebab-case naming for all directories and files
- Keep dependencies minimal

### Code Style

- Python: Follow PEP 8 conventions. Use `ruff check` or `flake8` for linting before submitting
- Shell: Use `set -euo pipefail` and quote all variables
- Markdown: Keep lines under 120 characters where practical
```

## File: `install.ps1`
```powershell
# Claude SEO Installer for Windows
# PowerShell installation script

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "|   Claude SEO - Installer             |" -ForegroundColor Cyan
Write-Host "|   Claude Code SEO Skill              |" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

function Resolve-Python {
    $pythonCmd = Get-Command -Name python -ErrorAction SilentlyContinue
    if ($null -ne $pythonCmd) {
        return @{ Exe = 'python'; Args = @() }
    }

    $pyCmd = Get-Command -Name py -ErrorAction SilentlyContinue
    if ($null -ne $pyCmd) {
        return @{ Exe = 'py'; Args = @('-3') }
    }

    return $null
}

function Invoke-External {
    param(
        [Parameter(Mandatory = $true)][string]$Exe,
        [Parameter(Mandatory = $true)][string[]]$Args,
        [switch]$Quiet
    )

    $previousErrorActionPreference = $ErrorActionPreference
    $hasNativePreference = $null -ne (Get-Variable -Name PSNativeCommandUseErrorActionPreference -ErrorAction SilentlyContinue)
    if ($hasNativePreference) {
        $previousNativePreference = $PSNativeCommandUseErrorActionPreference
    }

    try {
        $ErrorActionPreference = 'Continue'
        if ($hasNativePreference) {
            $PSNativeCommandUseErrorActionPreference = $false
        }

        $output = & $Exe @Args 2>&1 | ForEach-Object { $_.ToString() }
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
        if ($hasNativePreference) {
            $PSNativeCommandUseErrorActionPreference = $previousNativePreference
        }
    }

    if (-not $Quiet -and $null -ne $output -and $output.Count -gt 0) {
        $output | ForEach-Object { Write-Host $_ }
    }

    return @{ ExitCode = $exitCode; Output = $output }
}

# Check prerequisites
$python = Resolve-Python
if ($null -eq $python) {
    Write-Host "[x] Python is required but was not found (tried 'python' and 'py')." -ForegroundColor Red
    exit 1
}

try {
    $pythonVersion = & $python.Exe @($python.Args + @('--version')) 2>&1
    Write-Host "[+] $pythonVersion detected" -ForegroundColor Green
} catch {
    Write-Host "[x] Python is installed but could not be executed." -ForegroundColor Red
    exit 1
}

try {
    git --version | Out-Null
    Write-Host "[+] Git detected" -ForegroundColor Green
} catch {
    Write-Host "[x] Git is required but not installed." -ForegroundColor Red
    exit 1
}

# Set paths
$SkillDir = "$env:USERPROFILE\.claude\skills\seo"
$AgentDir = "$env:USERPROFILE\.claude\agents"
$RepoUrl = "https://github.com/AgriciDaniel/claude-seo"
# Pin to a specific release tag to prevent silent updates from main.
# Override: $env:CLAUDE_SEO_TAG = 'main'; .\install.ps1
$RepoTag = if ($env:CLAUDE_SEO_TAG) { $env:CLAUDE_SEO_TAG } else { 'v1.6.0' }

# Create directories
New-Item -ItemType Directory -Force -Path $SkillDir | Out-Null
New-Item -ItemType Directory -Force -Path $AgentDir | Out-Null

# Clone to temp directory
$TempDir = Join-Path $env:TEMP "claude-seo-install"
if (Test-Path $TempDir) {
    Remove-Item -Recurse -Force $TempDir
}

$keepTemp = ($env:CLAUDE_SEO_KEEP_TEMP -eq '1')

try {
    Write-Host ">> Downloading Claude SEO ($RepoTag)..." -ForegroundColor Yellow
    $clone = Invoke-External -Exe 'git' -Args @('clone','--depth','1','--branch',$RepoTag,$RepoUrl,$TempDir) -Quiet
    if ($clone.ExitCode -ne 0) {
        throw "git clone failed. Output:`n$($clone.Output -join "`n")"
    }

    # Copy skill files
    Write-Host "=> Installing skill files..." -ForegroundColor Yellow
    $skillSource = Join-Path $TempDir 'seo'
    if (-not (Test-Path $skillSource)) {
        $skillSource = Join-Path $TempDir 'skills\seo'
    }
    if (-not (Test-Path $skillSource)) {
        throw "Could not find skill source folder in repo clone."
    }
    Copy-Item -Recurse -Force (Join-Path $skillSource '*') $SkillDir

    # Copy sub-skills
    $SkillsPath = "$TempDir\skills"
    if (Test-Path $SkillsPath) {
        Get-ChildItem -Directory $SkillsPath | ForEach-Object {
            $target = "$env:USERPROFILE\.claude\skills\$($_.Name)"
            New-Item -ItemType Directory -Force -Path $target | Out-Null
            Copy-Item -Recurse -Force "$($_.FullName)\*" $target
        }
    }

    # Copy schema templates
    $SchemaPath = "$TempDir\schema"
    if (Test-Path $SchemaPath) {
        $SkillSchema = "$SkillDir\schema"
        New-Item -ItemType Directory -Force -Path $SkillSchema | Out-Null
        Copy-Item -Recurse -Force "$SchemaPath\*" $SkillSchema
    }

    # Copy reference docs
    $PdfPath = "$TempDir\pdf"
    if (Test-Path $PdfPath) {
        $SkillPdf = "$SkillDir\pdf"
        New-Item -ItemType Directory -Force -Path $SkillPdf | Out-Null
        Copy-Item -Recurse -Force "$PdfPath\*" $SkillPdf
    }

    # Copy agents
    Write-Host "=> Installing subagents..." -ForegroundColor Yellow
    $AgentsPath = Join-Path $TempDir 'agents'
    if (Test-Path $AgentsPath) {
        Copy-Item -Force (Join-Path $AgentsPath '*.md') $AgentDir -ErrorAction SilentlyContinue
    }

    # Copy shared scripts
    $ScriptsPath = "$TempDir\scripts"
    if (Test-Path $ScriptsPath) {
        $SkillScripts = "$SkillDir\scripts"
        New-Item -ItemType Directory -Force -Path $SkillScripts | Out-Null
        Copy-Item -Recurse -Force "$ScriptsPath\*" $SkillScripts
    }

    # Copy hooks
    $HooksPath = "$TempDir\hooks"
    if (Test-Path $HooksPath) {
        $SkillHooks = "$SkillDir\hooks"
        New-Item -ItemType Directory -Force -Path $SkillHooks | Out-Null
        Copy-Item -Recurse -Force "$HooksPath\*" $SkillHooks
    }

    # Copy extensions (optional add-ons: dataforseo, banana)
    $ExtensionsPath = Join-Path $TempDir 'extensions'
    if (Test-Path $ExtensionsPath) {
        Write-Host "=> Installing extensions..." -ForegroundColor Yellow
        Get-ChildItem -Directory $ExtensionsPath | ForEach-Object {
            $extName = $_.Name
            $extDir = $_.FullName
            # Extension skills
            $extSkills = Join-Path $extDir 'skills'
            if (Test-Path $extSkills) {
                Get-ChildItem -Directory $extSkills | ForEach-Object {
                    $target = "$env:USERPROFILE\.claude\skills\$($_.Name)"
                    New-Item -ItemType Directory -Force -Path $target | Out-Null
                    Copy-Item -Recurse -Force "$($_.FullName)\*" $target
                }
            }
            # Extension agents
            $extAgents = Join-Path $extDir 'agents'
            if (Test-Path $extAgents) {
                Copy-Item -Force (Join-Path $extAgents '*.md') $AgentDir -ErrorAction SilentlyContinue
            }
            # Extension references
            $extRefs = Join-Path $extDir 'references'
            if (Test-Path $extRefs) {
                $refTarget = "$SkillDir\extensions\$extName\references"
                New-Item -ItemType Directory -Force -Path $refTarget | Out-Null
                Copy-Item -Recurse -Force "$extRefs\*" $refTarget
            }
            # Extension scripts
            $extScripts = Join-Path $extDir 'scripts'
            if (Test-Path $extScripts) {
                $scriptTarget = "$SkillDir\extensions\$extName\scripts"
                New-Item -ItemType Directory -Force -Path $scriptTarget | Out-Null
                Copy-Item -Recurse -Force "$extScripts\*" $scriptTarget
            }
        }
    }

    # Copy requirements.txt to skill dir for retry
    $reqFile = Join-Path $TempDir 'requirements.txt'
    $installedReqFile = Join-Path $SkillDir 'requirements.txt'
    if (Test-Path $reqFile) {
        Copy-Item -Force $reqFile $installedReqFile
    }

    # Install Python dependencies
    Write-Host "=> Installing Python dependencies..." -ForegroundColor Yellow
    if (Test-Path $reqFile) {
        try {
            $pip = Invoke-External -Exe $python.Exe -Args @($python.Args + @('-m','pip','install','-q','-r',$reqFile)) -Quiet
            if ($pip.ExitCode -ne 0) {
                throw ($pip.Output -join "`n")
            }
        } catch {
            Write-Host "  [!]  Could not auto-install Python packages." -ForegroundColor Yellow
            Write-Host "  Try: $($python.Exe) $($python.Args -join ' ') -m pip install -r `"$installedReqFile`"" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  [!]  No requirements.txt found; skipping Python dependency install." -ForegroundColor Yellow
    }

    # Optional: Install Playwright browsers
    Write-Host "=> Installing Playwright browsers (optional, for visual analysis)..." -ForegroundColor Yellow
    try {
        $pw = Invoke-External -Exe $python.Exe -Args @($python.Args + @('-m','playwright','install','chromium')) -Quiet
        if ($pw.ExitCode -ne 0) {
            throw ($pw.Output -join "`n")
        }
    } catch {
        Write-Host "  [!]  Playwright install failed. Visual analysis will use WebFetch fallback." -ForegroundColor Yellow
    }
} catch {
    Write-Host ""
    Write-Host "[x] Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    if ($keepTemp -and (Test-Path $TempDir)) {
        Write-Host "Temp dir kept at: $TempDir" -ForegroundColor Yellow
    }
    throw
} finally {
    if (-not $keepTemp -and (Test-Path $TempDir)) {
        Remove-Item -Recurse -Force $TempDir
    }
}

Write-Host ""
Write-Host "[+] Claude SEO installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Usage:" -ForegroundColor Cyan
Write-Host "  1. Start Claude Code:  claude"
Write-Host "  2. Run commands:       /seo audit https://example.com"
Write-Host ""
Write-Host "Python deps location: $installedReqFile" -ForegroundColor Gray
```

## File: `install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Claude SEO Installer
# Wraps everything in main() to prevent partial execution on network failure

main() {
    SKILL_DIR="${HOME}/.claude/skills/seo"
    AGENT_DIR="${HOME}/.claude/agents"
    REPO_URL="https://github.com/AgriciDaniel/claude-seo"
    # Pin to a specific release tag to prevent silent updates from main.
    # Override: CLAUDE_SEO_TAG=main bash install.sh
    REPO_TAG="${CLAUDE_SEO_TAG:-v1.6.0}"

    echo "════════════════════════════════════════"
    echo "║   Claude SEO - Installer             ║"
    echo "║   Claude Code SEO Skill              ║"
    echo "════════════════════════════════════════"
    echo ""

    # Check prerequisites
    command -v python3 >/dev/null 2>&1 || { echo "✗ Python 3 is required but not installed."; exit 1; }
    command -v git >/dev/null 2>&1 || { echo "✗ Git is required but not installed."; exit 1; }

    # Check Python version (3.10+ required)
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PYTHON_OK=$(python3 -c 'import sys; print(1 if sys.version_info >= (3, 10) else 0)')
    if [ "${PYTHON_OK}" = "0" ]; then
        echo "✗ Python 3.10+ is required but ${PYTHON_VERSION} was found."
        exit 1
    fi
    echo "✓ Python ${PYTHON_VERSION} detected"

    # Create directories
    mkdir -p "${SKILL_DIR}"
    mkdir -p "${AGENT_DIR}"

    # Clone or update
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf ${TEMP_DIR}" EXIT

    echo "↓ Downloading Claude SEO (${REPO_TAG})..."
    git clone --depth 1 --branch "${REPO_TAG}" "${REPO_URL}" "${TEMP_DIR}/claude-seo" 2>/dev/null

    # Copy skill files
    echo "→ Installing skill files..."
    cp -r "${TEMP_DIR}/claude-seo/seo/"* "${SKILL_DIR}/"

    # Copy sub-skills
    if [ -d "${TEMP_DIR}/claude-seo/skills" ]; then
        for skill_dir in "${TEMP_DIR}/claude-seo/skills"/*/; do
            skill_name=$(basename "${skill_dir}")
            target="${HOME}/.claude/skills/${skill_name}"
            mkdir -p "${target}"
            cp -r "${skill_dir}"* "${target}/"
        done
    fi

    # Copy schema templates
    if [ -d "${TEMP_DIR}/claude-seo/schema" ]; then
        mkdir -p "${SKILL_DIR}/schema"
        cp -r "${TEMP_DIR}/claude-seo/schema/"* "${SKILL_DIR}/schema/"
    fi

    # Copy reference docs
    if [ -d "${TEMP_DIR}/claude-seo/pdf" ]; then
        mkdir -p "${SKILL_DIR}/pdf"
        cp -r "${TEMP_DIR}/claude-seo/pdf/"* "${SKILL_DIR}/pdf/"
    fi

    # Copy agents
    echo "→ Installing subagents..."
    cp -r "${TEMP_DIR}/claude-seo/agents/"*.md "${AGENT_DIR}/" 2>/dev/null || true

    # Copy shared scripts
    if [ -d "${TEMP_DIR}/claude-seo/scripts" ]; then
        mkdir -p "${SKILL_DIR}/scripts"
        cp -r "${TEMP_DIR}/claude-seo/scripts/"* "${SKILL_DIR}/scripts/"
    fi

    # Copy hooks
    if [ -d "${TEMP_DIR}/claude-seo/hooks" ]; then
        mkdir -p "${SKILL_DIR}/hooks"
        cp -r "${TEMP_DIR}/claude-seo/hooks/"* "${SKILL_DIR}/hooks/"
        chmod +x "${SKILL_DIR}/hooks/"*.sh 2>/dev/null || true
        chmod +x "${SKILL_DIR}/hooks/"*.py 2>/dev/null || true
    fi

    # Copy extensions (optional add-ons: dataforseo, banana)
    if [ -d "${TEMP_DIR}/claude-seo/extensions" ]; then
        echo "=> Installing extensions..."
        for ext_dir in "${TEMP_DIR}/claude-seo/extensions"/*/; do
            [ -d "${ext_dir}" ] || continue
            ext_name=$(basename "${ext_dir}")
            # Extension skills
            if [ -d "${ext_dir}skills" ]; then
                for ext_skill in "${ext_dir}skills"/*/; do
                    [ -d "${ext_skill}" ] || continue
                    ext_skill_name=$(basename "${ext_skill}")
                    target="${HOME}/.claude/skills/${ext_skill_name}"
                    mkdir -p "${target}"
                    cp -r "${ext_skill}"* "${target}/"
                done
            fi
            # Extension agents
            if [ -d "${ext_dir}agents" ]; then
                cp -r "${ext_dir}agents/"*.md "${AGENT_DIR}/" 2>/dev/null || true
            fi
            # Extension references
            if [ -d "${ext_dir}references" ]; then
                mkdir -p "${SKILL_DIR}/extensions/${ext_name}/references"
                cp -r "${ext_dir}references/"* "${SKILL_DIR}/extensions/${ext_name}/references/"
            fi
            # Extension scripts
            if [ -d "${ext_dir}scripts" ]; then
                mkdir -p "${SKILL_DIR}/extensions/${ext_name}/scripts"
                cp -r "${ext_dir}scripts/"* "${SKILL_DIR}/extensions/${ext_name}/scripts/"
            fi
        done
    fi

    # Copy requirements.txt to skill dir so users can retry later
    cp "${TEMP_DIR}/claude-seo/requirements.txt" "${SKILL_DIR}/requirements.txt" 2>/dev/null || true

    # Install Python dependencies (venv preferred, --user fallback)
    echo "→ Installing Python dependencies..."
    VENV_DIR="${SKILL_DIR}/.venv"
    if python3 -m venv "${VENV_DIR}" 2>/dev/null; then
        "${VENV_DIR}/bin/pip" install --quiet -r "${TEMP_DIR}/claude-seo/requirements.txt" 2>/dev/null && \
            echo "  ✓ Installed in venv at ${VENV_DIR}" || \
            echo "  ⚠  Venv pip install failed. Run: ${VENV_DIR}/bin/pip install -r ${SKILL_DIR}/requirements.txt"
    else
        pip install --quiet --user -r "${TEMP_DIR}/claude-seo/requirements.txt" 2>/dev/null || \
        echo "  ⚠  Could not auto-install. Run: pip install --user -r ${SKILL_DIR}/requirements.txt"
    fi

    # Optional: Install Playwright browsers (for screenshot analysis)
    echo "→ Installing Playwright browsers (optional, for visual analysis)..."
    if [ -f "${VENV_DIR}/bin/playwright" ]; then
        "${VENV_DIR}/bin/python" -m playwright install chromium 2>/dev/null || \
        echo "  ⚠  Playwright install failed. Visual analysis will use WebFetch fallback."
    else
        python3 -m playwright install chromium 2>/dev/null || \
        echo "  ⚠  Playwright install failed. Visual analysis will use WebFetch fallback."
    fi

    echo ""
    echo "✓ Claude SEO installed successfully!"
    echo ""
    echo "Usage:"
    echo "  1. Start Claude Code:  claude"
    echo "  2. Run commands:       /seo audit https://example.com"
    echo ""
    echo "Python deps location: ${SKILL_DIR}/requirements.txt"
    echo "To uninstall: curl -fsSL ${REPO_URL}/raw/main/uninstall.sh | bash"
}

main "$@"
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 agricidaniel

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

## File: `pyproject.toml`
```
[project]
name = "claude-seo"
version = "1.7.0"
description = "Comprehensive SEO analysis skill for Claude Code"
requires-python = ">=3.11"
license = "MIT"
readme = "README.md"

[project.urls]
Homepage = "https://github.com/AgriciDaniel/claude-seo"
Repository = "https://github.com/AgriciDaniel/claude-seo"
```

## File: `README.md`
```markdown
<!-- Updated: 2026-03-28 -->

![Claude SEO](screenshots/cover-image.jpeg)

# Claude SEO - SEO Audit Skill for Claude Code

Comprehensive SEO analysis skill for Claude Code. Covers technical SEO, on-page analysis, content quality (E-E-A-T), schema markup, image optimization, sitemap architecture, AI search optimization (GEO), local SEO, maps intelligence, Google SEO APIs (Search Console, PageSpeed, CrUX, GA4), PDF report generation, and strategic planning.

![SEO Command Demo](screenshots/seo-command-demo.gif)

[![CI](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml/badge.svg)](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-seo)](https://github.com/AgriciDaniel/claude-seo/releases)

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [Features](#features)
- [Architecture](#architecture)
- [Extensions](#extensions)
- [Ecosystem](#ecosystem)
- [Documentation](#documentation)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Contributing](#contributing)

## Installation

### Recommended Install (Unix/macOS/Linux)

```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

<details>
<summary>One-liner (curl)</summary>

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

Or via [install.cat](https://install.cat):

```bash
curl -fsSL install.cat/AgriciDaniel/claude-seo | bash
```

Prefer to review the script before running?

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh > install.sh
cat install.sh        # review
bash install.sh       # run when satisfied
rm install.sh
```

</details>

### Windows (PowerShell)

```powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
```

> **Why git clone instead of `irm | iex`?** Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk (downloading and executing remote code with no verification). The git clone approach lets you inspect the script at `claude-seo\install.ps1` before running it.

## Quick Start

```bash
# Start Claude Code
claude

# Run a full site audit
/seo audit https://example.com

# Analyze a single page
/seo page https://example.com/about

# Check schema markup
/seo schema https://example.com

# Generate a sitemap
/seo sitemap generate

# Optimize for AI search
/seo geo https://example.com
```
### Demo:
[Watch the full demo on YouTube](https://www.youtube.com/watch?v=COMnNlUakQk)

**`/seo audit`: full site audit with parallel subagents:**

![SEO Audit Demo](screenshots/seo-audit-demo.gif)

## Commands

| Command | Description |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel subagent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo sitemap <url>` | Analyze existing XML sitemap |
| `/seo sitemap generate` | Generate new sitemap with industry templates |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo images <url>` | Image optimization analysis |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <type>` | Strategic SEO planning (saas, local, ecommerce, publisher, agency) |
| `/seo programmatic <url>` | Programmatic SEO analysis and planning |
| `/seo competitor-pages <url>` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang <url>` | Hreflang/i18n SEO audit and generation |
| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |
| `/seo google report [type]` | Generate PDF/HTML report with charts (cwv-audit, gsc-performance, full) |

### `/seo programmatic [url|plan]`
**Programmatic SEO Analysis & Planning**

Build SEO pages at scale from data sources with quality safeguards.

**Capabilities:**
- Analyze existing programmatic pages for thin content and cannibalization
- Plan URL patterns and template structures for data-driven pages
- Internal linking automation between generated pages
- Canonical strategy and index bloat prevention
- Quality gates: WARNING at 100+ pages, HARD STOP at 500+ without audit

### `/seo competitor-pages [url|generate]`
**Competitor Comparison Page Generator**

Create high-converting "X vs Y" and "alternatives to X" pages.

**Capabilities:**
- Structured comparison tables with feature matrices
- Product schema markup with AggregateRating
- Conversion-optimized layouts with CTA placement
- Keyword targeting for comparison intent queries
- Fairness guidelines for accurate competitor representation

### `/seo hreflang [url]`
**Hreflang / i18n SEO Audit & Generation**

Validate and generate hreflang tags for multi-language sites.

**Capabilities:**
- Generate hreflang tags (HTML, HTTP headers, or XML sitemap)
- Validate self-referencing tags, return tags, x-default
- Detect common mistakes (missing returns, invalid codes, HTTP/HTTPS mismatch)
- Cross-domain hreflang support
- Language/region code validation (ISO 639-1 + ISO 3166-1)

## Features

### Core Web Vitals (Current Metrics)
- **LCP** (Largest Contentful Paint): Target < 2.5s
- **INP** (Interaction to Next Paint): Target < 200ms
- **CLS** (Cumulative Layout Shift): Target < 0.1

> Note: INP replaced FID on March 12, 2024. FID was fully removed from all Chrome tools on September 9, 2024.

### E-E-A-T Analysis
Updated to September 2025 Quality Rater Guidelines:
- **Experience**: First-hand knowledge signals
- **Expertise**: Author credentials and depth
- **Authoritativeness**: Industry recognition
- **Trustworthiness**: Contact info, security, transparency

### Schema Markup
- Detection: JSON-LD (preferred), Microdata, RDFa
- Validation against Google's supported types
- Generation with templates
- Deprecation awareness:
  - HowTo: Deprecated (Sept 2023)
  - FAQ: Restricted to gov/health sites (Aug 2023)
  - SpecialAnnouncement: Deprecated (July 2025)

### AI Search Optimization (GEO)
New for 2026 - optimize for:
- Google AI Overviews
- ChatGPT web search
- Perplexity
- Other AI-powered search

### Google SEO APIs (New in v1.7.0)
Direct integration with Google's SEO data:
- **PageSpeed Insights + CrUX**: Lab and field Core Web Vitals data
- **Search Console**: Top queries, URL inspection, sitemap status
- **Indexing API**: Notify Google of new/updated/removed URLs
- **GA4**: Organic traffic, top landing pages, device/country breakdown
- **PDF Reports**: Enterprise A4 reports with charts via WeasyPrint + matplotlib

4-tier credential system — get value at every level:
| Tier | Auth | APIs |
|------|------|------|
| 0 | API key | PSI, CrUX, CrUX History |
| 1 | + OAuth/SA | + GSC, URL Inspection, Indexing |
| 2 | + GA4 config | + GA4 organic traffic |
| 3 | + Ads token | + Keyword Planner |

### Local SEO & Maps Intelligence (New in v1.6.0)
- Google Business Profile optimization
- NAP consistency auditing
- Citation and review analysis
- Geo-grid rank tracking and competitor radius mapping

### Quality Gates
- Warning at 30+ location pages
- Hard stop at 50+ location pages
- Thin content detection per page type
- Doorway page prevention

## Architecture

```
~/.claude/skills/seo/         # Main orchestrator skill
~/.claude/skills/seo-*/       # Sub-skills (15 + 2 extensions)
~/.claude/agents/seo-*.md     # Subagents (10 + 2 extensions)
```

### Video & Live Schema (New)
Additional schema types for video content, live streaming, and key moments:
- VideoObject: Video page markup with thumbnails, duration, upload date
- BroadcastEvent: LIVE badge support for live streaming content
- Clip: Key moments / chapters within videos
- SeekToAction: Enable seek functionality in video rich results
- SoftwareSourceCode: Open source and code repository pages

See `schema/templates.json` for ready-to-use JSON-LD snippets.

### Recently Added
- Programmatic SEO skill (`/seo programmatic`)
- Competitor comparison pages skill (`/seo competitor-pages`)
- Multi-language hreflang validation (`/seo hreflang`)
- Video & Live schema types (VideoObject, BroadcastEvent, Clip, SeekToAction)
- Google SEO quick-reference guide

## Requirements

- Python 3.10+
- Claude Code CLI
- Optional: Playwright for screenshots
- Optional: Google API credentials for enriched data (see `/seo google setup`)

## Uninstall

```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/uninstall.sh
```

<details>
<summary>One-liner (curl)</summary>

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash
```

</details>

### MCP Integrations

Integrates with MCP servers for live SEO data, including official servers from **Ahrefs** (`@ahrefs/mcp`) and **Semrush**, plus community servers for Google Search Console, PageSpeed Insights, and DataForSEO. See [MCP Integration Guide](mcp-integration.md) for setup.

## Extensions

Optional add-ons that integrate external data sources via MCP servers.

### DataForSEO

Live SERP data, keyword research, backlinks, on-page analysis, content analysis, business listings, AI visibility checking, and LLM mention tracking. 22 commands across 9 API modules.

```bash
# Install (requires DataForSEO account)
./extensions/dataforseo/install.sh
```

```bash
# Example commands
/seo dataforseo serp best coffee shops
/seo dataforseo keywords seo tools
/seo dataforseo backlinks example.com
/seo dataforseo ai-mentions your brand
/seo dataforseo ai-scrape your brand name
```

See [DataForSEO Extension](../../../README.md) for full documentation.

### Banana (AI Image Generation)

Generate SEO images (OG previews, blog heroes, product photos, infographics) using the
[Claude Banana](https://github.com/AgriciDaniel/banana-claude) Creative Director pipeline.

```bash
# Install extension
./extensions/banana/install.sh
```

```bash
# Example commands
/seo image-gen og "Professional SaaS dashboard"
/seo image-gen hero "AI-powered content creation"
/seo image-gen batch "Product photography" 3
```

See [Banana Extension](../../../README.md) for full documentation.
Already using standalone Claude Banana? The extension reuses your existing nanobanana-mcp setup.

## Ecosystem

Claude SEO is part of a family of Claude Code skills that work together:

| Skill | What it does | How it connects |
|-------|-------------|-----------------|
| [Claude SEO](https://github.com/AgriciDaniel/claude-seo) | SEO analysis, audits, schema, GEO | Core -- analyzes sites, generates action plans |
| [Claude Blog](https://github.com/AgriciDaniel/claude-blog) | Blog writing, optimization, scoring | Companion -- write content optimized by SEO findings |
| [Claude Banana](https://github.com/AgriciDaniel/banana-claude) | AI image generation via Gemini | Shared -- generates images for SEO assets and blog posts |

**Workflow example:**
1. `/seo audit https://example.com` -- identify content gaps and image issues
2. `/blog write "target keyword"` -- create SEO-optimized blog posts
3. `/seo image-gen hero "blog topic"` -- generate hero images (banana extension)
4. `/seo geo https://example.com/blog/post` -- optimize for AI citations

## Documentation

- [Installation Guide](installation.md)
- [Commands Reference](../bmad_repo/commands.md)
- [Architecture](ARCHITECTURE.md)
- [MCP Integration](mcp-integration.md)
- [Troubleshooting](troubleshooting.md)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting PRs.

---

Built for Claude Code by [@AgriciDaniel](https://github.com/AgriciDaniel)
```

## File: `requirements.txt`
```
# Claude SEO - Python Dependencies
# Bounded version pinning with security-conscious minimums
# Last updated: February 7, 2026

beautifulsoup4>=4.12.0,<5.0.0     # No known CVEs
requests>=2.32.4,<3.0.0           # CVE-2024-47081, CVE-2024-35195 fixes
lxml>=6.0.2,<7.0.0                # CVE-2025-24928 + additional libxml2 security patches
playwright>=1.56.0,<2.0.0         # CVE-2025-59288 fix (macOS)
Pillow>=12.1.0,<13.0.0            # CVE-2025-48379 fix
urllib3>=2.6.3,<3.0.0             # CRITICAL: CVE-2026-21441 (CVSS 8.9), CVE-2025-66418
validators>=0.22.0,<1.0.0         # No known CVEs

# Report generation (for seo-google PDF reports)
matplotlib>=3.8.0,<4.0.0              # No known CVEs
weasyprint>=61.0,<70.0                # No known CVEs

# Google API dependencies (for seo-google skill)
google-api-python-client>=2.100.0,<3.0.0   # No known CVEs
google-auth>=2.20.0,<3.0.0                  # No known CVEs
google-auth-oauthlib>=1.0.0,<2.0.0          # No known CVEs
google-auth-httplib2>=0.2.0,<1.0.0           # No known CVEs
google-analytics-data>=0.18.0,<1.0.0         # No known CVEs
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT open a public issue**
2. Open a [GitHub Security Advisory](https://github.com/AgriciDaniel/claude-seo/security/advisories/new) on this repo
3. Or contact the maintainer directly

## Response Timeline

- **Acknowledgment**: Within 72 hours of report
- **Status update**: Within 7 days with initial assessment
- **Resolution**: We aim to release a fix within 30 days for confirmed vulnerabilities

## Supported Versions

Only the latest version receives security updates.

## Security Practices

- No credentials or API keys are stored in this repository
- Install scripts write only to user-level directories (`~/.claude/`)
- Python dependencies install in isolated virtual environments
```

## File: `SUPPORT.md`
```markdown
# Support

## Getting Help

- **Questions & Discussions**: [GitHub Discussions](https://github.com/AgriciDaniel/claude-seo/discussions)
- **Bug Reports**: [GitHub Issues](https://github.com/AgriciDaniel/claude-seo/issues) (use the bug report template)
- **Feature Requests**: [GitHub Discussions](https://github.com/AgriciDaniel/claude-seo/discussions)

## Documentation

- [Installation Guide](installation.md)
- [Commands Reference](../bmad_repo/commands.md)
- [Architecture](ARCHITECTURE.md)
- [MCP Integration](mcp-integration.md)
- [Troubleshooting](troubleshooting.md)

## Before Opening an Issue

1. Check [Troubleshooting](troubleshooting.md) for common solutions
2. Search [existing issues](https://github.com/AgriciDaniel/claude-seo/issues) for duplicates
3. Include your OS, Python version, and the full error output
```

## File: `TODO.md`
```markdown
# TODO: claude-seo

## Completed in v1.2.0

- [x] **Fix YAML frontmatter parsing**:Removed HTML comments before `---` in 8 files (from @kylewhirl fork)
- [x] **SSRF prevention in Python scripts**:Private IP blocking in fetch_page.py and analyze_visual.py (from @artyomsv #7)
- [x] **Install hardening**:venv-based pip, no `--break-system-packages` (from @JawandS #2)
- [x] **Windows install fixes**:`python -m pip`, `py -3` fallback, requirements.txt persistence (from @kfrancis #5, PR #6)
- [x] **requirements.txt persistence**:Copied to skill dir after install (from @edustef #1)
- [x] **Path traversal prevention**:Output path sanitization in capture_screenshot.py, file validation in parse_html.py

## Completed: Extensions

- [x] **Extension system**:`extensions/` directory convention with self-contained add-ons
- [x] **DataForSEO extension**:22 commands across 9 API modules (SERP, keywords, backlinks, on-page, content, business listings, AI visibility, LLM mentions). Install: `./extensions/dataforseo/install.sh`

## Deferred from Community Feedback

- [ ] **Reduce Bash scope on agents** (Priority: Medium, from @artyomsv #7)
  Evaluate which agents truly need Bash access. Consider replacing with WebFetch where possible.

- [ ] **Docker-based script execution** (Priority: Low, from @artyomsv #7)
  Sandbox Python scripts in Docker for users who want extra isolation.

- [ ] **Opencode compatibility** (Priority: Low, from @Ehtz #4)
  Adapt skill architecture for Opencode. @kylewhirl already ported to OpenAI Codex.

- [ ] **Subagent timeout/compact handling** (Priority: Medium, from @JawandS #3)
  Primary agent sometimes terminates before subagents finish. Consider encouraging subagents
  to run /compact and adding explicit wait logic.

- [ ] **Native Chrome tools vs Playwright** (Priority: Medium, from @artyomsv #7, @btafoya PR #8)
  Claude Code has native browser automation. Evaluate replacing Playwright with built-in tools
  to eliminate the ~200MB Chromium dependency.

## Deferred from February 2026 Research Report

- [ ] **Fake freshness detection** (Priority: Medium)
  Compare visible dates (`datePublished`, `dateModified`) against actual content modification signals.
  Flag pages with updated dates but unchanged body content.

- [ ] **Mobile content parity check** (Priority: Medium)
  Compare mobile vs desktop meta tags, structured data presence, and content completeness.
  Flag discrepancies that could affect mobile-first indexing.

- [ ] **Discover optimization checks** (Priority: Low-Medium)
  Clickbait title detection, content depth scoring, local relevance signals, sensationalism flags.

- [ ] **Brand mention analysis Python implementation** (Priority: Low)
  Currently documented in `seo-geo/SKILL.md` but no programmatic scoring.

## SPA / Client-Side Rendering Support (Issue #11)

Phase 2 (merged in v1.4.0):
- [x] **`--googlebot` flag in fetch_page.py**:Compare response size with default UA vs Googlebot UA to detect prerender services

Remaining phases (deferred):

- [ ] **Phase 1: render_page.py** (Priority: High):Playwright-based page renderer that exports fully-rendered DOM HTML. CLI: `python render_page.py https://example.com --output rendered.html`. Drop-in complement to `fetch_page.py`.

- [ ] **Phase 3: Screenshot DOM export** (Priority: Medium):Add `--export-html` flag to `capture_screenshot.py` so rendered DOM is available to other agents without a second browser launch.

- [ ] **Phase 4: Orchestrator SPA detection** (Priority: High):Add 6 SPA detection signals to `skills/seo/SKILL.md` (empty root div, minimal body, prerenderReady, framework markers, large JS bundles, React/Vue/Angular attributes). Route agents to raw vs rendered HTML based on detection result.

- [ ] **Phase 5: Agent updates** (Priority: High):Update seo-technical, seo-content, seo-schema, seo-performance, seo-visual to use rendered DOM when SPA detected. Add WRS (Web Rendering Service) dependency risk deductions.

- [ ] **Phase 6: SPA scoring methodology** (Priority: Medium):Separate scoring paths for SPAs with/without prerender. New "Rendering Architecture Assessment" report section.

- [ ] **Phase 7: Reference file updates** (Priority: Low):Add SPA section to quality-gates.md, eeat-framework.md, cwv-thresholds.md (Soft Navigations API guidance).

---

*Last updated: March 12, 2026*
```

## File: `uninstall.ps1`
```powershell
#!/usr/bin/env pwsh
# claude-seo uninstaller for Windows
# Cleanly removes all SEO skills, agents, and scripts

$ErrorActionPreference = "Stop"

function Write-Color($Color, $Text) {
    Write-Host $Text -ForegroundColor $Color
}

function Main {
    $SkillDir = Join-Path $env:USERPROFILE ".claude" "skills"
    $AgentDir = Join-Path $env:USERPROFILE ".claude" "agents"

    Write-Color Cyan "=== Uninstalling claude-seo ==="
    Write-Host ""

    # Remove main skill (includes venv, references, scripts, hooks)
    $seoDir = Join-Path $SkillDir "seo"
    if (Test-Path $seoDir) {
        Remove-Item -Recurse -Force $seoDir
        Write-Color Green "  Removed: $seoDir"
    }

    # Remove sub-skills
    $subSkills = @(
        "seo-audit", "seo-competitor-pages", "seo-content", "seo-geo",
        "seo-hreflang", "seo-images", "seo-page", "seo-plan",
        "seo-programmatic", "seo-schema", "seo-sitemap", "seo-technical"
    )
    foreach ($skill in $subSkills) {
        $skillPath = Join-Path $SkillDir $skill
        if (Test-Path $skillPath) {
            Remove-Item -Recurse -Force $skillPath
            Write-Color Green "  Removed: $skillPath"
        }
    }

    # Remove agents
    $agents = @(
        "seo-technical", "seo-content", "seo-schema",
        "seo-sitemap", "seo-performance", "seo-visual", "seo-geo"
    )
    foreach ($agent in $agents) {
        $agentPath = Join-Path $AgentDir "$agent.md"
        if (Test-Path $agentPath) {
            Remove-Item -Force $agentPath
            Write-Color Green "  Removed: $agentPath"
        }
    }

    Write-Host ""
    Write-Color Cyan "=== claude-seo uninstalled ==="
    Write-Host ""
    Write-Color Yellow "Restart Claude Code to complete removal."
}

Main
```

## File: `uninstall.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

main() {
    echo "→ Uninstalling Claude SEO..."

    # Remove main skill (includes venv and requirements.txt)
    rm -rf "${HOME}/.claude/skills/seo"

    # Remove sub-skills
    for skill in seo-audit seo-competitor-pages seo-content seo-geo seo-hreflang seo-images seo-page seo-plan seo-programmatic seo-schema seo-sitemap seo-technical; do
        rm -rf "${HOME}/.claude/skills/${skill}"
    done

    # Remove agents
    for agent in seo-technical seo-content seo-schema seo-sitemap seo-performance seo-visual seo-geo; do
        rm -f "${HOME}/.claude/agents/${agent}.md"
    done

    echo "✓ Claude SEO uninstalled."
}

main "$@"
```

## File: `agents/seo-content.md`
```markdown
---
name: seo-content
description: Content quality reviewer. Evaluates E-E-A-T signals, readability, content depth, AI citation readiness, and thin content detection.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write, Grep
---

You are a Content Quality specialist following Google's September 2025 Quality Rater Guidelines.

When given content to analyze:

1. Assess E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness)
2. Check word count against page type minimums
3. Calculate readability metrics
4. Evaluate keyword optimization (natural, not stuffed)
5. Assess AI citation readiness (quotable facts, structured data, clear hierarchy)
6. Check content freshness and update signals
7. Flag potential AI-generated content quality issues per Sept 2025 QRG criteria

## E-E-A-T Scoring

| Factor | Weight | What to Look For |
|--------|--------|------------------|
| Experience | 20% | First-hand signals, original content, case studies |
| Expertise | 25% | Author credentials, technical accuracy |
| Authoritativeness | 25% | External recognition, citations, reputation |
| Trustworthiness | 30% | Contact info, transparency, security |

## Content Minimums

| Page Type | Min Words |
|-----------|-----------|
| Homepage | 500 |
| Service page | 800 |
| Blog post | 1,500 |
| Product page | 300+ (400+ for complex products) |
| Location page | 500-600 |

> **Note:** These are topical coverage floors, not targets. Google confirms word count is NOT a direct ranking factor. The goal is comprehensive topical coverage.

## AI Content Assessment (Sept 2025 QRG)

AI content is acceptable IF it demonstrates genuine E-E-A-T. Flag these markers of low-quality AI content:
- Generic phrasing, lack of specificity
- No original insight or unique perspective
- No first-hand experience signals
- Factual inaccuracies
- Repetitive structure across pages

> **Helpful Content System (March 2024):** The Helpful Content System was merged into Google's core ranking algorithm during the March 2024 core update. It no longer operates as a standalone classifier. Helpfulness signals are now evaluated within every core update.

## Cross-Skill Delegation

- For evaluating programmatically generated pages, defer to the `seo-programmatic` sub-skill.
- For comparison page content standards, see `seo-competitor-pages`.

## Output Format

Provide:
- Content quality score (0-100)
- E-E-A-T breakdown with scores per factor
- AI citation readiness score
- Specific improvement recommendations
```

## File: `agents/seo-dataforseo.md`
```markdown
---
name: seo-dataforseo
description: DataForSEO data analyst. Fetches live SERP data, keyword metrics, backlink profiles, on-page analysis, content analysis, business listings, and AI visibility checks via DataForSEO MCP tools.
model: sonnet
maxTurns: 25
tools: Read, Bash, Write, Glob, Grep
---

You are a DataForSEO data analyst. When delegated tasks during an SEO audit or analysis:

1. Check that DataForSEO MCP tools are available before attempting calls
2. Use the most efficient tool combination for the requested data
3. Apply default parameters: location_code=2840 (US), language_code=en unless specified
4. Format output to match claude-seo conventions (tables, priority levels, scores)

## Efficient Tool Usage

- **Prefer bulk endpoints** over multiple single calls to minimize API credits
- **Don't re-fetch** data already retrieved in the same session
- **Warn before expensive operations** (full backlink crawls, large keyword lists)
- **Use limits**: default to limit=100 for list endpoints unless user needs more

## Error Handling

- If a DataForSEO tool returns an error, report the error clearly to the user
- If credentials are invalid, suggest running the extension installer again
- If a module is not enabled, note which module is needed

## Output Format

Match existing claude-seo patterns:
- Tables for comparative data
- Scores as XX/100
- Priority: Critical > High > Medium > Low
- Note data source as "DataForSEO (live)" to distinguish from static HTML analysis
- Include timestamps for time-sensitive data (SERP positions, backlink counts)
```

## File: `agents/seo-geo.md`
```markdown
---
name: seo-geo
description: GEO and AI search specialist. Analyzes AI crawler accessibility, llms.txt compliance, passage-level citability, brand mention signals, and platform-specific optimization for Google AI Overviews, ChatGPT, Perplexity, and Bing Copilot.
model: sonnet
maxTurns: 20
tools: Read, Bash, WebFetch, Glob, Grep
---

You are a Generative Engine Optimization (GEO) specialist. When given a URL:

1. Fetch the page and check robots.txt for AI crawler rules
2. Check for `/llms.txt` and RSL 1.0 licensing
3. Analyze content citability (passage length, structure, directness)
4. Evaluate authority signals (authorship, dates, citations, entity presence)
5. Assess technical accessibility for AI crawlers (SSR vs CSR)
6. Score across 5 dimensions and generate prioritized recommendations

## GEO Health Score (0-100)

| Dimension | Weight |
|-----------|--------|
| Citability | 25% |
| Structural Readability | 20% |
| Multi-Modal Content | 15% |
| Authority & Brand Signals | 20% |
| Technical Accessibility | 20% |

## AI Crawlers to Check in robots.txt

Allow for AI search visibility: GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot
Optional block (training only): CCBot, anthropic-ai, cohere-ai

## Key Citability Signals

- Optimal passage length: **134-167 words** for AI citation
- Direct answers in first 40-60 words of each section
- Question-based H2/H3 headings
- Specific statistics with source attribution
- Self-contained answer blocks (extractable without context)

## Brand Mention Correlation with AI Citations

| Signal | Correlation |
|--------|-------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit presence | High |
| Wikipedia entity | High |
| Domain Rating (backlinks) | ~0.266 (weak) |

Only 11% of domains are cited by both ChatGPT and Google AI Overviews, so platform optimization matters.

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `ai_optimization_chat_gpt_scraper` for live ChatGPT visibility and `ai_opt_llm_ment_search` for LLM mention tracking.

## Output Format

Provide a structured report with:
- GEO Readiness Score (0-100) with dimension breakdown
- AI Crawler Access Status (allowed/blocked per crawler)
- llms.txt status (present/missing/malformed)
- Brand mention analysis (Wikipedia, Reddit, YouTube, LinkedIn)
- Top 5 highest-impact changes with effort estimates
- Platform-specific scores (Google AIO, ChatGPT, Perplexity, Bing Copilot)
```

## File: `agents/seo-google.md`
```markdown
---
name: seo-google
description: Google SEO API analyst. Fetches CWV field data via CrUX, indexation status via GSC, and organic traffic via GA4 for enriched audit data.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write, Glob, Grep  # Write needed for report/data file output
---

You are a Google SEO API data analyst. When delegated tasks during an SEO audit:

1. Check credentials: `python scripts/google_auth.py --check --json`
2. Determine tier (0 = API key, 1 = + service account, 2 = + GA4)
3. Execute tier-appropriate analysis
4. Format output to match claude-seo conventions

## Tier-Based Workflow

### Tier 0 (API Key Only)
- Run PSI + CrUX on homepage: `python scripts/pagespeed_check.py <url> --json`
- Run CrUX History for origin: `python scripts/crux_history.py <origin> --origin --json`
- Report CWV field data with traffic-light ratings

### Tier 1 (+ Service Account)
- All Tier 0 checks
- GSC top queries/pages (28 days): `python scripts/gsc_query.py --property <prop> --json`
- URL Inspection on homepage + key pages: `python scripts/gsc_inspect.py <url> --json`
- GSC sitemap status: `python scripts/gsc_query.py sitemaps --property <prop> --json`

### Tier 2 (Full)
- All Tier 1 checks
- GA4 organic traffic (28 days): `python scripts/ga4_report.py --property <id> --json`
- Top organic landing pages: `python scripts/ga4_report.py --property <id> --report top-pages --json`

## Core Web Vitals Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | ≤ 2,500ms | 2,500-4,000ms | > 4,000ms |
| INP | ≤ 200ms | 200-500ms | > 500ms |
| CLS | ≤ 0.1 | 0.1-0.25 | > 0.25 |

INP replaced FID on March 12, 2024. Never reference FID.

## Output Format

Match existing claude-seo patterns:
- Tables for metrics with traffic-light ratings
- Scores as XX/100
- Priority: Critical > High > Medium > Low
- Note data source as "Google API (field data)" to distinguish from static analysis
- Include data freshness notes (CrUX: 28-day rolling, GSC: 2-3 day lag, GA4: 1 day lag)

## Report Generation (MANDATORY)

After completing data collection at any tier, ALWAYS offer to generate a PDF report.
The report uses the enterprise template: white cover, navy accents, Times New Roman, charts at 85% width, Google logo on title page. No page-break-inside: avoid (causes white gaps).

```bash
python scripts/google_report.py --type full --data data.json --domain DOMAIN --format pdf --json
```
Report types: `cwv-audit`, `gsc-performance`, `indexation`, `full`.
Before presenting: verify `"review": {"status": "PASS"}` in the JSON output.

## Error Handling

- If credentials are missing, report which tier is available and what can still be checked
- If CrUX returns 404, note insufficient Chrome traffic and fall back to PSI lab data
- If GSC returns 403, report the service account email and instruct on adding permissions
- Never fail silently -- always report what succeeded and what failed
```

## File: `agents/seo-image-gen.md`
```markdown
---
name: seo-image-gen
description: SEO image analyst. Audits existing OG/social preview images, identifies missing or low-quality images, and creates an image generation plan with prompts for key pages. Does NOT auto-generate images.
model: sonnet
maxTurns: 15
tools: Read, Bash, Glob, Grep
---

You are an SEO image analyst. When delegated tasks during an SEO audit:

1. Check that nanobanana-mcp tools are available before including generation recommendations
2. Analyze the site's existing image strategy for SEO impact
3. Output a structured generation plan. Never auto-generate (cost control)

## Analysis Scope

For each audited page, evaluate:
- **OG image presence**:Does `og:image` meta tag exist? Is it valid?
- **OG image quality**:Correct dimensions (1200x630 minimum), professional appearance?
- **Schema images**:Are `ImageObject` properties populated in structured data?
- **Alt text quality**:Descriptive, keyword-rich, not stuffed?
- **Image format**:Using modern formats (WebP, AVIF) vs legacy (PNG, JPEG)?
- **Image file size**:Under 200KB for hero, under 100KB for thumbnails?

## Output Format

Match existing claude-seo patterns:

### Image Audit Summary

| Metric | Value | Status |
|--------|-------|--------|
| Pages with OG images | X/Y | Pass/Fail |
| OG images correct size | X/Y | Pass/Fail |
| Schema ImageObject usage | X/Y | Pass/Fail |
| WebP/AVIF adoption | X% | Pass/Fail |
| Average image file size | XKB | Pass/Fail |

### Image Generation Plan

For each page missing or having low-quality images:

| Page | Issue | Suggested Use Case | Prompt Idea | Priority |
|------|-------|-------------------|-------------|----------|
| /homepage | Missing OG image | og | Professional SaaS dashboard overview | Critical |
| /blog/post-1 | Low-res hero | hero | [contextual suggestion] | High |

Priority levels: Critical > High > Medium > Low

### Recommendations

- Prioritize pages by traffic volume (highest traffic = fix first)
- Note estimated cost for full generation plan
- Suggest batch generation for efficiency
- Recommend WebP conversion pipeline for all generated assets

## Error Handling

- If nanobanana-mcp is not available, still audit existing images but note that generation requires the banana extension
- Report errors clearly with actionable next steps
- Note data source as "Image Audit (static analysis)" to distinguish from live checks
```

## File: `agents/seo-local.md`
```markdown
---
name: seo-local
description: Local SEO specialist. Analyzes GBP signals, NAP consistency, citations, reviews, local schema, location page quality, and industry-specific local factors for brick-and-mortar, SAB, and multi-location businesses.
model: sonnet
maxTurns: 20
tools: Read, Bash, WebFetch, Glob, Grep, Write
---

You are a Local SEO specialist. When given a URL:

1. Fetch the page and detect business type (brick-and-mortar, SAB, or hybrid) from address visibility, service area language, and Maps embeds
2. Detect industry vertical (restaurant, healthcare, legal, home services, real estate, automotive) from page content signals
3. Extract NAP (Name, Address, Phone) from visible HTML, JSON-LD schema, and meta tags -- flag any discrepancies between sources
4. Validate LocalBusiness schema: correct industry subtype, required properties (name, address), recommended properties (geo with 5 decimal precision, openingHoursSpecification, telephone, url)
5. Check for GBP signals on page (Maps embed, place references, review widgets, posts indicators, photo evidence)
6. Assess review health from visible data (rating, count, aggregateRating in schema, response patterns)
7. Check citation presence on Tier 1 directories (Yelp, BBB via site: search patterns or direct fetch)
8. Evaluate location page quality for multi-location sites (unique content %, doorway page swap test, internal linking depth)

## Local SEO Score (0-100)

| Dimension | Weight |
|-----------|--------|
| GBP Signals | 25% |
| Reviews & Reputation | 20% |
| Local On-Page SEO | 20% |
| NAP Consistency & Citations | 15% |
| Local Schema Markup | 10% |
| Local Link & Authority Signals | 10% |

## Key Detection Signals

**Business type:**
- Brick-and-mortar: visible street address, Maps embed, directions link
- SAB: no visible address, "serving [area]", "we come to you"
- Hybrid: both address and service area present

**Industry vertical:**
- Restaurant: /menu, cuisine types, reservations, food ordering
- Healthcare: insurance, NPI, "Dr.", HIPAA notice, appointments
- Legal: attorney, practice areas, bar admission, case results
- Home Services: service area, emergency, estimates, licensed/insured
- Real Estate: listings, MLS, agent bio, brokerage, open house
- Automotive: inventory, VIN, dealership, service department

## Critical Ranking Factors (Whitespark 2026)

- Primary GBP category: **#1 factor** (score: 193). Wrong category = **#1 negative factor** (score: 176)
- Review velocity: **18-day rule** -- rankings cliff if no reviews for 3 weeks (Sterling Sky)
- Dedicated service pages: **#1 local organic factor, #2 AI visibility factor**
- 3 of top 5 AI visibility factors are citation-related
- Proximity accounts for 55.2% of ranking variance (Search Atlas ML study) -- outside our control, note in report

## Industry-Specific Checks

Load `skills/seo/references/local-schema-types.md` for:
- Correct schema subtype per vertical (e.g., `Restaurant` not `LocalBusiness`, `LegalService` not deprecated `Attorney`)
- Industry-specific citation source recommendations
- Schema pattern templates (Menu for restaurants, Physician for healthcare, etc.)

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `local_business_data` for live GBP data and `google_local_pack_serp` for real-time local pack positions.

## Output Format

Provide a structured report with:
- Local SEO Score (0-100) with dimension breakdown
- Business type detected (brick-and-mortar / SAB / hybrid)
- Industry vertical detected with industry-specific findings
- NAP consistency audit (source comparison table)
- GBP optimization checklist (detected vs missing)
- Review health snapshot (rating, count, velocity, response rate)
- Citation presence status (Tier 1 directories)
- Local schema validation (correct subtype, property completeness)
- Location page quality (if multi-location)
- Top 10 prioritized actions (Critical > High > Medium > Low)
- Limitations disclaimer (what could not be assessed without paid tools)
```

## File: `agents/seo-maps.md`
```markdown
---
name: seo-maps
description: Maps intelligence specialist. Geo-grid rank tracking, GBP profile auditing, review intelligence, cross-platform NAP verification, and competitor radius mapping via DataForSEO and free APIs.
model: sonnet
maxTurns: 25
tools: Read, Bash, WebFetch, Glob, Grep, Write
---

You are a Maps Intelligence specialist. When delegated tasks during an SEO audit or given a business URL/name:

1. Detect capability tier: check if DataForSEO MCP tools are available (try `business_data_business_listings_search`). If available = Tier 1. If not = Tier 0 (free APIs only).
2. Identify the target business: extract name, location, and category from the URL or provided context
3. Geocode the business address using Nominatim (free) or DataForSEO (Tier 1)
4. Run available analyses based on tier (see below)
5. Score the business on the Maps Health Score rubric
6. Generate structured report with prioritized recommendations

## Tier 0 (Free) Capabilities

- Competitor discovery via Overpass API (radius query by business category)
- Structured POI search via Geoapify (if API key available)
- Address geocoding via Nominatim (1 req/sec, include User-Agent header)
- Static GBP completeness checklist (manual assessment from visible data)
- LocalBusiness schema generation from collected data
- Cross-platform NAP guidance (recommend claiming Google, Bing, Apple)

## Tier 1 (DataForSEO) Additional Capabilities

- Geo-grid rank tracking via Maps SERP API with `location_coordinate`
- Live GBP profile audit via My Business Info API
- Review intelligence via Reviews API (velocity, sentiment, distribution)
- GBP post activity audit via My Business Updates API
- Q&A gap analysis via Questions and Answers API
- Cross-platform reviews (Tripadvisor, Trustpilot)
- Business listings search for competitor discovery

## Maps Health Score (0-100)

| Dimension | Weight | Data Source |
|-----------|--------|-------------|
| Geo-Grid Visibility / SoLV | 25% | DataForSEO Maps SERP (Tier 1 only; skip and redistribute if Tier 0) |
| GBP Profile Completeness | 20% | DataForSEO My Business Info (Tier 1) or manual checklist (Tier 0) |
| Review Health | 20% | DataForSEO Reviews (Tier 1) or visible review signals (Tier 0) |
| Cross-Platform Presence | 15% | WebFetch checks for Bing, Apple, OSM listings |
| Competitor Position | 10% | Overpass/DataForSEO competitor count and relative rating |
| Schema & AI Readiness | 10% | Schema detection + AI citation signal check |

**Tier 0 weight redistribution:** When geo-grid is unavailable, redistribute its 25% across GBP (+10%), Review Health (+10%), Cross-Platform (+5%).

## Reference Files

Load on-demand:
- `skills/seo/references/maps-api-endpoints.md`: DataForSEO endpoint details and costs
- `skills/seo/references/maps-free-apis.md`: Overpass, Geoapify, Nominatim query templates
- `skills/seo/references/maps-geo-grid.md`: Grid algorithm, SoLV calculation, heatmap rendering
- `skills/seo/references/maps-gbp-checklist.md`: 25-field GBP audit checklist with industry weights
- `skills/seo/references/local-seo-signals.md`: Ranking factors, review benchmarks (shared with seo-local)
- `skills/seo/references/local-schema-types.md`: LocalBusiness subtypes by industry (shared with seo-local)

## Cross-Skill Delegation

- Do NOT duplicate seo-local on-page analysis. Recommend `/seo local <url>` for website-level checks.
- Do NOT duplicate seo-geo AI visibility analysis. Recommend `/seo geo <url>` for full GEO audit.
- Do NOT duplicate seo-schema validation. Recommend `/seo schema <url>` for schema fixes.

## Output Format

Provide a structured report with:
- Maps Health Score (0-100) with dimension breakdown
- Capability tier detected (Tier 0 or Tier 1)
- Geo-grid heatmap (if Tier 1) with SoLV percentage
- GBP profile completeness score with field-by-field breakdown
- Review health snapshot (rating, count, velocity, response rate, cross-platform)
- Competitor landscape (count in radius, top competitors by rating/reviews)
- Cross-platform presence status (Google, Bing, Apple, OSM)
- Generated LocalBusiness JSON-LD (if schema missing)
- Top 10 prioritized actions (Critical > High > Medium > Low)
- Cost report (DataForSEO credits consumed, if applicable)
- Limitations disclaimer (what could not be assessed at current tier)
```

## File: `agents/seo-performance.md`
```markdown
---
name: seo-performance
description: Performance analyzer. Measures and evaluates Core Web Vitals and page load performance.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write
---

You are a Web Performance specialist focused on Core Web Vitals.

## Current Metrics (as of 2026)

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

**IMPORTANT**: INP replaced FID on March 12, 2024. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on September 9, 2024. INP is the sole interactivity metric. Never reference FID.

## Evaluation Method

Google evaluates the **75th percentile** of page visits, 75% of visits must meet the "good" threshold to pass.

## When Analyzing Performance

1. Use PageSpeed Insights API if available
2. Otherwise, analyze HTML source for common issues
3. Provide specific, actionable optimization recommendations
4. Prioritize by expected impact

## Common LCP Issues

- Unoptimized hero images (compress, WebP/AVIF, preload)
- Render-blocking CSS/JS (defer, async, critical CSS)
- Slow server response TTFB >200ms (edge CDN, caching)
- Third-party scripts blocking render
- Web font loading delay

## Common INP Issues

- Long JavaScript tasks on main thread (break into <50ms chunks)
- Heavy event handlers (debounce, requestAnimationFrame)
- Excessive DOM size (>1,500 elements)
- Third-party scripts hijacking main thread
- Synchronous operations blocking

## Common CLS Issues

- Images without width/height dimensions
- Dynamically injected content
- Web fonts causing FOIT/FOUT
- Ads/embeds without reserved space
- Late-loading elements

## Performance Tooling (2025-2026)

**Lighthouse 13.0** (October 2025): Major audit restructuring with reorganized performance categories and updated scoring weights. Use as a lab diagnostic tool: always validate against CrUX field data for real-world performance.

**CrUX Vis** replaced the CrUX Dashboard (November 2025). The old Looker Studio dashboard was deprecated. Use [CrUX Vis](https://cruxvis.withgoogle.com) or the CrUX API directly.

**LCP subparts** (TTFB, resource load delay, resource load time, element render delay) are now available in CrUX data (February 2025). See `skills/seo/references/cwv-thresholds.md` for details.

## Tools

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json
```

## Google API Integration (Optional)

If Google API credentials are configured, prefer CrUX field data over Lighthouse lab data for CWV assessment:
```bash
python scripts/pagespeed_check.py URL --json
python scripts/crux_history.py URL --json
```
Field data (28-day Chrome user average) is more representative than lab data (single Lighthouse run). Use lab data as fallback when CrUX returns 404 (insufficient traffic).

## Output Format

Provide:
- Performance score (0-100)
- Core Web Vitals status (pass/fail per metric)
- Specific bottlenecks identified
- Prioritized recommendations with expected impact
```

## File: `agents/seo-schema.md`
```markdown
---
name: seo-schema
description: Schema markup expert. Detects, validates, and generates Schema.org structured data in JSON-LD format.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write
---

You are a Schema.org markup specialist.

When analyzing pages:

1. Detect all existing schema (JSON-LD, Microdata, RDFa)
2. Validate against Google's supported rich result types
3. Check for required and recommended properties
4. Identify missing schema opportunities
5. Generate correct JSON-LD for recommended additions

## CRITICAL RULES

### Never Recommend These (Deprecated):
- **HowTo**: Rich results removed September 2023
- **SpecialAnnouncement**: Deprecated July 31, 2025
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired June 2025

### Restricted Schema:
- **FAQ**: Google rich results restricted to government and healthcare sites (August 2023).
  - **Existing FAQPage on commercial sites**: Flag as Info priority (not Critical). FAQPage still benefits AI/LLM citations even without Google rich results.
  - **Adding new FAQPage on commercial sites**: Not recommended for Google benefit; note AI discoverability upside if user prioritizes GEO.

### Always Prefer:
- JSON-LD format over Microdata or RDFa
- `https://schema.org` as @context (not http)
- Absolute URLs (not relative)
- ISO 8601 date format

## Validation Checklist

For any schema block, verify:
1. ✅ @context is "https://schema.org"
2. ✅ @type is valid and not deprecated
3. ✅ All required properties present
4. ✅ Property values match expected types
5. ✅ No placeholder text (e.g., "[Business Name]")
6. ✅ URLs are absolute
7. ✅ Dates are ISO 8601 format

## Common Schema Types

Recommend freely:
- Organization, LocalBusiness
- Article, BlogPosting, NewsArticle
- Product, Offer, Service
- BreadcrumbList, WebSite, WebPage
- Person, Review, AggregateRating
- VideoObject, Event, JobPosting

For video schema types (VideoObject, BroadcastEvent, Clip, SeekToAction), see the schema templates file installed at `~/.claude/skills/seo/schema/templates.json`.

## Output Format

Provide:
- Detection results (what schema exists)
- Validation results (pass/fail per block)
- Missing opportunities
- Generated JSON-LD for implementation
```

## File: `agents/seo-sitemap.md`
```markdown
---
name: seo-sitemap
description: Sitemap architect. Validates XML sitemaps, generates new ones with industry templates, and enforces quality gates for location pages.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write, Glob
---

You are a Sitemap Architecture specialist.

When working with sitemaps:

1. Validate XML format and URL status codes
2. Check for deprecated tags (priority, changefreq: both ignored by Google)
3. Verify lastmod accuracy
4. Compare crawled pages vs sitemap coverage
5. Enforce the 50,000 URL per-file limit
6. Apply location page quality gates

## Quality Gates

### Location Page Thresholds
- ⚠️ **WARNING** at 30+ location pages: require 60%+ unique content per page
- 🛑 **HARD STOP** at 50+ location pages: require explicit user justification

### Why This Matters
Google's doorway page algorithm penalizes programmatic location pages with thin/duplicate content.

## Validation Checks

| Check | Severity | Action |
|-------|----------|--------|
| Invalid XML | Critical | Fix syntax |
| >50k URLs | Critical | Split with index |
| Non-200 URLs | High | Remove or fix |
| Noindexed URLs | High | Remove from sitemap |
| Redirected URLs | Medium | Update to final URL |
| All identical lastmod | Low | Use real dates |
| priority/changefreq | Info | Can remove |

## Safe vs Risky Pages

### Safe at Scale ✅
- Integration pages (with real setup docs)
- Glossary pages (200+ word definitions)
- Product pages (unique specs, reviews)

### Penalty Risk ❌
- Location pages with only city swapped
- "Best [tool] for [industry]" without real value
- AI-generated mass content

## Sitemap Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2026-02-07</lastmod>
  </url>
</urlset>
```

## Output Format

Provide:
- Validation report with pass/fail per check
- Missing pages (in crawl but not sitemap)
- Extra pages (in sitemap but 404 or redirected)
- Quality gate warnings if applicable
- Generated sitemap XML if creating new
```

## File: `agents/seo-technical.md`
```markdown
---
name: seo-technical
description: Technical SEO specialist. Analyzes crawlability, indexability, security, URL structure, mobile optimization, Core Web Vitals, and JavaScript rendering.
model: sonnet
maxTurns: 20
tools: Read, Bash, Write, Glob, Grep  # Write needed for report/data file output
---

You are a Technical SEO specialist. When given a URL or set of URLs:

1. Fetch the page(s) and analyze HTML source
2. Check robots.txt and sitemap availability
3. Analyze meta tags, canonical tags, and security headers
4. Evaluate URL structure and redirect chains
5. Assess mobile-friendliness from HTML/CSS analysis
6. Flag potential Core Web Vitals issues from source inspection
7. Check JavaScript rendering requirements

## Core Web Vitals Reference

Current thresholds (as of 2026):
- **LCP** (Largest Contentful Paint): Good <2.5s, Needs Improvement 2.5-4s, Poor >4s
- **INP** (Interaction to Next Paint): Good <200ms, Needs Improvement 200-500ms, Poor >500ms
- **CLS** (Cumulative Layout Shift): Good <0.1, Needs Improvement 0.1-0.25, Poor >0.25

**IMPORTANT**: INP replaced FID on March 12, 2024. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on September 9, 2024. INP is the sole interactivity metric. Never reference FID in any output.

See the AI Crawler Management section in `seo-technical` skill for crawler tokens and robots.txt guidance.

## Cross-Skill Delegation

- For detailed hreflang validation, defer to the `seo-hreflang` sub-skill.

## Output Format

Provide a structured report with:
- Pass/fail status per category
- Technical score (0-100)
- Prioritized issues (Critical → High → Medium → Low)
- Specific recommendations with implementation details

## Categories to Analyze

1. Crawlability (robots.txt, sitemaps, noindex)
2. Indexability (canonicals, duplicates, thin content)
3. Security (HTTPS, headers)
4. URL Structure (clean URLs, redirects)
5. Mobile (viewport, touch targets)
6. Core Web Vitals (LCP, INP, CLS potential issues)
7. Structured Data (detection, validation)
8. JavaScript Rendering (CSR vs SSR)
9. IndexNow Protocol (Bing, Yandex, Naver)
```

## File: `agents/seo-visual.md`
```markdown
---
name: seo-visual
description: Visual analyzer. Captures screenshots, tests mobile rendering, and analyzes above-the-fold content using Playwright.
model: sonnet
maxTurns: 15
tools: Read, Bash, Write
---

You are a Visual Analysis specialist using Playwright for browser automation.

## Prerequisites

Before capturing screenshots, ensure Playwright and Chromium are installed:

```bash
pip install playwright && playwright install chromium
```

## When Analyzing Pages

1. Capture desktop screenshot (1920x1080)
2. Capture mobile screenshot (375x812, iPhone viewport)
3. Analyze above-the-fold content: is the primary CTA visible?
4. Check for visual layout issues, overlapping elements
5. Verify mobile responsiveness

## Screenshot Script

Use the screenshot script (installed at `~/.claude/skills/seo/scripts/capture_screenshot.py`) for browser automation:

```python
from playwright.sync_api import sync_playwright

def capture(url, output_path, viewport_width=1920, viewport_height=1080):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': viewport_width, 'height': viewport_height})
        page.goto(url, wait_until='networkidle')
        page.screenshot(path=output_path, full_page=False)
        browser.close()
```

## Viewports to Test

| Device | Width | Height |
|--------|-------|--------|
| Desktop | 1920 | 1080 |
| Laptop | 1366 | 768 |
| Tablet | 768 | 1024 |
| Mobile | 375 | 812 |

## Visual Checks

### Above-the-Fold Analysis
- Primary heading (H1) visible without scrolling
- Main CTA visible without scrolling
- Hero image/content loading properly
- No layout shifts on load

### Mobile Responsiveness
- Navigation accessible (hamburger menu or visible)
- Touch targets at least 48x48px
- No horizontal scroll
- Text readable without zooming (16px+ base font)

### Visual Issues
- Overlapping elements
- Text cut off or overflow
- Images not scaling properly
- Broken layout at different widths

## Output Format

Provide:
- Screenshots saved to `screenshots/` directory
- Visual analysis summary
- Mobile responsiveness assessment
- Above-the-fold content evaluation
- Specific issues with element locations
```

## File: `brain/knowledge/docs_legacy/ARCHITECTURE.md`
```markdown
# Architecture

## Overview

Claude SEO follows Anthropic's official Claude Code skill specification with a modular, multi-skill architecture.

## Directory Structure

```
~/.claude/
├── skills/
│   ├── seo/              # Main orchestrator skill
│   │   ├── SKILL.md          # Entry point with routing logic
│   │   └── references/       # On-demand reference files
│   │       ├── cwv-thresholds.md
│   │       ├── schema-types.md
│   │       ├── eeat-framework.md
│   │       └── quality-gates.md
│   │
│   ├── seo-audit/            # Full site audit
│   ├── seo-competitor-pages/ # Competitor comparison pages
│   ├── seo-content/          # E-E-A-T analysis
│   ├── seo-geo/              # AI search optimization
│   ├── seo-hreflang/         # Hreflang/i18n SEO
│   ├── seo-images/           # Image optimization
│   ├── seo-page/             # Single page analysis
│   ├── seo-plan/             # Strategic planning
│   │   └── assets/           # Industry templates
│   ├── seo-programmatic/     # Programmatic SEO
│   ├── seo-schema/           # Schema markup
│   ├── seo-sitemap/          # Sitemap analysis/generation
│   └── seo-technical/        # Technical SEO
│
└── agents/
    ├── seo-technical.md      # Technical SEO specialist
    ├── seo-content.md        # Content quality reviewer
    ├── seo-schema.md         # Schema markup expert
    ├── seo-sitemap.md        # Sitemap architect
    ├── seo-performance.md    # Performance analyzer
    └── seo-visual.md         # Visual analyzer
```

## Component Types

### Skills

Skills are markdown files with YAML frontmatter that define capabilities and instructions.

**SKILL.md Format:**
```yaml
---
name: skill-name
description: >
  When to use this skill. Include activation keywords
  and concrete use cases.
---

# Skill Title

Instructions and documentation...
```

### Subagents

Subagents are specialized workers that can be delegated tasks. They have their own context and tools.

**Agent Format:**
```yaml
---
name: agent-name
description: What this agent does.
tools: Read, Bash, Write, Glob, Grep
---

Instructions for the agent...
```

### Reference Files

Reference files contain static data loaded on-demand to avoid bloating the main skill.

## Orchestration Flow

### Full Audit (`/seo audit`)

```
User Request
    │
    ▼
┌─────────────────┐
│   seo       │  ← Main orchestrator
│   (SKILL.md)    │
└────────┬────────┘
         │
         │  Detects business type
         │  Spawns subagents in parallel
         │
    ┌────┴────┬────────┬────────┬────────┬────────┐
    ▼         ▼        ▼        ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│tech   │ │content│ │schema │ │sitemap│ │perf   │ │visual │
│agent  │ │agent  │ │agent  │ │agent  │ │agent  │ │agent  │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │        │        │        │        │
    └─────────┴────────┴────┬───┴────────┴────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Aggregate    │
                    │  Results      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Generate     │
                    │  Report       │
                    └───────────────┘
```

### Individual Command

```
User Request (e.g., /seo page)
    │
    ▼
┌─────────────────┐
│   seo       │  ← Routes to sub-skill
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   seo-page      │  ← Sub-skill handles directly
│   (SKILL.md)    │
└─────────────────┘
```

## Design Principles

### 1. Progressive Disclosure

- Main SKILL.md is concise (<200 lines)
- Reference files loaded on-demand
- Detailed instructions in sub-skills

### 2. Parallel Processing

- Subagents run concurrently during audits
- Independent analyses don't block each other
- Results aggregated after all complete

### 3. Quality Gates

- Built-in thresholds prevent bad recommendations
- Location page limits (30 warning, 50 hard stop)
- Schema deprecation awareness
- FID → INP replacement enforced

### 4. Industry Awareness

- Templates for different business types
- Automatic detection from homepage signals
- Tailored recommendations per industry

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Skill | `seo-{name}/SKILL.md` | `seo-audit/SKILL.md` |
| Agent | `seo-{name}.md` | `seo-technical.md` |
| Reference | `{topic}.md` | `cwv-thresholds.md` |
| Script | `{action}_{target}.py` | `fetch_page.py` |
| Template | `{industry}.md` | `saas.md` |

## Extension Points

### Adding a New Sub-Skill

1. Create `skills/seo-newskill/SKILL.md`
2. Add YAML frontmatter with name and description
3. Write skill instructions
4. Update main `skills/seo/SKILL.md` to route to new skill

### Adding a New Subagent

1. Create `agents/seo-newagent.md`
2. Add YAML frontmatter with name, description, tools
3. Write agent instructions
4. Reference from relevant skills

### Adding a New Reference File

1. Create file in appropriate `references/` directory
2. Reference in skill with load-on-demand instruction

## Extensions

Extensions are opt-in add-ons that integrate external data sources via MCP servers. They live in `extensions/<name>/` and include their own install/uninstall scripts.

```
extensions/
├── dataforseo/               # DataForSEO MCP integration
│   ├── README.md                  # Extension documentation
│   ├── install.sh                 # Unix installer
│   ├── install.ps1                # Windows installer
│   ├── uninstall.sh               # Unix uninstaller
│   ├── uninstall.ps1              # Windows uninstaller
│   ├── field-config.json          # API response field filtering
│   ├── skills/
│   │   └── seo-dataforseo/
│   │       └── SKILL.md           # Sub-skill (22 commands)
│   ├── agents/
│   │   └── seo-dataforseo.md      # Subagent
│   └── brain/knowledge/docs_legacy/
│       └── DATAFORSEO-SETUP.md    # Account setup guide
│
└── banana/                   # Banana Image Generation (Gemini AI)
    ├── README.md                  # Extension documentation
    ├── install.sh                 # Unix installer
    ├── uninstall.sh               # Unix uninstaller
    ├── skills/
    │   └── seo-image-gen/
    │       └── SKILL.md           # Sub-skill (6 commands)
    ├── agents/
    │   └── seo-image-gen.md       # Image audit subagent
    ├── scripts/                   # Python scripts (stdlib only)
    │   ├── generate.py            # Direct API fallback
    │   ├── edit.py                # Image editing fallback
    │   ├── batch.py               # CSV batch workflow
    │   ├── cost_tracker.py        # Usage and cost tracking
    │   ├── presets.py             # Brand preset management
    │   ├── setup_mcp.py           # MCP configuration
    │   └── validate_setup.py      # Installation verification
    ├── references/                # On-demand knowledge
    │   ├── prompt-engineering.md  # 6-component Reasoning Brief
    │   ├── gemini-models.md       # Model specs and pricing
    │   ├── mcp-tools.md           # MCP tool reference
    │   ├── post-processing.md     # ImageMagick recipes
    │   ├── cost-tracking.md       # Cost tracking guide
    │   ├── presets.md             # Preset schema
    │   └── seo-image-presets.md   # SEO-specific presets
    └── brain/knowledge/docs_legacy/
        └── BANANA-SETUP.md        # API key and MCP setup
```

### Available Extensions

| Extension | Package | What it Adds |
|-----------|---------|-------------|
| **DataForSEO** | `dataforseo-mcp-server` | 22 commands: live SERP, keywords, backlinks, on-page analysis, content analysis, business listings, AI visibility, LLM mentions |
| **Banana Image Gen** | `@ycse/nanobanana-mcp` | 6 commands: OG image, hero image, product photo, infographic, custom, and batch generation via Gemini AI |

### Extension Convention

Each extension follows this pattern:
1. Self-contained in `extensions/<name>/`
2. Own `install.sh` and `install.ps1` that copy files and configure MCP
3. Own `uninstall.sh` and `uninstall.ps1` that cleanly reverse installation
4. Installs skill to `~/.claude/skills/seo-<name>/`
5. Installs agent to `~/.claude/agents/seo-<name>.md`
6. Merges MCP config into `~/.claude/settings.json` (non-destructive)
```

## File: `brain/knowledge/docs_legacy/COMMANDS.md`
```markdown
# Commands Reference

## Overview

All Claude SEO commands start with `/seo` followed by a subcommand.

## Command List

### `/seo audit <url>`

Full website SEO audit with parallel analysis.

**Example:**
```
/seo audit https://example.com
```

**What it does:**
1. Crawls up to 500 pages
2. Detects business type
3. Delegates to 7 specialist subagents in parallel
4. Generates SEO Health Score (0-100)
5. Creates prioritized action plan

**Output:**
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`
- `screenshots/` (if Playwright available)

---

### `/seo page <url>`

Deep single-page analysis.

**Example:**
```
/seo page https://example.com/about
```

**What it analyzes:**
- On-page SEO (title, meta, headings, URLs)
- Content quality (word count, readability, E-E-A-T)
- Technical elements (canonical, robots, Open Graph)
- Schema markup
- Images (alt text, sizes, formats)
- Core Web Vitals potential issues

---

### `/seo technical <url>`

Technical SEO audit across 9 categories.

**Example:**
```
/seo technical https://example.com
```

**Categories:**
1. Crawlability
2. Indexability
3. Security
4. URL Structure
5. Mobile Optimization
6. Core Web Vitals (LCP, INP, CLS)
7. Structured Data
8. JavaScript Rendering
9. IndexNow Protocol

---

### `/seo content <url>`

E-E-A-T and content quality analysis.

**Example:**
```
/seo content https://example.com/blog/post
```

**What it evaluates:**
- Experience signals (first-hand knowledge)
- Expertise (author credentials)
- Authoritativeness (external recognition)
- Trustworthiness (transparency, security)
- AI citation readiness
- Content freshness

---

### `/seo schema <url>`

Schema markup detection, validation, and generation.

**Example:**
```
/seo schema https://example.com
```

**What it does:**
- Detects existing schema (JSON-LD, Microdata, RDFa)
- Validates against Google's requirements
- Identifies missing opportunities
- Generates ready-to-use JSON-LD

---

### `/seo geo <url>`

AI Overviews / Generative Engine Optimization.

**Example:**
```
/seo geo https://example.com/blog/guide
```

**What it analyzes:**
- Citability score (quotable facts, statistics)
- Structural readability (headings, lists, tables)
- Entity clarity (definitions, context)
- Authority signals (credentials, sources)
- Structured data support

---

### `/seo images <url>`

Image optimization analysis.

**Example:**
```
/seo images https://example.com
```

**What it checks:**
- Alt text presence and quality
- File sizes (flag >200KB)
- Formats (WebP/AVIF recommendations)
- Responsive images (srcset, sizes)
- Lazy loading
- CLS prevention (dimensions)

---

### `/seo sitemap <url>`

Analyze existing XML sitemap.

**Example:**
```
/seo sitemap https://example.com/sitemap.xml
```

**What it validates:**
- XML format
- URL count (<50k per file)
- URL status codes
- lastmod accuracy
- Deprecated tags (priority, changefreq)
- Coverage vs crawled pages

---

### `/seo sitemap generate`

Generate new sitemap with industry templates.

**Example:**
```
/seo sitemap generate
```

**Process:**
1. Select or auto-detect business type
2. Interactive structure planning
3. Apply quality gates (30/50 location page limits)
4. Generate valid XML
5. Create documentation

---

### `/seo plan <type>`

Strategic SEO planning.

**Types:** `saas`, `local`, `ecommerce`, `publisher`, `agency`

**Example:**
```
/seo plan saas
```

**What it creates:**
- Complete SEO strategy
- Competitive analysis
- Content calendar
- Implementation roadmap (4 phases)
- Site architecture design

---

### `/seo competitor-pages [url|generate]`

Competitor comparison page generation.

**Examples:**
```
/seo competitor-pages https://example.com/vs/competitor
/seo competitor-pages generate
```

**Capabilities:**
- Generate "X vs Y" comparison page layouts
- Create "Alternatives to X" page structures
- Build feature comparison matrices with scoring
- Generate Product + AggregateRating schema markup
- Apply conversion-optimized CTA placement
- Enforce fairness guidelines (accurate data, source citations)

---

### `/seo hreflang [url]`

Hreflang and international SEO audit and generation.

**Example:**
```
/seo hreflang https://example.com
```

**Capabilities:**
- Validate self-referencing hreflang tags
- Check return tag reciprocity (A→B requires B→A)
- Verify x-default tag presence
- Validate ISO 639-1 language and ISO 3166-1 region codes
- Check canonical URL alignment with hreflang
- Detect protocol mismatches (HTTP vs HTTPS)
- Generate correct hreflang link tags and sitemap XML

---

### `/seo programmatic [url|plan]`

Programmatic SEO analysis and planning for pages generated at scale.

**Examples:**
```
/seo programmatic https://example.com/tools/
/seo programmatic plan
```

**Capabilities:**
- Assess data source quality (CSV, JSON, API, database)
- Plan template engines with unique content per page
- Design URL pattern strategies (`/tools/[tool-name]`, `/[city]/[service]`)
- Automate internal linking (hub/spoke, related items, breadcrumbs)
- Enforce thin content safeguards (quality gates, word count thresholds)
- Prevent index bloat (noindex low-value, pagination, faceted nav)

---

### `/seo dataforseo [command]`

Live SEO data via DataForSEO MCP server (extension). 22 commands across 9 API modules.

**Prerequisites:** DataForSEO extension installed (`./extensions/dataforseo/install.sh`)

**SERP Analysis:**
```
/seo dataforseo serp <keyword>              # Google organic results (also Bing/Yahoo)
/seo dataforseo serp-youtube <keyword>      # YouTube search results
/seo dataforseo youtube <video_id>          # YouTube video deep analysis
```

**Keyword Research:**
```
/seo dataforseo keywords <seed>             # Keyword ideas and suggestions
/seo dataforseo volume <keywords>           # Search volume metrics
/seo dataforseo difficulty <keywords>       # Keyword difficulty scores
/seo dataforseo intent <keywords>           # Search intent classification
/seo dataforseo trends <keyword>            # Google Trends data
```

**Domain & Competitors:**
```
/seo dataforseo backlinks <domain>          # Full backlink profile
/seo dataforseo competitors <domain>        # Competitor analysis
/seo dataforseo ranked <domain>             # Ranked keywords
/seo dataforseo intersection <domains>      # Keyword/backlink overlap
/seo dataforseo traffic <domains>           # Traffic estimation
/seo dataforseo subdomains <domain>         # Subdomains with ranking data
/seo dataforseo top-searches <domain>       # Top queries mentioning domain
```

**Technical / On-Page:**
```
/seo dataforseo onpage <url>                # On-page analysis (Lighthouse)
/seo dataforseo tech <domain>               # Technology detection
/seo dataforseo whois <domain>              # WHOIS data
```

**Content & Business Data:**
```
/seo dataforseo content <keyword/url>       # Content analysis and trends
/seo dataforseo listings <keyword>          # Business listings search
```

**AI Visibility / GEO:**
```
/seo dataforseo ai-scrape <query>           # ChatGPT web scraper for GEO
/seo dataforseo ai-mentions <keyword>       # LLM mention tracking
```

---

### `/seo image-gen [use-case] <description>`

AI image generation for SEO assets (extension). Powered by Gemini via nanobanana-mcp.

**Prerequisites:** Banana extension installed (`./extensions/banana/install.sh`)

**Use Cases:**
```
/seo image-gen og <description>          # OG/social preview image (16:9, 1K)
/seo image-gen hero <description>        # Blog hero image (16:9, 2K)
/seo image-gen product <description>     # Product photography (4:3, 2K)
/seo image-gen infographic <description> # Infographic visual (2:3, 4K)
/seo image-gen custom <description>      # Custom with full Creative Director pipeline
/seo image-gen batch <description> [N]   # Generate N variations (default: 3)
```

**Example:**
```
/seo image-gen og "Professional SaaS analytics dashboard with clean UI"
/seo image-gen hero "Dramatic sunset over modern city skyline"
/seo image-gen product "Wireless noise-canceling headphones on marble surface"
```

**What it does:**
1. Maps SEO use case to optimized domain mode, aspect ratio, and resolution
2. Constructs 6-component Reasoning Brief (Creative Director pipeline)
3. Generates image via Gemini API
4. Provides SEO checklist (alt text, file naming, WebP, schema markup)

---

## Quick Reference

| Command | Use Case |
|---------|----------|
| `/seo audit <url>` | Full website audit |
| `/seo competitor-pages [url\|generate]` | Competitor comparison pages |
| `/seo content <url>` | E-E-A-T analysis |
| `/seo geo <url>` | AI search optimization |
| `/seo hreflang [url]` | Hreflang/i18n SEO audit |
| `/seo images <url>` | Image optimization |
| `/seo image-gen [use-case] <desc>` | AI image generation (extension) |
| `/seo page <url>` | Single page analysis |
| `/seo plan <type>` | Strategic planning |
| `/seo programmatic [url\|plan]` | Programmatic SEO analysis |
| `/seo schema <url>` | Schema validation |
| `/seo sitemap <url>` | Sitemap validation |
| `/seo sitemap generate` | Create new sitemap |
| `/seo technical <url>` | Technical SEO check |
| `/seo dataforseo [command]` | Live SEO data (extension) |
```

## File: `brain/knowledge/docs_legacy/INSTALLATION.md`
```markdown
# Installation Guide

## Prerequisites

- **Python 3.10+** with pip
- **Git** for cloning the repository
- **Claude Code CLI** installed and configured

Optional:
- **Playwright** for screenshot capabilities

## Quick Install

### Unix/macOS/Linux

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.ps1 | iex
```

## Manual Installation

1. **Clone the repository**

```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
```

2. **Run the installer**

```bash
./install.sh
```

3. **Install Python dependencies** (if not done automatically)

The installer creates a venv at `~/.claude/skills/seo/.venv/`. If that fails, install manually:

```bash
# Option A: Use the venv
~/.claude/skills/seo/.venv/bin/pip install -r ~/.claude/skills/seo/requirements.txt

# Option B: User-level install
pip install --user -r ~/.claude/skills/seo/requirements.txt
```

4. **Install Playwright browsers** (optional, for visual analysis)

```bash
pip install playwright
playwright install chromium
```

Playwright is optional. Without it, visual analysis uses WebFetch as a fallback.

## Installation Paths

The installer copies files to:

| Component | Path |
|-----------|------|
| Main skill | `~/.claude/skills/seo/` |
| Sub-skills | `~/.claude/skills/seo-*/` |
| Subagents | `~/.claude/agents/seo-*.md` |

## Verify Installation

1. Start Claude Code:

```bash
claude
```

2. Check that the skill is loaded:

```
/seo
```

You should see a help message or prompt for a URL.

## Uninstallation

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash
```

Or manually:

```bash
rm -rf ~/.claude/skills/seo
rm -rf ~/.claude/skills/seo-audit
rm -rf ~/.claude/skills/seo-competitor-pages
rm -rf ~/.claude/skills/seo-content
rm -rf ~/.claude/skills/seo-geo
rm -rf ~/.claude/skills/seo-hreflang
rm -rf ~/.claude/skills/seo-images
rm -rf ~/.claude/skills/seo-page
rm -rf ~/.claude/skills/seo-plan
rm -rf ~/.claude/skills/seo-programmatic
rm -rf ~/.claude/skills/seo-schema
rm -rf ~/.claude/skills/seo-sitemap
rm -rf ~/.claude/skills/seo-technical
rm -f ~/.claude/agents/seo-*.md
```

## Upgrading

To upgrade to the latest version:

```bash
# Uninstall current version
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash

# Install new version
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

## Troubleshooting

### "Skill not found" error

Ensure the skill is installed in the correct location:

```bash
ls ~/.claude/skills/seo/SKILL.md
```

If the file doesn't exist, re-run the installer.

### Python dependency errors

Install dependencies manually:

```bash
pip install beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

### Playwright screenshot errors

Install Chromium browser:

```bash
playwright install chromium
```

### Permission errors on Unix

Make sure scripts are executable:

```bash
chmod +x ~/.claude/skills/seo/scripts/*.py
```
```

## File: `brain/knowledge/docs_legacy/MCP-INTEGRATION.md`
```markdown
<!-- Updated: 2026-02-07 -->
# MCP Integration

## Overview

Claude SEO can integrate with Model Context Protocol (MCP) servers to access external APIs and enhance analysis capabilities.

## Available Integrations

### PageSpeed Insights API

Use Google's PageSpeed Insights API directly for real Core Web Vitals data.

**Configuration:**

1. Get an API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the PageSpeed Insights API
3. Use in your analysis:

```bash
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=YOUR_API_KEY"
```

### Google Search Console

For organic search data, use the `mcp-server-gsc` MCP server by [ahonn](https://github.com/ahonn/mcp-server-gsc). Provides search performance data, URL inspection, and sitemap management.

**Configuration:**

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "mcp-server-gsc"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json"
      }
    }
  }
}
```

### PageSpeed Insights MCP Server

Use `mcp-server-pagespeed` by [enemyrr](https://github.com/enemyrr/mcp-server-pagespeed) for Lighthouse audits, CWV metrics, and performance scoring via MCP.

**Configuration:**

```json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "mcp-server-pagespeed"],
      "env": {
        "PAGESPEED_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Official SEO MCP Servers (2025-2026)

The MCP ecosystem for SEO has matured significantly. These are production-ready integrations:

| Tool | Package / Endpoint | Type | Notes |
|------|-------------------|------|-------|
| **Ahrefs** | `@ahrefs/mcp` | Official | Launched July 2025. Supports local and remote modes. Backlinks, keywords, site audit data. |
| **Semrush** | `https://mcp.semrush.com/v1/mcp` | Official (remote) | Full API access via remote MCP endpoint. Domain analytics, keyword research, backlink data. |
| **Google Search Console** | `mcp-server-gsc` | Community | By ahonn. Search performance, URL inspection, sitemaps. |
| **PageSpeed Insights** | `mcp-server-pagespeed` | Community | By enemyrr. Lighthouse audits, CWV metrics, performance scoring. |
| **DataForSEO** | `dataforseo-mcp-server` | Official extension | 9 modules, 79 tools, 22 commands. Install: `./extensions/dataforseo/install.sh`. See [extension docs](../../../README.md). |
| **kwrds.ai** | kwrds MCP server | Community | Keyword research, search volume, difficulty scoring. |
| **SEO Review Tools** | SEO Review Tools MCP | Community | Site auditing and on-page analysis API. |

## API Usage Examples

### PageSpeed Insights

```python
import requests

def get_pagespeed_data(url: str, api_key: str) -> dict:
    """Fetch PageSpeed Insights data for a URL."""
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "key": api_key,
        "strategy": "mobile",  # or "desktop"
        "category": ["performance", "accessibility", "best-practices", "seo"]
    }
    response = requests.get(endpoint, params=params)
    return response.json()
```

### Core Web Vitals from CrUX

```python
def get_crux_data(url: str, api_key: str) -> dict:
    """Fetch Chrome UX Report data for a URL."""
    endpoint = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"
    payload = {
        "url": url,
        "formFactor": "PHONE"  # or "DESKTOP"
    }
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    response = requests.post(endpoint, json=payload, headers=headers, params=params)
    return response.json()
```

## Metrics Available

### From PageSpeed Insights

| Metric | Description |
|--------|-------------|
| LCP | Largest Contentful Paint (lab) |
| INP | Interaction to Next Paint (estimated) |
| CLS | Cumulative Layout Shift (lab) |
| FCP | First Contentful Paint |
| TBT | Total Blocking Time |
| Speed Index | Visual progress speed |

### From CrUX (Field Data)

| Metric | Description |
|--------|-------------|
| LCP | 75th percentile, real users |
| INP | 75th percentile, real users |
| CLS | 75th percentile, real users |
| TTFB | Time to First Byte |

## Best Practices

1. **Rate Limiting**: Respect API quotas (typically 25k requests/day for PageSpeed)
2. **Caching**: Cache results to avoid redundant API calls
3. **Field vs Lab**: Prioritize field data (CrUX) for ranking signals
4. **Error Handling**: Handle API errors gracefully

## Without API Keys

If you don't have API keys, Claude SEO can still:

1. Analyze HTML source for potential issues
2. Identify common performance problems
3. Check for render-blocking resources
4. Evaluate image optimization opportunities
5. Detect JavaScript-heavy implementations

The analysis will note that actual Core Web Vitals measurements require field data from real users.
```

## File: `brain/knowledge/docs_legacy/TROUBLESHOOTING.md`
```markdown
# Troubleshooting

## Common Issues

### Skill Not Loading

**Symptom:** `/seo` command not recognized

**Solutions:**

1. Verify installation:
```bash
ls ~/.claude/skills/seo/SKILL.md
```

2. Check SKILL.md has proper frontmatter:
```bash
head -5 ~/.claude/skills/seo/SKILL.md
```
Should start with `---` followed by YAML.

3. Restart Claude Code:
```bash
claude
```

4. Re-run installer:
```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

---

### Python Dependency Errors

**Symptom:** `ModuleNotFoundError: No module named 'requests'`

**Solution:**

As of v1.2.0, dependencies are installed in a venv. Try:

```bash
# Use the venv pip
~/.claude/skills/seo/.venv/bin/pip install -r ~/.claude/skills/seo/requirements.txt
```

If the venv doesn't exist, install with `--user`:
```bash
pip install --user -r ~/.claude/skills/seo/requirements.txt
```

Or install individually:
```bash
pip install --user beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

### requirements.txt Not Found

**Symptom:** `No such file: requirements.txt` after install

**Solution:** As of v1.2.0, requirements.txt is copied to the skill directory:

```bash
ls ~/.claude/skills/seo/requirements.txt
```

If missing, download it directly:
```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/requirements.txt \
  -o ~/.claude/skills/seo/requirements.txt
```

### Windows Python Detection Issues

**Symptom:** `python is not recognized` or `pip points to wrong Python`

**Solution (v1.2.0+):** The Windows installer now tries both `python` and `py -3`. If both fail:

1. Install Python from [python.org](https://python.org) and check "Add to PATH"
2. Or use the Windows launcher: `py -3 -m pip install -r requirements.txt`
3. Use `python -m pip` instead of bare `pip`

---

### Playwright Screenshot Errors

**Symptom:** `playwright._impl._errors.Error: Executable doesn't exist`

**Solution:**
```bash
playwright install chromium
```

If that fails:
```bash
pip install playwright
python -m playwright install chromium
```

---

### Permission Denied Errors

**Symptom:** `Permission denied` when running scripts

**Solution:**
```bash
chmod +x ~/.claude/skills/seo/scripts/*.py
```

---

---

### Subagent Not Found

**Symptom:** `Agent 'seo-technical' not found`

**Solution:**

1. Verify agent files exist:
```bash
ls ~/.claude/agents/seo-*.md
```

2. Check agent frontmatter:
```bash
head -5 ~/.claude/agents/seo-technical.md
```

3. Re-install agents:
```bash
cp /path/to/claude-seo/agents/*.md ~/.claude/agents/
```

---

### Timeout Errors

**Symptom:** `Request timed out after 30 seconds`

**Solutions:**

1. The target site may be slow: try again
2. Increase timeout in script calls
3. Check your network connection
4. Some sites block automated requests

---

### Schema Validation False Positives

**Symptom:** Hook blocks valid schema

**Check:**

1. Ensure placeholders are replaced
2. Verify @context is `https://schema.org`
3. Check for deprecated types (HowTo, SpecialAnnouncement)
4. Validate at [Google's Rich Results Test](https://search.google.com/test/rich-results)

---

### Slow Audit Performance

**Symptom:** Full audit takes too long

**Solutions:**

1. Audit crawls up to 500 pages: large sites take time
2. Subagents run in parallel to speed up analysis
3. For faster checks, use `/seo page` on specific URLs
4. Check if site has slow response times

---

## Getting Help

1. **Check the docs:** Review [COMMANDS.md](../bmad_repo/commands.md) and [ARCHITECTURE.md](ARCHITECTURE.md)

2. **GitHub Issues:** Report bugs at the repository

3. **Logs:** Check Claude Code's output for error details

## Debug Mode

To see detailed output, check Claude Code's internal logs or run scripts directly:

```bash
# Test fetch
python3 ~/.claude/skills/seo/scripts/fetch_page.py https://example.com

# Test parse
python3 ~/.claude/skills/seo/scripts/parse_html.py page.html --json

# Test screenshot
python3 ~/.claude/skills/seo/scripts/capture_screenshot.py https://example.com
```
```

## File: `brain/knowledge/docs_legacy/superpowers/plans/2026-03-13-github-audit-fixes.md`
```markdown
# GitHub Audit Fixes Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise the GitHub repo health score from 70/100 by closing all audit gaps identified in the 2026-03-13 audit.

**Architecture:** All changes are isolated file edits and net-new file creation, with no refactoring and no dependency changes. GitHub settings are updated via `gh repo edit`. The `.github/` directory does not yet exist; all files in it are created from scratch with zero conflict risk.

**Tech Stack:** Markdown, YAML, GitHub Actions, `gh` CLI

---

## Pre-flight Checklist (Verify Before Any Changes)

- [ ] Confirm `agents/` directory has exactly 7 files:
  `seo-content.md seo-geo.md seo-performance.md seo-schema.md seo-sitemap.md seo-technical.md seo-visual.md`
- [ ] Confirm CITATION.cff does NOT exist: `ls CITATION.cff 2>&1` → "No such file"
- [ ] Confirm `.github/` does NOT exist: `ls .github/ 2>&1` → "No such file"
- [ ] Confirm `plugin.json` version is `"1.3.2"` and agents array has 6 items (missing seo-geo)
- [ ] Confirm README line 181 says `Subagents (6 total)`
- [ ] Confirm CHANGELOG.md line 123 says "6 subagents" - **this is in the v1.0.0 historical entry, do NOT touch it**

---

## Task 1: Fix plugin.json (version bump + add seo-geo agent)

**Files:** Modify `plugin.json`

**What & Why:** Version is still `1.3.2` but the codebase is on v1.4.0. The `agents` array is missing `agents/seo-geo.md` which was added in v1.4.0.

**Safe to change:** Purely additive - adding one entry to the array and bumping a string.

- [ ] Open `plugin.json`, verify current state:
  - `"version": "1.3.2"` ← stale
  - agents array has 6 items, ends with `"agents/seo-visual.md"` ← missing seo-geo
- [ ] Change `"version"` from `"1.3.2"` to `"1.4.0"`
- [ ] Add `"agents/seo-geo.md"` to the `agents` array (after `"agents/seo-visual.md"`)
- [ ] Verify the JSON is valid: `python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"`
- [ ] Commit:
  ```bash
  git add .claude-plugin/plugin.json
  git commit -m "fix: bump plugin.json to v1.4.0 and add seo-geo agent"
  ```

---

## Task 2: Fix README.md (H1 keyword, ToC, version badge, architecture count)

**Files:** Modify `README.md`

**What & Why:**
- H1 is `# Claude SEO` (weak keyword signal) → add keyword suffix
- No Table of Contents (10+ sections, hard to navigate)
- Only 2 badges → add GitHub release version badge
- Architecture block says `Subagents (6 total)` → should be 7

**Safe to change:** All edits are in isolated sections. No cross-file references break.

- [ ] Strengthen H1 (line 5):
  - Change `# Claude SEO` -> `# Claude SEO: SEO Audit Skill for Claude Code`
- [ ] Add version badge after existing badges (line 12, after License badge):
  ```markdown
  [![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-seo)](https://github.com/AgriciDaniel/claude-seo/releases)
  ```
- [ ] Add Table of Contents between the intro paragraph and `## Installation` section.
  Insert after line 12 (the badges block), before line 14 (`## Installation`):
  ```markdown

  ## Table of Contents

  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Commands](#commands)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Extensions](#extensions)
  - [Documentation](#documentation)
  - [Requirements](#requirements)
  - [Uninstall](#uninstall)
  - [Contributing](#contributing)
  ```
- [ ] Fix architecture block (line 181 after ToC insertion - find by content):
  - Change `~/.claude/agents/seo-*.md     # Subagents (6 total)` → `~/.claude/agents/seo-*.md     # Subagents (7 total)`
- [ ] Verify no other "6 total" or "6 subagent" strings remain:
  `grep -n "6 total\|6 subagent" README.md`
- [ ] Commit:
  ```bash
  git add README.md
  git commit -m "docs: strengthen H1, add ToC and version badge, fix subagent count to 7"
  ```

---

## Task 3: Fix SECURITY.md (add response timeline)

**Files:** Modify `SECURITY.md`

**What & Why:** Missing acknowledgment and resolution timeline, required for full Community Standards score.

**Safe to change:** Pure addition to existing section.

- [ ] Add response timeline to the "Reporting a Vulnerability" section.
  After the 3-item list and before `## Supported Versions`, insert:
  ```markdown

  ## Response Timeline

  - **Acknowledgment**: Within 72 hours of report
  - **Status update**: Within 7 days with initial assessment
  - **Resolution**: We aim to release a fix within 30 days for confirmed vulnerabilities
  ```
- [ ] Commit:
  ```bash
  git add SECURITY.md
  git commit -m "docs: add vulnerability response timeline to SECURITY.md"
  ```

---

## Task 4: Create CITATION.cff

**Files:** Create `CITATION.cff`

**What & Why:** File doesn't exist. Enables academic citation. Required for GitHub Community Standards full score.

- [ ] Create `CITATION.cff` at repo root:
  ```yaml
  cff-version: 1.2.0
  title: Claude SEO
  message: >-
    If you use this software, please cite it using the metadata from this file.
  type: software
  authors:
    - alias: AgriciDaniel
      given-names: Daniel
      family-names: Agricidaniel
  repository-code: 'https://github.com/AgriciDaniel/claude-seo'
  url: 'https://github.com/AgriciDaniel/claude-seo'
  license: MIT
  version: 1.4.0
  date-released: '2026-03-12'
  keywords:
    - seo
    - claude-code
    - ai-tools
    - schema-markup
    - e-e-a-t
    - geo
  ```
- [ ] Commit:
  ```bash
  git add CITATION.cff
  git commit -m "docs: add CITATION.cff for academic citation support"
  ```

---

## Task 5: Create .github/ directory infrastructure

**Files:** Create 8 new files under `.github/`

**What & Why:** No `.github/` directory exists. This single gap zeros out: issue templates (20pts), PR template (10pts), devcontainer/Dependabot (15pts) in Community Health scoring. Creating these closes the biggest single scoring gap.

**Safe to create:** Directory doesn't exist at all, so zero conflict risk.

### 5a: Issue Templates

- [ ] Create `.github/ISSUE_TEMPLATE/bug_report.yml`:
  ```yaml
  name: Bug Report
  description: Report a bug or unexpected behavior in Claude SEO
  title: "[Bug]: "
  labels: ["bug"]
  body:
    - type: markdown
      attributes:
        value: |
          Thanks for reporting a bug! Please fill in as much detail as possible.
    - type: input
      id: os
      attributes:
        label: Operating System
        description: e.g. macOS 14, Ubuntu 24.04, Windows 11
      validations:
        required: true
    - type: input
      id: python-version
      attributes:
        label: Python Version
        description: Run `python3 --version`
      validations:
        required: true
    - type: input
      id: command
      attributes:
        label: Command that failed
        description: e.g. `/seo audit https://example.com`
      validations:
        required: true
    - type: textarea
      id: error-output
      attributes:
        label: Full error output
        description: Copy the complete terminal output
        render: shell
      validations:
        required: true
    - type: textarea
      id: expected
      attributes:
        label: Expected behavior
        description: What did you expect to happen?
      validations:
        required: true
  ```

- [ ] Create `.github/ISSUE_TEMPLATE/feature_request.yml`:
  ```yaml
  name: Feature Request
  description: Suggest a new feature or improvement for Claude SEO
  title: "[Feature]: "
  labels: ["enhancement"]
  body:
    - type: markdown
      attributes:
        value: |
          Have a great idea? We'd love to hear it! For general discussion, consider using [GitHub Discussions](https://github.com/AgriciDaniel/claude-seo/discussions) instead.
    - type: textarea
      id: problem
      attributes:
        label: Problem statement
        description: What problem does this feature solve?
      validations:
        required: true
    - type: textarea
      id: solution
      attributes:
        label: Proposed solution
        description: Describe how you'd like it to work
      validations:
        required: true
    - type: textarea
      id: alternatives
      attributes:
        label: Alternatives considered
        description: Any alternative solutions or features you've considered?
  ```

- [ ] Create `.github/ISSUE_TEMPLATE/config.yml`:
  ```yaml
  blank_issues_enabled: false
  contact_links:
    - name: Question or Discussion
      url: https://github.com/AgriciDaniel/claude-seo/discussions
      about: Ask questions and discuss ideas in GitHub Discussions
  ```

- [ ] Commit:
  ```bash
  git add .github/ISSUE_TEMPLATE/
  git commit -m "ci: add YAML issue templates for bug reports and feature requests"
  ```

### 5b: PR Template

- [ ] Create `.github/PULL_REQUEST_TEMPLATE.md`:
  ```markdown
  ## Summary

  <!-- What does this PR do? Why is it needed? -->

  ## Type of Change

  - [ ] Bug fix
  - [ ] New feature / sub-skill
  - [ ] Documentation update
  - [ ] Refactor / code quality
  - [ ] Other (describe below)

  ## Checklist

  - [ ] Tested with a real URL before submitting
  - [ ] SKILL.md files stay under 500 lines (if modified)
  - [ ] Python scripts output JSON (if modified)
  - [ ] Reference files stay under 200 lines (if modified)
  - [ ] `set -euo pipefail` used in any new shell scripts
  - [ ] CHANGELOG.md updated with the change
  ```
- [ ] Commit:
  ```bash
  git add .github/PULL_REQUEST_TEMPLATE.md
  git commit -m "ci: add PR template with checklist"
  ```

### 5c: GitHub Actions CI

**What:** Python syntax validation for scripts in `scripts/`. No test suite exists, so this is the minimum viable CI. It validates that all scripts are syntactically correct Python 3.10+.

- [ ] Create `.github/workflows/ci.yml`:
  ```yaml
  name: CI

  on:
    push:
      branches: [main]
    pull_request:
      branches: [main]

  jobs:
    lint:
      name: Python Syntax Check
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4

        - name: Set up Python 3.10
          uses: actions/setup-python@v5
          with:
            python-version: "3.10"

        - name: Check Python syntax
          run: |
            python3 -m py_compile scripts/fetch_page.py
            python3 -m py_compile scripts/parse_html.py
            python3 -m py_compile scripts/analyze_visual.py
            python3 -m py_compile scripts/capture_screenshot.py
            echo "All scripts passed syntax check"
  ```
- [ ] Commit:
  ```bash
  git add .github/workflows/ci.yml
  git commit -m "ci: add GitHub Actions workflow for Python syntax validation"
  ```

### 5d: Dependabot

- [ ] Create `.github/dependabot.yml`:
  ```yaml
  version: 2
  updates:
    - package-ecosystem: "pip"
      directory: "/"
      schedule:
        interval: "weekly"
      labels:
        - "dependencies"

    - package-ecosystem: "github-actions"
      directory: "/"
      schedule:
        interval: "weekly"
      labels:
        - "dependencies"
  ```
- [ ] Commit:
  ```bash
  git add .github/dependabot.yml
  git commit -m "ci: add Dependabot for pip and GitHub Actions updates"
  ```

### 5e: FUNDING and Release Config

- [ ] Create `.github/FUNDING.yml`:
  ```yaml
  # Funding links for this project
  # See: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository
  custom:
    - https://www.skool.com/ai-marketing-hub-pro
  ```

- [ ] Create `.github/release.yml`:
  ```yaml
  changelog:
    exclude:
      labels:
        - ignore-for-release
    categories:
      - title: Security
        labels:
          - security
      - title: New Features
        labels:
          - enhancement
          - feature
      - title: Bug Fixes
        labels:
          - bug
          - fix
      - title: Documentation
        labels:
          - documentation
          - docs
      - title: Dependencies
        labels:
          - dependencies
      - title: Other Changes
        labels:
          - "*"
  ```

- [ ] Commit:
  ```bash
  git add .github/FUNDING.yml .github/release.yml
  git commit -m "ci: add FUNDING.yml and release.yml for auto-generated release notes"
  ```

---

## Task 6: Update GitHub Repository Settings

**What & Why:** These are GitHub UI settings that can be set via `gh repo edit`. Cannot be done via file commits; must use the CLI.

**Changes:**
1. Enable Discussions (currently off, but CONTRIBUTING.md tells users to use it)
2. Disable Wiki (currently on but unused, misleads visitors)
3. Fix description ("6 subagents" → "7 subagents")
4. Add topics: `python`, `skill`

**IMPORTANT:** These changes take effect immediately on the remote repo. Verify with `gh repo view` after each change.

- [ ] Enable Discussions:
  ```bash
  gh repo edit AgriciDaniel/claude-seo --enable-discussions
  ```
  Verify: `gh repo view AgriciDaniel/claude-seo --json hasDiscussionsEnabled --jq .hasDiscussionsEnabled`
  Expected: `true`

- [ ] Disable Wiki:
  ```bash
  gh repo edit AgriciDaniel/claude-seo --enable-wiki=false
  ```
  Verify: `gh repo view AgriciDaniel/claude-seo --json hasWikiEnabled --jq .hasWikiEnabled`
  Expected: `false`

- [ ] Fix description (replace "6 subagents" with "7 subagents"):
  ```bash
  gh repo edit AgriciDaniel/claude-seo --description "Universal SEO skill for Claude Code. 13 sub-skills, 7 subagents, extensions system with DataForSEO MCP integration. Technical SEO, E-E-A-T, schema, GEO/AEO, and strategic planning."
  ```
  Verify: `gh repo view AgriciDaniel/claude-seo --json description --jq .description`

- [ ] Add topics `python` and `skill`:
  ```bash
  gh repo edit AgriciDaniel/claude-seo --add-topic python --add-topic skill
  ```
  Verify: `gh repo view AgriciDaniel/claude-seo --json repositoryTopics --jq '.repositoryTopics | map(.name)'`
  Expected: 15 topics including `python` and `skill`

- [ ] Push all committed changes:
  ```bash
  git push origin main
  ```

---

## Task 7: Final Verification

- [ ] Confirm all 8 `.github/` files exist:
  ```bash
  find .github/ -type f | sort
  ```
  Expected 8 files: 3 under ISSUE_TEMPLATE/, PR template, ci.yml, dependabot.yml, FUNDING.yml, release.yml

- [ ] Confirm CITATION.cff exists and is valid YAML:
  ```bash
  python3 -c "import yaml; yaml.safe_load(open('CITATION.cff'))" && echo "valid"
  ```

- [ ] Confirm plugin.json is valid JSON and has 7 agents:
  ```bash
  python3 -c "import json; d=json.load(open('.claude-plugin/plugin.json')); print(d['version'], len(d['agents']))"
  ```
  Expected: `1.4.0 7`

- [ ] Confirm no stale "6 subagent/total" strings remain in actively-versioned content:
  ```bash
  grep -rn "6 subagent\|subagents (6\|6 total" --include="*.md" --include="*.json" . \
    --exclude-dir=".git" --exclude-dir="claude-seo-main" --exclude-dir="claude-ads-main"
  ```
  Expected: Only line 123 in CHANGELOG.md (v1.0.0 historical entry, correct, do not touch)

- [ ] Confirm GitHub settings applied:
  ```bash
  gh repo view AgriciDaniel/claude-seo --json description,hasDiscussionsEnabled,hasWikiEnabled,repositoryTopics
  ```

- [ ] Confirm CI workflow is visible on GitHub:
  ```bash
  gh workflow list --repo AgriciDaniel/claude-seo
  ```

---

## Do NOT Change

- `CHANGELOG.md` line 123: "6 subagents" is in the v1.0.0 historical entry. It was accurate when written.
- `seo/SKILL.md`: already correctly says "7 subagents"
- `CLAUDE.md`: already correctly says "7 parallel subagents"
- `brain/knowledge/docs_legacy/ARCHITECTURE.md`, `brain/knowledge/docs_legacy/COMMANDS.md`: no stale counts found
- `scripts/mobile_analysis.py`: already in `.gitignore` as a generated file

## Expected Score Impact

| Category | Before | Expected After |
|----------|--------|---------------|
| README Quality | 79 | ~84 (H1, ToC, badge) |
| Metadata & Discovery | 79 | ~87 (description, topics, Discussions) |
| Legal Compliance | 78 | ~88 (CITATION.cff, SECURITY timeline) |
| Community Health | 38 | ~68 (issue templates, PR template, dependabot) |
| Release & Maintenance | 67 | ~80 (CI, dependabot, release.yml, badge) |
| SEO & Discoverability | 73 | ~79 (Discussions, keyword H1) |
| **Overall** | **70** | **~81** |
```

## File: `extensions/banana/install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Banana Image Generation Extension Installer for Claude SEO
# Wraps everything in main() to prevent partial execution on network failure

main() {
    SKILL_DIR="${HOME}/.claude/skills/seo-image-gen"
    AGENT_DIR="${HOME}/.claude/agents"
    SEO_SKILL_DIR="${HOME}/.claude/skills/seo"
    SETTINGS_FILE="${HOME}/.claude/settings.json"

    echo "════════════════════════════════════════"
    echo "║  Banana Image Gen - SEO Extension    ║"
    echo "║  For Claude SEO                      ║"
    echo "════════════════════════════════════════"
    echo ""

    # Check prerequisites
    if [ ! -d "${SEO_SKILL_DIR}" ]; then
        echo "✗ Claude SEO is not installed."
        echo "  Install it first: curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash"
        exit 1
    fi
    echo "✓ Claude SEO detected"

    if ! command -v node >/dev/null 2>&1; then
        echo "✗ Node.js is required but not installed."
        echo "  Install Node.js 20+: https://nodejs.org/"
        exit 1
    fi

    NODE_VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
    if [ "${NODE_VERSION}" -lt 20 ]; then
        echo "✗ Node.js 20+ required (found v${NODE_VERSION})."
        echo "  Update: https://nodejs.org/"
        exit 1
    fi
    echo "✓ Node.js v$(node -v | sed 's/v//') detected"

    if ! command -v npx >/dev/null 2>&1; then
        echo "✗ npx is required but not found (comes with npm)."
        exit 1
    fi
    echo "✓ npx detected"

    # Determine script directory (works for both ./install.sh and repo-relative paths)
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # Check if running from repo or standalone
    if [ -f "${SCRIPT_DIR}/skills/seo-image-gen/SKILL.md" ]; then
        SOURCE_DIR="${SCRIPT_DIR}"
    elif [ -f "${SCRIPT_DIR}/extensions/banana/skills/seo-image-gen/SKILL.md" ]; then
        SOURCE_DIR="${SCRIPT_DIR}/extensions/banana"
    else
        echo "✗ Cannot find extension source files."
        echo "  Run this script from the claude-seo repo: ./extensions/banana/install.sh"
        exit 1
    fi

    # Check if nanobanana-mcp is already configured
    MCP_CONFIGURED=false
    if [ -f "${SETTINGS_FILE}" ]; then
        if python3 -c "
import json
with open('${SETTINGS_FILE}', 'r') as f:
    settings = json.load(f)
if 'mcpServers' in settings and 'nanobanana-mcp' in settings['mcpServers']:
    exit(0)
else:
    exit(1)
" 2>/dev/null; then
            MCP_CONFIGURED=true
            echo "✓ nanobanana-mcp already configured in settings.json"
        fi
    fi

    # If MCP not configured, prompt for API key
    if [ "${MCP_CONFIGURED}" = false ]; then
        echo ""
        echo "Google AI API key required for image generation."
        echo "Get a free key at: https://aistudio.google.com/apikey"
        echo ""

        read -rsp "Google AI API key (GOOGLE_AI_API_KEY): " GOOGLE_AI_API_KEY
        echo ""
        if [ -z "${GOOGLE_AI_API_KEY}" ]; then
            echo "✗ API key cannot be empty."
            exit 1
        fi

        # Configure MCP server
        echo "→ Configuring nanobanana-mcp server..."
        python3 -c "
import json, os

settings_path = '${SETTINGS_FILE}'

# Read existing settings or create new
if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        settings = json.load(f)
else:
    settings = {}

# Ensure mcpServers key exists
if 'mcpServers' not in settings:
    settings['mcpServers'] = {}

# Add nanobanana-mcp server config
settings['mcpServers']['nanobanana-mcp'] = {
    'command': 'npx',
    'args': ['-y', '@ycse/nanobanana-mcp@latest'],
    'env': {
        'GOOGLE_AI_API_KEY': '''${GOOGLE_AI_API_KEY}'''
    }
}

# Write back
os.makedirs(os.path.dirname(settings_path), exist_ok=True)
with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=2)

print('  ✓ nanobanana-mcp configured in settings.json')
" || {
            echo "✗ Could not auto-configure MCP server."
            echo "  See: extensions/banana/brain/knowledge/docs_legacy/BANANA-SETUP.md"
            exit 1
        }
    fi

    # Install skill
    echo ""
    echo "→ Installing seo-image-gen skill..."
    mkdir -p "${SKILL_DIR}"
    cp "${SOURCE_DIR}/skills/seo-image-gen/SKILL.md" "${SKILL_DIR}/SKILL.md"

    # Install agent
    echo "→ Installing seo-image-gen agent..."
    mkdir -p "${AGENT_DIR}"
    cp "${SOURCE_DIR}/agents/seo-image-gen.md" "${AGENT_DIR}/seo-image-gen.md"

    # Copy scripts and references to skill directory for ${CLAUDE_SKILL_DIR} resolution
    echo "→ Installing scripts and references..."
    mkdir -p "${SKILL_DIR}/scripts" "${SKILL_DIR}/references"
    cp "${SOURCE_DIR}/scripts/"*.py "${SKILL_DIR}/scripts/"
    cp "${SOURCE_DIR}/references/"*.md "${SKILL_DIR}/references/"

    # Pre-warm npx package
    echo "→ Pre-downloading nanobanana-mcp..."
    npx -y @ycse/nanobanana-mcp@latest --help >/dev/null 2>&1 || true

    echo ""
    echo "✓ Banana Image Generation extension installed successfully!"
    echo ""
    echo "Usage:"
    echo "  1. Start Claude Code:  claude"
    echo "  2. Run commands:"
    echo "     /seo image-gen og \"Professional SaaS dashboard\""
    echo "     /seo image-gen hero \"Dramatic sunset over city skyline\""
    echo "     /seo image-gen product \"Wireless headphones on marble\""
    echo "     /seo image-gen infographic \"SEO ranking factors 2026\""
    echo "     /seo image-gen custom \"Any creative concept\""
    echo "     /seo image-gen batch \"Product variations\" 3"
    echo ""
    echo "Full docs: extensions/banana/README.md"
    echo "To uninstall: ./extensions/banana/uninstall.sh"
}

main "$@"
```

## File: `extensions/banana/README.md`
```markdown
# Banana Image Generation Extension for Claude SEO

Generate production-ready SEO images using AI: OG/social previews, blog heroes,
product photography, infographics, and more. Powered by Google Gemini via the
banana Creative Director pipeline.

## Prerequisites

> This extension wraps [Claude Banana](https://github.com/AgriciDaniel/banana-claude)
> for SEO-specific use cases. Install the standalone skill for general-purpose image generation.

- **Claude SEO** installed (`~/.claude/skills/seo/`)
- **Node.js 18+** with npx
- **Google AI API key** (free at [aistudio.google.com/apikey](https://aistudio.google.com/apikey))
- **ImageMagick** (optional, for post-processing)

## Installation

```bash
./extensions/banana/install.sh
```

The installer will:
1. Verify Claude SEO is installed
2. Prompt for your Google AI API key (if nanobanana-mcp not already configured)
3. Install the `seo-image-gen` skill and agent
4. Configure the MCP server in `~/.claude/settings.json`

## Commands

| Command | What it does |
|---------|-------------|
| `/seo image-gen og <description>` | OG/social preview image (1200x630 feel) |
| `/seo image-gen hero <description>` | Blog hero image (widescreen, dramatic) |
| `/seo image-gen product <description>` | Product photography (clean, white BG) |
| `/seo image-gen infographic <description>` | Infographic visual (vertical, data-heavy) |
| `/seo image-gen custom <description>` | Custom with full Creative Director pipeline |
| `/seo image-gen batch <description> [N]` | Generate N variations (default: 3) |

## Use Case Defaults

| Use Case | Aspect Ratio | Resolution | Domain Mode | Cost |
|----------|-------------|------------|-------------|------|
| OG/Social Preview | 16:9 | 1K | Product/UI | ~$0.04 |
| Blog Hero | 16:9 | 2K | Cinema/Editorial | ~$0.08 |
| Product Photo | 4:3 | 2K | Product | ~$0.08 |
| Infographic | 2:3 | 4K | Infographic | ~$0.16 |
| Social Square | 1:1 | 1K | UI/Web | ~$0.04 |
| Favicon/Icon | 1:1 | 512 | Logo | ~$0.02 |

## How It Works

Claude acts as a **Creative Director**. It never passes raw text to the API.
Instead, it analyzes your intent, selects the optimal domain mode, and constructs
an optimized prompt using a proven 6-component Reasoning Brief system:

1. **Subject** (30%):Physical specificity and micro-details
2. **Style** (25%):Camera specs, film stock, brand references
3. **Context** (15%):Location, time, weather, supporting elements
4. **Action** (10%):Pose, gesture, movement, state
5. **Composition** (10%):Shot type, framing, focal length
6. **Lighting** (10%):Direction, quality, color temperature

## Post-Generation SEO Checklist

After every generation, Claude provides:
- Alt text suggestion (keyword-rich, descriptive)
- SEO-friendly file naming convention
- WebP conversion command
- ImageObject schema snippet
- OG meta tag markup (for social previews)

## Audit Integration

During `/seo audit`, the extension optionally spawns an image analysis agent that:
- Audits existing OG/social images across the site
- Identifies missing or low-quality images
- Creates a prioritized generation plan with prompt suggestions
- Estimates total cost for the generation plan

The agent never auto-generates images. It produces a plan for your review.

## Uninstallation

```bash
./extensions/banana/uninstall.sh
```

This removes the skill and agent. If you also use [Claude Banana](https://github.com/AgriciDaniel/banana-claude),
the MCP server config is preserved.

## Troubleshooting

See [brain/knowledge/docs_legacy/BANANA-SETUP.md](brain/knowledge/docs_legacy/BANANA-SETUP.md) for detailed setup instructions
and common issues.
```

## File: `extensions/banana/uninstall.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

main() {
    echo "→ Uninstalling Banana Image Generation extension..."

    # Remove skill (includes copied scripts and references)
    rm -rf "${HOME}/.claude/skills/seo-image-gen"

    # Remove agent
    rm -f "${HOME}/.claude/agents/seo-image-gen.md"

    # Ask before removing MCP server (user may use standalone banana skill)
    SETTINGS_FILE="${HOME}/.claude/settings.json"
    if [ -f "${SETTINGS_FILE}" ]; then
        # Check if standalone banana skill still exists
        if [ -d "${HOME}/.claude/skills/banana" ]; then
            echo "  ℹ  Standalone banana skill detected at ~/.claude/skills/banana/"
            echo "  ℹ  Keeping nanobanana-mcp in settings.json (used by standalone skill)"
        else
            # No standalone skill, safe to remove MCP
            python3 -c "
import json, os
settings_path = '${SETTINGS_FILE}'
with open(settings_path, 'r') as f:
    settings = json.load(f)
if 'mcpServers' in settings and 'nanobanana-mcp' in settings['mcpServers']:
    del settings['mcpServers']['nanobanana-mcp']
    if not settings['mcpServers']:
        del settings['mcpServers']
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print('  ✓ Removed nanobanana-mcp from settings.json')
else:
    print('  ✓ No nanobanana-mcp entry in settings.json')
" 2>/dev/null || echo "  ⚠  Could not auto-remove MCP config. Remove 'nanobanana-mcp' from ~/.claude/settings.json manually."
        fi
    fi

    echo "✓ Banana Image Generation extension uninstalled."
}

main "$@"
```

## File: `extensions/banana/agents/seo-image-gen.md`
```markdown
---
name: seo-image-gen
description: SEO image analyst. Audits existing OG/social preview images, identifies missing or low-quality images, and creates an image generation plan with prompts for key pages. Does NOT auto-generate images.
tools: Read, Bash, Glob, Grep
---

You are an SEO image analyst. When delegated tasks during an SEO audit:

1. Check that nanobanana-mcp tools are available before including generation recommendations
2. Analyze the site's existing image strategy for SEO impact
3. Output a structured generation plan. Never auto-generate (cost control)

## Analysis Scope

For each audited page, evaluate:
- **OG image presence**:Does `og:image` meta tag exist? Is it valid?
- **OG image quality**:Correct dimensions (1200x630 minimum), professional appearance?
- **Schema images**:Are `ImageObject` properties populated in structured data?
- **Alt text quality**:Descriptive, keyword-rich, not stuffed?
- **Image format**:Using modern formats (WebP, AVIF) vs legacy (PNG, JPEG)?
- **Image file size**:Under 200KB for hero, under 100KB for thumbnails?

## Output Format

Match existing claude-seo patterns:

### Image Audit Summary

| Metric | Value | Status |
|--------|-------|--------|
| Pages with OG images | X/Y | Pass/Fail |
| OG images correct size | X/Y | Pass/Fail |
| Schema ImageObject usage | X/Y | Pass/Fail |
| WebP/AVIF adoption | X% | Pass/Fail |
| Average image file size | XKB | Pass/Fail |

### Image Generation Plan

For each page missing or having low-quality images:

| Page | Issue | Suggested Use Case | Prompt Idea | Priority |
|------|-------|-------------------|-------------|----------|
| /homepage | Missing OG image | og | Professional SaaS dashboard overview | Critical |
| /blog/post-1 | Low-res hero | hero | [contextual suggestion] | High |

Priority levels: Critical > High > Medium > Low

### Recommendations

- Prioritize pages by traffic volume (highest traffic = fix first)
- Note estimated cost for full generation plan
- Suggest batch generation for efficiency
- Recommend WebP conversion pipeline for all generated assets

## Error Handling

- If nanobanana-mcp is not available, still audit existing images but note that generation requires the banana extension
- Report errors clearly with actionable next steps
- Note data source as "Image Audit (static analysis)" to distinguish from live checks
```

## File: `extensions/banana/brain/knowledge/docs_legacy/BANANA-SETUP.md`
```markdown
# Banana Extension Setup Guide

## Google AI API Key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API key"
4. Copy the key. You'll need it during installation

**Free tier limits:**
- ~10 requests per minute (RPM)
- ~500 requests per day (RPD)
- Resets at midnight Pacific time

## MCP Server Configuration

The installer configures this automatically. If you need to set it up manually,
add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "nanobanana-mcp": {
      "command": "npx",
      "args": ["-y", "@ycse/nanobanana-mcp@latest"],
      "env": {
        "GOOGLE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Verifying Installation

Run the validation script:
```bash
python3 ~/.claude/skills/seo-image-gen/scripts/validate_setup.py
```

Or check manually:
1. `ls ~/.claude/skills/seo-image-gen/SKILL.md`:skill file exists
2. `ls ~/.claude/agents/seo-image-gen.md`:agent file exists
3. `grep nanobanana ~/.claude/settings.json`:MCP configured

## Common Issues

### "MCP tools not available"
- Restart Claude Code after installing the extension
- Verify your API key is valid at [aistudio.google.com](https://aistudio.google.com)
- Check `~/.claude/settings.json` has the nanobanana-mcp entry

### "Rate limited (429)"
- Free tier: ~10 requests/minute, ~500/day
- Wait 60 seconds and retry
- For batch operations, add delays between requests

### "IMAGE_SAFETY" error
- The safety filter flagged your prompt (often a false positive)
- Claude will suggest rephrased alternatives automatically
- Common triggers: certain color descriptions, implied scenarios
- See `references/prompt-engineering.md` Safety Rephrase section

### "Node.js version too old"
- Requires Node.js 18+
- Update via nvm: `nvm install 18 && nvm use 18`
- Or download from [nodejs.org](https://nodejs.org/)

### Generated images not appearing
- Default output directory: `~/Documents/nanobanana_generated/`
- Check the path returned by Claude after generation
- Verify disk space is available

## ImageMagick (Optional)

For post-processing (WebP conversion, cropping, background removal):

```bash
# Ubuntu/Pop!_OS
sudo apt install imagemagick

# Verify
magick --version
```

If `magick` (v7) is not available, the scripts fall back to `convert` (v6).
```

## File: `extensions/banana/references/cost-tracking.md`
```markdown
# Cost Tracking Reference

> Load this on-demand when the user asks about costs or before batch operations.

## Pricing Table

| Model | Resolution | Cost/Image | Notes |
|-------|-----------|-----------|-------|
| 3.1 Flash | 512 | $0.020 | Quick drafts |
| 3.1 Flash | 1K | $0.039 | Standard (default) |
| 3.1 Flash | 2K | $0.078 | Quality assets |
| 3.1 Flash | 4K | $0.156 | Print/hero images |
| 2.5 Flash | 512 | $0.020 | Draft fallback |
| 2.5 Flash | 1K | $0.039 | Standard fallback |
| Batch API | Any | 50% of above | Asynchronous, higher latency |

Pricing is approximate, based on ~1,290 output tokens per image.
Research suggests actual costs may be ~$0.067/img. Verify at https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/pricing

## Free Tier Limits

- ~10 requests per minute (RPM)
- ~500 requests per day (RPD)
- Per Google Cloud project, resets midnight Pacific

## Cost Tracker Commands

```bash
# Log a generation
cost_tracker.py log --model gemini-3.1-flash-image-preview --resolution 1K --prompt "coffee shop hero"

# View summary (total + last 7 days)
cost_tracker.py summary

# Today's usage
cost_tracker.py today

# Estimate before batch
cost_tracker.py estimate --model gemini-3.1-flash-image-preview --resolution 1K --count 10

# Reset ledger
cost_tracker.py reset --confirm
```

## Storage

Ledger stored at `~/.banana/costs.json`. Created automatically on first use.
```

## File: `extensions/banana/references/gemini-models.md`
```markdown
# Gemini Image Generation Models

> Last updated: 2026-03-13
> Aligned with Google's March 2026 API state

## Available Models

### gemini-3.1-flash-image-preview (Recommended)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-3.1-flash-image-preview` |
| **Tier** | Nano Banana 2 (Flash) |
| **Speed** | Fast - optimized for high-volume use |
| **Aspect Ratios** | All 14 ratios (see table below) |
| **Max Resolution** | Up to 4096×4096 (4K tier) |
| **Features** | Google Search grounding (web + image), thinking levels, image-only output, extreme aspect ratios |
| **Rate Limits (Free)** | ~10 RPM / ~500 RPD (per Google Cloud project, resets midnight Pacific) |
| **Output Tokens** | ~1,290 output tokens per image |
| **Best For** | Most use cases, rapid iteration, batch generation |

### gemini-2.5-flash-image
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-2.5-flash-image` |
| **Tier** | Nano Banana 2 (Flash, previous gen) |
| **Speed** | Fast |
| **Aspect Ratios** | 1:1, 16:9, 9:16, 4:3, 3:4 |
| **Max Resolution** | Up to 1024×1024 (1K tier) |
| **Rate Limits (Free)** | ~10 RPM / ~500 RPD |
| **Best For** | Stable fallback, proven quality |

## Deprecated Models (DO NOT USE)

### gemini-3-pro-image-preview
- **Status:** Base model deprecated March 9, 2026. **Image generation variant may still be accessible**. Use at your own discretion via `set_model`. Prefer 3.1 Flash.
- **Was:** Nano Banana Pro tier (professional asset production, 4K output, 14 reference images)
- **Migration:** Use `gemini-3.1-flash-image-preview` instead

### gemini-2.0-flash-exp
- **Status:** Deprecated, replaced by gemini-2.5-flash-image

## Aspect Ratios

All 14 supported ratios. Availability varies by model:

| Ratio | Orientation | Use Cases | 3.1 Flash | 2.5 Flash |
|-------|-------------|-----------|:---------:|:---------:|
| `1:1` | Square | Social posts, avatars, thumbnails | ✅ | ✅ |
| `16:9` | Landscape | Blog headers, YouTube thumbnails, presentations | ✅ | ✅ |
| `9:16` | Portrait | Stories, Reels, TikTok, mobile | ✅ | ✅ |
| `4:3` | Landscape | Product shots, classic display | ✅ | ✅ |
| `3:4` | Portrait | Book covers, portrait framing | ✅ | ✅ |
| `2:3` | Portrait | Pinterest pins, posters | ✅ | ❌ |
| `3:2` | Landscape | DSLR standard, photo prints | ✅ | ❌ |
| `4:5` | Portrait | Instagram portrait, social | ✅ | ❌ |
| `5:4` | Landscape | Large format photography | ✅ | ❌ |
| `1:4` | Tall strip | Vertical banners, side panels | ✅ | ❌ |
| `4:1` | Wide strip | Website banners, headers | ✅ | ❌ |
| `1:8` | Extreme tall | Narrow vertical strips | ✅ | ❌ |
| `8:1` | Extreme wide | Ultra-wide banners | ✅ | ❌ |
| `21:9` | Ultra-wide | Cinematic, film-grade, ultra-wide monitors | ✅ | ❌ |

## Resolution Tiers

Control output resolution with the `imageSize` parameter. Note the **uppercase K** requirement.

| `imageSize` Value | Pixel Range | Model Availability | Use Case |
|-------------------|-------------|-------------------|----------|
| `512` | Up to 512×512 | All models | Drafts, quick iteration, low bandwidth |
| `1K` (default) | Up to 1024×1024 | All models | Standard web use, social media |
| `2K` | Up to 2048×2048 | 3.1 Flash | Quality assets, detailed work |
| `4K` | Up to 4096×4096 | 3.1 Flash | Print production, hero images, final assets |

**Notes:**
- Actual pixel dimensions depend on aspect ratio (e.g., 4K at 16:9 = 4096×2304)
- Higher resolutions consume more tokens and cost more
- Default is `1K` if `imageSize` is not specified

## API Configuration

### Endpoint
```
https://generativelanguage.googleapis.com/v1beta/models/{model-id}:generateContent
```

### Required Parameters
```json
{
  "contents": [{"parts": [{"text": "your prompt here"}]}],
  "generationConfig": {
    "responseModalities": ["TEXT", "IMAGE"],
    "imageConfig": {
      "aspectRatio": "16:9",
      "imageSize": "1K"
    }
  }
}
```

### Image-Only Output Mode
Force the model to return only an image (no text response):
```json
{
  "generationConfig": {
    "responseModalities": ["IMAGE"]
  }
}
```

### Thinking Level
Control how much the model "thinks" before generating. Higher levels improve complex compositions but increase latency:
```json
{
  "generationConfig": {
    "thinkingConfig": {
      "thinkingLevel": "medium"
    }
  }
}
```
Levels: `minimal`, `low`, `medium`, `high`

### Google Search Grounding
Ground generation in real-world visual references. Supports web and image search (3.1 Flash):
```json
{
  "tools": [{"googleSearch": {}}]
}
```
**Prompt pattern:** `[Search/source request] + [Analytical task] + [Visual translation]`

Example: "Search for the latest SpaceX Starship design, analyze its proportions and markings, then generate a photorealistic image of it at sunset on the launch pad."

### Multi-Image Input
Up to 14 reference images can be provided:
- **10 object references**: for style, composition, or visual matching
- **4 character references**: assign distinct names to preserve features across generations

Useful for character consistency, style transfer, and brand-aligned generation.

## Rate Limits by Tier

| Tier | RPM | RPD | Notes |
|------|-----|-----|-------|
| Free | ~10 | ~500 | Per Google Cloud project, resets midnight Pacific. Reduced Dec 2025. |
| Pay-as-you-go | 30 | 10,000 | Production workloads |
| Enterprise | Custom | Custom | Contact Google |

## Pricing

| Model | Resolution | Cost per Image | Notes |
|-------|-----------|---------------|-------|
| 3.1 Flash | 1K | ~$0.039 | Standard |
| 3.1 Flash | 2K | ~$0.078 | 2× standard |
| 3.1 Flash | 4K | ~$0.156 | 4× standard |
| 2.5 Flash | 1K | ~$0.039 | Standard |
| Batch API | Any | 50% discount | Asynchronous, higher latency |

Pricing is approximate and based on ~1,290 output tokens per image.
Research suggests NB2 pricing may be ~$0.067/img (vs documented $0.039). Verify current pricing at https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/pricing

## Image Output Specs

| Property | Value |
|----------|-------|
| **Format** | PNG |
| **Max Resolution** | Up to 4096×4096 (4K tier, 3.1 Flash) |
| **Color Space** | sRGB |
| **Text Rendering** | Supported - best under 25 characters |
| **Style Control** | Via prompt engineering |

## Safety Filters

Gemini uses a two-layer safety architecture:

1. **Input filters**: block prompts containing prohibited content before generation
2. **Output filters**: analyze generated images and block unsafe results

| `finishReason` | Meaning | Retryable? |
|----------------|---------|:----------:|
| `STOP` | Successful generation | N/A |
| `IMAGE_SAFETY` | Output blocked by safety filter | Rephrase prompt |
| `PROHIBITED_CONTENT` | Content policy violation | No - topic is blocked |
| `SAFETY` | General safety block | Rephrase prompt |
| `RECITATION` | Detected copyrighted content | Rephrase prompt |

**Known issue:** Filters are known to be overly cautious. Benign prompts may be blocked. Iterate with rephrased wording if this happens.

## Content Credentials

- **SynthID watermarks** are always embedded in generated images (invisible, machine-readable)
- **C2PA metadata** is included on Pro/paid outputs (verifiable provenance chain)

## Key Limitations
- No video generation (image only)
- No transparent backgrounds (PNG but always with background)
- Text rendering quality varies; keep text under 25 characters for best results
- Safety filters may block some prompts (violence, NSFW, public figures), known to be overly cautious
- Session context resets between Claude Code conversations
- `imageSize` and thinking level depend on MCP package version support
```

## File: `extensions/banana/references/mcp-tools.md`
```markdown
# MCP Tools Reference: @ycse/nanobanana-mcp

> Package: `@ycse/nanobanana-mcp`
> GitHub: https://github.com/YCSE/nanobanana-mcp

## Tools

### gemini_generate_image
Generate an image from a text prompt.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | string | Yes | Text description of the image to generate |

**Returns:** Image data + file path (saved to `~/Documents/nanobanana_generated/`)

**Example usage in Claude Code:**
```
User: "Generate a sunset over mountains in watercolor style"
→ Claude calls gemini_generate_image with prompt
→ Returns image path and description
```

### gemini_edit_image
Edit an existing image with text instructions.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `imagePath` | string | Yes | Path to the image file to edit |
| `prompt` | string | Yes | Edit instructions |

**Returns:** Modified image data + file path

**Example:**
```
User: "Remove the background from ~/Documents/photo.png"
→ Claude calls gemini_edit_image with path and instruction
```

### gemini_chat
Multi-turn visual conversation maintaining session context.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | Chat message (can reference previous images) |

**Returns:** Text response + optional image

**Key feature:** Session consistency, which maintains style, characters, and context across turns. Great for iterative refinement.

### set_aspect_ratio
Configure the aspect ratio for subsequent image generations.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `ratio` | string | Yes | Aspect ratio (e.g., "16:9", "1:1", "9:16") |

**Supported ratios:** 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 4:5, 5:4, 1:4, 4:1, 1:8, 8:1, 21:9

### set_model
Switch the active Gemini model.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Model identifier |

**Available models:**
- `gemini-3.1-flash-image-preview` (default, recommended)
- `gemini-2.5-flash-image` (stable fallback)

### get_image_history
Retrieve list of images generated in the current session.

**Parameters:** None

**Returns:** Array of image entries with paths and prompts

### clear_conversation
Reset session context and conversation history.

**Parameters:** None

**Returns:** Confirmation of reset

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_AI_API_KEY` | Yes | API key from https://aistudio.google.com/apikey |
| `NANOBANANA_MODEL` | No | Override default model (default: `gemini-3.1-flash-image-preview`) |

## Output Directory
All generated images are saved to: `~/Documents/nanobanana_generated/`

Images are named with timestamps for easy identification.

## Feature Availability via MCP

Some newer Gemini API features depend on the MCP package version of `@ycse/nanobanana-mcp`. Check the package version to confirm support:

| Feature | API Status | MCP Support |
|---------|-----------|-------------|
| `imageSize` (resolution control) | Available | Depends on package version |
| Thinking level (`thinkingConfig`) | Available | Depends on package version |
| Search grounding (`googleSearch`) | Available | Depends on package version |
| Image-only output (`responseModalities: ["IMAGE"]`) | Available | Depends on package version |
| Multi-image input (up to 14 refs) | Available | Via `gemini_chat` with image paths |
| All 14 aspect ratios | Available | Via `set_aspect_ratio` |

If a feature is not yet supported by the MCP package, you can still use it via direct API calls with `curl` or the Google AI SDK.
```

## File: `extensions/banana/references/post-processing.md`
```markdown
# Post-Processing Pipeline Reference

> Load this on-demand when the user needs image manipulation after generation.

## Prerequisites

Check availability before using:
```bash
which magick    # ImageMagick 7 (preferred)
which convert   # ImageMagick 6 (fallback)
which ffmpeg    # For video/animation
```

Install ImageMagick if not present: `sudo apt install imagemagick` (Debian/Ubuntu) or `brew install imagemagick` (macOS).

## Common Operations

### Resize for Platforms

```bash
# Instagram post (1080x1080)
magick input.png -resize 1080x1080^ -gravity center -extent 1080x1080 instagram.png

# Twitter/X header (1500x500)
magick input.png -resize 1500x500^ -gravity center -extent 1500x500 twitter-header.png

# YouTube thumbnail (1280x720)
magick input.png -resize 1280x720^ -gravity center -extent 1280x720 youtube-thumb.png

# LinkedIn banner (1584x396)
magick input.png -resize 1584x396^ -gravity center -extent 1584x396 linkedin-banner.png

# Favicon (multi-size ICO)
magick input.png -resize 32x32 favicon.ico
```

### Background Removal (Transparency)

```bash
# Remove solid white background
magick input.png -fuzz 10% -transparent white output.png

# Remove solid color background (specify color)
magick input.png -fuzz 15% -transparent "#F0F0F0" output.png

# Clean edges after transparency (anti-alias)
magick input.png -fuzz 10% -transparent white -channel A -blur 0x1 -level 50%,100% output.png

# Auto-crop transparent padding
magick input.png -trim +repage output.png
```

### Format Conversion

```bash
# PNG to WebP (web-optimized, smaller file)
magick input.png -quality 85 output.webp

# PNG to JPEG (with white background for transparency)
magick input.png -background white -flatten -quality 90 output.jpg

# PNG to AVIF (modern, smallest size)
magick input.png -quality 80 output.avif

# SVG trace (for logos; requires potrace)
potrace input.pbm -s -o output.svg
```

### Color Adjustments

```bash
# Increase contrast
magick input.png -contrast-stretch 2%x1% output.png

# Warm color temperature
magick input.png -modulate 100,110,105 output.png

# Cool color temperature
magick input.png -modulate 100,90,95 output.png

# Desaturate (muted colors)
magick input.png -modulate 100,70,100 output.png

# Convert to grayscale
magick input.png -colorspace Gray output.png

# Sepia tone
magick input.png -sepia-tone 80% output.png
```

### Compositing

```bash
# Overlay watermark (bottom-right, 20% opacity)
magick base.png watermark.png -gravity southeast -geometry +20+20 \
  -compose dissolve -define compose:args=20 -composite output.png

# Side-by-side comparison
magick input1.png input2.png +append comparison.png

# Vertical stack
magick input1.png input2.png -append stack.png

# Add padding/border
magick input.png -bordercolor white -border 40 output.png

# Add rounded corners
magick input.png \( +clone -alpha extract -draw \
  "roundrectangle 0,0,%[fx:w-1],%[fx:h-1],20,20" \) \
  -alpha off -compose CopyOpacity -composite rounded.png
```

### Batch Processing

```bash
# Resize all PNGs in directory
for f in ~/Documents/nanobanana_generated/*.png; do
  magick "$f" -resize 800x800 "${f%.png}_thumb.png"
done

# Convert all to WebP
for f in ~/Documents/nanobanana_generated/*.png; do
  magick "$f" -quality 85 "${f%.png}.webp"
done
```

## Animation (GIF/Video from Multiple Frames)

```bash
# Create GIF from multiple images
magick -delay 100 frame1.png frame2.png frame3.png animation.gif

# Create MP4 from image sequence
ffmpeg -framerate 1 -pattern_type glob -i '*.png' \
  -c:v libx264 -pix_fmt yuv420p slideshow.mp4
```

## Note on 4K Output

With Gemini 3.1 Flash's `imageSize: "4K"` option (up to 4096×4096), many traditional
upscaling post-processing steps are no longer necessary. If your target platform accepts
images at or below 4K resolution, generate at native 4K instead of generating at 1K
and upscaling. This produces better detail and avoids upscaling artifacts.

## Green Screen Transparency Pipeline

Gemini cannot generate transparent backgrounds. Use this workaround:

### 1. Generate with green screen prompt

Append to any prompt:
```
on a solid bright green (#00FF00) chroma key background
with a thin white outline separating the subject from the background
```

### 2. Remove green screen (ImageMagick)

```bash
magick input.png -fuzz 20% -transparent "#00FF00" output.png
```

### 3. Clean edges + trim (ImageMagick)

```bash
magick output.png -channel A -blur 0x1 -level 50%,100% -trim +repage final.png
```

### 4. Alternative (FFmpeg, better for batch)

```bash
ffmpeg -i input.png -vf "colorkey=0x00FF00:0.3:0.1,despill=type=green" -pix_fmt rgba output.png
```

### Tips
- `-fuzz 20%` handles slight color variations at edges; increase to 25% for softer edges
- The white outline in the prompt helps prevent color spill on subject edges
- For batch processing, the FFmpeg approach is faster and handles despill automatically
- Always verify edges after conversion; may need manual touchup for hair/fur

## Quality Assessment

```bash
# Get image dimensions and info
magick identify -verbose input.png | head -20

# Check file size
ls -lh input.png

# Get exact pixel dimensions
magick identify -format "%wx%h" input.png
```
```

## File: `extensions/banana/references/presets.md`
```markdown
# Brand/Style Presets Reference

> Load this on-demand when the user asks about presets or brand consistency.

## Preset Schema

Each preset is stored as `~/.banana/presets/NAME.json`:

```json
{
  "name": "tech-saas",
  "description": "Clean tech SaaS brand",
  "colors": ["#2563EB", "#1E40AF", "#F8FAFC"],
  "style": "clean minimal tech illustration, flat vectors, soft shadows",
  "typography": "bold geometric sans-serif",
  "lighting": "bright diffused studio, no harsh shadows",
  "mood": "professional, trustworthy, modern",
  "default_ratio": "16:9",
  "default_resolution": "2K"
}
```

## Example Presets

### tech-saas
- **Colors:** #2563EB, #1E40AF, #F8FAFC (blue + white)
- **Style:** Clean minimal tech illustration, flat vectors, soft shadows
- **Typography:** Bold geometric sans-serif
- **Mood:** Professional, trustworthy, modern

### luxury-brand
- **Colors:** #1A1A1A, #C9A96E, #FAFAF5 (black + gold + cream)
- **Style:** Elegant high-end photography, rich textures, deep contrast
- **Typography:** Thin elegant serif, generous letter-spacing
- **Mood:** Exclusive, sophisticated, aspirational

### editorial-magazine
- **Colors:** #000000, #FFFFFF, #FF3B30 (black + white + accent red)
- **Style:** Bold editorial photography, strong geometric composition
- **Typography:** Condensed all-caps sans-serif headlines
- **Mood:** Bold, provocative, contemporary

## How Presets Merge into Reasoning Brief

When a preset is active, Claude uses its values as defaults for the Reasoning Brief:
1. **Colors** → inform palette descriptions in Context and Style components
2. **Style** → becomes the base for the Style component
3. **Typography** → used for any text rendering
4. **Lighting** → becomes the base for the Lighting component
5. **Mood** → influences Action and Context components

User instructions always override preset values. If a user says "make it dark"
but the preset has bright lighting, follow the user's instruction.

## Managing Presets

```bash
# List presets
presets.py list

# Show details
presets.py show tech-saas

# Create interactively (Claude fills in details from conversation)
presets.py create NAME --colors "#hex,#hex" --style "..." --mood "..."

# Delete
presets.py delete NAME --confirm
```
```

## File: `extensions/banana/references/prompt-engineering.md`
```markdown
# Prompt Engineering Reference: Claude Banana

> Load this on-demand when constructing complex prompts or when the user
> asks about prompt techniques. Do NOT load at startup.
>
> Aligned with Google's March 2026 "Ultimate Prompting Guide" for Gemini image generation.

## The 6-Component Reasoning Brief

Every image prompt should contain these components, written as natural
narrative paragraphs, NEVER as comma-separated keyword lists.

### 1. Subject
The main focus of the image. Describe with physical specificity.

**Good:** "A weathered Japanese ceramicist in his 70s, deep sun-etched
wrinkles mapping decades of kiln work, calloused hands cradling a
freshly thrown tea bowl with an irregular, organic rim"

**Bad:** "old man, ceramic, bowl"

### 2. Action
What is happening. Movement, pose, gesture, state of being.

**Good:** "leaning forward with intense concentration, gently smoothing
the rim with a wet thumb, a thin trail of slip running down his wrist"

**Bad:** "making pottery"

### 3. Context
Environment, setting, temporal and spatial details.

**Good:** "inside a traditional wood-fired anagama kiln workshop,
stacked shelves of drying pots visible in the soft background, late
afternoon light filtering through rice paper screens"

**Bad:** "workshop, afternoon"

### 4. Composition
Camera angle, shot type, framing, spatial relationships.

**Good:** "intimate close-up shot from slightly below eye level,
shallow depth of field isolating the hands and bowl against the
soft bokeh of the workshop behind"

**Bad:** "close up"

### 5. Lighting
Light source, quality, direction, temperature, shadows.

**Good:** "warm directional light from a single high window camera-left,
creating gentle Rembrandt lighting on the face with a soft triangle
of light on the shadow-side cheek, deep warm shadows in the workshop"

**Bad:** "natural lighting"

### 6. Style
Art medium, aesthetic reference, technical photographic details.

**Good:** "captured with a Sony A7R IV, 85mm f/1.4 GM lens, Kodak Portra
400 color grading with lifted shadows and muted earth tones, reminiscent
of Dorothea Lange's documentary portraiture"

**Bad:** "photorealistic, 8K, masterpiece"

## Domain Mode Modifier Libraries

### Cinema Mode
**Camera specs:** RED V-Raptor, ARRI Alexa 65, Sony Venice 2, Blackmagic URSA
**Lenses:** Cooke S7/i, Zeiss Supreme Prime, Atlas Orion anamorphic
**Film stocks:** Kodak Vision3 500T (tungsten), Kodak Vision3 250D (daylight), Fuji Eterna Vivid
**Lighting setups:** three-point, chiaroscuro, Rembrandt, split, butterfly, rim/backlight
**Shot types:** establishing wide, medium close-up, extreme close-up, Dutch angle, overhead crane, Steadicam tracking
**Color grading:** teal and orange, desaturated cold, warm vintage, high-contrast noir

### Product Mode
**Surfaces:** polished marble, brushed concrete, raw linen, acrylic riser, gradient sweep
**Lighting:** softbox diffused, hard key with fill card, rim separation, tent lighting, light painting
**Angles:** 45-degree hero, flat lay, three-quarter, straight-on, worm's-eye
**Style refs:** Apple product photography, Aesop minimal, Bang & Olufsen clean, luxury cosmetics

### Portrait Mode
**Focal lengths:** 85mm (classic), 105mm (compression), 135mm (telephoto), 50mm (environmental)
**Apertures:** f/1.4 (dreamy bokeh), f/2.8 (subject-sharp), f/5.6 (environmental context)
**Pose language:** candid mid-gesture, direct-to-camera confrontational, profile silhouette, over-shoulder glance
**Skin/texture:** freckles visible, pores at macro distance, catch light in eyes, subsurface scattering

### Editorial/Fashion Mode
**Publication refs:** Vogue Italia, Harper's Bazaar, GQ, National Geographic, Kinfolk
**Styling notes:** layered textures, statement accessories, monochromatic palette, contrast patterns
**Locations:** marble staircase, rooftop at golden hour, industrial loft, desert dunes, neon-lit alley
**Poses:** power stance, relaxed editorial lean, movement blur, fabric in wind

### UI/Web Mode
**Styles:** flat vector, isometric 3D, line art, glassmorphism, neumorphism, material design
**Colors:** specify exact hex or descriptive palette (e.g., "cool blues #2563EB to #1E40AF")
**Sizing:** design at 2x for retina, specify exact pixel dimensions needed
**Backgrounds:** transparent (request solid white then post-process), gradient, solid color

### Logo Mode
**Construction:** geometric primitives, golden ratio, grid-based, negative space
**Typography:** bold sans-serif, elegant serif, custom lettermark, monogram
**Colors:** max 2-3 colors, works in monochrome, high contrast
**Output:** request on solid white background, post-process to transparent

### Landscape Mode
**Depth layers:** foreground interest, midground subject, background atmosphere
**Atmospherics:** fog, mist, haze, volumetric light rays, dust particles
**Time of day:** blue hour (pre-dawn), golden hour, magic hour (post-sunset), midnight blue
**Weather:** dramatic storm clouds, clearing after rain, snow-covered, sun-dappled

### Infographic Mode
**Layout:** modular sections, clear visual hierarchy, bento grid, flow top-to-bottom
**Text:** use quotes for exact text, descriptive font style, specify size hierarchy
**Data viz:** bar charts, pie charts, flow diagrams, timelines, comparison tables
**Colors:** high-contrast, accessible palette, consistent brand colors

### Abstract Mode
**Geometry:** fractals, voronoi tessellation, spirals, fibonacci, organic flow, crystalline
**Textures:** marble veining, fluid dynamics, smoke wisps, ink diffusion, watercolor bleed
**Color palettes:** analogous harmony, complementary clash, monochromatic gradient, neon-on-black
**Styles:** generative art, data visualization art, glitch, procedural, macro photography of materials

## Advanced Techniques

### Character Consistency (Multi-turn)
Use `gemini_chat` and maintain descriptive anchors:
- First turn: Generate character with exhaustive physical description
- Following turns: Reference "the same character" + repeat 2-3 key identifiers
- Key identifiers: hair color/style, distinctive clothing, facial feature

**Multi-image reference technique** (3.1 Flash):
- Provide up to 4-5 character reference images in the conversation
- Assign distinct names to each character ("Character A: the red-haired knight")
- Model preserves features across different angles, actions, and environments
- Works best when reference images show the character from multiple angles

### Style Transfer Without Reference Images
Describe the target style exhaustively instead of referencing an image:
```
Render this scene in the style of a 1950s travel poster: flat areas of
color in a limited palette of teal, coral, and cream. Bold geometric
shapes with visible paper texture. Hand-lettered title text with a
mid-century modern typeface feel.
```

### Text Rendering Tips
- Quote exact text: `with the text "OPEN DAILY" in bold condensed sans-serif`
- **25 characters or less**:this is the practical limit for reliable rendering
- **2-3 distinct phrases max**:more text fragments degrade quality
- Describe font characteristics, not font names
- Specify placement: "centered at the top third", "along the bottom edge"
- High contrast: light text on dark, or vice versa
- **Text-first hack:** Establish the text concept conversationally first ("I need a sign that says FRESH BREAD"), then generate. The model anchors on text mentioned early
- Expect creative font interpretations, not exact replication of described styles

### Positive Framing (No Negative Prompts)
Gemini does NOT support negative prompts. Rephrase exclusions:
- Instead of "no blur" → "sharp, in-focus, tack-sharp detail"
- Instead of "no people" → "empty, deserted, uninhabited"
- Instead of "no text" → "clean, uncluttered, text-free"
- Instead of "not dark" → "brightly lit, high-key lighting"

### Search-Grounded Generation
For images based on real-world data (weather, events, statistics),
Gemini can use Google Search grounding to incorporate live information.
Useful for infographics with current data.

**Three-part formula for search-grounded prompts:**
1. `[Source/Search request`:What to look up
2. `[Analytical task`:What to analyze or extract
3. `[Visual translation`:How to render it as an image

**Example:** "Search for the current top 5 programming languages by GitHub usage in 2026, analyze their relative popularity percentages, then generate a clean infographic bar chart with the language logos and percentages in a modern dark theme."

## Prompt Adaptation Rules

When adapting prompts from the claude-prompts database (Midjourney/DALL-E/etc.)
to Gemini's natural language format:

| Source Syntax | Gemini Equivalent |
|---------------|-------------------|
| `--ar 16:9` | Call `set_aspect_ratio("16:9")` separately |
| `--v 6`, `--style raw` | Remove - Gemini has no version/style flags |
| `--chaos 50` | Describe variety: "unexpected, surreal composition" |
| `--no trees` | Positive framing: "open clearing with no vegetation" |
| `(word:1.5)` weight | Descriptive emphasis: "prominently featuring [word]" |
| `8K, masterpiece, ultra-detailed` | Keep only "ultra-realistic, high resolution"; remove the rest |
| Comma-separated tags | Expand into descriptive narrative paragraphs |
| `shot on Hasselblad` | Keep - camera specs work well in Gemini |

## Common Prompt Mistakes

1. **Keyword stuffing**:stacking generic quality terms ("8K, masterpiece, best quality") adds nothing. Use only "ultra-realistic, high resolution" at the end
2. **Tag lists**:Gemini wants prose, not "red car, sunset, mountain, cinematic"
3. **Missing lighting**:The single biggest quality differentiator
4. **No composition direction**:Results in generic centered framing
5. **Vague style**:"make it look cool" vs specific art direction
6. **Ignoring aspect ratio**:Always set before generating
7. **Overlong prompts**:Diminishing returns past ~200 words; be precise, not verbose
8. **Text longer than ~25 characters**:Rendering degrades rapidly past this limit
9. **Burying key details at the end**:In long prompts, details placed last may be deprioritized; put critical specifics (exact text, key constraints) in the first third of the prompt
10. **Not iterating with follow-up prompts**:Use `gemini_chat` for progressive refinement instead of trying to get everything right in one generation

## Proven Prompt Templates

> Extracted from 2,500+ tested prompts. These patterns consistently produce
> high-quality results. Use them as starting points and adapt to the request.

### The Winning Formula (Weight Distribution)

| Component | Weight | What to include |
|-----------|--------|-----------------|
| **Subject** | 40% | Age, skin tone, hair color/style, eye color, body type, expression |
| **Styling** | 25% | Brand names, textures, fit, accessories, colors |
| **Environment** | 15% | Location + time of day + context details |
| **Camera** | 10% | Camera model + lens + focal length + shot type |
| **Lighting** | 10% | Quality, direction, color temperature, shadows |

### Instagram Ad / Social Media

**Pattern:** `[Subject with age/appearance] + [outfit with brand/texture] + [action verb] + [setting] + [camera spec] + [lighting] + [platform aesthetic]`

**Example (Product Placement):**
```
Hyper-realistic gym selfie of athletic 24yo influencer with glowing olive
skin, wearing crinkle-textured athleisure set in mauve. iPhone 16 Pro Max
front-facing portrait mode capturing sweat droplets on collarbones, hazel
eyes enhanced by gym LED lighting. Mirror reflection shows perfect form,
golden morning light through floor-to-ceiling windows. Frayed chestnut
ponytail with baby hairs, ultra-detailed skin texture, trending aesthetic.
```

**Example (Lifestyle Ad):**
```
A 24-year-old blonde fitness model in a high-energy sports drink
advertisement. Mid-run on a beach, wearing a vibrant orange sports bra
and black shorts, playful smile and sparkling blue eyes exuding vitality.
Bottle of the drink held in hand, waves crashing in background. Shot on
Nikon D850 with 70-200mm f/2.8 lens, natural light, fast shutter speed
capturing motion. Ultra-realistic skin texture, water droplets, product
label clearly visible.
```

**Example (Luxury Lifestyle):**
```
Gorgeous Instagram model wearing a designer silk gown, luxury rooftop
restaurant, golden hour lighting, champagne in hand, luxurious aspirational
lifestyle. Captured with Sony A7R IV, 85mm f/1.4 lens, shallow depth of
field, warm color grading.
```

### Product / Commercial Photography

**Pattern:** `[Product with brand/detail] + [dynamic elements] + [surface/setting] + "commercial photography for advertising campaign" + [lighting] + "high resolution"`

**Example (Beverage):**
```
Gatorade bottle with condensation dripping down the sides, surrounded by
lightning bolts and a burst of vibrant blue and orange light rays. The
Gatorade logo is prominently displayed on the bottle, with splashes of
water frozen in mid-air. Commercial food photography for an advertising
campaign, high resolution, high level of detail, vibrant complementary
colors.
```

**Example (Food):**
```
In and Out burger with layers of fresh lettuce, melted cheese, and pretzel
bun, placed on a white surface with the In and Out logo subtly glowing in
the background. Falling french fries and golden light, warm scene.
Commercial food photography for an advertising campaign, high resolution,
high level of detail, vibrant complementary colors.
```

### Fashion / Editorial

**Pattern:** `[Subject with ethnicity/age/features] + [outfit with texture/brand/cut] + [location] + [pose/action] + [camera + lens] + [lighting quality]`

**Example (Street Style):**
```
A 24-year-old female AI influencer posing confidently in an urban cityscape
during golden hour. Flawless sun-kissed skin, long wavy brown hair, deep
green eyes. Wearing a chic streetwear outfit: oversized beige blazer,
white top, high-waisted jeans. Captured with Sony A7R IV at 85mm f/1.4,
shallow depth of field with warm golden bokeh.
```

**Example (High Fashion):**
```
Stunning 24-year-old woman, long platinum blonde hair, radiant skin,
piercing blue eyes, dressed in a chic pastel blazer with a modern
minimalist aesthetic, soft sunlight glow, high-end fashion appeal.
Shot on Canon EOS R5, 85mm f/1.2 lens.
```

**Example (Avant-Garde):**
```
A blonde fitness model transformed into a runway-ready fashion icon,
wearing a bold avant-garde outfit: cropped leather jacket with neon pink
accents, paired with high-waisted athletic shorts and knee-high boots.
Captured mid-stride on a minimalist white runway, playful twinkle in her
eye, dramatic studio lighting from above.
```

### SaaS / Tech Marketing

**Pattern:** `[UI mockup or abstract visual] + "on [dark/light] background" + [specific colors with hex] + [typography description] + "clean, premium SaaS aesthetic" + [glassmorphism/gradient/glow effects]`

**Example (Dashboard Hero):**
```
A floating glassmorphism UI card on a deep charcoal background showing a
content analytics dashboard with a rising line graph in teal (#14B8A6),
bar charts in coral (#F97316), and a circular progress indicator at 94%.
Subtle grid lines, frosted glass effect with 20% opacity, teal glow
bleeding from the card edges. Clean premium SaaS aesthetic, no text
smaller than headline size.
```

**Example (Feature Highlight):**
```
An isometric 3D illustration of interconnected data nodes on a dark navy
background. Each node is a glowing teal sphere connected by thin luminous
lines, forming a constellation pattern. One central node pulses brighter
with radiating rings. Modern tech illustration style with subtle depth
of field, volumetric lighting from below.
```

**Example (Comparison/Before-After):**
```
Split-screen image: left side shows a cluttered, dim workspace with
scattered papers, red error indicators, and a frustrated expression
conveyed through a cracked coffee mug and tangled cables. Right side
shows a clean, organized dashboard interface glowing in teal and white
on a dark background, with smooth flowing lines and checkmarks. A sharp
vertical dividing line separates chaos from clarity.
```

### Logo / Branding

**Pattern:** `[Product/bottle/item] + "with [brand element] prominently displayed" + [dynamic visual elements] + "commercial photography" + [lighting style] + "high resolution, vibrant complementary colors"`

**Example:**
```
A sleek matte black bottle with a minimal white logo mark centered on the
label, surrounded by swirling gradient ribbons of teal and coral light.
The bottle sits on a reflective dark surface, sharp studio rim lighting
separating it from the background. Product photography for luxury
branding, high resolution, dramatic contrast.
```

### Key Tactics That Make Prompts Work

1. **Name real cameras**:"Sony A7R IV", "Canon EOS R5", "iPhone 16 Pro Max" anchor realism
2. **Specify exact lens**:"85mm f/1.4" gives the model precise depth-of-field information
3. **Use age + ethnicity + features**:"24yo with olive skin, hazel eyes" beats "a person"
4. **Name brands for styling**:"Lululemon mat", "Tom Ford suit" triggers specific visual associations
5. **Include micro-details**:"sweat droplets on collarbones", "baby hairs stuck to neck"
6. **Add platform context**:"Instagram aesthetic", "commercial photography for advertising"
7. **Describe textures**:"crinkle-textured", "metallic silver", "frosted glass"
8. **Use action verbs**:"mid-run", "posing confidently", "captured mid-stride"
9. **End with "ultra-realistic, high resolution"**:these two specific anchors help on Gemini. Avoid generic stacking like "8K, masterpiece, best quality" which adds no value
10. **For products, say "prominently displayed"**:ensures the product/logo isn't hidden

### Anti-Patterns (What NOT to Do)

- **"A dark-themed Instagram ad showing..."**:too meta, describes the concept not the image
- **"A sleek SaaS dashboard visualization..."**:abstract, no visual anchors
- **"Modern, clean, professional..."**:vague adjectives that mean nothing to the model
- **"A bold call to action with..."**:describes marketing intent, not visual content
- **Describing what the viewer should feel**:instead, describe what creates that feeling

## Safety Filter Rephrase Strategies

Gemini's safety filters (Layer 2: server-side output filter) cannot be disabled.
When a prompt is blocked, the only path forward is rephrasing.

### Common Trigger Categories

| Category | Triggers on | Rephrase approach |
|----------|------------|-------------------|
| Violence/weapons | Combat, blood, injuries, firearms | Use metaphor or aftermath: "battle-worn" → "weathered veteran" |
| Medical/gore | Surgery, wounds, anatomical detail | Abstract or clinical: "open wound" → "medical illustration" |
| Real public figures | Named celebrities, politicians | Use archetypes: "Elon Musk" → "a tech entrepreneur in a minimalist office" |
| Children + risk | Minors in any ambiguous context | Add safety context: specify educational, family, or playful framing |
| NSFW/suggestive | Revealing clothing, intimate poses | Use artistic framing: "fashion editorial, fully clothed, editorial pose" |

### Rephrase Patterns

1. **Abstraction**:Replace specific dangerous elements with abstract concepts
2. **Artistic framing**:Frame content as art, editorial, or documentary
3. **Metaphor**:Use symbolic language instead of literal descriptions
4. **Positive emphasis**:Describe what IS present, not what's dangerous
5. **Context shift**:Move from threatening to educational/professional context

### Example Rephrases

| Blocked prompt | Successful rephrase |
|----------------|---------------------|
| "a soldier in combat firing a rifle" | "a determined soldier standing guard at dawn, rifle slung over shoulder, morning mist over the outpost" |
| "a scary horror monster" | "a fantastical creature from a dark fairy tale, intricate organic textures, bioluminescent accents, concept art style" |
| "dog in a fight" | "a friendly golden retriever playing energetically in a sunny park, action shot, joyful expression" |
| "medical surgery scene" | "a clean modern operating room viewed from the observation gallery, soft blue surgical lights, professional documentary style" |
| "celebrity portrait of [name]" | "a distinguished middle-aged man in a tailored navy suit, warm studio lighting, editorial portrait style" |

### Key Principle

Layer 2 (output filter) analyzes the generated image, not just the prompt.
Even well-phrased prompts can be blocked if the model's interpretation triggers
the output filter. When this happens, try shifting the visual concept further
from the trigger rather than just changing words.
```

## File: `extensions/banana/references/seo-image-presets.md`
```markdown
# SEO Image Presets

Pre-configured presets for common SEO image use cases. These map to banana's
preset format (see `references/presets.md` for schema details).

## Preset Templates

### og-default:Standard OG/Social Preview

```json
{
  "name": "og-default",
  "description": "Clean, professional OG image for social sharing",
  "aspect_ratio": "16:9",
  "resolution": "1K",
  "domain_mode": "Product",
  "style": {
    "colors": ["#FFFFFF", "#F5F5F5"],
    "mood": "Professional, clean, trustworthy",
    "lighting": "Bright, even studio lighting with soft shadows",
    "typography": "Modern sans-serif if text needed"
  },
  "post_processing": "magick output.png -resize 1200x630^ -gravity center -extent 1200x630 output-og.webp"
}
```

### blog-hero:Widescreen Blog Hero Image

```json
{
  "name": "blog-hero",
  "description": "Dramatic widescreen hero for blog posts",
  "aspect_ratio": "16:9",
  "resolution": "2K",
  "domain_mode": "Cinema",
  "style": {
    "colors": ["contextual"],
    "mood": "Dramatic, atmospheric, editorial",
    "lighting": "Golden hour or moody blue hour, directional",
    "typography": "None:image only"
  },
  "post_processing": "magick output.png -quality 85 output-hero.webp"
}
```

### product-white:E-commerce Product Shot

```json
{
  "name": "product-white",
  "description": "Clean white background product photography",
  "aspect_ratio": "4:3",
  "resolution": "2K",
  "domain_mode": "Product",
  "style": {
    "colors": ["#FFFFFF"],
    "mood": "Clean, professional, catalog-ready",
    "lighting": "360-degree soft studio lighting, minimal shadows",
    "typography": "None"
  },
  "prompt_suffix": "Studio product photography, clean white background, professional catalog shot, high resolution",
  "post_processing": "magick output.png -fuzz 5% -transparent white output-transparent.png"
}
```

### social-square:Social Media Square

```json
{
  "name": "social-square",
  "description": "1:1 square image for social media platforms",
  "aspect_ratio": "1:1",
  "resolution": "1K",
  "domain_mode": "UI/Web",
  "style": {
    "colors": ["brand-contextual"],
    "mood": "Engaging, scroll-stopping, platform-native",
    "lighting": "Bright, even, high-contrast",
    "typography": "Bold sans-serif if text needed, under 25 characters"
  }
}
```

### infographic-vertical:Data-Heavy Infographic

```json
{
  "name": "infographic-vertical",
  "description": "Tall vertical infographic for data visualization",
  "aspect_ratio": "2:3",
  "resolution": "4K",
  "domain_mode": "Infographic",
  "style": {
    "colors": ["brand-contextual", "data-visualization palette"],
    "mood": "Informative, structured, authoritative",
    "lighting": "Flat, even, no dramatic shadows",
    "typography": "Clear hierarchy:headline, subheads, body, captions"
  },
  "notes": "Use thinking: high for better text rendering accuracy"
}
```

### favicon-mark:Favicon / App Icon

```json
{
  "name": "favicon-mark",
  "description": "Minimal iconic mark for favicon or app icon",
  "aspect_ratio": "1:1",
  "resolution": "512",
  "domain_mode": "Logo",
  "style": {
    "colors": ["2-3 brand colors max"],
    "mood": "Minimal, recognizable, scalable",
    "lighting": "Flat, no shadows",
    "typography": "Single letter or symbol only"
  },
  "post_processing": "magick output.png -resize 32x32 favicon.ico && magick output.png -resize 180x180 apple-touch-icon.png"
}
```

## Creating Custom Presets

Users can create their own presets:
```bash
python3 ~/.claude/skills/seo-image-gen/scripts/presets.py create my-brand
```

This creates `~/.banana/presets/my-brand.json` with the full schema.
Custom presets override SEO defaults when specified.

## Preset Selection Logic

1. If user specifies a use case command (og, hero, product), load the matching preset
2. If user mentions a brand preset name, load from `~/.banana/presets/`
3. Brand presets override SEO presets for colors, mood, and typography
4. SEO presets always provide aspect ratio and resolution defaults
```

## File: `extensions/banana/scripts/batch.py`
```python
#!/usr/bin/env python3
"""Claude Banana - CSV Batch Workflow

Parse a CSV file of image generation requests and output a structured plan.
Claude then executes each row via MCP.

Usage:
    batch.py --csv path/to/file.csv

CSV columns:
    prompt (required), ratio, resolution, model, preset (all optional)

Example CSV:
    prompt,ratio,resolution
    "coffee shop hero image",16:9,2K
    "team photo placeholder",1:1,1K
    "product shot on marble",4:3,2K
"""

import argparse
import csv
import json
import sys
from pathlib import Path

# Inline pricing for estimates
PRICING = {
    "gemini-3.1-flash-image-preview": {"512": 0.020, "1K": 0.039, "2K": 0.078, "4K": 0.156},
    "gemini-2.5-flash-image": {"512": 0.020, "1K": 0.039},
}
DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
DEFAULT_RESOLUTION = "1K"
DEFAULT_RATIO = "1:1"


def estimate_cost(model, resolution):
    """Estimate cost for a single image."""
    model_pricing = PRICING.get(model, PRICING[DEFAULT_MODEL])
    return model_pricing.get(resolution, model_pricing.get("1K", 0.039))


def main():
    parser = argparse.ArgumentParser(description="Parse CSV batch and output generation plan")
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    args = parser.parse_args()

    csv_path = Path(args.csv).resolve()
    if not csv_path.exists():
        print(json.dumps({"error": True, "message": f"CSV not found: {csv_path}"}))
        sys.exit(1)

    rows = []
    errors = []

    try:
        with open(csv_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or "prompt" not in reader.fieldnames:
                print(json.dumps({"error": True, "message": "CSV must have a 'prompt' column header"}))
                sys.exit(1)
            for i, row in enumerate(reader, start=2):  # Line 2+ (1 is header)
                prompt = row.get("prompt", "").strip()
                if not prompt:
                    errors.append(f"Row {i}: missing prompt")
                    continue

                rows.append({
                    "row": i,
                    "prompt": prompt,
                    "ratio": row.get("ratio", "").strip() or DEFAULT_RATIO,
                    "resolution": row.get("resolution", "").strip() or DEFAULT_RESOLUTION,
                    "model": row.get("model", "").strip() or DEFAULT_MODEL,
                    "preset": row.get("preset", "").strip() or None,
                })
    except (csv.Error, UnicodeDecodeError) as e:
        print(json.dumps({"error": True, "message": f"Failed to parse CSV: {e}"}))
        sys.exit(1)

    if errors:
        print("Validation errors:")
        for e in errors:
            print(f"  - {e}")
        if not rows:
            sys.exit(1)
        print()

    # Cost estimate
    total_cost = sum(estimate_cost(r["model"], r["resolution"]) for r in rows)

    # Output structured JSON for Claude to consume
    print(json.dumps({"rows": rows, "total_count": len(rows),
                       "estimated_cost": round(total_cost, 3),
                       "errors": errors}, indent=2))


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/cost_tracker.py`
```python
#!/usr/bin/env python3
"""Claude Banana - Cost Tracker

Track image generation costs, view summaries, and estimate batch costs.

Usage:
    cost_tracker.py log --model MODEL --resolution RES --prompt "summary"
    cost_tracker.py summary
    cost_tracker.py today
    cost_tracker.py estimate --model MODEL --resolution RES --count N
    cost_tracker.py reset --confirm
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LEDGER_PATH = Path.home() / ".banana" / "costs.json"

# Cost per image in USD (approximate, based on ~1,290 output tokens)
PRICING = {
    "gemini-3.1-flash-image-preview": {
        "512": 0.020,
        "1K": 0.039,
        "2K": 0.078,
        "4K": 0.156,
    },
    "gemini-2.5-flash-image": {
        "512": 0.020,
        "1K": 0.039,
    },
}

# Batch API gets 50% discount
BATCH_DISCOUNT = 0.5


def _load_ledger():
    """Load the cost ledger from disk."""
    if not LEDGER_PATH.exists():
        return {"total_cost": 0.0, "total_images": 0, "entries": [], "daily": {}}
    with open(LEDGER_PATH, "r") as f:
        return json.load(f)


def _save_ledger(ledger):
    """Save the cost ledger to disk."""
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2)


def _lookup_cost(model, resolution, batch=False):
    """Look up cost for a model+resolution combination."""
    model_pricing = PRICING.get(model)
    if not model_pricing:
        # Try partial match
        for key in PRICING:
            if key in model or model in key:
                model_pricing = PRICING[key]
                break
    if not model_pricing:
        print(f"Warning: Unknown model '{model}', using 3.1 Flash pricing", file=sys.stderr)
        model_pricing = PRICING["gemini-3.1-flash-image-preview"]

    valid_resolutions = {"512", "1K", "2K", "4K"}
    if resolution not in valid_resolutions:
        print(f"Warning: Unknown resolution '{resolution}', using 1K pricing", file=sys.stderr)
    cost = model_pricing.get(resolution, model_pricing.get("1K", 0.039))
    if batch:
        cost *= BATCH_DISCOUNT
    return cost


def cmd_log(args):
    """Log a generation to the ledger."""
    ledger = _load_ledger()
    cost = _lookup_cost(args.model, args.resolution, getattr(args, "batch", False))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    entry = {
        "ts": now,
        "model": args.model,
        "res": args.resolution,
        "cost": cost,
        "prompt": args.prompt[:100],
    }

    ledger["entries"].append(entry)
    ledger["total_cost"] = round(ledger["total_cost"] + cost, 4)
    ledger["total_images"] += 1

    if today not in ledger["daily"]:
        ledger["daily"][today] = {"count": 0, "cost": 0.0}
    ledger["daily"][today]["count"] += 1
    ledger["daily"][today]["cost"] = round(ledger["daily"][today]["cost"] + cost, 4)

    _save_ledger(ledger)
    print(json.dumps({"logged": True, "cost": cost, "total_cost": ledger["total_cost"],
                       "total_images": ledger["total_images"]}))


def cmd_summary(args):
    """Show cost summary."""
    ledger = _load_ledger()
    print(f"Total images: {ledger['total_images']}")
    print(f"Total cost:   ${ledger['total_cost']:.3f}")
    print()

    daily = ledger.get("daily", {})
    if daily:
        # Show last 7 days
        sorted_days = sorted(daily.keys(), reverse=True)[:7]
        print("Last 7 days:")
        for day in sorted_days:
            d = daily[day]
            print(f"  {day}: {d['count']} images, ${d['cost']:.3f}")
    else:
        print("No usage recorded yet.")


def cmd_today(args):
    """Show today's usage."""
    ledger = _load_ledger()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    daily = ledger.get("daily", {}).get(today, {"count": 0, "cost": 0.0})
    print(f"Today ({today}): {daily['count']} images, ${daily['cost']:.3f}")


def cmd_estimate(args):
    """Estimate cost for a batch."""
    cost_per = _lookup_cost(args.model, args.resolution, getattr(args, "batch", False))
    total = round(cost_per * args.count, 3)
    print(f"Model:      {args.model}")
    print(f"Resolution: {args.resolution}")
    print(f"Count:      {args.count}")
    print(f"Cost/image: ${cost_per:.3f}")
    print(f"Total est:  ${total:.3f}")
    if not getattr(args, "batch", False):
        batch_total = round(cost_per * BATCH_DISCOUNT * args.count, 3)
        print(f"Batch est:  ${batch_total:.3f} (50% discount)")


def cmd_reset(args):
    """Reset the ledger."""
    if not args.confirm:
        print("Error: Pass --confirm to reset the cost ledger.", file=sys.stderr)
        sys.exit(1)
    _save_ledger({"total_cost": 0.0, "total_images": 0, "entries": [], "daily": {}})
    print("Cost ledger reset.")


def main():
    parser = argparse.ArgumentParser(description="Claude Banana Cost Tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    # log
    p_log = sub.add_parser("log", help="Log a generation")
    p_log.add_argument("--model", required=True, help="Model ID")
    p_log.add_argument("--resolution", required=True, help="Resolution (512, 1K, 2K, 4K)")
    p_log.add_argument("--prompt", required=True, help="Brief prompt description")
    p_log.add_argument("--batch", action="store_true", help="Batch API (50%% discount)")

    # summary
    sub.add_parser("summary", help="Show cost summary")

    # today
    sub.add_parser("today", help="Show today's usage")

    # estimate
    p_est = sub.add_parser("estimate", help="Estimate batch cost")
    p_est.add_argument("--model", required=True, help="Model ID")
    p_est.add_argument("--resolution", required=True, help="Resolution (512, 1K, 2K, 4K)")
    p_est.add_argument("--count", required=True, type=int, help="Number of images")
    p_est.add_argument("--batch", action="store_true", help="Use batch pricing (50%% discount)")

    # reset
    p_reset = sub.add_parser("reset", help="Reset cost ledger")
    p_reset.add_argument("--confirm", action="store_true", help="Confirm reset")

    args = parser.parse_args()
    cmds = {"log": cmd_log, "summary": cmd_summary, "today": cmd_today,
            "estimate": cmd_estimate, "reset": cmd_reset}
    cmds[args.command](args)


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/edit.py`
```python
#!/usr/bin/env python3
"""Claude Banana - Direct API Fallback: Image Editing

Edit images via Gemini REST API when MCP is unavailable.
Uses only Python stdlib (no pip dependencies).

Usage:
    edit.py --image path/to/image.png --prompt "remove the background"
            [--model MODEL] [--api-key KEY]
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
OUTPUT_DIR = Path.home() / "Documents" / "nanobanana_generated"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def edit_image(image_path, prompt, model, api_key):
    """Call Gemini API to edit an image."""
    image_path = Path(image_path).resolve()
    if not image_path.exists():
        print(json.dumps({"error": True, "message": f"Image not found: {image_path}"}))
        sys.exit(1)

    # Read and encode image
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Determine MIME type
    suffix = image_path.suffix.lower()
    mime_types = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                  ".webp": "image/webp", ".gif": "image/gif"}
    mime_type = mime_types.get(suffix, "image/png")

    url = f"{API_BASE}/{model}:generateContent?key={api_key}"

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {"inlineData": {"mimeType": mime_type, "data": image_b64}},
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
        },
    }

    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print(json.dumps({"error": True, "status": e.code, "message": error_body}))
        sys.exit(1)
    except urllib.error.URLError as e:
        print(json.dumps({"error": True, "message": str(e.reason)}))
        sys.exit(1)

    # Extract image from response
    candidates = result.get("candidates", [])
    if not candidates:
        finish_reason = result.get("promptFeedback", {}).get("blockReason", "UNKNOWN")
        print(json.dumps({"error": True, "message": f"No candidates returned. Reason: {finish_reason}"}))
        sys.exit(1)

    parts = candidates[0].get("content", {}).get("parts", [])
    image_data = None
    text_response = ""

    for part in parts:
        if "inlineData" in part:
            image_data = part["inlineData"]["data"]
        elif "text" in part:
            text_response = part["text"]

    if not image_data:
        finish_reason = candidates[0].get("finishReason", "UNKNOWN")
        print(json.dumps({"error": True, "message": f"No image in response. finishReason: {finish_reason}"}))
        sys.exit(1)

    # Save image
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"banana_edit_{timestamp}.png"
    output_path = (OUTPUT_DIR / filename).resolve()

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    return {
        "path": str(output_path),
        "model": model,
        "source": str(image_path),
        "text": text_response,
    }


def main():
    parser = argparse.ArgumentParser(description="Edit images via Gemini REST API")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--prompt", required=True, help="Edit instruction")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--api-key", default=None, help="Google AI API key (or set GOOGLE_AI_API_KEY env)")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print(json.dumps({"error": True, "message": "No API key. Set GOOGLE_AI_API_KEY env or pass --api-key"}))
        sys.exit(1)

    result = edit_image(
        image_path=args.image,
        prompt=args.prompt,
        model=args.model,
        api_key=api_key,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/generate.py`
```python
#!/usr/bin/env python3
"""Claude Banana - Direct API Fallback: Image Generation

Generate images via Gemini REST API when MCP is unavailable.
Uses only Python stdlib (no pip dependencies).

Usage:
    generate.py --prompt "a cat in space" [--aspect-ratio 16:9] [--resolution 1K]
                [--model MODEL] [--api-key KEY] [--thinking LEVEL] [--image-only]
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
DEFAULT_RESOLUTION = "1K"
DEFAULT_RATIO = "1:1"
OUTPUT_DIR = Path.home() / "Documents" / "nanobanana_generated"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

VALID_RATIOS = {"1:1", "16:9", "9:16", "4:3", "3:4", "2:3", "3:2",
                "4:5", "5:4", "1:4", "4:1", "1:8", "8:1", "21:9"}
VALID_RESOLUTIONS = {"512", "1K", "2K", "4K"}


def generate_image(prompt, model, aspect_ratio, resolution, api_key,
                   thinking_level=None, image_only=False):
    """Call Gemini API to generate an image."""
    url = f"{API_BASE}/{model}:generateContent?key={api_key}"

    modalities = ["IMAGE"] if image_only else ["TEXT", "IMAGE"]
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": modalities,
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": resolution,
            },
        },
    }

    if thinking_level:
        body["generationConfig"]["thinkingConfig"] = {"thinkingLevel": thinking_level}

    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print(json.dumps({"error": True, "status": e.code, "message": error_body}))
        sys.exit(1)
    except urllib.error.URLError as e:
        print(json.dumps({"error": True, "message": str(e.reason)}))
        sys.exit(1)

    # Extract image from response
    candidates = result.get("candidates", [])
    if not candidates:
        finish_reason = result.get("promptFeedback", {}).get("blockReason", "UNKNOWN")
        print(json.dumps({"error": True, "message": f"No candidates returned. Reason: {finish_reason}"}))
        sys.exit(1)

    parts = candidates[0].get("content", {}).get("parts", [])
    image_data = None
    text_response = ""

    for part in parts:
        if "inlineData" in part:
            image_data = part["inlineData"]["data"]
        elif "text" in part:
            text_response = part["text"]

    if not image_data:
        finish_reason = candidates[0].get("finishReason", "UNKNOWN")
        print(json.dumps({"error": True, "message": f"No image in response. finishReason: {finish_reason}"}))
        sys.exit(1)

    # Save image
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"banana_{timestamp}.png"
    output_path = (OUTPUT_DIR / filename).resolve()

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    return {
        "path": str(output_path),
        "model": model,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "text": text_response,
    }


def main():
    parser = argparse.ArgumentParser(description="Generate images via Gemini REST API")
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--aspect-ratio", default=DEFAULT_RATIO, help=f"Aspect ratio (default: {DEFAULT_RATIO})")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION, help=f"Resolution: 512, 1K, 2K, 4K (default: {DEFAULT_RESOLUTION})")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--api-key", default=None, help="Google AI API key (or set GOOGLE_AI_API_KEY env)")
    parser.add_argument("--thinking", default=None, choices=["minimal", "low", "medium", "high"], help="Thinking level")
    parser.add_argument("--image-only", action="store_true", help="Return image only (no text)")

    args = parser.parse_args()

    if args.aspect_ratio not in VALID_RATIOS:
        print(json.dumps({"error": True, "message": f"Invalid aspect ratio '{args.aspect_ratio}'. Valid: {sorted(VALID_RATIOS)}"}))
        sys.exit(1)

    if args.resolution not in VALID_RESOLUTIONS:
        print(json.dumps({"error": True, "message": f"Invalid resolution '{args.resolution}'. Valid: {sorted(VALID_RESOLUTIONS)}"}))
        sys.exit(1)

    api_key = args.api_key or os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print(json.dumps({"error": True, "message": "No API key. Set GOOGLE_AI_API_KEY env or pass --api-key"}))
        sys.exit(1)

    result = generate_image(
        prompt=args.prompt,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        api_key=api_key,
        thinking_level=args.thinking,
        image_only=args.image_only,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/presets.py`
```python
#!/usr/bin/env python3
"""Claude Banana - Brand/Style Presets

Manage reusable brand and style presets for consistent image generation.

Usage:
    presets.py list
    presets.py show NAME
    presets.py create NAME --colors "#hex,#hex" --style "..." [options]
    presets.py delete NAME --confirm
"""

import argparse
import json
import re
import sys
from pathlib import Path

PRESETS_DIR = Path.home() / ".banana" / "presets"


def _ensure_dir():
    """Ensure presets directory exists."""
    PRESETS_DIR.mkdir(parents=True, exist_ok=True)


def _sanitize_name(name):
    """Sanitize preset name to prevent path traversal."""
    # Strip path separators and keep only safe characters
    safe = re.sub(r'[^a-zA-Z0-9_\-]', '', name)
    if not safe:
        print("Error: Preset name must contain only letters, numbers, hyphens, and underscores.", file=sys.stderr)
        sys.exit(1)
    return safe


def _preset_path(name):
    """Get path for a preset file."""
    safe_name = _sanitize_name(name)
    return PRESETS_DIR / f"{safe_name}.json"


def _load_preset(name):
    """Load a preset by name."""
    path = _preset_path(name)
    if not path.exists():
        print(f"Error: Preset '{name}' not found.", file=sys.stderr)
        sys.exit(1)
    with open(path, "r") as f:
        return json.load(f)


def cmd_list(args):
    """List available presets."""
    _ensure_dir()
    presets = sorted(PRESETS_DIR.glob("*.json"))
    if not presets:
        print("No presets found. Create one with: presets.py create NAME --style \"...\"")
        return
    print(f"Available presets ({len(presets)}):\n")
    for p in presets:
        try:
            with open(p, "r") as f:
                data = json.load(f)
            desc = data.get("description", "No description")
            print(f"  {p.stem:20s} - {desc}")
        except (json.JSONDecodeError, KeyError):
            print(f"  {p.stem:20s} - (invalid preset file)")


def cmd_show(args):
    """Show full preset details."""
    preset = _load_preset(args.name)
    print(json.dumps(preset, indent=2))


def cmd_create(args):
    """Create a new preset."""
    _ensure_dir()
    path = _preset_path(args.name)
    if path.exists():
        print(f"Error: Preset '{args.name}' already exists. Use a different name.", file=sys.stderr)
        sys.exit(1)

    colors = [c.strip() for c in args.colors.split(",")] if args.colors else []

    preset = {
        "name": args.name,
        "description": args.description or f"Custom preset: {args.name}",
        "colors": colors,
        "style": args.style or "",
        "typography": args.typography or "",
        "lighting": args.lighting or "",
        "mood": args.mood or "",
        "default_ratio": args.ratio or "16:9",
        "default_resolution": args.resolution or "2K",
    }

    with open(path, "w") as f:
        json.dump(preset, f, indent=2)

    print(f"Preset '{args.name}' created at {path}")
    print(json.dumps(preset, indent=2))


def cmd_delete(args):
    """Delete a preset."""
    if not args.confirm:
        print("Error: Pass --confirm to delete the preset.", file=sys.stderr)
        sys.exit(1)
    path = _preset_path(args.name)
    if not path.exists():
        print(f"Error: Preset '{args.name}' not found.", file=sys.stderr)
        sys.exit(1)
    path.unlink()
    print(f"Preset '{args.name}' deleted.")


def main():
    parser = argparse.ArgumentParser(description="Claude Banana Brand/Style Presets")
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    sub.add_parser("list", help="List available presets")

    # show
    p_show = sub.add_parser("show", help="Show preset details")
    p_show.add_argument("name", help="Preset name")

    # create
    p_create = sub.add_parser("create", help="Create a new preset")
    p_create.add_argument("name", help="Preset name (e.g., tech-saas, luxury-brand)")
    p_create.add_argument("--colors", default="", help="Comma-separated hex colors")
    p_create.add_argument("--style", default="", help="Visual style description")
    p_create.add_argument("--typography", default="", help="Typography description")
    p_create.add_argument("--lighting", default="", help="Lighting description")
    p_create.add_argument("--mood", default="", help="Mood/emotion description")
    p_create.add_argument("--description", default="", help="Brief preset description")
    p_create.add_argument("--ratio", default="16:9", help="Default aspect ratio")
    p_create.add_argument("--resolution", default="2K", help="Default resolution")

    # delete
    p_delete = sub.add_parser("delete", help="Delete a preset")
    p_delete.add_argument("name", help="Preset name")
    p_delete.add_argument("--confirm", action="store_true", help="Confirm deletion")

    args = parser.parse_args()
    cmds = {"list": cmd_list, "show": cmd_show, "create": cmd_create, "delete": cmd_delete}
    cmds[args.command](args)


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/setup_mcp.py`
```python
#!/usr/bin/env python3
"""
Setup script for Claude Banana MCP server in Claude Code.

Configures @ycse/nanobanana-mcp in Claude Code's settings.json
with the user's Google AI API key.

Usage:
    python3 setup_mcp.py                    # Interactive (prompts for key)
    python3 setup_mcp.py --key YOUR_KEY     # Non-interactive
    python3 setup_mcp.py --check            # Verify existing setup
    python3 setup_mcp.py --remove           # Remove MCP config
    python3 setup_mcp.py --help             # Show usage
"""

import json
import sys
import os
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
MCP_NAME = "nanobanana-mcp"
MCP_PACKAGE = "@ycse/nanobanana-mcp"
DEFAULT_MODEL = "gemini-3.1-flash-image-preview"


def load_settings() -> dict:
    """Load Claude Code settings.json."""
    if not SETTINGS_PATH.exists():
        return {}
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)


def save_settings(settings: dict) -> None:
    """Save Claude Code settings.json."""
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
    print(f"Settings saved to {SETTINGS_PATH}")


def check_setup() -> bool:
    """Check if MCP is already configured."""
    settings = load_settings()
    servers = settings.get("mcpServers", {})
    if MCP_NAME in servers:
        env = servers[MCP_NAME].get("env", {})
        key = env.get("GOOGLE_AI_API_KEY", "")
        masked = key[:8] + "..." + key[-4:] if len(key) > 12 else "(not set)"
        print(f"MCP server '{MCP_NAME}' is configured.")
        print(f"  Package: {MCP_PACKAGE}")
        print(f"  API Key: {masked}")
        print(f"  Model:   {env.get('NANOBANANA_MODEL', DEFAULT_MODEL)}")
        return True
    print(f"MCP server '{MCP_NAME}' is NOT configured.")
    return False


def remove_mcp() -> None:
    """Remove MCP configuration."""
    settings = load_settings()
    servers = settings.get("mcpServers", {})
    if MCP_NAME in servers:
        del servers[MCP_NAME]
        settings["mcpServers"] = servers
        save_settings(settings)
        print(f"Removed '{MCP_NAME}' from Claude Code settings.")
    else:
        print(f"'{MCP_NAME}' not found in settings.")


def setup_mcp(api_key: str) -> None:
    """Configure MCP server in Claude Code settings."""
    if not api_key or not api_key.strip():
        print("Error: API key cannot be empty.")
        sys.exit(1)

    api_key = api_key.strip()
    settings = load_settings()

    if "mcpServers" not in settings:
        settings["mcpServers"] = {}

    settings["mcpServers"][MCP_NAME] = {
        "command": "npx",
        "args": ["-y", MCP_PACKAGE],
        "env": {
            "GOOGLE_AI_API_KEY": api_key,
            "NANOBANANA_MODEL": DEFAULT_MODEL,
        },
    }

    save_settings(settings)
    print(f"\nMCP server '{MCP_NAME}' configured successfully!")
    print(f"  Package: {MCP_PACKAGE}")
    print(f"  Model:   {DEFAULT_MODEL}")
    print(f"\nRestart Claude Code for changes to take effect.")
    print(f"Generated images will be saved to: ~/Documents/nanobanana_generated/")


def main() -> None:
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print("Usage: python3 setup_mcp.py [OPTIONS]")
        print()
        print("Options:")
        print("  --key KEY        Provide API key non-interactively")
        print("  --check          Verify existing setup")
        print("  --remove         Remove MCP configuration")
        print("  --help, -h       Show this help message")
        print()
        print("Get a free API key at: https://aistudio.google.com/apikey")
        sys.exit(0)

    if "--check" in args:
        check_setup()
        return

    if "--remove" in args:
        remove_mcp()
        return

    # Get API key
    api_key = None
    for i, arg in enumerate(args):
        if arg == "--key" and i + 1 < len(args):
            api_key = args[i + 1]
            break

    if not api_key:
        # Check environment
        api_key = os.environ.get("GOOGLE_AI_API_KEY")

    if not api_key:
        print("Claude Banana - MCP Setup")
        print("=" * 40)
        print(f"\nGet your free API key at: https://aistudio.google.com/apikey")
        print()
        try:
            api_key = input("Enter your Google AI API key: ")
        except (EOFError, KeyboardInterrupt):
            print("\nError: No input received. Provide a key with --key or set GOOGLE_AI_API_KEY env var.")
            sys.exit(1)

    setup_mcp(api_key)


if __name__ == "__main__":
    main()
```

## File: `extensions/banana/scripts/validate_setup.py`
```python
#!/usr/bin/env python3
"""
Validate that the Claude Banana MCP server is properly configured.

Checks:
1. Claude Code settings.json has the MCP entry
2. API key is present
3. Node.js/npx is available
4. Output directory exists or can be created

Usage:
    python3 validate_setup.py
"""

import json
import shutil
import sys
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
MCP_NAME = "nanobanana-mcp"
OUTPUT_DIR = Path.home() / "Documents" / "nanobanana_generated"


def check(label: str, passed: bool, detail: str = "") -> bool:
    status = "PASS" if passed else "FAIL"
    msg = f"  [{status}] {label}"
    if detail:
        msg += f": {detail}"
    print(msg)
    return passed


def main() -> int:
    print("Claude Banana - Setup Validation")
    print("=" * 40)
    results = []

    # 1. Settings file exists
    results.append(check(
        "Claude Code settings.json exists",
        SETTINGS_PATH.exists(),
        str(SETTINGS_PATH),
    ))

    if not SETTINGS_PATH.exists():
        print("\nCannot continue without settings.json.")
        return 1

    # 2. Load and parse settings
    try:
        with open(SETTINGS_PATH) as f:
            settings = json.load(f)
        results.append(check("settings.json is valid JSON", True))
    except json.JSONDecodeError as e:
        results.append(check("settings.json is valid JSON", False, str(e)))
        return 1

    # 3. MCP entry exists
    servers = settings.get("mcpServers", {})
    has_mcp = MCP_NAME in servers
    results.append(check(f"MCP server '{MCP_NAME}' configured", has_mcp))

    if has_mcp:
        mcp = servers[MCP_NAME]

        # 4. Command is npx
        results.append(check(
            "Command is 'npx'",
            mcp.get("command") == "npx",
            mcp.get("command", "(missing)"),
        ))

        # 5. Package is correct
        args = mcp.get("args", [])
        has_pkg = "@ycse/nanobanana-mcp" in args
        results.append(check(
            "Package is @ycse/nanobanana-mcp",
            has_pkg,
            str(args),
        ))

        # 6. API key present
        env = mcp.get("env", {})
        key = env.get("GOOGLE_AI_API_KEY", "")
        results.append(check(
            "GOOGLE_AI_API_KEY is set",
            bool(key),
            f"{key[:8]}...{key[-4:]}" if len(key) > 12 else "(empty or short)",
        ))

        # 7. Model configured
        model = env.get("NANOBANANA_MODEL", "")
        results.append(check(
            "NANOBANANA_MODEL is set",
            bool(model),
            model or "(not set, will use package default)",
        ))

    # 8. Node.js/npx available
    has_npx = shutil.which("npx") is not None
    results.append(check(
        "npx is available in PATH",
        has_npx,
        shutil.which("npx") or "not found",
    ))

    # 9. Output directory
    if OUTPUT_DIR.exists():
        results.append(check("Output directory exists", True, str(OUTPUT_DIR)))
    else:
        try:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            results.append(check("Output directory created", True, str(OUTPUT_DIR)))
        except OSError as e:
            results.append(check("Output directory writable", False, str(e)))

    # Summary
    passed = sum(1 for r in results if r)
    total = len(results)
    print(f"\n{'=' * 40}")
    print(f"Results: {passed}/{total} checks passed")

    if passed == total:
        print("Status: Ready to generate images!")
        return 0
    else:
        print("Status: Some checks failed. Fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

## File: `extensions/banana/skills/seo-image-gen/SKILL.md`
```markdown
---
name: seo-image-gen
description: "AI image generation for SEO assets: OG/social preview images, blog hero images, schema images, product photography, infographics. Powered by Gemini via nanobanana-mcp. Requires banana extension installed. Use when user says \"generate image\", \"OG image\", \"social preview\", \"hero image\", \"blog image\", \"product photo\", \"infographic\", \"seo image\", \"create visual\", \"image-gen\", \"favicon\", \"schema image\", \"pinterest pin\", \"generate visual\", \"banner\", or \"thumbnail\"."
argument-hint: "[og|hero|product|infographic|custom|batch] <description>"
user-invokable: true
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
compatibility: "Requires nanobanana MCP server"
metadata:
  author: AgriciDaniel
  version: "1.6.1"
  category: seo
---

# SEO Image Gen: AI Image Generation for SEO Assets (Extension)

Generate production-ready images for SEO use cases using Gemini's image generation
via the banana Creative Director pipeline. Maps SEO needs to optimized domain modes,
aspect ratios, and resolution defaults.

## Architecture Note

This extension is built on [Claude Banana](https://github.com/AgriciDaniel/banana-claude),
the standalone AI image generation skill for Claude Code.

This skill has two components with distinct roles:
- **SKILL.md** (this file): Handles interactive `/seo image-gen` commands for generating images
- **Agent** (`agents/seo-image-gen.md`): Audit-only analyst spawned during `/seo audit` to assess existing OG/social images and produce a generation plan (never auto-generates)

## Prerequisites

This skill requires the banana extension to be installed:
```bash
./extensions/banana/install.sh
```

**Check availability:** Before using any image generation tool, verify the MCP server
is connected by checking if `gemini_generate_image` or `set_aspect_ratio` tools are
available. If tools are not available, inform the user the extension is not installed
and provide install instructions.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo image-gen og <description>` | Generate OG/social preview image (1200x630 feel) |
| `/seo image-gen hero <description>` | Blog hero image (widescreen, dramatic) |
| `/seo image-gen product <description>` | Product photography (clean, white BG) |
| `/seo image-gen infographic <description>` | Infographic visual (vertical, data-heavy) |
| `/seo image-gen custom <description>` | Custom image with full Creative Director pipeline |
| `/seo image-gen batch <description> [N]` | Generate N variations (default: 3) |

## SEO Image Use Cases

Each use case maps to pre-configured banana parameters:

| Use Case | Aspect Ratio | Resolution | Domain Mode | Notes |
|----------|-------------|------------|-------------|-------|
| **OG/Social Preview** | `16:9` | `1K` | Product or UI/Web | Clean, professional, text-friendly |
| **Blog Hero** | `16:9` | `2K` | Cinema or Editorial | Dramatic, atmospheric, editorial quality |
| **Schema Image** | `4:3` | `1K` | Product | Clean, descriptive, schema ImageObject |
| **Social Square** | `1:1` | `1K` | UI/Web | Platform-optimized square |
| **Product Photo** | `4:3` | `2K` | Product | White background, studio lighting |
| **Infographic** | `2:3` | `4K` | Infographic | Data-heavy, vertical layout |
| **Favicon/Icon** | `1:1` | `512` | Logo | Minimal, scalable, recognizable |
| **Pinterest Pin** | `2:3` | `2K` | Editorial | Tall vertical card |

## Generation Pipeline

For every generation request:

1. **Identify use case** from command or context (og, hero, product, etc.)
2. **Apply SEO defaults** from the use cases table above
3. **Set aspect ratio** via `set_aspect_ratio` MCP tool
4. **Construct Reasoning Brief** using the banana Creative Director pipeline:
   - Load `references/prompt-engineering.md` for the 6-component system
   - Apply domain mode emphasis (Subject 30%, Style 25%, Context 15%, etc.)
   - Be SPECIFIC and VISCERAL: describe what the camera sees
5. **Generate** via `gemini_generate_image` MCP tool
6. **Post-generation SEO checklist** (see below)

### Check for Presets

If the user mentions a brand or has SEO presets configured:
```bash
python3 ~/.claude/skills/seo-image-gen/scripts/presets.py list
```
Load matching preset and apply as defaults. Also check `references/seo-image-presets.md`
for SEO-specific preset templates.

## Post-Generation SEO Checklist

After every successful generation, guide the user on:

1. **Alt text**:Write descriptive, keyword-rich alt text for the generated image
2. **File naming**:Rename to SEO-friendly format: `keyword-description-widthxheight.webp`
3. **WebP conversion**:Convert to WebP for optimal page speed:
   ```bash
   magick output.png -quality 85 output.webp
   ```
4. **File size**:Target under 200KB for hero images, under 100KB for thumbnails
5. **Schema markup**:Suggest `ImageObject` schema for the generated image:
   ```json
   {
     "@type": "ImageObject",
     "url": "https://example.com/images/keyword-description.webp",
     "width": 1200,
     "height": 630,
     "caption": "Descriptive caption with target keyword"
   }
   ```
6. **OG meta tags**:For social preview images, remind about:
   ```html
   <meta property="og:image" content="https://example.com/images/og-image.webp" />
   <meta property="og:image:width" content="1200" />
   <meta property="og:image:height" content="630" />
   <meta property="og:image:alt" content="Descriptive alt text" />
   ```

## Cost Awareness

Image generation costs money. Be transparent:
- Show estimated cost before generating (especially for batch)
- Log every generation: `python3 ~/.claude/skills/seo-image-gen/scripts/cost_tracker.py log --model MODEL --resolution RES --prompt "brief"`
- Run `cost_tracker.py summary` if user asks about usage

Approximate costs (gemini-3.1-flash):
- 512: ~$0.02/image
- 1K resolution: ~$0.04/image
- 2K resolution: ~$0.08/image
- 4K resolution: ~$0.16/image

## Model Routing

| Scenario | Model | Why |
|----------|-------|-----|
| OG images, social previews | `gemini-3.1-flash-image-preview` @ 1K | Fast, cost-effective |
| Hero images, product photos | `gemini-3.1-flash-image-preview` @ 2K | Quality + detail |
| Infographics with text | `gemini-3.1-flash-image-preview` @ 2K, thinking: high | Better text rendering |
| Quick drafts | `gemini-2.5-flash-image` @ 512 | Rapid iteration |

## Error Handling

| Error | Resolution |
|-------|-----------|
| MCP not configured | Run `./extensions/banana/install.sh` |
| API key invalid | New key at https://aistudio.google.com/apikey |
| Rate limited (429) | Wait 60s, retry. Free tier: ~10 RPM / ~500 RPD |
| `IMAGE_SAFETY` | Rephrase prompt - see `references/prompt-engineering.md` Safety section |
| MCP unavailable | Fall back: `python3 ~/.claude/skills/seo-image-gen/scripts/generate.py --prompt "..." --aspect-ratio "16:9"` |
| Extension not installed | Show install instructions: `./extensions/banana/install.sh` |

## Cross-Skill Integration

- **seo-images** (analysis) feeds into **seo-image-gen** (generation): audit results from `/seo images` identify missing or low-quality images; use those findings to drive `/seo image-gen` commands
- **seo-audit** spawns the seo-image-gen **agent** (not this skill) to analyze OG/social images across the site and produce a prioritized generation plan
- **seo-schema** can consume generated images: after generation, suggest `ImageObject` schema markup pointing to the new assets

## Reference Documentation

Load on-demand. Do NOT load all at startup:
- `references/prompt-engineering.md`:6-component system, domain modes, templates
- `references/gemini-models.md`:Model specs, rate limits, capabilities
- `references/mcp-tools.md`:MCP tool parameters and responses
- `references/post-processing.md`:ImageMagick/FFmpeg pipeline recipes
- `references/cost-tracking.md`:Pricing, usage tracking
- `references/presets.md`:Brand preset management
- `references/seo-image-presets.md`:SEO-specific preset templates

## Response Format

After generating, always provide:
1. **Image path**:where it was saved
2. **Crafted prompt**:show what was sent to the API (educational)
3. **Settings**:model, aspect ratio, resolution
4. **SEO checklist**:alt text suggestion, file naming, WebP conversion
5. **Schema snippet**:ImageObject or og:image markup if applicable
```

## File: `extensions/dataforseo/field-config.json`
```json
{
  "_comment": "SEO-optimized field filtering for DataForSEO MCP server (9 modules, 79 tools). Reduces token usage ~75% by returning only SEO-relevant fields. Used via FIELD_CONFIG_PATH env var.",
  "serp": {
    "items": {
      "type": true,
      "rank_group": true,
      "rank_absolute": true,
      "position": true,
      "title": true,
      "description": true,
      "url": true,
      "domain": true,
      "breadcrumb": true,
      "featured_snippet": true,
      "is_featured_snippet": true,
      "rating": true,
      "timestamp": true,
      "local_pack": true,
      "ai_overview": true,
      "people_also_ask": true,
      "related_searches": true,
      "knowledge_graph": true,
      "video": {
        "title": true,
        "url": true,
        "channel_name": true,
        "views_count": true,
        "timestamp": true
      }
    }
  },
  "keywords_data": {
    "keyword": true,
    "search_volume": true,
    "cpc": true,
    "competition": true,
    "competition_level": true,
    "monthly_searches": true,
    "categories": true,
    "search_partners_search_volume": true
  },
  "dataforseo_labs": {
    "keyword_data": {
      "keyword": true,
      "search_volume": true,
      "cpc": true,
      "competition": true,
      "competition_level": true,
      "keyword_difficulty": true,
      "search_intent": true,
      "search_intent_secondary": true,
      "monthly_searches": true
    },
    "domain_data": {
      "domain": true,
      "rank": true,
      "organic_count": true,
      "organic_traffic": true,
      "organic_cost": true,
      "etv": true,
      "keywords_count": true,
      "is_competitor": true
    },
    "ranked_keywords": {
      "keyword": true,
      "rank_group": true,
      "rank_absolute": true,
      "url": true,
      "search_volume": true,
      "cpc": true,
      "competition": true,
      "traffic_share": true,
      "serp_features": true,
      "etv": true
    },
    "intersection": {
      "keyword": true,
      "rank_group": true,
      "rank_absolute": true,
      "url": true,
      "search_volume": true,
      "domain": true
    },
    "traffic_estimation": {
      "domain": true,
      "organic_traffic": true,
      "organic_cost": true,
      "etv": true,
      "count": true
    },
    "relevant_pages": {
      "url": true,
      "rank": true,
      "etv": true,
      "keywords_count": true,
      "organic_traffic": true
    }
  },
  "backlinks": {
    "summary": {
      "target": true,
      "total_backlinks": true,
      "total_referring_domains": true,
      "rank": true,
      "backlinks_spam_score": true,
      "dofollow": true,
      "nofollow": true,
      "new_backlinks": true,
      "lost_backlinks": true,
      "broken_backlinks": true,
      "referring_domains_nofollow": true,
      "referring_ips": true,
      "referring_subnets": true
    },
    "items": {
      "url_from": true,
      "url_to": true,
      "domain_from": true,
      "domain_to": true,
      "anchor": true,
      "rank": true,
      "page_from_rank": true,
      "dofollow": true,
      "type": true,
      "is_new": true,
      "is_lost": true,
      "first_seen": true,
      "last_seen": true,
      "tld_from": true
    },
    "anchors": {
      "anchor": true,
      "backlinks": true,
      "referring_domains": true,
      "dofollow": true,
      "first_seen": true
    },
    "referring_domains": {
      "domain": true,
      "rank": true,
      "backlinks": true,
      "dofollow": true,
      "first_seen": true,
      "tld": true
    },
    "spam_score": {
      "target": true,
      "spam_score": true
    },
    "timeseries": {
      "date": true,
      "rank": true,
      "total_backlinks": true,
      "total_referring_domains": true,
      "new_backlinks": true,
      "lost_backlinks": true
    }
  },
  "onpage": {
    "instant_pages": {
      "url": true,
      "status_code": true,
      "meta": {
        "title": true,
        "description": true,
        "canonical": true,
        "robots": true,
        "hreflang": true
      },
      "content": {
        "plain_text_word_count": true,
        "plain_text_rate": true
      },
      "page_timing": {
        "time_to_interactive": true,
        "dom_complete": true,
        "largest_contentful_paint": true,
        "cumulative_layout_shift": true,
        "first_contentful_paint": true
      },
      "onpage_score": true,
      "total_dom_size": true,
      "checks": true,
      "broken_links": true
    },
    "content_parsing": {
      "url": true,
      "plain_text": true,
      "plain_text_word_count": true
    },
    "lighthouse": {
      "categories": true,
      "audits": true
    }
  },
  "domain_analytics": {
    "technologies": {
      "technology": true,
      "category": true,
      "version": true
    },
    "whois": {
      "domain": true,
      "registrar": true,
      "creation_date": true,
      "expiration_date": true,
      "updated_date": true,
      "nameservers": true,
      "registrant": {
        "name": true,
        "organization": true,
        "country": true
      }
    }
  },
  "business_data": {
    "business_listings": {
      "title": true,
      "description": true,
      "category": true,
      "address": true,
      "phone": true,
      "domain": true,
      "rating": true,
      "reviews_count": true,
      "is_claimed": true
    }
  },
  "content_analysis": {
    "summary": {
      "sentiment": true,
      "readability": true,
      "keyword_density": true,
      "toxicity": true,
      "information_score": true,
      "adult_content": true,
      "language": true,
      "connotation_types": true
    },
    "search": {
      "url": true,
      "title": true,
      "snippet": true,
      "domain": true,
      "sentiment": true,
      "language": true,
      "date": true,
      "content_quality_score": true
    },
    "phrase_trends": {
      "phrase": true,
      "date": true,
      "frequency": true,
      "sentiment": true
    }
  },
  "ai_optimization": {
    "chatgpt_scraper": {
      "html": true,
      "sources": true,
      "urls": true,
      "status": true
    },
    "keyword_data": {
      "keyword": true,
      "search_volume": true,
      "location_code": true,
      "language_code": true
    },
    "llm_mentions": {
      "keyword": true,
      "domain": true,
      "url": true,
      "mention_count": true,
      "model": true,
      "timestamp": true,
      "metrics": true
    }
  }
}
```

## File: `extensions/dataforseo/install.ps1`
```powershell
# DataForSEO Extension Installer for Claude SEO (Windows)
# PowerShell installation script

$ErrorActionPreference = "Stop"

Write-Host "════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "║   DataForSEO Extension - Installer   ║" -ForegroundColor Cyan
Write-Host "║   For Claude SEO                     ║" -ForegroundColor Cyan
Write-Host "════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
$SeoSkillDir = "$env:USERPROFILE\.claude\skills\seo"
if (-not (Test-Path $SeoSkillDir)) {
    Write-Host "✗ Claude SEO is not installed." -ForegroundColor Red
    Write-Host "  Install it first: irm https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.ps1 | iex"
    exit 1
}
Write-Host "✓ Claude SEO detected" -ForegroundColor Green

$nodeCmd = Get-Command -Name node -ErrorAction SilentlyContinue
if ($null -eq $nodeCmd) {
    Write-Host "✗ Node.js is required but not installed." -ForegroundColor Red
    Write-Host "  Install Node.js 20+: https://nodejs.org/"
    exit 1
}

$nodeVersion = (node -v) -replace 'v','' -split '\.' | Select-Object -First 1
if ([int]$nodeVersion -lt 20) {
    Write-Host "✗ Node.js 20+ required (found v$nodeVersion)." -ForegroundColor Red
    exit 1
}
Write-Host "✓ Node.js $(node -v) detected" -ForegroundColor Green

$npxCmd = Get-Command -Name npx -ErrorAction SilentlyContinue
if ($null -eq $npxCmd) {
    Write-Host "✗ npx is required but not found (comes with npm)." -ForegroundColor Red
    exit 1
}
Write-Host "✓ npx detected" -ForegroundColor Green

# Prompt for credentials
Write-Host ""
Write-Host "DataForSEO API credentials required." -ForegroundColor Yellow
Write-Host "Sign up at: https://app.dataforseo.com/register"
Write-Host ""

$DfseUsername = Read-Host "DataForSEO username (email)"
if ([string]::IsNullOrEmpty($DfseUsername)) {
    Write-Host "✗ Username cannot be empty." -ForegroundColor Red
    exit 1
}

$DfsePasswordSecure = Read-Host "DataForSEO password" -AsSecureString
$DfsePassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [Runtime.InteropServices.Marshal]::SecureStringToBSTR($DfsePasswordSecure)
)
if ([string]::IsNullOrEmpty($DfsePassword)) {
    Write-Host "✗ Password cannot be empty." -ForegroundColor Red
    exit 1
}

# Determine source directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (Test-Path "$ScriptDir\skills\seo-dataforseo\SKILL.md") {
    $SourceDir = $ScriptDir
} elseif (Test-Path "$ScriptDir\extensions\dataforseo\skills\seo-dataforseo\SKILL.md") {
    $SourceDir = "$ScriptDir\extensions\dataforseo"
} else {
    Write-Host "✗ Cannot find extension source files." -ForegroundColor Red
    Write-Host "  Run this script from the claude-seo repo."
    exit 1
}

# Set paths
$SkillDir = "$env:USERPROFILE\.claude\skills\seo-dataforseo"
$AgentDir = "$env:USERPROFILE\.claude\agents"
$SettingsFile = "$env:USERPROFILE\.claude\settings.json"
$FieldConfigPath = "$SeoSkillDir\dataforseo-field-config.json"

# Install skill
Write-Host ""
Write-Host "→ Installing DataForSEO skill..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $SkillDir | Out-Null
Copy-Item -Force "$SourceDir\skills\seo-dataforseo\SKILL.md" "$SkillDir\SKILL.md"

# Install agent
Write-Host "→ Installing DataForSEO agent..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $AgentDir | Out-Null
Copy-Item -Force "$SourceDir\agents\seo-dataforseo.md" "$AgentDir\seo-dataforseo.md"

# Install field config
Write-Host "→ Installing field config..." -ForegroundColor Yellow
Copy-Item -Force "$SourceDir\field-config.json" $FieldConfigPath

# Merge MCP config into settings.json
Write-Host "→ Configuring MCP server..." -ForegroundColor Yellow

$python = Get-Command -Name python -ErrorAction SilentlyContinue
if ($null -eq $python) {
    $python = Get-Command -Name py -ErrorAction SilentlyContinue
}

if ($null -ne $python) {
    $pyExe = $python.Source
    $pyScript = @"
import json, os
settings_path = r'$SettingsFile'
if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        settings = json.load(f)
else:
    settings = {}
if 'mcpServers' not in settings:
    settings['mcpServers'] = {}
settings['mcpServers']['dataforseo'] = {
    'command': 'npx',
    'args': ['-y', 'dataforseo-mcp-server'],
    'env': {
        'DATAFORSEO_USERNAME': '$DfseUsername',
        'DATAFORSEO_PASSWORD': '$DfsePassword',
        'ENABLED_MODULES': 'SERP,KEYWORDS_DATA,ONPAGE,DATAFORSEO_LABS,BACKLINKS,DOMAIN_ANALYTICS,BUSINESS_DATA,CONTENT_ANALYSIS,AI_OPTIMIZATION',
        'FIELD_CONFIG_PATH': r'$FieldConfigPath'
    }
}
os.makedirs(os.path.dirname(settings_path), exist_ok=True)
with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=2)
print('  ok')
"@

    $result = & $pyExe -c $pyScript 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ MCP server configured in settings.json" -ForegroundColor Green
    } else {
        Write-Host "  ⚠  Could not auto-configure MCP server." -ForegroundColor Yellow
        Write-Host "  Add the dataforseo server manually to ~\.claude\settings.json"
    }
} else {
    Write-Host "  ⚠  Python not found. Configure MCP server manually." -ForegroundColor Yellow
    Write-Host "  See: extensions\dataforseo\brain\knowledge\docs_legacy\DATAFORSEO-SETUP.md"
}

# Pre-warm npx package
Write-Host "→ Pre-downloading dataforseo-mcp-server..." -ForegroundColor Yellow
try {
    & npx -y dataforseo-mcp-server --help 2>&1 | Out-Null
} catch {
    # Ignore errors from pre-warm
}

Write-Host ""
Write-Host "✓ DataForSEO extension installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Usage:" -ForegroundColor Cyan
Write-Host "  1. Start Claude Code:  claude"
Write-Host "  2. Run commands:"
Write-Host "     /seo dataforseo serp best coffee shops"
Write-Host "     /seo dataforseo keywords seo tools"
Write-Host "     /seo dataforseo backlinks example.com"
Write-Host "     /seo dataforseo ai-mentions your brand"
Write-Host ""
Write-Host "All 22 commands: see extensions\dataforseo\README.md"
Write-Host "To uninstall: .\extensions\dataforseo\uninstall.ps1"
```

## File: `extensions/dataforseo/install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# DataForSEO Extension Installer for Claude SEO
# Wraps everything in main() to prevent partial execution on network failure

main() {
    SKILL_DIR="${HOME}/.claude/skills/seo-dataforseo"
    AGENT_DIR="${HOME}/.claude/agents"
    SEO_SKILL_DIR="${HOME}/.claude/skills/seo"
    SETTINGS_FILE="${HOME}/.claude/settings.json"

    echo "════════════════════════════════════════"
    echo "║   DataForSEO Extension - Installer   ║"
    echo "║   For Claude SEO                     ║"
    echo "════════════════════════════════════════"
    echo ""

    # Check prerequisites
    if [ ! -d "${SEO_SKILL_DIR}" ]; then
        echo "✗ Claude SEO is not installed."
        echo "  Install it first: curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash"
        exit 1
    fi
    echo "✓ Claude SEO detected"

    if ! command -v node >/dev/null 2>&1; then
        echo "✗ Node.js is required but not installed."
        echo "  Install Node.js 20+: https://nodejs.org/"
        exit 1
    fi

    NODE_VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
    if [ "${NODE_VERSION}" -lt 20 ]; then
        echo "✗ Node.js 20+ required (found v${NODE_VERSION})."
        echo "  Update: https://nodejs.org/"
        exit 1
    fi
    echo "✓ Node.js v$(node -v | sed 's/v//') detected"

    if ! command -v npx >/dev/null 2>&1; then
        echo "✗ npx is required but not found (comes with npm)."
        exit 1
    fi
    echo "✓ npx detected"

    # Prompt for credentials
    echo ""
    echo "DataForSEO API credentials required."
    echo "Sign up at: https://app.dataforseo.com/register"
    echo ""

    read -rp "DataForSEO username (email): " DFSE_USERNAME
    if [ -z "${DFSE_USERNAME}" ]; then
        echo "✗ Username cannot be empty."
        exit 1
    fi

    read -rsp "DataForSEO password: " DFSE_PASSWORD
    echo ""
    if [ -z "${DFSE_PASSWORD}" ]; then
        echo "✗ Password cannot be empty."
        exit 1
    fi

    # Determine script directory (works for both ./install.sh and curl|bash)
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # Check if running from repo or standalone
    if [ -f "${SCRIPT_DIR}/skills/seo-dataforseo/SKILL.md" ]; then
        SOURCE_DIR="${SCRIPT_DIR}"
    elif [ -f "${SCRIPT_DIR}/extensions/dataforseo/skills/seo-dataforseo/SKILL.md" ]; then
        SOURCE_DIR="${SCRIPT_DIR}/extensions/dataforseo"
    else
        echo "✗ Cannot find extension source files."
        echo "  Run this script from the claude-seo repo: ./extensions/dataforseo/install.sh"
        exit 1
    fi

    # Install skill
    echo ""
    echo "→ Installing DataForSEO skill..."
    mkdir -p "${SKILL_DIR}"
    cp "${SOURCE_DIR}/skills/seo-dataforseo/SKILL.md" "${SKILL_DIR}/SKILL.md"

    # Install agent
    echo "→ Installing DataForSEO agent..."
    mkdir -p "${AGENT_DIR}"
    cp "${SOURCE_DIR}/agents/seo-dataforseo.md" "${AGENT_DIR}/seo-dataforseo.md"

    # Install field config
    echo "→ Installing field config..."
    cp "${SOURCE_DIR}/field-config.json" "${SEO_SKILL_DIR}/dataforseo-field-config.json"

    # Merge MCP config into settings.json
    echo "→ Configuring MCP server..."
    FIELD_CONFIG_PATH="${SEO_SKILL_DIR}/dataforseo-field-config.json"

    python3 -c "
import json, os, sys

settings_path = '${SETTINGS_FILE}'
username = '''${DFSE_USERNAME}'''
password = '''${DFSE_PASSWORD}'''
field_config = '${FIELD_CONFIG_PATH}'

# Read existing settings or create new
if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        settings = json.load(f)
else:
    settings = {}

# Ensure mcpServers key exists
if 'mcpServers' not in settings:
    settings['mcpServers'] = {}

# Add DataForSEO server config
settings['mcpServers']['dataforseo'] = {
    'command': 'npx',
    'args': ['-y', 'dataforseo-mcp-server'],
    'env': {
        'DATAFORSEO_USERNAME': username,
        'DATAFORSEO_PASSWORD': password,
        'ENABLED_MODULES': 'SERP,KEYWORDS_DATA,ONPAGE,DATAFORSEO_LABS,BACKLINKS,DOMAIN_ANALYTICS,BUSINESS_DATA,CONTENT_ANALYSIS,AI_OPTIMIZATION',
        'FIELD_CONFIG_PATH': field_config
    }
}

# Write back
os.makedirs(os.path.dirname(settings_path), exist_ok=True)
with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=2)

print('  ✓ MCP server configured in settings.json')
" || {
        echo "  ⚠  Could not auto-configure MCP server."
        echo "  Add the dataforseo server manually to ~/.claude/settings.json"
        echo "  See: extensions/dataforseo/brain/knowledge/docs_legacy/DATAFORSEO-SETUP.md"
    }

    # Pre-warm npx package
    echo "→ Pre-downloading dataforseo-mcp-server..."
    npx -y dataforseo-mcp-server --help >/dev/null 2>&1 || true

    echo ""
    echo "✓ DataForSEO extension installed successfully!"
    echo ""
    echo "Usage:"
    echo "  1. Start Claude Code:  claude"
    echo "  2. Run commands:"
    echo "     /seo dataforseo serp best coffee shops"
    echo "     /seo dataforseo keywords seo tools"
    echo "     /seo dataforseo backlinks example.com"
    echo "     /seo dataforseo ai-mentions your brand"
    echo ""
    echo "All 22 commands: see extensions/dataforseo/README.md"
    echo "To uninstall: ./extensions/dataforseo/uninstall.sh"
}

main "$@"
```

## File: `extensions/dataforseo/README.md`
```markdown
# DataForSEO Extension for Claude SEO

Live SEO data via the [DataForSEO MCP server](https://github.com/dataforseo/mcp-server-typescript). Adds 22 commands across 9 API modules: SERP analysis, keyword research, backlinks, on-page analysis, competitor analysis, content analysis, business listings, AI visibility checking, and LLM mention tracking.

## Prerequisites

- [Claude SEO](https://github.com/AgriciDaniel/claude-seo) installed
- Node.js 20+
- [DataForSEO account](https://app.dataforseo.com/register) with API credentials

## Installation

### Unix/macOS/Linux

```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
./extensions/dataforseo/install.sh
```

### Windows

```powershell
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
.\extensions\dataforseo\install.ps1
```

The installer will:
1. Prompt for your DataForSEO username and password
2. Install the skill and agent files
3. Configure the MCP server in `~/.claude/settings.json`
4. Pre-download the `dataforseo-mcp-server` npm package

## Commands

### SERP Analysis

| Command | Description |
|---------|-------------|
| `/seo dataforseo serp <keyword>` | Google organic SERP results (also supports Bing/Yahoo via `se` parameter) |
| `/seo dataforseo serp-youtube <keyword>` | YouTube search results |
| `/seo dataforseo youtube <video_id>` | YouTube video deep analysis (info, comments, subtitles) |

### Keyword Research

| Command | Description |
|---------|-------------|
| `/seo dataforseo keywords <seed>` | Keyword ideas, suggestions, and related terms |
| `/seo dataforseo volume <keywords>` | Search volume for keyword list |
| `/seo dataforseo difficulty <keywords>` | Keyword difficulty scores |
| `/seo dataforseo intent <keywords>` | Search intent classification |
| `/seo dataforseo trends <keyword>` | Google Trends data over time |

### Domain & Competitor Analysis

| Command | Description |
|---------|-------------|
| `/seo dataforseo backlinks <domain>` | Full backlink profile with spam scores |
| `/seo dataforseo competitors <domain>` | Competing domains and traffic estimates |
| `/seo dataforseo ranked <domain>` | Keywords a domain ranks for |
| `/seo dataforseo intersection <domains>` | Keyword/backlink overlap (2-20 domains) |
| `/seo dataforseo traffic <domains>` | Bulk traffic estimation |
| `/seo dataforseo subdomains <domain>` | Subdomains with ranking data |
| `/seo dataforseo top-searches <domain>` | Top queries mentioning domain |

### Technical / On-Page

| Command | Description |
|---------|-------------|
| `/seo dataforseo onpage <url>` | On-page analysis (Lighthouse + content parsing) |
| `/seo dataforseo tech <domain>` | Technology stack detection |
| `/seo dataforseo whois <domain>` | WHOIS registration data |

### Content & Business Data

| Command | Description |
|---------|-------------|
| `/seo dataforseo content <keyword/url>` | Content analysis, search, and phrase trends |
| `/seo dataforseo listings <keyword>` | Business listings search |

### AI Visibility / GEO

| Command | Description |
|---------|-------------|
| `/seo dataforseo ai-scrape <query>` | ChatGPT web scraper for GEO visibility |
| `/seo dataforseo ai-mentions <keyword>` | LLM mention tracking across AI platforms |

## API Modules

All 9 DataForSEO modules are enabled:

| Module | Purpose | Example Commands |
|--------|---------|-----------------|
| SERP | Search engine results | serp, serp-youtube, youtube |
| KEYWORDS_DATA | Search volume, trends | volume, trends |
| DATAFORSEO_LABS | Keyword research, competitors | keywords, difficulty, intent, competitors, ranked, subdomains, top-searches |
| BACKLINKS | Link profiles | backlinks, intersection |
| ONPAGE | Page analysis (Lighthouse) | onpage |
| DOMAIN_ANALYTICS | Tech detection, WHOIS | tech, whois |
| BUSINESS_DATA | Business listings | listings |
| CONTENT_ANALYSIS | Content quality, trends | content |
| AI_OPTIMIZATION | ChatGPT scraper, LLM mentions | ai-scrape, ai-mentions |

## API Credits

DataForSEO charges per API call. Credit costs vary by endpoint:

- **SERP** calls: ~0.001-0.003 per request
- **Keyword** research: ~0.0005-0.002 per keyword
- **Backlinks**: ~0.002-0.01 per request
- **On-page** analysis: ~0.01-0.05 per page
- **AI optimization**: ~0.01 per request

New accounts include a free trial balance. See [DataForSEO pricing](https://dataforseo.com/pricing) for current rates.

## Field Filtering

The extension includes a custom `field-config.json` that reduces API response sizes by ~75%, keeping only SEO-relevant fields. This saves tokens and speeds up analysis.

## Integration with Claude SEO

When installed, other Claude SEO skills automatically detect DataForSEO availability and use live data:

- **`/seo audit`**:Uses real SERP, backlink, and on-page data
- **`/seo technical`**:Uses on-page analysis for real technical data
- **`/seo content`**:Uses keyword volume, difficulty, and intent data
- **`/seo geo`**:Uses ChatGPT scraper and LLM mentions for GEO signals
- **`/seo plan`**:Uses competitor and keyword data for strategy

## Troubleshooting

### MCP server not connecting

1. Check credentials: `cat ~/.claude/settings.json | grep DATAFORSEO`
2. Test manually: `npx -y dataforseo-mcp-server`
3. Re-run installer: `./extensions/dataforseo/install.sh`

### API errors

- **401 Unauthorized**: Check username/password in settings.json
- **402 Payment Required**: Add credits at [app.dataforseo.com](https://app.dataforseo.com)
- **429 Rate Limited**: Wait and retry (DataForSEO has per-second limits)

### Module not available

If a specific command fails, check that the module is in `ENABLED_MODULES` in your settings.json. All 9 modules should be listed.

## Uninstall

### Unix/macOS/Linux

```bash
./extensions/dataforseo/uninstall.sh
```

### Windows

```powershell
.\extensions\dataforseo\uninstall.ps1
```

This removes the skill, agent, field config, and MCP server entry from settings.json.

## Links

- [DataForSEO API Docs](https://docs.dataforseo.com/)
- [DataForSEO MCP Server](https://github.com/dataforseo/mcp-server-typescript)
- [Claude SEO](https://github.com/AgriciDaniel/claude-seo)
```

## File: `extensions/dataforseo/uninstall.ps1`
```powershell
# DataForSEO Extension Uninstaller for Claude SEO (Windows)

$ErrorActionPreference = "Stop"

Write-Host "→ Uninstalling DataForSEO extension..." -ForegroundColor Yellow

# Remove skill
if (Test-Path "$env:USERPROFILE\.claude\skills\seo-dataforseo") {
    Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\skills\seo-dataforseo"
}

# Remove agent
$agentFile = "$env:USERPROFILE\.claude\agents\seo-dataforseo.md"
if (Test-Path $agentFile) {
    Remove-Item -Force $agentFile
}

# Remove field config
$fieldConfig = "$env:USERPROFILE\.claude\skills\seo\dataforseo-field-config.json"
if (Test-Path $fieldConfig) {
    Remove-Item -Force $fieldConfig
}

# Remove MCP server entry from settings.json
$settingsFile = "$env:USERPROFILE\.claude\settings.json"
if (Test-Path $settingsFile) {
    $python = Get-Command -Name python -ErrorAction SilentlyContinue
    if ($null -eq $python) {
        $python = Get-Command -Name py -ErrorAction SilentlyContinue
    }

    if ($null -ne $python) {
        $pyExe = $python.Source
        $pyScript = @"
import json
settings_path = r'$settingsFile'
with open(settings_path, 'r') as f:
    settings = json.load(f)
if 'mcpServers' in settings and 'dataforseo' in settings['mcpServers']:
    del settings['mcpServers']['dataforseo']
    if not settings['mcpServers']:
        del settings['mcpServers']
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print('  ok')
"@
        $result = & $pyExe -c $pyScript 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✓ Removed dataforseo from settings.json" -ForegroundColor Green
        } else {
            Write-Host "  ⚠  Could not auto-remove MCP config. Remove 'dataforseo' from ~\.claude\settings.json manually." -ForegroundColor Yellow
        }
    } else {
        Write-Host "  ⚠  Python not found. Remove 'dataforseo' from ~\.claude\settings.json manually." -ForegroundColor Yellow
    }
}

Write-Host "✓ DataForSEO extension uninstalled." -ForegroundColor Green
```

## File: `extensions/dataforseo/uninstall.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

main() {
    echo "→ Uninstalling DataForSEO extension..."

    # Remove skill
    rm -rf "${HOME}/.claude/skills/seo-dataforseo"

    # Remove agent
    rm -f "${HOME}/.claude/agents/seo-dataforseo.md"

    # Remove field config
    rm -f "${HOME}/.claude/skills/seo/dataforseo-field-config.json"

    # Remove MCP server entry from settings.json
    SETTINGS_FILE="${HOME}/.claude/settings.json"
    if [ -f "${SETTINGS_FILE}" ]; then
        python3 -c "
import json, os
settings_path = '${SETTINGS_FILE}'
with open(settings_path, 'r') as f:
    settings = json.load(f)
if 'mcpServers' in settings and 'dataforseo' in settings['mcpServers']:
    del settings['mcpServers']['dataforseo']
    if not settings['mcpServers']:
        del settings['mcpServers']
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print('  ✓ Removed dataforseo from settings.json')
else:
    print('  ✓ No dataforseo entry in settings.json')
" 2>/dev/null || echo "  ⚠  Could not auto-remove MCP config. Remove 'dataforseo' from ~/.claude/settings.json manually."
    fi

    echo "✓ DataForSEO extension uninstalled."
}

main "$@"
```

## File: `extensions/dataforseo/agents/seo-dataforseo.md`
```markdown
---
name: seo-dataforseo
description: DataForSEO data analyst. Fetches live SERP data, keyword metrics, backlink profiles, on-page analysis, content analysis, business listings, and AI visibility checks via DataForSEO MCP tools.
tools: Read, Bash, Write, Glob, Grep
---

You are a DataForSEO data analyst. When delegated tasks during an SEO audit or analysis:

1. Check that DataForSEO MCP tools are available before attempting calls
2. Use the most efficient tool combination for the requested data
3. Apply default parameters: location_code=2840 (US), language_code=en unless specified
4. Format output to match claude-seo conventions (tables, priority levels, scores)

## Efficient Tool Usage

- **Prefer bulk endpoints** over multiple single calls to minimize API credits
- **Don't re-fetch** data already retrieved in the same session
- **Warn before expensive operations** (full backlink crawls, large keyword lists)
- **Use limits**: default to limit=100 for list endpoints unless user needs more

## Error Handling

- If a DataForSEO tool returns an error, report the error clearly to the user
- If credentials are invalid, suggest running the extension installer again
- If a module is not enabled, note which module is needed

## Output Format

Match existing claude-seo patterns:
- Tables for comparative data
- Scores as XX/100
- Priority: Critical > High > Medium > Low
- Note data source as "DataForSEO (live)" to distinguish from static HTML analysis
- Include timestamps for time-sensitive data (SERP positions, backlink counts)
```

## File: `extensions/dataforseo/brain/knowledge/docs_legacy/DATAFORSEO-SETUP.md`
```markdown
# DataForSEO Account Setup

Step-by-step guide to getting DataForSEO API credentials for the Claude SEO extension.

## 1. Create Account

1. Go to [app.dataforseo.com/register](https://app.dataforseo.com/register)
2. Sign up with your email address
3. Verify your email

New accounts include a free trial balance for testing.

## 2. Find API Credentials

1. Log in to [app.dataforseo.com](https://app.dataforseo.com)
2. Go to **API Access** in the left sidebar
3. Your credentials are:
   - **Username**: Your registered email address
   - **Password**: Your API password (set during registration)

These are the values you'll enter when running the extension installer.

## 3. Understanding Credits

DataForSEO uses a credit-based system:

- Each API call costs a small number of credits
- Different endpoints have different costs
- Credits are purchased in advance
- Monitor usage at [app.dataforseo.com/dashboard](https://app.dataforseo.com/dashboard)

**Typical costs per call:**

| Endpoint Type | Approximate Cost |
|--------------|-----------------|
| SERP (single query) | $0.001-0.003 |
| Keyword volume (per keyword) | $0.0005-0.002 |
| Backlink summary | $0.002-0.005 |
| Backlink list | $0.005-0.01 |
| On-page crawl (per page) | $0.01-0.05 |
| AI optimization (per call) | $0.01 |

## 4. Manual MCP Configuration

If the installer's auto-configuration fails, add this to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your-email@example.com",
        "DATAFORSEO_PASSWORD": "your-api-password",
        "ENABLED_MODULES": "SERP,KEYWORDS_DATA,ONPAGE,DATAFORSEO_LABS,BACKLINKS,DOMAIN_ANALYTICS,BUSINESS_DATA,CONTENT_ANALYSIS,AI_OPTIMIZATION",
        "FIELD_CONFIG_PATH": "/home/youruser/.claude/skills/seo/dataforseo-field-config.json"
      }
    }
  }
}
```

Replace the username, password, and FIELD_CONFIG_PATH with your actual values.

## 5. Verify Installation

After installing, start Claude Code and run:

```
/seo dataforseo serp test query
```

If you see search results, the extension is working correctly.
```

## File: `extensions/dataforseo/skills/seo-dataforseo/SKILL.md`
```markdown
---
name: seo-dataforseo
description: >
  Live SEO data via DataForSEO MCP server. SERP analysis (Google, Bing, Yahoo,
  YouTube), keyword research (volume, difficulty, intent, trends), backlink
  profiles, on-page analysis (Lighthouse, content parsing), competitor analysis,
  content analysis, business listings, AI visibility (ChatGPT scraper, LLM
  mention tracking), and domain analytics. Requires DataForSEO extension
  installed. Use when user says "dataforseo", "live SERP", "keyword volume",
  "backlink data", "competitor data", "AI visibility check", "LLM mentions",
  or "real search data".
user-invokable: true
argument-hint: "[command] [query]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
compatibility: "Requires DataForSEO MCP server"
metadata:
  author: AgriciDaniel
  version: "1.6.1"
  category: seo
---

# DataForSEO: Live SEO Data (Extension)

Live search data via the DataForSEO MCP server. Provides real-time SERP results,
keyword metrics, backlink profiles, on-page analysis, content analysis, business
listings, AI visibility checking, and LLM mention tracking across
9 API modules with 79 MCP tools.

## Prerequisites

This skill requires the DataForSEO extension to be installed:
```bash
./extensions/dataforseo/install.sh
```

**Check availability:** Before using any DataForSEO tool, verify the MCP server
is connected by checking if `serp_organic_live_advanced` or any DataForSEO tool
is available. If tools are not available, inform the user the extension is not
installed and provide install instructions.

## API Credit Awareness

DataForSEO charges per API call. Be efficient:
- Prefer bulk endpoints over multiple single calls
- Use default parameters (US, English) unless user specifies otherwise
- Cache results mentally within a session; don't re-fetch the same data
- Warn user before running expensive operations (full backlink crawls, large keyword lists)

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo dataforseo serp <keyword>` | Google organic SERP results |
| `/seo dataforseo serp-youtube <keyword>` | YouTube search results |
| `/seo dataforseo youtube <video_id>` | YouTube video deep analysis |
| `/seo dataforseo keywords <seed>` | Keyword ideas and suggestions |
| `/seo dataforseo volume <keywords>` | Search volume for keywords |
| `/seo dataforseo difficulty <keywords>` | Keyword difficulty scores |
| `/seo dataforseo intent <keywords>` | Search intent classification |
| `/seo dataforseo trends <keyword>` | Google Trends data |
| `/seo dataforseo backlinks <domain>` | Full backlink profile |
| `/seo dataforseo competitors <domain>` | Competitor domain analysis |
| `/seo dataforseo ranked <domain>` | Ranked keywords for domain |
| `/seo dataforseo intersection <domains>` | Keyword/backlink overlap |
| `/seo dataforseo traffic <domains>` | Bulk traffic estimation |
| `/seo dataforseo subdomains <domain>` | Subdomains with ranking data |
| `/seo dataforseo top-searches <domain>` | Top queries mentioning domain |
| `/seo dataforseo onpage <url>` | On-page analysis (Lighthouse + parsing) |
| `/seo dataforseo tech <domain>` | Technology stack detection |
| `/seo dataforseo whois <domain>` | WHOIS registration data |
| `/seo dataforseo content <keyword/url>` | Content analysis and trends |
| `/seo dataforseo listings <keyword>` | Business listings search |
| `/seo dataforseo ai-scrape <query>` | ChatGPT web scraper for GEO |
| `/seo dataforseo ai-mentions <keyword>` | LLM mention tracking for GEO |

---

## SERP Analysis

### `/seo dataforseo serp <keyword>`

Fetch live Google organic search results.

**MCP tools:** `serp_organic_live_advanced`

**Default parameters:** location_code=2840 (US), language_code=en, device=desktop, depth=100

**Also supports:** The `serp_organic_live_advanced` tool supports Google, Bing, and Yahoo via the `se` parameter. Specify "bing" or "yahoo" to switch search engines.

**Output:** Rank, URL, title, description, domain, featured snippets, AI overview references, People Also Ask.

### `/seo dataforseo serp-youtube <keyword>`

Fetch YouTube search results. Valuable for GEO. YouTube mentions correlate most strongly with AI citations.

**MCP tools:** `serp_youtube_organic_live_advanced`

**Output:** Video title, channel, views, upload date, description, URL.

### `/seo dataforseo youtube <video_id>`

Deep analysis of a specific YouTube video: info, comments, and subtitles. YouTube mentions have the strongest correlation (0.737) with AI visibility, making this critical for GEO analysis.

**MCP tools:** `serp_youtube_video_info_live_advanced`, `serp_youtube_video_comments_live_advanced`, `serp_youtube_video_subtitles_live_advanced`

**Parameters:** video_id (the YouTube video ID, e.g., "dQw4w9WgXcQ")

**Output:** Video metadata (title, channel, views, likes, description), top comments with engagement, subtitle/transcript text.

---

## Keyword Research

### `/seo dataforseo keywords <seed>`

Generate keyword ideas, suggestions, and related terms from a seed keyword.

**MCP tools:** `dataforseo_labs_google_keyword_ideas`, `dataforseo_labs_google_keyword_suggestions`, `dataforseo_labs_google_related_keywords`

**Default parameters:** location_code=2840 (US), language_code=en, limit=50

**Output:** Keyword, search volume, CPC, competition level, keyword difficulty, trend.

### `/seo dataforseo volume <keywords>`

Get search volume and metrics for a list of keywords.

**MCP tools:** `kw_data_google_ads_search_volume`

**Parameters:** keywords (array, comma-separated), location_code, language_code

**Output:** Keyword, monthly search volume, CPC, competition, monthly trend data.

### `/seo dataforseo difficulty <keywords>`

Calculate keyword difficulty scores for ranking competitiveness.

**MCP tools:** `dataforseo_labs_bulk_keyword_difficulty`

**Parameters:** keywords (array), location_code, language_code

**Output:** Keyword, difficulty score (0-100), interpretation (Easy/Medium/Hard/Very Hard).

### `/seo dataforseo intent <keywords>`

Classify keywords by user search intent.

**MCP tools:** `dataforseo_labs_search_intent`

**Parameters:** keywords (array), location_code, language_code

**Output:** Keyword, intent type (informational, navigational, commercial, transactional), confidence score.

### `/seo dataforseo trends <keyword>`

Analyze keyword trends over time using Google Trends data.

**MCP tools:** `kw_data_google_trends_explore`

**Parameters:** keywords (array), location_code, date_from, date_to, language_code

**Output:** Keyword, time series data, trend direction, seasonality signals.

---

## Domain & Competitor Analysis

### `/seo dataforseo backlinks <domain>`

Comprehensive backlink profile analysis.

**MCP tools:** `backlinks_summary`, `backlinks_backlinks`, `backlinks_anchors`, `backlinks_referring_domains`, `backlinks_bulk_spam_score`, `backlinks_timeseries_summary`

**Default parameters:** limit=100 per sub-call

**Output:** Total backlinks, referring domains, domain rank, spam score, top anchors, new/lost backlinks over time, dofollow ratio, top referring domains.

### `/seo dataforseo competitors <domain>`

Identify competing domains and estimate traffic.

**MCP tools:** `dataforseo_labs_google_competitors_domain`, `dataforseo_labs_google_domain_rank_overview`, `dataforseo_labs_bulk_traffic_estimation`

**Output:** Competitor domains, keyword overlap %, estimated traffic, domain rank, common keywords.

### `/seo dataforseo ranked <domain>`

List keywords a domain ranks for with positions and page data.

**MCP tools:** `dataforseo_labs_google_ranked_keywords`, `dataforseo_labs_google_relevant_pages`

**Default parameters:** limit=100, location_code=2840

**Output:** Keyword, position, URL, search volume, traffic share, SERP features.

### `/seo dataforseo intersection <domain1> <domain2> [...]`

Find shared keywords and backlink sources across 2-20 domains.

**MCP tools:** `dataforseo_labs_google_domain_intersection`, `backlinks_domain_intersection`

**Parameters:** domains (2-20 array)

**Output:** Shared keywords with positions per domain, shared backlink sources, unique keywords per domain.

### `/seo dataforseo traffic <domains>`

Estimate organic search traffic for one or more domains.

**MCP tools:** `dataforseo_labs_bulk_traffic_estimation`

**Parameters:** domains (array)

**Output:** Domain, estimated organic traffic, estimated traffic cost, top keywords.

### `/seo dataforseo subdomains <domain>`

Enumerate subdomains with their ranking data and traffic estimates.

**MCP tools:** `dataforseo_labs_google_subdomains`

**Parameters:** target (domain), location_code, language_code

**Output:** Subdomain, ranked keywords count, estimated traffic, organic cost.

### `/seo dataforseo top-searches <domain>`

Find the most popular search queries that mention a specific domain in results.

**MCP tools:** `dataforseo_labs_google_top_searches`

**Parameters:** target (domain), location_code, language_code

**Output:** Query, search volume, domain position, SERP features, traffic share.

---

## Technical / On-Page

### `/seo dataforseo onpage <url>`

Run on-page analysis including Lighthouse audit and content parsing.

**MCP tools:** `on_page_instant_pages`, `on_page_content_parsing`, `on_page_lighthouse`

**Usage:**
- `on_page_instant_pages`:Quick page analysis (status codes, meta tags, content size, page timing, broken links, on-page checks)
- `on_page_content_parsing`:Extract and parse page content (plain text, word count, structure)
- `on_page_lighthouse`:Full Lighthouse audit (performance score, accessibility, best practices, SEO, Core Web Vitals)

**Output:** Pages crawled, status codes, meta tags, titles, content size, load times, Lighthouse scores, broken links, resource analysis.

### `/seo dataforseo tech <domain>`

Detect technologies used on a domain.

**MCP tools:** `domain_analytics_technologies_domain_technologies`

**Output:** Technology name, version, category (CMS, analytics, CDN, framework, etc.).

### `/seo dataforseo whois <domain>`

Retrieve WHOIS registration data.

**MCP tools:** `domain_analytics_whois_overview`

**Output:** Registrar, creation date, expiration date, nameservers, registrant info (if public).

---

## Content & Business Data

### `/seo dataforseo content <keyword/url>`

Analyze content quality, search for content by topic, and track phrase trends.

**MCP tools:** `content_analysis_search`, `content_analysis_summary`, `content_analysis_phrase_trends`

**Parameters:** keyword (for search/trends) or URL (for summary)

**Output:** Content matches with quality scores, sentiment analysis, readability metrics, phrase trend data over time.

### `/seo dataforseo listings <keyword>`

Search business listings for local SEO competitive analysis.

**MCP tools:** `business_data_business_listings_search`

**Parameters:** keyword, location (optional)

**Output:** Business name, description, category, address, phone, domain, rating, review count, claimed status.

---

## AI Visibility / GEO

### `/seo dataforseo ai-scrape <query>`

Scrape what ChatGPT web search returns for a query. Real GEO visibility check: see which sources ChatGPT cites for your target keywords.

**MCP tools:** `ai_optimization_chat_gpt_scraper`

**Parameters:** query, location_code (optional), language_code (optional). Use `ai_optimization_chat_gpt_scraper_locations` to look up available locations.

**Output:** ChatGPT response content, cited sources/URLs, referenced domains.

### `/seo dataforseo ai-mentions <keyword>`

Track how LLMs mention brands, domains, and topics. Critical for GEO. Measures actual AI visibility across multiple LLM platforms.

**MCP tools:** `ai_opt_llm_ment_search`, `ai_opt_llm_ment_top_domains`, `ai_opt_llm_ment_top_pages`, `ai_opt_llm_ment_agg_metrics`

**Parameters:** keyword, location_code (optional), language_code (optional). Use `ai_opt_llm_ment_loc_and_lang` for available locations/languages and `ai_optimization_llm_models` for supported LLM models.

**Workflow:**
1. Search LLM mentions with `ai_opt_llm_ment_search` (find mentions of a brand/keyword across LLM responses)
2. Get top cited domains with `ai_opt_llm_ment_top_domains` (which domains are most cited for this topic)
3. Get top cited pages with `ai_opt_llm_ment_top_pages` (which specific pages are most cited)
4. Get aggregate metrics with `ai_opt_llm_ment_agg_metrics` (overall mention volume, trends)

**Output:** LLM mention count, top cited domains with frequency, top cited pages, mention trends over time, cross-platform visibility scores.

**Advanced:** Use `ai_opt_llm_ment_cross_agg_metrics` for cross-model comparison (how mentions differ across ChatGPT, Claude, Perplexity, etc.).

---

## Available Utility Tools

These DataForSEO tools are available for internal use by the agent but do not have dedicated commands:

- `serp_locations`:Location code lookups for SERP queries
- `serp_youtube_locations`:Location code lookups for YouTube queries
- `kw_data_google_ads_locations`:Location lookups for keyword data
- `kw_data_dfs_trends_demography`:Demographic data for trend analysis
- `kw_data_dfs_trends_subregion_interests`:Subregion interest data for trends
- `kw_data_dfs_trends_explore`:DFS proprietary trends data
- `kw_data_google_trends_categories`:Google Trends category lookups
- `dataforseo_labs_google_keyword_overview`:Quick keyword metrics overview
- `dataforseo_labs_google_historical_serp`:Historical SERP results for a keyword
- `dataforseo_labs_google_serp_competitors`:Competitors for a specific SERP
- `dataforseo_labs_google_keywords_for_site`:Keywords a site ranks for (alternative to ranked)
- `dataforseo_labs_google_page_intersection`:Page-level intersection analysis
- `dataforseo_labs_google_historical_rank_overview`:Historical domain rank data
- `dataforseo_labs_google_historical_keyword_data`:Historical keyword metrics
- `dataforseo_labs_available_filters`:Available filter options for Labs endpoints
- `backlinks_competitors`:Find domains with similar backlink profiles
- `backlinks_bulk_backlinks`:Bulk backlink counts for multiple targets
- `backlinks_bulk_new_lost_referring_domains`:Bulk new/lost referring domains
- `backlinks_bulk_new_lost_backlinks`:Bulk new/lost backlinks
- `backlinks_bulk_ranks`:Bulk rank overview for multiple targets
- `backlinks_bulk_referring_domains`:Bulk referring domain counts
- `backlinks_domain_pages_summary`:Summary of pages on a domain
- `backlinks_domain_pages`:List pages on a domain with backlink data
- `backlinks_page_intersection`:Shared backlink sources at page level
- `backlinks_referring_networks`:Referring network analysis
- `backlinks_timeseries_new_lost_summary`:Track new/lost backlinks over time
- `backlinks_bulk_pages_summary`:Bulk page summaries
- `backlinks_available_filters`:Available filter options for Backlinks endpoints
- `domain_analytics_whois_available_filters`:WHOIS filter options
- `domain_analytics_technologies_available_filters`:Technology detection filter options
- `ai_opt_kw_data_loc_and_lang`:AI optimization keyword data locations/languages
- `ai_optimization_keyword_data_search_volume`:AI-specific keyword volume data
- `ai_optimization_llm_response`:Direct LLM response analysis
- `ai_optimization_llm_mentions_filters`:Available filters for LLM mentions
- `ai_optimization_chat_gpt_scraper_locations`:Available locations for ChatGPT scraper

## Cross-Skill Integration

When DataForSEO MCP tools are available, other claude-seo skills can leverage live data:

- **seo-audit**:Spawn `seo-dataforseo` agent for real SERP, backlink, on-page, and listings data
- **seo-technical**:Use `on_page_instant_pages` / `on_page_lighthouse` for real crawl data, `domain_analytics_technologies_domain_technologies` for stack detection
- **seo-content**:Use `kw_data_google_ads_search_volume`, `dataforseo_labs_bulk_keyword_difficulty`, `dataforseo_labs_search_intent` for real keyword metrics, `content_analysis_summary` for content quality
- **seo-page**:Use `serp_organic_live_advanced` for real SERP positions, `backlinks_summary` for link data
- **seo-geo**:Use `ai_optimization_chat_gpt_scraper` for real ChatGPT visibility, `ai_opt_llm_ment_search` for LLM mention tracking
- **seo-plan**:Use `dataforseo_labs_google_competitors_domain`, `dataforseo_labs_google_domain_intersection`, `dataforseo_labs_bulk_traffic_estimation` for real competitive intelligence

## Error Handling

- **MCP server not connected**: Report that DataForSEO extension is not installed or MCP server is unreachable. Suggest running `./extensions/dataforseo/install.sh`
- **API authentication failed**: Report invalid credentials. Suggest checking DataForSEO API login/password in MCP config
- **Rate limit exceeded**: Report the limit hit and suggest waiting before retrying
- **No results returned**: Report "no data found" for the query rather than guessing. Suggest broadening the query or checking location/language codes
- **Invalid location code**: Report the error and suggest using the locations lookup tool to find the correct code

## Output Formatting

Match existing claude-seo output patterns:
- Use tables for comparative data
- Prioritize issues as Critical > High > Medium > Low
- Include specific, actionable recommendations
- Show scores as XX/100 where applicable
- Note data source as "DataForSEO (live)" to distinguish from static analysis
```

## File: `hooks/hooks.json`
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/validate-schema.py\" \"$FILE_PATH\""
          }
        ]
      }
    ]
  }
}
```

## File: `hooks/pre-commit-seo-check.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Pre-commit SEO validation hook for Claude Code.
#
# Hook configuration in ~/.claude/settings.json:
# {
#   "hooks": {
#     "PreToolUse": [
#       {
#         "matcher": "Bash",
#         "hooks": [
#           {
#             "type": "command",
#             "command": "~/.claude/skills/seo/hooks/pre-commit-seo-check.sh"
#           }
#         ]
#       }
#     ]
#   }
# }
#
# NOTE: The matcher is "Bash" (tool name only). This script runs on ALL
# Bash tool uses. It checks if there are staged files before proceeding.
# If there are no staged changes, it exits 0 immediately.

ERRORS=0
WARNINGS=0

# Check if there are staged changes: exit early if not
if ! git diff --cached --quiet 2>/dev/null; then
    : # There are staged changes, proceed with checks
else
    exit 0  # No staged changes, nothing to check
fi

echo "🔍 Running pre-commit SEO checks..."

# Check staged HTML-like files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null | grep -E '\.(html|htm|php|jsx|tsx|vue|svelte)$' || true)

if [ -z "${STAGED_FILES}" ]; then
    echo "✓ No HTML files staged; skipping SEO checks"
    exit 0
fi

for file in ${STAGED_FILES}; do
    if [ ! -f "${file}" ]; then
        continue
    fi

    # Check for placeholder text in schema
    if grep -qiE '\[(Business Name|City|State|Phone|Address|Your|INSERT|REPLACE)\]' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: Contains placeholder text in schema markup"
        ERRORS=$((ERRORS + 1))
    fi

    # Check title tag length
    TITLE=$(grep -oP '(?<=<title>).*?(?=</title>)' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${TITLE}" ]; then
        TITLE_LEN=${#TITLE}
        if [ "${TITLE_LEN}" -lt 30 ] || [ "${TITLE_LEN}" -gt 60 ]; then
            echo "⚠️  ${file}: Title tag length ${TITLE_LEN} chars (recommend 30-60)"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi

    # Check for images without alt text
    if grep -qP '<img(?![^>]*alt=)' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: Images found without alt text"
        WARNINGS=$((WARNINGS + 1))
    fi

    # Check for deprecated schema types
    if grep -qE '"@type"\s*:\s*"(HowTo|SpecialAnnouncement)"' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: Contains deprecated schema type"
        ERRORS=$((ERRORS + 1))
    fi

    # Check for FID references (should be INP)
    if grep -qi 'First Input Delay\|"FID"' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: References FID; should use INP (Interaction to Next Paint)"
        WARNINGS=$((WARNINGS + 1))
    fi

    # Check meta description length
    META_DESC=$(grep -oP '(?<=<meta name="description" content=").*?(?=")' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${META_DESC}" ]; then
        META_LEN=${#META_DESC}
        if [ "${META_LEN}" -lt 120 ] || [ "${META_LEN}" -gt 160 ]; then
            echo "⚠️  ${file}: Meta description length ${META_LEN} chars (recommend 120-160)"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

echo ""
if [ "${ERRORS}" -gt 0 ]; then
    echo "🛑 ${ERRORS} critical error(s) found; commit blocked"
    echo "Fix the errors above and try again."
    exit 2
elif [ "${WARNINGS}" -gt 0 ]; then
    echo "⚠️  ${WARNINGS} warning(s) found; commit allowed"
    exit 0
else
    echo "✓ All SEO checks passed"
    exit 0
fi
```

## File: `hooks/validate-schema.py`
```python
#!/usr/bin/env python3
"""Post-edit schema validation hook for Claude Code.

Validates JSON-LD schema after file edits. Returns exit code 2 to block
if critical validation errors found.

Hook configuration in ~/.claude/settings.json:
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/seo/hooks/validate-schema.py \"$FILE_PATH\"",
            "exitCodes": { "2": "block" }
          }
        ]
      }
    ]
  }
}

Note: matcher filters by tool name only (Edit, Write). The script itself
checks if the file contains schema markup before validating.
"""

import json
import re
import sys
import os
from typing import List


def validate_jsonld(content: str) -> List[str]:
    """Validate JSON-LD blocks in HTML content."""
    errors = []
    pattern = r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>'
    blocks = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)

    if not blocks:
        return []  # No schema found; not an error

    for i, block in enumerate(blocks, 1):
        block = block.strip()
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"Block {i}: Invalid JSON; {e}")
            continue

        if isinstance(data, list):
            for item in data:
                errors.extend(_validate_schema_object(item, i))
        elif isinstance(data, dict):
            errors.extend(_validate_schema_object(data, i))

    return errors


def _validate_schema_object(obj: dict, block_num: int) -> List[str]:
    """Validate a single schema object."""
    errors = []
    prefix = f"Block {block_num}"

    # Check @context
    if "@context" not in obj:
        errors.append(f"{prefix}: Missing @context")
    elif obj["@context"] not in ("https://schema.org", "http://schema.org"):
        errors.append(f"{prefix}: @context should be 'https://schema.org'")

    # Check @type
    if "@type" not in obj:
        errors.append(f"{prefix}: Missing @type")

    # Check for placeholder text
    placeholders = [
        "[Business Name]",
        "[City]",
        "[State]",
        "[Phone]",
        "[Address]",
        "[Your",
        "[INSERT",
        "REPLACE",
        "[URL]",
        "[Email]",
    ]
    text = json.dumps(obj)
    for p in placeholders:
        if p.lower() in text.lower():
            errors.append(f"{prefix}: Contains placeholder text: {p}")

    # Check for deprecated types
    schema_type = obj.get("@type", "")
    deprecated = {
        "HowTo": "deprecated September 2023",
        "SpecialAnnouncement": "deprecated July 31, 2025",
        "CourseInfo": "retired June 2025",
        "EstimatedSalary": "retired June 2025",
        "LearningVideo": "retired June 2025",
        "ClaimReview": "retired June 2025; fact-check rich results discontinued",
        "VehicleListing": "retired June 2025; vehicle listing structured data discontinued",
    }
    if schema_type in deprecated:
        errors.append(f"{prefix}: @type '{schema_type}' is {deprecated[schema_type]}")

    # Check for restricted types used incorrectly
    restricted = {"FAQPage": "restricted to government and healthcare sites only (Aug 2023)"}
    if schema_type in restricted:
        errors.append(f"{prefix}: @type '{schema_type}' is {restricted[schema_type]}; verify site qualifies")

    return errors


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        sys.exit(0)

    # Only validate HTML-like files
    valid_extensions = (".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".php", ".ejs")
    if not filepath.endswith(valid_extensions):
        sys.exit(0)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except (OSError, IOError):
        sys.exit(0)

    errors = validate_jsonld(content)

    if not errors:
        sys.exit(0)

    # Categorize errors
    critical_keywords = ["placeholder", "deprecated", "retired"]
    critical = [e for e in errors if any(kw in e.lower() for kw in critical_keywords)]
    warnings = [e for e in errors if e not in critical]

    if warnings:
        print("⚠️  Schema validation warnings:")
        for w in warnings:
            print(f"  - {w}")

    if critical:
        print("🛑 Schema validation ERRORS (blocking):")
        for e in critical:
            print(f"  - {e}")
        sys.exit(2)  # Block the edit

    sys.exit(1)  # Warnings only; proceed


if __name__ == "__main__":
    main()
```

## File: `pdf/google-seo-reference.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Google SEO Quick Reference (February 2026)

Concise reference guide for subagents. Summarizes key Google Search concepts,
requirements, and best practices. Not a reproduction of Google's documentation;
see Official Documentation Links at the bottom for full details.

---

## How Google Search Works

Google Search operates in three stages: **Crawling** (Googlebot discovers pages by following links and reading sitemaps), **Indexing** (Google processes and stores page content, metadata, and signals in its search index), and **Serving** (when a user searches, Google's algorithms rank indexed pages by relevance, quality, and usability to return the most useful results). Pages must be crawlable and indexable to appear in search results.

---

## Google Search Essentials

Formerly known as "Webmaster Guidelines." Key requirements:

### Technical Requirements
- Pages must be accessible to Googlebot (not blocked by robots.txt or noindex)
- Pages must return HTTP 200 status for indexable content
- Content must be in a format Google can process (HTML preferred, JS-rendered content supported but slower)
- Pages must be served over HTTPS

### Spam Policies
- No cloaking (showing different content to Googlebot vs users)
- No doorway pages (pages created solely to rank for specific queries)
- No hidden text or links
- No keyword stuffing
- No link spam (buying links, excessive link exchanges)
- No scraped or auto-generated content without added value
- No sneaky redirects
- No thin affiliate pages

### Key Best Practices
- Create content for users, not search engines
- Make your site easy to navigate with a clear hierarchy
- Use descriptive, unique titles and meta descriptions per page
- Use heading tags (H1-H6) to structure content logically
- Optimize images with alt text and appropriate file sizes
- Ensure mobile-friendly responsive design
- Improve page load speed (Core Web Vitals)
- Submit an XML sitemap to Google Search Console
- Use structured data (JSON-LD) to help Google understand content

---

## Content Quality Signals

Google evaluates content quality through the E-E-A-T framework:

- **Experience**: Does the content creator have first-hand experience with the topic? (Original photos, personal stories, demonstrated use)
- **Expertise**: Does the creator have relevant knowledge or credentials? (Professional background, technical depth, accurate sourcing)
- **Authoritativeness**: Is the creator or site recognized as a go-to source? (Industry citations, brand mentions, expert recognition)
- **Trustworthiness**: Is the content and site reliable and transparent? (Contact info, secure site, editorial standards, accurate claims)

> **YMYL Note**: "Your Money or Your Life" topics (health, finance, safety, legal) are held to the highest E-E-A-T standards. Inaccurate YMYL content can cause real-world harm, so Google applies stricter quality thresholds.

> **December 2025 Update**: E-E-A-T evaluation now extends to ALL competitive queries, not just YMYL topics. Every page competing for ranking is assessed on these signals.

---

## Core Web Vitals

Measured at the 75th percentile of real user data (field data).

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s – 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms – 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 – 0.25 | > 0.25 |

**Key facts:**
- INP replaced FID (First Input Delay) on March 12, 2024. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on September 9, 2024. Do NOT reference FID.
- Core Web Vitals are a confirmed ranking signal (since June 2021)
- Field data (CrUX) is preferred over lab data (Lighthouse) for assessment
- Passing all three metrics at "Good" is the target

**Measurement tools:**
- Google PageSpeed Insights (field + lab data)
- Chrome User Experience Report (CrUX): field data
- Lighthouse (lab data only)
- Google Search Console Core Web Vitals report

---

## Structured Data Best Practices

- **JSON-LD is Google's preferred format** (over Microdata and RDFa)
- Place JSON-LD in `<script type="application/ld+json">` tags in the `<head>` or `<body>`
- Always include `@context` and `@type` properties
- **Required properties** must be present for rich result eligibility
- **Recommended properties** improve rich result quality but aren't mandatory
- Only mark up content that is visible on the page
- Use Google's Rich Results Test to validate before deployment
- Do not mark up content that is misleading or hidden from users
- Keep schema current: update when page content changes

### Deprecated/Restricted Types (as of Feb 2026)
- **HowTo**: Rich results removed (September 2023)
- **FAQ**: Restricted to government and healthcare authority sites (August 2023)
- **SpecialAnnouncement**: Deprecated (July 31, 2025)
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired (June 2025)
- **ClaimReview**: Retired (June 2025)
- **VehicleListing**: Retired (June 2025)

---

## Common Penalties & How to Avoid Them

### Manual Actions
Google Search Console notifications for violations. Common causes:
- **Unnatural links** (buying/selling links): Disavow bad links, request reconsideration
- **Thin content**: Add substantial unique value to affected pages
- **Cloaking/sneaky redirects**: Remove deceptive serving, request reconsideration
- **User-generated spam**: Moderate comments/forums, add nofollow to user links
- **Structured data issues**: Fix misleading or spam markup

### Algorithmic Demotions
No manual notification, detected through ranking drops. Common causes:
- **Helpful Content System**: Merged into Google's core ranking in March 2024: no longer a standalone system. Helpfulness signals are now evaluated within every core update. Low-value, AI-generated, or unhelpful content at scale still triggers demotions via core updates.
- **Core Updates**: Broad quality reassessment across all signals
- **Spam Updates**: Automated detection of spam patterns
- **Link Spam Updates**: Devaluation of manipulative link patterns

### Recovery Steps
1. Identify the issue (Search Console, ranking timeline analysis)
2. Fix the root cause (remove spam, improve content, clean links)
3. For manual actions: submit reconsideration request via Search Console
4. For algorithmic: improve quality, wait for next core update reassessment
5. Monitor recovery in Search Console performance reports

---

## Official Documentation Links

- [Google Search Essentials](https://developers.google.com/search/brain/knowledge/docs_legacy/essentials)
- [How Google Search Works](https://developers.google.com/search/brain/knowledge/docs_legacy/fundamentals/how-search-works)
- [Structured Data Overview](https://developers.google.com/search/brain/knowledge/docs_legacy/appearance/structured-data/intro-structured-data)
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Core Web Vitals Report](https://support.google.com/webmasters/answer/9205520)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Search Console Help](https://support.google.com/webmasters)
- [Manual Actions Report](https://support.google.com/webmasters/answer/9044175)
- [Google Search Status Dashboard](https://status.search.google.com/)
- [Google Search Central Blog](https://developers.google.com/search/blog)
- [Spam Policies](https://developers.google.com/search/brain/knowledge/docs_legacy/essentials/spam-policies)
- [E-E-A-T and Quality Rater Guidelines](https://developers.google.com/search/brain/knowledge/docs_legacy/fundamentals/creating-helpful-content)

> **Mobile-first indexing** is 100% complete as of July 5, 2024. Google now crawls and indexes ALL websites exclusively with the mobile Googlebot user-agent.
```

## File: `schema/templates.json`
```json
{
  "templates": [
    {
      "type": "VideoObject",
      "description": "Video content pages with thumbnails, duration, and playback URLs. Enables video rich results in Google Search.",
      "template": {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": "[Video Title]",
        "description": "[Video Description]",
        "thumbnailUrl": "[Thumbnail Image URL]",
        "uploadDate": "[YYYY-MM-DD]",
        "duration": "[ISO 8601 Duration, e.g. PT1H30M]",
        "contentUrl": "[Direct Video File URL]",
        "embedUrl": "[Embed Player URL]",
        "publisher": {
          "@type": "Organization",
          "name": "[Publisher Name]",
          "logo": {
            "@type": "ImageObject",
            "url": "[Logo URL]"
          }
        }
      }
    },
    {
      "type": "BroadcastEvent",
      "description": "Live streaming content for LIVE badge in Google Search results. Requires VideoObject and isLiveBroadcast flag.",
      "template": {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": "[Live Stream Title]",
        "description": "[Live Stream Description]",
        "thumbnailUrl": "[Thumbnail Image URL]",
        "uploadDate": "[YYYY-MM-DD]",
        "contentUrl": "[Stream URL]",
        "embedUrl": "[Embed Player URL]",
        "publication": {
          "@type": "BroadcastEvent",
          "isLiveBroadcast": true,
          "startDate": "[YYYY-MM-DDTHH:MM:SSZ]",
          "endDate": "[YYYY-MM-DDTHH:MM:SSZ]"
        }
      }
    },
    {
      "type": "Clip",
      "description": "Key moments or chapters within a video. Enables key moments rich results with timestamp links.",
      "template": {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": "[Video Title]",
        "description": "[Video Description]",
        "thumbnailUrl": "[Thumbnail Image URL]",
        "uploadDate": "[YYYY-MM-DD]",
        "contentUrl": "[Direct Video File URL]",
        "hasPart": [
          {
            "@type": "Clip",
            "name": "[Clip Title]",
            "startOffset": 0,
            "endOffset": 120,
            "url": "[Video URL with timestamp, e.g. ?t=0]"
          },
          {
            "@type": "Clip",
            "name": "[Next Clip Title]",
            "startOffset": 120,
            "endOffset": 300,
            "url": "[Video URL with timestamp, e.g. ?t=120]"
          }
        ]
      }
    },
    {
      "type": "SeekToAction",
      "description": "Enable seek functionality in video rich results. Allows users to jump to specific timestamps from search.",
      "template": {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": "[Video Title]",
        "description": "[Video Description]",
        "thumbnailUrl": "[Thumbnail Image URL]",
        "uploadDate": "[YYYY-MM-DD]",
        "contentUrl": "[Direct Video File URL]",
        "potentialAction": {
          "@type": "SeekToAction",
          "target": "[Video URL]?t={seek_to_second_number}",
          "startOffset-input": "required name=seek_to_second_number"
        }
      }
    },
    {
      "type": "SoftwareSourceCode",
      "description": "Open source and code repository pages. Describes programming language, platform, and repository location.",
      "template": {
        "@context": "https://schema.org",
        "@type": "SoftwareSourceCode",
        "name": "[Repository Name]",
        "description": "[Repository Description]",
        "codeRepository": "[Repository URL, e.g. https://github.com/org/repo]",
        "programmingLanguage": "[Language, e.g. Python]",
        "runtimePlatform": "[Platform, e.g. Node.js]",
        "author": {
          "@type": "Person",
          "name": "[Author Name]"
        },
        "license": "[License URL, e.g. https://opensource.org/licenses/MIT]",
        "dateCreated": "[YYYY-MM-DD]",
        "dateModified": "[YYYY-MM-DD]"
      }
    },
    {
      "type": "ProductGroup",
      "description": "E-commerce product variants grouped by attributes like size, color. Enables variant-aware rich results with variesBy and hasVariant properties.",
      "template": {
        "@context": "https://schema.org",
        "@type": "ProductGroup",
        "name": "[Product Name]",
        "description": "[Product group description]",
        "productGroupID": "[product-group-id]",
        "variesBy": ["https://schema.org/size", "https://schema.org/color"],
        "hasVariant": [
          {
            "@type": "Product",
            "name": "[Variant - Red, Large]",
            "sku": "[SKU-001]",
            "color": "[Red]",
            "size": "[Large]",
            "offers": {
              "@type": "Offer",
              "price": "[29.99]",
              "priceCurrency": "USD",
              "availability": "https://schema.org/InStock"
            }
          }
        ]
      }
    },
    {
      "type": "ProfilePage",
      "description": "Author, creator, or team member profile pages. Enhances E-E-A-T signals with mainEntity Person markup and sameAs links.",
      "template": {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "mainEntity": {
          "@type": "Person",
          "name": "[Author Name]",
          "url": "[Profile URL]",
          "description": "[Author bio and expertise summary]",
          "sameAs": [
            "[Twitter URL]",
            "[LinkedIn URL]"
          ]
        }
      }
    },
    {
      "type": "Certification",
      "description": "Product certifications (Energy Star, safety, organic, etc.). Replaced EnergyConsumptionDetails in April 2025.",
      "template": {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "[Product Name]",
        "hasCertification": {
          "@type": "Certification",
          "certificationIdentification": "[Certification Name, e.g. Energy Star]",
          "issuedBy": {
            "@type": "Organization",
            "name": "[Issuing Organization, e.g. EPA]"
          }
        }
      }
    },
    {
      "type": "OfferShippingDetails",
      "description": "Shipping and delivery information for e-commerce products. Includes shipping rate, handling time, and transit time.",
      "template": {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "[Product Name]",
        "offers": {
          "@type": "Offer",
          "price": "[Price]",
          "priceCurrency": "USD",
          "shippingDetails": {
            "@type": "OfferShippingDetails",
            "shippingRate": {
              "@type": "MonetaryAmount",
              "value": "[0]",
              "currency": "USD"
            },
            "deliveryTime": {
              "@type": "ShippingDeliveryTime",
              "handlingTime": {
                "@type": "QuantitativeValue",
                "minValue": 0,
                "maxValue": 1,
                "unitCode": "DAY"
              },
              "transitTime": {
                "@type": "QuantitativeValue",
                "minValue": 1,
                "maxValue": 5,
                "unitCode": "DAY"
              }
            }
          }
        }
      }
    }
  ]
}
```

## File: `scripts/analyze_visual.py`
```python
#!/usr/bin/env python3
"""
Analyze visual aspects of a web page using Playwright.

Usage:
    python analyze_visual.py https://example.com
"""

import argparse
import ipaddress
import json
import socket
import sys
from urllib.parse import ParseResult, urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Error: playwright required. Install with: pip install playwright && playwright install chromium")
    sys.exit(1)


def normalize_url(url: str) -> tuple[str, ParseResult]:
    """Normalize URL and return (url, parsed_url)."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")
    if not parsed.hostname:
        raise ValueError("Invalid URL: missing hostname")

    return url, parsed


def analyze_visual(url: str, timeout: int = 30000) -> dict:
    """
    Analyze visual aspects of a web page.

    Args:
        url: URL to analyze
        timeout: Page load timeout in milliseconds

    Returns:
        Dictionary with visual analysis results
    """
    result = {
        "url": url,
        "above_fold": {
            "h1_visible": False,
            "cta_visible": False,
            "hero_image": None,
        },
        "mobile": {
            "viewport_meta": False,
            "horizontal_scroll": False,
            "touch_targets_ok": True,
        },
        "layout": {
            "overlapping_elements": [],
            "text_overflow": [],
        },
        "fonts": {
            "base_size": None,
            "readable": True,
        },
        "error": None,
    }

    try:
        url, parsed = normalize_url(url)
        result["url"] = url
    except ValueError as e:
        result["error"] = str(e)
        return result

    # SSRF prevention: block private/internal IPs
    try:
        resolved_ip = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved_ip)
        if ip.is_private or ip.is_loopback or ip.is_reserved:
            result["error"] = f"Blocked: URL resolves to private/internal IP ({resolved_ip})"
            return result
    except socket.gaierror:
        pass

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            # Desktop analysis
            desktop = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = desktop.new_page()
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # Check H1 visibility above fold
            h1 = page.query_selector("h1")
            if h1:
                box = h1.bounding_box()
                if box and box["y"] < 1080:
                    result["above_fold"]["h1_visible"] = True

            # Check for CTA buttons above fold
            cta_selectors = [
                "a[href*='signup']",
                "a[href*='contact']",
                "a[href*='demo']",
                "button:has-text('Get Started')",
                "button:has-text('Sign Up')",
                "button:has-text('Contact')",
                ".cta",
                "[class*='cta']",
            ]
            for selector in cta_selectors:
                try:
                    cta = page.query_selector(selector)
                    if cta:
                        box = cta.bounding_box()
                        if box and box["y"] < 1080:
                            result["above_fold"]["cta_visible"] = True
                            break
                except Exception:
                    pass

            # Check hero image
            hero_selectors = [
                ".hero img",
                "[class*='hero'] img",
                "header img",
                "main img:first-of-type",
            ]
            for selector in hero_selectors:
                try:
                    hero = page.query_selector(selector)
                    if hero:
                        src = hero.get_attribute("src")
                        if src:
                            result["above_fold"]["hero_image"] = src
                            break
                except Exception:
                    pass

            desktop.close()

            # Mobile analysis
            mobile = browser.new_context(viewport={"width": 375, "height": 812})
            page = mobile.new_page()
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # Check viewport meta
            viewport_meta = page.query_selector('meta[name="viewport"]')
            result["mobile"]["viewport_meta"] = viewport_meta is not None

            # Check for horizontal scroll
            scroll_width = page.evaluate("document.documentElement.scrollWidth")
            viewport_width = page.evaluate("window.innerWidth")
            result["mobile"]["horizontal_scroll"] = scroll_width > viewport_width

            # Check font size
            base_font_size = page.evaluate("""
                () => {
                    const body = document.body;
                    const style = window.getComputedStyle(body);
                    return parseFloat(style.fontSize);
                }
            """)
            result["fonts"]["base_size"] = base_font_size
            result["fonts"]["readable"] = base_font_size >= 16

            mobile.close()
            browser.close()

    except PlaywrightTimeout:
        result["error"] = f"Page load timed out after {timeout}ms"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Analyze visual aspects of a web page")
    parser.add_argument("url", help="URL to analyze")
    parser.add_argument("--timeout", "-t", type=int, default=30000, help="Timeout in ms")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    result = analyze_visual(args.url, timeout=args.timeout)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Visual Analysis Results")
        print("=" * 40)

        print("\nAbove the Fold:")
        print(f"  H1 Visible: {'✓' if result['above_fold']['h1_visible'] else '✗'}")
        print(f"  CTA Visible: {'✓' if result['above_fold']['cta_visible'] else '✗'}")
        print(f"  Hero Image: {result['above_fold']['hero_image'] or 'None found'}")

        print("\nMobile Responsiveness:")
        print(f"  Viewport Meta: {'✓' if result['mobile']['viewport_meta'] else '✗'}")
        print(f"  Horizontal Scroll: {'✗ (problem)' if result['mobile']['horizontal_scroll'] else '✓'}")

        print("\nTypography:")
        print(f"  Base Font Size: {result['fonts']['base_size']}px")
        print(f"  Readable (≥16px): {'✓' if result['fonts']['readable'] else '✗'}")

        if result["error"]:
            print(f"\nError: {result['error']}")


if __name__ == "__main__":
    main()
```

## File: `scripts/capture_screenshot.py`
```python
#!/usr/bin/env python3
"""
Capture screenshots of web pages using Playwright.

Usage:
    python capture_screenshot.py https://example.com
    python capture_screenshot.py https://example.com --mobile
    python capture_screenshot.py https://example.com --output screenshots/
"""

import argparse
import ipaddress
import os
import socket
import sys
from urllib.parse import ParseResult, urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Error: playwright required. Install with: pip install playwright && playwright install chromium")
    sys.exit(1)


VIEWPORTS = {
    "desktop": {"width": 1920, "height": 1080},
    "laptop": {"width": 1366, "height": 768},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812},
}


def normalize_url(url: str) -> tuple[str, ParseResult]:
    """Normalize URL and return (url, parsed_url)."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")
    if not parsed.hostname:
        raise ValueError("Invalid URL: missing hostname")

    return url, parsed


def capture_screenshot(
    url: str,
    output_path: str,
    viewport: str = "desktop",
    full_page: bool = False,
    timeout: int = 30000,
) -> dict:
    """
    Capture a screenshot of a web page.

    Args:
        url: URL to capture
        output_path: Output file path
        viewport: Viewport preset (desktop, laptop, tablet, mobile)
        full_page: Whether to capture full page or just viewport
        timeout: Page load timeout in milliseconds

    Returns:
        Dictionary with capture results
    """
    result = {
        "url": url,
        "output": output_path,
        "viewport": viewport,
        "success": False,
        "error": None,
    }

    if viewport not in VIEWPORTS:
        result["error"] = f"Invalid viewport: {viewport}. Choose from: {list(VIEWPORTS.keys())}"
        return result

    try:
        url, parsed = normalize_url(url)
        result["url"] = url
    except ValueError as e:
        result["error"] = str(e)
        return result

    # SSRF prevention: block private/internal IPs
    try:
        resolved_ip = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved_ip)
        if ip.is_private or ip.is_loopback or ip.is_reserved:
            result["error"] = f"Blocked: URL resolves to private/internal IP ({resolved_ip})"
            return result
    except socket.gaierror:
        pass

    vp = VIEWPORTS[viewport]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": vp["width"], "height": vp["height"]},
                device_scale_factor=2 if viewport == "mobile" else 1,
            )
            page = context.new_page()

            # Navigate and wait for network idle
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # Wait a bit more for any lazy-loaded content
            page.wait_for_timeout(1000)

            # Capture screenshot
            page.screenshot(path=output_path, full_page=full_page)

            result["success"] = True
            browser.close()

    except PlaywrightTimeout:
        result["error"] = f"Page load timed out after {timeout}ms"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Capture web page screenshots")
    parser.add_argument("url", help="URL to capture")
    parser.add_argument("--output", "-o", default="screenshots", help="Output directory")
    parser.add_argument("--viewport", "-v", default="desktop", choices=VIEWPORTS.keys())
    parser.add_argument("--all", "-a", action="store_true", help="Capture all viewports")
    parser.add_argument("--full", "-f", action="store_true", help="Capture full page")
    parser.add_argument("--timeout", "-t", type=int, default=30000, help="Timeout in ms")

    args = parser.parse_args()

    # Sanitize output path - prevent directory traversal
    output_dir = os.path.realpath(args.output)
    cwd = os.getcwd()
    home = os.path.expanduser("~")
    if not (output_dir.startswith(cwd) or output_dir.startswith(home)):
        print("Error: Output path must be within current directory or home directory", file=sys.stderr)
        sys.exit(1)

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    try:
        normalized_url, parsed_url = normalize_url(args.url)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate filename from URL
    base_name = parsed_url.netloc.replace(".", "_")

    viewports = VIEWPORTS.keys() if args.all else [args.viewport]

    for viewport in viewports:
        filename = f"{base_name}_{viewport}.png"
        output_path = os.path.join(args.output, filename)

        print(f"Capturing {viewport} screenshot...")
        result = capture_screenshot(
            normalized_url,
            output_path,
            viewport=viewport,
            full_page=args.full,
            timeout=args.timeout,
        )

        if result["success"]:
            print(f"  ✓ Saved to {output_path}")
        else:
            print(f"  ✗ Failed: {result['error']}")


if __name__ == "__main__":
    main()
```

## File: `scripts/crux_history.py`
```python
#!/usr/bin/env python3
"""
CrUX History API for Core Web Vitals trends over time.

Fetches up to 25 weekly data points from the Chrome UX Report History API
and identifies improving, stable, or degrading trends per metric.

Usage:
    python crux_history.py https://example.com
    python crux_history.py https://example.com --form-factor PHONE --json
    python crux_history.py https://example.com --origin
"""

import argparse
import json
import sys
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)

try:
    from google_auth import get_api_key, validate_url
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_api_key, validate_url

CRUX_HISTORY_ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord"

CWV_THRESHOLDS = {
    "largest_contentful_paint": {"good": 2500, "poor": 4000, "label": "LCP", "unit": "ms"},
    "interaction_to_next_paint": {"good": 200, "poor": 500, "label": "INP", "unit": "ms"},
    "cumulative_layout_shift": {"good": 0.1, "poor": 0.25, "label": "CLS", "unit": ""},
    "first_contentful_paint": {"good": 1800, "poor": 3000, "label": "FCP", "unit": "ms"},
    "experimental_time_to_first_byte": {"good": 800, "poor": 1800, "label": "TTFB", "unit": "ms"},
}


def query_history(
    url_or_origin: str,
    api_key: str,
    form_factor: Optional[str] = None,
) -> dict:
    """
    Query CrUX History API for weekly CWV trends.

    Args:
        url_or_origin: Full URL or origin.
        api_key: Google API key.
        form_factor: DESKTOP, PHONE, or TABLET. None for all.

    Returns:
        Dictionary with metrics timeseries, collection periods, and trend analysis.
    """
    result = {
        "target": url_or_origin,
        "form_factor": form_factor or "ALL",
        "metrics": {},
        "collection_periods": [],
        "trends": {},
        "error": None,
    }

    if not validate_url(url_or_origin):
        result["error"] = "Invalid URL. Only http/https URLs to public hosts are accepted."
        return result

    parsed = urlparse(url_or_origin)
    is_origin = parsed.path in ("", "/") and not parsed.query

    body = {}
    if is_origin:
        body["origin"] = f"{parsed.scheme}://{parsed.netloc}"
    else:
        body["url"] = url_or_origin

    if form_factor:
        body["formFactor"] = form_factor.upper()

    try:
        resp = requests.post(
            f"{CRUX_HISTORY_ENDPOINT}?key={api_key}",
            json=body,
            timeout=30,
        )

        if resp.status_code == 404:
            target_type = "origin" if is_origin else "URL"
            result["error"] = (
                f"No CrUX history data for this {target_type}. "
                "Insufficient Chrome traffic volume for eligibility."
            )
            return result

        if resp.status_code == 429:
            result["error"] = "CrUX API rate limit exceeded (150 QPM shared). Wait and retry."
            return result

        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        result["error"] = f"CrUX History API request failed: {e}"
        return result

    record = data.get("record", {})

    # Collection periods
    periods = record.get("collectionPeriods", [])
    for period in periods:
        first = period.get("firstDate", {})
        last = period.get("lastDate", {})
        result["collection_periods"].append({
            "first": f"{first.get('year')}-{first.get('month', 0):02d}-{first.get('day', 0):02d}",
            "last": f"{last.get('year')}-{last.get('month', 0):02d}-{last.get('day', 0):02d}",
        })

    # Metrics timeseries
    for metric_name, metric_data in record.get("metrics", {}).items():
        if metric_name not in CWV_THRESHOLDS:
            continue

        thresholds = CWV_THRESHOLDS[metric_name]
        p75s_data = metric_data.get("percentilesTimeseries", {})
        p75s_raw = p75s_data.get("p75s", [])

        # Parse p75 values (CLS is string-encoded)
        p75s = []
        for val in p75s_raw:
            if val is None:
                p75s.append(None)
            elif metric_name == "cumulative_layout_shift":
                try:
                    p75s.append(float(str(val)))
                except (ValueError, TypeError):
                    p75s.append(None)
            else:
                try:
                    p75s.append(int(val))
                except (ValueError, TypeError):
                    try:
                        p75s.append(float(val))
                    except (ValueError, TypeError):
                        p75s.append(None)

        # Distributions timeseries
        histogram_ts = metric_data.get("histogramTimeseries", [])
        good_pcts = []
        if len(histogram_ts) >= 3:
            good_densities = histogram_ts[0].get("densities", [])
            for d in good_densities:
                if d is None or str(d) == "NaN":
                    good_pcts.append(None)
                else:
                    try:
                        good_pcts.append(round(float(d) * 100, 1))
                    except (ValueError, TypeError):
                        good_pcts.append(None)

        # Extract needs_improvement (bin 1) and poor (bin 2) percentages
        ni_pcts = []
        poor_pcts = []
        if len(histogram_ts) >= 3:
            for bin_idx, target_list in [(1, ni_pcts), (2, poor_pcts)]:
                bin_densities = histogram_ts[bin_idx].get("densities", [])
                for d in bin_densities:
                    if d is None or str(d) == "NaN":
                        target_list.append(None)
                    else:
                        try:
                            target_list.append(round(float(d) * 100, 1))
                        except (ValueError, TypeError):
                            target_list.append(None)

        result["metrics"][metric_name] = {
            "label": thresholds["label"],
            "unit": thresholds["unit"],
            "p75_values": p75s,
            "good_percentages": good_pcts,
            "needs_improvement_percentages": ni_pcts,
            "poor_percentages": poor_pcts,
            "latest_p75": p75s[-1] if p75s and p75s[-1] is not None else None,
            "good_threshold": thresholds["good"],
            "poor_threshold": thresholds["poor"],
        }

    # Trend analysis
    result["trends"] = detect_trends(result["metrics"])

    return result


def detect_trends(metrics: dict) -> dict:
    """
    Analyze p75 timeseries to detect trends.

    Compares the average of the last 4 weeks to the average of the first 4 weeks.

    Returns:
        Dictionary mapping metric names to trend info:
        direction (improving/stable/degrading), change_pct, latest, earliest.
    """
    trends = {}

    for metric_name, data in metrics.items():
        p75s = data.get("p75_values", [])
        valid = [v for v in p75s if v is not None]

        if len(valid) < 8:
            trends[metric_name] = {
                "direction": "insufficient_data",
                "label": data.get("label", metric_name),
            }
            continue

        # First 4 valid vs last 4 valid
        first_4 = valid[:4]
        last_4 = valid[-4:]
        avg_first = sum(first_4) / len(first_4)
        avg_last = sum(last_4) / len(last_4)

        if avg_first == 0:
            change_pct = 0
        else:
            change_pct = ((avg_last - avg_first) / avg_first) * 100

        # For CWV, lower is better (except CLS where lower is also better)
        # So a negative change_pct means improvement
        if abs(change_pct) < 5:
            direction = "stable"
        elif change_pct < 0:
            direction = "improving"
        else:
            direction = "degrading"

        trends[metric_name] = {
            "direction": direction,
            "change_pct": round(change_pct, 1),
            "earliest_avg": round(avg_first, 3) if data.get("unit") == "" else round(avg_first),
            "latest_avg": round(avg_last, 3) if data.get("unit") == "" else round(avg_last),
            "label": data.get("label", metric_name),
            "data_points": len(valid),
        }

    return trends


def main():
    parser = argparse.ArgumentParser(
        description="CrUX History API - Core Web Vitals trends over time"
    )
    parser.add_argument("url", help="URL or origin to analyze")
    parser.add_argument(
        "--form-factor",
        choices=["PHONE", "DESKTOP", "TABLET"],
        help="Filter by form factor",
    )
    parser.add_argument(
        "--api-key",
        help="Google API key (overrides config/env)",
    )
    parser.add_argument(
        "--origin",
        action="store_true",
        help="Force origin-level query (strip path/query)",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    api_key = args.api_key or get_api_key()
    if not api_key:
        print("Error: API key required. Use --api-key or configure GOOGLE_API_KEY.", file=sys.stderr)
        sys.exit(1)

    target = args.url
    if args.origin:
        parsed = urlparse(target)
        target = f"{parsed.scheme}://{parsed.netloc}"

    result = query_history(target, api_key, form_factor=args.form_factor)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get("error"):
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)

        print(f"=== CrUX History ({result.get('form_factor', 'ALL')}) ===")
        print(f"Target: {result.get('target')}")

        periods = result.get("collection_periods", [])
        if periods:
            print(f"Range: {periods[0]['first']} to {periods[-1]['last']} ({len(periods)} weeks)")

        print("\nTrend Analysis:")
        for name, trend in result.get("trends", {}).items():
            label = trend.get("label", name)
            direction = trend.get("direction", "?")
            if direction == "insufficient_data":
                print(f"  {label}: Insufficient data")
                continue

            arrow = {"improving": "IMPROVING", "stable": "STABLE", "degrading": "DEGRADING"}.get(direction, "?")
            change = trend.get("change_pct", 0)
            earliest = trend.get("earliest_avg")
            latest = trend.get("latest_avg")
            print(f"  {label}: {arrow} ({change:+.1f}%) | {earliest} -> {latest}")


if __name__ == "__main__":
    main()
```

## File: `scripts/fetch_page.py`
```python
#!/usr/bin/env python3
"""
Fetch a web page with proper headers and error handling.

Usage:
    python fetch_page.py https://example.com
    python fetch_page.py https://example.com --output page.html
"""

import argparse
import ipaddress
import socket
import sys
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 ClaudeSEO/1.2"
)

# Googlebot UA for prerender/dynamic rendering detection.
# Prerender services (Prerender.io, Rendertron) serve fully rendered HTML to
# Googlebot but raw JS shells to other UAs. Comparing response sizes between
# DEFAULT_USER_AGENT and GOOGLEBOT_USER_AGENT reveals whether a site uses
# dynamic rendering, a key signal for SPA detection.
GOOGLEBOT_USER_AGENT = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
)

DEFAULT_HEADERS = {
    "User-Agent": DEFAULT_USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}


def fetch_page(
    url: str,
    timeout: int = 30,
    follow_redirects: bool = True,
    max_redirects: int = 5,
    user_agent: Optional[str] = None,
) -> dict:
    """
    Fetch a web page and return response details.

    Args:
        url: The URL to fetch
        timeout: Request timeout in seconds
        follow_redirects: Whether to follow redirects
        max_redirects: Maximum number of redirects to follow

    Returns:
        Dictionary with:
            - url: Final URL after redirects
            - status_code: HTTP status code
            - content: Response body
            - headers: Response headers
            - redirect_chain: List of redirect URLs
            - error: Error message if failed
    """
    result = {
        "url": url,
        "status_code": None,
        "content": None,
        "headers": {},
        "redirect_chain": [],
        "redirect_details": [],
        "error": None,
    }

    # Validate URL
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        result["error"] = f"Invalid URL scheme: {parsed.scheme}"
        return result

    # SSRF prevention: block private/internal IPs
    try:
        resolved_ip = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved_ip)
        if ip.is_private or ip.is_loopback or ip.is_reserved:
            result["error"] = f"Blocked: URL resolves to private/internal IP ({resolved_ip})"
            return result
    except (socket.gaierror, ValueError):
        pass  # DNS resolution failure handled by requests below

    try:
        session = requests.Session()
        session.max_redirects = max_redirects

        headers = dict(DEFAULT_HEADERS)
        if user_agent:
            headers["User-Agent"] = user_agent

        response = session.get(
            url,
            headers=headers,
            timeout=timeout,
            allow_redirects=follow_redirects,
        )

        result["url"] = response.url
        result["status_code"] = response.status_code
        result["content"] = response.text
        result["headers"] = dict(response.headers)

        # Track redirect chain with status codes
        if response.history:
            result["redirect_chain"] = [r.url for r in response.history]
            result["redirect_details"] = [
                {"url": r.url, "status_code": r.status_code}
                for r in response.history
            ]

    except requests.exceptions.Timeout:
        result["error"] = f"Request timed out after {timeout} seconds"
    except requests.exceptions.TooManyRedirects:
        result["error"] = f"Too many redirects (max {max_redirects})"
    except requests.exceptions.SSLError as e:
        result["error"] = f"SSL error: {e}"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"Connection error: {e}"
    except requests.exceptions.RequestException as e:
        result["error"] = f"Request failed: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(description="Fetch a web page for SEO analysis")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="Timeout in seconds")
    parser.add_argument("--no-redirects", action="store_true", help="Don't follow redirects")
    parser.add_argument("--user-agent", help="Custom User-Agent string")
    parser.add_argument(
        "--googlebot",
        action="store_true",
        help=(
            "Use Googlebot UA to detect dynamic rendering / prerender services. "
            "Compare response size with default UA to identify SPA prerender configuration."
        ),
    )

    args = parser.parse_args()

    ua = args.user_agent
    if args.googlebot:
        ua = GOOGLEBOT_USER_AGENT

    result = fetch_page(
        args.url,
        timeout=args.timeout,
        follow_redirects=not args.no_redirects,
        user_agent=ua,
    )

    if result["error"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["content"])
        print(f"Saved to {args.output}")
    else:
        print(result["content"])

    # Print metadata to stderr
    print(f"\nURL: {result['url']}", file=sys.stderr)
    print(f"Status: {result['status_code']}", file=sys.stderr)
    if result["redirect_details"]:
        for rd in result["redirect_details"]:
            print(f"  {rd['status_code']} -> {rd['url']}", file=sys.stderr)
        print(f"  {result['status_code']} -> {result['url']} (final)", file=sys.stderr)
    elif result["redirect_chain"]:
        print(f"Redirects: {' -> '.join(result['redirect_chain'])}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

## File: `scripts/ga4_report.py`
```python
#!/usr/bin/env python3
"""
GA4 Data API v1beta - organic traffic reporting.

Queries the Google Analytics Data API for organic search traffic,
top landing pages, and session metrics with channel filtering.

Usage:
    python ga4_report.py --property 123456789
    python ga4_report.py --property 123456789 --days 90 --report top-pages
    python ga4_report.py --property 123456789 --report organic --json
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Optional

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Filter,
        FilterExpression,
        Metric,
        OrderBy,
        RunReportRequest,
    )
except ImportError:
    print(
        "Error: google-analytics-data required. "
        "Install with: pip install google-analytics-data",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from google_auth import get_oauth_credentials, load_config
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_oauth_credentials, load_config

GA4_SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def _build_ga4_client():
    """Build the GA4 BetaAnalyticsDataClient."""
    credentials = get_oauth_credentials(GA4_SCOPES)
    if not credentials:
        return None
    try:
        return BetaAnalyticsDataClient(credentials=credentials)
    except Exception as e:
        print(f"Error building GA4 client: {e}", file=sys.stderr)
        return None


def _resolve_property(property_id: str) -> str:
    """Ensure property ID is in the correct format."""
    if not property_id:
        return ""
    if property_id.startswith("properties/"):
        return property_id
    return f"properties/{property_id}"


def organic_traffic_report(
    property_id: str,
    days: int = 28,
    limit: int = 100,
) -> dict:
    """
    Generate organic traffic report from GA4.

    Filters by sessionDefaultChannelGroup == "Organic Search" and returns
    daily sessions, top landing pages, and key metrics.

    Args:
        property_id: GA4 property ID (numeric or 'properties/123456789').
        days: Number of days to query (default: 28).
        limit: Max rows (default: 100).

    Returns:
        Dictionary with daily_data, top_pages, totals, and quota usage.
    """
    result = {
        "property": property_id,
        "report": "organic_traffic",
        "date_range": None,
        "totals": {},
        "daily_data": [],
        "top_pages": [],
        "quota_tokens_used": None,
        "error": None,
    }

    client = _build_ga4_client()
    if not client:
        result["error"] = (
            "Could not build GA4 client. Ensure the service account has "
            "Viewer access in GA4 Admin > Property Access Management."
        )
        return result

    prop = _resolve_property(property_id)
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    result["date_range"] = {"start": start_date, "end": end_date}

    # Daily organic sessions
    try:
        daily_request = RunReportRequest(
            property=prop,
            dimensions=[Dimension(name="date")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="totalUsers"),
                Metric(name="screenPageViews"),
                Metric(name="bounceRate"),
                Metric(name="averageSessionDuration"),
                Metric(name="engagementRate"),
            ],
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimension_filter=FilterExpression(
                filter=Filter(
                    field_name="sessionDefaultChannelGroup",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.EXACT,
                        value="Organic Search",
                    ),
                )
            ),
            order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"))],
            limit=days + 5,
            return_property_quota=True,
        )

        daily_response = client.run_report(daily_request)

        for row in daily_response.rows:
            result["daily_data"].append({
                "date": row.dimension_values[0].value,
                "sessions": int(row.metric_values[0].value),
                "users": int(row.metric_values[1].value),
                "pageviews": int(row.metric_values[2].value),
                "bounce_rate": round(float(row.metric_values[3].value) * 100, 1),
                "avg_session_duration": round(float(row.metric_values[4].value), 1),
                "engagement_rate": round(float(row.metric_values[5].value) * 100, 1),
            })

        # Quota info
        if daily_response.property_quota:
            pq = daily_response.property_quota
            result["quota_tokens_used"] = {
                "daily_consumed": pq.tokens_per_day.consumed if pq.tokens_per_day else None,
                "daily_remaining": pq.tokens_per_day.remaining if pq.tokens_per_day else None,
                "hourly_consumed": pq.tokens_per_hour.consumed if pq.tokens_per_hour else None,
                "hourly_remaining": pq.tokens_per_hour.remaining if pq.tokens_per_hour else None,
            }

    except Exception as e:
        error_str = str(e)
        if "403" in error_str or "PERMISSION_DENIED" in error_str:
            result["error"] = (
                f"Permission denied for property '{property_id}'. "
                "Add the service account email as Viewer in "
                "GA4 Admin > Property Access Management."
            )
        elif "404" in error_str or "NOT_FOUND" in error_str:
            result["error"] = (
                f"Property '{property_id}' not found. "
                "Verify the numeric property ID in GA4 Admin > Property Details."
            )
        else:
            result["error"] = f"GA4 API error: {e}"
        return result

    # Top landing pages by organic sessions
    try:
        pages_request = RunReportRequest(
            property=prop,
            dimensions=[Dimension(name="landingPage")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="totalUsers"),
                Metric(name="screenPageViews"),
                Metric(name="bounceRate"),
                Metric(name="engagementRate"),
            ],
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimension_filter=FilterExpression(
                filter=Filter(
                    field_name="sessionDefaultChannelGroup",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.EXACT,
                        value="Organic Search",
                    ),
                )
            ),
            order_bys=[
                OrderBy(
                    metric=OrderBy.MetricOrderBy(metric_name="sessions"),
                    desc=True,
                )
            ],
            limit=limit,
        )

        pages_response = client.run_report(pages_request)

        for row in pages_response.rows:
            result["top_pages"].append({
                "landing_page": row.dimension_values[0].value,
                "sessions": int(row.metric_values[0].value),
                "users": int(row.metric_values[1].value),
                "pageviews": int(row.metric_values[2].value),
                "bounce_rate": round(float(row.metric_values[3].value) * 100, 1),
                "engagement_rate": round(float(row.metric_values[4].value) * 100, 1),
            })

    except Exception as e:
        # Non-fatal: daily data succeeded, pages failed
        result["pages_error"] = f"Error fetching top pages: {e}"

    # Calculate totals
    if result["daily_data"]:
        total_sessions = sum(d["sessions"] for d in result["daily_data"])
        total_users = sum(d["users"] for d in result["daily_data"])
        total_pageviews = sum(d["pageviews"] for d in result["daily_data"])
        result["totals"] = {
            "sessions": total_sessions,
            "users": total_users,
            "pageviews": total_pageviews,
            "avg_daily_sessions": round(total_sessions / len(result["daily_data"]), 1),
        }

    return result


def top_pages_report(
    property_id: str,
    days: int = 28,
    limit: int = 50,
) -> dict:
    """
    Get top organic landing pages from GA4.

    Args:
        property_id: GA4 property ID.
        days: Number of days.
        limit: Max pages to return.

    Returns:
        Dictionary with top pages ranked by organic sessions.
    """
    report = organic_traffic_report(property_id, days, limit)
    # Slim it down to just pages
    return {
        "property": property_id,
        "report": "top_organic_pages",
        "date_range": report.get("date_range"),
        "pages": report.get("top_pages", []),
        "total_organic_sessions": report.get("totals", {}).get("sessions", 0),
        "quota_tokens_used": report.get("quota_tokens_used"),
        "error": report.get("error"),
    }


def device_breakdown(
    property_id: str,
    days: int = 28,
) -> dict:
    """
    Organic sessions broken down by device category.

    Args:
        property_id: GA4 property ID.
        days: Number of days.

    Returns:
        Dictionary with device breakdown data.
    """
    result = {"property": property_id, "report": "device_breakdown", "devices": [], "error": None}

    client = _build_ga4_client()
    if not client:
        result["error"] = "Could not build GA4 client."
        return result

    prop = _resolve_property(property_id)
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    result["date_range"] = {"start": start_date, "end": end_date}

    try:
        request = RunReportRequest(
            property=prop,
            dimensions=[Dimension(name="deviceCategory")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="totalUsers"),
                Metric(name="bounceRate"),
                Metric(name="engagementRate"),
            ],
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimension_filter=FilterExpression(
                filter=Filter(
                    field_name="sessionDefaultChannelGroup",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.EXACT,
                        value="Organic Search",
                    ),
                )
            ),
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
        )
        response = client.run_report(request)
        for row in response.rows:
            result["devices"].append({
                "category": row.dimension_values[0].value,
                "sessions": int(row.metric_values[0].value),
                "users": int(row.metric_values[1].value),
                "bounce_rate": round(float(row.metric_values[2].value) * 100, 1),
                "engagement_rate": round(float(row.metric_values[3].value) * 100, 1),
            })
    except Exception as e:
        result["error"] = f"GA4 device breakdown error: {e}"

    return result


def country_breakdown(
    property_id: str,
    days: int = 28,
    limit: int = 20,
) -> dict:
    """
    Organic sessions broken down by country.

    Args:
        property_id: GA4 property ID.
        days: Number of days.
        limit: Max countries to return.

    Returns:
        Dictionary with country breakdown data.
    """
    result = {"property": property_id, "report": "country_breakdown", "countries": [], "error": None}

    client = _build_ga4_client()
    if not client:
        result["error"] = "Could not build GA4 client."
        return result

    prop = _resolve_property(property_id)
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    result["date_range"] = {"start": start_date, "end": end_date}

    try:
        request = RunReportRequest(
            property=prop,
            dimensions=[Dimension(name="country")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="totalUsers"),
            ],
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimension_filter=FilterExpression(
                filter=Filter(
                    field_name="sessionDefaultChannelGroup",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.EXACT,
                        value="Organic Search",
                    ),
                )
            ),
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
            limit=limit,
        )
        response = client.run_report(request)
        for row in response.rows:
            result["countries"].append({
                "country": row.dimension_values[0].value,
                "sessions": int(row.metric_values[0].value),
                "users": int(row.metric_values[1].value),
            })
    except Exception as e:
        result["error"] = f"GA4 country breakdown error: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="GA4 Data API - organic traffic reporting"
    )
    parser.add_argument(
        "--property", "-p",
        help="GA4 property ID (numeric, e.g., 123456789). Uses config default if not specified.",
    )
    parser.add_argument("--days", "-d", type=int, default=28, help="Number of days (default: 28)")
    parser.add_argument(
        "--report", "-r",
        choices=["organic", "top-pages", "device", "country"],
        default="organic",
        help="Report type (default: organic)",
    )
    parser.add_argument("--limit", type=int, default=50, help="Max rows (default: 50)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Resolve property
    prop = args.property
    if not prop:
        config = load_config()
        prop = config.get("ga4_property_id") or ""
        # Strip 'properties/' prefix if present for consistency
        if prop and prop.startswith("properties/"):
            prop = prop[len("properties/"):]
    if not prop:
        print(
            "Error: No GA4 property specified. Use --property or set ga4_property_id in config.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.report == "top-pages":
        result = top_pages_report(prop, args.days, args.limit)
    elif args.report == "device":
        result = device_breakdown(prop, args.days)
    elif args.report == "country":
        result = country_breakdown(prop, args.days, args.limit)
    else:
        result = organic_traffic_report(prop, args.days, args.limit)

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)
        if not args.json:
            sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if args.report == "top-pages":
            print(f"=== Top Organic Landing Pages ===")
            print(f"Property: {prop} | Period: {result.get('date_range', {}).get('start')} to {result.get('date_range', {}).get('end')}")
            print(f"Total organic sessions: {result.get('total_organic_sessions', 0):,}")
            print()
            for i, page in enumerate(result.get("pages", [])[:20], 1):
                print(f"  {i:2d}. {page['landing_page']}")
                print(f"      Sessions: {page['sessions']:,} | Users: {page['users']:,} | Bounce: {page['bounce_rate']}%")
        else:
            totals = result.get("totals", {})
            print(f"=== GA4 Organic Traffic Report ===")
            print(f"Property: {prop}")
            dr = result.get("date_range", {})
            print(f"Period: {dr.get('start')} to {dr.get('end')}")
            print(f"\nSessions: {totals.get('sessions', 0):,} | Users: {totals.get('users', 0):,} | Pageviews: {totals.get('pageviews', 0):,}")
            print(f"Avg Daily Sessions: {totals.get('avg_daily_sessions', 0):,.0f}")

            quota = result.get("quota_tokens_used")
            if quota and quota.get("daily_remaining") is not None:
                print(f"\nQuota: {quota['daily_consumed']} tokens used / {quota['daily_remaining']} remaining (daily)")

            pages = result.get("top_pages", [])
            if pages:
                print(f"\nTop {min(10, len(pages))} Organic Landing Pages:")
                for i, page in enumerate(pages[:10], 1):
                    print(f"  {i:2d}. {page['landing_page']} ({page['sessions']:,} sessions)")


if __name__ == "__main__":
    main()
```

## File: `scripts/google_auth.py`
```python
#!/usr/bin/env python3
"""
Google API credential management for Claude SEO.

Loads and validates credentials for Google Search Console, PageSpeed Insights,
CrUX, Indexing API, and GA4. Supports service accounts, OAuth web credentials
with token refresh, API keys, and environment variable fallbacks.

Usage:
    python google_auth.py --check                  # Check all credentials
    python google_auth.py --check gsc              # Check specific service
    python google_auth.py --check --json            # JSON output
    python google_auth.py --setup                   # Show setup instructions
    python google_auth.py --tier                    # Show detected credential tier
    python google_auth.py --auth --creds /path/to/client_secret.json  # OAuth browser flow
"""

import argparse
import json
import os
import sys
import time
from typing import Optional

CONFIG_PATH = os.path.expanduser("~/.config/claude-seo/google-api.json")
TOKEN_PATH = os.path.expanduser("~/.config/claude-seo/oauth-token.json")

# Service-to-scope mapping
SCOPES = {
    "gsc_readonly": "https://www.googleapis.com/auth/webmasters.readonly",
    "gsc_write": "https://www.googleapis.com/auth/webmasters",
    "indexing": "https://www.googleapis.com/auth/indexing",
    "ga4": "https://www.googleapis.com/auth/analytics.readonly",
}

# Which services need which auth type
SERVICE_AUTH = {
    "psi": "api_key",
    "crux": "api_key",
    "crux_history": "api_key",
    "gsc": "oauth_or_sa",
    "indexing": "oauth_or_sa",
    "ga4": "oauth_or_sa",
}

OAUTH_SCOPES = (
    "https://www.googleapis.com/auth/indexing "
    "https://www.googleapis.com/auth/webmasters "
    "https://www.googleapis.com/auth/analytics.readonly"
)
OAUTH_REDIRECT_URI = "http://localhost:8085"

# Human-readable service names
SERVICE_NAMES = {
    "psi": "PageSpeed Insights v5",
    "crux": "Chrome UX Report (CrUX) API",
    "crux_history": "CrUX History API",
    "gsc": "Google Search Console API",
    "indexing": "Google Indexing API v3",
    "ga4": "GA4 Data API v1beta",
}


def load_config() -> dict:
    """
    Load configuration from config file with environment variable fallbacks.

    Reads ~/.config/claude-seo/google-api.json first. Any missing fields
    are filled from environment variables.

    Returns:
        Dictionary with keys: service_account_path, api_key,
        default_property, ga4_property_id. Missing values are None.
    """
    config = {
        "service_account_path": None,
        "api_key": None,
        "default_property": None,
        "ga4_property_id": None,
    }

    # Load from config file
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                file_config = json.load(f)
            config.update({k: v for k, v in file_config.items() if v})
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config file: {e}", file=sys.stderr)

    # Environment variable fallbacks
    if not config["service_account_path"]:
        config["service_account_path"] = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

    if not config["api_key"]:
        config["api_key"] = os.environ.get("GOOGLE_API_KEY")

    if not config["ga4_property_id"]:
        config["ga4_property_id"] = os.environ.get("GA4_PROPERTY_ID")

    if not config["default_property"]:
        config["default_property"] = os.environ.get("GSC_PROPERTY")

    return config


def get_service_account_credentials(scopes: list):
    """
    Load Google service account credentials.

    Args:
        scopes: List of OAuth scope URLs.

    Returns:
        google.oauth2.service_account.Credentials object, or None on failure.
    """
    try:
        from google.oauth2 import service_account
    except ImportError:
        print(
            "Error: google-auth library required. "
            "Install with: pip install google-auth",
            file=sys.stderr,
        )
        return None

    config = load_config()
    sa_path = config.get("service_account_path")

    if not sa_path:
        return None

    sa_path = os.path.expanduser(sa_path)
    if not os.path.exists(sa_path):
        print(
            f"Error: Service account file not found: {sa_path}",
            file=sys.stderr,
        )
        return None

    try:
        credentials = service_account.Credentials.from_service_account_file(
            sa_path, scopes=scopes
        )
        return credentials
    except Exception as e:
        print(f"Error loading service account: {e}", file=sys.stderr)
        return None


def _load_oauth_client(creds_path: str) -> Optional[dict]:
    """Load OAuth client credentials from a client_secret JSON file."""
    try:
        with open(creds_path, "r") as f:
            data = json.load(f)
        return data.get("web", data.get("installed", {}))
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading OAuth client file: {e}", file=sys.stderr)
        return None


def _load_oauth_token() -> Optional[dict]:
    """Load saved OAuth token from TOKEN_PATH."""
    if not os.path.exists(TOKEN_PATH):
        return None
    try:
        with open(TOKEN_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def _save_oauth_token(token_data: dict):
    """Save OAuth token to TOKEN_PATH."""
    os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
    with open(TOKEN_PATH, "w") as f:
        json.dump(token_data, f, indent=2)


def _refresh_oauth_token(client: dict, token_data: dict) -> Optional[dict]:
    """Refresh an expired OAuth token using the refresh_token."""
    import urllib.parse
    import urllib.request

    if not token_data.get("refresh_token"):
        return None

    params = urllib.parse.urlencode({
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "refresh_token": token_data["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()

    try:
        req = urllib.request.Request(client.get("token_uri", "https://oauth2.googleapis.com/token"), data=params)
        with urllib.request.urlopen(req) as resp:
            new_data = json.loads(resp.read())
        token_data["access_token"] = new_data["access_token"]
        token_data["expires_at"] = time.time() + new_data.get("expires_in", 3600)
        _save_oauth_token(token_data)
        return token_data
    except Exception as e:
        print(f"Error refreshing OAuth token: {e}", file=sys.stderr)
        return None


def get_oauth_credentials(scopes: list):
    """
    Get OAuth credentials from saved token, refreshing if needed.

    Falls back to service account if no OAuth token is available.

    Args:
        scopes: List of OAuth scope URLs (used for service account fallback).

    Returns:
        google.oauth2.credentials.Credentials or service_account.Credentials, or None.
    """
    config = load_config()

    # Try OAuth token first
    token_data = _load_oauth_token()
    if token_data and token_data.get("access_token"):
        # Check if token needs refresh
        if time.time() > token_data.get("expires_at", 0) - 60:
            oauth_creds_path = config.get("oauth_client_path")
            if oauth_creds_path:
                client = _load_oauth_client(os.path.expanduser(oauth_creds_path))
                if client:
                    token_data = _refresh_oauth_token(client, token_data)
                    if not token_data:
                        print("OAuth token refresh failed. Re-run --auth.", file=sys.stderr)
                        return get_service_account_credentials(scopes)

        if token_data and token_data.get("access_token"):
            try:
                from google.oauth2.credentials import Credentials
                # Read client_secret from client file, never from stored token
                client_secret = None
                oauth_path = config.get("oauth_client_path")
                if oauth_path:
                    client_data = _load_oauth_client(os.path.expanduser(oauth_path))
                    if client_data:
                        client_secret = client_data.get("client_secret")
                return Credentials(
                    token=token_data["access_token"],
                    refresh_token=token_data.get("refresh_token"),
                    token_uri="https://oauth2.googleapis.com/token",
                    client_id=token_data.get("client_id"),
                    client_secret=client_secret,
                )
            except ImportError:
                print("Error: google-auth required. Install with: pip install google-auth", file=sys.stderr)

    # Fall back to service account
    return get_service_account_credentials(scopes)


def run_oauth_flow(creds_path: str):
    """
    Run OAuth browser-based authentication flow.

    Opens a browser for consent, captures the auth code via local HTTP server,
    exchanges for tokens, and saves them.

    Args:
        creds_path: Path to the OAuth client_secret JSON file.
    """
    import http.server
    import urllib.parse
    import urllib.request
    import webbrowser

    client = _load_oauth_client(creds_path)
    if not client:
        print("Error: Could not load OAuth client credentials.", file=sys.stderr)
        sys.exit(1)

    auth_url = (
        f"{client.get('auth_uri', 'https://accounts.google.com/o/oauth2/auth')}"
        f"?client_id={client['client_id']}"
        f"&redirect_uri={urllib.parse.quote(OAUTH_REDIRECT_URI)}"
        f"&response_type=code"
        f"&scope={urllib.parse.quote(OAUTH_SCOPES)}"
        f"&access_type=offline&prompt=consent"
    )

    auth_code = [None]

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if "code" in params:
                auth_code[0] = params["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Authentication successful!</h1><p>Close this tab.</p>")
            else:
                self.send_response(400)
                self.end_headers()
        def log_message(self, *a):
            pass

    server = http.server.HTTPServer(("localhost", 8085), Handler)
    server.timeout = 300

    print(f"\nOpen this URL in your browser:\n\n{auth_url}\n")
    print("Waiting up to 5 minutes for authentication...")

    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    server.handle_request()
    server.server_close()

    if not auth_code[0]:
        print("\nAuthentication failed or timed out.", file=sys.stderr)
        print("If the browser showed 'localhost refused to connect', copy the full URL")
        print("from the browser address bar and run:")
        print(f"  python scripts/google_auth.py --exchange --creds {creds_path} --code 'THE_CODE'")
        sys.exit(1)

    # Exchange code for tokens
    _exchange_code(client, auth_code[0])


def _exchange_code(client: dict, code: str):
    """Exchange an authorization code for tokens."""
    import urllib.parse
    import urllib.request

    params = urllib.parse.urlencode({
        "code": code,
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "redirect_uri": OAUTH_REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()

    try:
        req = urllib.request.Request(
            client.get("token_uri", "https://oauth2.googleapis.com/token"), data=params
        )
        with urllib.request.urlopen(req) as resp:
            token_data = json.loads(resp.read())
        token_data["expires_at"] = time.time() + token_data.get("expires_in", 3600)
        token_data["client_id"] = client["client_id"]
        # SECURITY: Never store client_secret in token file. It stays in client_secret.json only.
        token_data.pop("client_secret", None)
        _save_oauth_token(token_data)
        print("OAuth token saved successfully!")

        # Also save the OAuth client path to config
        config = load_config()
        # Don't overwrite existing config, just suggest
        print(f"\nToken saved to: {TOKEN_PATH}")
    except Exception as e:
        print(f"Error exchanging authorization code: {e}", file=sys.stderr)
        sys.exit(1)


def validate_url(url: str) -> bool:
    """
    Validate a URL for use with Google APIs. Rejects private/loopback addresses.

    Args:
        url: URL string to validate.

    Returns:
        True if the URL is a valid public http/https URL, False otherwise.
    """
    from urllib.parse import urlparse

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    if not parsed.hostname:
        return False
    blocked = [
        "localhost", "127.0.0.1", "0.0.0.0", "::1",
        "metadata.google.internal",
    ]
    if parsed.hostname in blocked:
        return False
    # Block private IP ranges (10.x, 172.16-31.x, 192.168.x)
    try:
        import ipaddress
        ip = ipaddress.ip_address(parsed.hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            return False
    except ValueError:
        pass  # Not an IP address (hostname), which is fine
    return True


def get_api_key() -> Optional[str]:
    """
    Get the Google API key from config or environment.

    Returns:
        API key string, or None if not configured.
    """
    config = load_config()
    return config.get("api_key")


def build_service(api_name: str, version: str, scopes: list):
    """
    Build a Google API discovery service client.

    Args:
        api_name: API name (e.g., 'searchconsole', 'indexing', 'pagespeedonline').
        version: API version (e.g., 'v1', 'v3', 'v5').
        scopes: OAuth scopes needed.

    Returns:
        googleapiclient.discovery.Resource object, or None on failure.
    """
    try:
        from googleapiclient.discovery import build
    except ImportError:
        print(
            "Error: google-api-python-client required. "
            "Install with: pip install google-api-python-client",
            file=sys.stderr,
        )
        return None

    credentials = get_oauth_credentials(scopes)
    if not credentials:
        return None

    try:
        service = build(api_name, version, credentials=credentials)
        return service
    except Exception as e:
        print(f"Error building {api_name} service: {e}", file=sys.stderr)
        return None


def check_credentials(service: str) -> dict:
    """
    Validate credentials for a specific Google API service.

    Args:
        service: One of 'psi', 'crux', 'crux_history', 'gsc', 'indexing', 'ga4'.

    Returns:
        Dictionary with:
            - available: bool
            - method: 'api_key' or 'service_account'
            - service: service name
            - error: error message or None
    """
    result = {
        "available": False,
        "method": SERVICE_AUTH.get(service, "unknown"),
        "service": SERVICE_NAMES.get(service, service),
        "error": None,
    }

    config = load_config()

    if SERVICE_AUTH.get(service) == "api_key":
        api_key = config.get("api_key")
        if api_key:
            result["available"] = True
        else:
            result["error"] = (
                "No API key found. Set GOOGLE_API_KEY environment variable "
                f"or add 'api_key' to {CONFIG_PATH}"
            )

    elif SERVICE_AUTH.get(service) == "oauth_or_sa":
        # Check OAuth token first
        token_data = _load_oauth_token()
        if token_data and token_data.get("access_token"):
            result["available"] = True
            result["method"] = "oauth_token"
            expired = time.time() > token_data.get("expires_at", 0) - 60
            if expired and token_data.get("refresh_token"):
                result["note"] = "Token expired but refresh_token available (will auto-refresh)"
            elif expired:
                result["available"] = False
                result["error"] = "OAuth token expired and no refresh_token. Re-run --auth."
        else:
            # Fall back to service account
            sa_path = config.get("service_account_path")
            if not sa_path:
                result["error"] = (
                    "No OAuth token or service account found. Either:\n"
                    "         1. Run: python scripts/google_auth.py --auth --creds /path/to/client_secret.json\n"
                    f"         2. Or add 'service_account_path' to {CONFIG_PATH}"
                )
            else:
                sa_path = os.path.expanduser(sa_path)
                if not os.path.exists(sa_path):
                    result["error"] = f"Service account file not found: {sa_path}"
                else:
                    try:
                        with open(sa_path, "r") as f:
                            sa_data = json.load(f)
                        if "client_email" not in sa_data or "private_key" not in sa_data:
                            result["error"] = "Service account JSON missing required fields (client_email, private_key)"
                        else:
                            result["available"] = True
                            result["method"] = "service_account"
                            result["client_email"] = sa_data.get("client_email")
                    except (json.JSONDecodeError, IOError) as e:
                        result["error"] = f"Invalid service account file: {e}"

        # GA4 also needs property ID
        if service == "ga4" and result["available"]:
            ga4_id = config.get("ga4_property_id")
            if not ga4_id:
                result["available"] = False
                result["error"] = (
                    "Credentials found but no GA4 property ID configured. "
                    f"Set GA4_PROPERTY_ID or add 'ga4_property_id' to {CONFIG_PATH}"
                )
    else:
        result["error"] = f"Unknown service: {service}"

    return result


def detect_tier() -> dict:
    """
    Detect the credential tier available.

    Returns:
        Dictionary with:
            - tier: 0, 1, or 2
            - description: human-readable tier description
            - capabilities: list of available API groups
            - missing: what's needed for the next tier
    """
    config = load_config()

    has_api_key = bool(config.get("api_key"))
    has_authenticated = False
    has_ga4 = False
    auth_method = None

    # Check OAuth token
    token_data = _load_oauth_token()
    if token_data and token_data.get("access_token"):
        has_authenticated = True
        auth_method = "oauth_token"

    # Check service account
    if not has_authenticated:
        sa_path = config.get("service_account_path")
        if sa_path:
            sa_path = os.path.expanduser(sa_path)
            if os.path.exists(sa_path):
                try:
                    with open(sa_path, "r") as f:
                        sa_data = json.load(f)
                    if "client_email" in sa_data and "private_key" in sa_data:
                        has_authenticated = True
                        auth_method = "service_account"
                except (json.JSONDecodeError, IOError):
                    pass

    if has_authenticated and config.get("ga4_property_id"):
        has_ga4 = True

    if has_ga4:
        return {
            "tier": 2,
            "description": "Full (API key + Service Account + GA4)",
            "capabilities": [
                "PageSpeed Insights", "CrUX", "CrUX History",
                "Search Console", "URL Inspection", "Sitemaps",
                "Indexing API", "GA4 Organic Traffic",
            ],
            "missing": None,
        }
    elif has_authenticated:
        return {
            "tier": 1,
            "description": "Authenticated (API key + OAuth/Service Account)",
            "capabilities": [
                "PageSpeed Insights", "CrUX", "CrUX History",
                "Search Console", "URL Inspection", "Sitemaps",
                "Indexing API",
            ],
            "missing": "Add 'ga4_property_id' to unlock GA4 organic traffic reports",
        }
    elif has_api_key:
        return {
            "tier": 0,
            "description": "API Key Only",
            "capabilities": [
                "PageSpeed Insights", "CrUX", "CrUX History",
            ],
            "missing": "Add a service account to unlock Search Console, URL Inspection, and Indexing API",
        }
    else:
        return {
            "tier": -1,
            "description": "No credentials configured",
            "capabilities": [],
            "missing": (
                f"Create config at {CONFIG_PATH} with at minimum an 'api_key' field. "
                "Run with --setup for full instructions."
            ),
        }


def print_setup_instructions():
    """Print step-by-step setup instructions."""
    print("""
Google SEO API Setup Instructions
=================================

1. CREATE A GOOGLE CLOUD PROJECT
   - Go to https://console.cloud.google.com
   - Create a new project (or select existing)
   - Note the project ID

2. ENABLE APIs
   In API Library (APIs & Services > Library), enable:
   - Google Search Console API
   - PageSpeed Insights API
   - Chrome UX Report API
   - Web Search Indexing API (for Indexing API)
   - Google Analytics Data API (for GA4)

3. CREATE AN API KEY (for PSI, CrUX -- free, no service account needed)
   - APIs & Services > Credentials > Create Credentials > API key
   - Restrict to: PageSpeed Insights API, Chrome UX Report API

4. CREATE A SERVICE ACCOUNT (for GSC, Indexing API, GA4)
   - IAM & Admin > Service Accounts > Create Service Account
   - Download JSON key file, store securely

5. GRANT ACCESS
   - Search Console: Settings > Users and permissions > Add user
     Paste the service account client_email, set as Owner (for Indexing API) or Full (read-only)
   - GA4: Admin > Property Access Management > Add
     Paste email, set Viewer role

6. CREATE CONFIG FILE
   mkdir -p ~/.config/claude-seo
   Save to ~/.config/claude-seo/google-api.json:

   {
     "service_account_path": "/path/to/service_account.json",
     "api_key": "AIzaSy...",
     "default_property": "sc-domain:example.com",
     "ga4_property_id": "properties/123456789"
   }

7. VERIFY
   python scripts/google_auth.py --check

ENVIRONMENT VARIABLE ALTERNATIVES:
   GOOGLE_API_KEY              - API key
   GOOGLE_APPLICATION_CREDENTIALS - Path to service account JSON
   GA4_PROPERTY_ID             - GA4 property ID (e.g., properties/123456789)
   GSC_PROPERTY                - Default Search Console property
""")


def main():
    parser = argparse.ArgumentParser(
        description="Google API credential management for Claude SEO"
    )
    parser.add_argument(
        "--check",
        nargs="?",
        const="all",
        metavar="SERVICE",
        help="Check credentials. Optionally specify service: psi, crux, gsc, indexing, ga4",
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Show setup instructions",
    )
    parser.add_argument(
        "--tier",
        action="store_true",
        help="Show detected credential tier",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )
    parser.add_argument(
        "--auth",
        action="store_true",
        help="Run OAuth browser-based authentication flow",
    )
    parser.add_argument(
        "--exchange",
        action="store_true",
        help="Manually exchange an auth code for tokens",
    )
    parser.add_argument(
        "--creds",
        help="Path to OAuth client_secret JSON file (for --auth and --exchange)",
    )
    parser.add_argument(
        "--code",
        help="Authorization code to exchange (for --exchange)",
    )

    args = parser.parse_args()

    if args.auth:
        if not args.creds:
            print("Error: --creds is required with --auth", file=sys.stderr)
            sys.exit(1)
        run_oauth_flow(args.creds)
        return

    if args.exchange:
        if not args.creds or not args.code:
            print("Error: --creds and --code are required with --exchange", file=sys.stderr)
            sys.exit(1)
        client = _load_oauth_client(args.creds)
        if client:
            _exchange_code(client, args.code)
        return

    if args.setup:
        print_setup_instructions()
        return

    if args.tier:
        tier_info = detect_tier()
        if args.json:
            print(json.dumps(tier_info, indent=2))
        else:
            print(f"Credential Tier: {tier_info['tier']} -- {tier_info['description']}")
            if tier_info["capabilities"]:
                print(f"Available APIs: {', '.join(tier_info['capabilities'])}")
            if tier_info["missing"]:
                print(f"Next tier: {tier_info['missing']}")
        return

    if args.check:
        services = (
            list(SERVICE_AUTH.keys())
            if args.check == "all"
            else [args.check]
        )

        results = {}
        for svc in services:
            if svc not in SERVICE_AUTH:
                results[svc] = {"available": False, "error": f"Unknown service: {svc}"}
                continue
            results[svc] = check_credentials(svc)

        if args.json:
            tier_info = detect_tier()
            output = {"tier": tier_info, "services": results}
            print(json.dumps(output, indent=2))
        else:
            tier_info = detect_tier()
            print(f"Credential Tier: {tier_info['tier']} -- {tier_info['description']}")
            print()
            for svc, result in results.items():
                status = "OK" if result["available"] else "MISSING"
                print(f"  [{status}] {result.get('service', svc)}")
                if result.get("error"):
                    print(f"         {result['error']}")
                if result.get("client_email"):
                    print(f"         Service account: {result['client_email']}")
            print()
            if tier_info["missing"]:
                print(f"Tip: {tier_info['missing']}")
        return

    # Default: show tier
    tier_info = detect_tier()
    if args.json:
        print(json.dumps(tier_info, indent=2))
    else:
        print(f"Credential Tier: {tier_info['tier']} -- {tier_info['description']}")
        if tier_info["missing"]:
            print(f"Run --setup for configuration instructions.")


if __name__ == "__main__":
    main()
```

## File: `scripts/google_report.py`
```python
#!/usr/bin/env python3
"""
Google SEO Report Generator - Professional PDF/HTML reports from API data.

Consumes JSON output from seo-google scripts and generates formatted reports
with charts, analytics, and actionable recommendations.

Usage:
    python google_report.py --type cwv-audit --data cwv-data.json --domain example.com
    python google_report.py --type gsc-performance --data gsc-data.json --domain example.com
    python google_report.py --type indexation --data inspect-data.json --domain example.com
    python google_report.py --type full --data full-data.json --domain example.com
    cat data.json | python google_report.py --type cwv-audit --domain example.com
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
except ImportError:
    print("Error: matplotlib required. Install with: pip install matplotlib", file=sys.stderr)
    sys.exit(1)

try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint required. Install with: pip install weasyprint", file=sys.stderr)
    sys.exit(1)


# ─── Brand Colors ────────────────────────────────────────────────────────────

BRAND = {
    "primary": "#1e3a5f",     # Navy (headers, borders)
    "secondary": "#4a5568",    # Warm gray
    "accent": "#b8860b",       # Dark gold
    "success": "#2d6a4f",      # Forest green (pass/good)
    "warning": "#d4740e",      # Warm amber (warnings)
    "danger": "#c53030",       # Deep red (fail/critical)
    "dark": "#1a1a2e",         # Dark navy
    "light_bg": "#faf9f7",     # Warm cream
    "grid": "#d6d3cc",         # Warm border
    "muted": "#6b7280",        # Muted text
}


def _score_color(score):
    """Return brand color based on Lighthouse-style score thresholds."""
    if score >= 90:
        return BRAND["success"]
    elif score >= 50:
        return BRAND["warning"]
    return BRAND["danger"]


def _rating_color(rating):
    """Return brand color based on CrUX rating strings."""
    r = str(rating).lower().replace("-", "_").replace(" ", "_")
    if r in ("good", "pass", "fast"):
        return BRAND["success"]
    elif r in ("needs_improvement", "needs-improvement", "average", "warn"):
        return BRAND["warning"]
    return BRAND["danger"]


def _score_class(score):
    """Return CSS class for TOC score badges."""
    if score >= 80:
        return "score-good"
    elif score >= 50:
        return "score-warn"
    return "score-bad"


def _rating_css_class(rating):
    """Return CSS status class from a rating string."""
    r = str(rating).lower()
    if "good" in r or "pass" in r:
        return "status-pass"
    elif "poor" in r or "fail" in r:
        return "status-fail"
    return "status-warn"


# ─── Chart Setup ─────────────────────────────────────────────────────────────

def _setup_matplotlib():
    """Configure matplotlib for professional chart output."""
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["DejaVu Serif", "Times New Roman", "Georgia"],
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "axes.grid": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


_setup_matplotlib()


# ─── Chart Functions ─────────────────────────────────────────────────────────

def chart_lighthouse_gauges(data: dict, output_dir: Path) -> str:
    """Generate 2x2 Lighthouse score gauges."""
    scores = data.get("lighthouse_scores", {})
    if not scores:
        return ""

    fig, axes = plt.subplots(2, 2, figsize=(8, 4), subplot_kw={"projection": "polar"})
    categories = [
        ("performance", "Performance"),
        ("accessibility", "Accessibility"),
        ("best-practices", "Best Practices"),
        ("seo", "SEO"),
    ]

    for ax, (key, label) in zip(axes.flat, categories):
        score = scores.get(key, 0)
        theta_bg = np.linspace(np.pi, 0, 100)
        theta_fill = np.linspace(np.pi, np.pi - (score / 100) * np.pi, 100)

        ax.plot(theta_bg, [1] * 100, linewidth=14, color="#e2e8f0", solid_capstyle="round")
        ax.plot(theta_fill, [1] * 100, linewidth=14, color=_score_color(score), solid_capstyle="round")

        ax.text(np.pi / 2, 0.35, f"{score}", ha="center", va="center",
                fontsize=24, fontweight="bold", color=BRAND["dark"])
        ax.text(np.pi / 2, -0.05, label, ha="center", va="center",
                fontsize=10, color=BRAND["muted"])

        ax.set_ylim(0, 1.3)
        ax.set_rticks([])
        ax.set_thetagrids([])
        ax.spines["polar"].set_visible(False)

    plt.tight_layout(pad=2)
    path = output_dir / "lighthouse_gauges.png"
    plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return str(path)


def chart_cwv_distributions(data: dict, output_dir: Path) -> str:
    """Generate stacked horizontal bars for CWV metric distributions."""
    crux = data.get("crux", {})
    metrics = crux.get("metrics", {})
    if not metrics:
        return ""

    cwv_order = [
        "largest_contentful_paint", "interaction_to_next_paint",
        "cumulative_layout_shift", "first_contentful_paint",
        "experimental_time_to_first_byte",
    ]

    labels, goods, nis, poors = [], [], [], []
    for name in cwv_order:
        m = metrics.get(name)
        if not m or "distribution" not in m:
            continue
        d = m["distribution"]
        labels.append(m.get("label", name))
        goods.append(d.get("good", 0))
        nis.append(d.get("needs_improvement", 0))
        poors.append(d.get("poor", 0))

    if not labels:
        return ""

    fig, ax = plt.subplots(figsize=(8, max(2.5, len(labels) * 0.7)))
    y = range(len(labels))

    ax.barh(y, goods, color=BRAND["success"], label="Good", height=0.5)
    ax.barh(y, nis, left=goods, color=BRAND["warning"], label="Needs Improvement", height=0.5)
    left2 = [g + n for g, n in zip(goods, nis)]
    ax.barh(y, poors, left=left2, color=BRAND["danger"], label="Poor", height=0.5)

    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(0, 100)
    ax.set_xlabel("% of page loads")
    ax.legend(loc="lower right", fontsize=9)
    ax.invert_yaxis()

    for i, (g, n, p) in enumerate(zip(goods, nis, poors)):
        if g > 10:
            ax.text(g / 2, i, f"{g:.0f}%", ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")
        if n > 10:
            ax.text(g + n / 2, i, f"{n:.0f}%", ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")
        if p > 10:
            ax.text(g + n + p / 2, i, f"{p:.0f}%", ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")

    plt.tight_layout()
    path = output_dir / "cwv_distributions.png"
    plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return str(path)


def chart_cwv_timeline(data: dict, output_dir: Path) -> str:
    """Generate CWV timeline chart from CrUX History data."""
    metrics = data.get("metrics", {})
    periods = data.get("collection_periods", [])
    if not metrics or not periods:
        return ""

    cwv_metrics = [
        "largest_contentful_paint",
        "interaction_to_next_paint",
        "cumulative_layout_shift",
    ]
    available = [m for m in cwv_metrics if m in metrics]
    if not available:
        return ""

    fig, axes = plt.subplots(len(available), 1, figsize=(10, 3 * len(available)), sharex=True)
    if len(available) == 1:
        axes = [axes]

    x_labels = [p.get("last", "")[-5:] for p in periods]  # MM-DD format
    x = range(len(x_labels))

    for ax, metric_name in zip(axes, available):
        m = metrics[metric_name]
        p75s = m.get("p75_values", [])
        label = m.get("label", metric_name)
        good_t = m.get("good_threshold", 0)
        poor_t = m.get("poor_threshold", 0)

        valid_x = [i for i, v in enumerate(p75s) if v is not None]
        valid_y = [v for v in p75s if v is not None]

        if not valid_y:
            continue

        # Threshold bands
        if good_t and poor_t:
            ax.axhspan(0, good_t, alpha=0.1, color=BRAND["success"])
            ax.axhspan(good_t, poor_t, alpha=0.1, color=BRAND["warning"])
            ax.axhline(y=good_t, color=BRAND["success"], linestyle="--", alpha=0.5, linewidth=1)
            ax.axhline(y=poor_t, color=BRAND["danger"], linestyle="--", alpha=0.5, linewidth=1)

        ax.plot(valid_x, valid_y, color=BRAND["primary"], linewidth=2, marker="o", markersize=3)
        ax.fill_between(valid_x, valid_y, alpha=0.1, color=BRAND["primary"])

        unit = m.get("unit", "")
        ax.set_ylabel(f"{label} (p75{unit})")
        ax.set_title(label, fontsize=12, fontweight="bold")

    if x_labels:
        step = max(1, len(x_labels) // 8)
        axes[-1].set_xticks(range(0, len(x_labels), step))
        axes[-1].set_xticklabels(
            [x_labels[i] for i in range(0, len(x_labels), step)],
            rotation=45, fontsize=8,
        )

    plt.tight_layout()
    path = output_dir / "cwv_timeline.png"
    plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return str(path)


def chart_top_queries(data: dict, output_dir: Path) -> str:
    """Generate horizontal bar chart of top queries by impressions."""
    rows = data.get("rows", [])
    if not rows:
        return ""

    # Sort by impressions (more meaningful than clicks for new sites)
    top = sorted(rows, key=lambda r: r.get("impressions", 0), reverse=True)[:12]
    top = [r for r in top if r.get("impressions", 0) > 0]
    if not top:
        return ""

    labels = [r.get("query", r.get("keys", ["?"])[0])[:35] for r in top]
    impressions = [r.get("impressions", 0) for r in top]
    clicks = [r.get("clicks", 0) for r in top]

    if not impressions or max(impressions) < 3:
        return ""

    fig, ax = plt.subplots(figsize=(7, max(2, len(labels) * 0.3)))
    y = range(len(labels))
    bars = ax.barh(y, impressions, color=BRAND["primary"], height=0.55, label="Impressions")
    if any(c > 0 for c in clicks):
        ax.barh(y, clicks, color=BRAND["success"], height=0.55, label="Clicks")
        ax.legend(fontsize=8, loc="lower right")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Count")
    ax.invert_yaxis()

    for bar, val in zip(bars, clicks):
        if val > 0:
            ax.text(
                bar.get_width() + max(clicks) * 0.02,
                bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=8, color=BRAND["dark"],
            )

    plt.tight_layout()
    path = output_dir / "top_queries.png"
    plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return str(path)


def chart_index_status(data: dict, output_dir: Path) -> str:
    """Generate donut chart for URL inspection results."""
    summary = data.get("summary", {})
    if not summary:
        return ""

    labels, sizes, colors = [], [], []
    for key, label, color in [
        ("pass", "Indexed", BRAND["success"]),
        ("fail", "Not Indexed", BRAND["danger"]),
        ("neutral", "Neutral", BRAND["grid"]),
        ("error", "Error", BRAND["muted"]),
    ]:
        val = summary.get(key, 0)
        if val > 0:
            labels.append(f"{label} ({val})")
            sizes.append(val)
            colors.append(color)

    if not sizes:
        return ""

    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors, autopct="%1.0f%%",
        startangle=90, pctdistance=0.75, textprops={"fontsize": 9},
    )
    centre = plt.Circle((0, 0), 0.50, fc="white")
    ax.add_artist(centre)
    total = sum(sizes)
    ax.text(0, 0, f"{total}\nURLs", ha="center", va="center",
            fontsize=16, fontweight="bold", color=BRAND["dark"])

    plt.tight_layout()
    path = output_dir / "index_status.png"
    plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return str(path)


# ─── CSS Template ────────────────────────────────────────────────────────────

def _build_css(domain: str) -> str:
    """
    Professional A4 report CSS adapted from generate_pdf.py.

    Uses Times New Roman / DejaVu Serif body font. All proven layout classes
    from the dexdia.com audit report are preserved with the WeasyPrint-safe
    patterns (div.section for page-break, float:right for badges,
    display:table for two-column layouts).
    """
    return f"""\
  @page {{
    size: A4;
    margin: 22mm 18mm 25mm 18mm;
    @bottom-center {{
      content: "Page " counter(page) " of " counter(pages);
      font-size: 9pt;
      color: #6b7280;
      font-family: 'DejaVu Serif', 'Times New Roman', Georgia, serif;
    }}
    @bottom-left {{
      content: "Confidential";
      font-size: 7pt;
      color: #d6d3cc;
      font-family: 'DejaVu Serif', 'Times New Roman', Georgia, serif;
    }}
    @bottom-right {{
      content: "{domain} Google SEO Report";
      font-size: 8pt;
      color: #cbd5e1;
      font-family: 'DejaVu Serif', 'Times New Roman', Georgia, serif;
    }}
  }}

  @page :first {{
    margin: 0;
    @bottom-left {{ content: none; }}
    @bottom-center {{ content: none; }}
    @bottom-right {{ content: none; }}
  }}

  @page toc {{
    @bottom-center {{
      content: counter(page);
      font-size: 9pt;
      color: #6b7280;
    }}
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Times New Roman', 'DejaVu Serif', Georgia, serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    background: white;
  }}

  /* ─── Title Page (Clean White) ─── */
  .title-page {{
    page: first;
    width: 210mm;
    height: 297mm;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #1a1a2e;
    position: relative;
    padding: 50mm 30mm 40mm 30mm;
    border-top: 6mm solid #1e3a5f;
  }}

  .title-page .badge {{
    background: #f7f6f3;
    border: 1px solid #d6d3cc;
    border-radius: 20px;
    padding: 6px 18px;
    font-size: 9pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15mm;
    color: #1e3a5f;
  }}

  .title-page h1 {{
    font-size: 28pt;
    font-weight: bold;
    margin-bottom: 5mm;
    letter-spacing: -0.5px;
    line-height: 1.2;
    color: #1a1a2e;
  }}

  .title-page .subtitle {{
    font-size: 13pt;
    color: #6b7280;
    margin-bottom: 12mm;
    font-weight: 300;
  }}

  .title-page .url {{
    font-size: 12pt;
    color: #1e3a5f;
    margin-bottom: 15mm;
    padding: 4mm 8mm;
    border: 1px solid #d6d3cc;
    border-radius: 6px;
    background: #faf9f7;
  }}

  .title-page .score-box {{
    background: #faf9f7;
    border: 2px solid #d6d3cc;
    border-radius: 12px;
    padding: 6mm 12mm;
    margin-bottom: 15mm;
  }}

  .title-page .score-number {{
    font-size: 42pt;
    font-weight: bold;
    color: #1e3a5f;
    line-height: 1;
  }}

  .title-page .score-label {{
    font-size: 10pt;
    color: #6b7280;
    margin-top: 2mm;
  }}

  .title-page .meta {{
    font-size: 9pt;
    color: #6b7280;
    margin-top: 8mm;
    padding-top: 5mm;
    border-top: 1px solid #d6d3cc;
  }}

  .title-page .meta span {{
    margin: 0 8px;
  }}

  /* ─── Table of Contents ─── */
  .toc-page {{
    page: toc;
    page-break-before: always;
  }}

  .toc-page h2 {{
    font-size: 18pt;
    color: #1e3a5f;
    margin-bottom: 8mm;
    padding-bottom: 3mm;
    border-bottom: 2px solid #1e3a5f;
  }}

  .toc-list {{
    list-style: none;
    padding: 0;
  }}

  .toc-list li {{
    padding: 2mm 0;
    border-bottom: 1px solid #f1f5f9;
    overflow: hidden;
  }}

  .toc-list li.toc-section {{
    font-weight: bold;
    font-size: 11pt;
    padding-top: 4mm;
    color: #0f172a;
  }}

  .toc-list li.toc-sub {{
    padding-left: 8mm;
    font-size: 9.5pt;
    color: #475569;
  }}

  .toc-score {{
    display: inline-block;
    float: right;
    padding: 1px 8px;
    border-radius: 10px;
    font-size: 9pt;
    font-weight: bold;
    color: white;
  }}

  .score-good {{ background: #2d6a4f; }}
  .score-warn {{ background: #d4740e; }}
  .score-bad {{ background: #c53030; }}

  /* ─── Section Styles ─── */
  div.section {{
    page-break-before: always;
  }}

  .section-header {{
    background: #faf9f7;
    border-left: 4px solid #1e3a5f;
    padding: 5mm 6mm;
    margin-bottom: 6mm;
    page-break-after: avoid;
  }}

  .section-header h2 {{
    font-size: 16pt;
    color: #0f172a;
    margin-bottom: 1mm;
  }}

  .section-header .section-score {{
    font-size: 12pt;
    font-weight: bold;
    float: right;
    margin-top: -6mm;
  }}

  h3 {{
    font-size: 12pt;
    color: #1e3a5f;
    margin-top: 6mm;
    margin-bottom: 3mm;
    padding-bottom: 1.5mm;
    border-bottom: 1px solid #d6d3cc;
    page-break-after: avoid;
  }}

  h4 {{
    font-size: 10.5pt;
    color: #334155;
    margin-top: 4mm;
    margin-bottom: 2mm;
    page-break-after: avoid;
  }}

  p {{
    margin-bottom: 3mm;
    color: #334155;
  }}

  .highlight {{
    background: #fef3c7;
    border-left: 3px solid #d4740e;
    padding: 3mm 4mm;
    margin: 4mm 0;
    font-size: 9.5pt;
    /* allow page breaks to prevent white gaps */
  }}

  .critical-box {{
    background: #fef2f2;
    border-left: 3px solid #c53030;
    padding: 3mm 4mm;
    margin: 4mm 0;
    font-size: 9.5pt;
    /* allow page breaks to prevent white gaps */
  }}

  .success-box {{
    background: #f0fdf4;
    border-left: 3px solid #2d6a4f;
    padding: 3mm 4mm;
    margin: 4mm 0;
    font-size: 9.5pt;
    /* allow page breaks to prevent white gaps */
  }}

  /* ─── Tables ─── */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 9pt;
  }}

  thead th {{
    background: #f7f6f3;
    color: #0f172a;
    font-weight: bold;
    padding: 3mm 4mm;
    text-align: left;
    border-bottom: 2px solid #d6d3cc;
    font-size: 9pt;
  }}

  tbody td {{
    padding: 2.5mm 3mm;
    border-bottom: 1px solid #f1f5f9;
    vertical-align: top;
  }}

  tbody tr:nth-child(even) {{
    background: #fdfcfa;
  }}

  .status-pass {{
    color: #2d6a4f;
    font-weight: bold;
  }}

  .status-fail {{
    color: #c53030;
    font-weight: bold;
  }}

  .status-warn {{
    color: #d4740e;
    font-weight: bold;
  }}

  .status-partial {{
    color: #4a5568;
    font-weight: bold;
  }}

  /* ─── Charts ─── */
  .chart-container {{
    text-align: center;
    margin: 4mm 0;
  }}

  .chart-container img {{
    max-width: 100%;
    max-height: 120mm;
    height: auto;
  }}

  .chart-caption {{
    font-size: 8.5pt;
    color: #6b7280;
    font-style: italic;
    margin-top: 2mm;
    text-align: center;
  }}

  .chart-half {{
    display: inline-block;
    width: 48%;
    vertical-align: top;
    text-align: center;
    margin: 2mm 0;
  }}

  .chart-half img {{
    max-width: 100%;
    height: auto;
  }}

  /* ─── Two column layout ─── */
  .two-col {{
    display: table;
    width: 100%;
    table-layout: fixed;
    margin: 3mm 0;
  }}

  .two-col .col {{
    display: table-cell;
    vertical-align: top;
    padding: 0 2mm;
  }}

  .four-col {{
    display: table;
    width: 100%;
    table-layout: fixed;
    margin: 3mm 0;
  }}

  .four-col .col {{
    display: table-cell;
    vertical-align: top;
    padding: 0 1.5mm;
  }}

  /* ─── Metric Cards ─── */
  .metric-card {{
    background: #faf9f7;
    border: 1px solid #d6d3cc;
    border-radius: 6px;
    padding: 2.5mm 3mm;
    text-align: center;
    margin: 2mm 0;
  }}

  .metric-card .value {{
    font-size: 14pt;
    font-weight: bold;
    line-height: 1.2;
  }}

  .metric-card .label {{
    font-size: 7.5pt;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 1mm;
  }}

  /* ─── Action Plan ─── */
  .action-item {{
    background: #faf9f7;
    border-radius: 4px;
    padding: 3mm 4mm;
    margin: 3mm 0;
    border-left: 3px solid #cbd5e1;
    /* allow page breaks to prevent white gaps */
  }}

  .action-item.critical {{
    border-left-color: #c53030;
    background: #fdf2f2;
  }}

  .action-item.high {{
    border-left-color: #d4740e;
    background: #fdf8ef;
  }}

  .action-item.medium {{
    border-left-color: #1e3a5f;
    background: #f0f4f8;
  }}

  .action-item.low {{
    border-left-color: #94a3b8;
  }}

  .action-item h4 {{
    margin-top: 0;
    margin-bottom: 1.5mm;
    border-bottom: none;
    padding-bottom: 0;
  }}

  .action-item .effort {{
    font-size: 8.5pt;
    color: #64748b;
    float: right;
  }}

  .priority-tag {{
    display: inline-block;
    padding: 0.5mm 3mm;
    border-radius: 3px;
    font-size: 8pt;
    font-weight: bold;
    color: white;
    margin-right: 2mm;
    vertical-align: middle;
  }}

  .priority-critical {{ background: #c53030; }}
  .priority-high {{ background: #d4740e; }}
  .priority-medium {{ background: #1e3a5f; }}
  .priority-low {{ background: #94a3b8; }}

  /* ─── Code blocks ─── */
  .code-block {{
    background: #1e293b;
    color: #e2e8f0;
    padding: 3mm 4mm;
    border-radius: 4px;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 8pt;
    line-height: 1.6;
    margin: 3mm 0;
    white-space: pre-wrap;
    word-break: break-all;
    /* allow page breaks to prevent white gaps */
  }}

  /* ─── Divider ─── */
  .divider {{
    border: none;
    border-top: 1px solid #d6d3cc;
    margin: 5mm 0;
  }}

  /* ─── Roadmap ─── */
  .roadmap-phase {{
    background: #faf9f7;
    border-radius: 6px;
    padding: 4mm 5mm;
    margin: 4mm 0;
    border: 1px solid #d6d3cc;
    /* allow page breaks to prevent white gaps */
  }}

  .roadmap-phase h4 {{
    margin-top: 0;
    border-bottom: none;
    color: #1e3a5f;
  }}

  .roadmap-phase ul {{
    margin: 2mm 0 0 5mm;
    padding: 0;
  }}

  .roadmap-phase li {{
    margin-bottom: 1.5mm;
    font-size: 9.5pt;
    color: #334155;
  }}

  /* ─── Lists ─── */
  ul {{
    margin-left: 5mm;
    margin-bottom: 3mm;
  }}

  li {{
    margin-bottom: 1.5mm;
  }}

  /* ─── Data freshness ─── */
  .data-freshness {{
    font-size: 8pt;
    color: #6b7280;
    font-style: italic;
    margin-top: 4mm;
    padding-top: 2mm;
    border-top: 1px solid #d6d3cc;
  }}
"""


# ─── HTML Helpers ────────────────────────────────────────────────────────────

def _img_tag(path, alt="Chart"):
    """Convert file path to file:// URI img tag for WeasyPrint."""
    if not path:
        return ""
    return f'<img src="file://{path}" style="max-width: 100%;" alt="{alt}">'


def _chart_html(path, caption, fig_num, alt="Chart"):
    """Build a complete chart container with figure caption."""
    if not path:
        return ""
    return (
        f'    <div class="chart-container">\n'
        f'      <img src="file://{path}" style="width: 85%;" alt="{alt}">\n'
        f'      <div class="chart-caption">Figure {fig_num}: {caption}</div>\n'
        f'    </div>\n'
    )


def _metric_card(value, label, color=None):
    """Build a metric card HTML block."""
    style = f' style="color: {color};"' if color else ""
    return (
        f'      <div class="metric-card">\n'
        f'        <div class="value"{style}>{value}</div>\n'
        f'        <div class="label">{label}</div>\n'
        f'      </div>\n'
    )


# ─── Section Builders ────────────────────────────────────────────────────────

def _build_title_page(domain, report_title, subtitle, score=None, score_label=None, meta_items=None):
    """Build the gradient title page."""
    score_html = ""
    if score is not None:
        score_html = (
            f'  <div class="score-box">\n'
            f'    <div class="score-number">{score}'
            f'<span style="font-size: 20pt; color: #94a3b8;">/100</span></div>\n'
            f'    <div class="score-label">{score_label or "Lighthouse Performance Score"}</div>\n'
            f'  </div>\n'
        )

    meta_html = ""
    if meta_items:
        spans = "\n    ".join(f"<span>{item}</span>" for item in meta_items)
        meta_html = (
            f'  <div class="meta">\n'
            f'    {spans}\n'
            f'  </div>\n'
        )

    # Google logo (if available in charts dir)
    google_logo_path = Path(__file__).parent.parent / "charts" / "google_logo.png"
    google_logo_html = ""
    if google_logo_path.exists():
        google_logo_html = (
            f'  <div style="margin-top: 8mm;">\n'
            f'    <img src="file://{google_logo_path}" style="height: 20px; opacity: 0.7;" alt="Google">\n'
            f'    <div style="font-size: 7pt; color: #6b7280; margin-top: 2mm;">Powered by Google APIs</div>\n'
            f'  </div>\n'
        )

    return (
        f'\n<!-- {"=" * 55} TITLE PAGE {"=" * 3} -->\n'
        f'<div class="title-page">\n'
        f'  <div class="badge">{report_title}</div>\n'
        f'  <h1>{domain}</h1>\n'
        f'  <div class="subtitle">Prepared by Claude SEO</div>\n'
        f'{score_html}'
        f'{meta_html}'
        f'{google_logo_html}'
        f'</div>\n'
    )


def _build_toc(sections_info):
    """
    Build a Table of Contents page.

    sections_info: list of dicts with keys 'num', 'title', 'score' (optional),
                   and 'subs' (list of subtitle strings).
    """
    items = []
    for sec in sections_info:
        score_html = ""
        if sec.get("score") is not None:
            cls = _score_class(sec["score"])
            score_html = f' <span class="toc-score {cls}">{sec["score"]}</span>'
        items.append(
            f'    <li class="toc-section">'
            f'<span>{sec["num"]}. {sec["title"]}</span>{score_html}'
            f'</li>'
        )
        for sub in sec.get("subs", []):
            items.append(f'    <li class="toc-sub"><span>{sub}</span></li>')

    items_html = "\n".join(items)
    return (
        f'\n<!-- {"=" * 55} TABLE OF CONTENTS {"=" * 3} -->\n'
        f'<div class="toc-page">\n'
        f'  <h2>Table of Contents</h2>\n'
        f'  <ul class="toc-list">\n'
        f'{items_html}\n'
        f'  </ul>\n'
        f'</div>\n'
    )


def _build_executive_summary(domain, timestamp, data, report_type):
    """Build the Executive Summary section with metric cards, issues, and wins."""
    lines = []
    lines.append(f'\n<!-- {"=" * 55} 1. EXECUTIVE SUMMARY {"=" * 3} -->')
    lines.append('<div class="section">')
    lines.append('  <div class="section-header">')
    lines.append('    <h2>1. Executive Summary</h2>')
    lines.append('  </div>')
    lines.append('')

    # Context paragraph
    lines.append(f'  <p>This report presents a comprehensive Google SEO analysis of '
                 f'<strong>{domain}</strong>, generated on {timestamp}. '
                 f'Data was collected from Google PageSpeed Insights, Chrome User Experience '
                 f'Report (CrUX), Google Search Console, and the URL Inspection API as available.</p>')
    lines.append('')

    # Metric cards row
    cards = []

    # PSI performance score
    psi = data.get("psi", {})
    mobile = psi.get("psi", {}).get("mobile", psi) if isinstance(psi, dict) else {}
    perf_score = mobile.get("lighthouse_scores", {}).get("performance")
    if perf_score is not None:
        color = _score_color(perf_score)
        cards.append(("perf", f"{perf_score}/100", "Lighthouse Performance", color))

    seo_score = mobile.get("lighthouse_scores", {}).get("seo")
    if seo_score is not None:
        color = _score_color(seo_score)
        cards.append(("seo", f"{seo_score}/100", "Lighthouse SEO", color))

    # GSC totals
    gsc = data.get("gsc", {})
    if gsc.get("totals"):
        clicks = gsc["totals"].get("clicks", 0)
        cards.append(("clicks", f"{clicks:,}", "Total Clicks", BRAND["primary"]))
        impr = gsc["totals"].get("impressions", 0)
        cards.append(("impr", f"{impr:,}", "Impressions", BRAND["secondary"]))

    # Indexation
    inspection = data.get("inspection", {})
    if inspection.get("summary"):
        indexed = inspection["summary"].get("pass", 0)
        total = inspection.get("total", 0)
        cards.append(("idx", f"{indexed}/{total}", "Indexed URLs", BRAND["success"]))

    # Render metric cards in a compact row
    if cards:
        col_class = "four-col" if len(cards) >= 4 else "two-col"
        display_cards = cards[:5]
        lines.append(f'  <div class="{col_class}">')
        for _, val, lbl, clr in display_cards:
            lines.append(f'    <div class="col">')
            lines.append(_metric_card(val, lbl, clr))
            lines.append(f'    </div>')
        lines.append('  </div>')
        lines.append('')

    # Critical issues box
    issues = []
    failed_audits = mobile.get("failed_audits", [])
    if failed_audits:
        top_fail = sorted(failed_audits, key=lambda a: a.get("score", 1))[:3]
        for a in top_fail:
            issues.append(f'<strong>{a.get("title", "Unknown")}</strong> '
                          f'(score: {a.get("score", 0):.0%})')

    seo_audits = mobile.get("seo_audits", [])
    seo_failed = [a for a in seo_audits if not a.get("pass")]
    for a in seo_failed[:2]:
        issues.append(f'<strong>SEO:</strong> {a.get("title", "Unknown")}')

    inspect_fails = inspection.get("summary", {}).get("fail", 0)
    if inspect_fails:
        issues.append(f'<strong>{inspect_fails} URL(s)</strong> not indexed')

    if issues:
        issue_items = "\n".join(f"      <li>{i}</li>" for i in issues[:5])
        lines.append('  <div class="critical-box">')
        lines.append('    <strong>Critical Issues Found:</strong>')
        lines.append('    <ol>')
        lines.append(issue_items)
        lines.append('    </ol>')
        lines.append('  </div>')
        lines.append('')

    # Quick wins box
    wins = []
    qw = gsc.get("quick_wins", [])
    if qw:
        wins.append(f'{len(qw)} search queries at positions 4-10 with high impressions '
                    f'(small ranking bump = significant traffic)')

    opps = mobile.get("opportunities", [])
    for o in opps[:3]:
        savings = o.get("savings_ms", 0)
        if savings:
            wins.append(f'{o.get("title", "Optimization")}: save ~{savings}ms')

    if wins:
        win_items = "\n".join(f"      <li>{w}</li>" for w in wins[:5])
        lines.append('  <div class="success-box">')
        lines.append('    <strong>Quick Wins:</strong>')
        lines.append('    <ol>')
        lines.append(win_items)
        lines.append('    </ol>')
        lines.append('  </div>')
        lines.append('')

    lines.append('</div>')
    return "\n".join(lines)


def _build_cwv_section(psi_data, crux_data, chart_paths, history_data=None, section_num=2):
    """Build the Core Web Vitals audit section."""
    fig_counter = [1]  # mutable counter for figure numbering

    def next_fig():
        n = fig_counter[0]
        fig_counter[0] += 1
        return n

    lines = []
    lines.append(f'\n<!-- {"=" * 55} {section_num}. CORE WEB VITALS {"=" * 3} -->')
    lines.append('<div class="section">')
    lines.append('  <div class="section-header">')
    lines.append(f'    <h2>{section_num}. Core Web Vitals &amp; Performance</h2>')

    # Section score from Lighthouse performance
    psi = psi_data if isinstance(psi_data, dict) else {}
    mobile = psi.get("psi", {}).get("mobile", psi)
    scores = mobile.get("lighthouse_scores", {})
    perf = scores.get("performance")
    if perf is not None:
        color = _score_color(perf)
        lines.append(f'    <div class="section-score" style="color: {color};">{perf}/100</div>')

    lines.append('  </div>')
    lines.append('')

    # 2.1 Lighthouse Scores gauges
    if scores:
        lines.append(f'  <h3>{section_num}.1 Lighthouse Scores</h3>')
        lines.append('')
        gauges_path = chart_paths.get("gauges_path", "")
        lines.append(_chart_html(
            gauges_path,
            "Lighthouse audit scores across Performance, Accessibility, Best Practices, and SEO.",
            next_fig(),
            "Lighthouse gauge scores",
        ))

        # Scores summary table
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Category</th><th>Score</th><th>Rating</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for key, label in [("performance", "Performance"), ("accessibility", "Accessibility"),
                           ("best-practices", "Best Practices"), ("seo", "SEO")]:
            s = scores.get(key)
            if s is not None:
                cls = "status-pass" if s >= 90 else ("status-warn" if s >= 50 else "status-fail")
                rating = "Good" if s >= 90 else ("Needs Work" if s >= 50 else "Poor")
                lines.append(f'      <tr><td>{label}</td><td class="{cls}">{s}</td><td>{rating}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # Divider between Lighthouse Scores and Lab Metrics
    lines.append('  <hr class="divider">')

    # 2.2 Lab Metrics
    lab = mobile.get("lab_metrics", {})
    if lab:
        lines.append(f'  <h3>{section_num}.2 Lab Metrics (Simulated)</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Metric</th><th>Value</th><th>Score</th><th>Threshold</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        metric_labels = {
            "first-contentful-paint": "First Contentful Paint (FCP)",
            "largest-contentful-paint": "Largest Contentful Paint (LCP)",
            "total-blocking-time": "Total Blocking Time (TBT)",
            "cumulative-layout-shift": "Cumulative Layout Shift (CLS)",
            "speed-index": "Speed Index",
            "interactive": "Time to Interactive (TTI)",
        }
        thresholds = {
            "first-contentful-paint": "\u2264 1.8s",
            "largest-contentful-paint": "\u2264 2.5s",
            "total-blocking-time": "\u2264 200ms",
            "cumulative-layout-shift": "\u2264 0.1",
            "speed-index": "\u2264 3.4s",
            "interactive": "\u2264 3.8s",
        }
        for k, v in lab.items():
            score_val = v.get("score")
            score_pct = f"{score_val:.0%}" if score_val is not None else "N/A"
            cls = ("status-pass" if score_val and score_val >= 0.9
                   else ("status-warn" if score_val and score_val >= 0.5 else "status-fail"))
            label = metric_labels.get(k, k.replace("-", " ").title())
            threshold = thresholds.get(k, "\u2014")
            lines.append(f'      <tr><td>{label}</td><td>{v.get("display", "")}</td>'
                         f'<td class="{cls}">{score_pct}</td><td>{threshold}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # 2.3 CrUX Field Data
    crux = crux_data if isinstance(crux_data, dict) else {}
    crux_metrics = crux.get("metrics", {})
    if crux_metrics:
        lines.append(f'  <h3>{section_num}.3 CrUX Field Data (28-day Rolling Average)</h3>')
        lines.append('')

        # Distribution chart
        dist_path = chart_paths.get("distributions_path", "")
        lines.append(_chart_html(
            dist_path,
            "Core Web Vitals field data distribution across Good, Needs Improvement, and Poor buckets.",
            next_fig(),
            "CWV distribution chart",
        ))

        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Metric</th><th>p75</th><th>Rating</th>'
                     '<th>Good %</th><th>NI %</th><th>Poor %</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for name, m in crux_metrics.items():
            rating = m.get("rating", "?")
            dist = m.get("distribution", {})
            unit = m.get("unit", "")
            p75 = m.get("p75", "?")
            display_val = f"{p75:.3f}" if name == "cumulative_layout_shift" else f"{p75}{unit}"
            cls = _rating_css_class(rating)
            lines.append(f'      <tr><td>{m.get("label", name)}</td><td>{display_val}</td>')
            lines.append(f'      <td class="{cls}">{rating.upper()}</td>')
            lines.append(f'      <td>{dist.get("good", "N/A")}%</td>'
                         f'<td>{dist.get("needs_improvement", "N/A")}%</td>'
                         f'<td>{dist.get("poor", "N/A")}%</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')

        cp = crux.get("collection_period", {})
        if cp:
            lines.append(f'  <p class="data-freshness">Collection period: {cp.get("first", "?")} '
                         f'to {cp.get("last", "?")}. CrUX data is a 28-day rolling average '
                         f'updated daily ~04:00 UTC.</p>')
        lines.append('')
    elif crux.get("error"):
        lines.append(f'  <h3>{section_num}.3 CrUX Field Data</h3>')
        lines.append(f'  <div class="highlight"><strong>CrUX Field Data:</strong> '
                     f'{crux["error"]}</div>')
        lines.append('')

    # CrUX History timeline
    if history_data and not history_data.get("error"):
        lines.append(f'  <h3>{section_num}.4 Core Web Vitals Trends (25-week)</h3>')
        timeline_path = chart_paths.get("timeline_path", "")
        lines.append(_chart_html(
            timeline_path,
            "CrUX p75 values over 25 weeks with Good/Poor threshold bands.",
            next_fig(),
            "CWV timeline trends",
        ))

        trends = history_data.get("trends", {})
        if trends:
            lines.append('  <table>')
            lines.append('    <thead>')
            lines.append('      <tr><th>Metric</th><th>Direction</th><th>Change</th>'
                         '<th>Earliest Avg</th><th>Latest Avg</th></tr>')
            lines.append('    </thead>')
            lines.append('    <tbody>')
            for name, t in trends.items():
                direction = t.get("direction", "?")
                cls = ("status-pass" if direction == "improving"
                       else ("status-fail" if direction == "degrading" else ""))
                lines.append(f'      <tr><td>{t.get("label", name)}</td>'
                             f'<td class="{cls}">{direction.upper()}</td>')
                lines.append(f'      <td>{t.get("change_pct", 0):+.1f}%</td>'
                             f'<td>{t.get("earliest_avg", "?")}</td>'
                             f'<td>{t.get("latest_avg", "?")}</td></tr>')
            lines.append('    </tbody>')
            lines.append('  </table>')
        lines.append('')

    # Failed audits
    failed = mobile.get("failed_audits", [])
    if failed:
        sub = f"{section_num}.5" if history_data and not history_data.get("error") else f"{section_num}.4"
        lines.append(f'  <h3>{sub} Failed / Warning Audits ({len(failed)})</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Audit</th><th>Score</th><th>Details</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for a in failed[:20]:
            score_pct = f"{a['score']:.0%}" if a.get("score") is not None else "?"
            lines.append(f'      <tr><td>{a.get("title", "")}</td>'
                         f'<td class="status-fail">{score_pct}</td>'
                         f'<td>{a.get("display", "")}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # SEO audit checks
    seo_audits = mobile.get("seo_audits", [])
    if seo_audits:
        seo_failed = [a for a in seo_audits if not a.get("pass")]
        if seo_failed:
            lines.append(f'  <h3>SEO Audit Issues ({len(seo_failed)})</h3>')
            for a in seo_failed:
                lines.append(f'  <div class="action-item critical">')
                lines.append(f'    <h4>{a.get("title", "")}</h4>')
                lines.append(f'  </div>')
        else:
            lines.append(f'  <div class="success-box"><strong>SEO:</strong> '
                         f'All {len(seo_audits)} Lighthouse SEO checks passed.</div>')
        lines.append('')

    # Accessibility issues
    a11y = mobile.get("accessibility_audits", [])
    if a11y:
        lines.append(f'  <h3>Accessibility Issues ({len(a11y)})</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Issue</th><th>Score</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for a in a11y:
            lines.append(f'      <tr><td>{a.get("title", "")}</td>'
                         f'<td class="status-fail">{a.get("score", 0):.0%}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # Opportunities
    opps = mobile.get("opportunities", [])
    if opps:
        lines.append(f'  <h3>Optimization Opportunities ({len(opps)})</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Opportunity</th><th>Estimated Savings</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for o in opps:
            lines.append(f'      <tr><td>{o.get("title", "")}</td>'
                         f'<td>{o.get("savings_ms", 0)}ms</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    lines.append('</div>')
    return "\n".join(lines), fig_counter[0]


def _build_gsc_section(gsc_data, chart_paths, section_num=3, fig_start=1):
    """Build the GSC Search Performance section."""
    fig_counter = [fig_start]

    def next_fig():
        n = fig_counter[0]
        fig_counter[0] += 1
        return n

    lines = []
    lines.append(f'\n<!-- {"=" * 55} {section_num}. SEARCH PERFORMANCE {"=" * 3} -->')
    lines.append('<div class="section">')
    lines.append('  <div class="section-header">')
    lines.append(f'    <h2>{section_num}. Search Console Performance</h2>')
    lines.append('  </div>')
    lines.append('')

    totals = gsc_data.get("totals", {})
    dr = gsc_data.get("date_range", {})

    if totals:
        domain = gsc_data.get("property", "?")
        lines.append(f'  <p>Period: {dr.get("start", "?")} to {dr.get("end", "?")} '
                     f'| Property: {domain}</p>')
        queries_count = gsc_data.get("row_count", 0)
        impr_total = totals.get("impressions", 0)
        lines.append(f'  <p><strong>{domain}</strong> appeared in <strong>{queries_count}</strong> unique search queries '
                     f'with <strong>{impr_total:,}</strong> total impressions during this period.</p>')
        lines.append('')

        clicks_val = f'{totals.get("clicks", 0):,}'
        impr_val = f'{totals.get("impressions", 0):,}'
        ctr_val = f'{totals.get("ctr", 0)}%'
        rows_val = str(gsc_data.get("row_count", 0))

        # Metric cards in single row
        lines.append(f'  <h3>{section_num}.1 Key Metrics</h3>')
        lines.append('  <div class="four-col">')
        lines.append(f'    <div class="col">{_metric_card(clicks_val, "Total Clicks", BRAND["primary"])}</div>')
        lines.append(f'    <div class="col">{_metric_card(impr_val, "Total Impressions", BRAND["secondary"])}</div>')
        lines.append(f'    <div class="col">{_metric_card(ctr_val, "Average CTR", BRAND["accent"])}</div>')
        lines.append(f'    <div class="col">{_metric_card(rows_val, "Queries Found", BRAND["dark"])}</div>')
        lines.append('  </div>')
        lines.append('  <hr class="divider">')
        lines.append('')

    # Top queries chart
    queries_path = chart_paths.get("top_queries_path", "")
    if queries_path:
        lines.append(f'  <h3>{section_num}.2 Top Queries by Impressions</h3>')
        lines.append(_chart_html(
            queries_path,
            "Top search queries ranked by impression volume from Google Search Console (28-day period).",
            next_fig(),
            "Top queries bar chart",
        ))

    # Top queries table
    rows = gsc_data.get("rows", [])
    if rows:
        lines.append(f'  <h3>{section_num}.3 Query Detail Table</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>#</th><th>Query</th><th>Clicks</th>'
                     '<th>Impressions</th><th>CTR</th><th>Position</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        sorted_rows = sorted(rows, key=lambda r: r.get("impressions", 0), reverse=True)
        for i, r in enumerate(sorted_rows[:15], 1):
            query = r.get("query", r.get("keys", ["?"])[0])
            pos = r.get("position", 0)
            pos_cls = ("status-pass" if pos <= 3
                       else ("status-warn" if pos <= 10 else "status-fail"))
            lines.append(f'      <tr><td>{i}</td><td>{query}</td>'
                         f'<td>{r.get("clicks", 0)}</td>'
                         f'<td>{r.get("impressions", 0):,}</td>')
            lines.append(f'      <td>{r.get("ctr", 0)}%</td>'
                         f'<td class="{pos_cls}">{pos:.1f}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # Position analysis
    if rows:
        top3 = len([r for r in rows if r.get("position", 99) <= 3])
        top10 = len([r for r in rows if r.get("position", 99) <= 10])
        beyond = len([r for r in rows if r.get("position", 99) > 10])
        lines.append(f'  <h3>{section_num}.4 Query Position Analysis</h3>')
        lines.append('  <div class="two-col">')
        lines.append(f'    <div class="col">')
        lines.append(_metric_card(str(top3), "Queries in Top 3", BRAND["success"]))
        lines.append(f'    </div>')
        lines.append(f'    <div class="col">')
        lines.append(_metric_card(str(top10), "Queries in Top 10", BRAND["warning"]))
        lines.append(f'    </div>')
        lines.append('  </div>')
        if beyond:
            lines.append(f'  <p>{beyond} queries rank beyond position 10 '
                         f'and may benefit from content optimization.</p>')
        lines.append('')

    # Quick wins
    qw = gsc_data.get("quick_wins", [])
    if qw:
        lines.append(f'  <h3>{section_num}.5 Quick Wins ({len(qw)} opportunities)</h3>')
        lines.append('  <div class="highlight">These queries rank at position 4-10 with '
                     'high impressions. A small ranking improvement could yield significant '
                     'traffic gains.</div>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>Query</th><th>Position</th>'
                     '<th>Impressions</th><th>Clicks</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for w in qw:
            query = w.get("keys", ["?"])[0] if w.get("keys") else w.get("query", "?")
            lines.append(f'      <tr><td>{query}</td>'
                         f'<td>{w.get("position", 0):.1f}</td>'
                         f'<td>{w.get("impressions", 0):,}</td>'
                         f'<td>{w.get("clicks", 0)}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    lines.append('  <p class="data-freshness">Search Analytics data has a 2-3 day lag. '
                 'Data available for ~16 months.</p>')
    lines.append('</div>')
    return "\n".join(lines), fig_counter[0]


def _build_indexation_section(inspect_data, chart_paths, section_num=4, fig_start=1):
    """Build the Indexation Status section."""
    fig_counter = [fig_start]

    def next_fig():
        n = fig_counter[0]
        fig_counter[0] += 1
        return n

    lines = []
    lines.append(f'\n<!-- {"=" * 55} {section_num}. INDEXATION STATUS {"=" * 3} -->')
    lines.append('<div class="section">')
    lines.append('  <div class="section-header">')
    lines.append(f'    <h2>{section_num}. Indexation Status</h2>')
    lines.append('  </div>')
    lines.append('')

    summary = inspect_data.get("summary", {})
    total = inspect_data.get("total", 0)

    if summary:
        # Donut chart
        idx_path = chart_paths.get("index_status_path", "")
        if idx_path:
            fig_n = next_fig()
            lines.append(f'  <h3>{section_num}.1 Index Coverage Overview</h3>')
            lines.append(f'    <div class="chart-container">')
            lines.append(f'      <img src="file://{idx_path}" style="width: 70%;" alt="Index status donut chart">')
            lines.append(f'      <div class="chart-caption">Figure {fig_n}: URL indexation status distribution from Google URL Inspection API.</div>')
            lines.append(f'    </div>')

        # Summary cards
        lines.append(f'  <p>Total URLs inspected: <strong>{total}</strong></p>')
        lines.append('  <div class="two-col">')
        lines.append(f'    <div class="col">')
        lines.append(_metric_card(summary.get("pass", 0), "Indexed", BRAND["success"]))
        lines.append(f'    </div>')
        lines.append(f'    <div class="col">')
        lines.append(_metric_card(summary.get("fail", 0), "Not Indexed", BRAND["danger"]))
        lines.append(f'    </div>')
        lines.append('  </div>')
        lines.append('')

        indexed = summary.get("pass", 0)
        not_indexed = summary.get("fail", 0)
        if total > 0:
            rate = round((indexed / total) * 100, 1)
            lines.append(f'  <p><strong>Index Rate:</strong> {rate}% of inspected URLs are indexed by Google.</p>')
        if total > 0 and indexed > 0:
            pct = (indexed / total) * 100
            cls = "success-box" if pct >= 90 else ("highlight" if pct >= 70 else "critical-box")
            lines.append(f'  <div class="{cls}"><strong>Index Rate:</strong> '
                         f'{pct:.0f}% of inspected URLs are indexed.</div>')
            lines.append('')

    # Per-URL results table
    results = inspect_data.get("results", [])
    if results:
        lines.append(f'  <h3>{section_num}.2 Per-URL Results</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>URL</th><th>Verdict</th>'
                     '<th>Coverage State</th><th>Last Crawl</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for r in results:
            verdict = r.get("verdict", "?")
            cls = ("status-pass" if verdict == "PASS"
                   else ("status-fail" if verdict == "FAIL" else ""))
            idx = r.get("index_status", {})
            cov = idx.get("coverage_state", r.get("error", "N/A"))
            crawl = idx.get("last_crawl_time", "N/A")
            if crawl and crawl != "N/A":
                crawl = crawl[:10]
            url_display = r.get("url", "?")
            lines.append(f'      <tr><td style="word-break:break-all;font-size:8pt;">'
                         f'{url_display}</td>')
            lines.append(f'      <td class="{cls}">{verdict}</td>'
                         f'<td>{cov}</td><td>{crawl}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    # Rich results
    rich = inspect_data.get("rich_results", [])
    if rich:
        lines.append(f'  <h3>{section_num}.3 Rich Results Detected</h3>')
        lines.append('  <table>')
        lines.append('    <thead>')
        lines.append('      <tr><th>URL</th><th>Rich Result Type</th></tr>')
        lines.append('    </thead>')
        lines.append('    <tbody>')
        for rr in rich:
            lines.append(f'      <tr><td style="word-break:break-all;font-size:8pt;">'
                         f'{rr.get("url", "?")}</td>'
                         f'<td>{rr.get("type", "?")}</td></tr>')
        lines.append('    </tbody>')
        lines.append('  </table>')
        lines.append('')

    lines.append('  <p class="data-freshness">URL Inspection API: '
                 '2,000 inspections/day per property.</p>')
    lines.append('</div>')
    return "\n".join(lines), fig_counter[0]


def _build_recommendations(data, section_num=5):
    """Build prioritized recommendations section based on discovered issues."""
    lines = []
    lines.append(f'\n<!-- {"=" * 55} {section_num}. RECOMMENDATIONS {"=" * 3} -->')
    lines.append('<div class="section">')
    lines.append('  <div class="section-header">')
    lines.append(f'    <h2>{section_num}. Recommendations</h2>')
    lines.append('  </div>')
    lines.append('')
    lines.append('  <p>Prioritized action items based on the data collected. '
                 'Items are ranked by expected impact on search visibility and user experience.</p>')
    lines.append('')

    item_num = 0

    # Collect critical items
    critical_items = []
    psi = data.get("psi", {})
    mobile = psi.get("psi", {}).get("mobile", psi) if isinstance(psi, dict) else {}

    perf = mobile.get("lighthouse_scores", {}).get("performance")
    if perf is not None and perf < 50:
        critical_items.append(
            ("Improve Lighthouse Performance Score", "Medium (2-4 hrs)",
             f"Current score is {perf}/100. Focus on reducing Largest Contentful Paint "
             f"and Total Blocking Time. Defer non-critical JavaScript and optimize images.")
        )

    seo_failed = [a for a in mobile.get("seo_audits", []) if not a.get("pass")]
    for a in seo_failed[:2]:
        critical_items.append(
            (f"Fix SEO Issue: {a.get('title', 'Unknown')}", "Low (30 min)",
             "This Lighthouse SEO check is failing. Address it to ensure proper crawling "
             "and indexing by search engines.")
        )

    inspect = data.get("inspection", {})
    not_indexed = inspect.get("summary", {}).get("fail", 0)
    if not_indexed:
        critical_items.append(
            (f"Resolve {not_indexed} Non-Indexed URL(s)", "Medium (2-4 hrs)",
             "These pages are not appearing in Google's index. Review coverage state, "
             "fix crawl errors, and request re-indexing via Search Console.")
        )

    if critical_items:
        lines.append(f'  <h3><span class="priority-tag priority-critical">CRITICAL</span> '
                     f'Fix Immediately</h3>')
        for title, effort, desc in critical_items:
            item_num += 1
            lines.append(f'  <div class="action-item critical">')
            lines.append(f'    <h4>{item_num}. {title} '
                         f'<span class="effort">Effort: {effort}</span></h4>')
            lines.append(f'    <p>{desc}</p>')
            lines.append(f'  </div>')
        lines.append('')

    # High priority items
    high_items = []
    failed_audits = mobile.get("failed_audits", [])
    top_fails = sorted(failed_audits, key=lambda a: a.get("score", 1))[:5]
    for a in top_fails:
        if a.get("score", 1) < 0.5:
            high_items.append(
                (f"Address: {a.get('title', 'Unknown')}", "Medium (1-2 hrs)",
                 f"Score: {a['score']:.0%}. {a.get('display', 'Review and optimize this audit.')}")
            )

    opps = mobile.get("opportunities", [])
    for o in opps[:3]:
        savings = o.get("savings_ms", 0)
        if savings:
            high_items.append(
                (f"{o.get('title', 'Optimization')}", "Medium (2-4 hrs)",
                 f"Potential savings of ~{savings}ms. Implement this to improve page load speed.")
            )

    gsc = data.get("gsc", {})
    qw = gsc.get("quick_wins", [])
    if qw:
        high_items.append(
            (f"Optimize {len(qw)} Quick-Win Queries", "Medium (2-4 hrs)",
             "These queries rank at positions 4-10 with high impressions. "
             "Improve on-page SEO and content depth to push them into top 3.")
        )

    if high_items:
        lines.append(f'  <h3><span class="priority-tag priority-high">HIGH</span> '
                     f'Fix Within 1 Week</h3>')
        for title, effort, desc in high_items:
            item_num += 1
            lines.append(f'  <div class="action-item high">')
            lines.append(f'    <h4>{item_num}. {title} '
                         f'<span class="effort">Effort: {effort}</span></h4>')
            lines.append(f'    <p>{desc}</p>')
            lines.append(f'  </div>')
        lines.append('')

    # Medium priority items
    medium_items = []
    a11y = mobile.get("accessibility_audits", [])
    if a11y:
        medium_items.append(
            (f"Fix {len(a11y)} Accessibility Issue(s)", "Low (30 min)",
             "Accessibility improvements benefit SEO (Lighthouse score) and user experience. "
             "Address failing accessibility audits.")
        )

    acc_score = mobile.get("lighthouse_scores", {}).get("accessibility")
    if acc_score is not None and acc_score < 90 and not a11y:
        medium_items.append(
            ("Improve Accessibility Score", "Medium (2-4 hrs)",
             f"Current score: {acc_score}/100. Run a detailed accessibility audit "
             f"and address any violations.")
        )

    bp_score = mobile.get("lighthouse_scores", {}).get("best-practices")
    if bp_score is not None and bp_score < 90:
        medium_items.append(
            ("Address Best Practices Issues", "Low (30 min)",
             f"Current score: {bp_score}/100. Review browser console for errors, "
             f"update deprecated APIs, and ensure HTTPS for all resources.")
        )

    if medium_items:
        lines.append(f'  <h3><span class="priority-tag priority-medium">MEDIUM</span> '
                     f'Fix Within 1 Month</h3>')
        for title, effort, desc in medium_items:
            item_num += 1
            lines.append(f'  <div class="action-item medium">')
            lines.append(f'    <h4>{item_num}. {title} '
                         f'<span class="effort">Effort: {effort}</span></h4>')
            lines.append(f'    <p>{desc}</p>')
            lines.append(f'  </div>')
        lines.append('')

    # If no recommendations were generated at all
    if item_num == 0:
        lines.append('  <div class="success-box"><strong>No critical issues detected.</strong> '
                     'Continue monitoring Core Web Vitals and search performance regularly.</div>')
        lines.append('')

    # Implementation Roadmap
    lines.append('  <hr class="divider">')
    lines.append('  <h3>Implementation Roadmap</h3>')
    lines.append('  <div class="roadmap-phase">')
    lines.append('    <h4>Week 1 &mdash; Quick Wins</h4>')
    lines.append('    <ul>')
    if seo_failed:
        lines.append('      <li>Fix failing Lighthouse SEO checks</li>')
    if a11y:
        lines.append(f'      <li>Address {len(a11y)} accessibility issue(s)</li>')
    bp_score_val = mobile.get("lighthouse_scores", {}).get("best-practices")
    if bp_score_val is not None and bp_score_val < 90:
        lines.append('      <li>Review and fix Best Practices issues</li>')
    if not seo_failed and not a11y and (bp_score_val is None or bp_score_val >= 90):
        lines.append('      <li>Verify all monitoring dashboards are active</li>')
    lines.append('    </ul>')
    lines.append('  </div>')
    lines.append('  <div class="roadmap-phase">')
    lines.append('    <h4>Week 2&ndash;3 &mdash; Performance &amp; Indexation</h4>')
    lines.append('    <ul>')
    if perf is not None and perf < 50:
        lines.append('      <li>Optimize Largest Contentful Paint and Total Blocking Time</li>')
    if not_indexed:
        lines.append(f'      <li>Resolve {not_indexed} non-indexed URL(s)</li>')
    if opps:
        lines.append(f'      <li>Implement {len(opps)} performance optimization(s)</li>')
    if (perf is None or perf >= 50) and not not_indexed and not opps:
        lines.append('      <li>Maintain current performance levels and monitor trends</li>')
    lines.append('    </ul>')
    lines.append('  </div>')
    lines.append('  <div class="roadmap-phase">')
    lines.append('    <h4>Week 4 &mdash; Content &amp; Search Optimization</h4>')
    lines.append('    <ul>')
    if qw:
        lines.append(f'      <li>Optimize {len(qw)} quick-win queries for top-3 rankings</li>')
    lines.append('      <li>Review and improve content depth for underperforming pages</li>')
    lines.append('      <li>Set up ongoing monitoring and reporting cadence</li>')
    lines.append('    </ul>')
    lines.append('  </div>')
    lines.append('')

    lines.append('</div>')
    return "\n".join(lines)


def _build_methodology_footer(domain, timestamp):
    """Build the Data Sources & Methodology footer section."""
    return (
        f'\n<!-- {"=" * 55} DATA SOURCES & METHODOLOGY {"=" * 3} -->\n'
        f'<div class="section" style="text-align: center; padding-top: 15mm;">\n'
        f'  <hr class="divider">\n'
        f'  <h3 style="text-align: left;">Data Sources &amp; Methodology</h3>\n'
        f'  <table>\n'
        f'    <thead>\n'
        f'      <tr><th>Source</th><th>Description</th><th>Update Frequency</th></tr>\n'
        f'    </thead>\n'
        f'    <tbody>\n'
        f'      <tr><td>PageSpeed Insights API</td>\n'
        f'          <td>Lighthouse lab audit (mobile emulation, Moto G Power, slow 4G)</td>\n'
        f'          <td>Real-time</td></tr>\n'
        f'      <tr><td>Chrome UX Report (CrUX)</td>\n'
        f'          <td>28-day rolling field data from real Chrome users</td>\n'
        f'          <td>Daily ~04:00 UTC</td></tr>\n'
        f'      <tr><td>CrUX History API</td>\n'
        f'          <td>25-week p75 trend data per metric</td>\n'
        f'          <td>Weekly</td></tr>\n'
        f'      <tr><td>Google Search Console</td>\n'
        f'          <td>Search Analytics (clicks, impressions, CTR, position)</td>\n'
        f'          <td>2-3 day lag</td></tr>\n'
        f'      <tr><td>URL Inspection API</td>\n'
        f'          <td>Per-URL index status, coverage state, crawl info</td>\n'
        f'          <td>Real-time (2,000/day)</td></tr>\n'
        f'    </tbody>\n'
        f'  </table>\n'
        f'  <p style="color: #94a3b8; font-size: 9pt; margin-top: 5mm;">\n'
        f'    Report generated by Claude SEO &mdash; Google SEO Intelligence Skill &mdash; '
        f'{timestamp}<br>\n'
        f'    Methodology based on Google Web Vitals thresholds, Search Console documentation, '
        f'and Lighthouse scoring algorithms.\n'
        f'  </p>\n'
        f'</div>\n'
    )


# ─── Report Assemblers ───────────────────────────────────────────────────────

def generate_report(report_type, data, domain, output_dir, output_format="pdf"):
    """
    Generate a complete professional PDF/HTML report.

    Args:
        report_type: 'cwv-audit', 'gsc-performance', 'indexation', or 'full'.
        data: Dictionary with all input data.
        domain: Domain name for the report header.
        output_dir: Directory for output files.
        output_format: 'pdf', 'html', or 'both'.

    Returns:
        Dictionary with output paths.
    """
    output_dir = Path(output_dir)
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%B %d, %Y")
    timestamp_short = datetime.now().strftime("%Y-%m-%d %H:%M")
    result = {"report_type": report_type, "domain": domain, "files": [], "error": None}

    # ── Generate Charts ──────────────────────────────────────────────────────

    chart_paths = {}

    if report_type in ("cwv-audit", "full"):
        psi = data.get("psi", data)
        mobile = psi.get("psi", {}).get("mobile", psi) if isinstance(psi, dict) else {}
        path = chart_lighthouse_gauges(mobile, charts_dir)
        if path:
            chart_paths["gauges_path"] = path

        crux = data.get("crux", {})
        path = chart_cwv_distributions({"crux": crux} if crux else data, charts_dir)
        if path:
            chart_paths["distributions_path"] = path

        history = data.get("crux_history", {})
        if history and not history.get("error"):
            path = chart_cwv_timeline(history, charts_dir)
            if path:
                chart_paths["timeline_path"] = path

    if report_type in ("gsc-performance", "full"):
        gsc = data.get("gsc", data)
        path = chart_top_queries(gsc, charts_dir)
        if path:
            chart_paths["top_queries_path"] = path

    if report_type in ("indexation", "full"):
        inspect = data.get("inspection", data)
        path = chart_index_status(inspect, charts_dir)
        if path:
            chart_paths["index_status_path"] = path

    # ── Build HTML Sections ──────────────────────────────────────────────────

    sections = []
    fig_num = 1

    # ── CWV-AUDIT report ─────────────────────────────────────────────────────
    if report_type == "cwv-audit":
        mobile = data.get("psi", data)
        if isinstance(mobile, dict):
            mobile = mobile.get("psi", {}).get("mobile", mobile)
        perf_score = mobile.get("lighthouse_scores", {}).get("performance") if isinstance(mobile, dict) else None

        sections.append(_build_title_page(
            domain, "Core Web Vitals Audit",
            "Performance &amp; User Experience Analysis",
            score=perf_score,
            score_label="Lighthouse Performance Score",
            meta_items=[timestamp, "PageSpeed Insights + CrUX"],
        ))

        # TOC
        toc_sections = [
            {"num": 1, "title": "Executive Summary", "subs": [
                "Key Metrics &amp; Critical Issues",
            ]},
            {"num": 2, "title": "Core Web Vitals &amp; Performance", "score": perf_score, "subs": [
                "Lighthouse Scores",
                "Lab Metrics",
                "CrUX Field Data",
                "Failed Audits &amp; SEO Checks",
            ]},
            {"num": 3, "title": "Recommendations", "subs": [
                "Prioritized Action Items",
            ]},
            {"num": 4, "title": "Data Sources &amp; Methodology", "subs": []},
        ]
        sections.append(_build_toc(toc_sections))

        sections.append(_build_executive_summary(domain, timestamp, data, report_type))

        cwv_html, fig_num = _build_cwv_section(
            data, data.get("crux", {}), chart_paths,
            data.get("crux_history"), section_num=2,
        )
        sections.append(cwv_html)

        sections.append(_build_recommendations(data, section_num=3))
        sections.append(_build_methodology_footer(domain, timestamp))

    # ── GSC-PERFORMANCE report ───────────────────────────────────────────────
    elif report_type == "gsc-performance":
        gsc = data.get("gsc", data)
        clicks = gsc.get("totals", {}).get("clicks", 0)

        sections.append(_build_title_page(
            domain, "Search Console Performance",
            "Google Search Analytics Report",
            score=f"{clicks:,}",
            score_label="Total Clicks",
            meta_items=[timestamp, "Google Search Console API"],
        ))

        toc_sections = [
            {"num": 1, "title": "Executive Summary", "subs": [
                "Key Metrics &amp; Quick Wins",
            ]},
            {"num": 2, "title": "Search Console Performance", "subs": [
                "Key Metrics",
                "Top Queries by Clicks",
                "Query Detail Table",
                "Position Analysis &amp; Quick Wins",
            ]},
            {"num": 3, "title": "Recommendations", "subs": [
                "Prioritized Action Items",
            ]},
            {"num": 4, "title": "Data Sources &amp; Methodology", "subs": []},
        ]
        sections.append(_build_toc(toc_sections))

        sections.append(_build_executive_summary(domain, timestamp, data, report_type))

        gsc_html, fig_num = _build_gsc_section(gsc, chart_paths, section_num=2)
        sections.append(gsc_html)

        sections.append(_build_recommendations(data, section_num=3))
        sections.append(_build_methodology_footer(domain, timestamp))

    # ── INDEXATION report ────────────────────────────────────────────────────
    elif report_type == "indexation":
        inspect = data.get("inspection", data)
        total = inspect.get("total", 0)

        sections.append(_build_title_page(
            domain, "Indexation Status Report",
            "URL Index Coverage Analysis",
            score=total,
            score_label="URLs Inspected",
            meta_items=[timestamp, "URL Inspection API"],
        ))

        toc_sections = [
            {"num": 1, "title": "Executive Summary", "subs": [
                "Index Coverage Overview",
            ]},
            {"num": 2, "title": "Indexation Status", "subs": [
                "Index Coverage Overview",
                "Per-URL Results",
            ]},
            {"num": 3, "title": "Recommendations", "subs": [
                "Prioritized Action Items",
            ]},
            {"num": 4, "title": "Data Sources &amp; Methodology", "subs": []},
        ]
        sections.append(_build_toc(toc_sections))

        sections.append(_build_executive_summary(domain, timestamp, data, report_type))

        idx_html, fig_num = _build_indexation_section(inspect, chart_paths, section_num=2)
        sections.append(idx_html)

        sections.append(_build_recommendations(data, section_num=3))
        sections.append(_build_methodology_footer(domain, timestamp))

    # ── FULL report ──────────────────────────────────────────────────────────
    elif report_type == "full":
        psi = data.get("psi", {})
        mobile = psi.get("psi", {}).get("mobile", psi) if isinstance(psi, dict) else {}
        perf_score = mobile.get("lighthouse_scores", {}).get("performance") if isinstance(mobile, dict) else None

        sections.append(_build_title_page(
            domain, "Google SEO Intelligence Report",
            "Comprehensive Analysis",
            score=perf_score,
            score_label="Lighthouse Performance Score" if perf_score else None,
            meta_items=[timestamp, "All Google APIs"],
        ))

        # Build TOC dynamically based on available data
        toc_sections = [
            {"num": 1, "title": "Executive Summary", "subs": [
                "Key Metrics, Critical Issues &amp; Quick Wins",
            ]},
        ]
        sec_num = 2
        if data.get("psi") or data.get("crux"):
            toc_sections.append({
                "num": sec_num, "title": "Core Web Vitals &amp; Performance",
                "score": perf_score, "subs": [
                    "Lighthouse Scores &amp; Lab Metrics",
                    "CrUX Field Data &amp; Trends",
                    "Failed Audits &amp; Opportunities",
                ],
            })
            sec_num += 1
        if data.get("gsc"):
            toc_sections.append({
                "num": sec_num, "title": "Search Console Performance", "subs": [
                    "Key Metrics &amp; Top Queries",
                    "Position Analysis &amp; Quick Wins",
                ],
            })
            sec_num += 1
        if data.get("inspection"):
            toc_sections.append({
                "num": sec_num, "title": "Indexation Status", "subs": [
                    "Index Coverage &amp; Per-URL Results",
                ],
            })
            sec_num += 1
        toc_sections.append({
            "num": sec_num, "title": "Recommendations", "subs": [
                "Prioritized Action Items",
            ],
        })
        rec_num = sec_num
        sec_num += 1
        toc_sections.append({
            "num": sec_num, "title": "Data Sources &amp; Methodology", "subs": [],
        })

        sections.append(_build_toc(toc_sections))
        sections.append(_build_executive_summary(domain, timestamp, data, report_type))

        current_sec = 2
        if data.get("psi") or data.get("crux"):
            cwv_html, fig_num = _build_cwv_section(
                data.get("psi", {}), data.get("crux", {}), chart_paths,
                data.get("crux_history"), section_num=current_sec,
            )
            sections.append(cwv_html)
            current_sec += 1

        if data.get("gsc"):
            gsc_html, fig_num = _build_gsc_section(
                data["gsc"], chart_paths,
                section_num=current_sec, fig_start=fig_num,
            )
            sections.append(gsc_html)
            current_sec += 1

        if data.get("inspection"):
            idx_html, fig_num = _build_indexation_section(
                data["inspection"], chart_paths,
                section_num=current_sec, fig_start=fig_num,
            )
            sections.append(idx_html)
            current_sec += 1

        sections.append(_build_recommendations(data, section_num=rec_num))
        sections.append(_build_methodology_footer(domain, timestamp))

    # ── Assemble Final HTML ──────────────────────────────────────────────────

    css = _build_css(domain)
    body = "\n".join(sections)
    html_content = (
        f'<!DOCTYPE html>\n'
        f'<html lang="en">\n'
        f'<head>\n'
        f'<meta charset="UTF-8">\n'
        f'<style>\n'
        f'{css}\n'
        f'</style>\n'
        f'</head>\n'
        f'<body>\n'
        f'{body}\n'
        f'</body>\n'
        f'</html>\n'
    )

    # ── Write Output Files ───────────────────────────────────────────────────

    safe_domain = domain.replace(":", "_").replace("/", "_")
    base_name = f"Google-SEO-Report-{safe_domain}-{report_type}"

    if output_format in ("html", "both"):
        html_path = output_dir / f"{base_name}.html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        result["files"].append(str(html_path))

    if output_format in ("pdf", "both"):
        pdf_path = output_dir / f"{base_name}.pdf"
        try:
            HTML(string=html_content).write_pdf(str(pdf_path))
            result["files"].append(str(pdf_path))
            # Post-generation review
            review = _review_pdf(str(pdf_path), html_content)
            if review:
                result["review"] = review
        except Exception as e:
            result["error"] = f"PDF generation failed: {e}"

    return result


def _review_pdf(pdf_path: str, html_content: str) -> dict:
    """
    RULE: Always review the PDF before presenting to the user.
    Check for common rendering issues.
    """
    review = {"issues": [], "page_count": None, "file_size_kb": None}

    # File size
    try:
        size = os.path.getsize(pdf_path)
        review["file_size_kb"] = round(size / 1024, 1)
    except OSError:
        pass

    # Page count (if pypdf available)
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        review["page_count"] = len(reader.pages)
    except ImportError:
        pass

    # HTML-level checks
    import re
    # Check for empty chart containers (img with no src)
    empty_imgs = re.findall(r'<img[^>]*src=""[^>]*>', html_content)
    if empty_imgs:
        review["issues"].append(f"{len(empty_imgs)} empty image tag(s) found")

    # Check for very short sections (might appear as mostly whitespace)
    sections = html_content.split('div class="section"')
    for i, sec in enumerate(sections[1:], 1):
        # Strip HTML tags to get text content
        text_only = re.sub(r'<[^>]+>', '', sec[:2000])
        text_only = re.sub(r'\s+', ' ', text_only).strip()
        if len(text_only) < 50:
            review["issues"].append(f"Section {i} has very little text content ({len(text_only)} chars)")

    # Check for duplicate content
    tables = re.findall(r'<table>.*?</table>', html_content, re.DOTALL)
    if len(tables) != len(set(tables)):
        review["issues"].append("Duplicate tables detected")

    if not review["issues"]:
        review["status"] = "PASS"
    else:
        review["status"] = f"WARN ({len(review['issues'])} issues)"

    return review


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Google SEO Report Generator - Professional PDF/HTML reports"
    )
    parser.add_argument(
        "--type", "-t",
        choices=["cwv-audit", "gsc-performance", "indexation", "full"],
        required=True,
        help="Report type",
    )
    parser.add_argument("--data", "-d", help="Path to JSON data file (or pipe via stdin)")
    parser.add_argument("--domain", required=True, help="Domain name for the report header")
    parser.add_argument("--output-dir", "-o", default=".", help="Output directory (default: current)")
    parser.add_argument(
        "--format", "-f",
        choices=["pdf", "html", "both"],
        default="pdf",
        help="Output format (default: pdf)",
    )
    parser.add_argument("--json", "-j", action="store_true", help="Output metadata as JSON")

    args = parser.parse_args()

    # Load data
    if args.data:
        try:
            with open(args.data, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading data file: {e}", file=sys.stderr)
            sys.exit(1)
    elif not sys.stdin.isatty():
        try:
            data = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            print(f"Error parsing stdin JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Provide --data file or pipe JSON via stdin.", file=sys.stderr)
        sys.exit(1)

    result = generate_report(
        report_type=args.type,
        data=data,
        domain=args.domain,
        output_dir=args.output_dir,
        output_format=args.format,
    )

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for f in result.get("files", []):
            print(f"Generated: {f}")


if __name__ == "__main__":
    main()
```

## File: `scripts/gsc_inspect.py`
```python
#!/usr/bin/env python3
"""
Google Search Console URL Inspection API helper.

Inspects URLs for indexing status, canonical selection, crawl info,
mobile usability, and rich results. Supports single URL and batch mode.

Usage:
    python gsc_inspect.py https://example.com/page --site-url sc-domain:example.com
    python gsc_inspect.py --batch urls.txt --site-url sc-domain:example.com
    python gsc_inspect.py https://example.com/page --json
"""

import argparse
import json
import sys
import time
from typing import Optional

try:
    from googleapiclient.discovery import build
except ImportError:
    print(
        "Error: google-api-python-client required. "
        "Install with: pip install google-api-python-client",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from google_auth import get_oauth_credentials, load_config
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_oauth_credentials, load_config

GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

# Daily limit per site
DAILY_LIMIT = 2000
QPM_LIMIT = 600


def _build_inspection_service():
    """Build the Search Console v1 service for URL Inspection."""
    credentials = get_oauth_credentials(GSC_SCOPES)
    if not credentials:
        return None
    try:
        return build("searchconsole", "v1", credentials=credentials)
    except Exception as e:
        print(f"Error building service: {e}", file=sys.stderr)
        return None


def inspect_url(
    inspection_url: str,
    site_url: str,
    language_code: str = "en",
) -> dict:
    """
    Inspect a single URL via the GSC URL Inspection API.

    Args:
        inspection_url: The URL to inspect.
        site_url: The GSC property (e.g., 'sc-domain:example.com').
        language_code: Language for localized messages (default: 'en').

    Returns:
        Dictionary with inspection results including index status,
        crawl info, canonical, mobile usability, and rich results.
    """
    result = {
        "url": inspection_url,
        "property": site_url,
        "index_status": None,
        "crawl_info": None,
        "canonical": None,
        "mobile_usability": None,
        "rich_results": None,
        "verdict": None,
        "error": None,
    }

    service = _build_inspection_service()
    if not service:
        result["error"] = "Could not build GSC service. Check service account credentials."
        return result

    body = {
        "inspectionUrl": inspection_url,
        "siteUrl": site_url,
        "languageCode": language_code,
    }

    try:
        response = service.urlInspection().index().inspect(body=body).execute()
    except Exception as e:
        error_str = str(e)
        if "403" in error_str:
            result["error"] = (
                f"Permission denied. Add the service account as an Owner "
                f"in GSC property '{site_url}'."
            )
        elif "429" in error_str:
            result["error"] = (
                f"Rate limit exceeded. URL Inspection: {QPM_LIMIT} QPM / {DAILY_LIMIT} QPD per site."
            )
        elif "400" in error_str:
            result["error"] = (
                f"Invalid request. Ensure the URL '{inspection_url}' belongs to "
                f"property '{site_url}'."
            )
        else:
            result["error"] = f"URL Inspection API error: {e}"
        return result

    ir = response.get("inspectionResult", {})

    # Index status
    idx = ir.get("indexStatusResult", {})
    result["verdict"] = idx.get("verdict", "VERDICT_UNSPECIFIED")
    result["index_status"] = {
        "verdict": idx.get("verdict"),
        "coverage_state": idx.get("coverageState"),
        "robots_txt_state": idx.get("robotsTxtState"),
        "indexing_state": idx.get("indexingState"),
        "page_fetch_state": idx.get("pageFetchState"),
        "last_crawl_time": idx.get("lastCrawlTime"),
        "crawled_as": idx.get("crawledAs"),
        "referring_urls": idx.get("referringUrls", []),
    }

    # Canonical
    result["canonical"] = {
        "google_canonical": idx.get("googleCanonical"),
        "user_canonical": idx.get("userCanonical"),
        "match": idx.get("googleCanonical") == idx.get("userCanonical")
        if idx.get("googleCanonical") and idx.get("userCanonical") else None,
    }

    # Mobile usability (deprecated April 2023 but may still return data)
    mu = ir.get("mobileUsabilityResult", {})
    if mu:
        result["mobile_usability"] = {
            "verdict": mu.get("verdict"),
            "issues": [
                {"type": issue.get("issueType"), "message": issue.get("message")}
                for issue in mu.get("issues", [])
            ],
        }

    # Rich results
    rr = ir.get("richResultsResult", {})
    if rr:
        result["rich_results"] = {
            "verdict": rr.get("verdict"),
            "detected_items": [
                {
                    "type": item.get("richResultType"),
                    "items": [
                        {"name": i.get("name"), "issues": i.get("issues", [])}
                        for i in item.get("items", [])
                    ],
                }
                for item in rr.get("detectedItems", [])
            ],
        }

    return result


def batch_inspect(
    urls: list,
    site_url: str,
    delay: float = 1.0,
    language_code: str = "en",
) -> dict:
    """
    Batch inspect multiple URLs with rate limiting.

    Args:
        urls: List of URLs to inspect.
        site_url: GSC property.
        delay: Seconds between requests (default: 1.0 for safety).
        language_code: Language code.

    Returns:
        Dictionary with results list and summary.
    """
    result = {
        "property": site_url,
        "total": len(urls),
        "results": [],
        "summary": {
            "pass": 0,
            "fail": 0,
            "neutral": 0,
            "error": 0,
        },
        "error": None,
    }

    if len(urls) > DAILY_LIMIT:
        result["error"] = (
            f"Batch size ({len(urls)}) exceeds daily limit ({DAILY_LIMIT}). "
            f"Only the first {DAILY_LIMIT} URLs will be processed."
        )
        urls = urls[:DAILY_LIMIT]

    for i, url in enumerate(urls):
        url = url.strip()
        if not url:
            continue

        print(f"Inspecting [{i + 1}/{len(urls)}]: {url}", file=sys.stderr)

        inspection = inspect_url(url, site_url, language_code)
        result["results"].append(inspection)

        verdict = inspection.get("verdict", "")
        if inspection.get("error"):
            result["summary"]["error"] += 1
        elif verdict == "PASS":
            result["summary"]["pass"] += 1
        elif verdict == "FAIL":
            result["summary"]["fail"] += 1
        else:
            result["summary"]["neutral"] += 1

        # Rate limiting
        if i < len(urls) - 1:
            time.sleep(delay)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Google Search Console URL Inspection API helper"
    )
    parser.add_argument("url", nargs="?", help="URL to inspect")
    parser.add_argument(
        "--site-url", "-s",
        help="GSC property (e.g., sc-domain:example.com). Uses default from config if not specified.",
    )
    parser.add_argument(
        "--batch", "-b",
        help="File with URLs to inspect (one per line)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between batch requests in seconds (default: 1.0)",
    )
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Resolve site URL
    site_url = args.site_url
    if not site_url:
        config = load_config()
        site_url = config.get("default_property")
    if not site_url:
        print("Error: No site URL specified. Use --site-url or set default_property in config.", file=sys.stderr)
        sys.exit(1)

    if args.batch:
        # Batch mode
        try:
            with open(args.batch, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error reading batch file: {e}", file=sys.stderr)
            sys.exit(1)

        result = batch_inspect(urls, site_url, delay=args.delay)
    elif args.url:
        result = inspect_url(args.url, site_url)
    else:
        parser.print_help()
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if args.batch:
            summary = result.get("summary", {})
            print(f"=== URL Inspection Batch Results ===")
            print(f"Property: {site_url}")
            print(f"Total: {result.get('total', 0)} | Pass: {summary.get('pass', 0)} | Fail: {summary.get('fail', 0)} | Errors: {summary.get('error', 0)}")
            print()
            for r in result.get("results", []):
                verdict = r.get("verdict", "?")
                status = {"PASS": "OK", "FAIL": "FAIL", "NEUTRAL": "--"}.get(verdict, "ERR")
                print(f"  [{status}] {r.get('url')}")
                if r.get("error"):
                    print(f"       Error: {r['error']}")
                elif verdict == "FAIL":
                    idx = r.get("index_status", {})
                    print(f"       Coverage: {idx.get('coverage_state')} | Fetch: {idx.get('page_fetch_state')}")
        else:
            if result.get("error"):
                print(f"Error: {result['error']}", file=sys.stderr)
                sys.exit(1)

            verdict = result.get("verdict", "?")
            print(f"=== URL Inspection: {result.get('url')} ===")
            print(f"Verdict: {verdict}")

            idx = result.get("index_status", {})
            if idx:
                print(f"\nIndex Status:")
                print(f"  Coverage: {idx.get('coverage_state')}")
                print(f"  Robots.txt: {idx.get('robots_txt_state')}")
                print(f"  Indexing: {idx.get('indexing_state')}")
                print(f"  Page Fetch: {idx.get('page_fetch_state')}")
                print(f"  Last Crawl: {idx.get('last_crawl_time', 'N/A')}")
                print(f"  Crawled As: {idx.get('crawled_as')}")

            canon = result.get("canonical", {})
            if canon:
                print(f"\nCanonical:")
                print(f"  Google: {canon.get('google_canonical', 'N/A')}")
                print(f"  User: {canon.get('user_canonical', 'N/A')}")
                match = canon.get("match")
                if match is not None:
                    print(f"  Match: {'Yes' if match else 'MISMATCH'}")

            rr = result.get("rich_results")
            if rr and rr.get("detected_items"):
                print(f"\nRich Results: {rr.get('verdict')}")
                for item in rr.get("detected_items", []):
                    print(f"  Type: {item.get('type')}")


if __name__ == "__main__":
    main()
```

## File: `scripts/gsc_query.py`
```python
#!/usr/bin/env python3
"""
Google Search Console Search Analytics query helper.

Queries the GSC Search Analytics API for clicks, impressions, CTR, and position
data. Supports filtering by dimensions, auto-pagination, and quick-win detection.

Usage:
    python gsc_query.py --property sc-domain:example.com
    python gsc_query.py --property sc-domain:example.com --days 90 --dimensions query
    python gsc_query.py sitemaps --property sc-domain:example.com
    python gsc_query.py sites
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Optional

try:
    from googleapiclient.discovery import build
except ImportError:
    print(
        "Error: google-api-python-client required. "
        "Install with: pip install google-api-python-client",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from google_auth import get_oauth_credentials, load_config
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_oauth_credentials, load_config

GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def _build_gsc_service():
    """Build the Search Console API service."""
    credentials = get_oauth_credentials(GSC_SCOPES)
    if not credentials:
        return None
    try:
        return build("searchconsole", "v1", credentials=credentials)
    except Exception as e:
        print(f"Error building GSC service: {e}", file=sys.stderr)
        return None


def query_search_analytics(
    site_url: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    dimensions: Optional[list] = None,
    search_type: str = "web",
    row_limit: int = 1000,
    filters: Optional[list] = None,
    data_state: str = "final",
) -> dict:
    """
    Query GSC Search Analytics API.

    Args:
        site_url: GSC property (e.g., 'sc-domain:example.com' or 'https://example.com/').
        start_date: Start date (YYYY-MM-DD). Default: 28 days ago.
        end_date: End date (YYYY-MM-DD). Default: 3 days ago (data lag).
        dimensions: List of dimensions: query, page, country, device, date, searchAppearance.
        search_type: web, image, video, news, discover, googleNews.
        row_limit: Max rows per request (1-25000). Auto-paginates if more.
        filters: List of filter dicts with dimension, operator, expression.
        data_state: 'final' or 'all' (includes fresh/unfinalized data).

    Returns:
        Dictionary with rows, totals, and quick_wins.
    """
    result = {
        "property": site_url,
        "rows": [],
        "totals": {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0},
        "quick_wins": [],
        "row_count": 0,
        "error": None,
    }

    service = _build_gsc_service()
    if not service:
        result["error"] = "Could not build GSC service. Check service account credentials."
        return result

    if not start_date:
        start_date = (datetime.now() - timedelta(days=28)).strftime("%Y-%m-%d")
    if not end_date:
        end_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    if dimensions is None:
        dimensions = ["query", "page"]

    result["date_range"] = {"start": start_date, "end": end_date}

    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "type": search_type,
        "rowLimit": min(row_limit, 25000),
        "dataState": data_state,
    }

    if filters:
        body["dimensionFilterGroups"] = [{"filters": filters}]

    # Auto-paginate
    all_rows = []
    start_row = 0
    page_size = min(row_limit, 25000)

    try:
        while True:
            body["startRow"] = start_row
            body["rowLimit"] = page_size

            response = service.searchanalytics().query(
                siteUrl=site_url, body=body
            ).execute()

            rows = response.get("rows", [])
            all_rows.extend(rows)

            if len(rows) < page_size:
                break

            start_row += page_size

            # Safety: cap at 100,000 rows
            if start_row >= 100000:
                break

    except Exception as e:
        error_str = str(e)
        if "403" in error_str:
            result["error"] = (
                f"Permission denied for property '{site_url}'. "
                "Ensure the service account email is added as a user in "
                "Google Search Console > Settings > Users and permissions."
            )
        elif "404" in error_str:
            result["error"] = (
                f"Property '{site_url}' not found. "
                "Use 'sc-domain:example.com' for domain properties or "
                "'https://example.com/' for URL-prefix properties."
            )
        else:
            result["error"] = f"GSC API error: {e}"
        return result

    # Process rows
    total_clicks = 0
    total_impressions = 0

    for row in all_rows:
        keys = row.get("keys", [])
        clicks = row.get("clicks", 0)
        impressions = row.get("impressions", 0)
        ctr = row.get("ctr", 0)
        position = row.get("position", 0)

        processed = {
            "keys": keys,
            "clicks": clicks,
            "impressions": impressions,
            "ctr": round(ctr * 100, 2),
            "position": round(position, 1),
        }

        # Label keys by dimension name
        for i, dim in enumerate(dimensions):
            if i < len(keys):
                processed[dim] = keys[i]

        result["rows"].append(processed)
        total_clicks += clicks
        total_impressions += impressions

    result["row_count"] = len(all_rows)
    result["totals"]["clicks"] = total_clicks
    result["totals"]["impressions"] = total_impressions
    if total_impressions > 0:
        result["totals"]["ctr"] = round((total_clicks / total_impressions) * 100, 2)

    # Quick wins: position 4-10 with high impressions
    if "query" in dimensions:
        sorted_by_impressions = sorted(all_rows, key=lambda r: r.get("impressions", 0), reverse=True)
        for row in sorted_by_impressions[:200]:
            pos = row.get("position", 0)
            if 4 <= pos <= 10 and row.get("impressions", 0) > 50:
                result["quick_wins"].append({
                    "keys": row.get("keys", []),
                    "position": round(pos, 1),
                    "impressions": row.get("impressions", 0),
                    "clicks": row.get("clicks", 0),
                    "ctr": round(row.get("ctr", 0) * 100, 2),
                    "opportunity": "Position 4-10 with high impressions -- small ranking improvement yields significant traffic gain",
                })

        result["quick_wins"] = result["quick_wins"][:20]

    return result


def list_sitemaps(site_url: str) -> dict:
    """
    List sitemaps for a GSC property.

    Args:
        site_url: GSC property URL.

    Returns:
        Dictionary with sitemaps list.
    """
    result = {"property": site_url, "sitemaps": [], "error": None}

    service = _build_gsc_service()
    if not service:
        result["error"] = "Could not build GSC service."
        return result

    try:
        response = service.sitemaps().list(siteUrl=site_url).execute()
        for sm in response.get("sitemap", []):
            result["sitemaps"].append({
                "path": sm.get("path"),
                "last_submitted": sm.get("lastSubmitted"),
                "is_pending": sm.get("isPending"),
                "is_index": sm.get("isSitemapsIndex"),
                "type": sm.get("type"),
                "warnings": sm.get("warnings", 0),
                "errors": sm.get("errors", 0),
                "contents": sm.get("contents", []),
            })
    except Exception as e:
        result["error"] = f"Error listing sitemaps: {e}"

    return result


def list_sites() -> dict:
    """
    List all verified GSC properties.

    Returns:
        Dictionary with sites list.
    """
    result = {"sites": [], "error": None}

    service = _build_gsc_service()
    if not service:
        result["error"] = "Could not build GSC service."
        return result

    try:
        response = service.sites().list().execute()
        for site in response.get("siteEntry", []):
            result["sites"].append({
                "url": site.get("siteUrl"),
                "permission": site.get("permissionLevel"),
            })
    except Exception as e:
        result["error"] = f"Error listing sites: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Google Search Console Search Analytics query helper"
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="query",
        choices=["query", "sitemaps", "sites"],
        help="Command: query (default), sitemaps, sites",
    )
    parser.add_argument(
        "--property", "-p",
        help="GSC property (e.g., sc-domain:example.com). Uses default from config if not specified.",
    )
    parser.add_argument("--days", "-d", type=int, default=28, help="Number of days (default: 28)")
    parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    parser.add_argument(
        "--dimensions",
        default="query,page",
        help="Comma-separated dimensions (default: query,page)",
    )
    parser.add_argument("--type", default="web", help="Search type (default: web)")
    parser.add_argument("--limit", type=int, default=1000, help="Row limit (default: 1000)")
    parser.add_argument(
        "--device",
        choices=["desktop", "mobile", "tablet"],
        help="Filter by device type",
    )
    parser.add_argument("--country", help="Filter by country (ISO 3166-1 alpha-3, e.g., USA)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Resolve property
    prop = args.property
    if not prop:
        config = load_config()
        prop = config.get("default_property")
    if not prop and args.command != "sites":
        print("Error: No property specified. Use --property or set default_property in config.", file=sys.stderr)
        sys.exit(1)

    if args.command == "sites":
        result = list_sites()
    elif args.command == "sitemaps":
        result = list_sitemaps(prop)
    else:
        start = args.start_date or (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")
        end = args.end_date or (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
        dims = [d.strip() for d in args.dimensions.split(",")]
        filters = []
        if args.device:
            filters.append({
                "dimension": "device",
                "operator": "equals",
                "expression": args.device.upper(),
            })
        if args.country:
            filters.append({
                "dimension": "country",
                "operator": "equals",
                "expression": args.country.upper(),
            })
        result = query_search_analytics(
            prop, start_date=start, end_date=end,
            dimensions=dims, search_type=args.type, row_limit=args.limit,
            filters=filters if filters else None,
        )

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)
        if not args.json:
            sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if args.command == "sites":
            print("=== Verified GSC Properties ===")
            for site in result.get("sites", []):
                print(f"  {site['url']} ({site['permission']})")
        elif args.command == "sitemaps":
            print(f"=== Sitemaps for {prop} ===")
            for sm in result.get("sitemaps", []):
                status = "pending" if sm.get("is_pending") else "processed"
                print(f"  {sm['path']} [{status}] errors={sm.get('errors', 0)} warnings={sm.get('warnings', 0)}")
        else:
            totals = result.get("totals", {})
            print(f"=== Search Analytics: {prop} ===")
            print(f"Period: {result.get('date_range', {}).get('start')} to {result.get('date_range', {}).get('end')}")
            print(f"Clicks: {totals.get('clicks', 0):,} | Impressions: {totals.get('impressions', 0):,} | CTR: {totals.get('ctr', 0)}% | Rows: {result.get('row_count', 0)}")

            qw = result.get("quick_wins", [])
            if qw:
                print(f"\nQuick Wins ({len(qw)} found):")
                for w in qw[:10]:
                    keys = " | ".join(w.get("keys", []))
                    print(f"  Pos {w['position']} | {w['impressions']:,} imp | {w['clicks']} clicks | {keys}")


if __name__ == "__main__":
    main()
```

## File: `scripts/indexing_notify.py`
```python
#!/usr/bin/env python3
"""
Google Indexing API v3 - notify Google of URL updates and removals.

Publishes URL_UPDATED or URL_DELETED notifications. Supports single URL
and batch mode (up to 200 URLs/day). Includes quota tracking.

IMPORTANT: The Indexing API is officially restricted to pages with
JobPosting or BroadcastEvent/VideoObject structured data. Google may
process other page types but provides no guarantees.

Usage:
    python indexing_notify.py https://example.com/jobs/123
    python indexing_notify.py https://example.com/jobs/123 --action URL_DELETED
    python indexing_notify.py --batch urls.txt
    python indexing_notify.py --status https://example.com/jobs/123
"""

import argparse
import json
import sys
import time
from typing import Optional

try:
    from googleapiclient.discovery import build
    from googleapiclient.http import BatchHttpRequest
except ImportError:
    print(
        "Error: google-api-python-client required. "
        "Install with: pip install google-api-python-client",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from google_auth import get_oauth_credentials
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_oauth_credentials

INDEXING_SCOPES = ["https://www.googleapis.com/auth/indexing"]
DAILY_QUOTA = 200

SCOPE_WARNING = (
    "NOTE: The Indexing API is officially for JobPosting and "
    "BroadcastEvent/VideoObject pages only. Google may process other "
    "page types but provides no guarantees."
)


def _build_indexing_service():
    """Build the Indexing API v3 service."""
    credentials = get_oauth_credentials(INDEXING_SCOPES)
    if not credentials:
        return None
    try:
        return build("indexing", "v3", credentials=credentials)
    except Exception as e:
        print(f"Error building Indexing service: {e}", file=sys.stderr)
        return None


def notify_url(
    url: str,
    action: str = "URL_UPDATED",
) -> dict:
    """
    Publish a single URL notification to the Indexing API.

    Args:
        url: The URL to notify about.
        action: 'URL_UPDATED' or 'URL_DELETED'.

    Returns:
        Dictionary with notification result.
    """
    result = {
        "url": url,
        "action": action,
        "notify_time": None,
        "error": None,
    }

    service = _build_indexing_service()
    if not service:
        result["error"] = (
            "Could not build Indexing service. Ensure the service account has "
            "'https://www.googleapis.com/auth/indexing' scope and is added as "
            "Owner in Google Search Console for the target domain."
        )
        return result

    body = {
        "url": url,
        "type": action,
    }

    try:
        response = service.urlNotifications().publish(body=body).execute()
        metadata = response.get("urlNotificationMetadata", {})
        latest = metadata.get("latestUpdate", {}) or metadata.get("latestRemove", {})
        result["notify_time"] = latest.get("notifyTime")
    except Exception as e:
        error_str = str(e)
        if "403" in error_str:
            result["error"] = (
                "Permission denied. The service account must be added as an "
                "Owner in Google Search Console for this domain. "
                "Also ensure the Indexing API is enabled in your GCP project."
            )
        elif "429" in error_str:
            result["error"] = (
                f"Quota exceeded. Daily limit: {DAILY_QUOTA} publish requests. "
                "Apply for a quota increase at https://developers.google.com/search/apis/indexing-api/v3/quota-increase"
            )
        elif "400" in error_str:
            result["error"] = f"Invalid URL or request: {e}"
        else:
            result["error"] = f"Indexing API error: {e}"

    return result


def get_notification_metadata(url: str) -> dict:
    """
    Get the latest notification metadata for a URL.

    Args:
        url: The URL to check.

    Returns:
        Dictionary with latest update and remove timestamps.
    """
    result = {
        "url": url,
        "latest_update": None,
        "latest_remove": None,
        "error": None,
    }

    service = _build_indexing_service()
    if not service:
        result["error"] = "Could not build Indexing service."
        return result

    try:
        response = service.urlNotifications().getMetadata(url=url).execute()
        update = response.get("latestUpdate", {})
        remove = response.get("latestRemove", {})

        if update:
            result["latest_update"] = {
                "url": update.get("url"),
                "type": update.get("type"),
                "notify_time": update.get("notifyTime"),
            }
        if remove:
            result["latest_remove"] = {
                "url": remove.get("url"),
                "type": remove.get("type"),
                "notify_time": remove.get("notifyTime"),
            }
    except Exception as e:
        if "404" in str(e):
            result["error"] = "No notification metadata found for this URL."
        else:
            result["error"] = f"Error fetching metadata: {e}"

    return result


def batch_notify(
    urls: list,
    action: str = "URL_UPDATED",
    delay: float = 0.5,
) -> dict:
    """
    Batch notify multiple URLs with quota awareness.

    Args:
        urls: List of URLs.
        action: 'URL_UPDATED' or 'URL_DELETED'.
        delay: Seconds between requests.

    Returns:
        Dictionary with results and quota usage.
    """
    result = {
        "action": action,
        "total": len(urls),
        "results": [],
        "summary": {"success": 0, "error": 0},
        "quota_warning": None,
        "error": None,
    }

    if len(urls) > DAILY_QUOTA:
        result["quota_warning"] = (
            f"Batch size ({len(urls)}) exceeds daily quota ({DAILY_QUOTA}). "
            f"Only the first {DAILY_QUOTA} URLs will be submitted."
        )
        urls = urls[:DAILY_QUOTA]

    if len(urls) > 50:
        result["quota_warning"] = (
            f"Submitting {len(urls)} URLs will use {len(urls)}/{DAILY_QUOTA} "
            f"of your daily quota."
        )

    for i, url in enumerate(urls):
        url = url.strip()
        if not url:
            continue

        print(f"Notifying [{i + 1}/{len(urls)}]: {url}", file=sys.stderr)

        notification = notify_url(url, action)
        result["results"].append(notification)

        if notification.get("error"):
            result["summary"]["error"] += 1
            # Stop on quota errors
            if "429" in str(notification.get("error", "")):
                result["error"] = "Stopped: daily quota exceeded."
                break
        else:
            result["summary"]["success"] += 1

        if i < len(urls) - 1:
            time.sleep(delay)

    remaining = DAILY_QUOTA - result["summary"]["success"]
    result["estimated_remaining_quota"] = max(0, remaining)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Google Indexing API v3 - URL notification helper"
    )
    parser.add_argument("url", nargs="?", help="URL to notify")
    parser.add_argument(
        "--action", "-a",
        choices=["URL_UPDATED", "URL_DELETED"],
        default="URL_UPDATED",
        help="Notification type (default: URL_UPDATED)",
    )
    parser.add_argument("--batch", "-b", help="File with URLs (one per line)")
    parser.add_argument("--status", help="Check notification status for a URL")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between batch requests in seconds (default: 0.5)",
    )
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.status:
        result = get_notification_metadata(args.status)
    elif args.batch:
        print(SCOPE_WARNING, file=sys.stderr)
        try:
            with open(args.batch, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error reading batch file: {e}", file=sys.stderr)
            sys.exit(1)
        result = batch_notify(urls, args.action, delay=args.delay)
    elif args.url:
        print(SCOPE_WARNING, file=sys.stderr)
        result = notify_url(args.url, args.action)
    else:
        parser.print_help()
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get("error"):
            print(f"Error: {result['error']}", file=sys.stderr)

        if args.status:
            print(f"=== Notification Status: {args.status} ===")
            update = result.get("latest_update")
            remove = result.get("latest_remove")
            if update:
                print(f"  Latest Update: {update.get('notify_time')} ({update.get('type')})")
            if remove:
                print(f"  Latest Remove: {remove.get('notify_time')} ({remove.get('type')})")
            if not update and not remove and not result.get("error"):
                print("  No notifications found.")
        elif args.batch:
            summary = result.get("summary", {})
            print(f"=== Batch Indexing Notification ===")
            print(f"Action: {args.action}")
            print(f"Total: {result.get('total', 0)} | Success: {summary.get('success', 0)} | Errors: {summary.get('error', 0)}")
            print(f"Estimated remaining daily quota: {result.get('estimated_remaining_quota', '?')}")
            if result.get("quota_warning"):
                print(f"Warning: {result['quota_warning']}")
        else:
            if result.get("notify_time"):
                print(f"Notified: {result['url']} ({result['action']}) at {result['notify_time']}")
            elif not result.get("error"):
                print(f"Notification sent for: {result['url']} ({result['action']})")


if __name__ == "__main__":
    main()
```

## File: `scripts/keyword_planner.py`
```python
#!/usr/bin/env python3
"""
Google Ads API - Keyword Planner for SEO keyword research.

Gold-standard source for keyword search volume, CPC, and competition data.
Requires a Google Ads Manager account with a developer token.

Usage:
    python keyword_planner.py ideas "seo tools" --json
    python keyword_planner.py volume "seo tools,seo audit,seo checker" --json
    python keyword_planner.py forecast "seo tools" --json

Prerequisites:
    - Google Ads Manager account (can be free)
    - Developer Token (apply at Google Ads API Center)
    - OAuth credentials or service account
    - google-ads Python library: pip install google-ads
    - Config: ~/.config/claude-seo/google-api.json with:
      {
        "ads_developer_token": "YOUR_DEV_TOKEN",
        "ads_customer_id": "123-456-7890",
        "ads_login_customer_id": "123-456-7890"
      }

Note: Accounts without active ad spend receive bucketed volume ranges
(e.g., "1K-10K") instead of exact numbers.
"""

import argparse
import json
import sys
from typing import Optional

try:
    from google.ads.googleads.client import GoogleAdsClient
    from google.ads.googleads.errors import GoogleAdsException
    HAS_GOOGLE_ADS = True
except ImportError:
    HAS_GOOGLE_ADS = False

try:
    from google_auth import load_config
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import load_config


def _build_ads_client() -> Optional[object]:
    """Build Google Ads client from config."""
    if not HAS_GOOGLE_ADS:
        print(
            "Error: google-ads library required. Install with: pip install google-ads",
            file=sys.stderr,
        )
        return None

    config = load_config()
    dev_token = config.get("ads_developer_token")
    customer_id = config.get("ads_customer_id", "").replace("-", "")
    login_customer_id = config.get("ads_login_customer_id", "").replace("-", "")
    oauth_client_path = config.get("oauth_client_path")

    if not dev_token:
        print(
            "Error: No Google Ads developer token configured. "
            "Add 'ads_developer_token' to ~/.config/claude-seo/google-api.json. "
            "Get a token at: https://ads.google.com/aw/apicenter",
            file=sys.stderr,
        )
        return None

    if not customer_id:
        print(
            "Error: No Google Ads customer ID configured. "
            "Add 'ads_customer_id' (format: 123-456-7890) to config.",
            file=sys.stderr,
        )
        return None

    try:
        # Build from dict configuration
        ads_config = {
            "developer_token": dev_token,
            "use_proto_plus": True,
        }
        if login_customer_id:
            ads_config["login_customer_id"] = login_customer_id

        # Try to use OAuth token if available
        token_path = os.path.expanduser("~/.config/claude-seo/oauth-token.json")
        if os.path.exists(token_path):
            with open(token_path) as f:
                token_data = json.load(f)
            if oauth_client_path:
                with open(os.path.expanduser(oauth_client_path)) as f:
                    client_data = json.load(f)
                client_info = client_data.get("web", client_data.get("installed", {}))
                ads_config["client_id"] = client_info.get("client_id")
                ads_config["client_secret"] = client_info.get("client_secret")
                ads_config["refresh_token"] = token_data.get("refresh_token")

        client = GoogleAdsClient.load_from_dict(ads_config)
        return client, customer_id

    except Exception as e:
        print(f"Error building Google Ads client: {e}", file=sys.stderr)
        return None


def generate_keyword_ideas(
    seed_keywords: list,
    language_id: str = "1000",
    location_id: str = "2840",
    limit: int = 50,
) -> dict:
    """
    Generate keyword ideas from seed keywords.

    Args:
        seed_keywords: List of seed keyword strings.
        language_id: Language ID (1000 = English).
        location_id: Location ID (2840 = United States).
        limit: Max results.

    Returns:
        Dictionary with keyword ideas and metrics.
    """
    result = {
        "seed_keywords": seed_keywords,
        "ideas": [],
        "error": None,
    }

    client_data = _build_ads_client()
    if not client_data:
        result["error"] = "Could not build Google Ads client. Check config."
        return result

    client, customer_id = client_data

    try:
        kp_service = client.get_service("KeywordPlanIdeaService")
        request = client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = customer_id
        request.language = f"languageConstants/{language_id}"
        request.geo_target_constants.append(f"geoTargetConstants/{location_id}")
        request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
        request.keyword_seed.keywords.extend(seed_keywords)

        response = kp_service.generate_keyword_ideas(request=request)

        for idea in response.results:
            metrics = idea.keyword_idea_metrics
            monthly_volumes = []
            for mv in metrics.monthly_search_volumes:
                monthly_volumes.append({
                    "year": mv.year,
                    "month": mv.month,
                    "volume": mv.monthly_searches,
                })

            result["ideas"].append({
                "keyword": idea.text,
                "avg_monthly_searches": metrics.avg_monthly_searches,
                "competition": metrics.competition.name if metrics.competition else "UNSPECIFIED",
                "competition_index": metrics.competition_index,
                "low_top_of_page_bid": metrics.low_top_of_page_bid_micros / 1_000_000 if metrics.low_top_of_page_bid_micros else None,
                "high_top_of_page_bid": metrics.high_top_of_page_bid_micros / 1_000_000 if metrics.high_top_of_page_bid_micros else None,
                "monthly_volumes": monthly_volumes[-12:] if monthly_volumes else [],
            })

            if len(result["ideas"]) >= limit:
                break

        # Sort by volume descending
        result["ideas"].sort(key=lambda k: k.get("avg_monthly_searches", 0) or 0, reverse=True)

    except GoogleAdsException as e:
        errors = [err.message for err in e.failure.errors]
        result["error"] = f"Google Ads API error: {'; '.join(errors)}"
    except Exception as e:
        result["error"] = f"Keyword Planner error: {e}"

    return result


def get_keyword_volumes(
    keywords: list,
    language_id: str = "1000",
    location_id: str = "2840",
) -> dict:
    """
    Get search volume for specific keywords.

    Args:
        keywords: List of keywords to check.
        language_id: Language ID.
        location_id: Location ID.

    Returns:
        Dictionary with keyword metrics.
    """
    result = {
        "keywords": [],
        "error": None,
    }

    client_data = _build_ads_client()
    if not client_data:
        result["error"] = "Could not build Google Ads client."
        return result

    client, customer_id = client_data

    try:
        kp_service = client.get_service("KeywordPlanIdeaService")
        request = client.get_type("GenerateKeywordHistoricalMetricsRequest")
        request.customer_id = customer_id
        request.keywords.extend(keywords)
        request.language = f"languageConstants/{language_id}"
        request.geo_target_constants.append(f"geoTargetConstants/{location_id}")
        request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH

        response = kp_service.generate_keyword_historical_metrics(request=request)

        for kw_result in response.results:
            metrics = kw_result.keyword_metrics
            result["keywords"].append({
                "keyword": kw_result.text,
                "avg_monthly_searches": metrics.avg_monthly_searches,
                "competition": metrics.competition.name if metrics.competition else "UNSPECIFIED",
                "competition_index": metrics.competition_index,
                "low_top_of_page_bid": metrics.low_top_of_page_bid_micros / 1_000_000 if metrics.low_top_of_page_bid_micros else None,
                "high_top_of_page_bid": metrics.high_top_of_page_bid_micros / 1_000_000 if metrics.high_top_of_page_bid_micros else None,
            })

    except GoogleAdsException as e:
        errors = [err.message for err in e.failure.errors]
        result["error"] = f"Google Ads API error: {'; '.join(errors)}"
    except Exception as e:
        result["error"] = f"Keyword volume error: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Google Ads Keyword Planner - SEO keyword research"
    )
    parser.add_argument(
        "command",
        choices=["ideas", "volume"],
        help="Command: ideas (keyword suggestions), volume (search volume lookup)",
    )
    parser.add_argument("keywords", help="Seed keyword(s), comma-separated for volume")
    parser.add_argument("--limit", type=int, default=50, help="Max results for ideas (default: 50)")
    parser.add_argument("--language", default="1000", help="Language ID (default: 1000 = English)")
    parser.add_argument("--location", default="2840", help="Location ID (default: 2840 = US)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.command == "ideas":
        seeds = [k.strip() for k in args.keywords.split(",")]
        result = generate_keyword_ideas(seeds, language_id=args.language, location_id=args.location, limit=args.limit)
    elif args.command == "volume":
        kws = [k.strip() for k in args.keywords.split(",")]
        result = get_keyword_volumes(kws, language_id=args.language, location_id=args.location)

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)
        if not args.json:
            sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if args.command == "ideas":
            print(f"=== Keyword Ideas ===")
            for i, idea in enumerate(result.get("ideas", [])[:20], 1):
                vol = idea.get("avg_monthly_searches", "?")
                comp = idea.get("competition", "?")
                bid_low = idea.get("low_top_of_page_bid")
                bid_high = idea.get("high_top_of_page_bid")
                bid_str = f"${bid_low:.2f}-${bid_high:.2f}" if bid_low and bid_high else "N/A"
                print(f"  {i:2d}. {idea['keyword']:40s} | Vol: {vol:>8} | Comp: {comp:8s} | CPC: {bid_str}")
        elif args.command == "volume":
            print(f"=== Keyword Volumes ===")
            for kw in result.get("keywords", []):
                vol = kw.get("avg_monthly_searches", "?")
                comp = kw.get("competition", "?")
                print(f"  {kw['keyword']:40s} | Vol: {vol:>8} | Comp: {comp}")


if __name__ == "__main__":
    main()
```

## File: `scripts/nlp_analyze.py`
```python
#!/usr/bin/env python3
"""
Google Cloud Natural Language API - Entity, sentiment, and content analysis.

Enhances E-E-A-T scoring with NLP entity coverage, sentiment analysis,
and Google's own content classification taxonomy.

Usage:
    python nlp_analyze.py --text "Your content here" --json
    python nlp_analyze.py --url https://example.com --json
    python nlp_analyze.py --text "Your content" --features entities,sentiment,classify
"""

import argparse
import json
import sys
from typing import Optional

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

try:
    from google_auth import get_api_key, validate_url
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_api_key, validate_url

NLP_ENDPOINT = "https://language.googleapis.com/v2/documents:annotateText"

# Free tier: 5,000 units/month per feature
# Paid: $0.001 per 1,000-character unit for entity/sentiment
FEATURES = {
    "entities": "extractEntities",
    "sentiment": "extractDocumentSentiment",
    "classify": "classifyText",
    "categories": "classifyText",
    "moderate": "moderateText",
}


def analyze_text(
    text: str,
    features: Optional[list] = None,
    api_key: Optional[str] = None,
    language: str = "en",
) -> dict:
    """
    Analyze text using Google Cloud Natural Language API.

    Args:
        text: Text content to analyze (max 1M characters).
        features: List of features: entities, sentiment, classify, moderate.
        api_key: Google API key.
        language: Language code (default: en).

    Returns:
        Dictionary with entities, sentiment, categories, and moderation results.
    """
    result = {
        "text_length": len(text),
        "language": language,
        "entities": [],
        "sentiment": None,
        "categories": [],
        "moderation": [],
        "error": None,
    }

    key = api_key or get_api_key()
    if not key:
        result["error"] = "No API key. Set GOOGLE_API_KEY or add 'api_key' to config."
        return result

    if features is None:
        features = ["entities", "sentiment", "classify"]

    # Build request
    feature_map = {}
    for f in features:
        api_feature = FEATURES.get(f)
        if api_feature:
            feature_map[api_feature] = True

    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text[:100000],  # API limit
            "languageCode": language,
        },
        "features": feature_map,
        "encodingType": "UTF8",
    }

    try:
        resp = requests.post(
            f"{NLP_ENDPOINT}?key={key}",
            json=body,
            timeout=30,
        )

        if resp.status_code == 403:
            result["error"] = (
                "Cloud Natural Language API access denied. Enable it in "
                "GCP Console: APIs & Services > Library > Cloud Natural Language API. "
                "Billing must be enabled on the project."
            )
            return result

        if resp.status_code == 429:
            result["error"] = "NLP API quota exceeded. Free tier: 5,000 units/month."
            return result

        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        result["error"] = f"NLP API request failed: {e}"
        return result

    # Entities
    for entity in data.get("entities", []):
        mentions = entity.get("mentions", [])
        result["entities"].append({
            "name": entity.get("name", ""),
            "type": entity.get("type", "UNKNOWN"),
            "salience": round(entity.get("salience", 0), 4),
            "sentiment_score": entity.get("sentiment", {}).get("score"),
            "sentiment_magnitude": entity.get("sentiment", {}).get("magnitude"),
            "mention_count": len(mentions),
            "metadata": entity.get("metadata", {}),
        })

    # Sort by salience (most important first)
    result["entities"].sort(key=lambda e: e["salience"], reverse=True)

    # Document sentiment
    doc_sentiment = data.get("documentSentiment", {})
    if doc_sentiment:
        score = doc_sentiment.get("score", 0)
        magnitude = doc_sentiment.get("magnitude", 0)
        if score > 0.25:
            tone = "positive"
        elif score < -0.25:
            tone = "negative"
        else:
            tone = "neutral"

        result["sentiment"] = {
            "score": round(score, 3),
            "magnitude": round(magnitude, 3),
            "tone": tone,
            "interpretation": (
                f"{'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'} "
                f"(score: {score:.2f}) with "
                f"{'high' if magnitude > 2 else 'moderate' if magnitude > 0.5 else 'low'} "
                f"emotional content (magnitude: {magnitude:.2f})"
            ),
        }

        # Sentence-level sentiment
        sentences = data.get("sentences", [])
        if sentences:
            result["sentiment"]["sentence_count"] = len(sentences)
            sent_scores = [s.get("sentiment", {}).get("score", 0) for s in sentences]
            result["sentiment"]["most_positive"] = max(sent_scores) if sent_scores else 0
            result["sentiment"]["most_negative"] = min(sent_scores) if sent_scores else 0

    # Categories (content classification)
    for cat in data.get("categories", []):
        result["categories"].append({
            "name": cat.get("name", ""),
            "confidence": round(cat.get("confidence", 0), 4),
        })

    # Moderation categories
    for mod in data.get("moderationCategories", []):
        if mod.get("confidence", 0) > 0.5:
            result["moderation"].append({
                "name": mod.get("name", ""),
                "confidence": round(mod.get("confidence", 0), 4),
            })

    return result


def analyze_url(
    url: str,
    features: Optional[list] = None,
    api_key: Optional[str] = None,
) -> dict:
    """
    Fetch a URL's text content and analyze it.

    Args:
        url: URL to fetch and analyze.
        features: NLP features to extract.
        api_key: API key override.

    Returns:
        Dictionary with NLP analysis results.
    """
    if not validate_url(url):
        return {"error": "Invalid URL. Only http/https URLs to public hosts are accepted."}

    # Fetch the page text
    try:
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (compatible; ClaudeSEO/1.7 NLP Analyzer)"
        })
        resp.raise_for_status()
        html = resp.text
    except requests.exceptions.RequestException as e:
        return {"error": f"Could not fetch URL: {e}"}

    # Extract text from HTML (simple approach)
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Remove script and style
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
    except ImportError:
        # Fallback: regex-based text extraction
        import re
        text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

    if not text or len(text) < 50:
        return {"error": "Extracted text too short for meaningful NLP analysis."}

    result = analyze_text(text, features=features, api_key=api_key)
    result["source_url"] = url
    result["extracted_text_length"] = len(text)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Google Cloud Natural Language API - Entity/sentiment/classification for SEO"
    )
    parser.add_argument("--text", "-t", help="Text to analyze")
    parser.add_argument("--url", "-u", help="URL to fetch and analyze")
    parser.add_argument(
        "--features", "-f",
        default="entities,sentiment,classify",
        help="Comma-separated features: entities, sentiment, classify, moderate (default: entities,sentiment,classify)",
    )
    parser.add_argument("--api-key", help="API key override")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not args.text and not args.url:
        print("Error: Provide --text or --url to analyze.", file=sys.stderr)
        sys.exit(1)

    features = [f.strip() for f in args.features.split(",")]

    if args.url:
        result = analyze_url(args.url, features=features, api_key=args.api_key)
    else:
        result = analyze_text(args.text, features=features, api_key=args.api_key)

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)
        if not args.json:
            sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get("source_url"):
            print(f"=== NLP Analysis: {result['source_url']} ===")
            print(f"Text extracted: {result.get('extracted_text_length', 0):,} chars")
        else:
            print(f"=== NLP Analysis ({result.get('text_length', 0):,} chars) ===")

        sent = result.get("sentiment")
        if sent:
            print(f"\nSentiment: {sent['tone'].upper()} (score: {sent['score']}, magnitude: {sent['magnitude']})")
            print(f"  {sent['interpretation']}")

        entities = result.get("entities", [])
        if entities:
            print(f"\nTop Entities ({len(entities)} total):")
            for e in entities[:15]:
                print(f"  [{e['type']:12s}] {e['name']} (salience: {e['salience']:.3f})")

        categories = result.get("categories", [])
        if categories:
            print(f"\nContent Categories:")
            for c in categories:
                print(f"  {c['name']} ({c['confidence']:.1%})")

        moderation = result.get("moderation", [])
        if moderation:
            print(f"\nModeration Flags:")
            for m in moderation:
                print(f"  {m['name']} ({m['confidence']:.1%})")


if __name__ == "__main__":
    main()
```

## File: `scripts/pagespeed_check.py`
```python
#!/usr/bin/env python3
"""
PageSpeed Insights v5 + CrUX API combined checker.

Runs Lighthouse lab analysis via PSI and fetches real Chrome UX field data
via the CrUX API. Merges both perspectives into a single report.

Usage:
    python pagespeed_check.py https://example.com
    python pagespeed_check.py https://example.com --strategy mobile
    python pagespeed_check.py https://example.com --crux-only
    python pagespeed_check.py https://example.com --psi-only --json
"""

import argparse
import json
import sys
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)

# Import credential helper (same directory)
try:
    from google_auth import get_api_key, load_config, validate_url
except ImportError:
    # Fallback: try relative import from scripts/
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_api_key, load_config, validate_url

PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
CRUX_ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"

# Core Web Vitals thresholds (March 2026)
CWV_THRESHOLDS = {
    "largest_contentful_paint": {"good": 2500, "poor": 4000, "unit": "ms", "label": "LCP"},
    "interaction_to_next_paint": {"good": 200, "poor": 500, "unit": "ms", "label": "INP"},
    "cumulative_layout_shift": {"good": 0.1, "poor": 0.25, "unit": "", "label": "CLS"},
    "first_contentful_paint": {"good": 1800, "poor": 3000, "unit": "ms", "label": "FCP"},
    "experimental_time_to_first_byte": {"good": 800, "poor": 1800, "unit": "ms", "label": "TTFB"},
}

PSI_METRIC_MAP = {
    "LARGEST_CONTENTFUL_PAINT_MS": "largest_contentful_paint",
    "INTERACTION_TO_NEXT_PAINT": "interaction_to_next_paint",
    "CUMULATIVE_LAYOUT_SHIFT_SCORE": "cumulative_layout_shift",
    "FIRST_CONTENTFUL_PAINT_MS": "first_contentful_paint",
    "EXPERIMENTAL_TIME_TO_FIRST_BYTE": "experimental_time_to_first_byte",
}


def rate_metric(metric_name: str, value: float) -> str:
    """Rate a CWV metric as good/needs-improvement/poor."""
    thresholds = CWV_THRESHOLDS.get(metric_name)
    if not thresholds:
        return "unknown"
    if value <= thresholds["good"]:
        return "good"
    elif value <= thresholds["poor"]:
        return "needs-improvement"
    else:
        return "poor"


def run_pagespeed(
    url: str,
    strategy: str = "mobile",
    api_key: Optional[str] = None,
    categories: Optional[list] = None,
) -> dict:
    """
    Run PageSpeed Insights v5 analysis.

    Args:
        url: URL to analyze.
        strategy: 'mobile' or 'desktop'.
        api_key: Google API key (optional but recommended for quota).
        categories: List of categories: PERFORMANCE, ACCESSIBILITY, BEST_PRACTICES, SEO.

    Returns:
        Dictionary with lighthouse scores, lab metrics, field data (if available),
        and opportunities. Error in 'error' field on failure.
    """
    result = {
        "url": url,
        "strategy": strategy,
        "lighthouse_scores": {},
        "lab_metrics": {},
        "field_metrics": {},
        "opportunities": [],
        "diagnostics": [],
        "failed_audits": [],
        "passed_audits_count": 0,
        "seo_audits": [],
        "accessibility_audits": [],
        "analysis_timestamp": None,
        "error": None,
    }

    if not validate_url(url):
        result["error"] = "Invalid URL. Only http/https URLs to public hosts are accepted."
        return result

    if categories is None:
        categories = ["PERFORMANCE", "ACCESSIBILITY", "BEST_PRACTICES", "SEO"]

    params = {
        "url": url,
        "strategy": strategy.upper(),
    }
    for cat in categories:
        params.setdefault("category", [])
        if isinstance(params["category"], list):
            params["category"].append(cat)

    if api_key:
        params["key"] = api_key

    try:
        resp = requests.get(PSI_ENDPOINT, params=params, timeout=120)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.Timeout:
        result["error"] = "PageSpeed Insights request timed out (120s). The target page may be very slow."
        return result
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 429:
            result["error"] = "PSI rate limit exceeded (240 QPM / 25,000 QPD). Wait and retry."
        elif resp.status_code == 400:
            result["error"] = f"Invalid URL or parameters: {resp.text}"
        else:
            result["error"] = f"PSI API error {resp.status_code}: {e}"
        return result
    except requests.exceptions.RequestException as e:
        result["error"] = f"Request failed: {e}"
        return result

    result["analysis_timestamp"] = data.get("analysisUTCTimestamp")

    # Lighthouse scores
    lr = data.get("lighthouseResult", {})
    for cat_key, cat_data in lr.get("categories", {}).items():
        result["lighthouse_scores"][cat_key] = round(cat_data.get("score", 0) * 100)

    # Lab metrics from Lighthouse audits
    audits = lr.get("audits", {})
    lab_audit_ids = [
        "first-contentful-paint", "largest-contentful-paint",
        "total-blocking-time", "cumulative-layout-shift",
        "speed-index", "interactive",
    ]
    for audit_id in lab_audit_ids:
        audit = audits.get(audit_id, {})
        if audit.get("numericValue") is not None:
            result["lab_metrics"][audit_id] = {
                "value": audit["numericValue"],
                "display": audit.get("displayValue", ""),
                "score": audit.get("score"),
            }

    # Field data from PSI (loading experience)
    for exp_key in ["loadingExperience", "originLoadingExperience"]:
        exp = data.get(exp_key, {})
        metrics = exp.get("metrics", {})
        if metrics:
            field_source = "url" if exp_key == "loadingExperience" else "origin"
            for psi_name, crux_name in PSI_METRIC_MAP.items():
                metric_data = metrics.get(psi_name, {})
                if metric_data:
                    p75 = metric_data.get("percentile")
                    category = metric_data.get("category", "NONE")
                    if p75 is not None:
                        # CLS from PSI is already numeric
                        if crux_name == "cumulative_layout_shift":
                            p75_val = p75 / 100 if p75 > 1 else p75
                        else:
                            p75_val = p75
                        result["field_metrics"][f"{field_source}_{crux_name}"] = {
                            "p75": p75_val,
                            "rating": category.lower().replace("_", "-"),
                            "source": f"PSI {field_source}-level",
                        }

    # Opportunities
    for audit_id, audit in audits.items():
        if audit.get("details", {}).get("type") == "opportunity":
            savings = audit.get("details", {}).get("overallSavingsMs")
            if savings and savings > 0:
                result["opportunities"].append({
                    "id": audit_id,
                    "title": audit.get("title", audit_id),
                    "savings_ms": savings,
                    "description": audit.get("description", ""),
                })

    result["opportunities"].sort(key=lambda x: x["savings_ms"], reverse=True)

    # Diagnostics (performance bottlenecks)
    diagnostic_ids = [
        "dom-size", "render-blocking-resources", "uses-long-cache-ttl",
        "total-byte-weight", "mainthread-work-breakdown", "bootup-time",
        "font-display", "third-party-summary", "largest-contentful-paint-element",
        "layout-shifts", "long-tasks", "duplicated-javascript",
        "legacy-javascript", "unused-javascript", "unused-css-rules",
    ]
    for diag_id in diagnostic_ids:
        audit = audits.get(diag_id, {})
        if audit:
            score = audit.get("score")
            result["diagnostics"].append({
                "id": diag_id,
                "title": audit.get("title", diag_id),
                "display": audit.get("displayValue", ""),
                "score": score,
                "description": audit.get("description", ""),
            })

    # Failed and warning audits (score < 0.9, excluding opportunities already captured)
    opportunity_ids = {o["id"] for o in result["opportunities"]}
    passed_count = 0
    for audit_id, audit in audits.items():
        score = audit.get("score")
        if score is None:
            continue
        if score >= 0.9:
            passed_count += 1
            continue
        if audit_id in opportunity_ids:
            continue
        result["failed_audits"].append({
            "id": audit_id,
            "title": audit.get("title", audit_id),
            "score": score,
            "display": audit.get("displayValue", ""),
            "description": audit.get("description", ""),
        })
    result["passed_audits_count"] = passed_count
    result["failed_audits"].sort(key=lambda x: x.get("score", 1))

    # SEO audits from the SEO category
    seo_cat = lr.get("categories", {}).get("seo", {})
    for ref in seo_cat.get("auditRefs", []):
        audit = audits.get(ref.get("id"), {})
        if audit and audit.get("score") is not None:
            result["seo_audits"].append({
                "id": ref["id"],
                "title": audit.get("title", ref["id"]),
                "score": audit["score"],
                "pass": audit["score"] >= 0.9,
            })

    # Accessibility audits from the accessibility category
    a11y_cat = lr.get("categories", {}).get("accessibility", {})
    for ref in a11y_cat.get("auditRefs", []):
        audit = audits.get(ref.get("id"), {})
        if audit and audit.get("score") is not None and audit["score"] < 0.9:
            result["accessibility_audits"].append({
                "id": ref["id"],
                "title": audit.get("title", ref["id"]),
                "score": audit["score"],
                "display": audit.get("displayValue", ""),
            })

    # Audit details: extract top items from audits with details.items[]
    # This captures WHICH specific resources are problems (e.g., "hero.jpg is 2MB")
    for audit_id, audit in audits.items():
        details = audit.get("details", {})
        items = details.get("items", [])
        headings = details.get("headings", [])
        if items and headings:
            heading_keys = [h.get("key", "") for h in headings if h.get("key")]
            extracted_items = []
            for item in items[:5]:
                row = {}
                for key in heading_keys:
                    val = item.get(key)
                    if isinstance(val, dict):
                        row[key] = val.get("url") or val.get("text") or str(val)[:200]
                    elif val is not None:
                        row[key] = val
                if row:
                    extracted_items.append(row)
            if extracted_items:
                result["audit_details"][audit_id] = {
                    "title": audit.get("title", audit_id),
                    "headings": heading_keys,
                    "items": extracted_items,
                    "total_items": len(items),
                }

    return result


def query_crux(
    url_or_origin: str,
    api_key: str,
    form_factor: Optional[str] = None,
) -> dict:
    """
    Query the CrUX API for field data (28-day rolling average).

    Args:
        url_or_origin: Full URL or origin (e.g., https://example.com).
        api_key: Google API key.
        form_factor: DESKTOP, PHONE, or TABLET. None for all form factors.

    Returns:
        Dictionary with p75 metrics, distributions, collection period, and rating.
        Error in 'error' field on failure.
    """
    result = {
        "target": url_or_origin,
        "metrics": {},
        "collection_period": None,
        "form_factor": form_factor or "ALL",
        "error": None,
    }

    if not validate_url(url_or_origin):
        result["error"] = "Invalid URL. Only http/https URLs to public hosts are accepted."
        return result

    parsed = urlparse(url_or_origin)
    # Determine if this is a URL or an origin
    is_origin = parsed.path in ("", "/") and not parsed.query

    body = {}
    if is_origin:
        body["origin"] = f"{parsed.scheme}://{parsed.netloc}"
    else:
        body["url"] = url_or_origin

    if form_factor:
        body["formFactor"] = form_factor.upper()

    try:
        resp = requests.post(
            f"{CRUX_ENDPOINT}?key={api_key}",
            json=body,
            timeout=30,
        )

        if resp.status_code == 404:
            target_type = "origin" if is_origin else "URL"
            result["error"] = (
                f"No CrUX data for this {target_type}. "
                "The site likely has insufficient Chrome traffic volume for eligibility."
            )
            return result

        if resp.status_code == 429:
            result["error"] = "CrUX API rate limit exceeded (150 QPM shared with History API). Wait and retry."
            return result

        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        result["error"] = f"CrUX API request failed: {e}"
        return result

    record = data.get("record", {})

    # Collection period
    cp = record.get("collectionPeriod", {})
    if cp:
        first = cp.get("firstDate", {})
        last = cp.get("lastDate", {})
        result["collection_period"] = {
            "first": f"{first.get('year')}-{first.get('month', 0):02d}-{first.get('day', 0):02d}",
            "last": f"{last.get('year')}-{last.get('month', 0):02d}-{last.get('day', 0):02d}",
        }

    # Metrics
    for metric_name, metric_data in record.get("metrics", {}).items():
        p75s = metric_data.get("percentiles", {})
        p75 = p75s.get("p75")
        if p75 is None:
            continue

        # CLS is string-encoded in CrUX -- parse carefully
        if metric_name == "cumulative_layout_shift":
            try:
                p75_val = float(str(p75))
            except (ValueError, TypeError):
                p75_val = 0.0
        else:
            try:
                p75_val = int(p75)
            except (ValueError, TypeError):
                try:
                    p75_val = float(p75)
                except (ValueError, TypeError):
                    continue

        rating = rate_metric(metric_name, p75_val)
        thresholds = CWV_THRESHOLDS.get(metric_name, {})

        result["metrics"][metric_name] = {
            "p75": p75_val,
            "rating": rating,
            "label": thresholds.get("label", metric_name),
            "unit": thresholds.get("unit", ""),
            "good_threshold": thresholds.get("good"),
            "poor_threshold": thresholds.get("poor"),
        }

        # Distributions
        histogram = metric_data.get("histogram", [])
        if histogram:
            densities = [bin_data.get("density", 0) for bin_data in histogram]
            if len(densities) >= 3:
                result["metrics"][metric_name]["distribution"] = {
                    "good": round(densities[0] * 100, 1),
                    "needs_improvement": round(densities[1] * 100, 1),
                    "poor": round(densities[2] * 100, 1),
                }

    return result


def combined_check(
    url: str,
    api_key: Optional[str] = None,
    strategy: str = "both",
) -> dict:
    """
    Run combined PSI + CrUX check.

    Args:
        url: URL to analyze.
        api_key: Google API key.
        strategy: 'mobile', 'desktop', or 'both'.

    Returns:
        Dictionary with PSI results (per strategy) and CrUX field data.
    """
    result = {
        "url": url,
        "psi": {},
        "crux": None,
        "error": None,
    }

    strategies = ["mobile", "desktop"] if strategy == "both" else [strategy]

    for strat in strategies:
        psi_result = run_pagespeed(url, strategy=strat, api_key=api_key)
        result["psi"][strat] = psi_result
        if psi_result.get("error"):
            result["error"] = psi_result["error"]

    # CrUX (separate call for accurate field data)
    if api_key:
        crux_result = query_crux(url, api_key)
        result["crux"] = crux_result
        # Also try origin-level if URL-level has no data
        if crux_result.get("error") and "insufficient" in crux_result.get("error", ""):
            parsed = urlparse(url)
            origin = f"{parsed.scheme}://{parsed.netloc}"
            origin_result = query_crux(origin, api_key)
            if not origin_result.get("error"):
                result["crux"] = origin_result
                result["crux"]["note"] = "URL-level data unavailable; showing origin-level data"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="PageSpeed Insights v5 + CrUX API combined checker"
    )
    parser.add_argument("url", help="URL to analyze")
    parser.add_argument(
        "--strategy", "-s",
        choices=["mobile", "desktop", "both"],
        default="both",
        help="Analysis strategy (default: both)",
    )
    parser.add_argument(
        "--api-key",
        help="Google API key (overrides config/env)",
    )
    parser.add_argument(
        "--crux-only",
        action="store_true",
        help="Only fetch CrUX field data (skip PSI Lighthouse)",
    )
    parser.add_argument(
        "--psi-only",
        action="store_true",
        help="Only run PSI Lighthouse (skip CrUX API)",
    )
    parser.add_argument(
        "--form-factor",
        choices=["PHONE", "DESKTOP", "TABLET"],
        help="CrUX form factor filter",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    api_key = args.api_key or get_api_key()

    if args.crux_only:
        if not api_key:
            print("Error: CrUX API requires an API key. Use --api-key or configure GOOGLE_API_KEY.", file=sys.stderr)
            sys.exit(1)
        result = query_crux(args.url, api_key, form_factor=args.form_factor)
    elif args.psi_only:
        strategies = ["mobile", "desktop"] if args.strategy == "both" else [args.strategy]
        result = {"psi": {}}
        for strat in strategies:
            result["psi"][strat] = run_pagespeed(args.url, strategy=strat, api_key=api_key)
    else:
        result = combined_check(args.url, api_key=api_key, strategy=args.strategy)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        # Pretty print summary
        if args.crux_only:
            _print_crux_summary(result)
        elif args.psi_only:
            for strat, psi in result.get("psi", {}).items():
                _print_psi_summary(psi)
        else:
            for strat, psi in result.get("psi", {}).items():
                _print_psi_summary(psi)
            if result.get("crux"):
                print()
                _print_crux_summary(result["crux"])

    # Exit with error code if any errors occurred
    if isinstance(result, dict) and result.get("error"):
        sys.exit(1)


def _print_psi_summary(psi: dict):
    """Print PSI results in human-readable format."""
    if psi.get("error"):
        print(f"PSI Error ({psi.get('strategy', '?')}): {psi['error']}")
        return

    print(f"\n=== PageSpeed Insights ({psi.get('strategy', 'unknown')}) ===")
    print(f"URL: {psi.get('url')}")
    print(f"Timestamp: {psi.get('analysis_timestamp', 'N/A')}")

    scores = psi.get("lighthouse_scores", {})
    if scores:
        print("\nLighthouse Scores:")
        for cat, score in scores.items():
            print(f"  {cat}: {score}/100")

    lab = psi.get("lab_metrics", {})
    if lab:
        print("\nLab Metrics:")
        for metric_id, data in lab.items():
            print(f"  {metric_id}: {data.get('display', data.get('value'))}")

    opps = psi.get("opportunities", [])
    if opps:
        print("\nTop Opportunities:")
        for opp in opps[:5]:
            print(f"  - {opp['title']} (save ~{opp['savings_ms']}ms)")

    failed = psi.get("failed_audits", [])
    if failed:
        print(f"\nFailed/Warning Audits ({len(failed)}):")
        for a in failed[:10]:
            score_pct = f"{a['score']:.0%}" if a['score'] is not None else "?"
            print(f"  [{score_pct}] {a['title']} {a.get('display', '')}")

    diags = psi.get("diagnostics", [])
    notable_diags = [d for d in diags if d.get("score") is not None and d["score"] < 0.9]
    if notable_diags:
        print(f"\nDiagnostics (needs attention):")
        for d in notable_diags[:5]:
            score_pct = f"{d['score']:.0%}" if d['score'] is not None else "info"
            print(f"  [{score_pct}] {d['title']}: {d.get('display', '')}")

    seo = psi.get("seo_audits", [])
    seo_failed = [a for a in seo if not a.get("pass")]
    if seo_failed:
        print(f"\nSEO Issues ({len(seo_failed)}):")
        for a in seo_failed:
            print(f"  [FAIL] {a['title']}")
    elif seo:
        print(f"\nSEO: All {len(seo)} checks passed")

    a11y = psi.get("accessibility_audits", [])
    if a11y:
        print(f"\nAccessibility Issues ({len(a11y)}):")
        for a in a11y[:5]:
            print(f"  [{a['score']:.0%}] {a['title']}")

    passed = psi.get("passed_audits_count", 0)
    if passed:
        print(f"\nPassed: {passed} audits")


def _print_crux_summary(crux: dict):
    """Print CrUX results in human-readable format."""
    if crux.get("error"):
        print(f"CrUX Error: {crux['error']}")
        return

    print(f"=== CrUX Field Data ({crux.get('form_factor', 'ALL')}) ===")
    print(f"Target: {crux.get('target')}")

    if crux.get("note"):
        print(f"Note: {crux['note']}")

    cp = crux.get("collection_period", {})
    if cp:
        print(f"Period: {cp.get('first')} to {cp.get('last')}")

    metrics = crux.get("metrics", {})
    if metrics:
        print("\nCore Web Vitals (p75):")
        for name, data in metrics.items():
            label = data.get("label", name)
            p75 = data.get("p75")
            unit = data.get("unit", "")
            rating = data.get("rating", "?")
            good = data.get("good_threshold")

            rating_icon = {"good": "GOOD", "needs-improvement": "NEEDS IMPROVEMENT", "poor": "POOR"}.get(rating, "?")

            if name == "cumulative_layout_shift":
                print(f"  {label}: {p75:.3f} [{rating_icon}] (threshold: <={good})")
            else:
                print(f"  {label}: {p75}{unit} [{rating_icon}] (threshold: <={good}{unit})")

            dist = data.get("distribution")
            if dist:
                print(f"       Good: {dist['good']}% | NI: {dist['needs_improvement']}% | Poor: {dist['poor']}%")


if __name__ == "__main__":
    main()
```

## File: `scripts/parse_html.py`
```python
#!/usr/bin/env python3
"""
Parse HTML and extract SEO-relevant elements.

Usage:
    python parse_html.py page.html
    python parse_html.py --url https://example.com
"""

import argparse
import json
import os
import re
import sys
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 required. Install with: pip install beautifulsoup4")
    sys.exit(1)

try:
    import lxml  # noqa: F401
    _HTML_PARSER = "lxml"
except ImportError:
    _HTML_PARSER = "html.parser"


def parse_html(html: str, base_url: Optional[str] = None) -> dict:
    """
    Parse HTML and extract SEO-relevant elements.

    Args:
        html: HTML content to parse
        base_url: Base URL for resolving relative links

    Returns:
        Dictionary with extracted SEO data
    """
    soup = BeautifulSoup(html, _HTML_PARSER)

    result = {
        "title": None,
        "meta_description": None,
        "meta_robots": None,
        "canonical": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "images": [],
        "links": {
            "internal": [],
            "external": [],
        },
        "schema": [],
        "open_graph": {},
        "twitter_card": {},
        "word_count": 0,
        "hreflang": [],
    }

    # Title
    title_tag = soup.find("title")
    if title_tag:
        result["title"] = title_tag.get_text(strip=True)

    # Meta tags
    for meta in soup.find_all("meta"):
        name = meta.get("name", "").lower()
        property_attr = meta.get("property", "").lower()
        content = meta.get("content", "")

        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content

        # Open Graph
        if property_attr.startswith("og:"):
            result["open_graph"][property_attr] = content

        # Twitter Card
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    # Canonical
    canonical = soup.find("link", rel="canonical")
    if canonical:
        result["canonical"] = canonical.get("href")

    # Hreflang
    for link in soup.find_all("link", rel="alternate"):
        hreflang = link.get("hreflang")
        if hreflang:
            result["hreflang"].append({
                "lang": hreflang,
                "href": link.get("href"),
            })

    # Headings
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                result[tag].append(text)

    # Images
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src:
            src = urljoin(base_url, src)

        result["images"].append({
            "src": src,
            "alt": img.get("alt"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
        })

    # Links
    if base_url:
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue

            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            link_data = {
                "href": full_url,
                "text": a.get_text(strip=True)[:100],
                "rel": a.get("rel", []),
            }

            if parsed.netloc == base_domain:
                result["links"]["internal"].append(link_data)
            else:
                result["links"]["external"].append(link_data)

    # Schema (JSON-LD)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            schema_data = json.loads(script.string)
            result["schema"].append(schema_data)
        except (json.JSONDecodeError, TypeError):
            pass

    # Word count (visible text only)
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r"\b\w+\b", text)
    result["word_count"] = len(words)

    return result


def main():
    parser = argparse.ArgumentParser(description="Parse HTML for SEO analysis")
    parser.add_argument("file", nargs="?", help="HTML file to parse")
    parser.add_argument("--url", "-u", help="Base URL for resolving links")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.file:
        real_path = os.path.realpath(args.file)
        if not os.path.isfile(real_path):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(real_path, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    result = parse_html(html, args.url)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Title: {result['title']}")
        print(f"Meta Description: {result['meta_description']}")
        print(f"Canonical: {result['canonical']}")
        print(f"H1 Tags: {len(result['h1'])}")
        print(f"H2 Tags: {len(result['h2'])}")
        print(f"Images: {len(result['images'])}")
        print(f"Internal Links: {len(result['links']['internal'])}")
        print(f"External Links: {len(result['links']['external'])}")
        print(f"Schema Blocks: {len(result['schema'])}")
        print(f"Word Count: {result['word_count']}")


if __name__ == "__main__":
    main()
```

## File: `scripts/youtube_search.py`
```python
#!/usr/bin/env python3
"""
YouTube Data API v3 - Search, video details, and channel data for SEO.

YouTube mentions have the strongest AI visibility correlation (0.737).
This script provides authoritative YouTube data directly from Google.

Usage:
    python youtube_search.py search "claude code seo"
    python youtube_search.py video dQw4w9WgXcQ --json
    python youtube_search.py channel UCxxxxxx --json
"""

import argparse
import json
import sys
from typing import Optional

try:
    from googleapiclient.discovery import build
except ImportError:
    print(
        "Error: google-api-python-client required. "
        "Install with: pip install google-api-python-client",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from google_auth import get_api_key
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from google_auth import get_api_key

# YouTube Data API v3 quota costs:
# search.list = 100 units, videos.list = 1 unit, channels.list = 1 unit
# Default quota: 10,000 units/day = ~100 searches or ~10,000 video lookups
YOUTUBE_API_SERVICE = "youtube"
YOUTUBE_API_VERSION = "v3"


def _build_youtube_service(api_key: Optional[str] = None):
    """Build the YouTube Data API v3 service."""
    key = api_key or get_api_key()
    if not key:
        return None
    try:
        return build(YOUTUBE_API_SERVICE, YOUTUBE_API_VERSION, developerKey=key)
    except Exception as e:
        print(f"Error building YouTube service: {e}", file=sys.stderr)
        return None


def search_videos(
    query: str,
    max_results: int = 10,
    order: str = "relevance",
    api_key: Optional[str] = None,
) -> dict:
    """
    Search YouTube for videos matching a query.

    Args:
        query: Search query string.
        max_results: Max results (1-50, default 10).
        order: Sort order: relevance, date, rating, viewCount, title.
        api_key: Optional API key override.

    Returns:
        Dictionary with videos list and metadata.
    """
    result = {"query": query, "videos": [], "total_results": 0, "error": None}

    service = _build_youtube_service(api_key)
    if not service:
        result["error"] = "No API key. Set GOOGLE_API_KEY or add 'api_key' to config."
        return result

    try:
        response = service.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=min(max_results, 50),
            order=order,
        ).execute()

        result["total_results"] = response.get("pageInfo", {}).get("totalResults", 0)

        # Get video IDs for statistics
        video_ids = []
        snippets = {}
        for item in response.get("items", []):
            vid = item["id"].get("videoId")
            if vid:
                video_ids.append(vid)
                snippets[vid] = item.get("snippet", {})

        # Fetch statistics for all videos in one call (1 unit)
        if video_ids:
            stats_response = service.videos().list(
                id=",".join(video_ids),
                part="statistics,contentDetails",
            ).execute()

            stats_map = {}
            for item in stats_response.get("items", []):
                stats_map[item["id"]] = {
                    "views": int(item.get("statistics", {}).get("viewCount", 0)),
                    "likes": int(item.get("statistics", {}).get("likeCount", 0)),
                    "comments": int(item.get("statistics", {}).get("commentCount", 0)),
                    "duration": item.get("contentDetails", {}).get("duration", ""),
                }

            for vid in video_ids:
                snip = snippets.get(vid, {})
                stats = stats_map.get(vid, {})
                result["videos"].append({
                    "video_id": vid,
                    "title": snip.get("title", ""),
                    "channel": snip.get("channelTitle", ""),
                    "channel_id": snip.get("channelId", ""),
                    "published": snip.get("publishedAt", ""),
                    "description": snip.get("description", "")[:300],
                    "thumbnail": snip.get("thumbnails", {}).get("high", {}).get("url", ""),
                    "views": stats.get("views", 0),
                    "likes": stats.get("likes", 0),
                    "comments": stats.get("comments", 0),
                    "duration": stats.get("duration", ""),
                    "url": f"https://www.youtube.com/watch?v={vid}",
                })

    except Exception as e:
        error_str = str(e)
        if "403" in error_str:
            result["error"] = (
                "YouTube Data API access denied. Ensure the API is enabled "
                "in your GCP project (APIs & Services > Library > YouTube Data API v3)."
            )
        elif "429" in error_str:
            result["error"] = "YouTube API quota exceeded (10,000 units/day). Search costs 100 units."
        else:
            result["error"] = f"YouTube API error: {e}"

    return result


def get_video_details(
    video_id: str,
    api_key: Optional[str] = None,
) -> dict:
    """
    Get detailed information about a specific YouTube video.

    Args:
        video_id: YouTube video ID.
        api_key: Optional API key override.

    Returns:
        Dictionary with video details, statistics, and top comments.
    """
    result = {"video_id": video_id, "details": None, "comments": [], "error": None}

    service = _build_youtube_service(api_key)
    if not service:
        result["error"] = "No API key configured."
        return result

    try:
        # Video details (1 unit)
        response = service.videos().list(
            id=video_id,
            part="snippet,statistics,contentDetails,topicDetails",
        ).execute()

        items = response.get("items", [])
        if not items:
            result["error"] = f"Video not found: {video_id}"
            return result

        item = items[0]
        snip = item.get("snippet", {})
        stats = item.get("statistics", {})
        content = item.get("contentDetails", {})
        topics = item.get("topicDetails", {})

        result["details"] = {
            "title": snip.get("title", ""),
            "channel": snip.get("channelTitle", ""),
            "channel_id": snip.get("channelId", ""),
            "published": snip.get("publishedAt", ""),
            "description": snip.get("description", ""),
            "tags": snip.get("tags", []),
            "category_id": snip.get("categoryId", ""),
            "duration": content.get("duration", ""),
            "definition": content.get("definition", ""),
            "caption": content.get("caption", "false"),
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "comments_count": int(stats.get("commentCount", 0)),
            "favorites": int(stats.get("favoriteCount", 0)),
            "topic_categories": topics.get("topicCategories", []),
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }

        # Top comments (1 unit)
        try:
            comments_response = service.commentThreads().list(
                videoId=video_id,
                part="snippet",
                maxResults=10,
                order="relevance",
                textFormat="plainText",
            ).execute()

            for thread in comments_response.get("items", []):
                comment = thread.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
                result["comments"].append({
                    "author": comment.get("authorDisplayName", ""),
                    "text": comment.get("textDisplay", "")[:500],
                    "likes": comment.get("likeCount", 0),
                    "published": comment.get("publishedAt", ""),
                })
        except Exception:
            pass  # Comments may be disabled

    except Exception as e:
        result["error"] = f"YouTube API error: {e}"

    return result


def get_channel_info(
    channel_id: str,
    api_key: Optional[str] = None,
) -> dict:
    """
    Get channel information.

    Args:
        channel_id: YouTube channel ID.
        api_key: Optional API key override.

    Returns:
        Dictionary with channel details.
    """
    result = {"channel_id": channel_id, "channel": None, "error": None}

    service = _build_youtube_service(api_key)
    if not service:
        result["error"] = "No API key configured."
        return result

    try:
        response = service.channels().list(
            id=channel_id,
            part="snippet,statistics,brandingSettings",
        ).execute()

        items = response.get("items", [])
        if not items:
            result["error"] = f"Channel not found: {channel_id}"
            return result

        item = items[0]
        snip = item.get("snippet", {})
        stats = item.get("statistics", {})

        result["channel"] = {
            "title": snip.get("title", ""),
            "description": snip.get("description", "")[:500],
            "custom_url": snip.get("customUrl", ""),
            "published": snip.get("publishedAt", ""),
            "country": snip.get("country", ""),
            "subscribers": int(stats.get("subscriberCount", 0)),
            "videos": int(stats.get("videoCount", 0)),
            "views": int(stats.get("viewCount", 0)),
            "thumbnail": snip.get("thumbnails", {}).get("high", {}).get("url", ""),
        }

    except Exception as e:
        result["error"] = f"YouTube API error: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="YouTube Data API v3 - Search and video analysis for SEO"
    )
    parser.add_argument(
        "command",
        choices=["search", "video", "channel"],
        help="Command: search, video (details), channel (info)",
    )
    parser.add_argument("query", help="Search query, video ID, or channel ID")
    parser.add_argument("--limit", type=int, default=10, help="Max results for search (default: 10)")
    parser.add_argument(
        "--order",
        choices=["relevance", "date", "rating", "viewCount", "title"],
        default="relevance",
        help="Sort order for search (default: relevance)",
    )
    parser.add_argument("--api-key", help="API key override")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.command == "search":
        result = search_videos(args.query, max_results=args.limit, order=args.order, api_key=args.api_key)
    elif args.command == "video":
        result = get_video_details(args.query, api_key=args.api_key)
    elif args.command == "channel":
        result = get_channel_info(args.query, api_key=args.api_key)

    if result.get("error"):
        print(f"Error: {result['error']}", file=sys.stderr)
        if not args.json:
            sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if args.command == "search":
            print(f"=== YouTube Search: {args.query} ===")
            print(f"Results: {result.get('total_results', 0):,}")
            for i, v in enumerate(result.get("videos", []), 1):
                print(f"\n  {i}. {v['title']}")
                print(f"     {v['channel']} | {v['views']:,} views | {v['likes']:,} likes | {v['duration']}")
                print(f"     {v['url']}")
        elif args.command == "video":
            d = result.get("details", {})
            if d:
                print(f"=== {d.get('title')} ===")
                print(f"Channel: {d.get('channel')}")
                print(f"Views: {d.get('views', 0):,} | Likes: {d.get('likes', 0):,} | Comments: {d.get('comments_count', 0):,}")
                print(f"Published: {d.get('published', '')[:10]} | Duration: {d.get('duration')}")
                tags = d.get("tags", [])
                if tags:
                    print(f"Tags: {', '.join(tags[:10])}")
                comments = result.get("comments", [])
                if comments:
                    print(f"\nTop Comments ({len(comments)}):")
                    for c in comments[:5]:
                        print(f"  [{c['likes']} likes] {c['author']}: {c['text'][:100]}")
        elif args.command == "channel":
            ch = result.get("channel", {})
            if ch:
                print(f"=== {ch.get('title')} ===")
                print(f"Subscribers: {ch.get('subscribers', 0):,} | Videos: {ch.get('videos', 0):,} | Views: {ch.get('views', 0):,}")


if __name__ == "__main__":
    main()
```

## File: `skills/seo/SKILL.md`
```markdown
---
name: seo
description: >
  Comprehensive SEO analysis for any website or business type. Performs full site
  audits, single-page deep analysis, technical SEO checks (crawlability, indexability,
  Core Web Vitals with INP), schema markup detection/validation/generation, content
  quality assessment (E-E-A-T framework per Dec 2025 update extending to all
  competitive queries), image optimization, sitemap analysis, and Generative Engine
  Optimization (GEO) for AI Overviews, ChatGPT, and Perplexity citations. Analyzes
  AI crawler accessibility (GPTBot, ClaudeBot, PerplexityBot), llms.txt compliance,
  brand mention signals, and passage-level citability. Industry detection for SaaS,
  e-commerce, local business, publishers, agencies. Triggers on: "SEO", "audit",
  "schema", "Core Web Vitals", "sitemap", "E-E-A-T", "AI Overviews", "GEO",
  "technical SEO", "content quality", "page speed", "structured data".
user-invokable: true
argument-hint: "[command] [url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Agent
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# SEO: Universal SEO Analysis Skill

**Invocation:** `/seo $1 $2` where `$1` is the command and `$2` is the URL or argument.

**Scripts:** Located at the plugin root `scripts/` directory.

Comprehensive SEO analysis across all industries (SaaS, local services,
e-commerce, publishers, agencies). Orchestrates 15 specialized sub-skills and 10 subagents
(+ 2 optional extension sub-skills: seo-dataforseo and seo-image-gen).

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel subagent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo sitemap <url or generate>` | Analyze or generate XML sitemaps |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo images <url>` | Image optimization analysis |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <business-type>` | Strategic SEO planning |
| `/seo programmatic [url\|plan]` | Programmatic SEO analysis and planning |
| `/seo competitor-pages [url\|generate]` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command] [args]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang [url]` | Hreflang/i18n SEO audit and generation |
| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |
| `/seo dataforseo [command]` | Live SEO data via DataForSEO (extension) |
| `/seo image-gen [use-case] <description>` | AI image generation for SEO assets (extension) |

## Orchestration Logic

When the user invokes `/seo audit`, delegate to subagents in parallel:
1. Detect business type (SaaS, local, ecommerce, publisher, agency, other)
2. Spawn subagents: seo-technical, seo-content, seo-schema, seo-sitemap, seo-performance, seo-visual, seo-geo
3. If Google API credentials detected (`python scripts/google_auth.py --check`), also spawn seo-google agent
4. If local business detected, also spawn seo-local agent
5. If local business detected AND DataForSEO MCP available, also spawn seo-maps agent
6. Collect results and generate unified report with SEO Health Score (0-100)
7. Create prioritized action plan (Critical -> High -> Medium -> Low)
8. **Offer PDF report**: "Generate a professional PDF report? Use `/seo google report full`"

For individual commands, load the relevant sub-skill directly.
After any analysis command completes, offer to generate a PDF report via `scripts/google_report.py`.

## Industry Detection

Detect business type from homepage signals:
- **SaaS**: pricing page, /features, /integrations, /docs, "free trial", "sign up"
- **Local Service**: phone number, address, service area, "serving [city]", Google Maps embed --> auto-suggest `/seo local` for deeper analysis
- **E-commerce**: /products, /collections, /cart, "add to cart", product schema
- **Publisher**: /blog, /articles, /topics, article schema, author pages, publication dates
- **Agency**: /case-studies, /portfolio, /industries, "our work", client logos

## Quality Gates

Read `references/quality-gates.md` for thin content thresholds per page type.
Hard rules:
- WARNING at 30+ location pages (enforce 60%+ unique content)
- HARD STOP at 50+ location pages (require user justification)
- Never recommend HowTo schema (deprecated Sept 2023)
- FAQ schema for Google rich results: only government and healthcare sites (Aug 2023 restriction); existing FAQPage on commercial sites -> flag Info priority (not Critical), noting AI/LLM citation benefit; adding new FAQPage -> not recommended for Google benefit
- All Core Web Vitals references use INP, never FID

## Reference Files

Load these on-demand as needed (do NOT load all at startup):
- `references/cwv-thresholds.md`: Current Core Web Vitals thresholds and measurement details
- `references/schema-types.md`: All supported schema types with deprecation status
- `references/eeat-framework.md`: E-E-A-T evaluation criteria (Sept 2025 QRG update)
- `references/quality-gates.md`: Content length minimums, uniqueness thresholds
- `references/local-seo-signals.md`: Local ranking factors, review benchmarks, citation tiers, GBP status
- `references/local-schema-types.md`: LocalBusiness subtypes, industry-specific schema and citation sources

Maps-specific references (loaded by seo-maps skill, not at startup):
- `references/maps-geo-grid.md`, `references/maps-gbp-checklist.md`, `references/maps-api-endpoints.md`, `references/maps-free-apis.md`

## Scoring Methodology

### SEO Health Score (0-100)
Weighted aggregate of all categories:

| Category | Weight |
|----------|--------|
| Technical SEO | 22% |
| Content Quality | 23% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| AI Search Readiness | 10% |
| Images | 5% |

### Priority Levels
- **Critical**: Blocks indexing or causes penalties (immediate fix required)
- **High**: Significantly impacts rankings (fix within 1 week)
- **Medium**: Optimization opportunity (fix within 1 month)
- **Low**: Nice to have (backlog)

## Sub-Skills

This skill orchestrates 15 specialized sub-skills (+ 2 extensions):

1. **seo-audit** -- Full website audit with parallel delegation
2. **seo-page** -- Deep single-page analysis
3. **seo-technical** -- Technical SEO (9 categories)
4. **seo-content** -- E-E-A-T and content quality
5. **seo-schema** -- Schema markup detection and generation
6. **seo-images** -- Image optimization
7. **seo-sitemap** -- Sitemap analysis and generation
8. **seo-geo** -- AI Overviews / GEO optimization
9. **seo-plan** -- Strategic planning with templates
10. **seo-programmatic** -- Programmatic SEO analysis and planning
11. **seo-competitor-pages** -- Competitor comparison page generation
12. **seo-hreflang** -- Hreflang/i18n SEO audit and generation
13. **seo-local** -- Local SEO (GBP, NAP, citations, reviews, local schema, multi-location)
14. **seo-maps** -- Maps intelligence (geo-grid, GBP audit, reviews, competitor radius)
15. **seo-google** -- Google SEO APIs (GSC, PageSpeed, CrUX, Indexing API, GA4)
16. **seo-dataforseo** -- Live SEO data via DataForSEO MCP (extension)
17. **seo-image-gen** -- AI image generation for SEO assets via Gemini (extension)

## Subagents

For parallel analysis during audits:
- `seo-technical` -- Crawlability, indexability, security, CWV
- `seo-content` -- E-E-A-T, readability, thin content
- `seo-schema` -- Detection, validation, generation
- `seo-sitemap` -- Structure, coverage, quality gates
- `seo-performance` -- Core Web Vitals measurement
- `seo-visual` -- Screenshots, mobile testing, above-fold
- `seo-geo` -- AI crawler access, llms.txt, citability, brand mention signals
- `seo-local` -- GBP signals, NAP consistency, reviews, local schema, industry-specific local factors (conditional: spawned when Local Service detected)
- `seo-maps` -- Geo-grid rank tracking, GBP audit, review intelligence, competitor radius mapping (conditional: spawned when Local Service detected AND DataForSEO MCP available)
- `seo-google` -- CWV field data, URL indexation status, organic traffic trends (conditional: spawned when Google API credentials detected)
- `seo-dataforseo` -- Live SERP, keyword, backlink, local SEO data (extension, optional)
- `seo-image-gen` -- SEO image audit and generation plan (extension, optional)

## Error Handling

| Scenario | Action |
|----------|--------|
| Unrecognized command | List available commands from the Quick Reference table. Suggest the closest matching command. |
| URL unreachable | Report the error and suggest the user verify the URL. Do not attempt to guess site content. |
| Sub-skill fails during audit | Report partial results from successful sub-skills. Clearly note which sub-skill failed and why. Suggest re-running the failed sub-skill individually. |
| Ambiguous business type detection | Present the top two detected types with supporting signals. Ask the user to confirm before proceeding with industry-specific recommendations. |
```

## File: `skills/seo/references/cwv-thresholds.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Core Web Vitals Thresholds (February 2026)

## Current Metrics

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

## Key Facts
- INP replaced FID (First Input Delay) on **March 12, 2024**. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on **September 9, 2024**. INP is the sole interactivity metric.
- Evaluation uses the **75th percentile** of real user data (field data from CrUX).
- Google assesses at the **page level** and the **origin level**.
- Core Web Vitals are a **tiebreaker** ranking signal: they matter most when content quality is similar between competitors.
- **Thresholds unchanged since original definitions**: ignore claims of "tightened thresholds" from SEO blogs.
- December 2025 core update appeared to weight **mobile CWV more heavily**.
- As of October 2025: **57.1%** desktop sites and **49.7%** mobile sites pass all three CWV.

## LCP Subparts (February 2025 CrUX Addition)

LCP can now be broken into diagnostic subparts:

| Subpart | What It Measures | Target |
|---------|------------------|--------|
| **TTFB** | Time to First Byte (server response) | <800ms |
| **Resource Load Delay** | Time from TTFB to resource request start | Minimize |
| **Resource Load Time** | Time to download the LCP resource | Depends on size |
| **Element Render Delay** | Time from resource loaded to rendered | Minimize |

**Total LCP = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay**

Use this breakdown to identify which phase is causing LCP issues.

## Soft Navigations API (Experimental)

**Chrome 139+ Origin Trial (July 2025)**: First step toward measuring CWV in SPAs.

- Addresses the long-standing SPA measurement blind spot
- Currently experimental, **no ranking impact yet**
- Detects "soft navigations" (URL changes without full page load)
- May affect future SPA CWV measurement

**Detection:** Check for SPA frameworks (React, Vue, Angular, Svelte) and warn about current CWV measurement limitations.

## Measurement Sources

### Field Data (Real Users)
- Chrome User Experience Report (CrUX)
- PageSpeed Insights (uses CrUX data)
- Search Console Core Web Vitals report

### Lab Data (Simulated)
- Lighthouse
- WebPageTest
- Chrome DevTools

> Field data is what Google uses for ranking. Lab data is useful for debugging.

## Common Bottlenecks

### LCP (Largest Contentful Paint)
- Unoptimized hero images (compress, use WebP/AVIF, add preload)
- Render-blocking CSS/JS (defer, async, critical CSS inlining)
- Slow server response (TTFB >200ms: use edge CDN, caching)
- Third-party script blocking (defer analytics, chat widgets)
- Web font loading delay (use font-display: swap + preload)

### INP (Interaction to Next Paint)
- Long JavaScript tasks on main thread (break into smaller tasks <50ms)
- Heavy event handlers (debounce, use requestAnimationFrame)
- Excessive DOM size (>1,500 elements is concerning)
- Third-party scripts hijacking main thread
- Synchronous XHR or localStorage operations
- Layout thrashing (multiple forced reflows)

### CLS (Cumulative Layout Shift)
- Images/iframes without width/height dimensions
- Dynamically injected content above existing content
- Web fonts causing layout shift (use font-display: swap + preload)
- Ads/embeds without reserved space
- Late-loading content pushing down the page

## Optimization Priority

1. **LCP**: Most impactful for perceived performance
2. **CLS**: Most common issue affecting user experience
3. **INP**: Matters most for interactive applications

## Tools

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json --output-path report.json
```

## Performance Tooling Updates (2025)

- **Lighthouse 13.0** (October 2025): Major audit restructuring with reorganized performance categories and updated scoring weights. Lighthouse is a lab tool (simulated conditions): always cross-reference with CrUX field data for real-world performance.
- **CrUX Vis** replaced the CrUX Dashboard (November 2025). The old Looker Studio dashboard was deprecated. Use [CrUX Vis](https://cruxvis.withgoogle.com) or the CrUX API directly.
- **LCP subparts** added to CrUX (February 2025): Time to First Byte (TTFB), resource load delay, resource load time, and element render delay are now available as sub-components of LCP in CrUX data.
- **Google Search Console 2025 features** (December 2025): AI-powered configuration for automated analysis. Branded vs. non-branded queries filter. Hourly data available in API. Custom chart annotations. Social channels tracking.

> **Mobile-first indexing** is 100% complete as of July 5, 2024. Google now crawls and indexes ALL websites exclusively with the mobile Googlebot user-agent. Ensure your mobile version contains all critical content, structured data, and meta tags.
```

## File: `skills/seo/references/eeat-framework.md`
```markdown
# E-E-A-T Evaluation Framework
## Updated per Google Quality Rater Guidelines: September 11, 2025
## Plus December 2025 Core Update Implications

## Overview

E-E-A-T = **E**xperience, **E**xpertise, **A**uthoritativeness, **T**rustworthiness

Trustworthiness is the most important factor. It is assessed based on the
other three signals plus direct trust indicators.

## CRITICAL: December 2025 Core Update

> **E-E-A-T now applies to ALL competitive queries, not just YMYL.**

The December 2025 core update was described as a "watershed moment" that:
- Extended E-E-A-T evaluation to virtually all competitive queries
- Made author attribution standards tighter across all categories
- Penalized anonymous or generic authorship even for non-YMYL content
- Significantly improved AI content quality detection

**Impact by industry:**
| Industry | Traffic Drops |
|----------|--------------|
| Affiliate sites | 71% average decline |
| Health/YMYL | 67% average decline |
| E-commerce | 52% average decline |

**Key takeaway:** Even entertainment and lifestyle content now requires demonstrated expertise. Generic content no longer ranks.

## YMYL (Your Money or Your Life)

Topics requiring **highest** E-E-A-T standards (but E-E-A-T now matters everywhere):
- Health and safety
- Financial advice and transactions
- Legal information
- News and current events
- **Elections and civic trust** (added Sept 2025)
- **Democratic processes** (added Sept 2025)
- Groups of people (potential for harm)

---

## Experience (Weight: 20%)

First-hand knowledge and personal involvement with the topic.

### Signals to Check
- [ ] Author has demonstrable first-hand experience with the topic
- [ ] Content includes original photos, screenshots, or data
- [ ] Case studies or real-world examples with specific details
- [ ] Personal process documentation or methodology descriptions
- [ ] Before/after results or outcome data
- [ ] Specific anecdotes that couldn't be fabricated

### Scoring
- **Strong**: Multiple first-hand experience signals, original content
- **Moderate**: Some personal experience evident
- **Weak**: Generic information, no personal touch
- **None**: Clearly AI-generated or scraped content

---

## Expertise (Weight: 25%)

Formal qualifications, training, and demonstrated knowledge.

### Signals to Check
- [ ] Author credentials relevant to topic (bio, certifications)
- [ ] Technical accuracy and depth appropriate for audience
- [ ] Claims supported by evidence or sources
- [ ] Specialized vocabulary used correctly
- [ ] Up-to-date with current developments in the field
- [ ] Byline with author name and credentials visible

### Scoring
- **Strong**: Verified credentials, deep technical accuracy
- **Moderate**: Demonstrable knowledge, some credentials
- **Weak**: Surface-level information, no credentials
- **None**: Factual errors, misinformation

---

## Authoritativeness (Weight: 25%)

Recognition by others as a go-to source.

### Signals to Check
- [ ] Site recognized as authority in its niche
- [ ] Author recognized as expert (external citations, speaking, publications)
- [ ] Content cited by other authoritative sources
- [ ] Industry awards, certifications, or accreditations
- [ ] Consistent publication history in the topic area
- [ ] Featured in reputable media outlets
- [ ] Professional affiliations

### Scoring
- **Strong**: Widely recognized authority, cited by others
- **Moderate**: Growing recognition, some external validation
- **Weak**: No external recognition
- **None**: Negative reputation, known for misinformation

---

## Trustworthiness (Weight: 30%)

The most important factor, overall reliability and transparency.

### Signals to Check
- [ ] Clear contact information (physical address, phone, email)
- [ ] Privacy policy and terms of service
- [ ] HTTPS with valid certificate
- [ ] Transparent about who creates content and why
- [ ] Customer reviews and testimonials
- [ ] Corrections and update history visible
- [ ] No deceptive practices (hidden ads, clickbait)
- [ ] Secure payment processing (for e-commerce)
- [ ] Return/refund policy visible

### Scoring
- **Strong**: Full transparency, verified business, positive reputation
- **Moderate**: Good trust signals, minor gaps
- **Weak**: Missing key trust signals
- **None**: Deceptive practices, scam indicators

---

## September 2025 QRG Updates

### AI Content Assessment
Raters now formally evaluate whether content appears AI-generated:
- AI content is **acceptable** if it demonstrates genuine E-E-A-T
- Low-quality AI content (generic, no unique value) is penalized
- The presence of AI-generated content is not inherently penalizing
- What matters: does the content provide unique value regardless of creation method?

### Markers of Low-Quality AI Content
- Generic phrasing without specificity
- Lack of original insight or unique perspective
- No first-hand experience signals
- Factual inaccuracies
- Repetitive structure across multiple pages
- No author attribution or expertise signals

### New Spam Categories
- **Expired domain abuse**: Buying expired domains for their backlinks
- **Site reputation abuse**: Using reputable site to host low-quality content
- **Scaled content abuse**: Mass-producing content without value

### AI Overview Evaluation
Raters assess quality of AI-generated summaries in search results.

### RSL 1.0 (Really Simple Licensing)
New machine-readable content licensing standard (December 2025) for AI training:
- Backed by: Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons
- Allows publishers to specify AI licensing terms
- Augments robots.txt for AI-specific permissions

---

## Experience Signals Are Critical Differentiators

The December 2025 update elevated the "Experience" dimension as a key differentiator:
- First-person narrative ("I tested this...", "In my experience...")
- Original photos and screenshots (not stock images)
- Specific examples with verifiable details
- Process documentation showing actual work done

**Why:** AI can generate expertise-sounding content but cannot fabricate genuine experience.

---

## Overall Scoring Guide

| Score | Description |
|-------|-------------|
| 90-100 | Exceptional E-E-A-T, authority site, recognized expert, full transparency |
| 70-89 | Strong E-E-A-T, demonstrated expertise, good trust signals |
| 50-69 | Moderate E-E-A-T, some signals, room for improvement |
| 30-49 | Weak E-E-A-T, minimal signals, significant gaps |
| 0-29 | Very low E-E-A-T, no visible signals, potential trust issues |

---

## Improvement Recommendations by Score

### 0-29 (Critical)
1. Add contact information and about page
2. Establish author identity with credentials
3. Implement HTTPS
4. Remove deceptive elements

### 30-49 (Major)
1. Add author bios with credentials
2. Include first-hand experience content
3. Get external citations/mentions
4. Add customer testimonials

### 50-69 (Moderate)
1. Deepen content with original research
2. Build topical authority through content clusters
3. Pursue industry recognition
4. Document processes and methodologies

### 70-89 (Minor)
1. Maintain freshness with regular updates
2. Expand author presence across platforms
3. Pursue speaking/publication opportunities
4. Add video/multimedia demonstrating expertise

### 90-100 (Maintenance)
1. Continue publishing high-quality content
2. Monitor and respond to reputation issues
3. Keep credentials and certifications current
```

## File: `skills/seo/references/local-schema-types.md`
```markdown
<!-- Updated: 2026-03-23 -->
# Local Schema Types & Industry-Specific Patterns (March 2026)

Schema is NOT a direct ranking factor (Confirmed: John Mueller, Gary Illyes). It indirectly impacts visibility through rich results (43% CTR increase, Webstix case study), better entity understanding, and AI search features.

---

## Google-Supported LocalBusiness Subtypes

### Food & Dining

| Schema Type | Use For |
|-------------|---------|
| `Restaurant` | Full-service restaurants |
| `CafeOrCoffeeShop` | Coffee shops, cafes |
| `BarOrPub` | Bars, pubs, taverns |
| `Bakery` | Bakeries |
| `FastFoodRestaurant` | Fast food, quick service |
| `IceCreamShop` | Ice cream, frozen yogurt |
| `FoodEstablishment` | Generic food (avoid if specific subtype exists) |

### Healthcare

| Schema Type | Use For |
|-------------|---------|
| `MedicalClinic` | Clinics, urgent care (eligible for rich results) |
| `Hospital` | Hospitals (eligible for rich results) |
| `Dentist` | Dental offices (eligible for rich results) |
| `Physician` | Individual doctor pages (use with Person) |
| `Optician` | Eye care, optical shops |
| `Pharmacy` | Pharmacies |
| `MedicalBusiness` | Generic medical (avoid if specific subtype exists) |

### Legal

| Schema Type | Use For | Notes |
|-------------|---------|-------|
| `LegalService` | Law firms, legal practices | **Correct type** |
| ~~`Attorney`~~ | ~~Individual attorneys~~ | **DEPRECATED by Schema.org. Use `LegalService` + `Person`** |

### Home Services

| Schema Type | Use For |
|-------------|---------|
| `Plumber` | Plumbing services |
| `Electrician` | Electrical services |
| `HVACBusiness` | Heating, ventilation, AC |
| `RoofingContractor` | Roofing |
| `GeneralContractor` | General contracting |
| `HousePainter` | Painting services |
| `Locksmith` | Locksmith services |
| `MovingCompany` | Moving services |
| `HomeAndConstructionBusiness` | Generic (avoid if specific subtype exists) |

### Real Estate

| Schema Type | Use For | Notes |
|-------------|---------|-------|
| `RealEstateAgent` | Both agents AND brokerages | No `RealEstateBrokerage` type exists |

### Automotive

| Schema Type | Use For |
|-------------|---------|
| `AutoDealer` | Sales departments |
| `AutoRepair` | Service departments |
| `AutoPartsStore` | Parts departments |

### Other Common Local Types

`AnimalShelter`, `BeautySalon`, `ChildCare`, `DaySpa`, `DryCleaningOrLaundry`, `EmergencyService`, `EmploymentAgency`, `EntertainmentBusiness`, `FinancialService`, `FireStation`, `FurnitureStore`, `GasStation`, `GolfCourse`, `GovernmentOffice`, `HealthClub`, `Hotel`, `InsuranceAgency`, `Library`, `LodgingBusiness`, `NightClub`, `PetStore`, `PoliceStation`, `PostOffice`, `RecyclingCenter`, `ShoppingCenter`, `SkiResort`, `SportsActivityLocation`, `Store`, `TouristInformationCenter`, `TravelAgency`, `VeterinaryCare`

---

## Required vs Recommended Properties

Per Google Developers documentation (updated December 10, 2025, Confirmed).

### Required (Minimum)

| Property | Type | Notes |
|----------|------|-------|
| `name` | Text | Business name, must match GBP exactly |
| `address` | PostalAddress | With streetAddress, addressLocality, addressRegion, postalCode |

### Recommended

| Property | Type | Notes |
|----------|------|-------|
| `aggregateRating` | AggregateRating | Rating summary with reviewCount |
| `geo` | GeoCoordinates | **Minimum 5 decimal places** (Confirmed, ~1.1m accuracy) |
| `openingHoursSpecification` | OpeningHoursSpecification | Standard, late-night, 24h, seasonal |
| `telephone` | Text | Must match GBP and page NAP |
| `url` | URL | Canonical URL for this location |
| `priceRange` | Text | Under 100 characters |
| `image` | URL | Business photo |
| `review` | Review | Individual reviews |
| `department` | LocalBusiness | For nested departments (auto dealers) |
| `menu` | URL or Menu | Restaurants only |
| `servesCuisine` | Text | Restaurants only |

### SAB-Specific

| Property | Type | Notes |
|----------|------|-------|
| `areaServed` | Place/GeoShape | NOT in Google's official recommended list but supported by Schema.org. Industry-recommended for SABs. Use named cities with `sameAs` links to Wikipedia/Wikidata. |

---

## Industry-Specific Schema Patterns

### Restaurant
```
Restaurant (or specific subtype)
  + Menu > MenuSection > MenuItem (name, price, nutrition, suitableForDiet)
  + ReserveAction (booking capabilities)
  + OrderAction (takeout/delivery)
  + servesCuisine, acceptsReservations
```
Note: Google Food Ordering (GFO) direct checkout discontinued June 2024. "Order Online" button now redirects to third-party platforms.

### Healthcare
```
MedicalClinic (or Hospital, Dentist)
  + Physician pages: Person + medicalSpecialty + hospitalAffiliation + hasCredential
  + MedicalSpecialty (helps match "hip replacement surgery" to relevant pages)
  + sameAs: link to NPI Registry entry and medical board page
```
**HIPAA constraint**: Cannot confirm/deny reviewer is a patient in review responses. Fine precedent: $30,000 (Manasa Health Center, 2023).

### Legal
```
LegalService (NOT Attorney -- deprecated)
  + Person on attorney bio pages: jobTitle, worksFor, alumniOf, hasCredential (bar admissions)
  + makesOffer > Service (one per practice area)
  + Practitioner GBP: unique phone per attorney, not sole lawyer at firm
```
Note: Reviews follow practitioner listing when attorney changes firms.

### Home Services
```
Specific subtype (Plumber, Electrician, etc.)
  + areaServed: named cities with sameAs to Wikipedia/Wikidata
  + Service on individual service pages, linked via provider
  + hasOfferCatalog for service listings
```
**SAB note**: Service area in GBP does NOT currently impact rankings -- rankings based on verification address (Sterling Sky, March 2025).

### Real Estate
```
RealEstateAgent (for both agent and brokerage)
  + Person on agent pages: memberOf (brokerage), credentials
  + RealEstateListing + SingleFamilyResidence/Apartment + Offer (pricing)
  + Event for open houses with organizing agent
```
Note: No `RealEstateBrokerage` type exists on Schema.org.

### Automotive
```
AutoDealer (sales)
  + Car/Vehicle: VIN, mileage, fuelType, vehicleTransmission
  + Offer: price, priceCurrency, availability
  + Separate GBP: AutoRepair (service), AutoPartsStore (parts)
```
**VehicleListing deprecated June 12, 2025** (Confirmed). Use Car + Offer instead. Feed-based Vehicle Listings via Google Merchant Center still functional.

---

## Industry-Specific Citation Sources

### Restaurant
Yelp, TripAdvisor (1B+ reviews), OpenTable (DA + bookings), DoorDash, UberEats, Grubhub, Foursquare (powers Apple Maps, Uber)

### Healthcare
Healthgrades (50% of Americans who see a doctor visit), Zocdoc (booking + lead gen), WebMD physician directory (high DA), Vitals, Doximity (80% of US physicians), NPI Registry (entity verification source of truth), state medical board directories

### Legal
FindLaw (DA~91, dofollow), Martindale-Hubbell (DA~84, peer review since 1868), Avvo (1-10 ratings, auto-created from bar data), Justia (DA~70, free profiles), Super Lawyers (top 5%, selection-based), state bar directories (entity verification)

Note: Internet Brands (KKR) owns Avvo + Martindale + Lawyers.com + Nolo. Thomson Reuters owns FindLaw + Super Lawyers + LawInfo.

### Home Services
Thumbtack ($400M revenue 2024, integrations with ChatGPT/Alexa/Zillow), BBB, Nextdoor, Yelp. **Declining**: Angi (revenue -30% from 2022 peak), Porch (pivoted to insurance), Houzz (pivoted to SaaS)

### Real Estate
Zillow (44% of all RE search traffic, integrated into ChatGPT Oct 2025), Homes.com (#2, overtook Realtor.com, 100M monthly visitors), Realtor.com, Redfin (acquired by Rocket Companies Mar 2025), local MLS sites

### Automotive
Cars.com, AutoTrader, CarGurus, DealerRater (reviews syndicate to Cars.com + OEM sites, supports salesperson ratings), Edmunds, Kelley Blue Book (pricing authority), OEM manufacturer dealer locators (entity verification)

---

## Multi-Location Schema Pattern

```json
// Homepage: Organization with branchOf references
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#org",
  "name": "Brand Name",
  "url": "https://example.com"
}

// Each location page: individual LocalBusiness
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "@id": "https://example.com/locations/downtown/#location",
  "name": "Brand Name - Downtown",
  "branchOf": { "@id": "https://example.com/#org" },
  "address": { ... },
  "geo": { "latitude": "40.71234", "longitude": "-74.00567" },
  "telephone": "+1-555-123-4567",
  "openingHoursSpecification": [ ... ]
}
```

Use `@id` for unique identifiers per location. Subdirectory structure recommended: `domain.com/locations/city-name/` (subdirectory consolidates link equity better than subdomain, Bruce Clay study: 50%+ traffic lift).

---

## Deprecated/Invalid Local Schema

| Type | Status | Date | Use Instead |
|------|--------|------|-------------|
| `Attorney` | Deprecated by Schema.org | -- | `LegalService` + `Person` |
| `VehicleListing` | Rich results removed | June 12, 2025 | `Car` + `Offer` |
| `HowTo` | Rich results removed | September 2023 | None |
| `SpecialAnnouncement` | Deprecated | July 31, 2025 | None |
```

## File: `skills/seo/references/local-seo-signals.md`
```markdown
<!-- Updated: 2026-03-23 -->
# Local SEO Ranking Signals & Benchmarks (March 2026)

## Source Key

- **Confirmed**: Google official documentation or employee statements
- **Study**: Data-driven industry research from recognized firms
- **Consensus**: Practitioner agreement without controlled testing
- **Caution**: Single-source or unverified claims

---

## Whitespark 2026 Local Search Ranking Factors

Published November 6, 2025. 47 experts surveyed across 187 factors. (Study)

### Local Pack/Maps Factor Groups

| Factor Group | Weight | Trend |
|---|---|---|
| GBP Signals | **32%** | Stable (top group) |
| Review Signals | **~20%** | Up from ~16% in 2023 |
| On-Page Signals | ~15-19% | Slight decline |
| Link Signals | Declining | Continued multi-year drop |
| Behavioral/Engagement | Rising | Clicks, calls, direction requests |
| Citation Signals | Lower for Pack | But 3 of top 5 AI visibility factors are citation-related |
| Social Signals | New entry | First time measured |
| AI Search Signals | New category | Added for the first time |

### Top 15 Individual Local Pack Factors

1. Primary GBP category (score: 193)
2. Keywords in GBP business title (score: 181)
3. Proximity of address to search point (score: 176)
4. Verified GBP
5. Business open at time of search (Sterling Sky controlled study)
6. High numerical Google ratings
7. Quantity of native Google reviews
8. Additional GBP categories
9. Review recency/velocity
10. Dedicated service pages
11. Domain authority
12. NAP consistency
13. Spam listing removal
14. Quality backlinks
15. Review sentiment

### Top Negative Factors

1. Incorrect primary category (score: 176) -- single worst mistake
2. Duplicate profiles at same address (score: 142)

---

## Search Atlas ML Study (August 2025)

XGBoost regression model, explains 92-93% of variance. (Study)

| Factor | Variance Explained |
|--------|-------------------|
| Proximity | **55.2%** |
| Review Count | **19.2%** |
| Domain Power | 5.9% |
| Semantic Relevance in Reviews | 5.3% |
| All others | <5% each |

---

## Review Benchmarks

### Sterling Sky Findings (2025, Study)

- **Magic 10 threshold**: Significant ranking boost at 10 reviews. 9-to-10 = noticeable increase. 10-to-11 = no similar bump.
- **18-Day Rule**: Rankings "fall off a cliff" if no new reviews for 3 weeks. Velocity > volume.

### BrightLocal LCRS 2026 (February 2026, Study)

| Metric | Value |
|--------|-------|
| Only care about reviews in last 3 months | 74% |
| "Always" read reviews | 41% (up from 29% in 2025) |
| Only use 4.5+ stars | 31% (up from 17% in 2025) |
| Only use 4+ stars | 68% (up from 55% in 2025) |
| Consumers use average review sites | 6 platforms |

### Review Platform Usage (BrightLocal 2026)

| Platform | Usage | Trend |
|----------|-------|-------|
| Google | 71% | Down from 83% in 2025 |
| Instagram | 37% | Rising |
| TikTok | 29% | Rising |
| Apple Maps | 27% | Up from 14% in 2025 |

### Enforcement

- Google blocked/removed **240M+ policy-violating reviews** in 2024 (Confirmed, 40% increase over 2023)
- Review deletion rates up **600%+** Jan-Jul 2025; 38% of deleted were 5-star (Study, GMBapi.com)
- FTC Consumer Review Rule effective Oct 21, 2024: penalties up to **$53,088/violation** (Confirmed, US law)
- **Review gating prohibited** by both Google (fake engagement policy) and FTC (Confirmed)

---

## Citation Source Tiers

### Tier 1 (Universal, All Industries)

| Source | Why It Matters |
|--------|---------------|
| Google Business Profile | Primary local signal source |
| Apple Business Connect | Usage nearly doubled, from 14% to 27% (BrightLocal 2026). 1B+ iPhone users |
| Bing Places | Overhauled Oct 2025. Powers ChatGPT, Copilot, Alexa. 900M queries/day |
| Facebook | Social + citation signal |
| Yelp | Still ranks on page 1 for many local queries |

### Tier 2 (Broad Directories)

BBB, YellowPages, Manta, Superpages, Foursquare, Nextdoor

### Tier 3 (Data Aggregators)

| Aggregator | Partnerships |
|-----------|-------------|
| Data Axle (formerly Infogroup) | Google, Bing, Apple |
| Foursquare | Merged with Factual. Powers Uber, Nextdoor, Yahoo, ChatGPT. 500M+ devices |
| Neustar/TransUnion Digital | 80+ platform partnerships including Bing, Apple |

### Industry-specific directories: see `local-schema-types.md`

---

## GBP Feature Status (March 2026)

### Deprecated/Removed

| Feature | Date | Replacement |
|---------|------|------------|
| Q&A section | Dec 3, 2025 | Ask Maps (Gemini AI) |
| GBP Messaging/Chat | Removed | None |
| Call History/Tracking | Jul 31, 2024 | None |
| GBP-hosted websites | Discontinued | Redirect to social/website |
| School reviews/ratings | Apr 30, 2025 | None |

### Active Features

Posts (with scheduling), Services menu, Attributes (including identity: Women-led, Eco-friendly), Photos/Video, Local Lists (Local Gems, Trending, Top List), AI-generated "Suggest Description", Google Verified badge (replaced Guaranteed/Screened Oct 2025)

### Key GBP Insights

- **Posts**: No direct ranking impact (WebFX empirical testing). Can trigger Post Justifications. (Study)
- **Photos**: "Likely a ranking benefit adding some vs none, but not continued benefit adding more" (WebFX). Geotagging has NO impact. 45% more direction requests with photos. (Study/Confirmed mix)
- **Attributes**: Identity attributes have minor, targeted impact for attribute-specific searches only (WebFX/Sterling Sky). General attributes are filter/informational, NOT direct ranking factors. (Study)

---

## Algorithm Updates Affecting Local (2025-2026)

| Update | Date | Impact | Source |
|--------|------|--------|--------|
| March 2025 Core | Mar 13-27 | Emphasized E-E-A-T, penalized thin/AI content | Confirmed |
| June 2025 Core | Jun-Jul 17 | General quality focus | Confirmed |
| August 2025 Spam | Aug 26-Sep 22 | Targeted keyword stuffing, fake reviews, PBNs. Local Pack often stable | Confirmed |
| December 2025 Core | Dec 11-29 | Enhanced E-E-A-T, behavioral signal weighting | Confirmed |
| February 2026 Discover Core | Feb 5-27 | Discover-only; favored local expertise | Confirmed |
| "Diversity Update" | 2025 | Harder to rank in both map pack AND organic simultaneously | Study (Sterling Sky) |

---

## Voice Search & Assistants

- 58% of voice searches are for local business information (Study, BusinessDasher)
- Voice queries typically 4-7 words, phrased as complete questions (Consensus)
- 80%+ of Google Assistant voice answers come from top 3 search results (Study)

| Voice Assistant | Primary Data Source |
|-----------------|-------------------|
| Google Assistant | GBP (transitioning to Gemini) |
| Siri (Apple) | Apple Business Connect + Yelp |
| Alexa (Amazon) | Bing Places + Yelp + aggregators |

---

## AI Search Impact on Local

| Metric | Value | Source |
|--------|-------|--------|
| ChatGPT/AI for local recommendations | 45% of users (up from 6%) | BrightLocal LCRS 2026 |
| ChatGPT conversion rate | 15.9% | Seer Interactive |
| Google organic conversion rate | 1.76% | Seer Interactive |
| AI Overviews on local searches | Up to 68% | Whitespark Q2 2025 |
| AI Overview CTR reduction for pos 1 | -58% | Ahrefs, Feb 2026 |
| Brand cited in AIO = organic CTR boost | +35% | Seer Interactive |
| ChatGPT traffic vs Google for local | ~2% | Sterling Sky, Feb 2026 |
| Top 5 AI visibility factors: 3 are citation-related | -- | Whitespark 2026 |

**ChatGPT sources**: Bing web index (primary), Yelp, TripAdvisor, BBB, Reddit. Does NOT access GBP directly. (Study, Search Engine Land)

**Perplexity sources**: Authority-first. 40% more from high-authority sites. Averages 21.87 citations per question. (Study, Qwairy)

---

## Local Pack Structure

- Standard: **3 results** (universal)
- New: Curated Local Lists (Local Gems, Trending) around position 4 (SOCi, Nov 2025)
- AI-powered local packs (mobile US): Only 1-2 businesses, 32% fewer businesses shown (Sterling Sky)
- Local pack ads grew from ~1% to **22%** of tracked mobile keywords in 12 months (Sterling Sky/Places Scout)
- Zero-click rate for local-intent searches: up to **78%** on mobile (Similarweb)

---

## Proximity & Search Behavior

- 46% of all Google searches seek local information (Study)
- 76% of mobile "near me" searches lead to visit within 24 hours (Confirmed, Google)
- 900% increase in "near me" searches over two years (Confirmed/Study, Google)
- Proximity varies: urban 1-2 miles, rural 5-10+ miles, specialty/niche = wider (Consensus)
- Google uses dynamic weighting per query: "emergency plumber near me" = proximity-dominant; "best plastic surgeon" = prominence-dominant (Consensus)
```

## File: `skills/seo/references/maps-api-endpoints.md`
```markdown
<!-- Updated: 2026-03-23 -->
# DataForSEO Maps & Business Data API Endpoints

## Source Key

- **Docs**: docs.dataforseo.com (official API documentation)
- **Pricing**: dataforseo.com/pricing (official pricing pages)

---

## Authentication & Limits

- HTTP Basic Auth (login:password)
- Rate limit: **2,000 API calls/minute** across all endpoints
- Each POST supports up to **100 tasks** in a single request
- Minimum deposit: $50. $1 free trial credit. Credits never expire.

---

## Google Maps SERP API (Geo-Grid Backbone)

**Endpoint:** `POST https://api.dataforseo.com/v3/serp/google/maps/live/advanced`
**Pricing source:** https://dataforseo.com/pricing/serp-api

### Request Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `keyword` | Yes | Search query (e.g., "dentist") |
| `location_name` | No | Named location (e.g., "Austin,Texas,United States") |
| `location_code` | No | DataForSEO location code (e.g., 1026339 for Austin) |
| `location_coordinate` | No | `"latitude,longitude,zoom"` (max 7 decimals, zoom 3z-21z) |
| `language_code` | No | Default: "en" |
| `device` | No | "desktop" or "mobile" |
| `depth` | No | Number of results to return |

**Critical for geo-grid:** Use `location_coordinate` to simulate searches from specific GPS points. Format: `"40.7128,-74.0060,15z"`.

### Response Fields (per business item)

`cid`, `place_id`, `feature_id`, `title`, `domain`, `url`, `category`, `additional_categories`, `address`, `phone` (via `contact_info` array), `rating.value`, `rating.votes_count`, `rating.rating_distribution` (1-5 star breakdown), `price_level`, `attributes` (grouped: accessibility, payments, children), `work_time` (per-day timetable + `current_status`), `popular_times` (hourly by day), `latitude`, `longitude`, `local_business_links` (booking, menu, order URLs)

### Pricing

| Method | Cost per task | Turnaround |
|--------|--------------|------------|
| Standard | $0.0006 (100 desktop / 20 mobile results) | Up to 5 min |
| Priority | $0.0012 | Up to 1 min |
| **Live** | **$0.002** | Up to 6 sec |

Search operators in keyword multiply cost by 5x.

---

## Google My Business Info API (Single Business Deep-Dive)

**Endpoint:** `POST https://api.dataforseo.com/v3/business_data/google/my_business_info/live`
**Pricing source:** https://dataforseo.com/pricing/business-data

### Input Options

- `keyword`: Business name + location (e.g., "Starbucks Austin TX")
- `"cid:XXXX"`: Direct CID lookup
- `"place_id:XXXX"`: Direct Place ID lookup

### Response Fields

Full profile: `title`, `description`, `category`, `additional_categories`, `category_ids`, `attributes` (available + unavailable, grouped by type), `contact_info` (phone array), `domain`, `url`, `work_hours` (per-day with open/close times), `popular_times`, `cid`, `place_id`, `rating` (with distribution), `address_info` (full breakdown), `latitude`/`longitude`, `photos_count`, `main_image`

**Cost:** $0.0015 per profile (standard queue)

**Use case:** Deep-dive on the TARGET business. Maps SERP for competitor discovery.

---

## Google Reviews API (Sentiment & Velocity)

**Endpoint:** `POST https://api.dataforseo.com/v3/business_data/google/reviews/task_post`
**Pricing source:** https://dataforseo.com/pricing/business-data

### Parameters

| Parameter | Description |
|-----------|-------------|
| `keyword` | Business name + location (or CID/place_id) |
| `depth` | Number of reviews to retrieve |
| `sort_by` | `"highest_rating"`, `"lowest_rating"`, `"most_relevant"`, `"newest"` |

### Response Fields (per review)

`review_text`, `original_review_text`, `time_ago`, `timestamp`, `rating.value`, `review_id`, `profile_name`, `profile_url`, `profile_image_url`, `owner_answer` (text + timestamp), `review_images`

### Pricing

| Method | Input Type | Cost |
|--------|-----------|------|
| Standard (per 10 reviews) | keyword | $0.003 |
| Extended (per 20 reviews) | keyword | $0.003 |
| Extended (per 20 reviews) | place_id/CID | **$0.00075** |

**Optimization:** Always use `place_id` or `cid` input (4x cheaper than keyword).

---

## Google Q&A API

**Endpoint:** `POST https://api.dataforseo.com/v3/business_data/google/questions_and_answers/live`

Returns questions, answers, upvotes, dates, answer sources. Live and standard methods available.

**Use case:** Identify unanswered questions, FAQ gap analysis.

**Note:** Google deprecated GBP Q&A in Dec 2025 (replaced by Ask Maps Gemini AI). This endpoint returns historical data.

---

## Business Listings Search (Pre-Indexed Database)

**Endpoint:** `POST https://api.dataforseo.com/v3/business_data/business_listings/search/live`

Queries DataForSEO's pre-indexed database (not live Google). Faster for bulk category-based queries. Up to 700+ results per query.

**Categories Aggregation:** `/v3/business_data/business_listings/categories_aggregation/live` provides category taxonomy.

**MCP tool name:** `business_data_business_listings_search`

---

## Cross-Platform Review APIs

### Tripadvisor

- Search: `/v3/business_data/tripadvisor/search/task_post`
- Reviews: `/v3/business_data/tripadvisor/reviews/task_post`
- Billed per 30 reviews. Standard method only.

### Trustpilot

- Search: `/v3/business_data/trustpilot/search/task_post`
- Reviews: `/v3/business_data/trustpilot/reviews/task_post`
- ~$0.00075/task. Standard method only.

---

## Cost Estimation Table

| Operation | API Calls | Est. Cost (Live) |
|-----------|-----------|-----------------|
| 7x7 geo-grid, 1 keyword | 49 | $0.098 |
| 7x7 geo-grid, 3 keywords | 147 | $0.294 |
| 3x3 geo-grid, 1 keyword | 9 | $0.018 |
| Target business profile | 1 | $0.0015 |
| 100 reviews (via place_id) | 5 | $0.00375 |
| 20 competitor profiles | 20 | $0.03 |
| GBP posts audit | 1 | ~$0.002 |
| Q&A retrieval | 1 | ~$0.002 |
| **Full audit (1-keyword grid)** | **~73** | **~$0.13** |
| **Full audit (3-keyword grid)** | **~171** | **~$0.33** |

**Formula:** `grid_size^2 x keywords x $0.002` (live) or `x $0.0006` (standard)
```

## File: `skills/seo/references/maps-free-apis.md`
```markdown
<!-- Updated: 2026-03-23 -->
# Free Maps APIs for claude-seo

## Source Key

- **Docs**: Official API documentation for each service
- **Policy**: Official usage policies and terms

---

## Overpass API (Best Free Option for Competitor Discovery)

**Base URL:** `https://overpass-api.de/api/interpreter`
**Docs:** https://wiki.openstreetmap.org/wiki/Overpass_API
**License:** ODbL (attribution required: "Data from OpenStreetMap")

### Rate Limits

- Slot-based: ~2 concurrent queries per IP
- Guideline: ~10,000 requests/day, ~1 GB/day download
- Default timeout: 180 seconds, 512 MiB memory per query
- Use `[timeout:25]` for lighter queries

### Query Templates

**Restaurants within 5km radius:**
```bash
curl -s "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:25];(node["amenity"="restaurant"](around:5000,LAT,LNG);way["amenity"="restaurant"](around:5000,LAT,LNG););out body;>;out skel qt;'
```

**All businesses on a street:**
```bash
curl -s "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:25];way["name"="STREET_NAME"]["addr:city"="CITY"];(._;>;);out body;'
```

**Competitor POIs by category in bounding box:**
```bash
curl -s "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:25];(node["amenity"="dentist"](SOUTH,WEST,NORTH,EAST);way["amenity"="dentist"](SOUTH,WEST,NORTH,EAST););out body;>;out skel qt;'
```

### Key OSM Tags for Local SEO

| Category | OSM Tag | Examples |
|----------|---------|---------|
| Food & Drink | `amenity=restaurant`, `amenity=cafe`, `amenity=fast_food` | Restaurants, cafes, takeaway |
| Healthcare | `amenity=dentist`, `amenity=doctors`, `amenity=pharmacy` | Dental, medical, pharmacy |
| Legal | `office=lawyer`, `office=notary` | Law firms, notaries |
| Home Services | `craft=plumber`, `craft=electrician`, `craft=hvac` | Trades, contractors |
| Retail | `shop=supermarket`, `shop=clothes`, `shop=car` | All retail types |
| Automotive | `shop=car`, `shop=car_repair`, `amenity=fuel` | Dealers, repair, gas |
| Hospitality | `tourism=hotel`, `tourism=motel`, `tourism=guest_house` | Accommodation |
| Financial | `amenity=bank`, `office=insurance`, `office=accountant` | Banks, insurance, accounting |

### Response Fields

Each element returns: `id`, `lat`, `lon`, `tags` object containing `name`, `phone`, `website`, `opening_hours`, `addr:street`, `addr:housenumber`, `addr:city`, `addr:postcode`, `cuisine`, `brand`, etc.

### Limitations

- No reviews, ratings, or popularity data
- No GBP-specific information
- Data quality varies by region (excellent in Europe, inconsistent elsewhere)
- Volunteer-contributed data; may be outdated
- Interactive tester: https://overpass-turbo.eu/

---

## Geoapify Places API (Structured POI Search)

**Base URL:** `https://api.geoapify.com/v2/places`
**Docs:** https://apidocs.geoapify.com/brain/knowledge/docs_legacy/places/
**Pricing:** https://www.geoapify.com/pricing

### Free Tier

- **3,000 credits/day** (1 credit = 20 places returned)
- 5 requests/second
- Requires API key (free registration, no credit card)
- **Caching and storage explicitly permitted** (unlike Google)

### Query Template

```bash
curl -s "https://api.geoapify.com/v2/places?categories=catering.restaurant&filter=circle:LNG,LAT,5000&limit=20&apiKey=YOUR_KEY"
```

### Category Hierarchy

Uses dot-separated categories: `catering.restaurant`, `commercial.supermarket`, `healthcare.dentist`, `service.financial.accounting`, `commercial.vehicle.car_dealer`

### Response Format

GeoJSON FeatureCollection. Each feature has `properties`: `name`, `city`, `state`, `postcode`, `country`, `street`, `housenumber`, `phone`, `website`, `categories`, `lat`, `lon`, `place_id`, `formatted` (full address string)

### Advantages Over Raw Overpass

- Cleaner, structured responses
- Aggregated data (OSM + OpenAddresses + WhosOnFirst + GeoNames)
- Hierarchical category taxonomy
- No rate limit surprises (clear credit system)

---

## Nominatim (Geocoding Only)

**Base URL:** `https://nominatim.openstreetmap.org`
**Docs:** https://nominatim.org/release-brain/knowledge/docs_legacy/latest/api/Overview/
**Policy:** https://operations.osmfoundation.org/policies/nominatim/

### Rate Limits (STRICT)

- **1 request/second** (absolute)
- Must include valid `User-Agent` header (stock library agents rejected)
- Auto-complete queries **forbidden**
- Bulk geocoding **forbidden** on public instance
- Repeated identical queries trigger bans (cache results)

### Forward Geocoding

```bash
curl -s "https://nominatim.openstreetmap.org/search?q=123+Main+St+Austin+TX&format=json&addressdetails=1" \
  -H "User-Agent: claude-seo/1.7.0"
```

### Reverse Geocoding

```bash
curl -s "https://nominatim.openstreetmap.org/reverse?lat=40.7128&lon=-74.0060&format=json" \
  -H "User-Agent: claude-seo/1.7.0"
```

### Response Fields

`place_id`, `lat`, `lon`, `display_name`, `importance`, `category`, `type`, `address` object (house_number, road, city, state, postcode, country)

### Best Use

- Address-to-coordinates conversion for geo-grid center point
- Reverse geocoding to validate business addresses
- **NOT suitable** for business listing discovery (use Overpass or Geoapify)

---

## Rate Limit Enforcement Pattern

```bash
# Nominatim: enforce 1 req/sec with sleep
for addr in "${addresses[@]}"; do
  curl -s "https://nominatim.openstreetmap.org/search?q=${addr}&format=json" \
    -H "User-Agent: claude-seo/1.7.0"
  sleep 1.1
done

# Overpass: no explicit rate limit, but use reasonable timeouts
# If HTTP 429 returned, implement exponential backoff

# Geoapify: 5 req/sec on free tier, no explicit enforcement needed
```

---

## Comparison Table

| Feature | Overpass | Geoapify | Nominatim |
|---------|---------|----------|-----------|
| Business discovery | Yes (tags) | Yes (categories) | Limited |
| Reviews/ratings | No | No | No |
| Geocoding | No | Yes | **Best** |
| Rate limit | ~10k/day | 3k credits/day | 1 req/sec |
| Auth required | No | API key | No |
| Caching allowed | Yes | **Explicitly** | **Required** |
| Data quality | Regional | Aggregated | Regional |
| Best for | Radius competitor search | Structured POI search | Address resolution |
```

## File: `skills/seo/references/maps-gbp-checklist.md`
```markdown
<!-- Updated: 2026-03-23 -->
# GBP Profile Completeness Checklist (Via API)

This checklist scores a Google Business Profile using data retrieved from
the DataForSEO My Business Info API. It measures profile completeness on
the maps PLATFORM, not on-page signals (seo-local handles on-page).

## Sources

- Google official: https://support.google.com/business/answer/7091
- Whitespark 2026 Local Search Ranking Factors (Study)
- BrightLocal LCRS 2026 (Study)

---

## Scoring System

Each field: **Present + Optimized = 2pts**, **Present = 1pt**, **Missing = 0pts**

Total possible: 50 points. Normalize to 0-100 scale: `(score / 50) * 100`

---

## Critical Fields (Direct Ranking Impact)

| # | Field | Points | Optimized Criteria |
|---|-------|--------|-------------------|
| 1 | **Primary category** | 2 | Most specific subtype for industry (e.g., "Cosmetic Dentist" not "Dentist") |
| 2 | **Additional categories** | 2 | 3-5 relevant categories (optimal: 4 additional per BrightLocal) |
| 3 | **Business name** | 2 | Matches real-world name exactly (no keyword stuffing) |
| 4 | **Physical address** | 2 | Complete, matches website NAP |
| 5 | **Phone number** | 2 | Local number (not toll-free), matches website |
| 6 | **Website URL** | 2 | Points to correct page (not strongest page -- Diversity Update risk) |
| 7 | **Business hours** | 2 | Complete with special/holiday hours. Open-at-search-time = factor #5 |
| 8 | **Verified status** | 2 | Google Verified badge active |

**Subtotal: 16 points (8 fields)**

---

## Important Fields (Significant Influence)

| # | Field | Points | Optimized Criteria |
|---|-------|--------|-------------------|
| 9 | **Business description** | 2 | 250-750 chars, includes primary service + location keywords naturally |
| 10 | **Services list** | 2 | All core services listed with descriptions |
| 11 | **Products** | 2 | Key products/services with prices (if applicable) |
| 12 | **Photos** | 2 | 10+ photos across types: logo, cover, interior, exterior, team, products |
| 13 | **Photo recency** | 2 | Photos uploaded within last 30 days |
| 14 | **Attributes** | 2 | Relevant attributes set (accessibility, payments, amenities, identity) |
| 15 | **Service areas** | 2 | Defined for SABs, up to 20 areas (cities or zip codes) |
| 16 | **Menu/services link** | 2 | Menu URL (restaurants) or services URL (others) |

**Subtotal: 16 points (8 fields)**

---

## Supplementary Fields (Supporting Signals)

| # | Field | Points | Optimized Criteria |
|---|-------|--------|-------------------|
| 17 | **Google Posts** | 2 | Active posting (1+/week). Types: update, offer, event, product |
| 18 | **Post recency** | 2 | Post within last 7 days |
| 19 | **Booking link** | 2 | Appointment/reservation URL configured |
| 20 | **Social profiles** | 2 | Linked via `sameAs` or GBP social links |
| 21 | **Logo** | 2 | High-quality square logo uploaded |
| 22 | **Cover photo** | 2 | On-brand, high-resolution cover image |
| 23 | **Videos** | 2 | At least 1 video uploaded |
| 24 | **Owner responses** | 2 | Responding to reviews (target: 80%+ response rate) |
| 25 | **Q&A engagement** | 2 | FAQ content on website (GBP Q&A deprecated Dec 2025) |

**Subtotal: 18 points (9 fields)**

---

## Industry-Specific Weight Adjustments

When scoring, apply multipliers to fields that matter more for specific industries:

### Restaurant
- Menu/services link: **x2** (critical for food-related searches)
- Photos: **x1.5** (food photos drive engagement)
- Booking link: **x1.5** (reservation systems expected)
- Attributes: **x1.5** (dietary, dine-in/takeout/delivery critical)

### Healthcare
- Business hours: **x1.5** (patients need accurate hours)
- Attributes: **x1.5** (insurance, accessibility, telehealth)
- Services list: **x2** (insurance and procedure matching)

### Legal
- Business description: **x1.5** (practice area clarity)
- Services list: **x2** (practice area matching drives visibility)
- Photos: **x0.5** (less impactful for legal)

### Home Services
- Service areas: **x2** (SAB model depends on this)
- Business hours: **x1.5** (emergency availability)
- Photos: **x1.5** (before/after project photos)

### Real Estate
- Photos: **x2** (property photos critical)
- Social profiles: **x1.5** (agent branding)
- Posts: **x1.5** (listing updates)

### Automotive
- Products: **x2** (vehicle inventory)
- Photos: **x2** (vehicle photos)
- Services list: **x1.5** (sales + service departments)

### Re-normalization After Multipliers

After applying industry multipliers, re-normalize so the total remains 0-100:
```
final_score = (weighted_raw_score / max_possible_weighted_score) * 100
```
This ensures consistent scoring regardless of which industry multipliers are active.

---

## Score Interpretation

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Excellent | Maintain posting cadence and photo freshness |
| 75-89 | Good | Fill remaining gaps in supplementary fields |
| 50-74 | Needs Work | Missing important fields, address Critical + Important gaps |
| 25-49 | Poor | Major profile gaps hurting visibility. Prioritize Critical fields |
| 0-24 | Critical | Profile barely exists or unclaimed. Start with verification + Critical fields |

---

## Data Mapping (DataForSEO → Checklist)

| Checklist Field | DataForSEO My Business Info Field |
|----------------|----------------------------------|
| Primary category | `category` |
| Additional categories | `additional_categories` |
| Business name | `title` |
| Address | `address_info` |
| Phone | `contact_info` (type: phone) |
| Website | `domain`, `url` |
| Hours | `work_hours` |
| Description | `description` |
| Services | (separate API or attributes) |
| Photos | `photos_count`, `main_image` |
| Attributes | `attributes` (grouped by type) |
| Popular times | `popular_times` |
| Posts | My Business Updates API |
| Verified status | Not directly exposed — infer from profile completeness + Maps SERP presence, or flag as "Unknown (manual check required)" |
```

## File: `skills/seo/references/maps-geo-grid.md`
```markdown
<!-- Updated: 2026-03-23 -->
# Geo-Grid Rank Tracking Algorithm

## Concept

Geo-grid rank tracking simulates Google Maps searches from multiple GPS
coordinates around a business to show how rankings vary across a geographic
area. The output is a heatmap revealing where the business ranks well (green)
and where competitors dominate (red).

---

## Grid Generation (Haversine-Based)

### Algorithm

1. Take center coordinates (business location): `center_lat`, `center_lng`
2. Define grid size (e.g., 7x7 = 49 points) and radius in km
3. Calculate spacing: `step = (2 * radius_km) / (grid_size - 1)`
4. Generate grid points using offset formula:

```
For each row i (0 to grid_size-1) and column j (0 to grid_size-1):
  dy = (i - center_index) * step_km
  dx = (j - center_index) * step_km
  new_lat = center_lat + (dy / 111.32)
  new_lng = center_lng + (dx / (111.32 * cos(center_lat * pi/180)))
```

Where `center_index = (grid_size - 1) / 2` and `111.32 km = 1 degree latitude`.

### Grid Sizes and Use Cases

| Grid | Points | Typical Radius | Best For | Est. Cost (Live) |
|------|--------|---------------|----------|-----------------|
| 3x3 | 9 | 2 km | Quick snapshot, low budget | $0.018/keyword |
| 5x5 | 25 | 3 km | Standard urban audit | $0.050/keyword |
| **7x7** | **49** | **5 km** | **Default. Best balance of coverage and cost** | **$0.098/keyword** |
| 9x9 | 81 | 8 km | Suburban/wide service area | $0.162/keyword |
| 13x13 | 169 | 15 km | Rural or large metro | $0.338/keyword |

**Radius guidelines:** Urban dense = 2-5 km, suburban = 5-10 km, rural = 10-25 km.

---

## DataForSEO Integration

Use the Google Maps SERP API with `location_coordinate` parameter:

```json
{
  "keyword": "dentist",
  "location_coordinate": "30.2672,-97.7431,15z",
  "language_code": "en",
  "device": "mobile",
  "depth": 20
}
```

For each grid point, fire one API call with the point's lat/lng. Parse the
`items` array to find the target business rank (position in results).

**Rate optimization:** DataForSEO allows up to 100 tasks per POST. For a 7x7
grid, batch all 49 tasks into a single request to minimize HTTP overhead.

---

## Share of Local Voice (SoLV)

Metric pioneered by Local Falcon. Measures visibility across the grid.

### Calculation

```
SoLV = (points_in_top_3 / total_grid_points) * 100
```

### Interpretation

| SoLV | Interpretation |
|------|---------------|
| 80-100% | Dominant. Business owns the local area. |
| 60-79% | Strong. Visible in most of the service area. |
| 40-59% | Moderate. Significant gaps in coverage. |
| 20-39% | Weak. Competitors dominate most areas. |
| 0-19% | Critical. Nearly invisible in maps results. |

### Extended Metrics

- **Average Rank**: Mean position across all grid points (lower = better)
- **Visibility Score**: Weighted average where top 3 = 3pts, 4-10 = 1pt, 10+ = 0pts
- **Worst Quadrant**: Identify which compass direction has weakest rankings

---

## ASCII Heatmap Rendering

For terminal/Markdown output, render a grid using rank-position symbols:

### Format

```
Geo-Grid: "dentist" (7x7, 5km radius, center: 30.267, -97.743)

     W -------- E
  N  1  1  2  3  5  8  -
  |  1  1  1  2  3  6  9
  |  2  1  [1] 1  2  4  7
  |  3  2  1  1  1  3  5
  |  5  3  2  1  2  4  8
  |  8  5  3  2  3  6  -
  S  -  8  5  4  5  9  -

Legend: [1]=center, 1-3=top 3 (strong), 4-10=visible, -=not ranked
SoLV: 57% (28/49 grid points in top 3)
Avg Rank: 3.4 | Weakest: NE quadrant (avg rank 7.2)
```

### Color Mapping (for enhanced output)

| Position | Symbol | Meaning |
|----------|--------|---------|
| 1 | `1` | #1 ranking (best) |
| 2-3 | `2`, `3` | Top 3 (strong local presence) |
| 4-10 | `4`-`9` | Visible but not dominant |
| 11-20 | `+` | Buried in results |
| Not found | `-` | Not ranking at this point |

---

## Multi-Keyword Grid

For comprehensive analysis, scan 2-3 keywords on the same grid:

1. Primary service keyword (e.g., "dentist")
2. Brand + location (e.g., "Smith Dental Austin")
3. Long-tail intent (e.g., "emergency dentist near me")

**Cost for 3-keyword 7x7 scan:** 147 API calls = ~$0.29 (live) or ~$0.088 (standard)

---

## Cost Warning Template

Before running a geo-grid scan, display:

```
Geo-Grid Scan Estimate:
  Grid: 7x7 (49 points)
  Keywords: 3
  API calls: 147
  Estimated cost: $0.09 (standard) - $0.29 (live)
  Proceed? [DataForSEO credits will be consumed]
```
```

## File: `skills/seo/references/quality-gates.md`
```markdown
# Content Quality Gates

## Minimum Word Counts by Page Type

| Page Type | Min Words | Unique Content % | Notes |
|-----------|-----------|-----------------|-------|
| Homepage | 500 | 100% | Must clearly communicate value proposition |
| Service / Feature Page | 800 | 100% | Detailed explanation of offering |
| Location (Primary) | 600 | 60%+ | City headquarters or main service area |
| Location (Secondary) | 500 | 40%+ | Satellite locations |
| Blog Post | 1,500 | 100% | In-depth, valuable content |
| Product Page | 400 | 80%+ | Unique descriptions, specs |
| Category Page | 400 | 100% | Unique intro, not just product listings |
| About Page | 400 | 100% | Company story, team, values |
| Landing Page | 600 | 100% | Focused conversion content |
| FAQ Page | 800 | 100% | Comprehensive Q&A |

---

## Location Page Thresholds

### Warning Level (30+ pages)
- ⚠️ **WARNING** at 30+ location pages
- Enforce 60%+ unique content per page
- Content must include:
  - Unique local information (landmarks, neighborhoods)
  - Location-specific services or offerings
  - Local team or staff information
  - Genuine customer testimonials from that area

### Hard Stop (50+ pages)
- 🛑 **HARD STOP** at 50+ location pages
- Require explicit user justification
- Must demonstrate:
  - Legitimate business presence in each location
  - Unique content strategy for each page
  - Local signals (Google Business Profile, local reviews)

### Why This Matters
Google's doorway page algorithm penalizes programmatic location pages with thin/duplicate content. Signs of doorway pages:
- Only city/state name changed between pages
- No unique local information
- No local business signals
- Keyword-stuffed URLs

---

## Safe vs. Risky Programmatic Pages

### Safe at Scale ✅
| Page Type | Why It's Safe |
|-----------|---------------|
| Integration pages | Real setup documentation, unique technical content |
| Template/tool pages | Downloadable assets, unique functionality |
| Glossary pages | 200+ word unique definitions |
| Product pages | Unique specs, images, reviews |
| User profile pages | User-generated unique content |

### Penalty Risk ❌
| Page Type | Why It's Risky |
|-----------|----------------|
| Location pages with only city swapped | Duplicate content, doorway pages |
| "Best [tool] for [industry]" | Often thin, no industry-specific value |
| "[Competitor] alternative" | Requires genuine comparison data |
| AI-generated mass content | No unique value, E-E-A-T failure |

---

## Title Tag Requirements

| Aspect | Requirement |
|--------|-------------|
| Minimum length | 30 characters |
| Maximum length | 60 characters (Google truncates ~60) |
| Primary keyword | Near the beginning |
| Brand name | At end (if included) |
| Uniqueness | Each page must have unique title |

### Good Examples
- "Emergency Plumbing Services in Austin | ABC Plumbing"
- "How to Fix a Leaky Faucet: Step-by-Step Guide"
- "Enterprise SEO Software | Comprehensive Platform"

### Bad Examples
- "Home" (too short, not descriptive)
- "Best Plumbing Services for All Your Plumbing Needs in Austin Texas and Surrounding Areas" (too long)
- "ABC Plumbing - Plumbing - Plumber - Plumbing Services" (keyword stuffing)

---

## Meta Description Requirements

| Aspect | Requirement |
|--------|-------------|
| Minimum length | 120 characters |
| Maximum length | 160 characters (Google truncates ~155-160) |
| Call-to-action | Include compelling CTA |
| Primary keyword | Include naturally |
| Uniqueness | Each page must have unique description |

---

## Image Alt Text Requirements

| Aspect | Requirement |
|--------|-------------|
| Required on | All non-decorative images |
| Length | 10-125 characters |
| Content | Describe the image content, not "image" or filename |
| Keywords | Include naturally where relevant |
| Decorative images | Use `alt=""` or `role="presentation"` |

### Good Examples
- "Professional plumber repairing kitchen sink faucet"
- "Red 2024 Toyota Camry sedan front view"
- "Team meeting in modern office conference room"

### Bad Examples
- "image.jpg" (filename, not description)
- "plumber plumbing plumber services" (keyword stuffing)
- "Click here" (not descriptive)

---

## Internal Linking Guidelines

| Page Type | Internal Links Target |
|-----------|----------------------|
| Blog post (1,500+ words) | 5-10 internal links |
| Service page | 3-5 internal links |
| Category page | Links to all child pages |
| Product page | 2-4 internal links |

### Anchor Text Rules
- Use descriptive anchor text (not "click here")
- Vary anchor text (don't always use exact match keywords)
- Link to relevant, related content
- Ensure no orphan pages (every page linked from at least one other page)

---

## Content Freshness Signals

| Content Type | Update Frequency |
|--------------|------------------|
| News/current events | Within hours/days |
| Blog posts (evergreen) | Review annually |
| Product pages | When specs change |
| Service pages | Review quarterly |
| Company info | When changes occur |

### Required Elements
- Publication date visible (for articles/blogs)
- Last updated date (if significantly revised)
- Changelog for major updates (optional but good)
```

## File: `skills/seo/references/schema-types.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Schema.org Types: Status & Recommendations (February 2026)

**Schema.org Version:** 29.4 (December 8, 2025)

## Format Preference
Always use **JSON-LD** (`<script type="application/ld+json">`).
Google's documentation explicitly recommends JSON-LD over Microdata and RDFa.

**AI Search Note:** Content with proper schema has ~2.5× higher chance of appearing in AI-generated answers (confirmed by Google and Microsoft, March 2025).

---

## Active: Recommend freely

| Type | Use Case | Key Properties |
|------|----------|----------------|
| Organization | Company info | name, url, logo, contactPoint, sameAs |
| LocalBusiness | Physical businesses | name, address, telephone, openingHours, geo, priceRange |
| SoftwareApplication | Desktop/mobile apps | name, operatingSystem, applicationCategory, offers, aggregateRating |
| WebApplication | Browser-based SaaS | name, applicationCategory, offers, browserRequirements, featureList |
| Product | Physical/digital products | name, image, description, sku, brand, offers, review |
| Offer | Pricing | price, priceCurrency, availability, url, validFrom |
| Service | Service businesses | name, provider, areaServed, description, offers |
| Article | Blog posts, news | headline, author, datePublished, dateModified, image, publisher |
| BlogPosting | Blog content | Same as Article + blog-specific context |
| NewsArticle | News content | Same as Article + news-specific context |
| Review | Individual reviews | reviewRating, author, itemReviewed, reviewBody |
| AggregateRating | Rating summaries | ratingValue, reviewCount, bestRating, worstRating |
| BreadcrumbList | Navigation | itemListElement with position, name, item |
| WebSite | Site-level | name, url, potentialAction (SearchAction for sitelinks search) |
| WebPage | Page-level | name, description, datePublished, dateModified |
| Person | Author/team | name, jobTitle, url, sameAs, image, worksFor |
| ContactPage | Contact pages | name, url |
| VideoObject | Video content | name, description, thumbnailUrl, uploadDate, duration, contentUrl |
| ImageObject | Image content | contentUrl, caption, creator, copyrightHolder |
| Event | Events | name, startDate, endDate, location, organizer, offers |
| JobPosting | Job listings | title, description, datePosted, hiringOrganization, jobLocation |
| Course | Educational content | name, description, provider, hasCourseInstance |
| DiscussionForumPosting | Forum threads | headline, author, datePublished, text, url |
| ProductGroup | Variant products | name, productGroupID, variesBy, hasVariant |
| ProfilePage | Author/creator profiles | mainEntity (Person), name, url, description, sameAs |

---

## Restricted: Only for specific site types

| Type | Restriction | Since |
|------|------------|-------|
| FAQPage | Government and healthcare authority sites ONLY | August 2023 |

> Google severely limited FAQ rich results in August 2023. Only authoritative sources (government, health organizations) receive FAQ rich results.
>
> **GEO nuance**: FAQPage schema still benefits AI/LLM citation visibility (ChatGPT, Perplexity, Google AI Overviews), even without Google rich results.
> - **Existing FAQPage on commercial site**: Flag at Info priority, not Critical. Removal removes GEO citation upside.
> - **Adding new FAQPage**: Not recommended for Google benefit; acceptable if AI search visibility is a priority.

---

## Deprecated: Never recommend

| Type | Status | Since | Notes |
|------|--------|-------|-------|
| HowTo | Rich results fully removed | September 2023 | Google stopped showing how-to rich results |
| SpecialAnnouncement | Deprecated | July 31, 2025 | COVID-era schema, no longer processed |
| CourseInfo | Retired from rich results | June 2025 | Merged into Course |
| EstimatedSalary | Retired from rich results | June 2025 | No longer displayed |
| LearningVideo | Retired from rich results | June 2025 | Use VideoObject instead |
| ClaimReview | Retired from rich results | June 2025 | Fact-check markup no longer generates rich results |
| VehicleListing | Retired from rich results | June 2025 | Vehicle listing structured data discontinued |
| Book Actions | Deprecated then REVERSED | June 2025 | **Still functional as of Feb 2026**: historical note only |
| Practice Problem | Retired from rich results | Late 2025 | Educational practice problems no longer displayed |
| Dataset | Retired from rich results | Late 2025 | Dataset Search feature discontinued |

---

## Recent Additions (2024-2026)

| Type/Feature | Added | Notes |
|-------------|-------|-------|
| Product Certification markup | April 2025 | Energy ratings, safety certifications. Replaced EnergyConsumptionDetails. |
| ProductGroup | 2025 | E-commerce product variants with variesBy, hasVariant properties |
| ProfilePage | 2025 | Author/creator profile pages with mainEntity Person for E-E-A-T |
| DiscussionForumPosting | 2024 | For forum/community content |
| Speakable | Updated 2024 | For voice search optimization |
| LoyaltyProgram | June 2025 | Member pricing, loyalty card structured data |
| Organization-level shipping/return policies | November 2025 | Configure via Search Console without Merchant Center |
| ConferenceEvent | December 2025 | Schema.org v29.4 addition |
| PerformingArtsEvent | December 2025 | Schema.org v29.4 addition |

## E-commerce Requirements (Updated)

| Requirement | Status | Since |
|-------------|--------|-------|
| `returnPolicyCountry` in MerchantReturnPolicy | **Required** | March 2025 |
| Product variant structured data | Expanded | 2025, includes apparel, cosmetics, electronics |

> **Note:** Content API for Shopping sunsets August 18, 2026. Migrate to Merchant API.

---

## Validation Checklist

For any schema block, verify:

1. ✅ `@context` is `"https://schema.org"` (not http)
2. ✅ `@type` is a valid, non-deprecated type
3. ✅ All required properties are present
4. ✅ Property values match expected data types
5. ✅ No placeholder text (e.g., "[Business Name]")
6. ✅ URLs are absolute, not relative
7. ✅ Dates are in ISO 8601 format
8. ✅ Images have valid URLs

## Testing Tools

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
```

## File: `skills/seo-audit/SKILL.md`
```markdown
---
name: seo-audit
description: >
  Full website SEO audit with parallel subagent delegation. Crawls up to 500
  pages, detects business type, delegates to 10 specialists (7 core + 3
  conditional), generates health score. Use when user says "audit",
  "full SEO check", "analyze my site", or "website health check".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Agent
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Full Website SEO Audit

## Process

1. **Fetch homepage**: use `scripts/fetch_page.py` to retrieve HTML
2. **Detect business type**: analyze homepage signals per seo orchestrator
3. **Crawl site**: follow internal links up to 500 pages, respect robots.txt
4. **Delegate to subagents** (if available, otherwise run inline sequentially):
   - `seo-technical` -- robots.txt, sitemaps, canonicals, Core Web Vitals, security headers
   - `seo-content` -- E-E-A-T, readability, thin content, AI citation readiness
   - `seo-schema` -- detection, validation, generation recommendations
   - `seo-sitemap` -- structure analysis, quality gates, missing pages
   - `seo-performance` -- LCP, INP, CLS measurements
   - `seo-visual` -- screenshots, mobile testing, above-fold analysis
   - `seo-geo` -- AI crawler access, llms.txt, citability, brand mention signals
   - `seo-local` -- GBP signals, NAP consistency, reviews, local schema, industry-specific local factors (spawn when Local Service industry detected: brick-and-mortar, SAB, or hybrid business type)
   - `seo-maps` -- Geo-grid rank tracking, GBP audit, review intelligence, competitor radius mapping (spawn when Local Service detected AND DataForSEO MCP available)
   - `seo-google` -- CWV field data (CrUX), URL indexation (GSC), organic traffic (GA4) (spawn when Google API credentials detected via `python scripts/google_auth.py --check`)
5. **Score** -- aggregate into SEO Health Score (0-100)
6. **Report** -- generate prioritized action plan

## Crawl Configuration

```
Max pages: 500
Respect robots.txt: Yes
Follow redirects: Yes (max 3 hops)
Timeout per page: 30 seconds
Concurrent requests: 5
Delay between requests: 1 second
```

## Output Files

- `FULL-AUDIT-REPORT.md`: Comprehensive findings
- `ACTION-PLAN.md`: Prioritized recommendations (Critical > High > Medium > Low)
- `screenshots/`: Desktop + mobile captures (if Playwright available)
- **PDF Report** (recommended): Generate a professional A4 PDF using `scripts/google_report.py --type full`. This produces a white-cover enterprise report with TOC, executive summary, charts (Lighthouse gauges, query bars, index donut), metric cards, threshold tables, prioritized recommendations with effort estimates, and implementation roadmap. Always offer PDF generation after completing an audit.

## Scoring Weights

| Category | Weight |
|----------|--------|
| Technical SEO | 22% |
| Content Quality | 23% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| AI Search Readiness | 10% |
| Images | 5% |

## Report Structure

### Executive Summary
- Overall SEO Health Score (0-100)
- Business type detected
- Top 5 critical issues
- Top 5 quick wins

### Technical SEO
- Crawlability issues
- Indexability problems
- Security concerns
- Core Web Vitals status

### Content Quality
- E-E-A-T assessment
- Thin content pages
- Duplicate content issues
- Readability scores

### On-Page SEO
- Title tag issues
- Meta description problems
- Heading structure
- Internal linking gaps

### Schema & Structured Data
- Current implementation
- Validation errors
- Missing opportunities

### Performance
- LCP, INP, CLS scores
- Resource optimization needs
- Third-party script impact

### Images
- Missing alt text
- Oversized images
- Format recommendations

### AI Search Readiness
- Citability score
- Structural improvements
- Authority signals

## Priority Definitions

- **Critical**: Blocks indexing or causes penalties (fix immediately)
- **High**: Significantly impacts rankings (fix within 1 week)
- **Medium**: Optimization opportunity (fix within 1 month)
- **Low**: Nice to have (backlog)

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, spawn the `seo-dataforseo` agent alongside existing subagents to enrich the audit with live data: real SERP positions, backlink profiles with spam scores, on-page analysis (Lighthouse), business listings, and AI visibility checks (ChatGPT scraper, LLM mentions).

## Google API Integration (Optional)

If Google API credentials are configured (`python scripts/google_auth.py --check`), spawn the `seo-google` agent to enrich the audit with real Google field data: CrUX Core Web Vitals (replaces lab-only estimates), GSC URL indexation status, search performance (clicks, impressions, CTR), and GA4 organic traffic trends. The Performance (CWV) category score benefits most from field data.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| robots.txt blocks crawling | Report which paths are blocked. Analyze only accessible pages and note the limitation in the report. |
| Rate limiting (429 responses) | Back off and reduce concurrent requests. Report partial results with a note on which sections could not be completed. |
| Timeout on large sites (500+ pages) | Cap the crawl at the timeout limit. Report findings for pages crawled and estimate total site scope. |
```

## File: `skills/seo-competitor-pages/SKILL.md`
```markdown
---
name: seo-competitor-pages
description: >
  Generate SEO-optimized competitor comparison and alternatives pages. Covers
  "X vs Y" layouts, "alternatives to X" pages, feature matrices, schema markup,
  and conversion optimization. Use when user says "comparison page", "vs page",
  "alternatives page", "competitor comparison", "X vs Y", "versus",
  "compare competitors", or "alternative to".
user-invokable: true
argument-hint: "[url or generate] [competitor]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Competitor Comparison & Alternatives Pages

Create high-converting comparison and alternatives pages that target
competitive intent keywords with accurate, structured content.

## Page Types

### 1. "X vs Y" Comparison Pages
- Direct head-to-head comparison between two products/services
- Balanced feature-by-feature analysis
- Clear verdict or recommendation with justification
- Target keyword: `[Product A] vs [Product B]`

### 2. "Alternatives to X" Pages
- List of alternatives to a specific product/service
- Each alternative with brief summary, pros/cons, best-for use case
- Target keyword: `[Product] alternatives`, `best alternatives to [Product]`

### 3. "Best [Category] Tools" Roundup Pages
- Curated list of top tools/services in a category
- Ranking criteria clearly stated
- Target keyword: `best [category] tools [year]`, `top [category] software`

### 4. Comparison Table Pages
- Feature matrix with multiple products in columns
- Sortable/filterable if interactive
- Target keyword: `[category] comparison`, `[category] comparison chart`

## Comparison Table Generation

### Feature Matrix Layout
```
| Feature          | Your Product | Competitor A | Competitor B |
|------------------|:------------:|:------------:|:------------:|
| Feature 1        | ✅           | ✅           | ❌           |
| Feature 2        | ✅           | ⚠️ Partial   | ✅           |
| Feature 3        | ✅           | ❌           | ❌           |
| Pricing (from)   | $X/mo        | $Y/mo        | $Z/mo        |
| Free Tier        | ✅           | ❌           | ✅           |
```

### Data Accuracy Requirements
- All feature claims must be verifiable from public sources
- Pricing must be current (include "as of [date]" note)
- Update frequency: review quarterly or when competitors ship major changes
- Link to source for each competitor data point where possible

## Schema Markup Recommendations

### Product Schema with AggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Product Description]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Rating]",
    "reviewCount": "[Count]",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### SoftwareApplication (for software comparisons)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Software Name]",
  "applicationCategory": "[Category]",
  "operatingSystem": "[OS]",
  "offers": {
    "@type": "Offer",
    "price": "[Price]",
    "priceCurrency": "USD"
  }
}
```

### ItemList (for roundup pages)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Best [Category] Tools [Year]",
  "itemListOrder": "https://schema.org/ItemListOrderDescending",
  "numberOfItems": "[Count]",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "[Product Name]",
      "url": "[Product URL]"
    }
  ]
}
```

## Keyword Targeting

### Comparison Intent Patterns
| Pattern | Example | Search Volume Signal |
|---------|---------|---------------------|
| `[A] vs [B]` | "Slack vs Teams" | High |
| `[A] alternative` | "Figma alternatives" | High |
| `[A] alternatives [year]` | "Notion alternatives 2026" | High |
| `best [category] tools` | "best project management tools" | High |
| `[A] vs [B] for [use case]` | "AWS vs Azure for startups" | Medium |
| `[A] review [year]` | "Monday.com review 2026" | Medium |
| `[A] vs [B] pricing` | "HubSpot vs Salesforce pricing" | Medium |
| `is [A] better than [B]` | "is Notion better than Confluence" | Medium |

### Title Tag Formulas
- X vs Y: `[A] vs [B]: [Key Differentiator] ([Year])`
- Alternatives: `[N] Best [A] Alternatives in [Year] (Free & Paid)`
- Roundup: `[N] Best [Category] Tools in [Year], Compared & Ranked`

### H1 Patterns
- Match title tag intent
- Include primary keyword naturally
- Keep under 70 characters

## Conversion-Optimized Layouts

### CTA Placement
- **Above fold**: Brief comparison summary with primary CTA
- **After comparison table**: "Try [Your Product] free" CTA
- **Bottom of page**: Final recommendation with CTA
- Avoid aggressive CTAs in competitor description sections (reduces trust)

### Social Proof Sections
- Customer testimonials relevant to comparison criteria
- G2/Capterra/TrustPilot ratings (with source links)
- Case studies showing migration from competitor
- "Switched from [Competitor]" stories

### Pricing Highlights
- Clear pricing comparison table
- Highlight value advantages (not just lowest price)
- Include hidden costs (setup fees, per-user pricing, overage charges)
- Link to full pricing page

### Trust Signals
- "Last updated [date]" timestamp
- Author with relevant expertise
- Methodology disclosure (how comparisons were conducted)
- Disclosure of own product affiliation

## Fairness Guidelines

- **Accuracy**: All competitor information must be verifiable from public sources
- **No defamation**: Never make false or misleading claims about competitors
- **Cite sources**: Link to competitor websites, review sites, or documentation
- **Timely updates**: Review and update when competitors release major changes
- **Disclose affiliation**: Clearly state which product is yours
- **Balanced presentation**: Acknowledge competitor strengths honestly
- **Pricing accuracy**: Include "as of [date]" disclaimers on all pricing data
- **Feature verification**: Test competitor features where possible, cite documentation otherwise

## Internal Linking

- Link to your own product/service pages from comparison sections
- Cross-link between related comparison pages (e.g., "A vs B" links to "A vs C")
- Link to feature-specific pages when discussing individual features
- Breadcrumb: Home > Comparisons > [This Page]
- Related comparisons section at bottom of page
- Link to case studies and testimonials mentioned in the comparison

## Output

### Comparison Page Template
- `COMPARISON-PAGE.md`: Ready-to-implement page structure with sections
- Feature matrix table
- Content outline with word count targets (minimum 1,500 words)

### Schema Markup
- `comparison-schema.json`: Product/SoftwareApplication/ItemList JSON-LD

### Keyword Strategy
- Primary and secondary keywords
- Related long-tail opportunities
- Content gaps vs existing competitor pages

### Recommendations
- Content improvements for existing comparison pages
- New comparison page opportunities
- Schema markup additions
- Conversion optimization suggestions

## Error Handling

| Scenario | Action |
|----------|--------|
| Competitor URL unreachable | Report which competitor URLs failed. Proceed with available data and note gaps in the comparison. |
| Insufficient competitor data (pricing, features unavailable) | Flag missing data points clearly. Use "Not publicly available" in comparison tables rather than guessing. |
| No product/service overlap found | Report that the products serve different markets. Suggest alternative competitors that share feature overlap, or pivot to a category roundup format. |
```

## File: `skills/seo-content/SKILL.md`
```markdown
---
name: seo-content
description: >
  Content quality and E-E-A-T analysis with AI citation readiness assessment.
  Use when user says "content quality", "E-E-A-T", "content analysis",
  "readability check", "thin content", or "content audit".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Content Quality & E-E-A-T Analysis

## E-E-A-T Framework (updated Sept 2025 QRG)

Read `skills/seo/references/eeat-framework.md` for full criteria.

### Experience (first-hand signals)
- Original research, case studies, before/after results
- Personal anecdotes, process documentation
- Unique data, proprietary insights
- Photos/videos from direct experience

### Expertise
- Author credentials, certifications, bio
- Professional background relevant to topic
- Technical depth appropriate for audience
- Accurate, well-sourced claims

### Authoritativeness
- External citations, backlinks from authoritative sources
- Brand mentions, industry recognition
- Published in recognized outlets
- Cited by other experts

### Trustworthiness
- Contact information, physical address
- Privacy policy, terms of service
- Customer testimonials, reviews
- Date stamps, transparent corrections
- Secure site (HTTPS)

## Content Metrics

### Word Count Analysis
Compare against page type minimums:
| Page Type | Minimum |
|-----------|---------|
| Homepage | 500 |
| Service page | 800 |
| Blog post | 1,500 |
| Product page | 300+ (400+ for complex products) |
| Location page | 500-600 |

> **Important:** These are **topical coverage floors**, not targets. Google has confirmed word count is NOT a direct ranking factor. The goal is comprehensive topical coverage; a 500-word page that thoroughly answers the query will outrank a 2,000-word page that doesn't. Use these as guidelines for adequate coverage depth, not rigid requirements.

### Readability
- Flesch Reading Ease: target 60-70 for general audience

> **Note:** Flesch Reading Ease is a useful proxy for content accessibility but is NOT a direct Google ranking factor. John Mueller has confirmed Google does not use basic readability scores for ranking. Yoast deprioritized Flesch scores in v19.3. Use readability analysis as a content quality indicator, not as an SEO metric to optimize directly.
- Grade level: match target audience
- Sentence length: average 15-20 words
- Paragraph length: 2-4 sentences

### Keyword Optimization
- Primary keyword in title, H1, first 100 words
- Natural density (1-3%)
- Semantic variations present
- No keyword stuffing

### Content Structure
- Logical heading hierarchy (H1 -> H2 -> H3)
- Scannable sections with descriptive headings
- Bullet/numbered lists where appropriate
- Table of contents for long-form content

### Multimedia
- Relevant images with proper alt text
- Videos where appropriate
- Infographics for complex data
- Charts/graphs for statistics

### Internal Linking
- 3-5 relevant internal links per 1000 words
- Descriptive anchor text
- Links to related content
- No orphan pages

### External Linking
- Cite authoritative sources
- Open in new tab for user experience
- Reasonable count (not excessive)

## AI Content Assessment (Sept 2025 QRG addition)

Google's raters now formally assess whether content appears AI-generated.

### Acceptable AI Content
- Demonstrates genuine E-E-A-T
- Provides unique value
- Has human oversight and editing
- Contains original insights

### Low-Quality AI Content Markers
- Generic phrasing, lack of specificity
- No original insight
- Repetitive structure across pages
- No author attribution
- Factual inaccuracies

> **Helpful Content System (March 2024):** The Helpful Content System was merged into Google's core ranking algorithm during the March 2024 core update. It no longer operates as a standalone classifier. Helpfulness signals are now weighted within every core update. The same principles apply (people-first content, demonstrating E-E-A-T, satisfying user intent), but enforcement is continuous rather than through separate HCU updates.

## AI Citation Readiness (GEO signals)

Optimize for AI search engines (ChatGPT, Perplexity, Google AI Overviews):

- Clear, quotable statements with statistics/facts
- Structured data (especially for data points)
- Strong heading hierarchy (H1->H2->H3 flow)
- Answer-first formatting for key questions
- Tables and lists for comparative data
- Clear attribution and source citations

### AI Search Visibility & GEO (2025-2026)

**Google AI Mode** launched publicly in May 2025 as a separate tab in Google Search, available in 180+ countries. Unlike AI Overviews (which appear above organic results), AI Mode provides a fully conversational search experience with **zero organic blue links**, making AI citation the only visibility mechanism.

**Key optimization strategies for AI citation:**
- **Structured answers:** Clear question-answer formats, definition patterns, and step-by-step instructions that AI systems can extract and cite
- **First-party data:** Original research, statistics, case studies, and unique datasets are highly cited by AI systems
- **Schema markup:** Article, FAQ (for non-Google AI platforms), and structured content schemas help AI systems parse and attribute content
- **Topical authority:** AI systems preferentially cite sources that demonstrate deep expertise. Build content clusters, not isolated pages
- **Entity clarity:** Ensure brand, authors, and key concepts are clearly defined with structured data (Organization, Person schema)
- **Multi-platform tracking:** Monitor visibility across Google AI Overviews, AI Mode, ChatGPT, Perplexity, and Bing Copilot, not just traditional rankings. Treat AI citation as a standalone KPI alongside organic rankings and traffic.

**Generative Engine Optimization (GEO):**
GEO is the emerging discipline of optimizing content specifically for AI-generated answers. Key GEO signals include: quotability (clear, concise extractable facts), attribution (source citations within your content), structure (well-organized heading hierarchy), and freshness (regularly updated data). Cross-reference the `seo-geo` skill for detailed GEO workflows.

## Content Freshness

- Publication date visible
- Last updated date if content has been revised
- Flag content older than 12 months without update for fast-changing topics

## Output

### Content Quality Score: XX/100

### E-E-A-T Breakdown
| Factor | Score | Key Signals |
|--------|-------|-------------|
| Experience | XX/25 | ... |
| Expertise | XX/25 | ... |
| Authoritativeness | XX/25 | ... |
| Trustworthiness | XX/25 | ... |

### AI Citation Readiness: XX/100

### Issues Found
### Recommendations

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `kw_data_google_ads_search_volume` for real keyword volume data, `dataforseo_labs_bulk_keyword_difficulty` for difficulty scores, `dataforseo_labs_search_intent` for intent classification, and `content_analysis_summary` for content quality analysis.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess page content. Suggest the user verify the URL and try again. |
| Content behind paywall (402/403, login wall) | Report that the content is not publicly accessible. Analyze only the visible portion (meta tags, headers) and note the limitation. |
| Thin content (fewer than 100 words retrievable) | Report the findings as-is rather than guessing. Flag the page as potentially JavaScript-rendered or gated, and suggest the user provide the full text directly. |
```

## File: `skills/seo-dataforseo/SKILL.md`
```markdown
---
name: seo-dataforseo
description: >
  Live SEO data via DataForSEO MCP server. SERP analysis (Google, Bing, Yahoo,
  YouTube), keyword research (volume, difficulty, intent, trends), backlink
  profiles, on-page analysis (Lighthouse, content parsing), competitor analysis,
  content analysis, business listings, AI visibility (ChatGPT scraper, LLM
  mention tracking), and domain analytics. Requires DataForSEO extension
  installed. Use when user says "dataforseo", "live SERP", "keyword volume",
  "backlink data", "competitor data", "AI visibility check", "LLM mentions",
  or "real search data".
user-invokable: true
argument-hint: "[command] [query]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
compatibility: "Requires DataForSEO MCP server"
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# DataForSEO: Live SEO Data (Extension)

Live search data via the DataForSEO MCP server. Provides real-time SERP results,
keyword metrics, backlink profiles, on-page analysis, content analysis, business
listings, AI visibility checking, and LLM mention tracking across
9 API modules with 79 MCP tools.

## Prerequisites

This skill requires the DataForSEO extension to be installed:
```bash
./extensions/dataforseo/install.sh
```

**Check availability:** Before using any DataForSEO tool, verify the MCP server
is connected by checking if `serp_organic_live_advanced` or any DataForSEO tool
is available. If tools are not available, inform the user the extension is not
installed and provide install instructions.

## API Credit Awareness

DataForSEO charges per API call. Be efficient:
- Prefer bulk endpoints over multiple single calls
- Use default parameters (US, English) unless user specifies otherwise
- Cache results mentally within a session; don't re-fetch the same data
- Warn user before running expensive operations (full backlink crawls, large keyword lists)

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo dataforseo serp <keyword>` | Google organic SERP results |
| `/seo dataforseo serp-youtube <keyword>` | YouTube search results |
| `/seo dataforseo youtube <video_id>` | YouTube video deep analysis |
| `/seo dataforseo keywords <seed>` | Keyword ideas and suggestions |
| `/seo dataforseo volume <keywords>` | Search volume for keywords |
| `/seo dataforseo difficulty <keywords>` | Keyword difficulty scores |
| `/seo dataforseo intent <keywords>` | Search intent classification |
| `/seo dataforseo trends <keyword>` | Google Trends data |
| `/seo dataforseo backlinks <domain>` | Full backlink profile |
| `/seo dataforseo competitors <domain>` | Competitor domain analysis |
| `/seo dataforseo ranked <domain>` | Ranked keywords for domain |
| `/seo dataforseo intersection <domains>` | Keyword/backlink overlap |
| `/seo dataforseo traffic <domains>` | Bulk traffic estimation |
| `/seo dataforseo subdomains <domain>` | Subdomains with ranking data |
| `/seo dataforseo top-searches <domain>` | Top queries mentioning domain |
| `/seo dataforseo onpage <url>` | On-page analysis (Lighthouse + parsing) |
| `/seo dataforseo tech <domain>` | Technology stack detection |
| `/seo dataforseo whois <domain>` | WHOIS registration data |
| `/seo dataforseo content <keyword/url>` | Content analysis and trends |
| `/seo dataforseo listings <keyword>` | Business listings search |
| `/seo dataforseo ai-scrape <query>` | ChatGPT web scraper for GEO |
| `/seo dataforseo ai-mentions <keyword>` | LLM mention tracking for GEO |

---

## SERP Analysis

### `/seo dataforseo serp <keyword>`

Fetch live Google organic search results.

**MCP tools:** `serp_organic_live_advanced`

**Default parameters:** location_code=2840 (US), language_code=en, device=desktop, depth=100

**Also supports:** The `serp_organic_live_advanced` tool supports Google, Bing, and Yahoo via the `se` parameter. Specify "bing" or "yahoo" to switch search engines.

**Output:** Rank, URL, title, description, domain, featured snippets, AI overview references, People Also Ask.

### `/seo dataforseo serp-youtube <keyword>`

Fetch YouTube search results. Valuable for GEO. YouTube mentions correlate most strongly with AI citations.

**MCP tools:** `serp_youtube_organic_live_advanced`

**Output:** Video title, channel, views, upload date, description, URL.

### `/seo dataforseo youtube <video_id>`

Deep analysis of a specific YouTube video: info, comments, and subtitles. YouTube mentions have the strongest correlation (0.737) with AI visibility, making this critical for GEO analysis.

**MCP tools:** `serp_youtube_video_info_live_advanced`, `serp_youtube_video_comments_live_advanced`, `serp_youtube_video_subtitles_live_advanced`

**Parameters:** video_id (the YouTube video ID, e.g., "dQw4w9WgXcQ")

**Output:** Video metadata (title, channel, views, likes, description), top comments with engagement, subtitle/transcript text.

---

## Keyword Research

### `/seo dataforseo keywords <seed>`

Generate keyword ideas, suggestions, and related terms from a seed keyword.

**MCP tools:** `dataforseo_labs_google_keyword_ideas`, `dataforseo_labs_google_keyword_suggestions`, `dataforseo_labs_google_related_keywords`

**Default parameters:** location_code=2840 (US), language_code=en, limit=50

**Output:** Keyword, search volume, CPC, competition level, keyword difficulty, trend.

### `/seo dataforseo volume <keywords>`

Get search volume and metrics for a list of keywords.

**MCP tools:** `kw_data_google_ads_search_volume`

**Parameters:** keywords (array, comma-separated), location_code, language_code

**Output:** Keyword, monthly search volume, CPC, competition, monthly trend data.

### `/seo dataforseo difficulty <keywords>`

Calculate keyword difficulty scores for ranking competitiveness.

**MCP tools:** `dataforseo_labs_bulk_keyword_difficulty`

**Parameters:** keywords (array), location_code, language_code

**Output:** Keyword, difficulty score (0-100), interpretation (Easy/Medium/Hard/Very Hard).

### `/seo dataforseo intent <keywords>`

Classify keywords by user search intent.

**MCP tools:** `dataforseo_labs_search_intent`

**Parameters:** keywords (array), location_code, language_code

**Output:** Keyword, intent type (informational, navigational, commercial, transactional), confidence score.

### `/seo dataforseo trends <keyword>`

Analyze keyword trends over time using Google Trends data.

**MCP tools:** `kw_data_google_trends_explore`

**Parameters:** keywords (array), location_code, date_from, date_to, language_code

**Output:** Keyword, time series data, trend direction, seasonality signals.

---

## Domain & Competitor Analysis

### `/seo dataforseo backlinks <domain>`

Comprehensive backlink profile analysis.

**MCP tools:** `backlinks_summary`, `backlinks_backlinks`, `backlinks_anchors`, `backlinks_referring_domains`, `backlinks_bulk_spam_score`, `backlinks_timeseries_summary`

**Default parameters:** limit=100 per sub-call

**Output:** Total backlinks, referring domains, domain rank, spam score, top anchors, new/lost backlinks over time, dofollow ratio, top referring domains.

### `/seo dataforseo competitors <domain>`

Identify competing domains and estimate traffic.

**MCP tools:** `dataforseo_labs_google_competitors_domain`, `dataforseo_labs_google_domain_rank_overview`, `dataforseo_labs_bulk_traffic_estimation`

**Output:** Competitor domains, keyword overlap %, estimated traffic, domain rank, common keywords.

### `/seo dataforseo ranked <domain>`

List keywords a domain ranks for with positions and page data.

**MCP tools:** `dataforseo_labs_google_ranked_keywords`, `dataforseo_labs_google_relevant_pages`

**Default parameters:** limit=100, location_code=2840

**Output:** Keyword, position, URL, search volume, traffic share, SERP features.

### `/seo dataforseo intersection <domain1> <domain2> [...]`

Find shared keywords and backlink sources across 2-20 domains.

**MCP tools:** `dataforseo_labs_google_domain_intersection`, `backlinks_domain_intersection`

**Parameters:** domains (2-20 array)

**Output:** Shared keywords with positions per domain, shared backlink sources, unique keywords per domain.

### `/seo dataforseo traffic <domains>`

Estimate organic search traffic for one or more domains.

**MCP tools:** `dataforseo_labs_bulk_traffic_estimation`

**Parameters:** domains (array)

**Output:** Domain, estimated organic traffic, estimated traffic cost, top keywords.

### `/seo dataforseo subdomains <domain>`

Enumerate subdomains with their ranking data and traffic estimates.

**MCP tools:** `dataforseo_labs_google_subdomains`

**Parameters:** target (domain), location_code, language_code

**Output:** Subdomain, ranked keywords count, estimated traffic, organic cost.

### `/seo dataforseo top-searches <domain>`

Find the most popular search queries that mention a specific domain in results.

**MCP tools:** `dataforseo_labs_google_top_searches`

**Parameters:** target (domain), location_code, language_code

**Output:** Query, search volume, domain position, SERP features, traffic share.

---

## Technical / On-Page

### `/seo dataforseo onpage <url>`

Run on-page analysis including Lighthouse audit and content parsing.

**MCP tools:** `on_page_instant_pages`, `on_page_content_parsing`, `on_page_lighthouse`

**Usage:**
- `on_page_instant_pages`:Quick page analysis (status codes, meta tags, content size, page timing, broken links, on-page checks)
- `on_page_content_parsing`:Extract and parse page content (plain text, word count, structure)
- `on_page_lighthouse`:Full Lighthouse audit (performance score, accessibility, best practices, SEO, Core Web Vitals)

**Output:** Pages crawled, status codes, meta tags, titles, content size, load times, Lighthouse scores, broken links, resource analysis.

### `/seo dataforseo tech <domain>`

Detect technologies used on a domain.

**MCP tools:** `domain_analytics_technologies_domain_technologies`

**Output:** Technology name, version, category (CMS, analytics, CDN, framework, etc.).

### `/seo dataforseo whois <domain>`

Retrieve WHOIS registration data.

**MCP tools:** `domain_analytics_whois_overview`

**Output:** Registrar, creation date, expiration date, nameservers, registrant info (if public).

---

## Content & Business Data

### `/seo dataforseo content <keyword/url>`

Analyze content quality, search for content by topic, and track phrase trends.

**MCP tools:** `content_analysis_search`, `content_analysis_summary`, `content_analysis_phrase_trends`

**Parameters:** keyword (for search/trends) or URL (for summary)

**Output:** Content matches with quality scores, sentiment analysis, readability metrics, phrase trend data over time.

### `/seo dataforseo listings <keyword>`

Search business listings for local SEO competitive analysis.

**MCP tools:** `business_data_business_listings_search`

**Parameters:** keyword, location (optional)

**Output:** Business name, description, category, address, phone, domain, rating, review count, claimed status.

---

## AI Visibility / GEO

### `/seo dataforseo ai-scrape <query>`

Scrape what ChatGPT web search returns for a query. Real GEO visibility check: see which sources ChatGPT cites for your target keywords.

**MCP tools:** `ai_optimization_chat_gpt_scraper`

**Parameters:** query, location_code (optional), language_code (optional). Use `ai_optimization_chat_gpt_scraper_locations` to look up available locations.

**Output:** ChatGPT response content, cited sources/URLs, referenced domains.

### `/seo dataforseo ai-mentions <keyword>`

Track how LLMs mention brands, domains, and topics. Critical for GEO. Measures actual AI visibility across multiple LLM platforms.

**MCP tools:** `ai_opt_llm_ment_search`, `ai_opt_llm_ment_top_domains`, `ai_opt_llm_ment_top_pages`, `ai_opt_llm_ment_agg_metrics`

**Parameters:** keyword, location_code (optional), language_code (optional). Use `ai_opt_llm_ment_loc_and_lang` for available locations/languages and `ai_optimization_llm_models` for supported LLM models.

**Workflow:**
1. Search LLM mentions with `ai_opt_llm_ment_search` (find mentions of a brand/keyword across LLM responses)
2. Get top cited domains with `ai_opt_llm_ment_top_domains` (which domains are most cited for this topic)
3. Get top cited pages with `ai_opt_llm_ment_top_pages` (which specific pages are most cited)
4. Get aggregate metrics with `ai_opt_llm_ment_agg_metrics` (overall mention volume, trends)

**Output:** LLM mention count, top cited domains with frequency, top cited pages, mention trends over time, cross-platform visibility scores.

**Advanced:** Use `ai_opt_llm_ment_cross_agg_metrics` for cross-model comparison (how mentions differ across ChatGPT, Claude, Perplexity, etc.).

---

## Available Utility Tools

These DataForSEO tools are available for internal use by the agent but do not have dedicated commands:

- `serp_locations`:Location code lookups for SERP queries
- `serp_youtube_locations`:Location code lookups for YouTube queries
- `kw_data_google_ads_locations`:Location lookups for keyword data
- `kw_data_dfs_trends_demography`:Demographic data for trend analysis
- `kw_data_dfs_trends_subregion_interests`:Subregion interest data for trends
- `kw_data_dfs_trends_explore`:DFS proprietary trends data
- `kw_data_google_trends_categories`:Google Trends category lookups
- `dataforseo_labs_google_keyword_overview`:Quick keyword metrics overview
- `dataforseo_labs_google_historical_serp`:Historical SERP results for a keyword
- `dataforseo_labs_google_serp_competitors`:Competitors for a specific SERP
- `dataforseo_labs_google_keywords_for_site`:Keywords a site ranks for (alternative to ranked)
- `dataforseo_labs_google_page_intersection`:Page-level intersection analysis
- `dataforseo_labs_google_historical_rank_overview`:Historical domain rank data
- `dataforseo_labs_google_historical_keyword_data`:Historical keyword metrics
- `dataforseo_labs_available_filters`:Available filter options for Labs endpoints
- `backlinks_competitors`:Find domains with similar backlink profiles
- `backlinks_bulk_backlinks`:Bulk backlink counts for multiple targets
- `backlinks_bulk_new_lost_referring_domains`:Bulk new/lost referring domains
- `backlinks_bulk_new_lost_backlinks`:Bulk new/lost backlinks
- `backlinks_bulk_ranks`:Bulk rank overview for multiple targets
- `backlinks_bulk_referring_domains`:Bulk referring domain counts
- `backlinks_domain_pages_summary`:Summary of pages on a domain
- `backlinks_domain_pages`:List pages on a domain with backlink data
- `backlinks_page_intersection`:Shared backlink sources at page level
- `backlinks_referring_networks`:Referring network analysis
- `backlinks_timeseries_new_lost_summary`:Track new/lost backlinks over time
- `backlinks_bulk_pages_summary`:Bulk page summaries
- `backlinks_available_filters`:Available filter options for Backlinks endpoints
- `domain_analytics_whois_available_filters`:WHOIS filter options
- `domain_analytics_technologies_available_filters`:Technology detection filter options
- `ai_opt_kw_data_loc_and_lang`:AI optimization keyword data locations/languages
- `ai_optimization_keyword_data_search_volume`:AI-specific keyword volume data
- `ai_optimization_llm_response`:Direct LLM response analysis
- `ai_optimization_llm_mentions_filters`:Available filters for LLM mentions
- `ai_optimization_chat_gpt_scraper_locations`:Available locations for ChatGPT scraper

## Cross-Skill Integration

When DataForSEO MCP tools are available, other claude-seo skills can leverage live data:

- **seo-audit**:Spawn `seo-dataforseo` agent for real SERP, backlink, on-page, and listings data
- **seo-technical**:Use `on_page_instant_pages` / `on_page_lighthouse` for real crawl data, `domain_analytics_technologies_domain_technologies` for stack detection
- **seo-content**:Use `kw_data_google_ads_search_volume`, `dataforseo_labs_bulk_keyword_difficulty`, `dataforseo_labs_search_intent` for real keyword metrics, `content_analysis_summary` for content quality
- **seo-page**:Use `serp_organic_live_advanced` for real SERP positions, `backlinks_summary` for link data
- **seo-geo**:Use `ai_optimization_chat_gpt_scraper` for real ChatGPT visibility, `ai_opt_llm_ment_search` for LLM mention tracking
- **seo-plan**:Use `dataforseo_labs_google_competitors_domain`, `dataforseo_labs_google_domain_intersection`, `dataforseo_labs_bulk_traffic_estimation` for real competitive intelligence

## Error Handling

- **MCP server not connected**: Report that DataForSEO extension is not installed or MCP server is unreachable. Suggest running `./extensions/dataforseo/install.sh`
- **API authentication failed**: Report invalid credentials. Suggest checking DataForSEO API login/password in MCP config
- **Rate limit exceeded**: Report the limit hit and suggest waiting before retrying
- **No results returned**: Report "no data found" for the query rather than guessing. Suggest broadening the query or checking location/language codes
- **Invalid location code**: Report the error and suggest using the locations lookup tool to find the correct code

## Output Formatting

Match existing claude-seo output patterns:
- Use tables for comparative data
- Prioritize issues as Critical > High > Medium > Low
- Include specific, actionable recommendations
- Show scores as XX/100 where applicable
- Note data source as "DataForSEO (live)" to distinguish from static analysis
```

## File: `skills/seo-geo/SKILL.md`
```markdown
---
name: seo-geo
description: >
  Optimize content for AI Overviews (formerly SGE), ChatGPT web search,
  Perplexity, and other AI-powered search experiences. Generative Engine
  Optimization (GEO) analysis including brand mention signals, AI crawler
  accessibility, llms.txt compliance, passage-level citability scoring, and
  platform-specific optimization. Use when user says "AI Overviews", "SGE",
  "GEO", "AI search", "LLM optimization", "Perplexity", "AI citations",
  "ChatGPT search", or "AI visibility".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# AI Search / GEO Optimization (February 2026)

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| AI Overviews reach | 1.5 billion users/month across 200+ countries | Google |
| AI Overviews query coverage | 50%+ of all queries | Industry data |
| AI-referred sessions growth | 527% (Jan-May 2025) | SparkToro |
| ChatGPT weekly active users | 900 million | OpenAI |
| Perplexity monthly queries | 500+ million | Perplexity |

## Critical Insight: Brand Mentions > Backlinks

**Brand mentions correlate 3x more strongly with AI visibility than backlinks.**
(Ahrefs December 2025 study of 75,000 brands)

| Signal | Correlation with AI Citations |
|--------|------------------------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit mentions | High |
| Wikipedia presence | High |
| LinkedIn presence | Moderate |
| Domain Rating (backlinks) | ~0.266 (weak) |

**Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query, so platform-specific optimization is essential.

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**92% of AI Overview citations come from top-10 ranking pages**, but 47% come from pages ranking below position 5, demonstrating different selection logic.

**Strong signals:**
- Clean H1->H2->H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript.** Server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt` for these AI crawlers:

| Crawler | Owner | Purpose |
|---------|-------|---------|
| GPTBot | OpenAI | ChatGPT web search |
| OAI-SearchBot | OpenAI | OpenAI search features |
| ChatGPT-User | OpenAI | ChatGPT browsing |
| ClaudeBot | Anthropic | Claude web features |
| PerplexityBot | Perplexity | Perplexity AI search |
| CCBot | Common Crawl | Training data (often blocked) |
| anthropic-ai | Anthropic | Claude training |
| Bytespider | ByteDance | TikTok/Douyin AI |
| cohere-ai | Cohere | Cohere models |

**Recommendation:** Allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot for AI search visibility. Block CCBot and training crawlers if desired.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Top-10 ranking pages (92%) | Traditional SEO + passage optimization |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Entity presence, authoritative sources |
| **Perplexity** | Reddit (46.7%), Wikipedia | Community validation, discussions |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

---

## Output

Generate `GEO-ANALYSIS.md` with:

1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity scores)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Server-Side Rendering Check** (JavaScript dependency analysis)
8. **Top 5 Highest-Impact Changes**
9. **Schema Recommendations** (for AI discoverability)
10. **Content Reformatting Suggestions** (specific passages to rewrite)

---

## Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

## Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

## High Impact

1. Create original research/surveys (unique citability)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `ai_optimization_chat_gpt_scraper` to check what ChatGPT web search returns for target queries (real GEO visibility check) and `ai_opt_llm_ment_search` with `ai_opt_llm_ment_top_domains` for LLM mention tracking across AI platforms.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| AI crawlers blocked by robots.txt | Report exactly which crawlers are blocked and which are allowed. Provide specific robots.txt directives to add for enabling AI search visibility. |
| No llms.txt found | Note the absence and provide a ready-to-use llms.txt template based on the site's content structure. |
| No structured data detected | Report the gap and provide specific schema recommendations (Article, Organization, Person) for improving AI discoverability. |
```

## File: `skills/seo-google/SKILL.md`
```markdown
---
name: seo-google
description: >
  Google SEO APIs: Search Console (Search Analytics, URL Inspection, Sitemaps),
  PageSpeed Insights v5, CrUX field data with 25-week history, Indexing API v3,
  and GA4 organic traffic. Provides real Google field data for Core Web Vitals,
  indexation status, search performance, and organic traffic trends. Use when
  user says "search console", "GSC", "PageSpeed", "CrUX", "field data",
  "indexing API", "GA4 organic", "URL inspection", "google api setup",
  "real CWV data", "impressions", "clicks", "CTR", "position data",
  "LCP", "INP", "CLS", "FCP", "TTFB", or "Lighthouse scores".
user-invokable: true
argument-hint: "[command] [url|property]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Google SEO APIs

Direct access to Google's own SEO data. Bridges the gap between crawl-based
analysis (existing claude-seo skills) and Google's real-time field data: actual
Chrome user metrics, real indexation status, search performance, and organic traffic.

All APIs are free. Setup requires a Google Cloud project with API key and/or
service account -- run `/seo google setup` for step-by-step instructions.

## Prerequisites

Before executing any command, check credentials:
```bash
python scripts/google_auth.py --check --json
```

Config file: `~/.config/claude-seo/google-api.json`
```json
{
  "service_account_path": "/path/to/service_account.json",
  "api_key": "AIzaSy...",
  "default_property": "sc-domain:example.com",
  "ga4_property_id": "properties/123456789"
}
```

If missing, read `references/auth-setup.md` and walk the user through setup.

### Credential Tiers

| Tier | Detection | Available Commands |
|------|-----------|-------------------|
| **0** (API Key) | `api_key` present | `pagespeed`, `crux`, `crux-history`, `youtube`, `nlp` |
| **1** (OAuth/SA) | + OAuth token or service account | Tier 0 + `gsc`, `inspect`, `sitemaps`, `index` |
| **2** (Full) | + `ga4_property_id` configured | Tier 1 + `ga4`, `ga4-pages` |
| **3** (Ads) | + `ads_developer_token` + `ads_customer_id` | Tier 2 + `keywords`, `volume` |

Always communicate the detected tier before running commands.

## Quick Reference

| Command | What it does | Tier |
|---------|-------------|------|
| `/seo google setup` | Check/configure API credentials | -- |
| `/seo google pagespeed <url>` | PSI Lighthouse + CrUX field data | 0 |
| `/seo google crux <url>` | CrUX field data only (p75 metrics) | 0 |
| `/seo google crux-history <url>` | 25-week CWV trend analysis | 0 |
| `/seo google gsc <property>` | Search Console: clicks, impressions, CTR, position | 1 |
| `/seo google inspect <url>` | URL Inspection: index status, canonical, crawl info | 1 |
| `/seo google inspect-batch <file>` | Batch URL Inspection from file | 1 |
| `/seo google sitemaps <property>` | GSC sitemap status | 1 |
| `/seo google index <url>` | Submit URL to Indexing API | 1 |
| `/seo google index-batch <file>` | Batch submit up to 200 URLs | 1 |
| `/seo google ga4 [property-id]` | GA4 organic traffic report | 2 |
| `/seo google ga4-pages [property-id]` | Top organic landing pages | 2 |
| `/seo google youtube <query>` | YouTube video search (views, likes, duration) | 0 |
| `/seo google youtube-video <id>` | YouTube video details + top comments | 0 |
| `/seo google nlp <url-or-text>` | NLP entity extraction + sentiment + classification | 0 |
| `/seo google entities <url-or-text>` | Entity analysis only (for E-E-A-T) | 0 |
| `/seo google keywords <seed>` | Keyword ideas from Google Ads Keyword Planner | 3 |
| `/seo google volume <keywords>` | Search volume lookup from Keyword Planner | 3 |
| `/seo google entity <query>` | Knowledge Graph entity check | 0 |
| `/seo google safety <url>` | Web Risk URL safety check | 0 |
| `/seo google quotas` | Show rate limits for all APIs | -- |

---

## PageSpeed + CrUX

### `/seo google pagespeed <url>`

Combined Lighthouse lab data + CrUX field data.

**Script:** `python scripts/pagespeed_check.py <url> --json`
**Reference:** `references/pagespeed-crux-api.md`
**Default:** Both mobile + desktop strategies, all Lighthouse categories.

Output merges lab scores (point-in-time Lighthouse) with field data (28-day
Chrome user metrics). CrUX tries URL-level first, falls back to origin-level.

### `/seo google crux <url>`

CrUX field data only (no Lighthouse run). Faster.

**Script:** `python scripts/pagespeed_check.py <url> --crux-only --json`

### `/seo google crux-history <url>`

25-week CrUX History trends. Shows whether CWV metrics are improving, stable, or degrading.

**Script:** `python scripts/crux_history.py <url> --json`
**Reference:** `references/pagespeed-crux-api.md`

Output includes per-metric trend direction, percentage change, and weekly p75 values.

---

## Search Console

### `/seo google gsc <property>`

Search Analytics: clicks, impressions, CTR, position for last 28 days.

**Script:** `python scripts/gsc_query.py --property <property> --json`
**Reference:** `references/search-console-api.md`
**Default:** 28 days, dimensions=query,page, type=web, limit=1000.

Includes quick-win detection: queries at position 4-10 with high impressions.

### `/seo google inspect <url>`

URL Inspection: real indexation status from Google.

**Script:** `python scripts/gsc_inspect.py <url> --json`

Returns: verdict (PASS/FAIL), coverage state, robots.txt status, indexing state,
page fetch state, canonical selection, mobile usability, rich results.

### `/seo google inspect-batch <file>`

Batch inspection from a file (one URL per line). Rate limited to 2,000/day per site.

**Script:** `python scripts/gsc_inspect.py --batch <file> --json`

### `/seo google sitemaps <property>`

List submitted sitemaps with status, errors, warnings.

**Script:** `python scripts/gsc_query.py sitemaps --property <property> --json`

---

## Indexing API

### `/seo google index <url>`

Notify Google of a URL update.

**Script:** `python scripts/indexing_notify.py <url> --json`
**Reference:** `references/indexing-api.md`

The Indexing API is officially for JobPosting and BroadcastEvent/VideoObject pages.
Always inform the user of this restriction. Daily quota: 200 publish requests.

### `/seo google index-batch <file>`

Batch submit URLs from a file. Tracks quota usage.

**Script:** `python scripts/indexing_notify.py --batch <file> --json`

---

## GA4 Traffic

### `/seo google ga4 [property-id]`

Organic traffic report: daily sessions, users, pageviews, bounce rate, engagement.

**Script:** `python scripts/ga4_report.py --property <id> --json`
**Reference:** `references/ga4-data-api.md`
**Default:** 28 days, filtered to Organic Search channel group.

### `/seo google ga4-pages [property-id]`

Top organic landing pages ranked by sessions.

**Script:** `python scripts/ga4_report.py --property <id> --report top-pages --json`

---

## YouTube (Video SEO)

YouTube mentions have the strongest AI visibility correlation (0.737). Free, API key only.

### `/seo google youtube <query>`

Search YouTube for videos. Returns title, channel, views, likes, duration.

**Script:** `python scripts/youtube_search.py search "<query>" --json`
**Reference:** `references/youtube-api.md`
**Quota:** 100 units per search (10,000 units/day free).

### `/seo google youtube-video <video_id>`

Detailed video info + tags + top 10 comments.

**Script:** `python scripts/youtube_search.py video <video_id> --json`
**Quota:** 2 units (video details + comments).

---

## NLP Content Analysis

Google's own entity/sentiment analysis. Enhances E-E-A-T scoring.

### `/seo google nlp <url-or-text>`

Full NLP analysis: entities, sentiment, content classification.

**Script:** `python scripts/nlp_analyze.py --url <url> --json` or `--text "..."`
**Reference:** `references/nlp-api.md`
**Free tier:** 5,000 units/month. Requires billing enabled on GCP project.

### `/seo google entities <url-or-text>`

Entity extraction only (faster, less quota).

**Script:** `python scripts/nlp_analyze.py --url <url> --features entities --json`

---

## Keyword Research (Google Ads)

Gold-standard keyword volume data. Requires Google Ads account.

### `/seo google keywords <seed>`

Generate keyword ideas from seed terms.

**Script:** `python scripts/keyword_planner.py ideas "<seed>" --json`
**Reference:** `references/keyword-planner-api.md`
**Requires:** Ads developer token + customer ID in config (Tier 3).

### `/seo google volume <keywords>`

Search volume for specific keywords (comma-separated).

**Script:** `python scripts/keyword_planner.py volume "<kw1>,<kw2>" --json`

---

## Supplementary

### `/seo google entity <query>`

Knowledge Graph entity check. Verifies brand presence.

**Reference:** `references/supplementary-apis.md`
Uses Knowledge Graph Search API with API key.

### `/seo google safety <url>`

Web Risk API check for malware/social engineering flags.

**Reference:** `references/supplementary-apis.md`

### `/seo google quotas`

Display rate limits table. Read `references/rate-limits-quotas.md`.

---

## Reports

After any analysis command, offer to generate a PDF/HTML report.

### `/seo google report <type>`

Generate a professional PDF report with charts and analytics.

**Script:** `python scripts/google_report.py --type <type> --data <json> --domain <domain> --format pdf`

| Type | Input | Output |
|------|-------|--------|
| `cwv-audit` | PSI + CrUX + CrUX History data | Core Web Vitals audit with gauges, timelines, distributions |
| `gsc-performance` | GSC query data | Search Console report with query tables, quick wins |
| `indexation` | Batch inspection data | Indexation status with coverage donut chart |
| `full` | All data combined | Comprehensive Google SEO report (all sections) |

**Workflow:**
1. Run data collection commands (pagespeed, gsc, inspect-batch, etc.)
2. Save JSON output to file: `python scripts/pagespeed_check.py <url> --json > data.json`
3. Generate report: `python scripts/google_report.py --type cwv-audit --data data.json --domain <domain>`

**Convention:** After completing analysis, suggest: "Generate a report? Use `/seo google report <type>`"

---

## Rate Limits

| API | Per-Minute | Per-Day | Auth |
|-----|-----------|---------|------|
| PSI v5 | 240 QPM | 25,000 QPD | API Key |
| CrUX + History | 150 QPM (shared) | Unlimited | API Key |
| GSC Search Analytics | 1,200 QPM/site | 30M QPD | Service Account |
| GSC URL Inspection | 600 QPM | 2,000 QPD/site | Service Account |
| Indexing API | 380 RPM | 200 publish/day | Service Account |
| GA4 Data API | 10 concurrent | ~25K tokens/day | Service Account |

## Cross-Skill Integration

- **seo-audit**: Spawns `seo-google` agent for live CWV + indexation data (conditional)
- **seo-technical**: Uses pagespeed_check.py for real CWV field data
- **seo-performance**: CrUX field data supplements Lighthouse lab data
- **seo-sitemap**: GSC sitemap status shows real crawl/index coverage
- **seo-content**: GSC query data informs keyword targeting
- **seo-geo**: GSC search appearance data includes AI Overview references

## Output Format

- CWV metrics: traffic-light rating (Good / Needs Improvement / Poor)
- Performance reports: tables with sortable columns
- Always include data freshness note
- Save reports as `GOOGLE-API-REPORT-{domain}.md`
- Use templates from `assets/templates/` for structured output

## Technical Notes

- INP replaced FID on March 12, 2024. Never reference FID.
- CLS values from CrUX are string-encoded (e.g., "0.05"). Scripts handle parsing.
- CrUX 404 = insufficient traffic, not an auth error.
- Search Analytics data has 2-3 day lag.
- `round_trip_time` replaced `effectiveConnectionType` in CrUX (Feb 2025).
- Custom Search JSON API is closed to new customers (2025).

## Error Handling

| Scenario | Action |
|----------|--------|
| No credentials configured | Run `/seo google setup`. List Tier 0 commands that work with just an API key. |
| Service account lacks GSC access | Report error. Instruct: add `client_email` to GSC > Settings > Users > Add. |
| CrUX data unavailable (404) | Report insufficient Chrome traffic. Suggest PSI lab data as fallback. |
| GA4 property not found | Report error. Show how to find property ID in GA4 Admin > Property Details. |
| Indexing API quota exceeded | Report 200/day limit. Suggest prioritizing most important URLs. |
| Rate limit (429) | Wait and retry with exponential backoff. Report which API hit the limit. |
```

## File: `skills/seo-google/assets/templates/cwv-audit-report.md`
```markdown
# Core Web Vitals Audit

**URL/Origin:** {target}
**Strategy:** {strategy}

## CrUX Field Data (28-day rolling average)

Real Chrome user experience data from the Chrome UX Report.

| Metric | p75 Value | Rating | Good Threshold | Distribution |
|--------|-----------|--------|----------------|-------------|
| LCP | {lcp_value} | {lcp_rating} | ≤ 2,500ms | Good: {lcp_good}% / NI: {lcp_ni}% / Poor: {lcp_poor}% |
| INP | {inp_value} | {inp_rating} | ≤ 200ms | Good: {inp_good}% / NI: {inp_ni}% / Poor: {inp_poor}% |
| CLS | {cls_value} | {cls_rating} | ≤ 0.1 | Good: {cls_good}% / NI: {cls_ni}% / Poor: {cls_poor}% |
| FCP | {fcp_value} | {fcp_rating} | ≤ 1,800ms | Good: {fcp_good}% / NI: {fcp_ni}% / Poor: {fcp_poor}% |
| TTFB | {ttfb_value} | {ttfb_rating} | ≤ 800ms | Good: {ttfb_good}% / NI: {ttfb_ni}% / Poor: {ttfb_poor}% |

**Collection Period:** {collection_start} to {collection_end}

## Lighthouse Lab Scores

| Category | Score |
|----------|-------|
| Performance | {perf_score}/100 |
| Accessibility | {a11y_score}/100 |
| Best Practices | {bp_score}/100 |
| SEO | {seo_score}/100 |

## CrUX History Trends (25-week)

| Metric | Direction | Change | Earliest → Latest |
|--------|-----------|--------|-------------------|
{trends_table}

## Top Opportunities

| Opportunity | Estimated Savings |
|-------------|-------------------|
{opportunities_table}

## Recommendations

{recommendations}

---
*CrUX data updated daily ~04:00 UTC. 28-day rolling average.*
*INP replaced FID as the responsiveness Core Web Vital on March 12, 2024.*
*Generated {timestamp}.*
```

## File: `skills/seo-google/assets/templates/gsc-performance-report.md`
```markdown
# Google Search Console Performance Report

**Property:** {property}
**Date Range:** {start_date} — {end_date}
**Search Type:** {search_type}

## Summary

| Metric | Value |
|--------|-------|
| Total Clicks | {total_clicks} |
| Total Impressions | {total_impressions} |
| Average CTR | {avg_ctr}% |
| Average Position | {avg_position} |

## Top Queries

| # | Query | Clicks | Impressions | CTR | Position |
|---|-------|--------|-------------|-----|----------|
{queries_table}

## Top Pages

| # | Page | Clicks | Impressions | CTR | Position |
|---|------|--------|-------------|-----|----------|
{pages_table}

## Quick Wins (Position 4-10, High Impressions)

These queries rank on page 1 but below position 3. A small ranking improvement could yield significant traffic gains.

| Query | Position | Impressions | Clicks | CTR | Opportunity |
|-------|----------|-------------|--------|-----|-------------|
{quick_wins_table}

## Device Breakdown

| Device | Clicks | Impressions | CTR | Position |
|--------|--------|-------------|-----|----------|
{device_table}

---
*Data freshness: Search Analytics has a 2-3 day lag. Data available for ~16 months.*
*Generated {timestamp} via Google Search Console API.*
```

## File: `skills/seo-google/assets/templates/indexation-status-report.md`
```markdown
# URL Indexation Status Report

**Property:** {property}
**URLs Inspected:** {total_urls}

## Summary

| Status | Count | Percentage |
|--------|-------|-----------|
| Indexed (PASS) | {pass_count} | {pass_pct}% |
| Not Indexed (FAIL) | {fail_count} | {fail_pct}% |
| Neutral | {neutral_count} | {neutral_pct}% |
| Errors | {error_count} | {error_pct}% |

## Detailed Results

| URL | Verdict | Coverage State | Fetch State | Google Canonical | Last Crawl |
|-----|---------|---------------|-------------|-----------------|------------|
{results_table}

## Canonical Mismatches

URLs where Google selected a different canonical than declared:

| URL | User Canonical | Google Canonical |
|-----|---------------|-----------------|
{canonical_mismatches_table}

## Common Issues

| Issue | Count | Priority | Action |
|-------|-------|----------|--------|
{issues_table}

## Rich Results Detected

| URL | Rich Result Type | Status |
|-----|-----------------|--------|
{rich_results_table}

---
*URL Inspection API: 2,000 inspections/day per site, 600/min.*
*Generated {timestamp} via Google Search Console URL Inspection API.*
```

## File: `skills/seo-google/references/auth-setup.md`
```markdown
# Google API Authentication Setup

## Overview

Three credential types serve different APIs:

| Type | Used By | Cost |
|------|---------|------|
| **API Key** | PageSpeed Insights, CrUX, CrUX History, Knowledge Graph | Free |
| **Service Account** | Search Console, Indexing API, GA4 | Free |
| **Both** | Full seo-google skill | Free |

## Step 1: Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Click **Select a project** > **New Project**
3. Name it (e.g., "Claude SEO") and note the project ID
4. Select the project after creation

## Step 2: Enable APIs

Navigate to **APIs & Services > Library** and enable:

| API | Required For |
|-----|-------------|
| Google Search Console API | GSC Search Analytics, URL Inspection, Sitemaps |
| PageSpeed Insights API | PSI Lighthouse lab data |
| Chrome UX Report API | CrUX field data + History |
| Web Search Indexing API | Indexing API v3 |
| Google Analytics Data API | GA4 organic traffic |
| Knowledge Graph Search API | Entity verification (optional) |

## Step 3: Create an API Key

1. **APIs & Services > Credentials > Create Credentials > API key**
2. Click **Restrict key**:
   - Under **API restrictions**, select: PageSpeed Insights API, Chrome UX Report API, Knowledge Graph Search API
3. Copy the key (starts with `AIzaSy...`)

## Step 4: Create a Service Account

1. **IAM & Admin > Service Accounts > Create Service Account**
2. Name: `claude-seo` (or similar)
3. Skip optional permissions steps
4. Click on the created service account > **Keys > Add Key > Create new key > JSON**
5. Download the JSON file and store it securely (e.g., `~/.config/claude-seo/service_account.json`)

The JSON file looks like:
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "claude-seo@your-project.iam.gserviceaccount.com",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

The `client_email` field is what you add to GSC and GA4.

## Step 5: Grant Search Console Access

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select your property
3. **Settings > Users and permissions > Add user**
4. Paste the service account `client_email`
5. Set permission level:
   - **Full** for read-only (Search Analytics, URL Inspection, Sitemaps)
   - **Owner** if you also need the Indexing API

## Step 6: Grant GA4 Access

1. Go to [Google Analytics](https://analytics.google.com)
2. **Admin > Property Access Management > Add users** (the + icon)
3. Paste the service account `client_email`
4. Set role: **Viewer** (minimum for read-only reporting)
5. Note the numeric property ID from **Admin > Property Details** (e.g., `123456789`)

## Step 7: Create Config File

```bash
mkdir -p ~/.config/claude-seo
```

Save to `~/.config/claude-seo/google-api.json`:

```json
{
  "service_account_path": "~/.config/claude-seo/service_account.json",
  "api_key": "AIzaSy...",
  "default_property": "sc-domain:example.com",
  "ga4_property_id": "properties/123456789"
}
```

### Property URL Formats

| Format | Example | When to Use |
|--------|---------|-------------|
| Domain property | `sc-domain:example.com` | Covers all URLs on the domain (recommended) |
| URL-prefix property | `https://example.com/` | Covers only that specific prefix |

## Step 8: Verify Setup

```bash
python scripts/google_auth.py --check
```

Expected output at Tier 2 (full):
```
Credential Tier: 2 -- Full (API key + Service Account + GA4)

  [OK] PageSpeed Insights v5
  [OK] Chrome UX Report (CrUX) API
  [OK] CrUX History API
  [OK] Google Search Console API
       Service account: claude-seo@your-project.iam.gserviceaccount.com
  [OK] Google Indexing API v3
  [OK] GA4 Data API v1beta
```

## Environment Variable Alternatives

Instead of (or in addition to) the config file:

| Variable | Purpose |
|----------|---------|
| `GOOGLE_API_KEY` | API key for PSI/CrUX |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account JSON |
| `GA4_PROPERTY_ID` | GA4 property (e.g., `properties/123456789`) |
| `GSC_PROPERTY` | Default GSC property (e.g., `sc-domain:example.com`) |

## OAuth Scopes Used

| Scope | APIs |
|-------|------|
| `https://www.googleapis.com/auth/webmasters.readonly` | GSC (read) |
| `https://www.googleapis.com/auth/webmasters` | GSC (read/write, needed for sitemap submission) |
| `https://www.googleapis.com/auth/indexing` | Indexing API |
| `https://www.googleapis.com/auth/analytics.readonly` | GA4 (read) |

## Troubleshooting

| Error | Fix |
|-------|-----|
| `403 Forbidden` on GSC | Service account email not added to GSC property, or wrong permission level |
| `403 Forbidden` on GA4 | Service account email not added to GA4 property as Viewer |
| `404 Not Found` on GSC | Wrong property URL format. Use `sc-domain:` or include trailing slash for URL-prefix |
| `404 Not Found` on CrUX | Site has insufficient Chrome traffic. Not a credentials issue. |
| `429 Rate Limit` | Wait and retry. See rate-limits-quotas.md for per-API limits |
| `API not enabled` | Enable the specific API in GCP Console > APIs & Services > Library |
```

## File: `skills/seo-google/references/ga4-data-api.md`
```markdown
# GA4 Data API v1beta Reference

## Overview

The Google Analytics Data API v1beta provides programmatic access to GA4 report data. For SEO, the primary use case is organic traffic analysis.

**Base URL:** `https://analyticsdata.googleapis.com/v1beta`

## Key Methods

| Method | Description |
|--------|-------------|
| `properties.runReport` | Run a standard report |
| `properties.batchRunReports` | Up to 5 reports in one call |
| `properties.runRealtimeReport` | Last 30 minutes of data |
| `properties.getMetadata` | Available dimensions and metrics |
| `properties.checkCompatibility` | Verify dimension/metric combinations |

## runReport Request

```json
{
  "property": "properties/123456789",
  "dimensions": [
    { "name": "date" },
    { "name": "landingPage" }
  ],
  "metrics": [
    { "name": "sessions" },
    { "name": "totalUsers" }
  ],
  "dateRanges": [
    { "startDate": "28daysAgo", "endDate": "yesterday" }
  ],
  "dimensionFilter": {
    "filter": {
      "fieldName": "sessionDefaultChannelGroup",
      "stringFilter": {
        "matchType": "EXACT",
        "value": "Organic Search"
      }
    }
  },
  "orderBys": [
    { "metric": { "metricName": "sessions" }, "desc": true }
  ],
  "limit": 100,
  "returnPropertyQuota": true
}
```

## SEO-Relevant Dimensions

| Dimension | Description |
|-----------|-------------|
| `date` | Date in YYYYMMDD format |
| `pagePath` | Page path (e.g., `/blog/post`) |
| `landingPage` | Entry page path |
| `landingPagePlusQueryString` | Entry page with query params |
| `fullPageUrl` | Full page URL |
| `pageTitle` | Page title |
| `sessionSource` | Traffic source (e.g., `google`) |
| `sessionMedium` | Traffic medium (e.g., `organic`) |
| `sessionDefaultChannelGroup` | Channel grouping (e.g., `Organic Search`) |
| `country` | User country |
| `deviceCategory` | `desktop`, `mobile`, `tablet` |
| `hostName` | Domain name |
| `pageReferrer` | Referrer URL |

## SEO-Relevant Metrics

| Metric | Description |
|--------|-------------|
| `sessions` | Number of sessions |
| `totalUsers` | Total unique users |
| `newUsers` | First-time users |
| `activeUsers` | Users with engagement |
| `screenPageViews` | Page views |
| `bounceRate` | Bounce rate (0-1, multiply by 100 for %) |
| `averageSessionDuration` | Avg duration in seconds |
| `engagementRate` | Engaged session rate (0-1) |
| `keyEvents` | Key events (replaced deprecated `conversions`) |
| `eventCount` | Total event count |

## Filter Expressions

### String Filter

```json
{
  "filter": {
    "fieldName": "sessionDefaultChannelGroup",
    "stringFilter": {
      "matchType": "EXACT",
      "value": "Organic Search"
    }
  }
}
```

Match types: `EXACT`, `BEGINS_WITH`, `ENDS_WITH`, `CONTAINS`, `FULL_REGEXP`, `PARTIAL_REGEXP`

### Combining Filters

```json
{
  "andGroup": {
    "expressions": [
      { "filter": { "fieldName": "country", "stringFilter": { "matchType": "EXACT", "value": "US" }}},
      { "filter": { "fieldName": "deviceCategory", "stringFilter": { "matchType": "EXACT", "value": "mobile" }}}
    ]
  }
}
```

Also supports `orGroup` and `notExpression`.

## Date Range Shortcuts

| Value | Meaning |
|-------|---------|
| `today` | Current day |
| `yesterday` | Previous day |
| `NdaysAgo` | N days ago (e.g., `28daysAgo`) |
| `YYYY-MM-DD` | Specific date |

Up to 4 date ranges per request (for period-over-period comparison).

## Token-Based Quotas

| Quota | Limit | Scope |
|-------|-------|-------|
| Daily tokens | 25,000 | Per property per project |
| Hourly tokens | 5,000 | Per property per project |
| Concurrent requests | 10 | Per property per project |
| Hourly tokens (project-wide) | 1,250 | Per project per property per hour |

Set `returnPropertyQuota: true` to monitor consumption. Simple reports cost ~1-10 tokens; complex ones up to ~100.

## Python Example

```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Filter, FilterExpression,
    Metric, OrderBy, RunReportRequest,
)
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "service_account.json",
    scopes=["https://www.googleapis.com/auth/analytics.readonly"],
)

client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
    property="properties/123456789",
    dimensions=[Dimension(name="landingPage")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="yesterday")],
    dimension_filter=FilterExpression(
        filter=Filter(
            field_name="sessionDefaultChannelGroup",
            string_filter=Filter.StringFilter(
                match_type=Filter.StringFilter.MatchType.EXACT,
                value="Organic Search",
            ),
        )
    ),
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=50,
    return_property_quota=True,
)

response = client.run_report(request)
for row in response.rows:
    print(f"{row.dimension_values[0].value}: {row.metric_values[0].value} sessions")
```

## Authentication
- **Scope:** `https://www.googleapis.com/auth/analytics.readonly`
- Service account must have **Viewer** role in GA4 property
- Add via GA4 Admin > Property Access Management
```

## File: `skills/seo-google/references/indexing-api.md`
```markdown
# Google Indexing API v3 Reference

## Overview

The Indexing API allows you to notify Google when pages are added or removed.

**IMPORTANT:** Officially restricted to pages with **JobPosting** or **BroadcastEvent/VideoObject** structured data. Google may process other page types, but provides no guarantees. Always inform users of this limitation.

## Endpoints

### Publish Notification

**`POST https://indexing.googleapis.com/v3/urlNotifications:publish`**

```json
{
  "url": "https://example.com/jobs/software-engineer",
  "type": "URL_UPDATED"
}
```

| Field | Values |
|-------|--------|
| `url` | The fully qualified URL |
| `type` | `URL_UPDATED` (page added/changed), `URL_DELETED` (page removed) |

**Response:**
```json
{
  "urlNotificationMetadata": {
    "url": "https://example.com/jobs/software-engineer",
    "latestUpdate": {
      "url": "https://example.com/jobs/software-engineer",
      "type": "URL_UPDATED",
      "notifyTime": "2026-03-27T10:00:00Z"
    }
  }
}
```

### Get Notification Metadata

**`GET https://indexing.googleapis.com/v3/urlNotifications/metadata?url={ENCODED_URL}`**

Returns `latestUpdate` and `latestRemove` timestamps for the URL.

### Batch Requests

**`POST https://indexing.googleapis.com/batch`**

Up to **100 URLs** per batch request using `multipart/mixed` format:

```
POST /batch HTTP/1.1
Content-Type: multipart/mixed; boundary=batch_boundary

--batch_boundary
Content-Type: application/http
Content-ID: <item1>

POST /v3/urlNotifications:publish HTTP/1.1
Content-Type: application/json

{"url": "https://example.com/jobs/1", "type": "URL_UPDATED"}
--batch_boundary
Content-Type: application/http
Content-ID: <item2>

POST /v3/urlNotifications:publish HTTP/1.1
Content-Type: application/json

{"url": "https://example.com/jobs/2", "type": "URL_UPDATED"}
--batch_boundary--
```

## Authentication

- **Scope:** `https://www.googleapis.com/auth/indexing`
- **Auth type:** Service account (OAuth 2.0)
- The service account must be **Owner** in Google Search Console for the target domain

## Quotas

| Limit | Value | Scope |
|-------|-------|-------|
| Publish requests | **200/day** (default) | Per project |
| Read-only requests | 180/min | Per project |
| Total requests | 380/min | Per project |

Request a quota increase: [Indexing API Quota Increase Form](https://developers.google.com/search/apis/indexing-api/v3/quota-increase)

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Malformed URL or request body | Check URL format |
| 403 | Permission denied or quota exceeded | Add service account as Owner in GSC, or check quota |
| 429 | Rate limit exceeded | Back off and retry with exponential delay |
| 500/503 | Server error | Retry with exponential backoff |

## Best Practices

1. Submit only URLs with actual content changes (don't spam updates)
2. Use `URL_DELETED` only when a page is permanently removed (returns 404/410)
3. Track daily quota usage -- the 200/day limit resets at midnight Pacific Time
4. For large-scale indexing, use XML sitemaps + Search Console instead
5. Batch requests count individually against the daily quota (100 batch = 100 quota)
```

## File: `skills/seo-google/references/keyword-planner-api.md`
```markdown
# Google Ads API - Keyword Planner Reference

Gold-standard source for keyword search volume. DataForSEO gets its volume data from Google Ads -- this cuts out the middleman.

## Prerequisites (More Complex Than Other Google APIs)

1. **Google Ads Manager Account** -- create at ads.google.com (free to create)
2. **Developer Token** -- apply at Google Ads API Center (requires Basic access approval)
3. **OAuth 2.0 credentials** -- reuse existing OAuth client from seo-google config
4. **For exact volumes**: Run a minimal campaign (~$5-10/day). Without spend, volumes are bucketed ranges ("1K-10K")

## Key Methods

### GenerateKeywordIdeas
Generate keyword suggestions from seed terms.

**Returns per keyword:**
- `text`: Keyword string
- `avg_monthly_searches`: Average monthly volume (exact if spending, bucketed if not)
- `competition`: LOW / MEDIUM / HIGH (for ads, not organic)
- `competition_index`: 0-100 competition score
- `low_top_of_page_bid_micros`: ~20th percentile CPC in micros
- `high_top_of_page_bid_micros`: ~80th percentile CPC in micros
- `monthly_search_volumes[]`: Per-month volume for last 12 months

### GenerateKeywordHistoricalMetrics
Get volume data for specific keywords.

Same return fields as above but for exact keyword list instead of suggestions.

### GenerateKeywordForecastMetrics
Predict clicks, impressions, and cost for keywords.

## Configuration

Add to `~/.config/claude-seo/google-api.json`:

```json
{
  "ads_developer_token": "YOUR_DEV_TOKEN",
  "ads_customer_id": "123-456-7890",
  "ads_login_customer_id": "123-456-7890"
}
```

## Rate Limits

- Keyword Planning requests are more strictly rate-limited than other Ads API services
- Exact QPM/QPS not publicly documented
- Google recommends caching results

## Python Library

```bash
pip install google-ads
```

Uses `google-ads` library (separate from `google-api-python-client`).

## Important Notes

- **Volume accuracy**: Without active ad spend, Google returns bucketed ranges ("1K-10K", "10K-100K") instead of exact numbers like "14,800"
- **Competition score**: Measures advertiser competition for ads, NOT organic ranking difficulty
- **CPC bids**: Reflect what advertisers pay, useful for estimating keyword commercial value
- **Location targeting**: Use location IDs (2840 = United States, 2826 = United Kingdom)
- **Language targeting**: Use language IDs (1000 = English, 1003 = Spanish)
```

## File: `skills/seo-google/references/nlp-api.md`
```markdown
# Google Cloud Natural Language API Reference

NLP analysis enhances E-E-A-T scoring by measuring entity coverage, content sentiment, and topic classification using Google's own taxonomy.

## Endpoint

`POST https://language.googleapis.com/v2/documents:annotateText?key={API_KEY}`

## Features

| Feature | What It Does | SEO Use |
|---------|-------------|---------|
| `extractEntities` | Extract people, orgs, places, events with salience scores | Topic coverage depth, entity optimization |
| `extractDocumentSentiment` | Document + sentence-level sentiment score/magnitude | Content tone assessment |
| `classifyText` | Map content to 700+ Google categories | Topic relevance verification |
| `moderateText` | Content safety/moderation categories | Content quality flags |

## Entity Types

PERSON, LOCATION, ORGANIZATION, EVENT, WORK_OF_ART, CONSUMER_GOOD, OTHER, PHONE_NUMBER, ADDRESS, DATE, NUMBER, PRICE

Each entity includes:
- `name`: Entity text
- `type`: Entity type
- `salience`: Importance score (0-1, higher = more relevant)
- `sentiment`: Per-entity sentiment (score + magnitude)
- `metadata`: Wikipedia URL, MID (Knowledge Graph ID)
- `mentions`: Occurrences in the text

## Sentiment Scoring

- **Score**: -1.0 (negative) to +1.0 (positive)
- **Magnitude**: 0 to infinity (emotional intensity, higher = more emotional)
- Neutral content: score ~0, low magnitude
- Mixed content: score ~0, HIGH magnitude (both positive and negative)

## Pricing

| Feature | Free/month | Paid (per 1K chars) |
|---------|-----------|-------------------|
| Entity Analysis | 5,000 units | $0.001 |
| Sentiment Analysis | 5,000 units | $0.001 |
| Content Classification | 30,000 units | $0.002 |
| Text Moderation | 50,000 units | $0.0005 |

One "unit" = 1,000 characters. Free tier resets monthly.

## Enable the API

1. Go to [console.cloud.google.com/apis/library](https://console.cloud.google.com/apis/library)
2. Search for "Cloud Natural Language API"
3. Click Enable
4. **Billing must be enabled** on the project (free tier still applies)

Uses the same API key as PSI/CrUX.
```

## File: `skills/seo-google/references/pagespeed-crux-api.md`
```markdown
# PageSpeed Insights v5 + CrUX API Reference

## Table of Contents
1. [PageSpeed Insights v5](#pagespeed-insights-v5)
2. [CrUX API (Daily)](#crux-api-daily)
3. [CrUX History API (Weekly)](#crux-history-api-weekly)
4. [Core Web Vitals Thresholds](#core-web-vitals-thresholds)

---

## PageSpeed Insights v5

**Endpoint:** `GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed`

### Parameters

| Param | Type | Description |
|-------|------|-------------|
| `url` | string | Required. URL to analyze. |
| `category` | string | `ACCESSIBILITY`, `BEST_PRACTICES`, `PERFORMANCE`, `SEO`. Can specify multiple. |
| `strategy` | string | `DESKTOP` or `MOBILE` (default). |
| `locale` | string | Locale for text (e.g., `en`). |
| `key` | string | API key. Optional but recommended for quota. |

### Response Structure

```
{
  "id": "https://example.com/",
  "loadingExperience": { ... },        // URL-level CrUX data
  "originLoadingExperience": { ... },  // Origin-level CrUX data
  "lighthouseResult": {
    "categories": {
      "performance": { "score": 0.85 },
      "accessibility": { "score": 0.92 },
      "best-practices": { "score": 0.88 },
      "seo": { "score": 0.95 }
    },
    "audits": { ... }                  // Individual audit results
  },
  "analysisUTCTimestamp": "2026-03-27T..."
}
```

### Field Data Metrics (in loadingExperience)

| PSI Key | CrUX Metric | Unit |
|---------|-------------|------|
| `LARGEST_CONTENTFUL_PAINT_MS` | LCP | ms |
| `INTERACTION_TO_NEXT_PAINT` | INP | ms |
| `CUMULATIVE_LAYOUT_SHIFT_SCORE` | CLS | unitless |
| `FIRST_CONTENTFUL_PAINT_MS` | FCP | ms |
| `EXPERIMENTAL_TIME_TO_FIRST_BYTE` | TTFB | ms |

Each metric contains: `percentile` (p75), `distributions[]` ({min, max, proportion}), `category` (FAST/AVERAGE/SLOW/NONE).

### Key Lighthouse Audit IDs

`first-contentful-paint`, `largest-contentful-paint`, `total-blocking-time`, `cumulative-layout-shift`, `speed-index`, `interactive`

### Rate Limits
- 25,000 QPD with API key
- 240 QPM
- Free, no billing required

### Note on Field Data Migration
Google is migrating CrUX field data out of PSI. For field data, prefer the CrUX API directly. Use PSI primarily for Lighthouse lab data.

---

## CrUX API (Daily)

**Endpoint:** `POST https://chromeuxreport.googleapis.com/v1/records:queryRecord?key={API_KEY}`

### Request

```json
{
  "origin": "https://example.com",
  "formFactor": "PHONE",
  "metrics": ["largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift"]
}
```

| Field | Description |
|-------|-------------|
| `origin` | Origin URL (mutually exclusive with `url`) |
| `url` | Specific page URL (mutually exclusive with `origin`) |
| `formFactor` | `DESKTOP`, `PHONE`, `TABLET` (optional, omit for all) |
| `metrics` | Array of metric names (optional, omit for all) |

### Available Metrics

| Metric | Type | Notes |
|--------|------|-------|
| `largest_contentful_paint` | int (ms) | Core Web Vital |
| `interaction_to_next_paint` | int (ms) | Core Web Vital (replaced FID) |
| `cumulative_layout_shift` | **string** | Core Web Vital. **String-encoded!** Parse carefully. |
| `first_contentful_paint` | int (ms) | |
| `experimental_time_to_first_byte` | int (ms) | |
| `round_trip_time` | int (ms) | Replaced effectiveConnectionType (Feb 2025) |
| `navigation_types` | fractions | navigate, navigate_cache, reload, etc. |
| `form_factors` | fractions | desktop/phone/tablet distribution |

### Response

```json
{
  "record": {
    "key": { "origin": "https://example.com" },
    "metrics": {
      "largest_contentful_paint": {
        "histogram": [
          { "start": 0, "end": 2500, "density": 0.72 },
          { "start": 2500, "end": 4000, "density": 0.18 },
          { "start": 4000, "density": 0.10 }
        ],
        "percentiles": { "p75": 2100 }
      },
      "cumulative_layout_shift": {
        "percentiles": { "p75": "0.05" }
      }
    },
    "collectionPeriod": {
      "firstDate": { "year": 2026, "month": 2, "day": 27 },
      "lastDate": { "year": 2026, "month": 3, "day": 26 }
    }
  }
}
```

### Important
- **CLS p75 is a string** (e.g., `"0.05"` not `0.05`). Always parse as float from string.
- Last histogram bin has **no `end`** (extends to infinity).
- Densities sum to approximately 1.0.
- **404** = no data (insufficient Chrome traffic). Not an auth error.
- Updated daily ~04:00 UTC with ~2 day lag.

### Rate Limits
- 150 QPM shared between CrUX and CrUX History APIs
- Free, no paid increase available

---

## CrUX History API (Weekly)

**Endpoint:** `POST https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord?key={API_KEY}`

Same request format as CrUX API. Returns up to **25 weekly collection periods**.

### Response Differences from CrUX API

Instead of single values, returns timeseries:

```json
{
  "record": {
    "metrics": {
      "largest_contentful_paint": {
        "histogramTimeseries": [
          { "start": 0, "end": 2500, "densities": [0.70, 0.71, 0.72, ...] },
          { "start": 2500, "end": 4000, "densities": [0.19, 0.18, 0.18, ...] },
          { "start": 4000, "densities": [0.11, 0.11, 0.10, ...] }
        ],
        "percentilesTimeseries": {
          "p75s": [2200, 2150, 2100, ...]
        }
      }
    },
    "collectionPeriods": [
      {
        "firstDate": { "year": 2025, "month": 9, "day": 29 },
        "lastDate": { "year": 2025, "month": 10, "day": 26 }
      },
      ...
    ]
  }
}
```

### NaN Handling
- `"NaN"` string for densities in ineligible periods
- `null` for percentile values in ineligible periods
- Always check for these before numeric operations

### Update Schedule
- Updated **Mondays** ~04:00 UTC
- Each period = 28-day rolling average ending on a Sunday

---

## Core Web Vitals Thresholds

Current as of March 2026. INP replaced FID on March 12, 2024.

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** | ≤ 2,500ms | 2,500–4,000ms | > 4,000ms |
| **INP** | ≤ 200ms | 200–500ms | > 500ms |
| **CLS** | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| **FCP** | ≤ 1,800ms | 1,800–3,000ms | > 3,000ms |
| **TTFB** | ≤ 800ms | 800–1,800ms | > 1,800ms |

FID was fully removed from Chrome tools (CrUX, PSI, Lighthouse) on September 9, 2024. Never reference FID in outputs.
```

## File: `skills/seo-google/references/rate-limits-quotas.md`
```markdown
# Google API Rate Limits & Quotas

## Consolidated Quota Table

| API | Per-Minute | Per-Day | Cost | Auth Type | Scope |
|-----|-----------|---------|------|-----------|-------|
| GSC Search Analytics | 1,200 QPM/user, 1,200 QPM/site | 30M QPD/project | Free | Service Account | Per user + per site |
| GSC URL Inspection | 600 QPM/site | 2,000 QPD/site | Free | Service Account | Per site |
| GSC Sitemaps | Standard | Standard | Free | Service Account | Per site |
| PageSpeed Insights v5 | 240 QPM | 25,000 QPD | Free | API Key | Per project |
| CrUX API | 150 QPM (shared) | Unlimited | Free | API Key | Per project |
| CrUX History API | 150 QPM (shared with CrUX) | Unlimited | Free | API Key | Per project |
| Indexing API | 380 RPM total, 180 read/min | 200 publish/day | Free | Service Account | Per project |
| GA4 Data API | 10 concurrent | ~25K tokens/day | Free | Service Account | Per property/project |
| Knowledge Graph | -- | 100,000 QPD | Free | API Key | Per project |
| Custom Search | -- | 10,000 QPD max | 100 free, $5/1K | API Key | Per project |
| Web Risk | 6,000 QPM | 100K/month | Free tier | API Key | Per project |

**Key distinction:** "Per site" quotas are scoped to a specific GSC property. "Per project" quotas are shared across all properties in a GCP project. "Per user" quotas are per authenticated user (service account).

## Exponential Backoff Strategy

When receiving 429 or 5xx errors:

```
Attempt 1: wait 1 second
Attempt 2: wait 2 seconds
Attempt 3: wait 4 seconds
Attempt 4: wait 8 seconds
Attempt 5: wait 16 seconds
Max: give up after 5 retries
```

Add random jitter (0-500ms) to each wait to avoid thundering herd.

## Common Error Codes

| Code | Meaning | Applies To | Action |
|------|---------|------------|--------|
| 400 | Bad request | All | Check URL format, request body |
| 401 | Unauthorized | Service Account APIs | Refresh credentials |
| 403 | Forbidden | GSC, GA4, Indexing | Check permissions (service account access) |
| 404 | Not found | CrUX, GSC | Insufficient traffic (CrUX) or invalid property (GSC) |
| 429 | Rate limited | All | Backoff and retry. Check Retry-After header. |
| 500 | Server error | All | Retry with backoff |
| 503 | Service unavailable | All | Retry with backoff |

## Retry-After Header

Some Google APIs return a `Retry-After` header with 429 responses. When present, use this value (in seconds) instead of exponential backoff.

## GA4 Token Budgeting

GA4 uses a token system rather than simple request counts:
- Simple 1-dimension, 1-metric report: ~1-5 tokens
- Complex multi-dimension, multi-metric: ~10-100 tokens
- Set `returnPropertyQuota: true` to monitor consumption
- Daily limit: 25,000 tokens per property per project
- Hourly limit: 5,000 tokens per property per project
- Concurrent: max 10 simultaneous requests

## CrUX Shared Quota

The CrUX API and CrUX History API share the same 150 QPM quota per project. Plan accordingly if querying both APIs in the same workflow.

## Cost Summary

**All APIs used by seo-google are free** at normal usage levels. No billing is required for:
- PSI, CrUX, CrUX History (API key, unlimited free)
- GSC (service account, 30M QPD)
- Indexing API (service account, 200 publish/day)
- GA4 Data API (service account, 25K tokens/day)
- Knowledge Graph (API key, 100K QPD)

Only Custom Search and Web Risk have paid tiers at high volumes.
```

## File: `skills/seo-google/references/search-console-api.md`
```markdown
# Google Search Console API Reference

## Table of Contents
1. [Search Analytics API](#search-analytics-api)
2. [URL Inspection API](#url-inspection-api)
3. [Sitemaps API](#sitemaps-api)
4. [Sites API](#sites-api)

---

## Search Analytics API

**Endpoint:** `POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query`

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| `startDate` | string | Required. YYYY-MM-DD format. |
| `endDate` | string | Required. YYYY-MM-DD format. |
| `dimensions` | string[] | `query`, `page`, `country`, `device`, `date`, `searchAppearance` |
| `type` | string | `web` (default), `image`, `video`, `news`, `discover`, `googleNews` |
| `dimensionFilterGroups` | object[] | Array of filter groups (see below) |
| `aggregationType` | string | `auto` (default), `byPage`, `byProperty`, `byNewsShowcasePanel` |
| `rowLimit` | int | 1-25000 (default: 1000) |
| `startRow` | int | Pagination offset (default: 0) |
| `dataState` | string | `final` (default), `all`, `hourly_all` |

### Dimension Filters

```json
{
  "dimensionFilterGroups": [{
    "filters": [{
      "dimension": "query",
      "operator": "contains",
      "expression": "seo"
    }]
  }]
}
```

**Operators:** `contains`, `equals`, `notContains`, `notEquals`, `includingRegex`, `excludingRegex`
- Regex uses RE2 syntax, max 4096 characters

### Response

```json
{
  "rows": [
    {
      "keys": ["seo tools", "https://example.com/tools"],
      "clicks": 150,
      "impressions": 5000,
      "ctr": 0.03,
      "position": 4.2
    }
  ],
  "responseAggregationType": "byPage"
}
```

### Important Notes
- Data has a **2-3 day lag**. Available for approximately 16 months.
- `discover` and `googleNews` types do not support `query` dimension or `position` metric.
- Country codes are **ISO 3166-1 alpha-3** (e.g., `USA`, `GBR`, `DEU`).
- Pagination: increment `startRow` by `rowLimit` until fewer rows returned.

### Rate Limits
- 1,200 QPM per user
- 1,200 QPM per site
- 40,000 QPM / 30,000,000 QPD per project

---

## URL Inspection API

**Endpoint:** `POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`

### Request

```json
{
  "inspectionUrl": "https://example.com/page",
  "siteUrl": "sc-domain:example.com",
  "languageCode": "en"
}
```

### Response Fields

**`indexStatusResult`:**

| Field | Values |
|-------|--------|
| `verdict` | `PASS`, `FAIL`, `NEUTRAL`, `PARTIAL`, `VERDICT_UNSPECIFIED` |
| `coverageState` | Human-readable coverage description |
| `robotsTxtState` | `ALLOWED`, `DISALLOWED` |
| `indexingState` | `INDEXING_ALLOWED`, `BLOCKED_BY_META_TAG`, `BLOCKED_BY_HTTP_HEADER` |
| `pageFetchState` | `SUCCESSFUL`, `SOFT_404`, `BLOCKED_ROBOTS_TXT`, `NOT_FOUND`, `ACCESS_DENIED`, `SERVER_ERROR`, `REDIRECT_ERROR`, `ACCESS_FORBIDDEN`, `BLOCKED_4XX`, `INTERNAL_CRAWL_ERROR`, `INVALID_URL` |
| `lastCrawlTime` | ISO 8601 timestamp |
| `googleCanonical` | URL Google selected as canonical |
| `userCanonical` | URL declared canonical by the page |
| `crawledAs` | `DESKTOP`, `MOBILE` |

**`richResultsResult`:** Verdict + detected rich result types (FAQPage, HowTo, etc.)

### Rate Limits
- 2,000 QPD / 600 QPM per site
- 10,000,000 QPD / 15,000 QPM per project

---

## Sitemaps API

**Base:** `https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/sitemaps`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/sitemaps` | List all sitemaps |
| `GET` | `/sitemaps/{feedpath}` | Get specific sitemap |
| `PUT` | `/sitemaps/{feedpath}` | Submit a sitemap |
| `DELETE` | `/sitemaps/{feedpath}` | Delete a sitemap |

### Sitemap Resource

| Field | Description |
|-------|-------------|
| `path` | URL of the sitemap |
| `lastSubmitted` | Last submission timestamp |
| `isPending` | Whether processing is incomplete |
| `isSitemapsIndex` | Whether this is a sitemap index |
| `type` | `sitemap`, `atomFeed`, `rssFeed`, `urlList`, `notSitemap` |
| `warnings` | Warning count |
| `errors` | Error count |
| `contents[]` | Array with `type` (web, image, video, news) and `submitted` count |

---

## Sites API

**Base:** `https://www.googleapis.com/webmasters/v3/sites`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/sites` | List all verified properties |
| `GET` | `/sites/{siteUrl}` | Get property info |
| `PUT` | `/sites/{siteUrl}` | Add a property |
| `DELETE` | `/sites/{siteUrl}` | Remove a property |

### Property Resource

| Field | Values |
|-------|--------|
| `siteUrl` | Property URL (e.g., `sc-domain:example.com`) |
| `permissionLevel` | `siteOwner`, `siteFullUser`, `siteRestrictedUser`, `siteUnverifiedUser` |
```

## File: `skills/seo-google/references/supplementary-apis.md`
```markdown
# Supplementary Google APIs for SEO

## Knowledge Graph Search API

Verify brand/entity presence in Google's Knowledge Graph.

**Endpoint:** `GET https://kgsearch.googleapis.com/v1/entities:search`

| Param | Description |
|-------|-------------|
| `query` | Search query |
| `ids` | Specific entity IDs (e.g., `/m/0d6lp`) |
| `languages` | Language codes (e.g., `en`) |
| `types` | Schema.org types to filter (e.g., `Organization`, `Person`) |
| `limit` | Max results (1-500) |
| `key` | API key (required) |

**Response:**
```json
{
  "itemListElement": [{
    "result": {
      "@id": "kg:/m/0d6lp",
      "name": "Google",
      "@type": ["Organization", "Corporation"],
      "description": "Technology company",
      "detailedDescription": {
        "articleBody": "Google LLC is an American...",
        "url": "https://en.wikipedia.org/wiki/Google"
      },
      "image": { "url": "..." },
      "url": "https://www.google.com"
    },
    "resultScore": 4892.5
  }]
}
```

**Use for SEO:** Verify if a brand has a Knowledge Panel, check entity disambiguation, find related entities.

**Quota:** 100,000 reads/day. Free. API key only.

---

## Custom Search JSON API

Programmatic Google search results (limited).

**Endpoint:** `GET https://customsearch.googleapis.com/customsearch/v1`

| Param | Description |
|-------|-------------|
| `key` | API key (required) |
| `cx` | Programmable Search Engine ID (required) |
| `q` | Search query |
| `num` | Results per page (1-10) |
| `start` | Start index (max 91) |
| `dateRestrict` | Date restriction (e.g., `d30` for 30 days) |
| `gl` | Country (e.g., `us`) |
| `lr` | Language restriction |
| `searchType` | `image` for image search |
| `siteSearch` | Restrict to a domain |

**Limitations:**
- Max 100 total results per query (10 pages x 10 results)
- **CLOSED to new customers as of 2025.** Existing customers must migrate by January 2027.
- 100 queries/day free, $5 per 1,000 up to 10,000/day

**For SERP data, prefer DataForSEO** (`/seo dataforseo serp`) which has no such limitations.

---

## Web Risk API

Check if URLs are flagged as unsafe by Google Safe Browsing.

**Endpoint:** `GET https://webrisk.googleapis.com/v1/uris:search`

| Param | Description |
|-------|-------------|
| `threatTypes` | `MALWARE`, `SOCIAL_ENGINEERING`, `UNWANTED_SOFTWARE`, `SOCIAL_ENGINEERING_EXTENDED_COVERAGE` |
| `uri` | URL to check |
| `key` | API key (required) |

**Response (clean URL):** Empty threat object.

**Response (flagged URL):**
```json
{
  "threat": {
    "threatTypes": ["MALWARE"],
    "expireTime": "2026-04-01T00:00:00Z"
  }
}
```

**Use for SEO:** Check if pages are flagged (could explain deindexing), verify competitor safety, audit outbound links.

**Quota:** 6,000 QPM. 100,000/month free tier. Requires billing enabled on GCP project.
```

## File: `skills/seo-google/references/youtube-api.md`
```markdown
# YouTube Data API v3 Reference

YouTube mentions have the strongest correlation with AI visibility (0.737 per GEO research). This API provides authoritative YouTube data directly from Google.

## Endpoints Used

| Method | Quota Cost | Description |
|--------|-----------|-------------|
| `search.list` | 100 units | Search for videos matching a query |
| `videos.list` | 1 unit | Get video details, statistics, content |
| `channels.list` | 1 unit | Get channel info, subscriber count |
| `commentThreads.list` | 1 unit | Get top comments on a video |

## Daily Quota

Default: **10,000 units/day** (free). This allows:
- ~100 searches per day, OR
- ~10,000 video/channel lookups per day

## Data Available

### Video Search
- Title, channel, channel ID, published date
- Description (first 300 chars), thumbnail URL
- Views, likes, comments count, duration

### Video Details
- Full description, tags, category ID
- Duration, definition (HD/SD), has captions
- Topic categories (Wikipedia URLs)
- Views, likes, comments, favorites
- Top 10 relevant comments with likes

### Channel Info
- Title, description, custom URL
- Subscriber count, video count, total views
- Country, published date, thumbnail

## Authentication

**API key only** (read-only public data). No OAuth needed.

## Enable the API

1. Go to [console.cloud.google.com/apis/library](https://console.cloud.google.com/apis/library)
2. Search for "YouTube Data API v3"
3. Click Enable

No billing required. The API key you already have for PSI/CrUX works.
```

## File: `skills/seo-hreflang/SKILL.md`
```markdown
---
name: seo-hreflang
description: >
  Hreflang and international SEO audit, validation, and generation. Detects
  common mistakes, validates language/region codes, and generates correct
  hreflang implementations. Use when user says "hreflang", "i18n SEO",
  "international SEO", "multi-language", "multi-region", or "language tags".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Hreflang & International SEO

Validate existing hreflang implementations or generate correct hreflang tags
for multi-language and multi-region sites. Supports HTML, HTTP header, and
XML sitemap implementations.

## Validation Checks

### 1. Self-Referencing Tags
- Every page must include an hreflang tag pointing to itself
- The self-referencing URL must exactly match the page's canonical URL
- Missing self-referencing tags cause Google to ignore the entire hreflang set

### 2. Return Tags
- If page A links to page B with hreflang, page B must link back to page A
- Every hreflang relationship must be bidirectional (A→B and B→A)
- Missing return tags invalidate the hreflang signal for both pages
- Check all language versions reference each other (full mesh)

### 3. x-default Tag
- Required: designates the fallback page for unmatched languages/regions
- Typically points to the language selector page or English version
- Only one x-default per set of alternates
- Must also have return tags from all other language versions

### 4. Language Code Validation
- Must use ISO 639-1 two-letter codes (e.g., `en`, `fr`, `de`, `ja`)
- Common errors:
  - `eng` instead of `en` (ISO 639-2, not valid for hreflang)
  - `jp` instead of `ja` (incorrect code for Japanese)
  - `zh` without region qualifier (ambiguous; use `zh-Hans` or `zh-Hant`)

### 5. Region Code Validation
- Optional region qualifier uses ISO 3166-1 Alpha-2 (e.g., `en-US`, `en-GB`, `pt-BR`)
- Format: `language-REGION` (lowercase language, uppercase region)
- Common errors:
  - `en-uk` instead of `en-GB` (UK is not a valid ISO 3166-1 code)
  - `es-LA` (Latin America is not a country; use specific countries)
  - Region without language prefix

### 6. Canonical URL Alignment
- Hreflang tags must only appear on canonical URLs
- If a page has `rel=canonical` pointing elsewhere, hreflang on that page is ignored
- The canonical URL and hreflang URL must match exactly (including trailing slashes)
- Non-canonical pages should not be in any hreflang set

### 7. Protocol Consistency
- All URLs in an hreflang set must use the same protocol (HTTPS or HTTP)
- Mixed HTTP/HTTPS in hreflang sets causes validation failures
- After HTTPS migration, update all hreflang tags to HTTPS

### 8. Cross-Domain Support
- Hreflang works across different domains (e.g., example.com and example.de)
- Cross-domain hreflang requires return tags on both domains
- Verify both domains are verified in Google Search Console
- Sitemap-based implementation recommended for cross-domain setups

## Common Mistakes

| Issue | Severity | Fix |
|-------|----------|-----|
| Missing self-referencing tag | Critical | Add hreflang pointing to same page URL |
| Missing return tags (A→B but no B→A) | Critical | Add matching return tags on all alternates |
| Missing x-default | High | Add x-default pointing to fallback/selector page |
| Invalid language code (e.g., `eng`) | High | Use ISO 639-1 two-letter codes |
| Invalid region code (e.g., `en-uk`) | High | Use ISO 3166-1 Alpha-2 codes |
| Hreflang on non-canonical URL | High | Move hreflang to canonical URL only |
| HTTP/HTTPS mismatch in URLs | Medium | Standardize all URLs to HTTPS |
| Trailing slash inconsistency | Medium | Match canonical URL format exactly |
| Hreflang in both HTML and sitemap | Low | Choose one method (sitemap preferred for large sites) |
| Language without region when needed | Low | Add region qualifier for geo-targeted content |

## Implementation Methods

### Method 1: HTML Link Tags
Best for: Sites with <50 language/region variants per page.

```html
<link rel="alternate" hreflang="en-US" href="https://example.com/page" />
<link rel="alternate" hreflang="en-GB" href="https://example.co.uk/page" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

Place in `<head>` section. Every page must include all alternates including itself.

### Method 2: HTTP Headers
Best for: Non-HTML files (PDFs, documents).

```
Link: <https://example.com/page>; rel="alternate"; hreflang="en-US",
      <https://example.com/fr/page>; rel="alternate"; hreflang="fr",
      <https://example.com/page>; rel="alternate"; hreflang="x-default"
```

Set via server configuration or CDN rules.

### Method 3: XML Sitemap (Recommended for large sites)
Best for: Sites with many language variants, cross-domain setups, or 50+ pages.

See Hreflang Sitemap Generation section below.

### Method Comparison
| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| HTML link tags | Small sites (<50 variants) | Easy to implement, visible in source | Bloats `<head>`, hard to maintain at scale |
| HTTP headers | Non-HTML files | Works for PDFs, images | Complex server config, not visible in HTML |
| XML sitemap | Large sites, cross-domain | Scalable, centralized management | Not visible on page, requires sitemap maintenance |

## Hreflang Generation

### Process
1. **Detect languages**: Scan site for language indicators (URL path, subdomain, TLD, HTML lang attribute)
2. **Map page equivalents**: Match corresponding pages across languages/regions
3. **Validate language codes**: Verify all codes against ISO 639-1 and ISO 3166-1
4. **Generate tags**: Create hreflang tags for each page including self-referencing
5. **Verify return tags**: Confirm all relationships are bidirectional
6. **Add x-default**: Set fallback for each page set
7. **Output**: Generate implementation code (HTML, HTTP headers, or sitemap XML)

## Hreflang Sitemap Generation

### Sitemap with Hreflang
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
  <url>
    <loc>https://example.com/fr/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
</urlset>
```

Key rules:
- Include the `xmlns:xhtml` namespace declaration
- Every `<url>` entry must include ALL language alternates (including itself)
- Each alternate must appear as a separate `<url>` entry with its own full set
- Split at 50,000 URLs per sitemap file

## Output

### Hreflang Validation Report

#### Summary
- Total pages scanned: XX
- Language variants detected: XX
- Issues found: XX (Critical: X, High: X, Medium: X, Low: X)

#### Validation Results
| Language | URL | Self-Ref | Return Tags | x-default | Status |
|----------|-----|----------|-------------|-----------|--------|
| en-US | https://... | ✅ | ✅ | ✅ | ✅ |
| fr | https://... | ❌ | ⚠️ | ✅ | ❌ |
| de | https://... | ✅ | ❌ | ✅ | ❌ |

### Generated Hreflang Tags
- HTML `<link>` tags (if HTML method chosen)
- HTTP header values (if header method chosen)
- `hreflang-sitemap.xml` (if sitemap method chosen)

### Recommendations
- Missing implementations to add
- Incorrect codes to fix
- Method migration suggestions (e.g., HTML to sitemap for scale)

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site structure. Suggest the user verify the URL and try again. |
| No hreflang tags found | Report the absence. Check for other internationalization signals (subdirectories, subdomains, ccTLDs) and recommend the appropriate hreflang implementation method. |
| Invalid language/region codes detected | List each invalid code with the correct replacement. Provide a corrected hreflang tag set ready to implement. |
```

## File: `skills/seo-image-gen/SKILL.md`
```markdown
---
name: seo-image-gen
description: "AI image generation for SEO assets: OG/social preview images, blog hero images, schema images, product photography, infographics. Powered by Gemini via nanobanana-mcp. Requires banana extension installed. Use when user says \"generate image\", \"OG image\", \"social preview\", \"hero image\", \"blog image\", \"product photo\", \"infographic\", \"seo image\", \"create visual\", \"image-gen\", \"favicon\", \"schema image\", \"pinterest pin\", \"generate visual\", \"banner\", or \"thumbnail\"."
argument-hint: "[og|hero|product|infographic|custom|batch] <description>"
user-invokable: true
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
compatibility: "Requires nanobanana MCP server"
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# SEO Image Gen: AI Image Generation for SEO Assets (Extension)

Generate production-ready images for SEO use cases using Gemini's image generation
via the banana Creative Director pipeline. Maps SEO needs to optimized domain modes,
aspect ratios, and resolution defaults.

## Architecture Note

This extension is built on [Claude Banana](https://github.com/AgriciDaniel/banana-claude),
the standalone AI image generation skill for Claude Code.

This skill has two components with distinct roles:
- **SKILL.md** (this file): Handles interactive `/seo image-gen` commands for generating images
- **Agent** (`agents/seo-image-gen.md`): Audit-only analyst spawned during `/seo audit` to assess existing OG/social images and produce a generation plan (never auto-generates)

## Prerequisites

This skill requires the banana extension to be installed:
```bash
./extensions/banana/install.sh
```

**Check availability:** Before using any image generation tool, verify the MCP server
is connected by checking if `gemini_generate_image` or `set_aspect_ratio` tools are
available. If tools are not available, inform the user the extension is not installed
and provide install instructions.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo image-gen og <description>` | Generate OG/social preview image (1200x630 feel) |
| `/seo image-gen hero <description>` | Blog hero image (widescreen, dramatic) |
| `/seo image-gen product <description>` | Product photography (clean, white BG) |
| `/seo image-gen infographic <description>` | Infographic visual (vertical, data-heavy) |
| `/seo image-gen custom <description>` | Custom image with full Creative Director pipeline |
| `/seo image-gen batch <description> [N]` | Generate N variations (default: 3) |

## SEO Image Use Cases

Each use case maps to pre-configured banana parameters:

| Use Case | Aspect Ratio | Resolution | Domain Mode | Notes |
|----------|-------------|------------|-------------|-------|
| **OG/Social Preview** | `16:9` | `1K` | Product or UI/Web | Clean, professional, text-friendly |
| **Blog Hero** | `16:9` | `2K` | Cinema or Editorial | Dramatic, atmospheric, editorial quality |
| **Schema Image** | `4:3` | `1K` | Product | Clean, descriptive, schema ImageObject |
| **Social Square** | `1:1` | `1K` | UI/Web | Platform-optimized square |
| **Product Photo** | `4:3` | `2K` | Product | White background, studio lighting |
| **Infographic** | `2:3` | `4K` | Infographic | Data-heavy, vertical layout |
| **Favicon/Icon** | `1:1` | `512` | Logo | Minimal, scalable, recognizable |
| **Pinterest Pin** | `2:3` | `2K` | Editorial | Tall vertical card |

## Generation Pipeline

For every generation request:

1. **Identify use case** from command or context (og, hero, product, etc.)
2. **Apply SEO defaults** from the use cases table above
3. **Set aspect ratio** via `set_aspect_ratio` MCP tool
4. **Construct Reasoning Brief** using the banana Creative Director pipeline:
   - Load `references/prompt-engineering.md` for the 6-component system
   - Apply domain mode emphasis (Subject 30%, Style 25%, Context 15%, etc.)
   - Be SPECIFIC and VISCERAL: describe what the camera sees
5. **Generate** via `gemini_generate_image` MCP tool
6. **Post-generation SEO checklist** (see below)

### Check for Presets

If the user mentions a brand or has SEO presets configured:
```bash
python3 ~/.claude/skills/seo-image-gen/scripts/presets.py list
```
Load matching preset and apply as defaults. Also check `references/seo-image-presets.md`
for SEO-specific preset templates.

## Post-Generation SEO Checklist

After every successful generation, guide the user on:

1. **Alt text**:Write descriptive, keyword-rich alt text for the generated image
2. **File naming**:Rename to SEO-friendly format: `keyword-description-widthxheight.webp`
3. **WebP conversion**:Convert to WebP for optimal page speed:
   ```bash
   magick output.png -quality 85 output.webp
   ```
4. **File size**:Target under 200KB for hero images, under 100KB for thumbnails
5. **Schema markup**:Suggest `ImageObject` schema for the generated image:
   ```json
   {
     "@type": "ImageObject",
     "url": "https://example.com/images/keyword-description.webp",
     "width": 1200,
     "height": 630,
     "caption": "Descriptive caption with target keyword"
   }
   ```
6. **OG meta tags**:For social preview images, remind about:
   ```html
   <meta property="og:image" content="https://example.com/images/og-image.webp" />
   <meta property="og:image:width" content="1200" />
   <meta property="og:image:height" content="630" />
   <meta property="og:image:alt" content="Descriptive alt text" />
   ```

## Cost Awareness

Image generation costs money. Be transparent:
- Show estimated cost before generating (especially for batch)
- Log every generation: `python3 ~/.claude/skills/seo-image-gen/scripts/cost_tracker.py log --model MODEL --resolution RES --prompt "brief"`
- Run `cost_tracker.py summary` if user asks about usage

Approximate costs (gemini-3.1-flash):
- 512: ~$0.02/image
- 1K resolution: ~$0.04/image
- 2K resolution: ~$0.08/image
- 4K resolution: ~$0.16/image

## Model Routing

| Scenario | Model | Why |
|----------|-------|-----|
| OG images, social previews | `gemini-3.1-flash-image-preview` @ 1K | Fast, cost-effective |
| Hero images, product photos | `gemini-3.1-flash-image-preview` @ 2K | Quality + detail |
| Infographics with text | `gemini-3.1-flash-image-preview` @ 2K, thinking: high | Better text rendering |
| Quick drafts | `gemini-2.5-flash-image` @ 512 | Rapid iteration |

## Error Handling

| Error | Resolution |
|-------|-----------|
| MCP not configured | Run `./extensions/banana/install.sh` |
| API key invalid | New key at https://aistudio.google.com/apikey |
| Rate limited (429) | Wait 60s, retry. Free tier: ~10 RPM / ~500 RPD |
| `IMAGE_SAFETY` | Rephrase prompt - see `references/prompt-engineering.md` Safety section |
| MCP unavailable | Fall back: `python3 ~/.claude/skills/seo-image-gen/scripts/generate.py --prompt "..." --aspect-ratio "16:9"` |
| Extension not installed | Show install instructions: `./extensions/banana/install.sh` |

## Cross-Skill Integration

- **seo-images** (analysis) feeds into **seo-image-gen** (generation): audit results from `/seo images` identify missing or low-quality images; use those findings to drive `/seo image-gen` commands
- **seo-audit** spawns the seo-image-gen **agent** (not this skill) to analyze OG/social images across the site and produce a prioritized generation plan
- **seo-schema** can consume generated images: after generation, suggest `ImageObject` schema markup pointing to the new assets

## Reference Documentation

Load on-demand. Do NOT load all at startup:
- `references/prompt-engineering.md`:6-component system, domain modes, templates
- `references/gemini-models.md`:Model specs, rate limits, capabilities
- `references/mcp-tools.md`:MCP tool parameters and responses
- `references/post-processing.md`:ImageMagick/FFmpeg pipeline recipes
- `references/cost-tracking.md`:Pricing, usage tracking
- `references/presets.md`:Brand preset management
- `references/seo-image-presets.md`:SEO-specific preset templates

## Response Format

After generating, always provide:
1. **Image path**:where it was saved
2. **Crafted prompt**:show what was sent to the API (educational)
3. **Settings**:model, aspect ratio, resolution
4. **SEO checklist**:alt text suggestion, file naming, WebP conversion
5. **Schema snippet**:ImageObject or og:image markup if applicable
```

## File: `skills/seo-image-gen/references/cost-tracking.md`
```markdown
# Cost Tracking Reference

> Load this on-demand when the user asks about costs or before batch operations.

## Pricing Table

| Model | Resolution | Cost/Image | Notes |
|-------|-----------|-----------|-------|
| 3.1 Flash | 512 | $0.020 | Quick drafts |
| 3.1 Flash | 1K | $0.039 | Standard (default) |
| 3.1 Flash | 2K | $0.078 | Quality assets |
| 3.1 Flash | 4K | $0.156 | Print/hero images |
| 2.5 Flash | 512 | $0.020 | Draft fallback |
| 2.5 Flash | 1K | $0.039 | Standard fallback |
| Batch API | Any | 50% of above | Asynchronous, higher latency |

Pricing is approximate, based on ~1,290 output tokens per image.
Research suggests actual costs may be ~$0.067/img. Verify at https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/pricing

## Free Tier Limits

- ~10 requests per minute (RPM)
- ~500 requests per day (RPD)
- Per Google Cloud project, resets midnight Pacific

## Cost Tracker Commands

```bash
# Log a generation
cost_tracker.py log --model gemini-3.1-flash-image-preview --resolution 1K --prompt "coffee shop hero"

# View summary (total + last 7 days)
cost_tracker.py summary

# Today's usage
cost_tracker.py today

# Estimate before batch
cost_tracker.py estimate --model gemini-3.1-flash-image-preview --resolution 1K --count 10

# Reset ledger
cost_tracker.py reset --confirm
```

## Storage

Ledger stored at `~/.banana/costs.json`. Created automatically on first use.
```

## File: `skills/seo-image-gen/references/gemini-models.md`
```markdown
# Gemini Image Generation Models

> Last updated: 2026-03-13
> Aligned with Google's March 2026 API state

## Available Models

### gemini-3.1-flash-image-preview (Recommended)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-3.1-flash-image-preview` |
| **Tier** | Nano Banana 2 (Flash) |
| **Speed** | Fast - optimized for high-volume use |
| **Aspect Ratios** | All 14 ratios (see table below) |
| **Max Resolution** | Up to 4096×4096 (4K tier) |
| **Features** | Google Search grounding (web + image), thinking levels, image-only output, extreme aspect ratios |
| **Rate Limits (Free)** | ~10 RPM / ~500 RPD (per Google Cloud project, resets midnight Pacific) |
| **Output Tokens** | ~1,290 output tokens per image |
| **Best For** | Most use cases, rapid iteration, batch generation |

### gemini-2.5-flash-image
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-2.5-flash-image` |
| **Tier** | Nano Banana 2 (Flash, previous gen) |
| **Speed** | Fast |
| **Aspect Ratios** | 1:1, 16:9, 9:16, 4:3, 3:4 |
| **Max Resolution** | Up to 1024×1024 (1K tier) |
| **Rate Limits (Free)** | ~10 RPM / ~500 RPD |
| **Best For** | Stable fallback, proven quality |

## Deprecated Models (DO NOT USE)

### gemini-3-pro-image-preview
- **Status:** Base model deprecated March 9, 2026. **Image generation variant may still be accessible**. Use at your own discretion via `set_model`. Prefer 3.1 Flash.
- **Was:** Nano Banana Pro tier (professional asset production, 4K output, 14 reference images)
- **Migration:** Use `gemini-3.1-flash-image-preview` instead

### gemini-2.0-flash-exp
- **Status:** Deprecated, replaced by gemini-2.5-flash-image

## Aspect Ratios

All 14 supported ratios. Availability varies by model:

| Ratio | Orientation | Use Cases | 3.1 Flash | 2.5 Flash |
|-------|-------------|-----------|:---------:|:---------:|
| `1:1` | Square | Social posts, avatars, thumbnails | ✅ | ✅ |
| `16:9` | Landscape | Blog headers, YouTube thumbnails, presentations | ✅ | ✅ |
| `9:16` | Portrait | Stories, Reels, TikTok, mobile | ✅ | ✅ |
| `4:3` | Landscape | Product shots, classic display | ✅ | ✅ |
| `3:4` | Portrait | Book covers, portrait framing | ✅ | ✅ |
| `2:3` | Portrait | Pinterest pins, posters | ✅ | ❌ |
| `3:2` | Landscape | DSLR standard, photo prints | ✅ | ❌ |
| `4:5` | Portrait | Instagram portrait, social | ✅ | ❌ |
| `5:4` | Landscape | Large format photography | ✅ | ❌ |
| `1:4` | Tall strip | Vertical banners, side panels | ✅ | ❌ |
| `4:1` | Wide strip | Website banners, headers | ✅ | ❌ |
| `1:8` | Extreme tall | Narrow vertical strips | ✅ | ❌ |
| `8:1` | Extreme wide | Ultra-wide banners | ✅ | ❌ |
| `21:9` | Ultra-wide | Cinematic, film-grade, ultra-wide monitors | ✅ | ❌ |

## Resolution Tiers

Control output resolution with the `imageSize` parameter. Note the **uppercase K** requirement.

| `imageSize` Value | Pixel Range | Model Availability | Use Case |
|-------------------|-------------|-------------------|----------|
| `512` | Up to 512×512 | All models | Drafts, quick iteration, low bandwidth |
| `1K` (default) | Up to 1024×1024 | All models | Standard web use, social media |
| `2K` | Up to 2048×2048 | 3.1 Flash | Quality assets, detailed work |
| `4K` | Up to 4096×4096 | 3.1 Flash | Print production, hero images, final assets |

**Notes:**
- Actual pixel dimensions depend on aspect ratio (e.g., 4K at 16:9 = 4096×2304)
- Higher resolutions consume more tokens and cost more
- Default is `1K` if `imageSize` is not specified

## API Configuration

### Endpoint
```
https://generativelanguage.googleapis.com/v1beta/models/{model-id}:generateContent
```

### Required Parameters
```json
{
  "contents": [{"parts": [{"text": "your prompt here"}]}],
  "generationConfig": {
    "responseModalities": ["TEXT", "IMAGE"],
    "imageConfig": {
      "aspectRatio": "16:9",
      "imageSize": "1K"
    }
  }
}
```

### Image-Only Output Mode
Force the model to return only an image (no text response):
```json
{
  "generationConfig": {
    "responseModalities": ["IMAGE"]
  }
}
```

### Thinking Level
Control how much the model "thinks" before generating. Higher levels improve complex compositions but increase latency:
```json
{
  "generationConfig": {
    "thinkingConfig": {
      "thinkingLevel": "medium"
    }
  }
}
```
Levels: `minimal`, `low`, `medium`, `high`

### Google Search Grounding
Ground generation in real-world visual references. Supports web and image search (3.1 Flash):
```json
{
  "tools": [{"googleSearch": {}}]
}
```
**Prompt pattern:** `[Search/source request] + [Analytical task] + [Visual translation]`

Example: "Search for the latest SpaceX Starship design, analyze its proportions and markings, then generate a photorealistic image of it at sunset on the launch pad."

### Multi-Image Input
Up to 14 reference images can be provided:
- **10 object references**: for style, composition, or visual matching
- **4 character references**: assign distinct names to preserve features across generations

Useful for character consistency, style transfer, and brand-aligned generation.

## Rate Limits by Tier

| Tier | RPM | RPD | Notes |
|------|-----|-----|-------|
| Free | ~10 | ~500 | Per Google Cloud project, resets midnight Pacific. Reduced Dec 2025. |
| Pay-as-you-go | 30 | 10,000 | Production workloads |
| Enterprise | Custom | Custom | Contact Google |

## Pricing

| Model | Resolution | Cost per Image | Notes |
|-------|-----------|---------------|-------|
| 3.1 Flash | 1K | ~$0.039 | Standard |
| 3.1 Flash | 2K | ~$0.078 | 2× standard |
| 3.1 Flash | 4K | ~$0.156 | 4× standard |
| 2.5 Flash | 1K | ~$0.039 | Standard |
| Batch API | Any | 50% discount | Asynchronous, higher latency |

Pricing is approximate and based on ~1,290 output tokens per image.
Research suggests NB2 pricing may be ~$0.067/img (vs documented $0.039). Verify current pricing at https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/pricing

## Image Output Specs

| Property | Value |
|----------|-------|
| **Format** | PNG |
| **Max Resolution** | Up to 4096×4096 (4K tier, 3.1 Flash) |
| **Color Space** | sRGB |
| **Text Rendering** | Supported - best under 25 characters |
| **Style Control** | Via prompt engineering |

## Safety Filters

Gemini uses a two-layer safety architecture:

1. **Input filters**: block prompts containing prohibited content before generation
2. **Output filters**: analyze generated images and block unsafe results

| `finishReason` | Meaning | Retryable? |
|----------------|---------|:----------:|
| `STOP` | Successful generation | N/A |
| `IMAGE_SAFETY` | Output blocked by safety filter | Rephrase prompt |
| `PROHIBITED_CONTENT` | Content policy violation | No - topic is blocked |
| `SAFETY` | General safety block | Rephrase prompt |
| `RECITATION` | Detected copyrighted content | Rephrase prompt |

**Known issue:** Filters are known to be overly cautious. Benign prompts may be blocked. Iterate with rephrased wording if this happens.

## Content Credentials

- **SynthID watermarks** are always embedded in generated images (invisible, machine-readable)
- **C2PA metadata** is included on Pro/paid outputs (verifiable provenance chain)

## Key Limitations
- No video generation (image only)
- No transparent backgrounds (PNG but always with background)
- Text rendering quality varies; keep text under 25 characters for best results
- Safety filters may block some prompts (violence, NSFW, public figures), known to be overly cautious
- Session context resets between Claude Code conversations
- `imageSize` and thinking level depend on MCP package version support
```

## File: `skills/seo-image-gen/references/mcp-tools.md`
```markdown
# MCP Tools Reference: @ycse/nanobanana-mcp

> Package: `@ycse/nanobanana-mcp`
> GitHub: https://github.com/YCSE/nanobanana-mcp

## Tools

### gemini_generate_image
Generate an image from a text prompt.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | string | Yes | Text description of the image to generate |

**Returns:** Image data + file path (saved to `~/Documents/nanobanana_generated/`)

**Example usage in Claude Code:**
```
User: "Generate a sunset over mountains in watercolor style"
→ Claude calls gemini_generate_image with prompt
→ Returns image path and description
```

### gemini_edit_image
Edit an existing image with text instructions.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `imagePath` | string | Yes | Path to the image file to edit |
| `prompt` | string | Yes | Edit instructions |

**Returns:** Modified image data + file path

**Example:**
```
User: "Remove the background from ~/Documents/photo.png"
→ Claude calls gemini_edit_image with path and instruction
```

### gemini_chat
Multi-turn visual conversation maintaining session context.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | Chat message (can reference previous images) |

**Returns:** Text response + optional image

**Key feature:** Session consistency, which maintains style, characters, and context across turns. Great for iterative refinement.

### set_aspect_ratio
Configure the aspect ratio for subsequent image generations.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `ratio` | string | Yes | Aspect ratio (e.g., "16:9", "1:1", "9:16") |

**Supported ratios:** 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 4:5, 5:4, 1:4, 4:1, 1:8, 8:1, 21:9

### set_model
Switch the active Gemini model.

**Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Model identifier |

**Available models:**
- `gemini-3.1-flash-image-preview` (default, recommended)
- `gemini-2.5-flash-image` (stable fallback)

### get_image_history
Retrieve list of images generated in the current session.

**Parameters:** None

**Returns:** Array of image entries with paths and prompts

### clear_conversation
Reset session context and conversation history.

**Parameters:** None

**Returns:** Confirmation of reset

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_AI_API_KEY` | Yes | API key from https://aistudio.google.com/apikey |
| `NANOBANANA_MODEL` | No | Override default model (default: `gemini-3.1-flash-image-preview`) |

## Output Directory
All generated images are saved to: `~/Documents/nanobanana_generated/`

Images are named with timestamps for easy identification.

## Feature Availability via MCP

Some newer Gemini API features depend on the MCP package version of `@ycse/nanobanana-mcp`. Check the package version to confirm support:

| Feature | API Status | MCP Support |
|---------|-----------|-------------|
| `imageSize` (resolution control) | Available | Depends on package version |
| Thinking level (`thinkingConfig`) | Available | Depends on package version |
| Search grounding (`googleSearch`) | Available | Depends on package version |
| Image-only output (`responseModalities: ["IMAGE"]`) | Available | Depends on package version |
| Multi-image input (up to 14 refs) | Available | Via `gemini_chat` with image paths |
| All 14 aspect ratios | Available | Via `set_aspect_ratio` |

If a feature is not yet supported by the MCP package, you can still use it via direct API calls with `curl` or the Google AI SDK.
```

## File: `skills/seo-image-gen/references/post-processing.md`
```markdown
# Post-Processing Pipeline Reference

> Load this on-demand when the user needs image manipulation after generation.

## Prerequisites

Check availability before using:
```bash
which magick    # ImageMagick 7 (preferred)
which convert   # ImageMagick 6 (fallback)
which ffmpeg    # For video/animation
```

Install ImageMagick if not present: `sudo apt install imagemagick` (Debian/Ubuntu) or `brew install imagemagick` (macOS).

## Common Operations

### Resize for Platforms

```bash
# Instagram post (1080x1080)
magick input.png -resize 1080x1080^ -gravity center -extent 1080x1080 instagram.png

# Twitter/X header (1500x500)
magick input.png -resize 1500x500^ -gravity center -extent 1500x500 twitter-header.png

# YouTube thumbnail (1280x720)
magick input.png -resize 1280x720^ -gravity center -extent 1280x720 youtube-thumb.png

# LinkedIn banner (1584x396)
magick input.png -resize 1584x396^ -gravity center -extent 1584x396 linkedin-banner.png

# Favicon (multi-size ICO)
magick input.png -resize 32x32 favicon.ico
```

### Background Removal (Transparency)

```bash
# Remove solid white background
magick input.png -fuzz 10% -transparent white output.png

# Remove solid color background (specify color)
magick input.png -fuzz 15% -transparent "#F0F0F0" output.png

# Clean edges after transparency (anti-alias)
magick input.png -fuzz 10% -transparent white -channel A -blur 0x1 -level 50%,100% output.png

# Auto-crop transparent padding
magick input.png -trim +repage output.png
```

### Format Conversion

```bash
# PNG to WebP (web-optimized, smaller file)
magick input.png -quality 85 output.webp

# PNG to JPEG (with white background for transparency)
magick input.png -background white -flatten -quality 90 output.jpg

# PNG to AVIF (modern, smallest size)
magick input.png -quality 80 output.avif

# SVG trace (for logos; requires potrace)
potrace input.pbm -s -o output.svg
```

### Color Adjustments

```bash
# Increase contrast
magick input.png -contrast-stretch 2%x1% output.png

# Warm color temperature
magick input.png -modulate 100,110,105 output.png

# Cool color temperature
magick input.png -modulate 100,90,95 output.png

# Desaturate (muted colors)
magick input.png -modulate 100,70,100 output.png

# Convert to grayscale
magick input.png -colorspace Gray output.png

# Sepia tone
magick input.png -sepia-tone 80% output.png
```

### Compositing

```bash
# Overlay watermark (bottom-right, 20% opacity)
magick base.png watermark.png -gravity southeast -geometry +20+20 \
  -compose dissolve -define compose:args=20 -composite output.png

# Side-by-side comparison
magick input1.png input2.png +append comparison.png

# Vertical stack
magick input1.png input2.png -append stack.png

# Add padding/border
magick input.png -bordercolor white -border 40 output.png

# Add rounded corners
magick input.png \( +clone -alpha extract -draw \
  "roundrectangle 0,0,%[fx:w-1],%[fx:h-1],20,20" \) \
  -alpha off -compose CopyOpacity -composite rounded.png
```

### Batch Processing

```bash
# Resize all PNGs in directory
for f in ~/Documents/nanobanana_generated/*.png; do
  magick "$f" -resize 800x800 "${f%.png}_thumb.png"
done

# Convert all to WebP
for f in ~/Documents/nanobanana_generated/*.png; do
  magick "$f" -quality 85 "${f%.png}.webp"
done
```

## Animation (GIF/Video from Multiple Frames)

```bash
# Create GIF from multiple images
magick -delay 100 frame1.png frame2.png frame3.png animation.gif

# Create MP4 from image sequence
ffmpeg -framerate 1 -pattern_type glob -i '*.png' \
  -c:v libx264 -pix_fmt yuv420p slideshow.mp4
```

## Note on 4K Output

With Gemini 3.1 Flash's `imageSize: "4K"` option (up to 4096×4096), many traditional
upscaling post-processing steps are no longer necessary. If your target platform accepts
images at or below 4K resolution, generate at native 4K instead of generating at 1K
and upscaling. This produces better detail and avoids upscaling artifacts.

## Green Screen Transparency Pipeline

Gemini cannot generate transparent backgrounds. Use this workaround:

### 1. Generate with green screen prompt

Append to any prompt:
```
on a solid bright green (#00FF00) chroma key background
with a thin white outline separating the subject from the background
```

### 2. Remove green screen (ImageMagick)

```bash
magick input.png -fuzz 20% -transparent "#00FF00" output.png
```

### 3. Clean edges + trim (ImageMagick)

```bash
magick output.png -channel A -blur 0x1 -level 50%,100% -trim +repage final.png
```

### 4. Alternative (FFmpeg, better for batch)

```bash
ffmpeg -i input.png -vf "colorkey=0x00FF00:0.3:0.1,despill=type=green" -pix_fmt rgba output.png
```

### Tips
- `-fuzz 20%` handles slight color variations at edges; increase to 25% for softer edges
- The white outline in the prompt helps prevent color spill on subject edges
- For batch processing, the FFmpeg approach is faster and handles despill automatically
- Always verify edges after conversion; may need manual touchup for hair/fur

## Quality Assessment

```bash
# Get image dimensions and info
magick identify -verbose input.png | head -20

# Check file size
ls -lh input.png

# Get exact pixel dimensions
magick identify -format "%wx%h" input.png
```
```

## File: `skills/seo-image-gen/references/presets.md`
```markdown
# Brand/Style Presets Reference

> Load this on-demand when the user asks about presets or brand consistency.

## Preset Schema

Each preset is stored as `~/.banana/presets/NAME.json`:

```json
{
  "name": "tech-saas",
  "description": "Clean tech SaaS brand",
  "colors": ["#2563EB", "#1E40AF", "#F8FAFC"],
  "style": "clean minimal tech illustration, flat vectors, soft shadows",
  "typography": "bold geometric sans-serif",
  "lighting": "bright diffused studio, no harsh shadows",
  "mood": "professional, trustworthy, modern",
  "default_ratio": "16:9",
  "default_resolution": "2K"
}
```

## Example Presets

### tech-saas
- **Colors:** #2563EB, #1E40AF, #F8FAFC (blue + white)
- **Style:** Clean minimal tech illustration, flat vectors, soft shadows
- **Typography:** Bold geometric sans-serif
- **Mood:** Professional, trustworthy, modern

### luxury-brand
- **Colors:** #1A1A1A, #C9A96E, #FAFAF5 (black + gold + cream)
- **Style:** Elegant high-end photography, rich textures, deep contrast
- **Typography:** Thin elegant serif, generous letter-spacing
- **Mood:** Exclusive, sophisticated, aspirational

### editorial-magazine
- **Colors:** #000000, #FFFFFF, #FF3B30 (black + white + accent red)
- **Style:** Bold editorial photography, strong geometric composition
- **Typography:** Condensed all-caps sans-serif headlines
- **Mood:** Bold, provocative, contemporary

## How Presets Merge into Reasoning Brief

When a preset is active, Claude uses its values as defaults for the Reasoning Brief:
1. **Colors** → inform palette descriptions in Context and Style components
2. **Style** → becomes the base for the Style component
3. **Typography** → used for any text rendering
4. **Lighting** → becomes the base for the Lighting component
5. **Mood** → influences Action and Context components

User instructions always override preset values. If a user says "make it dark"
but the preset has bright lighting, follow the user's instruction.

## Managing Presets

```bash
# List presets
presets.py list

# Show details
presets.py show tech-saas

# Create interactively (Claude fills in details from conversation)
presets.py create NAME --colors "#hex,#hex" --style "..." --mood "..."

# Delete
presets.py delete NAME --confirm
```
```

## File: `skills/seo-image-gen/references/prompt-engineering.md`
```markdown
# Prompt Engineering Reference: Claude Banana

> Load this on-demand when constructing complex prompts or when the user
> asks about prompt techniques. Do NOT load at startup.
>
> Aligned with Google's March 2026 "Ultimate Prompting Guide" for Gemini image generation.

## The 6-Component Reasoning Brief

Every image prompt should contain these components, written as natural
narrative paragraphs, NEVER as comma-separated keyword lists.

### 1. Subject
The main focus of the image. Describe with physical specificity.

**Good:** "A weathered Japanese ceramicist in his 70s, deep sun-etched
wrinkles mapping decades of kiln work, calloused hands cradling a
freshly thrown tea bowl with an irregular, organic rim"

**Bad:** "old man, ceramic, bowl"

### 2. Action
What is happening. Movement, pose, gesture, state of being.

**Good:** "leaning forward with intense concentration, gently smoothing
the rim with a wet thumb, a thin trail of slip running down his wrist"

**Bad:** "making pottery"

### 3. Context
Environment, setting, temporal and spatial details.

**Good:** "inside a traditional wood-fired anagama kiln workshop,
stacked shelves of drying pots visible in the soft background, late
afternoon light filtering through rice paper screens"

**Bad:** "workshop, afternoon"

### 4. Composition
Camera angle, shot type, framing, spatial relationships.

**Good:** "intimate close-up shot from slightly below eye level,
shallow depth of field isolating the hands and bowl against the
soft bokeh of the workshop behind"

**Bad:** "close up"

### 5. Lighting
Light source, quality, direction, temperature, shadows.

**Good:** "warm directional light from a single high window camera-left,
creating gentle Rembrandt lighting on the face with a soft triangle
of light on the shadow-side cheek, deep warm shadows in the workshop"

**Bad:** "natural lighting"

### 6. Style
Art medium, aesthetic reference, technical photographic details.

**Good:** "captured with a Sony A7R IV, 85mm f/1.4 GM lens, Kodak Portra
400 color grading with lifted shadows and muted earth tones, reminiscent
of Dorothea Lange's documentary portraiture"

**Bad:** "photorealistic, 8K, masterpiece"

## Domain Mode Modifier Libraries

### Cinema Mode
**Camera specs:** RED V-Raptor, ARRI Alexa 65, Sony Venice 2, Blackmagic URSA
**Lenses:** Cooke S7/i, Zeiss Supreme Prime, Atlas Orion anamorphic
**Film stocks:** Kodak Vision3 500T (tungsten), Kodak Vision3 250D (daylight), Fuji Eterna Vivid
**Lighting setups:** three-point, chiaroscuro, Rembrandt, split, butterfly, rim/backlight
**Shot types:** establishing wide, medium close-up, extreme close-up, Dutch angle, overhead crane, Steadicam tracking
**Color grading:** teal and orange, desaturated cold, warm vintage, high-contrast noir

### Product Mode
**Surfaces:** polished marble, brushed concrete, raw linen, acrylic riser, gradient sweep
**Lighting:** softbox diffused, hard key with fill card, rim separation, tent lighting, light painting
**Angles:** 45-degree hero, flat lay, three-quarter, straight-on, worm's-eye
**Style refs:** Apple product photography, Aesop minimal, Bang & Olufsen clean, luxury cosmetics

### Portrait Mode
**Focal lengths:** 85mm (classic), 105mm (compression), 135mm (telephoto), 50mm (environmental)
**Apertures:** f/1.4 (dreamy bokeh), f/2.8 (subject-sharp), f/5.6 (environmental context)
**Pose language:** candid mid-gesture, direct-to-camera confrontational, profile silhouette, over-shoulder glance
**Skin/texture:** freckles visible, pores at macro distance, catch light in eyes, subsurface scattering

### Editorial/Fashion Mode
**Publication refs:** Vogue Italia, Harper's Bazaar, GQ, National Geographic, Kinfolk
**Styling notes:** layered textures, statement accessories, monochromatic palette, contrast patterns
**Locations:** marble staircase, rooftop at golden hour, industrial loft, desert dunes, neon-lit alley
**Poses:** power stance, relaxed editorial lean, movement blur, fabric in wind

### UI/Web Mode
**Styles:** flat vector, isometric 3D, line art, glassmorphism, neumorphism, material design
**Colors:** specify exact hex or descriptive palette (e.g., "cool blues #2563EB to #1E40AF")
**Sizing:** design at 2x for retina, specify exact pixel dimensions needed
**Backgrounds:** transparent (request solid white then post-process), gradient, solid color

### Logo Mode
**Construction:** geometric primitives, golden ratio, grid-based, negative space
**Typography:** bold sans-serif, elegant serif, custom lettermark, monogram
**Colors:** max 2-3 colors, works in monochrome, high contrast
**Output:** request on solid white background, post-process to transparent

### Landscape Mode
**Depth layers:** foreground interest, midground subject, background atmosphere
**Atmospherics:** fog, mist, haze, volumetric light rays, dust particles
**Time of day:** blue hour (pre-dawn), golden hour, magic hour (post-sunset), midnight blue
**Weather:** dramatic storm clouds, clearing after rain, snow-covered, sun-dappled

### Infographic Mode
**Layout:** modular sections, clear visual hierarchy, bento grid, flow top-to-bottom
**Text:** use quotes for exact text, descriptive font style, specify size hierarchy
**Data viz:** bar charts, pie charts, flow diagrams, timelines, comparison tables
**Colors:** high-contrast, accessible palette, consistent brand colors

### Abstract Mode
**Geometry:** fractals, voronoi tessellation, spirals, fibonacci, organic flow, crystalline
**Textures:** marble veining, fluid dynamics, smoke wisps, ink diffusion, watercolor bleed
**Color palettes:** analogous harmony, complementary clash, monochromatic gradient, neon-on-black
**Styles:** generative art, data visualization art, glitch, procedural, macro photography of materials

## Advanced Techniques

### Character Consistency (Multi-turn)
Use `gemini_chat` and maintain descriptive anchors:
- First turn: Generate character with exhaustive physical description
- Following turns: Reference "the same character" + repeat 2-3 key identifiers
- Key identifiers: hair color/style, distinctive clothing, facial feature

**Multi-image reference technique** (3.1 Flash):
- Provide up to 4-5 character reference images in the conversation
- Assign distinct names to each character ("Character A: the red-haired knight")
- Model preserves features across different angles, actions, and environments
- Works best when reference images show the character from multiple angles

### Style Transfer Without Reference Images
Describe the target style exhaustively instead of referencing an image:
```
Render this scene in the style of a 1950s travel poster: flat areas of
color in a limited palette of teal, coral, and cream. Bold geometric
shapes with visible paper texture. Hand-lettered title text with a
mid-century modern typeface feel.
```

### Text Rendering Tips
- Quote exact text: `with the text "OPEN DAILY" in bold condensed sans-serif`
- **25 characters or less**:this is the practical limit for reliable rendering
- **2-3 distinct phrases max**:more text fragments degrade quality
- Describe font characteristics, not font names
- Specify placement: "centered at the top third", "along the bottom edge"
- High contrast: light text on dark, or vice versa
- **Text-first hack:** Establish the text concept conversationally first ("I need a sign that says FRESH BREAD"), then generate. The model anchors on text mentioned early
- Expect creative font interpretations, not exact replication of described styles

### Positive Framing (No Negative Prompts)
Gemini does NOT support negative prompts. Rephrase exclusions:
- Instead of "no blur" → "sharp, in-focus, tack-sharp detail"
- Instead of "no people" → "empty, deserted, uninhabited"
- Instead of "no text" → "clean, uncluttered, text-free"
- Instead of "not dark" → "brightly lit, high-key lighting"

### Search-Grounded Generation
For images based on real-world data (weather, events, statistics),
Gemini can use Google Search grounding to incorporate live information.
Useful for infographics with current data.

**Three-part formula for search-grounded prompts:**
1. `[Source/Search request`:What to look up
2. `[Analytical task`:What to analyze or extract
3. `[Visual translation`:How to render it as an image

**Example:** "Search for the current top 5 programming languages by GitHub usage in 2026, analyze their relative popularity percentages, then generate a clean infographic bar chart with the language logos and percentages in a modern dark theme."

## Prompt Adaptation Rules

When adapting prompts from the claude-prompts database (Midjourney/DALL-E/etc.)
to Gemini's natural language format:

| Source Syntax | Gemini Equivalent |
|---------------|-------------------|
| `--ar 16:9` | Call `set_aspect_ratio("16:9")` separately |
| `--v 6`, `--style raw` | Remove - Gemini has no version/style flags |
| `--chaos 50` | Describe variety: "unexpected, surreal composition" |
| `--no trees` | Positive framing: "open clearing with no vegetation" |
| `(word:1.5)` weight | Descriptive emphasis: "prominently featuring [word]" |
| `8K, masterpiece, ultra-detailed` | Keep only "ultra-realistic, high resolution"; remove the rest |
| Comma-separated tags | Expand into descriptive narrative paragraphs |
| `shot on Hasselblad` | Keep - camera specs work well in Gemini |

## Common Prompt Mistakes

1. **Keyword stuffing**:stacking generic quality terms ("8K, masterpiece, best quality") adds nothing. Use only "ultra-realistic, high resolution" at the end
2. **Tag lists**:Gemini wants prose, not "red car, sunset, mountain, cinematic"
3. **Missing lighting**:The single biggest quality differentiator
4. **No composition direction**:Results in generic centered framing
5. **Vague style**:"make it look cool" vs specific art direction
6. **Ignoring aspect ratio**:Always set before generating
7. **Overlong prompts**:Diminishing returns past ~200 words; be precise, not verbose
8. **Text longer than ~25 characters**:Rendering degrades rapidly past this limit
9. **Burying key details at the end**:In long prompts, details placed last may be deprioritized; put critical specifics (exact text, key constraints) in the first third of the prompt
10. **Not iterating with follow-up prompts**:Use `gemini_chat` for progressive refinement instead of trying to get everything right in one generation

## Proven Prompt Templates

> Extracted from 2,500+ tested prompts. These patterns consistently produce
> high-quality results. Use them as starting points and adapt to the request.

### The Winning Formula (Weight Distribution)

| Component | Weight | What to include |
|-----------|--------|-----------------|
| **Subject** | 40% | Age, skin tone, hair color/style, eye color, body type, expression |
| **Styling** | 25% | Brand names, textures, fit, accessories, colors |
| **Environment** | 15% | Location + time of day + context details |
| **Camera** | 10% | Camera model + lens + focal length + shot type |
| **Lighting** | 10% | Quality, direction, color temperature, shadows |

### Instagram Ad / Social Media

**Pattern:** `[Subject with age/appearance] + [outfit with brand/texture] + [action verb] + [setting] + [camera spec] + [lighting] + [platform aesthetic]`

**Example (Product Placement):**
```
Hyper-realistic gym selfie of athletic 24yo influencer with glowing olive
skin, wearing crinkle-textured athleisure set in mauve. iPhone 16 Pro Max
front-facing portrait mode capturing sweat droplets on collarbones, hazel
eyes enhanced by gym LED lighting. Mirror reflection shows perfect form,
golden morning light through floor-to-ceiling windows. Frayed chestnut
ponytail with baby hairs, ultra-detailed skin texture, trending aesthetic.
```

**Example (Lifestyle Ad):**
```
A 24-year-old blonde fitness model in a high-energy sports drink
advertisement. Mid-run on a beach, wearing a vibrant orange sports bra
and black shorts, playful smile and sparkling blue eyes exuding vitality.
Bottle of the drink held in hand, waves crashing in background. Shot on
Nikon D850 with 70-200mm f/2.8 lens, natural light, fast shutter speed
capturing motion. Ultra-realistic skin texture, water droplets, product
label clearly visible.
```

**Example (Luxury Lifestyle):**
```
Gorgeous Instagram model wearing a designer silk gown, luxury rooftop
restaurant, golden hour lighting, champagne in hand, luxurious aspirational
lifestyle. Captured with Sony A7R IV, 85mm f/1.4 lens, shallow depth of
field, warm color grading.
```

### Product / Commercial Photography

**Pattern:** `[Product with brand/detail] + [dynamic elements] + [surface/setting] + "commercial photography for advertising campaign" + [lighting] + "high resolution"`

**Example (Beverage):**
```
Gatorade bottle with condensation dripping down the sides, surrounded by
lightning bolts and a burst of vibrant blue and orange light rays. The
Gatorade logo is prominently displayed on the bottle, with splashes of
water frozen in mid-air. Commercial food photography for an advertising
campaign, high resolution, high level of detail, vibrant complementary
colors.
```

**Example (Food):**
```
In and Out burger with layers of fresh lettuce, melted cheese, and pretzel
bun, placed on a white surface with the In and Out logo subtly glowing in
the background. Falling french fries and golden light, warm scene.
Commercial food photography for an advertising campaign, high resolution,
high level of detail, vibrant complementary colors.
```

### Fashion / Editorial

**Pattern:** `[Subject with ethnicity/age/features] + [outfit with texture/brand/cut] + [location] + [pose/action] + [camera + lens] + [lighting quality]`

**Example (Street Style):**
```
A 24-year-old female AI influencer posing confidently in an urban cityscape
during golden hour. Flawless sun-kissed skin, long wavy brown hair, deep
green eyes. Wearing a chic streetwear outfit: oversized beige blazer,
white top, high-waisted jeans. Captured with Sony A7R IV at 85mm f/1.4,
shallow depth of field with warm golden bokeh.
```

**Example (High Fashion):**
```
Stunning 24-year-old woman, long platinum blonde hair, radiant skin,
piercing blue eyes, dressed in a chic pastel blazer with a modern
minimalist aesthetic, soft sunlight glow, high-end fashion appeal.
Shot on Canon EOS R5, 85mm f/1.2 lens.
```

**Example (Avant-Garde):**
```
A blonde fitness model transformed into a runway-ready fashion icon,
wearing a bold avant-garde outfit: cropped leather jacket with neon pink
accents, paired with high-waisted athletic shorts and knee-high boots.
Captured mid-stride on a minimalist white runway, playful twinkle in her
eye, dramatic studio lighting from above.
```

### SaaS / Tech Marketing

**Pattern:** `[UI mockup or abstract visual] + "on [dark/light] background" + [specific colors with hex] + [typography description] + "clean, premium SaaS aesthetic" + [glassmorphism/gradient/glow effects]`

**Example (Dashboard Hero):**
```
A floating glassmorphism UI card on a deep charcoal background showing a
content analytics dashboard with a rising line graph in teal (#14B8A6),
bar charts in coral (#F97316), and a circular progress indicator at 94%.
Subtle grid lines, frosted glass effect with 20% opacity, teal glow
bleeding from the card edges. Clean premium SaaS aesthetic, no text
smaller than headline size.
```

**Example (Feature Highlight):**
```
An isometric 3D illustration of interconnected data nodes on a dark navy
background. Each node is a glowing teal sphere connected by thin luminous
lines, forming a constellation pattern. One central node pulses brighter
with radiating rings. Modern tech illustration style with subtle depth
of field, volumetric lighting from below.
```

**Example (Comparison/Before-After):**
```
Split-screen image: left side shows a cluttered, dim workspace with
scattered papers, red error indicators, and a frustrated expression
conveyed through a cracked coffee mug and tangled cables. Right side
shows a clean, organized dashboard interface glowing in teal and white
on a dark background, with smooth flowing lines and checkmarks. A sharp
vertical dividing line separates chaos from clarity.
```

### Logo / Branding

**Pattern:** `[Product/bottle/item] + "with [brand element] prominently displayed" + [dynamic visual elements] + "commercial photography" + [lighting style] + "high resolution, vibrant complementary colors"`

**Example:**
```
A sleek matte black bottle with a minimal white logo mark centered on the
label, surrounded by swirling gradient ribbons of teal and coral light.
The bottle sits on a reflective dark surface, sharp studio rim lighting
separating it from the background. Product photography for luxury
branding, high resolution, dramatic contrast.
```

### Key Tactics That Make Prompts Work

1. **Name real cameras**:"Sony A7R IV", "Canon EOS R5", "iPhone 16 Pro Max" anchor realism
2. **Specify exact lens**:"85mm f/1.4" gives the model precise depth-of-field information
3. **Use age + ethnicity + features**:"24yo with olive skin, hazel eyes" beats "a person"
4. **Name brands for styling**:"Lululemon mat", "Tom Ford suit" triggers specific visual associations
5. **Include micro-details**:"sweat droplets on collarbones", "baby hairs stuck to neck"
6. **Add platform context**:"Instagram aesthetic", "commercial photography for advertising"
7. **Describe textures**:"crinkle-textured", "metallic silver", "frosted glass"
8. **Use action verbs**:"mid-run", "posing confidently", "captured mid-stride"
9. **End with "ultra-realistic, high resolution"**:these two specific anchors help on Gemini. Avoid generic stacking like "8K, masterpiece, best quality" which adds no value
10. **For products, say "prominently displayed"**:ensures the product/logo isn't hidden

### Anti-Patterns (What NOT to Do)

- **"A dark-themed Instagram ad showing..."**:too meta, describes the concept not the image
- **"A sleek SaaS dashboard visualization..."**:abstract, no visual anchors
- **"Modern, clean, professional..."**:vague adjectives that mean nothing to the model
- **"A bold call to action with..."**:describes marketing intent, not visual content
- **Describing what the viewer should feel**:instead, describe what creates that feeling

## Safety Filter Rephrase Strategies

Gemini's safety filters (Layer 2: server-side output filter) cannot be disabled.
When a prompt is blocked, the only path forward is rephrasing.

### Common Trigger Categories

| Category | Triggers on | Rephrase approach |
|----------|------------|-------------------|
| Violence/weapons | Combat, blood, injuries, firearms | Use metaphor or aftermath: "battle-worn" → "weathered veteran" |
| Medical/gore | Surgery, wounds, anatomical detail | Abstract or clinical: "open wound" → "medical illustration" |
| Real public figures | Named celebrities, politicians | Use archetypes: "Elon Musk" → "a tech entrepreneur in a minimalist office" |
| Children + risk | Minors in any ambiguous context | Add safety context: specify educational, family, or playful framing |
| NSFW/suggestive | Revealing clothing, intimate poses | Use artistic framing: "fashion editorial, fully clothed, editorial pose" |

### Rephrase Patterns

1. **Abstraction**:Replace specific dangerous elements with abstract concepts
2. **Artistic framing**:Frame content as art, editorial, or documentary
3. **Metaphor**:Use symbolic language instead of literal descriptions
4. **Positive emphasis**:Describe what IS present, not what's dangerous
5. **Context shift**:Move from threatening to educational/professional context

### Example Rephrases

| Blocked prompt | Successful rephrase |
|----------------|---------------------|
| "a soldier in combat firing a rifle" | "a determined soldier standing guard at dawn, rifle slung over shoulder, morning mist over the outpost" |
| "a scary horror monster" | "a fantastical creature from a dark fairy tale, intricate organic textures, bioluminescent accents, concept art style" |
| "dog in a fight" | "a friendly golden retriever playing energetically in a sunny park, action shot, joyful expression" |
| "medical surgery scene" | "a clean modern operating room viewed from the observation gallery, soft blue surgical lights, professional documentary style" |
| "celebrity portrait of [name]" | "a distinguished middle-aged man in a tailored navy suit, warm studio lighting, editorial portrait style" |

### Key Principle

Layer 2 (output filter) analyzes the generated image, not just the prompt.
Even well-phrased prompts can be blocked if the model's interpretation triggers
the output filter. When this happens, try shifting the visual concept further
from the trigger rather than just changing words.
```

## File: `skills/seo-image-gen/references/seo-image-presets.md`
```markdown
# SEO Image Presets

Pre-configured presets for common SEO image use cases. These map to banana's
preset format (see `references/presets.md` for schema details).

## Preset Templates

### og-default:Standard OG/Social Preview

```json
{
  "name": "og-default",
  "description": "Clean, professional OG image for social sharing",
  "aspect_ratio": "16:9",
  "resolution": "1K",
  "domain_mode": "Product",
  "style": {
    "colors": ["#FFFFFF", "#F5F5F5"],
    "mood": "Professional, clean, trustworthy",
    "lighting": "Bright, even studio lighting with soft shadows",
    "typography": "Modern sans-serif if text needed"
  },
  "post_processing": "magick output.png -resize 1200x630^ -gravity center -extent 1200x630 output-og.webp"
}
```

### blog-hero:Widescreen Blog Hero Image

```json
{
  "name": "blog-hero",
  "description": "Dramatic widescreen hero for blog posts",
  "aspect_ratio": "16:9",
  "resolution": "2K",
  "domain_mode": "Cinema",
  "style": {
    "colors": ["contextual"],
    "mood": "Dramatic, atmospheric, editorial",
    "lighting": "Golden hour or moody blue hour, directional",
    "typography": "None:image only"
  },
  "post_processing": "magick output.png -quality 85 output-hero.webp"
}
```

### product-white:E-commerce Product Shot

```json
{
  "name": "product-white",
  "description": "Clean white background product photography",
  "aspect_ratio": "4:3",
  "resolution": "2K",
  "domain_mode": "Product",
  "style": {
    "colors": ["#FFFFFF"],
    "mood": "Clean, professional, catalog-ready",
    "lighting": "360-degree soft studio lighting, minimal shadows",
    "typography": "None"
  },
  "prompt_suffix": "Studio product photography, clean white background, professional catalog shot, high resolution",
  "post_processing": "magick output.png -fuzz 5% -transparent white output-transparent.png"
}
```

### social-square:Social Media Square

```json
{
  "name": "social-square",
  "description": "1:1 square image for social media platforms",
  "aspect_ratio": "1:1",
  "resolution": "1K",
  "domain_mode": "UI/Web",
  "style": {
    "colors": ["brand-contextual"],
    "mood": "Engaging, scroll-stopping, platform-native",
    "lighting": "Bright, even, high-contrast",
    "typography": "Bold sans-serif if text needed, under 25 characters"
  }
}
```

### infographic-vertical:Data-Heavy Infographic

```json
{
  "name": "infographic-vertical",
  "description": "Tall vertical infographic for data visualization",
  "aspect_ratio": "2:3",
  "resolution": "4K",
  "domain_mode": "Infographic",
  "style": {
    "colors": ["brand-contextual", "data-visualization palette"],
    "mood": "Informative, structured, authoritative",
    "lighting": "Flat, even, no dramatic shadows",
    "typography": "Clear hierarchy:headline, subheads, body, captions"
  },
  "notes": "Use thinking: high for better text rendering accuracy"
}
```

### favicon-mark:Favicon / App Icon

```json
{
  "name": "favicon-mark",
  "description": "Minimal iconic mark for favicon or app icon",
  "aspect_ratio": "1:1",
  "resolution": "512",
  "domain_mode": "Logo",
  "style": {
    "colors": ["2-3 brand colors max"],
    "mood": "Minimal, recognizable, scalable",
    "lighting": "Flat, no shadows",
    "typography": "Single letter or symbol only"
  },
  "post_processing": "magick output.png -resize 32x32 favicon.ico && magick output.png -resize 180x180 apple-touch-icon.png"
}
```

## Creating Custom Presets

Users can create their own presets:
```bash
python3 ~/.claude/skills/seo-image-gen/scripts/presets.py create my-brand
```

This creates `~/.banana/presets/my-brand.json` with the full schema.
Custom presets override SEO defaults when specified.

## Preset Selection Logic

1. If user specifies a use case command (og, hero, product), load the matching preset
2. If user mentions a brand preset name, load from `~/.banana/presets/`
3. Brand presets override SEO presets for colors, mood, and typography
4. SEO presets always provide aspect ratio and resolution defaults
```

## File: `skills/seo-images/SKILL.md`
```markdown
---
name: seo-images
description: >
  Image optimization analysis for SEO and performance. Checks alt text, file
  sizes, formats, responsive images, lazy loading, and CLS prevention. Use when
  user says "image optimization", "alt text", "image SEO", "image size",
  or "image audit".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Image Optimization Analysis

## Checks

### Alt Text
- Present on all `<img>` elements (except decorative: `role="presentation"`)
- Descriptive: describes the image content, not "image.jpg" or "photo"
- Includes relevant keywords where natural, not keyword-stuffed
- Length: 10-125 characters

**Good examples:**
- "Professional plumber repairing kitchen sink faucet"
- "Red 2024 Toyota Camry sedan front view"
- "Team meeting in modern office conference room"

**Bad examples:**
- "image.jpg" (filename, not description)
- "plumber plumbing plumber services" (keyword stuffing)
- "Click here" (not descriptive)

### File Size

**Tiered thresholds by image category:**

| Image Category | Target | Warning | Critical |
|----------------|--------|---------|----------|
| Thumbnails | < 50KB | > 100KB | > 200KB |
| Content images | < 100KB | > 200KB | > 500KB |
| Hero/banner images | < 200KB | > 300KB | > 700KB |

Recommend compression to target thresholds where possible without quality loss.

### Format
| Format | Browser Support | Use Case |
|--------|-----------------|----------|
| WebP | 97%+ | Default recommendation |
| AVIF | 92%+ | Best compression, newer |
| JPEG | 100% | Fallback for photos |
| PNG | 100% | Graphics with transparency |
| SVG | 100% | Icons, logos, illustrations |

Recommend WebP/AVIF over JPEG/PNG. Check for `<picture>` element with format fallbacks.

#### Recommended `<picture>` Element Pattern

Use progressive enhancement with the most efficient format first:

```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Descriptive alt text" width="800" height="600" loading="lazy" decoding="async">
</picture>
```

The browser will use the first supported format. Current browser support: AVIF 93.8%, WebP 95.3%.

#### JPEG XL: Emerging Format

In November 2025, Google's Chromium team reversed its 2022 decision and announced it will restore JPEG XL support in Chrome using a Rust-based decoder. The implementation is feature-complete but not yet in Chrome stable. JPEG XL offers lossless JPEG recompression (~20% savings with zero quality loss) and competitive lossy compression. Not yet practical for web deployment, but worth monitoring for future adoption.

### Responsive Images
- `srcset` attribute for multiple sizes
- `sizes` attribute matching layout breakpoints
- Appropriate resolution for device pixel ratios

```html
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Description"
>
```

### Lazy Loading
- `loading="lazy"` on below-fold images
- Do NOT lazy-load above-fold/hero images (hurts LCP)
- Check for native vs JavaScript-based lazy loading

```html
<!-- Below fold - lazy load -->
<img src="photo.jpg" loading="lazy" alt="Description">

<!-- Above fold - eager load (default) -->
<img src="hero.jpg" alt="Hero image">
```

### `fetchpriority="high"` for LCP Images

Add `fetchpriority="high"` to your hero/LCP image to prioritize its download in the browser's network queue:

```html
<img src="hero.webp" fetchpriority="high" alt="Hero image description" width="1200" height="630">
```

**Critical:** Do NOT lazy-load above-the-fold/LCP images. Using `loading="lazy"` on LCP images directly harms LCP scores. Reserve `loading="lazy"` for below-the-fold images only.

### `decoding="async"` for Non-LCP Images

Add `decoding="async"` to non-LCP images to prevent image decoding from blocking the main thread:

```html
<img src="photo.webp" alt="Description" width="600" height="400" loading="lazy" decoding="async">
```

### CLS Prevention
- `width` and `height` attributes set on all `<img>` elements
- `aspect-ratio` CSS as alternative
- Flag images without dimensions

```html
<!-- Good - dimensions set -->
<img src="photo.jpg" width="800" height="600" alt="Description">

<!-- Good - CSS aspect ratio -->
<img src="photo.jpg" style="aspect-ratio: 4/3" alt="Description">

<!-- Bad - no dimensions -->
<img src="photo.jpg" alt="Description">
```

### File Names
- Descriptive: `blue-running-shoes.webp` not `IMG_1234.jpg`
- Hyphenated, lowercase, no special characters
- Include relevant keywords

### CDN Usage
- Check if images served from CDN (different domain, CDN headers)
- Recommend CDN for image-heavy sites
- Check for edge caching headers

## Output

### Image Audit Summary

| Metric | Status | Count |
|--------|--------|-------|
| Total Images | - | XX |
| Missing Alt Text | ❌ | XX |
| Oversized (>200KB) | ⚠️ | XX |
| Wrong Format | ⚠️ | XX |
| No Dimensions | ⚠️ | XX |
| Not Lazy Loaded | ⚠️ | XX |

### Prioritized Optimization List

Sorted by file size impact (largest savings first):

| Image | Current Size | Format | Issues | Est. Savings |
|-------|--------------|--------|--------|--------------|
| ... | ... | ... | ... | ... |

### Recommendations
1. Convert X images to WebP format (est. XX KB savings)
2. Add alt text to X images
3. Add dimensions to X images
4. Enable lazy loading on X below-fold images
5. Compress X oversized images

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL and checking if site requires authentication. |
| No images found on page | Report that no `<img>` elements were detected. Suggest checking if images are loaded via JavaScript or CSS background-image. |
| Images behind CDN or authentication | Note that image files could not be directly accessed for size analysis. Report available metadata (alt text, dimensions, format from markup) and flag inaccessible resources. |
```

## File: `skills/seo-local/SKILL.md`
```markdown
---
name: seo-local
description: >
  Local SEO analysis covering Google Business Profile optimization, NAP
  consistency, citation health, review signals, local schema markup,
  location page quality, multi-location SEO, and industry-specific
  recommendations. Detects business type (brick-and-mortar, SAB, hybrid)
  and industry vertical (restaurant, healthcare, legal, home services,
  real estate, automotive). Use when user says "local SEO", "Google
  Business Profile", "GBP", "map pack", "local pack", "citations",
  "NAP consistency", "local rankings", "service area", "multi-location",
  or "local search".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Local SEO Analysis (March 2026)

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| GBP signals share of local pack weight | 32% | Whitespark 2026 |
| Proximity share of ranking variance | 55.2% | Search Atlas ML study |
| Review signals share (up from 16%) | ~20% | Whitespark 2026 |
| Google searches seeking local info | 46% | Industry data |
| Mobile "near me" searches leading to visit in 24h | 76% | Google confirmed |
| ChatGPT/AI usage for local recommendations | 45% (up from 6%) | BrightLocal LCRS 2026 |
| ChatGPT local conversion rate | 15.9% | Seer Interactive |
| Google organic local conversion rate | 1.76% | Seer Interactive |
| Local pack ads growth (Jan 2025 to Jan 2026) | 1% to 22% | Sterling Sky |

---

## Business Type Detection

Detect from page signals before analysis. This determines which checks apply.

### Brick-and-Mortar
- Physical street address visible in page content or footer
- Google Maps embed with pin/directions
- "Visit us at", "Located at", "Come see us"
- Structured address in LocalBusiness schema

### Service Area Business (SAB)
- No visible physical address
- Service area mentions: "serving [city/region]", "service area includes"
- "We come to you", "On-site service", "Mobile [service]"
- `areaServed` in schema without `address.streetAddress`

### Hybrid
- Both physical address AND service area language present
- "Visit our showroom" combined with "We also serve [areas]"

**Impact on checks**: SABs skip embedded map verification and physical address consistency. Brick-and-mortar gets full NAP + map checks.

---

## Industry Vertical Detection

Detect from page signals and GBP category patterns. Routes to industry-specific checks from `references/local-schema-types.md`.

| Vertical | Detection Signals |
|----------|------------------|
| **Restaurant** | /menu, menu items, reservations, cuisine types, food ordering, "dine-in", "takeout" |
| **Healthcare** | insurance accepted, patients, appointments, NPI, medical terms, "Dr.", HIPAA notice |
| **Legal** | attorney, lawyer, practice areas, bar admission, case results, "free consultation" |
| **Home Services** | service area, emergency service, "free estimate", licensed/insured/bonded, "24/7" |
| **Real Estate** | listings, MLS, properties for sale/rent, agent bio, brokerage, "open house" |
| **Automotive** | inventory, VIN, test drive, dealership, service department, "new/used/certified" |

If no vertical detected, use generic `LocalBusiness` analysis path.

---

## Analysis Dimensions

### 1. GBP Signals (25%)

Primary category is the **single most important local pack factor** (Whitespark #1, score: 193). Incorrect primary category is the **#1 negative factor** (score: 176).

**Check for:**
- GBP embed or reference detectable on page (Maps iframe, place ID, reviews widget)
- Primary category appropriateness (infer from page content vs visible GBP data)
- Evidence of secondary categories (optimal: 4 additional per BrightLocal)
- GBP posts presence (no direct ranking impact per WebFX, but triggers Post Justifications)
- Photos/video evidence (45% more direction requests with photos, Agency Jet)
- Q&A content (deprecated Dec 2025, replaced by Ask Maps Gemini AI -- recommend recreating Q&A content as FAQ sections on website; GBP removed existing Q&A with no export available)
- Google Verified badge eligibility (replaced Guaranteed/Screened in Oct 2025)
- GBP link URL strategy: do NOT link to strongest website page (Sterling Sky Diversity Update -- risks suppressing organic rankings)
- Business hours visibility on page (businesses open at search time rank higher, factor #5)

**Scoring guide:**
- Full: GBP embed present, category signals align, posts active, photos present
- Partial: Some GBP signals present but incomplete
- Low: No visible GBP integration on website

### 2. Reviews & Reputation (20%)

Review velocity matters more than total count. The **18-day rule** (Sterling Sky): rankings cliff if no new reviews for 3 weeks.

**Check for:**
- Total Google review count visible on page or schema (magic threshold: 10, Sterling Sky)
- Star rating (31% of consumers only use 4.5+, 68% only use 4+, BrightLocal 2026)
- Review recency indicators (74% only care about reviews in last 3 months)
- `aggregateRating` in schema (ratingValue, reviewCount, bestRating)
- Third-party review presence (consumers use average of 6 review sites, BrightLocal 2026)
- Owner response patterns (88% would use business that responds, BrightLocal)
- Review gating detection: any pre-screening of satisfaction before directing to review platform is prohibited by Google (fake engagement policy) and FTC ($53,088/violation)

**Industry-specific:**
- Healthcare: HIPAA prohibits confirming/denying reviewer is a patient in responses
- Legal: attorney-client privilege considerations in review responses

**Scoring guide:**
- Full: 10+ reviews, 4.5+ stars, recent activity, owner responses, multi-platform presence
- Partial: Some reviews but gaps in recency, rating, or response rate
- Low: <10 reviews, no recent activity, no responses, single platform only

### 3. Local On-Page SEO (20%)

Dedicated service pages = **#1 local organic factor AND #2 AI visibility factor** (Whitespark 2026).

**Check for:**
- Title tag contains city/service keywords
- H1 tag with local intent (city + service)
- NAP (Name, Address, Phone) visible in page HTML (footer, contact section, header)
- Dedicated service pages (one page per core service)
- Location page quality for multi-location sites:
  - **>60-70% unique content** minimum (industry consensus, no Google-confirmed threshold)
  - **Swap test**: if you can swap the city name and content still makes sense, it's a doorway page (RicketyRoo method). HVAC company lost 80% rankings + 63% traffic after March 2024 Core Update for this pattern
  - Local photos, area-specific testimonials, local FAQs
- Embedded Google Map (geographic signal reinforcement, not direct ranking factor -- lazy-load to mitigate speed impact)
- Click-to-call button (`tel:` link) and contact form above the fold
- Internal linking architecture: hub-and-spoke, every critical page within 3 clicks of homepage
- 2-5 contextual internal links per 1,000 words with descriptive anchor text

**Multi-location specific:**
- Store locator with individual crawlable URLs (SSR/SSG preferred over CSR)
- Subdirectory structure: `domain.com/locations/city-name/` (subdirectories consolidate link equity better, Bruce Clay: 50%+ traffic lift)
- Each location page has unique LocalBusiness schema with `@id`

**Scoring guide:**
- Full: City in title + H1, NAP visible, dedicated service pages, no doorway patterns, good internal linking
- Partial: Some local signals but missing service pages or doorway page risk
- Low: Generic title/H1, NAP not visible, thin location pages

### 4. NAP Consistency & Citations (15%)

Citations declining for traditional pack rankings but **3 of top 5 AI visibility factors are citation-related** (Whitespark 2026). Google's July 2025 documentation update removed "directories" from prominence definition.

**Check for:**
- NAP extraction: compare Name, Address, Phone from:
  1. Visible page HTML (footer, contact page)
  2. LocalBusiness JSON-LD schema
  3. Any visible GBP data
  - Flag any discrepancies between these three sources
- Citation presence on Tier 1 directories (check via WebFetch or site: search patterns):
  - Google Business Profile signals on page
  - Yelp: `site:yelp.com "Business Name"`
  - BBB: `site:bbb.org "Business Name"`
  - Facebook business page references
- Apple Business Connect awareness (usage doubled to 27%, BrightLocal 2026 -- recommend claiming)
- Bing Places awareness (powers ChatGPT, Copilot, Alexa -- recommend claiming and optimizing)
- Industry-specific directory recommendations: load `references/local-schema-types.md` for per-vertical citation sources
- Data aggregator awareness: Data Axle, Foursquare, Neustar/TransUnion (recommend submission for downstream distribution)

**Scoring guide:**
- Full: Consistent NAP across page/schema, Tier 1 citations detected, industry directories present
- Partial: NAP present but inconsistencies, some citations missing
- Low: NAP discrepancies, no detectable citations, no schema address

### 5. Local Schema Markup (10%)

Schema is NOT a direct ranking factor (John Mueller confirmed). But enables rich results (43% CTR increase, Webstix case study) and helps AI systems parse business information.

**Check for:**
- LocalBusiness schema presence (extract JSON-LD blocks)
- Required properties: `name`, `address` with PostalAddress sub-properties
- Recommended properties: `geo` (minimum 5 decimal places, Confirmed), `openingHoursSpecification`, `telephone`, `url`, `priceRange` (<100 chars), `image`, `aggregateRating`
- **Correct subtype for industry** -- load `references/local-schema-types.md`:
  - Restaurant using `Restaurant` not generic `LocalBusiness`
  - Legal using `LegalService` not deprecated `Attorney`
  - Auto dealer using `AutoDealer` not deprecated `VehicleListing`
  - Healthcare using `MedicalClinic`/`Hospital`/`Dentist` not generic `MedicalBusiness`
- SAB-specific: `areaServed` with named cities (recommended, not in Google's official list but Schema.org supported)
- Multi-location: each location page has own LocalBusiness with unique `@id`, linked via `branchOf` to Organization on homepage
- Industry-specific schema patterns (per `references/local-schema-types.md`):
  - Restaurant: Menu + MenuSection + MenuItem + ReserveAction
  - Healthcare: Physician (Person) + MedicalSpecialty + sameAs to NPI
  - Legal: LegalService + Person + Service (practice areas)
  - Home Services: Subtype + areaServed + Service
  - Real Estate: RealEstateAgent + Person + RealEstateListing
  - Automotive: AutoDealer + Car + Offer (separate dept schemas)

**Scoring guide:**
- Full: Correct subtype, all recommended properties, industry-specific patterns, valid JSON-LD
- Partial: LocalBusiness present but generic type or missing recommended properties
- Low: No local schema, or schema with errors/placeholder content

### 6. Local Link & Authority Signals (10%)

Links declining for local pack but remain **~26% of local organic ranking** (Whitespark 2026, #2 factor group). "Best of" list placements = **#1 AI visibility citation factor**.

**Check for:**
- Local backlink indicators detectable from page:
  - Chamber of Commerce mentions or links (high Trust Flow, ~80% more consumer visits, GlueUp)
  - BBB accreditation/badge (Google uses BBB for business verification)
  - Local news/press mentions
  - Community involvement signals (sponsorships, local events, partnerships)
- "Best of" list presence (top AI visibility factor per Whitespark 2026)
- Digital PR signals: 66.2% of PR practitioners now track AI citations as KPI (BuzzStream 2026)
- Brand mentions correlate **3x more strongly** with AI visibility than traditional backlinks (Ahrefs: 0.664 vs 0.218 correlation)
- Link velocity benchmark: 5-10 quality local links/month for small businesses (consensus)

**Scoring guide:**
- Full: Local authority signals visible (chamber, BBB, press), community involvement evident
- Partial: Some authority signals but limited local link indicators
- Low: No detectable local authority signals

---

## AI Search Impact on Local

**Do not duplicate seo-geo analysis.** Provide local-specific AI context and recommend `/seo geo <url>` for full analysis.

Key local AI facts:
- AI Overviews appear on up to 68% of local searches (Whitespark Q2 2025)
- ChatGPT converts at 15.9% vs Google organic at 1.76% (Seer Interactive)
- 3 of top 5 AI visibility factors are citation-related (Whitespark 2026)
- ChatGPT does NOT access GBP directly -- sources from Bing index, Yelp, TripAdvisor, BBB, Reddit
- Bing Places is critical: powers ChatGPT, Copilot, Alexa
- AI-powered local packs (mobile US) show only 1-2 businesses, 32% fewer shown (Sterling Sky)

**Recommendation**: Run `/seo geo <url>` for comprehensive AI search visibility analysis including citability scoring, llms.txt check, and brand mention audit.

---

## Reference Files

Load on-demand as needed:
- `references/local-seo-signals.md`: Ranking factors, review benchmarks, citation tiers, GBP feature status, algorithm updates
- `references/local-schema-types.md`: LocalBusiness subtypes by industry, schema patterns, citation sources per vertical

---

## Output

Generate `LOCAL-SEO-ANALYSIS-{domain}.md` with:

1. **Local SEO Score: XX/100** with dimension breakdown table
2. **Business type**: Brick-and-mortar / SAB / Hybrid
3. **Industry vertical detected** + industry-specific findings
4. **GBP optimization checklist** (detected signals vs missing)
5. **Review health snapshot** (rating, count, velocity indicators, response patterns)
6. **NAP consistency audit** (page vs schema discrepancies, cross-source comparison)
7. **Citation presence check** (Tier 1 directory status)
8. **Local schema status** (present/missing/malformed + ready-to-use fix)
9. **Location page quality** (if multi-location: unique content %, doorway risk, store locator)
10. **Top 10 prioritized actions** (Critical > High > Medium > Low)
11. **Limitations disclaimer**: What this analysis could NOT assess (geo-grid ranking, Domain Authority, comprehensive backlinks, GBP Insights data, real-time local pack position) and which paid tools can fill those gaps

---

## Quick Wins

1. Claim and optimize Apple Business Connect (usage doubled to 27%)
2. Claim and optimize Bing Places (powers ChatGPT, Copilot, Alexa)
3. Fix any NAP discrepancies between page, schema, and GBP
4. Add LocalBusiness schema with correct industry subtype
5. Add `geo` coordinates with 5+ decimal precision
6. Ensure phone number uses `tel:` link for click-to-call
7. Add city + service keyword to title tag and H1

## Medium Effort

1. Create dedicated page for each core service (Whitespark: #1 local organic factor)
2. Build review generation strategy maintaining 18-day minimum cadence
3. Submit to three data aggregators (Data Axle, Foursquare, Neustar/TransUnion) for downstream distribution
4. Claim industry-specific directory listings (per vertical recommendations)
5. Add industry-specific schema patterns (Menu for restaurants, Physician for healthcare, etc.)
6. Implement hub-and-spoke internal linking for service/location pages

## High Impact

1. Build local digital PR strategy targeting "best of" lists (#1 AI visibility factor)
2. Develop unique, non-swappable content for each location page (>60% unique)
3. Establish presence on platforms ChatGPT sources from (Yelp, TripAdvisor, BBB, Reddit)
4. Pursue Chamber of Commerce and BBB membership (authority + verification signals)
5. Create community involvement content (sponsorships, local events, partnerships)

---

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `local_business_data` for live GBP data extraction, `google_local_pack_serp` for real-time local pack positions, and `business_listings` for automated citation auditing across directories.

---

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| No local signals detected on page | Report that no local business indicators were found. Suggest the user confirm this is a local business and provide the GBP listing URL if available. |
| NAP not found in page HTML | Check schema and meta tags. If still absent, flag as Critical issue. Recommend adding visible NAP to footer and contact page. |
| Industry vertical unclear | Present the top two detected verticals with supporting signals. Ask the user to confirm before applying industry-specific recommendations. |
| Multi-location with 50+ location pages | Apply the quality gates from seo orchestrator: WARNING at 30+ pages (enforce 60%+ unique), HARD STOP at 50+ pages (require user justification before continuing). |
```

## File: `skills/seo-maps/SKILL.md`
```markdown
---
name: seo-maps
description: >
  Maps intelligence for local SEO — geo-grid rank tracking, GBP profile
  auditing via API, review intelligence across Google/Tripadvisor/Trustpilot,
  cross-platform NAP verification (Google/Bing/Apple/OSM), competitor
  radius mapping, and LocalBusiness schema generation from API data.
  Three-tier capability: free (Overpass + Geoapify), DataForSEO (full
  intelligence), DataForSEO + Google (maximum coverage). Use when user
  says "maps", "geo-grid", "rank tracking", "GBP audit", "review
  velocity", "competitor radius", "maps analysis", "local rank
  tracking", "Share of Local Voice", or "SoLV".
user-invokable: true
argument-hint: "[command] [url|keyword|location]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
compatibility: "DataForSEO MCP for Tier 1+, Google Maps API for Tier 2"
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Maps Intelligence (March 2026)

Maps platform analysis for local businesses. Works with external APIs to assess
how a business appears on Google Maps, Bing Places, Apple Maps, and OpenStreetMap.

**Boundary with seo-local:** This skill analyzes the business on maps PLATFORMS
(via APIs). seo-local analyzes local SEO signals on the WEBSITE (via HTML fetch).
Do not duplicate seo-local on-page analysis. Recommend `/seo local <url>` for
website-level checks.

---

## Quick Reference

| Command | What it does | Tier |
|---------|-------------|------|
| `/seo maps <url>` | Full maps presence audit (auto-selects tier) | 0+ |
| `/seo maps grid <keyword> <location>` | Geo-grid rank scan (7x7, 1 keyword default) | 1+ |
| `/seo maps reviews <business> <location>` | Cross-platform review intelligence | 1+ |
| `/seo maps competitors <keyword> <location>` | Competitor radius mapping | 0+ |
| `/seo maps nap <business-name>` | Cross-platform NAP verification | 0+ |
| `/seo maps schema <business-name>` | Generate LocalBusiness JSON-LD from data | 0+ |
| `/seo maps gbp <business> <location>` | GBP completeness audit | 1+ |

---

## Three-Tier Capability Detection

Before any analysis, detect the available capability tier:

### Tier 0 (Free)
**Detection:** DataForSEO MCP tools NOT available.
**Capabilities:** Overpass API competitor discovery, Geoapify POI search, Nominatim geocoding, static GBP checklist, schema generation, cross-platform NAP guidance.
**Load:** `references/maps-free-apis.md`

### Tier 1 (DataForSEO)
**Detection:** `business_data_business_listings_search` MCP tool IS available.
**Capabilities:** Everything in Tier 0 PLUS geo-grid rank tracking, live GBP profile audit, review intelligence (velocity, sentiment, distribution), GBP post activity, Q&A data, Tripadvisor/Trustpilot reviews.
**Load:** `references/maps-api-endpoints.md`

### Tier 2 (DataForSEO + Google Maps Platform)
**Detection:** Tier 1 available AND Google Maps API key in environment.
**Capabilities:** Everything in Tier 1 PLUS Google Places details, real-time business status, AI-powered place summaries, photo analysis.
**Note:** Google ToS restricts storage to `place_id` only. Lat/lng cached 30 days max.

**Always communicate the detected tier to the user** at the start of analysis.

---

## Geo-Grid Rank Tracking (Tier 1+)

Simulates Google Maps searches from multiple GPS coordinates to show ranking
variation across a geographic area. Requires DataForSEO.

**Load:** `references/maps-geo-grid.md` for algorithm, SoLV formula, heatmap format.
**Load:** `references/maps-api-endpoints.md` for Maps SERP endpoint details.

### Workflow

1. Geocode business address to get center lat/lng
2. Generate grid points (default: 7x7, 5km radius) using Haversine offset formula
3. **Display cost estimate and ask for confirmation before proceeding**
4. Fire DataForSEO Maps SERP API calls with `location_coordinate` per grid point
5. Find target business rank at each point
6. Calculate SoLV: `(top_3_count / total_points) * 100`
7. Render ASCII heatmap in output

### Cost Warning (REQUIRED)

Before every geo-grid scan, display:
```
Geo-Grid Scan: [keyword] at [location]
Grid: 7x7 (49 points) | Keywords: [N] | Est. cost: $[amount]
DataForSEO credits will be consumed. Proceed?
```

---

## GBP Profile Audit (Tier 1 preferred, Tier 0 manual)

Audits the 25 fields that affect Google Business Profile quality and ranking.

**Load:** `references/maps-gbp-checklist.md` for full checklist and scoring.

### Tier 1 Workflow

1. Fetch business profile via DataForSEO My Business Info API (keyword or CID)
2. Map API response fields to 25-field checklist
3. Score each field: Present + Optimized = 2pts, Present = 1pt, Missing = 0pts
4. Apply industry-specific weight multipliers
5. Normalize to 0-100 scale

### Tier 0 Workflow

1. Fetch the business website via WebFetch
2. Extract any visible GBP signals (Maps embed, place references, review widgets)
3. Apply static checklist based on detectable signals
4. Mark undetectable fields as "Unknown (requires DataForSEO for live data)"

---

## Review Intelligence (Tier 1+)

Cross-platform review analysis: velocity, sentiment, rating distribution, fake detection.

**Reference:** `references/local-seo-signals.md` for benchmarks (shared with seo-local).

### Workflow

1. Fetch Google reviews via DataForSEO Reviews API (sort by newest)
2. Calculate review velocity: reviews per month over last 6 months
3. Check 18-day rule (Sterling Sky): any 3-week gap = ranking risk
4. Analyze rating distribution: healthy = bell curve skewed to 5-star
5. Calculate owner response rate: responses / total reviews
6. Fetch Tripadvisor and Trustpilot reviews (if available)
7. Cross-platform comparison table

### Fake Review Detection Signals

Flag reviews matching 2+ of these patterns:
- Uniform timing (multiple reviews same day/hour)
- Reviewer accounts with limited history or single review
- Geographic inconsistencies (reviewer location vs business location)
- Exclusively 5-star velocity spike (vs historical baseline)
- Identical or near-identical text across reviews
- Sudden volume spike without corresponding marketing activity

---

## Competitor Radius Mapping (Tier 0+)

Identify and analyze competitors within a defined radius.

### Tier 0 (Overpass API)

**Load:** `references/maps-free-apis.md` for query templates.

1. Geocode business address
2. Query Overpass API for businesses with same OSM tag within radius
3. Parse results: name, address, phone, website, distance from center
4. Sort by distance, present as competitor landscape table

### Tier 1 (DataForSEO)

1. Use Maps SERP API with business keyword + location
2. Extract top 20 competitors with full profile data
3. Compare: rating, review count, categories, photos, attributes
4. Calculate competitive density score: competitors per km^2

---

## Cross-Platform NAP Verification (Tier 0+)

Check business listing consistency across Google, Bing Places, Apple, and OSM.

### Workflow

1. Search for business name on each platform:
   - Google: infer from GBP data or Maps SERP result
   - Bing: `WebFetch https://www.bing.com/maps?q=BUSINESS+NAME+LOCATION`
   - Apple: manual check (no public API -- recommend Apple Business Connect at businessconnect.apple.com)
   - OSM: Overpass or Nominatim search
2. Extract NAP (Name, Address, Phone) from each source
3. Compare for consistency: exact match, partial match, missing, or conflicting
4. Flag discrepancies as Critical (name mismatch), High (address mismatch), Medium (phone mismatch)
5. Recommend claiming unclaimed profiles

---

## Schema Generation (Tier 0+)

Generate LocalBusiness JSON-LD markup from collected data.

**Reference:** `references/local-schema-types.md` for industry subtypes (shared with seo-local).

### Workflow

1. Determine most specific schema subtype for the industry
2. Populate required properties: `@type`, `name`, `address`, `image`
3. Add recommended properties: `telephone`, `url`, `geo`, `openingHoursSpecification`, `priceRange`
4. Add strategic properties for multi-location: `branchOf`, `areaServed`, `sameAs`
5. Add `aggregateRating` if review data available
6. Output valid JSON-LD block ready for implementation

**Do NOT generate self-serving review markup** -- Google ignores LocalBusiness review markup from the business itself. Only mark up third-party reviews visible on the page.

---

## Reference Files

Load on-demand as needed (do NOT load all at startup):
- `references/maps-api-endpoints.md`: DataForSEO endpoint details, params, costs
- `references/maps-free-apis.md`: Overpass, Geoapify, Nominatim query templates
- `references/maps-geo-grid.md`: Grid algorithm, SoLV formula, heatmap rendering
- `references/maps-gbp-checklist.md`: 25-field GBP audit with industry weights
- `references/local-seo-signals.md`: Ranking factors, review benchmarks (shared)
- `references/local-schema-types.md`: LocalBusiness subtypes by industry (shared)

---

## Output

Generate `MAPS-ANALYSIS-{domain}.md` with:

1. **Maps Health Score: XX/100** with dimension breakdown table
2. **Capability tier detected** (Tier 0 or Tier 1) with explanation of what's available
3. **Geo-grid heatmap** (Tier 1): ASCII grid with SoLV percentage and average rank
4. **GBP profile audit**: field-by-field scoring with industry-specific weights
5. **Review intelligence**: velocity chart, rating distribution, response rate, cross-platform comparison
6. **Competitor landscape**: count in radius, top 5 by rating/reviews, competitive density
7. **Cross-platform presence**: Google/Bing/Apple/OSM listing status
8. **Schema recommendation**: generated LocalBusiness JSON-LD (if missing or incomplete)
9. **Top 10 prioritized actions** (Critical > High > Medium > Low)
10. **Cost report**: DataForSEO credits consumed during analysis (Tier 1 only)
11. **Limitations disclaimer**: what could not be assessed at current tier

---

## Cross-Skill Delegation

- Website on-page local signals: recommend `/seo local <url>`
- Full AI search visibility: recommend `/seo geo <url>`
- Schema validation and fixes: recommend `/seo schema <url>`
- Live SERP and keyword data: recommend `/seo dataforseo [command]`

---

## Error Handling

| Scenario | Action |
|----------|--------|
| DataForSEO MCP not available | Drop to Tier 0. Inform user: "DataForSEO not detected. Running free-tier analysis. For geo-grid tracking and review intelligence, install the DataForSEO extension." |
| Business not found in Maps SERP | Try My Business Info with keyword. If still not found, report "Business not found in Google Maps for this location." |
| Geocoding fails (Nominatim) | Ask user to provide coordinates or a more specific address. |
| API rate limit hit | Report the limit. Suggest waiting or using standard (queued) method instead of live. |
| No reviews found | Report zero review state. Recommend review generation strategy with 18-day cadence target. |
| Multi-location detected | Ask user which location to analyze, or offer batch mode with per-location cost estimate. |
```

## File: `skills/seo-page/SKILL.md`
```markdown
---
name: seo-page
description: >
  Deep single-page SEO analysis covering on-page elements, content quality,
  technical meta tags, schema, images, and performance. Use when user says
  "analyze this page", "check page SEO", "single URL", "check this page",
  "page analysis", or provides a single URL for review.
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Single Page Analysis

## What to Analyze

### On-Page SEO
- Title tag: 50-60 characters, includes primary keyword, unique
- Meta description: 150-160 characters, compelling, includes keyword
- H1: exactly one, matches page intent, includes keyword
- H2-H6: logical hierarchy (no skipped levels), descriptive
- URL: short, descriptive, hyphenated, no parameters
- Internal links: sufficient, relevant anchor text, no orphan pages
- External links: to authoritative sources, reasonable count

### Content Quality
- Word count vs page type minimums (see quality-gates.md)
- Readability: Flesch Reading Ease score, grade level
- Keyword density: natural (1-3%), semantic variations present
- E-E-A-T signals: author bio, credentials, first-hand experience markers
- Content freshness: publication date, last updated date

### Technical Elements
- Canonical tag: present, self-referencing or correct
- Meta robots: index/follow unless intentionally blocked
- Open Graph: og:title, og:description, og:image, og:url
- Twitter Card: twitter:card, twitter:title, twitter:description
- Hreflang: if multi-language, correct implementation

### Schema Markup
- Detect all types (JSON-LD preferred)
- Validate required properties
- Identify missing opportunities
- NEVER recommend HowTo (deprecated) or FAQ (restricted to gov/health)

### Images
- Alt text: present, descriptive, includes keywords where natural
- File size: flag >200KB (warning), >500KB (critical)
- Format: recommend WebP/AVIF over JPEG/PNG
- Dimensions: width/height set for CLS prevention
- Lazy loading: loading="lazy" on below-fold images

### Core Web Vitals (reference only, not measurable from HTML alone)
- Flag potential LCP issues (huge hero images, render-blocking resources)
- Flag potential INP issues (heavy JS, no async/defer)
- Flag potential CLS issues (missing image dimensions, injected content)

## Output

### Page Score Card
```
Overall Score: XX/100

On-Page SEO:     XX/100  ████████░░
Content Quality: XX/100  ██████████
Technical:       XX/100  ███████░░░
Schema:          XX/100  █████░░░░░
Images:          XX/100  ████████░░
```

### Issues Found
Organized by priority: Critical -> High -> Medium -> Low

### Recommendations
Specific, actionable improvements with expected impact

### Schema Suggestions
Ready-to-use JSON-LD code for detected opportunities

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `serp_organic_live_advanced` for real SERP positions and `backlinks_summary` for backlink data and spam scores.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess page content. Suggest the user verify the URL and try again. |
| Page requires authentication (401/403) | Report that the page is behind authentication. Suggest the user provide the rendered HTML directly or a publicly accessible URL. |
| JavaScript-rendered content (empty body in HTML) | Note that key content may be rendered client-side. Analyze the available HTML and flag that results may be incomplete. Suggest using a browser-rendered snapshot if available. |
```

## File: `skills/seo-plan/SKILL.md`
```markdown
---
name: seo-plan
description: >
  Strategic SEO planning for new or existing websites. Industry-specific
  templates, competitive analysis, content strategy, and implementation
  roadmap. Use when user says "SEO plan", "SEO strategy", "SEO planning",
  "content strategy", "keyword strategy", "content calendar",
  "site architecture", or "SEO roadmap".
user-invokable: true
argument-hint: "[business-type]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Strategic SEO Planning

## Process

### 1. Discovery
- Business type, target audience, competitors, goals
- Current site assessment (if exists)
- Budget and timeline constraints
- Key performance indicators (KPIs)

### 2. Competitive Analysis
- Identify top 5 competitors
- Analyze their content strategy, schema usage, technical setup
- Identify keyword gaps and content opportunities
- Assess their E-E-A-T signals
- Estimate their domain authority

### 3. Architecture Design
- Load industry template from `assets/` directory
- Design URL hierarchy and content pillars
- Plan internal linking strategy
- Sitemap structure with quality gates applied
- Information architecture for user journeys

### 4. Content Strategy
- Content gaps vs competitors
- Page types and estimated counts
- Blog/resource topics and publishing cadence
- E-E-A-T building plan (author bios, credentials, experience signals)
- Content calendar with priorities

### 5. Technical Foundation
- Hosting and performance requirements
- Schema markup plan per page type
- Core Web Vitals baseline targets
- AI search readiness requirements
- Mobile-first considerations

### 6. Implementation Roadmap (4 phases)

#### Phase 1: Foundation (weeks 1-4)
- Technical setup and infrastructure
- Core pages (home, about, contact, main services)
- Essential schema implementation
- Analytics and tracking setup

#### Phase 2: Expansion (weeks 5-12)
- Content creation for primary pages
- Blog launch with initial posts
- Internal linking structure
- Local SEO setup (if applicable)

#### Phase 3: Scale (weeks 13-24)
- Advanced content development
- Link building and outreach
- GEO optimization
- Performance optimization

#### Phase 4: Authority (months 7-12)
- Thought leadership content
- PR and media mentions
- Advanced schema implementation
- Continuous optimization

## Industry Templates

Load from `assets/` directory:
- `saas.md`: SaaS/software companies
- `local-service.md`: Local service businesses
- `ecommerce.md`: E-commerce stores
- `publisher.md`: Content publishers/media
- `agency.md`: Agencies and consultancies
- `generic.md`: General business template

## Output

### Deliverables
- `SEO-STRATEGY.md`: Complete strategic plan
- `COMPETITOR-ANALYSIS.md`: Competitive insights
- `CONTENT-CALENDAR.md`: Content roadmap
- `IMPLEMENTATION-ROADMAP.md`: Phased action plan
- `SITE-STRUCTURE.md`: URL hierarchy and architecture

### KPI Targets
| Metric | Baseline | 3 Month | 6 Month | 12 Month |
|--------|----------|---------|---------|----------|
| Organic Traffic | ... | ... | ... | ... |
| Keyword Rankings | ... | ... | ... | ... |
| Domain Authority | ... | ... | ... | ... |
| Indexed Pages | ... | ... | ... | ... |
| Core Web Vitals | ... | ... | ... | ... |

### Success Criteria
- Clear, measurable goals per phase
- Resource requirements defined
- Dependencies identified
- Risk mitigation strategies

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `dataforseo_labs_google_competitors_domain` and `dataforseo_labs_google_domain_intersection` for real competitive intelligence, `dataforseo_labs_bulk_traffic_estimation` for traffic estimates, `kw_data_google_ads_search_volume` and `dataforseo_labs_bulk_keyword_difficulty` for keyword research, and `business_data_business_listings_search` for local business data.

## Error Handling

| Scenario | Action |
|----------|--------|
| Unrecognized business type | Fall back to `generic.md` template. Inform user that no industry-specific template was found and proceed with the general business template. |
| No website URL provided | Proceed with new-site planning mode. Skip current site assessment and competitive gap analysis that require a live URL. |
| Industry template not found | Check `assets/` directory for available templates. If the requested template file is missing, use `generic.md` and note the missing template in output. |
```

## File: `skills/seo-plan/assets/agency.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Agency/Consultancy SEO Strategy Template

## Industry Characteristics

- Service-based, high-value transactions
- Expertise and trust are paramount
- Long consideration cycles
- Portfolio/case study driven decisions
- Relationship-based sales
- Niche specialization benefits

## Recommended Site Architecture

```
/
├── Home
├── /services
│   ├── /service-1
│   │   ├── /sub-service-1
│   │   └── ...
│   └── /service-2
├── /industries
│   ├── /industry-1
│   ├── /industry-2
│   └── ...
├── /work (or /case-studies)
│   ├── /case-study-1
│   ├── /case-study-2
│   └── ...
├── /about
│   ├── /team
│   │   ├── /team-member-1
│   │   └── ...
│   ├── /culture
│   └── /careers
├── /insights (or /blog)
│   ├── /articles
│   ├── /guides
│   ├── /webinars
│   └── /podcasts
├── /contact
├── /process
└── /faq
```

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, ProfessionalService |
| Service Page | Service, ProfessionalService |
| Case Study | Article, Organization (client) |
| Team Member | Person, ProfilePage |
| Blog | Article, BlogPosting |

### ProfessionalService Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Agency Name",
  "description": "What the agency does",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Agency St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "areaServed": "National",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Service 1"
        }
      }
    ]
  }
}
```

## E-E-A-T Requirements

### Team Pages Must Include
- Professional headshots
- Detailed bios with credentials
- Industry experience
- Speaking engagements
- Publications
- Social profiles

### Case Studies Must Include
- Client name (with permission) or industry
- Challenge/problem statement
- Approach/methodology
- Results with specific metrics
- Timeline
- Testimonial quote

## Content Priorities

### High Priority
1. Service pages (detailed, specific)
2. Industry pages (vertical expertise)
3. 3-5 detailed case studies
4. Team/leadership pages

### Medium Priority
1. Methodology/process page
2. Blog with thought leadership
3. Comparison content (vs alternatives)
4. FAQ page

### Thought Leadership Topics
- Industry trend analysis
- How-to guides (non-competitive)
- Original research/surveys
- Event recaps and insights
- Expert interviews
- Tool/technology reviews

## Content Strategy

### Service Pages (min 800 words)
- Clear value proposition
- Methodology overview
- Deliverables list
- Relevant case studies
- Team members who deliver this service
- CTA to schedule consultation

### Industry Pages (min 800 words)
- Industry-specific challenges
- How you solve them differently
- Relevant case studies
- Industry credentials/experience
- Client logos (with permission)

### Case Studies (min 1,000 words)
- Executive summary
- Client background
- Challenge details
- Solution approach
- Implementation process
- Measurable results
- Client testimonial
- Related services/CTA

## Key Metrics to Track

- Organic traffic to service pages
- Case study page views
- Contact form submissions from organic
- Time on page for key content
- Blog → service page conversion

## Generative Engine Optimization (GEO) for Agencies

- [ ] Publish original case studies with specific, citable metrics and results
- [ ] Use Person schema with sameAs links for all team members (builds entity authority)
- [ ] Use ProfilePage schema for team member pages
- [ ] Include clear, quotable expertise statements in service page descriptions
- [ ] Produce original industry research and surveys AI systems can cite
- [ ] Structure thought leadership content with clear headings and extractable insights
- [ ] Maintain consistent agency entity information across directories, social profiles, and industry sites
- [ ] Monitor AI citation in ChatGPT, Perplexity, and Google AI Overviews for brand and key service terms
```

## File: `skills/seo-plan/assets/ecommerce.md`
```markdown
<!-- Updated: 2026-02-07 -->
# E-commerce SEO Strategy Template

## Industry Characteristics

- High transaction intent
- Product comparison behavior
- Price sensitivity
- Visual-first decision making
- Seasonal demand patterns
- Competitive marketplace listings

## Recommended Site Architecture

```
/
├── Home
├── /collections (or /categories)
│   ├── /category-1
│   │   ├── /subcategory-1
│   │   └── ...
│   ├── /category-2
│   └── ...
├── /products
│   ├── /product-1
│   ├── /product-2
│   └── ...
├── /brands
│   ├── /brand-1
│   └── ...
├── /sale (or /deals)
├── /new-arrivals
├── /best-sellers
├── /gift-guide
├── /blog
│   ├── /buying-guides
│   ├── /how-to
│   └── /trends
├── /about
├── /contact
├── /shipping
├── /returns
└── /faq
```

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Product Page | Product, Offer, AggregateRating, Review, BreadcrumbList |
| Category Page | CollectionPage, ItemList, BreadcrumbList |
| Brand Page | Brand, Organization |
| Blog | Article, BlogPosting |

### Additional E-commerce Schema (2025)

- **ProductGroup**: Use for products with variants (size, color). Wraps individual Product entries with `variesBy` and `hasVariant` properties. See `schema/templates.json`.
- **Certification**: For product certifications (Energy Star, safety, organic). Replaced EnergyConsumptionDetails (April 2025). Use `hasCertification` on Product.
- **OfferShippingDetails**: Include shipping rate, handling time, and transit time. Critical for Merchant Center eligibility.

> **Google Merchant Center Free Listings:** Products can appear in Google Shopping for free. Ensure Product structured data is in the initial server-rendered HTML (not JavaScript-injected) with required properties: `name`, `image`, `price`, `priceCurrency`, `availability`.

> **JS Rendering Note:** Product structured data should be in initial server-rendered HTML: not dynamically injected via JavaScript (per December 2025 Google JS SEO guidance).

### Product Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/product.jpg"],
  "description": "Product description",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/product"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "42"
  }
}
```

## Content Requirements

### Product Pages (min 400 words)
- Unique product descriptions (not manufacturer copy)
- Feature highlights
- Use cases / who it's for
- Specifications table
- Size/fit guide (for apparel)
- Care instructions
- Customer reviews

### Category Pages (min 400 words)
- Category introduction
- Buying guide excerpt
- Featured products
- Subcategory links
- Filter/sort options

## Technical Considerations

### Pagination
- Use rel="next"/rel="prev" or load-more
- Ensure all products are crawlable
- Canonical to main category page

### Faceted Navigation
- Noindex filter combinations that create duplicate content
- Use canonical tags appropriately
- Ensure popular filters are indexable

### Product Variations
- Single URL for parent product with variants
- Or separate URLs with canonical to parent
- Structured data for all variants

## Content Priorities

### High Priority
1. Category pages (top level)
2. Best-selling product pages
3. Homepage
4. Buying guides for main categories

### Medium Priority
1. Subcategory pages
2. Brand pages
3. Comparison content
4. Seasonal landing pages

### Blog Topics
- Buying guides ("How to Choose...")
- Product comparisons
- Trend reports
- Use cases and inspiration
- Care and maintenance guides

## Key Metrics to Track

- Revenue from organic search
- Product page rankings
- Category page rankings
- Click-through rate (rich results)
- Average order value from organic

## Generative Engine Optimization (GEO) for E-commerce

AI search platforms increasingly answer product queries directly. Optimize for AI citation:

- [ ] Include clear product specifications, dimensions, materials in structured format
- [ ] Use ProductGroup schema for variant products
- [ ] Provide original product photography with descriptive alt text
- [ ] Include genuine customer review content (AggregateRating schema)
- [ ] Maintain consistent product entity data across all platforms (site, Amazon, Merchant Center)
- [ ] Structure comparison content with clear feature tables AI can parse
- [ ] Add detailed FAQ content for common product questions
```

## File: `skills/seo-plan/assets/generic.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Generic Business SEO Strategy Template

## Overview

This template applies to businesses that don't fit neatly into SaaS, local service, e-commerce, publisher, or agency categories. Customize based on your specific business model.

## Recommended Site Architecture

```
/
├── Home
├── /products (or /services)
│   ├── /product-1
│   ├── /product-2
│   └── ...
├── /solutions (if applicable)
│   ├── /solution-1
│   └── ...
├── /about
│   ├── /team
│   ├── /history
│   └── /values
├── /resources
│   ├── /blog
│   ├── /guides
│   ├── /faq
│   └── /glossary
├── /contact
├── /support
└── /legal
    ├── /privacy
    └── /terms
```

## Universal SEO Principles

### Every Page Should Have
- Unique title tag (30-60 chars)
- Unique meta description (120-160 chars)
- Single H1 matching page intent
- Logical heading hierarchy (H1→H2→H3)
- Internal links to related content
- Clear call-to-action

### Schema for All Sites
| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, WebSite |
| About | Organization, AboutPage |
| Contact | ContactPage |
| Blog | Article, BlogPosting |
| FAQ | (FAQPage only for gov/health) |
| Product/Service | Product or Service |

## Content Quality Standards

### Minimum Word Counts
| Page Type | Min Words |
|-----------|-----------|
| Homepage | 500 |
| Product/Service | 800 |
| Blog Post | 1,500 |
| About Page | 400 |
| Landing Page | 600 |

### E-E-A-T Essentials
1. **Experience**: Share real examples and case studies
2. **Expertise**: Display credentials and qualifications
3. **Authoritativeness**: Earn mentions and citations
4. **Trustworthiness**: Full contact info, policies visible

## Technical Foundations

### Must-Haves
- [ ] HTTPS enabled
- [ ] Mobile-responsive design
- [ ] robots.txt configured
- [ ] XML sitemap submitted
- [ ] Google Search Console verified
- [ ] Core Web Vitals passing (LCP <2.5s, INP <200ms, CLS <0.1)

### Should-Haves
- [ ] Structured data on key pages
- [ ] Internal linking strategy
- [ ] 404 error page optimized
- [ ] Redirect chains eliminated
- [ ] Image optimization (WebP, lazy loading)

## Content Priorities

### Phase 1: Foundation (weeks 1-4)
1. Homepage optimization
2. Core product/service pages
3. About and contact pages
4. Basic schema implementation

### Phase 2: Expansion (weeks 5-12)
1. Blog launch (2-4 posts/month)
2. FAQ page
3. Additional product/service pages
4. Internal linking audit

### Phase 3: Growth (weeks 13-24)
1. Consistent content publishing
2. Link building outreach
3. GEO optimization
4. Performance optimization

### Phase 4: Authority (months 7-12)
1. Thought leadership content
2. Original research
3. PR and media mentions
4. Advanced schema

## Key Metrics to Track

- Organic traffic (overall and by section)
- Keyword rankings (branded and non-branded)
- Conversion rate from organic
- Pages indexed
- Core Web Vitals scores
- Backlinks acquired

## Customization Points

Adjust this template based on:

1. **Business Model**: B2B vs B2C vs D2C
2. **Geographic Scope**: Local, national, or international
3. **Content Type**: Product-focused vs content-heavy
4. **Competition Level**: Niche vs competitive market
5. **Resources**: Budget and team capacity

## Generative Engine Optimization (GEO) Checklist

- [ ] Include clear, quotable facts and statistics that AI systems can extract and cite
- [ ] Use structured data (Schema.org) to help AI systems understand content
- [ ] Build topical authority through comprehensive content clusters
- [ ] Provide original data, research, or unique perspectives AI cannot find elsewhere
- [ ] Maintain consistent entity information (brand, people, products) across the web
- [ ] Structure content with clear headings, definitions, and step-by-step formats
- [ ] Consider adding an `llms.txt` file at site root (emerging convention for AI crawlers: Google treats it as a regular text file)
- [ ] Monitor AI citation across Google AI Overviews, ChatGPT, Perplexity, and Bing Copilot
```

## File: `skills/seo-plan/assets/local-service.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Local Service Business SEO Strategy Template

## Industry Characteristics

- Geographic-focused searches
- High intent, quick decision making
- Reviews heavily influence decisions
- Phone calls are primary conversion
- Mobile-first user behavior
- Emergency/urgent service needs

## Recommended Site Architecture

```
/
├── Home
├── /services
│   ├── /service-1
│   ├── /service-2
│   └── ...
├── /locations
│   ├── /city-1
│   │   ├── /service-1-city-1
│   │   └── ...
│   ├── /city-2
│   └── ...
├── /about
├── /reviews
├── /gallery (or /portfolio)
├── /blog
├── /contact
├── /emergency (if applicable)
└── /faq
```

## Quality Gates

### Location Page Limits
- ⚠️ **WARNING** at 30+ location pages
- 🛑 **HARD STOP** at 50+ location pages

### Unique Content Requirements
| Page Type | Min Words | Unique % |
|-----------|-----------|----------|
| Primary Location | 600 | 60%+ |
| Service Area | 500 | 40%+ |
| Service Page | 800 | 100% |

### What Makes Location Pages Unique
- Local landmarks and neighborhoods
- Specific services offered at that location
- Local team members
- Location-specific testimonials
- Community involvement
- Local regulations or considerations

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | LocalBusiness, Organization |
| Service Pages | Service, LocalBusiness |
| Location Pages | LocalBusiness (with geo) |
| Contact | ContactPage, LocalBusiness |
| Reviews | LocalBusiness (with AggregateRating) |

### LocalBusiness Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "openingHours": "Mo-Fr 08:00-18:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "areaServed": ["City 1", "City 2"],
  "priceRange": "$$"
}
```

## Google Business Profile Integration

- Ensure NAP consistency (Name, Address, Phone)
- Sync service categories
- Regular post updates
- Photo uploads
- Review response strategy

### Google Business Profile Updates (2025-2026)

- **Video verification** is now standard: postcard verification has been largely phased out. Prepare for a short video verification process showing the business location or service area.
- **WhatsApp integration** replaced Google Business Chat (deprecated). Businesses can connect WhatsApp as their primary messaging channel.
- **Q&A removed from Maps**: replaced by AI-generated answers. Ensure your GBP description, services, and website FAQ are comprehensive, as Google AI uses them to answer queries.
- **Business hours are a top-5 ranking factor**: "Business is open at time of search" ranked as a top individual factor for the first time (Whitespark 2026 Local Search Ranking Factors Report). Keep hours accurate; consider extended hours if feasible.
- **Review "Stories" format**: Google Maps now shows review snippets in a swipeable Stories format on mobile. Encourage detailed, descriptive reviews with photos.

### Service Area Business (SAB) Update (June 2025)

Google updated SAB guidelines to **disallow entire states or countries** as service areas. SABs must specify: cities, postal/ZIP codes, or neighborhoods. If you serve an entire metro area, list the major cities within it rather than the state.

### AI Visibility for Local Businesses

AI Overviews appear for only ~0.14% of local keywords (March 2025 data), local SEO faces significantly less AI disruption than other verticals. However, ChatGPT and Perplexity are increasingly used for local recommendations.

To optimize for AI local visibility:
- Ensure presence on expert-curated "best of" lists (ranked #1 AI visibility factor in Whitespark 2026 report)
- Maintain consistent NAP (Name, Address, Phone) across all platforms
- Build genuine review volume and quality
- Use LocalBusiness schema with complete properties (geo, openingHours, priceRange, areaServed)

## Content Priorities

### High Priority
1. Homepage with clear service area
2. Core service pages
3. Primary city page
4. Contact page with all locations

### Medium Priority
1. Service + location combination pages
2. FAQ page
3. About/team page
4. Reviews/testimonials page

### Blog Topics
- Seasonal maintenance tips
- How to choose a [service provider]
- Warning signs of [problem]
- DIY vs professional comparisons
- Local regulations and permits

## Key Metrics to Track

- Local pack rankings
- Phone call volume from organic
- Direction requests
- Google Business Profile insights
- Reviews count and rating

## Generative Engine Optimization (GEO) for Local

- [ ] Include clear, quotable service descriptions and pricing ranges
- [ ] Use LocalBusiness schema with complete geo, openingHours, and areaServed
- [ ] Build presence on curated "best of" and local directory lists
- [ ] Maintain consistent NAP across all platforms (Google, Yelp, Apple Maps)
- [ ] Include original photos of work, team, and location
- [ ] Structure FAQ content for common local service questions
- [ ] Monitor AI citation in ChatGPT and Perplexity local recommendations
```

## File: `skills/seo-plan/assets/publisher.md`
```markdown
<!-- Updated: 2026-02-07 -->
# Publisher/Media SEO Strategy Template

## Industry Characteristics

- High content volume
- Time-sensitive content (news)
- Ad revenue dependent on traffic
- Authority and trust critical
- Competing with social platforms
- AI Overviews impact on traffic

## Recommended Site Architecture

```
/
├── Home
├── /news (or /latest)
├── /topics
│   ├── /topic-1
│   ├── /topic-2
│   └── ...
├── /authors
│   ├── /author-1
│   └── ...
├── /opinion
├── /reviews
├── /guides
├── /videos
├── /podcasts
├── /newsletter
├── /about
│   ├── /editorial-policy
│   ├── /corrections
│   └── /contact
└── /[year]/[month]/[slug] (article URLs)
```

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Article | NewsArticle or Article, Person (author), Organization (publisher) |
| Author Page | Person, ProfilePage |
| Topic Page | CollectionPage, ItemList |
| Homepage | WebSite, Organization |
| Video | VideoObject |
| Podcast | PodcastEpisode, PodcastSeries |

### NewsArticle Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Article Headline",
  "datePublished": "2026-02-07T10:00:00Z",
  "dateModified": "2026-02-07T14:30:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/authors/author-name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publication Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "image": ["https://example.com/article-image.jpg"],
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-url"
  }
}
```

## E-E-A-T Requirements

Publishers face highest E-E-A-T scrutiny.

### Author Pages Must Include
- Full name and photo
- Bio and credentials
- Areas of expertise
- Contact information
- Social profiles (sameAs)
- Previous articles by this author

### Editorial Standards
- Clear correction policy
- Transparent editorial process
- Fact-checking procedures
- Conflict of interest disclosures

## Content Priorities

### High Priority
1. Breaking news (speed matters)
2. Evergreen guides on core topics
3. Author pages with credentials
4. Topic hubs/pillar pages

### Medium Priority
1. Opinion/analysis pieces
2. Video content
3. Interactive content
4. Newsletter landing pages

### GEO Considerations
- Clear, quotable facts in articles
- Tables for data-heavy content
- Expert quotes with attribution
- Update dates prominently displayed
- Structured headings (H2/H3)
- First-party data and original research are highly cited by AI systems
- Ensure author entities are clearly defined with Person schema + sameAs links
- Monitor AI citation frequency across Google AI Overviews, AI Mode, ChatGPT, Perplexity
- Treat AI citation as a standalone KPI alongside organic traffic

### Publisher SEO Updates (2025-2026)

- **Google News automatic inclusion:** Google News no longer accepts manual applications (since March 2025). Inclusion is fully automatic based on Google's content quality criteria. Focus on Google News sitemap markup and consistent, high-quality publishing cadence.
- **KPI shift:** Traffic-based KPIs (sessions, pageviews) are declining in relevance as AI Overviews reduce click-through rates. Leading publishers are shifting to: subscriber conversions, time on page, scroll depth, newsletter signups, AI citation frequency, and revenue per visitor.
- **Site reputation abuse risk:** Publishers hosting third-party content (coupons, product reviews, affiliate content) under their domain are at high risk. Google penalized Forbes, WSJ, Time, and CNN for this in late 2024. If hosting third-party content, ensure strong editorial oversight and clear first-party involvement.

## Technical Considerations

### Core Web Vitals
- Ad placement affects CLS
- Lazy load ads and images below fold
- Optimize hero images for LCP
- Minimize render-blocking resources

### AMP (if used)
- Consider dropping AMP (no longer required for Top Stories)
- Ensure canonical setup is correct
- Monitor performance vs non-AMP

### Pagination
- Proper pagination for multi-page articles
- Or infinite scroll with proper indexing
- Canonical to page 1 or full article

## Key Metrics to Track

- Page views from organic
- Time on page
- Pages per session
- Newsletter signups from organic
- Google News/Discover traffic
- AI Overview appearances
```

## File: `skills/seo-plan/assets/saas.md`
```markdown
<!-- Updated: 2026-02-07 -->
# SaaS SEO Strategy Template

## Industry Characteristics

- Long sales cycles with multiple touchpoints
- Feature-focused decision making
- Comparison shopping behavior
- Heavy research phase before purchase
- Integration and ecosystem considerations

## Recommended Site Architecture

```
/
├── Home
├── /product (or /platform)
│   ├── /features
│   │   ├── /feature-1
│   │   ├── /feature-2
│   │   └── ...
│   ├── /integrations
│   │   ├── /integration-1
│   │   └── ...
│   └── /security
├── /solutions
│   ├── /by-industry
│   │   ├── /industry-1
│   │   └── ...
│   └── /by-use-case
│       ├── /use-case-1
│       └── ...
├── /pricing
├── /customers
│   ├── /case-studies
│   │   ├── /case-study-1
│   │   └── ...
│   └── /testimonials
├── /resources
│   ├── /blog
│   ├── /guides
│   ├── /webinars
│   ├── /templates
│   └── /glossary
├── /docs (or /help)
│   └── /api
├── /company
│   ├── /about
│   ├── /careers
│   ├── /press
│   └── /contact
└── /compare
    ├── /vs-competitor-1
    └── /vs-competitor-2
```

## Content Priorities

### High Priority Pages
1. Homepage (value proposition, social proof)
2. Features overview
3. Pricing page
4. Key integrations
5. Top 3-5 use case pages

### Medium Priority Pages
1. Individual feature pages
2. Industry solution pages
3. Case studies (2-3 detailed ones)
4. Comparison pages (vs competitors)

### Content Marketing Focus
1. Bottom-of-funnel: Comparison guides, ROI calculators
2. Middle-of-funnel: How-to guides, best practices
3. Top-of-funnel: Industry trends, educational content

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, WebSite, SoftwareApplication |
| Product/Features | SoftwareApplication, Offer |
| Pricing | SoftwareApplication, Offer (with pricing) |
| Blog | Article, BlogPosting |
| Case Studies | Article, Organization (customer) |
| Documentation | TechArticle |

## Key Metrics to Track

- Organic traffic to pricing page
- Demo/trial signups from organic
- Blog → pricing page conversion
- Comparison page rankings
- Integration page performance

## Comparison & Alternative Pages

Comparison pages are among the highest-converting content types for SaaS, with conversion rates of **4-7%** vs. 0.5-1.8% for standard blog content (35.8% of marketers report comparison content performs "better than ever" per Intergrowth November 2025 survey).

**Recommended page types:**
- `/{product}-vs-{competitor}`: Direct 1:1 comparison
- `/{competitor}-alternative`: Targeting competitor brand searches
- `/compare/{category}`: Category comparison hub
- `/best-{category}-tools`: Roundup-style pages

**Best practices:**
- Include structured comparison tables with pricing, features, pros/cons
- Be factually accurate about competitors: verify claims regularly
- Include customer testimonials from users who switched
- Add FAQ schema for common comparison questions (valuable for AI search)
- Update regularly: stale comparison data damages credibility
- Cross-reference the `seo-competitor-pages` skill for detailed frameworks

**Legal considerations:**
- Nominative fair use generally permits competitor brand mentions for comparison purposes
- Do NOT imply endorsement or affiliation
- Do NOT make false or unverifiable claims about competitor products
- Different jurisdictions have different trademark laws: consult legal counsel

## Competitive Considerations

- Monitor competitor feature releases
- Track competitor content strategies
- Identify keyword gaps in feature coverage
- Watch for new comparison opportunities

## Generative Engine Optimization (GEO) for SaaS

- [ ] Include clear, structured feature comparisons that AI systems can parse and cite
- [ ] Use SoftwareApplication schema with complete feature lists and pricing
- [ ] Publish original benchmark data, case studies, and ROI metrics
- [ ] Build content clusters around key product categories and use cases
- [ ] Ensure integration pages have clear, quotable descriptions
- [ ] Structure pricing information in tables AI can extract
- [ ] Monitor AI citation across Google AI Overviews, ChatGPT, and Perplexity
```

## File: `skills/seo-programmatic/SKILL.md`
```markdown
---
name: seo-programmatic
description: >
  Programmatic SEO planning and analysis for pages generated at scale from data
  sources. Covers template engines, URL patterns, internal linking automation,
  thin content safeguards, and index bloat prevention. Use when user says
  "programmatic SEO", "pages at scale", "dynamic pages", "template pages",
  "generated pages", or "data-driven SEO".
user-invokable: true
argument-hint: "[url or plan]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Programmatic SEO Analysis & Planning

Build and audit SEO pages generated at scale from structured data sources.
Enforces quality gates to prevent thin content penalties and index bloat.

## Data Source Assessment

Evaluate the data powering programmatic pages:
- **CSV/JSON files**: Row count, column uniqueness, missing values
- **API endpoints**: Response structure, data freshness, rate limits
- **Database queries**: Record count, field completeness, update frequency
- Data quality checks:
  - Each record must have enough unique attributes to generate distinct content
  - Flag duplicate or near-duplicate records (>80% field overlap)
  - Verify data freshness; stale data produces stale pages

## Template Engine Planning

Design templates that produce unique, valuable pages:
- **Variable injection points**: Title, H1, body sections, meta description, schema
- **Content blocks**: Static (shared across pages) vs dynamic (unique per page)
- **Conditional logic**: Show/hide sections based on data availability
- **Supplementary content**: Related items, contextual tips, user-generated content
- Template review checklist:
  - Each page must read as a standalone, valuable resource
  - No "mad-libs" patterns (just swapping city/product names in identical text)
  - Dynamic sections must add genuine information, not just keyword variations

## URL Pattern Strategy

### Common Patterns
- `/tools/[tool-name]`: Tool/product directory pages
- `/[city]/[service]`: Location + service pages
- `/integrations/[platform]`: Integration landing pages
- `/glossary/[term]`: Definition/reference pages
- `/templates/[template-name]`: Downloadable template pages

### URL Rules
- Lowercase, hyphenated slugs derived from data
- Logical hierarchy reflecting site architecture
- No duplicate slugs; enforce uniqueness at generation time
- Keep URLs under 100 characters
- No query parameters for primary content URLs
- Consistent trailing slash usage (match existing site pattern)

## Internal Linking Automation

- **Hub/spoke model**: Category hub pages linking to individual programmatic pages
- **Related items**: Auto-link to 3-5 related pages based on data attributes
- **Breadcrumbs**: Generate BreadcrumbList schema from URL hierarchy
- **Cross-linking**: Link between programmatic pages sharing attributes (same category, same city, same feature)
- **Anchor text**: Use descriptive, varied anchor text. Avoid exact-match keyword repetition
- Link density: 3-5 internal links per 1000 words (match seo-content guidelines)

## Thin Content Safeguards

### Quality Gates

| Metric | Threshold | Action |
|--------|-----------|--------|
| Pages without content review | 100+ | ⚠️ WARNING: require content audit before publishing |
| Pages without justification | 500+ | 🛑 HARD STOP: require explicit user approval and thin content audit |
| Unique content per page | <40% | ❌ Flag as thin content (likely penalty risk) |
| Word count per page | <300 | ⚠️ Flag for review (may lack sufficient value) |

### Scaled Content Abuse: Enforcement Context (2025-2026)

Google's Scaled Content Abuse policy (introduced March 2024) saw major enforcement escalation in 2025:

- **June 2025:** Wave of manual actions targeting websites with AI-generated content at scale
- **August 2025:** SpamBrain spam update enhanced pattern detection for AI-generated link schemes and content farms
- **Result:** Google reported 45% reduction in low-quality, unoriginal content in search results post-March 2024 enforcement

**Enhanced quality gates for programmatic pages:**
- **Content differentiation:** ≥30-40% of content must be genuinely unique between any two programmatic pages (not just city/keyword string replacement)
- **Human review:** Minimum 5-10% sample review of generated pages before publishing
- **Progressive rollout:** Publish in batches of 50-100 pages. Monitor indexing and rankings for 2-4 weeks before expanding. Never publish 500+ programmatic pages simultaneously without explicit quality review.
- **Standalone value test:** Each page should pass: "Would this page be worth publishing even if no other similar pages existed?"
- **Site reputation abuse:** If publishing programmatic content under a high-authority domain (not your own), this may trigger site reputation abuse penalties. Google began enforcing this aggressively in November 2024.

> **Recommendation:** The WARNING gate at `<40% unique content` remains appropriate. Consider a HARD STOP at `<30%` unique content to prevent scaled content abuse risk.

### Safe Programmatic Pages (OK at scale)
✅ Integration pages (with real setup docs, API details, screenshots)
✅ Template/tool pages (with downloadable content, usage instructions)
✅ Glossary pages (200+ word definitions with examples, related terms)
✅ Product pages (unique specs, reviews, comparison data)
✅ Data-driven pages (unique statistics, charts, analysis per record)

### Penalty Risk (avoid at scale)
❌ Location pages with only city name swapped in identical text
❌ "Best [tool] for [industry]" without industry-specific value
❌ "[Competitor] alternative" without real comparison data
❌ AI-generated pages without human review and unique value-add
❌ Pages where >60% of content is shared template boilerplate

### Uniqueness Calculation
Unique content % = (words unique to this page) / (total words on page) × 100

Measure against all other pages in the programmatic set. Shared headers, footers, and navigation are excluded from the calculation. Template boilerplate text IS included.

## Canonical Strategy

- Every programmatic page must have a self-referencing canonical tag
- Parameter variations (sort, filter, pagination) canonical to the base URL
- Paginated series: canonical to page 1 or use rel=next/prev
- If programmatic pages overlap with manual pages, the manual page is canonical
- No canonical to a different domain unless intentional cross-domain setup

## Sitemap Integration

- Auto-generate sitemap entries for all programmatic pages
- Split at 50,000 URLs per sitemap file (protocol limit)
- Use sitemap index if multiple sitemap files needed
- `<lastmod>` reflects actual data update timestamp (not generation time)
- Exclude noindexed programmatic pages from sitemap
- Register sitemap in robots.txt
- Update sitemap dynamically as new records are added to data source

## Index Bloat Prevention

- **Noindex low-value pages**: Pages that don't meet quality gates
- **Pagination**: Noindex paginated results beyond page 1 (or use rel=next/prev)
- **Faceted navigation**: Noindex filtered views, canonical to base category
- **Crawl budget**: For sites with >10k programmatic pages, monitor crawl stats in Search Console
- **Thin page consolidation**: Merge records with insufficient data into aggregated pages
- **Regular audits**: Monthly review of indexed page count vs intended count

## Output

### Programmatic SEO Score: XX/100

### Assessment Summary
| Category | Status | Score |
|----------|--------|-------|
| Data Quality | ✅/⚠️/❌ | XX/100 |
| Template Uniqueness | ✅/⚠️/❌ | XX/100 |
| URL Structure | ✅/⚠️/❌ | XX/100 |
| Internal Linking | ✅/⚠️/❌ | XX/100 |
| Thin Content Risk | ✅/⚠️/❌ | XX/100 |
| Index Management | ✅/⚠️/❌ | XX/100 |

### Critical Issues (fix immediately)
### High Priority (fix within 1 week)
### Medium Priority (fix within 1 month)
### Low Priority (backlog)

### Recommendations
- Data source improvements
- Template modifications
- URL pattern adjustments
- Quality gate compliance actions

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL accessibility and checking for authentication requirements. |
| No programmatic pages detected | Inform user that no template-generated or data-driven page patterns were found. Suggest checking if pages use client-side rendering or if the URL points to the correct section. |
| Thin content threshold exceeded | Trigger quality gate warning. Report the unique content percentage and flag pages below 40% uniqueness. Require user acknowledgment before proceeding. |
| Quality gate violation | Halt analysis at the HARD STOP threshold (500+ pages without justification or <30% unique content). Present findings and require explicit user approval to continue. |
```

## File: `skills/seo-schema/SKILL.md`
```markdown
---
name: seo-schema
description: >
  Detect, validate, and generate Schema.org structured data. JSON-LD format
  preferred. Use when user says "schema", "structured data", "rich results",
  "JSON-LD", or "markup".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Schema Markup Analysis & Generation

## Detection

1. Scan page source for JSON-LD `<script type="application/ld+json">`
2. Check for Microdata (`itemscope`, `itemprop`)
3. Check for RDFa (`typeof`, `property`)
4. Always recommend JSON-LD as primary format (Google's stated preference)

## Validation

- Check required properties per schema type
- Validate against Google's supported rich result types
- Test for common errors:
  - Missing @context
  - Invalid @type
  - Wrong data types
  - Placeholder text
  - Relative URLs (should be absolute)
  - Invalid date formats
- Flag deprecated types (see below)

## Schema Type Status (as of Feb 2026)

Read `references/schema-types.md` for the full list. Key rules:

### ACTIVE (recommend freely):
Organization, LocalBusiness, SoftwareApplication, WebApplication, Product (with Certification markup as of April 2025), ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

### VIDEO & SPECIALIZED (recommend freely):
BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode

See `schema/templates.json` for ready-to-use JSON-LD templates for these types.

> **JSON-LD and JavaScript rendering:** Per Google's December 2025 JS SEO guidance, structured data injected via JavaScript may face delayed processing. For time-sensitive markup (especially Product, Offer), include JSON-LD in the initial server-rendered HTML.

### RESTRICTED (only for specific sites):
- **FAQ**: ONLY for government and healthcare authority sites (restricted Aug 2023)

### DEPRECATED (never recommend):
- **HowTo**: Rich results removed September 2023
- **SpecialAnnouncement**: Deprecated July 31, 2025
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired June 2025
- **ClaimReview**: Retired from rich results June 2025
- **VehicleListing**: Retired from rich results June 2025
- **Practice Problem**: Retired from rich results late 2025
- **Dataset**: Retired from rich results late 2025
- **Book Actions**: Deprecated then reversed, still functional as of Feb 2026 (historical note)

## Generation

When generating schema for a page:
1. Identify page type from content analysis
2. Select appropriate schema type(s)
3. Generate valid JSON-LD with all required + recommended properties
4. Include only truthful, verifiable data. Use placeholders clearly marked for user to fill
5. Validate output before presenting

## Common Schema Templates

### Organization
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}
```

### LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
```

### Article/BlogPosting
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}
```

## Output

- `SCHEMA-REPORT.md`: detection and validation results
- `generated-schema.json`: ready-to-use JSON-LD snippets

### Validation Results
| Schema | Type | Status | Issues |
|--------|------|--------|--------|
| ... | ... | ✅/⚠️/❌ | ... |

### Recommendations
- Missing schema opportunities
- Validation fixes needed
- Generated code for implementation

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL and checking if the page requires authentication. |
| No schema markup found | Report that no JSON-LD, Microdata, or RDFa was detected. Recommend appropriate schema types based on page content analysis. |
| Invalid JSON-LD syntax | Parse and report specific syntax errors (missing brackets, trailing commas, unquoted keys). Provide corrected JSON-LD output. |
| Deprecated schema type detected | Flag the deprecated type with its retirement date. Recommend the current replacement type or advise removal if no replacement exists. |
```

## File: `skills/seo-sitemap/SKILL.md`
```markdown
---
name: seo-sitemap
description: >
  Analyze existing XML sitemaps or generate new ones with industry templates.
  Validates format, URLs, and structure. Use when user says "sitemap",
  "generate sitemap", "sitemap issues", or "XML sitemap".
user-invokable: true
argument-hint: "[url or generate]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Sitemap Analysis & Generation

## Mode 1: Analyze Existing Sitemap

### Validation Checks
- Valid XML format
- URL count <50,000 per file (protocol limit)
- All URLs return HTTP 200
- `<lastmod>` dates are accurate (not all identical)
- No deprecated tags: `<priority>` and `<changefreq>` are ignored by Google
- Sitemap referenced in robots.txt
- Compare crawled pages vs sitemap; flag missing pages

### Quality Signals
- Sitemap index file if >50k URLs
- Split by content type (pages, posts, images, videos)
- No non-canonical URLs in sitemap
- No noindexed URLs in sitemap
- No redirected URLs in sitemap
- HTTPS URLs only (no HTTP)

### Common Issues
| Issue | Severity | Fix |
|-------|----------|-----|
| >50k URLs in single file | Critical | Split with sitemap index |
| Non-200 URLs | High | Remove or fix broken URLs |
| Noindexed URLs included | High | Remove from sitemap |
| Redirected URLs included | Medium | Update to final URLs |
| All identical lastmod | Low | Use actual modification dates |
| Priority/changefreq used | Info | Can remove (ignored by Google) |

## Mode 2: Generate New Sitemap

### Process
1. Ask for business type (or auto-detect from existing site)
2. Load industry template from `../seo-plan/assets/` directory
3. Interactive structure planning with user
4. Apply quality gates:
   - ⚠️ WARNING at 30+ location pages (require 60%+ unique content)
   - 🛑 HARD STOP at 50+ location pages (require justification)
5. Generate valid XML output
6. Split at 50k URLs with sitemap index
7. Generate STRUCTURE.md documentation

### Safe Programmatic Pages (OK at scale)
✅ Integration pages (with real setup docs)
✅ Template/tool pages (with downloadable content)
✅ Glossary pages (200+ word definitions)
✅ Product pages (unique specs, reviews)
✅ User profile pages (user-generated content)

### Penalty Risk (avoid at scale)
❌ Location pages with only city name swapped
❌ "Best [tool] for [industry]" without industry-specific value
❌ "[Competitor] alternative" without real comparison data
❌ AI-generated pages without human review and unique value

## Sitemap Format

### Standard Sitemap
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2026-02-07</lastmod>
  </url>
</urlset>
```

### Sitemap Index (for >50k URLs)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-posts.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
</sitemapindex>
```

## Error Handling

- **URL unreachable**: Report the HTTP status code and suggest checking if the site is live
- **No sitemap found**: Check common locations (/sitemap.xml, /sitemap_index.xml, robots.txt reference) before reporting "not found"
- **Invalid XML format**: Report specific parsing errors with line numbers
- **Rate limiting detected**: Back off and report partial results with a note about retry timing

## Output

### For Analysis
- `VALIDATION-REPORT.md`: analysis results
- Issues list with severity
- Recommendations

### For Generation
- `sitemap.xml` (or split files with index)
- `STRUCTURE.md`: site architecture documentation
- URL count and organization summary
```

## File: `skills/seo-technical/SKILL.md`
```markdown
---
name: seo-technical
description: >
  Technical SEO audit across 9 categories: crawlability, indexability, security,
  URL structure, mobile, Core Web Vitals, structured data, JavaScript rendering,
  and IndexNow protocol. Use when user says "technical SEO", "crawl issues",
  "robots.txt", "Core Web Vitals", "site speed", or "security headers".
user-invokable: true
argument-hint: "[url]"
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata:
  author: AgriciDaniel
  version: "1.7.0"
  category: seo
---

# Technical SEO Audit

## Categories

### 1. Crawlability
- robots.txt: exists, valid, not blocking important resources
- XML sitemap: exists, referenced in robots.txt, valid format
- Noindex tags: intentional vs accidental
- Crawl depth: important pages within 3 clicks of homepage
- JavaScript rendering: check if critical content requires JS execution
- Crawl budget: for large sites (>10k pages), efficiency matters

#### AI Crawler Management

As of 2025-2026, AI companies actively crawl the web to train models and power AI search. Managing these crawlers via robots.txt is a critical technical SEO consideration.

**Known AI crawlers:**

| Crawler | Company | robots.txt token | Purpose |
|---------|---------|-----------------|---------|
| GPTBot | OpenAI | `GPTBot` | Model training |
| ChatGPT-User | OpenAI | `ChatGPT-User` | Real-time browsing |
| ClaudeBot | Anthropic | `ClaudeBot` | Model training |
| PerplexityBot | Perplexity | `PerplexityBot` | Search index + training |
| Bytespider | ByteDance | `Bytespider` | Model training |
| Google-Extended | Google | `Google-Extended` | Gemini training (NOT search) |
| CCBot | Common Crawl | `CCBot` | Open dataset |

**Key distinctions:**
- Blocking `Google-Extended` prevents Gemini training use but does NOT affect Google Search indexing or AI Overviews (those use `Googlebot`)
- Blocking `GPTBot` prevents OpenAI training but does NOT prevent ChatGPT from citing your content via browsing (`ChatGPT-User`)
- ~3-5% of websites now use AI-specific robots.txt rules

**Example, selective AI crawler blocking:**
```
# Allow search indexing, block AI training crawlers
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /

# Allow all other crawlers (including Googlebot for search)
User-agent: *
Allow: /
```

**Recommendation:** Consider your AI visibility strategy before blocking. Being cited by AI systems drives brand awareness and referral traffic. Cross-reference the `seo-geo` skill for full AI visibility optimization.

### 2. Indexability
- Canonical tags: self-referencing, no conflicts with noindex
- Duplicate content: near-duplicates, parameter URLs, www vs non-www
- Thin content: pages below minimum word counts per type
- Pagination: rel=next/prev or load-more pattern
- Hreflang: correct for multi-language/multi-region sites
- Index bloat: unnecessary pages consuming crawl budget

### 3. Security
- HTTPS: enforced, valid SSL certificate, no mixed content
- Security headers:
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Frame-Options
  - X-Content-Type-Options
  - Referrer-Policy
- HSTS preload: check preload list inclusion for high-security sites

### 4. URL Structure
- Clean URLs: descriptive, hyphenated, no query parameters for content
- Hierarchy: logical folder structure reflecting site architecture
- Redirects: no chains (max 1 hop), 301 for permanent moves
- URL length: flag >100 characters
- Trailing slashes: consistent usage

### 5. Mobile Optimization
- Responsive design: viewport meta tag, responsive CSS
- Touch targets: minimum 48x48px with 8px spacing
- Font size: minimum 16px base
- No horizontal scroll
- Mobile-first indexing: Google indexes mobile version. **Mobile-first indexing is 100% complete as of July 5, 2024.** Google now crawls and indexes ALL websites exclusively with the mobile Googlebot user-agent.

### 6. Core Web Vitals
- **LCP** (Largest Contentful Paint): target <2.5s
- **INP** (Interaction to Next Paint): target <200ms
  - INP replaced FID on March 12, 2024. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on September 9, 2024. Do NOT reference FID anywhere.
- **CLS** (Cumulative Layout Shift): target <0.1
- Evaluation uses 75th percentile of real user data
- Use PageSpeed Insights API or CrUX data if MCP available

### 7. Structured Data
- Detection: JSON-LD (preferred), Microdata, RDFa
- Validation against Google's supported types
- See seo-schema skill for full analysis

### 8. JavaScript Rendering
- Check if content visible in initial HTML vs requires JS
- Identify client-side rendered (CSR) vs server-side rendered (SSR)
- Flag SPA frameworks (React, Vue, Angular) that may cause indexing issues
- Verify dynamic rendering setup if applicable

#### JavaScript SEO: Canonical & Indexing Guidance (December 2025)

Google updated its JavaScript SEO documentation in December 2025 with critical clarifications:

1. **Canonical conflicts:** If a canonical tag in raw HTML differs from one injected by JavaScript, Google may use EITHER one. Ensure canonical tags are identical between server-rendered HTML and JS-rendered output.
2. **noindex with JavaScript:** If raw HTML contains `<meta name="robots" content="noindex">` but JavaScript removes it, Google MAY still honor the noindex from raw HTML. Serve correct robots directives in the initial HTML response.
3. **Non-200 status codes:** Google does NOT render JavaScript on pages returning non-200 HTTP status codes. Any content or meta tags injected via JS on error pages will be invisible to Googlebot.
4. **Structured data in JavaScript:** Product, Article, and other structured data injected via JS may face delayed processing. For time-sensitive structured data (especially e-commerce Product markup), include it in the initial server-rendered HTML.

**Best practice:** Serve critical SEO elements (canonical, meta robots, structured data, title, meta description) in the initial server-rendered HTML rather than relying on JavaScript injection.

### 9. IndexNow Protocol
- Check if site supports IndexNow for Bing, Yandex, Naver
- Supported by search engines other than Google
- Recommend implementation for faster indexing on non-Google engines

## Output

### Technical Score: XX/100

### Category Breakdown
| Category | Status | Score |
|----------|--------|-------|
| Crawlability | pass/warn/fail | XX/100 |
| Indexability | pass/warn/fail | XX/100 |
| Security | pass/warn/fail | XX/100 |
| URL Structure | pass/warn/fail | XX/100 |
| Mobile | pass/warn/fail | XX/100 |
| Core Web Vitals | pass/warn/fail | XX/100 |
| Structured Data | pass/warn/fail | XX/100 |
| JS Rendering | pass/warn/fail | XX/100 |
| IndexNow | pass/warn/fail | XX/100 |

### Critical Issues (fix immediately)
### High Priority (fix within 1 week)
### Medium Priority (fix within 1 month)
### Low Priority (backlog)

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `on_page_instant_pages` for real page analysis (status codes, page timing, broken links, on-page checks), `on_page_lighthouse` for Lighthouse audits (performance, accessibility, SEO scores), and `domain_analytics_technologies_domain_technologies` for technology stack detection.

## Google API Integration (Optional)

If Google API credentials are configured, use `python scripts/pagespeed_check.py <url> --json` for real PSI + CrUX field data (replaces lab-only CWV estimates), `python scripts/crux_history.py <url> --json` for 25-week CWV trends, and `python scripts/gsc_inspect.py <url> --json` for real indexation status per URL.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL, checking DNS resolution, and confirming the site is publicly accessible. |
| robots.txt not found | Note that no robots.txt was detected at the root domain. Recommend creating one with appropriate directives. Continue audit on remaining categories. |
| HTTPS not configured | Flag as a critical issue. Report whether HTTP is served without redirect, mixed content exists, or SSL certificate is missing/expired. |
| Core Web Vitals data unavailable | Note that CrUX data is not available (common for low-traffic sites). Suggest using Lighthouse lab data as a proxy and recommend increasing traffic before re-testing. |
```

