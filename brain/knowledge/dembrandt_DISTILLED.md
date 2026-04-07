---
id: dembrandt
type: knowledge
owner: OA_Triage
---
# dembrandt
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
#!/usr/bin/env node

/**
 * Dembrandt - Design Token Extraction CLI
 *
 * Extracts design tokens, brand colors, typography, spacing, and component styles
 * from any website using Playwright with advanced bot detection avoidance.
 */

import { program } from "commander";
import chalk from "chalk";
import ora from "ora";
import { chromium, firefox } from "playwright-core";
import { extractBranding } from "./lib/extractors.js";
import { displayResults } from "./lib/display.js";
import { toW3CFormat } from "./lib/w3c-exporter.js";
import { generatePDF } from "./lib/pdf.js";
import { parseSitemap } from "./lib/discovery.js";
import { mergeResults } from "./lib/merger.js";
import { writeFileSync, mkdirSync } from "fs";
import { join } from "path";

program
  .name("dembrandt")
  .description("Extract design tokens from any website")
  .version("0.9.0")
  .argument("<url>")
  .option("--browser <type>", "Browser to use (chromium|firefox)", "chromium")
  .option("--json-only", "Output raw JSON")
  .option("--save-output", "Save JSON file to output folder")
  .option("--dtcg", "Export in W3C Design Tokens (DTCG) format")
  .option("--dark-mode", "Extract colors from dark mode")
  .option("--mobile", "Extract from mobile viewport")
  .option("--slow", "3x longer timeouts for slow-loading sites")
  .option("--brand-guide", "Export a brand guide PDF")
  .option("--no-sandbox", "Disable browser sandbox (needed for Docker/CI)")
  .option("--raw-colors", "Include pre-filter raw colors in JSON output")
  .option("--screenshot <path>", "Save a screenshot of the page")
  .option("--pages <n>", "Analyze up to N total pages including start URL (default: 5)", (v) => {
    const n = parseInt(v, 10);
    if (isNaN(n) || n < 1) throw new Error(`--pages must be a positive integer, got: ${v}`);
    return n;
  })
  .option("--sitemap", "Discover pages from sitemap.xml instead of DOM links")
  .action(async (input, opts) => {
    let url = input;
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      url = "https://" + url;
    }

    // In --json-only mode, redirect all status output to stderr so stdout is clean JSON
    const originalConsoleLog = console.log;
    if (opts.jsonOnly) {
      console.log = (...args) => console.error(...args);
    }

    const spinner = ora({ text: "Starting extraction...", stream: opts.jsonOnly ? process.stderr : process.stdout }).start();
    let browser = null;

    try {
      let useHeaded = false;
      let result;

      while (true) {
        // Select browser type based on --browser flag
        const browserType = opts.browser === 'firefox' ? firefox : chromium;

        spinner.text = `Launching browser (${useHeaded ? "visible" : "headless"
          } mode)`;
        // Firefox-specific launch args (Firefox doesn't support Chromium flags)
        const launchArgs = opts.browser === 'firefox'
          ? [] // Firefox has different flags
          : ["--disable-blink-features=AutomationControlled"];

        if (opts.noSandbox && opts.browser === 'chromium') {
          launchArgs.push("--no-sandbox", "--disable-setuid-sandbox");
        }
        browser = await browserType.launch({
          headless: !useHeaded,
          args: launchArgs,
        });

        try {
          const isMultiPage = opts.pages || opts.sitemap;
          const maxPages = (opts.pages || 5) - 1; // -1 because homepage counts
          result = await extractBranding(url, spinner, browser, {
            navigationTimeout: 90000,
            darkMode: opts.darkMode,
            mobile: opts.mobile,
            slow: opts.slow,
            screenshotPath: opts.screenshot,
            discoverLinks: isMultiPage && !opts.sitemap ? maxPages : null,
          });

          // Multi-page crawl
          if (isMultiPage && maxPages > 0) {
            if (!opts.jsonOnly) spinner.start("Discovering pages...");

            let additionalUrls;
            if (opts.sitemap) {
              // Try post-redirect URL first, fall back to user-provided URL
              // (sites like spotify.com redirect browser to open.spotify.com
              // but sitemap lives at www.spotify.com)
              additionalUrls = await parseSitemap(result.url, maxPages);
              if (additionalUrls.length === 0 && result.url !== url) {
                additionalUrls = await parseSitemap(url, maxPages);
              }
            } else {
              additionalUrls = result._discoveredLinks || [];
            }

            delete result._discoveredLinks;

            if (additionalUrls.length === 0) {
              if (!opts.jsonOnly) spinner.warn("No additional pages discovered");
            } else {
              spinner.stop();
              if (!opts.jsonOnly) console.log(chalk.dim(`  Found ${additionalUrls.length} page(s) to analyze`));

              const allResults = [result];
              for (let i = 0; i < additionalUrls.length; i++) {
                const pageUrl = additionalUrls[i];
                const pageNum = i + 2;
                const total = additionalUrls.length + 1;
                if (!opts.jsonOnly) spinner.start(`Extracting page ${pageNum}/${total}: ${new URL(pageUrl).pathname}`);

                // Polite delay between pages
                await new Promise(r => setTimeout(r, 2000 + Math.random() * 3000));

                try {
                  const pageResult = await extractBranding(pageUrl, spinner, browser, {
                    navigationTimeout: 90000,
                    darkMode: opts.darkMode,
                    mobile: opts.mobile,
                    slow: opts.slow,
                  });
                  delete pageResult._discoveredLinks;
                  allResults.push(pageResult);
                } catch (err) {
                  if (!opts.jsonOnly) spinner.warn(`Skipping ${pageUrl}: ${String(err?.message || err).slice(0, 80)}`);
                }
              }

              spinner.stop();
              result = mergeResults(allResults);
            }
          } else {
            delete result._discoveredLinks;
          }

          break;
        } catch (err) {
          await browser.close();
          browser = null;

          if (useHeaded) throw err;

          if (
            err.message.includes("Timeout") ||
            err.message.includes("net::ERR_")
          ) {
            spinner.warn(
              "Bot detection detected → retrying with visible browser"
            );
            console.error(chalk.dim(`  ↳ Error: ${err.message}`));
            console.error(chalk.dim(`  ↳ URL: ${url}`));
            console.error(chalk.dim(`  ↳ Mode: headless`));
            useHeaded = true;
            continue;
          }
          throw err;
        }
      }

      console.log();

      // Strip raw colors unless --raw-colors flag is set
      if (!opts.rawColors && result.colors && result.colors.rawColors) {
        delete result.colors.rawColors;
      }

      // Convert to W3C format if requested
      const outputData = opts.dtcg ? toW3CFormat(result) : result;

      // Save JSON output if --save-output or --dtcg is specified
      if (opts.saveOutput || opts.dtcg) {
        try {
          const domain = new URL(url).hostname.replace("www.", "");
          const timestamp = new Date()
            .toISOString()
            .replace(/[:.]/g, "-")
            .split(".")[0];
          // Save to current working directory, not installation directory
          const outputDir = join(process.cwd(), "output", domain);
          mkdirSync(outputDir, { recursive: true });

          const suffix = opts.dtcg ? '.tokens' : '';
          const filename = `${timestamp}${suffix}.json`;
          const filepath = join(outputDir, filename);
          writeFileSync(filepath, JSON.stringify(outputData, null, 2));

          console.log(
            chalk.dim(
              `💾 JSON saved to: ${chalk.hex('#8BE9FD')(
                `output/${domain}/${filename}`
              )}`
            )
          );
        } catch (err) {
          console.log(
            chalk.hex('#FFB86C')(`⚠ Could not save JSON file: ${err.message}`)
          );
        }
      }

      // Generate PDF brand guide
      if (opts.brandGuide) {
        try {
          const pdfDomain = new URL(url).hostname.replace("www.", "");
          const now = new Date();
          const pdfDate = now.toISOString().slice(0, 10);
          const pdfTime = `${String(now.getHours()).padStart(2, '0')}-${String(now.getMinutes()).padStart(2, '0')}`;
          const pdfDir = join(process.cwd(), "output", pdfDomain);
          mkdirSync(pdfDir, { recursive: true });
          const pdfFilename = `${pdfDomain}-brand-guide-${pdfDate}-${pdfTime}.pdf`;
          const pdfPath = join(pdfDir, pdfFilename);
          spinner.start("Generating PDF brand guide...");
          await generatePDF(result, pdfPath, browser);
          spinner.stop();
          console.log(
            chalk.dim(
              `PDF saved to: ${chalk.hex('#8BE9FD')(
                `output/${pdfDomain}/${pdfFilename}`
              )}`
            )
          );
        } catch (err) {
          spinner.stop();
          console.log(
            chalk.hex('#FFB86C')(`Could not generate PDF: ${err.message}`)
          );
        }
      }

      // Output to terminal
      if (opts.jsonOnly) {
        console.log = originalConsoleLog;
        console.log(JSON.stringify(outputData, null, 2));
      } else {
        console.log();
        displayResults(result);
      }
    } catch (err) {
      spinner.fail("Failed");
      console.error(chalk.red("\n✗ Extraction failed"));
      console.error(chalk.red(`  Error: ${err.message}`));
      console.error(chalk.dim(`  URL: ${url}`));
      process.exit(1);
    } finally {
      if (browser) await browser.close();
    }
  });

