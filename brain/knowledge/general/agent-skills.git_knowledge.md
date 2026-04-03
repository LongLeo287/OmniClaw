---
id: agent-skills.git-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:40.975223
---

# KNOWLEDGE EXTRACT: agent-skills.git
> **Extracted on:** 2026-03-30 13:12:34
> **Source:** agent-skills.git

---

## File: `.gitignore`
```
.env
.DS_Store

# DEVELOPMENT
.vscode
.claude
context/
CLAUDE.md
PLAN.md
PLAN-*.md
.mcp.json
scripts/hooks/
.idea
```

## File: `gemini-extension.json`
```json
{
  "name": "apify-agent-skills",
  "description": "Provides access to Apify Agent Skills for web scraping, data extraction, and automation.",
  "version": "1.0.0",
  "contextFileName": "agents/AGENTS.md"
}
```

## File: `README.md`
```markdown
# Apify Agent Skills

A collection of AI agent skills for web scraping, data extraction, and Actor development on the Apify platform.

> Looking for more specialized skills? Check out [apify/awesome-skills](https://github.com/apify/awesome-skills) — a community collection of domain-specific skills for lead generation, brand monitoring, competitor intelligence, and more.

## Skills

### Scraping

- **[Ultimate scraper](skills/apify-ultimate-scraper/)** (`apify-ultimate-scraper`) — AI-powered web scraper for 55+ platforms including Instagram, Facebook, TikTok, YouTube, Google Maps, Amazon, Walmart, eBay, Booking.com, TripAdvisor, and more. Can also search the [Apify Store](https://apify.com/store) to find the right Actor for any platform not listed here.

### Development

- **[Actor development](skills/apify-actor-development/)** (`apify-actor-development`) — create, debug, and deploy Apify Actors from scratch in JavaScript, TypeScript, or Python.
- **[Actorization](skills/apify-actorization/)** (`apify-actorization`) — convert existing projects into Apify Actors. Supports JS/TS (SDK), Python (async context manager), and any language (CLI wrapper).
- **[Generate output schema](skills/apify-generate-output-schema/)** (`apify-generate-output-schema`) — generate output schemas (`dataset_schema.json`, `output_schema.json`, `key_value_store_schema.json`) for an Apify Actor by analyzing its source code.

## Installation

```bash
npx skills add apify/agent-skills
```

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add https://github.com/apify/agent-skills

# Install a skill
/plugin install apify-ultimate-scraper@apify-agent-skills
```

### Cursor / Windsurf

Add to your project's `.cursor/settings.json` or use the same Claude Code plugin format.

### Codex / Gemini CLI

Point your agent to the `agents/AGENTS.md` file which contains skill descriptions and paths:

```bash
# Gemini CLI uses gemini-extension.json automatically
# For Codex, reference agents/AGENTS.md in your configuration
```

### Other AI tools

Any AI tool that supports Markdown context can use the skills by pointing to:
- `agents/AGENTS.md` - auto-generated skill index
- `skills/*/SKILL.md` - individual skill documentation

## Prerequisites

