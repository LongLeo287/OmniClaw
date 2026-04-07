---
id: cli
type: knowledge
owner: OA_Triage
---
# cli
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "firecrawl-cli",
  "version": "1.12.2",
  "description": "Command-line interface for Firecrawl. Scrape, crawl, and extract data from any website directly from your terminal.",
  "main": "dist/index.js",
  "bin": {
    "firecrawl": "dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "start": "node dist/index.js",
    "local": "node dist/index.js",
    "clean": "rm -rf dist",
    "prepublishOnly": "pnpm run build",
    "prepare": "husky",
    "format": "prettier --write \"src/**/*.{ts,json}\" \"*.{json,md}\"",
    "format:check": "prettier --check \"src/**/*.{ts,json}\" \"*.{json,md}\"",
    "type-check": "tsc --noEmit",
    "test:watch": "vitest",
    "test": "vitest run",
    "publish-beta": "npm publish --tag beta",
    "publish-prod": "npm publish --access public",
    "build:binary": "bash scripts/build-binaries.sh",
    "build:binary:darwin": "bash scripts/build-binaries.sh darwin",
    "build:binary:linux": "bash scripts/build-binaries.sh linux",
    "build:binary:windows": "bash scripts/build-binaries.sh windows"
  },
  "lint-staged": {
    "*.{ts,json,md}": [
      "prettier --write"
    ]
  },
  "keywords": [
    "firecrawl",
    "cli",
    "web-scraping",
    "crawler",
    "scraper",
    "data-extraction",
    "llm",
    "markdown",
    "search",
    "web search",
    "skill"
  ],
  "author": "Firecrawl",
  "license": "ISC",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/firecrawl/cli.git"
  },
  "bugs": {
    "url": "https://github.com/firecrawl/cli/issues"
  },
  "homepage": "https://docs.firecrawl.dev/cli",
  "engines": {
    "node": ">=18.0.0"
  },
  "files": [
    "dist",
    "README.md"
  ],
  "packageManager": "pnpm@10.12.1",
  "devDependencies": {
    "@types/node": "^20.0.0",
    "husky": "^9.0.0",
    "lint-staged": "^15.0.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0",
    "vitest": "^4.0.0"
  },
  "dependencies": {
    "@inquirer/prompts": "^8.2.1",
    "@mendable/firecrawl-js": "4.17.0",
    "commander": "^14.0.2"
  }
}

```

### File: README.md
```md
# 🔥 Firecrawl CLI

Command-line interface for Firecrawl. Scrape, crawl, and extract data from any website directly from your terminal.

## Installation

```bash
npm install -g firecrawl-cli
```

Or set up everything in one command (install CLI globally, authenticate, and add skills across all detected coding editors):

```bash
npx -y firecrawl-cli@latest init -y --browser
```

- `-y` runs setup non-interactively
- `--browser` opens the browser for Firecrawl authentication automatically
- skills install globally to every detected AI coding agent by default

### Setup Skills and MCP

If you are using an AI coding agent like Claude Code, you can also install the skill individually with:

```bash
firecrawl setup skills
```

This installs skills globally across all detected coding editors by default. Use `--agent <agent>` to scope it to one editor.

To install the Firecrawl MCP server into your editors (Cursor, Claude Code, VS Code, etc.):

```bash
firecrawl setup mcp
```

Or directly via npx:

```bash
npx skills add firecrawl/cli --full-depth --global --all
npx add-mcp "npx -y firecrawl-mcp" --name firecrawl
```

## Quick Start

Just run a command - the CLI will prompt you to authenticate if needed:

```bash
firecrawl https://example.com
```

## Authentication

On first run, you'll be prompted to authenticate:

```
  🔥 firecrawl cli
  Turn websites into LLM-ready data

Welcome! To get started, authenticate with your Firecrawl account.

  1. Login with browser (recommended)
  2. Enter API key manually

Tip: You can also set FIRECRAWL_API_KEY environment variable

Enter choice [1/2]:
```

### Authentication Methods

```bash
# Interactive (prompts automatically when needed)
firecrawl

# Browser login
firecrawl login

# Direct API key
firecrawl login --api-key fc-your-api-key

# Environment variable
export FIRECRAWL_API_KEY=fc-your-api-key

# Per-command API key
firecrawl scrape https://example.com --api-key fc-your-api-key
```

### Self-hosted / Local Development

For self-hosted Firecrawl instances or local development, use the `--api-url` option:

```bash
# Use a local Firecrawl instance (no API key required)
firecrawl --api-url http://localhost:3002 scrape https://example.com

# Or set via environment variable
export FIRECRAWL_API_URL=http://localhost:3002
firecrawl scrape https://example.com

# Self-hosted with API key
firecrawl --api-url https://firecrawl.mycompany.com --api-key fc-xxx scrape https://example.com
```

When using a custom API URL (anything other than `https://api.firecrawl.dev`), authentication is automatically skipped, allowing you to use local instances without an API key.

---

## Commands

### `scrape` - Scrape URLs

Extract content from any webpage. Pass multiple URLs to scrape them concurrently -- each result is saved to `.firecrawl/` automatically.

```bash
# Basic usage (outputs markdown)
firecrawl https://example.com
firecrawl scrape https://example.com

# Get raw HTML
firecrawl https://example.com --html
firecrawl https://example.com -H

# Multiple formats (outputs JSON)
firecrawl https://example.com --format markdown,links,images

# Save to file
firecrawl https://example.com -o output.md
firecrawl https://example.com --format json -o data.json --pretty

# Multiple URLs (scraped concurrently, each saved to .firecrawl/)
firecrawl scrape https://firecrawl.dev https://firecrawl.dev/blog https://docs.firecrawl.dev
```

#### Scrape Options

| Option                     | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| `-f, --format <formats>`   | Output format(s), comma-separated                       |
| `-H, --html`               | Shortcut for `--format html`                            |
| `-S, --summary`            | Shortcut for `--format summary`                         |
| `--only-main-content`      | Extract only main content (removes navs, footers, etc.) |
| `--wait-for <ms>`          | Wait time before scraping (for JS-rendered content)     |
| `--screenshot`             | Take a screenshot                                       |
| `--full-page-screenshot`   | Take a full page screenshot                             |
| `--include-tags <tags>`    | Only include specific HTML tags                         |
| `--exclude-tags <tags>`    | Exclude specific HTML tags                              |
| `--max-age <milliseconds>` | Maximum age of cached content in milliseconds           |
| `-o, --output <path>`      | Save output to file                                     |
| `--json`                   | Output as JSON format                                   |
| `--pretty`                 | Pretty print JSON output                                |
| `--timing`                 | Show request timing info                                |

#### Available Formats

