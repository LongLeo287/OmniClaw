---
id: reader-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:07.548288
---

# KNOWLEDGE EXTRACT: reader
> **Extracted on:** 2026-03-30 13:51:08
> **Source:** reader

---

## File: `.env.example`
```
# =============================================================================
# Reader Environment Variables
# =============================================================================

# -----------------------------------------------------------------------------
# Core Configuration
# -----------------------------------------------------------------------------

# Logging level: debug, info, warn, error (default: info)
LOG_LEVEL=info

# Environment: development (pretty logs) or production (JSON logs)
NODE_ENV=development

# -----------------------------------------------------------------------------
# Browser Pool Configuration
# -----------------------------------------------------------------------------

# Number of browser instances in the pool (default: 2)
POOL_SIZE=5

# Retire browser after N page loads (default: 100)
POOL_RETIRE_AFTER_PAGES=100

# Retire browser after N milliseconds (default: 1800000 = 30 minutes)
POOL_RETIRE_AFTER_MS=1800000

# Maximum pending requests in queue (default: 100)
MAX_QUEUE_SIZE=100

# Queue timeout in milliseconds (default: 120000 = 2 minutes)
QUEUE_TIMEOUT=120000

# -----------------------------------------------------------------------------
# Server Configuration (for production examples)
# -----------------------------------------------------------------------------

# HTTP server port
PORT=3001

# -----------------------------------------------------------------------------
# Proxy Configuration (optional)
# -----------------------------------------------------------------------------

# Proxy URL (e.g., http://user:pass@host:port)
# PROXY_URL=

# -----------------------------------------------------------------------------
# Job Queue Configuration (for BullMQ examples)
# -----------------------------------------------------------------------------

# Redis connection URL
# REDIS_URL=redis://localhost:6379

# Number of concurrent jobs per worker (default: 2)
# WORKER_CONCURRENCY=2

# -----------------------------------------------------------------------------
# AI Integration (for AI examples)
# -----------------------------------------------------------------------------

# OpenAI API key (for openai-summary, vercel-ai-stream, embeddings)
# OPENAI_API_KEY=sk-...

# Anthropic API key (for anthropic-summary)
# ANTHROPIC_API_KEY=sk-ant-...

# -----------------------------------------------------------------------------
# Vector Database (for RAG examples)
# -----------------------------------------------------------------------------

# Qdrant URL and API key
# QDRANT_URL=http://localhost:6333
# QDRANT_API_KEY=

# Pinecone API key
# PINECONE_API_KEY=

# -----------------------------------------------------------------------------
# Serverless Deployment (for Vercel/Lambda)
# -----------------------------------------------------------------------------

# WebSocket endpoint for remote browser (e.g., Browserless)
# BROWSER_WS_ENDPOINT=wss://chrome.browserless.io?token=...
```

## File: `.eslintrc.json`
```json
{
  "root": true,
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module",
    "project": true
  },
  "plugins": ["@typescript-eslint"],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "env": {
    "node": true,
    "es2022": true
  },
  "rules": {
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "@typescript-eslint/explicit-function-return-type": "off",
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "@typescript-eslint/no-non-null-assertion": "warn",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  },
  "ignorePatterns": ["dist/", "node_modules/", "*.js", "*.config.ts"]
}
```

## File: `.gitignore`
```
# Dependencies
node_modules/

# Build output
dist/

# Environment files
.env
.env.local
.env.*.local

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp
*.swo

# Coverage
coverage/
.nyc_output/

# Package manager locks
# Note: package-lock.json is tracked for reproducible builds
yarn.lock

# Bun
bun.lockb

# Temporary files
tmp/
temp/
*.tmp

# Hero/Ulixee session data
.ulixee/

# Claude Code context
CLAUDE.md

# Deployment configs (contain sensitive data)
deploy/
```

## File: `.leasotrc`
```
{
  "tags": ["TODO", "FIXME", "HACK", "XXX", "BUG", "OPTIMIZE", "REVIEW"],
  "ignore": ["node_modules/**", "dist/**"]
}
```

## File: `.nvmrc`
```
v22.12.0
```

## File: `.prettierrc`
```
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

## File: `CITATION.cff`
```
cff-version: 1.2.0
message: "If you use Reader in your research or project, please cite it."
title: "Reader: Open-source, production-grade web scraping engine built for LLMs"
type: software
authors:
  - family-names: Kaul
    given-names: Nihal
license: Apache-2.0
url: "https://github.com/vakra-dev/reader"
repository-code: "https://github.com/vakra-dev/reader"
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a welcoming experience for everyone, regardless of background or
identity.

## Our Standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior:

- Trolling, insulting or derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement Responsibilities

Project maintainers are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate or harmful.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.

## Enforcement

Instances of unacceptable behavior may be reported to the project maintainers at
**nihal.codes@gmail.com**. All complaints will be reviewed and investigated
promptly and fairly.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact:** Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence:** A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the behavior
was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact:** A violation through a single incident or series of actions.

**Consequence:** A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact:** A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence:** A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact:** Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence:** A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/),
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html).
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Reader

Thank you for your interest in contributing to Reader! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- **Node.js** >= 18 (v22 recommended)
- **npm** for package management
- **Git**

> **Note:** Always run scripts with Node.js (`npx tsx` or `node`) as Hero has ESM compatibility issues with other runtimes.

### Getting Started

1. **Fork the repository** on GitHub

2. **Clone your fork:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/reader.git
   cd reader
   ```

3. **Install dependencies:**

   ```bash
   npm install
   ```

4. **Verify setup:**

   ```bash
   npm run typecheck
   npm run build
   ```

5. **Test the CLI:**
   ```bash
   npx tsx src/cli/index.ts scrape https://example.com
   ```

## Project Structure

```
src/
├── index.ts              # Public API exports
├── client.ts             # ReaderClient - main API entry point
├── scraper.ts            # Scraper class - main scraping logic
├── crawler.ts            # Crawler class - link discovery
├── types.ts              # TypeScript types for scraping
├── crawl-types.ts        # TypeScript types for crawling
│
├── browser/
│   ├── pool.ts           # BrowserPool - manages Hero instances
│   ├── hero-config.ts    # Hero configuration
│   └── types.ts          # Pool types
│
├── cloudflare/
│   ├── detector.ts       # Challenge detection
│   ├── handler.ts        # Challenge resolution
│   └── types.ts          # Cloudflare types
│
├── formatters/
│   ├── markdown.ts       # Markdown formatter
│   ├── html.ts           # HTML formatter
│   ├── json.ts           # JSON formatter
│   ├── text.ts           # Text formatter
│   └── index.ts          # Re-exports
│
├── utils/
│   ├── content-cleaner.ts    # HTML content cleaning
│   ├── metadata-extractor.ts # Metadata extraction
│   ├── url-helpers.ts        # URL utilities
│   ├── rate-limiter.ts       # Rate limiting
│   └── logger.ts             # Logging
│
├── proxy/
│   └── config.ts         # Proxy configuration
│
├── daemon/
│   ├── index.ts          # Module exports
│   ├── server.ts         # DaemonServer - HTTP server with browser pool
│   └── client.ts         # DaemonClient - connects CLI to daemon
│
└── cli/
    └── index.ts          # CLI implementation
```

## Development Workflow

### Running the CLI

```bash
# Run CLI directly
npx tsx src/cli/index.ts scrape https://example.com

# With verbose output
npx tsx src/cli/index.ts scrape https://example.com -v

# Show browser window
npx tsx src/cli/index.ts scrape https://example.com --show-chrome
```

### Daemon Mode

```bash
# Start daemon with browser pool
npx tsx src/cli/index.ts start --pool-size 5

# Check daemon status
npx tsx src/cli/index.ts status

# Run commands (auto-connects to daemon)
npx tsx src/cli/index.ts scrape https://example.com

# Force standalone mode (bypass daemon)
npx tsx src/cli/index.ts scrape https://example.com --standalone

# Stop daemon
npx tsx src/cli/index.ts stop
```

### Code Quality

Run these commands before submitting a PR:

```bash
# Type checking
npm run typecheck

# Linting
npm run lint

# Auto-fix lint issues
npm run lint:fix

# Format code
npm run format

# Check formatting
npm run format:check

# Build
npm run build
```

### Finding TODOs

Track outstanding work:

```bash
npm run todo
```

## Making Changes

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Commit Messages

Write clear, concise commit messages:

```
type: short description

Longer description if needed.
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Examples:

```
feat: add support for custom user agents
fix: resolve timeout issue with Cloudflare challenges
docs: update proxy configuration guide
refactor: simplify browser pool recycling logic
```

### Pull Request Process

1. Create a new branch from `main`
2. Make your changes
3. Run all checks:
   ```bash
   npm run lint
   npm run format:check
   npm run typecheck
   npm run build
   ```
4. Push your branch and create a PR
5. Fill out the PR template
6. Wait for review

## Common Tasks

### Adding a New Output Format

1. Create `src/formatters/newformat.ts`:

   ```typescript
   export function formatToNewFormat(
     pages: Page[],
     baseUrl: string,
     scrapedAt: string,
     duration: number,
     metadata?: WebsiteMetadata
   ): string {
     // Implementation
   }
   ```

2. Export from `src/formatters/index.ts`

3. Add to format type in `src/types.ts`

4. Call formatter in `src/scraper.ts`

5. Update CLI validation in `src/cli/index.ts`

### Adding a New ScrapeOption

1. Add to `ScrapeOptions` interface in `src/types.ts`
2. Add default in `DEFAULT_OPTIONS`
3. Use in `Scraper` class via `this.options.newOption`
4. Add CLI flag in `src/cli/index.ts` if applicable
5. Update documentation

### Modifying Cloudflare Detection

1. Detection patterns: `src/cloudflare/detector.ts`
2. Resolution logic: `src/cloudflare/handler.ts`
3. Test with known Cloudflare-protected sites

### Adjusting Browser Pool

1. Default config: `src/browser/types.ts`
2. Pool logic: `src/browser/pool.ts`

## Testing

Currently testing is done manually. When adding new features:

1. **Test basic functionality:**

   ```bash
   npx tsx src/cli/index.ts scrape https://example.com
   ```

2. **Test Cloudflare-protected sites:**

   ```bash
   npx tsx src/cli/index.ts scrape https://cloudflare-protected-site.com -v
   ```

3. **Test different output formats:**

   ```bash
   npx tsx src/cli/index.ts scrape https://example.com -f markdown,html,json,text
   ```

4. **Test crawling:**

   ```bash
   npx tsx src/cli/index.ts crawl https://example.com -d 2 -m 10
   ```

5. **Test batch scraping:**

   ```bash
   npx tsx src/cli/index.ts scrape url1 url2 url3 -c 3 -v
   ```

6. **Test daemon mode:**

   ```bash
   # Start daemon
   npx tsx src/cli/index.ts start --pool-size 3

   # Test scraping via daemon
   npx tsx src/cli/index.ts scrape https://example.com

   # Check status
   npx tsx src/cli/index.ts status

   # Stop daemon
   npx tsx src/cli/index.ts stop
   ```

## Running Examples

The `examples/` folder contains working examples:

```bash
cd examples
npm install

# Basic examples
npx tsx basic/basic-scrape.ts
npx tsx basic/batch-scrape.ts
npx tsx basic/crawl-website.ts

# AI integration examples (requires API keys)
export OPENAI_API_KEY="sk-..."
npx tsx ai-tools/openai-summary.ts https://example.com

# Production server
npx tsx production/express-server/src/index.ts
```

## Code Style

- Use TypeScript for all new code
- Follow existing patterns in the codebase
- Use async/await instead of callbacks
- Prefer explicit types over `any`
- Use meaningful variable and function names
- Add JSDoc comments for public APIs

## Documentation

When making changes:

1. Update relevant markdown files in `docs/`
2. Update README.md if adding new features
3. Add JSDoc comments to new public functions
4. Update CLAUDE.md for AI context if architecture changes

### Documentation Files

| File                      | Purpose                         |
| ------------------------- | ------------------------------- |
| `README.md`               | Main documentation, quick start |
| `CONTRIBUTING.md`         | This file                       |
| `docs/getting-started.md` | Detailed setup guide            |
| `docs/api-reference.md`   | Complete API docs               |
| `docs/architecture.md`    | System design                   |
| `docs/troubleshooting.md` | Common issues                   |
| `docs/guides/`            | Feature guides                  |
| `docs/deployment/`        | Deployment guides               |

## Reporting Issues

When reporting bugs, please include:

- Operating system and version
- Node.js version (`node --version`)
- Reader version
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces
- Verbose output (`-v` flag)

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow project guidelines

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

## Disclaimer

By using Reader, you agree to the following:

- You are solely responsible for respecting websites' policies when scraping and crawling
- You will adhere to applicable privacy policies and terms of use before initiating scraping activities
- Reader respects robots.txt directives by default, but ultimate compliance is your responsibility

## Questions?

- Check the [documentation](https://docs.reader.dev)
- Search [GitHub Issues](https://github.com/vakra-dev/reader/issues)
- Ask in [Discord](https://discord.gg/6tjkq7J5WV)
- Open a new issue or discussion

Thank you for contributing!
```

## File: `LICENSE`
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
      on behalf of whom a Contribution has been received by Licensor and
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
          within such NOTICE file, excluding those notices that do not
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

   Copyright 2026 The Reader Authors

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

## File: `package.json`
```json
{
  "name": "@vakra-dev/reader",
  "version": "0.1.2",
  "description": "Open source, production grade web scraping engine for LLMs. Clean markdown output, ready for your agents.",
  "license": "Apache-2.0",
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "bin": {
    "reader": "./dist/cli/index.js"
  },
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  },
  "files": [
    "dist",
    "README.md",
    "LICENSE"
  ],
  "keywords": [
    "web-scraper",
    "web-crawler",
    "markdown",
    "llm",
    "rag",
    "ai-agents",
    "headless-browser",
    "typescript",
    "nodejs",
    "puppeteer-alternative",
    "playwright-alternative",
    "firecrawl-alternative",
    "crawl4ai-alternative",
    "content-extraction",
    "html-to-markdown",
    "web-scraping",
    "ai",
    "ulixee-hero"
  ],
  "author": "Nihal <nihal.codes@gmail.com>",
  "repository": {
    "type": "git",
    "url": "https://github.com/vakra-dev/reader.git"
  },
  "scripts": {
    "start": "node dist/cli/index.js",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write 'src/**/*.ts'",
    "format:check": "prettier --check 'src/**/*.ts'",
    "todo": "leasot 'src/**/*.ts'",
    "typecheck": "tsc --noEmit",
    "build": "tsup",
    "build:tsc": "tsc",
    "dev": "tsup --watch",
    "clean": "rm -rf dist",
    "prepublishOnly": "npm run clean && npm run build"
  },
  "dependencies": {
    "@ulixee/hero": "^2.0.0-alpha.34",
    "@ulixee/hero-core": "^2.0.0-alpha.34",
    "commander": "^12.0.0",
    "got-scraping": "^4.1.3",
    "linkedom": "^0.18.12",
    "p-limit": "^4.0.0",
    "pino": "^9.0.0",
    "re2": "^1.23.0",
    "@vakra-dev/supermarkdown": "^0.0.3"
  },
  "devDependencies": {
    "@types/node": "^20.10.6",
    "@typescript-eslint/eslint-plugin": "^7.0.0",
    "@typescript-eslint/parser": "^7.0.0",
    "eslint": "^8.57.0",
    "leasot": "^13.3.0",
    "pino-pretty": "^13.1.3",
    "prettier": "^3.2.0",
    "tsup": "^8.5.1",
    "typescript": "^5.3.3"
  },
  "engines": {
    "node": ">=18"
  }
}
```

## File: `README.md`
```markdown
<p align="center">
  <img src="docs/assets/logo.png" alt="Reader Logo" width="200" />
</p>

<h1 align="center">Reader</h1>

<p align="center">
  <strong>Open-source, production-grade web scraping engine built for LLMs.</strong>
</p>

<p align="center">
  Scrape and crawl the entire web, clean markdown, ready for your agents.
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://www.npmjs.com/package/@vakra-dev/reader"><img src="https://img.shields.io/npm/v/@vakra-dev/reader.svg" alt="npm version"></a>
  <a href="https://github.com/vakra-dev/reader/stargazers"><img src="https://img.shields.io/github/stars/vakra-dev/reader.svg?style=social" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="https://docs.reader.dev">Docs</a> · <a href="https://docs.reader.dev/home/examples">Examples</a> · <a href="https://discord.gg/6tjkq7J5WV">Discord</a>
</p>

<p align="center">
  <img src="./docs/assets/demo.gif" alt="Reader demo — scrape any URL to clean markdown" width="700" />
</p>

## The Problem

Building agents that need web access is frustrating. You piece together Puppeteer, add stealth plugins, fight Cloudflare, manage proxies and it still breaks in production.

Because production grade web scraping isn't about rendering a page and converting HTML to markdown. It's about everything underneath:

| Layer                    | What it actually takes                                              |
| ------------------------ | ------------------------------------------------------------------- |
| **Browser architecture** | Managing browser instances at scale, not one-off scripts            |
| **Anti-bot bypass**      | Cloudflare, Turnstile, JS challenges, they all block naive scrapers |
| **TLS fingerprinting**   | Real browsers have fingerprints. Puppeteer doesn't. Sites know.     |
| **Proxy infrastructure** | Datacenter vs residential, rotation strategies, sticky sessions     |
| **Resource management**  | Browser pooling, memory limits, graceful recycling                  |
| **Reliability**          | Rate limiting, retries, timeouts, caching, graceful degradation     |

I built **Reader**, a production-grade web scraping engine on top of [Ulixee Hero](https://ulixee.org/), a headless browser designed for exactly this.

## The Solution

Two primitives. That's it.

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

// Scrape URLs → clean markdown
const result = await reader.scrape({ urls: ["https://example.com"] });
console.log(result.data[0].markdown);

// Crawl a site → discover + scrape pages
const pages = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  scrape: true,
});
console.log(`Found ${pages.urls.length} pages`);
```

All the hard stuff, browser pooling, challenge detection, proxy rotation, retries, happens under the hood. You get clean markdown. Your agents get the web.

> [!TIP]
> If Reader is useful to you, a [star on GitHub](https://github.com/vakra-dev/reader) helps others discover the project.

## Features

- **Cloudflare Bypass** - TLS fingerprinting, DNS over TLS, WebRTC masking
- **Clean Output** - Markdown and HTML with automatic main content extraction
- **Smart Content Cleaning** - Removes nav, headers, footers, popups, cookie banners
- **CLI & API** - Use from command line or programmatically
- **Browser Pool** - Auto-recycling, health monitoring, queue management
- **Concurrent Scraping** - Parallel URL processing with progress tracking
- **Website Crawling** - BFS link discovery with depth/page limits
- **Proxy Support** - Datacenter and residential with sticky sessions

## Installation

```bash
npm install @vakra-dev/reader
```

**Requirements:** Node.js >= 18

## Quick Start

### Basic Scrape

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown", "html"],
});

console.log(result.data[0].markdown);
console.log(result.data[0].html);

await reader.close();
```

### Batch Scraping with Concurrency

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com", "https://example.org", "https://example.net"],
  formats: ["markdown"],
  batchConcurrency: 3,
  onProgress: (progress) => {
    console.log(`${progress.completed}/${progress.total}: ${progress.currentUrl}`);
  },
});

console.log(`Scraped ${result.batchMetadata.successfulUrls} URLs`);

await reader.close();
```

### Crawling

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  maxPages: 20,
  scrape: true,
});

console.log(`Discovered ${result.urls.length} URLs`);
console.log(`Scraped ${result.scraped?.batchMetadata.successfulUrls} pages`);

await reader.close();
```

### With Proxy

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown"],
  proxy: {
    type: "residential",
    host: "proxy.example.com",
    port: 8080,
    username: "username",
    password: "password",
    country: "us",
  },
});

await reader.close();
```

### With Proxy Rotation

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({
  proxies: [
    { host: "proxy1.example.com", port: 8080, username: "user", password: "pass" },
    { host: "proxy2.example.com", port: 8080, username: "user", password: "pass" },
  ],
  proxyRotation: "round-robin", // or "random"
});

const result = await reader.scrape({
  urls: ["https://example.com", "https://example.org"],
  formats: ["markdown"],
  batchConcurrency: 2,
});

await reader.close();
```

### With Browser Pool Configuration

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({
  browserPool: {
    size: 5, // 5 browser instances
    retireAfterPages: 50, // Recycle after 50 pages
    retireAfterMinutes: 15, // Recycle after 15 minutes
  },
  verbose: true,
});

const result = await reader.scrape({
  urls: manyUrls,
  batchConcurrency: 5,
});

await reader.close();
```

## CLI Reference

### Daemon Mode

For multiple requests, start a daemon to keep browser pool warm:

```bash
# Start daemon with browser pool
npx reader start --pool-size 5

# All subsequent commands auto-connect to daemon
npx reader scrape https://example.com
npx reader crawl https://example.com -d 2

# Check daemon status
npx reader status

# Stop daemon
npx reader stop

# Force standalone mode (bypass daemon)
npx reader scrape https://example.com --standalone
```

### `reader scrape <urls...>`

Scrape one or more URLs.

```bash
# Scrape a single URL
npx reader scrape https://example.com

# Scrape with multiple formats
npx reader scrape https://example.com -f markdown,html

# Scrape multiple URLs concurrently
npx reader scrape https://example.com https://example.org -c 2

# Save to file
npx reader scrape https://example.com -o output.md
```

| Option                   | Type   | Default      | Description                                             |
| ------------------------ | ------ | ------------ | ------------------------------------------------------- |
| `-f, --format <formats>` | string | `"markdown"` | Output formats (comma-separated: markdown,html)         |
| `-o, --output <file>`    | string | stdout       | Output file path                                        |
| `-c, --concurrency <n>`  | number | `1`          | Parallel requests                                       |
| `-t, --timeout <ms>`     | number | `30000`      | Request timeout in milliseconds                         |
| `--batch-timeout <ms>`   | number | `300000`     | Total timeout for entire batch operation                |
| `--proxy <url>`          | string | -            | Proxy URL (e.g., http://user:pass@host:port)            |
| `--user-agent <string>`  | string | -            | Custom user agent string                                |
| `--show-chrome`          | flag   | -            | Show browser window for debugging                       |
| `--no-main-content`      | flag   | -            | Disable main content extraction (include full page)     |
| `--include-tags <sel>`   | string | -            | CSS selectors for elements to include (comma-separated) |
| `--exclude-tags <sel>`   | string | -            | CSS selectors for elements to exclude (comma-separated) |
| `-v, --verbose`          | flag   | -            | Enable verbose logging                                  |

### `reader crawl <url>`

Crawl a website to discover pages.

```bash
# Crawl with default settings
npx reader crawl https://example.com

# Crawl deeper with more pages
npx reader crawl https://example.com -d 3 -m 50

# Crawl and scrape content
npx reader crawl https://example.com -d 2 --scrape

# Filter URLs with patterns
npx reader crawl https://example.com --include "blog/*" --exclude "admin/*"
```

| Option                   | Type   | Default      | Description                                     |
| ------------------------ | ------ | ------------ | ----------------------------------------------- |
| `-d, --depth <n>`        | number | `1`          | Maximum crawl depth                             |
| `-m, --max-pages <n>`    | number | `20`         | Maximum pages to discover                       |
| `-s, --scrape`           | flag   | -            | Also scrape content of discovered pages         |
| `-f, --format <formats>` | string | `"markdown"` | Output formats when scraping (comma-separated)  |
| `-o, --output <file>`    | string | stdout       | Output file path                                |
| `--delay <ms>`           | number | `1000`       | Delay between requests in milliseconds          |
| `-t, --timeout <ms>`     | number | -            | Total timeout for crawl operation               |
| `--include <patterns>`   | string | -            | URL patterns to include (comma-separated regex) |
| `--exclude <patterns>`   | string | -            | URL patterns to exclude (comma-separated regex) |
| `--proxy <url>`          | string | -            | Proxy URL (e.g., http://user:pass@host:port)    |
| `--user-agent <string>`  | string | -            | Custom user agent string                        |
| `--show-chrome`          | flag   | -            | Show browser window for debugging               |
| `-v, --verbose`          | flag   | -            | Enable verbose logging                          |

## API Reference

### `ReaderClient`

The recommended way to use Reader. Manages HeroCore lifecycle automatically.

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({ verbose: true });

// Scrape
const result = await reader.scrape({ urls: ["https://example.com"] });

// Crawl
const crawlResult = await reader.crawl({ url: "https://example.com", depth: 2 });

// Close when done (optional - auto-closes on exit)
await reader.close();
```

#### Constructor Options

| Option          | Type                | Default         | Description                                      |
| --------------- | ------------------- | --------------- | ------------------------------------------------ |
| `verbose`       | `boolean`           | `false`         | Enable verbose logging                           |
| `showChrome`    | `boolean`           | `false`         | Show browser window for debugging                |
| `browserPool`   | `BrowserPoolConfig` | `undefined`     | Browser pool configuration (size, recycling)     |
| `proxies`       | `ProxyConfig[]`     | `undefined`     | Array of proxies for rotation                    |
| `proxyRotation` | `string`            | `"round-robin"` | Rotation strategy: `"round-robin"` or `"random"` |

#### BrowserPoolConfig

| Option               | Type     | Default | Description                         |
| -------------------- | -------- | ------- | ----------------------------------- |
| `size`               | `number` | `2`     | Number of browser instances in pool |
| `retireAfterPages`   | `number` | `100`   | Recycle browser after N page loads  |
| `retireAfterMinutes` | `number` | `30`    | Recycle browser after N minutes     |
| `maxQueueSize`       | `number` | `100`   | Max pending requests in queue       |

#### Methods

| Method            | Description                        |
| ----------------- | ---------------------------------- |
| `scrape(options)` | Scrape one or more URLs            |
| `crawl(options)`  | Crawl a website to discover pages  |
| `start()`         | Pre-initialize HeroCore (optional) |
| `isReady()`       | Check if client is initialized     |
| `close()`         | Close client and release resources |

### `scrape(options): Promise<ScrapeResult>`

Scrape one or more URLs. Can be used directly or via `ReaderClient`.

| Option             | Type                          | Required | Default        | Description                                                     |
| ------------------ | ----------------------------- | -------- | -------------- | --------------------------------------------------------------- |
| `urls`             | `string[]`                    | Yes      | -              | Array of URLs to scrape                                         |
| `formats`          | `Array<"markdown" \| "html">` | No       | `["markdown"]` | Output formats                                                  |
| `onlyMainContent`  | `boolean`                     | No       | `true`         | Extract only main content (removes nav/header/footer)           |
| `includeTags`      | `string[]`                    | No       | `[]`           | CSS selectors for elements to keep                              |
| `excludeTags`      | `string[]`                    | No       | `[]`           | CSS selectors for elements to remove                            |
| `userAgent`        | `string`                      | No       | -              | Custom user agent string                                        |
| `timeoutMs`        | `number`                      | No       | `30000`        | Request timeout in milliseconds                                 |
| `includePatterns`  | `string[]`                    | No       | `[]`           | URL patterns to include (regex strings)                         |
| `excludePatterns`  | `string[]`                    | No       | `[]`           | URL patterns to exclude (regex strings)                         |
| `batchConcurrency` | `number`                      | No       | `1`            | Number of URLs to process in parallel                           |
| `batchTimeoutMs`   | `number`                      | No       | `300000`       | Total timeout for entire batch operation                        |
| `maxRetries`       | `number`                      | No       | `2`            | Maximum retry attempts for failed URLs                          |
| `onProgress`       | `function`                    | No       | -              | Progress callback: `({ completed, total, currentUrl }) => void` |
| `proxy`            | `ProxyConfig`                 | No       | -              | Proxy configuration object                                      |
| `waitForSelector`  | `string`                      | No       | -              | CSS selector to wait for before page is loaded                  |
| `verbose`          | `boolean`                     | No       | `false`        | Enable verbose logging                                          |
| `showChrome`       | `boolean`                     | No       | `false`        | Show Chrome window for debugging                                |
| `connectionToCore` | `any`                         | No       | -              | Connection to shared Hero Core (for production)                 |

**Returns:** `Promise<ScrapeResult>`

```typescript
interface ScrapeResult {
  data: WebsiteScrapeResult[];
  batchMetadata: BatchMetadata;
}

interface WebsiteScrapeResult {
  markdown?: string;
  html?: string;
  metadata: {
    baseUrl: string;
    totalPages: number;
    scrapedAt: string;
    duration: number;
    website: WebsiteMetadata;
  };
}

interface BatchMetadata {
  totalUrls: number;
  successfulUrls: number;
  failedUrls: number;
  scrapedAt: string;
  totalDuration: number;
  errors?: Array<{ url: string; error: string }>;
}
```

### `crawl(options): Promise<CrawlResult>`

Crawl a website to discover pages.

| Option              | Type                                              | Required | Default                | Description                                     |
| ------------------- | ------------------------------------------------- | -------- | ---------------------- | ----------------------------------------------- |
| `url`               | `string`                                          | Yes      | -                      | Single seed URL to start crawling from          |
| `depth`             | `number`                                          | No       | `1`                    | Maximum depth to crawl                          |
| `maxPages`          | `number`                                          | No       | `20`                   | Maximum pages to discover                       |
| `scrape`            | `boolean`                                         | No       | `false`                | Also scrape full content of discovered pages    |
| `delayMs`           | `number`                                          | No       | `1000`                 | Delay between requests in milliseconds          |
| `timeoutMs`         | `number`                                          | No       | -                      | Total timeout for entire crawl operation        |
| `includePatterns`   | `string[]`                                        | No       | -                      | URL patterns to include (regex strings)         |
| `excludePatterns`   | `string[]`                                        | No       | -                      | URL patterns to exclude (regex strings)         |
| `formats`           | `Array<"markdown" \| "html" \| "json" \| "text">` | No       | `["markdown", "html"]` | Output formats for scraped content              |
| `scrapeConcurrency` | `number`                                          | No       | `2`                    | Number of URLs to scrape in parallel            |
| `proxy`             | `ProxyConfig`                                     | No       | -                      | Proxy configuration object                      |
| `userAgent`         | `string`                                          | No       | -                      | Custom user agent string                        |
| `verbose`           | `boolean`                                         | No       | `false`                | Enable verbose logging                          |
| `showChrome`        | `boolean`                                         | No       | `false`                | Show Chrome window for debugging                |
| `connectionToCore`  | `any`                                             | No       | -                      | Connection to shared Hero Core (for production) |

**Returns:** `Promise<CrawlResult>`

```typescript
interface CrawlResult {
  urls: CrawlUrl[];
  scraped?: ScrapeResult;
  metadata: CrawlMetadata;
}

interface CrawlUrl {
  url: string;
  title: string;
  description: string | null;
}

interface CrawlMetadata {
  totalUrls: number;
  maxDepth: number;
  totalDuration: number;
  seedUrl: string;
}
```

### ProxyConfig

| Option     | Type                            | Required | Default | Description                                             |
| ---------- | ------------------------------- | -------- | ------- | ------------------------------------------------------- |
| `url`      | `string`                        | No       | -       | Full proxy URL (takes precedence over other fields)     |
| `type`     | `"datacenter" \| "residential"` | No       | -       | Proxy type                                              |
| `host`     | `string`                        | No       | -       | Proxy host                                              |
| `port`     | `number`                        | No       | -       | Proxy port                                              |
| `username` | `string`                        | No       | -       | Proxy username                                          |
| `password` | `string`                        | No       | -       | Proxy password                                          |
| `country`  | `string`                        | No       | -       | Country code for residential proxies (e.g., 'us', 'uk') |

## Advanced Usage

### Browser Pool

For high-volume scraping, use the browser pool directly:

```typescript
import { BrowserPool } from "@vakra-dev/reader";

const pool = new BrowserPool({ size: 5 });
await pool.initialize();

// Use withBrowser for automatic acquire/release
const title = await pool.withBrowser(async (hero) => {
  await hero.goto("https://example.com");
  return await hero.document.title;
});

// Check pool health
const health = await pool.healthCheck();
console.log(`Pool healthy: ${health.healthy}`);

await pool.shutdown();
```

### Shared Hero Core (Production)

For production servers, use a shared Hero Core to avoid spawning new Chrome for each request:

```typescript
import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";
import { scrape } from "@vakra-dev/reader";

// Initialize once at startup
const heroCore = new HeroCore();
await heroCore.start();

// Create connection for each request
function createConnection() {
  const bridge = new TransportBridge();
  heroCore.addConnection(bridge.transportToClient);
  return new ConnectionToHeroCore(bridge.transportToCore);
}

// Use in requests
const result = await scrape({
  urls: ["https://example.com"],
  connectionToCore: createConnection(),
});

// Shutdown on exit
await heroCore.close();
```

### Cloudflare Challenge Detection

```typescript
import { detectChallenge, waitForChallengeResolution } from "@vakra-dev/reader";

const detection = await detectChallenge(hero);

if (detection.isChallenge) {
  console.log(`Challenge detected: ${detection.type}`);

  const result = await waitForChallengeResolution(hero, {
    maxWaitMs: 45000,
    pollIntervalMs: 500,
    verbose: true,
    initialUrl: await hero.url,
  });

  if (result.resolved) {
    console.log(`Challenge resolved via ${result.method} in ${result.waitedMs}ms`);
  }
}
```

### Custom Formatters

```typescript
import { formatToMarkdown, formatToText, formatToHTML, formatToJson } from "@vakra-dev/reader";

// Format pages to different outputs
const markdown = formatToMarkdown(pages, baseUrl, scrapedAt, duration, metadata);
const text = formatToText(pages, baseUrl, scrapedAt, duration, metadata);
const html = formatToHTML(pages, baseUrl, scrapedAt, duration, metadata);
const json = formatToJson(pages, baseUrl, scrapedAt, duration, metadata);
```

## How It Works

### Cloudflare Bypass

Reader uses [Ulixee Hero](https://ulixee.org/), a headless browser with advanced anti-detection:

1. **TLS Fingerprinting** - Emulates real Chrome browser fingerprints
2. **DNS over TLS** - Uses Cloudflare DNS (1.1.1.1) to mimic Chrome behavior
3. **WebRTC IP Masking** - Prevents IP leaks
4. **Multi-Signal Detection** - Detects challenges using DOM elements and text patterns
5. **Dynamic Waiting** - Polls for challenge resolution with URL redirect detection

### Browser Pool

- **Auto-Recycling** - Browsers recycled after 100 requests or 30 minutes
- **Health Monitoring** - Background health checks every 5 minutes
- **Request Queuing** - Queues requests when pool is full (max 100)

### HTML to Markdown: supermarkdown

Reader uses [**supermarkdown**](https://github.com/vakra-dev/supermarkdown) for HTML to Markdown conversion - a sister project we built from scratch specifically for web scraping and LLM pipelines.

**Why we built it:**

When you're scraping the web, you encounter messy, malformed HTML that breaks most converters. And when you're feeding content to LLMs, you need clean output without artifacts or noise. We needed a converter that handles real-world HTML reliably while producing high-quality markdown.

**What supermarkdown offers:**

| Feature              | Benefit                                              |
| -------------------- | ---------------------------------------------------- |
| **Written in Rust**  | Native performance with Node.js bindings via napi-rs |
| **Full GFM support** | Tables, task lists, strikethrough, autolinks         |
| **LLM-optimized**    | Clean output designed for AI consumption             |
| **Battle-tested**    | Handles malformed HTML from real web pages           |
| **CSS selectors**    | Include/exclude elements during conversion           |

supermarkdown is open source and available as both a Rust crate and npm package:

```bash
# npm
npm install @vakra-dev/supermarkdown

# Rust
cargo add supermarkdown
```

Check out the [supermarkdown repository](https://github.com/vakra-dev/supermarkdown) for examples and documentation.

## Server Deployment

Reader uses a real Chromium browser under the hood. On headless Linux servers (VPS, EC2, etc.), you need to install Chrome's system dependencies:

```bash
# Debian/Ubuntu
sudo apt-get install -y libnspr4 libnss3 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libxcb1 libatspi2.0-0 libx11-6 libxcomposite1 libxdamage1 \
  libxext6 libxfixes3 libxrandr2 libgbm1 libcairo2 libpango-1.0-0 libasound2
```

This is the same requirement that Puppeteer and Playwright have on headless Linux. macOS, Windows, and Linux desktops already have these libraries.

For Docker and production deployment guides, see the [deployment documentation](https://docs.reader.dev/documentation/guides/deployment).

## Documentation

Full documentation is available at **[docs.reader.dev](https://docs.reader.dev)**, including guides for scraping, crawling, proxy configuration, browser pool management, and deployment.

### Examples

| Example                                                      | Description                                |
| ------------------------------------------------------------ | ------------------------------------------ |
| [Basic Scraping](examples/basic/basic-scrape.ts)             | Simple single-URL scraping                 |
| [Batch Scraping](examples/basic/batch-scrape.ts)             | Concurrent multi-URL scraping              |
| [Browser Pool Config](examples/basic/browser-pool-config.ts) | Configure browser pool for high throughput |
| [Proxy Pool](examples/basic/proxy-pool.ts)                   | Proxy rotation with multiple proxies       |
| [Cloudflare Bypass](examples/basic/cloudflare-bypass.ts)     | Scrape Cloudflare-protected sites          |
| [All Formats](examples/basic/all-formats.ts)                 | Output in markdown, html, json, text       |
| [Crawl Website](examples/basic/crawl-website.ts)             | Crawl and discover pages                   |
| [AI Tools](examples/ai-tools/)                               | OpenAI, Anthropic, LangChain integrations  |
| [Production](examples/production/)                           | Express server, job queues                 |
| [Deployment](examples/deployment/)                           | Docker, Lambda, Vercel                     |

## Development

```bash
# Install dependencies
npm install

# Run linting
npm run lint

# Format code
npm run format

# Type check
npm run typecheck

# Find TODOs
npm run todo
```

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[Apache 2.0](LICENSE) - See LICENSE for details.

## Citation

If you use Reader in your research or project, please cite it:

```bibtex
@software{reader.dev,
  author = {Kaul, Nihal},
  title = {Reader: Open-source, production-grade web scraping engine built for LLMs},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/vakra-dev/reader}
}
```

## Support

- [GitHub Issues](https://github.com/vakra-dev/reader/issues)
- [Documentation](https://docs.reader.dev)
- [Discord](https://discord.gg/6tjkq7J5WV)
```

## File: `result.md`
```markdown
{
  "data": [
    {
      "markdown": "Example Domain\n\n# Example Domain\n\nThis domain is for use in documentation examples without needing permission. Avoid use in operations.\n\n[Learn more](https://iana.org/domains/example)",
      "metadata": {
        "baseUrl": "https://example.com",
        "totalPages": 1,
        "scrapedAt": "2026-02-02T01:43:05.132Z",
        "duration": 256,
        "website": {
          "title": "Example Domain",
          "description": null,
          "author": null,
          "language": "en",
          "charset": null,
          "favicon": "https://example.com/favicon.ico",
          "canonical": null,
          "image": null,
          "keywords": null,
          "robots": null,
          "themeColor": null,
          "openGraph": null,
          "twitter": null
        }
      }
    }
  ],
  "batchMetadata": {
    "totalUrls": 1,
    "successfulUrls": 1,
    "failedUrls": 0,
    "scrapedAt": "2026-02-02T01:43:05.132Z",
    "totalDuration": 260,
    "errors": []
  }
}
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| Latest  | Yes       |

We only provide security fixes for the latest release.

## Reporting a Vulnerability

If you discover a security vulnerability in Reader, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, email **nihal.codes@gmail.com** with:

- A description of the vulnerability
- Steps to reproduce the issue
- The potential impact
- Any suggested fixes (optional)

## What to Expect

- **Acknowledgment** within 48 hours of your report
- **Status update** within 7 days with an assessment and timeline
- **Credit** in the release notes (unless you prefer to remain anonymous)

## Scope

The following are in scope:

- The `@vakra-dev/reader` npm package
- The Reader CLI tool
- The Reader Cloud API (`cloud.reader.dev`)

The following are out of scope:

- Vulnerabilities in upstream dependencies (report these to the respective projects)
- Issues related to websites blocking scraping (this is expected behavior, not a vulnerability)

## Responsible Use

Reader is a web scraping tool. Users are responsible for complying with applicable laws and website terms of service. The project maintainers are not responsible for how the tool is used.
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ESNext", "DOM"],
    "outDir": "./dist",
    "baseUrl": ".",
    "paths": {
      "@vakra-dev/reader": ["./src/index.ts"]
    },
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "removeComments": false,
    "noImplicitAny": true,
    "noImplicitReturns": false,
    "noImplicitThis": true,
    "noUnusedLocals": true,
    "noUnusedParameters": false,
    "exactOptionalPropertyTypes": false,
    "resolveJsonModule": true,
    "types": ["node"]
  },
  "include": ["src/**/*", "examples/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

## File: `tsup.config.ts`
```typescript
import { defineConfig } from "tsup";

// Packages that should not be bundled (native modules, CommonJS deps)
const external = [
  "@ulixee/hero",
  "@ulixee/hero-core",
  "@ulixee/net",
  "@ulixee/commons",
  "re2",
  "pino",
  "pino-pretty",
];

export default defineConfig([
  // Main library
  {
    entry: ["src/index.ts"],
    format: ["esm"],
    dts: true,
    clean: true,
    outDir: "dist",
    splitting: false,
    sourcemap: true,
    target: "node18",
    external,
  },
  // CLI (shebang preserved from source)
  {
    entry: ["src/cli/index.ts"],
    format: ["esm"],
    dts: false,
    outDir: "dist/cli",
    splitting: false,
    sourcemap: true,
    target: "node18",
    external,
  },
]);
```

## File: `docs/api-reference.md`
```markdown
# API Reference

Complete API documentation for Reader.

## ReaderClient (Recommended)

The recommended way to use Reader. Manages HeroCore lifecycle automatically, reuses connections efficiently, and auto-closes on process exit.

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({ verbose: true });

// Scrape URLs
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown", "text"],
});

// Crawl a website
const crawlResult = await reader.crawl({
  url: "https://example.com",
  depth: 2,
});

// Close when done (optional - auto-closes on exit)
await reader.close();
```

### Constructor

```typescript
new ReaderClient(options?: ReaderClientOptions)
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `verbose` | `boolean` | `false` | Enable verbose logging |
| `showChrome` | `boolean` | `false` | Show browser window for debugging |
| `browserPool` | `BrowserPoolConfig` | - | Browser pool configuration |
| `proxies` | `ProxyConfig[]` | - | List of proxies to rotate through |
| `proxyRotation` | `"round-robin" \| "random"` | `"round-robin"` | Proxy rotation strategy |

#### BrowserPoolConfig

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `size` | `number` | `2` | Number of browser instances |
| `retireAfterPages` | `number` | `100` | Retire browser after N page loads |
| `retireAfterMinutes` | `number` | `30` | Retire browser after N minutes |
| `maxQueueSize` | `number` | `100` | Maximum pending requests in queue |

### Methods

#### start()

Pre-initialize HeroCore. Called automatically on first scrape/crawl.

```typescript
await reader.start(): Promise<void>
```

#### scrape(options)

Scrape one or more URLs.

```typescript
const result = await reader.scrape(options): Promise<ScrapeResult>
```

See [ScrapeOptions](#scrapeoptions) for available options.

#### crawl(options)

Crawl a website to discover pages.

```typescript
const result = await reader.crawl(options): Promise<CrawlResult>
```

See [CrawlOptions](#crawloptions) for available options.

#### isReady()

Check if the client is initialized and ready.

```typescript
reader.isReady(): boolean
```

#### close()

Close the client and release resources.

```typescript
await reader.close(): Promise<void>
```

---

## Direct Functions (Advanced)

For advanced use cases where you need custom HeroCore management, you can use the direct functions. Note that without `connectionToCore`, each call spawns a new HeroCore instance which is less efficient.

### scrape(options)

Scrape one or more URLs and return content in specified formats.

```typescript
import { scrape } from "@vakra-dev/reader";

const result = await scrape({
  urls: ["https://example.com"],
  formats: ["markdown", "text"],
});
```

#### Parameters

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `urls` | `string[]` | Yes | - | Array of URLs to scrape |
| `formats` | `FormatType[]` | No | `["markdown"]` | Output formats |
| `includeMetadata` | `boolean` | No | `true` | Include metadata in formatted output |
| `userAgent` | `string` | No | - | Custom user agent string |
| `timeoutMs` | `number` | No | `30000` | Request timeout in milliseconds |
| `includePatterns` | `string[]` | No | `[]` | URL patterns to include (regex) |
| `excludePatterns` | `string[]` | No | `[]` | URL patterns to exclude (regex) |
| `batchConcurrency` | `number` | No | `1` | URLs to process in parallel |
| `batchTimeoutMs` | `number` | No | `300000` | Total batch timeout |
| `maxRetries` | `number` | No | `2` | Retry attempts for failed URLs |
| `onProgress` | `ProgressCallback` | No | - | Progress callback function |
| `proxy` | `ProxyConfig` | No | - | Proxy configuration |
| `waitForSelector` | `string` | No | - | CSS selector to wait for |
| `verbose` | `boolean` | No | `false` | Enable verbose logging |
| `showChrome` | `boolean` | No | `false` | Show browser window |
| `connectionToCore` | `any` | No | - | Shared Hero Core connection |

#### Returns

`Promise<ScrapeResult>`

```typescript
interface ScrapeResult {
  data: WebsiteScrapeResult[];
  batchMetadata: BatchMetadata;
}
```

#### Example

```typescript
// Using ReaderClient (recommended)
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com", "https://example.org"],
  formats: ["markdown", "json"],
  batchConcurrency: 2,
  onProgress: ({ completed, total, currentUrl }) => {
    console.log(`[${completed}/${total}] ${currentUrl}`);
  },
});

for (const site of result.data) {
  console.log("URL:", site.metadata.baseUrl);
  console.log("Markdown:", site.markdown?.substring(0, 200));
}

await reader.close();
```

---

### crawl(options)

Crawl a website to discover pages, optionally scraping their content.

```typescript
// Using ReaderClient (recommended)
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();
const result = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  maxPages: 20,
  scrape: true,
});
await reader.close();
```

#### Parameters

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | `string` | Yes | - | Seed URL to start crawling |
| `depth` | `number` | No | `1` | Maximum crawl depth |
| `maxPages` | `number` | No | `20` | Maximum pages to discover |
| `scrape` | `boolean` | No | `false` | Also scrape discovered pages |
| `delayMs` | `number` | No | `1000` | Delay between requests |
| `timeoutMs` | `number` | No | - | Total crawl timeout |
| `includePatterns` | `string[]` | No | - | URL patterns to include |
| `excludePatterns` | `string[]` | No | - | URL patterns to exclude |
| `formats` | `FormatType[]` | No | `["markdown", "html"]` | Output formats when scraping |
| `scrapeConcurrency` | `number` | No | `2` | Scraping parallelism |
| `proxy` | `ProxyConfig` | No | - | Proxy configuration |
| `userAgent` | `string` | No | - | Custom user agent |
| `verbose` | `boolean` | No | `false` | Enable verbose logging |
| `showChrome` | `boolean` | No | `false` | Show browser window |
| `connectionToCore` | `any` | No | - | Shared Hero Core connection |

#### Returns

`Promise<CrawlResult>`

```typescript
interface CrawlResult {
  urls: CrawlUrl[];
  scraped?: ScrapeResult;
  metadata: CrawlMetadata;
}
```

#### Example

```typescript
const reader = new ReaderClient();
const result = await reader.crawl({
  url: "https://docs.example.com",
  depth: 3,
  maxPages: 50,
  includePatterns: ["docs/*"],
  excludePatterns: ["docs/archive/*"],
  scrape: true,
});

console.log(`Discovered ${result.urls.length} pages`);
result.urls.forEach((page) => {
  console.log(`- ${page.title}: ${page.url}`);
});

if (result.scraped) {
  console.log(`Scraped ${result.scraped.batchMetadata.successfulUrls} pages`);
}

await reader.close();
```

---

## Type Definitions

### ScrapeOptions

```typescript
interface ScrapeOptions {
  urls: string[];
  formats?: Array<"markdown" | "html" | "json" | "text">;
  includeMetadata?: boolean;
  userAgent?: string;
  timeoutMs?: number;
  includePatterns?: string[];
  excludePatterns?: string[];
  batchConcurrency?: number;
  batchTimeoutMs?: number;
  maxRetries?: number;
  onProgress?: (progress: ProgressInfo) => void;
  proxy?: ProxyConfig;
  waitForSelector?: string;
  verbose?: boolean;
  showChrome?: boolean;
  connectionToCore?: any;
}
```

### CrawlOptions

```typescript
interface CrawlOptions {
  url: string;
  depth?: number;
  maxPages?: number;
  scrape?: boolean;
  delayMs?: number;
  timeoutMs?: number;
  includePatterns?: string[];
  excludePatterns?: string[];
  formats?: Array<"markdown" | "html" | "json" | "text">;
  scrapeConcurrency?: number;
  proxy?: ProxyConfig;
  userAgent?: string;
  verbose?: boolean;
  showChrome?: boolean;
  connectionToCore?: any;
}
```

### ProxyConfig

```typescript
interface ProxyConfig {
  url?: string;
  type?: "datacenter" | "residential";
  host?: string;
  port?: number;
  username?: string;
  password?: string;
  country?: string;
}
```

### ScrapeResult

```typescript
interface ScrapeResult {
  data: WebsiteScrapeResult[];
  batchMetadata: BatchMetadata;
}
```

### WebsiteScrapeResult

```typescript
interface WebsiteScrapeResult {
  markdown?: string;
  html?: string;
  json?: string;
  text?: string;
  metadata: {
    baseUrl: string;
    totalPages: number;
    scrapedAt: string;
    duration: number;
    website: WebsiteMetadata;
    proxy?: ProxyMetadata;  // Included when proxy pooling is used
  };
}
```

### ProxyMetadata

```typescript
interface ProxyMetadata {
  host: string;
  port: number;
  country?: string;  // If geo-targeting was used
}
```

### BatchMetadata

```typescript
interface BatchMetadata {
  totalUrls: number;
  successfulUrls: number;
  failedUrls: number;
  scrapedAt: string;
  totalDuration: number;
  errors?: Array<{ url: string; error: string }>;
}
```

### CrawlResult

```typescript
interface CrawlResult {
  urls: CrawlUrl[];
  scraped?: ScrapeResult;
  metadata: CrawlMetadata;
}
```

### CrawlUrl

```typescript
interface CrawlUrl {
  url: string;
  title: string;
  description: string | null;
}
```

### CrawlMetadata

```typescript
interface CrawlMetadata {
  totalUrls: number;
  maxDepth: number;
  totalDuration: number;
  seedUrl: string;
}
```

### WebsiteMetadata

```typescript
interface WebsiteMetadata {
  title: string | null;
  description: string | null;
  author: string | null;
  language: string | null;
  charset: string | null;
  favicon: string | null;
  image: string | null;
  canonical: string | null;
  keywords: string[] | null;
  robots: string | null;
  themeColor: string | null;
  openGraph: {
    title: string | null;
    description: string | null;
    type: string | null;
    url: string | null;
    image: string | null;
    siteName: string | null;
    locale: string | null;
  } | null;
  twitter: {
    card: string | null;
    site: string | null;
    creator: string | null;
    title: string | null;
    description: string | null;
    image: string | null;
  } | null;
}
```

### ProgressInfo

```typescript
interface ProgressInfo {
  completed: number;
  total: number;
  currentUrl: string;
}
```

---

## Classes

### BrowserPool

Manages a pool of Hero browser instances for efficient scraping.

```typescript
import { BrowserPool } from "@vakra-dev/reader";

const pool = new BrowserPool({ size: 5 });
await pool.initialize();

const result = await pool.withBrowser(async (hero) => {
  await hero.goto("https://example.com");
  return await hero.document.title;
});

await pool.shutdown();
```

#### Constructor

```typescript
new BrowserPool(config?: PoolConfig)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `size` | `number` | `2` | Number of browser instances |
| `retireAfterPages` | `number` | `100` | Recycle after N pages |
| `retireAfterMinutes` | `number` | `30` | Recycle after N minutes |
| `maxQueueSize` | `number` | `100` | Maximum pending requests |
| `healthCheckIntervalMs` | `number` | `300000` | Health check interval |

#### Methods

##### initialize()

Initialize the browser pool.

```typescript
await pool.initialize(): Promise<void>
```

##### withBrowser(fn)

Execute a function with an acquired browser, automatically releasing it after.

```typescript
await pool.withBrowser<T>(fn: (hero: Hero) => Promise<T>): Promise<T>
```

##### acquire()

Manually acquire a browser instance. Must be paired with `release()`.

```typescript
const hero = await pool.acquire(): Promise<Hero>
```

##### release(hero)

Release a browser instance back to the pool.

```typescript
await pool.release(hero: Hero): Promise<void>
```

##### healthCheck()

Check the health of all pool instances.

```typescript
const health = await pool.healthCheck(): Promise<HealthCheckResult>
```

##### getStats()

Get current pool statistics.

```typescript
const stats = pool.getStats(): PoolStats
```

##### shutdown()

Shutdown all browser instances.

```typescript
await pool.shutdown(): Promise<void>
```

---

## Cloudflare Functions

### detectChallenge(hero)

Detect if a Cloudflare challenge is present on the current page.

```typescript
import { detectChallenge } from "@vakra-dev/reader";

const detection = await detectChallenge(hero);

if (detection.isChallenge) {
  console.log("Challenge type:", detection.type);
  console.log("Signals:", detection.signals);
}
```

#### Returns

```typescript
interface ChallengeDetection {
  isChallenge: boolean;
  type: "js_challenge" | "turnstile" | "captcha" | "blocked" | null;
  signals: Array<{
    type: "dom" | "text" | "url";
    value: string;
  }>;
}
```

---

### waitForChallengeResolution(hero, options)

Wait for a Cloudflare challenge to be resolved.

```typescript
import { waitForChallengeResolution } from "@vakra-dev/reader";

const result = await waitForChallengeResolution(hero, {
  maxWaitMs: 45000,
  pollIntervalMs: 500,
  verbose: true,
  initialUrl: await hero.url,
});

if (result.resolved) {
  console.log(`Resolved via ${result.method} in ${result.waitedMs}ms`);
}
```

#### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `maxWaitMs` | `number` | `45000` | Maximum wait time |
| `pollIntervalMs` | `number` | `500` | Polling interval |
| `verbose` | `boolean` | `false` | Enable logging |
| `initialUrl` | `string` | - | Starting URL for redirect detection |

#### Returns

```typescript
interface ChallengeResolutionResult {
  resolved: boolean;
  method?: "redirect" | "element_removal";
  waitedMs: number;
}
```

---

## Formatter Functions

### formatToMarkdown(pages, baseUrl, scrapedAt, duration, metadata?)

Convert scraped pages to Markdown format.

```typescript
import { formatToMarkdown } from "@vakra-dev/reader";

const markdown = formatToMarkdown(
  pages,
  "https://example.com",
  new Date().toISOString(),
  1500,
  metadata
);
```

---

### formatToHTML(pages, baseUrl, scrapedAt, duration, metadata?)

Convert scraped pages to a complete HTML document.

```typescript
import { formatToHTML } from "@vakra-dev/reader";

const html = formatToHTML(
  pages,
  "https://example.com",
  new Date().toISOString(),
  1500,
  metadata
);
```

---

### formatToJson(pages, baseUrl, scrapedAt, duration, metadata?)

Convert scraped pages to structured JSON.

```typescript
import { formatToJson } from "@vakra-dev/reader";

const json = formatToJson(
  pages,
  "https://example.com",
  new Date().toISOString(),
  1500,
  metadata
);
```

---

### formatToText(pages, baseUrl, scrapedAt, duration, metadata?)

Convert scraped pages to plain text.

```typescript
import { formatToText } from "@vakra-dev/reader";

const text = formatToText(
  pages,
  "https://example.com",
  new Date().toISOString(),
  1500,
  metadata
);
```

---

## Utility Functions

### cleanContent(html)

Remove navigation, ads, scripts, and other non-content elements from HTML.

```typescript
import { cleanContent } from "@vakra-dev/reader";

const cleanHtml = cleanContent(rawHtml);
```

---

### extractMetadata(html)

Extract metadata from HTML including Open Graph and Twitter cards.

```typescript
import { extractMetadata } from "@vakra-dev/reader";

const metadata = extractMetadata(html);
console.log(metadata.title);
console.log(metadata.openGraph?.image);
```

---

## Default Values

```typescript
const DEFAULT_OPTIONS = {
  formats: ["markdown"],
  includeMetadata: true,
  timeoutMs: 30000,
  includePatterns: [],
  excludePatterns: [],
  batchConcurrency: 1,
  batchTimeoutMs: 300000,
  maxRetries: 2,
  verbose: false,
  showChrome: false,
};

const DEFAULT_CRAWL_OPTIONS = {
  depth: 1,
  maxPages: 20,
  scrape: false,
  delayMs: 1000,
  formats: ["markdown", "html"],
  scrapeConcurrency: 2,
  verbose: false,
  showChrome: false,
};

const DEFAULT_POOL_CONFIG = {
  size: 2,
  retireAfterPages: 100,
  retireAfterMinutes: 30,
  maxQueueSize: 100,
  healthCheckIntervalMs: 300000,
};
```

---

## See Also

- [Getting Started](getting-started.md) - Quick start guide
- [Architecture](architecture.md) - System design
- [Browser Pool Guide](guides/browser-pool.md) - Pool management
- [Cloudflare Bypass Guide](guides/cloudflare-bypass.md) - Challenge handling
```

## File: `docs/architecture.md`
```markdown
# Architecture

This document describes the internal architecture of Reader, helping contributors understand how the system works.

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Public API                                │
│                   scrape() / crawl()                             │
└─────────────────────────────┬───────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
        ┌─────▼─────┐                   ┌─────▼─────┐
        │  Scraper  │                   │  Crawler  │
        │  Class    │                   │  Class    │
        └─────┬─────┘                   └─────┬─────┘
              │                               │
              └───────────────┬───────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   BrowserPool     │
                    │   (Hero Manager)  │
                    └─────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
┌─────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
│   Hero Config    │ │   Cloudflare    │ │   Formatters    │
│ (TLS, DNS, etc.) │ │   Detection     │ │ (MD, HTML, etc) │
└──────────────────┘ └─────────────────┘ └─────────────────┘
```

## Directory Structure

```
src/
├── index.ts              # Public API exports
├── scraper.ts            # Scraper class - main scraping logic
├── crawler.ts            # Crawler class - link discovery + scraping
├── types.ts              # ScrapeOptions, ScrapeResult, etc.
├── crawl-types.ts        # CrawlOptions, CrawlResult, etc.
│
├── browser/
│   ├── pool.ts           # BrowserPool - manages Hero instances
│   ├── hero-config.ts    # Hero configuration (TLS, DNS, viewport)
│   └── types.ts          # IBrowserPool, PoolConfig, PoolStats
│
├── cloudflare/
│   ├── detector.ts       # detectChallenge() - DOM/text matching
│   ├── handler.ts        # waitForChallengeResolution() - polling
│   └── types.ts          # ChallengeDetection, ResolutionResult
│
├── formatters/
│   ├── markdown.ts       # formatToMarkdown() - uses supermarkdown
│   ├── html.ts           # formatToHTML() - full HTML document
│   ├── json.ts           # formatToJson() - structured JSON
│   ├── text.ts           # formatToText() - plain text
│   └── index.ts          # Re-exports all formatters
│
├── utils/
│   ├── content-cleaner.ts    # cleanContent() - removes nav, ads
│   ├── metadata-extractor.ts # extractMetadata() - OG tags, etc.
│   ├── url-helpers.ts        # URL validation, normalization
│   ├── rate-limiter.ts       # Simple delay-based rate limiting
│   └── logger.ts             # Pino logger with pretty print
│
├── proxy/
│   └── config.ts         # createProxyUrl(), parseProxyUrl()
│
└── cli/
    └── index.ts          # CLI using Commander.js
```

## Core Components

### Scraper

The `Scraper` class (`src/scraper.ts`) handles URL scraping:

```typescript
class Scraper {
  constructor(options: ScrapeOptions) { ... }

  async scrape(): Promise<ScrapeResult> {
    // 1. Initialize browser pool
    // 2. Process URLs with concurrency control (p-limit)
    // 3. For each URL: fetch, detect challenges, extract content
    // 4. Format to requested output formats
    // 5. Aggregate results and metadata
  }

  private async scrapeSingleUrl(url: string): Promise<WebsiteScrapeResult> {
    // 1. Acquire browser from pool
    // 2. Navigate to URL
    // 3. Detect Cloudflare challenge
    // 4. Wait for resolution if needed
    // 5. Extract HTML and metadata
    // 6. Clean content
    // 7. Format to outputs
    // 8. Release browser to pool
  }
}
```

**Key design decisions:**

- Uses `p-limit` for concurrency control
- Each URL gets its own browser instance from the pool
- Cloudflare detection runs before content extraction
- All formatters run in parallel for each URL

### Crawler

The `Crawler` class (`src/crawler.ts`) discovers links:

```typescript
class Crawler {
  async crawl(): Promise<CrawlResult> {
    // BFS (Breadth-First Search) algorithm
    // 1. Start with seed URL at depth 0
    // 2. Fetch page, extract links
    // 3. Filter links (same domain, patterns)
    // 4. Add to queue with depth + 1
    // 5. Repeat until maxPages or maxDepth
    // 6. Optionally scrape discovered URLs
  }
}
```

**Key design decisions:**

- BFS ensures shallow pages are discovered first
- Respects `maxPages` and `depth` limits
- Optional scraping reuses the Scraper class
- Delay between requests for rate limiting

### Browser Pool

The `BrowserPool` class (`src/browser/pool.ts`) manages Hero instances:

```typescript
class BrowserPool {
  private instances: HeroInstance[];
  private available: HeroInstance[];
  private queue: PendingRequest[];

  async initialize(): Promise<void> { ... }
  async acquire(): Promise<Hero> { ... }
  async release(hero: Hero): Promise<void> { ... }

  async withBrowser<T>(fn: (hero: Hero) => Promise<T>): Promise<T> {
    const hero = await this.acquire();
    try {
      return await fn(hero);
    } finally {
      await this.release(hero);
    }
  }
}
```

**Pool lifecycle:**

1. **Initialize** - Create `size` Hero instances
2. **Acquire** - Get available instance or queue the request
3. **Use** - Execute scraping logic
4. **Release** - Return to pool or recycle if stale
5. **Recycle** - Close old instance, create new one
6. **Shutdown** - Close all instances

**Recycling triggers:**

- After N pages (default: 100)
- After N minutes (default: 30)
- On health check failure

### Cloudflare Detection

Detection happens in two phases:

**1. Challenge Detection** (`src/cloudflare/detector.ts`):

```typescript
async function detectChallenge(hero: Hero): Promise<ChallengeDetection> {
  // Check DOM for challenge elements
  const signals = [];

  // CSS selectors that indicate challenges
  if (await hero.document.querySelector("#challenge-form")) {
    signals.push({ type: "dom", selector: "#challenge-form" });
  }

  // Text patterns that indicate challenges
  const bodyText = await hero.document.body.textContent;
  if (bodyText.includes("checking your browser")) {
    signals.push({ type: "text", pattern: "checking your browser" });
  }

  return {
    isChallenge: signals.length > 0,
    type: determineType(signals),
    signals,
  };
}
```

**2. Challenge Resolution** (`src/cloudflare/handler.ts`):

```typescript
async function waitForChallengeResolution(
  hero: Hero,
  options: ResolutionOptions
): Promise<ResolutionResult> {
  const startTime = Date.now();

  while (Date.now() - startTime < options.maxWaitMs) {
    // Check if URL changed (redirect after challenge)
    if ((await hero.url) !== options.initialUrl) {
      return { resolved: true, method: "redirect" };
    }

    // Check if challenge elements disappeared
    const detection = await detectChallenge(hero);
    if (!detection.isChallenge) {
      return { resolved: true, method: "element_removal" };
    }

    await sleep(options.pollIntervalMs);
  }

  return { resolved: false };
}
```

### Formatters

Each formatter transforms scraped pages into a specific format:

| Formatter | Input | Output |
|-----------|-------|--------|
| `formatToMarkdown` | Pages, metadata | Markdown document with frontmatter |
| `formatToHTML` | Pages, metadata | Complete HTML document with CSS |
| `formatToJson` | Pages, metadata | Structured JSON object |
| `formatToText` | Pages, metadata | Plain text extraction |

**Markdown formatter** uses [supermarkdown](https://github.com/vakra-dev/supermarkdown) - a high-performance Rust-based HTML-to-Markdown converter with full GFM support.

## Data Flow

### Scrape Request Flow

```
scrape({ urls: ["https://example.com"], formats: ["markdown"] })
  │
  ├─► Scraper.scrape()
  │     │
  │     ├─► BrowserPool.initialize(size=concurrency)
  │     │
  │     ├─► For each URL (controlled by p-limit):
  │     │     │
  │     │     ├─► pool.withBrowser(async hero => {
  │     │     │     │
  │     │     │     ├─► hero.goto(url)
  │     │     │     │
  │     │     │     ├─► detectChallenge(hero)
  │     │     │     │     └─► Returns { isChallenge, type, signals }
  │     │     │     │
  │     │     │     ├─► if (isChallenge):
  │     │     │     │     └─► waitForChallengeResolution(hero)
  │     │     │     │
  │     │     │     ├─► Extract title, HTML
  │     │     │     │
  │     │     │     ├─► cleanContent(html)
  │     │     │     │     └─► Remove nav, ads, scripts
  │     │     │     │
  │     │     │     ├─► extractMetadata(html)
  │     │     │     │     └─► OG tags, Twitter cards, etc.
  │     │     │     │
  │     │     │     └─► Format to requested formats
  │     │     │   })
  │     │     │
  │     │     └─► Add to results array
  │     │
  │     ├─► pool.shutdown()
  │     │
  │     └─► Return ScrapeResult { data[], batchMetadata }
  │
  └─► Result returned to caller
```

### Crawl Request Flow

```
crawl({ url: "https://example.com", depth: 2, scrape: true })
  │
  ├─► Crawler.crawl()
  │     │
  │     ├─► Initialize queue with seed URL at depth 0
  │     │
  │     ├─► BFS loop (while queue not empty && pages < maxPages):
  │     │     │
  │     │     ├─► Dequeue next URL
  │     │     │
  │     │     ├─► Fetch page with Hero
  │     │     │
  │     │     ├─► Extract links via regex
  │     │     │
  │     │     ├─► Filter links:
  │     │     │     ├─► Same domain only
  │     │     │     ├─► Match includePatterns
  │     │     │     └─► Exclude excludePatterns
  │     │     │
  │     │     ├─► Add new links to queue with depth + 1
  │     │     │
  │     │     ├─► Rate limit (delay between requests)
  │     │     │
  │     │     └─► Add to discovered URLs
  │     │
  │     ├─► If scrape=true:
  │     │     └─► scrape({ urls: discoveredUrls })
  │     │
  │     └─► Return CrawlResult { urls[], scraped?, metadata }
  │
  └─► Result returned to caller
```

## Design Decisions

### Why Hero?

[Ulixee Hero](https://ulixee.org/) was chosen for:

1. **Stealth** - Advanced TLS fingerprinting and anti-detection
2. **Speed** - Optimized for headless automation
3. **API** - Clean async/await interface
4. **Stability** - Production-tested at scale

### Pool vs Per-Request Browsers

We use a pool because:

- Browser startup is slow (~2-3 seconds)
- Memory overhead per browser is high
- Connection reuse improves performance

Trade-off: Stale browsers can accumulate state, so we recycle them periodically.

### Cloudflare Detection Strategy

Multi-signal approach because:

- No single indicator is 100% reliable
- Cloudflare changes their challenge pages
- Different challenge types have different signatures

Detection signals include:
- DOM elements (`#challenge-form`, `.cf-browser-verification`)
- Text patterns ("checking your browser", "ray id")
- URL patterns (`/cdn-cgi/challenge-platform/`)
- HTTP status codes

### Content Cleaning

We clean HTML before formatting because:

- Navigation, ads, scripts bloat output
- LLMs perform better with focused content
- Reduces token usage

Cleaning removes:
- `<script>`, `<style>` tags
- Navigation elements
- Footer/sidebar content
- Ad containers
- Hidden elements

## Extension Points

### Adding a New Formatter

1. Create `src/formatters/newformat.ts`:
   ```typescript
   export function formatToNewFormat(
     pages: Page[],
     baseUrl: string,
     scrapedAt: string,
     duration: number,
     metadata?: WebsiteMetadata
   ): string {
     // Your formatting logic
   }
   ```

2. Export from `src/formatters/index.ts`

3. Add to format type in `src/types.ts`:
   ```typescript
   formats?: Array<"markdown" | "html" | "json" | "text" | "newformat">
   ```

4. Call formatter in `src/scraper.ts`

### Adding a New ScrapeOption

1. Add to `ScrapeOptions` in `src/types.ts`
2. Add default in `DEFAULT_OPTIONS`
3. Use in `Scraper` class via `this.options.newOption`
4. Add CLI flag in `src/cli/index.ts` if needed

### Modifying Cloudflare Detection

- Detection patterns: `src/cloudflare/detector.ts`
- Resolution logic: `src/cloudflare/handler.ts`

## Testing

Currently testing is manual. Key test scenarios:

1. **Basic scraping** - example.com
2. **Cloudflare-protected sites** - Sites with JS challenges
3. **Batch scraping** - Multiple URLs with concurrency
4. **Crawling** - Multi-page discovery
5. **All output formats** - Verify each formatter

## Related Guides

- [Browser Pool](guides/browser-pool.md) - Deep dive into pool management
- [Cloudflare Bypass](guides/cloudflare-bypass.md) - Understanding antibot bypass
- [Production Server](deployment/production-server.md) - Shared Hero Core pattern
```

## File: `docs/getting-started.md`
```markdown
# Getting Started

This guide walks you through setting up Reader, verifying your installation, and running your first scrape.

## Prerequisites

- **Node.js >= 18** (v22 recommended)
- **npm** package manager

> **Note:** The Hero browser runtime requires Node.js. Always run your scripts with `node` or `npx tsx`.

## Installation

### From npm

```bash
npm install @vakra-dev/reader
```

### From source

```bash
git clone https://github.com/vakra-dev/reader.git
cd reader
npm install
npm run build
```

## Verify Installation

### Test the CLI

```bash
npx reader scrape https://example.com
```

You should see markdown output of the example.com page.

### Test the API

Create a file `test-scrape.ts`:

```typescript
import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  const reader = new ReaderClient();

  const result = await reader.scrape({
    urls: ["https://example.com"],
    formats: ["markdown"],
  });

  console.log("Success:", result.batchMetadata.successfulUrls === 1);
  console.log("Content length:", result.data[0].markdown?.length);

  await reader.close();
}

main().catch(console.error);
```

Run it:

```bash
npx tsx test-scrape.ts
```

## Your First Scrape

### Single URL

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://news.ycombinator.com"],
  formats: ["markdown", "text"],
});

// Access the markdown content
console.log(result.data[0].markdown);

// Access metadata
console.log("Title:", result.data[0].metadata.website.title);
console.log("Duration:", result.data[0].metadata.duration, "ms");

await reader.close();
```

### Multiple URLs

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: [
    "https://example.com",
    "https://example.org",
    "https://example.net",
  ],
  formats: ["markdown"],
  batchConcurrency: 3,
  onProgress: ({ completed, total, currentUrl }) => {
    console.log(`[${completed}/${total}] Scraping: ${currentUrl}`);
  },
});

console.log(`Scraped ${result.batchMetadata.successfulUrls} URLs`);
console.log(`Failed: ${result.batchMetadata.failedUrls}`);

await reader.close();
```

### Crawl a Website

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  maxPages: 10,
  scrape: true,
});

console.log(`Discovered ${result.urls.length} URLs:`);
result.urls.forEach((page) => {
  console.log(`  - ${page.title}: ${page.url}`);
});

if (result.scraped) {
  console.log(`\nScraped ${result.scraped.batchMetadata.successfulUrls} pages`);
}

await reader.close();
```

## Understanding the Output

### ScrapeResult Structure

```typescript
interface ScrapeResult {
  // Array of scraped websites (one per URL)
  data: WebsiteScrapeResult[];

  // Metadata about the batch operation
  batchMetadata: {
    totalUrls: number;
    successfulUrls: number;
    failedUrls: number;
    scrapedAt: string;      // ISO timestamp
    totalDuration: number;  // milliseconds
    errors?: Array<{ url: string; error: string }>;
  };
}

interface WebsiteScrapeResult {
  // Content in requested formats
  markdown?: string;
  html?: string;
  json?: string;
  text?: string;

  // Metadata about this specific scrape
  metadata: {
    baseUrl: string;
    totalPages: number;
    scrapedAt: string;
    duration: number;
    website: WebsiteMetadata;  // Title, description, OG tags, etc.
  };
}
```

### CrawlResult Structure

```typescript
interface CrawlResult {
  // Discovered URLs with basic info
  urls: Array<{
    url: string;
    title: string;
    description: string | null;
  }>;

  // Full scrape results (only when scrape: true)
  scraped?: ScrapeResult;

  // Crawl operation metadata
  metadata: {
    totalUrls: number;
    maxDepth: number;
    totalDuration: number;
    seedUrl: string;
  };
}
```

## CLI Quick Reference

### Daemon Mode (Recommended for Multiple Requests)

```bash
# Start daemon (once, in a separate terminal or background)
npx reader start --pool-size 5

# Scrape (auto-detects and uses daemon if running)
npx reader scrape https://example.com

# Crawl (auto-detects and uses daemon if running)
npx reader crawl https://example.com -d 2

# Check daemon status
npx reader status

# Stop daemon
npx reader stop

# Force standalone mode (bypass daemon)
npx reader scrape https://example.com --standalone
```

### Scraping

```bash
# Scrape a URL to markdown
npx reader scrape https://example.com

# Scrape with multiple formats
npx reader scrape https://example.com -f markdown,text,json

# Scrape multiple URLs concurrently
npx reader scrape url1 url2 url3 -c 3

# Save output to file
npx reader scrape https://example.com -o output.md

# Enable verbose logging
npx reader scrape https://example.com -v

# Show browser window (debugging)
npx reader scrape https://example.com --show-chrome
```

### Crawling

```bash
# Crawl a website
npx reader crawl https://example.com -d 2 -m 20

# Crawl and scrape content
npx reader crawl https://example.com -d 2 --scrape
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `LOG_LEVEL` | Logging level: `debug`, `info`, `warn`, `error` (default: `info`) |
| `NODE_ENV` | Set to `development` for pretty-printed logs |

## Common Issues

### "Chrome/Chromium not found"

Hero automatically downloads Chrome on first run. If this fails:

```bash
# Manually install Chrome dependencies (Ubuntu/Debian)
sudo apt-get install -y chromium-browser

# Or use the system Chrome
export CHROME_PATH=/usr/bin/chromium-browser
```

### "ECONNREFUSED" errors

This usually means the target site is blocking requests. Try:

1. Use a proxy: `--proxy http://user:pass@host:port`
2. Add delays between requests: `--delay 2000`
3. Use verbose mode to see what's happening: `-v`

### ESM/CommonJS issues

Reader is ESM-only. Make sure your `package.json` has:

```json
{
  "type": "module"
}
```

Or use the `.mjs` extension for your files.

## Next Steps

Based on your use case, explore these guides:

| Use Case | Guide |
|----------|-------|
| Understanding Cloudflare bypass | [Cloudflare Bypass](guides/cloudflare-bypass.md) |
| Setting up proxies | [Proxy Configuration](guides/proxy-configuration.md) |
| Production server deployment | [Production Server](deployment/production-server.md) |
| High-volume scraping | [Browser Pool](guides/browser-pool.md) |
| Docker deployment | [Docker](deployment/docker.md) |
| Serverless deployment | [Serverless](deployment/serverless.md) |

## Need Help?

- Check the [Troubleshooting Guide](troubleshooting.md)
- Browse [Examples](../examples/)
- Open an issue on [GitHub](https://github.com/vakra-dev/reader/issues)
```

## File: `docs/troubleshooting.md`
```markdown
# Troubleshooting

This guide covers common issues and their solutions when using Reader.

## Quick Diagnostics

Before diving into specific issues, try these debugging steps:

```bash
# Enable verbose logging
npx reader scrape https://example.com -v

# Show the browser window to see what's happening
npx reader scrape https://example.com --show-chrome

# Check Node.js version (should be >= 18)
node --version
```

## Common Errors

### Chrome/Chromium Not Found

**Error:**
```
Error: Could not find Chrome installation
```

**Cause:** Hero needs Chrome/Chromium to run. It tries to download it automatically on first run.

**Solutions:**

1. **Let Hero download Chrome:**
   ```bash
   # Clear any cached downloads and try again
   rm -rf ~/.cache/ulixee
   npx reader scrape https://example.com
   ```

2. **Install Chrome manually (Ubuntu/Debian):**
   ```bash
   sudo apt-get update
   sudo apt-get install -y chromium-browser
   ```

3. **Install Chrome manually (macOS):**
   ```bash
   brew install --cask chromium
   ```

4. **Point to existing Chrome:**
   ```bash
   export CHROME_PATH=/usr/bin/chromium-browser
   # or on macOS
   export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   ```

### Connection Refused (ECONNREFUSED)

**Error:**
```
Error: connect ECONNREFUSED 127.0.0.1:9222
```

**Cause:** Hero couldn't start or connect to Chrome.

**Solutions:**

1. **Check if Chrome is running:**
   ```bash
   ps aux | grep chrome
   # Kill any zombie processes
   pkill -f chrome
   ```

2. **Check for port conflicts:**
   ```bash
   lsof -i :9222
   ```

3. **Try with a fresh browser instance:**
   ```typescript
   const reader = new ReaderClient({ showChrome: true });
   const result = await reader.scrape({
     urls: ["https://example.com"],
   });
   await reader.close();
   ```

### Request Timeout

**Error:**
```
Error: Navigation timeout of 30000 ms exceeded
```

**Cause:** The page took too long to load, or Cloudflare challenge took too long to resolve.

**Solutions:**

1. **Increase timeout:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.scrape({
     urls: ["https://example.com"],
     timeoutMs: 60000,  // 60 seconds
   });
   await reader.close();
   ```

2. **For batch operations, increase batch timeout:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.scrape({
     urls: [...manyUrls],
     batchTimeoutMs: 600000,  // 10 minutes total
   });
   await reader.close();
   ```

3. **Check if the site is accessible:**
   ```bash
   curl -I https://example.com
   ```

### Cloudflare Block (403/1020)

**Error:**
```
Error: Access denied (Error code 1020)
```

**Cause:** Cloudflare detected automated access and blocked the request.

**Solutions:**

1. **Use a proxy:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.scrape({
     urls: ["https://example.com"],
     proxy: {
       type: "residential",
       host: "proxy.example.com",
       port: 8080,
       username: "username",
       password: "password",
     },
   });
   await reader.close();
   ```

2. **Add delays between requests:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.crawl({
     url: "https://example.com",
     delayMs: 3000,  // 3 seconds between requests
   });
   await reader.close();
   ```

3. **Try a different user agent:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.scrape({
     urls: ["https://example.com"],
     userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
   });
   await reader.close();
   ```

4. **Enable verbose mode to see challenge detection:**
   ```typescript
   const reader = new ReaderClient({ verbose: true, showChrome: true });
   const result = await reader.scrape({
     urls: ["https://example.com"],
   });
   await reader.close();
   ```

### Memory Issues

**Error:**
```
FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
```

**Cause:** Too many browser instances or large pages consuming memory.

**Solutions:**

1. **Reduce concurrency:**
   ```typescript
   const reader = new ReaderClient();
   const result = await reader.scrape({
     urls: [...manyUrls],
     batchConcurrency: 2,  // Lower concurrency
   });
   await reader.close();
   ```

2. **Increase Node.js memory:**
   ```bash
   NODE_OPTIONS="--max-old-space-size=4096" npx reader scrape ...
   ```

3. **Use browser pool recycling (happens automatically, but you can tune it):**
   ```typescript
   import { BrowserPool } from "@vakra-dev/reader";

   const pool = new BrowserPool({
     size: 2,
     retireAfterPages: 50,  // Recycle browsers more frequently
   });
   ```

### ESM/CommonJS Issues

**Error:**
```
SyntaxError: Cannot use import statement outside a module
```

**Cause:** Reader is ESM-only, but your project is using CommonJS.

**Solutions:**

1. **Add to package.json:**
   ```json
   {
     "type": "module"
   }
   ```

2. **Or use .mjs extension:**
   ```bash
   mv script.js script.mjs
   node script.mjs
   ```

3. **Or use dynamic import in CommonJS:**
   ```javascript
   // script.cjs
   async function main() {
     const { scrape } = await import("@vakra-dev/reader");
     // ...
   }
   main();
   ```

### "Bun runtime not supported"

**Error:**
```
Error: Hero doesn't work with Bun runtime
```

**Cause:** Hero requires Node.js runtime and is not compatible with Bun.

**Solution:** Use Node.js to run your scripts:

```bash
# Use npx tsx
npx tsx script.ts

# or node with loader
node --loader tsx script.ts
```

## Debugging Tips

### Enable Verbose Logging

```typescript
const reader = new ReaderClient({ verbose: true });
const result = await reader.scrape({
  urls: ["https://example.com"],
});
await reader.close();
```

This shows:
- Cloudflare challenge detection
- Page navigation events
- Timing information
- Error details

### Show Browser Window

```typescript
const reader = new ReaderClient({ showChrome: true });
const result = await reader.scrape({
  urls: ["https://example.com"],
});
await reader.close();
```

This opens a visible Chrome window so you can see:
- What the page looks like
- Cloudflare challenges appearing
- JavaScript errors in DevTools

### Check Challenge Detection

```typescript
import { detectChallenge } from "@vakra-dev/reader";

// In your scraping logic
const detection = await detectChallenge(hero);
console.log("Challenge detected:", detection.isChallenge);
console.log("Challenge type:", detection.type);
console.log("Detection signals:", detection.signals);
```

### Log Progress

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: manyUrls,
  batchConcurrency: 3,
  onProgress: ({ completed, total, currentUrl }) => {
    console.log(`[${completed}/${total}] ${currentUrl}`);
  },
});
await reader.close();
```

## Performance Issues

### Slow Scraping

1. **Increase concurrency (if resources allow):**
   ```typescript
   batchConcurrency: 5  // Default is 1
   ```

2. **Use browser pool for repeated scrapes:**
   ```typescript
   import { BrowserPool } from "@vakra-dev/reader";

   const pool = new BrowserPool({ size: 5 });
   await pool.initialize();

   // Reuse pool for multiple operations
   for (const url of urls) {
     await pool.withBrowser(async (hero) => {
       await hero.goto(url);
       // ...
     });
   }

   await pool.shutdown();
   ```

3. **Use shared Hero Core for production:**
   See [Production Server Guide](deployment/production-server.md)

### High Memory Usage

1. **Reduce pool size:**
   ```typescript
   const pool = new BrowserPool({ size: 2 });
   ```

2. **Enable more aggressive recycling:**
   ```typescript
   const pool = new BrowserPool({
     size: 3,
     retireAfterPages: 30,      // Default: 100
     retireAfterMinutes: 15,    // Default: 30
   });
   ```

3. **Process URLs in smaller batches:**
   ```typescript
   const reader = new ReaderClient();
   const batchSize = 10;
   for (let i = 0; i < urls.length; i += batchSize) {
     const batch = urls.slice(i, i + batchSize);
     await reader.scrape({ urls: batch, batchConcurrency: 3 });
     // Allow garbage collection between batches
     await new Promise(r => setTimeout(r, 1000));
   }
   await reader.close();
   ```

## Site-Specific Issues

### JavaScript-Heavy Sites

Some sites require waiting for JavaScript to render:

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://spa-site.com"],
  waitForSelector: ".main-content",  // Wait for this element
  timeoutMs: 60000,
});
await reader.close();
```

### Sites with Infinite Scroll

Crawling may not discover all content. Consider:

1. Limiting depth and using specific URL patterns
2. Using the API directly with custom scroll logic

### Login-Protected Content

Reader doesn't handle authentication directly. Options:

1. Use cookies from an authenticated session
2. Build custom authentication logic using the Browser Pool
3. Use a headless browser automation tool for login, then Reader for scraping

## Getting More Help

1. **Check the logs** with `-v` flag
2. **Search existing issues** on [GitHub](https://github.com/vakra-dev/reader/issues)
3. **Open a new issue** with:
   - Node.js version
   - Reader version
   - Operating system
   - Error message and stack trace
   - Minimal reproduction steps

## Related Guides

- [Getting Started](getting-started.md)
- [Cloudflare Bypass](guides/cloudflare-bypass.md)
- [Browser Pool](guides/browser-pool.md)
- [Proxy Configuration](guides/proxy-configuration.md)
```

## File: `docs/assets/demo.tape`
```
# VHS tape file for Reader demo GIF
# Run: vhs docs/assets/demo.tape

Output docs/assets/demo.gif

Set FontSize 16
Set Width 900
Set Height 500
Set Theme "Catppuccin Mocha"
Set Padding 20

# Scrape a URL and extract the markdown
Type "npx reader scrape https://reader.dev | jq -r '.data[0].markdown' | head -n 12"
Sleep 500ms
Enter
Sleep 3s

# Let output display
Sleep 3s
```

## File: `docs/deployment/docker.md`
```markdown
# Docker Deployment Guide

Deploy Reader in Docker containers.

## Quick Start

### Basic Dockerfile

```dockerfile
# Dockerfile
FROM node:22-slim

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Set Chrome path for Hero
ENV CHROME_PATH=/usr/bin/chromium

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application
COPY . .

# Build if TypeScript
RUN npm run build 2>/dev/null || true

EXPOSE 3000

CMD ["node", "dist/server.js"]
```

### Build and Run

```bash
# Build image
docker build -t reader .

# Run container
docker run -p 3000:3000 reader
```

## Docker Compose

### Basic Setup

```yaml
# docker-compose.yml
version: "3.8"

services:
  reader:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - LOG_LEVEL=info
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 2G
```

### With Redis (for job queues)

```yaml
# docker-compose.yml
version: "3.8"

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.api
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis
    restart: unless-stopped

  worker:
    build:
      context: .
      dockerfile: Dockerfile.worker
    environment:
      - NODE_ENV=production
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 2G
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data
    restart: unless-stopped

volumes:
  redis-data:
```

### Start Services

```bash
# Start all services
docker-compose up -d

# Scale workers
docker-compose up -d --scale worker=5

# View logs
docker-compose logs -f worker

# Stop services
docker-compose down
```

## Optimized Dockerfile

### Multi-stage Build

```dockerfile
# Dockerfile
# Build stage
FROM node:22-slim AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:22-slim

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_PATH=/usr/bin/chromium
ENV NODE_ENV=production

WORKDIR /app

# Copy only production dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy built application
COPY --from=builder /app/dist ./dist

# Non-root user for security
RUN groupadd -r app && useradd -r -g app app
USER app

EXPOSE 3000

CMD ["node", "dist/server.js"]
```

## Configuration

### Environment Variables

```yaml
# docker-compose.yml
services:
  reader:
    environment:
      - NODE_ENV=production
      - PORT=3000
      - LOG_LEVEL=info
      - CHROME_PATH=/usr/bin/chromium
      - MAX_CONCURRENT_REQUESTS=10
      - REQUEST_TIMEOUT_MS=60000
```

### Resource Limits

```yaml
services:
  reader:
    deploy:
      resources:
        limits:
          cpus: "2"
          memory: 4G
        reservations:
          cpus: "1"
          memory: 2G
```

### Health Checks

```yaml
services:
  reader:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## Chrome Configuration

### Sandbox Mode

Chrome requires special configuration in Docker:

```dockerfile
# Add to Dockerfile
ENV CHROME_FLAGS="--no-sandbox --disable-setuid-sandbox"
```

Or configure in Hero:

```typescript
// In your application
const pool = new BrowserPool({
  heroOptions: {
    noChromeSandbox: true,
  },
});
```

### Shared Memory

Chrome needs sufficient shared memory:

```yaml
services:
  reader:
    shm_size: "2gb"
```

Or mount tmpfs:

```yaml
services:
  reader:
    volumes:
      - /dev/shm:/dev/shm
```

## Production Considerations

### Logging

```yaml
services:
  reader:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

### Networking

```yaml
services:
  reader:
    networks:
      - internal
      - external

networks:
  internal:
    internal: true
  external:
```

### Secrets

```yaml
services:
  reader:
    secrets:
      - proxy_credentials

secrets:
  proxy_credentials:
    file: ./secrets/proxy.txt
```

### Volumes for Data

```yaml
services:
  reader:
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
```

## Scaling

### Docker Swarm

```yaml
# docker-stack.yml
version: "3.8"

services:
  reader:
    image: reader:latest
    deploy:
      replicas: 5
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure
    networks:
      - traefik

networks:
  traefik:
    external: true
```

Deploy:

```bash
docker stack deploy -c docker-stack.yml reader
```

### Kubernetes

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reader
spec:
  replicas: 3
  selector:
    matchLabels:
      app: reader
  template:
    metadata:
      labels:
        app: reader
    spec:
      containers:
        - name: reader
          image: reader:latest
          ports:
            - containerPort: 3000
          resources:
            limits:
              memory: "2Gi"
              cpu: "1"
          env:
            - name: NODE_ENV
              value: "production"
---
apiVersion: v1
kind: Service
metadata:
  name: reader
spec:
  selector:
    app: reader
  ports:
    - port: 80
      targetPort: 3000
```

## Troubleshooting

### Chrome Won't Start

```bash
# Check Chrome installation
docker exec -it container_name chromium --version

# Test Chrome manually
docker exec -it container_name chromium --headless --no-sandbox --dump-dom https://example.com
```

### Memory Issues

```yaml
# Increase limits
services:
  reader:
    deploy:
      resources:
        limits:
          memory: 4G
    shm_size: "2gb"
```

### Network Issues

```bash
# Debug networking
docker exec -it container_name curl https://example.com

# Check DNS
docker exec -it container_name nslookup example.com
```

## Complete Example

See [examples/deployment/docker/](../../examples/deployment/docker/) for a complete Docker setup.

## Related Guides

- [Production Server](production-server.md) - Server setup
- [Job Queues](job-queues.md) - Async processing
- [Serverless](serverless.md) - Lambda/Vercel deployment
```

## File: `docs/deployment/job-queues.md`
```markdown
# Job Queues Guide

Use job queues for async scraping at scale with BullMQ.

## Overview

For high-volume scraping, use a job queue to:
- Process requests asynchronously
- Handle retries automatically
- Scale workers independently
- Monitor job progress
- Avoid overwhelming target sites

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   API       │────▶│   Redis     │────▶│   Workers   │
│   Server    │     │   Queue     │     │   (N)       │
└─────────────┘     └─────────────┘     └─────────────┘
       │                                       │
       │         ┌─────────────┐              │
       └────────▶│   Results   │◀─────────────┘
                 │   Store     │
                 └─────────────┘
```

## Setup

### Installation

```bash
npm install bullmq ioredis @vakra-dev/reader
```

### Basic Queue Setup

```typescript
// queue.ts
import { Queue, Worker, Job } from "bullmq";
import { scrape } from "@vakra-dev/reader";

const connection = {
  host: process.env.REDIS_HOST || "localhost",
  port: parseInt(process.env.REDIS_PORT || "6379"),
};

// Create queue
export const scrapeQueue = new Queue("scrape", { connection });

// Job data interface
interface ScrapeJobData {
  urls: string[];
  formats: ("markdown" | "html" | "json" | "text")[];
  callbackUrl?: string;
}

// Add job to queue
export async function enqueueScrape(data: ScrapeJobData) {
  const job = await scrapeQueue.add("scrape", data, {
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 5000,
    },
  });

  return job.id;
}
```

### Worker Process

```typescript
// worker.ts
import { Worker, Job } from "bullmq";
import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";
import { scrape } from "@vakra-dev/reader";

const connection = {
  host: process.env.REDIS_HOST || "localhost",
  port: parseInt(process.env.REDIS_PORT || "6379"),
};

// Shared Hero Core
let heroCore: HeroCore;

async function createConnection() {
  const bridge = new TransportBridge();
  heroCore.addConnection(bridge.transportToClient);
  return new ConnectionToHeroCore(bridge.transportToCore);
}

// Process jobs
const worker = new Worker(
  "scrape",
  async (job: Job) => {
    const { urls, formats } = job.data;

    console.log(`Processing job ${job.id}: ${urls.length} URLs`);

    const result = await scrape({
      urls,
      formats,
      connectionToCore: await createConnection(),
      onProgress: async ({ completed, total }) => {
        await job.updateProgress((completed / total) * 100);
      },
    });

    // Callback if provided
    if (job.data.callbackUrl) {
      await fetch(job.data.callbackUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(result),
      });
    }

    return result;
  },
  {
    connection,
    concurrency: 5,
  }
);

// Event handlers
worker.on("completed", (job) => {
  console.log(`Job ${job.id} completed`);
});

worker.on("failed", (job, err) => {
  console.error(`Job ${job?.id} failed:`, err.message);
});

// Start worker
async function start() {
  heroCore = new HeroCore();
  await heroCore.start();
  console.log("Worker started, waiting for jobs...");
}

// Graceful shutdown
async function shutdown() {
  console.log("Shutting down worker...");
  await worker.close();
  if (heroCore) await heroCore.close();
  process.exit(0);
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);

start().catch(console.error);
```

### API Server

```typescript
// api.ts
import express from "express";
import { scrapeQueue, enqueueScrape } from "./queue";

const app = express();
app.use(express.json());

// Enqueue scrape job
app.post("/scrape", async (req, res) => {
  const { urls, formats, callbackUrl } = req.body;

  const jobId = await enqueueScrape({ urls, formats, callbackUrl });

  res.json({ jobId, status: "queued" });
});

// Get job status
app.get("/job/:id", async (req, res) => {
  const job = await scrapeQueue.getJob(req.params.id);

  if (!job) {
    return res.status(404).json({ error: "Job not found" });
  }

  const state = await job.getState();
  const progress = job.progress;

  res.json({
    id: job.id,
    state,
    progress,
    data: job.data,
    result: job.returnvalue,
    failedReason: job.failedReason,
  });
});

// Get job result
app.get("/job/:id/result", async (req, res) => {
  const job = await scrapeQueue.getJob(req.params.id);

  if (!job) {
    return res.status(404).json({ error: "Job not found" });
  }

  const state = await job.getState();

  if (state !== "completed") {
    return res.status(202).json({ status: state, progress: job.progress });
  }

  res.json(job.returnvalue);
});

app.listen(3000, () => {
  console.log("API server running on port 3000");
});
```

## Job Options

### Retry Configuration

```typescript
await scrapeQueue.add("scrape", data, {
  attempts: 5,
  backoff: {
    type: "exponential",
    delay: 5000,  // 5s, 10s, 20s, 40s, 80s
  },
});
```

### Priority

```typescript
// High priority (lower number = higher priority)
await scrapeQueue.add("scrape", urgentData, { priority: 1 });

// Normal priority
await scrapeQueue.add("scrape", normalData, { priority: 5 });

// Low priority
await scrapeQueue.add("scrape", bulkData, { priority: 10 });
```

### Delayed Jobs

```typescript
// Process after 5 minutes
await scrapeQueue.add("scrape", data, {
  delay: 5 * 60 * 1000,
});
```

### Rate Limiting

```typescript
// Max 10 jobs per minute
const worker = new Worker("scrape", processor, {
  limiter: {
    max: 10,
    duration: 60000,
  },
});
```

## Scaling Workers

### Multiple Workers

Run multiple worker processes:

```bash
# Terminal 1
WORKER_ID=1 npx tsx worker.ts

# Terminal 2
WORKER_ID=2 npx tsx worker.ts

# Terminal 3
WORKER_ID=3 npx tsx worker.ts
```

### Worker Concurrency

```typescript
const worker = new Worker("scrape", processor, {
  connection,
  concurrency: 5,  // Process 5 jobs simultaneously
});
```

### Auto-Scaling

```typescript
// Scale based on queue depth
async function checkScale() {
  const waiting = await scrapeQueue.getWaitingCount();
  const active = await scrapeQueue.getActiveCount();

  console.log(`Queue: ${waiting} waiting, ${active} active`);

  if (waiting > 100) {
    // Signal to scale up
    await notifyScaleUp();
  }
}

setInterval(checkScale, 30000);
```

## Monitoring

### Queue Dashboard (Bull Board)

```typescript
import { createBullBoard } from "@bull-board/api";
import { BullMQAdapter } from "@bull-board/api/bullMQAdapter";
import { ExpressAdapter } from "@bull-board/express";

const serverAdapter = new ExpressAdapter();
serverAdapter.setBasePath("/admin/queues");

createBullBoard({
  queues: [new BullMQAdapter(scrapeQueue)],
  serverAdapter,
});

app.use("/admin/queues", serverAdapter.getRouter());
```

### Metrics

```typescript
// Queue stats
async function getQueueStats() {
  return {
    waiting: await scrapeQueue.getWaitingCount(),
    active: await scrapeQueue.getActiveCount(),
    completed: await scrapeQueue.getCompletedCount(),
    failed: await scrapeQueue.getFailedCount(),
    delayed: await scrapeQueue.getDelayedCount(),
  };
}

app.get("/stats", async (req, res) => {
  res.json(await getQueueStats());
});
```

### Events

```typescript
// Listen to queue events
scrapeQueue.on("completed", (job) => {
  metrics.increment("jobs.completed");
  metrics.timing("jobs.duration", job.processedOn - job.timestamp);
});

scrapeQueue.on("failed", (job, err) => {
  metrics.increment("jobs.failed");
  alerting.notify(`Job ${job.id} failed: ${err.message}`);
});
```

## Error Handling

### Retry Strategy

```typescript
const worker = new Worker(
  "scrape",
  async (job) => {
    try {
      return await scrape(job.data);
    } catch (error) {
      // Don't retry on certain errors
      if (error.message.includes("Invalid URL")) {
        throw new Error(`Permanent failure: ${error.message}`);
      }
      // Retry on transient errors
      throw error;
    }
  },
  {
    connection,
    settings: {
      backoffStrategy: (attemptsMade) => {
        // Custom backoff: 5s, 30s, 2m, 10m
        const delays = [5000, 30000, 120000, 600000];
        return delays[Math.min(attemptsMade - 1, delays.length - 1)];
      },
    },
  }
);
```

### Dead Letter Queue

```typescript
// Move failed jobs to DLQ after all retries
await scrapeQueue.add("scrape", data, {
  attempts: 3,
  removeOnFail: {
    age: 24 * 3600,  // Keep for 24 hours
  },
});

// Process DLQ manually
const failedJobs = await scrapeQueue.getFailed();
for (const job of failedJobs) {
  console.log(`Failed job ${job.id}: ${job.failedReason}`);
  // Optionally retry
  await job.retry();
}
```

## Complete Example

```typescript
// complete-example.ts
import { Queue, Worker, Job } from "bullmq";
import express from "express";
import HeroCore from "@ulixee/hero-core";
import { scrape, ScrapeResult } from "@vakra-dev/reader";

const app = express();
app.use(express.json());

// Redis connection
const connection = { host: "localhost", port: 6379 };

// Queue
const scrapeQueue = new Queue("scrape", { connection });

// Shared Hero Core
let heroCore: HeroCore;

// Worker
const worker = new Worker<any, ScrapeResult>(
  "scrape",
  async (job: Job) => {
    const result = await scrape({
      ...job.data,
      connectionToCore: await createConnection(),
    });
    return result;
  },
  { connection, concurrency: 3 }
);

// API endpoints
app.post("/scrape/async", async (req, res) => {
  const job = await scrapeQueue.add("scrape", req.body);
  res.json({ jobId: job.id });
});

app.get("/scrape/:jobId", async (req, res) => {
  const job = await scrapeQueue.getJob(req.params.jobId);
  if (!job) return res.status(404).json({ error: "Not found" });

  const state = await job.getState();
  res.json({
    state,
    progress: job.progress,
    result: state === "completed" ? job.returnvalue : null,
  });
});

// Start
async function start() {
  heroCore = new HeroCore();
  await heroCore.start();

  app.listen(3000, () => console.log("Server running"));
}

start();
```

## Related Guides

- [Production Server](production-server.md) - Basic server setup
- [Docker](docker.md) - Containerized deployment
- [Browser Pool](../guides/browser-pool.md) - Managing browsers
```

## File: `docs/deployment/production-server.md`
```markdown
# Production Server Guide

Deploy Reader as a production-ready API server.

## Overview

For production servers, use a **shared Hero Core** pattern instead of spawning individual Chrome processes per request. This dramatically reduces resource usage and improves performance.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                Express Server                    │
├─────────────────────────────────────────────────┤
│              Shared Hero Core                    │
│         (Single Chrome Process)                  │
├─────────────────────────────────────────────────┤
│   Browser 1  │  Browser 2  │  Browser 3  │ ...  │
│   (Tab)      │  (Tab)      │  (Tab)      │      │
└─────────────────────────────────────────────────┘
```

**Benefits:**
- Single Chrome process instead of one per request
- Lower memory footprint
- Faster browser creation
- Better resource utilization

## Basic Setup

### Installation

```bash
npm install @vakra-dev/reader express
npm install @ulixee/hero-core @ulixee/net  # For shared Core
```

### Server Code

```typescript
// server.ts
import express from "express";
import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";
import { scrape, crawl } from "@vakra-dev/reader";

const app = express();
app.use(express.json());

// Shared Hero Core - initialized once
let heroCore: HeroCore;

async function createConnection() {
  const bridge = new TransportBridge();
  heroCore.addConnection(bridge.transportToClient);
  return new ConnectionToHeroCore(bridge.transportToCore);
}

// Scrape endpoint
app.post("/scrape", async (req, res) => {
  const { urls, formats = ["markdown"] } = req.body;

  try {
    const result = await scrape({
      urls,
      formats,
      connectionToCore: await createConnection(),
    });

    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

// Crawl endpoint
app.post("/crawl", async (req, res) => {
  const { url, depth = 2, maxPages = 20, scrape: doScrape = false } = req.body;

  try {
    const result = await crawl({
      url,
      depth,
      maxPages,
      scrape: doScrape,
      connectionToCore: await createConnection(),
    });

    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

// Health check
app.get("/health", (req, res) => {
  res.json({ status: "ok", heroCore: heroCore ? "running" : "stopped" });
});

// Start server
async function start() {
  // Initialize shared Hero Core
  heroCore = new HeroCore();
  await heroCore.start();
  console.log("Hero Core started");

  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

// Graceful shutdown
async function shutdown() {
  console.log("Shutting down...");
  if (heroCore) {
    await heroCore.close();
  }
  process.exit(0);
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);

start().catch(console.error);
```

### Run the Server

```bash
npx tsx server.ts
```

### Test Endpoints

```bash
# Scrape
curl -X POST http://localhost:3000/scrape \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com"], "formats": ["markdown"]}'

# Crawl
curl -X POST http://localhost:3000/crawl \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "depth": 2, "scrape": true}'
```

## Production Configuration

### Environment Variables

```bash
# .env
PORT=3000
NODE_ENV=production
LOG_LEVEL=info
MAX_CONCURRENT_REQUESTS=10
REQUEST_TIMEOUT_MS=60000
```

### Request Limits

```typescript
import rateLimit from "express-rate-limit";

// Rate limiting
const limiter = rateLimit({
  windowMs: 60 * 1000,  // 1 minute
  max: 100,             // 100 requests per minute
});

app.use(limiter);

// Request timeout
app.use((req, res, next) => {
  res.setTimeout(60000, () => {
    res.status(408).json({ error: "Request timeout" });
  });
  next();
});
```

### Request Validation

```typescript
import { z } from "zod";

const scrapeSchema = z.object({
  urls: z.array(z.string().url()).min(1).max(100),
  formats: z.array(z.enum(["markdown", "html", "json", "text"])).optional(),
  batchConcurrency: z.number().min(1).max(10).optional(),
});

app.post("/scrape", async (req, res) => {
  const parsed = scrapeSchema.safeParse(req.body);

  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues });
  }

  // ... handle request
});
```

## Concurrency Control

### Request Queue

```typescript
import PQueue from "p-queue";

const requestQueue = new PQueue({
  concurrency: parseInt(process.env.MAX_CONCURRENT_REQUESTS || "10"),
});

app.post("/scrape", async (req, res) => {
  try {
    const result = await requestQueue.add(() =>
      scrape({
        urls: req.body.urls,
        formats: req.body.formats,
        connectionToCore: await createConnection(),
      })
    );

    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});
```

### Timeout Handling

```typescript
async function scrapeWithTimeout(options: ScrapeOptions, timeoutMs: number) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  try {
    return await scrape({
      ...options,
      connectionToCore: await createConnection(),
    });
  } finally {
    clearTimeout(timeout);
  }
}
```

## Monitoring

### Health Checks

```typescript
let activeRequests = 0;
let totalRequests = 0;
let failedRequests = 0;

app.use((req, res, next) => {
  activeRequests++;
  totalRequests++;

  res.on("finish", () => {
    activeRequests--;
    if (res.statusCode >= 500) failedRequests++;
  });

  next();
});

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    heroCore: heroCore ? "running" : "stopped",
    stats: {
      activeRequests,
      totalRequests,
      failedRequests,
      queueSize: requestQueue.size,
      queuePending: requestQueue.pending,
    },
  });
});
```

### Logging

```typescript
import pino from "pino";
import pinoHttp from "pino-http";

const logger = pino({
  level: process.env.LOG_LEVEL || "info",
});

app.use(pinoHttp({ logger }));

// Log scrape requests
app.post("/scrape", async (req, res) => {
  const startTime = Date.now();

  try {
    const result = await scrape({ ... });

    logger.info({
      type: "scrape",
      urls: req.body.urls.length,
      duration: Date.now() - startTime,
      successful: result.batchMetadata.successfulUrls,
    });

    res.json(result);
  } catch (error) {
    logger.error({ type: "scrape_error", error: error.message });
    res.status(500).json({ error: error.message });
  }
});
```

## Scaling

### Horizontal Scaling

Run multiple server instances behind a load balancer:

```bash
# Start multiple instances
PORT=3001 npx tsx server.ts &
PORT=3002 npx tsx server.ts &
PORT=3003 npx tsx server.ts &
```

### PM2 Cluster Mode

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: "reader",
    script: "server.ts",
    interpreter: "npx",
    interpreter_args: "tsx",
    instances: "max",
    exec_mode: "cluster",
    env: {
      NODE_ENV: "production",
      PORT: 3000,
    },
  }],
};
```

```bash
pm2 start ecosystem.config.js
```

### Memory Limits

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: "reader",
    script: "server.ts",
    max_memory_restart: "2G",
    node_args: "--max-old-space-size=2048",
  }],
};
```

## Complete Example

See [examples/production/express-server/](../../examples/production/express-server/) for a complete production server implementation.

## Related Guides

- [Docker Deployment](docker.md) - Containerized deployment
- [Job Queues](job-queues.md) - Async job processing
- [Browser Pool](../guides/browser-pool.md) - Pool management
```

## File: `docs/deployment/serverless.md`
```markdown
# Serverless Deployment Guide

Deploy Reader to serverless platforms.

## Overview

Serverless deployment requires special consideration because:
- Chrome can't run in standard serverless environments
- Cold starts are slow for browser automation
- Memory and timeout limits apply

**Solution:** Use remote browser services or container-based serverless.

> **Note:** For serverless environments, use the direct `scrape()` function with `connectionToCore` instead of `ReaderClient`, since you're connecting to a remote browser service rather than managing a local HeroCore instance.

## Remote Browser Services

Connect to a hosted Chrome instance instead of running locally.

### Browserless

```typescript
import { scrape } from "@vakra-dev/reader";

const result = await scrape({
  urls: ["https://example.com"],
  connectionToCore: "wss://chrome.browserless.io?token=YOUR_TOKEN",
});
```

### Other Providers

- [Browserless](https://browserless.io) - Popular, good Hero support
- [Bright Data](https://brightdata.com/products/scraping-browser) - Built-in proxy rotation
- [Apify](https://apify.com) - Browser automation platform

## AWS Lambda

### Container-based Lambda

Lambda supports containers, which can include Chrome.

#### Dockerfile

```dockerfile
FROM public.ecr.aws/lambda/nodejs:20

# Install Chrome dependencies
RUN yum install -y \
    chromium \
    nss \
    freetype \
    freetype-devel \
    fontconfig \
    pango \
    --skip-broken

ENV CHROME_PATH=/usr/bin/chromium-browser
ENV FONTCONFIG_PATH=/etc/fonts

COPY package*.json ./
RUN npm ci --only=production

COPY . .

CMD ["dist/handler.handler"]
```

#### Handler

```typescript
// handler.ts
import { scrape } from "@vakra-dev/reader";
import { APIGatewayProxyHandler } from "aws-lambda";

export const handler: APIGatewayProxyHandler = async (event) => {
  const body = JSON.parse(event.body || "{}");

  try {
    const result = await scrape({
      urls: body.urls,
      formats: body.formats || ["markdown"],
      showChrome: false,
    });

    return {
      statusCode: 200,
      body: JSON.stringify(result),
    };
  } catch (error: any) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
```

#### Deploy

```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com

docker build -t reader-lambda .
docker tag reader-lambda:latest YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/reader-lambda:latest
docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/reader-lambda:latest

# Create Lambda function
aws lambda create-function \
  --function-name reader \
  --package-type Image \
  --code ImageUri=YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/reader-lambda:latest \
  --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \
  --memory-size 2048 \
  --timeout 60
```

### Lambda with Remote Browser

Use Browserless or similar with standard Lambda:

```typescript
// handler.ts
import { scrape } from "@vakra-dev/reader";

export const handler = async (event: any) => {
  const body = JSON.parse(event.body || "{}");

  const result = await scrape({
    urls: body.urls,
    formats: body.formats || ["markdown"],
    connectionToCore: process.env.BROWSERLESS_URL,
  });

  return {
    statusCode: 200,
    body: JSON.stringify(result),
  };
};
```

## Vercel Functions

### With Remote Browser

```typescript
// api/scrape.ts
import { scrape } from "@vakra-dev/reader";
import type { VercelRequest, VercelResponse } from "@vercel/node";

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { urls, formats = ["markdown"] } = req.body;

  try {
    const result = await scrape({
      urls,
      formats,
      connectionToCore: process.env.BROWSERLESS_URL,
    });

    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
}

export const config = {
  maxDuration: 60,
};
```

### vercel.json

```json
{
  "functions": {
    "api/scrape.ts": {
      "memory": 1024,
      "maxDuration": 60
    }
  }
}
```

### Environment Variables

```bash
vercel env add BROWSERLESS_URL
```

## Cloudflare Workers

Workers don't support Node.js natively, but you can:

### Use Remote Browser

```typescript
// src/index.ts
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405 });
    }

    const { urls } = await request.json();

    // Call external scraping service
    const response = await fetch(env.SCRAPER_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ urls }),
    });

    return response;
  },
};
```

### Use Browser Rendering API

Cloudflare offers Browser Rendering API in beta:

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const browser = await puppeteer.launch(env.BROWSER);
    const page = await browser.newPage();

    await page.goto("https://example.com");
    const html = await page.content();

    await browser.close();

    return new Response(html);
  },
};
```

## Google Cloud Functions

### With Container

```yaml
# cloudbuild.yaml
steps:
  - name: "gcr.io/cloud-builders/docker"
    args: ["build", "-t", "gcr.io/$PROJECT_ID/reader", "."]
  - name: "gcr.io/cloud-builders/docker"
    args: ["push", "gcr.io/$PROJECT_ID/reader"]
  - name: "gcr.io/cloud-builders/gcloud"
    args:
      - "run"
      - "deploy"
      - "reader"
      - "--image"
      - "gcr.io/$PROJECT_ID/reader"
      - "--region"
      - "us-central1"
      - "--memory"
      - "2Gi"
      - "--timeout"
      - "60"
```

### With Remote Browser

```typescript
import * as functions from "@google-cloud/functions-framework";
import { scrape } from "@vakra-dev/reader";

functions.http("scrape", async (req, res) => {
  const { urls, formats } = req.body;

  try {
    const result = await scrape({
      urls,
      formats,
      connectionToCore: process.env.BROWSERLESS_URL,
    });

    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});
```

## Configuration

### Memory & Timeout

| Platform | Max Memory | Max Timeout |
|----------|------------|-------------|
| AWS Lambda | 10 GB | 15 min |
| Vercel | 3 GB | 60 sec (Pro: 300s) |
| Google Cloud Functions | 16 GB | 60 min |
| Cloudflare Workers | 128 MB | 30 sec (unbounded) |

### Recommended Settings

```typescript
// Optimize for serverless
const result = await scrape({
  urls: [url],  // Process one at a time
  formats: ["markdown"],  // Single format
  timeoutMs: 30000,
  connectionToCore: process.env.BROWSERLESS_URL,
});
```

## Cost Optimization

### Minimize Invocations

```typescript
// Batch URLs when possible
const result = await scrape({
  urls: ["url1", "url2", "url3"],  // Multiple URLs per invocation
  batchConcurrency: 3,
});
```

### Use Caching

```typescript
import { createClient } from "@vercel/kv";

const kv = createClient({ /* config */ });

async function cachedScrape(url: string) {
  // Check cache
  const cached = await kv.get(`scrape:${url}`);
  if (cached) return cached;

  // Scrape
  const result = await scrape({ urls: [url] });

  // Cache for 1 hour
  await kv.set(`scrape:${url}`, result, { ex: 3600 });

  return result;
}
```

### Reduce Cold Starts

```typescript
// Keep connection warm
let connectionPromise: Promise<any>;

function getConnection() {
  if (!connectionPromise) {
    connectionPromise = initializeConnection();
  }
  return connectionPromise;
}
```

## Troubleshooting

### Timeout Issues

- Reduce URL count per request
- Use remote browser service
- Increase function timeout

### Memory Issues

- Increase memory allocation
- Process fewer URLs
- Use streaming responses

### Cold Start Issues

- Use provisioned concurrency (AWS)
- Keep functions warm with scheduled pings
- Use remote browser (faster connection)

## Related Guides

- [Production Server](production-server.md) - Traditional server setup
- [Docker](docker.md) - Container deployment
- [Troubleshooting](../troubleshooting.md) - Common issues
```

## File: `docs/guides/browser-pool.md`
```markdown
# Browser Pool Guide

This guide covers browser pool management for production-grade scraping.

## When to Use BrowserPool vs ReaderClient

| Use Case | Recommended |
|----------|-------------|
| Simple scraping/crawling | `ReaderClient` |
| Scripts and CLI tools | `ReaderClient` |
| Custom browser control | `BrowserPool` |
| Express/production servers | `BrowserPool` or Shared Hero Core |
| Low-level page interaction | `BrowserPool` |

For most use cases, **ReaderClient is recommended** as it manages the HeroCore lifecycle automatically. Use `BrowserPool` when you need direct access to Hero browser instances for custom logic.

## Overview

Browser instances are expensive:
- ~2-3 seconds to start
- ~200-500MB memory each
- Can accumulate state over time

The `BrowserPool` class manages a pool of reusable browser instances, handling lifecycle, recycling, and health monitoring.

## Basic Usage

### Using ReaderClient (Recommended)

The simplest way to configure browser pool settings:

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({
  browserPool: {
    size: 5,                   // Number of browser instances
    retireAfterPages: 50,      // Recycle after N pages
    retireAfterMinutes: 15,    // Recycle after N minutes
    maxQueueSize: 100,         // Max pending requests
  },
});

// All scrape/crawl operations use the configured pool
const result = await reader.scrape({
  urls: ["https://example.com", "https://example.org"],
  batchConcurrency: 3,
});

await reader.close();
```

### Using BrowserPool Directly (Advanced)

For custom browser control:

```typescript
import { BrowserPool } from "@vakra-dev/reader";

const pool = new BrowserPool({ size: 5 });
await pool.initialize();

// Use withBrowser for automatic acquire/release
const title = await pool.withBrowser(async (hero) => {
  await hero.goto("https://example.com");
  return await hero.document.title;
});

await pool.shutdown();
```

## Configuration

```typescript
const pool = new BrowserPool({
  size: 5,                    // Number of browser instances
  retireAfterPages: 100,      // Recycle after N pages
  retireAfterMinutes: 30,     // Recycle after N minutes
  maxQueueSize: 100,          // Max pending requests
  healthCheckIntervalMs: 300000, // Health check interval (5 min)
});
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `size` | `2` | Number of browser instances in the pool |
| `retireAfterPages` | `100` | Recycle browser after this many pages |
| `retireAfterMinutes` | `30` | Recycle browser after this many minutes |
| `maxQueueSize` | `100` | Maximum requests that can wait for a browser |
| `healthCheckIntervalMs` | `300000` | Interval between health checks (5 minutes) |

## Pool Lifecycle

### Initialization

```typescript
const pool = new BrowserPool({ size: 5 });
await pool.initialize();
```

This:
1. Creates `size` Hero instances
2. Starts background health checking
3. Makes pool ready for requests

### Acquire and Release

**Recommended: Use `withBrowser`**

```typescript
const result = await pool.withBrowser(async (hero) => {
  await hero.goto("https://example.com");
  const title = await hero.document.title;
  return title;
});
```

Benefits:
- Automatic acquire/release
- Exception-safe (always releases on error)
- Clean, readable code

**Manual acquire/release (advanced)**

```typescript
const hero = await pool.acquire();
try {
  await hero.goto("https://example.com");
  // ... do work
} finally {
  await pool.release(hero);
}
```

### Recycling

Browsers are automatically recycled when:

1. **Page limit reached** - After `retireAfterPages` navigations
2. **Time limit reached** - After `retireAfterMinutes`
3. **Health check failure** - If browser becomes unresponsive

Recycling closes the old browser and creates a fresh one.

### Shutdown

```typescript
await pool.shutdown();
```

This:
1. Stops health checking
2. Closes all browser instances
3. Clears the queue

## Monitoring

### Get Pool Stats

```typescript
const stats = pool.getStats();
console.log(stats);
// {
//   total: 5,
//   available: 3,
//   inUse: 2,
//   queueSize: 0,
//   totalAcquired: 150,
//   totalRecycled: 3
// }
```

### Health Check

```typescript
const health = await pool.healthCheck();
console.log(health);
// {
//   healthy: true,
//   instances: [
//     { id: 0, healthy: true, pages: 45, ageMinutes: 12 },
//     { id: 1, healthy: true, pages: 38, ageMinutes: 10 },
//     ...
//   ]
// }
```

## Production Patterns

### Shared Pool for Express Server

```typescript
import express from "express";
import { BrowserPool } from "@vakra-dev/reader";

const app = express();
const pool = new BrowserPool({ size: 10 });

// Initialize on startup
pool.initialize().then(() => {
  console.log("Browser pool ready");
});

app.get("/scrape", async (req, res) => {
  const url = req.query.url as string;

  try {
    const result = await pool.withBrowser(async (hero) => {
      await hero.goto(url);
      return await hero.document.body.innerHTML;
    });

    res.json({ html: result });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Graceful shutdown
process.on("SIGTERM", async () => {
  await pool.shutdown();
  process.exit(0);
});

app.listen(3000);
```

### Queue Management

When all browsers are busy, requests queue up:

```typescript
const pool = new BrowserPool({
  size: 5,
  maxQueueSize: 100,  // Max 100 waiting requests
});

// If queue is full, acquire() throws an error
try {
  const hero = await pool.acquire();
} catch (error) {
  if (error.message.includes("queue full")) {
    // Handle backpressure
    console.log("Too many pending requests");
  }
}
```

### Scaling Guidelines

| Concurrent Users | Pool Size | Memory (approx) |
|------------------|-----------|-----------------|
| 1-5 | 2-3 | 1-1.5 GB |
| 5-20 | 5-10 | 2.5-5 GB |
| 20-50 | 10-20 | 5-10 GB |
| 50+ | Consider distributed pools | 10+ GB |

## Shared Hero Core Pattern

For production servers, use a shared Hero Core instead of individual cores per browser:

```typescript
import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";

// Initialize once at startup
const heroCore = new HeroCore();
await heroCore.start();

// Create connection for each scrape
function createConnection() {
  const bridge = new TransportBridge();
  heroCore.addConnection(bridge.transportToClient);
  return new ConnectionToHeroCore(bridge.transportToCore);
}

// Use with scrape
const result = await scrape({
  urls: ["https://example.com"],
  connectionToCore: createConnection(),
});

// Shutdown on exit
await heroCore.close();
```

**Why use shared Core?**

- Single Chrome process manages all browsers
- Lower memory overhead
- Better resource utilization
- Faster browser creation

See [Production Server Guide](../deployment/production-server.md) for complete examples.

## Memory Management

### Reduce Memory Usage

```typescript
const pool = new BrowserPool({
  size: 3,                   // Fewer browsers
  retireAfterPages: 50,      // Recycle more often
  retireAfterMinutes: 15,    // Shorter lifetime
});
```

### Monitor Memory

```typescript
import { memoryUsage } from "process";

setInterval(() => {
  const usage = memoryUsage();
  console.log(`Memory: ${Math.round(usage.heapUsed / 1024 / 1024)} MB`);

  const stats = pool.getStats();
  console.log(`Pool: ${stats.inUse}/${stats.total} in use`);
}, 30000);
```

### Force Garbage Collection

Between large batch operations:

```typescript
const reader = new ReaderClient();

// Process batch
await reader.scrape({ urls: batch1 });

// Allow GC before next batch
await new Promise(r => setTimeout(r, 1000));

// Process next batch
await reader.scrape({ urls: batch2 });

await reader.close();
```

## Error Handling

### Browser Crashes

If a browser crashes, the pool automatically:
1. Removes it from the pool
2. Creates a replacement
3. Continues serving requests

### Timeout Handling

```typescript
const result = await pool.withBrowser(async (hero) => {
  // Set navigation timeout
  await hero.goto(url, { timeoutMs: 30000 });

  // ... rest of logic
}, { timeoutMs: 60000 }); // Overall operation timeout
```

### Retry Logic

```typescript
async function scrapeWithRetry(url: string, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await pool.withBrowser(async (hero) => {
        await hero.goto(url);
        return await hero.document.body.innerHTML;
      });
    } catch (error) {
      if (attempt === maxRetries) throw error;
      console.log(`Attempt ${attempt} failed, retrying...`);
      await new Promise(r => setTimeout(r, 1000 * attempt));
    }
  }
}
```

## Best Practices

1. **Always use `withBrowser`** - Ensures proper acquire/release
2. **Size pool appropriately** - Balance memory vs throughput
3. **Enable recycling** - Prevents memory leaks from long-running browsers
4. **Monitor stats** - Track pool utilization
5. **Handle shutdown gracefully** - Close pool on process exit
6. **Use shared Hero Core** - For production servers

## Related Guides

- [Production Server](../deployment/production-server.md) - Shared Hero Core setup
- [Cloudflare Bypass](cloudflare-bypass.md) - Challenge handling
- [Troubleshooting](../troubleshooting.md) - Common issues
```

## File: `docs/guides/cloudflare-bypass.md`
```markdown
# Cloudflare Bypass Guide

This guide explains how Reader bypasses Cloudflare and other bot detection systems.

## Overview

Many websites use Cloudflare to protect against bots. Reader uses [Ulixee Hero](https://ulixee.org/) which employs multiple techniques to appear as a legitimate browser.

## How It Works

### 1. TLS Fingerprinting

Every browser has a unique TLS (HTTPS) fingerprint based on:
- Supported cipher suites
- TLS extensions order
- ALPN protocols

Hero emulates Chrome's exact TLS fingerprint, making connections indistinguishable from a real browser.

### 2. DNS over TLS

Chrome uses DNS over HTTPS/TLS to Cloudflare's 1.1.1.1 servers. Hero replicates this behavior, which Cloudflare can detect and uses as a trust signal.

### 3. WebRTC IP Masking

WebRTC can leak your real IP even behind a proxy. Hero masks WebRTC to prevent IP detection that could reveal automation.

### 4. JavaScript Environment

Hero creates a complete browser environment:
- Navigator properties match real Chrome
- WebGL fingerprints are realistic
- Canvas fingerprints are consistent
- Plugin arrays match real installations

## Challenge Types

Reader detects and handles these challenge types:

| Challenge | Detection | Bypass Method |
|-----------|-----------|---------------|
| **JS Challenge** | "Checking your browser" text | Wait for auto-resolution |
| **Turnstile** | Turnstile widget in DOM | Wait for user interaction simulation |
| **Under Attack Mode** | Interstitial page | Extended wait with polling |
| **CAPTCHA** | hCaptcha/reCAPTCHA widget | Cannot bypass (requires human) |
| **WAF Block** | 403/1020 error codes | Cannot bypass (IP blocked) |

## Detection API

You can manually check for challenges:

```typescript
import { detectChallenge } from "@vakra-dev/reader";

const detection = await detectChallenge(hero);

console.log("Is challenge:", detection.isChallenge);
console.log("Type:", detection.type);
console.log("Signals:", detection.signals);
```

### Detection Signals

The detector looks for multiple signals:

**DOM Signals:**
- `#challenge-form` - Main challenge container
- `.cf-browser-verification` - Verification widget
- `#turnstile-wrapper` - Turnstile CAPTCHA
- `#cf-hcaptcha-container` - hCaptcha container

**Text Signals:**
- "Checking your browser"
- "Please wait..."
- "DDoS protection by Cloudflare"
- "Ray ID:"

**URL Signals:**
- `/cdn-cgi/challenge-platform/`
- `__cf_chl_` parameters

## Resolution API

Wait for a challenge to be resolved:

```typescript
import { waitForChallengeResolution } from "@vakra-dev/reader";

const result = await waitForChallengeResolution(hero, {
  maxWaitMs: 45000,        // Maximum wait time
  pollIntervalMs: 500,     // Check every 500ms
  verbose: true,           // Log progress
  initialUrl: await hero.url,
});

if (result.resolved) {
  console.log(`Resolved via: ${result.method}`);
  console.log(`Wait time: ${result.waitedMs}ms`);
} else {
  console.log("Challenge not resolved within timeout");
}
```

### Resolution Methods

1. **Redirect Detection** - URL changes after challenge is solved
2. **Element Removal** - Challenge DOM elements disappear

## Improving Success Rate

### Use Residential Proxies

Cloudflare trusts residential IPs more than datacenter IPs:

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://protected-site.com"],
  proxy: {
    type: "residential",
    host: "proxy.example.com",
    port: 8080,
    username: "username",
    password: "password",
    country: "us",
  },
});
await reader.close();
```

### Add Delays

Rate limiting makes your traffic look more human:

```typescript
const reader = new ReaderClient();

// For crawling
const result = await reader.crawl({
  url: "https://protected-site.com",
  delayMs: 3000,  // 3 seconds between requests
});

// For batch scraping, lower concurrency
const batchResult = await reader.scrape({
  urls: manyUrls,
  batchConcurrency: 1,  // One at a time
});

await reader.close();
```

### Rotate User Agents

Some sites track user agent patterns:

```typescript
const userAgents = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...",
];

const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  userAgent: userAgents[Math.floor(Math.random() * userAgents.length)],
});
await reader.close();
```

### Increase Timeout

Challenges can take 30+ seconds to resolve:

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://protected-site.com"],
  timeoutMs: 60000,  // 60 seconds
});
await reader.close();
```

## What Can't Be Bypassed

### CAPTCHAs

CAPTCHAs require human interaction. Reader cannot solve:
- hCaptcha
- reCAPTCHA
- Cloudflare Turnstile (interactive mode)

For these, consider:
- CAPTCHA solving services (2Captcha, Anti-Captcha)
- Manual solving workflows
- Alternative data sources

### IP Bans

If your IP is blocked by Cloudflare's WAF:
- You'll see 403 or 1020 errors
- No amount of browser emulation helps
- Solution: Use different IPs (proxies)

### Rate Limits

Excessive requests trigger blocks:
- Implement delays between requests
- Use multiple proxies
- Reduce concurrency

## Debugging Challenges

### Visual Debugging

See exactly what's happening:

```typescript
const reader = new ReaderClient({ showChrome: true, verbose: true });
const result = await reader.scrape({
  urls: ["https://protected-site.com"],
});
await reader.close();
```

### Check Detection Results

```typescript
import { detectChallenge } from "@vakra-dev/reader";

// After navigation
const detection = await detectChallenge(hero);
console.log(JSON.stringify(detection, null, 2));
```

### Monitor Network

Hero supports network monitoring:

```typescript
await pool.withBrowser(async (hero) => {
  hero.on("resource", (resource) => {
    if (resource.url.includes("cdn-cgi")) {
      console.log("Cloudflare resource:", resource.url);
    }
  });

  await hero.goto("https://protected-site.com");
});
```

## Best Practices

1. **Start with verbose mode** to understand what's happening
2. **Use residential proxies** for heavily protected sites
3. **Implement delays** to avoid triggering rate limits
4. **Handle failures gracefully** - not every request will succeed
5. **Rotate IPs** for large-scale scraping
6. **Respect robots.txt** when possible
7. **Cache results** to minimize repeat requests

## Example: Full Challenge Handling

```typescript
import { scrape, detectChallenge, waitForChallengeResolution } from "@vakra-dev/reader";
import { BrowserPool } from "@vakra-dev/reader";

async function scrapeWithChallengeHandling(url: string) {
  const pool = new BrowserPool({ size: 1 });
  await pool.initialize();

  try {
    return await pool.withBrowser(async (hero) => {
      // Navigate to page
      await hero.goto(url, { timeoutMs: 60000 });

      // Check for challenge
      const detection = await detectChallenge(hero);

      if (detection.isChallenge) {
        console.log(`Challenge detected: ${detection.type}`);

        // Wait for resolution
        const resolution = await waitForChallengeResolution(hero, {
          maxWaitMs: 45000,
          pollIntervalMs: 500,
          verbose: true,
          initialUrl: url,
        });

        if (!resolution.resolved) {
          throw new Error(`Challenge not resolved: ${detection.type}`);
        }

        console.log(`Challenge resolved in ${resolution.waitedMs}ms`);
      }

      // Extract content
      const html = await hero.document.body.innerHTML;
      const title = await hero.document.title;

      return { html, title };
    });
  } finally {
    await pool.shutdown();
  }
}
```

## Related Guides

- [Proxy Configuration](proxy-configuration.md) - Setting up proxies
- [Browser Pool](browser-pool.md) - Managing browser instances
- [Troubleshooting](../troubleshooting.md) - Common issues
```

## File: `docs/guides/output-formats.md`
```markdown
# Output Formats Guide

Reader supports four output formats: Markdown, HTML, JSON, and plain text.

## Overview

| Format | Best For | Features |
|--------|----------|----------|
| **markdown** | LLMs, documentation | Clean formatting, headers, links |
| **html** | Web display, archiving | Complete document with CSS |
| **json** | APIs, data processing | Structured data, metadata |
| **text** | Search indexing, NLP | Pure text, no formatting |

## Requesting Formats

### Single Format

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown"],
});

console.log(result.data[0].markdown);
await reader.close();
```

### Multiple Formats

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown", "text", "json"],
});

console.log(result.data[0].markdown);
console.log(result.data[0].text);
console.log(result.data[0].json);
await reader.close();
```

### CLI

```bash
# Single format
npx reader scrape https://example.com -f markdown

# Multiple formats
npx reader scrape https://example.com -f markdown,text,json
```

## Markdown Format

Best for LLM consumption and documentation.

### Features

- Clean heading hierarchy
- Preserved links and images
- Code blocks with syntax hints
- Tables converted from HTML
- Lists (ordered and unordered)

### Example Output

```markdown
---
url: https://example.com
title: Example Domain
scraped_at: 2024-01-15T10:30:00Z
duration_ms: 1523
---

# Example Domain

This domain is for use in illustrative examples in documents.

## More Information

You may use this domain in literature without prior coordination.

[More information...](https://www.iana.org/domains/example)
```

### With Metadata Disabled

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown"],
  includeMetadata: false,
});
await reader.close();
```

Output without frontmatter:

```markdown
# Example Domain

This domain is for use in illustrative examples...
```

## HTML Format

Best for web display and archiving.

### Features

- Complete HTML document
- Inline CSS styles
- Preserved structure
- Self-contained

### Example Output

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Example Domain</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
    /* ... more styles ... */
  </style>
</head>
<body>
  <header>
    <p>Scraped from: <a href="https://example.com">https://example.com</a></p>
    <p>Scraped at: 2024-01-15T10:30:00Z</p>
  </header>
  <main>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents.</p>
    <!-- ... rest of content ... -->
  </main>
</body>
</html>
```

## JSON Format

Best for APIs and data processing.

### Features

- Structured data
- Full metadata
- Easy to parse
- Type-safe

### Example Output

```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "scrapedAt": "2024-01-15T10:30:00Z",
  "duration": 1523,
  "content": {
    "text": "Example Domain\n\nThis domain is for use in illustrative examples...",
    "wordCount": 28
  },
  "metadata": {
    "title": "Example Domain",
    "description": null,
    "author": null,
    "language": "en",
    "openGraph": {
      "title": null,
      "description": null,
      "image": null
    },
    "twitter": {
      "card": null,
      "site": null
    }
  },
  "links": [
    {
      "text": "More information...",
      "href": "https://www.iana.org/domains/example"
    }
  ]
}
```

### Parsing JSON Output

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["json"],
});

const data = JSON.parse(result.data[0].json);
console.log("Title:", data.title);
console.log("Word count:", data.content.wordCount);
console.log("Links:", data.links.length);

await reader.close();
```

## Text Format

Best for search indexing and NLP.

### Features

- Pure text content
- No HTML or formatting
- Whitespace normalized
- Preserves hierarchy through indentation

### Example Output

```
Example Domain
==============

This domain is for use in illustrative examples in documents.

More Information
----------------

You may use this domain in literature without prior coordination.

More information: https://www.iana.org/domains/example
```

### Use Case: Search Indexing

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["text"],
});

// Index plain text
await searchIndex.add({
  url: result.data[0].metadata.baseUrl,
  content: result.data[0].text,
});

await reader.close();
```

## Format Comparison

### Same Content, Different Formats

**Original HTML:**
```html
<h1>Welcome</h1>
<p>Hello <strong>world</strong>!</p>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

**Markdown:**
```markdown
# Welcome

Hello **world**!

- Item 1
- Item 2
```

**Text:**
```
Welcome

Hello world!

- Item 1
- Item 2
```

**JSON:**
```json
{
  "content": {
    "text": "Welcome\n\nHello world!\n\n- Item 1\n- Item 2"
  }
}
```

## Content Cleaning

All formats benefit from content cleaning:

### What Gets Removed

- `<script>` and `<style>` tags
- Navigation elements (`<nav>`, `<header>`, `<footer>`)
- Advertisement containers
- Hidden elements (`display: none`)
- Cookie banners
- Social share buttons

### What Gets Preserved

- Main content (`<main>`, `<article>`)
- Headings and paragraphs
- Links and images
- Tables and lists
- Code blocks

## Custom Formatters

You can use the formatter functions directly:

```typescript
import {
  formatToMarkdown,
  formatToHTML,
  formatToJson,
  formatToText,
} from "@vakra-dev/reader";

// After scraping pages manually
const markdown = formatToMarkdown(
  pages,           // Array of Page objects
  "https://example.com",
  new Date().toISOString(),
  1500,            // Duration in ms
  metadata         // WebsiteMetadata
);
```

## Performance Considerations

| Format | Speed | Size |
|--------|-------|------|
| text | Fastest | Smallest |
| markdown | Fast | Small |
| json | Medium | Medium |
| html | Slowest | Largest |

For high-volume scraping, consider:
- Request only needed formats
- Use `text` for indexing
- Use `markdown` for LLMs
- Avoid `html` unless displaying

## Related Guides

- [Getting Started](../getting-started.md) - Basic usage
- [API Reference](../api-reference.md) - Full API docs
- [Architecture](../architecture.md) - How formatters work
```

## File: `docs/guides/proxy-configuration.md`
```markdown
# Proxy Configuration Guide

This guide covers proxy setup for Reader.

## Overview

Proxies help with:
- Bypassing IP-based blocks
- Accessing geo-restricted content
- Distributing requests across multiple IPs
- Avoiding rate limits

## Quick Start

### Using Proxy URL

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  proxy: {
    url: "http://username:password@proxy.example.com:8080",
  },
});
await reader.close();
```

### Using Structured Config

```typescript
const reader = new ReaderClient();
const result = await reader.scrape({
  urls: ["https://example.com"],
  proxy: {
    type: "residential",
    host: "proxy.example.com",
    port: 8080,
    username: "username",
    password: "password",
    country: "us",
  },
});
await reader.close();
```

### CLI Usage

```bash
npx reader scrape https://example.com --proxy http://user:pass@host:port
```

## Proxy Types

### Datacenter Proxies

- **Pros:** Fast, cheap, reliable
- **Cons:** Easily detected, often blocked
- **Best for:** Sites without bot protection

```typescript
proxy: {
  type: "datacenter",
  host: "proxy.example.com",
  port: 8080,
  username: "username",
  password: "password",
}
```

### Residential Proxies

- **Pros:** Real IPs, hard to detect, trusted by Cloudflare
- **Cons:** Slower, more expensive, limited bandwidth
- **Best for:** Cloudflare-protected sites, sensitive scraping

```typescript
proxy: {
  type: "residential",
  host: "proxy.example.com",
  port: 8080,
  username: "username",
  password: "password",
  country: "us",
}
```

### Mobile Proxies

- **Pros:** Highest trust level, shared by many users
- **Cons:** Most expensive, limited availability
- **Best for:** Most aggressive anti-bot systems

## Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `url` | `string` | Full proxy URL (takes precedence) |
| `type` | `"datacenter" \| "residential"` | Proxy type |
| `host` | `string` | Proxy server hostname |
| `port` | `number` | Proxy server port |
| `username` | `string` | Authentication username |
| `password` | `string` | Authentication password |
| `country` | `string` | Country code (e.g., "us", "uk", "de") |

## Provider Examples

### IPRoyal

```typescript
proxy: {
  type: "residential",
  host: "geo.iproyal.com",
  port: 12321,
  username: "customer-username",
  password: "password",
  country: "us",
}
```

### Bright Data (Luminati)

```typescript
proxy: {
  type: "residential",
  host: "brd.superproxy.io",
  port: 22225,
  username: "customer-zone-residential",
  password: "password",
  country: "us",
}
```

### Oxylabs

```typescript
proxy: {
  type: "residential",
  host: "pr.oxylabs.io",
  port: 7777,
  username: "customer-username",
  password: "password",
  country: "us",
}
```

### SmartProxy

```typescript
proxy: {
  type: "residential",
  host: "gate.smartproxy.com",
  port: 7000,
  username: "user",
  password: "pass",
  country: "us",
}
```

## Proxy Pooling

Reader supports built-in proxy pooling with automatic rotation:

```typescript
const reader = new ReaderClient({
  // Configure multiple proxies
  proxies: [
    { host: "proxy1.example.com", port: 8080, username: "user", password: "pass" },
    { host: "proxy2.example.com", port: 8080, username: "user", password: "pass" },
    { host: "proxy3.example.com", port: 8080, username: "user", password: "pass", country: "us" },
  ],
  // Rotation strategy: "round-robin" (default) or "random"
  proxyRotation: "round-robin",
});

// Each request automatically uses the next proxy in rotation
const result = await reader.scrape({
  urls: ["https://example1.com", "https://example2.com", "https://example3.com"],
});

// Check which proxy handled each request
result.data.forEach((site) => {
  console.log(`${site.metadata.baseUrl} -> ${site.metadata.proxy?.host}:${site.metadata.proxy?.port}`);
});

await reader.close();
```

### Proxy Metadata in Response

When using proxy pooling, each result includes metadata about which proxy was used:

```typescript
interface ProxyMetadata {
  host: string;    // Proxy host that handled the request
  port: number;    // Proxy port
  country?: string; // Country code if geo-targeting was used
}
```

## Rotation Strategies

### Per-Request Rotation

Most residential proxy providers rotate IPs automatically:

```typescript
const reader = new ReaderClient();

// Each request gets a different IP
for (const url of urls) {
  await reader.scrape({
    urls: [url],
    proxy: proxyConfig,
  });
}

await reader.close();
```

### Sticky Sessions

Keep the same IP for multiple requests:

```typescript
// Some providers support session IDs
proxy: {
  host: "proxy.example.com",
  port: 8080,
  username: "user-session-abc123",  // Session in username
  password: "pass",
}
```

### Manual Rotation

Rotate through a list of proxies:

```typescript
const proxies = [
  { host: "proxy1.example.com", port: 8080 },
  { host: "proxy2.example.com", port: 8080 },
  { host: "proxy3.example.com", port: 8080 },
];

let proxyIndex = 0;
const reader = new ReaderClient();

async function scrapeWithRotation(url: string) {
  const proxy = proxies[proxyIndex % proxies.length];
  proxyIndex++;

  return await reader.scrape({
    urls: [url],
    proxy: {
      ...proxy,
      username: "username",
      password: "password",
    },
  });
}

// Don't forget to close when done
// await reader.close();
```

## Geo-Targeting

Target specific countries for localized content:

```typescript
const reader = new ReaderClient();

// US content
const usResult = await reader.scrape({
  urls: ["https://example.com"],
  proxy: { ...baseProxy, country: "us" },
});

// UK content
const ukResult = await reader.scrape({
  urls: ["https://example.com"],
  proxy: { ...baseProxy, country: "uk" },
});

await reader.close();
```

Common country codes:
- `us` - United States
- `uk` or `gb` - United Kingdom
- `de` - Germany
- `fr` - France
- `jp` - Japan
- `au` - Australia

## Error Handling

### Proxy Failures

```typescript
const reader = new ReaderClient();

async function scrapeWithFallback(url: string) {
  const proxies = [residentialProxy, datacenterProxy, null];

  for (const proxy of proxies) {
    try {
      return await reader.scrape({
        urls: [url],
        proxy,
        timeoutMs: 30000,
      });
    } catch (error) {
      console.log(`Proxy failed: ${proxy?.host || "direct"}`);
      continue;
    }
  }

  throw new Error("All proxies failed");
}

// Don't forget to close when done
// await reader.close();
```

### Connection Errors

Common proxy errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| `ECONNREFUSED` | Proxy server down | Try different proxy |
| `407 Proxy Auth Required` | Wrong credentials | Check username/password |
| `403 Forbidden` | Proxy blocked by site | Use residential proxy |
| `Timeout` | Slow proxy | Increase timeout |

## Testing Proxies

### Verify Proxy Works

```typescript
const reader = new ReaderClient();

async function testProxy(proxy: ProxyConfig): Promise<boolean> {
  try {
    const result = await reader.scrape({
      urls: ["https://httpbin.org/ip"],
      formats: ["text"],
      proxy,
      timeoutMs: 10000,
    });

    console.log("Proxy IP:", result.data[0].text);
    return true;
  } catch (error) {
    console.log("Proxy failed:", error.message);
    return false;
  }
}

await reader.close();
```

### Check Geo-Location

```typescript
const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://ipinfo.io/json"],
  formats: ["json"],
  proxy: { ...proxyConfig, country: "uk" },
});

const info = JSON.parse(result.data[0].json);
console.log("Country:", info.country);  // Should be "GB"

await reader.close();
```

## Best Practices

1. **Start with datacenter proxies** - Cheaper, see if you need more
2. **Upgrade to residential** - When blocked or for Cloudflare sites
3. **Use geo-targeting** - Match target site's expected users
4. **Implement rotation** - Spread requests across IPs
5. **Handle failures gracefully** - Have fallback proxies
6. **Monitor bandwidth** - Residential proxies charge by GB
7. **Test before deploying** - Verify proxies work with target site

## Cost Considerations

| Proxy Type | Typical Cost | Best For |
|------------|--------------|----------|
| Datacenter | $0.50-2/GB | Unprotected sites |
| Residential | $3-15/GB | Cloudflare, sensitive sites |
| Mobile | $20-50/GB | Highest security sites |

## Related Guides

- [Cloudflare Bypass](cloudflare-bypass.md) - Works best with residential proxies
- [Browser Pool](browser-pool.md) - Managing browser instances
- [Troubleshooting](../troubleshooting.md) - Common proxy issues
```

## File: `examples/.gitignore`
```
# Dependencies
node_modules/
bun.lockb

# Build outputs
dist/
*.js
*.d.ts
*.map

# Environment
.env
.env.local
.env.*.local

# Logs
*.log
npm-debug.log*

# OS
.DS_Store

# IDE
.idea/
.vscode/
*.swp
*.swo
```

## File: `examples/.nvmrc`
```
v22.12.0
```

## File: `examples/debug-handles.ts`
```typescript
import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting...");
  
  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.scrape({
      urls: ["https://example.com"],
      formats: ["markdown"],
    });
    console.log("Scrape done, title:", result.data[0]?.metadata.website.title);
  } finally {
    await reader.close();
  }
  
  console.log("After close, checking what keeps process alive...");
  
  // @ts-ignore
  const handles = process._getActiveHandles();
  // @ts-ignore  
  const requests = process._getActiveRequests();
  
  console.log("\nActive handles:", handles.length);
  handles.forEach((h: any, i: number) => {
    console.log("  " + i + ": " + h.constructor.name);
  });
  
  console.log("\nActive requests:", requests.length);
  
  setTimeout(() => {
    console.log("\nForce exiting...");
    process.exit(0);
  }, 2000);
}

main().catch(console.error);
```

## File: `examples/package.json`
```json
{
  "name": "reader-examples",
  "version": "1.0.0",
  "private": true,
  "description": "Examples for @vakra-dev/reader",
  "type": "module",
  "dependencies": {
    "@vakra-dev/reader": "file:.."
  },
  "devDependencies": {
    "@ai-sdk/openai": "^1.0.0",
    "@anthropic-ai/sdk": "^0.39.0",
    "@langchain/core": "^0.3.0",
    "@pinecone-database/pinecone": "^4.0.0",
    "@qdrant/js-client-rest": "^1.12.0",
    "@types/aws-lambda": "^8.10.145",
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.6",
    "@ulixee/hero": "^2.0.0-alpha.34",
    "@ulixee/hero-core": "^2.0.0-alpha.34",
    "@ulixee/net": "^2.0.0-alpha.29",
    "@vercel/node": "^3.2.0",
    "ai": "^4.0.0",
    "express": "^4.18.2",
    "llamaindex": "^0.8.0",
    "openai": "^4.0.0",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

## File: `examples/README.md`
```markdown
# Reader Examples

Examples demonstrating various uses of Reader.

## Structure

```
examples/
├── basic/                    # Basic usage examples
│   ├── basic-scrape.ts       # Single URL scraping
│   ├── batch-scrape.ts       # Concurrent multi-URL scraping
│   ├── large-batch-scrape.ts # Large-scale batch scraping (1000+ URLs)
│   ├── browser-pool-config.ts # Browser pool configuration
│   ├── proxy-pool.ts         # Proxy rotation with multiple proxies
│   ├── cloudflare-bypass.ts  # Cloudflare-protected site scraping
│   ├── crawl-website.ts      # Website crawling
│   ├── all-formats.ts        # All output formats
│   └── with-proxy.ts         # Single proxy configuration
│
├── ai-tools/                 # AI framework integrations
│   ├── openai-summary.ts     # OpenAI summarization
│   ├── anthropic-summary.ts  # Anthropic summarization
│   ├── vercel-ai-stream.ts   # Vercel AI SDK streaming
│   ├── langchain-loader.ts   # LangChain document loader
│   ├── llamaindex-loader.ts  # LlamaIndex document loader
│   ├── pinecone-ingest.ts    # Pinecone vector store
│   └── qdrant-ingest.ts      # Qdrant vector store
│
├── production/               # Production-ready setups
│   └── express-server/       # REST API server
│
└── deployment/               # Cloud deployment guides
    ├── docker/               # Docker + docker-compose
    ├── aws-lambda/           # AWS Lambda (container)
    └── vercel-functions/     # Vercel serverless
```

## Quick Start

1. Install dependencies from the examples folder:

```bash
cd examples
npm install
```

2. Start Ulixee Cloud (in a separate terminal):

```bash
npx @ulixee/cloud start
```

3. Run any example using tsx:

```bash
# Basic examples
npx tsx basic/basic-scrape.ts
npx tsx basic/batch-scrape.ts
npx tsx basic/large-batch-scrape.ts  # Large-scale (1000+ URLs)
npx tsx basic/browser-pool-config.ts
npx tsx basic/proxy-pool.ts
npx tsx basic/cloudflare-bypass.ts
npx tsx basic/crawl-website.ts

# AI tools examples (requires API keys)
export OPENAI_API_KEY="sk-..."
npx tsx ai-tools/openai-summary.ts https://example.com

export ANTHROPIC_API_KEY="sk-..."
npx tsx ai-tools/anthropic-summary.ts https://example.com

# Production server
npx tsx production/express-server/src/index.ts
```

### Deploy with Docker

```bash
cd examples/deployment/docker
docker-compose up -d
```

## Requirements

- **Node.js** >= 18
- For LLM examples: API keys for OpenAI/Anthropic
- For deployment: Docker, cloud CLI tools

## Contributing

Have an example to share? Open a PR!
```

## File: `examples/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ESNext"],
    "baseUrl": "..",
    "paths": {
      "@vakra-dev/reader": ["./src/index.ts"]
    },
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "noEmit": true,
    "resolveJsonModule": true,
    "types": ["node"]
  },
  "include": [
    "basic/**/*.ts",
    "ai-tools/**/*.ts",
    "production/**/*.ts",
    "deployment/**/*.ts"
  ],
  "exclude": ["node_modules"]
}
```

## File: `examples/ai-tools/anthropic-summary.ts`
```typescript
/**
 * Anthropic (Claude) Summarization Example
 *
 * Scrapes a webpage and uses Claude to summarize the content.
 *
 * Usage:
 *   npx tsx ai-tools/anthropic-summary.ts https://example.com
 *
 * Requirements:
 *   - Set ANTHROPIC_API_KEY environment variable
 */

import { ReaderClient } from "@vakra-dev/reader";
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const url = process.argv[2] || "https://example.com";

  console.log(`Scraping ${url}...\n`);

  // Check for API key
  if (!process.env.ANTHROPIC_API_KEY) {
    console.error("Error: ANTHROPIC_API_KEY environment variable is required");
    process.exit(1);
  }

  const reader = new ReaderClient();

  try {
    // Step 1: Scrape the webpage
    const result = await reader.scrape({
      urls: [url],
      formats: ["markdown"], // Markdown is best for LLM consumption
    });

    const content = result.data[0]?.markdown;
    if (!content) {
      console.error("No content scraped");
      process.exit(1);
    }

    console.log(`Scraped ${content.length} characters`);
    console.log("Sending to Claude for summarization...\n");

    // Step 2: Summarize with Claude
    const anthropic = new Anthropic();

    const message = await anthropic.messages.create({
      model: "claude-3-haiku-20240307",
      max_tokens: 500,
      messages: [
        {
          role: "user",
          content: `Please summarize the following webpage content in 2-3 paragraphs:\n\n${content.slice(0, 10000)}`,
        },
      ],
    });

    const summary = message.content[0].type === "text" ? message.content[0].text : "";

    console.log("=== SUMMARY ===\n");
    console.log(summary);
    console.log("\n=== METADATA ===");
    console.log(`Source: ${url}`);
    console.log(`Content length: ${content.length} chars`);
    console.log(`Model: ${message.model}`);
    console.log(`Tokens: ${message.usage.input_tokens} in / ${message.usage.output_tokens} out`);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/ai-tools/langchain-loader.ts`
```typescript
/**
 * LangChain Document Loader Example
 *
 * Creates a custom LangChain document loader using Reader.
 *
 * Usage:
 *   npx tsx ai-tools/langchain-loader.ts
 */

import { ReaderClient } from "@vakra-dev/reader";
import { Document } from "@langchain/core/documents";
import { BaseDocumentLoader } from "@langchain/core/document_loaders/base";

/**
 * Custom LangChain document loader powered by Reader
 */
class ReaderEngineLoader extends BaseDocumentLoader {
  private urls: string[];
  private crawlMode: boolean;
  private maxPages: number;
  private depth: number;
  private reader: ReaderClient;

  constructor(options: {
    urls: string[];
    crawl?: boolean;
    maxPages?: number;
    depth?: number;
    reader: ReaderClient;
  }) {
    super();
    this.urls = options.urls;
    this.crawlMode = options.crawl ?? false;
    this.maxPages = options.maxPages ?? 20;
    this.depth = options.depth ?? 1;
    this.reader = options.reader;
  }

  async load(): Promise<Document[]> {
    const documents: Document[] = [];

    if (this.crawlMode && this.urls.length === 1) {
      // Crawl mode: discover pages from a single seed URL
      const result = await this.reader.crawl({
        url: this.urls[0],
        depth: this.depth,
        maxPages: this.maxPages,
        scrape: true,
      });

      if (result.scraped) {
        for (const page of result.scraped.data) {
          documents.push(
            new Document({
              pageContent: page.markdown || "",
              metadata: {
                source: page.metadata.baseUrl,
                title: page.metadata.website.title,
                description: page.metadata.website.description,
                scrapedAt: page.metadata.scrapedAt,
              },
            })
          );
        }
      }
    } else {
      // Scrape mode: scrape specific URLs
      const result = await this.reader.scrape({
        urls: this.urls,
        formats: ["markdown"],
        batchConcurrency: 2,
      });

      for (const page of result.data) {
        documents.push(
          new Document({
            pageContent: page.markdown || "",
            metadata: {
              source: page.metadata.baseUrl,
              title: page.metadata.website.title,
              description: page.metadata.website.description,
              scrapedAt: page.metadata.scrapedAt,
            },
          })
        );
      }
    }

    return documents;
  }
}

// Example usage
async function main() {
  console.log("LangChain Document Loader Example\n");

  const reader = new ReaderClient({ verbose: true });

  try {
    // Example 1: Load specific URLs
    console.log("--- Example 1: Load specific URLs ---");
    const loader1 = new ReaderEngineLoader({
      urls: ["https://example.com", "https://example.org"],
      reader,
    });

    const docs1 = await loader1.load();
    console.log(`Loaded ${docs1.length} documents`);
    for (const doc of docs1) {
      console.log(`  - ${doc.metadata.source}: ${doc.pageContent.length} chars`);
    }

    // Example 2: Crawl a website
    console.log("\n--- Example 2: Crawl a website ---");
    const loader2 = new ReaderEngineLoader({
      urls: ["https://example.com"],
      crawl: true,
      depth: 1,
      maxPages: 5,
      reader,
    });

    const docs2 = await loader2.load();
    console.log(`Crawled and loaded ${docs2.length} documents`);
    for (const doc of docs2) {
      console.log(`  - ${doc.metadata.source}: ${doc.pageContent.length} chars`);
    }

    // The documents can now be used with LangChain:
    // - Text splitters for chunking
    // - Vector stores for embeddings
    // - RAG pipelines
    // - etc.
  } finally {
    await reader.close();
  }
}

main().catch(console.error);
```

## File: `examples/ai-tools/llamaindex-loader.ts`
```typescript
/**
 * LlamaIndex Document Loader Example
 *
 * Creates a custom LlamaIndex document loader using Reader.
 *
 * Usage:
 *   npx tsx ai-tools/llamaindex-loader.ts
 */

import { ReaderClient } from "@vakra-dev/reader";
import { Document } from "llamaindex";

/**
 * Load documents from URLs using Reader
 */
async function loadDocuments(reader: ReaderClient, urls: string[]): Promise<Document[]> {
  const result = await reader.scrape({
    urls,
    formats: ["markdown"],
    batchConcurrency: 2,
  });

  return result.data.map(
    (page) =>
      new Document({
        text: page.markdown || "",
        metadata: {
          source: page.metadata.baseUrl,
          title: page.metadata.website.title ?? undefined,
          description: page.metadata.website.description ?? undefined,
          scrapedAt: page.metadata.scrapedAt,
        },
      })
  );
}

/**
 * Crawl a website and load all discovered pages as documents
 */
async function crawlAndLoadDocuments(
  reader: ReaderClient,
  url: string,
  options: { depth?: number; maxPages?: number } = {}
): Promise<Document[]> {
  const result = await reader.crawl({
    url,
    depth: options.depth ?? 1,
    maxPages: options.maxPages ?? 20,
    scrape: true,
  });

  if (!result.scraped) {
    return [];
  }

  return result.scraped.data.map(
    (page) =>
      new Document({
        text: page.markdown || "",
        metadata: {
          source: page.metadata.baseUrl,
          title: page.metadata.website.title ?? undefined,
          description: page.metadata.website.description ?? undefined,
          scrapedAt: page.metadata.scrapedAt,
        },
      })
  );
}

// Example usage
async function main() {
  console.log("LlamaIndex Document Loader Example\n");

  const reader = new ReaderClient({ verbose: true });

  try {
    // Example 1: Load specific URLs
    console.log("--- Example 1: Load specific URLs ---");
    const docs1 = await loadDocuments(reader, ["https://example.com", "https://example.org"]);
    console.log(`Loaded ${docs1.length} documents`);
    for (const doc of docs1) {
      console.log(`  - ${doc.metadata.source}: ${doc.getText().length} chars`);
    }

    // Example 2: Crawl a website
    console.log("\n--- Example 2: Crawl a website ---");
    const docs2 = await crawlAndLoadDocuments(reader, "https://example.com", {
      depth: 1,
      maxPages: 5,
    });
    console.log(`Crawled and loaded ${docs2.length} documents`);
    for (const doc of docs2) {
      console.log(`  - ${doc.metadata.source}: ${doc.getText().length} chars`);
    }

    // The documents can now be used with LlamaIndex:
    // - VectorStoreIndex for similarity search
    // - SummaryIndex for summarization
    // - KnowledgeGraphIndex for graph-based retrieval
  } finally {
    await reader.close();
  }
}

main().catch(console.error);
```

## File: `examples/ai-tools/openai-summary.ts`
```typescript
/**
 * OpenAI Summarization Example
 *
 * Scrapes a webpage and uses OpenAI to summarize the content.
 *
 * Usage:
 *   npx tsx ai-tools/openai-summary.ts https://example.com
 *
 * Requirements:
 *   - Set OPENAI_API_KEY environment variable
 */

import { ReaderClient } from "@vakra-dev/reader";
import OpenAI from "openai";

async function main() {
  const url = process.argv[2] || "https://example.com";

  console.log(`Scraping ${url}...\n`);

  // Check for API key
  if (!process.env.OPENAI_API_KEY) {
    console.error("Error: OPENAI_API_KEY environment variable is required");
    process.exit(1);
  }

  const reader = new ReaderClient();

  try {
    // Step 1: Scrape the webpage
    const result = await reader.scrape({
      urls: [url],
      formats: ["markdown"], // Markdown is best for LLM consumption
    });

    const content = result.data[0]?.markdown;
    if (!content) {
      console.error("No content scraped");
      process.exit(1);
    }

    console.log(`Scraped ${content.length} characters`);
    console.log("Sending to OpenAI for summarization...\n");

    // Step 2: Summarize with OpenAI
    const openai = new OpenAI();

    const completion = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        {
          role: "system",
          content:
            "You are a helpful assistant that summarizes web content. Provide a concise summary in 2-3 paragraphs.",
        },
        {
          role: "user",
          content: `Please summarize the following webpage content:\n\n${content.slice(0, 10000)}`,
        },
      ],
      max_tokens: 500,
    });

    const summary = completion.choices[0]?.message?.content;

    console.log("=== SUMMARY ===\n");
    console.log(summary);
    console.log("\n=== METADATA ===");
    console.log(`Source: ${url}`);
    console.log(`Content length: ${content.length} chars`);
    console.log(`Model: ${completion.model}`);
    console.log(`Tokens used: ${completion.usage?.total_tokens}`);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/ai-tools/pinecone-ingest.ts`
```typescript
/**
 * Pinecone Vector Store Ingestion Example
 *
 * Scrapes webpages and ingests them into Pinecone for semantic search.
 *
 * Usage:
 *   npx tsx ai-tools/pinecone-ingest.ts
 *
 * Requirements:
 *   - Set PINECONE_API_KEY environment variable
 *   - Set OPENAI_API_KEY environment variable (for embeddings)
 *   - Create a Pinecone index with dimension 1536 (for text-embedding-3-small)
 */

import { ReaderClient } from "@vakra-dev/reader";
import { Pinecone } from "@pinecone-database/pinecone";
import OpenAI from "openai";

const INDEX_NAME = "reader-docs";

async function main() {
  // Check for required API keys
  if (!process.env.PINECONE_API_KEY) {
    console.error("Error: PINECONE_API_KEY environment variable is required");
    process.exit(1);
  }
  if (!process.env.OPENAI_API_KEY) {
    console.error("Error: OPENAI_API_KEY environment variable is required");
    process.exit(1);
  }

  console.log("Pinecone Vector Store Ingestion Example\n");

  // Initialize clients
  const pinecone = new Pinecone();
  const openai = new OpenAI();
  const reader = new ReaderClient({ verbose: true });

  try {
    // Step 1: Scrape webpages
    const urls = ["https://example.com", "https://example.org"];

    console.log(`Scraping ${urls.length} URLs...`);
    const result = await reader.scrape({
      urls,
      formats: ["markdown"],
      batchConcurrency: 2,
    });

    console.log(`Scraped ${result.batchMetadata.successfulUrls} pages`);

    // Step 2: Generate embeddings and prepare vectors
    console.log("\nGenerating embeddings...");
    const index = pinecone.index(INDEX_NAME);

    const vectors = [];
    for (const page of result.data) {
      const content = page.markdown || "";
      if (!content) continue;

      // Truncate content to fit embedding model limits
      const truncatedContent = content.slice(0, 8000);

      // Generate embedding
      const embeddingResponse = await openai.embeddings.create({
        model: "text-embedding-3-small",
        input: truncatedContent,
      });

      const embedding = embeddingResponse.data[0].embedding;

      vectors.push({
        id: Buffer.from(page.metadata.baseUrl).toString("base64"),
        values: embedding,
        metadata: {
          url: page.metadata.baseUrl,
          title: page.metadata.website.title || "",
          description: page.metadata.website.description || "",
          content: truncatedContent.slice(0, 1000), // Store preview in metadata
          scrapedAt: page.metadata.scrapedAt,
        },
      });

      console.log(`  - Embedded: ${page.metadata.baseUrl}`);
    }

    // Step 3: Upsert to Pinecone
    console.log(`\nUpserting ${vectors.length} vectors to Pinecone...`);
    await index.upsert(vectors);

    console.log("\nDone! Vectors are now searchable in Pinecone.");
    console.log(`Index: ${INDEX_NAME}`);

    // Example: Query the index
    console.log("\n--- Example Query ---");
    const queryText = "example domain";
    const queryEmbedding = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: queryText,
    });

    const queryResponse = await index.query({
      vector: queryEmbedding.data[0].embedding,
      topK: 3,
      includeMetadata: true,
    });

    console.log(`Query: "${queryText}"`);
    console.log("Results:");
    for (const match of queryResponse.matches) {
      console.log(`  - ${match.metadata?.title} (score: ${match.score?.toFixed(3)})`);
      console.log(`    URL: ${match.metadata?.url}`);
    }
  } finally {
    await reader.close();
  }
}

main().catch(console.error);
```

## File: `examples/ai-tools/qdrant-ingest.ts`
```typescript
/**
 * Qdrant Vector Store Ingestion Example
 *
 * Scrapes webpages and ingests them into Qdrant for semantic search.
 *
 * Usage:
 *   npx tsx ai-tools/qdrant-ingest.ts
 *
 * Requirements:
 *   - Set QDRANT_URL environment variable (default: http://localhost:6333)
 *   - Set QDRANT_API_KEY environment variable (optional, for Qdrant Cloud)
 *   - Set OPENAI_API_KEY environment variable (for embeddings)
 */

import { ReaderClient } from "@vakra-dev/reader";
import { QdrantClient } from "@qdrant/js-client-rest";
import OpenAI from "openai";

const COLLECTION_NAME = "reader-docs";
const VECTOR_SIZE = 1536; // text-embedding-3-small dimension

async function main() {
  // Check for required API keys
  if (!process.env.OPENAI_API_KEY) {
    console.error("Error: OPENAI_API_KEY environment variable is required");
    process.exit(1);
  }

  console.log("Qdrant Vector Store Ingestion Example\n");

  // Initialize clients
  const qdrantUrl = process.env.QDRANT_URL || "http://localhost:6333";
  const qdrant = new QdrantClient({
    url: qdrantUrl,
    apiKey: process.env.QDRANT_API_KEY,
  });
  const openai = new OpenAI();
  const reader = new ReaderClient({ verbose: true });

  try {
    // Ensure collection exists
    try {
      await qdrant.getCollection(COLLECTION_NAME);
      console.log(`Using existing collection: ${COLLECTION_NAME}`);
    } catch {
      console.log(`Creating collection: ${COLLECTION_NAME}`);
      await qdrant.createCollection(COLLECTION_NAME, {
        vectors: {
          size: VECTOR_SIZE,
          distance: "Cosine",
        },
      });
    }

    // Step 1: Scrape webpages
    const urls = ["https://example.com", "https://example.org"];

    console.log(`\nScraping ${urls.length} URLs...`);
    const result = await reader.scrape({
      urls,
      formats: ["markdown"],
      batchConcurrency: 2,
    });

    console.log(`Scraped ${result.batchMetadata.successfulUrls} pages`);

    // Step 2: Generate embeddings and prepare points
    console.log("\nGenerating embeddings...");
    const points = [];

    for (let i = 0; i < result.data.length; i++) {
      const page = result.data[i];
      const content = page.markdown || "";
      if (!content) continue;

      // Truncate content to fit embedding model limits
      const truncatedContent = content.slice(0, 8000);

      // Generate embedding
      const embeddingResponse = await openai.embeddings.create({
        model: "text-embedding-3-small",
        input: truncatedContent,
      });

      const embedding = embeddingResponse.data[0].embedding;

      points.push({
        id: i + 1, // Qdrant requires positive integers or UUIDs
        vector: embedding,
        payload: {
          url: page.metadata.baseUrl,
          title: page.metadata.website.title || "",
          description: page.metadata.website.description || "",
          content: truncatedContent.slice(0, 1000), // Store preview in payload
          scrapedAt: page.metadata.scrapedAt,
        },
      });

      console.log(`  - Embedded: ${page.metadata.baseUrl}`);
    }

    // Step 3: Upsert to Qdrant
    console.log(`\nUpserting ${points.length} points to Qdrant...`);
    await qdrant.upsert(COLLECTION_NAME, {
      wait: true,
      points,
    });

    console.log("\nDone! Points are now searchable in Qdrant.");
    console.log(`Collection: ${COLLECTION_NAME}`);
    console.log(`Qdrant URL: ${qdrantUrl}`);

    // Example: Query the collection
    console.log("\n--- Example Query ---");
    const queryText = "example domain";
    const queryEmbedding = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: queryText,
    });

    const searchResponse = await qdrant.search(COLLECTION_NAME, {
      vector: queryEmbedding.data[0].embedding,
      limit: 3,
      with_payload: true,
    });

    console.log(`Query: "${queryText}"`);
    console.log("Results:");
    for (const result of searchResponse) {
      console.log(`  - ${result.payload?.title} (score: ${result.score.toFixed(3)})`);
      console.log(`    URL: ${result.payload?.url}`);
    }
  } finally {
    await reader.close();
  }
}

main().catch(console.error);
```

## File: `examples/ai-tools/README.md`
```markdown
# AI Tools Examples

Examples showing how to integrate Reader with AI frameworks, LLMs, and vector stores.

## Prerequisites

Start Ulixee Cloud in a separate terminal:

```bash
npx @ulixee/cloud start
```

## Examples

### LLM Summarization

Scrape webpages and summarize with LLMs.

| Example | Description | API Key Required |
|---------|-------------|------------------|
| [openai-summary.ts](./openai-summary.ts) | Summarize with GPT | `OPENAI_API_KEY` |
| [anthropic-summary.ts](./anthropic-summary.ts) | Summarize with Claude | `ANTHROPIC_API_KEY` |
| [vercel-ai-stream.ts](./vercel-ai-stream.ts) | Streaming summary with Vercel AI SDK | `OPENAI_API_KEY` |

```bash
export OPENAI_API_KEY="sk-..."
npx tsx ai-tools/openai-summary.ts https://example.com

export ANTHROPIC_API_KEY="sk-ant-..."
npx tsx ai-tools/anthropic-summary.ts https://example.com
```

### RAG Frameworks

Load scraped content into RAG frameworks for retrieval-augmented generation.

| Example | Description |
|---------|-------------|
| [langchain-loader.ts](./langchain-loader.ts) | Custom LangChain document loader |
| [llamaindex-loader.ts](./llamaindex-loader.ts) | LlamaIndex document loader |

```bash
npx tsx ai-tools/langchain-loader.ts
npx tsx ai-tools/llamaindex-loader.ts
```

### Vector Stores

Scrape and ingest content directly into vector databases for semantic search.

| Example | Description | API Keys Required |
|---------|-------------|-------------------|
| [pinecone-ingest.ts](./pinecone-ingest.ts) | Ingest into Pinecone | `PINECONE_API_KEY`, `OPENAI_API_KEY` |
| [qdrant-ingest.ts](./qdrant-ingest.ts) | Ingest into Qdrant | `OPENAI_API_KEY`, optionally `QDRANT_URL` |

```bash
# Pinecone
export PINECONE_API_KEY="..."
export OPENAI_API_KEY="sk-..."
npx tsx ai-tools/pinecone-ingest.ts

# Qdrant (local)
docker run -p 6333:6333 qdrant/qdrant
export OPENAI_API_KEY="sk-..."
npx tsx ai-tools/qdrant-ingest.ts
```

## Tips

- Use `markdown` format for LLM input (cleaner than HTML)
- Truncate content if it exceeds token limits
- For production, consider chunking large documents before embedding
```

## File: `examples/ai-tools/vercel-ai-stream.ts`
```typescript
/**
 * Vercel AI SDK Streaming Example
 *
 * Scrapes a webpage and streams a summary using the Vercel AI SDK.
 *
 * Usage:
 *   npx tsx ai-tools/vercel-ai-stream.ts https://example.com
 *
 * Requirements:
 *   - Set OPENAI_API_KEY environment variable
 */

import { ReaderClient } from "@vakra-dev/reader";
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";

async function main() {
  const url = process.argv[2] || "https://example.com";

  console.log(`Scraping ${url}...\n`);

  // Check for API key
  if (!process.env.OPENAI_API_KEY) {
    console.error("Error: OPENAI_API_KEY environment variable is required");
    process.exit(1);
  }

  const reader = new ReaderClient({ verbose: true });

  try {
    // Step 1: Scrape the webpage
    const result = await reader.scrape({
      urls: [url],
      formats: ["markdown"],
    });

    const content = result.data[0]?.markdown;
    if (!content) {
      console.error("No content scraped");
      process.exit(1);
    }

    console.log(`Scraped ${content.length} characters`);
    console.log("Streaming summary...\n");
    console.log("=== STREAMING SUMMARY ===\n");

    // Step 2: Stream summary with Vercel AI SDK
    const { textStream } = await streamText({
      model: openai("gpt-4o-mini"),
      system:
        "You are a helpful assistant that summarizes web content. Provide a concise summary in 2-3 paragraphs.",
      prompt: `Please summarize the following webpage content:\n\n${content.slice(0, 10000)}`,
      maxTokens: 500,
    });

    // Stream the response to stdout
    for await (const chunk of textStream) {
      process.stdout.write(chunk);
    }

    console.log("\n\n=== METADATA ===");
    console.log(`Source: ${url}`);
    console.log(`Content length: ${content.length} chars`);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/all-formats.ts`
```typescript
#!/usr/bin/env node
/**
 * All Formats Example
 *
 * Demonstrates outputting content in all supported formats (markdown and html)
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting all-formats example\n");

  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.scrape({
      urls: ["https://example.com"],
      formats: ["markdown", "html"],
    });

    const page = result.data[0];

    if (!page) {
      console.error("No data returned - scrape may have failed");
      console.log("Errors:", result.batchMetadata.errors);
      process.exit(1);
    }

    console.log("\nScrape completed!");
    console.log("\nFormat Lengths:");
    console.log(`  Markdown: ${page.markdown?.length || 0} chars`);
    console.log(`  HTML: ${page.html?.length || 0} chars`);

    console.log("\n--- MARKDOWN OUTPUT ---");
    console.log(page.markdown?.slice(0, 500));

    console.log("\n--- HTML OUTPUT (first 500 chars) ---");
    console.log(page.html?.slice(0, 500));

    console.log("\n--- FULL RESULT (JSON) ---");
    console.log(JSON.stringify(result, null, 2).slice(0, 1000));
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/basic-scrape.ts`
```typescript
#!/usr/bin/env node
/**
 * Basic Scraping Example
 *
 * Demonstrates simple single-URL scraping with reader
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting basic scrape example\n");

  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.scrape({
      urls: ["https://example.com"],
      formats: ["markdown", "html"],
    });

    const page = result.data[0];

    if (!page) {
      console.error("No data returned - scrape may have failed");
      console.log("Errors:", result.batchMetadata.errors);
      process.exit(1);
    }

    console.log("\nScrape completed!");
    console.log("\nResults:");
    console.log(`  URL: ${page.metadata.baseUrl}`);
    console.log(`  Title: ${page.metadata.website.title}`);
    console.log(`  Duration: ${page.metadata.duration}ms`);
    console.log(`  Markdown length: ${page.markdown?.length || 0} chars`);
    console.log(`  HTML length: ${page.html?.length || 0} chars`);

    console.log("\nMarkdown Preview (first 500 chars):");
    console.log(page.markdown?.slice(0, 500));

    console.log("\nBatch Metadata:");
    console.log(`  Total URLs: ${result.batchMetadata.totalUrls}`);
    console.log(`  Successful: ${result.batchMetadata.successfulUrls}`);
    console.log(`  Failed: ${result.batchMetadata.failedUrls}`);
    console.log(`  Total Duration: ${result.batchMetadata.totalDuration}ms`);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/batch-scrape.ts`
```typescript
#!/usr/bin/env node
/**
 * Batch Scraping Example
 *
 * Demonstrates concurrent scraping of multiple URLs
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting batch scrape example\n");

  const urls = ["https://example.com", "https://example.org", "https://example.net"];

  console.log(`Scraping ${urls.length} URLs with concurrency=2\n`);

  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.scrape({
      urls,
      formats: ["markdown"],
      batchConcurrency: 2, // Process 2 URLs in parallel
      onProgress: (progress) => {
        console.log(`\nProgress: ${progress.completed}/${progress.total} - ${progress.currentUrl}`);
      },
    });

    console.log("\nBatch scrape completed!\n");
    console.log("Results:");

    for (const page of result.data) {
      console.log(`\n  ${page.metadata.baseUrl}`);
      console.log(`     Title: ${page.metadata.website.title}`);
      console.log(`     Duration: ${page.metadata.duration}ms`);
      console.log(`     Content: ${page.markdown?.length || 0} chars`);
    }

    console.log("\nBatch Metadata:");
    console.log(`  Total URLs: ${result.batchMetadata.totalUrls}`);
    console.log(`  Successful: ${result.batchMetadata.successfulUrls}`);
    console.log(`  Failed: ${result.batchMetadata.failedUrls}`);
    console.log(`  Total Duration: ${result.batchMetadata.totalDuration}ms`);
    console.log(
      `  Avg Per URL: ${Math.round(
        result.batchMetadata.totalDuration / result.batchMetadata.totalUrls
      )}ms`
    );
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/browser-pool-config.ts`
```typescript
#!/usr/bin/env node
/**
 * Browser Pool Configuration Example
 *
 * Demonstrates configuring the browser pool for high-throughput scraping.
 * Useful when scraping many URLs to optimize performance and resource usage.
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting browser pool configuration example\n");

  // Configure browser pool for high-throughput scraping
  const reader = new ReaderClient({
    verbose: true,

    // Browser pool configuration
    browserPool: {
      size: 5, // Run 5 browser instances in parallel
      retireAfterPages: 50, // Recycle browser after 50 pages (prevents memory leaks)
      retireAfterMinutes: 15, // Recycle browser after 15 minutes
      maxQueueSize: 200, // Allow up to 200 pending requests in queue
    },
  });

  // Sample URLs to scrape
  const urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
  ];

  console.log(`Scraping ${urls.length} URLs with pool size=5, concurrency=3\n`);

  try {
    const result = await reader.scrape({
      urls,
      formats: ["markdown"],
      batchConcurrency: 3, // Process 3 URLs in parallel
      onProgress: (progress) => {
        console.log(`Progress: ${progress.completed}/${progress.total} - ${progress.currentUrl}`);
      },
    });

    console.log("\nScrape completed!\n");
    console.log("Results:");

    for (const page of result.data) {
      console.log(`\n  ${page.metadata.baseUrl}`);
      console.log(`     Title: ${page.metadata.website.title}`);
      console.log(`     Duration: ${page.metadata.duration}ms`);
      console.log(`     Content: ${page.markdown?.length || 0} chars`);
    }

    console.log("\nBatch Metadata:");
    console.log(`  Total URLs: ${result.batchMetadata.totalUrls}`);
    console.log(`  Successful: ${result.batchMetadata.successfulUrls}`);
    console.log(`  Failed: ${result.batchMetadata.failedUrls}`);
    console.log(`  Total Duration: ${result.batchMetadata.totalDuration}ms`);
    console.log(
      `  Avg Per URL: ${Math.round(
        result.batchMetadata.totalDuration / result.batchMetadata.totalUrls
      )}ms`
    );
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/cloudflare-bypass.ts`
```typescript
#!/usr/bin/env node
/**
 * Cloudflare Bypass Example
 *
 * Demonstrates scraping a Cloudflare-protected website.
 * Reader automatically detects and handles Cloudflare challenges
 * using TLS fingerprinting, DNS over TLS, and WebRTC masking.
 *
 * Test URL: https://www.scrapingcourse.com/cloudflare-challenge
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting Cloudflare bypass example\n");

  // Cloudflare-protected test URL
  const url = process.argv[2] || "https://www.scrapingcourse.com/cloudflare-challenge";

  console.log(`Target: ${url}`);
  console.log("This site is protected by Cloudflare challenge.\n");

  const reader = new ReaderClient({
    verbose: true,
    showChrome: false, // Set to true to watch the bypass in action
  });

  try {
    console.log("Scraping (Cloudflare bypass handled automatically)...\n");

    const result = await reader.scrape({
      urls: [url],
      formats: ["markdown"],
      timeoutMs: 5000, // Allow extra time for challenge resolution
    });

    const page = result.data[0];

    if (!page) {
      console.error("No data returned - scrape may have failed");
      console.log("Errors:", result.batchMetadata.errors);
      process.exit(1);
    }

    console.log("\nScrape completed successfully!");
    console.log("\nResults:");
    console.log(`  URL: ${page.metadata.baseUrl}`);
    console.log(`  Title: ${page.metadata.website.title}`);
    console.log(`  Duration: ${page.metadata.duration}ms`);
    console.log(`  Content length: ${page.markdown?.length || 0} chars`);

    console.log("\n--- CONTENT PREVIEW (first 500 chars) ---\n");
    console.log(page.markdown?.slice(0, 500));

    console.log("\n--- METADATA ---");
    console.log(`  Description: ${page.metadata.website.description || "N/A"}`);
  } catch (error: any) {
    console.error("Error:", error.message);
    console.log("\nTip: If the challenge fails, try:");
    console.log("  - Increasing timeoutMs");
    console.log("  - Using --show-chrome to debug visually");
    console.log("  - Using a residential proxy");
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/crawl-website.ts`
```typescript
#!/usr/bin/env node
/**
 * Crawling Example
 *
 * Demonstrates website crawling with link discovery
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting crawl example\n");

  const seedUrl = process.argv[2] || "https://example.com";

  console.log(`Crawling: ${seedUrl}`);
  console.log(`   Depth: 2`);
  console.log(`   Max Pages: 10`);
  console.log(`   Scrape Content: true\n`);

  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.crawl({
      url: seedUrl,
      depth: 2,
      maxPages: 10,
      scrape: true,
    });

    console.log("\nCrawl completed!\n");
    console.log("Discovered URLs:");

    for (const crawlUrl of result.urls) {
      console.log(`\n  ${crawlUrl.url}`);
      console.log(`     Title: ${crawlUrl.title}`);
      if (crawlUrl.description) {
        console.log(`     Description: ${crawlUrl.description.slice(0, 100)}...`);
      }
    }

    console.log("\nCrawl Metadata:");
    console.log(`  Total URLs: ${result.metadata.totalUrls}`);
    console.log(`  Max Depth: ${result.metadata.maxDepth}`);
    console.log(`  Duration: ${result.metadata.totalDuration}ms`);
    console.log(`  Seed URL: ${result.metadata.seedUrl}`);

    if (result.scraped) {
      console.log("\nScraped Content:");
      console.log(`  Pages Scraped: ${result.scraped.batchMetadata.successfulUrls}`);
      console.log(
        `  Total Content: ${result.scraped.data.reduce(
          (acc, page) => acc + (page.markdown?.length || 0),
          0
        )} chars`
      );
    }
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/large-batch-scrape.ts`
```typescript
#!/usr/bin/env node
/**
 * Large-Scale Batch Scraping Example (1000 URLs)
 *
 * Demonstrates how to configure Reader for scraping
 * large batches of URLs efficiently.
 *
 * Key configurations for large batches:
 * - browserPool.size: More browsers = more parallelism
 * - browserPool.maxQueueSize: Must exceed total URL count
 * - batchConcurrency: How many URLs to process in parallel
 * - batchTimeoutMs: Must be long enough for all URLs
 *
 * Configuration Guide:
 * | URLs  | Pool Size | Concurrency | Queue Size | Timeout  | Est. Time   |
 * |-------|-----------|-------------|------------|----------|-------------|
 * | 100   | 5         | 5           | 100        | 10 min   | 3-5 min     |
 * | 500   | 8         | 8           | 500        | 30 min   | 15-25 min   |
 * | 1000  | 10        | 10          | 1000       | 1 hour   | 25-50 min   |
 * | 5000  | 10        | 10          | 5000       | 3 hours  | 2-4 hours   |
 *
 * Memory requirements:
 * - Each browser: ~100-300MB RAM
 * - 10 browsers: ~1-3GB RAM
 * - Recommended: 8GB+ system RAM for 10 browser instances
 */

import { ReaderClient } from "@vakra-dev/reader";

/**
 * Generate sample URLs for demonstration
 * In production, you'd load these from a file, database, or API
 */
function generateSampleUrls(count: number): string[] {
  // Using httpbin.org endpoints which are safe for testing
  const urls: string[] = [];
  for (let i = 0; i < count; i++) {
    // Rotate through different endpoints to simulate variety
    urls.push(`https://httpbin.org/html?page=${i}`);
  }
  return urls;
}

async function main() {
  // For demo purposes, use a smaller batch (10 URLs)
  // Change to 1000 for actual large-scale scraping
  const BATCH_SIZE = 10; // Set to 1000 for real large-scale scraping

  console.log(`\n╔══════════════════════════════════════════════════════════╗`);
  console.log(`║         Large-Scale Batch Scraping Example               ║`);
  console.log(`╚══════════════════════════════════════════════════════════╝\n`);

  const urls = generateSampleUrls(BATCH_SIZE);
  console.log(`Preparing to scrape ${urls.length} URLs\n`);

  // Configure for large-scale scraping
  const reader = new ReaderClient({
    verbose: true,

    browserPool: {
      // More browsers = more parallelism (adjust based on RAM)
      // Each browser uses ~100-300MB RAM
      size: 10,

      // Queue must be large enough for all URLs
      maxQueueSize: 1000,

      // Recycle browsers more frequently with large batches
      retireAfterPages: 200,
      retireAfterMinutes: 30,
    },
  });

  const startTime = Date.now();
  let lastProgressUpdate = 0;

  try {
    const result = await reader.scrape({
      urls,
      formats: ["markdown"], // Use single format for efficiency

      // Match concurrency to browser pool size
      batchConcurrency: 10,

      // Long timeout for large batches (1 hour)
      batchTimeoutMs: 3600000,

      // Progress tracking
      onProgress: (progress) => {
        const now = Date.now();
        // Update every 5 seconds to avoid console spam
        if (now - lastProgressUpdate > 5000 || progress.completed === progress.total) {
          const elapsed = Math.round((now - startTime) / 1000);
          const rate = progress.completed / (elapsed || 1);
          const eta = Math.round((progress.total - progress.completed) / rate);

          console.log(
            `[${elapsed}s] Progress: ${progress.completed}/${progress.total} ` +
              `(${Math.round((progress.completed / progress.total) * 100)}%) ` +
              `| Rate: ${rate.toFixed(1)} URLs/s | ETA: ${eta}s`
          );
          lastProgressUpdate = now;
        }
      },
    });

    const duration = Date.now() - startTime;

    console.log(`\n╔══════════════════════════════════════════════════════════╗`);
    console.log(`║                    Batch Complete                        ║`);
    console.log(`╚══════════════════════════════════════════════════════════╝\n`);

    console.log(`Summary:`);
    console.log(`  Total URLs:      ${result.batchMetadata.totalUrls}`);
    console.log(`  Successful:      ${result.batchMetadata.successfulUrls}`);
    console.log(`  Failed:          ${result.batchMetadata.failedUrls}`);
    console.log(`  Total Duration:  ${Math.round(duration / 1000)}s`);
    console.log(`  Avg Per URL:     ${Math.round(duration / result.batchMetadata.totalUrls)}ms`);
    console.log(
      `  Throughput:      ${(result.batchMetadata.totalUrls / (duration / 1000)).toFixed(2)} URLs/s`
    );

    // Show failed URLs if any
    if (result.batchMetadata.errors && result.batchMetadata.errors.length > 0) {
      console.log(`\nFailed URLs:`);
      for (const error of result.batchMetadata.errors.slice(0, 10)) {
        console.log(`  - ${error.url}: ${error.error}`);
      }
      if (result.batchMetadata.errors.length > 10) {
        console.log(`  ... and ${result.batchMetadata.errors.length - 10} more`);
      }
    }

    // Sample output from successful scrapes
    if (result.data.length > 0) {
      console.log(`\nSample Results (first 3):`);
      for (const page of result.data.slice(0, 3)) {
        console.log(`  - ${page.metadata.baseUrl}`);
        console.log(`    Title: ${page.metadata.website.title || "N/A"}`);
        console.log(`    Content: ${page.markdown?.length || 0} chars`);
      }
    }
  } catch (error: any) {
    console.error("\nError:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
    console.log("\nDone!");
  }
}

main();
```

## File: `examples/basic/proxy-pool.ts`
```typescript
#!/usr/bin/env node
/**
 * Proxy Pool Example
 *
 * Demonstrates configuring multiple proxies with rotation for scraping.
 * Useful for avoiding rate limits and IP blocks when scraping at scale.
 *
 * Usage:
 *   Set your proxy credentials and run:
 *   npx tsx basic/proxy-pool.ts
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting proxy pool example\n");

  // Configure proxy pool with rotation
  // Replace with your actual proxy credentials
  const reader = new ReaderClient({
    verbose: true,

    // List of proxies to rotate through
    proxies: [
      {
        host: "proxy1.example.com",
        port: 8080,
        username: "user1",
        password: "pass1",
        type: "datacenter",
      },
      {
        host: "proxy2.example.com",
        port: 8080,
        username: "user2",
        password: "pass2",
        type: "datacenter",
      },
      {
        host: "residential.example.com",
        port: 9000,
        username: "user3",
        password: "pass3",
        type: "residential",
        country: "us", // Geo-target to US
      },
    ],

    // Rotation strategy: "round-robin" (default) or "random"
    proxyRotation: "round-robin",
  });

  // URLs to scrape - each will use a different proxy from the pool
  const urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
  ];

  console.log(`Scraping ${urls.length} URLs with proxy rotation\n`);
  console.log("Proxy rotation: round-robin");
  console.log("Proxy pool size: 3\n");

  try {
    const result = await reader.scrape({
      urls,
      formats: ["markdown"],
      batchConcurrency: 1, // Sequential to demonstrate rotation
      onProgress: (progress) => {
        console.log(`Progress: ${progress.completed}/${progress.total} - ${progress.currentUrl}`);
      },
    });

    console.log("\nScrape completed!\n");
    console.log("Results:");

    for (const page of result.data) {
      console.log(`\n  ${page.metadata.baseUrl}`);
      console.log(`     Title: ${page.metadata.website.title}`);
      console.log(`     Duration: ${page.metadata.duration}ms`);

      // Show which proxy was used (if available)
      if (page.metadata.proxy) {
        console.log(`     Proxy: ${page.metadata.proxy.host}:${page.metadata.proxy.port}`);
        if (page.metadata.proxy.country) {
          console.log(`     Country: ${page.metadata.proxy.country}`);
        }
      }
    }

    console.log("\nBatch Metadata:");
    console.log(`  Total URLs: ${result.batchMetadata.totalUrls}`);
    console.log(`  Successful: ${result.batchMetadata.successfulUrls}`);
    console.log(`  Failed: ${result.batchMetadata.failedUrls}`);
    console.log(`  Total Duration: ${result.batchMetadata.totalDuration}ms`);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/basic/README.md`
```markdown
# Basic Examples

Simple examples demonstrating core Reader functionality.

## Prerequisites

Before running examples, start Ulixee Cloud in a separate terminal:

```bash
npx @ulixee/cloud start
```

For production server usage with shared Core, see [examples/production/express-server](../production/express-server/).

## Examples

### basic-scrape.ts

Scrape a single URL and display the results.

```bash
npx tsx basic-scrape.ts
```

### batch-scrape.ts

Scrape multiple URLs concurrently.

```bash
npx tsx batch-scrape.ts
```

### crawl-website.ts

Crawl a website to discover and scrape pages.

```bash
# Crawl example.com
npx tsx crawl-website.ts

# Crawl a specific URL
npx tsx crawl-website.ts https://docs.example.com
```

### all-formats.ts

Output content in all supported formats (markdown, html).

```bash
npx tsx all-formats.ts
```

### with-proxy.ts

Scrape using a proxy server.

```bash
# Set proxy URL
export PROXY_URL="http://user:pass@proxy.example.com:8080"
npx tsx with-proxy.ts
```

## Running Examples

1. Install dependencies in the examples folder:
   ```bash
   cd examples
   npm install
   ```

2. Run any example:
   ```bash
   npx tsx <example-name>.ts
   ```
```

## File: `examples/basic/with-proxy.ts`
```typescript
#!/usr/bin/env node
/**
 * Proxy Example
 *
 * Demonstrates scraping with a proxy configuration
 */

import { ReaderClient } from "@vakra-dev/reader";

async function main() {
  console.log("Starting proxy example\n");

  // Example proxy configurations:
  //
  // 1. Simple proxy URL:
  // proxy: { url: "http://user:pass@proxy.example.com:8080" }
  //
  // 2. Residential proxy with country targeting:
  // proxy: {
  //   type: "residential",
  //   host: "geo.iproyal.com",
  //   port: 12321,
  //   username: "customer-user",
  //   password: "password",
  //   country: "us"
  // }
  //
  // 3. Datacenter proxy:
  // proxy: {
  //   type: "datacenter",
  //   host: "proxy.example.com",
  //   port: 8080,
  //   username: "user",
  //   password: "pass"
  // }

  // For this example, we'll skip the proxy if not configured
  const proxyUrl = process.env.PROXY_URL;

  if (!proxyUrl) {
    console.log("No PROXY_URL environment variable set.");
    console.log("Set PROXY_URL=http://user:pass@host:port to test proxy scraping.");
    console.log("\nRunning without proxy...\n");
  }

  const reader = new ReaderClient({ verbose: true });

  try {
    const result = await reader.scrape({
      urls: ["https://httpbin.org/ip"], // Shows your IP address
      formats: ["markdown"],
      proxy: proxyUrl ? { url: proxyUrl } : undefined,
    });

    const page = result.data[0];

    if (!page) {
      console.error("No data returned - scrape may have failed");
      console.log("Errors:", result.batchMetadata.errors);
      process.exit(1);
    }

    console.log("\nScrape completed!");
    console.log("\nResponse (should show proxy IP if configured):");
    console.log(page.markdown);
  } catch (error: any) {
    console.error("Error:", error.message);
    process.exit(1);
  } finally {
    await reader.close();
  }
}

main();
```

## File: `examples/deployment/README.md`
```markdown
# Deployment Examples

Guides for deploying Reader to various platforms.

## Available Guides

### Docker

Containerized deployment with Docker and docker-compose.

[View Example](./docker/)

- Dockerfile with Chrome dependencies
- docker-compose.yml for easy deployment
- Health checks and graceful shutdown
- Production tips

### AWS Lambda

Serverless deployment on AWS Lambda.

[View Example](./aws-lambda/)

- Container-based Lambda function
- API Gateway integration
- Remote browser service recommendation

### Vercel Functions

Serverless deployment on Vercel.

[View Example](./vercel-functions/)

- Serverless function setup
- Remote browser integration
- Edge function alternative

## Platform Recommendations

| Platform | Browser Support | Best For |
|----------|----------------|----------|
| Docker/K8s | Full | Production workloads |
| AWS ECS/Fargate | Full | Scalable cloud deployment |
| AWS EC2 | Full | Full control |
| AWS Lambda | Limited* | Low-traffic, with remote browser |
| Vercel | Limited* | Low-traffic, with remote browser |
| Fly.io | Full | Easy global deployment |
| Railway | Full | Simple deployment |

\* Running Chrome in serverless has significant limitations. Use remote browser services for best results.

## Remote Browser Services

For serverless platforms, consider using a remote browser service:

- [Browserless](https://browserless.io) - Chrome as a service
- [Browserbase](https://browserbase.com) - Headless browser infrastructure
- [Apify](https://apify.com) - Web scraping platform
- Self-hosted: Deploy Chrome in a container with WebSocket access
```

## File: `examples/deployment/aws-lambda/handler.ts`
```typescript
/**
 * AWS Lambda Handler for Reader
 *
 * NOTE: Running a full browser in Lambda requires special configuration:
 * - Use Lambda container images (not zip packages)
 * - Include Chrome/Chromium in the container
 * - Configure sufficient memory (2GB+)
 * - Set longer timeout (30-60 seconds)
 *
 * Consider using AWS ECS/Fargate for production browser workloads.
 */

import { ReaderClient } from "@vakra-dev/reader";
import type { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";

interface ScrapeRequest {
  urls: string[];
  formats?: string[];
}

// Reuse client across warm Lambda invocations
let reader: ReaderClient | null = null;

async function getReader(): Promise<ReaderClient> {
  if (!reader) {
    reader = new ReaderClient();
    await reader.start();
  }
  return reader;
}

export async function handler(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  // CORS headers
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };

  // Handle preflight
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 200, headers, body: "" };
  }

  try {
    // Parse request body
    const body: ScrapeRequest = JSON.parse(event.body || "{}");

    if (!body.urls || !Array.isArray(body.urls) || body.urls.length === 0) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({
          success: false,
          error: "urls is required and must be a non-empty array",
        }),
      };
    }

    // Limit URLs per request
    if (body.urls.length > 5) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({
          success: false,
          error: "Maximum 5 URLs per request",
        }),
      };
    }

    // Get or initialize reader client
    const client = await getReader();

    // Scrape URLs
    const result = await client.scrape({
      urls: body.urls,
      formats: (body.formats as any) || ["markdown"],
      batchConcurrency: 1, // Sequential in Lambda
      timeoutMs: 25000, // Leave buffer for Lambda timeout
    });

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        data: result.data,
        batchMetadata: result.batchMetadata,
      }),
    };
  } catch (error: any) {
    console.error("Lambda error:", error);

    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({
        success: false,
        error: error.message || "Internal server error",
      }),
    };
  }
}
```

## File: `examples/deployment/aws-lambda/README.md`
```markdown
# AWS Lambda Deployment

Deploy Reader as an AWS Lambda function.

## Important Considerations

Running a full browser in Lambda is challenging due to:
- Cold start times (Chrome takes 5-10+ seconds to start)
- Memory requirements (2GB+ recommended)
- Binary size limits
- Execution time limits

**Recommendation**: For production browser workloads, consider:
- **AWS ECS/Fargate**: Better suited for long-running browser processes
- **AWS EC2**: Full control over browser lifecycle
- **External Browser Service**: Use Browserless, Browserbase, or similar

## Lambda Container Approach

If you still want to use Lambda, use container images:

### Dockerfile

```dockerfile
FROM public.ecr.aws/lambda/nodejs:18

# Install Chrome dependencies
RUN yum install -y \
    alsa-lib \
    atk \
    cups-libs \
    gtk3 \
    ipa-gothic-fonts \
    libXcomposite \
    libXcursor \
    libXdamage \
    libXext \
    libXi \
    libXrandr \
    libXScrnSaver \
    libXtst \
    pango \
    xorg-x11-fonts-100dpi \
    xorg-x11-fonts-75dpi \
    xorg-x11-fonts-cyrillic \
    xorg-x11-fonts-misc \
    xorg-x11-fonts-Type1 \
    xorg-x11-utils

# Copy function code
COPY package*.json ./
RUN npm install --production
COPY . .

CMD ["handler.handler"]
```

### Build and Deploy

```bash
# Build container
docker build -t reader-lambda .

# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REPO
docker tag reader-lambda:latest $ECR_REPO/reader-lambda:latest
docker push $ECR_REPO/reader-lambda:latest

# Create/update Lambda
aws lambda create-function \
  --function-name reader \
  --package-type Image \
  --code ImageUri=$ECR_REPO/reader-lambda:latest \
  --role arn:aws:iam::ACCOUNT:role/lambda-role \
  --memory-size 2048 \
  --timeout 60
```

## API Gateway Integration

```yaml
# SAM template
Resources:
  ReaderFunction:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      MemorySize: 2048
      Timeout: 60
      Events:
        Api:
          Type: Api
          Properties:
            Path: /scrape
            Method: post
```

## Alternative: Use Remote Browser

Instead of running Chrome in Lambda, connect to a remote browser service:

```typescript
import { scrape } from "@vakra-dev/reader";

const result = await scrape({
  urls: ["https://example.com"],
  connectionToCore: "wss://browserless.io?token=YOUR_TOKEN",
});
```

This approach:
- Eliminates cold starts
- No Chrome binary in Lambda
- Faster, more reliable
- Scales independently
```

## File: `examples/deployment/docker/docker-compose.yml`
```yaml
version: '3.8'

services:
  reader:
    # Force x86_64 for Chrome compatibility (Hero bundles x86_64 Chromium)
    platform: linux/amd64
    build:
      context: ../../..
      dockerfile: examples/deployment/docker/Dockerfile
    ports:
      - "3001:3001"
    environment:
      - PORT=3001
      - NODE_ENV=production
      # Optional: Proxy configuration
      # - PROXY_URL=http://user:pass@proxy:8080
    restart: unless-stopped
    # Increase shared memory for Chrome
    shm_size: '2gb'
    # Security options for Chrome
    security_opt:
      - seccomp:unconfined
    # Disable Chrome sandbox (redundant with noChromeSandbox but helps with some setups)
    cap_add:
      - SYS_ADMIN
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:3001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
```

## File: `examples/deployment/docker/Dockerfile`
```
# Reader Docker Image
# Containerizes the Express server example with Hero browser

FROM node:22-slim

# Install Chrome dependencies for Hero (based on Ulixee Cloud Docker setup)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    curl \
    # Fonts for proper rendering
    fonts-liberation \
    fonts-freefont-ttf \
    # Virtual framebuffer for headless Chrome
    xvfb \
    # Chrome dependencies
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    libxshmfence1 \
    libxss1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Configure shared memory for Chrome
RUN chmod +x /dev/shm

# Set working directory
WORKDIR /app

# Copy reader package
COPY package.json ./
COPY src ./src

# Install reader dependencies
RUN npm install

# Copy examples package.json and install
COPY examples/package.json ./examples/
WORKDIR /app/examples
RUN npm install

# Install browser dependencies (official Ulixee method)
RUN npx install-browser-deps || true

# Copy express server code
COPY examples/production ./production

# Install tsx globally for running TypeScript
RUN npm install -g tsx

# Expose port
EXPOSE 3001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3001/health || exit 1

# Set display for xvfb
ENV DISPLAY=:99

# Run with xvfb virtual display for Chrome
CMD xvfb-run --auto-servernum --server-args="-screen 0 1920x1080x24" tsx production/express-server/src/index.ts
```

## File: `examples/deployment/docker/README.md`
```markdown
# Docker Deployment

Run Reader as a REST API server in a Docker container.

## Platform Requirements

**Supported:**
- x86_64 Linux servers (native)
- x86_64 cloud VMs (AWS EC2, GCP, Azure, DigitalOcean)

**Not Supported:**
- Apple Silicon Macs (M1/M2/M3) - Hero bundles x86_64 Chromium which doesn't run stably under Rosetta 2/QEMU emulation

### Apple Silicon Workarounds

If you're developing on an Apple Silicon Mac:

1. **Run locally without Docker** (recommended for development):
   ```bash
   cd examples/production/express-server
   npx tsx src/index.ts
   ```

2. **Deploy to a cloud VM** for Docker testing:
   - Use an x86_64 Linux VM (AWS t3.medium, DigitalOcean droplet, etc.)
   - Docker runs natively without emulation issues

3. **Use a remote browser service**:
   ```typescript
   const result = await scrape({
     urls: ["https://example.com"],
     connectionToCore: "wss://chrome.browserless.io?token=YOUR_TOKEN",
   });
   ```

## Quick Start

From the `reader` package directory:

```bash
cd examples/deployment/docker
docker-compose up -d
```

The server will be available at http://localhost:3001

## API Endpoints

```bash
# Health check
curl http://localhost:3001/health

# Scrape a URL
curl -X POST http://localhost:3001/scrape \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com"], "formats": ["markdown"]}'

# Crawl a website
curl -X POST http://localhost:3001/crawl \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "depth": 1, "maxPages": 10}'
```

## Manual Build

From the `reader` package directory:

```bash
# Build image
docker build -t reader -f examples/deployment/docker/Dockerfile .

# Run container
docker run -d \
  --name reader \
  -p 3001:3001 \
  --shm-size=2gb \
  --security-opt seccomp=unconfined \
  --cap-add SYS_ADMIN \
  reader
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| PORT | 3001 | Server port |
| NODE_ENV | production | Node environment |
| PROXY_URL | - | Optional proxy URL |

### Resource Requirements

- **Memory**: Minimum 2GB RAM (4GB recommended)
- **Shared Memory**: 2GB (`--shm-size=2gb`) required for Chrome
- **CPU**: 1+ cores (2+ recommended for concurrent scraping)

## Logs

```bash
# View logs
docker-compose logs -f

# Check health status
docker inspect --format='{{.State.Health.Status}}' reader
```

## Stop

```bash
docker-compose down
```

## Troubleshooting

### Chrome Crashes

Increase shared memory:

```bash
docker run --shm-size=4gb ...
```

### Network Issues

Use host network mode for debugging:

```bash
docker run --network=host ...
```

### Architecture Issues (Apple Silicon)

If you see errors like:
- `qemu-x86_64: Could not open '/lib64/ld-linux-x86-64.so.2'`
- `Page has been closed` during scrape operations
- Chrome crashes or ECONNRESET errors

This is due to x86_64 emulation instability on ARM64 Macs. See "Platform Requirements" above for workarounds.
```

## File: `examples/deployment/vercel-functions/README.md`
```markdown
# Vercel Functions Deployment

Deploy Reader as Vercel Serverless Functions.

## Important Notes

Running a full browser in Vercel Functions is not recommended due to:
- Cold start times
- Memory limits
- Binary size restrictions
- Execution time limits (10-30 seconds)

**Recommended approach**: Use a remote browser service.

## Setup with Remote Browser

1. Sign up for a browser service:
   - [Browserless](https://browserless.io)
   - [Browserbase](https://browserbase.com)
   - Or self-hosted

2. Set environment variable:
   ```bash
   vercel env add BROWSER_WS_ENDPOINT
   # Enter: wss://chrome.browserless.io?token=YOUR_TOKEN
   ```

3. Deploy:
   ```bash
   vercel deploy
   ```

## Project Structure

```
vercel-functions/
├── api/
│   └── scrape.ts    # /api/scrape endpoint
├── package.json
└── vercel.json
```

## Configuration

### vercel.json

```json
{
  "functions": {
    "api/scrape.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

### package.json

```json
{
  "dependencies": {
    "@vakra-dev/reader": "^1.0.0"
  }
}
```

## Usage

```bash
curl -X POST https://your-app.vercel.app/api/scrape \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com"]}'
```

## Alternative: Edge Functions

For better performance, use Vercel Edge Functions with a fetch-based approach:

```typescript
// api/scrape-edge.ts
export const config = {
  runtime: "edge",
};

export default async function handler(req: Request) {
  // Use fetch to call Reader running elsewhere
  const response = await fetch("https://your-reader.com/scrape", {
    method: "POST",
    body: req.body,
  });
  return response;
}
```

This approach:
- Sub-second cold starts
- Global edge network
- Lower latency for users
```

## File: `examples/deployment/vercel-functions/api/scrape.ts`
```typescript
/**
 * Vercel Serverless Function for Reader
 *
 * NOTE: Vercel Functions have similar limitations to AWS Lambda.
 * For browser workloads, consider using Vercel Edge Functions with
 * a remote browser service, or deploy to a different platform.
 *
 * This example demonstrates connecting to an external browser service.
 */

import { scrape } from "@vakra-dev/reader";
import type { VercelRequest, VercelResponse } from "@vercel/node";

// Use a remote browser service (recommended for serverless)
const BROWSER_WS_ENDPOINT = process.env.BROWSER_WS_ENDPOINT;

export default async function handler(req: VercelRequest, res: VercelResponse) {
  // CORS
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({
      success: false,
      error: "Method not allowed",
    });
  }

  try {
    const { urls, formats } = req.body;

    if (!urls || !Array.isArray(urls) || urls.length === 0) {
      return res.status(400).json({
        success: false,
        error: "urls is required and must be a non-empty array",
      });
    }

    // Limit URLs per request (serverless timeout constraints)
    if (urls.length > 3) {
      return res.status(400).json({
        success: false,
        error: "Maximum 3 URLs per request",
      });
    }

    // Check for browser endpoint
    if (!BROWSER_WS_ENDPOINT) {
      return res.status(500).json({
        success: false,
        error: "BROWSER_WS_ENDPOINT not configured. Set up Browserless, Browserbase, or similar.",
      });
    }

    const result = await scrape({
      urls,
      formats: formats || ["markdown"],
      batchConcurrency: 1,
      timeoutMs: 25000, // Leave buffer for Vercel timeout
      connectionToCore: BROWSER_WS_ENDPOINT,
    });

    return res.status(200).json({
      success: true,
      data: result.data,
      batchMetadata: result.batchMetadata,
    });
  } catch (error: any) {
    console.error("Vercel function error:", error);

    return res.status(500).json({
      success: false,
      error: error.message || "Internal server error",
    });
  }
}

export const config = {
  maxDuration: 30, // Maximum execution time in seconds
};
```

## File: `examples/production/README.md`
```markdown
# Production Examples

Production-ready setups for running Reader at scale.

## Available Examples

### [Express Server](./express-server/)

A full-featured REST API server with:
- Health checks and graceful shutdown
- Scrape and crawl endpoints
- Shared Hero Core for efficiency
- Request validation and error handling

### [Job Queue (BullMQ)](./job-queue-bullmq/)

Async job processing with Redis:
- Submit jobs via API, process in background
- Progress tracking and webhook notifications
- Automatic retries with exponential backoff
- Horizontally scalable workers

### [Browser Pool Scaling](./browser-pool-scaling/)

Advanced browser pool management:
- Pool metrics (JSON and Prometheus formats)
- Health checks with auto-recovery
- Browser recycling to prevent memory leaks
- Graceful degradation under load

## Best Practices

1. **Use a Shared Core**: Initialize Hero Core once and share across requests
2. **Implement Health Checks**: Monitor browser pool health
3. **Add Rate Limiting**: Protect against abuse
4. **Use Caching**: Cache scrape results (Redis, Memcached)
5. **Queue Long Operations**: Use job queues for batch scraping
6. **Monitor Resources**: Track memory, CPU, and pool metrics

## Quick Comparison

| Example | Use Case | Dependencies |
|---------|----------|--------------|
| Express Server | Simple REST API | Express |
| Job Queue | Async batch processing | BullMQ, Redis |
| Pool Scaling | High-throughput scraping | Express |

## Getting Started

Each example has its own README with setup instructions:

```bash
# Express Server
cd express-server && npm install && npm start

# Job Queue
cd job-queue-bullmq && npm install
npm run start   # API server
npm run worker  # Worker process

# Pool Scaling
cd browser-pool-scaling && npm install && npm start
```
```

## File: `examples/production/browser-pool-scaling/package.json`
```json
{
  "name": "browser-pool-scaling-example",
  "version": "1.0.0",
  "private": true,
  "description": "Browser pool scaling example with metrics and health monitoring",
  "type": "module",
  "scripts": {
    "start": "npx tsx src/index.ts"
  },
  "dependencies": {
    "@vakra-dev/reader": "file:../../..",
    "express": "^4.18.2"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.6",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

## File: `examples/production/browser-pool-scaling/README.md`
```markdown
# Browser Pool Scaling

Advanced browser pool configuration with metrics, health monitoring, and scaling.

## Overview

This example demonstrates production-grade browser pool management:

- **Pool metrics**: Monitor browser utilization, queue depth, and request latency
- **Health checks**: Detect and recover from unhealthy browsers
- **Auto-recycling**: Prevent memory leaks by retiring browsers after use
- **Prometheus integration**: Export metrics for monitoring dashboards
- **Graceful degradation**: Handle overload without crashing

## Setup

1. Install dependencies:
   ```bash
   cd examples/production/browser-pool-scaling
   npm install
   ```

2. Start the server:
   ```bash
   npm run start
   ```

## API Endpoints

### Health Check

```bash
curl http://localhost:3003/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "uptime": 3600000,
  "uptimeFormatted": "1h 0m",
  "pool": {
    "healthy": true,
    "issues": []
  }
}
```

### Metrics (JSON)

```bash
curl http://localhost:3003/metrics
```

Response:
```json
{
  "pool": {
    "total": 4,
    "available": 2,
    "busy": 2,
    "recycling": 0,
    "unhealthy": 0,
    "queueLength": 0
  },
  "performance": {
    "totalRequests": 150,
    "avgRequestDurationMs": 2500
  },
  "utilization": {
    "percentage": 50,
    "status": "moderate"
  },
  "config": {
    "poolSize": 4,
    "retireAfterPageCount": 50,
    "retireAfterAgeMs": 900000,
    "maxQueueSize": 200,
    "queueTimeout": 120000
  }
}
```

### Metrics (Prometheus)

```bash
curl "http://localhost:3003/metrics?format=prometheus"
```

Response:
```
# HELP reader_pool_total Total browser instances in pool
# TYPE reader_pool_total gauge
reader_pool_total 4

# HELP reader_pool_available Available browser instances
# TYPE reader_pool_available gauge
reader_pool_available 2

# HELP reader_pool_busy Busy browser instances
# TYPE reader_pool_busy gauge
reader_pool_busy 2
...
```

### Scrape URL

```bash
curl -X POST http://localhost:3003/scrape \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

Response:
```json
{
  "success": true,
  "url": "https://example.com",
  "title": "Example Domain",
  "htmlLength": 1256,
  "durationMs": 1523
}
```

### Batch Scrape

```bash
curl -X POST http://localhost:3003/batch \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://example.com", "https://httpbin.org/html"],
    "concurrency": 2
  }'
```

Response:
```json
{
  "success": true,
  "summary": {
    "total": 2,
    "successful": 2,
    "failed": 0,
    "durationMs": 3200,
    "avgPerUrl": 1600
  },
  "results": [...]
}
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 3003 | Server port |
| `POOL_SIZE` | 4 | Number of browser instances |
| `RETIRE_AFTER_PAGES` | 50 | Recycle browser after N pages |
| `RETIRE_AFTER_MS` | 900000 | Recycle browser after 15 minutes |
| `MAX_QUEUE_SIZE` | 200 | Maximum pending requests |
| `QUEUE_TIMEOUT` | 120000 | Request timeout in queue (2 min) |

### Scaling Recommendations

| Use Case | Pool Size | Notes |
|----------|-----------|-------|
| Development | 2 | Low memory usage |
| Small API | 4-8 | Handles ~10 req/min |
| Medium traffic | 8-16 | Handles ~50 req/min |
| High traffic | 16-32+ | Use multiple instances |

### Memory Considerations

Each browser instance uses approximately 100-300MB RAM. Plan accordingly:

| Pool Size | Memory (approx) |
|-----------|-----------------|
| 2 | 400-600 MB |
| 4 | 800 MB - 1.2 GB |
| 8 | 1.6 - 2.4 GB |
| 16 | 3.2 - 4.8 GB |

## Prometheus & Grafana

### Prometheus Configuration

Add to `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'reader'
    scrape_interval: 15s
    metrics_path: /metrics
    params:
      format: ['prometheus']
    static_configs:
      - targets: ['localhost:3003']
```

### Grafana Dashboard

Key metrics to monitor:

1. **Pool Utilization**: `reader_pool_busy / reader_pool_total`
2. **Queue Depth**: `reader_pool_queue_length`
3. **Unhealthy Instances**: `reader_pool_unhealthy`
4. **Request Latency**: `reader_pool_request_duration_avg_ms`

### Alerting Rules

```yaml
groups:
  - name: reader
    rules:
      - alert: HighPoolUtilization
        expr: reader_pool_busy / reader_pool_total > 0.9
        for: 5m
        annotations:
          summary: "Browser pool near capacity"

      - alert: UnhealthyBrowsers
        expr: reader_pool_unhealthy > 0
        for: 2m
        annotations:
          summary: "Unhealthy browser instances detected"

      - alert: HighQueueDepth
        expr: reader_pool_queue_length > 50
        for: 1m
        annotations:
          summary: "Request queue growing"
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Browser Pool                            │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Browser  │  │ Browser  │  │ Browser  │  │ Browser  │    │
│  │   #1     │  │   #2     │  │   #3     │  │   #4     │    │
│  │  (busy)  │  │ (avail)  │  │  (busy)  │  │ (avail)  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
├─────────────────────────────────────────────────────────────┤
│  Request Queue: [req5] [req6] [req7] ...                    │
├─────────────────────────────────────────────────────────────┤
│  Recycler: Checks every 60s, retires old/heavy browsers     │
│  Health Check: Every 5min, marks unhealthy browsers         │
└─────────────────────────────────────────────────────────────┘
```

## Files

```
browser-pool-scaling/
├── README.md           # This file
├── package.json        # Dependencies
└── src/
    └── index.ts        # Server with pool management
```
```

## File: `examples/production/browser-pool-scaling/src/index.ts`
```typescript
/**
 * Browser Pool Scaling Example
 *
 * Demonstrates advanced browser pool configuration with:
 * - Pool metrics endpoint for monitoring
 * - Health checks with detailed status
 * - Graceful degradation under load
 * - Resource cleanup on shutdown
 *
 * Usage: npx tsx src/index.ts
 */

import express, { Request, Response, NextFunction } from "express";
import { BrowserPool } from "@vakra-dev/reader";
import type { PoolConfig } from "@vakra-dev/reader";
import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";

// Global HeroCore instance
let heroCore: HeroCore | null = null;

function createConnectionToCore(): ConnectionToHeroCore {
  if (!heroCore) {
    throw new Error("HeroCore not initialized");
  }
  const bridge = new TransportBridge();
  heroCore.addConnection(bridge.transportToClient);
  return new ConnectionToHeroCore(bridge.transportToCore);
}

// ============================================================================
// Pool Configuration
// ============================================================================

const poolConfig: Partial<PoolConfig> = {
  // Number of browser instances to maintain
  size: parseInt(process.env.POOL_SIZE || "4"),

  // Retire browser after N pages (prevents memory leaks)
  retireAfterPageCount: parseInt(process.env.RETIRE_AFTER_PAGES || "50"),

  // Retire browser after N milliseconds (15 minutes default)
  retireAfterAgeMs: parseInt(process.env.RETIRE_AFTER_MS || String(15 * 60 * 1000)),

  // How often to check for browsers to recycle (1 minute)
  recycleCheckInterval: 60 * 1000,

  // Health check interval (5 minutes)
  healthCheckInterval: 5 * 60 * 1000,

  // Max failures before marking browser unhealthy
  maxConsecutiveFailures: 3,

  // Request queue settings
  maxQueueSize: parseInt(process.env.MAX_QUEUE_SIZE || "200"),
  queueTimeout: parseInt(process.env.QUEUE_TIMEOUT || String(120 * 1000)),
};

// Pool instance (created after HeroCore starts)
let pool: BrowserPool;

const app = express();
const PORT = process.env.PORT || 3003;
const serverStartTime = Date.now();

// Middleware
app.use(express.json({ limit: "1mb" }));

// Request logging
app.use((req: Request, res: Response, next: NextFunction) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// ============================================================================
// Routes
// ============================================================================

/**
 * GET /health - Basic health check
 */
app.get("/health", async (req: Request, res: Response) => {
  try {
    const health = await pool.healthCheck();
    const uptime = Date.now() - serverStartTime;

    res.status(health.healthy ? 200 : 503).json({
      status: health.healthy ? "healthy" : "degraded",
      timestamp: new Date().toISOString(),
      uptime,
      uptimeFormatted: formatDuration(uptime),
      pool: {
        healthy: health.healthy,
        issues: health.issues,
      },
    });
  } catch (error: any) {
    res.status(503).json({
      status: "unhealthy",
      error: error.message,
    });
  }
});

/**
 * GET /metrics - Detailed pool metrics (Prometheus-compatible format available)
 */
app.get("/metrics", (req: Request, res: Response) => {
  const stats = pool.getStats();
  const format = req.query.format;

  if (format === "prometheus") {
    // Prometheus exposition format
    const lines = [
      `# HELP reader_pool_total Total browser instances in pool`,
      `# TYPE reader_pool_total gauge`,
      `reader_pool_total ${stats.total}`,
      ``,
      `# HELP reader_pool_available Available browser instances`,
      `# TYPE reader_pool_available gauge`,
      `reader_pool_available ${stats.available}`,
      ``,
      `# HELP reader_pool_busy Busy browser instances`,
      `# TYPE reader_pool_busy gauge`,
      `reader_pool_busy ${stats.busy}`,
      ``,
      `# HELP reader_pool_recycling Browser instances being recycled`,
      `# TYPE reader_pool_recycling gauge`,
      `reader_pool_recycling ${stats.recycling}`,
      ``,
      `# HELP reader_pool_unhealthy Unhealthy browser instances`,
      `# TYPE reader_pool_unhealthy gauge`,
      `reader_pool_unhealthy ${stats.unhealthy}`,
      ``,
      `# HELP reader_pool_queue_length Pending requests in queue`,
      `# TYPE reader_pool_queue_length gauge`,
      `reader_pool_queue_length ${stats.queueLength}`,
      ``,
      `# HELP reader_pool_requests_total Total requests processed`,
      `# TYPE reader_pool_requests_total counter`,
      `reader_pool_requests_total ${stats.totalRequests}`,
      ``,
      `# HELP reader_pool_request_duration_avg_ms Average request duration`,
      `# TYPE reader_pool_request_duration_avg_ms gauge`,
      `reader_pool_request_duration_avg_ms ${stats.avgRequestDuration.toFixed(2)}`,
    ];

    res.set("Content-Type", "text/plain; version=0.0.4");
    res.send(lines.join("\n"));
  } else {
    // JSON format
    res.json({
      pool: {
        total: stats.total,
        available: stats.available,
        busy: stats.busy,
        recycling: stats.recycling,
        unhealthy: stats.unhealthy,
        queueLength: stats.queueLength,
      },
      performance: {
        totalRequests: stats.totalRequests,
        avgRequestDurationMs: Math.round(stats.avgRequestDuration),
      },
      utilization: {
        percentage: stats.total > 0 ? Math.round((stats.busy / stats.total) * 100) : 0,
        status: getUtilizationStatus(stats),
      },
      config: {
        poolSize: poolConfig.size,
        retireAfterPageCount: poolConfig.retireAfterPageCount,
        retireAfterAgeMs: poolConfig.retireAfterAgeMs,
        maxQueueSize: poolConfig.maxQueueSize,
        queueTimeout: poolConfig.queueTimeout,
      },
    });
  }
});

/**
 * POST /scrape - Scrape a URL using the pool
 */
app.post("/scrape", async (req: Request, res: Response) => {
  const { url, waitForSelector, timeout } = req.body;

  // Validation
  if (!url || typeof url !== "string") {
    return res.status(400).json({
      success: false,
      error: "url is required and must be a string",
    });
  }

  try {
    new URL(url);
  } catch {
    return res.status(400).json({
      success: false,
      error: `Invalid URL: ${url}`,
    });
  }

  const startTime = Date.now();

  try {
    const result = await pool.withBrowser(async (hero) => {
      // Navigate to URL
      await hero.goto(url);

      // Wait for selector if specified
      if (waitForSelector) {
        await hero.waitForElement(hero.document.querySelector(waitForSelector), {
          timeoutMs: timeout || 30000,
        });
      } else {
        await hero.waitForLoad("AllContentLoaded");
      }

      // Extract content
      const html = await hero.document.documentElement.outerHTML;
      const title = await hero.document.title;

      return { html, title };
    });

    const duration = Date.now() - startTime;

    res.json({
      success: true,
      url,
      title: result.title,
      htmlLength: result.html.length,
      durationMs: duration,
    });
  } catch (error: any) {
    const duration = Date.now() - startTime;

    console.error(`[Scrape] Error for ${url}:`, error.message);

    res.status(500).json({
      success: false,
      url,
      error: error.message,
      durationMs: duration,
    });
  }
});

/**
 * POST /batch - Scrape multiple URLs concurrently
 */
app.post("/batch", async (req: Request, res: Response) => {
  const { urls, concurrency = 2 } = req.body;

  // Validation
  if (!urls || !Array.isArray(urls) || urls.length === 0) {
    return res.status(400).json({
      success: false,
      error: "urls is required and must be a non-empty array",
    });
  }

  const startTime = Date.now();
  const results: Array<{ url: string; success: boolean; title?: string; error?: string }> = [];

  // Process URLs with limited concurrency
  const chunks: string[][] = [];
  for (let i = 0; i < urls.length; i += concurrency) {
    chunks.push(urls.slice(i, i + concurrency));
  }

  for (const chunk of chunks) {
    const chunkResults = await Promise.allSettled(
      chunk.map(async (url: string) => {
        try {
          const result = await pool.withBrowser(async (hero) => {
            await hero.goto(url);
            await hero.waitForLoad("AllContentLoaded");
            const title = await hero.document.title;
            return { url, success: true, title };
          });
          return result;
        } catch (error: any) {
          return { url, success: false, error: error.message };
        }
      })
    );

    for (const result of chunkResults) {
      if (result.status === "fulfilled") {
        results.push(result.value);
      } else {
        results.push({ url: "unknown", success: false, error: result.reason?.message });
      }
    }
  }

  const duration = Date.now() - startTime;
  const successCount = results.filter((r) => r.success).length;

  res.json({
    success: true,
    summary: {
      total: urls.length,
      successful: successCount,
      failed: urls.length - successCount,
      durationMs: duration,
      avgPerUrl: Math.round(duration / urls.length),
    },
    results,
  });
});

// ============================================================================
// Helpers
// ============================================================================

function formatDuration(ms: number): string {
  const seconds = Math.floor(ms / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (days > 0) return `${days}d ${hours % 24}h`;
  if (hours > 0) return `${hours}h ${minutes % 60}m`;
  if (minutes > 0) return `${minutes}m ${seconds % 60}s`;
  return `${seconds}s`;
}

function getUtilizationStatus(stats: { total: number; busy: number; queueLength: number }): string {
  const utilization = stats.total > 0 ? stats.busy / stats.total : 0;

  if (stats.queueLength > 0) return "saturated";
  if (utilization > 0.8) return "high";
  if (utilization > 0.5) return "moderate";
  if (utilization > 0) return "low";
  return "idle";
}

// ============================================================================
// Error handling
// ============================================================================

app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  console.error("[Server Error]", err);
  res.status(500).json({
    success: false,
    error: err.message || "Internal server error",
  });
});

// 404 handler
app.use((req: Request, res: Response) => {
  res.status(404).json({
    success: false,
    error: `Not found: ${req.method} ${req.path}`,
  });
});

// ============================================================================
// Start server
// ============================================================================

async function startServer() {
  try {
    // Start HeroCore first
    console.log("[Pool] Starting HeroCore...");
    heroCore = new HeroCore();
    await heroCore.start();
    console.log("[Pool] HeroCore started");

    // Create pool with connection to HeroCore
    console.log("[Pool] Initializing browser pool...");
    pool = new BrowserPool(
      poolConfig,
      undefined, // proxy
      false, // showChrome
      createConnectionToCore()
    );
    await pool.initialize();
    console.log(`[Pool] Pool initialized with ${poolConfig.size} browsers`);

    app.listen(PORT, () => {
      console.log(`
╔════════════════════════════════════════════════════════════════╗
║       Reader - Browser Pool Scaling Example             ║
╠════════════════════════════════════════════════════════════════╣
║  Server running on http://localhost:${PORT}                       ║
╠════════════════════════════════════════════════════════════════╣
║  Endpoints:                                                    ║
║    GET  /health           - Health check with pool status      ║
║    GET  /metrics          - Pool metrics (JSON or Prometheus)  ║
║    POST /scrape           - Scrape a single URL                ║
║    POST /batch            - Scrape multiple URLs               ║
╠════════════════════════════════════════════════════════════════╣
║  Pool Configuration:                                           ║
║    Size: ${poolConfig.size} browsers                                        ║
║    Retire after: ${poolConfig.retireAfterPageCount} pages or ${Math.round((poolConfig.retireAfterAgeMs || 0) / 60000)}min             ║
║    Max queue: ${poolConfig.maxQueueSize} requests                                ║
╚════════════════════════════════════════════════════════════════╝
      `);
    });

    // Graceful shutdown
    const shutdown = async () => {
      console.log("\n[Pool] Shutting down...");
      await pool.shutdown();
      if (heroCore) {
        await heroCore.close();
      }
      console.log("[Pool] Pool shutdown complete");
      process.exit(0);
    };

    process.on("SIGINT", shutdown);
    process.on("SIGTERM", shutdown);
  } catch (error: any) {
    console.error("[Pool] Failed to start:", error.message);
    process.exit(1);
  }
}

startServer();
```

## File: `examples/production/express-server/package.json`
```json
{
  "name": "reader-express-server",
  "version": "1.0.0",
  "private": true,
  "description": "Express server example for @vakra-dev/reader",
  "type": "module",
  "scripts": {
    "start": "npx tsx src/index.ts",
    "dev": "npx tsx --watch src/index.ts"
  },
  "dependencies": {
    "@ulixee/hero": "^2.0.0-alpha.34",
    "@ulixee/hero-core": "^2.0.0-alpha.34",
    "@ulixee/net": "^2.0.0-alpha.29",
    "@vakra-dev/reader": "^1.0.0",
    "express": "^4.18.2"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.6",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

## File: `examples/production/express-server/README.md`
```markdown
# Express Server Example

A production-ready Express server exposing Reader as a REST API.

## Features

- Health check endpoint
- Scrape endpoint (single and batch)
- Crawl endpoint
- Shared Hero Core for efficiency
- Graceful shutdown handling

## Setup

```bash
cd examples
npm install
```

## Usage

```bash
# Start the server
npx tsx production/express-server/src/index.ts
```

Server runs on http://localhost:3001

## API Endpoints

### GET /health

Health check endpoint.

```bash
curl http://localhost:3001/health
```

### POST /scrape

Scrape one or more URLs.

```bash
curl -X POST http://localhost:3001/scrape \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://example.com"],
    "formats": ["markdown", "html"]
  }'
```

**Request body:**
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| urls | string[] | required | URLs to scrape |
| formats | string[] | ["markdown"] | Output formats |
| batchConcurrency | number | 1 | Parallel requests |
| verbose | boolean | false | Enable logging |

### POST /crawl

Crawl a website to discover pages.

```bash
curl -X POST http://localhost:3001/crawl \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "depth": 2,
    "maxPages": 20,
    "scrape": true
  }'
```

**Request body:**
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| url | string | required | Seed URL |
| depth | number | 1 | Max depth (0-5) |
| maxPages | number | 20 | Max pages (1-100) |
| scrape | boolean | false | Also scrape content |

## Why Shared Hero Core?

This server uses a shared Hero Core instance instead of letting each request create its own:

| Approach | Startup Time | Memory | Best For |
|----------|--------------|--------|----------|
| Per-request Core | ~5-10s | High (each request) | Scripts, CLI |
| Shared Core | Once at startup | Shared across requests | Servers |

The shared Core is initialized once when the server starts, and all incoming requests share it via `TransportBridge`. This approach:

- **Eliminates cold starts** - No browser startup delay per request
- **Reduces memory usage** - Single Core instance shared across all requests
- **Improves throughput** - Requests don't wait for Core initialization

See [src/index.ts](./src/index.ts) for the implementation.

## Docker

See the [Docker deployment example](../../deployment/docker) for containerized deployment.

## Production Considerations

1. **Rate Limiting**: Add rate limiting middleware
2. **Authentication**: Add API key authentication
3. **Caching**: Cache scrape results (Redis, etc.)
4. **Queue**: Use job queue for async processing
5. **Monitoring**: Add metrics and logging
```

## File: `examples/production/express-server/src/index.ts`
```typescript
/**
 * Express Server Example for Reader
 *
 * Demonstrates how to run Reader as a REST API.
 * Uses ReaderClient which manages the HeroCore lifecycle internally.
 *
 * Key concepts:
 * - Initialize ReaderClient once at startup
 * - Reuse the same client for all requests
 * - Graceful shutdown to properly close the client
 */

import express, { Request, Response, NextFunction } from "express";
import { ReaderClient } from "@vakra-dev/reader";
import type { ScrapeResult, CrawlResult } from "@vakra-dev/reader";

// Global ReaderClient instance (initialized in startServer)
let reader: ReaderClient | null = null;

const app = express();
const PORT = process.env.PORT || 3001;
const serverStartTime = Date.now();

// Middleware
app.use(express.json({ limit: "10mb" }));

// Request logging
app.use((req: Request, res: Response, next: NextFunction) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// ============================================================================
// Routes
// ============================================================================

/**
 * GET /health - Health check endpoint
 */
app.get("/health", (req: Request, res: Response) => {
  const uptime = Date.now() - serverStartTime;

  res.json({
    status: "healthy",
    timestamp: new Date().toISOString(),
    uptime,
    uptimeFormatted: `${Math.floor(uptime / 1000)}s`,
  });
});

/**
 * POST /scrape - Scrape one or more URLs
 *
 * Request body:
 * {
 *   urls: string[]              // Required
 *   formats?: string[]          // Default: ['markdown']
 *   batchConcurrency?: number   // Default: 1
 *   waitForSelector?: string
 *   screenshot?: boolean
 *   verbose?: boolean
 *   showChrome?: boolean
 *   proxy?: ProxyConfig
 * }
 */
app.post("/scrape", async (req: Request, res: Response) => {
  try {
    const { urls, formats, ...options } = req.body;

    // Validation
    if (!urls || !Array.isArray(urls) || urls.length === 0) {
      return res.status(400).json({
        success: false,
        error: "urls is required and must be a non-empty array",
      });
    }

    // Validate URLs
    for (const url of urls) {
      try {
        new URL(url);
      } catch {
        return res.status(400).json({
          success: false,
          error: `Invalid URL: ${url}`,
        });
      }
    }

    // Validate formats if provided
    if (formats) {
      const validFormats = ["markdown", "html"];
      if (!Array.isArray(formats) || !formats.every((f: string) => validFormats.includes(f))) {
        return res.status(400).json({
          success: false,
          error: "formats must be an array of: markdown, html",
        });
      }
    }

    console.log(`[scrape] Starting scrape of ${urls.length} URL(s)`);

    if (!reader) {
      throw new Error("ReaderClient not initialized");
    }

    const result: ScrapeResult = await reader.scrape({
      urls,
      formats: formats || ["markdown"],
      ...options,
    });

    console.log(
      `[scrape] Completed: ${result.batchMetadata.successfulUrls}/${result.batchMetadata.totalUrls} successful`
    );

    res.json({
      success: true,
      data: result.data,
      batchMetadata: result.batchMetadata,
    });
  } catch (error: any) {
    console.error("[scrape] Error:", error);
    res.status(500).json({
      success: false,
      error: error.message || "Scrape failed",
    });
  }
});

/**
 * POST /crawl - Crawl a website
 *
 * Request body:
 * {
 *   url: string        // Required - seed URL
 *   depth?: number     // Default: 1, max: 5
 *   maxPages?: number  // Default: 20, max: 100
 *   scrape?: boolean   // Also scrape full content
 * }
 */
app.post("/crawl", async (req: Request, res: Response) => {
  try {
    const { url, depth, maxPages, scrape: shouldScrape } = req.body;

    // Validation
    if (!url || typeof url !== "string") {
      return res.status(400).json({
        success: false,
        error: "url is required and must be a string",
      });
    }

    try {
      new URL(url);
    } catch {
      return res.status(400).json({
        success: false,
        error: `Invalid URL: ${url}`,
      });
    }

    // Validate depth
    if (depth !== undefined && (typeof depth !== "number" || depth < 0 || depth > 5)) {
      return res.status(400).json({
        success: false,
        error: "depth must be a number between 0 and 5",
      });
    }

    // Validate maxPages
    if (
      maxPages !== undefined &&
      (typeof maxPages !== "number" || maxPages < 1 || maxPages > 100)
    ) {
      return res.status(400).json({
        success: false,
        error: "maxPages must be a number between 1 and 100",
      });
    }

    console.log(`[crawl] Starting crawl of ${url} (depth: ${depth || 1})`);

    if (!reader) {
      throw new Error("ReaderClient not initialized");
    }

    const result: CrawlResult = await reader.crawl({
      url,
      depth: depth || 1,
      maxPages: maxPages || 20,
      scrape: shouldScrape || false,
    });

    console.log(`[crawl] Completed: found ${result.urls.length} URLs`);

    res.json({
      success: true,
      urls: result.urls,
      scraped: result.scraped
        ? {
            success: true,
            data: result.scraped.data,
            batchMetadata: result.scraped.batchMetadata,
          }
        : undefined,
      metadata: result.metadata,
    });
  } catch (error: any) {
    console.error("[crawl] Error:", error);
    res.status(500).json({
      success: false,
      error: error.message || "Crawl failed",
    });
  }
});

// ============================================================================
// Error handling
// ============================================================================

app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  console.error("[Server Error]", err);
  res.status(500).json({
    success: false,
    error: err.message || "Internal server error",
  });
});

// 404 handler
app.use((req: Request, res: Response) => {
  res.status(404).json({
    success: false,
    error: `Not found: ${req.method} ${req.path}`,
  });
});

// ============================================================================
// Start server
// ============================================================================

// Initialize ReaderClient and start Express server
async function startServer() {
  try {
    // Initialize ReaderClient (starts HeroCore internally)
    reader = new ReaderClient({ verbose: true });
    await reader.start();
    console.log("[reader] ReaderClient started");

    app.listen(PORT, () => {
      console.log(`
╔════════════════════════════════════════════════════════════════╗
║       Reader - Express Server Example                   ║
╠════════════════════════════════════════════════════════════════╣
║  Server running on http://localhost:${PORT}                    ║
╠════════════════════════════════════════════════════════════════╣
║  Endpoints:                                                    ║
║    GET  /health  - Health check                                ║
║    POST /scrape  - Scrape URLs                                 ║
║    POST /crawl   - Crawl website                               ║
╚════════════════════════════════════════════════════════════════╝
      `);
    });

    // Graceful shutdown
    const shutdown = async () => {
      console.log("\n[reader] Shutting down...");
      if (reader) {
        await reader.close();
      }
      process.exit(0);
    };

    process.on("SIGINT", shutdown);
    process.on("SIGTERM", shutdown);
  } catch (err: any) {
    console.error("[reader] Failed to start:", err.message);
    process.exit(1);
  }
}

startServer();
```

## File: `examples/production/job-queue-bullmq/package.json`
```json
{
  "name": "job-queue-bullmq-example",
  "version": "1.0.0",
  "private": true,
  "description": "Async job queue example using BullMQ and Redis",
  "type": "module",
  "scripts": {
    "start": "npx tsx src/index.ts",
    "worker": "npx tsx src/worker.ts",
    "dev": "concurrently \"npm run start\" \"npm run worker\""
  },
  "dependencies": {
    "@vakra-dev/reader": "file:../../..",
    "@ulixee/hero": "^2.0.0-alpha.34",
    "@ulixee/hero-core": "^2.0.0-alpha.34",
    "@ulixee/net": "^2.0.0-alpha.29",
    "bullmq": "^5.0.0",
    "express": "^4.18.2",
    "ioredis": "^5.3.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.6",
    "concurrently": "^8.2.0",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

## File: `examples/production/job-queue-bullmq/README.md`
```markdown
# Job Queue with BullMQ

Async job processing for Reader using BullMQ and Redis.

## Overview

This example demonstrates how to run scrape operations asynchronously using a job queue. This is ideal for:

- **Batch processing**: Submit hundreds of URLs and process them in the background
- **Webhook notifications**: Get notified when jobs complete
- **Horizontal scaling**: Run multiple workers to increase throughput
- **Retry logic**: Automatically retry failed jobs with exponential backoff
- **Progress tracking**: Monitor job progress in real-time

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  API Server │────▶│    Redis    │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────┐
                    │                          │                          │
              ┌─────▼─────┐            ┌───────▼───────┐           ┌──────▼──────┐
              │  Worker 1 │            │   Worker 2    │           │  Worker N   │
              └───────────┘            └───────────────┘           └─────────────┘
```

## Prerequisites

- Redis server running (local or remote)
- Node.js >= 18

## Setup

1. Install dependencies:
   ```bash
   cd examples/production/job-queue-bullmq
   npm install
   ```

2. Start Redis (if not running):
   ```bash
   # Using Docker
   docker run -d -p 6379:6379 redis:alpine

   # Or using Homebrew (macOS)
   brew services start redis
   ```

3. Start the API server:
   ```bash
   npm run start
   ```

4. Start the worker (in a separate terminal):
   ```bash
   npm run worker
   ```

5. Or run both together:
   ```bash
   npm run dev
   ```

## API Endpoints

### Submit a Job

```bash
curl -X POST http://localhost:3002/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://example.com", "https://httpbin.org/html"],
    "formats": ["markdown"],
    "webhookUrl": "https://your-server.com/webhook"
  }'
```

Response:
```json
{
  "jobId": "1",
  "status": "queued",
  "urls": 2
}
```

### Check Job Status

```bash
curl http://localhost:3002/jobs/1
```

Response:
```json
{
  "id": "1",
  "state": "completed",
  "progress": 100,
  "data": {
    "urls": ["https://example.com"],
    "formats": ["markdown"]
  },
  "result": {
    "success": true,
    "data": {
      "batchMetadata": {
        "totalUrls": 1,
        "successfulUrls": 1,
        "failedUrls": 0,
        "totalDurationMs": 2500
      },
      "results": [...]
    }
  },
  "timestamps": {
    "created": 1704067200000,
    "processed": 1704067201000,
    "finished": 1704067203500
  },
  "attempts": 1
}
```

### Queue Statistics

```bash
curl http://localhost:3002/stats
```

Response:
```json
{
  "waiting": 5,
  "active": 2,
  "completed": 150,
  "failed": 3,
  "delayed": 0
}
```

### Retry a Failed Job

```bash
curl -X POST http://localhost:3002/jobs/1/retry
```

### Remove a Job

```bash
curl -X DELETE http://localhost:3002/jobs/1
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 3002 | API server port |
| `REDIS_URL` | redis://localhost:6379 | Redis connection URL |
| `WORKER_CONCURRENCY` | 2 | Jobs processed simultaneously |

### Job Options

When submitting a job, you can configure:

```json
{
  "urls": ["..."],
  "formats": ["markdown", "html"],
  "webhookUrl": "https://...",
  "priority": 1,
  "delay": 5000
}
```

- **priority**: Lower number = higher priority (default: undefined)
- **delay**: Milliseconds to wait before processing (default: 0)

## Webhook Notifications

When a `webhookUrl` is provided, the worker sends notifications:

### Job Completed
```json
{
  "event": "job.completed",
  "jobId": "1",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "result": {
    "success": true,
    "batchMetadata": {...},
    "urlCount": 2
  }
}
```

### Job Failed
```json
{
  "event": "job.failed",
  "jobId": "1",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "error": "Timeout waiting for page"
}
```

## Scaling Workers

Run multiple workers to increase throughput:

```bash
# Terminal 1
WORKER_CONCURRENCY=4 npm run worker

# Terminal 2
WORKER_CONCURRENCY=4 npm run worker

# Terminal 3
WORKER_CONCURRENCY=4 npm run worker
```

Each worker processes jobs independently. BullMQ ensures no job is processed twice.

## Production Considerations

1. **Redis Persistence**: Configure Redis with AOF or RDB persistence for durability
2. **Memory Limits**: Set Redis maxmemory to prevent OOM
3. **Worker Health**: Use process managers like PM2 to restart crashed workers
4. **Monitoring**: Use BullMQ's built-in dashboard or integrate with observability tools
5. **Rate Limiting**: The worker is configured to process max 10 jobs/second

## Files

```
job-queue-bullmq/
├── README.md           # This file
├── package.json        # Dependencies
└── src/
    ├── index.ts        # API server
    ├── queue.ts        # Queue configuration
    └── worker.ts       # Job processor
```
```

## File: `examples/production/job-queue-bullmq/src/index.ts`
```typescript
/**
 * Job Queue API Server
 *
 * REST API for submitting and monitoring scrape jobs.
 * Jobs are processed asynchronously by the worker process.
 *
 * Usage: npx tsx src/index.ts
 */

import express, { Request, Response, NextFunction } from "express";
import {
  addScrapeJob,
  getJob,
  getQueueStats,
  scrapeQueue,
  connection,
  ScrapeJobData,
} from "./queue.js";

const app = express();
const PORT = process.env.PORT || 3002;

// Middleware
app.use(express.json({ limit: "1mb" }));

// Request logging
app.use((req: Request, res: Response, next: NextFunction) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// ============================================================================
// Routes
// ============================================================================

/**
 * GET /health - Health check
 */
app.get("/health", async (req: Request, res: Response) => {
  try {
    // Check Redis connection
    await connection.ping();

    const stats = await getQueueStats();

    res.json({
      status: "healthy",
      timestamp: new Date().toISOString(),
      queue: stats,
    });
  } catch (error: any) {
    res.status(503).json({
      status: "unhealthy",
      error: error.message,
    });
  }
});

/**
 * GET /stats - Queue statistics
 */
app.get("/stats", async (req: Request, res: Response) => {
  try {
    const stats = await getQueueStats();
    res.json(stats);
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * POST /jobs - Submit a new scrape job
 *
 * Request body:
 * {
 *   urls: string[]          // Required: URLs to scrape
 *   formats?: string[]      // Optional: Output formats (default: ['markdown'])
 *   webhookUrl?: string     // Optional: URL to notify on completion
 *   priority?: number       // Optional: Job priority (lower = higher priority)
 *   delay?: number          // Optional: Delay in ms before processing
 * }
 */
app.post("/jobs", async (req: Request, res: Response) => {
  try {
    const { urls, formats, webhookUrl, priority, delay } = req.body;

    // Validation
    if (!urls || !Array.isArray(urls) || urls.length === 0) {
      return res.status(400).json({
        error: "urls is required and must be a non-empty array",
      });
    }

    // Validate URLs
    for (const url of urls) {
      try {
        new URL(url);
      } catch {
        return res.status(400).json({
          error: `Invalid URL: ${url}`,
        });
      }
    }

    // Validate formats if provided
    const validFormats = ["markdown", "html"];
    if (formats) {
      if (!Array.isArray(formats) || !formats.every((f: string) => validFormats.includes(f))) {
        return res.status(400).json({
          error: `formats must be an array of: ${validFormats.join(", ")}`,
        });
      }
    }

    // Validate webhook URL if provided
    if (webhookUrl) {
      try {
        new URL(webhookUrl);
      } catch {
        return res.status(400).json({
          error: `Invalid webhook URL: ${webhookUrl}`,
        });
      }
    }

    // Create job data
    const jobData: ScrapeJobData = {
      urls,
      formats: formats || ["markdown"],
      webhookUrl,
      priority,
    };

    // Add job to queue
    const jobId = await addScrapeJob(jobData, { priority, delay });

    console.log(`[API] Job ${jobId} created: ${urls.length} URL(s)`);

    res.status(201).json({
      jobId,
      status: "queued",
      urls: urls.length,
      estimatedWait: delay ? `${delay}ms` : undefined,
    });
  } catch (error: any) {
    console.error("[API] Error creating job:", error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * GET /jobs/:id - Get job status and result
 */
app.get("/jobs/:id", async (req: Request, res: Response) => {
  try {
    const job = await getJob(req.params.id);

    if (!job) {
      return res.status(404).json({ error: "Job not found" });
    }

    const state = await job.getState();
    const progress = job.progress;
    const result = job.returnvalue;
    const failedReason = job.failedReason;

    res.json({
      id: job.id,
      state,
      progress,
      data: job.data,
      result: result || undefined,
      error: failedReason || undefined,
      timestamps: {
        created: job.timestamp,
        processed: job.processedOn,
        finished: job.finishedOn,
      },
      attempts: job.attemptsMade,
    });
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * DELETE /jobs/:id - Cancel/remove a job
 */
app.delete("/jobs/:id", async (req: Request, res: Response) => {
  try {
    const job = await getJob(req.params.id);

    if (!job) {
      return res.status(404).json({ error: "Job not found" });
    }

    const state = await job.getState();

    if (state === "active") {
      return res.status(400).json({
        error: "Cannot remove active job. Wait for it to complete or fail.",
      });
    }

    await job.remove();

    res.json({
      message: "Job removed",
      id: req.params.id,
    });
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * POST /jobs/:id/retry - Retry a failed job
 */
app.post("/jobs/:id/retry", async (req: Request, res: Response) => {
  try {
    const job = await getJob(req.params.id);

    if (!job) {
      return res.status(404).json({ error: "Job not found" });
    }

    const state = await job.getState();

    if (state !== "failed") {
      return res.status(400).json({
        error: `Cannot retry job in state: ${state}. Only failed jobs can be retried.`,
      });
    }

    await job.retry();

    res.json({
      message: "Job retried",
      id: req.params.id,
      newState: "waiting",
    });
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// Error handling
// ============================================================================

app.use((err: Error, req: Request, res: Response) => {
  console.error("[API Error]", err);
  res.status(500).json({ error: err.message || "Internal server error" });
});

// 404 handler
app.use((req: Request, res: Response) => {
  res.status(404).json({ error: `Not found: ${req.method} ${req.path}` });
});

// ============================================================================
// Start server
// ============================================================================

async function startServer() {
  try {
    // Test Redis connection
    await connection.ping();
    console.log("[API] Redis connected");

    app.listen(PORT, () => {
      console.log(`
╔════════════════════════════════════════════════════════════════╗
║       Reader - Job Queue API                            ║
╠════════════════════════════════════════════════════════════════╣
║  Server running on http://localhost:${PORT}                    ║
╠════════════════════════════════════════════════════════════════╣
║  Endpoints:                                                    ║
║    GET  /health        - Health check with queue stats         ║
║    GET  /stats         - Queue statistics                      ║
║    POST /jobs          - Submit a new scrape job               ║
║    GET  /jobs/:id      - Get job status and result             ║
║    DELETE /jobs/:id    - Remove a job                          ║
║    POST /jobs/:id/retry - Retry a failed job                   ║
╠════════════════════════════════════════════════════════════════╣
║  Note: Start the worker separately with: npm run worker        ║
╚════════════════════════════════════════════════════════════════╝
      `);
    });

    // Graceful shutdown
    const shutdown = async () => {
      console.log("\n[API] Shutting down...");
      await scrapeQueue.close();
      await connection.quit();
      process.exit(0);
    };

    process.on("SIGINT", shutdown);
    process.on("SIGTERM", shutdown);
  } catch (error: any) {
    console.error("[API] Failed to start:", error.message);
    process.exit(1);
  }
}

startServer();
```

## File: `examples/production/job-queue-bullmq/src/queue.ts`
```typescript
/**
 * Queue Configuration
 *
 * Defines the BullMQ queue and job types for async scraping.
 */

import { Queue } from "bullmq";
import IORedis from "ioredis";

// Redis connection (shared across queue and workers)
export const connection = new IORedis(process.env.REDIS_URL || "redis://localhost:6379", {
  maxRetriesPerRequest: null, // Required by BullMQ
});

// Scrape job queue
export const scrapeQueue = new Queue("scrape", {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 1000,
    },
    removeOnComplete: {
      age: 3600, // Keep completed jobs for 1 hour
      count: 1000, // Keep last 1000 completed jobs
    },
    removeOnFail: {
      age: 86400, // Keep failed jobs for 24 hours
    },
  },
});

/**
 * Scrape job input data
 */
export interface ScrapeJobData {
  /** URLs to scrape */
  urls: string[];
  /** Output formats */
  formats: string[];
  /** Optional webhook URL to notify on completion */
  webhookUrl?: string;
  /** Optional priority (lower = higher priority) */
  priority?: number;
}

/**
 * Scrape job result
 */
export interface ScrapeJobResult {
  success: boolean;
  data?: {
    batchMetadata: {
      totalUrls: number;
      successfulUrls: number;
      failedUrls: number;
      totalDurationMs: number;
    };
    results: Array<{
      url: string;
      success: boolean;
      markdown?: string;
      html?: string;
      json?: object;
      error?: string;
    }>;
  };
  error?: string;
}

/**
 * Add a scrape job to the queue
 */
export async function addScrapeJob(
  data: ScrapeJobData,
  options?: { priority?: number; delay?: number }
): Promise<string> {
  const job = await scrapeQueue.add("scrape", data, {
    priority: options?.priority ?? data.priority,
    delay: options?.delay,
  });
  return job.id!;
}

/**
 * Get job by ID
 */
export async function getJob(jobId: string) {
  return scrapeQueue.getJob(jobId);
}

/**
 * Get queue statistics
 */
export async function getQueueStats() {
  const [waiting, active, completed, failed, delayed] = await Promise.all([
    scrapeQueue.getWaitingCount(),
    scrapeQueue.getActiveCount(),
    scrapeQueue.getCompletedCount(),
    scrapeQueue.getFailedCount(),
    scrapeQueue.getDelayedCount(),
  ]);

  return { waiting, active, completed, failed, delayed };
}
```

## File: `examples/production/job-queue-bullmq/src/worker.ts`
```typescript
/**
 * Scrape Worker
 *
 * Processes scrape jobs from the BullMQ queue.
 * Run this as a separate process from the API server.
 *
 * Usage: npx tsx src/worker.ts
 */

import { Worker, Job } from "bullmq";
import { ReaderClient } from "@vakra-dev/reader";
import { connection, ScrapeJobData, ScrapeJobResult } from "./queue.js";

// Shared ReaderClient instance
let reader: ReaderClient | null = null;

/**
 * Process a scrape job
 */
async function processJob(job: Job<ScrapeJobData>): Promise<ScrapeJobResult> {
  const { urls, formats, webhookUrl } = job.data;

  console.log(`[Worker] Processing job ${job.id}: ${urls.length} URL(s)`);

  if (!reader) {
    throw new Error("ReaderClient not initialized");
  }

  try {
    // Update progress: starting
    await job.updateProgress(10);

    // Perform scrape
    const result = await reader.scrape({
      urls,
      formats: formats as Array<"markdown" | "html">,
    });

    // Update progress: scraping complete
    await job.updateProgress(80);

    // Send webhook notification if configured
    if (webhookUrl) {
      try {
        await fetch(webhookUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            event: "job.completed",
            jobId: job.id,
            timestamp: new Date().toISOString(),
            result: {
              success: true,
              batchMetadata: result.batchMetadata,
              urlCount: urls.length,
            },
          }),
        });
        console.log(`[Worker] Webhook sent to ${webhookUrl}`);
      } catch (webhookError) {
        console.error(`[Worker] Webhook failed:`, webhookError);
        // Don't fail the job if webhook fails
      }
    }

    // Update progress: complete
    await job.updateProgress(100);

    console.log(
      `[Worker] Job ${job.id} completed: ${result.batchMetadata.successfulUrls}/${result.batchMetadata.totalUrls} successful`
    );

    return {
      success: true,
      data: {
        batchMetadata: {
          totalUrls: result.batchMetadata.totalUrls,
          successfulUrls: result.batchMetadata.successfulUrls,
          failedUrls: result.batchMetadata.failedUrls,
          totalDurationMs: result.batchMetadata.totalDuration,
        },
        results: result.data.map((r) => ({
          url: r.metadata.baseUrl,
          success: true,
          markdown: r.markdown,
          html: r.html,
        })),
      },
    };
  } catch (error: any) {
    console.error(`[Worker] Job ${job.id} failed:`, error.message);

    // Send failure webhook if configured
    if (webhookUrl) {
      try {
        await fetch(webhookUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            event: "job.failed",
            jobId: job.id,
            timestamp: new Date().toISOString(),
            error: error.message,
          }),
        });
      } catch {
        // Ignore webhook errors on failure
      }
    }

    throw error; // Re-throw to mark job as failed
  }
}

/**
 * Start the worker
 */
async function startWorker() {
  console.log("[Worker] Starting ReaderClient...");

  // Initialize ReaderClient
  reader = new ReaderClient({ verbose: true });
  await reader.start();

  console.log("[Worker] ReaderClient started");

  // Create worker
  const worker = new Worker<ScrapeJobData, ScrapeJobResult>("scrape", processJob, {
    connection,
    concurrency: parseInt(process.env.WORKER_CONCURRENCY || "2"),
    limiter: {
      max: 10,
      duration: 1000, // Max 10 jobs per second
    },
  });

  // Event handlers
  worker.on("completed", (job) => {
    console.log(`[Worker] Job ${job.id} completed successfully`);
  });

  worker.on("failed", (job, error) => {
    console.error(`[Worker] Job ${job?.id} failed:`, error.message);
  });

  worker.on("error", (error) => {
    console.error("[Worker] Worker error:", error);
  });

  console.log(`
╔════════════════════════════════════════════════════════════════╗
║       Reader - BullMQ Worker                            ║
╠════════════════════════════════════════════════════════════════╣
║  Worker started and listening for jobs                         ║
║  Concurrency: ${process.env.WORKER_CONCURRENCY || "2"} jobs                                          ║
║  Redis: ${process.env.REDIS_URL || "redis://localhost:6379"}                            ║
╚════════════════════════════════════════════════════════════════╝
  `);

  // Graceful shutdown
  const shutdown = async () => {
    console.log("\n[Worker] Shutting down...");

    // Close worker (waits for active jobs to complete)
    await worker.close();

    // Close ReaderClient
    if (reader) {
      await reader.close();
    }

    // Close Redis connection
    await connection.quit();

    console.log("[Worker] Shutdown complete");
    process.exit(0);
  };

  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}

// Start worker
startWorker().catch((error) => {
  console.error("[Worker] Failed to start:", error);
  process.exit(1);
});
```

## File: `src/client.ts`
```typescript
/**
 * ReaderClient
 *
 * A client wrapper that manages HeroCore lifecycle and provides
 * a simple interface for scraping and crawling.
 *
 * @example
 * const reader = new ReaderClient();
 *
 * const result = await reader.scrape({
 *   urls: ['https://example.com'],
 *   formats: ['markdown'],
 * });
 *
 * console.log(result.data[0].markdown);
 *
 * // When done (optional - auto-closes on process exit)
 * await reader.close();
 */

import HeroCore from "@ulixee/hero-core";
import { TransportBridge } from "@ulixee/net";
import { ConnectionToHeroCore } from "@ulixee/hero";
import { scrape } from "./scraper";
import { crawl } from "./crawler";
import { HeroBrowserPool } from "./browser/pool";
import type { ScrapeOptions, ScrapeResult, ProxyConfig, BrowserPoolConfig } from "./types";
import type { CrawlOptions, CrawlResult } from "./crawl-types";
import { createLogger } from "./utils/logger";

const logger = createLogger("client");

/**
 * Proxy rotation strategy
 */
export type ProxyRotation = "round-robin" | "random";

/**
 * Configuration options for ReaderClient
 */
export interface ReaderClientOptions {
  /** Enable verbose logging (default: false) */
  verbose?: boolean;
  /** Show Chrome browser window (default: false) */
  showChrome?: boolean;

  /** Browser pool configuration */
  browserPool?: BrowserPoolConfig;

  /** List of proxies to rotate through */
  proxies?: ProxyConfig[];

  /** Proxy rotation strategy (default: "round-robin") */
  proxyRotation?: ProxyRotation;

  /** Skip TLS/SSL certificate verification (default: true) */
  skipTLSVerification?: boolean;
}

/**
 * ReaderClient manages the HeroCore lifecycle and provides
 * scrape/crawl methods with automatic initialization.
 */
export class ReaderClient {
  private heroCore: HeroCore | null = null;
  private pool: HeroBrowserPool | null = null;
  private initialized = false;
  private initializing: Promise<void> | null = null;
  private closed = false;
  private options: ReaderClientOptions;
  private proxyIndex = 0;
  private cleanupHandler: (() => Promise<void>) | null = null;

  constructor(options: ReaderClientOptions = {}) {
    this.options = options;

    // Configure TLS verification
    // Hero uses MITM_ALLOW_INSECURE env var to skip certificate verification
    // Default is true (skip verification) for compatibility with various sites
    const skipTLS = options.skipTLSVerification ?? true;
    if (skipTLS) {
      process.env.MITM_ALLOW_INSECURE = "true";
    }

    // Register cleanup on process exit
    this.registerCleanup();
  }

  /**
   * Get the next proxy from the rotation pool
   */
  private getNextProxy(): ProxyConfig | undefined {
    const { proxies, proxyRotation = "round-robin" } = this.options;

    if (!proxies || proxies.length === 0) {
      return undefined;
    }

    if (proxyRotation === "random") {
      return proxies[Math.floor(Math.random() * proxies.length)];
    }

    // Round-robin (default)
    const proxy = proxies[this.proxyIndex % proxies.length];
    this.proxyIndex++;
    return proxy;
  }

  /**
   * Initialize HeroCore. Called automatically on first scrape/crawl.
   * Can be called explicitly if you want to pre-warm the client.
   */
  async start(): Promise<void> {
    if (this.closed) {
      throw new Error("ReaderClient has been closed. Create a new instance.");
    }

    if (this.initialized) {
      return;
    }

    // Prevent concurrent initialization
    if (this.initializing) {
      await this.initializing;
      return;
    }

    this.initializing = this.initializeCore();
    await this.initializing;
    this.initializing = null;
  }

  /**
   * Internal initialization logic
   */
  private async initializeCore(): Promise<void> {
    try {
      if (this.options.verbose) {
        logger.info("Starting HeroCore...");
      }

      this.heroCore = new HeroCore();
      await this.heroCore.start();

      if (this.options.verbose) {
        logger.info("HeroCore started successfully");
      }

      // Initialize browser pool
      if (this.options.verbose) {
        logger.info("Initializing browser pool...");
      }

      const browserPoolConfig = this.options.browserPool;
      const poolConfig = {
        size: browserPoolConfig?.size ?? 2,
        retireAfterPageCount: browserPoolConfig?.retireAfterPages ?? 100,
        retireAfterAgeMs: (browserPoolConfig?.retireAfterMinutes ?? 30) * 60 * 1000,
        maxQueueSize: browserPoolConfig?.maxQueueSize ?? 100,
      };

      this.pool = new HeroBrowserPool(
        poolConfig,
        undefined, // proxy set per-request
        this.options.showChrome,
        this.createConnection(),
        undefined, // userAgent
        this.options.verbose
      );
      await this.pool.initialize();

      this.initialized = true;

      if (this.options.verbose) {
        logger.info("Browser pool initialized successfully");
      }
    } catch (error: any) {
      // Clean up on failure
      if (this.pool) {
        await this.pool.shutdown().catch(() => {});
        this.pool = null;
      }
      if (this.heroCore) {
        await this.heroCore.close().catch(() => {});
        this.heroCore = null;
      }
      this.initialized = false;

      // Provide helpful error messages
      const message = error.message || String(error);

      if (message.includes("EADDRINUSE")) {
        throw new Error(
          "Failed to start HeroCore: Port already in use. " +
            "Another instance may be running. " +
            "Close it or use a different port."
        );
      }

      if (message.includes("chrome") || message.includes("Chrome")) {
        throw new Error(
          "Failed to start HeroCore: Chrome/Chromium not found. " +
            "Please install Chrome or set CHROME_PATH environment variable."
        );
      }

      throw new Error(`Failed to start HeroCore: ${message}`);
    }
  }

  /**
   * Create a connection to the HeroCore instance
   */
  private createConnection(): ConnectionToHeroCore {
    if (!this.heroCore) {
      throw new Error("HeroCore not initialized. This should not happen.");
    }

    const bridge = new TransportBridge();
    this.heroCore.addConnection(bridge.transportToClient);
    return new ConnectionToHeroCore(bridge.transportToCore);
  }

  /**
   * Ensure client is initialized before operation
   */
  private async ensureInitialized(): Promise<void> {
    if (this.closed) {
      throw new Error("ReaderClient has been closed. Create a new instance.");
    }

    if (!this.initialized) {
      await this.start();
    }
  }

  /**
   * Scrape one or more URLs
   *
   * @param options - Scrape options (urls, formats, etc.)
   * @returns Scrape result with data and metadata
   *
   * @example
   * const result = await reader.scrape({
   *   urls: ['https://example.com'],
   *   formats: ['markdown', 'html'],
   * });
   */
  async scrape(options: Omit<ScrapeOptions, "connectionToCore" | "pool">): Promise<ScrapeResult> {
    await this.ensureInitialized();

    if (!this.pool) {
      throw new Error("Browser pool not initialized. This should not happen.");
    }

    // Use proxy rotation if proxies are configured and no specific proxy is provided
    const proxy = options.proxy ?? this.getNextProxy();

    return await scrape({
      ...options,
      proxy,
      showChrome: options.showChrome ?? this.options.showChrome,
      verbose: options.verbose ?? this.options.verbose,
      pool: this.pool,
    });
  }

  /**
   * Crawl a website to discover URLs
   *
   * @param options - Crawl options (url, depth, maxPages, etc.)
   * @returns Crawl result with discovered URLs and optional scraped content
   *
   * @example
   * const result = await reader.crawl({
   *   url: 'https://example.com',
   *   depth: 2,
   *   maxPages: 50,
   *   scrape: true,
   * });
   */
  async crawl(options: Omit<CrawlOptions, "connectionToCore" | "pool">): Promise<CrawlResult> {
    await this.ensureInitialized();

    if (!this.pool) {
      throw new Error("Browser pool not initialized. This should not happen.");
    }

    // Use proxy rotation if proxies are configured and no specific proxy is provided
    const proxy = options.proxy ?? this.getNextProxy();

    return await crawl({
      ...options,
      proxy,
      pool: this.pool,
    });
  }

  /**
   * Check if the client is initialized and ready
   */
  isReady(): boolean {
    return this.initialized && !this.closed;
  }

  /**
   * Close the client and release resources
   *
   * Note: This is optional - the client will auto-close on process exit.
   */
  async close(): Promise<void> {
    if (this.closed) {
      return;
    }

    this.closed = true;

    // Remove process event handlers to allow clean exit
    this.removeCleanupHandlers();

    // Shutdown pool first (closes browser instances)
    if (this.pool) {
      if (this.options.verbose) {
        logger.info("Shutting down browser pool...");
      }

      try {
        await this.pool.shutdown();
      } catch (error: any) {
        if (this.options.verbose) {
          logger.warn(`Error shutting down pool: ${error.message}`);
        }
      }

      this.pool = null;
    }

    // Then close HeroCore
    if (this.heroCore) {
      if (this.options.verbose) {
        logger.info("Closing HeroCore...");
      }

      try {
        await this.heroCore.close();
        // Also call static shutdown to clean up any remaining resources
        await HeroCore.shutdown();
      } catch (error: any) {
        // Ignore close errors
        if (this.options.verbose) {
          logger.warn(`Error closing HeroCore: ${error.message}`);
        }
      }

      this.heroCore = null;
    }

    this.initialized = false;

    if (this.options.verbose) {
      logger.info("ReaderClient closed");
    }
  }

  /**
   * Register cleanup handlers for process exit
   */
  private registerCleanup(): void {
    this.cleanupHandler = async () => {
      await this.close();
    };

    // Handle various exit signals
    process.once("beforeExit", this.cleanupHandler);
    process.once("SIGINT", async () => {
      await this.cleanupHandler?.();
      process.exit(0);
    });
    process.once("SIGTERM", async () => {
      await this.cleanupHandler?.();
      process.exit(0);
    });
  }

  /**
   * Remove process cleanup handlers
   */
  private removeCleanupHandlers(): void {
    if (this.cleanupHandler) {
      process.removeListener("beforeExit", this.cleanupHandler);
      this.cleanupHandler = null;
    }
  }
}
```

## File: `src/crawl-types.ts`
```typescript
import type { ScrapeResult, ProxyConfig } from "./types";
import type { IBrowserPool } from "./browser/types";

/**
 * Crawl options interface
 */
export interface CrawlOptions {
  /** Single seed URL to start crawling from */
  url: string;

  /** Maximum depth to crawl (default: 1) */
  depth?: number;

  /** Maximum pages to discover (default: 20) */
  maxPages?: number;

  /** Also scrape full content (default: false) */
  scrape?: boolean;

  /** Delay between requests in milliseconds (default: 1000) */
  delayMs?: number;

  /** Total timeout for the entire crawl operation in milliseconds */
  timeoutMs?: number;

  /** URL patterns to include (regex strings) - if set, only matching URLs are crawled */
  includePatterns?: string[];

  /** URL patterns to exclude (regex strings) - matching URLs are skipped */
  excludePatterns?: string[];

  // ============================================================================
  // Scrape options (used when scrape: true)
  // ============================================================================

  /** Output formats for scraped content (default: ['markdown']) */
  formats?: Array<"markdown" | "html">;

  /** Number of URLs to scrape in parallel (default: 2) */
  scrapeConcurrency?: number;

  // ============================================================================
  // Content cleaning options
  // ============================================================================

  /** Remove ads and tracking elements (default: true) */
  removeAds?: boolean;

  /** Remove base64-encoded images to reduce output size (default: true) */
  removeBase64Images?: boolean;

  // ============================================================================
  // Hero-specific options
  // ============================================================================

  /** Proxy configuration for Hero */
  proxy?: ProxyConfig;

  /** Custom user agent string */
  userAgent?: string;

  /** Enable verbose logging (default: false) */
  verbose?: boolean;

  /** Show Chrome window (default: false) */
  showChrome?: boolean;

  /** Connection to Hero Core (for shared Core usage) */
  connectionToCore?: any;

  /** Browser pool instance (internal, provided by ReaderClient) */
  pool?: IBrowserPool;
}

/**
 * Crawl URL result interface
 */
export interface CrawlUrl {
  /** URL of the page */
  url: string;

  /** Page title */
  title: string;

  /** Page description or null if not found */
  description: string | null;
}

/**
 * Crawl result interface
 */
export interface CrawlResult {
  /** Array of discovered URLs with basic info */
  urls: CrawlUrl[];

  /** Full scrape results (only when scrape: true) */
  scraped?: ScrapeResult;

  /** Crawl operation metadata */
  metadata: CrawlMetadata;
}

/**
 * Crawl metadata interface
 */
export interface CrawlMetadata {
  /** Total URLs discovered */
  totalUrls: number;

  /** Maximum depth reached */
  maxDepth: number;

  /** Total crawl duration in milliseconds */
  totalDuration: number;

  /** Seed URL that started the crawl */
  seedUrl: string;
}
```

## File: `src/crawler.ts`
```typescript
import Hero from "@ulixee/hero";
import { parseHTML } from "linkedom";
import type { IBrowserPool } from "./browser/types";
import { detectChallenge } from "./cloudflare/detector";
import { waitForChallengeResolution } from "./cloudflare/handler";
import { resolveUrl, isValidUrl, isSameDomain, getUrlKey, isContentUrl, shouldIncludeUrl } from "./utils/url-helpers";
import { fetchRobotsTxt, isUrlAllowed, type RobotsRules } from "./utils/robots-parser";
import { rateLimit } from "./utils/rate-limiter";
import { createLogger } from "./utils/logger";
import { scrape } from "./scraper";
import type { CrawlOptions, CrawlResult, CrawlUrl, CrawlMetadata } from "./crawl-types";
import type { ScrapeResult } from "./types";

/**
 * Crawler class for discovering and optionally scraping pages
 *
 * Features:
 * - BFS/DFS crawling with depth control
 * - Automatic Cloudflare challenge handling
 * - Link extraction and filtering
 * - Optional full content scraping
 * - URL deduplication
 *
 * @example
 * const crawler = new Crawler({
 *   url: 'https://example.com',
 *   depth: 2,
 *   maxPages: 20,
 *   scrape: true
 * });
 *
 * const result = await crawler.crawl();
 * console.log(`Discovered ${result.urls.length} URLs`);
 */
export class Crawler {
  private options: Omit<
    Required<CrawlOptions>,
    "proxy" | "timeoutMs" | "userAgent" | "includePatterns" | "excludePatterns" | "pool" | "removeAds" | "removeBase64Images"
  > & {
    proxy?: CrawlOptions["proxy"];
    timeoutMs?: CrawlOptions["timeoutMs"];
    userAgent?: CrawlOptions["userAgent"];
    includePatterns?: string[];
    excludePatterns?: string[];
    removeAds?: boolean;
    removeBase64Images?: boolean;
  };
  private visited: Set<string> = new Set();
  private queue: Array<{ url: string; depth: number }> = [];
  private urls: CrawlUrl[] = [];
  private pool: IBrowserPool;
  private logger = createLogger("crawler");
  private robotsRules: RobotsRules | null = null;

  constructor(options: CrawlOptions) {
    // Pool must be provided by client
    if (!options.pool) {
      throw new Error("Browser pool must be provided. Use ReaderClient for automatic pool management.");
    }
    this.pool = options.pool;

    this.options = {
      url: options.url,
      depth: options.depth || 1,
      maxPages: options.maxPages || 20,
      scrape: options.scrape || false,
      delayMs: options.delayMs || 1000,
      timeoutMs: options.timeoutMs,
      includePatterns: options.includePatterns,
      excludePatterns: options.excludePatterns,
      formats: options.formats || ["markdown", "html"],
      scrapeConcurrency: options.scrapeConcurrency || 2,
      proxy: options.proxy,
      userAgent: options.userAgent,
      verbose: options.verbose || false,
      showChrome: options.showChrome || false,
      connectionToCore: options.connectionToCore,
      // Content cleaning options
      removeAds: options.removeAds,
      removeBase64Images: options.removeBase64Images,
    };
  }

  /**
   * Start crawling
   */
  async crawl(): Promise<CrawlResult> {
    const startTime = Date.now();

    // Fetch robots.txt rules before crawling
    this.robotsRules = await fetchRobotsTxt(this.options.url);
    if (this.robotsRules) {
      this.logger.info("Loaded robots.txt rules");
    }

    // Pool is managed by ReaderClient - just use it
    // Add seed URL to queue (if allowed by robots.txt)
    if (isUrlAllowed(this.options.url, this.robotsRules)) {
      this.queue.push({ url: this.options.url, depth: 0 });
    } else {
      this.logger.warn(`Seed URL blocked by robots.txt: ${this.options.url}`);
    }

    // Crawl URLs
    while (this.queue.length > 0 && this.urls.length < this.options.maxPages) {
      // Check timeout
      if (this.options.timeoutMs && Date.now() - startTime > this.options.timeoutMs) {
        this.logger.warn(`Crawl timed out after ${this.options.timeoutMs}ms`);
        break;
      }

      const item = this.queue.shift()!;
      const urlKey = getUrlKey(item.url);

      if (this.visited.has(urlKey)) {
        continue;
      }

      // Fetch page
      const result = await this.fetchPage(item.url);

      if (result) {
        this.urls.push(result.crawlUrl);
        this.visited.add(urlKey);

        // Extract links from the fetched HTML if not at max depth
        if (item.depth < this.options.depth) {
          const links = this.extractLinks(result.html, item.url, item.depth + 1);
          this.queue.push(...links);
        }
      }

      // Rate limit (use robots.txt crawl-delay if specified, otherwise use configured delay)
      const delay = this.robotsRules?.crawlDelay || this.options.delayMs;
      await rateLimit(delay);
    }

    // Build metadata
    const metadata: CrawlMetadata = {
      totalUrls: this.urls.length,
      maxDepth: this.options.depth,
      totalDuration: Date.now() - startTime,
      seedUrl: this.options.url,
    };

    // Optionally scrape all discovered URLs
    let scraped: ScrapeResult | undefined;
    if (this.options.scrape) {
      scraped = await this.scrapeDiscoveredUrls();
    }

    return {
      urls: this.urls,
      scraped,
      metadata,
    };
  }

  /**
   * Fetch a single page and extract basic info
   */
  private async fetchPage(url: string): Promise<{ crawlUrl: CrawlUrl; html: string } | null> {
    try {
      return await this.pool.withBrowser(async (hero: Hero) => {
        // Navigate
        await hero.goto(url, { timeoutMs: 30000 });
        await hero.waitForPaintingStable();

        // Handle Cloudflare challenge
        const initialUrl = await hero.url;
        const detection = await detectChallenge(hero);

        if (detection.isChallenge) {
          if (this.options.verbose) {
            this.logger.info(`Challenge detected on ${url}`);
          }

          const result = await waitForChallengeResolution(hero, {
            maxWaitMs: 45000,
            pollIntervalMs: 500,
            verbose: this.options.verbose,
            initialUrl,
          });

          if (!result.resolved) {
            throw new Error(`Challenge not resolved`);
          }
        }

        // Extract basic info and HTML
        const title = await hero.document.title;
        const html = await hero.document.documentElement.outerHTML;

        // Try to extract description from meta tags
        let description: string | null = null;
        try {
          const metaDesc = await hero.document.querySelector('meta[name="description"]');
          if (metaDesc) {
            description = await metaDesc.getAttribute("content");
          }
        } catch {
          // No description found
        }

        return {
          crawlUrl: {
            url,
            title: title || "Untitled",
            description,
          },
          html,
        };
      });
    } catch (error: any) {
      this.logger.error(`Failed to fetch ${url}: ${error.message}`);
      return null;
    }
  }

  /**
   * Extract links from HTML content using DOM parsing
   * Handles all href formats (single quotes, double quotes, unquoted)
   */
  private extractLinks(
    html: string,
    baseUrl: string,
    depth: number
  ): Array<{ url: string; depth: number }> {
    const links: Array<{ url: string; depth: number }> = [];
    const { document } = parseHTML(html);

    // Use proper DOM API to find all anchor elements with href
    document.querySelectorAll("a[href]").forEach((anchor: Element) => {
      const rawHref = anchor.getAttribute("href");
      if (!rawHref) return;

      // Trim whitespace from href
      const href = rawHref.trim();
      if (!href) return;

      // Skip fragment-only links (#, #section, etc.)
      if (href.startsWith("#")) return;

      // Skip non-HTTP schemes (javascript:, mailto:, tel:, data:, blob:, ftp:)
      const lowerHref = href.toLowerCase();
      if (
        lowerHref.startsWith("javascript:") ||
        lowerHref.startsWith("mailto:") ||
        lowerHref.startsWith("tel:") ||
        lowerHref.startsWith("data:") ||
        lowerHref.startsWith("blob:") ||
        lowerHref.startsWith("ftp:")
      ) {
        return;
      }

      // Resolve relative URLs
      let resolved = resolveUrl(href, baseUrl);
      if (!resolved || !isValidUrl(resolved)) return;

      // Strip hash fragments from URLs
      try {
        const parsed = new URL(resolved);
        parsed.hash = "";
        resolved = parsed.toString();
      } catch {
        return;
      }

      // Check if same domain
      if (!isSameDomain(resolved, this.options.url)) return;

      // Check if content page (skip legal, policy, utility pages)
      if (!isContentUrl(resolved)) return;

      // Check include/exclude patterns
      if (!shouldIncludeUrl(resolved, this.options.includePatterns, this.options.excludePatterns)) return;

      // Check if allowed by robots.txt
      if (!isUrlAllowed(resolved, this.robotsRules)) return;

      // Check if already visited or queued
      const urlKey = getUrlKey(resolved);
      if (this.visited.has(urlKey) || this.queue.some((q) => getUrlKey(q.url) === urlKey)) {
        return;
      }

      links.push({ url: resolved, depth });
    });

    return links;
  }

  /**
   * Scrape all discovered URLs
   */
  private async scrapeDiscoveredUrls(): Promise<ScrapeResult> {
    const urls = this.urls.map((u) => u.url);

    return scrape({
      urls,
      formats: this.options.formats,
      batchConcurrency: this.options.scrapeConcurrency,
      proxy: this.options.proxy,
      userAgent: this.options.userAgent,
      verbose: this.options.verbose,
      showChrome: this.options.showChrome,
      pool: this.pool,
      // Content cleaning options
      removeAds: this.options.removeAds,
      removeBase64Images: this.options.removeBase64Images,
    });
  }
}

/**
 * Convenience function to crawl a website
 *
 * @param options - Crawl options
 * @returns Crawl result
 *
 * @example
 * const result = await crawl({
 *   url: 'https://example.com',
 *   depth: 2,
 *   maxPages: 20,
 *   scrape: true
 * });
 */
export async function crawl(options: CrawlOptions): Promise<CrawlResult> {
  const crawler = new Crawler(options);
  return crawler.crawl();
}
```

## File: `src/errors.ts`
```typescript
/**
 * Typed error classes for Reader
 *
 * Provides actionable error messages and structured error information
 * for better debugging and error handling.
 */

/**
 * Error codes for categorization
 */
export enum ReaderErrorCode {
  // Network errors
  NETWORK_ERROR = "NETWORK_ERROR",
  TIMEOUT = "TIMEOUT",
  CONNECTION_REFUSED = "CONNECTION_REFUSED",

  // Cloudflare/bot detection
  CLOUDFLARE_CHALLENGE = "CLOUDFLARE_CHALLENGE",
  BOT_DETECTED = "BOT_DETECTED",
  ACCESS_DENIED = "ACCESS_DENIED",

  // Content errors
  CONTENT_EXTRACTION_FAILED = "CONTENT_EXTRACTION_FAILED",
  EMPTY_CONTENT = "EMPTY_CONTENT",

  // Validation errors
  INVALID_URL = "INVALID_URL",
  INVALID_OPTIONS = "INVALID_OPTIONS",

  // Robots.txt
  ROBOTS_BLOCKED = "ROBOTS_BLOCKED",

  // Browser/pool errors
  BROWSER_ERROR = "BROWSER_ERROR",
  POOL_EXHAUSTED = "POOL_EXHAUSTED",

  // Client errors
  CLIENT_CLOSED = "CLIENT_CLOSED",
  NOT_INITIALIZED = "NOT_INITIALIZED",

  // Unknown
  UNKNOWN = "UNKNOWN",
}

/**
 * Base error class for all Reader errors
 */
export class ReaderError extends Error {
  readonly code: ReaderErrorCode;
  readonly url?: string;
  readonly cause?: Error;
  readonly timestamp: string;
  readonly retryable: boolean;

  constructor(
    message: string,
    code: ReaderErrorCode,
    options?: {
      url?: string;
      cause?: Error;
      retryable?: boolean;
    }
  ) {
    super(message);
    this.name = "ReaderError";
    this.code = code;
    this.url = options?.url;
    this.cause = options?.cause;
    this.timestamp = new Date().toISOString();
    this.retryable = options?.retryable ?? false;

    // Maintain proper stack trace
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }
  }

  /**
   * Convert to a plain object for serialization
   */
  toJSON(): Record<string, unknown> {
    return {
      name: this.name,
      code: this.code,
      message: this.message,
      url: this.url,
      timestamp: this.timestamp,
      retryable: this.retryable,
      cause: this.cause?.message,
      stack: this.stack,
    };
  }
}

/**
 * Network-related errors (connection issues, DNS failures, etc.)
 */
export class NetworkError extends ReaderError {
  constructor(message: string, options?: { url?: string; cause?: Error }) {
    super(message, ReaderErrorCode.NETWORK_ERROR, {
      ...options,
      retryable: true,
    });
    this.name = "NetworkError";
  }
}

/**
 * Timeout errors (page load, navigation, etc.)
 */
export class TimeoutError extends ReaderError {
  readonly timeoutMs: number;

  constructor(message: string, timeoutMs: number, options?: { url?: string; cause?: Error }) {
    super(message, ReaderErrorCode.TIMEOUT, {
      ...options,
      retryable: true,
    });
    this.name = "TimeoutError";
    this.timeoutMs = timeoutMs;
  }

  toJSON(): Record<string, unknown> {
    return {
      ...super.toJSON(),
      timeoutMs: this.timeoutMs,
    };
  }
}

/**
 * Cloudflare challenge errors
 */
export class CloudflareError extends ReaderError {
  readonly challengeType: string;

  constructor(challengeType: string, options?: { url?: string; cause?: Error }) {
    super(
      `Cloudflare ${challengeType} challenge not resolved. Consider using a residential proxy or increasing timeout.`,
      ReaderErrorCode.CLOUDFLARE_CHALLENGE,
      {
        ...options,
        retryable: true,
      }
    );
    this.name = "CloudflareError";
    this.challengeType = challengeType;
  }

  toJSON(): Record<string, unknown> {
    return {
      ...super.toJSON(),
      challengeType: this.challengeType,
    };
  }
}

/**
 * Access denied errors (blocked, forbidden, etc.)
 */
export class AccessDeniedError extends ReaderError {
  readonly statusCode?: number;

  constructor(message: string, options?: { url?: string; statusCode?: number; cause?: Error }) {
    super(message, ReaderErrorCode.ACCESS_DENIED, {
      ...options,
      retryable: false,
    });
    this.name = "AccessDeniedError";
    this.statusCode = options?.statusCode;
  }

  toJSON(): Record<string, unknown> {
    return {
      ...super.toJSON(),
      statusCode: this.statusCode,
    };
  }
}

/**
 * Content extraction errors
 */
export class ContentExtractionError extends ReaderError {
  constructor(message: string, options?: { url?: string; cause?: Error }) {
    super(message, ReaderErrorCode.CONTENT_EXTRACTION_FAILED, {
      ...options,
      retryable: false,
    });
    this.name = "ContentExtractionError";
  }
}

/**
 * Validation errors (invalid URLs, options, etc.)
 */
export class ValidationError extends ReaderError {
  readonly field?: string;

  constructor(message: string, options?: { field?: string; url?: string }) {
    super(message, ReaderErrorCode.INVALID_OPTIONS, {
      url: options?.url,
      retryable: false,
    });
    this.name = "ValidationError";
    this.field = options?.field;
  }

  toJSON(): Record<string, unknown> {
    return {
      ...super.toJSON(),
      field: this.field,
    };
  }
}

/**
 * URL validation error
 */
export class InvalidUrlError extends ReaderError {
  constructor(url: string, reason?: string) {
    super(reason ? `Invalid URL "${url}": ${reason}` : `Invalid URL: ${url}`, ReaderErrorCode.INVALID_URL, {
      url,
      retryable: false,
    });
    this.name = "InvalidUrlError";
  }
}

/**
 * Robots.txt blocked error
 */
export class RobotsBlockedError extends ReaderError {
  constructor(url: string) {
    super(`URL blocked by robots.txt: ${url}. Set respectRobotsTxt: false to override.`, ReaderErrorCode.ROBOTS_BLOCKED, {
      url,
      retryable: false,
    });
    this.name = "RobotsBlockedError";
  }
}

/**
 * Browser pool errors
 */
export class BrowserPoolError extends ReaderError {
  constructor(message: string, options?: { cause?: Error }) {
    super(message, ReaderErrorCode.BROWSER_ERROR, {
      ...options,
      retryable: true,
    });
    this.name = "BrowserPoolError";
  }
}

/**
 * Client state errors
 */
export class ClientClosedError extends ReaderError {
  constructor() {
    super("ReaderClient has been closed. Create a new instance to continue.", ReaderErrorCode.CLIENT_CLOSED, {
      retryable: false,
    });
    this.name = "ClientClosedError";
  }
}

/**
 * Not initialized error
 */
export class NotInitializedError extends ReaderError {
  constructor(component: string) {
    super(`${component} not initialized. This should not happen - please report this bug.`, ReaderErrorCode.NOT_INITIALIZED, {
      retryable: false,
    });
    this.name = "NotInitializedError";
  }
}

/**
 * Helper to wrap unknown errors in ReaderError
 */
export function wrapError(error: unknown, url?: string): ReaderError {
  if (error instanceof ReaderError) {
    return error;
  }

  if (error instanceof Error) {
    // Check for common error patterns
    const message = error.message.toLowerCase();

    if (message.includes("timeout") || message.includes("timed out")) {
      return new TimeoutError(error.message, 30000, { url, cause: error });
    }

    if (message.includes("econnrefused") || message.includes("connection refused")) {
      return new NetworkError(`Connection refused: ${error.message}`, { url, cause: error });
    }

    if (message.includes("enotfound") || message.includes("dns")) {
      return new NetworkError(`DNS lookup failed: ${error.message}`, { url, cause: error });
    }

    if (message.includes("cloudflare") || message.includes("challenge")) {
      return new CloudflareError("unknown", { url, cause: error });
    }

    return new ReaderError(error.message, ReaderErrorCode.UNKNOWN, {
      url,
      cause: error,
      retryable: false,
    });
  }

  return new ReaderError(String(error), ReaderErrorCode.UNKNOWN, {
    url,
    retryable: false,
  });
}
```

## File: `src/index.ts`
```typescript
/**
 * @vakra-dev/reader
 *
 * Production-grade web scraping engine with anti-bot bypass using Ulixee Hero
 * Drop-in replacement for @reader/core with superior Cloudflare bypass capabilities
 */

// =============================================================================
// Main API exports
// =============================================================================
export { ReaderClient } from "./client";
export type { ReaderClientOptions, ProxyRotation } from "./client";
export { scrape, Scraper } from "./scraper";
export { crawl, Crawler } from "./crawler";

// =============================================================================
// Daemon exports
// =============================================================================
export {
  DaemonServer,
  DaemonClient,
  isDaemonRunning,
  getDaemonInfo,
  getPidFilePath,
  DEFAULT_DAEMON_PORT,
} from "./daemon";
export type { DaemonServerOptions, DaemonClientOptions, DaemonStatus } from "./daemon";

// =============================================================================
// Type exports
// =============================================================================
export type {
  ScrapeOptions,
  ScrapeResult,
  WebsiteScrapeResult,
  BatchMetadata,
  Page,
  WebsiteMetadata,
  ProxyConfig,
  ProxyMetadata,
  BrowserPoolConfig,
} from "./types";

export type { CrawlOptions, CrawlResult, CrawlUrl, CrawlMetadata } from "./crawl-types";

// =============================================================================
// Formatter exports (for custom formatting)
// =============================================================================
export { formatToMarkdown, htmlToMarkdown } from "./formatters/markdown";
export { formatToHTML } from "./formatters/html";

// =============================================================================
// Utility exports (for advanced usage)
// =============================================================================
export { extractMetadata } from "./utils/metadata-extractor";
export { cleanContent } from "./utils/content-cleaner";
export {
  isSameDomain,
  resolveUrl,
  isValidUrl,
  validateUrls,
  getUrlKey,
  shouldCrawlUrl,
} from "./utils/url-helpers";
export { rateLimit } from "./utils/rate-limiter";

// =============================================================================
// Browser pool exports (for advanced usage)
// =============================================================================
export { BrowserPool, HeroBrowserPool } from "./browser/pool";
export { createHeroConfig } from "./browser/hero-config";
export type {
  IBrowserPool,
  PoolConfig,
  BrowserInstance,
  PoolStats,
  HealthStatus,
} from "./browser/types";

// =============================================================================
// Cloudflare exports (for advanced usage)
// =============================================================================
export { detectChallenge, isChallengePage } from "./cloudflare/detector";
export { waitForChallengeResolution, waitForSelector, handleChallenge } from "./cloudflare/handler";
export type {
  ChallengeDetection,
  ChallengeResolutionResult,
  ChallengeWaitOptions,
} from "./cloudflare/types";

// =============================================================================
// Proxy exports (for advanced usage)
// =============================================================================
export { createProxyUrl, parseProxyUrl } from "./proxy/config";

// =============================================================================
// Default options export
// =============================================================================
export { DEFAULT_OPTIONS, isValidFormat, shouldCrawlUrl as shouldCrawlUrlFn } from "./types";

// =============================================================================
// Error exports
// =============================================================================
export {
  ReaderError,
  ReaderErrorCode,
  NetworkError,
  TimeoutError,
  CloudflareError,
  AccessDeniedError,
  ContentExtractionError,
  ValidationError,
  InvalidUrlError,
  RobotsBlockedError,
  BrowserPoolError,
  ClientClosedError,
  NotInitializedError,
  wrapError,
} from "./errors";
```

## File: `src/scraper.ts`
```typescript
import pLimit from "p-limit";
import { htmlToMarkdown } from "./formatters/markdown";
import { cleanContent } from "./utils/content-cleaner";
import { extractMetadata } from "./utils/metadata-extractor";
import { createLogger } from "./utils/logger";
import { fetchRobotsTxt, isUrlAllowed, type RobotsRules } from "./utils/robots-parser";
import {
  DEFAULT_OPTIONS,
  type ScrapeOptions,
  type ScrapeResult,
  type WebsiteScrapeResult,
  type BatchMetadata,
  type ProxyMetadata,
} from "./types";
import { EngineOrchestrator, AllEnginesFailedError } from "./engines/index.js";

/**
 * Scraper class with built-in concurrency support
 *
 * Features:
 * - Hero-based browser automation
 * - Automatic Cloudflare challenge detection and bypass
 * - Built-in concurrency via browser pool
 * - Progress tracking
 * - Error handling per URL
 *
 * @example
 * const scraper = new Scraper({
 *   urls: ['https://example.com', 'https://example.org'],
 *   formats: ['markdown', 'html'],
 *   batchConcurrency: 2,
 *   proxy: { type: 'residential', ... }
 * });
 *
 * const result = await scraper.scrape();
 * console.log(`Scraped ${result.batchMetadata.successfulUrls} URLs`);
 */
export class Scraper {
  private options: Required<ScrapeOptions>;
  private logger = createLogger("scraper");
  private robotsCache: Map<string, RobotsRules | null> = new Map();

  constructor(options: ScrapeOptions) {
    // Merge with defaults
    this.options = {
      ...DEFAULT_OPTIONS,
      ...options,
    } as Required<ScrapeOptions>;

    // Pool is required for Hero engine (but may not be needed if using http/tlsclient only)
    // The orchestrator will check availability when needed
  }

  /**
   * Get robots.txt rules for a URL, cached per domain
   */
  private async getRobotsRules(url: string): Promise<RobotsRules | null> {
    const origin = new URL(url).origin;
    if (!this.robotsCache.has(origin)) {
      const rules = await fetchRobotsTxt(origin);
      this.robotsCache.set(origin, rules);
    }
    return this.robotsCache.get(origin) ?? null;
  }

  /**
   * Scrape all URLs
   *
   * @returns Scrape result with pages and metadata
   */
  async scrape(): Promise<ScrapeResult> {
    const startTime = Date.now();

    // Pool is managed by ReaderClient - just use it
    // Scrape URLs with concurrency control
    const results = await this.scrapeWithConcurrency();

    // Build response
    return this.buildScrapeResult(results, startTime);
  }

  /**
   * Scrape URLs with concurrency control
   */
  private async scrapeWithConcurrency(): Promise<
    Array<{ result: WebsiteScrapeResult | null; error?: string }>
  > {
    const limit = pLimit(this.options.batchConcurrency || 1);
    const tasks = this.options.urls.map((url, index) =>
      limit(() => this.scrapeSingleUrlWithRetry(url, index))
    );

    const batchPromise = Promise.all(tasks);

    // Apply batch timeout if specified
    if (this.options.batchTimeoutMs && this.options.batchTimeoutMs > 0) {
      const timeoutPromise = new Promise<never>((_, reject) => {
        setTimeout(() => {
          reject(new Error(`Batch operation timed out after ${this.options.batchTimeoutMs}ms`));
        }, this.options.batchTimeoutMs);
      });

      return Promise.race([batchPromise, timeoutPromise]);
    }

    return batchPromise;
  }

  /**
   * Scrape a single URL with retry logic
   */
  private async scrapeSingleUrlWithRetry(
    url: string,
    index: number
  ): Promise<{ result: WebsiteScrapeResult | null; error?: string }> {
    const maxRetries = this.options.maxRetries || 2;
    let lastError: string | undefined;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
      try {
        const result = await this.scrapeSingleUrl(url, index);
        if (result) {
          return { result };
        }
        // Result is null but no exception - unexpected state
        lastError = `Failed to scrape ${url}: No content returned`;
      } catch (error: any) {
        lastError = error.message;
        if (attempt < maxRetries) {
          // Exponential backoff: 1s, 2s, 4s...
          const delay = Math.pow(2, attempt) * 1000;
          this.logger.warn(`Retry ${attempt + 1}/${maxRetries} for ${url} in ${delay}ms`);
          await new Promise((resolve) => setTimeout(resolve, delay));
        }
      }
    }

    this.logger.error(`Failed to scrape ${url} after ${maxRetries + 1} attempts: ${lastError}`);
    return { result: null, error: lastError };
  }

  /**
   * Scrape a single URL using the engine orchestrator
   */
  private async scrapeSingleUrl(url: string, index: number): Promise<WebsiteScrapeResult | null> {
    const startTime = Date.now();

    // Check robots.txt before scraping
    const robotsRules = await this.getRobotsRules(url);
    if (!isUrlAllowed(url, robotsRules)) {
      throw new Error(`URL blocked by robots.txt: ${url}`);
    }

    try {
      // Create orchestrator with configured engines
      const orchestrator = new EngineOrchestrator({
        engines: this.options.engines,
        skipEngines: this.options.skipEngines,
        forceEngine: this.options.forceEngine,
        logger: this.logger,
        verbose: this.options.verbose,
      });

      // Use orchestrator to fetch HTML
      const engineResult = await orchestrator.scrape({
        url,
        options: this.options,
        logger: this.logger,
      });

      if (this.options.verbose) {
        this.logger.info(
          `[scraper] ${url} scraped with ${engineResult.engine} engine in ${engineResult.duration}ms ` +
            `(attempted: ${engineResult.attemptedEngines.join(" → ")})`
        );
      }

      // Clean content with configurable options
      const cleanedHtml = cleanContent(engineResult.html, engineResult.url, {
        removeAds: this.options.removeAds,
        removeBase64Images: this.options.removeBase64Images,
        onlyMainContent: this.options.onlyMainContent,
        includeTags: this.options.includeTags,
        excludeTags: this.options.excludeTags,
      });

      // Extract metadata
      const websiteMetadata = extractMetadata(cleanedHtml, engineResult.url);

      const duration = Date.now() - startTime;

      // Convert to requested formats
      const markdown = this.options.formats.includes("markdown")
        ? htmlToMarkdown(cleanedHtml)
        : undefined;

      const htmlOutput = this.options.formats.includes("html") ? cleanedHtml : undefined;

      // Report progress
      if (this.options.onProgress) {
        this.options.onProgress({
          completed: index + 1,
          total: this.options.urls.length,
          currentUrl: url,
        });
      }

      // Build proxy metadata if proxy was used
      let proxyMetadata: ProxyMetadata | undefined;
      if (this.options.proxy) {
        const proxy = this.options.proxy;
        // Extract host and port from either url or direct config
        if (proxy.url) {
          try {
            const proxyUrl = new URL(proxy.url);
            proxyMetadata = {
              host: proxyUrl.hostname,
              port: parseInt(proxyUrl.port, 10) || 80,
              country: proxy.country,
            };
          } catch {
            // Invalid URL, skip proxy metadata
          }
        } else if (proxy.host && proxy.port) {
          proxyMetadata = {
            host: proxy.host,
            port: proxy.port,
            country: proxy.country,
          };
        }
      }

      // Build result
      const result: WebsiteScrapeResult = {
        markdown,
        html: htmlOutput,
        metadata: {
          baseUrl: url,
          totalPages: 1,
          scrapedAt: new Date().toISOString(),
          duration,
          website: websiteMetadata,
          proxy: proxyMetadata,
        },
      };

      return result;
    } catch (error: unknown) {
      // Handle AllEnginesFailedError with detailed logging
      if (error instanceof AllEnginesFailedError) {
        const engineSummary = error.attemptedEngines
          .map((e) => `${e}: ${error.errors.get(e)?.message || "unknown"}`)
          .join("; ");
        this.logger.error(`Failed to scrape ${url}: All engines failed - ${engineSummary}`);
      } else if (error instanceof Error) {
        this.logger.error(`Failed to scrape ${url}: ${error.message}`);
      } else {
        this.logger.error(`Failed to scrape ${url}: ${String(error)}`);
      }

      // Report progress (failed)
      if (this.options.onProgress) {
        this.options.onProgress({
          completed: index + 1,
          total: this.options.urls.length,
          currentUrl: url,
        });
      }

      return null; // Return null for failed URLs
    }
  }

  /**
   * Build final scrape result
   */
  private buildScrapeResult(
    results: Array<{ result: WebsiteScrapeResult | null; error?: string }>,
    startTime: number
  ): ScrapeResult {
    const successful = results
      .filter((r) => r.result !== null)
      .map((r) => r.result as WebsiteScrapeResult);

    const errors: Array<{ url: string; error: string }> = [];
    results.forEach((r, index) => {
      if (r.result === null && r.error) {
        errors.push({ url: this.options.urls[index], error: r.error });
      }
    });

    const batchMetadata: BatchMetadata = {
      totalUrls: this.options.urls.length,
      successfulUrls: successful.length,
      failedUrls: results.filter((r) => r.result === null).length,
      scrapedAt: new Date().toISOString(),
      totalDuration: Date.now() - startTime,
      errors,
    };

    return {
      data: successful,
      batchMetadata,
    };
  }
}

/**
 * Convenience function to scrape URLs
 *
 * @param options - Scrape options
 * @returns Scrape result
 *
 * @example
 * const result = await scrape({
 *   urls: ['https://example.com'],
 *   formats: ['markdown']
 * });
 */
export async function scrape(options: ScrapeOptions): Promise<ScrapeResult> {
  const scraper = new Scraper(options);
  return scraper.scrape();
}
```

## File: `src/types.ts`
```typescript
import type { IBrowserPool } from "./browser/types";
import type { EngineName } from "./engines/types.js";

/**
 * Proxy configuration for Hero
 */
export interface ProxyConfig {
  /** Full proxy URL (takes precedence over other fields) */
  url?: string;
  /** Proxy type */
  type?: "datacenter" | "residential";
  /** Proxy username */
  username?: string;
  /** Proxy password */
  password?: string;
  /** Proxy host */
  host?: string;
  /** Proxy port */
  port?: number;
  /** Country code for residential proxies (e.g., 'us', 'uk') */
  country?: string;
}

/**
 * Proxy metadata in scrape results
 */
export interface ProxyMetadata {
  /** Proxy host that was used */
  host: string;
  /** Proxy port that was used */
  port: number;
  /** Country code if geo-targeting was used */
  country?: string;
}

/**
 * Browser pool configuration for ReaderClient
 */
export interface BrowserPoolConfig {
  /** Number of browser instances (default: 2) */
  size?: number;
  /** Retire browser after this many page loads (default: 100) */
  retireAfterPages?: number;
  /** Retire browser after this many minutes (default: 30) */
  retireAfterMinutes?: number;
  /** Maximum pending requests in queue (default: 100) */
  maxQueueSize?: number;
}

/**
 * Main scraping options interface
 */
export interface ScrapeOptions {
  /** Array of URLs to scrape */
  urls: string[];

  /** Output formats - which content fields to include (default: ['markdown']) */
  formats?: Array<"markdown" | "html">;

  /** Custom user agent string */
  userAgent?: string;

  /** Custom headers for requests */
  headers?: Record<string, string>;

  /** Request timeout in milliseconds (default: 30000) */
  timeoutMs?: number;

  /** URL patterns to include (regex strings) */
  includePatterns?: string[];

  /** URL patterns to exclude (regex strings) */
  excludePatterns?: string[];

  // ============================================================================
  // Content cleaning options
  // ============================================================================

  /** Remove ads and tracking elements (default: true) */
  removeAds?: boolean;

  /** Remove base64-encoded images to reduce output size (default: true) */
  removeBase64Images?: boolean;

  /** Extract only main content, removing nav/header/footer/sidebar (default: true) */
  onlyMainContent?: boolean;

  /** CSS selectors for elements to include (if set, only these elements are kept) */
  includeTags?: string[];

  /** CSS selectors for elements to exclude (removed from output) */
  excludeTags?: string[];

  /** Skip TLS/SSL certificate verification (default: true) */
  skipTLSVerification?: boolean;

  // ============================================================================
  // Batch processing options
  // ============================================================================

  /** Number of URLs to process in parallel (default: 1 - sequential) */
  batchConcurrency?: number;

  /** Total timeout for the entire batch operation in milliseconds (default: 300000) */
  batchTimeoutMs?: number;

  /** Maximum retry attempts for failed URLs (default: 2) */
  maxRetries?: number;

  /** Progress callback for batch operations */
  onProgress?: (progress: { completed: number; total: number; currentUrl: string }) => void;

  // ============================================================================
  // Hero-specific options
  // ============================================================================

  /** Proxy configuration for Hero */
  proxy?: ProxyConfig;

  /** CSS selector to wait for before considering page loaded */
  waitForSelector?: string;

  /** Enable verbose logging (default: false) */
  verbose?: boolean;

  /** Show Chrome window (default: false) */
  showChrome?: boolean;

  /** Connection to Hero Core (for shared Core usage) */
  connectionToCore?: any;

  /** Browser pool configuration (passed from ReaderClient) */
  browserPool?: BrowserPoolConfig;

  /** Browser pool instance (internal, provided by ReaderClient) */
  pool?: IBrowserPool;

  // ============================================================================
  // Engine options
  // ============================================================================

  /** Engines to use in order (default: ['http', 'tlsclient', 'hero']) */
  engines?: EngineName[];

  /** Skip specific engines (e.g., ['http'] to skip native fetch) */
  skipEngines?: EngineName[];

  /** Force a specific engine, skipping the cascade */
  forceEngine?: EngineName;
}

/**
 * Website metadata extracted from the base page
 */
export interface WebsiteMetadata {
  /** Basic meta tags */
  title: string | null /** <title> or <meta property="og:title"> */;
  description: string | null /** <meta name="description"> */;
  author: string | null /** <meta name="author"> */;
  language: string | null /** <html lang="..."> */;
  charset: string | null /** <meta charset="..."> */;

  /** Links */
  favicon: string | null /** <link rel="icon"> */;
  image: string | null /** <meta property="og:image"> */;
  canonical: string | null /** <link rel="canonical"> */;

  /** SEO */
  keywords: string[] | null /** <meta name="keywords"> */;
  robots: string | null /** <meta name="robots"> */;

  /** Branding */
  themeColor: string | null /** <meta name="theme-color"> */;

  /** Open Graph */
  openGraph: {
    title: string | null /** <meta property="og:title"> */;
    description: string | null /** <meta property="og:description"> */;
    type: string | null /** <meta property="og:type"> */;
    url: string | null /** <meta property="og:url"> */;
    image: string | null /** <meta property="og:image"> */;
    siteName: string | null /** <meta property="og:site_name"> */;
    locale: string | null /** <meta property="og:locale"> */;
  } | null;

  /** Twitter Card */
  twitter: {
    card: string | null /** <meta name="twitter:card"> */;
    site: string | null /** <meta name="twitter:site"> */;
    creator: string | null /** <meta name="twitter:creator"> */;
    title: string | null /** <meta name="twitter:title"> */;
    description: string | null /** <meta name="twitter:description"> */;
    image: string | null /** <meta name="twitter:image"> */;
  } | null;
}

/**
 * Individual page data
 */
export interface Page {
  /** Full URL of the page */
  url: string;

  /** Page title */
  title: string;

  /** Markdown content */
  markdown: string;

  /** HTML content */
  html: string;

  /** When the page was fetched */
  fetchedAt: string;

  /** Crawl depth from base URL */
  depth: number;

  // ============================================================================
  // Hero-specific fields
  // ============================================================================

  /** Whether a Cloudflare challenge was detected */
  hadChallenge?: boolean;

  /** Type of challenge encountered */
  challengeType?: string;

  /** Time spent waiting for challenge resolution (ms) */
  waitTimeMs?: number;
}

/**
 * Individual website scrape result
 */
export interface WebsiteScrapeResult {
  /** Markdown content (present if 'markdown' in formats) */
  markdown?: string;

  /** HTML content (present if 'html' in formats) */
  html?: string;

  /** Metadata about the scraping operation */
  metadata: {
    /** Base URL that was scraped */
    baseUrl: string;

    /** Total number of pages scraped */
    totalPages: number;

    /** ISO timestamp when scraping started */
    scrapedAt: string;

    /** Duration in milliseconds */
    duration: number;

    /** Website metadata extracted from base page */
    website: WebsiteMetadata;

    /** Proxy used for this request (if proxy pooling was enabled) */
    proxy?: ProxyMetadata;
  };
}

/**
 * Batch metadata for multi-URL operations
 */
export interface BatchMetadata {
  /** Total number of URLs provided */
  totalUrls: number;

  /** Number of URLs successfully scraped */
  successfulUrls: number;

  /** Number of URLs that failed */
  failedUrls: number;

  /** ISO timestamp when the batch operation started */
  scrapedAt: string;

  /** Total duration for the entire batch in milliseconds */
  totalDuration: number;

  /** Array of errors for failed URLs */
  errors?: Array<{ url: string; error: string }>;
}

/**
 * Main scrape result interface
 */
export interface ScrapeResult {
  /** Array of individual website results */
  data: WebsiteScrapeResult[];

  /** Metadata about the batch operation */
  batchMetadata: BatchMetadata;
}

/**
 * Internal crawler state
 */
export interface CrawlerState {
  /** Set of visited URLs to avoid duplicates */
  visited: Set<string>;

  /** Queue of URLs to process */
  queue: Array<{ url: string; depth: number }>;

  /** Completed pages */
  pages: Page[];
}

/**
 * Internal scraper configuration
 */
export interface ScraperConfig {
  /** Merged options with defaults */
  options: Required<ScrapeOptions>;

  /** Parsed base URL */
  baseUrl: URL;

  /** Base domain for same-origin checking */
  baseDomain: string;
}

/**
 * Default scrape options
 */
export const DEFAULT_OPTIONS: Omit<
  Required<ScrapeOptions>,
  "proxy" | "waitForSelector" | "connectionToCore" | "userAgent" | "headers" | "browserPool" | "pool" | "engines" | "skipEngines" | "forceEngine"
> & {
  proxy?: ProxyConfig;
  waitForSelector?: string;
  connectionToCore?: any;
  userAgent?: string;
  headers?: Record<string, string>;
  browserPool?: BrowserPoolConfig;
  pool?: IBrowserPool;
  engines?: EngineName[];
  skipEngines?: EngineName[];
  forceEngine?: EngineName;
} = {
  urls: [],
  formats: ["markdown"],
  timeoutMs: 30000,
  includePatterns: [],
  excludePatterns: [],
  // Content cleaning defaults
  removeAds: true,
  removeBase64Images: true,
  onlyMainContent: true,
  includeTags: [],
  excludeTags: [],
  skipTLSVerification: true,
  // Batch defaults
  batchConcurrency: 1,
  batchTimeoutMs: 300000,
  maxRetries: 2,
  onProgress: () => {}, // Default no-op progress callback
  // Hero-specific defaults
  verbose: false,
  showChrome: false,
};

/**
 * Format type guard
 */
export function isValidFormat(format: string): format is "markdown" | "html" {
  return format === "markdown" || format === "html";
}

/**
 * Check if a URL should be crawled based on base domain
 */
export function shouldCrawlUrl(url: URL, baseDomain: string): boolean {
  return url.hostname === baseDomain || url.hostname.endsWith(`.${baseDomain}`);
}
```

## File: `src/browser/hero-config.ts`
```typescript
import type { ProxyConfig } from "../types";
import { createProxyUrl } from "../proxy/config";

/**
 * Hero configuration options
 */
export interface HeroConfigOptions {
  /** Proxy configuration */
  proxy?: ProxyConfig;
  /** Show Chrome window (default: false) */
  showChrome?: boolean;
  /** Custom user agent */
  userAgent?: string;
  /** Connection to Core (for in-process Core) */
  connectionToCore?: any;
}

/**
 * Create Hero configuration with optimal anti-bot bypass settings
 *
 * Extracted from proven hero-test implementation.
 * Includes:
 * - TLS fingerprint emulation (disableMitm: false)
 * - DNS over TLS (mimics Chrome)
 * - WebRTC IP masking
 * - Proper locale and timezone
 *
 * @param options - Configuration options
 * @returns Hero configuration object
 */
export function createHeroConfig(options: HeroConfigOptions = {}): any {
  const config: any = {
    // Show or hide Chrome window
    showChrome: options.showChrome ?? false,

    // ============================================================================
    // CRITICAL: TLS fingerprint emulation
    // ============================================================================
    // Setting disableMitm to false enables TLS/TCP fingerprint emulation
    // This is ESSENTIAL for bypassing Cloudflare and other anti-bot systems
    disableMitm: false,

    // ============================================================================
    // Session management
    // ============================================================================
    // Use incognito for clean session state
    disableIncognito: false,

    // ============================================================================
    // Docker compatibility
    // ============================================================================
    // Required when running in containerized environments
    noChromeSandbox: true,

    // ============================================================================
    // DNS over TLS (mimics Chrome behavior)
    // ============================================================================
    // Using Cloudflare's DNS (1.1.1.1) over TLS makes the connection
    // look more like a real Chrome browser
    dnsOverTlsProvider: {
      host: "1.1.1.1",
      servername: "cloudflare-dns.com",
    },

    // ============================================================================
    // WebRTC IP leak prevention
    // ============================================================================
    // Masks the real IP address in WebRTC connections
    // Uses ipify.org to detect the public IP
    upstreamProxyIpMask: {
      ipLookupService: "https://api.ipify.org?format=json",
    },

    // ============================================================================
    // Locale and timezone
    // ============================================================================
    locale: "en-US",
    timezoneId: "America/New_York",

    // ============================================================================
    // Viewport (standard desktop size)
    // ============================================================================
    viewport: {
      width: 1920,
      height: 1080,
    },

    // ============================================================================
    // User agent (if provided)
    // ============================================================================
    ...(options.userAgent && { userAgent: options.userAgent }),

    // ============================================================================
    // Connection to Core (if provided)
    // ============================================================================
    ...(options.connectionToCore && { connectionToCore: options.connectionToCore }),
  };

  // ============================================================================
  // Proxy configuration
  // ============================================================================
  if (options.proxy) {
    config.upstreamProxyUrl = createProxyUrl(options.proxy);
    // Don't use system DNS when using proxy
    config.upstreamProxyUseSystemDns = false;
  }

  return config;
}

/**
 * Default Hero configuration (no proxy)
 */
export function getDefaultHeroConfig(): any {
  return createHeroConfig();
}
```

## File: `src/browser/pool.ts`
```typescript
import Hero from "@ulixee/hero";
import { createHeroConfig } from "./hero-config";
import type {
  BrowserInstance,
  QueueItem,
  PoolConfig,
  PoolStats,
  HealthStatus,
  IBrowserPool,
} from "./types";
import type { ProxyConfig } from "../types";
import { createLogger } from "../utils/logger";

/**
 * Default pool configuration
 */
const DEFAULT_POOL_CONFIG: PoolConfig = {
  size: 2,
  retireAfterPageCount: 100,
  retireAfterAgeMs: 30 * 60 * 1000, // 30 minutes
  recycleCheckInterval: 60 * 1000, // 1 minute
  healthCheckInterval: 5 * 60 * 1000, // 5 minutes
  maxConsecutiveFailures: 3,
  maxQueueSize: 100,
  queueTimeout: 60 * 1000, // 1 minute
};

/**
 * Generate unique ID
 */
function generateId(): string {
  return `browser_${Date.now()}_${Math.random().toString(36).slice(2, 9)}`;
}

/**
 * Browser Pool
 *
 * Manages a pool of Hero browser instances with:
 * - Auto-recycling based on age/request count
 * - Request queuing when pool is full
 * - Health monitoring
 *
 * @example
 * const pool = new BrowserPool({ size: 5 });
 * await pool.initialize();
 *
 * // Use withBrowser for automatic acquire/release
 * await pool.withBrowser(async (hero) => {
 *   await hero.goto('https://example.com');
 *   const title = await hero.document.title;
 *   return title;
 * });
 *
 * await pool.shutdown();
 */
export class BrowserPool implements IBrowserPool {
  private instances: BrowserInstance[] = [];
  private available: BrowserInstance[] = [];
  private inUse: Set<BrowserInstance> = new Set();
  private queue: QueueItem[] = [];
  private config: PoolConfig;
  private proxy?: ProxyConfig;
  private recycleTimer?: NodeJS.Timeout;
  private healthTimer?: NodeJS.Timeout;
  private totalRequests = 0;
  private totalRequestDuration = 0;
  private showChrome: boolean;
  private connectionToCore?: any;
  private userAgent?: string;
  private verbose: boolean;
  private logger = createLogger("pool");

  constructor(
    config: Partial<PoolConfig> = {},
    proxy?: ProxyConfig,
    showChrome: boolean = false,
    connectionToCore?: any,
    userAgent?: string,
    verbose: boolean = false
  ) {
    this.config = { ...DEFAULT_POOL_CONFIG, ...config };
    this.proxy = proxy;
    this.showChrome = showChrome;
    this.connectionToCore = connectionToCore;
    this.userAgent = userAgent;
    this.verbose = verbose;
  }

  /**
   * Initialize the pool by pre-launching browsers
   */
  async initialize(): Promise<void> {
    if (this.verbose) {
      this.logger.info(`Initializing pool with ${this.config.size} browsers...`);
    }

    // Pre-launch browsers
    const launchPromises: Promise<BrowserInstance>[] = [];
    for (let i = 0; i < this.config.size; i++) {
      launchPromises.push(this.createInstance());
    }

    this.instances = await Promise.all(launchPromises);
    this.available = [...this.instances];

    // Start background tasks
    this.startRecycling();
    this.startHealthChecks();

    if (this.verbose) {
      this.logger.info(`Pool ready: ${this.instances.length} browsers available`);
    }
  }

  /**
   * Shutdown the pool and close all browsers
   */
  async shutdown(): Promise<void> {
    if (this.verbose) {
      const stats = this.getStats();
      this.logger.info(
        `Shutting down pool: ${stats.totalRequests} total requests processed, ` +
          `${Math.round(stats.avgRequestDuration)}ms avg duration`
      );
    }

    // Stop background tasks
    if (this.recycleTimer) clearInterval(this.recycleTimer);
    if (this.healthTimer) clearInterval(this.healthTimer);

    // Reject all queued requests
    for (const item of this.queue) {
      item.reject(new Error("Pool shutting down"));
    }
    this.queue = [];

    // Close all browsers
    const closePromises = this.instances.map((instance) => instance.hero.close().catch(() => {}));
    await Promise.all(closePromises);

    // Disconnect the connection to core to release event listeners
    if (this.connectionToCore) {
      try {
        await this.connectionToCore.disconnect();
      } catch {
        // Ignore disconnect errors
      }
      this.connectionToCore = undefined;
    }

    // Clear instances
    this.instances = [];
    this.available = [];
    this.inUse.clear();
  }

  /**
   * Acquire a browser from the pool
   */
  async acquire(): Promise<Hero> {
    // Get available instance
    const instance = this.available.shift();
    if (!instance) {
      // No available instances, queue the request
      if (this.verbose) {
        this.logger.info(`No browsers available, queuing request (queue: ${this.queue.length + 1})`);
      }
      return this.queueRequest();
    }

    // Mark as busy
    instance.status = "busy";
    instance.lastUsed = Date.now();
    this.inUse.add(instance);

    if (this.verbose) {
      this.logger.info(
        `Acquired browser ${instance.id} (available: ${this.available.length}, busy: ${this.inUse.size})`
      );
    }

    return instance.hero;
  }

  /**
   * Release a browser back to the pool
   */
  release(hero: Hero): void {
    const instance = this.instances.find((i) => i.hero === hero);
    if (!instance) return;

    // Update stats
    instance.status = "idle";
    instance.requestCount++;
    this.inUse.delete(instance);

    if (this.verbose) {
      this.logger.info(
        `Released browser ${instance.id} (requests: ${instance.requestCount}, available: ${this.available.length + 1})`
      );
    }

    // Check if needs recycling
    if (this.shouldRecycle(instance)) {
      if (this.verbose) {
        this.logger.info(`Recycling browser ${instance.id} (age or request limit reached)`);
      }
      this.recycleInstance(instance).catch(() => {});
    } else {
      this.available.push(instance);
      this.processQueue();
    }
  }

  /**
   * Execute callback with auto-managed browser
   */
  async withBrowser<T>(callback: (hero: Hero) => Promise<T>): Promise<T> {
    const startTime = Date.now();
    const hero = await this.acquire();

    try {
      const result = await callback(hero);

      // Update request stats
      this.totalRequests++;
      this.totalRequestDuration += Date.now() - startTime;

      return result;
    } finally {
      this.release(hero);
    }
  }

  /**
   * Get pool statistics
   */
  getStats(): PoolStats {
    const recycling = this.instances.filter((i) => i.status === "recycling").length;
    const unhealthy = this.instances.filter((i) => i.status === "unhealthy").length;

    return {
      total: this.instances.length,
      available: this.available.length,
      busy: this.inUse.size,
      recycling,
      unhealthy,
      queueLength: this.queue.length,
      totalRequests: this.totalRequests,
      avgRequestDuration:
        this.totalRequests > 0 ? this.totalRequestDuration / this.totalRequests : 0,
    };
  }

  /**
   * Run health check
   */
  async healthCheck(): Promise<HealthStatus> {
    const issues: string[] = [];
    const stats = this.getStats();

    // Check for unhealthy instances
    if (stats.unhealthy > 0) {
      issues.push(`${stats.unhealthy} unhealthy instances`);
    }

    // Check queue size
    if (stats.queueLength > this.config.maxQueueSize * 0.8) {
      issues.push(`Queue near capacity: ${stats.queueLength}/${this.config.maxQueueSize}`);
    }

    // Check if pool is saturated
    if (stats.available === 0 && stats.queueLength > 0) {
      issues.push("Pool saturated - all browsers busy with pending requests");
    }

    return {
      healthy: issues.length === 0,
      issues,
      stats,
    };
  }

  // =========================================================================
  // Private methods
  // =========================================================================

  /**
   * Create a new browser instance
   */
  private async createInstance(): Promise<BrowserInstance> {
    const heroConfig = createHeroConfig({
      proxy: this.proxy,
      showChrome: this.showChrome,
      connectionToCore: this.connectionToCore,
      userAgent: this.userAgent,
    });

    const hero = new Hero(heroConfig);

    return {
      hero,
      id: generateId(),
      createdAt: Date.now(),
      lastUsed: Date.now(),
      requestCount: 0,
      status: "idle",
    };
  }

  /**
   * Check if instance should be recycled
   */
  private shouldRecycle(instance: BrowserInstance): boolean {
    const age = Date.now() - instance.createdAt;
    return (
      instance.requestCount >= this.config.retireAfterPageCount ||
      age >= this.config.retireAfterAgeMs
    );
  }

  /**
   * Recycle an instance (close old, create new)
   */
  private async recycleInstance(instance: BrowserInstance): Promise<void> {
    instance.status = "recycling";

    try {
      // Close old instance
      await instance.hero.close().catch(() => {});

      // Create new instance
      const newInstance = await this.createInstance();

      // Replace in instances array
      const index = this.instances.indexOf(instance);
      if (index !== -1) {
        this.instances[index] = newInstance;
      }

      // Add to available pool
      this.available.push(newInstance);

      if (this.verbose) {
        this.logger.info(`Recycled browser: ${instance.id} → ${newInstance.id}`);
      }

      // Process queue
      this.processQueue();
    } catch (error) {
      // Failed to recycle, mark as unhealthy
      instance.status = "unhealthy";
      if (this.verbose) {
        this.logger.warn(`Failed to recycle browser ${instance.id}`);
      }
    }
  }

  /**
   * Queue a request when no browsers available
   */
  private queueRequest(): Promise<Hero> {
    return new Promise<Hero>((resolve, reject) => {
      // Check queue size
      if (this.queue.length >= this.config.maxQueueSize) {
        reject(new Error("Queue full"));
        return;
      }

      // Add to queue
      const item: QueueItem = {
        resolve,
        reject,
        queuedAt: Date.now(),
      };
      this.queue.push(item);

      // Set timeout
      setTimeout(() => {
        const index = this.queue.indexOf(item);
        if (index !== -1) {
          this.queue.splice(index, 1);
          reject(new Error("Queue timeout"));
        }
      }, this.config.queueTimeout);
    });
  }

  /**
   * Process queued requests
   */
  private processQueue(): void {
    while (this.queue.length > 0 && this.available.length > 0) {
      const item = this.queue.shift()!;

      // Check if still valid (not timed out)
      const age = Date.now() - item.queuedAt;
      if (age > this.config.queueTimeout) {
        item.reject(new Error("Queue timeout"));
        continue;
      }

      // Acquire and resolve
      this.acquire().then(item.resolve).catch(item.reject);
    }
  }

  /**
   * Start background recycling task
   */
  private startRecycling(): void {
    this.recycleTimer = setInterval(() => {
      for (const instance of this.instances) {
        if (instance.status === "idle" && this.shouldRecycle(instance)) {
          this.recycleInstance(instance).catch(() => {});
        }
      }
    }, this.config.recycleCheckInterval);
    // Allow process to exit even if timer is still running
    this.recycleTimer.unref();
  }

  /**
   * Start background health checks
   */
  private startHealthChecks(): void {
    this.healthTimer = setInterval(async () => {
      const health = await this.healthCheck();
      if (!health.healthy && health.issues.length > 0) {
        console.warn("[BrowserPool] Health issues:", health.issues);
      }
    }, this.config.healthCheckInterval);
    // Allow process to exit even if timer is still running
    this.healthTimer.unref();
  }
}

// Backward compatibility alias
export { BrowserPool as HeroBrowserPool };
```

## File: `src/browser/types.ts`
```typescript
import type Hero from "@ulixee/hero";

/**
 * Browser instance in the pool
 */
export interface BrowserInstance {
  /** Hero instance */
  hero: Hero;

  /** Unique identifier */
  id: string;

  /** When the instance was created */
  createdAt: number;

  /** When the instance was last used */
  lastUsed: number;

  /** Number of requests handled */
  requestCount: number;

  /** Current status */
  status: "idle" | "busy" | "recycling" | "unhealthy";
}

/**
 * Queue item for pending requests
 */
export interface QueueItem {
  /** Promise resolve function */
  resolve: (hero: Hero) => void;

  /** Promise reject function */
  reject: (error: Error) => void;

  /** When the request was queued */
  queuedAt: number;
}

/**
 * Pool configuration
 */
export interface PoolConfig {
  /** Pool size (number of browser instances) */
  size: number;

  /** Retire browser after this many page loads */
  retireAfterPageCount: number;

  /** Retire browser after this age in milliseconds */
  retireAfterAgeMs: number;

  /** How often to check for recycling (ms) */
  recycleCheckInterval: number;

  /** How often to run health checks (ms) */
  healthCheckInterval: number;

  /** Max consecutive failures before marking unhealthy */
  maxConsecutiveFailures: number;

  /** Maximum queue size */
  maxQueueSize: number;

  /** Queue timeout in milliseconds */
  queueTimeout: number;
}

/**
 * Pool statistics
 */
export interface PoolStats {
  /** Total instances */
  total: number;

  /** Available instances */
  available: number;

  /** Busy instances */
  busy: number;

  /** Recycling instances */
  recycling: number;

  /** Unhealthy instances */
  unhealthy: number;

  /** Queue length */
  queueLength: number;

  /** Total requests handled */
  totalRequests: number;

  /** Average request duration */
  avgRequestDuration: number;
}

/**
 * Health status
 */
export interface HealthStatus {
  /** Overall health */
  healthy: boolean;

  /** Issues found */
  issues: string[];

  /** Stats snapshot */
  stats: PoolStats;
}

/**
 * Browser pool interface
 */
export interface IBrowserPool {
  /** Initialize the pool */
  initialize(): Promise<void>;

  /** Shutdown the pool */
  shutdown(): Promise<void>;

  /** Acquire a browser instance */
  acquire(): Promise<Hero>;

  /** Release a browser instance back to the pool */
  release(hero: Hero): void;

  /** Execute callback with auto-managed browser */
  withBrowser<T>(callback: (hero: Hero) => Promise<T>): Promise<T>;

  /** Get pool statistics */
  getStats(): PoolStats;

  /** Run health check */
  healthCheck?(): Promise<HealthStatus>;
}
```

## File: `src/cli/index.ts`
```typescript
#!/usr/bin/env node
/**
 * Reader CLI
 *
 * Command-line interface for web scraping with Cloudflare bypass.
 *
 * @example
 * # Start daemon (once)
 * npx reader start --pool-size 5
 *
 * # Scrape a single URL (auto-detects daemon)
 * npx reader scrape https://example.com
 *
 * # Scrape multiple URLs with markdown and text output
 * npx reader scrape https://example.com https://example.org -f markdown,text
 *
 * # Crawl a website
 * npx reader crawl https://example.com -d 2 -m 20
 *
 * # Force standalone mode (bypass daemon)
 * npx reader scrape https://example.com --standalone
 *
 * # Check daemon status
 * npx reader status
 *
 * # Stop daemon
 * npx reader stop
 */

import { Command } from "commander";
import { ReaderClient } from "../client";
import { DaemonServer, DaemonClient, isDaemonRunning, getDaemonInfo, DEFAULT_DAEMON_PORT } from "../daemon";
import { readFileSync, writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

// Get version from package.json
const __dirname = dirname(fileURLToPath(import.meta.url));
const pkg = JSON.parse(readFileSync(join(__dirname, "../../package.json"), "utf-8"));

const program = new Command();

program
  .name("reader")
  .description(
    "Production-grade web scraping engine for LLMs. Clean markdown output, ready for your agents."
  )
  .version(pkg.version);

// =============================================================================
// Daemon Commands
// =============================================================================

program
  .command("start")
  .description("Start the reader daemon server")
  .option("-p, --port <n>", `Port to listen on (default: ${DEFAULT_DAEMON_PORT})`, String(DEFAULT_DAEMON_PORT))
  .option("--pool-size <n>", "Browser pool size", "5")
  .option("--show-chrome", "Show browser windows for debugging")
  .option("-v, --verbose", "Enable verbose logging")
  .action(async (options) => {
    const port = parseInt(options.port, 10);

    // Check if daemon is already running
    if (await isDaemonRunning(port)) {
      console.error(`Error: Daemon is already running on port ${port}`);
      process.exit(1);
    }

    const daemon = new DaemonServer({
      port,
      poolSize: parseInt(options.poolSize, 10),
      verbose: options.verbose || false,
      showChrome: options.showChrome || false,
    });

    try {
      await daemon.start();
      console.log(`Reader daemon started on port ${port} with pool size ${options.poolSize}`);
      console.log(`Use "npx reader stop" to stop the daemon`);

      // Keep process running
      process.on("SIGINT", async () => {
        console.log("\nShutting down daemon...");
        await daemon.stop();
        process.exit(0);
      });

      process.on("SIGTERM", async () => {
        await daemon.stop();
        process.exit(0);
      });
    } catch (error: any) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    }
  });

program
  .command("stop")
  .description("Stop the running reader daemon")
  .option("-p, --port <n>", `Daemon port (default: ${DEFAULT_DAEMON_PORT})`, String(DEFAULT_DAEMON_PORT))
  .action(async (options) => {
    const port = parseInt(options.port, 10);
    const client = new DaemonClient({ port });

    try {
      if (!(await client.isRunning())) {
        console.log("Daemon is not running");
        return;
      }

      await client.shutdown();
      console.log("Daemon stopped");
    } catch (error: any) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    }
  });

program
  .command("status")
  .description("Check daemon status")
  .option("-p, --port <n>", `Daemon port (default: ${DEFAULT_DAEMON_PORT})`, String(DEFAULT_DAEMON_PORT))
  .action(async (options) => {
    // First check PID file
    const daemonInfo = await getDaemonInfo();

    if (!daemonInfo) {
      console.log("Daemon is not running");
      return;
    }

    // Use port from options if specified, otherwise from PID file
    const port = options.port ? parseInt(options.port, 10) : daemonInfo.port;

    // Verify it's actually running by connecting
    const client = new DaemonClient({ port });
    try {
      const status = await client.status();
      console.log("Daemon is running:");
      console.log(`  Port: ${status.port}`);
      console.log(`  PID: ${status.pid}`);
      console.log(`  Pool size: ${status.poolSize}`);
      console.log(`  Uptime: ${Math.round(status.uptime / 1000)}s`);
    } catch {
      console.log("Daemon is not running (stale PID file)");
    }
  });

// =============================================================================
// Scrape Command
// =============================================================================

program
  .command("scrape <urls...>")
  .description("Scrape one or more URLs")
  .option(
    "-f, --format <formats>",
    "Content formats to include (comma-separated: markdown,html)",
    "markdown"
  )
  .option("-o, --output <file>", "Output file (stdout if omitted)")
  .option("-c, --concurrency <n>", "Parallel requests", "1")
  .option("-t, --timeout <ms>", "Request timeout in milliseconds", "30000")
  .option("--proxy <url>", "Proxy URL (e.g., http://user:pass@host:port)")
  .option("--user-agent <string>", "Custom user agent string")
  .option("--batch-timeout <ms>", "Total timeout for entire batch operation", "300000")
  .option("--show-chrome", "Show browser window for debugging")
  .option("--standalone", "Force standalone mode (bypass daemon)")
  .option("-p, --port <n>", `Daemon port (default: ${DEFAULT_DAEMON_PORT})`, String(DEFAULT_DAEMON_PORT))
  .option("-v, --verbose", "Enable verbose logging")
  .option("--no-main-content", "Disable main content extraction (include full page)")
  .option("--include-tags <selectors>", "CSS selectors for elements to include (comma-separated)")
  .option("--exclude-tags <selectors>", "CSS selectors for elements to exclude (comma-separated)")
  .option("--engine <name>", "Force a specific engine (http, tlsclient, hero)")
  .option("--skip-engine <names>", "Skip specific engines (comma-separated: http,tlsclient,hero)")
  .action(async (urls: string[], options) => {
    const port = parseInt(options.port, 10);
    const useStandalone = options.standalone || false;

    // Auto-detect daemon unless --standalone is specified
    let useDaemon = false;
    if (!useStandalone) {
      useDaemon = await isDaemonRunning(port);
      if (options.verbose && useDaemon) {
        console.error(`Using daemon on port ${port}`);
      }
    }

    // Create client (daemon or standalone)
    const daemonClient = useDaemon ? new DaemonClient({ port }) : null;
    const standaloneClient = !useDaemon
      ? new ReaderClient({
          verbose: options.verbose || false,
          showChrome: options.showChrome || false,
        })
      : null;

    try {
      const formats = options.format.split(",").map((f: string) => f.trim());

      // Validate formats
      const validFormats = ["markdown", "html"];
      for (const format of formats) {
        if (!validFormats.includes(format)) {
          console.error(
            `Error: Invalid format "${format}". Valid formats: ${validFormats.join(", ")}`
          );
          process.exit(1);
        }
      }

      if (options.verbose) {
        console.error(`Scraping ${urls.length} URL(s)...`);
        console.error(`Formats: ${formats.join(", ")}`);
      }

      // Parse tag selectors
      const includeTags = options.includeTags
        ? options.includeTags.split(",").map((s: string) => s.trim())
        : undefined;
      const excludeTags = options.excludeTags
        ? options.excludeTags.split(",").map((s: string) => s.trim())
        : undefined;

      // Parse engine options
      const skipEngines = options.skipEngine
        ? options.skipEngine.split(",").map((s: string) => s.trim())
        : undefined;

      const scrapeOptions = {
        urls,
        formats,
        batchConcurrency: parseInt(options.concurrency, 10),
        timeoutMs: parseInt(options.timeout, 10),
        batchTimeoutMs: parseInt(options.batchTimeout, 10),
        proxy: options.proxy ? { url: options.proxy } : undefined,
        userAgent: options.userAgent,
        verbose: options.verbose || false,
        showChrome: options.showChrome || false,
        // Content cleaning options
        onlyMainContent: options.mainContent !== false, // --no-main-content sets this to false
        includeTags,
        excludeTags,
        // Engine options
        forceEngine: options.engine,
        skipEngines,
        onProgress: options.verbose
          ? ({ completed, total, currentUrl }: { completed: number; total: number; currentUrl: string }) => {
              console.error(`[${completed}/${total}] ${currentUrl}`);
            }
          : undefined,
      };

      const result = useDaemon
        ? await daemonClient!.scrape(scrapeOptions)
        : await standaloneClient!.scrape(scrapeOptions);

      // Always output JSON
      const output = JSON.stringify(result, null, 2);

      // Write output
      if (options.output) {
        writeFileSync(options.output, output);
        if (options.verbose) {
          console.error(`Output written to ${options.output}`);
        }
      } else {
        console.log(output);
      }

      // Print summary to stderr
      if (options.verbose) {
        console.error(`\nSummary:`);
        console.error(
          `  Successful: ${result.batchMetadata.successfulUrls}/${result.batchMetadata.totalUrls}`
        );
        console.error(`  Duration: ${result.batchMetadata.totalDuration}ms`);
      }

      // Exit with error code if any URLs failed
      if (result.batchMetadata.failedUrls > 0) {
        process.exit(1);
      }
    } catch (error: any) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    } finally {
      if (standaloneClient) {
        await standaloneClient.close();
        process.exit(0);
      }
    }
  });

// =============================================================================
// Crawl Command
// =============================================================================

program
  .command("crawl <url>")
  .description("Crawl a website to discover and optionally scrape pages")
  .option("-d, --depth <n>", "Maximum crawl depth", "1")
  .option("-m, --max-pages <n>", "Maximum pages to discover", "20")
  .option("-s, --scrape", "Also scrape content of discovered pages")
  .option("-f, --format <formats>", "Content formats when scraping (comma-separated: markdown,html)", "markdown")
  .option("-o, --output <file>", "Output file (stdout if omitted)")
  .option("--delay <ms>", "Delay between requests in milliseconds", "1000")
  .option("-t, --timeout <ms>", "Total timeout for crawl operation in milliseconds")
  .option("--include <patterns>", "URL patterns to include (comma-separated regex)")
  .option("--exclude <patterns>", "URL patterns to exclude (comma-separated regex)")
  .option("--proxy <url>", "Proxy URL (e.g., http://user:pass@host:port)")
  .option("--user-agent <string>", "Custom user agent string")
  .option("--show-chrome", "Show browser window for debugging")
  .option("--standalone", "Force standalone mode (bypass daemon)")
  .option("-p, --port <n>", `Daemon port (default: ${DEFAULT_DAEMON_PORT})`, String(DEFAULT_DAEMON_PORT))
  .option("-v, --verbose", "Enable verbose logging")
  .action(async (url: string, options) => {
    const port = parseInt(options.port, 10);
    const useStandalone = options.standalone || false;

    // Auto-detect daemon unless --standalone is specified
    let useDaemon = false;
    if (!useStandalone) {
      useDaemon = await isDaemonRunning(port);
      if (options.verbose && useDaemon) {
        console.error(`Using daemon on port ${port}`);
      }
    }

    // Create client (daemon or standalone)
    const daemonClient = useDaemon ? new DaemonClient({ port }) : null;
    const standaloneClient = !useDaemon
      ? new ReaderClient({
          verbose: options.verbose || false,
          showChrome: options.showChrome || false,
        })
      : null;

    try {
      if (options.verbose) {
        console.error(`Crawling ${url}...`);
        console.error(`Max depth: ${options.depth}, Max pages: ${options.maxPages}`);
      }

      // Parse include/exclude patterns
      const includePatterns = options.include
        ? options.include.split(",").map((p: string) => p.trim())
        : undefined;
      const excludePatterns = options.exclude
        ? options.exclude.split(",").map((p: string) => p.trim())
        : undefined;

      const crawlOptions = {
        url,
        depth: parseInt(options.depth, 10),
        maxPages: parseInt(options.maxPages, 10),
        scrape: options.scrape || false,
        delayMs: parseInt(options.delay, 10),
        timeoutMs: options.timeout ? parseInt(options.timeout, 10) : undefined,
        includePatterns,
        excludePatterns,
        proxy: options.proxy ? { url: options.proxy } : undefined,
        userAgent: options.userAgent,
        verbose: options.verbose || false,
        showChrome: options.showChrome || false,
      };

      // Add formats to crawl options if scraping
      const formats = options.format.split(",").map((f: string) => f.trim());
      const crawlOptionsWithFormats = {
        ...crawlOptions,
        formats,
      };

      const result = useDaemon
        ? await daemonClient!.crawl(crawlOptionsWithFormats)
        : await standaloneClient!.crawl(crawlOptionsWithFormats);

      // Always output JSON
      const output = JSON.stringify(result, null, 2);

      // Write output
      if (options.output) {
        writeFileSync(options.output, output);
        if (options.verbose) {
          console.error(`Output written to ${options.output}`);
        }
      } else {
        console.log(output);
      }

      // Print summary to stderr
      if (options.verbose) {
        console.error(`\nSummary:`);
        console.error(`  Discovered: ${result.urls.length} URLs`);
        console.error(`  Duration: ${result.metadata.totalDuration}ms`);
      }
    } catch (error: any) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    } finally {
      if (standaloneClient) {
        await standaloneClient.close();
        process.exit(0);
      }
    }
  });

// =============================================================================
// Parse and execute
// =============================================================================

program.parse();
```

## File: `src/cloudflare/detector.ts`
```typescript
import type Hero from "@ulixee/hero";
import type { ChallengeDetection } from "./types";

/**
 * CLOUDFLARE-SPECIFIC DOM SELECTORS
 *
 * These are ONLY present during active Cloudflare challenges.
 * We query for actual DOM elements, not string matching.
 */
const CLOUDFLARE_CHALLENGE_SELECTORS = [
  "#challenge-running",
  "#challenge-stage",
  "#challenge-form",
  ".cf-browser-verification",
  "#cf-wrapper",
  "#cf-hcaptcha-container",
  "#turnstile-wrapper",
];

/**
 * CLOUDFLARE-SPECIFIC TEXT PATTERNS
 *
 * These phrases only appear during active Cloudflare challenges.
 * Must be combined with other Cloudflare signals to avoid false positives.
 */
const CLOUDFLARE_TEXT_PATTERNS = [
  "checking if the site connection is secure",
  "this process is automatic. your browser will redirect",
  "ray id:",
  "performance & security by cloudflare",
];

/**
 * CLOUDFLARE INFRASTRUCTURE SIGNALS
 *
 * Indicators that the page is served by Cloudflare
 */
const CLOUDFLARE_INFRA_PATTERNS = [
  "/cdn-cgi/",
  "cloudflare",
  "__cf_bm",
  "cf-ray",
];

/**
 * BLOCKED/403 SIGNALS (Cloudflare-specific)
 *
 * Detect when Cloudflare explicitly blocks access
 */
const CLOUDFLARE_BLOCKED_PATTERNS = [
  "sorry, you have been blocked",
  "ray id:",
];

/**
 * Detect if current page is a Cloudflare challenge
 *
 * Uses multi-signal approach requiring BOTH:
 * 1. Cloudflare infrastructure indicators (cdn-cgi, cf-ray, etc.)
 * 2. Challenge-specific elements or text
 *
 * This prevents false positives on login pages or other sites
 * that happen to use similar text.
 *
 * @param hero - Hero instance with loaded page
 * @returns Detection result with confidence score and signals
 */
export async function detectChallenge(hero: Hero): Promise<ChallengeDetection> {
  const signals: string[] = [];
  let type: ChallengeDetection["type"] = "none";
  let hasCloudflareInfra = false;
  let hasChallengeIndicator = false;

  try {
    // Ensure we have access to document
    if (!hero.document) {
      return {
        isChallenge: false,
        type: "none",
        confidence: 0,
        signals: ["No document available"],
      };
    }

    // =========================================================================
    // CHECK 1: CLOUDFLARE INFRASTRUCTURE (required for any detection)
    // =========================================================================
    const html = await hero.document.documentElement.outerHTML;
    const htmlLower = html.toLowerCase();

    for (const pattern of CLOUDFLARE_INFRA_PATTERNS) {
      if (htmlLower.includes(pattern)) {
        hasCloudflareInfra = true;
        signals.push(`Cloudflare infra: "${pattern}"`);
        break;
      }
    }

    // If no Cloudflare infrastructure detected, it's not a Cloudflare challenge
    if (!hasCloudflareInfra) {
      return {
        isChallenge: false,
        type: "none",
        confidence: 0,
        signals: ["No Cloudflare infrastructure detected"],
      };
    }

    // =========================================================================
    // CHECK 2: CHALLENGE DOM ELEMENTS (using actual DOM queries)
    // =========================================================================
    for (const selector of CLOUDFLARE_CHALLENGE_SELECTORS) {
      try {
        const element = await hero.document.querySelector(selector);
        if (element) {
          hasChallengeIndicator = true;
          signals.push(`Challenge element: ${selector}`);
          type = "js_challenge";
        }
      } catch {
        // Element not found, continue
      }
    }

    // =========================================================================
    // CHECK 3: CHALLENGE-SPECIFIC TEXT
    // =========================================================================
    for (const pattern of CLOUDFLARE_TEXT_PATTERNS) {
      if (htmlLower.includes(pattern)) {
        hasChallengeIndicator = true;
        signals.push(`Challenge text: "${pattern}"`);
        type = type === "none" ? "js_challenge" : type;
      }
    }

    // =========================================================================
    // CHECK 4: "WAITING FOR" + "TO RESPOND" (Cloudflare-specific combo)
    // =========================================================================
    if (htmlLower.includes("waiting for") && htmlLower.includes("to respond")) {
      hasChallengeIndicator = true;
      signals.push('Challenge text: "waiting for...to respond"');
      type = type === "none" ? "js_challenge" : type;
    }

    // =========================================================================
    // CHECK 5: CLOUDFLARE BLOCKED DETECTION
    // =========================================================================
    // Check for blocked page with Ray ID (Cloudflare-specific)
    const hasBlocked = CLOUDFLARE_BLOCKED_PATTERNS.every((p) => htmlLower.includes(p));
    if (hasBlocked) {
      hasChallengeIndicator = true;
      signals.push("Cloudflare block page detected");
      type = "blocked";
    }

    // Challenge only if we have BOTH Cloudflare infra AND challenge indicators
    const isChallenge = hasCloudflareInfra && hasChallengeIndicator;
    const confidence = isChallenge ? 100 : 0;

    return {
      isChallenge,
      type: isChallenge ? type : "none",
      confidence,
      signals,
    };
  } catch (error: any) {
    return {
      isChallenge: false,
      type: "none",
      confidence: 0,
      signals: [`Error during detection: ${error.message}`],
    };
  }
}

/**
 * Quick check - just returns boolean
 *
 * @param hero - Hero instance
 * @returns True if challenge page detected
 */
export async function isChallengePage(hero: Hero): Promise<boolean> {
  const detection = await detectChallenge(hero);
  return detection.isChallenge;
}
```

## File: `src/cloudflare/handler.ts`
```typescript
import type Hero from "@ulixee/hero";
import { detectChallenge } from "./detector";
import type { ChallengeResolutionResult, ChallengeWaitOptions } from "./types";

/**
 * Wait for Cloudflare challenge to resolve
 *
 * Uses multiple detection strategies:
 * 1. URL redirect detection (page redirects after challenge)
 * 2. Signal polling (challenge-specific elements/text disappear)
 *
 * @param hero - Hero instance with challenge page loaded
 * @param options - Waiting options
 * @returns Resolution result with method and time waited
 *
 * @example
 * const result = await waitForChallengeResolution(hero, {
 *   maxWaitMs: 45000,
 *   pollIntervalMs: 500,
 *   verbose: true,
 *   initialUrl: 'https://example.com'
 * });
 *
 * if (result.resolved) {
 *   console.log(`Challenge resolved via ${result.method} in ${result.waitedMs}ms`);
 * }
 */
export async function waitForChallengeResolution(
  hero: Hero,
  options: ChallengeWaitOptions
): Promise<ChallengeResolutionResult> {
  const { maxWaitMs = 45000, pollIntervalMs = 500, verbose = false, initialUrl } = options;

  const startTime = Date.now();
  const log = (msg: string) => verbose && console.log(`   ${msg}`);

  while (Date.now() - startTime < maxWaitMs) {
    const elapsed = Date.now() - startTime;

    // =========================================================================
    // STRATEGY 1: Check for URL change (redirect after challenge)
    // =========================================================================
    try {
      const currentUrl = await hero.url;
      if (currentUrl !== initialUrl) {
        log(`✓ URL changed: ${initialUrl} → ${currentUrl}`);
        // Wait for the new page to fully load after redirect
        log(`  Waiting for new page to load...`);
        try {
          await hero.waitForLoad("DomContentLoaded", { timeoutMs: 30000 });
          log(`  DOMContentLoaded`);
        } catch {
          log(`  DOMContentLoaded timeout, continuing...`);
        }
        // Additional wait for JS to execute and render
        await hero.waitForPaintingStable().catch(() => {});
        log(`  Page stabilized`);
        return { resolved: true, method: "url_redirect", waitedMs: elapsed };
      }
    } catch {
      // URL check failed, continue with other strategies
    }

    // =========================================================================
    // STRATEGY 2: Check if challenge signals are gone
    // =========================================================================
    const detection = await detectChallenge(hero);

    if (!detection.isChallenge) {
      log(`✓ Challenge signals cleared (confidence dropped to ${detection.confidence})`);
      // Wait for page to fully load after challenge clears
      log(`  Waiting for page to load...`);
      try {
        await hero.waitForLoad("DomContentLoaded", { timeoutMs: 30000 });
        log(`  DOMContentLoaded`);
      } catch {
        log(`  DOMContentLoaded timeout, continuing...`);
      }
      await hero.waitForPaintingStable().catch(() => {});
      log(`  Page stabilized`);
      return { resolved: true, method: "signals_cleared", waitedMs: elapsed };
    }

    // Log progress
    log(
      `⏳ ${(elapsed / 1000).toFixed(1)}s - Still challenge (confidence: ${detection.confidence})`
    );

    // Wait before next poll
    await new Promise((resolve) => setTimeout(resolve, pollIntervalMs));
  }

  // Timeout reached
  return {
    resolved: false,
    method: "timeout",
    waitedMs: Date.now() - startTime,
  };
}

/**
 * Wait for a specific CSS selector to appear
 *
 * Useful when you know exactly what element should appear after challenge.
 *
 * @param hero - Hero instance
 * @param selector - CSS selector to wait for
 * @param maxWaitMs - Maximum time to wait
 * @param verbose - Enable logging
 * @returns Whether selector was found and time waited
 *
 * @example
 * const result = await waitForSelector(hero, '.content', 30000, true);
 * if (result.found) {
 *   console.log(`Content appeared after ${result.waitedMs}ms`);
 * }
 */
export async function waitForSelector(
  hero: Hero,
  selector: string,
  maxWaitMs: number,
  verbose: boolean = false
): Promise<{ found: boolean; waitedMs: number }> {
  const startTime = Date.now();
  const log = (msg: string) => verbose && console.log(`   ${msg}`);

  log(`Waiting for selector: "${selector}"`);

  while (Date.now() - startTime < maxWaitMs) {
    try {
      const element = await hero.document.querySelector(selector);
      if (element) {
        const elapsed = Date.now() - startTime;
        log(`✓ Selector found after ${(elapsed / 1000).toFixed(1)}s`);
        return { found: true, waitedMs: elapsed };
      }
    } catch {
      // Selector not found yet, continue
    }

    await new Promise((resolve) => setTimeout(resolve, 300));
  }

  log(`✗ Selector not found within timeout`);
  return { found: false, waitedMs: Date.now() - startTime };
}

/**
 * Handle Cloudflare challenge with automatic detection and waiting
 *
 * High-level function that combines detection and resolution.
 *
 * @param hero - Hero instance
 * @param options - Wait options (without initialUrl)
 * @returns Resolution result
 *
 * @example
 * await hero.goto('https://example.com');
 * const result = await handleChallenge(hero, { verbose: true });
 * if (result.resolved) {
 *   // Challenge passed, continue scraping
 * }
 */
export async function handleChallenge(
  hero: Hero,
  options: Omit<ChallengeWaitOptions, "initialUrl"> = {}
): Promise<ChallengeResolutionResult> {
  // Get current URL
  const initialUrl = await hero.url;

  // Detect challenge
  const detection = await detectChallenge(hero);

  if (!detection.isChallenge) {
    // No challenge, return immediately
    return { resolved: true, method: "signals_cleared", waitedMs: 0 };
  }

  // Challenge detected, wait for resolution
  return waitForChallengeResolution(hero, {
    ...options,
    initialUrl,
  });
}
```

## File: `src/cloudflare/types.ts`
```typescript
/**
 * Cloudflare challenge detection result
 */
export interface ChallengeDetection {
  /** Whether a challenge was detected */
  isChallenge: boolean;

  /** Type of challenge */
  type: "js_challenge" | "turnstile" | "captcha" | "blocked" | "none";

  /** Confidence level (0-100) */
  confidence: number;

  /** Detection signals found */
  signals: string[];
}

/**
 * Challenge resolution result
 */
export interface ChallengeResolutionResult {
  /** Whether the challenge was resolved */
  resolved: boolean;

  /** Method used to detect resolution */
  method: "url_redirect" | "signals_cleared" | "timeout";

  /** Time waited in milliseconds */
  waitedMs: number;
}

/**
 * Challenge waiting options
 */
export interface ChallengeWaitOptions {
  /** Maximum time to wait for resolution (default: 45000ms) */
  maxWaitMs?: number;

  /** How often to poll for resolution (default: 500ms) */
  pollIntervalMs?: number;

  /** Enable verbose logging */
  verbose?: boolean;

  /** Initial URL before challenge */
  initialUrl: string;
}
```

## File: `src/daemon/client.ts`
```typescript
/**
 * Daemon Client
 *
 * A client that connects to the daemon server via HTTP.
 * Used by CLI commands when a daemon is running.
 *
 * @example
 * const client = new DaemonClient({ port: 3847 });
 *
 * const result = await client.scrape({
 *   urls: ['https://example.com'],
 *   formats: ['markdown'],
 * });
 */

import http from "http";
import type { ScrapeOptions, ScrapeResult } from "../types";
import type { CrawlOptions, CrawlResult } from "../crawl-types";
import type { DaemonStatus } from "./server";
import { DEFAULT_DAEMON_PORT } from "./server";

/**
 * Daemon client configuration
 */
export interface DaemonClientOptions {
  /** Port the daemon is running on (default: 3847) */
  port?: number;
  /** Request timeout in milliseconds (default: 600000 = 10 minutes) */
  timeoutMs?: number;
}

/**
 * Daemon Client
 */
export class DaemonClient {
  private options: Required<DaemonClientOptions>;

  constructor(options: DaemonClientOptions = {}) {
    this.options = {
      port: options.port ?? DEFAULT_DAEMON_PORT,
      timeoutMs: options.timeoutMs ?? 600000, // 10 minutes default
    };
  }

  /**
   * Scrape URLs via daemon
   */
  async scrape(options: Omit<ScrapeOptions, "connectionToCore">): Promise<ScrapeResult> {
    return this.request<ScrapeResult>({
      action: "scrape",
      options,
    });
  }

  /**
   * Crawl URL via daemon
   */
  async crawl(options: Omit<CrawlOptions, "connectionToCore">): Promise<CrawlResult> {
    return this.request<CrawlResult>({
      action: "crawl",
      options,
    });
  }

  /**
   * Get daemon status
   */
  async status(): Promise<DaemonStatus> {
    return this.request<DaemonStatus>({
      action: "status",
    });
  }

  /**
   * Request daemon shutdown
   */
  async shutdown(): Promise<void> {
    await this.request<{ message: string }>({
      action: "shutdown",
    });
  }

  /**
   * Check if daemon is reachable
   */
  async isRunning(): Promise<boolean> {
    try {
      await this.status();
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Make HTTP request to daemon
   */
  private request<T>(body: object): Promise<T> {
    return new Promise((resolve, reject) => {
      const data = JSON.stringify(body);

      const req = http.request(
        {
          hostname: "127.0.0.1",
          port: this.options.port,
          path: "/",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(data),
          },
          timeout: this.options.timeoutMs,
        },
        (res) => {
          let responseBody = "";

          res.on("data", (chunk) => {
            responseBody += chunk;
          });

          res.on("end", () => {
            try {
              const response = JSON.parse(responseBody);

              if (response.success) {
                resolve(response.data);
              } else {
                reject(new Error(response.error || "Unknown daemon error"));
              }
            } catch (error) {
              reject(new Error(`Failed to parse daemon response: ${responseBody}`));
            }
          });
        }
      );

      req.on("error", (error: NodeJS.ErrnoException) => {
        if (error.code === "ECONNREFUSED") {
          reject(new Error(`Cannot connect to daemon on port ${this.options.port}. Is it running?`));
        } else {
          reject(error);
        }
      });

      req.on("timeout", () => {
        req.destroy();
        reject(new Error(`Request to daemon timed out after ${this.options.timeoutMs}ms`));
      });

      req.write(data);
      req.end();
    });
  }
}

/**
 * Check if daemon is running on the specified port
 */
export async function isDaemonRunning(port: number = DEFAULT_DAEMON_PORT): Promise<boolean> {
  const client = new DaemonClient({ port, timeoutMs: 5000 });
  return client.isRunning();
}
```

## File: `src/daemon/index.ts`
```typescript
/**
 * Daemon module exports
 */

export { DaemonServer, DEFAULT_DAEMON_PORT, getDaemonInfo, getPidFilePath } from "./server";
export type { DaemonServerOptions, DaemonStatus } from "./server";

export { DaemonClient, isDaemonRunning } from "./client";
export type { DaemonClientOptions } from "./client";
```

## File: `src/daemon/server.ts`
```typescript
/**
 * Daemon Server
 *
 * An HTTP server that wraps ReaderClient, allowing multiple CLI
 * commands to share a single browser pool for efficient scraping.
 *
 * @example
 * // Start daemon
 * const daemon = new DaemonServer({ port: 3847, poolSize: 5 });
 * await daemon.start();
 *
 * // Stop daemon
 * await daemon.stop();
 */

import http from "http";
import { ReaderClient, type ReaderClientOptions } from "../client";
import type { ScrapeOptions, ScrapeResult } from "../types";
import type { CrawlOptions, CrawlResult } from "../crawl-types";
import { createLogger } from "../utils/logger";

const logger = createLogger("daemon");

export const DEFAULT_DAEMON_PORT = 3847;
const PID_FILE_NAME = ".reader-daemon.pid";

/**
 * Daemon server configuration
 */
export interface DaemonServerOptions {
  /** Port to listen on (default: 3847) */
  port?: number;
  /** Browser pool size (default: 5) */
  poolSize?: number;
  /** Enable verbose logging (default: false) */
  verbose?: boolean;
  /** Show Chrome browser windows (default: false) */
  showChrome?: boolean;
}

/**
 * Request body types
 */
interface ScrapeRequest {
  action: "scrape";
  options: Omit<ScrapeOptions, "connectionToCore">;
}

interface CrawlRequest {
  action: "crawl";
  options: Omit<CrawlOptions, "connectionToCore">;
}

interface StatusRequest {
  action: "status";
}

interface ShutdownRequest {
  action: "shutdown";
}

type DaemonRequest = ScrapeRequest | CrawlRequest | StatusRequest | ShutdownRequest;

/**
 * Response types
 */
interface SuccessResponse<T> {
  success: true;
  data: T;
}

interface ErrorResponse {
  success: false;
  error: string;
}

type DaemonResponse<T> = SuccessResponse<T> | ErrorResponse;

/**
 * Status response data
 */
export interface DaemonStatus {
  running: true;
  port: number;
  poolSize: number;
  uptime: number;
  pid: number;
}

/**
 * Daemon Server
 */
export class DaemonServer {
  private server: http.Server | null = null;
  private client: ReaderClient | null = null;
  private options: Required<DaemonServerOptions>;
  private startTime: number = 0;

  constructor(options: DaemonServerOptions = {}) {
    this.options = {
      port: options.port ?? DEFAULT_DAEMON_PORT,
      poolSize: options.poolSize ?? 5,
      verbose: options.verbose ?? false,
      showChrome: options.showChrome ?? false,
    };
  }

  /**
   * Start the daemon server
   */
  async start(): Promise<void> {
    if (this.server) {
      throw new Error("Daemon is already running");
    }

    // Initialize ReaderClient
    const clientOptions: ReaderClientOptions = {
      verbose: this.options.verbose,
      showChrome: this.options.showChrome,
      browserPool: {
        size: this.options.poolSize,
      },
    };

    this.client = new ReaderClient(clientOptions);
    await this.client.start();

    // Create HTTP server
    this.server = http.createServer(this.handleRequest.bind(this));

    // Start listening
    await new Promise<void>((resolve, reject) => {
      this.server!.listen(this.options.port, () => {
        this.startTime = Date.now();
        if (this.options.verbose) {
          logger.info(`Daemon started on port ${this.options.port} with pool size ${this.options.poolSize}`);
        }
        resolve();
      });

      this.server!.on("error", (error: NodeJS.ErrnoException) => {
        if (error.code === "EADDRINUSE") {
          reject(new Error(`Port ${this.options.port} is already in use. Is another daemon running?`));
        } else {
          reject(error);
        }
      });
    });

    // Write PID file
    await this.writePidFile();
  }

  /**
   * Stop the daemon server
   */
  async stop(): Promise<void> {
    if (this.server) {
      await new Promise<void>((resolve) => {
        this.server!.close(() => resolve());
      });
      this.server = null;
    }

    if (this.client) {
      await this.client.close();
      this.client = null;
    }

    // Remove PID file
    await this.removePidFile();

    if (this.options.verbose) {
      logger.info("Daemon stopped");
    }
  }

  /**
   * Get the port the daemon is running on
   */
  getPort(): number {
    return this.options.port;
  }

  /**
   * Handle incoming HTTP requests
   */
  private async handleRequest(req: http.IncomingMessage, res: http.ServerResponse): Promise<void> {
    // Only accept POST requests to /
    if (req.method !== "POST" || req.url !== "/") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ success: false, error: "Not found" }));
      return;
    }

    // Parse request body
    let body = "";
    for await (const chunk of req) {
      body += chunk;
    }

    let request: DaemonRequest;
    try {
      request = JSON.parse(body);
    } catch {
      this.sendResponse(res, 400, { success: false, error: "Invalid JSON" });
      return;
    }

    // Handle request
    try {
      switch (request.action) {
        case "scrape":
          await this.handleScrape(res, request.options);
          break;
        case "crawl":
          await this.handleCrawl(res, request.options);
          break;
        case "status":
          this.handleStatus(res);
          break;
        case "shutdown":
          await this.handleShutdown(res);
          break;
        default:
          this.sendResponse(res, 400, { success: false, error: "Unknown action" });
      }
    } catch (error: any) {
      this.sendResponse(res, 500, { success: false, error: error.message });
    }
  }

  /**
   * Handle scrape request
   */
  private async handleScrape(
    res: http.ServerResponse,
    options: Omit<ScrapeOptions, "connectionToCore">
  ): Promise<void> {
    if (!this.client) {
      this.sendResponse(res, 500, { success: false, error: "Client not initialized" });
      return;
    }

    const result = await this.client.scrape(options);
    this.sendResponse<ScrapeResult>(res, 200, { success: true, data: result });
  }

  /**
   * Handle crawl request
   */
  private async handleCrawl(
    res: http.ServerResponse,
    options: Omit<CrawlOptions, "connectionToCore">
  ): Promise<void> {
    if (!this.client) {
      this.sendResponse(res, 500, { success: false, error: "Client not initialized" });
      return;
    }

    const result = await this.client.crawl(options);
    this.sendResponse<CrawlResult>(res, 200, { success: true, data: result });
  }

  /**
   * Handle status request
   */
  private handleStatus(res: http.ServerResponse): void {
    const status: DaemonStatus = {
      running: true,
      port: this.options.port,
      poolSize: this.options.poolSize,
      uptime: Date.now() - this.startTime,
      pid: process.pid,
    };
    this.sendResponse<DaemonStatus>(res, 200, { success: true, data: status });
  }

  /**
   * Handle shutdown request
   */
  private async handleShutdown(res: http.ServerResponse): Promise<void> {
    this.sendResponse(res, 200, { success: true, data: { message: "Shutting down" } });

    // Delay shutdown to allow response to be sent
    setTimeout(() => {
      this.stop().then(() => process.exit(0));
    }, 100);
  }

  /**
   * Send JSON response
   */
  private sendResponse<T>(res: http.ServerResponse, statusCode: number, data: DaemonResponse<T>): void {
    res.writeHead(statusCode, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data));
  }

  /**
   * Write PID file
   */
  private async writePidFile(): Promise<void> {
    const fs = await import("fs/promises");
    const path = await import("path");
    const os = await import("os");

    const pidFile = path.join(os.tmpdir(), PID_FILE_NAME);
    const data = JSON.stringify({
      pid: process.pid,
      port: this.options.port,
      startedAt: new Date().toISOString(),
    });

    await fs.writeFile(pidFile, data);
  }

  /**
   * Remove PID file
   */
  private async removePidFile(): Promise<void> {
    const fs = await import("fs/promises");
    const path = await import("path");
    const os = await import("os");

    const pidFile = path.join(os.tmpdir(), PID_FILE_NAME);
    try {
      await fs.unlink(pidFile);
    } catch {
      // Ignore errors
    }
  }
}

/**
 * Get path to PID file
 */
export async function getPidFilePath(): Promise<string> {
  const path = await import("path");
  const os = await import("os");
  return path.join(os.tmpdir(), PID_FILE_NAME);
}

/**
 * Check if daemon is running by reading PID file
 */
export async function getDaemonInfo(): Promise<{ pid: number; port: number; startedAt: string } | null> {
  const fs = await import("fs/promises");
  const pidFile = await getPidFilePath();

  try {
    const data = await fs.readFile(pidFile, "utf-8");
    const info = JSON.parse(data);

    // Check if process is still running
    try {
      process.kill(info.pid, 0); // Signal 0 tests if process exists
      return info;
    } catch {
      // Process not running, clean up stale PID file
      await fs.unlink(pidFile).catch(() => {});
      return null;
    }
  } catch {
    return null;
  }
}
```

## File: `src/engines/errors.ts`
```typescript
/**
 * Engine-specific error classes
 *
 * These errors are used internally by engines and the orchestrator
 * to signal specific failure conditions and control flow.
 */

import type { EngineName } from "./types.js";

/**
 * Base error for all engine errors
 */
export class EngineError extends Error {
  readonly engine: EngineName;
  readonly retryable: boolean;

  constructor(engine: EngineName, message: string, options?: { cause?: Error; retryable?: boolean }) {
    super(`[${engine}] ${message}`);
    this.name = "EngineError";
    this.engine = engine;
    this.retryable = options?.retryable ?? true;
    this.cause = options?.cause;

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }
  }
}

/**
 * Challenge detected (Cloudflare, CAPTCHA, etc.)
 * Signals orchestrator to try next engine
 */
export class ChallengeDetectedError extends EngineError {
  readonly challengeType: string;

  constructor(engine: EngineName, challengeType?: string) {
    super(engine, `Challenge detected: ${challengeType || "unknown"}`, { retryable: true });
    this.name = "ChallengeDetectedError";
    this.challengeType = challengeType || "unknown";
  }
}

/**
 * Content too short or empty
 * May indicate blocked page or JS-required content
 */
export class InsufficientContentError extends EngineError {
  readonly contentLength: number;
  readonly threshold: number;

  constructor(engine: EngineName, contentLength: number, threshold: number = 100) {
    super(engine, `Insufficient content: ${contentLength} chars (threshold: ${threshold})`, { retryable: true });
    this.name = "InsufficientContentError";
    this.contentLength = contentLength;
    this.threshold = threshold;
  }
}

/**
 * HTTP error status (4xx, 5xx)
 */
export class HttpError extends EngineError {
  readonly statusCode: number;

  constructor(engine: EngineName, statusCode: number, statusText?: string) {
    const retryable = statusCode >= 500 || statusCode === 429;
    super(engine, `HTTP ${statusCode}${statusText ? `: ${statusText}` : ""}`, { retryable });
    this.name = "HttpError";
    this.statusCode = statusCode;
  }
}

/**
 * Engine timeout
 */
export class EngineTimeoutError extends EngineError {
  readonly timeoutMs: number;

  constructor(engine: EngineName, timeoutMs: number) {
    super(engine, `Timeout after ${timeoutMs}ms`, { retryable: true });
    this.name = "EngineTimeoutError";
    this.timeoutMs = timeoutMs;
  }
}

/**
 * Engine not available (not configured, missing dependency)
 */
export class EngineUnavailableError extends EngineError {
  constructor(engine: EngineName, reason?: string) {
    super(engine, reason || "Engine not available", { retryable: false });
    this.name = "EngineUnavailableError";
  }
}

/**
 * Signal to orchestrator to move to next engine
 * Not a real error - used for control flow
 */
export class NextEngineSignal extends Error {
  readonly fromEngine: EngineName;
  readonly reason: string;

  constructor(fromEngine: EngineName, reason: string) {
    super(`Next engine signal from ${fromEngine}: ${reason}`);
    this.name = "NextEngineSignal";
    this.fromEngine = fromEngine;
    this.reason = reason;
  }
}

/**
 * All engines exhausted without success
 */
export class AllEnginesFailedError extends Error {
  readonly attemptedEngines: EngineName[];
  readonly errors: Map<EngineName, Error>;

  constructor(attemptedEngines: EngineName[], errors: Map<EngineName, Error>) {
    const summary = attemptedEngines
      .map((e) => `${e}: ${errors.get(e)?.message || "unknown"}`)
      .join("; ");
    super(`All engines failed: ${summary}`);
    this.name = "AllEnginesFailedError";
    this.attemptedEngines = attemptedEngines;
    this.errors = errors;
  }
}
```

## File: `src/engines/index.ts`
```typescript
/**
 * Multi-Engine Scraping System
 *
 * Provides a cascading engine architecture for web scraping:
 *   1. http - Native fetch, fastest, works for static sites
 *   2. tlsclient - TLS fingerprinting via got-scraping
 *   3. hero - Full browser with JavaScript execution
 *
 * The orchestrator manages fallback between engines automatically.
 *
 * @example
 * import { createOrchestrator } from './engines';
 *
 * const orchestrator = createOrchestrator({ verbose: true });
 * const result = await orchestrator.scrape({
 *   url: 'https://example.com',
 *   options: { pool }
 * });
 * console.log(`Scraped with ${result.engine} in ${result.duration}ms`);
 */

// Types
export type {
  EngineName,
  Engine,
  EngineConfig,
  EngineFeatures,
  EngineMeta,
  EngineResult,
} from "./types.js";

export { ENGINE_CONFIGS, DEFAULT_ENGINE_ORDER } from "./types.js";

// Errors
export {
  EngineError,
  ChallengeDetectedError,
  InsufficientContentError,
  HttpError,
  EngineTimeoutError,
  EngineUnavailableError,
  NextEngineSignal,
  AllEnginesFailedError,
} from "./errors.js";

// Individual engines
export { httpEngine, HttpEngine } from "./http/index.js";
export { tlsClientEngine, TlsClientEngine } from "./tlsclient/index.js";
export { heroEngine, HeroEngine } from "./hero/index.js";

// Orchestrator
export {
  EngineOrchestrator,
  createOrchestrator,
  orchestratedScrape,
  type OrchestratorOptions,
  type OrchestratorResult,
} from "./orchestrator.js";
```

## File: `src/engines/orchestrator.ts`
```typescript
/**
 * Engine Orchestrator
 *
 * Manages multi-engine scraping with waterfall fallback pattern.
 * Tries engines in order of speed/efficiency:
 *   1. http - Native fetch, fastest, works for static sites
 *   2. tlsclient - TLS fingerprinting for better compatibility
 *   3. hero - Full browser, handles Cloudflare and JS-heavy sites
 *
 * Features:
 * - Staggered timeouts (each engine gets its configured time before fallback)
 * - Parallel racing option (start next engine while previous still running)
 * - Graceful fallback on challenge detection
 * - Detailed error tracking per engine
 */

import type { Engine, EngineName, EngineMeta, EngineResult } from "./types.js";
import { DEFAULT_ENGINE_ORDER } from "./types.js";
import {
  EngineError,
  ChallengeDetectedError,
  InsufficientContentError,
  HttpError,
  EngineTimeoutError,
  EngineUnavailableError,
  AllEnginesFailedError,
} from "./errors.js";
import { httpEngine } from "./http/index.js";
import { tlsClientEngine } from "./tlsclient/index.js";
import { heroEngine } from "./hero/index.js";
import type { Logger } from "../utils/logger.js";

/**
 * Orchestrator options
 */
export interface OrchestratorOptions {
  /** Engines to use (in order). Default: ['http', 'tlsclient', 'hero'] */
  engines?: EngineName[];
  /** Skip specific engines */
  skipEngines?: EngineName[];
  /** Force a specific engine (skips others) */
  forceEngine?: EngineName;
  /** Enable parallel racing (start next engine while previous still running) */
  parallelRacing?: boolean;
  /** Logger instance */
  logger?: Logger;
  /** Verbose logging */
  verbose?: boolean;
}

/**
 * Engine registry
 */
const ENGINE_REGISTRY: Record<EngineName, Engine> = {
  http: httpEngine,
  tlsclient: tlsClientEngine,
  hero: heroEngine,
};

/**
 * Orchestrator result with engine metadata
 */
export interface OrchestratorResult extends EngineResult {
  /** Engines that were attempted */
  attemptedEngines: EngineName[];
  /** Errors from failed engines */
  engineErrors: Map<EngineName, Error>;
}

/**
 * Engine Orchestrator
 *
 * Coordinates multiple scraping engines with fallback logic.
 *
 * @example
 * const orchestrator = new EngineOrchestrator({ verbose: true });
 * const result = await orchestrator.scrape({
 *   url: 'https://example.com',
 *   options: { timeoutMs: 30000 }
 * });
 * console.log(`Scraped with ${result.engine} engine`);
 */
export class EngineOrchestrator {
  private options: OrchestratorOptions;
  private engines: Engine[];
  private engineOrder: EngineName[];

  constructor(options: OrchestratorOptions = {}) {
    this.options = options;
    this.engineOrder = this.resolveEngineOrder();
    this.engines = this.engineOrder
      .map((name) => ENGINE_REGISTRY[name])
      .filter((engine) => engine.isAvailable());
  }

  /**
   * Resolve the engine order based on options
   */
  private resolveEngineOrder(): EngineName[] {
    // If force engine is set, use only that
    if (this.options.forceEngine) {
      return [this.options.forceEngine];
    }

    // Start with configured order or default
    let order = this.options.engines || [...DEFAULT_ENGINE_ORDER];

    // Remove skipped engines
    if (this.options.skipEngines) {
      order = order.filter((e) => !this.options.skipEngines!.includes(e));
    }

    return order;
  }

  /**
   * Get available engines
   */
  getAvailableEngines(): EngineName[] {
    return this.engines.map((e) => e.config.name);
  }

  /**
   * Scrape a URL using the engine cascade
   *
   * @param meta - Engine metadata (url, options, logger, abortSignal)
   * @returns Scrape result with engine metadata
   * @throws AllEnginesFailedError if all engines fail
   */
  async scrape(meta: EngineMeta): Promise<OrchestratorResult> {
    const attemptedEngines: EngineName[] = [];
    const engineErrors = new Map<EngineName, Error>();
    const logger = meta.logger || this.options.logger;
    const verbose = this.options.verbose || meta.options.verbose;

    if (this.engines.length === 0) {
      throw new AllEnginesFailedError([], engineErrors);
    }

    const log = (msg: string) => {
      if (verbose) {
        logger?.info(msg);
      } else {
        logger?.debug(msg);
      }
    };

    log(`[orchestrator] Starting scrape of ${meta.url} with engines: ${this.engineOrder.join(" → ")}`);

    // Try each engine in order
    for (const engine of this.engines) {
      const engineName = engine.config.name;
      attemptedEngines.push(engineName);

      try {
        log(`[orchestrator] Trying ${engineName} engine...`);

        // Create abort controller for this engine's timeout
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), engine.config.maxTimeout);

        // Link external abort signal
        if (meta.abortSignal) {
          meta.abortSignal.addEventListener("abort", () => controller.abort(), { once: true });
        }

        try {
          const result = await engine.scrape({
            ...meta,
            abortSignal: controller.signal,
          });

          clearTimeout(timeoutId);

          log(`[orchestrator] ✓ ${engineName} succeeded in ${result.duration}ms`);

          return {
            ...result,
            attemptedEngines,
            engineErrors,
          };
        } finally {
          clearTimeout(timeoutId);
        }
      } catch (error: unknown) {
        const err = error instanceof Error ? error : new Error(String(error));
        engineErrors.set(engineName, err);

        // Log the error with appropriate detail
        if (error instanceof ChallengeDetectedError) {
          log(`[orchestrator] ${engineName} detected challenge: ${error.challengeType}`);
        } else if (error instanceof InsufficientContentError) {
          log(`[orchestrator] ${engineName} insufficient content: ${error.contentLength} chars`);
        } else if (error instanceof HttpError) {
          log(`[orchestrator] ${engineName} HTTP error: ${error.statusCode}`);
        } else if (error instanceof EngineTimeoutError) {
          log(`[orchestrator] ${engineName} timed out after ${error.timeoutMs}ms`);
        } else if (error instanceof EngineUnavailableError) {
          log(`[orchestrator] ${engineName} unavailable: ${err.message}`);
        } else {
          log(`[orchestrator] ${engineName} failed: ${err.message}`);
        }

        // Check if we should continue to next engine
        if (!this.shouldRetry(error)) {
          log(`[orchestrator] Non-retryable error, stopping cascade`);
          break;
        }

        // Continue to next engine
        log(`[orchestrator] Falling back to next engine...`);
      }
    }

    // All engines failed
    log(`[orchestrator] All engines failed for ${meta.url}`);
    throw new AllEnginesFailedError(attemptedEngines, engineErrors);
  }

  /**
   * Determine if we should retry with next engine
   */
  private shouldRetry(error: unknown): boolean {
    // Always retry on these errors
    if (
      error instanceof ChallengeDetectedError ||
      error instanceof InsufficientContentError ||
      error instanceof EngineTimeoutError
    ) {
      return true;
    }

    // Retry on HTTP errors that might be bot detection or server issues
    // 403 Forbidden - often bot detection, try better fingerprinting
    // 404 Not Found - might be JS-rendered SPA that needs browser
    // 429 Too Many Requests - rate limited, try different engine
    // 5xx Server errors - might be blocking, try again
    if (error instanceof HttpError) {
      return error.statusCode === 403 || error.statusCode === 404 || error.statusCode === 429 || error.statusCode >= 500;
    }

    // Don't retry on unavailable (won't help)
    if (error instanceof EngineUnavailableError) {
      return true; // Skip to next engine
    }

    // Generic engine errors - check retryable flag
    if (error instanceof EngineError) {
      return error.retryable;
    }

    // Unknown errors - retry
    return true;
  }
}

/**
 * Create an orchestrator with default settings
 */
export function createOrchestrator(options: OrchestratorOptions = {}): EngineOrchestrator {
  return new EngineOrchestrator(options);
}

/**
 * Convenience function to scrape with orchestrator
 *
 * @example
 * const result = await orchestratedScrape({
 *   url: 'https://example.com',
 *   options: { pool }
 * });
 */
export async function orchestratedScrape(
  meta: EngineMeta,
  options: OrchestratorOptions = {}
): Promise<OrchestratorResult> {
  const orchestrator = new EngineOrchestrator(options);
  return orchestrator.scrape(meta);
}
```

## File: `src/engines/types.ts`
```typescript
/**
 * Engine types for multi-engine scraping architecture
 *
 * Engine stack (in order of preference):
 * 1. http - Native fetch, fastest, no browser
 * 2. tlsclient - TLS fingerprinting via got-scraping
 * 3. hero - Full browser with JavaScript execution
 */

import type { ScrapeOptions } from "../types.js";
import type { Logger } from "../utils/logger.js";

/**
 * Available engine names
 */
export type EngineName = "http" | "tlsclient" | "hero";

/**
 * Result returned by an engine after scraping
 */
export interface EngineResult {
  /** Raw HTML content */
  html: string;
  /** Final URL after redirects */
  url: string;
  /** HTTP status code */
  statusCode: number;
  /** Content-Type header */
  contentType?: string;
  /** Response headers */
  headers?: Record<string, string>;

  /** Engine that produced this result */
  engine: EngineName;
  /** Time taken in milliseconds */
  duration: number;
}

/**
 * Metadata passed to engine scrape method
 */
export interface EngineMeta {
  /** URL to scrape */
  url: string;
  /** Scrape options */
  options: ScrapeOptions;
  /** Logger instance */
  logger?: Logger;
  /** Abort signal for cancellation */
  abortSignal?: AbortSignal;
}

/**
 * Engine configuration
 */
export interface EngineConfig {
  /** Engine name */
  name: EngineName;
  /** Timeout before starting next engine (ms) */
  timeout: number;
  /** Absolute max time before killing (ms) */
  maxTimeout: number;
  /** Quality score - higher means preferred (for sorting) */
  quality: number;
  /** Engine capabilities */
  features: EngineFeatures;
}

/**
 * Engine feature flags
 */
export interface EngineFeatures {
  /** Can execute JavaScript */
  javascript: boolean;
  /** Can handle Cloudflare challenges */
  cloudflare: boolean;
  /** Matches browser TLS fingerprint */
  tlsFingerprint: boolean;
  /** Supports waitFor selector */
  waitFor: boolean;
  /** Can take screenshots */
  screenshots: boolean;
}

/**
 * Engine interface - all engines must implement this
 */
export interface Engine {
  /** Engine configuration */
  readonly config: EngineConfig;

  /**
   * Scrape a URL
   * @param meta - Scrape metadata (url, options, logger, abortSignal)
   * @returns Engine result with HTML and metadata
   * @throws EngineError on failure
   */
  scrape(meta: EngineMeta): Promise<EngineResult>;

  /**
   * Check if engine is available and configured
   * @returns true if engine can be used
   */
  isAvailable(): boolean;
}

/**
 * Default engine configurations
 */
export const ENGINE_CONFIGS: Record<EngineName, EngineConfig> = {
  http: {
    name: "http",
    timeout: 3000,
    maxTimeout: 10000,
    quality: 100,
    features: {
      javascript: false,
      cloudflare: false,
      tlsFingerprint: false,
      waitFor: false,
      screenshots: false,
    },
  },
  tlsclient: {
    name: "tlsclient",
    timeout: 5000,
    maxTimeout: 15000,
    quality: 80,
    features: {
      javascript: false,
      cloudflare: false,
      tlsFingerprint: true,
      waitFor: false,
      screenshots: false,
    },
  },
  hero: {
    name: "hero",
    timeout: 30000,
    maxTimeout: 60000,
    quality: 50,
    features: {
      javascript: true,
      cloudflare: true,
      tlsFingerprint: true,
      waitFor: true,
      screenshots: true,
    },
  },
};

/**
 * Default engine order (by quality, highest first)
 */
export const DEFAULT_ENGINE_ORDER: EngineName[] = ["http", "tlsclient", "hero"];
```

## File: `src/engines/hero/index.ts`
```typescript
/**
 * Hero Engine - Full browser with JavaScript execution
 *
 * Uses Hero browser automation with browser pool.
 * Handles JavaScript-heavy sites and challenge pages.
 * Most capable but slowest engine - used as fallback.
 */

import Hero from "@ulixee/hero";
import type { Engine, EngineConfig, EngineMeta, EngineResult } from "../types.js";
import {
  EngineError,
  ChallengeDetectedError,
  InsufficientContentError,
  EngineTimeoutError,
  EngineUnavailableError,
} from "../errors.js";
import { ENGINE_CONFIGS } from "../types.js";
import { detectChallenge } from "../../cloudflare/detector.js";
import { waitForChallengeResolution } from "../../cloudflare/handler.js";
import type { IBrowserPool } from "../../browser/types.js";

/**
 * Minimum content length threshold
 */
const MIN_CONTENT_LENGTH = 100;

/**
 * Hero Engine implementation using browser pool
 */
export class HeroEngine implements Engine {
  readonly config: EngineConfig = ENGINE_CONFIGS.hero;

  async scrape(meta: EngineMeta): Promise<EngineResult> {
    const startTime = Date.now();
    const { url, options, logger, abortSignal } = meta;

    // Get browser pool from options
    const pool = options.pool as IBrowserPool | undefined;
    if (!pool) {
      throw new EngineUnavailableError("hero", "Browser pool not available");
    }

    // Check for abort before starting
    if (abortSignal?.aborted) {
      throw new EngineTimeoutError("hero", 0);
    }

    logger?.debug(`[hero] Starting browser scrape of ${url}`);

    try {
      const result = await pool.withBrowser(async (hero: Hero) => {
        // Set up abort handling
        let aborted = false;
        if (abortSignal) {
          abortSignal.addEventListener("abort", () => {
            aborted = true;
          }, { once: true });
        }

        // Navigate to URL
        const timeoutMs = options.timeoutMs || this.config.maxTimeout;
        await hero.goto(url, { timeoutMs });

        if (aborted) {
          throw new EngineTimeoutError("hero", Date.now() - startTime);
        }

        // Wait for initial page load
        try {
          await hero.waitForLoad("DomContentLoaded", { timeoutMs });
        } catch {
          // Timeout is OK, continue anyway
        }
        await hero.waitForPaintingStable();

        if (aborted) {
          throw new EngineTimeoutError("hero", Date.now() - startTime);
        }

        // Detect and handle Cloudflare challenge
        const initialUrl = await hero.url;
        const detection = await detectChallenge(hero);

        if (detection.isChallenge) {
          logger?.debug(`[hero] Challenge detected: ${detection.type}`);

          // If it's a blocked challenge, we can't proceed
          if (detection.type === "blocked") {
            throw new ChallengeDetectedError("hero", "blocked");
          }

          // Wait for resolution
          const resolution = await waitForChallengeResolution(hero, {
            maxWaitMs: 45000,
            pollIntervalMs: 500,
            verbose: options.verbose,
            initialUrl,
          });

          if (!resolution.resolved) {
            throw new ChallengeDetectedError("hero", `unresolved: ${detection.type}`);
          }

          logger?.debug(`[hero] Challenge resolved via ${resolution.method} in ${resolution.waitedMs}ms`);
        }

        if (aborted) {
          throw new EngineTimeoutError("hero", Date.now() - startTime);
        }

        // Wait for final page to stabilize (handles Cloudflare silent redirects)
        await this.waitForFinalPage(hero, url, logger);

        if (aborted) {
          throw new EngineTimeoutError("hero", Date.now() - startTime);
        }

        // Wait for selector if specified
        if (options.waitForSelector) {
          try {
            await hero.waitForElement(hero.document.querySelector(options.waitForSelector), {
              timeoutMs,
            });
          } catch {
            logger?.debug(`[hero] Selector not found: ${options.waitForSelector}`);
          }
        }

        // Extract content
        const html = await hero.document.documentElement.outerHTML;
        const finalUrl = await hero.url;

        // Validate content length
        const textContent = this.extractText(html);
        if (textContent.length < MIN_CONTENT_LENGTH) {
          logger?.debug(`[hero] Insufficient content: ${textContent.length} chars`);
          throw new InsufficientContentError("hero", textContent.length, MIN_CONTENT_LENGTH);
        }

        const duration = Date.now() - startTime;
        logger?.debug(`[hero] Success: ${html.length} chars in ${duration}ms`);

        return {
          html,
          url: finalUrl,
          statusCode: 200, // Hero doesn't expose status code directly
          engine: "hero" as const,
          duration,
        };
      });

      return result;
    } catch (error: unknown) {
      // Re-throw our own errors
      if (
        error instanceof ChallengeDetectedError ||
        error instanceof InsufficientContentError ||
        error instanceof EngineTimeoutError ||
        error instanceof EngineUnavailableError
      ) {
        throw error;
      }

      // Handle specific error types
      if (error instanceof Error) {
        // Timeout errors
        if (error.name === "TimeoutError" || error.message.includes("timeout")) {
          throw new EngineTimeoutError("hero", this.config.maxTimeout);
        }

        // Navigation errors
        if (error.message.includes("Navigation") || error.message.includes("ERR_")) {
          throw new EngineError("hero", `Navigation failed: ${error.message}`, { cause: error });
        }

        // Wrap other errors
        throw new EngineError("hero", error.message, { cause: error });
      }

      throw new EngineError("hero", String(error));
    }
  }

  /**
   * Wait for the final page to load after any Cloudflare redirects
   */
  private async waitForFinalPage(hero: Hero, originalUrl: string, logger?: EngineMeta["logger"]): Promise<void> {
    const maxWaitMs = 15000;
    const startTime = Date.now();

    // Wait for any pending navigation to complete
    try {
      await hero.waitForLoad("AllContentLoaded", { timeoutMs: maxWaitMs });
    } catch {
      // Timeout is OK
    }

    // Check if URL changed (Cloudflare redirect)
    let currentUrl = await hero.url;
    const normalizeUrl = (url: string) => url.replace(/\/+$/, "");
    const urlChanged = normalizeUrl(currentUrl) !== normalizeUrl(originalUrl);

    if (urlChanged || currentUrl.includes("__cf_chl")) {
      logger?.debug(`[hero] Cloudflare redirect detected: ${originalUrl} → ${currentUrl}`);

      // Wait for the redirect to complete and new page to load
      let lastUrl = currentUrl;
      let stableCount = 0;

      while (Date.now() - startTime < maxWaitMs) {
        await new Promise((resolve) => setTimeout(resolve, 500));

        try {
          currentUrl = await hero.url;

          // URL is stable if it hasn't changed for 2 consecutive checks
          if (currentUrl === lastUrl) {
            stableCount++;
            if (stableCount >= 2) {
              break;
            }
          } else {
            stableCount = 0;
            lastUrl = currentUrl;
            logger?.debug(`[hero] URL changed to: ${currentUrl}`);
          }
        } catch {
          // Error getting URL, continue waiting
        }
      }

      // Final wait for page content to render
      try {
        await hero.waitForLoad("AllContentLoaded", { timeoutMs: 10000 });
      } catch {
        // Timeout OK
      }
    }

    // Final stabilization
    await hero.waitForPaintingStable();

    // Buffer for JS execution and dynamic content loading
    await new Promise((resolve) => setTimeout(resolve, 2000));
  }

  /**
   * Extract visible text from HTML
   */
  private extractText(html: string): string {
    return html
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  isAvailable(): boolean {
    // Hero is always available if we can import it
    // Actual pool availability is checked in scrape()
    return true;
  }
}

/**
 * Singleton instance
 */
export const heroEngine = new HeroEngine();
```

## File: `src/engines/http/index.ts`
```typescript
/**
 * HTTP Engine - Native fetch
 *
 * Fastest engine, no browser overhead.
 * Works for ~60-70% of static sites.
 * Falls back to tlsclient/hero when blocked or challenged.
 */

import type { Engine, EngineConfig, EngineMeta, EngineResult } from "../types.js";
import {
  EngineError,
  ChallengeDetectedError,
  InsufficientContentError,
  HttpError,
  EngineTimeoutError,
} from "../errors.js";
import { ENGINE_CONFIGS } from "../types.js";

/**
 * Browser-like headers for fetch requests
 */
const DEFAULT_HEADERS: Record<string, string> = {
  "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.9",
  "Accept-Encoding": "gzip, deflate, br",
  "Cache-Control": "no-cache",
  Pragma: "no-cache",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
};

/**
 * Challenge indicators in HTML content
 * These patterns suggest the page requires JS execution or is blocked
 */
const CHALLENGE_PATTERNS = [
  // Cloudflare
  "cf-browser-verification",
  "cf_chl_opt",
  "challenge-platform",
  "cf-spinner",
  "Just a moment",
  "Checking your browser",
  "checking if the site connection is secure",
  "Enable JavaScript and cookies",
  "Attention Required",
  "_cf_chl_tk",
  "Verifying you are human",
  "cf-turnstile",
  "/cdn-cgi/challenge-platform/",

  // Generic bot detection
  "Please Wait...",
  "DDoS protection by",
  "Access denied",
  "bot detection",
  "are you a robot",
  "complete the security check",
];

/**
 * Patterns indicating Cloudflare infrastructure
 */
const CLOUDFLARE_INFRA_PATTERNS = ["/cdn-cgi/", "cloudflare", "__cf_bm", "cf-ray"];

/**
 * Minimum content length threshold (characters)
 */
const MIN_CONTENT_LENGTH = 100;

/**
 * HTTP Engine implementation using native fetch
 */
export class HttpEngine implements Engine {
  readonly config: EngineConfig = ENGINE_CONFIGS.http;

  async scrape(meta: EngineMeta): Promise<EngineResult> {
    const startTime = Date.now();
    const { url, options, logger, abortSignal } = meta;

    try {
      // Create abort controller for timeout
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), this.config.maxTimeout);

      // Link external abort signal
      if (abortSignal) {
        abortSignal.addEventListener("abort", () => controller.abort(), { once: true });
      }

      logger?.debug(`[http] Fetching ${url}`);

      const response = await fetch(url, {
        method: "GET",
        headers: {
          ...DEFAULT_HEADERS,
          ...(options.headers || {}),
        },
        redirect: "follow",
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      const duration = Date.now() - startTime;
      const html = await response.text();

      logger?.debug(`[http] Got response: ${response.status} (${html.length} chars) in ${duration}ms`);

      // Check for HTTP errors
      if (response.status >= 400) {
        throw new HttpError("http", response.status, response.statusText);
      }

      // Check for challenge pages
      const challengeType = this.detectChallenge(html);
      if (challengeType) {
        logger?.debug(`[http] Challenge detected: ${challengeType}`);
        throw new ChallengeDetectedError("http", challengeType);
      }

      // Check for sufficient content
      const textContent = this.extractText(html);
      if (textContent.length < MIN_CONTENT_LENGTH) {
        logger?.debug(`[http] Insufficient content: ${textContent.length} chars`);
        throw new InsufficientContentError("http", textContent.length, MIN_CONTENT_LENGTH);
      }

      return {
        html,
        url: response.url,
        statusCode: response.status,
        contentType: response.headers.get("content-type") || undefined,
        headers: this.headersToRecord(response.headers),
        engine: "http",
        duration,
      };
    } catch (error: unknown) {
      // Re-throw our own errors
      if (
        error instanceof ChallengeDetectedError ||
        error instanceof InsufficientContentError ||
        error instanceof HttpError
      ) {
        throw error;
      }

      // Handle abort/timeout
      if (error instanceof Error) {
        if (error.name === "AbortError") {
          throw new EngineTimeoutError("http", this.config.maxTimeout);
        }

        // Wrap other errors
        throw new EngineError("http", error.message, { cause: error });
      }

      throw new EngineError("http", String(error));
    }
  }

  /**
   * Detect challenge patterns in HTML
   * @returns Challenge type or null if no challenge detected
   */
  private detectChallenge(html: string): string | null {
    const htmlLower = html.toLowerCase();

    // Check for Cloudflare infrastructure + challenge patterns
    const hasCloudflare = CLOUDFLARE_INFRA_PATTERNS.some((p) => htmlLower.includes(p.toLowerCase()));

    for (const pattern of CHALLENGE_PATTERNS) {
      if (htmlLower.includes(pattern.toLowerCase())) {
        if (hasCloudflare || pattern.includes("cf")) {
          return "cloudflare";
        }
        return "bot-detection";
      }
    }

    return null;
  }

  /**
   * Convert Headers to Record<string, string>
   */
  private headersToRecord(headers: Headers): Record<string, string> {
    const record: Record<string, string> = {};
    headers.forEach((value, key) => {
      record[key] = value;
    });
    return record;
  }

  /**
   * Extract visible text from HTML (rough extraction)
   */
  private extractText(html: string): string {
    return html
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  isAvailable(): boolean {
    return true; // Native fetch is always available in Node.js 18+
  }
}

/**
 * Singleton instance
 */
export const httpEngine = new HttpEngine();
```

## File: `src/engines/tlsclient/index.ts`
```typescript
/**
 * TLS Client Engine - got-scraping
 *
 * Uses got-scraping for browser-like TLS fingerprinting.
 * Better compatibility with sites that check TLS signatures.
 * Falls back to hero when JS execution is required.
 */

import { gotScraping } from "got-scraping";
import type { Engine, EngineConfig, EngineMeta, EngineResult } from "../types.js";
import {
  EngineError,
  ChallengeDetectedError,
  InsufficientContentError,
  HttpError,
  EngineTimeoutError,
  EngineUnavailableError,
} from "../errors.js";
import { ENGINE_CONFIGS } from "../types.js";

/**
 * Challenge indicators that require JS execution
 */
const JS_REQUIRED_PATTERNS = [
  // Cloudflare JS challenge
  "cf-browser-verification",
  "challenge-platform",
  "_cf_chl_tk",
  "/cdn-cgi/challenge-platform/",

  // Generic JS requirements
  "Enable JavaScript",
  "JavaScript is required",
  "Please enable JavaScript",
  "requires JavaScript",
  "noscript",
];

/**
 * Blocked/denied patterns
 */
const BLOCKED_PATTERNS = [
  "Access denied",
  "Sorry, you have been blocked",
  "bot detected",
  "suspicious activity",
  "too many requests",
];

/**
 * Minimum content length threshold
 */
const MIN_CONTENT_LENGTH = 100;

/**
 * TLS Client Engine implementation using got-scraping
 */
export class TlsClientEngine implements Engine {
  readonly config: EngineConfig = ENGINE_CONFIGS.tlsclient;
  private available: boolean = true;

  constructor() {
    // Check if got-scraping is properly loaded
    try {
      if (!gotScraping) {
        this.available = false;
      }
    } catch {
      this.available = false;
    }
  }

  async scrape(meta: EngineMeta): Promise<EngineResult> {
    if (!this.available) {
      throw new EngineUnavailableError("tlsclient", "got-scraping not available");
    }

    const startTime = Date.now();
    const { url, options, logger, abortSignal } = meta;

    try {
      // Create abort controller for timeout
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), this.config.maxTimeout);

      // Link external abort signal
      if (abortSignal) {
        abortSignal.addEventListener("abort", () => controller.abort(), { once: true });
      }

      logger?.debug(`[tlsclient] Fetching ${url}`);

      const response = await gotScraping({
        url,
        timeout: {
          request: this.config.maxTimeout,
        },
        headers: options.headers,
        followRedirect: true,
        // got-scraping handles browser fingerprinting automatically
        // It uses header generators and proper TLS settings
      });

      clearTimeout(timeoutId);

      const duration = Date.now() - startTime;
      const html = response.body;

      logger?.debug(`[tlsclient] Got response: ${response.statusCode} (${html.length} chars) in ${duration}ms`);

      // Check for HTTP errors
      if (response.statusCode >= 400) {
        throw new HttpError("tlsclient", response.statusCode, response.statusMessage);
      }

      // Check for JS-required challenges
      const challengeType = this.detectJsRequired(html);
      if (challengeType) {
        logger?.debug(`[tlsclient] JS required: ${challengeType}`);
        throw new ChallengeDetectedError("tlsclient", challengeType);
      }

      // Check for blocked patterns
      const blockedReason = this.detectBlocked(html);
      if (blockedReason) {
        logger?.debug(`[tlsclient] Blocked: ${blockedReason}`);
        throw new ChallengeDetectedError("tlsclient", `blocked: ${blockedReason}`);
      }

      // Check for sufficient content
      const textContent = this.extractText(html);
      if (textContent.length < MIN_CONTENT_LENGTH) {
        logger?.debug(`[tlsclient] Insufficient content: ${textContent.length} chars`);
        throw new InsufficientContentError("tlsclient", textContent.length, MIN_CONTENT_LENGTH);
      }

      return {
        html,
        url: response.url,
        statusCode: response.statusCode,
        contentType: response.headers["content-type"] as string | undefined,
        headers: response.headers as Record<string, string>,
        engine: "tlsclient",
        duration,
      };
    } catch (error: unknown) {
      // Re-throw our own errors
      if (
        error instanceof ChallengeDetectedError ||
        error instanceof InsufficientContentError ||
        error instanceof HttpError ||
        error instanceof EngineUnavailableError
      ) {
        throw error;
      }

      // Handle timeout
      if (error instanceof Error) {
        if (error.name === "TimeoutError" || error.message.includes("timeout")) {
          throw new EngineTimeoutError("tlsclient", this.config.maxTimeout);
        }

        if (error.name === "AbortError") {
          throw new EngineTimeoutError("tlsclient", this.config.maxTimeout);
        }

        // Wrap other errors
        throw new EngineError("tlsclient", error.message, { cause: error });
      }

      throw new EngineError("tlsclient", String(error));
    }
  }

  /**
   * Detect patterns that require JS execution
   */
  private detectJsRequired(html: string): string | null {
    const htmlLower = html.toLowerCase();

    for (const pattern of JS_REQUIRED_PATTERNS) {
      if (htmlLower.includes(pattern.toLowerCase())) {
        if (pattern.includes("cf") || pattern.includes("cloudflare")) {
          return "cloudflare-js";
        }
        return "js-required";
      }
    }

    return null;
  }

  /**
   * Detect blocked/denied patterns
   */
  private detectBlocked(html: string): string | null {
    const htmlLower = html.toLowerCase();

    for (const pattern of BLOCKED_PATTERNS) {
      if (htmlLower.includes(pattern.toLowerCase())) {
        return pattern;
      }
    }

    return null;
  }

  /**
   * Extract visible text from HTML
   */
  private extractText(html: string): string {
    return html
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  isAvailable(): boolean {
    return this.available;
  }
}

/**
 * Singleton instance
 */
export const tlsClientEngine = new TlsClientEngine();
```

## File: `src/formatters/html.ts`
```typescript
/**
 * HTML formatter
 *
 * Returns the cleaned HTML content as-is.
 * The content has already been processed by content-cleaner.ts
 * (ads removed, base64 images stripped, scripts/styles removed).
 */

/**
 * Return HTML content as-is (already cleaned by content-cleaner)
 *
 * This is essentially a pass-through. The cleaning happens in scraper.ts
 * via cleanContent() before this is called.
 */
export function formatToHTML(html: string): string {
  return html;
}
```

## File: `src/formatters/index.ts`
```typescript
// Export all formatters
export { formatToMarkdown, htmlToMarkdown } from "./markdown";
export { formatToHTML } from "./html";
```

## File: `src/formatters/markdown.ts`
```typescript
import { convert } from "@vakra-dev/supermarkdown";

/**
 * Convert HTML to Markdown
 *
 * Simple conversion without any headers, metadata, or formatting wrappers.
 * Returns clean markdown content ready for LLM consumption.
 *
 * Uses supermarkdown (Rust-based) for high-performance conversion.
 */
export function htmlToMarkdown(html: string): string {
  try {
    return convert(html, {
      headingStyle: "atx",
      bulletMarker: "-",
      codeFence: "`",
      linkStyle: "inline",
    });
  } catch (error) {
    console.warn("Error converting HTML to Markdown:", error);
    // Fallback: extract text content
    return html.replace(/<[^>]*>/g, "").trim();
  }
}

/**
 * Alias for htmlToMarkdown (backward compatibility)
 */
export const formatToMarkdown = htmlToMarkdown;
```

## File: `src/proxy/config.ts`
```typescript
import type { ProxyConfig } from "../types";

/**
 * Create proxy URL from configuration
 *
 * Supports both datacenter and residential proxies.
 * For residential proxies (e.g., IPRoyal), generates a sticky session ID.
 *
 * @param config - Proxy configuration
 * @returns Formatted proxy URL
 *
 * @example
 * // Datacenter proxy
 * createProxyUrl({
 *   type: 'datacenter',
 *   username: 'user',
 *   password: 'pass',
 *   host: 'proxy.example.com',
 *   port: 8080
 * })
 * // Returns: "http://user:pass@proxy.example.com:8080"
 *
 * @example
 * // Residential proxy with sticky session
 * createProxyUrl({
 *   type: 'residential',
 *   username: 'customer-abc',
 *   password: 'secret',
 *   host: 'geo.iproyal.com',
 *   port: 12321,
 *   country: 'us'
 * })
 * // Returns: "http://customer-abc_session-hero_123_abc456_country-us:secret@geo.iproyal.com:12321"
 */
export function createProxyUrl(config: ProxyConfig): string {
  // If full URL provided, use it directly
  if (config.url) {
    return config.url;
  }

  // Residential proxy with sticky session
  if (config.type === "residential") {
    // Generate unique session ID for sticky sessions
    const sessionId = `hero_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;

    // Format: customer-{username}_session-{sessionId}_country-{country}:{password}@{host}:{port}
    return `http://customer-${config.username}_session-${sessionId}_country-${
      config.country || "us"
    }:${config.password}@${config.host}:${config.port}`;
  }

  // Datacenter proxy (simple authentication)
  return `http://${config.username}:${config.password}@${config.host}:${config.port}`;
}

/**
 * Parse proxy URL into ProxyConfig
 *
 * @param url - Proxy URL string
 * @returns Parsed proxy configuration
 *
 * @example
 * parseProxyUrl("http://user:pass@proxy.example.com:8080")
 * // Returns: { username: 'user', password: 'pass', host: 'proxy.example.com', port: 8080 }
 */
export function parseProxyUrl(url: string): ProxyConfig {
  try {
    const parsed = new URL(url);

    return {
      url,
      username: parsed.username,
      password: parsed.password,
      host: parsed.hostname,
      port: parsed.port ? parseInt(parsed.port, 10) : undefined,
    };
  } catch (error) {
    throw new Error(`Invalid proxy URL: ${url}`);
  }
}
```

## File: `src/utils/content-cleaner.ts`
```typescript
import { parseHTML } from "linkedom";

/**
 * HTML content cleaning utilities using DOM parsing
 *
 * Layered extraction strategy:
 * 1. Remove scripts, styles, hidden elements (always safe)
 * 2. Remove overlays/modals (always safe)
 * 3. Remove ads (if enabled)
 * 4. Remove navigation with protection (check each element before removing)
 * 5. Find and isolate main content
 */

/**
 * Content cleaning options
 */
export interface CleaningOptions {
  /** Remove ads and tracking elements (default: true) */
  removeAds?: boolean;
  /** Remove base64-encoded images (default: true) */
  removeBase64Images?: boolean;
  /** Extract only main content, removing nav/header/footer/sidebar (default: true) */
  onlyMainContent?: boolean;
  /** CSS selectors for elements to include (if set, only these elements are kept) */
  includeTags?: string[];
  /** CSS selectors for elements to exclude (removed from output) */
  excludeTags?: string[];
}

/**
 * Selectors for elements that should ALWAYS be removed (never content)
 */
const ALWAYS_REMOVE_SELECTORS = [
  // Scripts and styles
  "script",
  "style",
  "noscript",
  "link[rel='stylesheet']",

  // Hidden elements
  "[hidden]",
  "[aria-hidden='true']",
  "[style*='display: none']",
  "[style*='display:none']",
  "[style*='visibility: hidden']",
  "[style*='visibility:hidden']",

  // SVG icons and decorative elements
  "svg[aria-hidden='true']",
  "svg.icon",
  "svg[class*='icon']",

  // Template and metadata
  "template",
  "meta",

  // Embeds that don't convert to text
  "iframe",
  "canvas",
  "object",
  "embed",

  // Forms (usually not main content)
  "form",
  "input",
  "select",
  "textarea",
  "button",
];

/**
 * Selectors for overlays, modals, popups (always remove)
 */
const OVERLAY_SELECTORS = [
  "[class*='modal']",
  "[class*='popup']",
  "[class*='overlay']",
  "[class*='dialog']",
  "[role='dialog']",
  "[role='alertdialog']",
  "[class*='cookie']",
  "[class*='consent']",
  "[class*='gdpr']",
  "[class*='privacy-banner']",
  "[class*='notification-bar']",
  "[id*='cookie']",
  "[id*='consent']",
  "[id*='gdpr']",
  // Fixed/sticky positioned elements
  "[style*='position: fixed']",
  "[style*='position:fixed']",
  "[style*='position: sticky']",
  "[style*='position:sticky']",
];

/**
 * Navigation/boilerplate selectors - exact matches only
 * No wildcards like [class*="nav-"] which are too aggressive
 */
const NAVIGATION_SELECTORS = [
  // Semantic elements
  "header",
  "footer",
  "nav",
  "aside",

  // Header variations
  ".header",
  ".top",
  ".navbar",
  "#header",

  // Footer variations
  ".footer",
  ".bottom",
  "#footer",

  // Sidebars
  ".sidebar",
  ".side",
  ".aside",
  "#sidebar",

  // Modals/popups (backup if not caught by OVERLAY_SELECTORS)
  ".modal",
  ".popup",
  "#modal",
  ".overlay",

  // Ads
  ".ad",
  ".ads",
  ".advert",
  "#ad",

  // Language selectors
  ".lang-selector",
  ".language",
  "#language-selector",

  // Social
  ".social",
  ".social-media",
  ".social-links",
  "#social",

  // Navigation/menus
  ".menu",
  ".navigation",
  "#nav",

  // Breadcrumbs
  ".breadcrumbs",
  "#breadcrumbs",

  // Share buttons
  ".share",
  "#share",

  // Widgets
  ".widget",
  "#widget",

  // Cookie notices (backup)
  ".cookie",
  "#cookie",
];

/**
 * Force-include selectors - elements containing these are PROTECTED from removal
 */
const FORCE_INCLUDE_SELECTORS = [
  // IDs
  "#main",
  "#content",
  "#main-content",
  "#article",
  "#post",
  "#page-content",

  // Semantic elements
  "main",
  "article",
  "[role='main']",

  // Classes
  ".main-content",
  ".content",
  ".post-content",
  ".article-content",
  ".entry-content",
  ".page-content",
  ".article-body",
  ".post-body",
  ".story-content",
  ".blog-content",
];

/**
 * Ad-related selectors (removed when removeAds is true)
 */
const AD_SELECTORS = [
  // Google ads
  "ins.adsbygoogle",
  ".google-ad",
  ".adsense",

  // Generic ad containers
  "[data-ad]",
  "[data-ads]",
  "[data-ad-slot]",
  "[data-ad-client]",

  // Common ad class patterns
  ".ad-container",
  ".ad-wrapper",
  ".advertisement",
  ".sponsored-content",

  // Tracking pixels
  "img[width='1'][height='1']",
  "img[src*='pixel']",
  "img[src*='tracking']",
  "img[src*='analytics']",
];

// ============================================================================
// Content Scoring Heuristics
// ============================================================================

/**
 * Calculate link density of an element (ratio of link text to total text)
 * High link density (>0.5) indicates navigation, not content
 */
function getLinkDensity(element: Element): number {
  const text = element.textContent || "";
  const textLength = text.trim().length;
  if (textLength === 0) return 1;

  let linkLength = 0;
  element.querySelectorAll("a").forEach((link: Element) => {
    linkLength += (link.textContent || "").trim().length;
  });

  return linkLength / textLength;
}

/**
 * Calculate content score for an element
 * Higher scores indicate more likely to be main content
 */
function getContentScore(element: Element): number {
  let score = 0;
  const text = element.textContent || "";
  const textLength = text.trim().length;

  // Positive signals
  score += Math.min(textLength / 100, 50); // Text density (capped)
  score += element.querySelectorAll("p").length * 3; // Paragraphs
  score += element.querySelectorAll("h1, h2, h3, h4, h5, h6").length * 2; // Headings
  score += element.querySelectorAll("img").length * 1; // Images (slight bonus)

  // Negative signals
  score -= element.querySelectorAll("a").length * 0.5; // Too many links
  score -= element.querySelectorAll("li").length * 0.2; // Too many list items

  // Link density penalty
  const linkDensity = getLinkDensity(element);
  if (linkDensity > 0.5) score -= 30;
  else if (linkDensity > 0.3) score -= 15;

  // Class/ID signals
  const classAndId = (element.className || "") + " " + (element.id || "");
  if (/article|content|post|body|main|entry/i.test(classAndId)) score += 25;
  if (/comment|sidebar|footer|nav|menu|header|widget|ad/i.test(classAndId)) score -= 25;

  return score;
}

/**
 * Check if an element looks like navigation (high link density, list-heavy)
 */
function looksLikeNavigation(element: Element): boolean {
  const linkDensity = getLinkDensity(element);
  if (linkDensity > 0.5) return true;

  // Check for menu-like structures (many list items with links)
  const listItems = element.querySelectorAll("li");
  const links = element.querySelectorAll("a");
  if (listItems.length > 5 && links.length > listItems.length * 0.8) return true;

  return false;
}

// ============================================================================
// Removal Functions
// ============================================================================

/**
 * Simple removal without protection checks (for always-safe selectors)
 */
function removeElements(document: Document, selectors: string[]): void {
  for (const selector of selectors) {
    try {
      document.querySelectorAll(selector).forEach((el: Element) => el.remove());
    } catch {
      // Some selectors may not be supported, skip them
    }
  }
}

/**
 * Remove elements WITH PROTECTION - checks each element before removing
 * This is the key fix: if an element contains protected content, don't remove it
 */
function removeWithProtection(
  document: Document,
  selectorsToRemove: string[],
  protectedSelectors: string[]
): void {
  for (const selector of selectorsToRemove) {
    try {
      document.querySelectorAll(selector).forEach((element: Element) => {
        // Check 1: Is this element itself protected?
        const isProtected = protectedSelectors.some((ps) => {
          try {
            return element.matches(ps);
          } catch {
            return false;
          }
        });
        if (isProtected) return;

        // Check 2: Does element CONTAIN protected content?
        const containsProtected = protectedSelectors.some((ps) => {
          try {
            return element.querySelector(ps) !== null;
          } catch {
            return false;
          }
        });
        if (containsProtected) return;

        // Safe to remove
        element.remove();
      });
    } catch {
      // Skip invalid selector
    }
  }
}

// ============================================================================
// Main Content Extraction
// ============================================================================

/**
 * Find the main content container using multiple strategies
 */
function findMainContent(document: Document): Element | null {
  // Helper to validate a content element
  const isValidContent = (el: Element | null): el is Element => {
    if (!el) return false;
    const text = el.textContent || "";
    if (text.trim().length < 100) return false;
    // Reject if it looks like navigation
    if (looksLikeNavigation(el)) return false;
    return true;
  };

  // Priority 1: Semantic <main> element
  const main = document.querySelector("main");
  if (isValidContent(main) && getLinkDensity(main) < 0.4) {
    return main;
  }

  // Priority 2: [role="main"]
  const roleMain = document.querySelector('[role="main"]');
  if (isValidContent(roleMain) && getLinkDensity(roleMain) < 0.4) {
    return roleMain;
  }

  // Priority 3: Single <article> element
  const articles = document.querySelectorAll("article");
  if (articles.length === 1 && isValidContent(articles[0])) {
    return articles[0];
  }

  // Priority 4: Content container by ID/class
  const contentSelectors = [
    "#content",
    "#main-content",
    "#main",
    ".content",
    ".main-content",
    ".post-content",
    ".article-content",
    ".entry-content",
    ".page-content",
    ".article-body",
    ".post-body",
    ".story-content",
    ".blog-content",
  ];

  for (const selector of contentSelectors) {
    try {
      const el = document.querySelector(selector);
      if (isValidContent(el) && getLinkDensity(el) < 0.4) {
        return el;
      }
    } catch {
      // Invalid selector, skip
    }
  }

  // Priority 5: Score-based selection (find highest scoring element)
  const candidates: Array<{ el: Element; score: number }> = [];
  const containers = document.querySelectorAll("div, section, article");

  containers.forEach((el: Element) => {
    const text = el.textContent || "";
    if (text.trim().length < 200) return;

    const score = getContentScore(el);
    if (score > 0) {
      candidates.push({ el, score });
    }
  });

  // Sort by score and return highest
  candidates.sort((a, b) => b.score - a.score);

  if (candidates.length > 0 && candidates[0].score > 20) {
    return candidates[0].el;
  }

  // No main content found
  return null;
}

/**
 * Clean HTML content using layered extraction strategy
 */
export function cleanHtml(html: string, baseUrl: string, options: CleaningOptions = {}): string {
  const {
    removeAds = true,
    removeBase64Images = true,
    onlyMainContent = true,
    includeTags,
    excludeTags,
  } = options;

  const { document } = parseHTML(html);

  // ============================================================================
  // Layer 1: Always remove scripts, styles, hidden elements, overlays
  // ============================================================================
  removeElements(document, ALWAYS_REMOVE_SELECTORS);
  removeElements(document, OVERLAY_SELECTORS);

  // ============================================================================
  // Layer 2: Remove ad-related elements (if enabled)
  // ============================================================================
  if (removeAds) {
    removeElements(document, AD_SELECTORS);
  }

  // ============================================================================
  // Layer 3: Apply user-provided excludeTags
  // ============================================================================
  if (excludeTags && excludeTags.length > 0) {
    removeElements(document, excludeTags);
  }

  // ============================================================================
  // Layer 4: Extract main content (if enabled)
  // KEY FIX: Use protection-aware removal
  // ============================================================================
  if (onlyMainContent) {
    // Remove navigation elements WITH PROTECTION
    // Each element is checked: if it contains #main, .content, etc., don't remove
    removeWithProtection(document, NAVIGATION_SELECTORS, FORCE_INCLUDE_SELECTORS);

    // Then try to find and isolate main content
    const mainContent = findMainContent(document);

    if (mainContent) {
      // Replace body with just the main content
      const body = document.body;
      if (body) {
        const clone = mainContent.cloneNode(true) as Element;
        body.innerHTML = "";
        body.appendChild(clone);
      }
    }
    // If no main content found, we've removed navigation with protection, which is good
  }

  // ============================================================================
  // Layer 5: Apply user-provided includeTags (whitelist mode)
  // ============================================================================
  if (includeTags && includeTags.length > 0) {
    const matchedElements: Element[] = [];

    for (const selector of includeTags) {
      try {
        document.querySelectorAll(selector).forEach((el: Element) => {
          matchedElements.push(el.cloneNode(true) as Element);
        });
      } catch {
        // Invalid selector, skip
      }
    }

    if (matchedElements.length > 0) {
      const body = document.body;
      if (body) {
        body.innerHTML = "";
        matchedElements.forEach((el) => body.appendChild(el));
      }
    }
  }

  // ============================================================================
  // Layer 6: Clean up remaining elements
  // ============================================================================

  // Remove base64 images
  if (removeBase64Images) {
    removeBase64ImagesFromDocument(document);
  }

  // Remove HTML comments
  const walker = document.createTreeWalker(document, 128 /* NodeFilter.SHOW_COMMENT */);
  const comments: Node[] = [];
  while (walker.nextNode()) {
    comments.push(walker.currentNode);
  }
  comments.forEach((comment) => comment.parentNode?.removeChild(comment));

  // Convert relative URLs to absolute
  convertRelativeUrls(document, baseUrl);

  return document.documentElement?.outerHTML || html;
}

/**
 * Remove base64-encoded images from the document
 */
function removeBase64ImagesFromDocument(document: Document): void {
  // Remove img elements with base64 src
  document.querySelectorAll("img[src^='data:']").forEach((el: Element) => {
    el.remove();
  });

  // Remove elements with base64 background images
  document.querySelectorAll("[style*='data:image']").forEach((el: Element) => {
    const style = el.getAttribute("style");
    if (style) {
      const cleanedStyle = style.replace(
        /background(-image)?:\s*url\([^)]*data:image[^)]*\)[^;]*;?/gi,
        ""
      );
      if (cleanedStyle.trim()) {
        el.setAttribute("style", cleanedStyle);
      } else {
        el.removeAttribute("style");
      }
    }
  });

  // Remove source elements with base64 src/srcset
  document.querySelectorAll("source[src^='data:'], source[srcset*='data:']").forEach((el: Element) => {
    el.remove();
  });
}

/**
 * Convert relative URLs to absolute URLs
 */
function convertRelativeUrls(document: Document, baseUrl: string): void {
  // Convert src attributes
  document.querySelectorAll("[src]").forEach((el: Element) => {
    const src = el.getAttribute("src");
    if (src && !src.startsWith("http") && !src.startsWith("//") && !src.startsWith("data:")) {
      try {
        el.setAttribute("src", new URL(src, baseUrl).toString());
      } catch {
        // Invalid URL, leave as-is
      }
    }
  });

  // Convert href attributes
  document.querySelectorAll("[href]").forEach((el: Element) => {
    const href = el.getAttribute("href");
    if (
      href &&
      !href.startsWith("http") &&
      !href.startsWith("//") &&
      !href.startsWith("#") &&
      !href.startsWith("mailto:") &&
      !href.startsWith("tel:") &&
      !href.startsWith("javascript:")
    ) {
      try {
        el.setAttribute("href", new URL(href, baseUrl).toString());
      } catch {
        // Invalid URL, leave as-is
      }
    }
  });
}

/**
 * Main export - clean HTML content
 */
export function cleanContent(html: string, baseUrl: string, options: CleaningOptions = {}): string {
  return cleanHtml(html, baseUrl, options);
}
```

## File: `src/utils/logger.ts`
```typescript
import pino from "pino";

/**
 * Logger type
 */
export type Logger = ReturnType<typeof createLogger>;

/**
 * Check if pino-pretty is available
 */
function hasPinoPretty(): boolean {
  try {
    require.resolve("pino-pretty");
    return true;
  } catch {
    return false;
  }
}

/**
 * Create a logger instance
 *
 * @param name - Logger name
 * @param level - Log level (default: from env or 'info')
 * @returns Pino logger instance
 */
export function createLogger(
  name: string = "reader",
  level: string = process.env.LOG_LEVEL || "info"
) {
  const usePretty =
    process.env.NODE_ENV !== "production" && hasPinoPretty();

  return pino({
    name,
    level,
    transport: usePretty
      ? {
          target: "pino-pretty",
          options: {
            colorize: true,
            translateTime: "SYS:standard",
            ignore: "pid,hostname",
          },
        }
      : undefined,
  });
}

/**
 * Default logger instance
 */
export const logger = createLogger();
```

## File: `src/utils/metadata-extractor.ts`
```typescript
import { parseHTML } from "linkedom";
import type { WebsiteMetadata } from "../types";
import { normalizeUrl } from "./url-helpers";

/**
 * Extract comprehensive website metadata from HTML content
 * Uses proper DOM parsing for reliable attribute extraction
 */
export function extractMetadata(html: string, baseUrl: string): WebsiteMetadata {
  return extractWebsiteMetadata(html, baseUrl);
}

/**
 * Extract comprehensive website metadata from HTML content
 */
export function extractWebsiteMetadata(html: string, baseUrl: string): WebsiteMetadata {
  const { document } = parseHTML(html);

  const metadata: WebsiteMetadata = {
    title: null,
    description: null,
    author: null,
    language: null,
    charset: null,
    favicon: null,
    canonical: null,
    image: null,
    keywords: null,
    robots: null,
    themeColor: null,
    openGraph: null,
    twitter: null,
  };

  // Extract basic meta tags
  metadata.title = extractTitle(document);
  metadata.description = extractMetaContent(document, "description");
  metadata.author = extractMetaContent(document, "author");
  metadata.language = extractLanguage(document);
  metadata.charset = extractCharset(document);

  // Extract links
  metadata.favicon = extractFavicon(document, baseUrl);
  metadata.canonical = extractCanonical(document, baseUrl);
  metadata.image =
    extractMetaContent(document, "og:image") || extractMetaContent(document, "twitter:image");

  // Extract SEO metadata
  metadata.keywords = extractKeywords(document);
  metadata.robots = extractMetaContent(document, "robots");
  metadata.themeColor = extractMetaContent(document, "theme-color");

  // Extract Open Graph metadata
  metadata.openGraph = extractOpenGraph(document);

  // Extract Twitter Card metadata
  metadata.twitter = extractTwitterCard(document);

  return metadata;
}

/**
 * Extract page title from HTML
 */
function extractTitle(document: Document): string | null {
  // Try <title> tag first
  const titleElement = document.querySelector("title");
  if (titleElement?.textContent) {
    return titleElement.textContent.trim();
  }

  // Fallback to og:title
  return extractMetaContent(document, "og:title");
}

/**
 * Extract content from meta tag by name or property
 * Works regardless of attribute order
 */
function extractMetaContent(document: Document, name: string): string | null {
  // Try name attribute first
  const byName = document.querySelector(`meta[name="${name}"]`);
  if (byName) {
    const content = byName.getAttribute("content");
    if (content) return content.trim();
  }

  // Try property attribute (for Open Graph)
  const byProperty = document.querySelector(`meta[property="${name}"]`);
  if (byProperty) {
    const content = byProperty.getAttribute("content");
    if (content) return content.trim();
  }

  return null;
}

/**
 * Extract language from HTML tag
 */
function extractLanguage(document: Document): string | null {
  const lang = document.documentElement?.getAttribute("lang");
  return lang?.trim() || null;
}

/**
 * Extract character set from meta tag
 */
function extractCharset(document: Document): string | null {
  // Try <meta charset="...">
  const charsetMeta = document.querySelector("meta[charset]");
  if (charsetMeta) {
    const charset = charsetMeta.getAttribute("charset");
    if (charset) return charset.trim();
  }

  // Try <meta http-equiv="Content-Type" content="...charset=...">
  const httpEquivMeta = document.querySelector('meta[http-equiv="Content-Type"]');
  if (httpEquivMeta) {
    const content = httpEquivMeta.getAttribute("content");
    if (content) {
      const charsetMatch = content.match(/charset=([^\s;]+)/i);
      if (charsetMatch) return charsetMatch[1].trim();
    }
  }

  return null;
}

/**
 * Extract favicon URL
 */
function extractFavicon(document: Document, baseUrl: string): string | null {
  // Try various icon link types
  const iconSelectors = [
    'link[rel="icon"]',
    'link[rel="shortcut icon"]',
    'link[rel="apple-touch-icon"]',
    'link[rel*="icon"]',
  ];

  for (const selector of iconSelectors) {
    const iconLink = document.querySelector(selector);
    if (iconLink) {
      const href = iconLink.getAttribute("href");
      if (href) {
        return normalizeUrl(href, baseUrl);
      }
    }
  }

  // Fallback to /favicon.ico
  try {
    return normalizeUrl("/favicon.ico", baseUrl);
  } catch {
    return null;
  }
}

/**
 * Extract canonical URL
 */
function extractCanonical(document: Document, baseUrl: string): string | null {
  const canonicalLink = document.querySelector('link[rel="canonical"]');
  if (canonicalLink) {
    const href = canonicalLink.getAttribute("href");
    if (href) {
      return normalizeUrl(href, baseUrl);
    }
  }

  return null;
}

/**
 * Extract keywords from meta tag
 */
function extractKeywords(document: Document): string[] | null {
  const keywordsContent = extractMetaContent(document, "keywords");
  if (!keywordsContent) {
    return null;
  }

  return keywordsContent
    .split(",")
    .map((keyword) => keyword.trim())
    .filter((keyword) => keyword.length > 0);
}

/**
 * Extract Open Graph metadata
 */
function extractOpenGraph(document: Document): WebsiteMetadata["openGraph"] {
  const openGraph: WebsiteMetadata["openGraph"] = {
    title: null,
    description: null,
    type: null,
    url: null,
    image: null,
    siteName: null,
    locale: null,
  };

  openGraph.title = extractMetaContent(document, "og:title");
  openGraph.description = extractMetaContent(document, "og:description");
  openGraph.type = extractMetaContent(document, "og:type");
  openGraph.url = extractMetaContent(document, "og:url");
  openGraph.image = extractMetaContent(document, "og:image");
  openGraph.siteName = extractMetaContent(document, "og:site_name");
  openGraph.locale = extractMetaContent(document, "og:locale");

  // Return null if no Open Graph data found
  if (Object.values(openGraph).every((value) => !value)) {
    return null;
  }

  return openGraph;
}

/**
 * Extract Twitter Card metadata
 */
function extractTwitterCard(document: Document): WebsiteMetadata["twitter"] {
  const twitter: WebsiteMetadata["twitter"] = {
    card: null,
    site: null,
    creator: null,
    title: null,
    description: null,
    image: null,
  };

  twitter.card = extractMetaContent(document, "twitter:card");
  twitter.site = extractMetaContent(document, "twitter:site");
  twitter.creator = extractMetaContent(document, "twitter:creator");
  twitter.title = extractMetaContent(document, "twitter:title");
  twitter.description = extractMetaContent(document, "twitter:description");
  twitter.image = extractMetaContent(document, "twitter:image");

  // Return null if no Twitter Card data found
  if (Object.values(twitter).every((value) => !value)) {
    return null;
  }

  return twitter;
}

/**
 * Extract structured data (JSON-LD) from HTML
 */
export function extractStructuredData(html: string): unknown[] {
  const { document } = parseHTML(html);
  const structuredData: unknown[] = [];

  document.querySelectorAll('script[type="application/ld+json"]').forEach((script: Element) => {
    try {
      const jsonData = JSON.parse(script.textContent || "");
      structuredData.push(jsonData);
    } catch {
      // Invalid JSON, skip
    }
  });

  return structuredData;
}

/**
 * Extract microdata from HTML (basic implementation)
 */
export function extractMicrodata(_html: string): unknown[] {
  const microdata: unknown[] = [];
  // This is a simplified implementation
  // In a real-world scenario, you'd want to use a proper microdata parser
  return microdata;
}

/**
 * Get a summary of the website metadata for debugging
 */
export function getMetadataSummary(metadata: WebsiteMetadata): string {
  const parts: string[] = [];

  if (metadata.title) parts.push(`Title: ${metadata.title}`);
  if (metadata.description) parts.push(`Description: ${metadata.description.substring(0, 100)}...`);
  if (metadata.author) parts.push(`Author: ${metadata.author}`);
  if (metadata.language) parts.push(`Language: ${metadata.language}`);
  if (metadata.keywords) parts.push(`Keywords: ${metadata.keywords.length} found`);
  if (metadata.openGraph)
    parts.push(`Open Graph: ${Object.keys(metadata.openGraph).length} fields`);
  if (metadata.twitter) parts.push(`Twitter Card: ${Object.keys(metadata.twitter).length} fields`);

  return parts.join(" | ") || "No metadata found";
}
```

## File: `src/utils/rate-limiter.ts`
```typescript
import pLimit from "p-limit";

/**
 * Simple rate limit function
 */
export async function rateLimit(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Rate limiter using p-limit to control concurrent requests
 */
export class RateLimiter {
  private limit: ReturnType<typeof pLimit>;

  constructor(requestsPerSecond: number) {
    // Convert requests per second to concurrency limit
    // For rate limiting, we use pLimit with a delay between requests
    this.limit = pLimit(1);
    this.requestsPerSecond = requestsPerSecond;
  }

  private requestsPerSecond: number;
  private lastRequestTime = 0;

  /**
   * Execute a function with rate limiting
   */
  async execute<T>(fn: () => Promise<T>): Promise<T> {
    return this.limit(async () => {
      await this.waitForNextSlot();
      return fn();
    });
  }

  /**
   * Wait for the next available time slot based on rate limit
   */
  private async waitForNextSlot(): Promise<void> {
    const now = Date.now();
    const timeSinceLastRequest = now - this.lastRequestTime;
    const minInterval = 1000 / this.requestsPerSecond;

    if (timeSinceLastRequest < minInterval) {
      const delay = minInterval - timeSinceLastRequest;
      await new Promise((resolve) => setTimeout(resolve, delay));
    }

    this.lastRequestTime = Date.now();
  }

  /**
   * Execute multiple functions concurrently with rate limiting
   */
  async executeAll<T>(functions: Array<() => Promise<T>>): Promise<T[]> {
    return Promise.all(functions.map((fn) => this.execute(fn)));
  }
}
```

## File: `src/utils/robots-parser.ts`
```typescript
/**
 * Simple robots.txt parser for crawler compliance
 */

export interface RobotsRules {
  disallowedPaths: string[];
  allowedPaths: string[];
  crawlDelay: number | null;
}

/**
 * Parse robots.txt content and extract rules for a specific user agent
 */
export function parseRobotsTxt(content: string, userAgent: string = "*"): RobotsRules {
  const rules: RobotsRules = {
    disallowedPaths: [],
    allowedPaths: [],
    crawlDelay: null,
  };

  const lines = content.split("\n").map((line) => line.trim());
  let currentUserAgent = "";
  let matchesUserAgent = false;

  for (const line of lines) {
    // Skip empty lines and comments
    if (!line || line.startsWith("#")) {
      continue;
    }

    const colonIndex = line.indexOf(":");
    if (colonIndex === -1) {
      continue;
    }

    const directive = line.substring(0, colonIndex).trim().toLowerCase();
    const value = line.substring(colonIndex + 1).trim();

    if (directive === "user-agent") {
      currentUserAgent = value.toLowerCase();
      // Match specific user agent or wildcard
      matchesUserAgent = currentUserAgent === "*" || currentUserAgent === userAgent.toLowerCase();
    } else if (matchesUserAgent) {
      if (directive === "disallow" && value) {
        rules.disallowedPaths.push(value);
      } else if (directive === "allow" && value) {
        rules.allowedPaths.push(value);
      } else if (directive === "crawl-delay") {
        const delay = parseFloat(value);
        if (!isNaN(delay)) {
          rules.crawlDelay = delay * 1000; // Convert to milliseconds
        }
      }
    }
  }

  return rules;
}

/**
 * Check if a URL path is allowed by robots.txt rules
 */
export function isPathAllowed(path: string, rules: RobotsRules): boolean {
  // Normalize path
  const normalizedPath = path.startsWith("/") ? path : "/" + path;

  // Check allow rules first (they take precedence)
  for (const allowedPath of rules.allowedPaths) {
    if (pathMatches(normalizedPath, allowedPath)) {
      return true;
    }
  }

  // Check disallow rules
  for (const disallowedPath of rules.disallowedPaths) {
    if (pathMatches(normalizedPath, disallowedPath)) {
      return false;
    }
  }

  // Default: allowed
  return true;
}

/**
 * Check if a path matches a robots.txt pattern
 * Supports * (wildcard) and $ (end anchor)
 */
function pathMatches(path: string, pattern: string): boolean {
  // Empty pattern matches nothing
  if (!pattern) {
    return false;
  }

  // Convert robots.txt pattern to regex
  let regexPattern = pattern
    .replace(/[.+?^${}()|[\]\\]/g, "\\$&") // Escape regex special chars except * and $
    .replace(/\*/g, ".*"); // * becomes .*

  // Handle $ end anchor
  if (regexPattern.endsWith("\\$")) {
    regexPattern = regexPattern.slice(0, -2) + "$";
  } else {
    regexPattern = "^" + regexPattern;
  }

  try {
    const regex = new RegExp(regexPattern);
    return regex.test(path);
  } catch {
    // Invalid pattern, treat as literal prefix match
    return path.startsWith(pattern);
  }
}

/**
 * Fetch and parse robots.txt for a given base URL
 */
export async function fetchRobotsTxt(baseUrl: string): Promise<RobotsRules | null> {
  try {
    const url = new URL("/robots.txt", baseUrl);
    const response = await fetch(url.toString(), {
      headers: {
        "User-Agent": "ReaderEngine/1.0",
      },
    });

    if (!response.ok) {
      // No robots.txt or error - allow everything
      return null;
    }

    const content = await response.text();
    return parseRobotsTxt(content, "ReaderEngine");
  } catch {
    // Network error or invalid URL - allow everything
    return null;
  }
}

/**
 * Check if a URL is allowed by robots.txt
 */
export function isUrlAllowed(url: string, rules: RobotsRules | null): boolean {
  if (!rules) {
    return true;
  }

  try {
    const parsedUrl = new URL(url);
    return isPathAllowed(parsedUrl.pathname + parsedUrl.search, rules);
  } catch {
    return true;
  }
}
```

## File: `src/utils/url-helpers.ts`
```typescript
import { URL } from "url";
import RE2 from "re2";

/**
 * URL validation and normalization utilities
 */

/**
 * Resolve a relative URL against a base URL
 */
export function resolveUrl(relative: string, base: string): string {
  try {
    return new URL(relative, base).toString();
  } catch {
    return relative;
  }
}

/**
 * Validate if a string is a valid URL
 */
export function isValidUrl(string: string): boolean {
  try {
    new URL(string);
    return true;
  } catch {
    return false;
  }
}

/**
 * Normalize a URL by removing fragments and ensuring proper format
 */
export function normalizeUrl(url: string, baseUrl?: string): string {
  try {
    let parsedUrl: URL;

    if (url.startsWith("http://") || url.startsWith("https://")) {
      parsedUrl = new URL(url);
    } else if (baseUrl) {
      parsedUrl = new URL(url, baseUrl);
    } else {
      throw new Error("Relative URL requires base URL");
    }

    // Remove fragment and search params for consistency
    parsedUrl.hash = "";

    return parsedUrl.toString();
  } catch {
    throw new Error(`Invalid URL: ${url}`);
  }
}

/**
 * Extract base domain from a URL
 */
export function extractBaseDomain(url: string): string {
  try {
    const parsedUrl = new URL(url);
    return parsedUrl.hostname;
  } catch {
    throw new Error(`Invalid URL for domain extraction: ${url}`);
  }
}

/**
 * Extract the root domain from a hostname (e.g., "blog.example.com" -> "example.com")
 */
function getRootDomain(hostname: string): string {
  const parts = hostname.split(".");

  // Handle edge cases
  if (parts.length <= 2) {
    return hostname;
  }

  // Handle common two-part TLDs (co.uk, com.au, etc.)
  const twoPartTLDs = ["co.uk", "com.au", "co.nz", "com.br", "co.jp", "co.kr", "com.mx", "org.uk"];
  const lastTwo = parts.slice(-2).join(".");

  if (twoPartTLDs.includes(lastTwo)) {
    // Return last 3 parts for two-part TLDs
    return parts.slice(-3).join(".");
  }

  // Standard case: return last 2 parts
  return parts.slice(-2).join(".");
}

/**
 * Check if a URL belongs to the same domain as the base URL
 * Supports subdomains: blog.example.com matches example.com
 */
export function isSameDomain(url: string, baseUrl: string): boolean {
  try {
    const urlDomain = extractBaseDomain(url);
    const baseDomain = extractBaseDomain(baseUrl);

    // Exact match
    if (urlDomain === baseDomain) {
      return true;
    }

    // Check if URL is a subdomain of base domain
    // e.g., "blog.example.com" should match "example.com"
    const urlRoot = getRootDomain(urlDomain);
    const baseRoot = getRootDomain(baseDomain);

    return urlRoot === baseRoot;
  } catch {
    return false;
  }
}

/**
 * Generate a URL key for deduplication
 * Normalizes:
 * - Removes fragments (hash)
 * - Removes search params
 * - Removes trailing slashes (except root)
 * - Lowercases
 * - Normalizes www vs non-www
 * - Removes default ports (80 for http, 443 for https)
 * - Normalizes index files (index.html, index.htm, default.html)
 */
export function getUrlKey(url: string): string {
  try {
    const parsedUrl = new URL(url);

    // Remove hash fragments
    parsedUrl.hash = "";

    // Remove search params for consistency
    parsedUrl.search = "";

    // Normalize www vs non-www (remove www. prefix for deduplication)
    if (parsedUrl.hostname.startsWith("www.")) {
      parsedUrl.hostname = parsedUrl.hostname.slice(4);
    }

    // Remove default ports (80 for http, 443 for https)
    if (
      (parsedUrl.protocol === "http:" && parsedUrl.port === "80") ||
      (parsedUrl.protocol === "https:" && parsedUrl.port === "443")
    ) {
      parsedUrl.port = "";
    }

    // Normalize index files (treat /path/index.html as /path/)
    const indexFiles = ["index.html", "index.htm", "default.html", "default.htm", "index.php"];
    for (const indexFile of indexFiles) {
      if (parsedUrl.pathname.endsWith(`/${indexFile}`)) {
        parsedUrl.pathname = parsedUrl.pathname.slice(0, -indexFile.length);
        break;
      }
    }

    // Normalize trailing slashes (keep for root path only)
    let normalized = parsedUrl.toString().toLowerCase();
    if (normalized.endsWith("/") && parsedUrl.pathname !== "/") {
      normalized = normalized.slice(0, -1);
    }

    return normalized;
  } catch {
    return url.toLowerCase();
  }
}

/**
 * Validate an array of URLs and return validation results
 */
export function validateUrls(urls: string[]): {
  isValid: boolean;
  validUrls: string[];
  errors: Array<{ url: string; error: string }>;
} {
  const validUrls: string[] = [];
  const errors: Array<{ url: string; error: string }> = [];

  if (!urls || urls.length === 0) {
    return {
      isValid: false,
      validUrls: [],
      errors: [{ url: "", error: "At least one URL is required" }],
    };
  }

  for (const url of urls) {
    if (!url || typeof url !== "string") {
      errors.push({
        url: String(url),
        error: "URL must be a non-empty string",
      });
      continue;
    }

    const trimmedUrl = url.trim();
    if (trimmedUrl === "") {
      errors.push({ url: String(url), error: "URL cannot be empty" });
      continue;
    }

    if (!isValidUrl(trimmedUrl)) {
      errors.push({ url: trimmedUrl, error: "Invalid URL format" });
      continue;
    }

    if (!trimmedUrl.startsWith("http://") && !trimmedUrl.startsWith("https://")) {
      errors.push({
        url: trimmedUrl,
        error: "URL must start with http:// or https://",
      });
      continue;
    }

    validUrls.push(trimmedUrl);
  }

  // Remove duplicates while preserving order
  const uniqueValidUrls = Array.from(new Set(validUrls));

  return {
    isValid: uniqueValidUrls.length > 0 && errors.length === 0,
    validUrls: uniqueValidUrls,
    errors,
  };
}

/**
 * Check if a URL matches any of the given regex patterns
 *
 * Uses Google's RE2 engine which guarantees linear time execution,
 * preventing ReDoS attacks from malicious or pathological patterns.
 */
export function matchesPatterns(url: string, patterns: string[]): boolean {
  if (!patterns || patterns.length === 0) {
    return false;
  }

  return patterns.some((pattern) => {
    try {
      const regex = new RE2(pattern, "i");
      return regex.test(url);
    } catch {
      // Invalid regex pattern or unsupported RE2 syntax, skip it
      return false;
    }
  });
}

/**
 * Check if a URL should be included based on include/exclude patterns
 * - If includePatterns is set, URL must match at least one
 * - If excludePatterns is set, URL must not match any
 */
export function shouldIncludeUrl(
  url: string,
  includePatterns?: string[],
  excludePatterns?: string[]
): boolean {
  // If include patterns are specified, URL must match at least one
  if (includePatterns && includePatterns.length > 0) {
    if (!matchesPatterns(url, includePatterns)) {
      return false;
    }
  }

  // If exclude patterns are specified, URL must not match any
  if (excludePatterns && excludePatterns.length > 0) {
    if (matchesPatterns(url, excludePatterns)) {
      return false;
    }
  }

  return true;
}

/**
 * Check if a URL is likely a content page (not legal, policy, or utility page)
 * Used by crawler to filter out non-content pages
 */
export function isContentUrl(url: string): boolean {
  const lowerUrl = url.toLowerCase();

  // Skip legal and policy pages
  const nonContentPatterns = [
    // Legal and policy pages
    /\/(privacy|terms|tos|legal|cookie|gdpr|disclaimer|imprint|impressum)\b/i,
    /\/(privacy-policy|terms-of-service|terms-of-use|terms-and-conditions)\b/i,
    /\/(cookie-policy|data-protection|acceptable-use|user-agreement)\b/i,
    /\/(refund|cancellation|shipping|return)-?(policy)?\b/i,
    // Contact and support pages (usually not main content)
    /\/(contact|support|help|faq|feedback)\/?$/i,
    // About pages that are typically boilerplate
    /\/(about-us|careers|jobs|press|investors|team)\/?$/i,
    // Authentication and admin areas
    /\/(admin|login|auth|account|dashboard|profile|settings)\//i,
    // E-commerce utility pages
    /\/(cart|checkout|payment|subscription|wishlist)\//i,
    // File downloads and assets
    /\/(uploads|assets|files|static|media|resources)\//i,
    // API endpoints
    /\/(api|graphql|rest|webhook)\//i,
  ];

  if (nonContentPatterns.some((pattern) => pattern.test(lowerUrl))) {
    return false;
  }

  // Skip common non-content file extensions
  const skipExtensions = [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".exe"];
  if (skipExtensions.some((ext) => lowerUrl.endsWith(ext))) {
    return false;
  }

  return true;
}

/**
 * Check if a URL should be crawled based on various criteria
 */
export function shouldCrawlUrl(
  url: string,
  baseUrl: string,
  maxDepth: number,
  currentDepth: number,
  visited: Set<string>
): boolean {
  // Check depth limit - FIXED: use > instead of >=
  if (currentDepth > maxDepth) {
    return false;
  }

  // Check if already visited
  const urlKey = getUrlKey(url);
  if (visited.has(urlKey)) {
    return false;
  }

  // Check if same domain
  if (!isSameDomain(url, baseUrl)) {
    return false;
  }

  // Enhanced filtering for non-content files and patterns
  const lowerUrl = url.toLowerCase();

  // Skip common non-content file extensions
  const skipExtensions = [
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".tar",
    ".gz",
    ".exe",
    ".dmg",
    ".pkg",
    ".deb",
    ".rpm",
    ".apk",
    ".ipa",
    // Image files
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".svg",
    ".webp",
    ".ico",
    ".favicon",
    // Video files
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    // Audio files
    ".mp3",
    ".wav",
    ".ogg",
    ".m4a",
    ".aac",
    // Font files
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".eot",
    // Style and script files
    ".css",
    ".js",
    ".mjs",
    ".ts",
    ".jsx",
    ".tsx",
    // Data and config files
    ".json",
    ".xml",
    ".txt",
    ".md",
    ".rss",
    ".atom",
    ".sitemap",
    ".robots",
    ".webmanifest",
    // Archive files
    ".zip",
    ".tar",
    ".gz",
    ".bz2",
    ".7z",
  ];

  if (skipExtensions.some((ext) => lowerUrl.includes(ext))) {
    return false;
  }

  // Skip common non-content URL patterns
  const skipPatterns = [
    // File downloads and assets
    /\/(uploads|assets|files|static|media|resources)\//i,
    // Authentication and admin areas
    /\/(admin|login|auth|account|dashboard|profile|settings)\//i,
    // API endpoints
    /\/(api|graphql|rest|ws:|webhook)\//i,
    // Common tracking and analytics
    /\/(analytics|tracking|pixel|beacon|ads)\//i,
    // Development and testing areas
    /\/(test|dev|staging|beta|demo)\//i,
    // Common utility and service pages
    /\/(search|cart|checkout|payment|subscription)\//i,
    // Social media and external services
    /\/(facebook|twitter|instagram|youtube|linkedin|github)\//i,
    // Legal and policy pages
    /\/(privacy|terms|tos|legal|cookie|gdpr|disclaimer|imprint|impressum)\b/i,
    /\/(privacy-policy|terms-of-service|terms-of-use|terms-and-conditions)\b/i,
    /\/(cookie-policy|data-protection|acceptable-use|user-agreement)\b/i,
    /\/(refund|cancellation|shipping|return)-?(policy)?\b/i,
    // Contact and support pages (usually not main content)
    /\/(contact|support|help|faq|feedback)\/?$/i,
    // About pages that are typically boilerplate
    /\/(about-us|careers|jobs|press|investors|team)\/?$/i,
  ];

  if (skipPatterns.some((pattern) => pattern.test(url))) {
    return false;
  }

  // Skip URLs with query parameters that indicate non-content
  if (
    url.includes("?") &&
    ["download", "file", "attachment", "export", "print", "share", "email"].some((param) =>
      url.toLowerCase().includes(param)
    )
  ) {
    return false;
  }

  // Skip very short URLs (likely navigation or utility)
  if (url.split("/").filter(Boolean).length < 2 && url.split("?")[0].split("/").length <= 2) {
    return false;
  }

  return true;
}
```