1. **Apify account** — [apify.com](https://apify.com)
2. **API token** — get from [Apify Console](https://console.apify.com/account/integrations), add `APIFY_TOKEN=your_token` to `.env`
3. **Node.js 20.6+** (for the scraper skill)

## Pricing

Apify Actors use pay-per-result pricing. Check individual Actor pricing on the [Apify platform](https://apify.com).

## Support

- [Apify Documentation](https://docs.apify.com)
- [Apify Discord](https://discord.gg/jyEM2PRvMU)

## License

[Apache-2.0](LICENSE)
```

## File: `agents/AGENTS.md`
```markdown
<skills>

You have additional SKILLs documented in directories containing a "SKILL.md" file.

These skills are:
 - apify-actor-development -> "skills/apify-actor-development/SKILL.md"
 - apify-actorization -> "skills/apify-actorization/SKILL.md"
 - apify-generate-output-schema -> "skills/apify-generate-output-schema/SKILL.md"
 - apify-ultimate-scraper -> "skills/apify-ultimate-scraper/SKILL.md"

IMPORTANT: You MUST read the SKILL.md file whenever the description of the skills matches the user intent, or may help accomplish their task.

<available_skills>

apify-actor-development: `Develop, debug, and deploy Apify Actors - serverless cloud programs for web scraping, automation, and data processing. Use when creating new Actors, modifying existing ones, or troubleshooting Actor code.`
apify-actorization: `Convert existing projects into Apify Actors - serverless cloud programs. Actorize JavaScript/TypeScript (SDK with Actor.init/exit), Python (async context manager), or any language (CLI wrapper). Use when migrating code to Apify, wrapping CLI tools as Actors, or adding Actor SDK to existing projects.`
apify-generate-output-schema: `Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) for an Apify Actor by analyzing its source code. Use when creating or updating Actor output schemas.`
apify-ultimate-scraper: `Universal AI-powered web scraper for any platform. Scrape data from Instagram, Facebook, TikTok, YouTube, Google Maps, Google Search, Google Trends, Booking.com, and TripAdvisor. Use for lead generation, brand monitoring, competitor analysis, influencer discovery, trend research, content analytics, audience analysis, or any data extraction task.`
</available_skills>

Paths referenced within SKILL.md files are relative to that SKILL folder. For example `reference/workflows.md` refers to the workflows file inside the skill's reference folder.

</skills>
```

## File: `commands/create-actor.md`
```markdown
---
description: Guided Apify Actor development with best practices and systematic workflow
argument-hint: Optional actor description
---

# Actor Development

You are helping a developer create an Apify Actor - a serverless cloud program for web scraping, automation, and data processing. Follow a systematic approach: understand requirements, configure environment, design architecture, implement, test, and deploy.

## Core Principles

- **Ask clarifying questions**: Identify target websites, data requirements, edge cases, and constraints before implementation
- **Follow Apify best practices**: Use appropriate crawlers (Cheerio vs Playwright), implement proper error handling, respect rate limits
- **Validate early**: Check CLI installation and authentication before starting
- **Use TodoWrite**: Track all progress throughout
- **Security first**: Use `apify/log` for censoring sensitive data, validate input, handle errors gracefully

---

## Phase 1: Discovery

**Goal**: Understand what actor needs to be built

Initial request: $ARGUMENTS

**Actions**:
1. Create todo list with all phases
2. Ask user for clarification if needed:
   - What is the actor's primary purpose? (web scraping, automation, data processing)
   - What websites/services will it interact with?
   - What data should it extract or what actions should it perform?
   - Any specific requirements or constraints?
3. Summarize understanding and confirm with user

---

## Phase 2: Environment Setup

**Goal**: Verify Apify CLI is installed and authenticated

**CRITICAL**: Do not proceed without proper setup

**Actions**:
1. Check if Apify CLI is installed: `apify --help`
2. If not installed, guide user to install:
   ```bash
   curl -fsSL https://apify.com/install-cli.sh | bash
   # Or: brew install apify-cli (Mac)
   # Or: npm install -g apify-cli
   ```
3. Verify authentication: `apify info`
4. If not logged in:
   - Check for APIFY_TOKEN environment variable
   - If missing, ask user to generate token at https://console.apify.com/settings/integrations
   - Login with: `apify login -t $APIFY_TOKEN`

---

## Phase 3: Language Selection

**Goal**: Choose programming language and template

**Actions**:
1. **Ask user which language they prefer:**
   - JavaScript (skills/apify-actor-development/references/actor-template-js.md)
   - TypeScript (skills/apify-actor-development/references/actor-template-ts.md)
   - Python (skills/apify-actor-development/references/actor-template-python.md)
2. Note: Additional packages (Crawlee, Playwright, etc.) can be installed later as needed

---

## Phase 4: Requirements & Architecture Design

**Goal**: Define input/output schemas and implementation approach

**Actions**:
1. Clarify detailed requirements:
   - What input parameters should the actor accept?
   - What output format is needed? (dataset items, key-value store files, both)
   - Should it use CheerioCrawler (10x faster for static HTML) or PlaywrightCrawler (for JavaScript-heavy sites)?
   - Concurrency settings? (HTTP: 10-50, Browser: 1-5)
   - Rate limiting and retry strategies?
   - Should standby mode be enabled?
2. Design architecture:
   - Input schema structure
   - Output/dataset schema structure
   - Key-value store schema (if needed)
   - Error handling approach
   - Data validation and cleaning strategy
3. Present architecture to user and get approval

---

## Phase 5: Actor Creation

**Goal**: Create actor from template and configure schemas

**DO NOT START WITHOUT USER APPROVAL**

**Actions**:
1. Wait for explicit user approval
2. Copy appropriate language template from `skills/apify-actor-development/references/` directory
3. Update `.actor/actor.json`:
   - Set actor name and version
   - **IMPORTANT**: Fill in `generatedBy` property with current model name
   - Configure runtime, memory, timeout
   - Set `usesStandbyMode` if applicable
4. Create/update `.actor/input_schema.json` with input parameters
5. Create/update `.actor/output_schema.json` with output structure
6. Create/update `.actor/dataset_schema.json` if using datasets
7. Create/update `.actor/key_value_store_schema.json` if using key-value store
8. Update todos as you progress

**Reference documentation:**
- [skills/apify-actor-development/references/actor-json.md](skills/apify-actor-development/references/actor-json.md)
- [skills/apify-actor-development/references/input-schema.md](skills/apify-actor-development/references/input-schema.md)
- [skills/apify-actor-development/references/output-schema.md](skills/apify-actor-development/references/output-schema.md)
- [skills/apify-actor-development/references/dataset-schema.md](skills/apify-actor-development/references/dataset-schema.md)
- [skills/apify-actor-development/references/key-value-store-schema.md](skills/apify-actor-development/references/key-value-store-schema.md)

---

## Phase 6: Implementation

**Goal**: Implement actor logic following best practices

**Actions**:
1. Implement actor code in `src/main.py`, `src/main.js`, or `src/main.ts`
2. Follow best practices:
   - ✓ Use Apify SDK (`apify`) for code running on Apify platform
   - ✓ Validate input early with proper error handling
   - ✓ Use CheerioCrawler for static HTML (10x faster)
   - ✓ Use PlaywrightCrawler only for JavaScript-heavy sites
   - ✓ Use router pattern for complex crawls
   - ✓ Implement retry strategies with exponential backoff
   - ✓ Use proper concurrency settings
   - ✓ Clean and validate data before pushing to dataset
   - ✓ **Always use `apify/log` package** - censors sensitive data
   - ✓ Implement readiness probe handler if using standby mode
   - ✗ Don't use browser crawlers when HTTP/Cheerio works
   - ✗ Don't hard code values that should be in input schema
   - ✗ Don't skip input validation or error handling
   - ✗ Don't overload servers - use appropriate concurrency and delays
3. Implement standby mode readiness probe if `usesStandbyMode: true` (see [skills/apify-actor-development/references/standby-mode.md](skills/apify-actor-development/references/standby-mode.md))
4. Use proper logging (see [skills/apify-actor-development/references/logging.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/pytorch_lightning/references/logging.md))
5. Update todos as you progress

---

## Phase 7: Documentation

**Goal**: Create comprehensive README for marketplace

**Actions**:
1. Create README.md with:
   - Clear description of what the actor does
   - Input parameters with examples
   - Output format with examples
   - Usage instructions
   - Limitations and known issues
   - Example runs
2. Include code examples for common use cases
3. Mention rate limits, costs, or legal considerations if applicable

---

## Phase 8: Local Testing

**Goal**: Test actor locally before deployment

**Actions**:
1. Install dependencies:
   - JavaScript/TypeScript: `npm install`
   - Python: `pip install -r requirements.txt`
2. Create test input file at `vault/key_value_stores/default/INPUT.json` with sample parameters
3. Run actor locally: `apify run`
4. Verify:
   - Input is parsed correctly
   - Actor completes successfully
   - Output is in expected format
   - Error handling works
   - Logging is appropriate
5. Fix any issues found
6. Test edge cases and error scenarios

---

## Phase 9: Deployment

**Goal**: Deploy actor to Apify platform

**DO NOT DEPLOY WITHOUT USER APPROVAL**

**Actions**:
1. **Ask user if they want to deploy now**
2. If yes, deploy with: `apify push`
3. Actor will be deployed with name from `.actor/actor.json`
4. Provide user with:
   - Deployment confirmation
   - Actor URL on Apify platform
   - Instructions for running on platform

---

## Phase 10: Summary

**Goal**: Document what was accomplished

**Actions**:
1. Mark all todos complete
2. Summarize:
   - What actor was built
   - Key features and capabilities
   - Input/output schemas
   - Files created/modified
   - Deployment status
   - Suggested next steps (testing on platform, publishing to store, monitoring)

---

## Additional Resources

**MCP Tools** (if configured):
- `search-apify-docs` - Search documentation
- `fetch-apify-docs` - Get full doc pages

**Documentation:**
- [docs.apify.com/llms.txt](https://docs.apify.com/llms.txt) - Apify quick reference
- [docs.apify.com/llms-full.txt](https://docs.apify.com/llms-full.txt) - Apify complete docs
- [crawlee.dev/llms.txt](https://crawlee.dev/llms.txt) - Crawlee quick reference
- [crawlee.dev/llms-full.txt](https://crawlee.dev/llms-full.txt) - Crawlee complete docs
- [whitepaper.actor](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md) - Complete Actor specification
```

## File: `scripts/AGENTS_TEMPLATE.md`
```markdown
<skills>

You have additional SKILLs documented in directories containing a "SKILL.md" file.

These skills are:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

IMPORTANT: You MUST read the SKILL.md file whenever the description of the skills matches the user intent, or may help accomplish their task.

<available_skills>

{{#skills}}
{{name}}: `{{description}}`

{{/skills}}
</available_skills>

Paths referenced within SKILL.md files are relative to that SKILL folder. For example `reference/workflows.md` refers to the workflows file inside the skill's reference folder.

</skills>
```

## File: `scripts/generate_agents.py`
```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Generate AGENTS.md from AGENTS_TEMPLATE.md and SKILL.md frontmatter.

Also validates that marketplace.json is in sync with discovered skills.

Usage:
  uv run scripts/generate_agents.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "scripts" / "AGENTS_TEMPLATE.md"
OUTPUT_PATH = ROOT / "agents" / "AGENTS.md"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"


def load_template() -> str:
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse a minimal YAML-ish frontmatter block without external deps."""
    match = re.search(r"^---\s*\n(.*?)\n---\s*", text, re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def collect_skills() -> list[dict[str, str]]:
    skills: list[dict[str, str]] = []
    for skill_md in ROOT.glob("skills/*/SKILL.md"):
        meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        name = meta.get("name")
        description = meta.get("description")
        if not name or not description:
            continue
        skills.append(
            {
                "name": name,
                "description": description,
                "path": str(skill_md.parent.relative_to(ROOT)),
            }
        )
    # Keep deterministic order for consistent output
    return sorted(skills, key=lambda s: s["name"].lower())


def render(template: str, skills: list[dict[str, str]]) -> str:
    """Very small Mustache-like renderer that only supports a single skills loop."""
    def repl(match: re.Match[str]) -> str:
        block = match.group(1).strip("\n")
        rendered_blocks = []
        for skill in skills:
            rendered = (
                block.replace("{{name}}", skill["name"])
                .replace("{{description}}", skill["description"])
                .replace("{{path}}", skill["path"])
            )
            rendered_blocks.append(rendered)
        return "\n".join(rendered_blocks)

    # Render loop blocks
    content = re.sub(r"{{#skills}}(.*?){{/skills}}", repl, template, flags=re.DOTALL)
    return content


def validate_marketplace(skills: list[dict[str, str]]) -> list[str]:
    """Validate marketplace.json against discovered skills. Returns error messages."""
    if not MARKETPLACE_PATH.exists():
        return [f"marketplace.json not found at {MARKETPLACE_PATH}"]

    marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    plugins = marketplace.get("plugins", [])
    errors: list[str] = []

    # Every plugin with skills should have at least one SKILL.md
    for plugin in plugins:
        source = plugin.get("source", "").lstrip("./")
        plugin_skills = [s for s in skills if s["path"].startswith(source)]
        if not plugin_skills:
            errors.append(
                f"Plugin '{plugin['name']}' at '{source}' has no SKILL.md files"
            )

    # Every discovered skill should be covered by a plugin
    for skill in skills:
        found = any(
            skill["path"].startswith(p.get("source", "").lstrip("./"))
            for p in plugins
        )
        if not found:
            errors.append(
                f"Skill '{skill['name']}' at '{skill['path']}' is not covered by any plugin"
            )

    return errors


def main() -> None:
    template = load_template()
    skills = collect_skills()
    output = render(template, skills)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {len(skills)} skills.")

    # Validate marketplace.json
    errors = validate_marketplace(skills)
    if errors:
        print("\nMarketplace.json validation errors:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        sys.exit(1)
    print("Marketplace.json validation passed.")


if __name__ == "__main__":
    main()
```

## File: `skills/apify-actor-development/SKILL.md`
```markdown
---
name: apify-actor-development
description: Develop, debug, and deploy Apify Actors - serverless cloud programs for web scraping, automation, and data processing. Use when creating new Actors, modifying existing ones, or troubleshooting Actor code.
---

# Apify Actor Development

**Important:** Before you begin, fill in the `generatedBy` property in the meta section of `.actor/actor.json`. Replace it with the tool and model you're currently using, such as "Claude Code with Claude Sonnet 4.5". This helps Apify monitor and improve AGENTS.md for specific AI tools and models.

## What are Apify Actors?

Actors are serverless programs inspired by the UNIX philosophy - programs that do one thing well and can be easily combined to build complex systems. They're packaged as Docker images and run in isolated containers in the cloud.

**Core Concepts:**
- Accept well-defined JSON input
- Perform isolated tasks (web scraping, automation, data processing)
- Produce structured JSON output to datasets and/or store data in key-value stores
- Can run from seconds to hours or even indefinitely
- Persist state and can be restarted

## Prerequisites & Setup (MANDATORY)

Before creating or modifying actors, verify that `apify` CLI is installed `apify --help`.

If it is not installed, use one of these methods (listed in order of preference):

```bash
# Preferred: install via a package manager (provides integrity checks)
npm install -g apify-cli

# Or (Mac): brew install apify-cli
```

> **Security note:** Do NOT install the CLI by piping remote scripts to a shell
> (e.g. `curl … | bash` or `irm … | iex`). Always use a package manager.

When the apify CLI is installed, check that it is logged in with:

```bash
apify info  # Should return your username
```

If it is not logged in, check if the `APIFY_TOKEN` environment variable is defined (if not, ask the user to generate one on https://console.apify.com/settings/integrations and then define `APIFY_TOKEN` with it).

Then authenticate using one of these methods:

```bash
# Option 1 (preferred): The CLI automatically reads APIFY_TOKEN from the environment.
# Just ensure the env var is exported and run any apify command — no explicit login needed.

# Option 2: Interactive login (prompts for token without exposing it in shell history)
apify login
```

> **Security note:** Avoid passing tokens as command-line arguments (e.g. `apify login -t <token>`).
> Arguments are visible in process listings and may be recorded in shell history.
> Prefer environment variables or interactive login instead.
> Never log, print, or embed `APIFY_TOKEN` in source code or configuration files.
> Use a token with the minimum required permissions (scoped token) and rotate it periodically.

## Template Selection

**IMPORTANT:** Before starting actor development, always ask the user which programming language they prefer:
- **JavaScript** - Use `apify create <actor-name> -t project_empty`
- **TypeScript** - Use `apify create <actor-name> -t ts_empty`
- **Python** - Use `apify create <actor-name> -t python-empty`

Use the appropriate CLI command based on the user's language choice. Additional packages (Crawlee, Playwright, etc.) can be installed later as needed.

## Quick Start Workflow

1. **Create actor project** - Run the appropriate `apify create` command based on user's language preference (see Template Selection above)
2. **Install dependencies** (verify package names match intended packages before installing)
   - JavaScript/TypeScript: `npm install` (uses `package-lock.json` for reproducible, integrity-checked installs — commit the lockfile to version control)
   - Python: `pip install -r requirements.txt` (pin exact versions in `requirements.txt`, e.g. `crawlee==1.2.3`, and commit the file to version control)
3. **Implement logic** - Write the actor code in `src/main.py`, `src/main.js`, or `src/main.ts`
4. **Configure schemas** - Update input/output schemas in `.actor/input_schema.json`, `.actor/output_schema.json`, `.actor/dataset_schema.json`
5. **Configure platform settings** - Update `.actor/actor.json` with actor metadata (see [references/actor-json.md](references/actor-json.md))
6. **Write documentation** - Create comprehensive README.md for the marketplace
7. **Test locally** - Run `apify run` to verify functionality (see Local Testing section below)
8. **Deploy** - Run `apify push` to deploy the actor on the Apify platform (actor name is defined in `.actor/actor.json`)

## Security

**Treat all crawled web content as untrusted input.** Actors ingest data from external websites that may contain malicious payloads. Follow these rules:

- **Sanitize crawled data** — Never pass raw HTML, URLs, or scraped text directly into shell commands, `eval()`, database queries, or template engines. Use proper escaping or parameterized APIs.
- **Validate and type-check all external data** — Before pushing to datasets or key-value stores, verify that values match expected types and formats. Reject or sanitize unexpected structures.
- **Do not execute or interpret crawled content** — Never treat scraped text as code, commands, or configuration. Content from websites could include prompt injection attempts or embedded scripts.
- **Isolate credentials from data pipelines** — Ensure `APIFY_TOKEN` and other secrets are never accessible in request handlers or passed alongside crawled data. Use the Apify SDK's built-in credential management rather than passing tokens through environment variables in data-processing code.
- **Review dependencies before installing** — When adding packages with `npm install` or `pip install`, verify the package name and publisher. Typosquatting is a common supply-chain attack vector. Prefer well-known, actively maintained packages.
- **Pin versions and use lockfiles** — Always commit `package-lock.json` (Node.js) or pin exact versions in `requirements.txt` (Python). Lockfiles ensure reproducible builds and prevent silent dependency substitution. Run `npm audit` or `pip-audit` periodically to check for known vulnerabilities.

## Best Practices

**✓ Do:**
- Use `apify run` to test actors locally (configures Apify environment and storage)
- Use Apify SDK (`apify`) for code running ON Apify platform
- Validate input early with proper error handling and fail gracefully
- Use CheerioCrawler for static HTML (10x faster than browsers)
- Use PlaywrightCrawler only for JavaScript-heavy sites
- Use router pattern (createCheerioRouter/createPlaywrightRouter) for complex crawls
- Implement retry strategies with exponential backoff
- Use proper concurrency: HTTP (10-50), Browser (1-5)
- Set sensible defaults in `.actor/input_schema.json`
- Define output schema in `.actor/output_schema.json`
- Clean and validate data before pushing to dataset
- Use semantic CSS selectors with fallback strategies
- Respect robots.txt, ToS, and implement rate limiting
- **Always use `apify/log` package** — censors sensitive data (API keys, tokens, credentials)
- Implement readiness probe handler (required if your Actor uses standby mode)

**✗ Don't:**
- Use `npm start`, `npm run start`, `npx apify run`, or similar commands to run actors (use `apify run` instead)
- Assume local storage from `apify run` is pushed to or visible in the Apify Console — it is local-only; deploy with `apify push` and run on the platform to see results in the Console
- Rely on `Dataset.getInfo()` for final counts on Cloud
- Use browser crawlers when HTTP/Cheerio works
- Hard code values that should be in input schema or environment variables
- Skip input validation or error handling
- Overload servers - use appropriate concurrency and delays
- Scrape prohibited content or ignore Terms of Service
- Store personal/sensitive data unless explicitly permitted
- Use deprecated options like `requestHandlerTimeoutMillis` on CheerioCrawler (v3.x)
- Use `additionalHttpHeaders` - use `preNavigationHooks` instead
- Pass raw crawled content into shell commands, `eval()`, or code-generation functions
- Use `console.log()` or `print()` instead of the Apify logger — these bypass credential censoring
- Disable standby mode without explicit permission

## Logging

See [references/logging.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/pytorch_lightning/references/logging.md) for complete logging documentation including available log levels and best practices for JavaScript/TypeScript and Python.

Check `usesStandbyMode` in `.actor/actor.json` - only implement if set to `true`.

## Commands

```bash
apify run          # Run Actor locally
apify login        # Authenticate account
apify push         # Deploy to Apify platform (uses name from .actor/actor.json)
apify help         # List all commands
```

**IMPORTANT:** Always use `apify run` to test actors locally. Do not use `npm run start`, `npm start`, `yarn start`, or other package manager commands - these will not properly configure the Apify environment and storage.

## Local Testing

When testing an actor locally with `apify run`, provide input data by creating a JSON file at:

```
vault/key_value_stores/default/INPUT.json
```

This file should contain the input parameters defined in your `.actor/input_schema.json`. The actor will read this input when running locally, mirroring how it receives input on the Apify platform.

**IMPORTANT - Local storage is NOT synced to the Apify Console:**
- Running `apify run` stores all data (datasets, key-value stores, request queues) **only on your local filesystem** in the `vault/` directory.
- This data is **never** automatically uploaded or pushed to the Apify platform. It exists only on your machine.
- To verify results on the Apify Console, you must deploy the Actor with `apify push` and then run it on the platform.
- Do **not** rely on checking the Apify Console to verify results from local runs — instead, inspect the local `vault/` directory or check the Actor's log output.

## Standby Mode

See [references/standby-mode.md](references/standby-mode.md) for complete standby mode documentation including readiness probe implementation for JavaScript/TypeScript and Python.

## Project Structure

```
.actor/
├── actor.json           # Actor config: name, version, env vars, runtime
├── input_schema.json    # Input validation & Console form definition
└── output_schema.json   # Output storage and display templates
src/
└── main.js/ts/py       # Actor entry point
vault/                # Local-only storage (NOT synced to Apify Console)
├── datasets/           # Output items (JSON objects)
├── key_value_stores/   # Files, config, INPUT
└── request_queues/     # Pending crawl requests
Dockerfile              # Container image definition
```

## Actor Configuration

See [references/actor-json.md](references/actor-json.md) for complete actor.json structure and configuration options.

## Input Schema

See [references/input-schema.md](references/input-schema.md) for input schema structure and examples.

## Output Schema

See [references/output-schema.md](references/output-schema.md) for output schema structure, examples, and template variables.

## Dataset Schema

See [references/dataset-schema.md](references/dataset-schema.md) for dataset schema structure, configuration, and display properties.

## Key-Value Store Schema

See [references/key-value-store-schema.md](references/key-value-store-schema.md) for key-value store schema structure, collections, and configuration.


## Apify MCP Tools

If MCP server is configured, use these tools for documentation:

- `search-apify-docs` - Search documentation
- `fetch-apify-docs` - Get full doc pages

Otherwise, the MCP Server url: `https://mcp.apify.com/?tools=docs`.

## Resources

- [docs.apify.com/llms.txt](https://docs.apify.com/llms.txt) - Apify quick reference documentation
- [docs.apify.com/llms-full.txt](https://docs.apify.com/llms-full.txt) - Apify complete documentation
- [https://crawlee.dev/llms.txt](https://crawlee.dev/llms.txt) - Crawlee quick reference documentation
- [https://crawlee.dev/llms-full.txt](https://crawlee.dev/llms-full.txt) - Crawlee complete documentation
- [whitepaper.actor](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md) - Complete Actor specification
```

## File: `skills/apify-actor-development/references/actor-json.md`
```markdown
# Actor Configuration (actor.json)

The `.actor/actor.json` file contains the Actor's configuration including metadata, schema references, and platform settings.

## Structure

```json
{
    "actorSpecification": 1,
    "name": "project-name",
    "title": "Project Title",
    "description": "Actor description",
    "version": "0.0",
    "meta": {
        "templateId": "template-id",
        "generatedBy": "<FILL-IN-TOOL-AND-MODEL>"
    },
    "input": "./input_schema.json",
    "output": "./output_schema.json",
    "storages": {
        "dataset": "./dataset_schema.json"
    },
    "dockerfile": "../Dockerfile"
}
```

## Example

```json
{
    "actorSpecification": 1,
    "name": "project-cheerio-crawler-javascript",
    "title": "Project Cheerio Crawler Javascript",
    "description": "Crawlee and Cheerio project in javascript.",
    "version": "0.0",
    "meta": {
        "templateId": "js-crawlee-cheerio",
        "generatedBy": "Claude Code with Claude Sonnet 4.5"
    },
    "input": "./input_schema.json",
    "output": "./output_schema.json",
    "storages": {
        "dataset": "./dataset_schema.json"
    },
    "dockerfile": "../Dockerfile"
}
```

## Properties

- `actorSpecification` (integer, required) - Version of actor specification (currently 1)
- `name` (string, required) - Actor identifier (lowercase, hyphens allowed)
- `title` (string, required) - Human-readable title displayed in UI
- `description` (string, optional) - Actor description for marketplace
- `version` (string, required) - Semantic version number
- `meta` (object, optional) - Metadata about actor generation
  - `templateId` (string) - ID of template used to create the actor
  - `generatedBy` (string) - Tool and model name that generated/modified the actor (e.g., "Claude Code with Claude Sonnet 4.5")
- `input` (string, optional) - Path to input schema file
- `output` (string, optional) - Path to output schema file
- `storages` (object, optional) - Storage schema references
  - `dataset` (string) - Path to dataset schema file
  - `keyValueStore` (string) - Path to key-value store schema file
- `dockerfile` (string, optional) - Path to Dockerfile

**Important:** Always fill in the `generatedBy` property with the tool and model you're currently using (e.g., "Claude Code with Claude Sonnet 4.5") to help Apify improve documentation.
```

## File: `skills/apify-actor-development/references/dataset-schema.md`
```markdown
# Dataset Schema Reference

The dataset schema defines how your Actor's output data is structured, transformed, and displayed in the Output tab in the Apify Console.

## Examples

### JavaScript and TypeScript

Consider an example Actor that calls `Actor.pushData()` to store data into dataset:

```javascript
import { Actor } from 'apify';
// Initialize the JavaScript SDK
await Actor.init();

/**
 * Actor code
 */
await Actor.pushData({
    numericField: 10,
    pictureUrl: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png',
    linkUrl: 'https://google.com',
    textField: 'Google',
    booleanField: true,
    dateField: new Date(),
    arrayField: ['#hello', '#world'],
    objectField: {},
});

// Exit successfully
await Actor.exit();
```

### Python

Consider an example Actor that calls `Actor.push_data()` to store data into dataset:

```python
# Dataset push example (Python)
import asyncio
from datetime import datetime
from apify import Actor

async def main():
    await Actor.init()

    # Actor code
    await Actor.push_data({
        'numericField': 10,
        'pictureUrl': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png',
        'linkUrl': 'https://google.com',
        'textField': 'Google',
        'booleanField': True,
        'dateField': datetime.now().isoformat(),
        'arrayField': ['#hello', '#world'],
        'objectField': {},
    })

    # Exit successfully
    await Actor.exit()

if __name__ == '__main__':
    asyncio.run(main())
```

## Configuration

To set up the Actor's output tab UI, reference a dataset schema file in `.actor/actor.json`:

```json
{
    "actorSpecification": 1,
    "name": "book-library-scraper",
    "title": "Book Library Scraper",
    "version": "1.0.0",
    "storages": {
        "dataset": "./dataset_schema.json"
    }
}
```

Then create the dataset schema in `.actor/dataset_schema.json`:

```json
{
    "actorSpecification": 1,
    "fields": {},
    "views": {
        "overview": {
            "title": "Overview",
            "transformation": {
                "fields": [
                    "pictureUrl",
                    "linkUrl",
                    "textField",
                    "booleanField",
                    "arrayField",
                    "objectField",
                    "dateField",
                    "numericField"
                ]
            },
            "display": {
                "component": "table",
                "properties": {
                    "pictureUrl": {
                        "label": "Image",
                        "format": "image"
                    },
                    "linkUrl": {
                        "label": "Link",
                        "format": "link"
                    },
                    "textField": {
                        "label": "Text",
                        "format": "text"
                    },
                    "booleanField": {
                        "label": "Boolean",
                        "format": "boolean"
                    },
                    "arrayField": {
                        "label": "Array",
                        "format": "array"
                    },
                    "objectField": {
                        "label": "Object",
                        "format": "object"
                    },
                    "dateField": {
                        "label": "Date",
                        "format": "date"
                    },
                    "numericField": {
                        "label": "Number",
                        "format": "number"
                    }
                }
            }
        }
    }
}
```

## Structure

```json
{
    "actorSpecification": 1,
    "fields": {},
    "views": {
        "<VIEW_NAME>": {
            "title": "string (required)",
            "description": "string (optional)",
            "transformation": {
                "fields": ["string (required)"],
                "unwind": ["string (optional)"],
                "flatten": ["string (optional)"],
                "omit": ["string (optional)"],
                "limit": "integer (optional)",
                "desc": "boolean (optional)"
            },
            "display": {
                "component": "table (required)",
                "properties": {
                    "<FIELD_NAME>": {
                        "label": "string (optional)",
                        "format": "text|number|date|link|boolean|image|array|object (optional)"
                    }
                }
            }
        }
    }
}
```

## Properties

### Dataset Schema Properties

- `actorSpecification` (integer, required) - Specifies the version of dataset schema structure document (currently only version 1)
- `fields` (JSONSchema object, required) - Schema of one dataset object (use JsonSchema Draft 2020-12 or compatible)
- `views` (DatasetView object, required) - Object with API and UI views description

### DatasetView Properties

- `title` (string, required) - Visible in UI Output tab and API
- `description` (string, optional) - Only available in API response
- `transformation` (ViewTransformation object, required) - Data transformation applied when loading from Dataset API
- `display` (ViewDisplay object, required) - Output tab UI visualization definition

### ViewTransformation Properties

- `fields` (string[], required) - Fields to present in output (order matches column order)
- `unwind` (string[], optional) - Deconstructs nested children into parent object
- `flatten` (string[], optional) - Transforms nested object into flat structure
- `omit` (string[], optional) - Removes specified fields from output
- `limit` (integer, optional) - Maximum number of results (default: all)
- `desc` (boolean, optional) - Sort order (true = newest first)

### ViewDisplay Properties

- `component` (string, required) - Only `table` is available
- `properties` (Object, optional) - Keys matching `transformation.fields` with ViewDisplayProperty values

### ViewDisplayProperty Properties

- `label` (string, optional) - Table column header
- `format` (string, optional) - One of: `text`, `number`, `date`, `link`, `boolean`, `image`, `array`, `object`
```

## File: `skills/apify-actor-development/references/input-schema.md`
```markdown
# Input Schema Reference

The input schema defines the input parameters for an Actor. It's a JSON object comprising various field types supported by the Apify platform.

## Structure

```json
{
    "title": "<INPUT-SCHEMA-TITLE>",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        /* define input fields here */
    },
    "required": []
}
```

## Example

```json
{
    "title": "E-commerce Product Scraper Input",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        "startUrls": {
            "title": "Start URLs",
            "type": "array",
            "description": "URLs to start scraping from (category pages or product pages)",
            "editor": "requestListSources",
            "default": [{ "url": "https://example.com/category" }],
            "prefill": [{ "url": "https://example.com/category" }]
        },
        "followVariants": {
            "title": "Follow Product Variants",
            "type": "boolean",
            "description": "Whether to scrape product variants (different colors, sizes)",
            "default": true
        },
        "maxRequestsPerCrawl": {
            "title": "Max Requests per Crawl",
            "type": "integer",
            "description": "Maximum number of pages to scrape (0 = unlimited)",
            "default": 1000,
            "minimum": 0
        },
        "proxyConfiguration": {
            "title": "Proxy Configuration",
            "type": "object",
            "description": "Proxy settings for anti-bot protection",
            "editor": "proxy",
            "default": { "useApifyProxy": false }
        },
        "locale": {
            "title": "Locale",
            "type": "string",
            "description": "Language/country code for localized content",
            "default": "cs",
            "enum": ["cs", "en", "de", "sk"],
            "enumTitles": ["Czech", "English", "German", "Slovak"]
        }
    },
    "required": ["startUrls"]
}
```
```

## File: `skills/apify-actor-development/references/key-value-store-schema.md`
```markdown
# Key-Value Store Schema Reference

The key-value store schema organizes keys into logical groups called collections for easier data management.

## Examples

### JavaScript and TypeScript

Consider an example Actor that calls `Actor.setValue()` to save records into the key-value store:

```javascript
import { Actor } from 'apify';
// Initialize the JavaScript SDK
await Actor.init();

/**
 * Actor code
 */
await Actor.setValue('document-1', 'my text data', { contentType: 'text/plain' });

await Actor.setValue(`image-${imageID}`, imageBuffer, { contentType: 'image/jpeg' });

// Exit successfully
await Actor.exit();
```

### Python

Consider an example Actor that calls `Actor.set_value()` to save records into the key-value store:

```python
# Key-Value Store set example (Python)
import asyncio
from apify import Actor

async def main():
    await Actor.init()

    # Actor code
    await Actor.set_value('document-1', 'my text data', content_type='text/plain')

    image_id = '123'          # example placeholder
    image_buffer = b'...'     # bytes buffer with image data
    await Actor.set_value(f'image-{image_id}', image_buffer, content_type='image/jpeg')

    # Exit successfully
    await Actor.exit()

if __name__ == '__main__':
    asyncio.run(main())
```

## Configuration

To configure the key-value store schema, reference a schema file in `.actor/actor.json`:

```json
{
    "actorSpecification": 1,
    "name": "data-collector",
    "title": "Data Collector",
    "version": "1.0.0",
    "storages": {
        "keyValueStore": "./key_value_store_schema.json"
    }
}
```

Then create the key-value store schema in `.actor/key_value_store_schema.json`:

```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "Key-Value Store Schema",
    "collections": {
        "documents": {
            "title": "Documents",
            "description": "Text documents stored by the Actor",
            "keyPrefix": "document-"
        },
        "images": {
            "title": "Images",
            "description": "Images stored by the Actor",
            "keyPrefix": "image-",
            "contentTypes": ["image/jpeg"]
        }
    }
}
```

## Structure

```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "string (required)",
    "description": "string (optional)",
    "collections": {
        "<COLLECTION_NAME>": {
            "title": "string (required)",
            "description": "string (optional)",
            "key": "string (conditional - use key OR keyPrefix)",
            "keyPrefix": "string (conditional - use key OR keyPrefix)",
            "contentTypes": ["string (optional)"],
            "jsonSchema": "object (optional)"
        }
    }
}
```

## Properties

### Key-Value Store Schema Properties

- `actorKeyValueStoreSchemaVersion` (integer, required) - Version of key-value store schema structure document (currently only version 1)
- `title` (string, required) - Title of the schema
- `description` (string, optional) - Description of the schema
- `collections` (Object, required) - Object where each key is a collection ID and value is a Collection object

### Collection Properties

- `title` (string, required) - Collection title shown in UI tabs
- `description` (string, optional) - Description appearing in UI tooltips
- `key` (string, conditional) - Single specific key for this collection
- `keyPrefix` (string, conditional) - Prefix for keys included in this collection
- `contentTypes` (string[], optional) - Allowed content types for validation
- `jsonSchema` (object, optional) - JSON Schema Draft 07 format for `application/json` content type validation

Either `key` or `keyPrefix` must be specified for each collection, but not both.
```

## File: `skills/apify-actor-development/references/logging.md`
```markdown
# Actor Logging Reference

## JavaScript and TypeScript

**ALWAYS use the `apify/log` package for logging** - This package contains critical security logic including censoring sensitive data (Apify tokens, API keys, credentials) to prevent accidental exposure in logs.

### Available Log Levels in `apify/log`

The Apify log package provides the following methods for logging:

- `log.debug()` - Debug level logs (detailed diagnostic information)
- `log.info()` - Info level logs (general informational messages)
- `log.warning()` - Warning level logs (warning messages for potentially problematic situations)
- `log.warningOnce()` - Warning level logs (same warning message logged only once)
- `log.error()` - Error level logs (error messages for failures)
- `log.exception()` - Exception level logs (for exceptions with stack traces)
- `log.perf()` - Performance level logs (performance metrics and timing information)
- `log.deprecated()` - Deprecation level logs (warnings about deprecated code)
- `log.softFail()` - Soft failure logs (non-critical failures that don't stop execution, e.g., input validation errors, skipped items)
- `log.internal()` - Internal level logs (internal/system messages)

### Best Practices

- Use `log.debug()` for detailed operation-level diagnostics (inside functions)
- Use `log.info()` for general informational messages (API requests, successful operations)
- Use `log.warning()` for potentially problematic situations (validation failures, unexpected states)
- Use `log.error()` for actual errors and failures
- Use `log.exception()` for caught exceptions with stack traces

## Python

**ALWAYS use `Actor.log` for logging** - This logger contains critical security logic including censoring sensitive data (Apify tokens, API keys, credentials) to prevent accidental exposure in logs.

### Available Log Levels

The Apify Actor logger provides the following methods for logging:

- `Actor.log.debug()` - Debug level logs (detailed diagnostic information)
- `Actor.log.info()` - Info level logs (general informational messages)
- `Actor.log.warning()` - Warning level logs (warning messages for potentially problematic situations)
- `Actor.log.error()` - Error level logs (error messages for failures)
- `Actor.log.exception()` - Exception level logs (for exceptions with stack traces)

### Best Practices

- Use `Actor.log.debug()` for detailed operation-level diagnostics (inside functions)
- Use `Actor.log.info()` for general informational messages (API requests, successful operations)
- Use `Actor.log.warning()` for potentially problematic situations (validation failures, unexpected states)
- Use `Actor.log.error()` for actual errors and failures
- Use `Actor.log.exception()` for caught exceptions with stack traces
```

## File: `skills/apify-actor-development/references/output-schema.md`
```markdown
# Output Schema Reference

The Actor output schema builds upon the schemas for the dataset and key-value store. It specifies where an Actor stores its output and defines templates for accessing that output. Apify Console uses these output definitions to display run results.

## Structure

```json
{
    "actorOutputSchemaVersion": 1,
    "title": "<OUTPUT-SCHEMA-TITLE>",
    "properties": {
        /* define your outputs here */
    }
}
```

## Example

```json
{
    "actorOutputSchemaVersion": 1,
    "title": "Output schema of the files scraper",
    "properties": {
        "files": {
            "type": "string",
            "title": "Files",
            "template": "{{links.apiDefaultKeyValueStoreUrl}}/keys"
        },
        "dataset": {
            "type": "string",
            "title": "Dataset",
            "template": "{{links.apiDefaultDatasetUrl}}/items"
        }
    }
}
```

## Output Schema Template Variables

- `links` (object) - Contains quick links to most commonly used URLs
- `links.publicRunUrl` (string) - Public run url in format `https://console.apify.com/view/runs/:runId`
- `links.consoleRunUrl` (string) - Console run url in format `https://console.apify.com/actors/runs/:runId`
- `links.apiRunUrl` (string) - API run url in format `https://api.apify.com/v2/actor-runs/:runId`
- `links.apiDefaultDatasetUrl` (string) - API url of default dataset in format `https://api.apify.com/v2/datasets/:defaultDatasetId`
- `links.apiDefaultKeyValueStoreUrl` (string) - API url of default key-value store in format `https://api.apify.com/v2/key-value-stores/:defaultKeyValueStoreId`
- `links.containerRunUrl` (string) - URL of a webserver running inside the run in format `https://<containerId>.runs.apify.net/`
- `run` (object) - Contains information about the run same as it is returned from the `GET Run` API endpoint
- `run.defaultDatasetId` (string) - ID of the default dataset
- `run.defaultKeyValueStoreId` (string) - ID of the default key-value store
```

## File: `skills/apify-actor-development/references/standby-mode.md`
```markdown
# Actor Standby Mode Reference

## JavaScript and TypeScript

- **NEVER disable standby mode (`usesStandbyMode: false`) in `.actor/actor.json` without explicit permission** - Actor Standby mode solves this problem by letting you have the Actor ready in the background, waiting for the incoming HTTP requests. In a sense, the Actor behaves like a real-time web server or standard API server instead of running the logic once to process everything in batch. Always keep `usesStandbyMode: true` unless there is a specific documented reason to disable it
- **ALWAYS implement readiness probe handler for standby Actors** - Handle the `x-apify-container-server-readiness-probe` header at GET / endpoint to ensure proper Actor lifecycle management

You can recognize a standby Actor by checking the `usesStandbyMode` property in `.actor/actor.json`. Only implement the readiness probe if this property is set to `true`.

### Readiness Probe Implementation Example

```javascript
// Apify standby readiness probe at root path
app.get('/', (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    if (req.headers['x-apify-container-server-readiness-probe']) {
        res.end('Readiness probe OK\n');
    } else {
        res.end('Actor is ready\n');
    }
});
```

Key points:

- Detect the `x-apify-container-server-readiness-probe` header in incoming requests
- Respond with HTTP 200 status code for both readiness probe and normal requests
- This enables proper Actor lifecycle management in standby mode

## Python

- **NEVER disable standby mode (`usesStandbyMode: false`) in `.actor/actor.json` without explicit permission** - Actor Standby mode solves this problem by letting you have the Actor ready in the background, waiting for the incoming HTTP requests. In a sense, the Actor behaves like a real-time web server or standard API server instead of running the logic once to process everything in batch. Always keep `usesStandbyMode: true` unless there is a specific documented reason to disable it
- **ALWAYS implement readiness probe handler for standby Actors** - Handle the `x-apify-container-server-readiness-probe` header at GET / endpoint to ensure proper Actor lifecycle management

You can recognize a standby Actor by checking the `usesStandbyMode` property in `.actor/actor.json`. Only implement the readiness probe if this property is set to `true`.

### Readiness Probe Implementation Example

```python
# Apify standby readiness probe
from http.server import SimpleHTTPRequestHandler

class GetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle Apify standby readiness probe
        if 'x-apify-container-server-readiness-probe' in self.headers:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Readiness probe OK')
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Actor is ready')
```

Key points:

- Detect the `x-apify-container-server-readiness-probe` header in incoming requests
- Respond with HTTP 200 status code for both readiness probe and normal requests
- This enables proper Actor lifecycle management in standby mode
```

## File: `skills/apify-actorization/SKILL.md`
```markdown
---
name: apify-actorization
description: Convert existing projects into Apify Actors - serverless cloud programs. Actorize JavaScript/TypeScript (SDK with Actor.init/exit), Python (async context manager), or any language (CLI wrapper). Use when migrating code to Apify, wrapping CLI tools as Actors, or adding Actor SDK to existing projects.
---

# Apify Actorization

Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, and optionally produce structured JSON output.

## Quick Start

1. Run `apify init` in project root
2. Wrap code with SDK lifecycle (see language-specific section below)
3. Configure `.actor/input_schema.json`
4. Test with `apify run --input '{"key": "value"}'`
5. Deploy with `apify push`

## When to Use This Skill

- Converting an existing project to run on Apify platform
- Adding Apify SDK integration to a project
- Wrapping a CLI tool or script as an Actor
- Migrating a Crawlee project to Apify

## Prerequisites

Verify `apify` CLI is installed:

```bash
apify --help
```

If not installed:

```bash
curl -fsSL https://apify.com/install-cli.sh | bash

# Or (Mac): brew install apify-cli
# Or (Windows): irm https://apify.com/install-cli.ps1 | iex
# Or: npm install -g apify-cli
```

Verify CLI is logged in:

```bash
apify info  # Should return your username
```

If not logged in, check if `APIFY_TOKEN` environment variable is defined. If not, ask the user to generate one at https://console.apify.com/settings/integrations, then:

```bash
apify login -t $APIFY_TOKEN
```

## Actorization Checklist

Copy this checklist to track progress:

- [ ] Step 1: Analyze project (language, entry point, inputs, outputs)
- [ ] Step 2: Run `apify init` to create Actor structure
- [ ] Step 3: Apply language-specific SDK integration
- [ ] Step 4: Configure `.actor/input_schema.json`
- [ ] Step 5: Configure `.actor/output_schema.json` (if applicable)
- [ ] Step 6: Update `.actor/actor.json` metadata
- [ ] Step 7: Test locally with `apify run`
- [ ] Step 8: Deploy with `apify push`

## Step 1: Analyze the Project

Before making changes, understand the project:

1. **Identify the language** - JavaScript/TypeScript, Python, or other
2. **Find the entry point** - The main file that starts execution
3. **Identify inputs** - Command-line arguments, environment variables, config files
4. **Identify outputs** - Files, console output, API responses
5. **Check for state** - Does it need to persist data between runs?

## Step 2: Initialize Actor Structure

Run in the project root:

```bash
apify init
```

This creates:
- `.actor/actor.json` - Actor configuration and metadata
- `.actor/input_schema.json` - Input definition for the Apify Console
- `Dockerfile` (if not present) - Container image definition

## Step 3: Apply Language-Specific Changes

Choose based on your project's language:

- **JavaScript/TypeScript**: See [js-ts-actorization.md](references/js-ts-actorization.md)
- **Python**: See [python-actorization.md](references/python-actorization.md)
- **Other Languages (CLI-based)**: See [cli-actorization.md](references/cli-actorization.md)

### Quick Reference

| Language | Install | Wrap Code |
|----------|---------|-----------|
| JS/TS | `npm install apify` | `await Actor.init()` ... `await Actor.exit()` |
| Python | `pip install apify` | `async with Actor:` |
| Other | Use CLI in wrapper script | `apify actor:get-input` / `apify actor:push-data` |

## Steps 4-6: Configure Schemas

See [schemas-and-output.md](references/schemas-and-output.md) for detailed configuration of:
- Input schema (`.actor/input_schema.json`)
- Output schema (`.actor/output_schema.json`)
- Actor configuration (`.actor/actor.json`)
- State management (request queues, key-value stores)

Validate schemas against `@apify/json_schemas` npm package.

## Step 7: Test Locally

Run the actor with inline input (for JS/TS and Python actors):

```bash
apify run --input '{"startUrl": "https://example.com", "maxItems": 10}'
```

Or use an input file:

```bash
apify run --input-file ./test-input.json
```

**Important:** Always use `apify run`, not `npm start` or `python main.py`. The CLI sets up the proper environment and storage.

## Step 8: Deploy

```bash
apify push
```

This uploads and builds your actor on the Apify platform.

## Monetization (Optional)

After deploying, you can monetize your actor in the Apify Store. The recommended model is **Pay Per Event (PPE)**:

- Per result/item scraped
- Per page processed
- Per API call made

Configure PPE in the Apify Console under Actor > Monetization. Charge for events in your code with `await Actor.charge('result')`.

Other options: **Rental** (monthly subscription) or **Free** (open source).

## Pre-Deployment Checklist

- [ ] `.actor/actor.json` exists with correct name and description
- [ ] `.actor/actor.json` validates against `@apify/json_schemas` (`actor.schema.json`)
- [ ] `.actor/input_schema.json` defines all required inputs
- [ ] `.actor/input_schema.json` validates against `@apify/json_schemas` (`input.schema.json`)
- [ ] `.actor/output_schema.json` defines output structure (if applicable)
- [ ] `.actor/output_schema.json` validates against `@apify/json_schemas` (`output.schema.json`)
- [ ] `Dockerfile` is present and builds successfully
- [ ] `Actor.init()` / `Actor.exit()` wraps main code (JS/TS)
- [ ] `async with Actor:` wraps main code (Python)
- [ ] Inputs are read via `Actor.getInput()` / `Actor.get_input()`
- [ ] Outputs use `Actor.pushData()` or key-value store
- [ ] `apify run` executes successfully with test input
- [ ] `generatedBy` is set in actor.json meta section

## Apify MCP Tools

If MCP server is configured, use these tools for documentation:

- `search-apify-docs` - Search documentation
- `fetch-apify-docs` - Get full doc pages

Otherwise, the MCP Server url: `https://mcp.apify.com/?tools=docs`.

## Resources

- [Actorization Academy](https://docs.apify.com/academy/actorization) - Comprehensive guide
- [Apify SDK for JavaScript](https://docs.apify.com/sdk/js) - Full SDK reference
- [Apify SDK for Python](https://docs.apify.com/sdk/python) - Full SDK reference
- [Apify CLI Reference](https://docs.apify.com/cli) - CLI commands
- [Actor Specification](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md) - Complete specification
```

## File: `skills/apify-actorization/references/cli-actorization.md`
```markdown
# CLI-Based Actorization

For languages without an SDK (Go, Rust, Java, etc.), create a wrapper script that uses the Apify CLI.

## Create Wrapper Script

Create `start.sh` in project root:

```bash
#!/bin/bash
set -e

# Get input from Apify key-value store
INPUT=$(apify actor:get-input)

# Parse input values (adjust based on your input schema)
MY_PARAM=$(echo "$INPUT" | jq -r '.myParam // "default"')

# Run your application with the input
./your-application --param "$MY_PARAM"

# If your app writes to a file, push it to key-value store
# apify actor:set-value OUTPUT --contentType application/json < output.json

# Or push structured data to dataset
# apify actor:push-data '{"result": "value"}'
```

## Update Dockerfile

Reference the [cli-start template Dockerfile](https://github.com/apify/actor-templates/blob/master/templates/cli-start/Dockerfile) which includes the `ubi` utility for installing binaries from GitHub releases.

```dockerfile
FROM apify/actor-node:20

# Install ubi for easy GitHub release installation
RUN curl --silent --location \
    https://raw.githubusercontent.com/houseabsolute/ubi/master/bootstrap/bootstrap-ubi.sh | sh

# Install your CLI tool from GitHub releases (example)
# RUN ubi --project your-org/your-tool --in /usr/local/bin

# Or install apify-cli and jq manually
RUN npm install -g apify-cli
RUN apt-get update && apt-get install -y jq

# Copy your application
COPY . .

# Build your application if needed
# RUN ./build.sh

# Make start script executable
RUN chmod +x start.sh

# Run the wrapper script
CMD ["./start.sh"]
```

## Testing CLI-Based Actors

For CLI-based actors (shell wrapper scripts), you may need to test the underlying application directly with mock input, as `apify run` requires a Node.js or Python entry point.

Test your wrapper script locally:

```bash
# Set up mock input
export INPUT='{"myParam": "test-value"}'

# Run wrapper script
./start.sh
```

## CLI Commands Reference

| Command | Description |
|---------|-------------|
| `apify actor:get-input` | Get input JSON from key-value store |
| `apify actor:set-value KEY` | Store value in key-value store |
| `apify actor:push-data JSON` | Push data to dataset |
| `apify actor:get-value KEY` | Retrieve value from key-value store |
```

## File: `skills/apify-actorization/references/js-ts-actorization.md`
```markdown
# JavaScript/TypeScript Actorization

## Install the Apify SDK

```bash
npm install apify
```

## Wrap Main Code with Actor Lifecycle

```javascript
import { Actor } from 'apify';

// Initialize connection to Apify platform
await Actor.init();

// ============================================
// Your existing code goes here
// ============================================

// Example: Get input from Apify Console or API
const input = await Actor.getInput();
console.log('Input:', input);

// Example: Your crawler or processing logic
// const crawler = new PlaywrightCrawler({ ... });
// await crawler.run([input.startUrl]);

// Example: Push results to dataset
// await Actor.pushData({ result: 'data' });

// ============================================
// End of your code
// ============================================

// Graceful shutdown
await Actor.exit();
```

## Key Points

- `Actor.init()` configures storage to use Apify API when running on platform
- `Actor.exit()` handles graceful shutdown and cleanup
- Both calls must be awaited
- Local execution remains unchanged - the SDK automatically detects the environment

## Crawlee Projects

Crawlee projects require minimal changes - just wrap with Actor lifecycle:

```javascript
import { Actor } from 'apify';
import { PlaywrightCrawler } from 'crawlee';

await Actor.init();

// Get and validate input
const input = await Actor.getInput();
const {
    startUrl = 'https://example.com',
    maxItems = 100,
} = input ?? {};

let itemCount = 0;

const crawler = new PlaywrightCrawler({
    requestHandler: async ({ page, request, pushData }) => {
        if (itemCount >= maxItems) return;

        const title = await page.title();
        await pushData({ url: request.url, title });
        itemCount++;
    },
});

await crawler.run([startUrl]);

await Actor.exit();
```

## Express/HTTP Servers

For web servers, use standby mode in actor.json:

```json
{
    "actorSpecification": 1,
    "name": "my-api",
    "usesStandbyMode": true
}
```

Then implement readiness probe. See [standby-mode.md](../../apify-actor-development/references/standby-mode.md).

## Batch Processing Scripts

```javascript
import { Actor } from 'apify';

await Actor.init();

const input = await Actor.getInput();
const items = input.items || [];

for (const item of items) {
    const result = processItem(item);
    await Actor.pushData(result);
}

await Actor.exit();
```
```

## File: `skills/apify-actorization/references/python-actorization.md`
```markdown
# Python Actorization

## Install the Apify SDK

```bash
pip install apify
```

## Wrap Main Function with Actor Context Manager

```python
import asyncio
from apify import Actor

async def main() -> None:
    async with Actor:
        # ============================================
        # Your existing code goes here
        # ============================================

        # Example: Get input from Apify Console or API
        actor_input = await Actor.get_input()
        print(f'Input: {actor_input}')

        # Example: Your crawler or processing logic
        # crawler = PlaywrightCrawler(...)
        # await crawler.run([actor_input.get('startUrl')])

        # Example: Push results to dataset
        # await Actor.push_data({'result': 'data'})

        # ============================================
        # End of your code
        # ============================================

if __name__ == '__main__':
    asyncio.run(main())
```

## Key Points

- `async with Actor:` handles both initialization and cleanup
- Automatically manages platform event listeners and graceful shutdown
- Local execution remains unchanged - the SDK automatically detects the environment

## Crawlee Python Projects

```python
import asyncio
from apify import Actor
from crawlee.playwright_crawler import PlaywrightCrawler

async def main() -> None:
    async with Actor:
        # Get and validate input
        actor_input = await Actor.get_input() or {}
        start_url = actor_input.get('startUrl', 'https://example.com')
        max_items = actor_input.get('maxItems', 100)

        item_count = 0

        async def request_handler(context):
            nonlocal item_count
            if item_count >= max_items:
                return

            title = await context.page.title()
            await context.push_data({'url': context.request.url, 'title': title})
            item_count += 1

        crawler = PlaywrightCrawler(request_handler=request_handler)
        await crawler.run([start_url])

if __name__ == '__main__':
    asyncio.run(main())
```

## Batch Processing Scripts

```python
import asyncio
from apify import Actor

async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        items = actor_input.get('items', [])

        for item in items:
            result = process_item(item)
            await Actor.push_data(result)

if __name__ == '__main__':
    asyncio.run(main())
```
```

## File: `skills/apify-actorization/references/schemas-and-output.md`
```markdown
# Schemas and Output Configuration

## Input Schema

Map your application's inputs to `.actor/input_schema.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`input.schema.json`).

```json
{
    "title": "My Actor Input",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        "startUrl": {
            "title": "Start URL",
            "type": "string",
            "description": "The URL to start processing from",
            "editor": "textfield",
            "prefill": "https://example.com"
        },
        "maxItems": {
            "title": "Max Items",
            "type": "integer",
            "description": "Maximum number of items to process",
            "default": 100,
            "minimum": 1
        }
    },
    "required": ["startUrl"]
}
```

### Mapping Guidelines

- Command-line arguments → input schema properties
- Environment variables → input schema or Actor env vars in actor.json
- Config files → input schema with object/array types
- Flatten deeply nested structures for better UX

## Output Schema

Define output structure in `.actor/output_schema.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`output.schema.json`).

### For Table-Like Data (Multiple Items)

- Use `Actor.pushData()` (JS) or `Actor.push_data()` (Python)
- Each item becomes a row in the dataset

### For Single Files or Blobs

- Use key-value store: `Actor.setValue()` / `Actor.set_value()`
- Get the public URL and include it in the dataset:

```javascript
// Store file with public access
await Actor.setValue('report.pdf', pdfBuffer, { contentType: 'application/pdf' });

// Get the public URL
const storeInfo = await Actor.openKeyValueStore();
const publicUrl = `https://api.apify.com/v2/key-value-stores/${storeInfo.id}/records/report.pdf`;

// Include URL in dataset output
await Actor.pushData({ reportUrl: publicUrl });
```

### For Multiple Files with a Common Prefix (Collections)

```javascript
// Store multiple files with a prefix
for (const [name, data] of files) {
    await Actor.setValue(`screenshots/${name}`, data, { contentType: 'image/png' });
}
// Files are accessible at: .../records/screenshots%2F{name}
```

## Actor Configuration (actor.json)

Configure `.actor/actor.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`actor.schema.json`).

```json
{
    "actorSpecification": 1,
    "name": "my-actor",
    "title": "My Actor",
    "description": "Brief description of what the actor does",
    "version": "1.0.0",
    "meta": {
        "templateId": "ts_empty",
        "generatedBy": "Claude Code with Claude Opus 4.5"
    },
    "input": "./input_schema.json",
    "dockerfile": "../Dockerfile"
}
```

**Important:** Fill in the `generatedBy` property with the tool/model used.

## State Management

### Request Queue - For Pausable Task Processing

The request queue works for any task processing, not just web scraping. Use a dummy URL with custom `uniqueKey` and `userData` for non-URL tasks:

```javascript
const requestQueue = await Actor.openRequestQueue();

// Add tasks to the queue (works for any processing, not just URLs)
await requestQueue.addRequest({
    url: 'https://placeholder.local',  // Dummy URL for non-scraping tasks
    uniqueKey: `task-${taskId}`,       // Unique identifier for deduplication
    userData: { itemId: 123, action: 'process' },  // Your custom task data
});

// Process tasks from the queue (with Crawlee)
const crawler = new BasicCrawler({
    requestQueue,
    requestHandler: async ({ request }) => {
        const { itemId, action } = request.userData;
        // Process your task using userData
        await processTask(itemId, action);
    },
});
await crawler.run();

// Or manually consume without Crawlee:
let request;
while ((request = await requestQueue.fetchNextRequest())) {
    await processTask(request.userData);
    await requestQueue.markRequestHandled(request);
}
```

### Key-Value Store - For Checkpoint State

```javascript
// Save state
await Actor.setValue('STATE', { processedCount: 100 });

// Restore state on restart
const state = await Actor.getValue('STATE') || { processedCount: 0 };
```
```

## File: `skills/apify-generate-output-schema/SKILL.md`
```markdown
---
name: apify-generate-output-schema
description: Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) for an Apify Actor by analyzing its source code. Use when creating or updating Actor output schemas.
---

# Generate Actor Output Schema

You are generating output schema files for an Apify Actor. The output schema tells Apify Console how to display run results. You will analyze the Actor's source code, create `dataset_schema.json`, `output_schema.json`, and `key_value_store_schema.json` (if the Actor uses key-value store), and update `actor.json`.

## Core Principles

- **Analyze code first**: Read the Actor's source to understand what data it actually pushes to the dataset — never guess
- **Every field is nullable**: APIs and websites are unpredictable — always set `"nullable": true`
- **Anonymize examples**: Never use real user IDs, usernames, or personal data in examples
- **Verify against code**: If TypeScript types exist, cross-check the schema against both the type definition AND the code that produces the values
- **Reuse existing patterns**: Before generating schemas, check if other Actors in the same repository already have output schemas — match their structure, naming conventions, description style, and formatting
- **Don't reinvent the wheel**: Reuse existing type definitions, interfaces, and utilities from the codebase instead of creating duplicate definitions

---

## Phase 1: Discover Actor Structure

**Goal**: Locate the Actor and understand its output

Initial request: $ARGUMENTS

**Actions**:
1. Create todo list with all phases
2. Find the `.actor/` directory containing `actor.json`
3. Read `actor.json` to understand the Actor's configuration
4. Check if `dataset_schema.json`, `output_schema.json`, and `key_value_store_schema.json` already exist
5. **Search for existing schemas in the repository**: Look for other `.actor/` directories or schema files (e.g., `**/dataset_schema.json`, `**/output_schema.json`, `**/key_value_store_schema.json`) to learn the repo's conventions — match their description style, field naming, example formatting, and overall structure
6. Find all places where data is pushed to the dataset:
   - **JavaScript/TypeScript**: Search for `Actor.pushData(`, `dataset.pushData(`, `Dataset.pushData(`
   - **Python**: Search for `Actor.push_data(`, `dataset.push_data(`, `Dataset.push_data(`
7. Find all places where data is stored in the key-value store:
   - **JavaScript/TypeScript**: Search for `Actor.setValue(`, `keyValueStore.setValue(`, `KeyValueStore.setValue(`
   - **Python**: Search for `Actor.set_value(`, `key_value_store.set_value(`, `KeyValueStore.set_value(`
8. Find output type definitions — **reuse them directly** instead of recreating from scratch:
   - **TypeScript**: Look for output type interfaces/types (e.g., in `src/types/`, `src/types/output.ts`). If an interface or type already defines the output shape, derive the schema fields from it — do not create a parallel definition
   - **Python**: Look for TypedDict, dataclass, or Pydantic model definitions. Use the existing field names, types, and docstrings as the source of truth
9. Check for existing shared schema utilities or helper functions in the codebase that handle schema generation or validation — reuse them rather than creating new logic
10. If inline `storages.dataset` or `storages.keyValueStore` config exists in `actor.json`, note it for migration

Present findings to user: list all discovered dataset output fields, key-value store keys, their types, and where they come from.

---

## Phase 2: Generate `dataset_schema.json`

**Goal**: Create a complete dataset schema with field definitions and display views

### File structure

```json
{
    "actorSpecification": 1,
    "fields": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            // ALL output fields here — every field the Actor can produce,
            // not just the ones shown in the overview view
        },
        "required": [],
        "additionalProperties": true
    },
    "views": {
        "overview": {
            "title": "Overview",
            "description": "Most important fields at a glance",
            "transformation": {
                "fields": [
                    // 8-12 most important field names
                ]
            },
            "display": {
                "component": "table",
                "properties": {
                    // Display config for each overview field
                }
            }
        }
    }
}
```

### Consistency with existing schemas

If existing output schemas were found in the repository during Phase 1 (step 5), follow their conventions:
- Match the **description writing style** (sentence case vs. lowercase, period vs. no period, etc.)
- Match the **field naming convention** (camelCase vs. snake_case) — this must also match the actual keys produced by the Actor code
- Match the **example value style** (e.g., date formats, URL patterns, placeholder names)
- Match the **view structure** (number of fields in overview, display format choices)
- Match the **JSON formatting** (indentation, property ordering, spacing) — all schemas in the same repository must use identical formatting, including standalone Actors

When the Actor code already has well-defined TypeScript interfaces or Python type classes, derive fields directly from those types rather than re-analyzing pushData/push_data calls from scratch. The type definition is the canonical source.

### Hard rules (no exceptions)

| Rule | Detail |
|------|--------|
| **All fields in `properties`** | The `fields.properties` object must contain **every** field the Actor can output, not just the fields shown in the overview view. The views section selects a subset for display — the `properties` section must be the complete superset |
| `"nullable": true` | On **every** field — APIs are unpredictable |
| `"additionalProperties": true` | On the **top-level `fields` object** AND on **every nested object** within `properties`. This is the most commonly missed rule — it must appear at both levels |
| `"required": []` | Always empty array — on the **top-level `fields` object** AND on **every nested object** within `properties` |
| Anonymized examples | No real user IDs, usernames, or content |
| `"type"` required with `"nullable"` | AJV rejects `nullable` without a `type` on the same field |

> **Warning — most common mistakes**:
> 1. Only including fields that appear in the overview view. The `fields.properties` must list ALL output fields, even if they are not in the `views` section.
> 2. Only adding `"required": []` and `"additionalProperties": true` on nested object-type properties but forgetting them on the top-level `fields` object. Both levels need them.

> **Note**: `nullable` is an Apify-specific extension to JSON Schema draft-07. It is intentional and correct.

### Field type patterns

**String field:**
```json
"title": {
    "type": "string",
    "description": "Title of the scraped item",
    "nullable": true,
    "example": "Example Item Title"
}
```

**Number field:**
```json
"viewCount": {
    "type": "number",
    "description": "Number of views",
    "nullable": true,
    "example": 15000
}
```

**Boolean field:**
```json
"isVerified": {
    "type": "boolean",
    "description": "Whether the account is verified",
    "nullable": true,
    "example": true
}
```

**Array field:**
```json
"hashtags": {
    "type": "array",
    "description": "Hashtags associated with the item",
    "items": { "type": "string" },
    "nullable": true,
    "example": ["#example", "#demo"]
}
```

**Nested object field:**
```json
"authorInfo": {
    "type": "object",
    "description": "Information about the author",
    "properties": {
        "name": { "type": "string", "nullable": true },
        "url": { "type": "string", "nullable": true }
    },
    "required": [],
    "additionalProperties": true,
    "nullable": true,
    "example": { "name": "Example Author", "url": "https://example.com/author" }
}
```

**Enum field:**
```json
"contentType": {
    "type": "string",
    "description": "Type of content",
    "enum": ["article", "video", "image"],
    "nullable": true,
    "example": "article"
}
```

**Union type (e.g., TypeScript `ObjectType | string`):**
```json
"metadata": {
    "type": ["object", "string"],
    "description": "Structured metadata object, or error string if unavailable",
    "nullable": true,
    "example": { "key": "value" }
}
```

### Anonymized example values

Use realistic but generic values. Follow platform ID format conventions:

| Field type | Example approach |
|---|---|
| IDs | Match platform format and length (e.g., 11 chars for YouTube video IDs) |
| Usernames | `"exampleuser"`, `"sampleuser123"` |
| Display names | `"Example Channel"`, `"Sample Author"` |
| URLs | Use platform's standard URL format with fake IDs |
| Dates | `"2025-01-15T12:00:00.000Z"` (ISO 8601) |
| Text content | Generic descriptive text, e.g., `"This is an example description."` |

### Views section

- `transformation.fields`: List 8–12 most important field names (order = column order in UI)
- `display.properties`: One entry per overview field with `label` and `format`
- Available formats: `"text"`, `"number"`, `"date"`, `"link"`, `"boolean"`, `"image"`, `"array"`, `"object"`

Pick fields that give users the most useful at-a-glance summary of the data.

---

## Phase 3: Generate `key_value_store_schema.json` (if applicable)

**Goal**: Define key-value store collections if the Actor stores data in the key-value store

> **Skip this phase** if no `Actor.setValue()` / `Actor.set_value()` calls were found in Phase 1 (beyond the default `INPUT` key).

### File structure

```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "<Descriptive title — what the key-value store contains>",
    "description": "<One sentence describing the stored data>",
    "collections": {
        "<collectionName>": {
            "title": "<Human-readable title>",
            "description": "<What this collection contains>",
            "keyPrefix": "<prefix->"
        }
    }
}
```

### How to identify collections

Group the discovered `setValue` / `set_value` calls by key pattern:

1. **Fixed keys** (e.g., `"RESULTS"`, `"summary"`) — use `"key"` (exact match)
2. **Dynamic keys with a prefix** (e.g., `"screenshot-${id}"`, `f"image-{name}"`) — use `"keyPrefix"`

Each group becomes a collection.

### Collection properties

| Property | Required | Description |
|----------|----------|-------------|
| `title` | Yes | Shown in UI tabs |
| `description` | No | Shown in UI tooltips |
| `key` | Conditional | Exact key for single-key collections (use `key` OR `keyPrefix`, not both) |
| `keyPrefix` | Conditional | Prefix for multi-key collections (use `key` OR `keyPrefix`, not both) |
| `contentTypes` | No | Restrict allowed MIME types (e.g., `["image/jpeg"]`, `["application/json"]`) |
| `jsonSchema` | No | JSON Schema draft-07 for validating `application/json` content |

### Examples

**Single file output (e.g., a report):**
```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "Analysis Results",
    "description": "Key-value store containing analysis output",
    "collections": {
        "report": {
            "title": "Report",
            "description": "Final analysis report",
            "key": "REPORT",
            "contentTypes": ["application/json"]
        }
    }
}
```

**Multiple files with prefix (e.g., screenshots):**
```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "Scraped Files",
    "description": "Key-value store containing downloaded files and screenshots",
    "collections": {
        "screenshots": {
            "title": "Screenshots",
            "description": "Page screenshots captured during scraping",
            "keyPrefix": "screenshot-",
            "contentTypes": ["image/png", "image/jpeg"]
        },
        "documents": {
            "title": "Documents",
            "description": "Downloaded document files",
            "keyPrefix": "doc-",
            "contentTypes": ["application/pdf", "text/html"]
        }
    }
}
```

---

## Phase 4: Generate `output_schema.json`

**Goal**: Create the output schema that tells Apify Console where to find results

For most Actors that push data to a dataset, this is a minimal file:

```json
{
    "actorOutputSchemaVersion": 1,
    "title": "<Descriptive title — what the Actor returns>",
    "description": "<One sentence describing the output data>",
    "properties": {
        "dataset": {
            "type": "string",
            "title": "Results",
            "description": "Dataset containing all scraped data",
            "template": "{{links.apiDefaultDatasetUrl}}/items"
        }
    }
}
```

> **Critical**: Each property entry **must** include `"type": "string"` — this is an Apify-specific convention. The Apify meta-validator rejects properties without it (and rejects `"type": "object"` — only `"string"` is valid here).

If `key_value_store_schema.json` was generated in Phase 3, add a second property:
```json
"files": {
    "type": "string",
    "title": "Files",
    "description": "Key-value store containing downloaded files",
    "template": "{{links.apiDefaultKeyValueStoreUrl}}/keys"
}
```

### Available template variables

- `{{links.apiDefaultDatasetUrl}}` — API URL of default dataset
- `{{links.apiDefaultKeyValueStoreUrl}}` — API URL of default key-value store
- `{{links.publicRunUrl}}` — Public run URL
- `{{links.consoleRunUrl}}` — Console run URL
- `{{links.apiRunUrl}}` — API run URL
- `{{links.containerRunUrl}}` — URL of webserver running inside the run
- `{{run.defaultDatasetId}}` — ID of the default dataset
- `{{run.defaultKeyValueStoreId}}` — ID of the default key-value store

---

## Phase 5: Update `actor.json`

**Goal**: Wire the schema files into the Actor configuration

**Actions**:
1. Read the current `actor.json`
2. Add or update the `storages.dataset` reference:
   ```json
   "storages": {
       "dataset": "./dataset_schema.json"
   }
   ```
3. If `key_value_store_schema.json` was generated, add the reference:
   ```json
   "storages": {
       "dataset": "./dataset_schema.json",
       "keyValueStore": "./key_value_store_schema.json"
   }
   ```
4. Add or update the `output` reference:
   ```json
   "output": "./output_schema.json"
   ```
5. If `actor.json` had inline `storages.dataset` or `storages.keyValueStore` objects (not string paths), migrate their content into the respective schema files and replace the inline objects with file path strings

---

## Phase 6: Review and Validate

**Goal**: Ensure correctness and completeness

**Checklist**:
- [ ] **Every** output field from the source code is in `dataset_schema.json` `fields.properties` — not just the overview view fields but ALL fields the Actor can produce
- [ ] Every field has `"nullable": true`
- [ ] The **top-level `fields` object** has both `"additionalProperties": true` and `"required": []`
- [ ] Every **nested object** within `properties` also has `"additionalProperties": true` and `"required": []`
- [ ] Every field has a `"description"` and an `"example"`
- [ ] All example values are anonymized
- [ ] `"type"` is present on every field that has `"nullable"`
- [ ] Views list 8–12 most useful fields with correct display formats
- [ ] `output_schema.json` has `"type": "string"` on every property
- [ ] If key-value store is used: `key_value_store_schema.json` has collections matching all `setValue`/`set_value` calls
- [ ] If key-value store is used: each collection uses either `key` or `keyPrefix` (not both)
- [ ] `actor.json` references all generated schema files
- [ ] Schema field names match the actual keys in the code (camelCase/snake_case consistency)
- [ ] If existing schemas were found in the repo, the new schema follows their conventions (description style, example format, view structure)
- [ ] Schema fields are derived from existing type definitions (interfaces, TypedDicts, dataclasses) where available — no duplicated or divergent field definitions

Present the generated schemas to the user for review before writing them.

---

## Phase 7: Summary

**Goal**: Document what was created

Report:
- Files created or updated
- Number of fields in the dataset schema
- Number of collections in the key-value store schema (if generated)
- Fields selected for the overview view
- Any fields that need user clarification (ambiguous types, unclear nullability)
- Suggested next steps (test locally with `apify run`, verify output tab in Console)
```

## File: `skills/apify-ultimate-scraper/SKILL.md`
```markdown
---
name: apify-ultimate-scraper
description: Universal AI-powered web scraper for any platform. Scrape data from Instagram, Facebook, TikTok, YouTube, Google Maps, Google Search, Google Trends, Booking.com, and TripAdvisor. Use for lead generation, brand monitoring, competitor analysis, influencer discovery, trend research, content analytics, audience analysis, or any data extraction task.
---

# Universal Web Scraper

AI-driven data extraction from 55+ Actors across all major platforms. This skill automatically selects the best Actor for your task.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Understand user goal and select Actor
- [ ] Step 2: Fetch Actor schema
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the scraper script
- [ ] Step 5: Summarize results and offer follow-ups
```

### Step 1: Understand User Goal and Select Actor

First, understand what the user wants to achieve. Then select the best Actor from the options below.

#### Instagram Actors (12)

| Actor ID | Best For |
|----------|----------|
| `apify/instagram-profile-scraper` | Profile data, follower counts, bio info |
| `apify/instagram-post-scraper` | Individual post details, engagement metrics |
| `apify/instagram-comment-scraper` | Comment extraction, sentiment analysis |
| `apify/instagram-hashtag-scraper` | Hashtag content, trending topics |
| `apify/instagram-hashtag-stats` | Hashtag performance metrics |
| `apify/instagram-reel-scraper` | Reels content and metrics |
| `apify/instagram-search-scraper` | Search users, places, hashtags |
| `apify/instagram-tagged-scraper` | Posts tagged with specific accounts |
| `apify/instagram-followers-count-scraper` | Follower count tracking |
| `apify/instagram-scraper` | Comprehensive Instagram data |
| `apify/instagram-api-scraper` | API-based Instagram access |
| `apify/export-instagram-comments-posts` | Bulk comment/post export |

#### Facebook Actors (14)

| Actor ID | Best For |
|----------|----------|
| `apify/facebook-pages-scraper` | Page data, metrics, contact info |
| `apify/facebook-page-contact-information` | Emails, phones, addresses from pages |
| `apify/facebook-posts-scraper` | Post content and engagement |
| `apify/facebook-comments-scraper` | Comment extraction |
| `apify/facebook-likes-scraper` | Reaction analysis |
| `apify/facebook-reviews-scraper` | Page reviews |
| `apify/facebook-groups-scraper` | Group content and members |
| `apify/facebook-events-scraper` | Event data |
| `apify/facebook-ads-scraper` | Ad creative and targeting |
| `apify/facebook-search-scraper` | Search results |
| `apify/facebook-reels-scraper` | Reels content |
| `apify/facebook-photos-scraper` | Photo extraction |
| `apify/facebook-marketplace-scraper` | Marketplace listings |
| `apify/facebook-followers-following-scraper` | Follower/following lists |

#### TikTok Actors (14)

| Actor ID | Best For |
|----------|----------|
| `clockworks/tiktok-scraper` | Comprehensive TikTok data |
| `clockworks/free-tiktok-scraper` | Free TikTok extraction |
| `clockworks/tiktok-profile-scraper` | Profile data |
| `clockworks/tiktok-video-scraper` | Video details and metrics |
| `clockworks/tiktok-comments-scraper` | Comment extraction |
| `clockworks/tiktok-followers-scraper` | Follower lists |
| `clockworks/tiktok-user-search-scraper` | Find users by keywords |
| `clockworks/tiktok-hashtag-scraper` | Hashtag content |
| `clockworks/tiktok-sound-scraper` | Trending sounds |
| `clockworks/tiktok-ads-scraper` | Ad content |
| `clockworks/tiktok-discover-scraper` | Discover page content |
| `clockworks/tiktok-explore-scraper` | Explore content |
| `clockworks/tiktok-trends-scraper` | Trending content |
| `clockworks/tiktok-live-scraper` | Live stream data |

#### YouTube Actors (5)

| Actor ID | Best For |
|----------|----------|
| `streamers/youtube-scraper` | Video data and metrics |
| `streamers/youtube-channel-scraper` | Channel information |
| `streamers/youtube-comments-scraper` | Comment extraction |
| `streamers/youtube-shorts-scraper` | Shorts content |
| `streamers/youtube-video-scraper-by-hashtag` | Videos by hashtag |

#### Google Maps Actors (4)

| Actor ID | Best For |
|----------|----------|
| `compass/crawler-google-places` | Business listings, ratings, contact info |
| `compass/google-maps-extractor` | Detailed business data |
| `compass/Google-Maps-Reviews-Scraper` | Review extraction |
| `poidata/google-maps-email-extractor` | Email discovery from listings |

#### Other Actors (6)

| Actor ID | Best For |
|----------|----------|
| `apify/google-search-scraper` | Google search results |
| `apify/google-trends-scraper` | Google Trends data |
| `voyager/booking-scraper` | Booking.com hotel data |
| `voyager/booking-reviews-scraper` | Booking.com reviews |
| `maxcopell/tripadvisor-reviews` | TripAdvisor reviews |
| `vdrmota/contact-info-scraper` | Contact enrichment from URLs |

---

#### Actor Selection by Use Case

| Use Case | Primary Actors |
|----------|---------------|
| **Lead Generation** | `compass/crawler-google-places`, `poidata/google-maps-email-extractor`, `vdrmota/contact-info-scraper` |
| **Influencer Discovery** | `apify/instagram-profile-scraper`, `clockworks/tiktok-profile-scraper`, `streamers/youtube-channel-scraper` |
| **Brand Monitoring** | `apify/instagram-tagged-scraper`, `apify/instagram-hashtag-scraper`, `compass/Google-Maps-Reviews-Scraper` |
| **Competitor Analysis** | `apify/facebook-pages-scraper`, `apify/facebook-ads-scraper`, `apify/instagram-profile-scraper` |
| **Content Analytics** | `apify/instagram-post-scraper`, `clockworks/tiktok-scraper`, `streamers/youtube-scraper` |
| **Trend Research** | `apify/google-trends-scraper`, `clockworks/tiktok-trends-scraper`, `apify/instagram-hashtag-stats` |
| **Review Analysis** | `compass/Google-Maps-Reviews-Scraper`, `voyager/booking-reviews-scraper`, `maxcopell/tripadvisor-reviews` |
| **Audience Analysis** | `apify/instagram-followers-count-scraper`, `clockworks/tiktok-followers-scraper`, `apify/facebook-followers-following-scraper` |

---

#### Multi-Actor Workflows

For complex tasks, chain multiple Actors:

| Workflow | Step 1 | Step 2 |
|----------|--------|--------|
| **Lead enrichment** | `compass/crawler-google-places` → | `vdrmota/contact-info-scraper` |
| **Influencer vetting** | `apify/instagram-profile-scraper` → | `apify/instagram-comment-scraper` |
| **Competitor deep-dive** | `apify/facebook-pages-scraper` → | `apify/facebook-posts-scraper` |
| **Local business analysis** | `compass/crawler-google-places` → | `compass/Google-Maps-Reviews-Scraper` |

#### Can't Find a Suitable Actor?

If none of the Actors above match the user's request, search the Apify Store directly:

```bash
node ${CLAUDE_PLUGIN_ROOT}/reference/scripts/search_actors.js --query "SEARCH_KEYWORDS"
```

Replace `SEARCH_KEYWORDS` with 1-3 simple terms (e.g., "LinkedIn profiles", "Amazon products", "Twitter").

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details:

```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/fetch_actor_details.js --actor "ACTOR_ID"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `compass/crawler-google-places`).

This returns:
- Actor info (title, description, URL, categories, stats, rating)
- README summary
- Input schema (required and optional parameters)

### Step 3: Ask User Preferences

**Skip this step** for simple lookups (e.g., "what's Nike's follower count?", "find me 5 coffee shops in Prague") — just use quick answer mode and move to Step 4.

For larger scraping tasks, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

**Cost safety**: Always set a sensible result limit in the Actor input (e.g., `maxResults`, `resultsLimit`, `maxCrawledPages`, or equivalent field from the input schema). Default to 100 results unless the user explicitly asks for more. Warn the user before running large scrapes (1000+ results) as they consume more Apify credits.

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Results and Offer Follow-ups

After completion, report:
- Number of results found
- File location and name
- Key fields available
- **Suggested follow-up workflows** based on results:

| If User Got | Suggest Next |
|-------------|--------------|
| Business listings | Enrich with `vdrmota/contact-info-scraper` or get reviews |
| Influencer profiles | Analyze engagement with comment scrapers |
| Competitor pages | Deep-dive with post/ad scrapers |
| Trend data | Validate with platform-specific hashtag scrapers |


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`
```

## File: `skills/apify-ultimate-scraper/reference/scripts/fetch_actor_details.js`
```javascript
#!/usr/bin/env node
/**
 * Fetch Apify Actor details: README, input schema, and description.
 *
 * Usage:
 *   node --env-file=.env scripts/fetch_actor_details.js --actor "apify/instagram-profile-scraper"
 */

import { parseArgs } from 'node:util';

const USER_AGENT = 'apify-agent-skills/apify-ultimate-scraper-1.3.0';

function parseCliArgs() {
    const options = {
        actor: { type: 'string', short: 'a' },
        help: { type: 'boolean', short: 'h' },
    };

    const { values } = parseArgs({ options, allowPositionals: false });

    if (values.help) {
        console.log(`
Fetch Apify Actor details (README, input schema, description)

Usage:
  node --env-file=.env scripts/fetch_actor_details.js --actor "ACTOR_ID"

Options:
  --actor, -a    Actor ID (e.g., apify/instagram-profile-scraper) [required]
  --help, -h     Show this help message
`);
        process.exit(0);
    }

    if (!values.actor) {
        console.error('Error: --actor is required');
        process.exit(1);
    }

    return { actor: values.actor };
}

async function fetchActorInfo(token, actorId) {
    const apiActorId = actorId.replace('/', '~');
    const url = `https://api.apify.com/v2/acts/${apiActorId}?token=${encodeURIComponent(token)}`;

    const response = await fetch(url, {
        headers: { 'User-Agent': `${USER_AGENT}/fetch_actor_info` },
    });

    if (response.status === 404) {
        console.error(`Error: Actor '${actorId}' not found`);
        process.exit(1);
    }

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Failed to fetch actor info (${response.status}): ${text}`);
        process.exit(1);
    }

    return (await response.json()).data;
}

async function fetchBuildDetails(token, actorId, buildId) {
    const apiActorId = actorId.replace('/', '~');
    const url = `https://api.apify.com/v2/acts/${apiActorId}/builds/${buildId}?token=${encodeURIComponent(token)}`;

    const response = await fetch(url, {
        headers: { 'User-Agent': `${USER_AGENT}/fetch_build` },
    });

    if (!response.ok) {
        return null;
    }

    return (await response.json()).data;
}

async function main() {
    const args = parseCliArgs();

    const token = process.env.APIFY_TOKEN;
    if (!token) {
        console.error('Error: APIFY_TOKEN not found in .env file');
        console.error('Add your token to .env: APIFY_TOKEN=your_token_here');
        console.error('Get your token: https://console.apify.com/account/integrations');
        process.exit(1);
    }

    // Step 1: Get actor info (includes readmeSummary, taggedBuilds)
    const actorInfo = await fetchActorInfo(token, args.actor);

    // Step 2: Get build details for input schema
    const buildId = actorInfo.taggedBuilds?.latest?.buildId;
    let inputSchema = null;

    if (buildId) {
        const build = await fetchBuildDetails(token, args.actor, buildId);
        if (build) {
            const schemaRaw = build.inputSchema;
            if (schemaRaw) {
                inputSchema = typeof schemaRaw === 'string' ? JSON.parse(schemaRaw) : schemaRaw;
            }
        }
    }

    // Compose output
    const stats = actorInfo.stats || {};
    const output = {
        actorId: args.actor,
        title: actorInfo.title || null,
        url: `https://apify.com/${args.actor}`,
        description: actorInfo.description || null,
        categories: actorInfo.categories || [],
        isDeprecated: actorInfo.isDeprecated || false,
        stats: {
            totalUsers: stats.totalUsers || 0,
            monthlyUsers: stats.totalUsers30Days || 0,
            bookmarks: stats.bookmarkCount || 0,
        },
        rating: {
            average: stats.actorReviewRating || null,
            count: stats.actorReviewCount || 0,
        },
        readmeSummary: actorInfo.readmeSummary || null,
        inputSchema: inputSchema || null,
    };

    console.log(JSON.stringify(output, null, 2));
}

main().catch((err) => {
    console.error(`Error: ${err.message}`);
    process.exit(1);
});
```

## File: `skills/apify-ultimate-scraper/reference/scripts/run_actor.js`
```javascript
#!/usr/bin/env node
/**
 * Apify Actor Runner - Runs Apify actors and exports results.
 *
 * Usage:
 *   # Quick answer (display in chat, no file saved)
 *   node --env-file=.env scripts/run_actor.js --actor ACTOR_ID --input '{}'
 *
 *   # Export to file
 *   node --env-file=.env scripts/run_actor.js --actor ACTOR_ID --input '{}' --output leads.csv --format csv
 */

import { parseArgs } from 'node:util';
import { writeFileSync, statSync } from 'node:fs';

// User-Agent for tracking skill usage in Apify analytics
const USER_AGENT = 'apify-agent-skills/apify-ultimate-scraper-1.3.0';

// Parse command-line arguments
function parseCliArgs() {
    const options = {
        actor: { type: 'string', short: 'a' },
        input: { type: 'string', short: 'i' },
        output: { type: 'string', short: 'o' },
        format: { type: 'string', short: 'f', default: 'csv' },
        timeout: { type: 'string', short: 't', default: '600' },
        'poll-interval': { type: 'string', default: '5' },
        help: { type: 'boolean', short: 'h' },
    };

    const { values } = parseArgs({ options, allowPositionals: false });

    if (values.help) {
        printHelp();
        process.exit(0);
    }

    if (!values.actor) {
        console.error('Error: --actor is required');
        printHelp();
        process.exit(1);
    }

    if (!values.input) {
        console.error('Error: --input is required');
        printHelp();
        process.exit(1);
    }

    return {
        actor: values.actor,
        input: values.input,
        output: values.output,
        format: values.format || 'csv',
        timeout: parseInt(values.timeout, 10),
        pollInterval: parseInt(values['poll-interval'], 10),
    };
}

function printHelp() {
    console.log(`
Apify Actor Runner - Run Apify actors and export results

Usage:
  node --env-file=.env scripts/run_actor.js --actor ACTOR_ID --input '{}'

Options:
  --actor, -a       Actor ID (e.g., compass/crawler-google-places) [required]
  --input, -i       Actor input as JSON string [required]
  --output, -o      Output file path (optional - if not provided, displays quick answer)
  --format, -f      Output format: csv, json (default: csv)
  --timeout, -t     Max wait time in seconds (default: 600)
  --poll-interval   Seconds between status checks (default: 5)
  --help, -h        Show this help message

Output Formats:
  JSON (all data)     --output file.json --format json
  CSV (all data)      --output file.csv --format csv
  Quick answer        (no --output) - displays top 5 in chat

Examples:
  # Quick answer - display top 5 in chat
  node --env-file=.env scripts/run_actor.js \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}'

  # Export all data to CSV
  node --env-file=.env scripts/run_actor.js \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}' \\
    --output leads.csv --format csv
`);
}

// Start an actor run and return { runId, datasetId }
async function startActor(token, actorId, inputJson) {
    // Convert "author/actor" format to "author~actor" for API compatibility
    const apiActorId = actorId.replace('/', '~');
    const url = `https://api.apify.com/v2/acts/${apiActorId}/runs?token=${encodeURIComponent(token)}`;

    let data;
    try {
        data = JSON.parse(inputJson);
    } catch (e) {
        console.error(`Error: Invalid JSON input: ${e.message}`);
        process.exit(1);
    }

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'User-Agent': `${USER_AGENT}/start_actor`,
        },
        body: JSON.stringify(data),
    });

    if (response.status === 404) {
        console.error(`Error: Actor '${actorId}' not found`);
        process.exit(1);
    }

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: API request failed (${response.status}): ${text}`);
        process.exit(1);
    }

    const result = await response.json();
    return {
        runId: result.data.id,
        datasetId: result.data.defaultDatasetId,
    };
}

// Poll run status until complete or timeout
async function pollUntilComplete(token, runId, timeout, interval) {
    const url = `https://api.apify.com/v2/actor-runs/${runId}?token=${encodeURIComponent(token)}`;
    const startTime = Date.now();
    let lastStatus = null;

    while (true) {
        const response = await fetch(url);
        if (!response.ok) {
            const text = await response.text();
            console.error(`Error: Failed to get run status: ${text}`);
            process.exit(1);
        }

        const result = await response.json();
        const status = result.data.status;

        // Only print when status changes
        if (status !== lastStatus) {
            console.log(`Status: ${status}`);
            lastStatus = status;
        }

        if (['SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'].includes(status)) {
            return status;
        }

        const elapsed = (Date.now() - startTime) / 1000;
        if (elapsed > timeout) {
            console.error(`Warning: Timeout after ${timeout}s, actor still running`);
            return 'TIMED-OUT';
        }

        await sleep(interval * 1000);
    }
}

// Download dataset items
async function downloadResults(token, datasetId, outputPath, format) {
    const url = `https://api.apify.com/v2/datasets/${datasetId}/items?token=${encodeURIComponent(token)}&format=json`;

    const response = await fetch(url, {
        headers: {
            'User-Agent': `${USER_AGENT}/download_${format}`,
        },
    });

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Failed to download results: ${text}`);
        process.exit(1);
    }

    const data = await response.json();

    if (format === 'json') {
        writeFileSync(outputPath, JSON.stringify(data, null, 2));
    } else {
        // CSV output
        if (data.length > 0) {
            const fieldnames = Object.keys(data[0]);
            const csvLines = [fieldnames.join(',')];

            for (const row of data) {
                const values = fieldnames.map((key) => {
                    let value = row[key];

                    // Truncate long text fields
                    if (typeof value === 'string' && value.length > 200) {
                        value = value.slice(0, 200) + '...';
                    } else if (Array.isArray(value) || (typeof value === 'object' && value !== null)) {
                        value = JSON.stringify(value) || '';
                    }

                    // CSV escape: wrap in quotes if contains comma, quote, or newline
                    if (value === null || value === undefined) {
                        return '';
                    }
                    const strValue = String(value);
                    if (strValue.includes(',') || strValue.includes('"') || strValue.includes('\n')) {
                        return `"${strValue.replace(/"/g, '""')}"`;
                    }
                    return strValue;
                });
                csvLines.push(values.join(','));
            }

            writeFileSync(outputPath, csvLines.join('\n'));
        } else {
            writeFileSync(outputPath, '');
        }
    }

    console.log(`Saved to: ${outputPath}`);
}

// Display top 5 results in chat format
async function displayQuickAnswer(token, datasetId) {
    const url = `https://api.apify.com/v2/datasets/${datasetId}/items?token=${encodeURIComponent(token)}&format=json`;

    const response = await fetch(url, {
        headers: {
            'User-Agent': `${USER_AGENT}/quick_answer`,
        },
    });

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Failed to download results: ${text}`);
        process.exit(1);
    }

    const data = await response.json();
    const total = data.length;

    if (total === 0) {
        console.log('\nNo results found.');
        return;
    }

    // Display top 5
    console.log(`\n${'='.repeat(60)}`);
    console.log(`TOP 5 RESULTS (of ${total} total)`);
    console.log('='.repeat(60));

    for (let i = 0; i < Math.min(5, data.length); i++) {
        const item = data[i];
        console.log(`\n--- Result ${i + 1} ---`);

        for (const [key, value] of Object.entries(item)) {
            let displayValue = value;

            // Truncate long values
            if (typeof value === 'string' && value.length > 100) {
                displayValue = value.slice(0, 100) + '...';
            } else if (Array.isArray(value) || (typeof value === 'object' && value !== null)) {
                const jsonStr = JSON.stringify(value);
                displayValue = jsonStr.length > 100 ? jsonStr.slice(0, 100) + '...' : jsonStr;
            }

            console.log(`  ${key}: ${displayValue}`);
        }
    }

    console.log(`\n${'='.repeat(60)}`);
    if (total > 5) {
        console.log(`Showing 5 of ${total} results.`);
    }
    console.log(`Full data available at: https://console.apify.com/vault/datasets/${datasetId}`);
    console.log('='.repeat(60));
}

// Report summary of downloaded data
function reportSummary(outputPath, format) {
    const stats = statSync(outputPath);
    const size = stats.size;

    let count;
    try {
        const content = require('fs').readFileSync(outputPath, 'utf-8');
        if (format === 'json') {
            const data = JSON.parse(content);
            count = Array.isArray(data) ? data.length : 1;
        } else {
            // CSV - count lines minus header
            const lines = content.split('\n').filter((line) => line.trim());
            count = Math.max(0, lines.length - 1);
        }
    } catch {
        count = 'unknown';
    }

    console.log(`Records: ${count}`);
    console.log(`Size: ${size.toLocaleString()} bytes`);
}

// Helper: sleep for ms
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

// Main function
async function main() {
    // Parse args first so --help works without token
    const args = parseCliArgs();

    // Check for APIFY_TOKEN
    const token = process.env.APIFY_TOKEN;
    if (!token) {
        console.error('Error: APIFY_TOKEN not found in .env file');
        console.error('');
        console.error('Add your token to .env file:');
        console.error('  APIFY_TOKEN=your_token_here');
        console.error('');
        console.error('Get your token: https://console.apify.com/account/integrations');
        process.exit(1);
    }

    // Start the actor run
    console.log(`Starting actor: ${args.actor}`);
    const { runId, datasetId } = await startActor(token, args.actor, args.input);
    console.log(`Run ID: ${runId}`);
    console.log(`Dataset ID: ${datasetId}`);

    // Poll for completion
    const status = await pollUntilComplete(token, runId, args.timeout, args.pollInterval);

    if (status !== 'SUCCEEDED') {
        console.error(`Error: Actor run ${status}`);
        console.error(`Details: https://console.apify.com/actors/runs/${runId}`);
        process.exit(1);
    }

    // Determine output mode
    if (args.output) {
        // File output mode
        await downloadResults(token, datasetId, args.output, args.format);
        reportSummary(args.output, args.format);
    } else {
        // Quick answer mode - display in chat
        await displayQuickAnswer(token, datasetId);
    }
}

main().catch((err) => {
    console.error(`Error: ${err.message}`);
    process.exit(1);
});
```

## File: `skills/apify-ultimate-scraper/reference/scripts/search_actors.js`
```javascript
#!/usr/bin/env node
/**
 * Search Apify Store for Actors matching keywords.
 *
 * Usage:
 *   node --env-file=.env scripts/search_actors.js --query "instagram"
 *   node --env-file=.env scripts/search_actors.js --query "amazon products" --limit 5
 */

import { parseArgs } from 'node:util';

const USER_AGENT = 'apify-agent-skills/apify-ultimate-scraper-1.3.0';

function parseCliArgs() {
    const options = {
        query: { type: 'string', short: 'q' },
        limit: { type: 'string', short: 'l', default: '10' },
        help: { type: 'boolean', short: 'h' },
    };

    const { values } = parseArgs({ options, allowPositionals: false });

    if (values.help) {
        console.log(`
Search Apify Store for Actors

Usage:
  node --env-file=.env scripts/search_actors.js --query "KEYWORDS"

Options:
  --query, -q    Search keywords (e.g., "instagram", "amazon products") [required]
  --limit, -l    Max results to return (default: 10)
  --help, -h     Show this help message
`);
        process.exit(0);
    }

    if (!values.query) {
        console.error('Error: --query is required');
        process.exit(1);
    }

    return {
        query: values.query,
        limit: parseInt(values.limit, 10) || 10,
    };
}

async function searchStore(query, limit) {
    const params = new URLSearchParams({ search: query, limit: String(limit) });
    const url = `https://api.apify.com/v2/store?${params}`;

    const response = await fetch(url, {
        headers: { 'User-Agent': `${USER_AGENT}/search_actors` },
    });

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Store search failed (${response.status}): ${text}`);
        process.exit(1);
    }

    const result = await response.json();
    return result.data?.items || [];
}

function formatResults(actors) {
    if (actors.length === 0) {
        console.log('No actors found.');
        return;
    }

    console.log(`Found ${actors.length} actor(s):\n`);

    for (const actor of actors) {
        const id = `${actor.username}/${actor.name}`;
        const title = actor.title || id;
        const desc = actor.description
            ? actor.description.length > 120
                ? actor.description.slice(0, 120) + '...'
                : actor.description
            : 'No description';
        const runs = actor.stats?.totalRuns?.toLocaleString() || '0';
        const users = actor.stats?.totalUsers?.toLocaleString() || '0';

        console.log(`  ${id}`);
        console.log(`    Title: ${title}`);
        console.log(`    ${desc}`);
        console.log(`    Runs: ${runs} | Users: ${users}`);
        console.log();
    }
}

async function main() {
    const args = parseCliArgs();
    const actors = await searchStore(args.query, args.limit);
    formatResults(actors);
}

main().catch((err) => {
    console.error(`Error: ${err.message}`);
    process.exit(1);
});
```