| Format           | Description                  |
| ---------------- | ---------------------------- |
| `markdown`       | Clean markdown (default)     |
| `html`           | Cleaned HTML                 |
| `rawHtml`        | Original HTML                |
| `links`          | All links on the page        |
| `images`         | All images on the page       |
| `screenshot`     | Screenshot as base64         |
| `summary`        | AI-generated summary         |
| `json`           | Structured JSON extraction   |
| `changeTracking` | Track changes on the page    |
| `attributes`     | Page attributes and metadata |
| `branding`       | Brand identity extraction    |

#### Examples

```bash
# Extract only main content as markdown
firecrawl https://blog.example.com --only-main-content

# Wait for JS to render, then scrape
firecrawl https://spa-app.com --wait-for 3000

# Get all links from a page
firecrawl https://example.com --format links

# Screenshot + markdown
firecrawl https://example.com --format markdown --screenshot

# Extract specific elements only
firecrawl https://example.com --include-tags article,main

# Exclude navigation and ads
firecrawl https://example.com --exclude-tags nav,aside,.ad
```

---

### `search` - Search the web

Search the web and optionally scrape content from search results.

```bash
# Basic search
firecrawl search "firecrawl web scraping"

# Limit results
firecrawl search "AI news" --limit 10

# Search news sources
firecrawl search "tech startups" --sources news

# Search images
firecrawl search "landscape photography" --sources images

# Multiple sources
firecrawl search "machine learning" --sources web,news,images

# Filter by category (GitHub, research papers, PDFs)
firecrawl search "web scraping python" --categories github
firecrawl search "transformer architecture" --categories research
firecrawl search "machine learning" --categories github,research

# Time-based search
firecrawl search "AI announcements" --tbs qdr:d   # Past day
firecrawl search "tech news" --tbs qdr:w          # Past week

# Location-based search
firecrawl search "restaurants" --location "San Francisco,California,United States"
firecrawl search "local news" --country DE

# Search and scrape results
firecrawl search "firecrawl tutorials" --scrape
firecrawl search "API documentation" --scrape --scrape-formats markdown,links

# Output as pretty JSON
firecrawl search "web scraping"
```

#### Search Options

| Option                       | Description                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| `--limit <n>`                | Maximum results (default: 5, max: 100)                                                      |
| `--sources <sources>`        | Comma-separated: `web`, `images`, `news` (default: web)                                     |
| `--categories <categories>`  | Comma-separated: `github`, `research`, `pdf`                                                |
| `--tbs <value>`              | Time filter: `qdr:h` (hour), `qdr:d` (day), `qdr:w` (week), `qdr:m` (month), `qdr:y` (year) |
| `--location <location>`      | Geo-targeting (e.g., "Germany", "San Francisco,California,United States")                   |
| `--country <code>`           | ISO country code (default: US)                                                              |
| `--timeout <ms>`             | Timeout in milliseconds (default: 60000)                                                    |
| `--ignore-invalid-urls`      | Exclude URLs invalid for other Firecrawl endpoints                                          |
| `--scrape`                   | Enable scraping of search results                                                           |
| `--scrape-formats <formats>` | Scrape formats when `--scrape` enabled (default: markdown)                                  |
| `--only-main-content`        | Include only main content when scraping (default: true)                                     |
| `-o, --output <path>`        | Save to file                                                                                |
| `--json`                     | Output as compact JSON                                                                      |

#### Examples

```bash
# Research a topic with recent results
firecrawl search "React Server Components" --tbs qdr:m --limit 10

# Find GitHub repositories
firecrawl search "web scraping library" --categories github --limit 20

# Search and get full content
firecrawl search "firecrawl documentation" --scrape --scrape-formats markdown --json -o results.json

# Find research papers
firecrawl search "large language models" --categories research --json

# Search with location targeting
firecrawl search "best coffee shops" --location "Berlin,Germany" --country DE

# Get news from the past week
firecrawl search "AI startups funding" --sources news --tbs qdr:w --limit 15
```

---

### `map` - Discover all URLs on a website

Quickly discover all URLs on a website without scraping content.

```bash
# List all URLs (one per line)
firecrawl map https://example.com

# Output as JSON
firecrawl map https://example.com --json

# Search for specific URLs
firecrawl map https://example.com --search "blog"

# Limit results
firecrawl map https://example.com --limit 500
```

#### Map Options

| Option                      | Description                       |
| --------------------------- | --------------------------------- |
| `--limit <n>`               | Maximum URLs to discover          |
| `--search <query>`          | Filter URLs by search query       |
| `--sitemap <mode>`          | `include`, `skip`, or `only`      |
| `--include-subdomains`      | Include subdomains                |
| `--ignore-query-parameters` | Dedupe URLs with different params |
| `--timeout <seconds>`       | Request timeout                   |
| `--json`                    | Output as JSON                    |
| `-o, --output <path>`       | Save to file                      |

#### Examples

```bash
# Find all product pages
firecrawl map https://shop.example.com --search "product"

# Get sitemap URLs only
firecrawl map https://example.com --sitemap only

# Save URL list to file
firecrawl map https://example.com -o urls.txt

# Include subdomains
firecrawl map https://example.com --include-subdomains --limit 1000
```

---

### `crawl` - Crawl an entire website

Crawl multiple pages from a website.

```bash
# Start a crawl (returns job ID)
firecrawl crawl https://example.com

# Wait for crawl to complete
firecrawl crawl https://example.com --wait

# With progress indicator
firecrawl crawl https://example.com --wait --progress

# Check crawl status
firecrawl crawl <job-id>

# Limit pages
firecrawl crawl https://example.com --limit 100 --max-depth 3
```

#### Crawl Options

| Option                      | Description                              |
| --------------------------- | ---------------------------------------- |
| `--wait`                    | Wait for crawl to complete               |
| `--progress`                | Show progress while waiting              |
| `--limit <n>`               | Maximum pages to crawl                   |
| `--max-depth <n>`           | Maximum crawl depth                      |
| `--include-paths <paths>`   | Only crawl matching paths                |
| `--exclude-paths <paths>`   | Skip matching paths                      |
| `--sitemap <mode>`          | `include`, `skip`, or `only`             |
| `--allow-subdomains`        | Include subdomains                       |
| `--allow-external-links`    | Follow external links                    |
| `--crawl-entire-domain`     | Crawl entire domain                      |
| `--ignore-query-parameters` | Treat URLs with different params as same |
| `--delay <ms>`              | Delay between requests                   |
| `--max-concurrency <n>`     | Max concurrent requests                  |
| `--timeout <seconds>`       | Timeout when waiting                     |
| `--poll-interval <seconds>` | Status check interval                    |

#### Examples

```bash
# Crawl blog section only
firecrawl crawl https://example.com --include-paths /blog,/posts

# Exclude admin pages
firecrawl crawl https://example.com --exclude-paths /admin,/login

# Crawl with rate limiting
firecrawl crawl https://example.com --delay 1000 --max-concurrency 2

# Deep crawl with high limit
firecrawl crawl https://example.com --limit 1000 --max-depth 10 --wait --progress

# Save results
firecrawl crawl https://example.com --wait -o crawl-results.json --pretty
```

