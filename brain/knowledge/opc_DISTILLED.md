---
id: opc
type: knowledge
owner: OA_Triage
---
# opc
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# OPC Skills

<p align="center">
  <img src="website/opc-banner.png" alt="OPC Skills - AI Agent Skills for Solopreneurs" width="100%">
</p>

<p align="center">
  <a href="https://opc.dev"><img src="https://img.shields.io/badge/Website-opc.dev-black?style=flat-square" alt="Website"></a>
  <a href="https://skills.sh/ReScienceLab/opc-skills"><img src="https://img.shields.io/badge/Browse-skills.sh-blue?style=flat-square" alt="Browse on skills.sh"></a>
  <a href="https://deepwiki.com/ReScienceLab/opc-skills"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
  <a href="https://code.claude.com/docs/en/plugin-marketplaces"><img src="https://img.shields.io/badge/Claude_Code-Marketplace-orange?style=flat-square&logo=anthropic" alt="Claude Code Marketplace"></a>
  <a href="https://github.com/ReScienceLab/opc-skills/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="https://github.com/ReScienceLab/opc-skills/stargazers"><img src="https://img.shields.io/github/stars/ReScienceLab/opc-skills?style=flat-square" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="https://github.com/ReScienceLab/opc-skills/issues"><img src="https://img.shields.io/github/issues/ReScienceLab/opc-skills?style=flat-square" alt="GitHub issues"></a>
  <a href="https://github.com/ReScienceLab/opc-skills/pulls"><img src="https://img.shields.io/github/issues-pr/ReScienceLab/opc-skills?style=flat-square" alt="GitHub pull requests"></a>
  <img src="https://img.shields.io/github/last-commit/ReScienceLab/opc-skills?style=flat-square" alt="Last commit">
  <a href="https://github.com/ReScienceLab/opc-skills/graphs/contributors"><img src="https://img.shields.io/github/contributors/ReScienceLab/opc-skills?style=flat-square" alt="Contributors"></a>
  <a href="https://x.com/Yilin0x"><img src="https://img.shields.io/badge/Twitter-@Yilin0x-black?style=flat-square&logo=x" alt="Twitter"></a>
  <a href="https://discord.gg/Y2yBpRXvVa"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <strong>AI Agent Skills for Solopreneurs, Indie Hackers, and One-Person Companies</strong>
</p>

<p align="center">
  Extend Claude Code, Cursor, Codex, and more with automation skills.<br>
  <a href="https://opc.dev">Browse Skills</a> · <a href="#quick-install">Quick Install</a> · <a href="#included-skills">View All Skills</a>
</p>

---

## What are Skills?

Skills are folders of instructions, scripts, and resources that AI agents load dynamically to improve performance on specialized tasks. Each skill is self-contained with a `SKILL.md` file containing instructions and metadata.

For more information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).

## Included Skills

| | Skill | Description |
|:---:|-------|-------------|
| <img src="./skill-logos/seo-geo.svg" width="24"> | [seo-geo](./skills/seo-geo) | SEO & GEO optimization for AI search engines (ChatGPT, Perplexity, Google) |
| <img src="./skill-logos/requesthunt.svg" width="24"> | [requesthunt](./skills/requesthunt) | Research user demand from Reddit, X, and GitHub |
| <img src="./skill-logos/domain-hunter.svg" width="24"> | [domain-hunter](./skills/domain-hunter) | Find domains, compare registrar prices, and discover promo codes |
| <img src="./skill-logos/logo-creator.svg" width="24"> | [logo-creator](./skills/logo-creator) | Create logos with AI, crop, remove background, export as SVG |
| <img src="./skill-logos/banner-creator.svg" width="24"> | [banner-creator](./skills/banner-creator) | Create banners for GitHub, Twitter, LinkedIn, etc. |
| <img src="./skill-logos/nanobanana.svg" width="24"> | [nanobanana](./skills/nanobanana) | Generate images using Gemini 3 Pro Image (Nano Banana Pro) |
| <img src="./skill-logos/reddit.svg" width="24"> | [reddit](./skills/reddit) | Search and retrieve content from Reddit via the public JSON API |
| <img src="./skill-logos/twitter.svg" width="24"> | [twitter](./skills/twitter) | Search and retrieve content from Twitter/X via twitterapi.io |
| <img src="./skill-logos/producthunt.svg" width="24"> | [producthunt](./skills/producthunt) | Search Product Hunt posts, topics, users, and collections |
| <img src="./skill-logos/archive.svg" width="24"> | [archive](./skills/archive) | Archive session learnings and debugging solutions with indexed markdown |

## Quick Install

### Claude Code Plugin Marketplace

Install directly from Claude Code's plugin marketplace:

```bash
# Add the OPC Skills marketplace
/plugin marketplace add ReScienceLab/opc-skills

# Install specific skills
/plugin install requesthunt@opc-skills
/plugin install domain-hunter@opc-skills
/plugin install seo-geo@opc-skills

# List all available skills
/plugin marketplace list opc-skills
```

### Universal Installation (16+ AI Tools)

Install with one command - works with Claude Code, Cursor, Windsurf, Droid, and 12+ other AI tools:

```bash
# Install all skills
npx skills add ReScienceLab/opc-skills

# Install specific skill
npx skills add ReScienceLab/opc-skills --skill reddit

# Install to specific agent
npx skills add ReScienceLab/opc-skills -a droid
```