program.parse();

```

### File: package.json
```json
{
  "name": "dembrandt",
  "version": "0.9.0",
  "description": "Extract design tokens and brand assets from any website",
  "mcpName": "io.github.dembrandt/dembrandt",
  "main": "index.js",
  "type": "module",
  "bin": {
    "dembrandt": "index.js",
    "dembrandt-mcp": "mcp-server.js"
  },
  "files": [
    "index.js",
    "mcp-server.js",
    "lib/"
  ],
  "scripts": {
    "start": "node index.js",
    "brand-challenge": "node run-no-login-challenge.mjs",
    "brand-challenge:report": "node run-no-login-challenge.mjs || true",
    "install-browser": "npx playwright install chromium firefox || echo 'Playwright browser installation failed. You may need to install system dependencies manually.'",
    "local-ui": "cd local-ui && npm start",
    "qa:baseline": "node test/qa.mjs --baseline",
    "qa:diff": "node test/qa.mjs --diff",
    "qa:site": "node test/qa.mjs --site"
  },
  "keywords": [
    "design-tokens",
    "design-system",
    "branding",
    "web-scraping",
    "cli",
    "playwright",
    "extraction"
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/dembrandt/dembrandt.git"
  },
  "bugs": {
    "url": "https://github.com/dembrandt/dembrandt/issues"
  },
  "homepage": "https://dembrandt.com",
  "author": "thevangelist <info@esajuhana.com>",
  "license": "MIT",
  "dependencies": {
    "@modelcontextprotocol/sdk": "1.29.0",
    "@playwright/browser-chromium": "^1.57.0",
    "@playwright/browser-firefox": "^1.57.0",
    "chalk": "^5.3.0",
    "commander": "^11.1.0",
    "ora": "^7.0.1",
    "playwright-core": "^1.57.0",
    "zod": "4.3.6"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}

```

### File: README.md
```md
# Dembrandt.

[![npm version](https://img.shields.io/npm/v/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![npm downloads](https://img.shields.io/npm/dm/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![license](https://img.shields.io/npm/l/dembrandt.svg)](https://github.com/dembrandt/dembrandt/blob/main/LICENSE)

Extract any website’s design system into design tokens in a few seconds: logo, colors, typography, borders, and more. One command.

![Dembrandt — Any website to design tokens](https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/images/banner.png)

**CLI output**

![CLI extraction of netflix.com](https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/images/cli-output.png)

**Brand Guide PDF**

![Brand guide PDF extracted from any URL](https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/images/brand-guide.png)

**Local UI**

![Local UI showing extracted brand](https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/images/local-ui.png)

## Install

Install globally: `npm install -g dembrandt`

```bash
dembrandt bmw.de
```

Or use npx without installing: `npx dembrandt bmw.de`

Requires Node.js 18+

## AI Agent Integration (MCP)

Use Dembrandt as a tool in Claude Code, Cursor, Windsurf, or any MCP-compatible client. Ask your agent to "extract the color palette from stripe.com" and it calls Dembrandt automatically.

```bash
claude mcp add --transport stdio dembrandt -- npx -y dembrandt-mcp
```

Or add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "dembrandt": {
      "command": "npx",
      "args": ["-y", "dembrandt-mcp"]
    }
  }
}
```

7 tools available: `get_design_tokens`, `get_color_palette`, `get_typography`, `get_component_styles`, `get_surfaces`, `get_spacing`, `get_brand_identity`.

## What to expect from extraction?

- Colors (semantic, palette, CSS variables)
- Typography (fonts, sizes, weights, sources)
- Spacing (margin/padding scales)
- Borders (radius, widths, styles, colors)
- Shadows
- Components (buttons, badges, inputs, links)
- Breakpoints
- Icons & frameworks

## Usage

```bash
dembrandt <url>                    # Basic extraction (terminal display only)
dembrandt bmw.de --json-only       # Output raw JSON to terminal (no formatted display, no file save)
dembrandt bmw.de --save-output     # Save JSON to output/bmw.de/YYYY-MM-DDTHH-MM-SS.json
dembrandt bmw.de --dtcg            # Export in W3C Design Tokens (DTCG) format (auto-saves as .tokens.json)
dembrandt bmw.de --dark-mode       # Extract colors from dark mode variant
dembrandt bmw.de --mobile          # Use mobile viewport (390x844, iPhone 12/13/14/15) for responsive analysis
dembrandt bmw.de --slow            # 3x longer timeouts (24s hydration) for JavaScript-heavy sites
dembrandt bmw.de --brand-guide      # Generate a brand guide PDF
dembrandt bmw.de --pages 5         # Analyze 5 pages (homepage + 4 discovered pages), merges results
dembrandt bmw.de --sitemap          # Discover pages from sitemap.xml instead of DOM links
dembrandt bmw.de --pages 10 --sitemap # Combine: up to 10 pages discovered via sitemap
dembrandt bmw.de --no-sandbox      # Disable Chromium sandbox (required for Docker/CI)
dembrandt bmw.de --browser=firefox # Use Firefox instead of Chromium (better for Cloudflare bypass)
```

Default: formatted terminal display only. Use `--save-output` to persist results as JSON files. Browser automatically retries in visible mode if headless extraction fails.

### Multi-Page Extraction

Analyze multiple pages to get a more complete picture of a site's design system. Results are merged into a single unified output with cross-page confidence boosting — colors appearing on multiple pages get higher confidence scores.

```bash
# Analyze homepage + 4 auto-discovered pages (default: 5 total)
dembrandt stripe.com --pages 5

# Use sitemap.xml for page discovery instead of DOM link scraping
dembrandt stripe.com --sitemap

# Combine both: up to 10 pages from sitemap
dembrandt stripe.com --pages 10 --sitemap
```

**Page discovery** works two ways:
- **DOM links** (default): Scrapes navigation, header, and footer links from the homepage, prioritizing key pages like /pricing, /about, /features
- **Sitemap** (`--sitemap`): Parses sitemap.xml (checks robots.txt first), follows sitemapindex references, and scores URLs by importance

Pages are crawled sequentially with polite delays. Failed pages are skipped without aborting the run.

### Browser Selection

By default, dembrandt uses Chromium. If you encounter bot detection or timeouts (especially on sites behind Cloudflare), try Firefox which is often more successful at bypassing these protections:

```bash
# Use Firefox instead of Chromium
dembrandt bmw.de --browser=firefox

# Combine with other flags
dembrandt bmw.de --browser=firefox --save-output --dtcg
```

**When to use Firefox:**
- Sites behind Cloudflare or other bot detection systems
- Timeout issues on heavily protected sites
- WSL environments where headless Chromium may struggle

**Installation:**
Firefox browser is installed automatically with `npm install`. If you need to install manually:

```bash
npx playwright install firefox
```

### W3C Design Tokens (DTCG) Format

Use `--dtcg` to export in the standardized [W3C Design Tokens Community Group](https://www.designtokens.org/) format:

```bash
dembrandt stripe.com --dtcg
# Saves to: output/stripe.com/TIMESTAMP.tokens.json
```

The DTCG format is an industry-standard JSON schema that can be consumed by design tools and token transformation libraries like [Style Dictionary](https://styledictionary.com).

## Local UI

Browse your extracted brands in a visual interface.

### Setup

```bash
cd local-ui
npm install
```

### Running

```bash
npm start
```

Opens http://localhost:5173 with API on port 3002.

### Features

- Visual grid of all extracted brands
- Color palettes with click-to-copy
- Typography specimens
- Spacing, shadows, border radius visualization
- Button and link component previews
- Dark/light theme toggle
- Section nav links on extraction pages — jump directly to Colors, Typography, Shadows, etc. via a sticky sidebar

Extractions are performed via CLI (`dembrandt <url> --save-output`) and automatically appear in the UI.

## Use Cases

- Brand audits & competitive analysis
- Design system documentation
- Reverse engineering brands
- Multi-site brand consolidation

## How It Works

Uses Playwright to render the page, extracts computed styles from the DOM, analyzes color usage and confidence, groups similar typography, detects spacing patterns, and returns actionable design tokens.

### Extraction Process

1. Browser Launch - Launches browser (Chromium by default, Firefox optional) with stealth configuration
2. Anti-Detection - Injects scripts to bypass bot detection
3. Navigation - Navigates to target URL with retry logic
4. Hydration - Waits for SPAs to fully load (8s initial + 4s stabilization)
5. Content Validation - Verifies page content is substantial (>500 chars)
6. Parallel Extraction - Runs all extractors concurrently for speed
7. Analysis - Analyzes computed styles, DOM structure, and CSS variables
8. Scoring - Assigns confidence scores based on context and usage

### Color Confidence

- High — Logo, brand elements, primary buttons
- Medium — Interactive elements, icons, navigation
- Low — Generic UI components (filtered from display)
- Only shows high and medium confidence colors in terminal. Full palette in JSON.

## Limitations

- Dark mode requires --dark-mode flag (not automatically detected)
- Hover/focus states extracted from CSS (not fully interactive)
- Canvas/WebGL-rendered sites cannot be analyzed (e.g., Tesla, Apple Vision Pro demos)
- JavaScript-heavy sites require hydration time (8s initial + 4s stabilization)
- Some dynamically-loaded content may be missed
- Default viewport is 1920x1080 (use --mobile for 390x844 iPhone viewport)

## Ethics & Legality

Dembrandt extracts publicly available design information (colors, fonts, spacing) from website DOMs for analysis purposes. This falls under fair use in most jurisdictions (USA's DMCA § 1201(f), EU Software Directive 2009/24/EC) when used for competitive analysis, documentation, or learning.

Legal: Analyzing public HTML/CSS is generally legal. Does not bypass protections or violate copyright. Check site ToS before mass extraction.

Ethical: Use for inspiration and analysis, not direct copying. Respect servers (no mass crawling), give credit to sources, be transparent about data origin.

## Contributing

Bugs you found? Weird websites that make it cry? Pull requests (even one-liners make me happy)?

Spam me in [Issues](https://github.com/dembrandt/dembrandt/issues) or PRs. I reply to everything.

Let's keep the light alive together.

@thevangelist

---

MIT — do whatever you want with it.

```

### File: examples\README.md
```md
# Dembrandt Examples

This folder contains real-world examples of design token extraction from popular websites. Each JSON file demonstrates Dembrandt's ability to extract colors, typography, spacing, shadows, and component styles from production sites.

## Examples

### 1. [material.io.json](material.io.json) - Google Material Design 3

**Why this matters:** Google's Material Design is the foundation for Android and countless web apps. This extraction captures Material 3's latest design tokens.

**Key findings:**
- **Primary color**: `rgb(100, 66, 214)` - Material's signature purple
- **Typography**: Google Sans & Google Sans Text font families
  - Display: 96px / 6rem (h1)
  - Headline: 57px / 3.56rem (h2)
  - Body: 16px / 1rem with 500 weight for links
- **Spacing scale**: 8px base grid system (8px, 16px, 24px, 32px, 64px, 96px)
- **Border radius**: 24px (high confidence), 16px, 4px - Material's rounded corners
- **Components**: 3 button variants detected
  - Primary: Purple fill (`rgb(100, 66, 214)`) with 48px border radius
  - Container: Light purple background
  - Text-only: Transparent background

**Design system characteristics:**
- Clean, semantic color palette with 15 unique colors
- CSS variables for theming (`--mio-theme-color-*`)
- 6 responsive breakpoints (600px, 960px, 1294px)
- Bootstrap framework patterns detected

---

### 2. [carbon.design.json](carbon.design.json) - IBM Carbon Design System

**Why this matters:** IBM Carbon is built for enterprise applications with accessibility and consistency at its core. Perfect example of a mature, production design system.

**Key findings:**
- **Color palette**: Enterprise-grade neutrals
  - Primary: `rgb(0, 0, 0)` - 272 instances
  - Gray scale: `rgb(40, 40, 40)` (197 instances), `rgb(78, 78, 78)` (71 instances)
  - Minimal accent colors - enterprise aesthetic
- **Typography**: IBM Plex family
  - Sans: 32px / 2rem (medium weight)
  - Mono: 14px / 0.875rem (400 weight) - for code/data
  - Text: 16px / 1rem - body text
- **Spacing scale**: Conservative, accessible spacing
  - 8px, 16px, 24px, 32px (4px not as prominent as Material)
- **Components**: Minimal button styles (1 variant) - emphasizes function over form

**Design system characteristics:**
- Highly accessible (10 unique colors, high contrast)
- 2 frameworks detected (React + custom components)
- Professional, minimal aesthetic
- Perfect for data-heavy enterprise UIs

---

### 3. [stripe.com.json](stripe.com.json) - Stripe Payment Platform

**Why this matters:** Stripe's design is polished, conversion-focused, and represents modern SaaS UI best practices.

**Key findings:**
- **Rich color palette**: 57 unique colors (most diverse of the three)
  - Primary text: `rgb(66, 84, 102)` - 3,685 instances (slate blue)
  - Accent blues and purples throughout
  - Professional yet friendly color scheme
- **Typography**: Custom sans-serif stack
  - 21 distinct typography styles (most complex)
  - Range from 12px to 80px
  - Sophisticated type scale for marketing + product
- **Spacing scale**: 20 unique spacing values
  - Fine-grained control for pixel-perfect layouts
  - Mix of 4px and 8px base increments
- **Border radius**: 28 different radius values
  - Highly polished, consistent rounding
  - Ranges from subtle (2px) to prominent (24px+)
- **Shadows**: 14 shadow variants
  - Sophisticated depth system
  - Elevates CTAs and cards
- **Components**: Rich component library
  - 1 button variant, 1 input style detected
  - SVG logo extracted (60x25px)
- **Responsive**: 13 breakpoints - fine-tuned responsive design
- **Icons**: 1 icon system detected

**Design system characteristics:**
- Most comprehensive extraction (101KB content analyzed)
- Production-grade component library
- Conversion-optimized design (fintech trust signals)
- No framework detected (custom implementation)

---

## Comparison Table

| Metric | Material.io | Carbon.design | Stripe.com |
|--------|------------|---------------|------------|
| **Colors** | 15 | 10 | 57 |
| **Typography Styles** | 10 | 3 | 21 |
| **Spacing Values** | 13 | 5 | 20 |
| **Border Radius** | 8 | 1 | 28 |
| **Shadows** | 1 | 0 | 14 |
| **Buttons** | 3 | 1 | 1 |
| **Breakpoints** | 6 | 0 | 13 |
| **Design Philosophy** | Consumer-friendly, bold | Enterprise, accessible | Conversion-focused, polished |

---

## How These Were Generated

Each example was generated with a single command:

```bash
npx dembrandt material.io --json-only > examples/material.io.json
npx dembrandt carbon.design --json-only > examples/carbon.design.json
npx dembrandt stripe.com --json-only > examples/stripe.com.json
```

**Key capabilities demonstrated:**
- ✅ Automatic redirect handling (material.io → m3.material.io)
- ✅ SPA hydration detection (8-second wait for JavaScript-heavy sites)
- ✅ Component analysis (buttons, inputs, etc.)
- ✅ Framework detection (Bootstrap, React)
- ✅ Logo extraction (SVG dimensions)
- ✅ Responsive breakpoint discovery
- ✅ CSS variable extraction

---

## What You Can Do With These

**For designers:**
- Import color palettes into Figma/Sketch
- Understand competitor design systems
- Build design system documentation

**For developers:**
- Generate Tailwind configs from extracted tokens
- Audit brand consistency across sites
- Reverse-engineer spacing scales for your own projects

**For product teams:**
- Competitive analysis of design patterns
- Build design system guidelines
- Document existing implementations

---

## Try It Yourself

```bash
# Extract any site (no installation needed!)
npx dembrandt yoursite.com

# Export as JSON
npx dembrandt yoursite.com --json-only > tokens.json
```

---

**🎨 These examples showcase how Dembrandt extracts production design tokens without requiring API access or authentication - just a URL.**

```

### File: CHANGELOG.md
```md
# Changelog

## [0.3.0] - 2025-11-24

### Added
- `--slow` flag for slow-loading sites with 3x longer timeouts
- Tailwind CSS exporter (`lib/exporters.js`)
- Brand challenge test suite against SPA/heavy-JS sites (Tesla, Dribbble, SoundCloud, Airtable, Product Hunt, Behance)
- GitHub Actions CI workflow for automated testing
- Border detection with confidence scoring

### Changed
- Improved terminal output with tree structure
- Enhanced retry logic for empty content
- Better SPA hydration detection
- Test suite refocused on SPA and interactive sites
- Lowered content validation threshold from 500 to 100 chars for minimal-text sites
- Clearer border style display with `(per-side)` label for shorthand values
- Shadows now sorted by confidence and usage frequency (most confident first)
- Button detection now includes outline/bordered buttons (previously skipped transparent backgrounds)

## [0.2.0] - 2025-11-22

### Added
- `--dark-mode` and `--mobile` flags
- Clickable terminal links
- Enhanced bot detection avoidance

## [0.1.0] - 2025-11-21

Initial public release

```

### File: CONTRIBUTING.md
```md
# Contributing to Dembrandt

Dembrandt reveals any website’s brand the way Rembrandt revealed light from shadow... color, typography, tone, emotion, and drama in seconds.

De-em-brand-t is the smartest way to dissect a brand, design system and design tokens from any website. Useful for various use cases.

I’m @thevangelist, and I welcome you to develop this creative tool with me. Be it stargazers, dreamers, bug hunters, or just local hobos.

Please tell me about:

- Bugs you found
- Weird websites that make it cry
- Pull requests (even one-liners make me happy)
- Open a discussion, I’ll talk to you, promise
- Graphic design workflow ideas
- Dev workflow pain
- Missing design tokens
- Marketing–design–dev chaos
- Design systems you love/hate
- How to use more AI without selling our souls
- Tone of voice obsessions
- How you wish to use this thing
- Your latest dream (or nightmare)

I am quite easy to work with. Really. 
Spam me in Issues, PRs, or anywhere. I reply to everything.

@thevangelist.

```

### File: DEVELOPMENT.md
```md
# Development Guide

This guide covers development workflows, testing, and contribution guidelines for Dembrandt.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/dembrandt/dembrandt.git
cd dembrandt
```

2. Install dependencies:
```bash
npm install
```

3. Install Playwright browser:
```bash
npm run install-browser
```

## Development Commands

```bash
# Run locally
node index.js <url>

# Run with options
node index.js stripe.com --debug        # Visible browser
node index.js stripe.com --json-only    # JSON only
node index.js stripe.com --slow         # 3x timeouts

# Brand challenge suite (tests against complex sites)
npm run brand-challenge

# Version diff test (compare npm vs main branch)
# Use Claude Code slash command: /test-version-diff stripe.com
```

## Testing

### Version Diff Test

Compare output between the latest npm release and the main branch to catch regressions before publishing.

**Using Claude Code (recommended):**

```bash
# In Claude Code, use the slash command:
/test-version-diff stripe.com

# Or just:
/test-version-diff
# (Claude will ask for the domain)
```

**What it does:**
1. Runs the latest npm release version (`npx dembrandt@latest`) against your domain
2. Runs the current main branch version against the same domain
3. Compares the JSON outputs and shows differences
4. Saves all outputs and diff to `test-output/<domain>-<timestamp>/`

**Output files:**
- `npm-release.json` - Output from latest npm version
- `main-branch.json` - Output from current main branch
- `npm-release-formatted.json` - Sorted JSON for npm version
- `main-branch-formatted.json` - Sorted JSON for main branch
- `diff.txt` - Line-by-line differences (if any)

**Example outputs:**

✅ **No differences:**
```
🧪 Testing version diff for: stripe.com
📁 Output directory: ./test-output/stripe.com-20250128-143022

📦 Running latest npm release version...
✅ NPM version output saved to: ./test-output/stripe.com-20250128-143022/npm-release.json

🔨 Running current main branch version...
✅ Main branch output saved to: ./test-output/stripe.com-20250128-143022/main-branch.json

📊 Comparing outputs...

✅ No differences found! Outputs are identical.

📁 All files saved to: ./test-output/stripe.com-20250128-143022
```

📝 **With differences:**
```
📊 Comparing outputs...

📝 Differences found:

--- ./test-output/stripe.com-20250128-143022/npm-release-formatted.json
+++ ./test-output/stripe.com-20250128-143022/main-branch-formatted.json
@@ -45,7 +45,10 @@
       "value": "1px",
       "count": 33,
       "confidence": "high"
-    }
+    },
+    "combinations": [
+      { "width": "1px", "style": "solid", "color": "#e0e0e0" }
+    ]
   ],
   "typography": {

💾 Full diff saved to: ./test-output/stripe.com-20250128-143022/diff.txt
```

**Use cases:**
- Before releases to ensure changes don't break existing functionality
- After major refactoring to verify output consistency
- When debugging extraction issues to compare behavior
- To document intentional changes in output format

### Brand Challenge Suite

Test against complex SPA/interactive sites with heavy JavaScript:

```bash
npm run brand-challenge
```

Tests against:
- Tesla (WebGL/3D, bot protection)
- Dribbble (interactive previews)
- SoundCloud (SPA, media streaming)
- Airtable (SaaS grids, dynamic content)
- Product Hunt (SPA, async listings)
- Behance (portfolios, AJAX content)

Uses `--slow` flag for 3x timeouts (24s hydration, 12s stabilization).

## Project Structure

```
dembrandt/
├── index.js                      # CLI entry point
├── lib/
│   ├── extractors.js            # Core extraction functions
│   └── display.js               # Terminal output formatting
├── test-version-diff.mjs        # Version comparison test
├── test-version-diff.sh         # Version comparison test (bash)
├── run-no-login-challenge.mjs   # Brand challenge suite
├── examples/                    # Example outputs
└── output/                      # Extraction outputs
```

## Architecture

See [CLAUDE.md](CLAUDE.md) for detailed architecture documentation, including:
- Entry point flow and browser lifecycle
- Core extraction engine and parallelization
- Anti-bot protection strategies
- Color confidence scoring
- Display layer formatting

## Release Process

1. **Test changes:**
```bash
npm run test:version-diff stripe.com
npm run brand-challenge
```

2. **Update version:**
```bash
# Edit package.json version manually
git add package.json
git commit -m "bump: version x.y.z"
```

3. **Create git tag:**
```bash
git tag -a vx.y.z -m "Release vx.y.z - Description"
git push origin main --tags
```

4. **Publish to npm:**
```bash
npm publish
```

5. **Verify:**
```bash
npx dembrandt@latest stripe.com
```

## Contributing Guidelines

1. **Code style:**
   - Use ES modules (`import`/`export`)
   - Prefer async/await over promises
   - Add JSDoc comments for public functions
   - Follow existing formatting conventions

2. **Adding extractors:**
   - Add function to `lib/extractors.js`
   - Add to `Promise.all` in `extractBranding()`
   - Add display function to `lib/display.js`
   - Add call in `displayResults()`

3. **Testing:**
   - Test against multiple sites (simple and complex)
   - Run brand challenge suite
   - Run version diff test against known-good sites
   - Test with `--debug` flag to see browser behavior

4. **Pull requests:**
   - Include test results in PR description
   - Document breaking changes clearly
   - Update CHANGELOG.md if applicable
   - Add examples for new features

## Common Development Tasks

### Adding a new extraction function

1. Create async function in `lib/extractors.js`:
```javascript
async function extractNewFeature(page) {
  return await page.evaluate(() => {
    // DOM analysis in browser context
    return { /* extracted data */ };
  });
}
```

2. Add to extraction pipeline in `extractBranding()`:
```javascript
const results = await Promise.all([
  extractLogo(page),
  extractColors(page),
  extractNewFeature(page), // <-- Add here
  // ... other extractors
]);
```

3. Add display function in `lib/display.js`:
```javascript
function displayNewFeature(data) {
  if (!data) return;
  console.log(chalk.dim('├─') + ' ' + chalk.bold('New Feature'));
  // ... formatting
}
```

4. Call display function in `displayResults()`:
```javascript
displayNewFeature(data.newFeature);
```

### Modifying confidence scoring

Edit `contextScores` object in `extractColors()` or similar scoring logic:

```javascript
const contextScores = {
  logo: 5,        // Highest confidence
  brand: 5,
  primary: 4,
  button: 3,
  // ... add your contexts
};
```

### Adjusting timeouts

Timeouts use `timeoutMultiplier` (3x when `--slow` is used):

```javascript
const timeoutMultiplier = options.slow ? 3 : 1;

// Navigation timeout
await page.goto(url, {
  timeout: 20000 * timeoutMultiplier,
  waitUntil: 'networkidle',
});

// Hydration wait
await page.waitForTimeout(8000 * timeoutMultiplier);
```

## Debugging Tips

1. **Use `--debug` flag** to see browser:
```bash
node index.js stripe.com --debug
```

2. **Check extraction step by step:**
```javascript
// Add console.log in extractors.js
console.log('Extracted colors:', colors);
```

3. **Test in browser console:**
```javascript
// Copy extraction logic to browser DevTools
document.querySelectorAll('button').length
```

4. **Check bot detection:**
```bash
# If site loads differently, likely bot detection
node index.js site.com --debug
# vs
# Open site.com in regular Chrome
```

5. **Verify output structure:**
```bash
node index.js stripe.com --json-only
cat output/stripe.com/latest.json | jq .
```

## Performance Optimization

- Extractors run in parallel using `Promise.all()`
- DOM queries happen in browser context (`page.evaluate()`)
- Minimize data transfer between Node and browser
- Use CSS selectors efficiently
- Cache repeated computations

## Security Considerations

- Never expose API keys or credentials
- Validate all user input (URLs)
- Use stealth mode to avoid bot detection
- Respect robots.txt and site ToS
- Rate limit to avoid overwhelming servers

## Support

- Issues: https://github.com/dembrandt/dembrandt/issues
- Discussions: https://github.com/dembrandt/dembrandt/discussions
- Email: info@esajuhana.com

```

### File: mcp-server.js
```js
#!/usr/bin/env node

/**
 * Dembrandt MCP Server
 *
 * Extract design tokens from any live website. Works with Claude Code, Cursor,
 * Windsurf, and any MCP-compatible client.
 *
 * Install:
 *   claude mcp add --transport stdio dembrandt -- npx -y dembrandt-mcp
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { chromium } from "playwright-core";
import { readFileSync } from "node:fs";
import { extractBranding } from "./lib/extractors.js";

const { version } = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8"));

const server = new McpServer({
  name: "dembrandt",
  version,
});

// extractBranding expects a spinner — stub it for MCP context
const nullSpinner = {
  text: "",
  start(msg) { this.text = msg; return this; },
  stop() { return this; },
  succeed(msg) { return this; },
  fail(msg) { return this; },
};

/**
 * Run extraction with error handling suitable for MCP responses.
 * Returns { ok, data?, error? } so tool handlers never throw.
 */
async function runExtraction(url, options = {}) {
  if (!/^https?:\/\//i.test(url)) url = "https://" + url;
  let browser;
  try {
    browser = await chromium.launch({
      headless: true,
      args: ["--disable-blink-features=AutomationControlled"],
    });
  } catch (err) {
    return {
      ok: false,
      error: `Browser launch failed. Is Playwright installed? Run: npx playwright install chromium\n\n${err.message}`,
    };
  }

  // Suppress console output — extractors.js writes directly to stdout
  // which would corrupt the JSON-RPC stream
  const _log = console.log;
  const _warn = console.warn;
  const _error = console.error;
  console.log = () => {};
  console.warn = () => {};
  console.error = () => {};

  try {
    const data = await extractBranding(url, nullSpinner, browser, {
      navigationTimeout: 90000,
      slow: options.slow || false,
      darkMode: options.darkMode || false,
      mobile: options.mobile || false,
    });
    return { ok: true, data };
  } catch (err) {
    const msg = err.message || String(err);
    if (msg.includes("timeout") || msg.includes("Timeout")) {
      return { ok: false, error: `Extraction timed out for ${url}. Try with slow: true for heavy SPAs.` };
    }
    if (msg.includes("net::ERR_NAME_NOT_RESOLVED")) {
      return { ok: false, error: `Could not resolve ${url}. Check the URL.` };
    }
    if (msg.includes("net::ERR_CONNECTION_REFUSED")) {
      return { ok: false, error: `Connection refused by ${url}.` };
    }
    return { ok: false, error: `Extraction failed for ${url}: ${msg}` };
  } finally {
    console.log = _log;
    console.warn = _warn;
    console.error = _error;
    await browser.close().catch(() => {});
  }
}

function jsonResult(data) {
  return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
}

function errorResult(message) {
  return { content: [{ type: "text", text: message }], isError: true };
}

/**
 * Wrapper that handles extraction + error formatting for all tools.
 * `pick` receives the full result and returns the filtered subset.
 */
function toolHandler(pick, extraOptions = {}) {
  return async (params) => {
    const { url, slow, darkMode } = params;
    const result = await runExtraction(url, { slow, darkMode, ...extraOptions });
    if (!result.ok) return errorResult(result.error);
    return jsonResult(pick(result.data));
  };
}

// ── Shared params ──────────────────────────────────────────────────────

const url = z.string().describe("Website URL (e.g. stripe.com)");
const slow = z.boolean().optional().default(false).describe("3x timeouts for heavy SPAs");

// ── Tools ──────────────────────────────────────────────────────────────

server.tool(
  "get_design_tokens",
  "Extract the full design system from a live website. Launches a real browser, navigates to the site, and returns production-ready design tokens: color palette (hex, RGB, LCH, OKLCH) with semantic roles and CSS custom properties, typography scale (families, fallbacks, sizes, weights, line heights, letter spacing by context), spacing system with grid detection, border radii, border patterns, box shadows for elevation, component styles (buttons with hover/focus states, inputs, links, badges), responsive breakpoints, logo and favicons, site name, detected CSS frameworks, and icon systems. Takes 15-40 seconds depending on site complexity.",
  { url, slow },
  toolHandler((d) => d),
);

server.tool(
  "get_color_palette",
  "Extract brand colors from a live website. Returns semantic colors (primary, secondary, accent), full palette ranked by usage frequency and confidence (high/medium/low), CSS custom properties with their design-system names, and hover/focus state colors discovered by simulating real user interactions. Each color in hex, RGB, LCH, and OKLCH.",
  {
    url, slow,
    darkMode: z.boolean().optional().default(false).describe("Also extract dark mode palette"),
  },
  toolHandler((d) => ({ url: d.url, colors: d.colors })),
);

server.tool(
  "get_typography",
  "Extract typography from a live website. Returns every font family with its fallback stack, the complete type scale grouped by context (heading, body, button, link, caption) with pixel and rem sizes, weights, line heights, letter spacing, and text transforms. Also reports font sources: Google Fonts URLs, Adobe Fonts usage, and variable font detection.",
  { url, slow },
  toolHandler((d) => ({ url: d.url, typography: d.typography })),
);

server.tool(
  "get_component_styles",
  "Extract UI component styles from a live website. Returns button variants with default, hover, active, and focus states (background, text color, padding, border radius, border, shadow, outline, opacity), input field styles (border, focus ring, padding, placeholder), link styles (color, text decoration, hover changes), and badge/tag styles.",
  { url, slow },
  toolHandler((d) => ({ url: d.url, components: d.components })),
);

server.tool(
  "get_surfaces",
  "Extract surface treatment tokens from a live website: border radii with element context (which radii are used on buttons vs cards vs inputs vs modals), border patterns (width + style + color combinations), and box shadow elevation levels.",
  { url, slow },
  toolHandler((d) => ({
    url: d.url,
    borderRadius: d.borderRadius,
    borders: d.borders,
    shadows: d.shadows,
  })),
);

server.tool(
  "get_spacing",
  "Extract the spacing system from a live website: common margin and padding values sorted by frequency, pixel and rem values, and grid system detection (4px, 8px, or custom scale).",
  { url, slow },
  toolHandler((d) => ({ url: d.url, spacing: d.spacing })),
);

server.tool(
  "get_brand_identity",
  "Extract brand identity from a live website: site name, logo (source, dimensions, safe zone), all favicon variants (icon, apple-touch-icon, og:image, twitter:image with sizes and URLs), detected CSS frameworks (Tailwind, Bootstrap, MUI, etc.), icon systems (Font Awesome, Material Icons, SVG), and responsive breakpoints.",
  { url, slow },
  toolHandler((d) => ({
    url: d.url,
    siteName: d.siteName,
    logo: d.logo,
    favicons: d.favicons,
    frameworks: d.frameworks,
    iconSystem: d.iconSystem,
    breakpoints: d.breakpoints,
  })),
);

// ── Start ──────────────────────────────────────────────────────────────

const transport = new StdioServerTransport();
await server.connect(transport);

```

### File: package-lock.json
```json
{
  "name": "dembrandt",
  "version": "0.8.2",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "dembrandt",
      "version": "0.8.2",
      "license": "MIT",
      "dependencies": {
        "@modelcontextprotocol/sdk": "1.29.0",
        "@playwright/browser-chromium": "^1.57.0",
        "@playwright/browser-firefox": "^1.57.0",
        "chalk": "^5.3.0",
        "commander": "^11.1.0",
        "ora": "^7.0.1",
        "playwright-core": "^1.57.0",
        "zod": "4.3.6"
      },
      "bin": {
        "dembrandt": "index.js"
      },
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/@hono/node-server": {
      "version": "1.19.12",
      "resolved": "https://registry.npmjs.org/@hono/node-server/-/node-server-1.19.12.tgz",
      "integrity": "sha512-txsUW4SQ1iilgE0l9/e9VQWmELXifEFvmdA1j6WFh/aFPj99hIntrSsq/if0UWyGVkmrRPKA1wCeP+UCr1B9Uw==",
      "license": "MIT",
      "engines": {
        "node": ">=18.14.1"
      },
      "peerDependencies": {
        "hono": "^4"
      }
    },
    "node_modules/@modelcontextprotocol/sdk": {
      "version": "1.29.0",
      "resolved": "https://registry.npmjs.org/@modelcontextprotocol/sdk/-/sdk-1.29.0.tgz",
      "integrity": "sha512-zo37mZA9hJWpULgkRpowewez1y6ML5GsXJPY8FI0tBBCd77HEvza4jDqRKOXgHNn867PVGCyTdzqpz0izu5ZjQ==",
      "license": "MIT",
      "dependencies": {
        "@hono/node-server": "^1.19.9",
        "ajv": "^8.17.1",
        "ajv-formats": "^3.0.1",
        "content-type": "^1.0.5",
        "cors": "^2.8.5",
        "cross-spawn": "^7.0.5",
        "eventsource": "^3.0.2",
        "eventsource-parser": "^3.0.0",
        "express": "^5.2.1",
        "express-rate-limit": "^8.2.1",
        "hono": "^4.11.4",
        "jose": "^6.1.3",
        "json-schema-typed": "^8.0.2",
        "pkce-challenge": "^5.0.0",
        "raw-body": "^3.0.0",
        "zod": "^3.25 || ^4.0",
        "zod-to-json-schema": "^3.25.1"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "@cfworker/json-schema": "^4.1.1",
        "zod": "^3.25 || ^4.0"
      },
      "peerDependenciesMeta": {
        "@cfworker/json-schema": {
          "optional": true
        },
        "zod": {
          "optional": false
        }
      }
    },
    "node_modules/@playwright/browser-chromium": {
      "version": "1.57.0",
      "resolved": "https://registry.npmjs.org/@playwright/browser-chromium/-/browser-chromium-1.57.0.tgz",
      "integrity": "sha512-pUg+2p6HwewLp8KCD9G6VYaS2iewdkNkyqMcSIxXBXOlp1ojTxLF6/bwyR4ixLMy6tyv75jhE8PzzMZiX5KzwQ==",
      "hasInstallScript": true,
      "license": "Apache-2.0",
      "dependencies": {
        "playwright-core": "1.57.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@playwright/browser-firefox": {
      "version": "1.57.0",
      "resolved": "https://registry.npmjs.org/@playwright/browser-firefox/-/browser-firefox-1.57.0.tgz",
      "integrity": "sha512-Kb9CUiCDqm/1yQVyzcQfXvg8EqVW9YXwJJ/7nvr1ekeV2XX1n5FHrzm1rPiZV13Rk1mBeuWrBNook+HmwCTLpw==",
      "hasInstallScript": true,
      "license": "Apache-2.0",
      "dependencies": {
        "playwright-core": "1.57.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/accepts": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-2.0.0.tgz",
      "integrity": "sha512-5cvg6CtKwfgdmVqY1WIiXKc3Q1bkRqGLi+2W/6ao+6Y7gu/RCwRuAhGEzh5B4KlszSuTLgZYuqFqo5bImjNKng==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "^3.0.0",
        "negotiator": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/ajv": {
      "version": "8.18.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-8.18.0.tgz",
      "integrity": "sha512-PlXPeEWMXMZ7sPYOHqmDyCJzcfNrUr3fGNKtezX14ykXOEIvyK81d+qydx89KY5O71FKMPaQ2vBfBFI5NHR63A==",
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.3",
        "fast-uri": "^3.0.1",
        "json-schema-traverse": "^1.0.0",
        "require-from-string": "^2.0.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ajv-formats": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/ajv-formats/-/ajv-formats-3.0.1.tgz",
      "integrity": "sha512-8iUql50EUR+uUcdRQ3HDqa6EVyo3docL8g5WJ3FNcWmu62IbkGUue/pEyLBW8VGKKucTPgqeks4fIU1DA4yowQ==",
      "license": "MIT",
      "dependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependenciesMeta": {
        "ajv": {
          "optional": true
        }
      }
    },
    "node_modules/ansi-regex": {
      "version": "6.2.2",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.2.2.tgz",
      "integrity": "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==",
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/bl": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/bl/-/bl-5.1.0.tgz",
      "integrity": "sha512-tv1ZJHLfTDnXE6tMHv73YgSJaWR2AFuPwMntBe7XL/GBFHnT0CLnsHMogfk5+GzCDC5ZWarSCYaIGATZt9dNsQ==",
      "license": "MIT",
      "dependencies": {
        "buffer": "^6.0.3",
        "inherits": "^2.0.4",
        "readable-stream": "^3.4.0"
      }
    },
    "node_modules/body-parser": {
      "version": "2.2.2",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-2.2.2.tgz",
      "integrity": "sha512-oP5VkATKlNwcgvxi0vM0p/D3n2C3EReYVX+DNYs5TjZFn/oQt2j+4sVJtSMr18pdRr8wjTcBl6LoV+FUwzPmNA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "^3.1.2",
        "content-type": "^1.0.5",
        "debug": "^4.4.3",
        "http-errors": "^2.0.0",
        "iconv-lite": "^0.7.0",
        "on-finished": "^2.4.1",
        "qs": "^6.14.1",
        "raw-body": "^3.0.1",
        "type-is": "^2.0.1"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/buffer": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-6.0.3.tgz",
      "integrity": "sha512-FTiCpNxtwiZZHEZbcbTIcZjERVICn9yq/pDFkTl95/AxzD1naBctN7YO68riM/gLSDY7sdrMby8hofADYuuqOA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.2.1"
      }
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/chalk": {
      "version": "5.6.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.6.2.tgz",
      "integrity": "sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==",
      "license": "MIT",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/cli-cursor": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/cli-cursor/-/cli-cursor-4.0.0.tgz",
      "integrity": "sha512-VGtlMu3x/4DOtIUwEkRezxUZ2lBacNJCHash0N0WeZDBS+7Ux1dm3XWAgWYxLJFMMdOeXMHXorshEFhbMSGelg==",
      "license": "MIT",
      "dependencies": {
        "restore-cursor": "^4.0.0"
      },
      "engines": {
        "node": "^12.20.0 || ^14.13.1 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/commander": {
      "version": "11.1.0",
      "resolved": "https://registry.npmjs.org/commander/-/commander-11.1.0.tgz",
      "integrity": "sha512-yPVavfyCcRhmorC7rWlkHn15b4wDVgVmBA7kV4QVBsF7kv/9TKJAbAXVTxvTnwP8HHKjRCJDClKbciiYS7p0DQ==",
      "license": "MIT",
      "engines": {
        "node": ">=16"
      }
    },
    "node_modules/content-disposition": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-1.0.1.tgz",
      "integrity": "sha512-oIXISMynqSqm241k6kcQ5UwttDILMK4BiurCfGEREw6+X9jkkpEe5T9FZaApyLGGOnFuyMWZpdolTXMtvEJ08Q==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.2.2.tgz",
      "integrity": "sha512-D76uU73ulSXrD1UXF4KE2TMxVVwhsnCgfAyTg9k8P6KGZjlXKrOLe4dJQKI3Bxi5wjesZoFXJWElNWBjPZMbhg==",
      "license": "MIT",
      "engines": {
        "node": ">=6.6.0"
      }
    },
    "node_modules/cors": {
      "version": "2.8.6",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.6.tgz",
      "integrity": "sha512-tJtZBBHA6vjIAaF6EnIaq6laBBP9aq/Y3ouVJjEfoHbRBcHBAHYcMh/w8LDrk2PvIMMq8gmopa5D4V8RmbrxGw==",
      "license": "MIT",
      "dependencies": {
        "object-assign": "^4",
        "vary": "^1"
      },
      "engines": {
        "node": ">= 0.10"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/eastasianwidth": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/eastasianwidth/-/eastasianwidth-0.2.0.tgz",
      "integrity": "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==",
      "license": "MIT"
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