---

### `credit-usage` - Check your credits

```bash
# Show credit usage
firecrawl credit-usage

# Output as JSON
firecrawl credit-usage --json --pretty
```

---

### `agent` - AI-powered web data extraction

Run an AI agent that autonomously browses and extracts structured data from the web based on natural language prompts.

> **Note:** Agent tasks typically take **2 to 5 minutes** to complete, and sometimes longer for complex extractions. Use sparingly and consider `--max-credits` to limit costs.

```bash
# Basic usage (returns job ID immediately)
firecrawl agent "Find the pricing plans for Firecrawl"

# Wait for completion
firecrawl agent "Extract all product names and prices from this store" --wait

# Focus on specific URLs
firecrawl agent "Get the main features listed" --urls https://example.com/features

# Use structured output with JSON schema
firecrawl agent "Extract company info" --schema '{"type":"object","properties":{"name":{"type":"string"},"employees":{"type":"number"}}}'

# Load schema from file
firecrawl agent "Extract product data" --schema-file ./product-schema.json --wait

# Check status of an existing job
firecrawl agent <job-id>
firecrawl agent <job-id> --wait
```

#### Agent Options

| Option                      | Description                                                   |
| --------------------------- | -------------------------------------------------------
... [TRUNCATED]
```

### File: docs\README.md
```md
This folder is used for documentation related to developing `gh`. Docs for `gh` installation and usage are available at [https://cli.github.com/manual](https://cli.github.com/manual).
```

### File: src\__tests__\README.md
```md
# Testing Guide

This directory contains tests for the Firecrawl CLI commands. Tests use Vitest and mock the Firecrawl client to avoid making real API calls.

## Running Tests

```bash
# Run tests once
pnpm test:run

# Run tests in watch mode
pnpm test:watch

# Run tests with UI
pnpm test:ui
```

## Test Structure

- `commands/` - Tests for command implementations
- `utils/` - Test utilities and helpers

## Writing Tests

### Key Principles

1. **No Real API Calls**: All tests mock the Firecrawl client or fetch API
2. **Verify API Call Generation**: Tests ensure commands generate correct API call parameters
3. **Verify Response Handling**: Tests ensure commands properly handle success and error responses
4. **Type Safety**: TypeScript ensures type correctness

### Example Test Pattern

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { executeScrape } from '../../commands/scrape';
import { getClient } from '../../utils/client';
import { setupTest, teardownTest } from '../utils/mock-client';

// Mock the client module
vi.mock('../../utils/client', async () => {
  const actual = await vi.importActual('../../utils/client');
  return {
    ...actual,
    getClient: vi.fn(),
  };
});

describe('executeScrape', () => {
  let mockClient: any;

  beforeEach(() => {
    setupTest();
    mockClient = { scrape: vi.fn() };
    vi.mocked(getClient).mockReturnValue(mockClient);
  });

  it('should call scrape with correct parameters', async () => {
    mockClient.scrape.mockResolvedValue({ markdown: '# Test' });

    await executeScrape({ url: 'https://example.com' });

    expect(mockClient.scrape).toHaveBeenCalledWith('https://example.com', {
      formats: ['markdown'],
    });
  });
});
```

## Test Utilities

### `setupTest()` / `teardownTest()`

Resets client and config state between tests. Always use these in `beforeEach`/`afterEach`.

### Mocking Patterns

- **Client methods**: Mock `getClient()` to return a mock client with stubbed methods
- **Fetch API**: Mock `global.fetch` for commands that use fetch directly
- **Config**: Use `initializeConfig()` to set test configuration

## What to Test

1. **API Call Parameters**: Verify commands pass correct parameters to the client
2. **Response Handling**: Test success and error response handling
3. **Option Parsing**: Ensure CLI options are correctly converted to API parameters
4. **Edge Cases**: Test with missing/optional parameters, null values, etc.

```

### File: .claude-plugin_DISTILLED.md
```md
---
id: .claude-plugin
type: distilled_knowledge
---
# .claude-plugin

## SWALLOW ENGINE DISTILLATION

### File: marketplace.json
```json
{
  "name": "firecrawl",
  "owner": {
    "name": "Firecrawl"
  },
  "plugins": [
    {
      "name": "firecrawl",
      "source": "./",
      "description": "Scrape, search, crawl, and map the web with a single command.",
      "skills": ["./skills/firecrawl-cli"]
    }
  ]
}
```

### File: plugin.json
```json
{
    "name": "firecrawl",
    "description": "Scrape, search, crawl, and map the web with a single command.",
    "version": "1.0.8",
    "author": {
        "name": "Firecrawl"
    },
    "skills": ["./skills/firecrawl-cli"]
}
```


```

### File: .devcontainer_DISTILLED.md
```md
---
id: .devcontainer
type: distilled_knowledge
---
# .devcontainer

## SWALLOW ENGINE DISTILLATION

### File: devcontainer.json
```json
{
	"image": "mcr.microsoft.com/devcontainers/go:1.25",
	"features": {
		"ghcr.io/devcontainers/features/sshd:1": {}
	},
	"remoteUser": "vscode",
	"customizations": {
		"vscode": {
			"extensions": [
				"golang.go"
			],
			"settings": {
				"go.toolsManagement.checkForUpdates": "local",
				"go.useLanguageServer": true,
				"go.gopath": "/go"
			}
		}
	},
	"runArgs": [
		"--cap-add=SYS_PTRACE",
		"--security-opt",
		"seccomp=unconfined"
	]
}

```


```

### File: .prettierrc.json
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}

```

### File: AGENTS.md
```md
# AGENTS.md

This is the GitHub CLI (`gh`), a command-line tool for interacting with GitHub. The module path is `github.com/cli/cli/v2`.

## Build, Test, and Lint

```bash
make                                       # Build (Unix) — outputs bin/gh
go run script/build.go                     # Build (Windows)
go test ./...                              # All unit tests
go test ./pkg/cmd/issue/list/... -run TestIssueList_nontty  # Single test
go test -tags acceptance ./acceptance      # Acceptance tests
make lint                                  # golangci-lint (same as CI)
```

**Before committing, ensure both tests and linter pass:**
```bash
go test ./...
make lint
```

## Architecture

Entry point: `cmd/gh/main.go` → `internal/ghcmd.Main()` → `pkg/cmd/root.NewCmdRoot()`.

Key packages:
- `pkg/cmd/<command>/<subcommand>/` — CLI command implementations
- `pkg/cmdutil/` — Factory, error types, flag helpers (`NilStringFlag`, `NilBoolFlag`, `StringEnumFlag`)
- `pkg/iostreams/` — I/O abstraction with TTY detection, color, pager
- `pkg/httpmock/` — HTTP mocking for tests
- `api/` — GitHub API client (GraphQL + REST)
- `internal/featuredetection/` — GitHub.com vs GHES capability detection
- `internal/tableprinter/` — Table output for list commands

