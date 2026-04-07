---
id: claude-seo
type: knowledge
owner: OA_Triage
---
# claude-seo
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- Updated: 2026-03-28 -->

![Claude SEO](screenshots/cover-image.jpeg)

# Claude SEO - SEO Audit Skill for Claude Code

Comprehensive SEO analysis skill for Claude Code. Covers technical SEO, on-page analysis, content quality (E-E-A-T), schema markup, image optimization, sitemap architecture, AI search optimization (GEO), local SEO, maps intelligence, Google SEO APIs (Search Console, PageSpeed, CrUX, GA4), PDF report generation, and strategic planning.

![SEO Command Demo](screenshots/seo-command-demo.gif)

[![CI](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml/badge.svg)](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-seo)](https://github.com/AgriciDaniel/claude-seo/releases)

> **Blog:** [Full breakdown of the Claude Code SEO stack](https://agricidaniel.com/blog/claude-code-seo-stack) | [v1.7.2 release: Firecrawl backlink analysis](https://agricidaniel.com/blog/claude-seo-172-firecrawl-backlink-analysis)

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

### Plugin Install (Claude Code 1.0.33+)

```bash
# Add marketplace (one-time)
/plugin marketplace add AgriciDaniel/claude-seo

# Install plugin
/plugin install claude-seo@AgriciDaniel-claude-seo
```

### Manual Install (Unix/macOS/Linux)

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

Integrates with MCP servers for live SEO data, including official servers from **Ahrefs** (`@ahrefs/mcp`) and **Semrush**, plus community servers for Google Search Console, PageSpeed Insights, and DataForSEO. See [MCP Integration Guide](docs/MCP-INTEGRATION.md) for setup.

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

See [DataForSEO Extension](extensions/dataforseo/README.md) for full documentation.

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

See [Banana Extension](extensions/banana/README.md) for full documentation.
Already using standalone Claude Banana? The extension reuses your existing nanobanana-mcp setup.

## Ecosystem

Claude SEO is part of a family of Claude Code skills that work together:

| Skill | What it does | How it connects |
|-------|-------------|-----------------|
| [Claude SEO](https://github.com/AgriciDaniel/claude-seo) | SEO analysis, audits, schema, GEO | Core -- analyzes sites, generates action plans |
| [Claude Blog](https://github.com/AgriciDaniel/claude-blog) | Blog writing, optimization, scoring | Companion -- write content optimized by SEO findings |
| [Claude Banana](https://github.com/AgriciDaniel/banana-claude) | AI image generation via Gemini | Shared -- generates images for SEO assets and blog posts |
| [AI Marketing Claude](https://github.com/zubair-trabzada/ai-marketing-claude) | Copywriting, emails, social, ads, funnels, CRO | Community -- post-audit marketing action from SEO findings |

**Workflow example:**
1. `/seo audit https://example.com` -- identify content gaps and technical issues
2. `/seo backlinks https://example.com` -- analyze link profile and competitor gaps
3. `/blog write "target keyword"` -- create SEO-optimized blog posts
4. `/seo image-gen hero "blog topic"` -- generate hero images (banana extension)
5. `/seo geo https://example.com/blog/post` -- optimize for AI citations

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Commands Reference](docs/COMMANDS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [MCP Integration](docs/MCP-INTEGRATION.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting PRs.

---

Built for Claude Code by [@AgriciDaniel](https://github.com/AgriciDaniel)

```

### File: requirements.txt
```txt
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

# Report generation (for seo-google PDF/Excel reports)
matplotlib>=3.8.0,<4.0.0              # No known CVEs
weasyprint>=61.0,<70.0                # No known CVEs
openpyxl>=3.1.0,<4.0.0                # No known CVEs (Excel export)

# Google API dependencies (for seo-google skill)
google-api-python-client>=2.100.0,<3.0.0   # No known CVEs
google-auth>=2.20.0,<3.0.0                  # No known CVEs
google-auth-oauthlib>=1.0.0,<2.0.0          # No known CVEs
google-auth-httplib2>=0.2.0,<1.0.0           # No known CVEs
google-analytics-data>=0.18.0,<1.0.0         # No known CVEs

```

### File: extensions\banana\README.md
```md
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

See [docs/BANANA-SETUP.md](docs/BANANA-SETUP.md) for detailed setup instructions
and common issues.

```

### File: extensions\dataforseo\README.md
```md
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

### File: extensions\firecrawl\README.md
```md
# Firecrawl Extension for Claude SEO

Full-site crawling, scraping, and site mapping powered by [Firecrawl](https://www.firecrawl.dev/). Enables comprehensive site-wide SEO analysis with JavaScript rendering support.

## Prerequisites

- [Claude SEO](https://github.com/AgriciDaniel/claude-seo) installed
- Node.js 20+
- Firecrawl API key ([sign up](https://www.firecrawl.dev/app/sign-up) -- free tier: 500 credits/month)

## Installation

### macOS / Linux

```bash
./extensions/firecrawl/install.sh
```

### Windows (PowerShell)

```powershell
.\extensions\firecrawl\install.ps1
```

The installer will prompt for your Firecrawl API key and configure the MCP server automatically.

## Commands

| Command | Purpose | Credits |
|---------|---------|---------|
| `/seo firecrawl crawl <url>` | Full-site crawl with content extraction | 1 per page |
| `/seo firecrawl map <url>` | Discover site structure (URLs only) | 0.5 per URL |
| `/seo firecrawl scrape <url>` | Single-page deep scrape with JS rendering | 1 |
| `/seo firecrawl search <query> <url>` | Search within a site | 1 per result |

## Integration with Claude SEO

When installed, other Claude SEO skills automatically leverage Firecrawl:

- **`/seo audit`**: Uses `map` to discover all pages, then `crawl` for deep analysis
- **`/seo technical`**: Broken link detection across entire site
- **`/seo sitemap`**: Compare XML sitemap vs actual crawlable pages
- **`/seo content`**: Thin content detection at scale

## Cost

| Plan | Credits/month | Price |
|------|--------------|-------|
| Free | 500 | $0 |
| Hobby | 3,000 | $16/mo |
| Standard | 100,000 | $83/mo |
| Growth | 500,000 | $333/mo |

1 credit = 1 page crawled or scraped. Map operations use 0.5 credits per URL.

## Troubleshooting

**MCP not connecting?**
- Check: `cat ~/.claude/settings.json | python3 -m json.tool | grep firecrawl`
- Manual config: See [FIRECRAWL-SETUP.md](docs/FIRECRAWL-SETUP.md)

**Credits exhausted?**
- Check usage: https://www.firecrawl.dev/app
- Upgrade plan or wait for monthly reset

**Site blocking crawls?**
- Some sites block automated crawling via robots.txt or Cloudflare
- Try `scrape` (single page) instead of `crawl` (full site)
- Fall back to `fetch_page.py` for basic HTML retrieval

## Uninstall

```bash
./extensions/firecrawl/uninstall.sh      # macOS/Linux
.\extensions\firecrawl\uninstall.ps1     # Windows
```

## Links

- [Firecrawl Documentation](https://docs.firecrawl.dev/)
- [Firecrawl MCP Server](https://www.npmjs.com/package/firecrawl-mcp)
- [Claude SEO](https://github.com/AgriciDaniel/claude-seo)

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.2] - 2026-03-30

### Added
- **Firecrawl extension**: Full-site crawling, scraping, and site mapping via Firecrawl MCP (`extensions/firecrawl/`)
  - 4 commands: crawl, map, scrape, search
  - JS rendering support for SPA/CSR sites (addresses #11)
  - Cross-skill integration with audit, technical, sitemap, and content skills
  - Self-contained install/uninstall scripts (Bash + PowerShell)
- **Backlink analysis skill**: `skills/seo-backlinks/SKILL.md` with `/seo backlinks` command
  - 7-section analysis: profile overview, anchor text, referring domain quality, toxic links, top pages, competitor gap, new/lost links
  - Backlink health score (0-100) with weighted factors
  - Disavow recommendations with export format
  - Requires DataForSEO extension for live data
- **Backlink quality reference**: `skills/seo/references/backlink-quality.md` with 30 toxic link patterns, anchor text benchmarks by industry
- **Excel export**: `--format xlsx` option in `scripts/google_report.py`
  - Sheets: Summary, Queries, Pages, Indexation (conditional on data available)
  - Navy header styling matching PDF palette, auto-column-width, frozen headers, auto-filter
  - New format options: `xlsx`, `all` (pdf+html+xlsx)
- **Ecosystem cross-links**: AI Marketing Claude added to README and CLAUDE.md ecosystem sections

### Changed
- Sub-skill count: 18 -> 19 (added seo-backlinks)
- Extension count: 2 -> 3 (added Firecrawl)
- Orchestrator routing table updated with `/seo backlinks` and `/seo firecrawl` commands
- Audit orchestration: Firecrawl `map` used for URL discovery when available
- `requirements.txt`: added `openpyxl>=3.1.0` for Excel export

## [1.7.1] - 2026-03-30

### Fixed
- install.sh: broken skill copy path `seo/` corrected to `skills/seo/` (h/t @hieu-e via #39)
- install.sh: version tag pinned to v1.7.1 (was stuck at v1.6.0)
- install.ps1: version tag pinned to v1.7.1 (was stuck at v1.6.0)
- install.ps1: removed unnecessary `seo/` fallback path, uses `skills\seo` directly

### Changed
- CI: syntax check expanded from 4 to 15 Python scripts (all v1.7.0 Google API scripts now covered)

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
- **Python requirement**: Corrected from `3.8+` to `3.10+` in `README.md` and `docs/INSTALLATION.md`.

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
- **WebApplication schema**: Added as correct type for bro
... [TRUNCATED]
```

### File: claude-seo-v1.8.0-release.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
@page {
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
}
@page :first {
    margin: 0;
}

body {
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #2d2d2d;
}

/* Title page */
.title-page {
    page-break-after: always;
    height: 297mm;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    padding: 40mm 30mm;
    background: #ffffff;
    position: relative;
}
.title-page::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 8mm;
    background: #1e3a5f;
}
.title-page::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3mm;
    background: #b8860b;
}
.title-page h1 {
    font-size: 32pt;
    color: #1e3a5f;
    margin: 0 0 8mm 0;
    font-weight: 700;
    letter-spacing: -0.5px;
}
.title-page .subtitle {
    font-size: 16pt;
    color: #555;
    margin: 0 0 12mm 0;
}
.title-page .version {
    font-size: 22pt;
    color: #b8860b;
    font-weight: 600;
    margin: 0 0 8mm 0;
}
.title-page .date {
    font-size: 12pt;
    color: #777;
    margin: 4mm 0;
}
.title-page .author {
    font-size: 11pt;
    color: #999;
    margin: 2mm 0;
}
.title-page .url {
    font-size: 10pt;
    color: #1e3a5f;
    margin: 8mm 0 0 0;
}

/* Section headings */
h2 {
    font-size: 17pt;
    color: #1e3a5f;
    border-bottom: 2px solid #b8860b;
    padding-bottom: 3mm;
    margin-top: 10mm;
    margin-bottom: 5mm;
    page-break-after: avoid;
}
h3 {
    font-size: 13pt;
    color: #1e3a5f;
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
}
h4 {
    font-size: 11pt;
    color: #b8860b;
    margin-top: 5mm;
    margin-bottom: 2mm;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 9.5pt;
}
th {
    background: #1e3a5f;
    color: #fff;
    padding: 2.5mm 3mm;
    text-align: left;
    font-weight: 600;
}
td {
    padding: 2mm 3mm;
    border-bottom: 0.5px solid #ddd;
    vertical-align: top;
}
tr:nth-child(even) td {
    background: #faf9f7;
}

/* Code blocks */
code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    background: #f0f0f0;
    padding: 0.5mm 1.5mm;
    border-radius: 1mm;
}
pre {
    background: #1e2a3a;
    color: #e0e8f0;
    padding: 4mm;
    border-radius: 2mm;
    font-size: 8.5pt;
    line-height: 1.5;
    overflow: hidden;
    white-space: pre-wrap;
    margin: 3mm 0;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 1mm 3mm;
    border-radius: 1mm;
    font-size: 8pt;
    font-weight: 600;
    color: #fff;
    margin: 0 1mm;
}
.badge-pass { background: #2d6a4f; }
.badge-warn { background: #d4740e; }
.badge-fail { background: #c53030; }
.badge-info { background: #1e3a5f; }
.badge-new { background: #b8860b; }

/* Callout boxes */
.callout {
    border-left: 4px solid #b8860b;
    background: #faf9f7;
    padding: 3mm 4mm;
    margin: 4mm 0;
    border-radius: 0 2mm 2mm 0;
}
.callout-blue {
    border-left-color: #1e3a5f;
}

/* Architecture diagram */
.arch-box {
    background: #1e2a3a;
    color: #e0e8f0;
    padding: 5mm;
    border-radius: 2mm;
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.6;
    margin: 4mm 0;
}

/* Footer */
.footer {
    font-size: 8pt;
    color: #999;
    text-align: center;
    margin-top: 10mm;
    padding-top: 3mm;
    border-top: 0.5px solid #ddd;
}

/* Tier diagram */
.tier-box {
    border: 1.5px solid #1e3a5f;
    border-radius: 3mm;
    padding: 4mm;
    margin: 3mm 0;
    background: #faf9f7;
}
.tier-box .tier-label {
    font-weight: 700;
    color: #1e3a5f;
    font-size: 11pt;
}
.tier-box .tier-desc {
    color: #555;
    font-size: 9.5pt;
    margin-top: 1mm;
}

ul { margin: 2mm 0; padding-left: 6mm; }
li { margin: 1mm 0; }
</style>
</head>
<body>

<!-- TITLE PAGE -->
<div class="title-page">
    <h1>Claude SEO</h1>
    <div class="subtitle">Free Backlink Data Integration</div>
    <div class="version">v1.8.0 Release Notes</div>
    <div class="date">March 31, 2026</div>
    <div class="author">by AgriciDaniel</div>
    <div class="url">github.com/AgriciDaniel/claude-seo</div>
</div>

<!-- EXECUTIVE SUMMARY -->
<h2>Executive Summary</h2>

<p>Version 1.8.0 transforms the <code>/seo backlinks</code> command from a paid-only feature into a <strong>multi-tier free-to-premium</strong> backlink analysis system. Users can now get actionable backlink intelligence with zero cost and zero configuration, with progressively richer data as they add free API keys.</p>

<div class="callout">
<strong>Key achievement:</strong> Free sources combined can capture <strong>60–70% of actionable backlink intelligence</strong> — the highest-authority links most likely appear in free tool samples. For sites with fewer than 500 backlinks, free sources capture 50%+ of the meaningful profile.
</div>

<h3>What Changed</h3>
<table>
    <tr><th>Before (v1.7.2)</th><th>After (v1.8.0)</th></tr>
    <tr><td>Required DataForSEO extension (paid)</td><td>Works with zero config — Common Crawl + verification always available</td></tr>
    <tr><td>Single data source</td><td>5 data sources with confidence-weighted merging</td></tr>
    <tr><td>No fallback — just "install extension"</td><td>3-tier cascade: free → free-signup → paid</td></tr>
    <tr><td>No backlink verification</td><td>Built-in crawler verifies if known links still exist</td></tr>
    <tr><td>No data validation</td><td>Automated pre-delivery report validator catches false findings</td></tr>
</table>

<!-- ARCHITECTURE -->
<h2>Architecture</h2>

<h3>3-Tier Cascade</h3>

<div class="tier-box">
    <div class="tier-label">Tier 0 — Always Available <span class="badge badge-pass">ZERO CONFIG</span></div>
    <div class="tier-desc">
        <strong>Common Crawl Web Graph:</strong> Domain-level PageRank, harmonic centrality from the latest quarterly release (134M+ domains). Streams data via incremental decompression — no full download needed.<br>
        <strong>Verification Crawler:</strong> Fetches source pages, parses HTML, confirms if backlinks exist. Detects JS-rendered pages. Polite crawling (1 req/sec per domain).
    </div>
</div>

<div class="tier-box">
    <div class="tier-label">Tier 1–2 — Free Signup <span class="badge badge-new">FREE</span></div>
    <div class="tier-desc">
        <strong>Moz API:</strong> Domain Authority, Page Authority, Spam Score, referring domains, anchor text. 2,500 rows/month, 1 req/10 sec. JSON-RPC 2.0 at api.moz.com.<br>
        <strong>Bing Webmaster Tools:</strong> Inbound links with anchor text + unique competitor comparison feature. Free for verified sites.
    </div>
</div>

<div class="tier-box">
    <div class="tier-label">Tier 3 — Premium <span class="badge badge-info">PAID</span></div>
    <div class="tier-desc">
        <strong>DataForSEO:</strong> 35+ trillion links, real-time updates, toxic scoring, competitor gap analysis. Existing integration completely untouched — all v1.7.2 DataForSEO workflows still work identically.
    </div>
</div>

<h3>Confidence Weighting</h3>
<p>When merging data from multiple sources, each metric is weighted by source reliability:</p>
<table>
    <tr><th>Source</th><th>Confidence</th><th>Coverage vs Commercial</th><th>Update Frequency</th></tr>
    <tr><td>DataForSEO</td><td>1.00</td><td>~90%+</td><td>Real-time</td></tr>
    <tr><td>Verification Crawler</td><td>0.95</td><td>N/A (binary check)</td><td>On-demand</td></tr>
    <tr><td>Moz API</td><td>0.85</td><td>~70% for DA/PA</td><td>~3 days</td></tr>
    <tr><td>Bing Webmaster</td><td>0.70</td><td>~15% (Bing index)</td><td>Near real-time</td></tr>
    <tr><td>Common Crawl</td><td>0.50</td><td>~25–40% domains</td><td>Quarterly</td></tr>
</table>

<div class="callout callout-blue">
<strong>Data sufficiency gate:</strong> If fewer than 4 of 7 scoring factors have data, the system reports "INSUFFICIENT DATA" instead of a misleading numeric score. A score of 25/100 with 1 data source would imply "bad site" when the reality is "not enough data."
</div>

<!-- NEW FILES -->
<h2>New Components</h2>

<h3>Python Scripts (6 new)</h3>
<table>
    <tr><th>Script</th><th>Purpose</th><th>Auth</th></tr>
    <tr><td><code>backlinks_auth.py</code></td><td>Credential management, tier detection, <code>--setup</code> guided wizard</td><td>—</td></tr>
    <tr><td><code>moz_api.py</code></td><td>Moz Link Explorer: DA/PA, spam, domains, anchors, top pages</td><td>API key (free)</td></tr>
    <tr><td><code>bing_webmaster.py</code></td><td>Bing Webmaster: links, counts, competitor comparison</td><td>API key (free)</td></tr>
    <tr><td><code>commoncrawl_graph.py</code></td><td>CC Web Graph: PageRank, harmonic centrality, crawl detection</td><td>None</td></tr>
    <tr><td><code>verify_backlinks.py</code></td><td>Link verification: existence, anchor text, rel attributes, JS detection</td><td>None</td></tr>
    <tr><td><code>validate_backlink_report.py</code></td><td>Pre-delivery validator: catches false findings automatically</td><td>—</td></tr>
</table>

<h3>Skill, Agent & Reference</h3>
<table>
    <tr><th>File</th><th>Purpose</th></tr>
    <tr><td><code>skills/seo-backlinks/SKILL.md</code></td><td>Rewritten with multi-source analysis, 7 sections, fallback cascade, 11-item pre-delivery checklist</td></tr>
    <tr><td><code>agents/seo-backlinks.md</code></td><td>New agent — tier-based workflow, confidence scoring, automated + manual review steps</td></tr>
    <tr><td><code>references/free-backlink-sources.md</code></td><td>Source comparison, confidence methodology, setup guides, data quality reality check</td></tr>
</table>

<!-- COMMANDS -->
<h2>Commands</h2>

<table>
    <tr><th>Command</th><th>What It Does</th></tr>
    <tr><td><code>/seo backlinks &lt;url&gt;</code></td><td>Full backlink profile analysis using all available sources</td></tr>
    <tr><td><code>/seo backlinks gap &lt;url1&gt; &lt;url2&gt;</code></td><td>Competitor backlink gap analysis (Bing unique feature)</td></tr>
    <tr><td><code>/seo backlinks toxic &lt;url&gt;</code></td><td>Toxic link detection (Moz spam score + verification)</td></tr>
    <tr><td><code>/seo backlinks verify &lt;url&gt;</code></td><td>Verify known backlinks still exist</td></tr>
    <tr><td><code>/seo backlinks setup</code></td><td>Guided setup for free Moz and Bing API keys</td></tr>
</table>

<!-- DATA ACCURACY -->
<h2>Data Accuracy Safeguards</h2>

<p>Three layers of protection ensure reports are accurate before reaching the user:</p>

<h3>Layer 1: Script-Level Detection</h3>
<table>
    <tr><th>Protection</th><th>What It Catches</th></tr>
    <tr><td>JS-rendering detection</td><td>Instagram, Facebook, SPAs reported as <code>unverifiable_js</code> instead of false <code>link_removed</code></td></tr>
    <tr><td>Suspicious H1 flagging</td><td>Counter/stat numbers (e.g., "67") flagged in <code>h1_suspicious</code>, not reported as headings</td></tr>
    <tr><td><code>@graph</code> schema flattening</td><td>Valid JSON-LD using <code>@graph</code> wrapper correctly parsed as individual <code>@type</code> entries</td></tr>
    <tr><td>CC <code>in_crawl</code> vs <code>in_rankings</code></td><td>Distinguishes "not crawled" from "crawled but below ranking threshold"</td></tr>
    <tr><td>Subdomain matching</td><td><code>shop.example.com</code> correctly matches target <code>example.com</code></td></tr>
</table>

<h3>Layer 2: Automated Validator</h3>
<p><code>validate_backlink_report.py</code> runs 6 programmatic checks on collected data:</p>
<table>
    <tr><th>Check</th><th>Catches</th></tr>
    <tr><td>Schema claims</td><td>Unflattened <code>@graph</code>, missing <code>@type</code>, deprecated types</td></tr>
    <tr><td>Verification results</td><td>Social media pages falsely marked <code>link_removed</code>, summary/detail mismatches</td></tr>
    <tr><td>H1 claims</td><td>All H1s suspicious (no real heading)</td></tr>
    <tr><td>CC interpretation</td><td>"Not crawled" misinterpreted as "low authority"</td></tr>
    <tr><td>Reciprocal links</td><td>Bidirectional link patterns (A→B and B→A)</td></tr>
    <tr><td>Health score</td><td>Numeric score with insufficient data (&lt;4/7 factors)</td></tr>
</table>

<h3>Layer 3: Agent Instruction Checklist</h3>
<p>The skill and agent include a mandatory pre-delivery review with 11 checks covering source labels, inference vs fact, platform detection, and cross-check consistency.</p>

<!-- SECURITY -->
<h2>Security</h2>

<table>
    <tr><th>Protection</th><th>Implementation</th></tr>
    <tr><td>SSRF protection</td><td>All user-supplied URLs validated via <code>validate_url()</code> — blocks private IPs, loopback, metadata endpoints</td></tr>
    <tr><td>Credential isolation</td><td>Config at <code>~/.config/claude-seo/backlinks-api.json</code> (outside repo, never committed)</td></tr>
    <tr><td>Rate limiting</td><td>Moz: 10s delay persisted via lockfile. Bing: 1s polite delay. Verify: 1s per domain.</td></tr>
    <tr><td>Memory safety</td><td>CC downloads capped at 500 MiB, incremental decompression, explicit buffer cleanup</td></tr>
    <tr><td>No hardcoded paths</td><td>All scripts use <code>os.path.dirname(os.path.abspath(__file__))</code></td></tr>
</table>

<!-- TESTING -->
<h2>Testing Results</h2>

<h3>Real-World Domain Tests</h3>
<table>
    <tr><th>Domain</th><th>CC Result</th><th>Verification</th></tr>
    <tr><td>google.com</td><td>PageRank #1, HC #3, 41,269 hosts</td><td>—</td></tr>
    <tr><td>github.com</td><td>PageRank #24, HC #32, 6,038 hosts</td><td>—</td></tr>
    <tr><td>21collagen.com</td><td>in_crawl: true, in_rankings: false</td><td>3 verified, 2 unverifiable_js</td></tr>
    <tr><td>collagenwise.ro</td><td>in_crawl: false (not yet crawled)</td><td>3 verified, 1 lost (LinkedIn 404), 1 unverifiable_js</td></tr>
</table>

<h3>Validator Test</h3>
<p>Simulated a report with all known bug classes — validator caught all 5 issues:</p>
<table>
    <tr><th>Issue</th><th>Severity</th><th>Detected?</th></tr>
    <tr><td>Unflattened @graph schema</td><td><span class="badge badge-fail">ERROR</span></td><td>Yes</td></tr>
    <tr><td>Instagram falsely marked link_removed</td><td><span class="badge badge-fail">ERROR</span></td><td>Yes</td></tr>
    <tr><td>Numeric score with 1/7 factors</td><td><span class="badge badge-fail">ERROR</span></td><td>Yes</td></tr>
    <tr><td>Reciprocal link not flagged</td><td><span class="badge badge-warn">WARNING</span></td><td>Yes</td></tr>
    <tr><td>CC absence misinterpreted</td><td><span class="badge badge-info">INFO</span></td><td>Yes</td></tr>
</table>

<!-- GETTING STARTED -->
<h2>Getting Started</h2>

<h3>Zero-Config (Immediate)</h3>
<pre>/seo backlinks https://your-domain.com</pre>
<p>Works immediately with Common Crawl + verification crawler. No API keys needed.</p>

<h3>Add Free APIs (5 minutes)</h3>
<pre>
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