Browse and discover skills at **[skills.sh](https://skills.sh/ReScienceLab/opc-skills)** 🎯

### Skills with Dependencies

Some skills require other skills to function properly:

- **domain-hunter** → requires `twitter` and `reddit`
- **logo-creator** → requires `nanobanana`
- **banner-creator** → requires `nanobanana`

Install them together:

```bash
npx skills add ReScienceLab/opc-skills --skill reddit --skill twitter --skill domain-hunter
```

---

## Supported AI Tools

OPC Skills work with 16+ AI coding agents via `npx skills add`:

- **Claude Code** - Desktop app for AI-assisted coding
- **Cursor** - AI-first code editor
- **Factory Droid** - AI software engineering agent
- **Windsurf** - AI-powered IDE
- **OpenCode** - Open-source AI coding assistant
- **Codex** - AI code generation tool
- **GitHub Copilot** - AI pair programmer
- **Gemini CLI** - Command-line AI assistant
- **Goose** - Terminal-based AI agent
- **Kilo Code** - Lightweight AI coding tool
- **Roo Code** - AI code assistant
- **Trae** - AI development companion
- **And more...**

See the [full compatibility list](https://github.com/vercel-labs/add-skill#available-agents) for all supported tools.

---

## Documentation & Resources

Explore OPC Skills through multiple channels:

- **[DeepWiki](https://deepwiki.com/ReScienceLab/opc-skills)** - AI-powered interactive documentation with code exploration and Q&A
- **[Skills Browser](https://skills.sh/ReScienceLab/opc-skills)** - Browse and discover all available skills
- **[Official Website](https://opc.dev)** - Guides, tutorials, and usage examples
- **[Agent Skills Standard](https://agentskills.io/)** - Learn about the skills specification

### Using DeepWiki

DeepWiki provides an AI assistant that can answer questions about the codebase:
- Ask: "How does the domain-hunter skill work?"
- Ask: "Show me the dependencies between skills"
- Ask: "Explain the skill installation process"

The documentation auto-syncs with the repository, so it's always up to date.

---

## Creating New Skills

See the template in `./template/` directory for the basic structure:

1. Create a folder in `skills/` with your skill name
2. Add a `SKILL.md` file with YAML frontmatter
3. (Optional) Add scripts, examples, or other resources

**Required fields in SKILL.md:**
```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
```

For detailed guidance, check out existing skills or visit the [Agent Skills specification](https://agentskills.io/).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ReScienceLab/opc-skills&type=Date)](https://star-history.com/#ReScienceLab/opc-skills&Date)

## Contributing

1. Fork this repository
2. Create a new skill folder in `skills/`
3. Add a `SKILL.md` with proper frontmatter
4. Submit a pull request

## License

Apache 2.0

```

### File: website\package.json
```json
{
  "dependencies": {
    "marked": "^17.0.1"
  }
}

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to OPC Skills are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Skill Compatibility & Dependency Matrix

Each skill maintains its own independent version. Use this matrix to understand dependencies and compatibility.

| Skill | Current Version | Requires | Min Versions |
|-------|-----------------|----------|--------------|
| **requesthunt** | 2.0.0 | - | - |
| **domain-hunter** | 1.0.0 | twitter, reddit | twitter ≥1.0.0, reddit ≥1.0.0 |
| **logo-creator** | 1.0.0 | nanobanana | nanobanana ≥1.0.0 |
| **banner-creator** | 1.0.0 | nanobanana | nanobanana ≥1.0.0 |
| **nanobanana** | 1.0.0 | - | - |
| **reddit** | 1.0.0 | - | - |
| **twitter** | 1.0.0 | - | - |
| **producthunt** | 1.0.0 | - | - |
| **seo-geo** | 1.0.0 | twitter, reddit | twitter ≥1.0.0, reddit ≥1.0.0 |
| **archive** | 1.1.0 | - | - |

**Key Points:**
- Each skill has an independent version number (MAJOR.MINOR.PATCH)
- Skills can be released independently without coordinating with others
- Use this matrix to identify dependencies before updating a skill
- When a dependency skill updates with breaking changes, dependent skills need to be tested

---

## [Unreleased]

## Released Versions

## [1.1.1] - 2026-03-31

### requesthunt

#### [2.0.1] - 2026-03-31
- **Changed**: Updated auth documentation to describe device code flow (visit URL + enter code) instead of generic browser approval

## [1.1.0] - 2026-03-31

### requesthunt

#### [2.0.0] - 2026-03-31
- **Changed**: Switched from Python scripts to `requesthunt` Rust CLI as the sole interface
- **Added**: Browser authentication via `requesthunt auth login` (with `config set-key` fallback for headless/CI)
- **Added**: CLI commands in skills.json registry (search, list, scrape start/status, topics, usage)
- **Added**: Link to agent setup guide (`https://requesthunt.com/setup.md`)
- **Added**: TOON output mode documentation (Token-Oriented Object Notation)
- **Changed**: Switched usage and pricing documentation from cached/realtime quotas to the unified credits model
- **Removed**: Python scripts (`scripts/`) — replaced entirely by CLI commands
- **Fixed**: Updated RequestHunt settings links to use `/dashboard`

## [1.0.11] - 2026-03-13

### archive
#### [1.1.0] - 2026-03-13
- **Added**: Claude Code / Droid plugin support (`.factory-plugin/plugin.json`)
- **Added**: `hooks/hooks.json` — `SessionStart` hook auto-loads `.archive/MEMORY.md` into session context when plugin is installed, enabling cross-session knowledge reuse without manual configuration
- **Added**: `hooks/load-memory.py` — supports `FACTORY_PROJECT_DIR`, `CLAUDE_PROJECT_DIR`, and `cwd()` fallback for cross-platform compatibility

## [1.0.10] - 2026-02-23

### archive
#### [1.0.1] - 2026-02-23
- **Fixed**: Description YAML block scalar (`>-`) replaced with single-line string to fix broken description display on skills.sh and other parsers

## [1.0.9] - 2026-02-23

### Blog
- **Added**: Archive skill announcement blog post (#62)
  - "Stop Losing Context Between AI Sessions: Introducing the Archive Skill"
  - Includes OG banner image

## [1.0.8] - 2026-02-23

### Skills
- **Added**: Archive skill for indexed session knowledge (#57, #59)
  - Archive session learnings, debugging solutions, and deployment logs
  - Maintains `.archive/MEMORY.md` index for cross-session knowledge reuse
  - Includes logo, install commands, README listing, and website integration
- **Added**: `add-new-opc-skill` checklist skill under `.factory/skills/` (#60)
  - Comprehensive guide for adding new skills to the project

### Infrastructure
- **Fixed**: Replace broken `curl -fsSL opc.dev/install.sh` with `npx skills add` (#55, #58)
  - install.sh endpoint was returning 404
  - Updated all install commands in skills.json and website/worker.js
  - Redirect `/install.sh` to GitHub README installation section
## [1.0.7] - 2026-02-15

### Infrastructure
- **Added**: Twitter ([@Yilin0x](https://x.com/Yilin0x)) and Discord badges to README (#52)
- **Changed**: Ranked seo-geo skill at the top of skills list in skills.json and README (#53)

## [1.0.6] - 2026-02-15

### Infrastructure
- **Fixed**: Install stats scraper now handles abbreviated count formats (e.g. "2.8K") from skills.sh (#50)
  - Added `_parse_count()` helper for K-suffix abbreviations
  - Previously caused seo-geo to steal logo-creator's count and logo-creator to be dropped entirely

### Skills
- **Refactored**: Aligned all SKILL.md frontmatter with Anthropic skill standard (#51)
  - Removed `triggers` field from all 9 skills and the template
  - Merged trigger keywords into `description` field as "Use when..." clauses
  - Frontmatter now only uses `name` and `description` fields
  - Fixes seo-geo broken description display on skills.sh (YAML `|` block rendered as literal `|`)

## [1.0.5] - 2026-01-29

### Infrastructure
- **Fixed**: Removed `pluginRoot` and updated all source paths to work around Claude Code bug
  - Removed `pluginRoot: "./skills"` from marketplace metadata (Claude Code doesn't respect this field)
  - Updated all plugin source paths from `"./domain-hunter"` to `"./skills/domain-hunter"`
  - Fixes "Source path does not exist" error when installing plugins
  - Workaround for known Claude Code issues #11243 and #11278

### Skills
- (no skill version changes in this release)

## [1.0.4] - 2026-01-29

### Infrastructure
- **Fixed**: Updated marketplace metadata version to trigger cache refresh
  - Changed marketplace metadata version from 1.0.0 to 1.0.3
  - Fixes "Source path does not exist" error when installing plugins in Claude Code
  - Ensures Claude Code refreshes marketplace cache with correct plugin paths

### Skills
- (no skill version changes in this release)

## [1.0.3] - 2026-01-29

### Website
- **Fixed**: Blog OG image path for installation tutorial post
  - Corrected image path from `2026-01-28-install-tutorial-og.png` to `2026-01-28-install-opc-skills-claude-code-og.png`
  - Fixes broken Open Graph preview on social media shares

### Skills
- (no skill version changes in this release)

## [1.0.2] - 2026-01-29

### Infrastructure
- **Fixed**: Claude Code Plugin Marketplace schema validation errors
  - Updated all plugin source paths from bare names to relative paths (e.g., `"requesthunt"` → `"./requesthunt"`)
  - Ensures compatibility with Claude Code's `/plugin marketplace add` command
  - Resolves "Invalid input" errors when adding marketplace

### Skills
- (no skill version changes in this release)

## [1.0.1] - 2026-01-29

### Website
- **Added**: New blog post "Why Skills Beat Docs: The Rise of Agent-Native Documentation"
  - Analysis of 100x engagement gap between docs and skills
  - Comprehensive ecosystem overview (Skills.sh, Mintlify, awesome-claude-code)
  - Step-by-step guide for converting docs to skills

### Skills
- (no skill version changes in this release)

### requesthunt

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Generate user demand research reports from Reddit, X, and GitHub
- Collect real user feedback across multiple platforms
- Filter and search by topic, platform, and timeframe
- Generate structured demand research reports

### domain-hunter

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Search domains, compare registrar prices, and find promo codes
- Query domain availability and pricing
- Compare prices across registrars
- Find current promo codes from Twitter and Reddit
- **Dependencies**: twitter ≥1.0.0, reddit ≥1.0.0

### logo-creator

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Create logos using AI image generation
- Generate logo variations with Gemini
- Remove background from images
- Crop logos to desired aspect ratios
- Export as SVG vector format
- **Dependencies**: nanobanana ≥1.0.0

### banner-creator

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Create banners for GitHub, Twitter, LinkedIn, and other platforms
- Generate banner variations with Gemini
- Crop to platform-specific ratios (16:9, 21:9, 2:1, etc.)
- Support for different banner formats and styles
- **Dependencies**: nanobanana ≥1.0.0

### nanobanana

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Generate and edit images using Google Gemini 3 Pro Image (Nano Banana Pro)
- Text-to-image generation
- Image-to-image editing and variations
- Support for multiple aspect ratios (1:1, 2:3, 3:2, 16:9, 21:9, etc.)
- 2K and 4K high-resolution output options
- Batch image generation

### reddit

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Search and retrieve content from Reddit
- Access public JSON API without authentication
- Search posts and subreddits
- Get user profiles and comment threads
- No API key required

### twitter

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Search and retrieve content from Twitter/X
- User information and tweet retrieval
- Search tweets by keyword
- Get follower information and trends
- Via twitterapi.io API service

### producthunt

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- Search and retrieve content from Product Hunt
- Query posts, topics, and collections
- Get user and product information
- Access GraphQL API for detailed data
- Requires Product Hunt API access token

### seo-geo

#### [1.0.0] - 2025-01-21
- **Added**: Initial release
- SEO & GEO (Generative Engine Optimization) for websites
- Optimize for traditional search engines (Google, Bing)
- Optimize for AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude)
- Generate schema markup and JSON-LD
- Keyword research and SERP analysis
- Princeton GEO research methods for +40% AI visibility
- Optional DataForSEO API integration for advanced features
- **Dependencies**: twitter ≥1.0.0, reddit ≥1.0.0

---

## Initial Release Features

### Unified Installation & Support
- Unified installation system via `npx skills add`
- Support for 16+ AI agent tools (Claude Code, Cursor, Droid, Windsurf, etc.)
- Composable skills with dependency management
- Comprehensive documentation website (opc.dev)
- SKILL.md standard with YAML frontmatter for all skills

### Documentation & Resources
- Official website: https://opc.dev
- Skill browser: https://skills.sh/ReScienceLab/opc-skills
- Individual skill repositories on GitHub
- Example workflows in each skill directory
- API documentation and rate limit information

### Infrastructure
- GitHub repository: https://github.com/ReScienceLab/opc-skills
- MIT License
- Automated skill installation scripts
- Website deployment pipeline

## Version Compatibility

| Version | Status | Release Date | Notable Changes |
|---------|--------|--------------|-----------------|
| 1.1.0 | Stable | 2026-03-31 | requesthunt v2.0.0 — CLI-first, Python scripts removed |
| 1.0.0 | Stable | 2025-01-21 | Initial release with 9 core skills |

## Migration Guides

### Coming Soon
Migration guides for major version upgrades will be documented here.

## Notes

### API Keys Required
- **requesthunt**: CLI device code auth (`requesthunt auth login`) or REQUESTHUNT_API_KEY (requesthunt.com/dashboard)
- **twitter**: TWITTERAPI_API_KEY (twitterapi.io, ~$0.15-0.18/1k requests)
- **logo-creator**: GEMINI_API_KEY, REMOVE_BG_API_KEY, RECRAFT_API_KEY
- **banner-creator**: GEMINI_API_KEY (Google AI Studio)
- **nanobanana**: GEMINI_API_KEY
- **producthunt**: PRODUCTHUNT_ACCESS_TOKEN
- **seo-geo**: DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD (optional)

### Rate Limits
- **requesthunt**: Free tier 100 credits/month at 10 req/min, Pro tier 2,000 credits/month at 60 req/min, 1 credit per API call, scrapes cost depth x platforms
- **twitter**: Depends on twitterapi.io plan
- **nanobanana**: Google Gemini API limits apply
- **seo-geo**: DataForSEO API limits apply

### Supported Platforms
- Claude Code (Desktop)
- Cursor
- Factory Droid
- Windsurf
- OpenCode
- Codex
- GitHub Copilot
- Gemini CLI
- Goose
- Kilo Code
- Roo Code
- Trae
- And more via `npx skills add`

## Contributing

Interested in contributing? Please see:
- Contributing Guidelines: https://github.com/ReScienceLab/opc-skills/blob/main/CONTRIBUTING.md (coming soon)
- Issue Tracker: https://github.com/ReScienceLab/opc-skills/issues
- Skill Template: https://github.com/ReScienceLab/opc-skills/tree/main/template

## Support

For issues and questions:
- GitHub Issues: https://github.com/ReScienceLab/opc-skills/issues
- Website: https://opc.dev
- Documentation: https://skills.sh/ReScienceLab/opc-skills

## License

All OPC Skills are released under the [MIT License](https://github.com/ReScienceLab/opc-skills/blob/main/LICENSE).

---

Generated: 2025-01-21
Project: OPC Skills - AI Agent Skills for Solopreneurs

```

### File: skills.json
```json
{
  "version": "1.1.1",
  "name": "OPC Skills",
  "description": "Agent Skills for One Person Companies",
  "repository": "https://github.com/ReScienceLab/opc-skills",
  "website": "https://opc.dev",
  "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/website/opc-logo.svg",
  "skills": [
    {
      "name": "seo-geo",
      "version": "1.0.0",
      "description": "SEO & GEO (Generative Engine Optimization) for websites. Optimize for AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude) and traditional search (Google, Bing). Includes Princeton GEO research methods for +40% AI visibility.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/seo-geo.svg",
      "icon": "search",
      "color": "10B981",
      "triggers": [
        "SEO",
        "GEO",
        "search optimization",
        "schema markup",
        "JSON-LD",
        "meta tags",
        "keyword research",
        "AI visibility",
        "ChatGPT ranking",
        "Perplexity"
      ],
      "dependencies": {
        "twitter": ">=1.0.0",
        "reddit": ">=1.0.0"
      },
      "auth": {
        "required": false,
        "type": "api_key",
        "keys": [
          {
            "env": "DATAFORSEO_LOGIN",
            "url": "https://dataforseo.com",
            "optional": true
          },
          {
            "env": "DATAFORSEO_PASSWORD",
            "url": "https://dataforseo.com",
            "optional": true
          }
        ]
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill seo-geo -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill seo-geo -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill seo-geo -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill seo-geo -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill seo-geo",
          "droid": "npx skills add ReScienceLab/opc-skills --skill seo-geo",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill seo-geo",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill seo-geo",
          "codex": "npx skills add ReScienceLab/opc-skills --skill seo-geo"
        }
      },
      "commands": [
        "python3 scripts/seo_audit.py \"{url}\"",
        "python3 scripts/keyword_research.py \"{keyword}\" --limit 20",
        "python3 scripts/serp_analysis.py \"{keyword}\" --depth 20",
        "python3 scripts/backlinks.py \"{domain}\" --limit 20",
        "python3 scripts/domain_overview.py \"{domain}\""
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/seo-geo",
        "example": "https://github.com/ReScienceLab/opc-skills/blob/main/skills/seo-geo/examples/opc-skills-case-study.md"
      }
    },
    {
      "name": "requesthunt",
      "version": "2.0.0",
      "description": "Generate user demand research reports from real user feedback. Scrape and analyze feature requests, complaints, and questions from Reddit, X, and GitHub.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/requesthunt.svg",
      "icon": "globe",
      "color": "6366F1",
      "triggers": [
        "requesthunt",
        "request hunt",
        "feature request",
        "user demand",
        "demand research"
      ],
      "dependencies": {},
      "auth": {
        "required": true,
        "type": "cli",
        "setup": "curl -fsSL https://requesthunt.com/cli | sh && requesthunt auth login",
        "keys": [
          {
            "env": "REQUESTHUNT_API_KEY",
            "url": "https://requesthunt.com/dashboard",
            "optional": true,
            "note": "Only needed if browser auth is not available"
          }
        ]
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill requesthunt -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill requesthunt -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill requesthunt -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill requesthunt -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill requesthunt",
          "droid": "npx skills add ReScienceLab/opc-skills --skill requesthunt",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill requesthunt",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill requesthunt",
          "codex": "npx skills add ReScienceLab/opc-skills --skill requesthunt"
        }
      },
      "commands": [
        "requesthunt search \"{query}\" --expand --limit 20",
        "requesthunt list --topic \"{topic}\" --limit 20",
        "requesthunt scrape start \"{topic}\" --platforms reddit,x,github --depth 2",
        "requesthunt scrape status \"{job_id}\"",
        "requesthunt topics",
        "requesthunt usage"
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/requesthunt",
        "docs": "https://requesthunt.com/docs",
        "setup": "https://requesthunt.com/setup.md",
        "example": "https://github.com/ReScienceLab/opc-skills/blob/main/skills/requesthunt/examples/calendar-app-research.md"
      }
    },
    {
      "name": "domain-hunter",
      "version": "1.0.0",
      "description": "Search domains, compare registrar prices, and find promo codes. Help users find and purchase domain names at the best price.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/domain-hunter.svg",
      "icon": "globe",
      "color": "4A90D9",
      "triggers": [
        "domain",
        "registrar",
        "buy domain",
        "domain price",
        ".ai domain",
        ".com domain"
      ],
      "dependencies": {
        "twitter": ">=1.0.0",
        "reddit": ">=1.0.0"
      },
      "auth": {
        "required": false,
        "type": null,
        "keys": []
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill domain-hunter -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill domain-hunter -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill domain-hunter -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill domain-hunter -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill domain-hunter",
          "droid": "npx skills add ReScienceLab/opc-skills --skill domain-hunter",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill domain-hunter",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill domain-hunter",
          "codex": "npx skills add ReScienceLab/opc-skills --skill domain-hunter"
        }
      },
      "commands": [
        "whois {domain}.{tld}",
        "WebSearch: cheapest .{tld} domain registrar"
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/domain-hunter",
        "example": "https://github.com/ReScienceLab/opc-skills/blob/main/skills/domain-hunter/examples/auto-video-editing-domain.md"
      }
    },
    {
      "name": "logo-creator",
      "version": "1.0.0",
      "description": "Create logos using AI image generation. Discuss style/ratio, generate variations, iterate with user feedback, crop, remove background, and export as SVG.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/logo-creator.svg",
      "icon": "image",
      "color": "8B5CF6",
      "triggers": [
        "logo",
        "brand",
        "icon",
        "favicon",
        "mascot",
        "emblem",
        "create logo",
        "design logo"
      ],
      "dependencies": {
        "nanobanana": ">=1.0.0"
      },
      "auth": {
        "required": true,
        "type": "api_key",
        "keys": [
          {
            "env": "GEMINI_API_KEY",
            "url": "https://aistudio.google.com/apikey"
          },
          {
            "env": "REMOVE_BG_API_KEY",
            "url": "https://www.remove.bg/api",
            "optional": true
          },
          {
            "env": "RECRAFT_API_KEY",
            "url": "https://www.recraft.ai/api",
            "optional": true
          }
        ]
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill logo-creator -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill logo-creator -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill logo-creator -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill logo-creator -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill logo-creator",
          "droid": "npx skills add ReScienceLab/opc-skills --skill logo-creator",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill logo-creator",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill logo-creator",
          "codex": "npx skills add ReScienceLab/opc-skills --skill logo-creator"
        }
      },
      "commands": [
        "python3 <nanobanana>/scripts/batch_generate.py \"{prompt}\" -n 20 --ratio 1:1 -d ./logos -p logo",
        "python3 scripts/crop_logo.py {input.png} {output.png}",
        "python3 scripts/remove_bg.py {input.png} {output.png}",
        "python3 scripts/vectorize.py {input.png} {output.svg}"
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/logo-creator",
        "example": "https://github.com/ReScienceLab/opc-skills/blob/main/skills/logo-creator/examples/opc-logo-creation.md"
      }
    },
    {
      "name": "banner-creator",
      "version": "1.0.0",
      "description": "Create banners using AI image generation. Discuss format/style, generate variations, iterate with user feedback, crop to target ratio for GitHub, Twitter, LinkedIn, etc.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/banner-creator.svg",
      "icon": "image",
      "color": "F59E0B",
      "triggers": [
        "banner",
        "header",
        "hero image",
        "cover image",
        "create banner",
        "github banner",
        "twitter header",
        "readme banner"
      ],
      "dependencies": {
        "nanobanana": ">=1.0.0"
      },
      "auth": {
        "required": true,
        "type": "api_key",
        "keys": [
          {
            "env": "GEMINI_API_KEY",
            "url": "https://aistudio.google.com/apikey"
          }
        ]
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill banner-creator -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill banner-creator -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill banner-creator -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill banner-creator -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill banner-creator",
          "droid": "npx skills add ReScienceLab/opc-skills --skill banner-creator",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill banner-creator",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill banner-creator",
          "codex": "npx skills add ReScienceLab/opc-skills --skill banner-creator"
        }
      },
      "commands": [
        "python3 <nanobanana>/scripts/batch_generate.py \"{prompt}\" -n 20 --ratio 21:9 -d ./banners -p banner",
        "python3 scripts/crop_banner.py {input.png} {output.png} --ratio 2:1 --width 1280"
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/banner-creator",
        "example": "https://github.com/ReScienceLab/opc-skills/blob/main/skills/banner-creator/examples/opc-banner-creation.md"
      }
    },
    {
      "name": "nanobanana",
      "version": "1.0.0",
      "description": "Generate and edit images using Google Gemini 3 Pro Image (Nano Banana Pro). Supports text-to-image, image editing, aspect ratios, and 2K/4K output.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/nanobanana.svg",
      "icon": "googlegemini",
      "color": "8E75B2",
      "triggers": [
        "generate image",
        "create image",
        "nano banana",
        "nanobanana",
        "gemini image",
        "AI image"
      ],
      "dependencies": {},
      "auth": {
        "required": true,
        "type": "api_key",
        "keys": [
          {
            "env": "GEMINI_API_KEY",
            "url": "https://aistudio.google.com/apikey"
          }
        ]
      },
      "install": {
        "user": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill nanobanana -a claude",
          "droid": "npx skills add ReScienceLab/opc-skills --skill nanobanana -a droid",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill nanobanana -a opencode",
          "codex": "npx skills add ReScienceLab/opc-skills --skill nanobanana -a codex"
        },
        "project": {
          "claude": "npx skills add ReScienceLab/opc-skills --skill nanobanana",
          "droid": "npx skills add ReScienceLab/opc-skills --skill nanobanana",
          "cursor": "npx skills add ReScienceLab/opc-skills --skill nanobanana",
          "opencode": "npx skills add ReScienceLab/opc-skills --skill nanobanana",
          "codex": "npx skills add ReScienceLab/opc-skills --skill nanobanana"
        }
      },
      "commands": [
        "python3 scripts/generate.py \"{prompt}\" -o {output.png}",
        "python3 scripts/generate.py \"{prompt}\" -i {input.jpg} -o {output.png}",
        "python3 scripts/batch_generate.py \"{prompt}\" -n 20 -d ./images -p image"
      ],
      "links": {
        "github": "https://github.com/ReScienceLab/opc-skills/tree/main/skills/nanobanana",
        "docs": "https://ai.google.dev/gemini-api/docs/image-generation"
      }
    },
    {
      "name": "reddit",
      "version": "1.0.0",
      "description": "Search and retrieve content from Reddit. Get posts, comments, subreddit info, and user profiles via the public JSON API.",
      "logo": "https://raw.githubusercontent.com/ReScienceLab/opc-skills/main/skill-logos/reddit.svg",
      "icon": "reddit",
      "color": "FF4500",
      "triggers": [
        "reddit",
        "subreddit",
        "r/"
      ],
      "dependencies": {},
      "auth": {
        "required": false,
        "type": null,
        "ke
... [TRUNCATED]
```

### File: .claude-plugin\marketplace.json
```json
{
  "name": "opc-skills",
  "owner": {
    "name": "ReScienceLab",
    "email": "yilin.jing@rescience.com"
  },
  "metadata": {
    "description": "Agent Skills for One Person Companies - Boost your AI agent with specialized skills for solopreneurs and indie hackers",
    "version": "1.0.4"
  },
  "keywords": [
    "skills",
    "agents",
    "automation",
    "solopreneur",
    "indie-hacker",
    "one-person-company",
    "productivity",
    "seo",
    "social-media",
    "design",
    "market-research"
  ],
  "plugins": [
    {
      "name": "requesthunt",
      "source": "./skills/requesthunt",
      "description": "Generate user demand research reports from real user feedback. Scrape and analyze feature requests, complaints, and questions from Reddit, X, and GitHub.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/requesthunt",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "market-research",
      "keywords": [
        "market-research",
        "user-feedback",
        "reddit",
        "twitter",
        "github",
        "demand-analysis"
      ],
      "strict": true
    },
    {
      "name": "domain-hunter",
      "source": "./skills/domain-hunter",
      "description": "Search domains, compare registrar prices, and find promo codes. Help users find and purchase domain names at the best price.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/domain-hunter",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "business",
      "keywords": [
        "domain",
        "registrar",
        "pricing",
        "whois"
      ],
      "strict": true
    },
    {
      "name": "logo-creator",
      "source": "./skills/logo-creator",
      "description": "Create logos using AI image generation. Discuss style/ratio, generate variations, iterate with user feedback, crop, remove background, and export as SVG.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/logo-creator",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "design",
      "keywords": [
        "logo",
        "design",
        "branding",
        "ai-image-generation",
        "svg"
      ],
      "strict": true
    },
    {
      "name": "banner-creator",
      "source": "./skills/banner-creator",
      "description": "Create banners using AI image generation. Discuss format/style, generate variations, iterate with user feedback, crop to target ratio for GitHub, Twitter, LinkedIn, etc.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/banner-creator",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "design",
      "keywords": [
        "banner",
        "header",
        "social-media",
        "ai-image-generation"
      ],
      "strict": true
    },
    {
      "name": "nanobanana",
      "source": "./skills/nanobanana",
      "description": "Generate and edit images using Google Gemini 3 Pro Image (Nano Banana Pro). Supports text-to-image, image editing, aspect ratios, and 2K/4K output.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/nanobanana",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "ai-tools",
      "keywords": [
        "gemini",
        "image-generation",
        "ai",
        "batch-processing"
      ],
      "strict": true
    },
    {
      "name": "reddit",
      "source": "./skills/reddit",
      "description": "Search and retrieve content from Reddit. Get posts, comments, subreddit info, and user profiles via the public JSON API.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/reddit",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "social-media",
      "keywords": [
        "reddit",
        "social-media",
        "api",
        "content-scraping"
      ],
      "strict": true
    },
    {
      "name": "twitter",
      "source": "./skills/twitter",
      "description": "Search and retrieve content from Twitter/X. Get user info, tweets, replies, followers, communities, spaces, and trends via twitterapi.io.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/twitter",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "social-media",
      "keywords": [
        "twitter",
        "x",
        "social-media",
        "api"
      ],
      "strict": true
    },
    {
      "name": "producthunt",
      "source": "./skills/producthunt",
      "description": "Search and retrieve content from Product Hunt. Get posts, topics, users, and collections via the GraphQL API.",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/producthunt",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "product-discovery",
      "keywords": [
        "producthunt",
        "product-launch",
        "api"
      ],
      "strict": true
    },
    {
      "name": "seo-geo",
      "source": "./skills/seo-geo",
      "description": "SEO & GEO (Generative Engine Optimization) for websites. Optimize for AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude) and traditional search (Google, Bing).",
      "version": "1.0.0",
      "homepage": "https://opc.dev/skills/seo-geo",
      "repository": "https://github.com/ReScienceLab/opc-skills",
      "license": "MIT",
      "category": "seo",
      "keywords": [
        "seo",
        "geo",
        "optimization",
        "schema-markup",
        "ai-visibility"
      ],
      "strict": true
    }
  ]
}
```

### File: .factory\AGENTS.md
```md
# OPC Skills

OPC Skills is a library of reusable AI agent skills for solopreneurs, indie hackers, and one-person companies. Each skill extends AI agents with specialized capabilities through structured instructions and automation scripts.

## Core Commands

- **Lint**: `npm run lint` (website) / `python3 -m pylint skills/*/scripts/*.py` (skills)
- **Type-check**: `npm run typecheck` (website)
- **Test**: `npm run test` (website)
- **Dev**: `npm run dev` (website)
- **Build**: `npm run build` (website)
- **Publish**: See [Release Process](#release-process)

## Project Layout

```
├── skills/                    → Source skill implementations
│   ├── requesthunt/           → RequestHunt skill
│   ├── domain-hunter/         → Domain search & pricing
│   ├── logo-creator/          → Logo generation
│   ├── banner-creator/        → Banner creation
│   ├── nanobanana/            → Gemini image generation
│   ├── reddit/                → Reddit integration
│   ├── twitter/               → Twitter/X integration
│   ├── producthunt/           → Product Hunt integration
│   └── seo-geo/               → SEO & GEO optimization
├── .factory/skills/           → Installed skill versions
├── skills.json                → Global metadata and version registry
├── website/                   → Documentation website
├── CHANGELOG.md               → Version history
└── .factory/AGENTS.md         → This file
```

## Skill Structure

Each skill follows this standard structure:

```
skills/<skill-name>/
├── SKILL.md                   → Main skill documentation (required)
│   └── YAML frontmatter:
│       - name: skill identifier
│       - description: what it does
│       - triggers: activation keywords
│       - dependencies: required skills (e.g., ["twitter", "reddit"])
├── scripts/                   → Executable Python/Shell scripts
├── examples/                  → Usage examples
└── references/                → API docs and references
```

**SKILL.md** must include YAML frontmatter with these fields:
- `name`: Unique identifier (kebab-case)
- `description`: Clear description of functionality
- `triggers`: Keywords that activate the skill
- `dependencies`: List of required skill names (optional)

Example:
```yaml
---
name: domain-hunter
description: Search domains, compare registrar prices, and find promo codes
triggers:
  - domain
  - registrar
  - buy domain
dependencies:
  - twitter
  - reddit
---
```

## Skill Development Patterns

### Creating a New Skill

1. **Create skill directory**
   ```bash
   mkdir -p skills/your-skill-name/scripts
   ```

2. **Write SKILL.md** with proper YAML frontmatter and usage instructions

3. **Add Python/Shell scripts** in `scripts/` directory with clear CLI interfaces

4. **Include examples** in `examples/` directory showing real workflows

5. **Add references** in `references/` for API documentation and resources

### Skill Script Guidelines

- Use clear argument names and help text (`--help`)
- Output machine-readable formats (JSON for data, markdown for reports)
- Include error handling and meaningful error messages
- Document dependencies and environment variables required
- Use relative paths or `${SKILL_DIR}` for portability
- When a skill adds CLI flags, scripts, or pricing changes, update `SKILL.md` examples and API notes in the same change so the docs stay aligned with the shipped behavior.

### Dependencies & Composition

When a skill requires other skills:
- List them in SKILL.md `dependencies` field
- Document which skills and minimum versions are needed
- Users install dependencies via: `npx skills add ReScienceLab/opc-skills --skill <dependency>`

Example (from domain-hunter):
```yaml
dependencies:
  - twitter
  - reddit
```

## Versioning & Dependencies Strategy

### Semantic Versioning

All version numbers follow [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH
- MAJOR: Breaking changes or API incompatibility
- MINOR: New features (backward compatible)
- PATCH: Bug fixes
```

### Individual Skill Versions

Each skill has its own version number in `skills.json`:

```json
{
  "name": "domain-hunter",
  "version": "1.0.0",
  "dependencies": ["twitter", "reddit"]
}
```

**Version updates:**
- Update version when skill functionality changes
- Update `skills.json` entry
- Add entry to `CHANGELOG.md` under the appropriate version

### Global Project Version

The root `version` in `skills.json` tracks the overall project:
- Updated during major releases coordinating multiple skills
- Useful for milestone tracking (1.0.0 = Initial release, 2.0.0 = Major refactor, etc.)
- Individual skills can increment independently

### Dependency Compatibility

When updating dependencies:
1. Test that dependent skills still work with new versions
2. Document breaking changes clearly in CHANGELOG.md
3. Consider running dependent skill tests before merging

**Example breaking change:**
```markdown
## [2.0.0] - 2025-XX-XX

### Changed
- **seo-geo**: Updated DataForSEO API integration (API v3.0 required)

### Fixed
- **twitter**: Fixed rate limiting handling (requires twitter >= 1.1.0)
```

## Git Workflow

We use **Git Flow** for version control. See [Git Flow](https://github.com/nvie/gitflow).

### Branching Strategy

```
main                               → Production releases
develop                            → Integration branch for next release

feature/skill/<name>/<feature>     → New skill feature
fix/skill/<name>/<issue>           → Skill bug fix
release/v<version>                 → Release preparation
hotfix/v<version>                  → Urgent production fixes
```

### Branch Naming Examples

```
feature/skill/domain-hunter/promo-code-scraper
fix/skill/requesthunt/reddit-pagination
feature/skill/seo-geo/perplexity-optimization
hotfix/v1.0.1
```

### Git Flow Commands

```bash
# Initialize git flow (first time only)
git flow init

# Start a new feature
git flow feature start skill/domain-hunter/advanced-filtering

# Finish feature - DO NOT use git flow feature finish
# Instead:
git push -u origin feature/skill/domain-hunter/advanced-filtering
gh pr create --base develop --head feature/skill/domain-hunter/advanced-filtering

# Start a release
git flow release start v2.0.0

# Finish release (merges to main, develop, creates tag)
git flow release finish v2.0.0
git push origin main develop --tags

# Start a hotfix
git flow hotfix start v1.0.1

# Finish hotfix
git flow hotfix finish v1.0.1
git push origin main develop --tags
```

### Important: Features Must Use PRs

**Never directly merge feature branches.** Always:
1. Push feature branch to origin
2. Create PR targeting `develop`
3. Request review and get approval
4. Merge via GitHub UI
5. Verify tests pass before merge

## Commit Convention

Use conventional commits for clear history:

```
feat(skill-name): Add new feature description
fix(skill-name): Fix bug description
docs(skill-name): Update documentation
test(skill-name): Add or update tests
refactor(skill-name): Refactor code without feature change
chore(skills): Maintenance task not specific to one skill
```

**Examples:**
```
feat(domain-hunter): Add WHOIS lookup for domain availability
fix(requesthunt): Handle Reddit API pagination edge case
docs(logo-creator): Add SVG export examples
chore(skills): Update dependencies
```

**Important**: Do not add any watermark or AI-generated signatures to commit messages.

## Issue Management

When creating issues, use type labels to categorize:

### Type Labels
- `bug` - Something isn't working
- `feature` - New skill or feature request
- `enhancement` - Improvement to existing skill
- `documentation` - Documentation improvements
- `refactor` - Code refactoring needed
- `test` - Test-related issues
- `chore` - Maintenance tasks

### Priority Labels
- `priority:high` - Critical or blocking
- `priority:medium` - Important but not blocking
- `priority:low` - Nice-to-have
- `good first issue` - Suitable for newcomers
- `help wanted` - Extra attention needed

### Skill-Specific Labels
One label per skill area:
- `skill:requesthunt`
- `skill:domain-hunter`
- `skill:logo-creator`
- `skill:banner-creator`
- `skill:nanobanana`
- `skill:reddit`
- `skill:twitter`
- `skill:producthunt`
- `skill:seo-geo`
- `infrastructure` - For tooling and overall project

### Writing Clear Issues

**For bugs:**
- Include reproduction steps
- Show expected vs actual behavior
- Link to related code or SKILL.md section

**For features:**
- Describe use case and desired outcome
- Reference any dependencies or related skills
- Provide example commands or workflows

**Example:**
```markdown
## Bug: RequestHunt pagination fails on large subreddits

**Reproduction:**
1. Run: `python3 scripts/list_requests.py --topic "python" --limit 1000`
2. See pagination error after 100 items

**Expected:** Fetch all 1000 items
**Actual:** Error after 100 items

**Related:** Issue #42 for similar Reddit API issue
```

## PR Requirements & Release Checklist

### Before Merging a PR

All of the following must pass:

- [ ] **Tests pass**: `npm run test` (website) passes without errors
- [ ] **Type checking**: `npm run typecheck` (website) shows no errors
- [ ] **Lint**: `npm run lint` (website) passes
- [ ] **Skill files valid**: SKILL.md has proper YAML frontmatter
- [ ] **Version updated**: `skills.json` version field updated (if functionality changed)
- [ ] **CHANGELOG.md updated**: Entry added under `[Unreleased]` section
- [ ] **Documentation updated**: SKILL.md or examples updated as needed
- [ ] **Dependencies checked**: New dependencies declared in SKILL.md
- [ ] **PR description**: References issue number (e.g., `Fixes #123`)

### Version Update Rules

Update versions in `skills.json` when:
- **MAJOR**: Breaking API changes, incompatible updates
- **MINOR**: New features or significant enhancements
- **PATCH**: Bug fixes, minor improvements

Do NOT update versions for:
- Documentation-only changes
- Internal refactoring without behavior changes
- Dependency version bumps (unless breaking)

### Merging and Closing Issues

Use closing keywords in PR description to auto-close issues:
```markdown
Fixes #123
Closes #124
Resolves #125
```

## Release Process

### Quick Release - Single Skill Update

Each skill maintains **independent version numbers** and can be released independently.

#### Example: Update twitter v1.0.0 → v1.1.0

1. **Create feature branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/skill/twitter/rate-limit-improvement
   ```

2. **Update version in skills.json** (only this skill)
   ```json
   {
     "name": "twitter",
     "version": "1.1.0"  // ← update version only
   }
   ```

3. **Update CHANGELOG.md** - Add entry in the appropriate Unreleased section
   ```markdown
   ### twitter
   #### [1.1.0] - 2025-01-22
   - **Added**: Retry mechanism for rate limit handling
   - **Fixed**: Improved error handling for connection timeouts
   ```

4. **Commit with conventional commit**
   ```bash
   git commit -m "feat(twitter): Add retry mechanism and improve rate limiting"
   ```

5. **Push and create PR**
   ```bash
   git push -u origin feature/skill/twitter/rate-limit-improvement
   gh pr create --base develop --head feature/skill/twitter/rate-limit-improvement
   ```

6. **Merge PR** when approved and tests pass

7. **After merge, identify and test dependents**
   - Check CHANGELOG.md Compatibility Matrix for who depends on twitter
   - Skills that depend on twitter: domain-hunter, seo-geo
   - Run compatibility tests: `python3 skills/domain-hunter/scripts/test_twitter.py`
   - **No need to bump dependent versions** unless there's a breaking change

### Coordinated Release - Multiple Skills

When multiple skills should release together (rare, for milestone releases):

1. **Start release branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/v2.0.0
   ```

2. **Update multiple skill versions** in `skills.json`
   ```json
   [
     { "name": "twitter", "version": "2.0.0" },
     { "name": "reddit", "version": "1.1.0" },
     { "name": "domain-hunter", "version": "1.1.0" }
   ]
   ```

3. **Update CHANGELOG.md** - Reorganize Unreleased sections into [2.0.0]
   - Move items from `[Unreleased]` sections to `## [2.0.0] - 2025-01-23`
   - Keep organization by skill (see example below)

4. **Run tests**
   ```bash
   npm run test && npm run typecheck
   ```

5. **Create single PR** targeting main
   ```bash
   git add skills.json CHANGELOG.md
   git commit -m "chore(release): Version 2.0.0 - multiple skill updates"
   git push -u origin release/v2.0.0
   gh pr create --base main --head release/v2.0.0
   ```

6. **Merge to main**

7. **Create GitHub release** with version tag and changelog

### Breaking Changes - Important ⚠️

When a skill introduces breaking changes, **clearly mark** them:

```markdown
### twitter
#### [2.0.0] - 2025-01-23 ⚠️ BREAKING
- **Changed**: API now requires v2 endpoint authentication
- **Removed**: Deprecated v1 endpoint support (use twitter-legacy v1.0.0 if needed)
- **Migration Guide**: See docs/migration-guide.md
```

#### Handling Breaking Changes in Dependent Skills

When a dependency skill has breaking changes:

1. **Identify dependent skills** using CHANGELOG Matrix
2. **Create separate PRs** for each dependent skill to adapt to the breaking change
3. **Test compatibility** before merging dependent updates
4. **Update dependent skill versions** only if they contain breaking change fixes

Example workflow:
```
Main dependency: twitter v1.0.0 → v2.0.0 (breaking)

Affected: domain-hunter, seo-geo

Create two PRs:
- feature/skill/domain-hunter/twitter-v2-compat
- feature/skill/seo-geo/twitter-v2-compat

Each can be reviewed and merged independently
```

### Version Compatibility Testing

**Before merging any skill update, test compatibility:**

```bash
# If skill has dependencies, test that it still works
# Example: when updating domain-hunter
python3 skills/domain-hunter/scripts/test_dependencies.py

# If skill is a dependency, test dependent skills
# Example: when updating nanobanana
python3 skills/logo-creator/scripts/test_nanobanana_compat.py
python3 skills/banner-creator/scripts/test_nanobanana_compat.py
```

### Dependency Update Rules

| Scenario | Action | Version Bump |
|----------|--------|-------------|
| Skill A releases minor update | Dependent skill B **no action needed** | No change |
| Skill A releases patch update | Dependent skill B **no action needed** | No change |
| Skill A releases breaking change | Dependent skill B **must update** to support new version | Patch or Minor |
| Dependent skill B wants to document support for new Skill A | Update B's CHANGELOG only | No version bump needed |

### Release Checklist

Before merging any release PR:

- [ ] Version numbers updated in `skills.json` (only for skills being released)
- [ ] CHANGELOG.md entries created for each updated skill
- [ ] Skill's own dependencies tested (if applicable)
- [ 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