## Command Structure

A command `gh foo bar` lives in `pkg/cmd/foo/bar/` with `bar.go`, `bar_test.go`, and optionally `http.go`/`http_test.go`.

### Canonical Examples

- **Command + tests**: `pkg/cmd/issue/list/list.go` and `list_test.go`
- **Factory wiring**: `pkg/cmd/factory/default.go`
- **Unit tests**: `internal/agents/detect_test.go`

### The Options + Factory Pattern

Every command follows this structure (see `pkg/cmd/issue/list/list.go`):

1. `Options` struct with `IO`, `HttpClient`, `Config`, `BaseRepo` + flags
2. `NewCmdFoo(f *cmdutil.Factory, runF func(*FooOptions) error)` constructor — `runF` is the test injection point
3. Separate `fooRun(opts)` function with the business logic

Key rules:
- Lazy-init `BaseRepo`, `Remotes`, `Branch` inside `RunE`, not the constructor
- Commands register in `pkg/cmd/root/root.go`; subcommand groups use `cmdutil.AddGroup()`

### Command Examples and Help Text

Use `heredoc.Doc` for examples with `#` comment lines and `$ ` command prefixes:
```go
Example: heredoc.Doc(`
    # Do the thing
    $ gh foo bar --flag value
`),
```

### JSON Output

Add `--json`, `--jq`, `--template` flags via `cmdutil.AddJSONFlags(cmd, &opts.Exporter, fieldNames)`. In the run function: `if opts.Exporter != nil { return opts.Exporter.Write(opts.IO, data) }`. See `pkg/cmd/pr/list/list.go`.

## Testing

### HTTP Mocking

Use `httpmock.Registry` with `defer reg.Verify(t)` to ensure all stubs are called:

```go
reg := &httpmock.Registry{}
defer reg.Verify(t)

reg.Register(
    httpmock.REST("GET", "repos/OWNER/REPO"),
    httpmock.JSONResponse(someData),
)
reg.Register(
    httpmock.GraphQL(`query PullRequestList\b`),
    httpmock.FileResponse("./fixtures/prList.json"),
)
client := &http.Client{Transport: reg}
```

Common: `REST(method, path)`, `GraphQL(pattern)`, `JSONResponse(body)`, `FileResponse(path)`. See `pkg/httpmock/` for all matchers/responders.

### IOStreams in Tests

```go
ios, stdin, stdout, stderr := iostreams.Test()
ios.SetStdoutTTY(true)  // simulate terminal
```

### Assertions

Use `testify`. Always use `require` (not `assert`) for error checks so the test halts immediately:

```go
require.NoError(t, err)
require.Error(t, err)
assert.Equal(t, "expected", actual)
```

### Generated Mocks

Interfaces use `moq`: `//go:generate moq -rm -out prompter_mock.go . Prompter`. Run `go generate ./...` after interface changes.

### Table-Driven Tests

Use table-driven tests for functions with multiple input/output scenarios. See `internal/agents/detect_test.go` or `pkg/cmd/issue/list/list_test.go` for examples:

```go
tests := []struct {
    name      string
    // inputs and expected outputs
}{
    {name: "descriptive case name", ...},
}
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        // arrange, act, assert
    })
}
```

## Code Style

- Add godoc comments to all exported functions, types, and constants
- Avoid unnecessary code comments — only comment when the *why* isn't obvious from the code
- Do not comment just to restate what the code does

## Error Handling

Error types in `pkg/cmdutil/errors.go`:
- `FlagErrorf(...)` — flag validation (prints usage)
- `cmdutil.SilentError` — exit 1, no message
- `cmdutil.CancelError` — user cancelled
- `cmdutil.PendingError` — outcome pending
- `cmdutil.NoResultsError` — empty results

Use `cmdutil.MutuallyExclusive("message", cond1, cond2)` for mutually exclusive flags.

## Feature Detection

Commands using feature detection must include a `// TODO <cleanupIdentifier>` comment directly above the if-statement for linter compliance:

```go
// TODO someFeatureCleanup
if features.SomeCapability {
    // use new API
} else {
    // fallback for older GHES
}
```

## API Patterns

```go
client := api.NewClientFromHTTP(httpClient)
client.GraphQL(hostname, query, variables, &data)
client.REST(hostname, "GET", "repos/owner/repo", nil, &data)
```

For host resolution, use `cfg.Authentication().DefaultHost()` — not `ghinstance.Default()` which always returns `github.com`.
```

### File: api_DISTILLED.md
```md
---
id: api
type: distilled_knowledge
---
# api

## SWALLOW ENGINE DISTILLATION

### File: client.go
```go
package api

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"regexp"
	"strings"

	ghAPI "github.com/cli/go-gh/v2/pkg/api"
	ghauth "github.com/cli/go-gh/v2/pkg/auth"
)

const (
	apiVersion      = "X-GitHub-Api-Version"
	apiVersionValue = "2022-11-28"
	authorization   = "Authorization"
	cacheTTL        = "X-GH-CACHE-TTL"
	graphqlFeatures = "GraphQL-Features"
	features        = "merge_queue"
	userAgent       = "User-Agent"
)

var linkRE = regexp.MustCompile(`<([^>]+)>;\s*rel="([^"]+)"`)

func NewClientFromHTTP(httpClient *http.Client) *Client {
	client := &Client{http: httpClient}
	return client
}

type Client struct {
	http *http.Client
}

func (c *Client) HTTP() *http.Client {
	return c.http
}

type GraphQLError struct {
	*ghAPI.GraphQLError
}

type HTTPError struct {
	*ghAPI.HTTPError
	scopesSuggestion string
}

func (err HTTPError) ScopesSuggestion() string {
	return err.scopesSuggestion
}

// GraphQL performs a GraphQL request using the query string and parses the response into data receiver. If there are errors in the response,
// GraphQLError will be returned, but the receiver will also be partially populated.
func (c Client) GraphQL(hostname string, query string, variables map[string]interface{}, data interface{}) error {
	opts := clientOptions(hostname, c.http.Transport)
	opts.Headers[graphqlFeatures] = features
	gqlClient, err := ghAPI.NewGraphQLClient(opts)
	if err != nil {
		return err
	}
	return handleResponse(gqlClient.Do(query, variables, data))
}

// Mutate performs a GraphQL mutation based on a struct and parses the response with the same struct as the receiver. If there are errors in the response,
// GraphQLError will be returned, but the receiver will also be partially populated.
func (c Client) Mutate(hostname, name string, mutation interface{}, variables map[string]interface{}) error {
	opts := clientOptions(hostname, c.http.Transport)
	opts.Headers[graphqlFeatures] = features
	gqlClient, err := ghAPI.NewGraphQLClient(opts)
	if err != nil {
		return err
	}
	return handleResponse(gqlClient.Mutate(name, mutation, variables))
}

// Query performs a GraphQL query based on a struct and parses the response with the same struct as the receiver. If there are errors in the response,
// GraphQLError will be returned, but the receiver will also be partially populated.
func (c Client) Query(hostname, name string, query interface{}, variables map[string]interface{}) error {
	opts := clientOptions(hostname, c.http.Transport)
	opts.Headers[graphqlFeatures] = features
	gqlClient, err := ghAPI.NewGraphQLClient(opts)
	if err != nil {
		return err
	}
	return handleResponse(gqlClient.Query(name, query, variables))
}

// QueryWithContext performs a GraphQL query based on a struct and parses the response with the same struct as the receiver. If there are errors in the response,
// GraphQLError will be returned, but the receiver will also be partially populated.
func (c Client) QueryWithContext(ctx context.Context, hostname, name string, query interface{}, variables map[string]interface{}) error {
	opts := clientOptions(hostname, c.http.Transport)
	opts.Headers[graphqlFeatures] = features
	gqlClient, err := ghAPI.NewGraphQLClient(opts)
	if err != nil {
		return err
	}
	return handleResponse(gqlClient.QueryWithContext(ctx, name, query, variables))
}

// REST performs a REST request and parses the response.
func (c Client) REST(hostname string, method string, p string, body io.Reader, data interface{}) error {
	opts := clientOptions(hostname, c.http.Transport)
	restClient, err := ghAPI.NewRESTClient(opts)
	if err != nil {
		return err
	}
	return handleResponse(restClient.Do(method, p, body, data))
}

func (c Client) RESTWithNext(hostname string, method string, p string, body io.Reader, data interface{}) (string, error) {
	opts := clientOptions(hostname, c.http.Transport)
	restClient, err := ghAPI.NewRESTClient(opts)
	if err != nil {
		return "", err
	}

	resp, err := restClient.Request(method, p, body)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	success := resp.StatusCode >= 200 && resp.StatusCode < 300
	if !success {
		return "", HandleHTTPError(resp)
	}

	if resp.StatusCode == http.StatusNoContent {
		return "", nil
	}

	b, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	err = json.Unmarshal(b, &data)
	if err != nil {
		return "", err
	}

	var next string
	for _, m := range linkRE.FindAllStringSubmatch(resp.Header.Get("Link"), -1) {
		if len(m) > 2 && m[2] == "next" {
			next = m[1]
		}
	}

	return next, nil
}

// HandleHTTPError parses a http.Response into a HTTPError.
//
// The caller is responsible to close the response body stream.
func HandleHTTPError(resp *http.Response) error {
	return handleResponse(ghAPI.HandleHTTPError(resp))
}

// handleResponse takes a ghAPI.HTTPError or ghAPI.GraphQLError and converts it into an
// HTTPError or GraphQLError respectively.
func handleResponse(err error) error {
	if err == nil {
		return nil
	}

	var restErr *ghAPI.HTTPError
	if errors.As(err, &restErr) {
		return HTTPError{
			HTTPError: restErr,
			scopesSuggestion: generateScopesSuggestion(restErr.StatusCode,
				restErr.Headers.Get("X-Accepted-Oauth-Scopes"),
				restErr.Headers.Get("X-Oauth-Scopes"),
				restErr.RequestURL.Hostname()),
		}
	}

	var gqlErr *ghAPI.GraphQLError
	if errors.As(err, &gqlErr) {
		return GraphQLError{
			GraphQLError: gqlErr,
		}
	}

	return err
}

// ScopesSuggestion is an error messaging utility that prints the suggestion to request additional OAuth
// scopes in case a server response indicates that there are missing scopes.
func ScopesSuggestion(resp *http.Response) string {
	return generateScopesSuggestion(resp.StatusCode,
		resp.Header.Get("X-Accepted-Oauth-Scopes"),
		resp.Header.Get("X-Oauth-Scopes"),
		resp.Request.URL.Hostname())
}

// EndpointNeedsScopes adds additional OAuth scopes to an HTTP response as if they were returned from the
// server endpoint. This improves HTTP 4xx error messaging for endpoints that don't explicitly list the
// OAuth scopes they need.
func EndpointNeedsScopes(resp *http.Response, s string) {
	if resp.StatusCode >= 400 && resp.StatusCode < 500 {
		oldScopes := resp.Header.Get("X-Accepted-Oauth-Scopes")
		resp.Header.Set("X-Accepted-Oauth-Scopes", fmt.Sprintf("%s, %s", oldScopes, s))
	}
}

func generateScopesSuggestion(statusCode int, endpointNeedsScopes, tokenHasScopes, hostname string) string {
	if statusCode < 400 || statusCode > 499 || statusCode == 422 {
		return ""
	}

	if tokenHasScopes == "" {
		return ""
	}

	gotScopes := map[string]struct{}{}
	for _, s := range strings.Split(tokenHasScopes, ",") {
		s = strings.TrimSpace(s)
		gotScopes[s] = struct{}{}

		// Certain scopes may be grouped under a single "top-level" scope. The following branch
		// statements include these grouped/implied scopes when the top-level scope is encountered.
		// See https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps.
		if s == "repo" {
			gotScopes["repo:status"] = struct{}{}
			gotScopes["repo_deployment"] = struct{}{}
			gotScopes["public_repo"] = struct{}{}
			gotScopes["repo:invite"] = struct{}{}
			gotScopes["security_events"] = struct{}{}
		} else if s == "user" {
			gotScopes["read:user"] = struct{}{}
			gotScopes["user:email"] = struct{}{}
			gotScopes["user:follow"] = struct{}{}
		} else if s == "codespace" {
			gotScopes["codespace:secrets"] = struct{}{}
		} else if strings.HasPrefix(s, "admin:") {
			gotScopes["read:"+strings.TrimPrefix(s, "admin:")] = struct{}{}
			gotScopes["write:"+strings.TrimPrefix(s, "admin:")] = struct{}{}
		} else if strings.HasPrefix(s, "write:") {
			gotScopes["read:"+strings.TrimPrefix(s, "write:")] = struct{}{}
		}
	}

	for _, s := range strings.Split(endpointNeedsScopes, ",") {
		s = strings.TrimSpace(s)
		if _, gotScope := gotScopes[s]; s == "" || gotScope {
			continue
		}
		return fmt.Sprintf(
			"This API operation needs the %[1]q scope. To request it, run:  gh auth refresh -h %[2]s -s %[1]s",
			s,
			ghauth.NormalizeHostname(hostname),
		)
	}

	return ""
}

func clientOptions(hostname string, transport http.RoundTripper) ghAPI.ClientOptions {
	// AuthToken, and Headers are being handled by transport,
	// so let go-gh know that it does not need to resolve them.
	opts := ghAPI.ClientOptions{
		AuthToken: "none",
		Headers: map[string]string{
			authorization: "",
			apiVersion:    apiVersionValue,
		},
		Host:               hostname,
		SkipDefaultHeaders: true,
		Transport:          transport,
		LogIgnoreEnv:       true,
	}
	return opts
}

```

### File: client_test.go
```go
package api

import (
	"bytes"
	"errors"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/cli/cli/v2/pkg/httpmock"
	"github.com/cli/cli/v2/pkg/iostreams"
	"github.com/stretchr/testify/assert"
)

func newTestClient(reg *httpmock.Registry) *Client {
	client := &http.Client{}
	httpmock.ReplaceTripper(client, reg)
	return NewClientFromHTTP(client)
}

func TestGraphQL(t *testing.T) {
	http := &httpmock.Registry{}
	client := newTestClient(http)

	vars := map[string]interface{}{"name": "Mona"}
	response := struct {
		Viewer struct {
			Login string
		}
	}{}

	http.Register(
		httpmock.GraphQL("QUERY"),
		httpmock.StringResponse(`{"data":{"viewer":{"login":"hubot"}}}`),
	)

	err := client.GraphQL("github.com", "QUERY", vars, &response)
	assert.NoError(t, err)
	assert.Equal(t, "hubot", response.Viewer.Login)

	req := http.Requests[0]
	reqBody, _ := io.ReadAll(req.Body)
	assert.Equal(t, `{"query":"QUERY","variables":{"name":"Mona"}}`, string(reqBody))
}

func TestGraphQLError(t *testing.T) {
	reg := &httpmock.Registry{}
	client := newTestClient(reg)

	response := struct{}{}

	reg.Register(
		httpmock.GraphQL(""),
		httpmock.StringResponse(`
			{ "errors": [
				{
					"type": "NOT_FOUND",
					"message": "OH NO",
					"path": ["repository", "issue"]
				},
				{
					"type": "ACTUALLY_ITS_FINE",
					"message": "this is fine",
					"path": ["repository", "issues", 0, "comments"]
				}
			  ]
			}
		`),
	)

	err := client.GraphQL("github.com", "", nil, &response)
	if err == nil || err.Error() != "GraphQL: OH NO (repository.issue), this is fine (repository.issues.0.comments)" {
		t.Fatalf("got %q", err.Error())
	}
}

func TestRESTGetDelete(t *testing.T) {
	http := &httpmock.Registry{}
	client := newTestClient(http)

	http.Register(
		httpmock.REST("DELETE", "applications/CLIENTID/grant"),
		httpmock.StatusStringResponse(204, "{}"),
	)

	r := bytes.NewReader([]byte(`{}`))
	err := client.REST("github.com", "DELETE", "applications/CLIENTID/grant", r, nil)
	assert.NoError(t, err)
}

func TestRESTWithFullURL(t *testing.T) {
	http := &httpmock.Registry{}
	client := newTestClient(http)

	http.Register(
		httpmock.REST("GET", "api/v3/user/repos"),
		httpmock.StatusStringResponse(200, "{}"))
	http.Register(
		httpmock.REST("GET", "user/repos"),
		httpmock.StatusStringResponse(200, "{}"))

	err := client.REST("example.com", "GET", "user/repos", nil, nil)
	assert.NoError(t, err)
	err = client.REST("example.com", "GET", "https://another.net/user/repos", nil, nil)
	assert.NoError(t, err)

	assert.Equal(t, "example.com", http.Requests[0].URL.Hostname())
	assert.Equal(t, "another.net", http.Requests[1].URL.Hostname())
}

func TestRESTError(t *testing.T) {
	fakehttp := &httpmock.Registry{}
	client := newTestClient(fakehttp)

	fakehttp.Register(httpmock.MatchAny, func(req *http.Request) (*http.Response, error) {
		return &http.Response{
			Request:    req,
			StatusCode: 422,
			Body:       io.NopCloser(bytes.NewBufferString(`{"message": "OH NO"}`)),
			Header: map[string][]string{
				"Content-Type": {"application/json; charset=utf-8"},
			},
		}, nil
	})

	var httpErr HTTPError
	err := client.REST("github.com", "DELETE", "repos/branch", nil, nil)
	if err == nil || !errors.As(err, &httpErr) {
		t.Fatalf("got %v", err)
	}

	if httpErr.StatusCode != 422 {
		t.Errorf("expected status code 422, got %d", httpErr.StatusCode)
	}
	if httpErr.Error() != "HTTP 422: OH NO (https://api.github.com/repos/branch)" {
		t.Errorf("got %q", httpErr.Error())
	}
}

func TestHandleHTTPError_GraphQL502(t *testing.T) {
	req, err := http.NewRequest("GET", "https://api.github.com/user", nil)
	if err != nil {
		t.Fatal(err)
	}
	resp := &http.Response{
		Request:    req,
		StatusCode: 502,
		Body:       io.NopCloser(bytes.NewBufferString(`{ "data": null, "errors": [{ "message": "Something went wrong" }] }`)),
		Header:     map[string][]string{"Content-Type": {"application/json"}},
	}
	err = HandleHTTPError(resp)
	if err == nil || err.Error() != "HTTP 502: Something went wrong (https://api.github.com/user)" {
		t.Errorf("got error: %v", err)
	}
}

func TestHTTPError_ScopesSuggestion(t *testing.T) {
	makeResponse := func(s int, u, haveScopes, needScopes string) *http.Response {
		req, err := http.NewRequest("GET", u, nil)
		if err != nil {
			t.Fatal(err)
		}
		return &http.Response{
			Request:    req,
			StatusCode: s,
			Body:       io.NopCloser(bytes.NewBufferString(`{}`)),
			Header: map[string][]string{
				"Content-Type":            {"application/json"},
				"X-Oauth-Scopes":          {haveScopes},
				"X-Accepted-Oauth-Scopes": {needScopes},
			},
		}
	}

	tests := []struct {
		name string
		resp *http.Response
		want string
	}{
		{
			name: "has necessary scopes",
			resp: makeResponse(404, "https://api.github.com/gists", "repo, gist, read:org", "gist"),
			want: ``,
		},
		{
			name: "normalizes scopes",
			resp: makeResponse(404, "https://api.github.com/orgs/ORG/discussions", "admin:org, write:discussion", "read:org, read:discussion"),
			want: ``,
		},
		{
			name: "no scopes on endpoint",
			resp: makeResponse(404, "https://api.github.com/user", "repo", ""),
			want: ``,
		},
		{
			name: "missing a scope",
			resp: makeResponse(404, "https://api.github.com/gists", "repo, read:org", "gist, delete_repo"),
			want: `This API operation needs the "gist" scope. To request it, run:  gh auth refresh -h github.com -s gist`,
		},
		{
			name: "server error",
			resp: makeResponse(500, "https://api.github.com/gists", "repo", "gist"),
			want: ``,
		},
		{
			name: "no scopes on token",
			resp: makeResponse(404, "https://api.github.com/gists", "", "gist, delete_repo"),
			want: ``,
		},
		{
			name: "http code is 422",
			resp: makeResponse(422, "https://api.github.com/gists", "", "gist"),
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			httpError := HandleHTTPError(tt.resp)
			if got := httpError.(HTTPError).ScopesSuggestion(); got != tt.want {
				t.Errorf("HTTPError.ScopesSuggestion() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestHTTPHeaders(t *testing.T) {
	var gotReq *http.Request
	ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		gotReq = r
		w.WriteHeader(http.StatusNoContent)
	}))
	defer ts.Clo
... [TRUNCATED]
```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
This folder is used for documentation related to developing `gh`. Docs for `gh` installation and usage are available at [https://cli.github.com/manual](https://cli.github.com/manual).
```

### File: codespaces.md
```md
# Guide to working with Codespaces using the CLI

For more information on Codespaces, see [Codespaces section in GitHub Docs](https://docs.github.com/en/codespaces).

## Access to other repositories

The codespace creation process will prompt you to review and authorize additional permissions defined in
`devcontainer.json` at creation time:

```json
{
  "customizations": {
    "codespaces": {
      "repositories": {
        "my_org/my_repo": {
          "permissions": {
            "issues": "write"
          }
        }
      }
    }
  }
}
```

However, any changes to `codespaces` customizations will not be re-evaluated for an existing
codespace.  This requires you to create a new codespace in order to authorize the new
permissions using `gh codespace create`.

For more information, see ["Repository access"](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces).

If additional access is needed for an existing codespace or access to a repository outside of
your user or organization account, the use of a fine-grained personal access token as an
environment variable or Codespaces secret might be considered.

For more information, see ["Authenticating to repositories"](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-authentication-to-a-repository).

```

### File: command-line-syntax.md
```md
# How we document our command line syntax

## Literal text

Use plain text for parts of the command that cannot be changed.

_example:_
`gh help`
The argument help is required in this command.

## Placeholder values

Use angled brackets to represent a value the user must replace. No other expressions can be contained within the angled brackets.

_example:_
`gh pr view <issue-number>`
Replace `<issue-number>` with an issue number.

## Optional arguments

Place optional arguments in square brackets. Mutually exclusive arguments can be included inside square brackets if they are separated with vertical bars.

_example:_
`gh pr checkout [--web]`
The argument `--web` is optional.

`gh pr view [<number> | <url>]`
The `<number>` and `<url>` arguments are optional.

## Required mutually exclusive arguments

Place required mutually exclusive arguments inside braces, separate arguments with vertical bars.

_example:_
`gh pr {view | create}`

## Repeatable arguments

Ellipsis represent arguments that can appear multiple times.

_example:_
`gh pr close <pr-number>...`

## Variable naming

For multi-word variables use dash-case (all lower case with words separated by dashes)

_example:_
`gh pr checkout <issue-number>`

## Additional examples

_optional argument with placeholder:_
`command sub-command [<arg>]`

_required argument with mutually exclusive options:_
`command sub-command {<path> | <string> | literal}`

_optional argument with mutually exclusive options:_
`command sub-command [<path> | <string>]`

```

### File: gh-vs-hub.md
```md
# GitHub CLI & `hub`

[GitHub CLI](https://cli.github.com/) (`gh`) was [announced in early 2020](https://github.blog/2020-02-12-supercharge-your-command-line-experience-github-cli-is-now-in-beta/) and provides a more seamless way to interact with your GitHub repositories from the command line. We also know that many people are interested in the very similar [`hub`](https://hub.github.com/) project, so we wanted to clarify some potential points of confusion.

## Why didn’t you just build `gh` on top of `hub`?

We wrestled with the decision of whether to continue building onto `hub` and adopt it as an official GitHub project. In weighing different possibilities, we decided to start fresh without the constraints of 10 years of design decisions that `hub` has baked in and without the assumption that `hub` can be safely aliased to `git`. We also wanted to be more opinionated and focused on GitHub workflows, and doing this with `hub` had the risk of alienating many `hub` users who love the existing tool and expected it to work in the way they were used to.

## What’s next for `hub`?

The GitHub CLI team is focused solely on building out the new tool, `gh`. We aren’t shutting down `hub` or doing anything to change it. It’s an open source project and will continue to exist as long as it’s maintained and keeps receiving contributions.

## What does it mean that GitHub CLI is official and `hub` is unofficial?

GitHub CLI is built and maintained by a team of people who work on the tool on behalf of GitHub. When there’s something wrong with it, people can reach out to GitHub support or create an issue in the issue tracker, where an employee at GitHub will respond. 

`hub` is a project whose maintainer also happens to be a GitHub employee. He chooses to maintain `hub` in his spare time, as many of our employees do with open source projects.

## Should I use `gh` or `hub`?

We have no interest in forcing anyone to use GitHub CLI instead of `hub`. We think people should use whatever set of tools makes them happiest and most productive working with GitHub. 

If you are set on using a tool that acts as a wrapper for Git itself, `hub` is likely a better choice than `gh`.

If you want a tool that’s more opinionated and intended to help simplify your GitHub workflows from the command line, we hope you’ll use `gh`. And since `gh` is maintained by a team at GitHub, we intend to be responsive to people’s concerns and needs and improve the tool based on how people are using it over time.

GitHub CLI is not intended to be an exact replacement for `hub` and likely never will be, but our hope is that the vast majority of GitHub users who use the CLI will find more and more value in using `gh` as we continue to improve it.

```

### File: install_linux.md
```md
# Installing gh on Linux and BSD

## Recommended _(Official)_

### Debian

Debian packages are hosted on the [GitHub CLI marketing site](https://cli.github.com/) for various operating systems including:

- [Debian](https://www.debian.org/)
- [Raspberry Pi](https://www.raspberrypi.com/)
- [Ubuntu Linux](https://ubuntu.com/)

These packages are supported by the GitHub CLI maintainers with updates powered by [GitHub CLI deployment workflow](https://github.com/cli/cli/actions/workflows/deployment.yml).

To install:

```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

To upgrade:

```bash
sudo apt update
sudo apt install gh
```

### RPM

RPM packages are hosted on the [GitHub CLI marketing site](https://cli.github.com) for various operating systems including:

- [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/)
- [CentOS](https://www.centos.org/)
- [Fedora](https://fedoraproject.org/)
- [Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)
- [openSUSE](https://www.opensuse.org/)
- [SUSE](https://www.suse.com/)

These packages are supported by the GitHub CLI maintainers with updates powered by [GitHub CLI deployment workflow](https://github.com/cli/cli/actions/workflows/deployment.yml).

#### DNF5

> [!IMPORTANT]
> **These commands apply to DNF5 only**. If you're using DNF4, please use [the DNF4 instructions](#dnf4).

To install:

```bash
sudo dnf install dnf5-plugins
sudo dnf config-manager addrepo --from-repofile=https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install gh --repo gh-cli
```

To upgrade:

```bash
sudo dnf update gh
```

#### DNF4

> [!IMPORTANT]
> **These commands apply to DNF4 only**. If you're using DNF5, please use [the DNF5 instructions](#dnf5).

To install:

```bash
sudo dnf install 'dnf-command(config-manager)'
sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install gh --repo gh-cli
```

To upgrade:

```bash
sudo dnf update gh
```

#### Amazon Linux 2 (yum)

To install:

```bash
type -p yum-config-manager >/dev/null || sudo yum install yum-utils
sudo yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo yum install gh
```

To upgrade:

```bash
sudo yum update gh
```

#### openSUSE/SUSE Linux (zypper)

To install:

```bash
sudo zypper addrepo https://cli.github.com/packages/rpm/gh-cli.repo
sudo zypper ref
sudo zypper install gh
```

To upgrade:

```bash
sudo zypper ref
sudo zypper update gh
```

### Homebrew

[Homebrew](https://brew.sh/) is a free and open-source software package management system that simplifies the installation of software on Apple's operating system, macOS, as well as Linux.

The [GitHub CLI formulae](https://formulae.brew.sh/formula/gh) is supported by the GitHub CLI maintainers with help from our friends at Homebrew with updated powered by [homebrew/hoomebrew-core](https://github.com/Homebrew/homebrew-core/blob/main/Formula/g/gh.rb).

To install:

```shell
brew install gh
```

To upgrade:

```shell
brew upgrade gh
```

### Precompiled binaries

[GitHub CLI releases](https://github.com/cli/cli/releases/latest) contain precompiled binaries for `386`, `amd64`, `arm64`, and `armv6` architectures.

## Community _(Unofficial)_

> [!IMPORTANT]
> The GitHub CLI team does not maintain the following packages or repositories. We are unable to provide support for these installation methods or any guarantees of stability, security, or availability for these installation methods.

### Alpine Linux

The [GitHub CLI package](https://pkgs.alpinelinux.org/package/edge/community/x86_64/github-cli) is supported by the Alpine Linux community with updates powered by [alpine/aports](https://gitlab.alpinelinux.org/alpine/aports/-/tree/master/community/github-cli).

To install stable release:

```bash
apk add github-cli
```

To install edge release:

```bash
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
apk add github-cli@community
```

### Android

The [GitHub CLI package](https://packages.termux.dev/apt/termux-main/pool/main/g/gh/) is supported by the Termux community with updates powered by [termux/termux-packages](https://github.com/termux/termux-packages/tree/master/packages/gh).

To install and upgrade:

```bash
pkg install gh
```

### Arch Linux

The [GitHub CLI package](https://www.archlinux.org/packages/extra/x86_64/github-cli) is supported by the Arch Linux community with updates powered by [Arch Linux packaging](https://gitlab.archlinux.org/archlinux/packaging/packages/github-cli).

To install:

```bash
sudo pacman -S github-cli
```

To upgrade all packages:

```bash
sudo pacman -Syu
```

Alternatively, use the [unofficial AUR package](https://aur.archlinux.org/packages/github-cli-git) to build GitHub CLI from source.

### Conda

[Conda](https://docs.conda.io/en/latest/) is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them. It works on Linux, OS X and Windows, and was created for Python programs but can package and distribute any software.

The [GitHub CLI package](https://anaconda.org/conda-forge/gh) is supported by the Conda community with updates powered by [conda-forge/gh-feedstock](https://github.com/conda-forge/gh-feedstock#installing-gh).

To install:

```shell
conda install gh --channel conda-forge
```

To upgrade:

```shell
conda update gh --channel conda-forge
```

### Debian Community

The [GitHub CLI package](https://packages.debian.org/stable/gh) is supported by the Debian community with updates powered by [Debian Go Packaging Team](https://salsa.debian.org/go-team/packages/gh).

> [!NOTE]
> As of November 2025, GitHub CLI maintainers strongly recommend [official Debian packages](#debian) especially as the community-distributed `2.45.x` / `2.46.x` version is broken due to deprecated GitHub APIs.

### Fedora Community

The [GitHub CLI package](https://packages.fedoraproject.org/pkgs/gh/gh/) is supported by the Fedora community with updates powered by [Fedora Project](https://src.fedoraproject.org/rpms/gh).

To install:

```bash
sudo dnf install gh
```

To upgrade:

```bash
sudo dnf update gh
```

### Flox

[Flox](https://flox.dev/) is a virtual environment and package manager all in one. With Flox you create environments that layer and replace dependencies just where it matters, making them portable across the full software lifecycle.

Flox relies upon the [GitHub CLI package](https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/gh/gh/package.nix) supported by the [NixOS community](https://nixos.org/)

To install:

```shell
flox install gh
```

To upgrade:

```shell
flox upgrade toplevel
```

### FreeBSD

The [GitHub CLI port](https://www.freshports.org/devel/gh/) is supported by the FreeBSD community with updates powered by [FreeBSD ports](https://cgit.freebsd.org/ports/tree/devel/gh).

```bash
cd /usr/ports/devel/gh/ && make install clean
```

Or via [pkg(8)](https://www.freebsd.org/cgi/man.cgi?pkg(8)):

```bash
pkg install gh
```

### Funtoo

The GitHub CLI portage is supported by the Funtoo community with updates powered by [funtoo/dev-kit](https://github.com/funtoo/dev-kit/tree/1.4-release/dev-util/github-cli).

To install:

```bash
emerge -av github-cli
```

To upgrade:

```bash
ego sync
emerge -u github-cli
```

### Gentoo

The [GitHub CLI portage](https://packages.gentoo.org/packages/dev-util/github-cli) is supported by the Gentoo community with updates powered by [Gentoo portage](https://gitweb.gentoo.org/repo/gentoo.git/tree/dev-util/github-cli).

To install:

``` bash
emerge -av github-cli
```

To upgrade:

``` bash
emerge --sync
emerge -u github-cli
```

### Manjaro Linux

The [GitHub CLI package](https://manjaristas.org/branch_compare?q=github-cli) is the same package produced by the [Arch Linux community](#arch-linux)

To install and upgrade:

```bash
pamac install github-cli
```

### MidnightBSD

The [GitHub CLI port](https://www.midnightbsd.org/mports/devel/gh/README.html) is supported by the MidnightBSD community with updates powered by [MidnightBSD/mports](https://github.com/MidnightBSD/mports/tree/master/devel/gh).

To install:

```bash
cd /usr/mports/deve
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
