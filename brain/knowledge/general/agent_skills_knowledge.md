# Knowledge Dump for agent_skills

## File: DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: FETCHED_agent-skills_144258

# DEEP_KNOWLEDGE.md: Observability Skill Repository Analysis

## 🧠 Overview and Purpose

This repository constitutes a specialized **Knowledge Graph Augmentation Layer** designed to elevate the capabilities of AI coding agents in the domain of software observability. It does not implement logging functionality itself, but rather provides a structured, highly parameterized set of 'skills'—best practice blueprints, validation routines, and instructional templates—that guide an agent through the complex process of implementing, reviewing, and optimizing logging and monitoring infrastructure.

The primary objective is to enforce architectural consistency and adherence to industry best practices (e.g., structured logging, correlation IDs, metric aggregation) within the code generated or reviewed by the AI agent, thereby mitigating the common pitfalls of ad-hoc, unstructured logging.

## 🏗️ Architectural Patterns

The repository employs a **Skill-Based Knowledge Architecture (SKKA)**, which deviates from traditional software design patterns (like MVC or layered architecture). Instead, it models knowledge as discrete, callable, and verifiable *skills*.

### 1. Skill Abstraction Layer
The core architectural pattern is the abstraction of complex human expertise (e.g., "How to implement distributed tracing") into a machine-readable, executable skill module. Each skill module is self-contained and operates on a defined input context (e.g., existing code snippet, function signature, or architectural diagram).

### 2. Pattern-Driven Development (PDD)
The repository enforces a Pattern-Driven Development methodology. Instead of generating raw code, the agent is guided to generate code that conforms to established patterns:

*   **Structured Logging Pattern:** Mandates the use of key-value pairs (JSON or similar) rather than concatenated strings.
*   **Context Propagation Pattern:** Ensures the automatic inclusion of correlation IDs (e.g., `trace_id`, `span_id`) across service boundaries.
*   **Observability Hook Pattern:** Defines standardized points (hooks) where logging or metric collection must occur (e.g., entry/exit points of critical functions).

### 3. Meta-Instructional Architecture
The repository acts as a meta-instructional system. It doesn't just provide code; it provides the *process* of writing code. This includes pre-flight checklists, post-review validation scripts, and iterative refinement steps, guiding the agent through a structured cognitive workflow.

## ⚙️ Core Algorithms and Mechanisms

The "algorithms" within this context are sophisticated **Reasoning and Transformation Algorithms** that guide the agent's code generation and review processes.

### 1. The Observability Compliance Algorithm (OCA)
The OCA is the primary validation mechanism. It operates as a multi-pass static analysis routine applied to the agent's proposed code output.

**Input:** Code Snippet ($C$), Target Skill ($S$), Context ($X$).
**Process:**
1.  **Pattern Matching:** $C$ is scanned for structural elements that violate the requirements defined by $S$.
2.  **Contextual Gap Analysis:** The algorithm identifies missing observability elements (e.g., if a function handles a database call but lacks an associated `db_query` log level).
3.  **Transformation Suggestion:** If a violation or gap is found, the algorithm generates a precise, actionable transformation suggestion ($\Delta C$) that, when applied to $C$, brings it into compliance with $S$.

$$
\text{Compliance}(C, S) = \begin{cases} \text{True} & \text{if } \text{OCA}(C, S) \text{ yields no critical violations} \\ \text{False} & \text{otherwise, suggesting } \Delta C \end{cases}
$$

### 2. Structured Logging Transformation Mechanism (SLTM)
This mechanism is responsible for converting unstructured logging calls (e.g., `logger.info("User {} logged in from IP {}", user, ip)`) into structured, machine-readable formats (e.g., JSON).

**Mechanism Flow:**
1.  **Tokenization:** The raw log message string is tokenized into components (literal text, variable placeholders).
2.  **Schema Mapping:** Each token is mapped to a predefined schema key (e.g., `user` $\rightarrow$ `user_id`, `ip` $\rightarrow$ `source_ip`).
3.  **Serialization:** The structured key-value pairs are serialized into the target format (e.g., JSON, Logfmt).

### 3. Context Propagation Mechanism (CPM)
The CPM ensures that transaction context is maintained across asynchronous boundaries. It mandates the injection and extraction of correlation identifiers.

**Core Logic:**
1.  **Injection Point Identification:** Identifies the entry point of a service call.
2.  **Context Initialization:** Generates a unique `trace_id` and initializes the current `span_id`.
3.  **Propagation Hook:** Inserts logic (e.g., HTTP headers, message queue metadata) to pass the current context identifiers to the downstream service call.
4.  **Context Extraction:** At the receiving service, the logic intercepts the incoming context and uses it to resume the existing trace.

## 🛠️ Implementation Details and Best Practices

| Component | Function | Technical Output | Best Practice Enforced |
| :--- | :--- | :--- | :--- |
| **Skill Templates** | Provides the structural skeleton for a task. | Boilerplate code blocks, function signatures. | Consistency, Immediate adherence to required context variables. |
| **Validation Scripts** | Automated checks against generated code. | Unit tests, Linting rules (e.g., `no-unstructured-log`). | High coverage, Zero tolerance for non-compliant logging. |
| **Instruction Sets** | Guides the agent's reasoning process. | Step-by-step markdown guides, decision trees. | Systematic thinking, Comprehensive coverage (e.g., logging at entry, exit, and failure points). |
| **Schema Definitions** | Defines the allowed keys and data types for logs. | JSON Schema definitions, Type hints. | Data integrity, Ease of parsing by log aggregation systems (ELK, Splunk). |

### Key Takeaway for Agent Utilization

The repository's power lies in its ability to transition the AI agent from a *code generator* to a *compliance engineer*. By forcing the agent to pass its output through the OCA and SLTM, the system guarantees that the generated code is not merely functional, but also fully observable, auditable, and maintainable.
```

## File: README.md
```
# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### logging-best-practices

Logging best practices focused on wide events (canonical log lines). Contains guidelines for effective logging that enables powerful debugging and analytics.

**Use when:**
- Writing or reviewing logging code
- Adding console.log, logger.info, or similar
- Designing logging strategy for new services
- Setting up logging infrastructure

**Key concepts:**
- Wide Events (Critical) - One context-rich event per request per service
- High Cardinality & Dimensionality (Critical) - Many fields, unique identifiers
- Business Context (Critical) - User subscription, cart value, feature flags
- Environment Context (Critical) - Commit hash, version, region, instance ID
- Single Logger (High) - One logger instance, configured at startup
- Middleware Pattern (High) - Infrastructure in middleware, business context in handlers

**References:**
- [Logging Sucks](https://loggingsucks.com)
- [Observability Wide Events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)

## Installation

```bash
npx add-skill boristane/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Add logging to this endpoint
```
```
Review my logging code
```
```
Help me set up logging for this service
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `rules/` - Individual guideline files
- `metadata.json` - Version and references

```

## File: schema.json
```
{
  "id": "agent_skills",
  "name": "Agent Skills",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "agent-framework",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "\\ecosystem\\skills\\agent_skills\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for agent_skills",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "agent"
  ]
}
```

## File: SKILL.md
```
# SKILL PROFILE: repo_fetched_agent_skills_144258
# Department Registry: OAP Toolchain
# Scope: Pure OS-sanctioned Tools
---

## 1. Domain Capability
Generic specialist agent.

## 2. Linked Toolkit
> [!NOTE]
> No static YAML skills mapped. Awaiting dynamic plugin hooks from OAP Orchestrator.

---
*Capability Register hardened by OmniClaw OA Skill Auditor.*

```

## File: _DIR_IDENTITY.md
```
---
id: repo-fetched-agent-skills-144258
type: skill
owner: OA
registered_at: 2026-04-04T17:37:15.092218
tags: ["auto-cloned", "AI Agents", "Software Development", "Observability", "Logging", "oa-assimilated", "premium-repo"]
---

# FETCHED_agent-skills_144258

## Assimilation Report
This repository provides a collection of specialized 'skills' designed to enhance AI coding agents, focusing on best practices for logging and observability. It packages structured instructions and scripts to guide agents when tasks involve logging implementation or review.

```

## File: .claude-plugin\marketplace.json
```
{
  "name": "apify-agent-skills",
  "owner": {
    "name": "Apify",
    "email": "support@apify.com"
  },
  "metadata": {
    "description": "Official Apify Agent Skills for web scraping, data extraction, and automation",
    "version": "2.0.0"
  },
  "plugins": [
    {
      "name": "apify-ultimate-scraper",
      "source": "./skills/apify-ultimate-scraper",
      "skills": "./",
      "description": "Universal AI-powered web scraper for 55+ platforms. Scrape data from Instagram, Facebook, TikTok, YouTube, Google Maps, Google Search, Google Trends, Booking.com, TripAdvisor, Amazon, Walmart, eBay, and more for lead generation, brand monitoring, competitor analysis, influencer discovery, trend research, content analytics, audience analysis, e-commerce pricing, and reviews",
      "keywords": [
        "scraping",
        "web-scraper",
        "data-extraction",
        "apify",
        "instagram",
        "facebook",
        "tiktok",
        "youtube",
        "google-maps"
      ],
      "category": "data-extraction",
      "version": "2.0.0"
    },
    {
      "name": "apify-actor-development",
      "source": "./skills/apify-actor-development",
      "skills": "./",
      "description": "Develop, debug, and deploy Apify Actors - serverless cloud programs for web scraping, automation, and data processing",
      "keywords": [
        "apify",
        "actor",
        "development",
        "deploy",
        "serverless"
      ],
      "category": "development",
      "version": "2.0.0"
    },
    {
      "name": "apify-actorization",
      "source": "./skills/apify-actorization",
      "skills": "./",
      "description": "Convert existing projects into Apify Actors - serverless cloud programs. Actorize JavaScript/TypeScript (SDK with Actor.init/exit), Python (async context manager), or any language (CLI wrapper)",
      "keywords": [
        "apify",
        "actor",
        "actorization",
        "migration",
        "convert"
      ],
      "category": "development",
      "version": "2.0.0"
    },
    {
      "name": "apify-generate-output-schema",
      "source": "./skills/apify-generate-output-schema",
      "skills": "./",
      "description": "Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) for an Apify Actor by analyzing its source code",
      "keywords": [
        "apify",
        "actor",
        "schema",
        "output",
        "dataset"
      ],
      "category": "development",
      "version": "2.0.0"
    },
    {
      "name": "apify-actor-commands",
      "description": "Commands for Apify Actor development workflow",
      "version": "2.0.0",
      "author": {
        "name": "Apify",
        "email": "support@apify.com"
      },
      "source": "./",
      "category": "development",
      "commands": [
        "./commands/create-actor.md"
      ]
    }
  ]
}

```

## File: .claude-plugin\plugin.json
```
{
  "name": "apify-agent-skills",
  "version": "1.6.1",
  "description": "Official Apify agent skills for web scraping, data extraction, and automation",
  "author": {
    "name": "Apify",
    "email": "support@apify.com"
  },
  "homepage": "https://github.com/apify/agent-skills",
  "repository": "https://github.com/apify/agent-skills",
  "license": "Apache-2.0",
  "keywords": [
    "apify",
    "scraping",
    "automation",
    "leads",
    "data-extraction"
  ]
}

```

## File: .github\workflows\clickhouse-best-practices-ci.yml
```
name: ClickHouse Best Practices CI

on:
  push:
    branches: [main]
    paths:
      - 'skills/clickhouse-best-practices/**'
      - 'packages/clickhouse-best-practices-build/**'
  pull_request:
    paths:
      - 'skills/clickhouse-best-practices/**'
      - 'packages/clickhouse-best-practices-build/**'

jobs:
  validate-and-build:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: packages/clickhouse-best-practices-build
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1

      - uses: oven-sh/setup-bun@4bc047ad259df6fc24a6c9b0f9a0cb08cf17fbe5 # v1.2.2
        with:
          bun-version: latest

      - name: Install dependencies
        run: bun install

      - name: Validate rule structure
        run: bun run validate

      - name: Validate SQL syntax
        run: bun run validate-sql

      - name: Check internal links
        run: bun run check-links

      - name: Build documentation
        run: bun run build

      - name: Upload AGENTS.md artifact
        uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
        with:
          name: agents-md
          path: skills/clickhouse-best-practices/AGENTS.md

      - name: Send Slack notification
        if: github.ref == 'refs/heads/main' && success()
        uses: slackapi/slack-github-action@91efab103c0de0a537f72a35f6b8cda0ee76bf0a #v2.1.1
        with:
          webhook: ${{ secrets.RELEASE_SLACK_WEBHOOK }}
          webhook-type: incoming-webhook
          payload: |
            {
              "text": "agent-skills: ClickHouse Best Practices CI completed successfully",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "agent-skills: ClickHouse Best Practices validated and built successfully\n*Branch:* ${{ github.ref_name }}\n*Commit:* <${{ github.event.head_commit.url }}|${{ github.event.head_commit.message }}>"
                  }
                }
              ]
            }

```

## File: .github\workflows\external-links-check.yml
```
name: Daily External Links Check

on:
  schedule:
    - cron: '0 9 * * 1-5'  # 9 AM UTC, Monday-Friday
  workflow_dispatch:  # Allow manual triggering

jobs:
  check-external-links:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    defaults:
      run:
        working-directory: packages/clickhouse-best-practices-build

    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1

      - uses: oven-sh/setup-bun@4bc047ad259df6fc24a6c9b0f9a0cb08cf17fbe5 # v1.2.2
        with:
          bun-version: latest

      - name: Install dependencies
        run: bun install

      - name: Check external links
        run: bun run check-external-links

      - name: Send Slack notification on failure
        if: failure()
        uses: slackapi/slack-github-action@70cd7be8e40a46e8b0eced40b0de447bdb42f68e # v1.27.0
        with:
          webhook-url: ${{ secrets.RELEASE_SLACK_WEBHOOK }}
          payload: |
            {
              "text": "❌ External Links Check Failed",
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "❌ External Links Check Failed"
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {
                      "type": "mrkdwn",
                      "text": "*Repository:*\n${{ github.repository }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Workflow:*\n${{ github.workflow }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Branch:*\n${{ github.ref_name }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Run:*\n<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|View Run>"
                    }
                  ]
                }
              ]
            }

```

## File: .github\workflows\generate-agents.yml
```
name: Check AGENTS.md and marketplace.json

on:
  pull_request:
    paths:
      - "scripts/AGENTS_TEMPLATE.md"
      - "scripts/generate_agents.py"
      - "**/SKILL.md"
      - "agents/AGENTS.md"
      - ".claude-plugin/marketplace.json"

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up uv
        uses: astral-sh/setup-uv@v4

      - name: Generate AGENTS.md and validate marketplace.json
        run: uv run scripts/generate_agents.py

      - name: Ensure AGENTS.md is up to date
        run: |
          git diff --quiet -- agents/AGENTS.md || {
            echo "::error::agents/AGENTS.md is outdated. Run 'uv run scripts/generate_agents.py' and commit the changes."
            exit 1
          }

```

## File: .github\workflows\publish.yml
```
name: publish

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      tag:
        description: 'Release tag'
        required: true
        type: string
      branch:
        description: 'Branch to deploy from'
        required: false
        default: 'main'
        type: string

env:
  HUSKY: 0

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write      # For git push and tagging
      id-token: write      # For OIDC trusted publishing to npm
    steps:
      - name: Set tag from input (manual trigger)
        if: github.event_name == 'workflow_dispatch'
        run: |
          echo "GITHUB_TAG=${{ github.event.inputs.tag }}" >> "$GITHUB_ENV"
          # Check if input is a semantic version (e.g., 0.0.242) or a tag name (e.g., beta, scss-deprecation)
          if [[ "${{ github.event.inputs.tag }}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-.*)?$ ]]; then
            echo "IS_VERSION_INPUT=true" >> "$GITHUB_ENV"
          else
            echo "IS_VERSION_INPUT=false" >> "$GITHUB_ENV"
          fi
      - name: Set tag from release (automatic trigger)
        if: github.event_name == 'release'
        run: |
          echo "GITHUB_TAG=${GITHUB_REF#refs/tags/}" >> "$GITHUB_ENV"
          echo "IS_VERSION_INPUT=true" >> "$GITHUB_ENV"
      - name: Checkout repository (manual trigger)
        if: github.event_name == 'workflow_dispatch'
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.inputs.branch }}
          token: ${{secrets.PAT_TOKEN}}
          fetch-depth: 0
      - name: Checkout repository (automatic release)
        if: github.event_name == 'release'
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.release.target_commitish }}
          token: ${{secrets.PAT_TOKEN}}
          fetch-depth: 0
      - name: Set up Git
        run: |
          git config user.email "actions@clickhouse.com"
          git config user.name "GitHub Actions"
      - name: Bump package version (for version inputs)
        if: ${{ env.IS_VERSION_INPUT == 'true' }}
        run: |
          npm pkg set version=$GITHUB_TAG
      - name: Generate prerelease version (for tag inputs)
        if: ${{ env.IS_VERSION_INPUT == 'false' }}
        run: |
          # Get current version from package.json
          CURRENT_VERSION=$(node -p "require('./package.json').version")
          # Extract base version (remove any existing prerelease suffix)
          BASE_VERSION=$(echo $CURRENT_VERSION | cut -d'-' -f1)
          # Generate prerelease version: base-tagname.0
          NEW_VERSION="${BASE_VERSION}-${GITHUB_TAG}.0"
          echo "Generated prerelease version: $NEW_VERSION"
          npm pkg set version=$NEW_VERSION --no-git-tag-version
      - uses: actions/setup-node@v4
        with:
          node-version: '22.x'  # Node 22 includes npm >= 11.5.1 with OIDC support
      - name: Upgrade npm for OIDC support
        run: |
          npm install -g npm@latest
          echo "npm version: $(npm --version)"
      - name: Enable Corepack
        run: corepack enable
      - name: Install dependencies
        run: yarn install --immutable
      - run: yarn test
      - run: yarn build
      - name: Determine npm tag
        run: |
          # If it's a version input (e.g., 0.0.242 or 0.0.242-beta.1), check for prerelease keywords
          if [[ "$IS_VERSION_INPUT" == "true" ]]; then
            if [[ "$GITHUB_TAG" == *"beta"* ]] || [[ "$GITHUB_TAG" == *"alpha"* ]] || [[ "$GITHUB_TAG" == *"rc"* ]]; then
              echo "NPM_TAG=beta" >> "$GITHUB_ENV"
            else
              echo "NPM_TAG=latest" >> "$GITHUB_ENV"
            fi
          else
            # If it's a tag name input (e.g., scss-deprecation), use it as the npm tag
            echo "NPM_TAG=$GITHUB_TAG" >> "$GITHUB_ENV"
          fi
      - name: Publish to npm with OIDC
        run: npm publish --tag $NPM_TAG --provenance
      - name: update package version (for version inputs only)
        if: ${{ env.IS_VERSION_INPUT == 'true' }}
        run: |
          git add package.json yarn.lock
          git commit -m 'bump version to ${{ env.GITHUB_TAG }}'
          git push
      - name: Create and push git tag (for version inputs only)
        if: ${{ github.event_name == 'workflow_dispatch' && env.IS_VERSION_INPUT == 'true' }}
        run: |
          git tag $GITHUB_TAG
          git push origin $GITHUB_TAG


```

## File: agents\agents.md
```
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

## File: agents\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-agents
name: Agents
path: ecosystem/skills/repo-fetched-agent-skills-124622/agents
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Agents
Storage area for 'agents' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: brave-search\SKILL.md
```
---
name: Vincent - Brave Search for agents
description: |
  Web and news search powered by Brave Search. Use this skill when users want to search the web,
  find news articles, or look up current information. Pay-per-call via Vincent credit system.
  Triggers on "search the web", "web search", "brave search", "search news", "find information",
  "look up", "current events".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*), Bash(jq:*), Bash(bc:*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources
        - ./datasources
---

# Vincent - Brave Search for agents

Use this skill to search the web and news using Brave Search. All requests are proxied through the Vincent backend, which handles authentication with the Brave Search API, enforces rate limits, tracks per-call costs, and deducts from your credit balance automatically.

**No API keys to manage.** The agent authenticates with a Vincent API key scoped to a `DATA_SOURCES` secret. Vincent handles the upstream Brave Search API credentials server-side -- the agent never sees or manages Brave API keys.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with pay-per-call pricing and human oversight**.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates a `DATA_SOURCES` secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources/` or `./datasources/`) are declared in this skill's metadata.

**The agent's API key is not a Brave Search API key.** It is a scoped Bearer token for the Vincent proxy. The Vincent server authenticates with Brave Search on the agent's behalf. The agent cannot access the upstream API directly or bypass the proxy's credit and rate-limit enforcement.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous web search capabilities. The agent is expected to search the web and news on its own. The human controls spending through credit balance and payment method management at `https://heyvincent.ai`.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The Vincent server then calls the Brave Search API. The agent does not contact Brave directly.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type DATA_SOURCES` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership, add credit, and manage payment at `https://heyvincent.ai`.
- **Credit**: Each API call costs a small amount (see Pricing below). The human adds credit via the frontend. Calls are rejected when credit runs out and no payment method is on file.
- **Revocation**: The secret owner can revoke the agent's API key at any time from the Vincent frontend.

## Pricing

| Endpoint | Cost per call |
| --- | --- |
| Web search | $0.005 |
| News search | $0.005 |

Credit is deducted automatically per call. The response includes `_vincent.creditRemainingUsd` so the agent can track remaining balance.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type DATA_SOURCES
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new secret.

### 2. Create a Data Sources Secret

```bash
npx @vincentai/cli@latest secret create --type DATA_SOURCES --memo "My agent data sources"
```

Returns `keyId` (use for all future commands) and `claimUrl` (share with the user).

After creating, tell the user:

> "Here is your data sources claim URL: `<claimUrl>`. Use this to claim ownership and add credit for Brave Search and other data sources at https://heyvincent.ai."

**Important:** The secret must be claimed and have credit (or a payment method on file) before API calls will succeed.

### 3. Web Search

```bash
npx @vincentai/cli@latest brave web --key-id <KEY_ID> --q "latest AI news" --count 10
```

Parameters:

- `--q` (required): Search query (1-400 characters)
- `--count` (optional): Number of results, 1-20 (default: 10)
- `--offset` (optional): Pagination offset, 0-9
- `--freshness` (optional): Time filter — `pd` (past day), `pw` (past week), `pm` (past month), `py` (past year)
- `--country` (optional): 2-letter country code for localized results (e.g., `us`, `gb`, `de`)

Returns web results with titles, URLs, descriptions, and metadata.

### 4. News Search

```bash
npx @vincentai/cli@latest brave news --key-id <KEY_ID> --q bitcoin --count 10
```

Parameters:

- `--q` (required): Search query (1-400 characters)
- `--count` (optional): Number of results, 1-20 (default: 10)
- `--freshness` (optional): Time filter — `pd` (past day), `pw` (past week), `pm` (past month), `py` (past year)

Returns news articles with titles, URLs, descriptions, publication dates, and source information.

## Response Metadata

Every successful response includes a `_vincent` object with:

```json
{
  "_vincent": {
    "costUsd": 0.005,
    "creditRemainingUsd": 4.99
  }
}
```

Use `creditRemainingUsd` to warn the user when credit is running low.

## Output Format

Web search results:

```json
{
  "web": {
    "results": [
      {
        "title": "Article Title",
        "url": "https://example.com/article",
        "description": "A brief description of the article content."
      }
    ]
  },
  "_vincent": {
    "costUsd": 0.005,
    "creditRemainingUsd": 4.99
  }
}
```

News search results follow the same structure with additional `age` and `source` fields per result.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `402 Insufficient Credit` | Credit balance is zero and no payment method on file | User must add credit at heyvincent.ai |
| `429 Rate Limited` | Exceeded 60 requests/minute | Wait and retry with backoff |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |

## Rate Limits

- 60 requests per minute per API key across all data source endpoints (Twitter + Brave Search combined)
- If rate limited, you'll receive a `429` response. Wait and retry.

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Adding Credits

When your credit balance runs low, you can purchase more credits autonomously using USDC on Base via the x402 payment protocol — no human intervention required.

**Available tiers:** $1, $5, $10, $25, $50, $100

### Check Balance

```bash
npx @vincentai/cli@latest credits balance --key-id <KEY_ID>
```

### Purchase Credits via x402 (USDC on Base)

```bash
npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
```

**How it works:**

1. The CLI sends a POST request to the x402 credit endpoint
2. The server returns HTTP 402 with a dynamic USDC deposit address on Base
3. The CLI signs the payment using your agent's wallet
4. The CLI retries the request with the payment proof
5. The server verifies the payment and adds credits to your account

**Requirements:**
- An x402-compatible wallet with USDC on Base (chain ID 8453)
- Your Vincent DATA_SOURCES API key

### Purchase Credits via Card (Human)

```bash
npx @vincentai/cli@latest credits checkout --key-id <KEY_ID>
```

Returns a Stripe Checkout URL. Share this with the user to complete payment with a card.

### MCP Tools

| Tool | Description |
| --- | --- |
| `vincent_credit_balance` | Check current credit balance and top-up options |
| `vincent_add_credits` | Get x402 payment instructions for purchasing credits |

### Auto-Replenish Pattern

For long-running agents, check your balance before expensive operations and top up when low:

```bash
BALANCE=$(npx @vincentai/cli@latest credits balance --key-id <KEY_ID> --json | jq -r '.balance')
if (( $(echo "$BALANCE < 2.00" | bc -l) )); then
  npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
fi
```

## Important Notes

- A single `DATA_SOURCES` API key works for **all** data sources (Twitter, Brave Search, etc.). You do not need a separate key per data source.
- Always share the claim URL with the user after creating a secret.
- If a call is rejected with a credit error, tell the user to add credit at `https://heyvincent.ai`.

```

## File: brave-search\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-brave-search
name: Brave-Search
path: ecosystem/skills/repo-fetched-agent-skills-054345/brave-search
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Brave-Search
Storage area for 'brave-search' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: commands\create_actor.md
```
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
4. Use proper logging (see [skills/apify-actor-development/references/logging.md](skills/apify-actor-development/references/logging.md))
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
2. Create test input file at `storage/key_value_stores/default/INPUT.json` with sample parameters
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

## File: commands\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-commands
name: Commands
path: ecosystem/skills/repo-fetched-agent-skills-124622/commands
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Commands
Storage area for 'commands' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: credentials\SKILL.md
```
---
name: Vincent - Credentials for agents
description: |
  Secure credential management for agents. Use this skill when users need to store API keys,
  passwords, OAuth tokens, or SSH keys and write them to .env files without exposing values.
  Triggers on "store credentials", "API key", "manage secrets", "write to env", ".env file",
  "credential", "password", "token storage".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials
        - ./credentials
---

# Vincent - Credentials for agents

Use this skill to securely manage credentials that your application needs — API keys, passwords, OAuth tokens, SSH keys, or structured username/password pairs. The agent creates a secret, the user (or agent) sets the value, and the agent uses the CLI to write it directly to a `.env` file. **The credential value never appears in the agent's context or stdout.**

This is useful when the agent is building something that needs credentials (e.g. a third-party API key). Instead of the user pasting the credential into chat (where it enters the agent's context), they set it via the Vincent dashboard, and the agent writes it to the `.env` file using the CLI.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **keeping credentials out of the agent's context window**.

**How it works:** The `secret env` CLI command fetches the credential from the Vincent server and writes it directly to a `.env` file on disk. The value is never printed to stdout and never appears in the agent's conversation context. Many agent frameworks blacklist reading `.env` files, so even though the file is on disk, the agent cannot read it back. The application the agent is building reads the `.env` file normally at runtime.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own credential secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials/` or `./credentials/`) are declared in this skill's metadata.

**Overwrite guard:** Once a value is set by an agent's API key, only that same API key can overwrite it. This prevents other agents or keys from tampering with the credential. The guard is enforced atomically at the database level.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type CREDENTIALS` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Value set**: The user sets the credential value via the dashboard after claiming, or the agent sets it via the CLI.
- **Write to .env**: The agent runs `secret env` to write the value to a `.env` file without exposing it.
- **Claim**: The human operator uses the claim URL to take ownership and manage the secret from the dashboard.
- **Revocation**: The secret owner can revoke the agent's API key at any time from `https://heyvincent.ai`.

## Secret Types

| Type | Value format | Use case |
|---|---|---|
| `API_KEY` | Non-empty string | Third-party API keys |
| `SSH_KEY` | Non-empty string | SSH private keys |
| `OAUTH_TOKEN` | Non-empty string | OAuth access/refresh tokens |
| `CREDENTIALS` | JSON object with `password` or `secret` | Username/password, key/secret pairs |

All four types support the same create, set, and `env` workflow.

### CREDENTIALS Value Format

The `CREDENTIALS` value must be a JSON object containing at least one of:

- `password` (string) — e.g. `{"username": "alice", "password": "hunter2"}`
- `secret` (string) — e.g. `{"accountId": "acct-1", "secret": "top-secret"}`

Additional fields are preserved as-is. All values are limited to 16KB.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type CREDENTIALS
```

If a key is returned, use its `id` as the `--key-id` for subsequent commands. If no keys exist, create a new secret.

### 2. Create a Credentials Secret

```bash
npx @vincentai/cli@latest secret create --type CREDENTIALS --memo "Acme API credentials"
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `secretId`.

After creating, tell the user:

> "Here is your credentials claim URL: `<claimUrl>`. Use this to claim ownership and set the credential value at https://heyvincent.ai."

### 3. Set the Credential Value

**Option A: User sets via dashboard (recommended)**

The user claims the secret using the claim URL, then sets the credential value from the dashboard. This keeps the value completely out of the agent's hands.

**Option B: Agent sets via CLI**

For agent-first workflows where the agent has the credential (e.g. it obtained an API key from a service):

```bash
npx @vincentai/cli@latest secret set-value --key-id <KEY_ID> --value '{"username": "alice", "password": "hunter2"}'
```

For simple string types (`API_KEY`, `SSH_KEY`, `OAUTH_TOKEN`):

```bash
npx @vincentai/cli@latest secret set-value --key-id <KEY_ID> --value "sk-my-third-party-api-key"
```

### 4. Write to .env File

Once the value is set (by the user or the agent), use the CLI to write it to a `.env` file. **The value is never printed to stdout.**

```bash
# Write an API_KEY secret as an env var
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var ACME_API_KEY

# For CREDENTIALS: extract a specific field
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var DB_PASSWORD --field password

# Write to a specific path (default: ./.env)
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var SERVICE_TOKEN --path ./config/.env
```

The command outputs a confirmation JSON (without the value) so the agent knows it succeeded:

```json
{
  "written": "ACME_API_KEY",
  "path": "/path/to/.env",
  "type": "API_KEY"
}
```

**Flags:**

| Flag | Required | Description |
|---|---|---|
| `--env-var` | Yes | Environment variable name (e.g. `MY_API_KEY`) |
| `--path` | No | Path to `.env` file (default: `./.env`) |
| `--key-id` | No | API key ID (auto-discovered if only one credential key exists) |
| `--field` | No | For `CREDENTIALS` type: extract a specific JSON field instead of writing the full JSON |

**Behavior:**

- Creates the `.env` file if it doesn't exist (with `0600` permissions)
- Updates the variable in-place if it already exists in the file
- Appends a new line if the variable doesn't exist
- Values with special characters are automatically quoted

### 5. Use in Your Application

Your application reads the `.env` file normally:

```bash
# Node.js with dotenv
require('dotenv').config()
const apiKey = process.env.ACME_API_KEY

# Python with python-dotenv
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('ACME_API_KEY')
```

## Example: Full Workflow

```bash
# 1. Agent creates a CREDENTIALS secret
npx @vincentai/cli@latest secret create --type CREDENTIALS --memo "Acme service credentials"
# → keyId: abc-123, claimUrl: https://heyvincent.ai/claim/...

# 2. Tell the user to claim and set the value via the dashboard

# 3. Once set, write individual fields to .env
npx @vincentai/cli@latest secret env --key-id abc-123 --env-var ACME_USERNAME --field username
npx @vincentai/cli@latest secret env --key-id abc-123 --env-var ACME_PASSWORD --field password

# Result in .env:
# ACME_USERNAME=alice
# ACME_PASSWORD=hunter2
```

## Output Format

The `secret env` command outputs a confirmation JSON (without the credential value):

```json
{
  "written": "ACME_API_KEY",
  "path": "/path/to/.env",
  "type": "API_KEY"
}
```

The `secret create` command returns:

```json
{
  "keyId": "abc-123",
  "claimUrl": "https://heyvincent.ai/claim/...",
  "secretId": "sec-456"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Overwrite Rejected` | A different API key set this credential's value | Secret owner must manage from the dashboard |
| `404 Value Not Set` | Credential value hasn't been set yet | User must set the value via dashboard or agent sets via CLI |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Important Notes

- **The credential value never enters the agent's context.** The `secret env` command writes directly to a file — it does not print the value to stdout.
- Many agent frameworks (OpenClaw, Claude Code, etc.) blacklist reading `.env` files, providing an additional layer of protection.
- Always share the claim URL with the user after creating a secret.
- The 16KB size limit applies to the serialized value.
- If the overwrite is rejected with a `403`, it means a different API key set the value. The secret owner can manage this from the dashboard.

```

## File: credentials\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-credentials
name: Credentials
path: ecosystem/skills/repo-fetched-agent-skills-054345/credentials
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Credentials
Storage area for 'credentials' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: hyperliquid\SKILL.md
```
---
name: Vincent - HyperLiquid for agents
description: Use this skill to create a HyperLiquid perpetuals and spot wallet for your agent. Trade perps, manage spot balances, transfer USDC between sub-accounts, get prices, place orders — all without exposing private keys.
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - HyperLiquid for agents

Use this skill to create a HyperLiquid perpetuals and spot wallet for your agent. Trade perps, check spot balances, and transfer USDC between perps and spot sub-accounts. The generated EOA **is** the HyperLiquid account — fund it directly via the HL bridge and start trading immediately with no Safe deployment or collateral approval steps.

**The agent never sees the private key.** All operations are executed server-side. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically.

## Security Model

**No environment variables are required.** The agent creates its own HyperLiquid wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure.

**The generated EOA is a standalone HyperLiquid account.** Unlike Polymarket (which deploys a Gnosis Safe), the EOA private key IS the HyperLiquid account. Deposits go directly to this address via the HyperLiquid bridge from Arbitrum, or via `usdSend` from another HL account.

**The agent's API key is not a private key.** It is a scoped Bearer token enforced server-side. The Vincent server evaluates all policies before executing any trade. If a trade violates a policy, the server rejects it. If a trade requires human approval, the server holds it and notifies the wallet owner via Telegram.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The service calls `api.hyperliquid.xyz` server-side on the agent's behalf.

**Key lifecycle:**

- **Creation**: Agent runs `secret create` — Vincent generates the EOA, stores the key, returns `keyId`, `walletAddress`, and `claimUrl`.
- **Claim**: Human operator uses the claim URL to take ownership and configure policies at `https://heyvincent.ai`.
- **Revocation**: Wallet owner revokes the agent's API key from the frontend at any time.
- **Re-linking**: Agent exchanges a one-time re-link token (generated by the owner) for a new key via `secret relink`.

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type HYPERLIQUID_WALLET
```

If a key is returned, use its `id` as `--key-id` for all subsequent commands. If not, create one.

### 2. Create a HyperLiquid Wallet

```bash
npx @vincentai/cli@latest secret create --type HYPERLIQUID_WALLET --memo "My HL perp wallet"
```

Returns:

- `keyId` — use for all future commands
- `walletAddress` — the EOA address (this IS the HyperLiquid account)
- `claimUrl` — share with the user to take ownership

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

**Important:** The wallet is empty at creation. The user must deposit USDC before trading.

### 3. Get Balance

```bash
npx @vincentai/cli@latest hyperliquid balance --key-id <KEY_ID>
```

Returns:

- `walletAddress` — the EOA address
- `accountValue` — total perps account value in USD (cross-margin)
- `withdrawable` — USDC available to withdraw from the perps account
- `positions` — array of open perpetual positions
- `spotBalances` — array of spot token balances (each with `coin`, `token`, `hold`, `total`)

### 4. Transfer Between Perps and Spot

HyperLiquid has separate perps and spot sub-accounts. USDC must be in the correct sub-account before trading. Use `internal-transfer` to move USDC between them.

```bash
# Move 100 USDC from spot → perps (needed before perp trading)
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 100 --to-perp true

# Move 50 USDC from perps → spot (needed before spot trading)
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 50 --to-perp false
```

Parameters:

- `--amount`: USDC amount to transfer (string, numeric)
- `--to-perp`: `true` = spot→perps, `false` = perps→spot

**Response codes:**
- `200` — `status: "executed"` — transfer completed
- `202` — `status: "pending_approval"` (human approval required by policy)
- `403` — `status: "denied"` (rejected by policy)

### 5. Fund the Wallet

Deposit USDC to the EOA address via:

- **HyperLiquid bridge** from Arbitrum: visit `https://app.hyperliquid.xyz/portfolio` and bridge USDC to the EOA address
- **HL→HL transfer** (`usdSend`) from another HL account — instant

Minimum for a BTC perp trade: **$2 USDC** (covers $10 notional at 20x default leverage + taker fees).

### 6. Browse Markets

```bash
npx @vincentai/cli@latest hyperliquid markets --key-id <KEY_ID>
```

Returns a JSON object mapping coin names to mid prices (e.g. `{"BTC": "105234.5", "ETH": "3412.0", ...}`).

### 7. Get Order Book

```bash
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
```

Returns `levels` — a two-element array `[bids, asks]`. Each entry is `[price, size, numOrders]`. Use `levels[1][0][0]` for best ask, `levels[0][0][0]` for best bid.

### 8. Place a Trade

```bash
# Market buy (IoC — fills immediately or cancels)
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 \
  --limit-px 106000 --order-type market

# Market sell to close (reduceOnly)
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy false --sz 0.0001 \
  --limit-px 104000 --order-type market --reduce-only

# GTC limit buy
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 \
  --limit-px 100000 --order-type limit
```

Parameters:

- `--coin`: Asset name (e.g. `BTC`, `ETH`, `SOL`)
- `--is-buy`: `true` for long, `false` for short/close
- `--sz`: Size in base currency (e.g. `0.0001` BTC)
- `--limit-px`: Price. For market orders, set slightly above ask (buy) or below bid (sell) to ensure fill. Recommended: `askPx * 1.005` for buys, `bidPx * 0.995` for sells.
- `--order-type`: `market` (IoC) or `limit` (GTC)
- `--reduce-only`: Pass when closing a position to prevent accidentally opening a new one in the opposite direction

**Minimum notional:** $10 (e.g. 0.0001 BTC at $100k/BTC). Default leverage is 20x cross-margin.

**Response codes:**
- `200` — `status: "executed"` with `orderId` (numeric) and `fillDetails`
- `202` — `status: "pending_approval"` (human approval required by policy)
- `403` — `status: "denied"` (rejected by policy)

### 9. View Open Orders

```bash
# All open orders
npx @vincentai/cli@latest hyperliquid open-orders --key-id <KEY_ID>

# Filter by coin
npx @vincentai/cli@latest hyperliquid open-orders --key-id <KEY_ID> --coin BTC
```

### 10. View Trade History

```bash
# All fills
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID>

# Filter by coin
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID> --coin ETH
```

### 11. Cancel Orders

```bash
# Cancel a specific order (requires coin and numeric order ID)
npx @vincentai/cli@latest hyperliquid cancel-order --key-id <KEY_ID> --coin BTC --oid <ORDER_ID>

# Cancel all open orders
npx @vincentai/cli@latest hyperliquid cancel-all --key-id <KEY_ID>

# Cancel all orders for a specific coin
npx @vincentai/cli@latest hyperliquid cancel-all --key-id <KEY_ID> --coin ETH
```

## Trading Engine: Stop-Loss, Take-Profit & Trailing Stop

The **Trading Engine** fully supports HyperLiquid. You can set automated stop-loss, take-profit, and trailing stop rules on any HL position. Rules execute automatically when price conditions are met — no LLM involved.

For HyperLiquid rules, use `--venue hyperliquid` and set `--market-id` / `--token-id` to the coin name (e.g. `BTC`, `ETH`, `SOL`). The `--trigger-price` is an absolute USD price (not 0–1 like Polymarket).

### Stop-Loss

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

Sells the position if BTC drops to $95,000.

### Take-Profit

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id ETH --token-id ETH \
  --rule-type TAKE_PROFIT --trigger-price 4500
```

Sells the position if ETH rises to $4,500.

### Trailing Stop

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id SOL --token-id SOL \
  --rule-type TRAILING_STOP --trigger-price 170 --trailing-percent 5
```

Stop price ratchets up as SOL rises. Sells if SOL drops 5% from its peak.

### Manage Rules

```bash
# List all rules
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID>

# Update trigger price
npx @vincentai/cli@latest trading-engine update-rule --key-id <KEY_ID> --rule-id <RULE_ID> --trigger-price 98000

# Cancel a rule
npx @vincentai/cli@latest trading-engine delete-rule --key-id <KEY_ID> --rule-id <RULE_ID>

# View rule events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>
```

For full strategy docs (LLM-powered strategies, signal pipeline, drivers), see the **Trading Engine** skill.

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies at `https://heyvincent.ai`. All policies are enforced server-side before any trade executes.

| Policy                      | What it does                                                     |
| --------------------------- | ---------------------------------------------------------------- |
| **Spending limit (per tx)** | Max USD notional per trade                                       |
| **Spending limit (daily)**  | Max USD notional per rolling 24 hours                            |
| **Spending limit (weekly)** | Max USD notional per rolling 7 days                              |
| **Require approval**        | Every trade needs human approval via Telegram                    |
| **Approval threshold**      | Trades above a USD amount need human approval via Telegram       |

If a trade is blocked, the API returns `status: "denied"` with the reason. If approval is needed, `status: "pending_approval"` is returned and the wallet owner receives a Telegram notification.

## Re-linking

If the agent loses its API key:

1. User generates a re-link token from `https://heyvincent.ai`
2. User gives the token to the agent
3. Agent runs:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

Re-link tokens are one-time use and expire after 10 minutes.

## Workflow Example

```bash
# 1. Create wallet
npx @vincentai/cli@latest secret create --type HYPERLIQUID_WALLET --memo "HL wallet"
# → returns keyId, walletAddress, claimUrl

# 2. Tell user: "Fund <walletAddress> on HyperLiquid with USDC, then I can trade."

# 3. Check balance after funding (returns both perps and spot balances)
npx @vincentai/cli@latest hyperliquid balance --key-id <KEY_ID>
# → accountValue shows perps balance, spotBalances shows spot holdings

# 4. Transfer USDC between sub-accounts if needed
# Move 100 USDC from spot → perps before perp trading:
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 100 --to-perp true
# Move 50 USDC from perps → spot before spot trading:
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 50 --to-perp false

# 5. Get BTC mid price
npx @vincentai/cli@latest hyperliquid markets --key-id <KEY_ID>

# 6. Get order book to find best ask
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
# → levels[1][0][0] is best ask, e.g. "105200.0"

# 7. Open long — 0.5% above ask to ensure IoC fill
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 --limit-px 105726 --order-type market

# 8. Check fills
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID> --coin BTC

# 9. Close long — 0.5% below bid
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy false --sz 0.0001 --limit-px 104674 --order-type market --reduce-only
```

## Output Format

All CLI commands return JSON to stdout.

**balance:**
```json
{
  "walletAddress": "0x...",
  "accountValue": "105.23",
  "withdrawable": "95.00",
  "positions": [
    {
      "position": {
        "coin": "BTC",
        "szi": "0.0001",
        "entryPx": "105200.0",
        "positionValue": "10.52",
        "unrealizedPnl": "0.05",
        "liquidationPx": null,
        "leverage": { "type": "cross", "value": 20 }
      },
      "type": "oneWay"
    }
  ],
  "spotBalances": [
    {
      "coin": "USDC",
      "token": 0,
      "hold": "0.0",
      "total": "50.0"
    }
  ]
}
```

**markets:**
```json
{
  "BTC": "105234.5",
  "ETH": "3412.0",
  "SOL": "185.3"
}
```

**orderbook:**
```json
{
  "coin": "BTC",
  "levels": [
    [["105200.0", "0.5", 3], ["105100.0", "1.2", 5]],
    [["105300.0", "0.3", 2], ["105400.0", "0.8", 4]]
  ]
}
```
`levels[0]` = bids (descending), `levels[1]` = asks (ascending). Each entry is `[price, size, numOrders]`. Best bid: `levels[0][0][0]`, best ask: `levels[1][0][0]`.

**trade (executed):**
```json
{
  "orderId": 12345678,
  "status": "executed",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "fillDetails": {
    "totalSz": "0.0001",
    "avgPx": "105250.0"
  }
}
```

**trade (pending approval):**
```json
{
  "status": "pending_approval",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "reason": "Exceeds approval threshold"
}
```

**trade (denied):**
```json
{
  "status": "denied",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "reason": "Exceeds daily spending limit"
}
```

**internal-transfer (executed):**
```json
{
  "status": "executed",
  "transactionLogId": "clx..."
}
```

**internal-transfer (pending approval):**
```json
{
  "status": "pending_approval",
  "transactionLogId": "clx...",
  "reason": "Exceeds approval threshold"
}
```

**internal-transfer (denied):**
```json
{
  "status": "denied",
  "transactionLogId": "clx...",
  "reason": "Exceeds daily spending limit"
}
```

**open-orders:**
```json
{
  "walletAddress": "0x...",
  "openOrders": [
    {
      "coin": "BTC",
      "side": "B",
      "limitPx": "100000.0",
      "sz": "0.0001",
      "oid": 12345678,
      "timestamp": 1700000000000,
      "origSz": "0.0001"
    }
  ]
}
```
`side`: `"B"` = buy/long, `"A"` = ask/sell.

**trades (fills):**
```json
{
  "walletAddress": "0x...",
  "fills": [
    {
      "coin": "BTC",
      "px": "105200.0",
      "sz": "0.0001",
      "side": "B",
      "time": 1700000000000,
      "dir": "Open Long",
      "closedPnl": "0",
      "fee": "0.0105",
      "oid": 12345678
    }
  ]
}
```

**cancel-order / cancel-all:**
```json
{}
```
Empty object on success. Any non-zero exit code indicates failure.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check key-id is correct; re-link if needed |
| `status: "denied"` | Trade blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `status: "pending_approval"` | Trade exceeds approval threshold | Do not retry — wallet owner receives Telegram notification to approve/deny |
| `400 Bad Request` | Invalid parameters (e.g. non-numeric oid, bad coin) | Fix the parameter values |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `500 TRADE_FAILED` | HyperLiquid rejected the order (e.g. insufficient margin, bad price) | Check account balance and order parameters |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

## Important Notes

- **No gas required.** HyperLiquid L1 is gasless — all perp trades settle natively.
- **Perps and spot sub-accounts.** The generated EOA has both a perps sub-account (cross-margin) and a spot sub-account. Use `internal-transfer` to move USDC between them. Deposits via the HL bridge land in the perps account by default.
- **Never try to access raw secret values.** The private key stays server-side.
- Always share the claim URL with the user after creating a wallet.
- For market orders, always set `limitPx` slightly outside the best price (`* 1.005` for buys, `* 0.995` for sells) to guarantee IoC fill at the current market price.
- If a trade returns `status: "pending_approval"`, do not retry — wait for the wallet owner to respond via Telegram.

```

## File: hyperliquid\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-hyperliquid
name: Hyperliquid
path: ecosystem/skills/repo-fetched-agent-skills-054345/hyperliquid
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Hyperliquid
Storage area for 'hyperliquid' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: packages\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-043028-packages
name: Packages
path: ecosystem/skills/repo-fetched-agent-skills-043028/packages
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Packages
Storage area for 'packages' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: packages\clickhouse-best-practices-build\package.json
```
{
  "name": "clickhouse-best-practices-build",
  "version": "0.1.0",
  "description": "Build tooling for ClickHouse Best Practices skill",
  "type": "module",
  "scripts": {
    "build": "bun run build-agents",
    "build-agents": "bun src/build.ts",
    "validate": "bun src/validate.ts",
    "validate-sql": "bun src/validate-sql.ts",
    "check-links": "bun src/check-links.ts",
    "check-external-links": "bun src/check-external-links.ts",
    "dev": "bun run build && bun run validate"
  },
  "keywords": [
    "clickhouse",
    "performance",
    "guidelines",
    "llm",
    "agents"
  ],
  "license": "Apache-2.0",
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  }
}

```

## File: packages\clickhouse-best-practices-build\tsconfig.json
```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "node",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}

```

## File: packages\clickhouse-best-practices-build\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-043028-packages-clickhouse-best-practices-build
name: Clickhouse-Best-Practices-Build
path: ecosystem/skills/repo-fetched-agent-skills-043028/packages/clickhouse-best-practices-build
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Clickhouse-Best-Practices-Build
Storage area for 'clickhouse-best-practices-build' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: packages\clickhouse-best-practices-build\src\build.ts
```
#!/usr/bin/env node
/**
 * Build script to compile individual rule files into AGENTS.md
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readdir, readFile, writeFile } from 'fs/promises'
import { join } from 'path'
import { Rule, Section, GuidelinesDocument, ImpactLevel } from './types.js'
import { parseRuleFile, RuleFile } from './parser.js'
import { RULES_DIR, METADATA_FILE, OUTPUT_FILE, SKILL_DIR } from './config.js'

// Parse command line arguments
const args = process.argv.slice(2)
const upgradeVersion = args.includes('--upgrade-version')

/**
 * Increment a semver-style version string (e.g., "0.1.0" -> "0.1.1", "1.0" -> "1.1")
 */
function incrementVersion(version: string): string {
  const parts = version.split('.').map(Number)
  // Increment the last part
  parts[parts.length - 1]++
  return parts.join('.')
}

/**
 * Generate markdown from rules
 */
function generateMarkdown(
  sections: Section[],
  metadata: {
    version: string
    organization: string
    date: string
    abstract: string
    references?: string[]
    clickhouseVersion?: string
  }
): string {
  let md = `# ClickHouse Best Practices\n\n`
  md += `**Version ${metadata.version}**  \n`
  md += `${metadata.organization}  \n`
  md += `${metadata.date}\n`
  if (metadata.clickhouseVersion) {
    md += `ClickHouse ${metadata.clickhouseVersion}\n`
  }
  md += `\n`
  md += `> **Note:**  \n`
  md += `> This document is mainly for agents and LLMs to follow when designing,  \n`
  md += `> optimizing, or maintaining ClickHouse databases. Humans may also find it  \n`
  md += `> useful, but guidance here is optimized for automation and consistency by  \n`
  md += `> AI-assisted workflows.\n\n`
  md += `---\n\n`
  md += `## Abstract\n\n`
  md += `${metadata.abstract}\n\n`
  md += `---\n\n`
  md += `## Table of Contents\n\n`

  // Generate TOC
  sections.forEach((section) => {
    md += `${section.number}. [${section.title}](#${
      section.number
    }-${section.title.toLowerCase().replace(/\s+/g, '-')}) — **${
      section.impact
    }**\n`
    section.rules.forEach((rule) => {
      // GitHub generates anchors from the full heading text: "1.1 Title" -> "#11-title"
      const anchor = `${rule.id} ${rule.title}`
        .toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w-]/g, '') // Remove special characters except hyphens
      md += `   - ${rule.id} [${rule.title}](#${anchor})\n`
    })
  })

  md += `\n---\n\n`

  // Generate sections
  sections.forEach((section) => {
    md += `## ${section.number}. ${section.title}\n\n`
    md += `**Impact: ${section.impact}${
      section.impactDescription ? ` (${section.impactDescription})` : ''
    }**\n\n`
    if (section.introduction) {
      md += `${section.introduction}\n\n`
    }

    section.rules.forEach((rule) => {
      md += `### ${rule.id} ${rule.title}\n\n`
      md += `**Impact: ${rule.impact}${
        rule.impactDescription ? ` (${rule.impactDescription})` : ''
      }**\n\n`
      md += `${rule.explanation}\n\n`

      rule.examples.forEach((example) => {
        if (example.description) {
          md += `**${example.label}: ${example.description}**\n\n`
        } else {
          md += `**${example.label}:**\n\n`
        }
        // Only generate code block if there's actual code
        if (example.code && example.code.trim()) {
          md += `\`\`\`${example.language || 'sql'}\n`
          md += `${example.code}\n`
          md += `\`\`\`\n\n`
        }
        if (example.additionalText) {
          md += `${example.additionalText}\n\n`
        }
      })

      if (rule.references && rule.references.length > 0) {
        md += `Reference: ${rule.references
          .map((ref) => `[${ref}](${ref})`)
          .join(', ')}\n\n`
      }
    })

    md += `---\n\n`
  })

  // Add references section
  if (metadata.references && metadata.references.length > 0) {
    md += `## References\n\n`
    metadata.references.forEach((ref, i) => {
      md += `${i + 1}. [${ref}](${ref})\n`
    })
  }

  return md
}

/**
 * Main build function
 */
async function build() {
  try {
    console.log('Building AGENTS.md from rules...')
    console.log(`Rules directory: ${RULES_DIR}`)
    console.log(`Output file: ${OUTPUT_FILE}`)

    // Read all rule files (exclude files starting with _ and README.md)
    const files = await readdir(RULES_DIR)
    const ruleFiles = files
      .filter(
        (f) => f.endsWith('.md') && !f.startsWith('_') && f !== 'README.md'
      )
      .sort() // Sort filenames for consistent ordering across systems

    const ruleData: RuleFile[] = []
    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const parsed = await parseRuleFile(filePath)
        ruleData.push(parsed)
      } catch (error) {
        console.error(`Error parsing ${file}:`, error)
      }
    }

    // Group rules by section
    const sectionsMap = new Map<number, Section>()

    ruleData.forEach(({ section, rule }) => {
      if (!sectionsMap.has(section)) {
        sectionsMap.set(section, {
          number: section,
          title: `Section ${section}`, // Will be overridden by section metadata
          impact: rule.impact,
          rules: [],
        })
      }
      sectionsMap.get(section)!.rules.push(rule)
    })

    // Sort rules within each section by title (using en-US locale for consistency across environments)
    sectionsMap.forEach((section) => {
      section.rules.sort((a, b) =>
        a.title.localeCompare(b.title, 'en-US', { sensitivity: 'base' })
      )

      // Assign IDs based on sorted order
      section.rules.forEach((rule, index) => {
        rule.id = `${section.number}.${index + 1}`
        rule.subsection = index + 1
      })
    })

    // Convert to array and sort
    const sections = Array.from(sectionsMap.values()).sort(
      (a, b) => a.number - b.number
    )

    // Read section metadata from consolidated _sections.md file
    const sectionsFile = join(RULES_DIR, '_sections.md')
    try {
      const sectionsContent = await readFile(sectionsFile, 'utf-8')

      // Parse sections using regex to match each section block
      const sectionBlocks = sectionsContent
        .split(/(?=^## \d+\. )/m)
        .filter(Boolean)

      for (const block of sectionBlocks) {
        // Extract section number and title, removing section ID in parentheses
        const headerMatch = block.match(
          /^## (\d+)\.\s+(.+?)(?:\s+\([^)]+\))?$/m
        )
        if (!headerMatch) continue

        const sectionNumber = parseInt(headerMatch[1])
        const sectionTitle = headerMatch[2].trim() // Strip (id) for output

        // Extract impact (format: **Impact:** CRITICAL)
        const impactMatch = block.match(/\*\*Impact:\*\*\s+(\w+(?:-\w+)?)/i)
        const impactLevel = impactMatch
          ? (impactMatch[1].toUpperCase().replace(/-/g, '-') as ImpactLevel)
          : 'MEDIUM'

        // Extract description (format: **Description:** text)
        const descMatch = block.match(
          /\*\*Description:\*\*\s+(.+?)(?=\n\n##|$)/s
        )
        const description = descMatch ? descMatch[1].trim() : ''

        // Update section if it exists
        const section = sections.find((s) => s.number === sectionNumber)
        if (section) {
          section.title = sectionTitle
          section.impact = impactLevel
          section.introduction = description
        }
      }
    } catch (error) {
      console.warn(
        'Warning: Could not read _sections.md, using defaults',
        error
      )
    }

    // Read metadata
    let metadata
    try {
      const metadataContent = await readFile(METADATA_FILE, 'utf-8')
      metadata = JSON.parse(metadataContent)
    } catch {
      metadata = {
        version: '0.1.0',
        organization: 'ClickHouse Inc',
        date: new Date().toLocaleDateString('en-US', {
          month: 'long',
          year: 'numeric',
        }),
        clickhouseVersion: '24.1+',
        abstract:
          'Performance optimization guide for ClickHouse databases, ordered by impact.',
      }
    }

    // Upgrade version if flag is passed
    if (upgradeVersion) {
      const oldVersion = metadata.version
      metadata.version = incrementVersion(oldVersion)
      console.log(`Upgrading version: ${oldVersion} -> ${metadata.version}`)

      // Write updated metadata.json
      await writeFile(METADATA_FILE, JSON.stringify(metadata, null, 2) + '\n', 'utf-8')
      console.log(`✓ Updated metadata.json`)

      // Update SKILL.md frontmatter
      const skillFile = join(SKILL_DIR, 'SKILL.md')
      const skillContent = await readFile(skillFile, 'utf-8')
      const updatedSkillContent = skillContent.replace(
        /^(---[\s\S]*?version:\s*)"[^"]*"([\s\S]*?---)$/m,
        `$1"${metadata.version}"$2`
      )
      await writeFile(skillFile, updatedSkillContent, 'utf-8')
      console.log(`✓ Updated SKILL.md`)
    }

    // Generate markdown
    const markdown = generateMarkdown(sections, metadata)

    // Write output
    await writeFile(OUTPUT_FILE, markdown, 'utf-8')

    console.log(
      `✓ Built AGENTS.md with ${sections.length} sections and ${ruleData.length} rules`
    )
  } catch (error) {
    console.error('Build failed:', error)
    process.exit(1)
  }
}

build()

```

## File: packages\clickhouse-best-practices-build\src\check-external-links.ts
```
#!/usr/bin/env node
/**
 * Check for broken external HTTP/HTTPS links in skill files
 *
 * This script:
 * - Scans all .md and .json files in the skills directory
 * - Extracts HTTP/HTTPS URLs from markdown links and JSON fields
 * - Validates each URL returns a 2XX status code
 * - Processes links asynchronously in batches (max 5 concurrent)
 * - Retries failed links with exponential backoff
 * - Reports detailed errors for any broken links
 */

import { readdir, readFile } from 'fs/promises'
import { join, relative } from 'path'
import { SKILL_DIR } from './config.js'

interface LinkInfo {
  url: string
  source: {
    skill: string
    file: string
  }
}

interface LinkCheckResult {
  url: string
  success: boolean
  statusCode?: number
  error?: string
  source: { skill: string, file: string }
  retriesUsed: number
}

const TIMEOUT_MS = 10000 // 10 seconds
const MAX_RETRIES = 2 // Try up to 2 additional times after initial failure
const CONCURRENCY = 5 // Max concurrent requests per batch
const RETRY_DELAYS = [100, 200, 400] // Exponential backoff delays in ms

/**
 * Extract markdown links from content
 */
function extractMarkdownLinks(content: string): string[] {
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
  const links: string[] = []
  let match

  while ((match = linkRegex.exec(content)) !== null) {
    links.push(match[2])
  }

  return links
}

/**
 * Extract URLs from JSON content (recursively)
 */
function extractJsonUrls(obj: any, urls: string[] = []): string[] {
  if (typeof obj === 'string') {
    if (obj.startsWith('http://') || obj.startsWith('https://')) {
      urls.push(obj)
    }
  } else if (Array.isArray(obj)) {
    for (const item of obj) {
      extractJsonUrls(item, urls)
    }
  } else if (obj !== null && typeof obj === 'object') {
    for (const value of Object.values(obj)) {
      extractJsonUrls(value, urls)
    }
  }
  return urls
}

/**
 * Check if a URL is external (HTTP/HTTPS)
 */
function isExternalUrl(url: string): boolean {
  return url.startsWith('http://') || url.startsWith('https://')
}

/**
 * Sleep for specified milliseconds
 */
function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms))
}

/**
 * Validate a single URL with retry logic
 */
async function validateUrl(
  url: string,
  source: { skill: string, file: string },
  timeout: number = TIMEOUT_MS,
  maxRetries: number = MAX_RETRIES
): Promise<LinkCheckResult> {
  let lastError: string = ''
  let lastStatusCode: number | undefined
  let retriesUsed = 0

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    if (attempt > 0) {
      // Wait before retry with exponential backoff
      const delay = RETRY_DELAYS[Math.min(attempt - 1, RETRY_DELAYS.length - 1)]
      await sleep(delay)
      retriesUsed++
    }

    try {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), timeout)

      try {
        // Try HEAD request first (faster, less bandwidth)
        let response = await fetch(url, {
          method: 'HEAD',
          signal: controller.signal,
          redirect: 'follow'
        })

        // If HEAD fails or returns error, try GET
        if (!response.ok) {
          const headStatusCode = response.status
          response = await fetch(url, {
            method: 'GET',
            signal: controller.signal,
            redirect: 'follow'
          })

          // If GET succeeded but HEAD failed, use GET result
          if (response.ok) {
            clearTimeout(timeoutId)
            return {
              url,
              success: true,
              statusCode: response.status,
              source,
              retriesUsed
            }
          }

          // Both failed, use GET status
          lastStatusCode = response.status
        } else {
          // HEAD succeeded
          clearTimeout(timeoutId)
          return {
            url,
            success: true,
            statusCode: response.status,
            source,
            retriesUsed
          }
        }

        clearTimeout(timeoutId)

        // Check if status code is 2XX
        if (response.status >= 200 && response.status < 300) {
          return {
            url,
            success: true,
            statusCode: response.status,
            source,
            retriesUsed
          }
        }

        lastStatusCode = response.status
        lastError = `${response.status} ${response.statusText}`
      } catch (fetchError: any) {
        clearTimeout(timeoutId)
        throw fetchError
      }
    } catch (error: any) {
      if (error.name === 'AbortError') {
        lastError = 'Request timeout'
      } else if (error.code === 'ENOTFOUND') {
        lastError = 'DNS lookup failed'
      } else if (error.code === 'ECONNREFUSED') {
        lastError = 'Connection refused'
      } else {
        lastError = error.message || 'Unknown error'
      }
    }
  }

  // All retries exhausted
  return {
    url,
    success: false,
    statusCode: lastStatusCode,
    error: lastError,
    source,
    retriesUsed
  }
}

/**
 * Validate URLs in batches with concurrency limit
 */
async function validateUrlsBatch(
  linkInfos: LinkInfo[],
  concurrency: number
): Promise<LinkCheckResult[]> {
  const results: LinkCheckResult[] = []

  // Process in batches
  for (let i = 0; i < linkInfos.length; i += concurrency) {
    const batch = linkInfos.slice(i, i + concurrency)
    const batchResults = await Promise.allSettled(
      batch.map(info => validateUrl(info.url, info.source))
    )

    for (const result of batchResults) {
      if (result.status === 'fulfilled') {
        results.push(result.value)
      } else {
        // This shouldn't happen as validateUrl catches all errors
        // but handle it just in case
        const info = batch[results.length % batch.length]
        results.push({
          url: info.url,
          success: false,
          error: result.reason?.message || 'Unknown error',
          source: info.source,
          retriesUsed: 0
        })
      }
    }

    // Show progress
    console.log(`Checked ${Math.min(i + concurrency, linkInfos.length)}/${linkInfos.length} links...`)
  }

  return results
}

/**
 * Print summary table of results
 */
function printSummaryTable(results: LinkCheckResult[]): void {
  console.log('\n' + '='.repeat(80))
  console.log('External Links Check Summary')
  console.log('='.repeat(80) + '\n')

  // Sort: failures first, then by URL
  const sortedResults = [...results].sort((a, b) => {
    if (a.success !== b.success) {
      return a.success ? 1 : -1
    }
    return a.url.localeCompare(b.url)
  })

  // Print table header
  console.log('┌─────────────────────────────────────────────────────────────────────────────┐')
  console.log('│ URL                                                      │ Status │ Source  │')
  console.log('├──────────────────────────────────────────────────────────┼────────┼─────────┤')

  for (const result of sortedResults) {
    const truncatedUrl = result.url.length > 56
      ? result.url.substring(0, 53) + '...'
      : result.url
    const statusText = result.success
      ? `${result.statusCode} ✓`
      : result.statusCode
        ? `${result.statusCode} ✗`
        : 'ERR ✗'
    const sourceFile = result.source.file.length > 12
      ? '...' + result.source.file.substring(result.source.file.length - 9)
      : result.source.file

    console.log(
      `│ ${truncatedUrl.padEnd(56)} │ ${statusText.padEnd(6)} │ ${sourceFile.padEnd(7)} │`
    )
  }

  console.log('└──────────────────────────────────────────────────────────┴────────┴─────────┘')

  // Print summary counts
  const passed = results.filter(r => r.success).length
  const failed = results.filter(r => !r.success).length
  console.log(`\nSummary: ${results.length} links checked, ${passed} passed, ${failed} failed`)
}

/**
 * Print detailed error information
 */
function printDetailedErrors(results: LinkCheckResult[]): void {
  const failures = results.filter(r => !r.success)

  if (failures.length === 0) {
    return
  }

  console.log('\n✗ External link checking failed:\n')

  for (const failure of failures) {
    console.log(`  ${failure.source.file}`)
    console.log(`    Link: ${failure.url}`)
    if (failure.statusCode) {
      console.log(`    Status: ${failure.statusCode}`)
    }
    if (failure.error) {
      console.log(`    Error: ${failure.error}`)
    }
    console.log(`    (Verified with ${failure.retriesUsed} retries)`)
    console.log('')
  }
}

/**
 * Recursively find all files with given extensions
 * Excludes files starting with underscore (templates and metadata)
 */
async function findFiles(dir: string, extensions: string[]): Promise<string[]> {
  const files: string[] = []

  async function walk(currentDir: string): Promise<void> {
    const entries = await readdir(currentDir, { withFileTypes: true })

    for (const entry of entries) {
      const fullPath = join(currentDir, entry.name)

      if (entry.isDirectory()) {
        await walk(fullPath)
      } else if (entry.isFile()) {
        // Skip files starting with underscore (templates, metadata)
        if (entry.name.startsWith('_')) {
          continue
        }

        const hasExtension = extensions.some(ext => entry.name.endsWith(ext))
        if (hasExtension) {
          files.push(fullPath)
        }
      }
    }
  }

  await walk(dir)
  return files
}

/**
 * Main external link checking function
 */
async function checkExternalLinks(): Promise<void> {
  try {
    console.log('Checking external links...')
    console.log(`Skill directory: ${SKILL_DIR}\n`)

    // Find all .md and .json files
    const files = await findFiles(SKILL_DIR, ['.md', '.json'])
    console.log(`Found ${files.length} files to scan\n`)

    // Collect all external links with their sources
    const linkMap = new Map<string, LinkInfo>()

    for (const filePath of files) {
      const content = await readFile(filePath, 'utf-8')
      const relativePath = relative(SKILL_DIR, filePath)
      let urls: string[] = []

      if (filePath.endsWith('.md')) {
        urls = extractMarkdownLinks(content).filter(isExternalUrl)
      } else if (filePath.endsWith('.json')) {
        try {
          const jsonData = JSON.parse(content)
          urls = extractJsonUrls(jsonData).filter(isExternalUrl)
        } catch (error) {
          console.warn(`Warning: Could not parse JSON file ${relativePath}`)
          continue
        }
      }

      // Add to map (deduplicate URLs, but keep first source)
      for (const url of urls) {
        if (!linkMap.has(url)) {
          linkMap.set(url, {
            url,
            source: {
              skill: 'clickhouse-best-practices',
              file: relativePath
            }
          })
        }
      }
    }

    const uniqueLinks = Array.from(linkMap.values())

    if (uniqueLinks.length === 0) {
      console.log('No external links found')
      return
    }

    console.log(`Found ${uniqueLinks.length} unique external links\n`)

    // Validate all URLs in batches
    const results = await validateUrlsBatch(uniqueLinks, CONCURRENCY)

    // Print summary table
    printSummaryTable(results)

    // Check for failures
    const failures = results.filter(r => !r.success)

    if (failures.length > 0) {
      printDetailedErrors(results)
      process.exit(1)
    } else {
      console.log(`\n✓ All ${results.length} external links are valid`)
    }
  } catch (error) {
    console.error('External link checking failed:', error)
    process.exit(1)
  }
}

checkExternalLinks()

```

## File: packages\clickhouse-best-practices-build\src\check-links.ts
```
#!/usr/bin/env node
/**
 * Check for broken internal links in rule files
 */

import { readdir, readFile } from 'fs/promises'
import { join, basename } from 'path'
import { RULES_DIR } from './config.js'

interface LinkError {
  file: string
  link: string
  message: string
}

/**
 * Extract markdown links from content
 */
function extractLinks(content: string): string[] {
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
  const links: string[] = []
  let match

  while ((match = linkRegex.exec(content)) !== null) {
    links.push(match[2])
  }

  return links
}

/**
 * Check if a link is internal (relative path or anchor)
 */
function isInternalLink(link: string): boolean {
  return !link.startsWith('http://') && !link.startsWith('https://')
}

/**
 * Main link checking function
 */
async function checkLinks() {
  try {
    console.log('Checking internal links in rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    // Read all rule files
    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md'))

    // Build a set of available files (for reference checking)
    const availableFiles = new Set(ruleFiles.map(f => basename(f, '.md')))

    const allErrors: LinkError[] = []

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      const content = await readFile(filePath, 'utf-8')

      // Extract all links
      const links = extractLinks(content)

      // Check internal links
      for (const link of links) {
        if (isInternalLink(link)) {
          // Check if it's a reference to another rule file
          if (link.endsWith('.md')) {
            const referencedFile = basename(link)
            if (!ruleFiles.includes(referencedFile)) {
              allErrors.push({
                file,
                link,
                message: `Referenced file does not exist: ${referencedFile}`
              })
            }
          }
          // Check if it's a reference to a rule by ID (e.g., #21-use-prewhere)
          else if (link.startsWith('#')) {
            // Extract the rule file name from anchor if it follows pattern #section-title
            const anchorMatch = link.match(/^#(\w+)/)
            if (anchorMatch) {
              const prefix = anchorMatch[1]
              // Check if there's a file starting with this prefix
              const hasMatchingFile = ruleFiles.some(f => f.startsWith(prefix))
              if (!hasMatchingFile && !link.match(/^\d+-\d+/)) {
                // Only warn if it's not a standard section anchor (like #1-schema-design)
                // and there's no matching file
                // Skip this check as it's too strict for section anchors
              }
            }
          }
        }
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ Link checking failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file}`)
        console.error(`    Link: ${error.link}`)
        console.error(`    ${error.message}`)
        console.error('')
      })
      process.exit(1)
    } else {
      console.log(`✓ All internal links are valid`)
    }
  } catch (error) {
    console.error('Link checking failed:', error)
    process.exit(1)
  }
}

checkLinks()

```

## File: packages\clickhouse-best-practices-build\src\config.ts
```
/**
 * Configuration for the build tooling
 */

import { join, dirname } from 'path'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))

// Path to the skill directory (relative to this package)
export const SKILL_DIR = join(__dirname, '../../..', 'skills/clickhouse-best-practices')
export const BUILD_DIR = join(__dirname, '..')
export const RULES_DIR = join(SKILL_DIR, 'rules')
export const METADATA_FILE = join(SKILL_DIR, 'metadata.json')
export const OUTPUT_FILE = join(SKILL_DIR, 'AGENTS.md')

```

## File: packages\clickhouse-best-practices-build\src\parser.ts
```
/**
 * Parser for rule markdown files
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readFile } from 'fs/promises'
import { basename } from 'path'
import { Rule, ImpactLevel } from './types.js'

export interface RuleFile {
  section: number
  subsection?: number
  rule: Rule
}

/**
 * Parse a rule markdown file into a Rule object
 */
export async function parseRuleFile(filePath: string): Promise<RuleFile> {
  const rawContent = await readFile(filePath, 'utf-8')
  // Normalize Windows CRLF line endings to LF for consistent parsing
  const content = rawContent.replace(/\r\n/g, '\n')
  const lines = content.split('\n')

  // Extract frontmatter if present
  let frontmatter: Record<string, any> = {}
  let contentStart = 0

  if (content.startsWith('---')) {
    const frontmatterEnd = content.indexOf('---', 3)
    if (frontmatterEnd !== -1) {
      const frontmatterText = content.slice(3, frontmatterEnd).trim()
      frontmatterText.split('\n').forEach((line) => {
        const [key, ...valueParts] = line.split(':')
        if (key && valueParts.length) {
          const value = valueParts.join(':').trim()
          frontmatter[key.trim()] = value.replace(/^["']|["']$/g, '')
        }
      })
      contentStart = frontmatterEnd + 3
    }
  }

  // Parse the rule content
  const ruleContent = content.slice(contentStart).trim()
  const ruleLines = ruleContent.split('\n')

  // Extract title (first # or ## heading)
  let title = ''
  let titleLine = 0
  for (let i = 0; i < ruleLines.length; i++) {
    if (ruleLines[i].startsWith('##')) {
      title = ruleLines[i].replace(/^##+\s*/, '').trim()
      titleLine = i
      break
    }
  }

  // Extract impact
  let impact: Rule['impact'] = 'MEDIUM'
  let impactDescription = ''
  let explanation = ''
  let examples: Rule['examples'] = []
  let references: string[] = []

  // Parse content after title
  let currentExample: {
    label: string
    description?: string
    code: string
    language?: string
    additionalText?: string
  } | null = null
  let inCodeBlock = false
  let codeBlockLanguage = 'sql'
  let codeBlockContent: string[] = []
  let afterCodeBlock = false
  let additionalText: string[] = []
  let hasCodeBlockForCurrentExample = false

  for (let i = titleLine + 1; i < ruleLines.length; i++) {
    const line = ruleLines[i]

    // Impact line
    if (line.includes('**Impact:')) {
      const match = line.match(
        /\*\*Impact:\s*(\w+(?:-\w+)?)\s*(?:\(([^)]+)\))?/i
      )
      if (match) {
        impact = match[1].toUpperCase().replace(/-/g, '-') as ImpactLevel
        impactDescription = match[2] || ''
      }
      continue
    }

    // Code block start
    if (line.startsWith('```')) {
      if (inCodeBlock) {
        // End of code block
        if (currentExample) {
          currentExample.code = codeBlockContent.join('\n')
          currentExample.language = codeBlockLanguage
        }
        codeBlockContent = []
        inCodeBlock = false
        afterCodeBlock = true
      } else {
        // Start of code block
        inCodeBlock = true
        hasCodeBlockForCurrentExample = true
        codeBlockLanguage = line.slice(3).trim() || 'sql'
        codeBlockContent = []
        afterCodeBlock = false
      }
      continue
    }

    if (inCodeBlock) {
      codeBlockContent.push(line)
      continue
    }

    // Example label (Incorrect, Correct, Example, Usage, Implementation, etc.)
    // Match pattern: **Label:** or **Label (description):** at end of line
    // This distinguishes example labels from inline bold text like "**Trade-off:** some text"
    const labelMatch = line.match(/^\*\*([^:]+?):\*?\*?$/)
    if (labelMatch) {
      // Save previous example if it exists
      if (currentExample) {
        if (additionalText.length > 0) {
          currentExample.additionalText = additionalText.join('\n\n')
          additionalText = []
        }
        examples.push(currentExample)
      }
      afterCodeBlock = false
      hasCodeBlockForCurrentExample = false

      const fullLabel = labelMatch[1].trim()
      // Try to extract description from parentheses if present (handles simple cases)
      // For nested parentheses like "Incorrect (O(n) per lookup)", we keep the full label
      const descMatch = fullLabel.match(
        /^([A-Za-z]+(?:\s+[A-Za-z]+)*)\s*\(([^()]+)\)$/
      )
      currentExample = {
        label: descMatch ? descMatch[1].trim() : fullLabel,
        description: descMatch ? descMatch[2].trim() : undefined,
        code: '',
        language: codeBlockLanguage,
      }
      continue
    }

    // Reference links
    if (line.startsWith('Reference:') || line.startsWith('References:')) {
      // Save current example before processing references
      if (currentExample) {
        if (additionalText.length > 0) {
          currentExample.additionalText = additionalText.join('\n\n')
          additionalText = []
        }
        examples.push(currentExample)
        currentExample = null
      }

      const refMatch = line.match(/\[([^\]]+)\]\(([^)]+)\)/g)
      if (refMatch) {
        references.push(
          ...refMatch.map((ref) => {
            const m = ref.match(/\[([^\]]+)\]\(([^)]+)\)/)
            return m ? m[2] : ref
          })
        )
      }
      continue
    }

    // Regular text (explanation or additional context after examples)
    if (line.trim() && !line.startsWith('#')) {
      if (!currentExample && !inCodeBlock) {
        // Main explanation before any examples
        explanation += (explanation ? '\n\n' : '') + line
      } else if (currentExample && (afterCodeBlock || !hasCodeBlockForCurrentExample)) {
        // Text after a code block, or text in a section without a code block
        // (e.g., "When NOT to use this pattern:" with bullet points instead of code)
        additionalText.push(line)
      }
    }
  }

  // Handle last example if still open
  if (currentExample) {
    if (additionalText.length > 0) {
      currentExample.additionalText = additionalText.join('\n\n')
    }
    examples.push(currentExample)
  }

  // Infer section from filename patterns
  // Pattern: area-description.md where area determines section
  const filename = basename(filePath)
  const sectionMap: Record<string, number> = {
    schema: 1,
    query: 2,
    insert: 3,
    table: 4,
    index: 5,
    materialized: 6,
    cluster: 7,
    ops: 8,
    performance: 9,
  }

  // Extract area from filename (first part before first dash)
  const area = filename.split('-')[0]
  const section = frontmatter.section || sectionMap[area] || 0

  const rule: Rule = {
    id: '', // Will be assigned by build script based on sorted order
    title: frontmatter.title || title,
    section: section,
    subsection: undefined,
    impact: frontmatter.impact || impact,
    impactDescription: frontmatter.impactDescription || impactDescription,
    explanation: frontmatter.explanation || explanation.trim(),
    examples,
    references: frontmatter.references
      ? frontmatter.references.split(',').map((r: string) => r.trim())
      : references,
    tags: frontmatter.tags
      ? frontmatter.tags.split(',').map((t: string) => t.trim())
      : undefined,
  }

  return {
    section,
    subsection: 0,
    rule,
  }
}

```

## File: packages\clickhouse-best-practices-build\src\types.ts
```
/**
 * Type definitions for ClickHouse Best Practices rules
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

export type ImpactLevel = 'CRITICAL' | 'HIGH' | 'MEDIUM-HIGH' | 'MEDIUM' | 'LOW-MEDIUM' | 'LOW'

export interface CodeExample {
  label: string // e.g., "Incorrect", "Correct", "Example"
  description?: string // Optional description before code
  code: string
  language?: string // Default: 'sql'
  additionalText?: string // Optional text after code block (explanations, reasons)
}

export interface Rule {
  id: string // e.g., "1.1", "2.3"
  title: string
  section: number // Main section number (1-8)
  subsection?: number // Subsection number within section
  impact: ImpactLevel
  impactDescription?: string // e.g., "2-10× improvement"
  explanation: string
  examples: CodeExample[]
  references?: string[] // URLs or citations
  tags?: string[] // For categorization/search
}

export interface Section {
  number: number
  title: string
  impact: ImpactLevel
  impactDescription?: string
  introduction?: string
  rules: Rule[]
}

export interface GuidelinesDocument {
  version: string
  organization: string
  date: string
  abstract: string
  sections: Section[]
  references?: string[]
  clickhouseVersion?: string
}

```

## File: packages\clickhouse-best-practices-build\src\validate-sql.ts
```
#!/usr/bin/env node
/**
 * Validate SQL syntax in rule files using ClickHouse binary
 */

import { readdir, readFile, writeFile, mkdir, chmod, stat } from 'fs/promises'
import { join } from 'path'
import { tmpdir } from 'os'
import { exec } from 'child_process'
import { promisify } from 'util'
import { parseRuleFile } from './parser.js'
import { RULES_DIR, BUILD_DIR } from './config.js'

const execAsync = promisify(exec)

const CLICKHOUSE_VERSION = '24.1.8.22'
const CLICKHOUSE_BINARY_NAME = 'clickhouse'
const CLICKHOUSE_DIR = join(BUILD_DIR, 'bin')
const CLICKHOUSE_BINARY = join(CLICKHOUSE_DIR, CLICKHOUSE_BINARY_NAME)

interface SQLValidationError {
  file: string
  ruleTitle: string
  exampleLabel: string
  error: string
  sql: string
}

/**
 * Detect the current platform
 */
function getPlatform(): 'macos' | 'linux' | 'unsupported' {
  const platform = process.platform
  if (platform === 'darwin') return 'macos'
  if (platform === 'linux') return 'linux'
  return 'unsupported'
}

/**
 * Get the download URL for ClickHouse binary
 */
function getDownloadUrl(): string | null {
  const platform = getPlatform()
  if (platform === 'macos') {
    return `https://github.com/ClickHouse/ClickHouse/releases/download/v${CLICKHOUSE_VERSION}/clickhouse-macos`
  } else if (platform === 'linux') {
    return `https://github.com/ClickHouse/ClickHouse/releases/download/v${CLICKHOUSE_VERSION}/clickhouse`
  }
  return null
}

/**
 * Download ClickHouse binary if not present
 */
async function ensureClickHouse(): Promise<boolean> {
  try {
    // Check if binary already exists
    await stat(CLICKHOUSE_BINARY)
    console.log('✓ ClickHouse binary found')
    return true
  } catch {
    // Binary doesn't exist, need to download
    console.log('Downloading ClickHouse binary...')

    const url = getDownloadUrl()
    if (!url) {
      console.error('✗ Unsupported platform. SQL validation requires macOS or Linux.')
      return false
    }

    try {
      // Create bin directory if it doesn't exist
      await mkdir(CLICKHOUSE_DIR, { recursive: true })

      // Download using curl
      await execAsync(`curl -L -o "${CLICKHOUSE_BINARY}" "${url}"`)

      // Make executable
      await chmod(CLICKHOUSE_BINARY, 0o755)

      console.log('✓ ClickHouse binary downloaded')
      return true
    } catch (error) {
      console.error('✗ Failed to download ClickHouse binary:', error)
      return false
    }
  }
}

/**
 * Check if SQL contains dangerous patterns that could access external resources
 * Handles various obfuscation techniques: comments, whitespace, case variations
 */
function containsDangerousPatterns(sql: string): string | null {
  // Remove comments to prevent bypass via file/**/() or file--\n()
  const sqlNoComments = sql
    .replace(/\/\*[\s\S]*?\*\//g, ' ')  // Remove /* */ comments
    .replace(/--[^\n]*/g, ' ')           // Remove -- comments
    .replace(/\s+/g, ' ')                // Normalize whitespace

  const dangerous = [
    // File and network access
    { pattern: /\bfile\s*\(/i, description: 'file() table function (file system access)' },
    { pattern: /\burl\s*\(/i, description: 'url() table function (HTTP access)' },
    { pattern: /\bs3\s*\(/i, description: 's3() table function (cloud storage access)' },

    // Database connections
    { pattern: /\bmysql\s*\(/i, description: 'mysql() table function (database access)' },
    { pattern: /\bpostgresql\s*\(/i, description: 'postgresql() table function (database access)' },
    { pattern: /\bmongodb\s*\(/i, description: 'mongodb() table function (database access)' },
    { pattern: /\bhdfs\s*\(/i, description: 'hdfs() table function (HDFS access)' },
    { pattern: /\bodbc\s*\(/i, description: 'odbc() table function (ODBC access)' },
    { pattern: /\bjdbc\s*\(/i, description: 'jdbc() table function (JDBC access)' },

    // Command execution and remote access
    { pattern: /\bexecutable\s*\(/i, description: 'executable() table function (command execution)' },
    { pattern: /\bremote\s*\(/i, description: 'remote() table function (remote server access)' },
    { pattern: /\bcluster\s*\(/i, description: 'cluster() table function (cluster access)' },
    { pattern: /\binput\s*\(/i, description: 'input() table function (stdin access)' },

    // Timing and error-based exfiltration
    { pattern: /\bsleep\s*\(/i, description: 'sleep() function (timing attack vector)' },
    { pattern: /\bthrowIf\s*\(/i, description: 'throwIf() function (error-based exfiltration)' },

    // Note: system.* tables are allowed as they're commonly used in examples
    // and clickhouse-local runs in isolation with no sensitive data
  ]

  for (const { pattern, description } of dangerous) {
    if (pattern.test(sqlNoComments)) {
      return `Security: SQL contains dangerous pattern: ${description}`
    }
  }

  return null
}

/**
 * Validate a single SQL snippet
 */
async function validateSQL(sql: string): Promise<string | null> {
  // First check for dangerous patterns
  const dangerousPattern = containsDangerousPatterns(sql)
  if (dangerousPattern) {
    return dangerousPattern
  }

  // Write SQL to temporary file
  const tmpFile = join(tmpdir(), `clickhouse-validate-${Date.now()}.sql`)
  await writeFile(tmpFile, sql, 'utf-8')

  try {
    // Run clickhouse-local with the SQL file in restricted mode
    // Security restrictions to prevent arbitrary file/network access:
    // - readonly=2: Strictest readonly mode, blocks DDL and writes
    // - allow_introspection_functions=0: Blocks introspection functions
    // - allow_ddl=0: Explicitly disable DDL operations
    // - max_execution_time=10: Kill queries after 10 seconds (DoS protection)
    // - max_memory_usage=100000000: Limit memory to 100MB (DoS protection)
    // - max_rows_to_read=1000000: Limit rows read (DoS protection)
    // - user_files_path: Set to nonexistent path to block file() function
    // - format_schema_path: Set to nonexistent path to block schema loading
    // Note: Pattern blocking provides primary defense; these are secondary
    const { stderr } = await execAsync(
      `"${CLICKHOUSE_BINARY}" local --query-file "${tmpFile}" --output-format Null ` +
      `--readonly=2 --allow_introspection_functions=0 --allow_ddl=0 ` +
      `--max_execution_time=10 --max_memory_usage=100000000 --max_rows_to_read=1000000 ` +
      `--user_files_path="/dev/null" --format_schema_path="/dev/null" ` +
      `2>&1 || true`
    )

    // ClickHouse returns errors in stderr
    if (stderr && (stderr.includes('Exception') || stderr.includes('Error'))) {
      return stderr.trim()
    }

    return null
  } catch (error) {
    if (error instanceof Error) {
      return error.message
    }
    return String(error)
  } finally {
    // Clean up temp file
    try {
      await execAsync(`rm -f "${tmpFile}"`)
    } catch {}
  }
}

/**
 * Main validation function
 */
async function validateSQLInRules() {
  try {
    console.log('Validating SQL syntax in rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    // Ensure ClickHouse binary is available
    const hasClickHouse = await ensureClickHouse()
    if (!hasClickHouse) {
      console.warn('⚠ Skipping SQL validation (ClickHouse binary not available)')
      process.exit(0)
    }

    // Read all rule files
    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md') && !f.startsWith('_') && f !== 'README.md')

    const allErrors: SQLValidationError[] = []
    let totalSQLExamples = 0

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const { rule } = await parseRuleFile(filePath)

        // Extract SQL examples
        for (const example of rule.examples) {
          if (example.code && example.code.trim() && (example.language === 'sql' || !example.language)) {
            totalSQLExamples++
            const error = await validateSQL(example.code)

            if (error) {
              allErrors.push({
                file,
                ruleTitle: rule.title,
                exampleLabel: example.label,
                error,
                sql: example.code.slice(0, 100) + (example.code.length > 100 ? '...' : '')
              })
            }
          }
        }
      } catch (error) {
        console.error(`Error processing ${file}:`, error)
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ SQL validation failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file} (${error.ruleTitle})`)
        console.error(`    Example: ${error.exampleLabel}`)
        console.error(`    SQL: ${error.sql}`)
        console.error(`    Error: ${error.error}`)
        console.error('')
      })
      process.exit(1)
    } else {
      console.log(`✓ All ${totalSQLExamples} SQL examples are valid`)
    }
  } catch (error) {
    console.error('SQL validation failed:', error)
    process.exit(1)
  }
}

validateSQLInRules()

```

## File: packages\clickhouse-best-practices-build\src\validate.ts
```
#!/usr/bin/env node
/**
 * Validate rule files follow the correct structure
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readdir } from 'fs/promises'
import { join } from 'path'
import { Rule } from './types.js'
import { parseRuleFile } from './parser.js'
import { RULES_DIR } from './config.js'

interface ValidationError {
  file: string
  ruleId?: string
  message: string
}

/**
 * Validate a rule
 */
function validateRule(rule: Rule, file: string): ValidationError[] {
  const errors: ValidationError[] = []

  // Note: rule.id is auto-generated during build, not required in source files

  if (!rule.title || rule.title.trim().length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing or empty title' })
  }

  if (!rule.explanation || rule.explanation.trim().length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing or empty explanation' })
  }

  if (!rule.examples || rule.examples.length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing examples (need at least one bad and one good example)' })
  } else {
    // Filter out informational examples (notes, trade-offs, etc.) that don't have code
    const codeExamples = rule.examples.filter(e => e.code && e.code.trim().length > 0)

    const hasBad = codeExamples.some(e =>
      e.label.toLowerCase().includes('incorrect') ||
      e.label.toLowerCase().includes('wrong') ||
      e.label.toLowerCase().includes('bad')
    )
    const hasGood = codeExamples.some(e =>
      e.label.toLowerCase().includes('correct') ||
      e.label.toLowerCase().includes('good') ||
      e.label.toLowerCase().includes('usage') ||
      e.label.toLowerCase().includes('implementation') ||
      e.label.toLowerCase().includes('example')
    )

    if (codeExamples.length === 0) {
      errors.push({ file, ruleId: rule.id, message: 'Missing code examples' })
    } else if (!hasBad && !hasGood) {
      errors.push({ file, ruleId: rule.id, message: 'Missing bad/incorrect or good/correct examples' })
    }
  }

  const validImpacts: Rule['impact'][] = ['CRITICAL', 'HIGH', 'MEDIUM-HIGH', 'MEDIUM', 'LOW-MEDIUM', 'LOW']
  if (!validImpacts.includes(rule.impact)) {
    errors.push({ file, ruleId: rule.id, message: `Invalid impact level: ${rule.impact}. Must be one of: ${validImpacts.join(', ')}` })
  }

  return errors
}

/**
 * Main validation function
 */
async function validate() {
  try {
    console.log('Validating rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md') && !f.startsWith('_'))

    const allErrors: ValidationError[] = []

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const { rule } = await parseRuleFile(filePath)
        const errors = validateRule(rule, file)
        allErrors.push(...errors)
      } catch (error) {
        allErrors.push({
          file,
          message: `Failed to parse: ${error instanceof Error ? error.message : String(error)}`
        })
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ Validation failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file}${error.ruleId ? ` (${error.ruleId})` : ''}: ${error.message}`)
      })
      process.exit(1)
    } else {
      console.log(`✓ All ${ruleFiles.length} rule files are valid`)
    }
  } catch (error) {
    console.error('Validation failed:', error)
    process.exit(1)
  }
}

validate()

```

## File: packages\clickhouse-best-practices-build\src\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-043028-packages-clickhouse-best-practices-build-src
name: Src
path: ecosystem/skills/repo-fetched-agent-skills-043028/packages/clickhouse-best-practices-build/src
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Src
Storage area for 'src' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: polymarket\SKILL.md
```
---
name: Vincent - Polymarket for agents
description: |
  Polymarket prediction market trading for agents. Use this skill when users want to create a
  Polymarket wallet, browse markets, place bets, manage positions, or withdraw funds.
  Triggers on "polymarket", "prediction market", "place bet", "browse markets", "trade prediction",
  "polymarket wallet", "betting", "market odds".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - Polymarket for agents

Use this skill to create a Polymarket wallet for your agent and trade on prediction markets. Browse markets, place bets, track holdings, and manage orders — all without exposing private keys to the agent. Wallets use Gnosis Safe on Polygon with gasless trading through Polymarket's relayer.

**The agent never sees the private key.** All operations are executed server-side. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies. The private key never leaves the Vincent server.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent trading with human oversight via server-side controls**. Understanding this model is important:

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own Polymarket wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure. The CLI stores the returned API key automatically during wallet creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet/` or `./agentwallet/`) are declared in this skill's metadata.

**The agent's API key is not a private key.** It is a scoped Bearer token that can only execute actions within the policies set by the wallet owner. The Vincent server enforces all policies server-side — the agent cannot bypass them regardless of what it sends. If a trade violates a policy, the server rejects it. If a trade requires approval, the server holds it and notifies the wallet owner via Telegram for out-of-band human approval.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous Polymarket trading capabilities. The agent is expected to invoke trading actions (browse markets, place bets, manage positions) on its own, within the boundaries the human operator defines. The human controls what the agent can do through policies (spending limits, approval thresholds) — not by gating individual invocations. The stored key is scoped and policy-constrained — even if another process reads it, it can only perform actions the wallet owner's policies allow, and the owner can revoke it instantly.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted. The agent does not read, collect, or transmit any data beyond what is needed for Polymarket wallet operations.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership and configure policies at `https://heyvincent.ai`.
- **Revocation**: The wallet owner can revoke the agent's API key at any time from the Vincent frontend. Revoked keys are rejected immediately by the server.
- **Re-linking**: If the agent loses its API key, the wallet owner generates a one-time re-link token and the agent exchanges it for a new key via `secret relink`.
- **Rotation**: The wallet owner can revoke the current key and issue a re-link token to rotate credentials at any time.

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type POLYMARKET_WALLET
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new wallet.

### 2. Create a Polymarket Wallet

```bash
npx @vincentai/cli@latest secret create --type POLYMARKET_WALLET --memo "My prediction market wallet"
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `walletAddress` (the EOA address; Safe is deployed lazily on first use).

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

**Important:** After creation, the wallet has no funds. The user must send **USDC.e (bridged USDC)** on Polygon to the Safe address before placing bets.

### 3. Get Balance

```bash
npx @vincentai/cli@latest polymarket balance --key-id <KEY_ID>
```

Returns:

- `walletAddress` — the Safe address (deployed on first call if needed)
- `collateral.balance` — USDC.e balance available for trading
- `collateral.allowance` — approved amount for Polymarket contracts

**Note:** The first balance call triggers Safe deployment and collateral approval (gasless via relayer). This may take 30-60 seconds.

### 4. Fund the Wallet

Before placing bets, the user must send USDC.e to the Safe address:

1. Get the wallet address from the balance command
2. Send USDC.e (bridged USDC, contract `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`) on Polygon to that address
3. Minimum $1 required per bet (Polymarket minimum)

**Do not send native USDC** (`0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359`). Polymarket only accepts bridged USDC.e.

### 5. Transfer from Vincent EVM Wallet (Alternative Funding Method)

If you have a Vincent EVM wallet with funds, you can transfer directly to your Polymarket wallet using the wallet `transfer-between` commands (see the wallet skill). Vincent verifies you own both secrets and automatically handles token conversion and cross-chain bridging to get USDC.e on Polygon.

```bash
# Preview the transfer first (use your EVM wallet key-id)
npx @vincentai/cli@latest wallet transfer-between preview --key-id <EVM_KEY_ID> \
  --to-secret-id <POLYMARKET_SECRET_ID> --from-chain 8453 --to-chain 137 \
  --token-in 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 --amount 10 \
  --token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 --slippage 100

# Execute the transfer
npx @vincentai/cli@latest wallet transfer-between execute --key-id <EVM_KEY_ID> \
  --to-secret-id <POLYMARKET_SECRET_ID> --from-chain 8453 --to-chain 137 \
  --token-in 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 --amount 10 \
  --token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 --slippage 100
```

**Key points:**

- Use your **EVM wallet's key-id** (not the Polymarket key-id) for these commands
- The `--to-secret-id` must be your Polymarket wallet's secret ID
- For Polymarket destinations, only `--to-chain 137` (Polygon) and `--token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` (USDC.e) are allowed
- The server verifies you own both secrets — transfers to other users' wallets are rejected
- For cross-chain transfers, check status with `wallet transfer-between status --key-id <EVM_KEY_ID> --relay-id <RELAY_REQUEST_ID>`

### 6. Browse & Search Markets

```bash
# Search markets by keyword (recommended)
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --query bitcoin --limit 20

# Search by Polymarket URL or slug
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --slug btc-updown-5m-1771380900

# Or use a full Polymarket URL as the slug parameter
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --slug https://polymarket.com/event/btc-updown-5m-1771380900

# Get all active markets
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --active --limit 50

# Get specific market by condition ID
npx @vincentai/cli@latest polymarket market --key-id <KEY_ID> --condition-id <CONDITION_ID>
```

**Market response includes:**

- `question`: The market question
- `outcomes`: Array like `["Yes", "No"]` or `["Team A", "Team B"]`
- `outcomePrices`: Current prices for each outcome
- `tokenIds`: **Array of token IDs for each outcome** — use these for placing bets
- `acceptingOrders`: Whether the market is open for trading
- `closed`: Whether the market has resolved

**Important:** Always use the `tokenIds` array from the market response. Each outcome has a corresponding token ID at the same index. For a "Yes/No" market:

- `tokenIds[0]` = "Yes" token ID
- `tokenIds[1]` = "No" token ID

### 7. Get Order Book

```bash
npx @vincentai/cli@latest polymarket orderbook --key-id <KEY_ID> --token-id <TOKEN_ID>
```

Returns bids and asks with prices and sizes. Use this to determine current market prices before placing orders.

### 8. Place a Bet

```bash
npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id <TOKEN_ID> --side BUY --amount 5 --price 0.55
```

Parameters:

- `--token-id`: The outcome token ID (from market data or order book)
- `--side`: `BUY` or `SELL`
- `--amount`: For BUY orders, USD amount to spend. For SELL orders, number of shares to sell.
- `--price`: Optional limit price (0.01 to 0.99). Omit for market order. ALWAYS use a market order unless the user specifies a limit price.

**BUY orders:**

- `amount` is the USD you want to spend (e.g., `5` = $5)
- You'll receive `amount / price` shares (e.g., $5 at 0.50 = 10 shares)
- Minimum order is $1

**SELL orders:**

- `amount` is the number of shares to sell
- You'll receive `amount * price` USD
- Must own the shares first (from a previous BUY)

**Important timing:** After a BUY fills, wait a few seconds before selling. Shares need time to settle on-chain.

If a trade violates a policy, the server returns an error explaining which policy was triggered. If a trade requires human approval (based on the approval threshold policy), the server returns `status: "pending_approval"` and the wallet owner receives a Telegram notification to approve or deny.

### 9. View Holdings, Open Orders & Trades

```bash
# Get current holdings with P&L (recommended for viewing positions)
npx @vincentai/cli@latest polymarket holdings --key-id <KEY_ID>

# Get open orders (unfilled limit orders in the order book)
npx @vincentai/cli@latest polymarket open-orders --key-id <KEY_ID>

# Filter open orders by market
npx @vincentai/cli@latest polymarket open-orders --key-id <KEY_ID> --market <CONDITION_ID>

# Get trade history
npx @vincentai/cli@latest polymarket trades --key-id <KEY_ID>
```

**Holdings** returns all positions with shares owned, average entry price, current price, and unrealized P&L. This is the best endpoint for:

- Checking current positions before placing sell orders
- Setting up stop-loss or take-profit rules
- Calculating total portfolio value and performance
- Showing the user their active bets

**Open Orders** returns unfilled limit orders waiting in the order book.

**Trades** returns historical trade activity.

### 10. Cancel Orders

```bash
# Cancel specific order
npx @vincentai/cli@latest polymarket cancel-order --key-id <KEY_ID> --order-id <ORDER_ID>

# Cancel all open orders
npx @vincentai/cli@latest polymarket cancel-all --key-id <KEY_ID>
```

### 11. Redeem Resolved Positions

After a market resolves, winning positions can be redeemed to convert conditional tokens back into USDC.e. Use the holdings command to check which positions have `redeemable: true`, then call redeem.

```bash
# Redeem all redeemable positions
npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID>

# Redeem specific markets by condition ID
npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID> --condition-ids 0xabc123,0xdef456
```

If no positions are redeemable, `redeemed` will be an empty array and no transaction is submitted.

**How it works:** Redemption is gasless (executed via Polymarket's relayer through the Safe). For standard markets, it calls `redeemPositions` on the CTF contract. For negative-risk markets, it calls `redeemPositions` on the NegRiskAdapter. Both types are handled automatically.

**When to redeem:** Check holdings periodically. After a market resolves, it may take some time before positions become redeemable. Look for `redeemable: true` in the holdings response.

### 12. Withdraw USDC

Transfer USDC.e from your Polymarket Safe to any Ethereum address on Polygon. This is gasless — executed via Polymarket's relayer.

```bash
npx @vincentai/cli@latest polymarket withdraw --key-id <KEY_ID> --to <RECIPIENT_ADDRESS> --amount <AMOUNT>
```

Parameters:

- `--to`: Recipient Ethereum address (0x..., 42 characters)
- `--amount`: Amount in USDC (human-readable, e.g. "100" = 100 USDC)

**Response:**

- `status`: `"executed"`, `"pending_approval"`, or `"denied"`
- `transactionHash`: Polygon transaction hash (only if executed)
- `walletAddress`: The Safe address that sent the funds

If the amount exceeds the wallet's USDC balance, the server returns an `INSUFFICIENT_BALANCE` error. Policy checks (spending limits, approval thresholds) apply to withdrawals the same way they apply to bets.

## Output Format

CLI commands return JSON to stdout. Market search results:

```json
{
  "markets": [
    {
      "question": "Will Bitcoin exceed $100k?",
      "outcomes": ["Yes", "No"],
      "outcomePrices": ["0.65", "0.35"],
      "tokenIds": ["123456...", "789012..."],
      "acceptingOrders": true
    }
  ]
}
```

Bet placement:

```json
{
  "orderId": "0x...",
  "status": "MATCHED",
  "side": "BUY",
  "price": "0.55",
  "size": "9.09"
}
```

For trades requiring human approval:

```json
{
  "status": "pending_approval",
  "message": "Transaction requires owner approval via Telegram"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Policy Violation` | Trade blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `INSUFFICIENT_BALANCE` | Not enough USDC.e for the trade | Fund the wallet with USDC.e on Polygon |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `pending_approval` | Trade exceeds approval threshold | User will receive Telegram notification to approve/deny |
| `No orderbook exists` | Market closed or wrong token ID | Verify `acceptingOrders: true` and use `tokenIds[]`, not `conditionId` |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies via the claim URL at `https://heyvincent.ai`. All policies are enforced server-side by the Vincent API — the agent cannot bypass or modify them. If a trade violates a policy, the API rejects it. If a trade triggers an approval threshold, the API holds it and sends the wallet owner a Telegram notification for out-of-band human approval.

| Policy                      | What it does                                                     |
| --------------------------- | ---------------------------------------------------------------- |
| **Spending limit (per tx)** | Max USD value per transaction                                    |
| **Spending limit (daily)**  | Max USD value per rolling 24 hours                               |
| **Spending limit (weekly)** | Max USD value per rolling 7 days                                 |
| **Require approval**        | Every transaction needs human approval via Telegram              |
| **Approval threshold**      | Transactions above a USD amount need human approval via Telegram |

Before the wallet is claimed, the agent can operate without policy restrictions. This is by design: agent-first onboarding allows the agent to begin trading immediately. Once the human operator claims the wallet via the claim URL, they can add any combination of policies to constrain the agent's behavior. The wallet owner can also revoke the agent's API key entirely at any time.

## Re-linking (Recovering API Access)

If the agent loses its API key, the wallet owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new scoped API key.

**How it works:**

1. The user generates a re-link token from the wallet detail page at `https://heyvincent.ai`
2. The user gives the token to the agent (e.g. by pasting it in chat)
3. The agent runs the relink command:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Use this `keyId` for all subsequent commands.

**Important:** Re-link tokens are one-time use and expire after 10 minutes, so it's safe for users to send you a relink token through chat since you will immediately consume it.

## Workflow Example

1. **Create wallet:**

   ```bash
   npx @vincentai/cli@latest secret create --type POLYMARKET_WALLET --memo "Betting wallet"
   ```

2. **Get Safe address (triggers deployment):**

   ```bash
   npx @vincentai/cli@latest polymarket balance --key-id <KEY_ID>
   # Returns walletAddress — give this to user to fund
   ```

3. **User sends USDC.e to the Safe address on Polygon**

4. **Search for a market:**

   ```bash
   # Search by keyword — returns only active, tradeable markets
   # Tip: use short keyword phrases; stop-words like "or" can cause empty results
   npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --query "bitcoin up down" --active
   ```

5. **Check order book for the outcome you want:**

   ```bash
   npx @vincentai/cli@latest polymarket orderbook --key-id <KEY_ID> --token-id 123456...
   ```

6. **Place BUY bet using the correct token ID:**

   ```bash
   # tokenId must be from the tokenIds array, NOT the conditionId
   npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456... --side BUY --amount 5 --price 0.55
   ```

7. **Wait for settlement** (a few seconds)

8. **Sell position:**

   ```bash
   npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456... --side SELL --amount 9.09 --price 0.54
   ```

9. **Redeem after market resolves** (if holding through resolution):

   ```bash
   # Check holdings for redeemable positions
   npx @vincentai/cli@latest polymarket holdings --key-id <KEY_ID>
   # If redeemable: true, redeem to get USDC.e back
   npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID>
   ```

10. **Withdraw USDC to another wallet:**

    ```bash
    npx @vincentai/cli@latest polymarket withdraw --key-id <KEY_ID> --to 0xRecipientAddress --amount 50
    ```

## Important Notes

- **After any bet or trade**, share the user's Polymarket profile link so they can verify and view their positions: `https://polymarket.com/profile/<polymarketWalletAddress>` (use the wallet's Safe address).
- **No gas needed.** All Polymarket transactions are gasless via Polymarket's relayer.
- **Never try to access raw secret values.** The private key stays server-side — that's the whole point.
- Always share the claim URL with the user after creating a wallet.
- If a transaction is rejected, it may be blocked by a server-side policy. Tell the user to check their policy settings at `https://heyvincent.ai`.
- If a transaction requires approval, it will return `status: "pending_approval"`. The wallet owner will receive a Telegram notification to approve or deny.

See the **Error Handling** section above for a full list of common errors and resolutions.

```

## File: polymarket\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-polymarket
name: Polymarket
path: ecosystem/skills/repo-fetched-agent-skills-054345/polymarket
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Polymarket
Storage area for 'polymarket' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: scripts\agents_template.md
```
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

## File: scripts\generate_agents.py
```
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

## File: scripts\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-scripts
name: Scripts
path: ecosystem/skills/repo-fetched-agent-skills-124622/scripts
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Scripts
Storage area for 'scripts' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_skills_144258-skills
name: Skills
path: ecosystem/skills/repo_fetched_agent_skills_144258/skills
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skills
Storage area for 'skills' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-actor-development\SKILL.md
```
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
6. **Write documentation** - Create comprehensive README.md for the marketplace (see [references/actor-readme.md](references/actor-readme.md) — this is mandatory, not optional)
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

See [references/logging.md](references/logging.md) for complete logging documentation including available log levels and best practices for JavaScript/TypeScript and Python.

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
storage/key_value_stores/default/INPUT.json
```

This file should contain the input parameters defined in your `.actor/input_schema.json`. The actor will read this input when running locally, mirroring how it receives input on the Apify platform.

**IMPORTANT - Local storage is NOT synced to the Apify Console:**
- Running `apify run` stores all data (datasets, key-value stores, request queues) **only on your local filesystem** in the `storage/` directory.
- This data is **never** automatically uploaded or pushed to the Apify platform. It exists only on your machine.
- To verify results on the Apify Console, you must deploy the Actor with `apify push` and then run it on the platform.
- Do **not** rely on checking the Apify Console to verify results from local runs — instead, inspect the local `storage/` directory or check the Actor's log output.

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
storage/                # Local-only storage (NOT synced to Apify Console)
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

## Actor README

**IMPORTANT:** Always generate a README.md as part of Actor development. The README is the Actor's landing page on Apify Store and is critical for discoverability (SEO), user onboarding, and support. Do not consider an Actor complete without a proper README.

See [references/actor-readme.md](references/actor-readme.md) for the required structure, SEO best practices, and content guidelines. Also review these top Actors for best practices:

- [Instagram Scraper](https://apify.com/apify/instagram-scraper)
- [Google Maps Scraper](https://apify.com/compass/crawler-google-places)

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

## File: skills\apify-actor-development\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-actor-development
name: Apify-Actor-Development
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-actor-development
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Apify-Actor-Development
Storage area for 'apify-actor-development' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-actor-development\references\actor_json.md
```
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

## File: skills\apify-actor-development\references\actor_readme.md
```
# Actor README Guidelines

The README is the Actor's landing page on Apify Store. It serves as SEO content, first impression, usage guide, and support resource. **Always generate a README.md when creating or deploying an Actor.**

## Required Structure

Write in Markdown. Use H2 (`##`) for main sections (these form the table of contents) and H3 (`###`) for subsections. Do not use H1 — the Actor name is automatically used as H1.

### 1. What does [Actor name] do?

- 1-2 sentences explaining what the Actor does and doesn't do
- Include a link to the target website
- Mention keywords like "API" (e.g., "Instagram API alternative")
- Bold the most important terms

### 2. Why use [Actor name]? / Why scrape [target site]?

- Business use cases and benefits
- List main features and capabilities
- Highlight Apify platform advantages: scheduling, API access, integrations, proxy rotation, monitoring

### 3. What data can [Actor name] extract?

- Table showing main data fields the Actor outputs (field name, type, description)
- Don't list every field — focus on the most useful and understandable ones

### 4. How to scrape [target site]

- Numbered step-by-step tutorial (Google may pick these up as rich snippets)
- Include a link to blog tutorials if they exist

### 5. How much will it cost to scrape [target site]?

- Set pricing expectations based on the Actor's pricing model
- For pay-per-result: mention free tier limits and what larger plans offer
- For compute units: explain average data volume per dollar
- Cost-related questions rank well in Google search

### 6. Input

- Reference the input tab: "See the input tab for full configuration options"
- Explain any complex input fields or special formatting requirements
- Screenshot of the input schema is optional but helpful

### 7. Output

- Include: "You can download the dataset in various formats such as JSON, HTML, CSV, or Excel"
- Show a simplified JSON output example (2-3 items)
- If output is complex, show separate examples for different data types

### 8. Tips / Advanced options (if applicable)

- How to limit compute unit usage
- How to get more accurate results or improve speed

### 9. FAQ, Disclaimers, and Support

- Legal/scraping disclaimer (use this template and customize with the target site name):
  > Our Actors are ethical and do not extract any private user data, such as email addresses, gender, or location. They only extract what the user has chosen to share publicly. We therefore believe that our Actors, when used for ethical purposes by Apify users, are safe. However, you should be aware that your results could contain personal data. Personal data is protected by the GDPR in the European Union and by other regulations around the world. You should not scrape personal data unless you have a legitimate reason to do so. If you're unsure whether your reason is legitimate, consult your lawyers.
- Common troubleshooting tips
- Mention the Issues tab for feedback
- Link to API tab for programmatic access
- Use cases for the extracted data

## SEO Best Practices

- Include keywords naturally in H2/H3 headings (e.g., "How to scrape Instagram" not just "How to use")
- Target "People Also Ask" style questions as H3 headings
- Aim for at least 300 words total
- Embed a YouTube video URL if available (renders automatically as a player)
- Make images clickable with links

## Tone

- Match the README tone to the target audience skill level
- For no-code users: use plain language, avoid code blocks early on
- For developers: include technical details, code examples, and API references
- Be clear about what technical knowledge is needed to use the Actor

## Reference Actors

Before writing a README, review these top Actors on the Apify Store for best practices on structure, tone, and content:

- [Instagram Scraper](https://apify.com/apify/instagram-scraper)
- [Google Maps Scraper](https://apify.com/compass/crawler-google-places)

## Key Rules

- Always write the README as part of Actor development — do not skip this step
- The first 25% of the README is what most visitors read — put the most important info there
- Use emojis sparingly as bullet points to break up text
- Keep images compressed but good quality
- Use [Carbon](https://github.com/carbon-app/carbon) for code snippet screenshots if needed

```

## File: skills\apify-actor-development\references\dataset_schema.md
```
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

## File: skills\apify-actor-development\references\input_schema.md
```
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

## File: skills\apify-actor-development\references\key_value_store_schema.md
```
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

## File: skills\apify-actor-development\references\logging.md
```
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

## File: skills\apify-actor-development\references\output_schema.md
```
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

## File: skills\apify-actor-development\references\standby_mode.md
```
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

## File: skills\apify-actor-development\references\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-actor-development-references
name: References
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-actor-development/references
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# References
Storage area for 'references' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-actorization\SKILL.md
```
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

If not installed, use one of these methods (listed in order of preference):

```bash
# Preferred: install via a package manager (provides integrity checks)
npm install -g apify-cli

# Or (Mac): brew install apify-cli
```

> **Security note:** Do NOT install the CLI by piping remote scripts to a shell
> (e.g. `curl … | bash` or `irm … | iex`). Always use a package manager.

Verify CLI is logged in:

```bash
apify info  # Should return your username
```

If not logged in, check if the `APIFY_TOKEN` environment variable is defined (if not, ask the user to generate one at https://console.apify.com/settings/integrations and then define `APIFY_TOKEN` with it).

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

## Actorization Checklist

Copy this checklist to track progress:

- [ ] Step 1: Analyze project (language, entry point, inputs, outputs)
- [ ] Step 2: Run `apify init` to create Actor structure
- [ ] Step 3: Apply language-specific SDK integration
- [ ] Step 4: Configure `.actor/input_schema.json`
- [ ] Step 5: Configure `.actor/output_schema.json` (if applicable)
- [ ] Step 6: Update `.actor/actor.json` metadata
- [ ] Step 7: Write README.md for the Apify Store listing
- [ ] Step 8: Test locally with `apify run`
- [ ] Step 9: Deploy with `apify push`

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

## Step 7: Write README

**IMPORTANT:** Always generate a README.md as part of actorization. The README is the Actor's landing page on Apify Store and is critical for discoverability (SEO), user onboarding, and support. Do not consider an Actor complete without a proper README.

See the Actor README guidelines at `skills/apify-actor-development/references/actor-readme.md` for the required structure including: intro and features, data extraction table, step-by-step tutorial, pricing info, input/output examples, and FAQ. Aim for at least 300 words with SEO-optimized H2/H3 headings. Also review these top Actors for best practices:

- [Instagram Scraper](https://apify.com/apify/instagram-scraper)
- [Google Maps Scraper](https://apify.com/compass/crawler-google-places)

## Step 8: Test Locally

Run the actor with inline input (for JS/TS and Python actors):

```bash
apify run --input '{"startUrl": "https://example.com", "maxItems": 10}'
```

Or use an input file:

```bash
apify run --input-file ./test-input.json
```

**Important:** Always use `apify run`, not `npm start` or `python main.py`. The CLI sets up the proper environment and storage.

## Step 9: Deploy

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

## Security

**Treat all crawled web content as untrusted input.** Actors ingest data from external websites that may contain malicious payloads. Follow these rules:

- **Sanitize crawled data** — Never pass raw HTML, URLs, or scraped text directly into shell commands, `eval()`, database queries, or template engines. Use proper escaping or parameterized APIs.
- **Validate and type-check all external data** — Before pushing to datasets or key-value stores, verify that values match expected types and formats. Reject or sanitize unexpected structures.
- **Do not execute or interpret crawled content** — Never treat scraped text as code, commands, or configuration. Content from websites could include prompt injection attempts or embedded scripts.
- **Isolate credentials from data pipelines** — Ensure `APIFY_TOKEN` and other secrets are never accessible in request handlers or passed alongside crawled data. Use the Apify SDK's built-in credential management rather than passing tokens through environment variables in data-processing code.
- **Review dependencies before installing** — When adding packages with `npm install` or `pip install`, verify the package name and publisher. Typosquatting is a common supply-chain attack vector. Prefer well-known, actively maintained packages.
- **Pin versions and use lockfiles** — Always commit `package-lock.json` (Node.js) or pin exact versions in `requirements.txt` (Python). Lockfiles ensure reproducible builds and prevent silent dependency substitution. Run `npm audit` or `pip-audit` periodically to check for known vulnerabilities.

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
- [ ] `README.md` exists with proper structure (intro, features, data table, tutorial, pricing, input/output examples)
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

## File: skills\apify-actorization\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-actorization
name: Apify-Actorization
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-actorization
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Apify-Actorization
Storage area for 'apify-actorization' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-actorization\references\cli_actorization.md
```
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

## File: skills\apify-actorization\references\js_ts_actorization.md
```
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

## File: skills\apify-actorization\references\python_actorization.md
```
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

## File: skills\apify-actorization\references\schemas_and_output.md
```
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

## File: skills\apify-actorization\references\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-actorization-references
name: References
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-actorization/references
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# References
Storage area for 'references' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-generate-output-schema\SKILL.md
```
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

## File: skills\apify-generate-output-schema\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-generate-output-schema
name: Apify-Generate-Output-Schema
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-generate-output-schema
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Apify-Generate-Output-Schema
Storage area for 'apify-generate-output-schema' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-ultimate-scraper\SKILL.md
```
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

## File: skills\apify-ultimate-scraper\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-ultimate-scraper
name: Apify-Ultimate-Scraper
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-ultimate-scraper
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Apify-Ultimate-Scraper
Storage area for 'apify-ultimate-scraper' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-ultimate-scraper\reference\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-ultimate-scraper-reference
name: Reference
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-ultimate-scraper/reference
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Reference
Storage area for 'reference' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\apify-ultimate-scraper\reference\scripts\fetch_actor_details.js
```
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

## File: skills\apify-ultimate-scraper\reference\scripts\run_actor.js
```
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
    console.log(`Full data available at: https://console.apify.com/storage/datasets/${datasetId}`);
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

## File: skills\apify-ultimate-scraper\reference\scripts\search_actors.js
```
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

## File: skills\apify-ultimate-scraper\reference\scripts\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-124622-skills-apify-ultimate-scraper-reference-scripts
name: Scripts
path: ecosystem/skills/repo-fetched-agent-skills-124622/skills/apify-ultimate-scraper/reference/scripts
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Scripts
Storage area for 'scripts' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\clickhouse-best-practices\agents.md
```
# ClickHouse Best Practices

**Version 0.1.0**  
ClickHouse Inc  
January 2026
ClickHouse 24.1+

> **Note:**  
> This document is mainly for agents and LLMs to follow when designing,  
> optimizing, or maintaining ClickHouse databases. Humans may also find it  
> useful, but guidance here is optimized for automation and consistency by  
> AI-assisted workflows.

---

## Abstract

Comprehensive best practices for ClickHouse database optimization. Covers schema design, query optimization, table engines, indexing strategies, materialized views, distributed operations, and operational best practices. Each rule includes detailed explanations, SQL examples comparing incorrect vs. correct implementations, and specific impact metrics to guide database design and query optimization.

---

## Table of Contents

1. [Schema Design](#1-schema-design) — **CRITICAL**
   - 1.1 [Avoid Nullable Unless Semantically Required](#11-avoid-nullable-unless-semantically-required)
   - 1.2 [Consider Starting Without Partitioning](#12-consider-starting-without-partitioning)
   - 1.3 [Filter on ORDER BY Columns in Queries](#13-filter-on-order-by-columns-in-queries)
   - 1.4 [Keep Partition Cardinality Low (100-1,000 Values)](#14-keep-partition-cardinality-low-100-1000-values)
   - 1.5 [Minimize Bit-Width for Numeric Types](#15-minimize-bit-width-for-numeric-types)
   - 1.6 [Order Columns by Cardinality (Low to High)](#16-order-columns-by-cardinality-low-to-high)
   - 1.7 [Plan PRIMARY KEY Before Table Creation](#17-plan-primary-key-before-table-creation)
   - 1.8 [Prioritize Filter Columns in ORDER BY](#18-prioritize-filter-columns-in-order-by)
   - 1.9 [Understand Partition Query Performance Trade-offs](#19-understand-partition-query-performance-trade-offs)
   - 1.10 [Use Enum for Finite Value Sets](#110-use-enum-for-finite-value-sets)
   - 1.11 [Use JSON Type for Dynamic Schemas](#111-use-json-type-for-dynamic-schemas)
   - 1.12 [Use LowCardinality for Repeated Strings](#112-use-lowcardinality-for-repeated-strings)
   - 1.13 [Use Native Types Instead of String](#113-use-native-types-instead-of-string)
   - 1.14 [Use Partitioning for Data Lifecycle Management](#114-use-partitioning-for-data-lifecycle-management)
2. [Query Optimization](#2-query-optimization) — **CRITICAL**
   - 2.1 [Choose the Right JOIN Algorithm](#21-choose-the-right-join-algorithm)
   - 2.2 [Consider Alternatives to JOINs](#22-consider-alternatives-to-joins)
   - 2.3 [Filter Tables Before Joining](#23-filter-tables-before-joining)
   - 2.4 [Optimize NULL Handling in Outer JOINs](#24-optimize-null-handling-in-outer-joins)
   - 2.5 [Use ANY JOIN When Only One Match Needed](#25-use-any-join-when-only-one-match-needed)
   - 2.6 [Use Data Skipping Indices for Non-ORDER BY Filters](#26-use-data-skipping-indices-for-non-order-by-filters)
   - 2.7 [Use Incremental MVs for Real-Time Aggregations](#27-use-incremental-mvs-for-real-time-aggregations)
   - 2.8 [Use Refreshable MVs for Complex Joins and Batch Workflows](#28-use-refreshable-mvs-for-complex-joins-and-batch-workflows)
3. [Insert Strategy](#3-insert-strategy) — **CRITICAL**
   - 3.1 [Avoid ALTER TABLE DELETE](#31-avoid-alter-table-delete)
   - 3.2 [Avoid ALTER TABLE UPDATE](#32-avoid-alter-table-update)
   - 3.3 [Avoid OPTIMIZE TABLE FINAL](#33-avoid-optimize-table-final)
   - 3.4 [Batch Inserts Appropriately (10K-100K rows)](#34-batch-inserts-appropriately-10k-100k-rows)
   - 3.5 [Use Async Inserts for High-Frequency Small Batches](#35-use-async-inserts-for-high-frequency-small-batches)
   - 3.6 [Use Native Format for Best Insert Performance](#36-use-native-format-for-best-insert-performance)

---

## 1. Schema Design

**Impact: CRITICAL**

Proper schema design is foundational to ClickHouse performance. ORDER BY is immutable after table creation; wrong choices require full data migration. Includes primary key selection, data types, partitioning strategy, and JSON usage. Column types and ordering can impact query speed by orders of magnitude.

### 1.1 Avoid Nullable Unless Semantically Required

**Impact: HIGH (Nullable adds storage overhead; use DEFAULT values instead)**

Nullable columns maintain a separate UInt8 column for tracking null values, increasing storage and degrading performance. Use DEFAULT values instead when feasible.

**Incorrect: Nullable everywhere**

```sql
CREATE TABLE users (
    id Nullable(UInt64),              -- IDs should never be null
    name Nullable(String),            -- Empty string is fine
    age Nullable(UInt8),              -- 0 is a valid default
    login_count Nullable(UInt32)      -- 0 is a valid default
)
```

**Correct: DEFAULT values, Nullable only when semantic**

```sql
CREATE TABLE users (
    id UInt64,                                    -- Never null
    name String DEFAULT '',                       -- Empty = unknown
    age UInt8 DEFAULT 0,                          -- 0 = unknown
    login_count UInt32 DEFAULT 0,                 -- 0 = never logged in
    deleted_at Nullable(DateTime),                -- NULL = not deleted (semantic!)
    parent_id Nullable(UInt64)                    -- NULL = no parent (semantic!)
)
```

**When Nullable IS appropriate:**

| Use Case | Why |

|----------|-----|

| `deleted_at` | NULL = "not deleted", timestamp = "deleted at X" |

| `parent_id` | NULL = "no parent", value = "has parent" |

| `discount_percent` | NULL = "no discount", 0 = "0% discount" |

**Defaults instead of Nullable:**

| Type | Default |

|------|---------|

| String | `''` (empty string) |

| UInt*/Int* | `0` |

| DateTime | `now()` or `toDateTime(0)` |

| UUID | `generateUUIDv4()` |

Reference: [https://clickhouse.com/docs/best-practices/select-data-types](https://clickhouse.com/docs/best-practices/select-data-types)

### 1.2 Consider Starting Without Partitioning

**Impact: MEDIUM (Add partitioning later when you have clear lifecycle requirements)**

Start without partitioning and add it later only if:

- You have clear data lifecycle requirements (retention, archiving)

- Your access patterns clearly benefit from partition pruning

- You understand the cardinality implications

**Example: start simple**

```sql
-- Start simple, no partitioning
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Add partitioning later if needed for lifecycle management
-- (requires table recreation or materialized view migration)
```

**When to add partitioning:**

| Need | Add Partitioning? |

|------|-------------------|

| Time-based data retention | Yes |

| Archive old data to cold storage | Yes |

| Query performance on time ranges | Maybe (test first) |

| No specific lifecycle needs | No |

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

### 1.3 Filter on ORDER BY Columns in Queries

**Impact: CRITICAL (Skipping prefix columns prevents index usage)**

Even with good schema design, queries must use ORDER BY columns to benefit. Skipping prefix columns or filtering on non-ORDER BY columns prevents index usage.

**Incorrect: skips prefix or uses non-ORDER BY columns**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Skips prefix columns - can't use index effectively
SELECT * FROM events WHERE event_type = 'click';

-- Filter on column not in ORDER BY - full table scan
SELECT * FROM events WHERE user_agent LIKE '%Chrome%';
```

**Correct: uses ORDER BY prefix**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Full prefix match - best performance
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click';

-- Partial prefix - still uses index
SELECT * FROM events WHERE tenant_id = 123;

-- Range on later column after equality on earlier
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click' AND timestamp >= '2024-01-01';
```

**Index usage reference:**

| Filter | Index Used? |

|--------|-------------|

| `WHERE tenant_id = 123` | Full |

| `WHERE tenant_id = 123 AND event_type = 'click'` | Full |

| `WHERE event_type = 'click'` | None (skipped prefix) |

| `WHERE timestamp > '2024-01-01'` | None (skipped both) |

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-primary-key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

### 1.4 Keep Partition Cardinality Low (100-1,000 Values)

**Impact: HIGH (Too many partitions cause part explosion and 'too many parts' errors)**

Too many distinct partition values create excessive data parts, eventually triggering "too many parts" errors. ClickHouse enforces limits via `max_parts_in_total` and `parts_to_throw_insert` settings.

**Incorrect: high cardinality partitioning**

```sql
-- High cardinality = too many partitions
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY user_id  -- Millions of partitions!
ORDER BY (timestamp);

-- Daily partitions can grow unbounded over years
CREATE TABLE logs (...)
ENGINE = MergeTree()
PARTITION BY toDate(timestamp)  -- 3650 partitions over 10 years
ORDER BY (service, timestamp);
```

**Correct: bounded cardinality**

```sql
-- Monthly partitions = 12 per year, bounded cardinality
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp);
```

**Validation:**

```sql
-- Check partition count and health
SELECT
    partition,
    count() as parts,
    sum(rows) as rows,
    formatReadableSize(sum(bytes_on_disk)) as size
FROM system.parts
WHERE table = 'events' AND active
GROUP BY partition
ORDER BY partition;

-- Warning signs: hundreds or thousands of partitions
```

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

### 1.5 Minimize Bit-Width for Numeric Types

**Impact: HIGH (Smaller types reduce storage and improve cache efficiency)**

Select the smallest numeric type that accommodates your data range. Prefer unsigned types when negative values aren't needed.

**Incorrect: oversized types**

```sql
CREATE TABLE metrics (
    status_code Int64,        -- HTTP codes are 100-599
    age Int64,                -- Human age fits in UInt8
    year Int64,               -- Years fit in UInt16
    item_count Int64          -- Often small numbers
)
```

**Correct: right-sized types**

```sql
CREATE TABLE metrics (
    status_code UInt16,       -- 0-65,535 (HTTP codes fit easily)
    age UInt8,                -- 0-255 (sufficient for age)
    year UInt16,              -- 0-65,535 (sufficient for years)
    item_count UInt32         -- 0-4 billion (adjust based on actual max)
)
```

**Numeric Type Reference:**

| Type | Range | Bytes |

|------|-------|-------|

| UInt8 | 0 to 255 | 1 |

| UInt16 | 0 to 65,535 | 2 |

| UInt32 | 0 to 4.3 billion | 4 |

| UInt64 | 0 to 18 quintillion | 8 |

| Int8 | -128 to 127 | 1 |

| Int16 | -32,768 to 32,767 | 2 |

| Int32 | -2.1 billion to 2.1 billion | 4 |

| Int64 | -9 quintillion to 9 quintillion | 8 |

Reference: [https://clickhouse.com/docs/best-practices/select-data-types](https://clickhouse.com/docs/best-practices/select-data-types)

### 1.6 Order Columns by Cardinality (Low to High)

**Impact: CRITICAL (Enables granule skipping; high-cardinality first prevents index pruning)**

Since the sparse primary index operates on data blocks (granules) rather than individual rows, low-cardinality leading columns create more useful index entries that can skip entire blocks. Place lower-cardinality columns before higher-cardinality ones in the ordering key.

**Incorrect: high cardinality first**

```sql
-- UUID first means no pruning benefit
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id, event_type, timestamp);
-- Every granule has different event_id values, index can't skip anything
```

**Correct: low cardinality first**

```sql
-- Low cardinality first enables pruning
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_type, event_date, event_id);
-- Index can skip entire event_type groups
```

**Column Order Guidelines:**

| Position | Cardinality | Examples |

|----------|-------------|----------|

| 1st | Low (few distinct values) | event_type, status, country |

| 2nd | Date (coarse granularity) | toDate(timestamp) |

| 3rd+ | Medium-High | user_id, session_id |

| Last | High (if needed) | event_id, uuid |

**Tip:** Use `toDate(timestamp)` instead of raw `DateTime` columns when day-level filtering suffices - this reduces index size from 32-bit to 16-bit representations.

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-primary-key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

### 1.7 Plan PRIMARY KEY Before Table Creation

**Impact: CRITICAL (ORDER BY is immutable; wrong choice requires full data migration)**

ClickHouse's ORDER BY clause defines physical data ordering and the sparse index. Unlike other databases, **ORDER BY cannot be modified after table creation**. A wrong choice requires creating a new table and migrating all data.

**Incorrect: arbitrary ORDER BY without query analysis**

```sql
-- Creating table without analyzing query patterns
CREATE TABLE events (
    event_id UUID,
    user_id UInt64,
    timestamp DateTime
)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Chosen arbitrarily

-- Later: "Most queries filter by user_id!"
-- Cannot fix with: ALTER TABLE events MODIFY ORDER BY (user_id, timestamp)
-- ERROR: Cannot modify ORDER BY
```

**Correct: query-driven ORDER BY selection**

```sql
-- Step 1: Document query patterns BEFORE creating table
/*
Query Analysis:
- 60% of queries: WHERE user_id = ? AND timestamp BETWEEN ? AND ?
- 25% of queries: WHERE event_type = ? AND timestamp > ?
- 15% of queries: WHERE event_id = ?

Conclusion: user_id and event_type are primary filters
*/

-- Step 2: Create table with correct ORDER BY
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    user_id UInt64,
    event_type LowCardinality(String),
    timestamp DateTime,
    event_date Date DEFAULT toDate(timestamp)
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(event_date)
ORDER BY (user_id, event_date, event_id);
```

**Pre-creation checklist:**

- [ ] Listed top 5-10 query patterns

- [ ] Identified columns in WHERE clauses with frequency

- [ ] Prioritized columns that exclude large numbers of rows

- [ ] Ordered columns by cardinality (low first, high last)

- [ ] Limited to 4-5 key columns (typically sufficient)

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-primary-key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

### 1.8 Prioritize Filter Columns in ORDER BY

**Impact: CRITICAL (Columns not in ORDER BY cause full table scans)**

Prioritize columns frequently used in query filters (WHERE clause), especially those that exclude large numbers of rows. Queries filtering on columns not in ORDER BY result in full table scans.

**Incorrect: ORDER BY doesn't match query patterns**

```sql
-- If most queries filter by tenant_id:
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Queries by tenant_id will full-scan!
```

**Correct: ORDER BY matches filter patterns**

```sql
-- ORDER BY matches query filter patterns
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (tenant_id, event_date, event_id);

-- Query now uses primary index:
SELECT * FROM events WHERE tenant_id = 123 AND event_date >= '2024-01-01';
```

**Validation:**

```sql
-- Verify index usage
EXPLAIN indexes = 1
SELECT * FROM events WHERE tenant_id = 123;
-- Look for "PrimaryKey" with Key Condition
```

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-primary-key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

### 1.9 Understand Partition Query Performance Trade-offs

**Impact: MEDIUM (Partition pruning helps some queries; spanning many partitions hurts others)**

Partitioning can help or hurt query performance:

- **Potential improvement**: Queries filtering by partition key may benefit from partition pruning

- **Potential degradation**: Queries spanning many partitions increase total parts scanned

ClickHouse automatically builds **MinMax indexes** on partition columns. Data merges occur **within partitions only**, not across them.

**Incorrect: query scans all partitions**

```sql
-- Query must scan all partitions
SELECT count(*) FROM events
WHERE event_type = 'click';  -- No partition pruning
```

**Correct: query prunes to single partition**

```sql
-- Query prunes to single partition
SELECT count(*) FROM events
WHERE timestamp >= '2024-01-01' AND timestamp < '2024-02-01'
  AND event_type = 'click';
```

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

### 1.10 Use Enum for Finite Value Sets

**Impact: MEDIUM (Insert-time validation and natural ordering; 1-2 bytes storage)**

Enum types provide validation at insert time and enable queries that exploit natural ordering. Use Enum8 (up to 256 values) or Enum16 (up to 65,536 values).

**Incorrect: String without validation**

```sql
CREATE TABLE orders (
    status String    -- No validation, typos like "shiped" allowed
)

-- Ordering requires CASE statements
SELECT * FROM orders ORDER BY
    CASE status
        WHEN 'pending' THEN 1
        WHEN 'processing' THEN 2
        WHEN 'shipped' THEN 3
    END;
```

**Correct: Enum with validation and ordering**

```sql
CREATE TABLE orders (
    status Enum8('pending' = 1, 'processing' = 2, 'shipped' = 3, 'delivered' = 4)
)

-- Insert validation: invalid values rejected
INSERT INTO orders VALUES ('shiped');  -- ERROR: Unknown element 'shiped'

-- Natural ordering works automatically
SELECT * FROM orders ORDER BY status;  -- Orders by enum value (1, 2, 3, 4)

-- Comparisons use natural order
SELECT * FROM orders WHERE status > 'processing';  -- shipped and delivered
```

**Enum Guidelines:**

| Scenario | Use |

|----------|-----|

| Fixed set of values known at schema time | Enum8/Enum16 |

| Values may change frequently | LowCardinality(String) |

| Need insert-time validation | Enum |

| Need natural ordering in queries | Enum |

| < 256 distinct values | Enum8 (1 byte) |

| 256-65,536 distinct values | Enum16 (2 bytes) |

Reference: [https://clickhouse.com/docs/best-practices/select-data-types](https://clickhouse.com/docs/best-practices/select-data-types)

### 1.11 Use JSON Type for Dynamic Schemas

**Impact: MEDIUM (Field-level querying for semi-structured data; use typed columns for known schemas)**

ClickHouse's JSON type splits JSON objects into separate sub-columns, enabling field-level query optimization. Use it for truly dynamic data, not everything.

**Incorrect: schema bloat or opaque String**

```sql
-- BAD: Hundreds of nullable columns for event properties
CREATE TABLE events (
    event_id UUID,
    prop_page_url Nullable(String),
    prop_button_id Nullable(String),
    -- ... 100 more nullable columns
)

-- BAD: JSON as String when you need field queries
CREATE TABLE events (
    event_id UUID,
    properties String  -- No field-level optimization
)
```

**Correct: JSON for dynamic, typed for known**

```sql
-- Use JSON type for dynamic properties
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    event_type LowCardinality(String),
    timestamp DateTime DEFAULT now(),
    properties JSON  -- Flexible schema with type inference
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Query JSON paths directly
SELECT
    event_type,
    properties.url as page_url,
    properties.amount as purchase_amount
FROM events
WHERE event_type = 'page_view' AND properties.url = '/home';
```

**When to use JSON:**

```sql
CREATE TABLE events (
    properties JSON(
        url String,
        amount Float64,
        product_id UInt64
    )
)
```

| Scenario | Use JSON? |

|----------|-----------|

| Data structure varies unpredictably | Yes |

| Field types/schemas change over time | Yes |

| Need field-level querying | Yes |

| Fixed, known schema | No (use typed columns) |

| JSON as opaque blob (no field queries) | No (use String) |

**Optimization: specify types for known paths:**

Reference: [https://clickhouse.com/docs/best-practices/use-json-where-appropriate](https://clickhouse.com/docs/best-practices/use-json-where-appropriate)

### 1.12 Use LowCardinality for Repeated Strings

**Impact: HIGH (Dictionary encoding for <10K unique values; significant storage reduction)**

String columns with repeated values store each value repeatedly. LowCardinality uses dictionary encoding for significant storage reduction.

**Incorrect: plain String for repeated values**

```sql
CREATE TABLE events (
    country String,       -- "United States" stored 500M times
    browser String,       -- "Chrome" stored 300M times
    event_type String     -- "page_view" stored 800M times
)
```

**Correct: LowCardinality for low unique counts**

```sql
CREATE TABLE events (
    country LowCardinality(String),      -- ~200 unique values
    browser LowCardinality(String),      -- ~50 unique values
    event_type LowCardinality(String)    -- ~100 unique values
)
```

**When to use LowCardinality:**

```sql
-- Check cardinality before deciding
SELECT uniq(column_name) FROM table_name;
```

| Unique Values | Recommendation |

|---------------|----------------|

| < 10,000 | Use LowCardinality |

| > 10,000 | Use regular String |

**LowCardinality vs FixedString:**

```sql
-- FixedString: Only for truly fixed-length data
country_code FixedString(2),    -- "US", "DE", "JP" - always 2 chars

-- LowCardinality: For variable-length low-cardinality strings
country_name LowCardinality(String),  -- "United States", "Germany"
```

Reserve `FixedString` for strictly fixed-length data (e.g., 2-char country codes). For most low-cardinality text, `LowCardinality(String)` outperforms `FixedString`.

Reference: [https://clickhouse.com/docs/best-practices/select-data-types](https://clickhouse.com/docs/best-practices/select-data-types)

### 1.13 Use Native Types Instead of String

**Impact: CRITICAL (2-10x storage reduction; enables compression and correct semantics)**

Using String for all data wastes storage, prevents compression optimization, and makes comparisons slower. ClickHouse's column-oriented architecture benefits directly from optimal type selection.

**Incorrect: String for everything**

```sql
CREATE TABLE events (
    event_id String,        -- "550e8400-e29b-41d4-a716-446655440000" = 36 bytes
    user_id String,         -- "12345" = 5 bytes (no numeric operations)
    created_at String,      -- "2024-01-15 10:30:00" = 19 bytes
    count String,           -- "42" - can't do math!
    is_active String        -- "true" = 4 bytes
)
```

**Correct: native types**

```sql
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),     -- 16 bytes (vs 36)
    user_id UInt64,                              -- 8 bytes, numeric ops
    created_at DateTime DEFAULT now(),           -- 4 bytes (vs 19)
    count UInt32 DEFAULT 0,                      -- 4 bytes, math works
    is_active Bool DEFAULT true                  -- 1 byte (vs 4)
)
```

**Type Selection Quick Reference:**

| Data | Use | Avoid |

|------|-----|-------|

| Sequential IDs | UInt32/UInt64 | String |

| UUIDs | UUID | String |

| Status/Category | Enum8 or LowCardinality(String) | String |

| Timestamps | DateTime | DateTime64, String |

| Dates only | Date or Date32 | DateTime, String |

| Counts | UInt8/16/32 (smallest that fits) | Int64, String |

| Money | Decimal(P,S) or Int64 (cents) | Float64, String |

| Booleans | Bool or UInt8 | String |

Reference: [https://clickhouse.com/docs/best-practices/select-data-types](https://clickhouse.com/docs/best-practices/select-data-types)

### 1.14 Use Partitioning for Data Lifecycle Management

**Impact: HIGH (DROP PARTITION is instant; DELETE is expensive row-by-row scan)**

Partitioning is **primarily a data management technique, not a query optimization tool**. It excels at:

- **Dropping data**: Remove entire partitions as single metadata operations

- **TTL retention**: Implement time-based retention policies efficiently

- **Tiered storage**: Move old partitions to cold storage

- **Archiving**: Move partitions between tables

**Incorrect: no time alignment for lifecycle**

```sql
-- Cannot efficiently drop old data by time
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY event_type  -- No time alignment
ORDER BY (timestamp);

-- Slow: must scan and delete row by row
DELETE FROM events WHERE timestamp < '2023-01-01';
```

**Correct: time-based for lifecycle**

```sql
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String)
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp)
TTL timestamp + INTERVAL 1 YEAR DELETE;  -- Drops whole partitions

-- Fast: metadata-only operation
ALTER TABLE events DROP PARTITION '202301';

-- Archive to cold storage
ALTER TABLE events_archive ATTACH PARTITION '202301' FROM events;
```

Reference: [https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

---

## 2. Query Optimization

**Impact: CRITICAL**

Query patterns dramatically affect performance. JOIN algorithms, filtering strategies, skipping indices, and materialized views can reduce query time from minutes to milliseconds. Pre-computed aggregations read thousands of rows instead of billions.

### 2.1 Choose the Right JOIN Algorithm

**Impact: CRITICAL (Wrong algorithm causes OOM; right algorithm handles large tables efficiently)**

ClickHouse's default hash join loads the RIGHT table entirely into memory. Choose the right algorithm based on table sizes and constraints.

**Algorithm selection:**

| Algorithm | Best For | Trade-off |

|-----------|----------|-----------|

| `parallel_hash` | Small-to-medium in-memory tables | Default since 24.11; fast, concurrent |

| `hash` | General purpose, all join types | Single-threaded hash table build |

| `direct` | Dictionary lookups (INNER/LEFT only) | Fastest; no hash table construction |

| `full_sorting_merge` | Tables already sorted on join key | Skips sort if pre-ordered; low memory |

| `partial_merge` | Large tables, memory-constrained | Minimized memory; slower execution |

| `grace_hash` | Large datasets, tunable memory | Flexible; disk-spilling capability |

| `auto` | Adaptive algorithm selection | Tries hash first, falls back on memory pressure |

**Example usage:**

```sql
-- Let ClickHouse choose automatically
SET join_algorithm = 'auto';

-- For large-to-large joins where memory is constrained
SET join_algorithm = 'partial_merge';
SELECT * FROM large_a JOIN large_b ON large_b.id = large_a.id;

-- When joining by primary key columns, sort-merge skips sorting step
SET join_algorithm = 'full_sorting_merge';
SELECT * FROM table_a a JOIN table_b b ON b.pk_col = a.pk_col;
```

**Note:** ClickHouse 24.12+ automatically positions smaller tables on the right side. For earlier versions, manually ensure the smaller table is on the RIGHT.

Reference: [https://clickhouse.com/docs/best-practices/minimize-optimize-joins](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

### 2.2 Consider Alternatives to JOINs

**Impact: CRITICAL (Dictionaries and denormalization shift work from query time to insert time)**

Repeated JOINs to dimension tables add overhead. Dictionaries or denormalization shift computational work from query time to insert/pre-processing time.

**Incorrect: JOIN on every query**

```sql
-- JOIN on every query
SELECT o.order_id, c.name, c.email
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01';
```

**Correct - Dictionary Lookup:**

```sql
-- Create dictionary
CREATE DICTIONARY customer_dict (
    id UInt64,
    name String,
    email String
)
PRIMARY KEY id
SOURCE(CLICKHOUSE(TABLE 'customers'))
LAYOUT(HASHED())
LIFETIME(MIN 300 MAX 360);

-- Use dictGet instead of JOIN (uses direct join algorithm - fastest)
SELECT
    order_id,
    dictGet('customer_dict', 'name', customer_id) as customer_name,
    dictGet('customer_dict', 'email', customer_id) as customer_email
FROM orders
WHERE created_at > '2024-01-01';
```

**Correct - Denormalization:**

```sql
-- Denormalized table with materialized view
CREATE MATERIALIZED VIEW orders_enriched_mv TO orders_enriched AS
SELECT
    o.order_id, o.customer_id,
    c.name as customer_name,
    c.email as customer_email,
    o.total, o.created_at
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

**Approach comparison:**

| Approach | Use Case | Performance |

|----------|----------|-------------|

| Dictionary | Frequent lookups to small dimension | Fastest (in-memory) |

| Denormalization | Analytics always need enriched data | Fast (no join at query) |

| IN subquery | Existence filtering | Often faster than JOIN |

| JOIN | Infrequent or complex joins | Acceptable |

**Critical dictionary caveat:** Dictionaries silently deduplicate duplicate keys, retaining only the final value. Only use when source has unique keys.

Reference: [https://clickhouse.com/docs/best-practices/minimize-optimize-joins](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

### 2.3 Filter Tables Before Joining

**Impact: CRITICAL (Joining full tables then filtering wastes resources)**

Joining full tables then filtering wastes resources. Add filtering in `WHERE` or `JOIN ON` clauses. If automatic pushdown fails, restructure as a subquery.

**Incorrect: join then filter**

```sql
-- Joins entire tables, then filters
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01' AND c.country = 'US';
```

**Correct: filter in subqueries before joining**

```sql
-- Filter in subqueries before joining
SELECT o.order_id, c.name, o.total
FROM (
    SELECT order_id, customer_id, total
    FROM orders
    WHERE created_at > '2024-01-01'
) o
JOIN (
    SELECT id, name
    FROM customers
    WHERE country = 'US'
) c ON c.id = o.customer_id;
```

**Even better - aggregate before joining:**

```sql
SELECT c.country, o.total_revenue
FROM (
    SELECT customer_id, sum(total) as total_revenue
    FROM orders
    WHERE created_at > '2024-01-01'
    GROUP BY customer_id
) o
JOIN customers c ON c.id = o.customer_id;
```

Reference: [https://clickhouse.com/docs/best-practices/minimize-optimize-joins](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

### 2.4 Optimize NULL Handling in Outer JOINs

**Impact: MEDIUM (Default values instead of NULL reduces memory overhead)**

Set `join_use_nulls = 0` to use default column values instead of NULL markers, reducing memory overhead compared to Nullable wrappers.

**Example:**

```sql
-- Use default values instead of NULLs for non-matching rows
SET join_use_nulls = 0;

SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
-- Non-matching rows get '' for name instead of NULL
```

**When to use:**

| Setting | Behavior | Use Case |

|---------|----------|----------|

| `join_use_nulls = 0` | Default values (empty string, 0) for non-matches | When you can handle default values |

| `join_use_nulls = 1` (default) | NULL for non-matches | When you need to distinguish "no match" from "matched with default" |

Reference: [https://clickhouse.com/docs/best-practices/minimize-optimize-joins](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

### 2.5 Use ANY JOIN When Only One Match Needed

**Impact: HIGH (Returns first match only; less memory and faster execution)**

Use `ANY` JOINs when you only need a single match rather than all matches. They consume less memory and execute faster.

**Incorrect: returns all matches**

```sql
-- Returns all matching rows, uses more memory
SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
```

**Correct: returns first match only**

```sql
-- Returns only first match per row, faster and less memory
SELECT o.order_id, c.name
FROM orders o
LEFT ANY JOIN customers c ON c.id = o.customer_id;
```

**ANY JOIN types:**

| Type | Behavior |

|------|----------|

| `LEFT ANY JOIN` | At most one match from right table |

| `INNER ANY JOIN` | At most one match, only matching rows |

| `RIGHT ANY JOIN` | At most one match from left table |

Reference: [https://clickhouse.com/docs/best-practices/minimize-optimize-joins](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

### 2.6 Use Data Skipping Indices for Non-ORDER BY Filters

**Impact: HIGH (Up to 60x faster queries by skipping irrelevant granules)**

Queries filtering on columns not in ORDER BY cannot use the primary index and result in full scans. Data skipping indices store metadata about blocks and skip granules that definitely don't match.

**Important:** Skip indices should be considered **after** optimizing data types, primary key selection, and materialized views.

**When to use:**

- High overall cardinality but low cardinality within blocks

- Rare values critical for search (error codes, specific IDs)

- Column correlates with primary key

**When NOT to use:**

- As a first optimization step

- Matching values scattered across many blocks

- Without testing on real data

**Incorrect: filtering on non-ORDER BY column**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64    -- Not in ORDER BY
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Query filters on user_id - scans all matching event_type
SELECT * FROM events
WHERE event_type = 'click' AND user_id = 12345;
```

**Correct: add skipping index**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64,
    INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Or add to existing table
ALTER TABLE events ADD INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4;
ALTER TABLE events MATERIALIZE INDEX idx_user_id;
```

**Index types:**

| Type | Best For | Example Filter |

|------|----------|----------------|

| `bloom_filter` | Equality on high-cardinality | `WHERE user_id = 123` |

| `set(N)` | Low cardinality (N unique values) | `WHERE status IN ('a','b')` |

| `minmax` | Range queries | `WHERE amount > 1000` |

| `ngrambf_v1` | Text search | `WHERE text LIKE '%term%'` |

| `tokenbf_v1` | Token search | `WHERE hasToken(text, 'word')` |

**Validation:**

```sql
EXPLAIN indexes = 1
SELECT * FROM events WHERE user_id = 12345;
-- Look for "Skip" in output showing granules skipped
```

Reference: [https://clickhouse.com/docs/best-practices/use-data-skipping-indices-where-appropriate](https://clickhouse.com/docs/best-practices/use-data-skipping-indices-where-appropriate)

### 2.7 Use Incremental MVs for Real-Time Aggregations

**Impact: HIGH (Read thousands of rows instead of billions; minimal cluster overhead)**

Incremental MVs automatically apply the view's query to new data blocks at insert time. Results are written to a target table and partial results merge over time.

**Incorrect: full aggregation on every query**

```sql
-- Full aggregation on every dashboard load
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    count() as events,
    uniq(user_id) as unique_users
FROM events
WHERE timestamp >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Scans 7 days of data every time (billions of rows)
```

**Correct: incremental MV with pre-aggregation**

```sql
-- Create target table for aggregated data
CREATE TABLE events_hourly (
    event_type LowCardinality(String),
    hour DateTime,
    events AggregateFunction(count),
    unique_users AggregateFunction(uniq, UInt64)
)
ENGINE = AggregatingMergeTree()
ORDER BY (event_type, hour);

-- Create materialized view to populate incrementally
CREATE MATERIALIZED VIEW events_hourly_mv TO events_hourly AS
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    countState() as events,
    uniqState(user_id) as unique_users
FROM events
GROUP BY event_type, hour;

-- Query the pre-aggregated data
SELECT
    event_type, hour,
    countMerge(events) as events,
    uniqMerge(unique_users) as unique_users
FROM events_hourly
WHERE hour >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Reads thousands of rows instead of billions
```

**Key points:**

- Use `-State` functions in MV, `-Merge` functions in query

- Incremental - existing data not automatically included (backfill separately)

- Minimal cluster overhead at insert time

Reference: [https://clickhouse.com/docs/best-practices/use-materialized-views](https://clickhouse.com/docs/best-practices/use-materialized-views)

### 2.8 Use Refreshable MVs for Complex Joins and Batch Workflows

**Impact: HIGH (Sub-millisecond queries with periodic refresh; ideal for complex joins)**

Refreshable MVs execute queries periodically on a schedule. The full query re-executes and overwrites (or appends to) the target table.

**Best for:**

- Sub-millisecond latency where minor staleness is acceptable

- Caching "top N" results or lookup tables

- Complex multi-table joins requiring denormalization

- Batch workflows and DAG dependencies

**Incorrect: expensive join on every request**

```sql
-- Complex join executed on every request
SELECT
    o.order_id, o.total,
    c.name as customer_name,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;
```

**Correct: refreshable MV**

```sql
-- Create refreshable MV that runs every 5 minutes
CREATE MATERIALIZED VIEW orders_denormalized
REFRESH EVERY 5 MINUTE
ENGINE = MergeTree()
ORDER BY (created_at, order_id)
AS SELECT
    o.order_id, o.created_at, o.total,
    c.name as customer_name, c.segment,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;

-- Query the pre-joined data (sub-millisecond)
SELECT * FROM orders_denormalized WHERE segment = 'enterprise';
```

**APPEND vs REPLACE modes:**

| Mode | Behavior | Use Case |

|------|----------|----------|

| `REPLACE` (default) | Overwrites previous contents | Current state, lookup tables |

| `APPEND` | Adds new rows to existing data | Periodic snapshots, historical accumulation |

**Critical warning:** Query should run quickly compared to refresh interval. Don't schedule every 10 seconds if the query takes 10+ seconds.

Reference: [https://clickhouse.com/docs/best-practices/use-materialized-views](https://clickhouse.com/docs/best-practices/use-materialized-views)

---

## 3. Insert Strategy

**Impact: CRITICAL**

Each INSERT creates a data part. Single-row inserts overwhelm the merge process. Proper batching (10K-100K rows), async inserts for high-frequency writes, mutation avoidance, and letting background merges work are essential for stable cluster performance.

### 3.1 Avoid ALTER TABLE DELETE

**Impact: CRITICAL (Use lightweight DELETE, CollapsingMergeTree, or DROP PARTITION instead)**

`ALTER TABLE DELETE` is a mutation that rewrites entire data parts. Use alternatives like lightweight DELETE, CollapsingMergeTree, or DROP PARTITION.

**Incorrect: mutation delete**

```sql
-- Mutation delete for cleanup
ALTER TABLE orders DELETE WHERE status = 'cancelled';

-- Time-based cleanup via mutation (very expensive)
ALTER TABLE sessions DELETE WHERE created_at < now() - INTERVAL 7 DAY;
```

**Correct - CollapsingMergeTree:**

```sql
CREATE TABLE orders (
    order_id UInt64,
    customer_id UInt64,
    total Decimal(10,2),
    sign Int8  -- 1 = active, -1 = deleted
)
ENGINE = CollapsingMergeTree(sign)
ORDER BY order_id;

-- Insert order
INSERT INTO orders VALUES (123, 456, 99.99, 1);

-- "Delete" by inserting with sign = -1
INSERT INTO orders VALUES (123, 456, 99.99, -1);

-- Query collapses +1 and -1 pairs
SELECT order_id, sum(total * sign) as total
FROM orders GROUP BY order_id HAVING sum(sign) > 0;
```

**Correct - Lightweight Deletes (23.3+):**

```sql
-- Marks rows, doesn't rewrite immediately
DELETE FROM orders WHERE status = 'cancelled';
-- Physical deletion happens during normal merges
```

**Correct - DROP PARTITION for Bulk Deletion:**

```sql
-- Instant deletion of old data
ALTER TABLE events DROP PARTITION '202301';

-- Much faster than:
ALTER TABLE events DELETE WHERE toYYYYMM(timestamp) = 202301;
```

**Delete strategy comparison:**

| Method | Speed | When to Use |

|--------|-------|-------------|

| ALTER DELETE | Slow | Rare corrections only |

| CollapsingMergeTree | Fast | Frequent soft deletes |

| Lightweight DELETE | Medium | Occasional deletes |

| DROP PARTITION | Instant | Bulk deletion by partition |

Reference: [https://clickhouse.com/docs/best-practices/avoid-mutations](https://clickhouse.com/docs/best-practices/avoid-mutations)

### 3.2 Avoid ALTER TABLE UPDATE

**Impact: CRITICAL (Mutations rewrite entire parts; use ReplacingMergeTree instead)**

`ALTER TABLE UPDATE` is a mutation - an asynchronous background process that rewrites entire data parts affected by the change. This is extremely expensive for frequent or large-scale operations.

**Why mutations are problematic:**

- **Write amplification:** Rewrite complete parts even for minor changes

- **Disk I/O spike:** Degrades overall cluster performance

- **No rollback:** Cannot be rolled back after submission

- **Inconsistent reads:** SELECT may read mix of mutated and unmutated parts

**Incorrect: mutation for updates**

```sql
-- Rewrites potentially huge amounts of data
ALTER TABLE users UPDATE status = 'inactive'
WHERE last_login < now() - INTERVAL 90 DAY;

-- Frequent row updates via mutation
ALTER TABLE inventory UPDATE quantity = quantity - 1
WHERE product_id = 123;
-- If product exists across 100 parts, rewrites ALL 100 parts
```

**Correct: ReplacingMergeTree**

```sql
-- Table design for updates
CREATE TABLE users (
    user_id UInt64,
    name String,
    status LowCardinality(String),
    updated_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(updated_at)
ORDER BY user_id;

-- "Update" by inserting new version
INSERT INTO users (user_id, name, status)
VALUES (123, 'John', 'inactive');

-- Query with FINAL to get latest version
SELECT * FROM users FINAL WHERE user_id = 123;

-- Or use aggregation
SELECT user_id, argMax(status, updated_at) as status
FROM users GROUP BY user_id;
```

Reference: [https://clickhouse.com/docs/best-practices/avoid-mutations](https://clickhouse.com/docs/best-practices/avoid-mutations)

### 3.3 Avoid OPTIMIZE TABLE FINAL

**Impact: HIGH (Forces expensive merge of all parts; let background merges work)**

`OPTIMIZE TABLE ... FINAL` forces immediate merge of all parts into one part per partition. This is resource-intensive and rarely necessary. ClickHouse already performs smart background merges.

**Note:** `OPTIMIZE FINAL` is not the same as `FINAL`. The `FINAL` modifier in SELECT queries may be necessary for deduplicated results in ReplacingMergeTree and is generally fine to use.

**Incorrect: OPTIMIZE FINAL after inserts**

```sql
-- Running OPTIMIZE FINAL after every batch insert
INSERT INTO events SELECT * FROM staging_events;
OPTIMIZE TABLE events FINAL;  -- Expensive and unnecessary!

-- Scheduled OPTIMIZE FINAL jobs
-- Cron: 0 * * * * clickhouse-client -q "OPTIMIZE TABLE events FINAL"
```

**Correct: let background merges work**

```sql
-- Let background merges handle optimization
INSERT INTO events SELECT * FROM staging_events;
-- Done! ClickHouse merges automatically

-- For ReplacingMergeTree deduplication, use FINAL in queries
SELECT * FROM events FINAL WHERE user_id = 123;
-- Instead of running OPTIMIZE FINAL to deduplicate
```

**Problems with OPTIMIZE FINAL:**

- Rewrites entire partition regardless of need

- Ignores the ~150 GB part size safeguard

- Can cause memory pressure or OOM errors

- Lengthy execution time for large datasets

**When OPTIMIZE FINAL may be acceptable:**

- Finalizing data before table freezing

- Preparing data for export operations

- One-time operations, not regular workflows

**Better alternatives:**

| Need | Alternative |

|------|-------------|

| Deduplicate ReplacingMergeTree | Use `FINAL` modifier in SELECT |

| Reduce part count | Rely on background merges |

Reference: [https://clickhouse.com/docs/best-practices/avoid-optimize-final](https://clickhouse.com/docs/best-practices/avoid-optimize-final)

### 3.4 Batch Inserts Appropriately (10K-100K rows)

**Impact: CRITICAL (Each INSERT creates a part; single-row inserts overwhelm merge process)**

Each INSERT creates a new data part. Single-row or small-batch inserts create thousands of tiny parts, overwhelming the merge process and causing cluster instability.

**Incorrect: single-row or tiny batches**

```python
# Single-row inserts - creates 10,000 parts!
for event in events:
    client.execute("INSERT INTO events VALUES", [event])

# Tiny batches - still too many parts
for batch in chunks(events, 100):  # 100 rows per INSERT
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct: proper batch size**

```python
# Ideal batch size: 10,000-100,000 rows
BATCH_SIZE = 10_000
for batch in chunks(events, BATCH_SIZE):
    client.execute("INSERT INTO events VALUES", batch)
```

**Recommended batch sizes:**

| Threshold | Value |

|-----------|-------|

| Minimum | 1,000 rows |

| Ideal range | 10,000-100,000 rows |

| Insert rate (sync) | ~1 insert per second |

**Validation:**

```sql
-- Monitor part count (>3000 per partition blocks inserts)
SELECT table, count() as parts, sum(rows) as total_rows
FROM system.parts
WHERE active AND database = 'default'
GROUP BY table
ORDER BY parts DESC;
```

Reference: [https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

### 3.5 Use Async Inserts for High-Frequency Small Batches

**Impact: HIGH (Server-side buffering when client batching isn't practical)**

When client-side batching isn't practical, async inserts buffer server-side and create larger parts automatically.

**Incorrect: small batches without async**

```python
# Small batches without async_insert - creates too many parts
for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct: enable async inserts**

```sql
-- Configure server-side for specific users
ALTER USER my_app_user SETTINGS
    async_insert = 1,
    wait_for_async_insert = 1,
    async_insert_max_data_size = 10000000,  -- Flush at 10MB
    async_insert_busy_timeout_ms = 1000;    -- Flush after 1s
```

**Flush conditions: whichever occurs first**

- Buffer reaches `async_insert_max_data_size`

- Time threshold `async_insert_busy_timeout_ms` elapses

- Maximum insert queries accumulate

**Return modes:**

| Setting | Behavior | Use Case |

|---------|----------|----------|

| `wait_for_async_insert=1` | Waits for flush, confirms durability | **Recommended** |

| `wait_for_async_insert=0` | Fire-and-forget, unaware of errors | **Risky** - only if you accept data loss |

Reference: [https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

### 3.6 Use Native Format for Best Insert Performance

**Impact: MEDIUM (Native format is most efficient; JSONEachRow is expensive to parse)**

Data format affects insert performance. Native format is column-oriented with minimal parsing overhead.

**Performance Ranking: fastest to slowest**

| Format | Notes |

|--------|-------|

| **Native** | Most efficient. Column-oriented, minimal parsing. Recommended. |

| **RowBinary** | Efficient row-based alternative |

| **JSONEachRow** | Easier to use but expensive to parse |

**Example:**

```python
# Use Native format for best performance
client.execute("INSERT INTO events VALUES", data, settings={'input_format': 'Native'})
```

Reference: [https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

---

## References

1. [https://clickhouse.com/docs](https://clickhouse.com/docs)
2. [https://github.com/ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)

```

## File: skills\clickhouse-best-practices\metadata.json
```
{
  "version": "0.1.0",
  "organization": "ClickHouse Inc",
  "date": "January 2026",
  "clickhouseVersion": "24.1+",
  "abstract": "Comprehensive best practices for ClickHouse database optimization. Covers schema design, query optimization, table engines, indexing strategies, materialized views, distributed operations, and operational best practices. Each rule includes detailed explanations, SQL examples comparing incorrect vs. correct implementations, and specific impact metrics to guide database design and query optimization.",
  "references": [
    "https://clickhouse.com/docs",
    "https://github.com/ClickHouse/ClickHouse"
  ]
}

```

## File: skills\clickhouse-best-practices\README.md
```
# ClickHouse Best Practices

Agent skill providing comprehensive ClickHouse guidance for schema design, query optimization, and data ingestion.

## Installation

```bash
npx skills add ClickHouse/clickhouse-agent-skills
```

## What's Included

**28 atomic rules** organized by prefix:

| Prefix | Count | Coverage |
|--------|-------|----------|
| `schema-pk-*` | 4 | PRIMARY KEY selection, cardinality ordering |
| `schema-types-*` | 5 | Data types, LowCardinality, Nullable |
| `schema-partition-*` | 4 | Partitioning strategy, lifecycle management |
| `schema-json-*` | 1 | JSON type usage |
| `query-join-*` | 5 | JOIN algorithms, filtering, alternatives |
| `query-index-*` | 1 | Data skipping indices |
| `query-mv-*` | 2 | Incremental and refreshable MVs |
| `insert-batch-*` | 1 | Batch sizing (10K-100K rows) |
| `insert-async-*` | 2 | Async inserts, data formats |
| `insert-mutation-*` | 2 | Mutation avoidance |
| `insert-optimize-*` | 1 | OPTIMIZE FINAL avoidance |

## Trigger Phrases

This skill activates when you:
- "Create a table for..."
- "Optimize this query..."
- "Design a schema for..."
- "Why is this query slow?"
- "How should I insert data into..."
- "Should I use UPDATE or..."

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Quick reference and decision frameworks |
| `AGENTS.md` | Complete rule reference (auto-generated) |
| `rules/*.md` | Individual rule definitions |

## Related Documentation

All rules link to official ClickHouse documentation:
- [ClickHouse Best Practices](https://clickhouse.com/docs/best-practices)

```

## File: skills\clickhouse-best-practices\SKILL.md
```
---
name: clickhouse-best-practices
description: MUST USE when reviewing ClickHouse schemas, queries, or configurations. Contains 28 rules that MUST be checked before providing recommendations. Always read relevant rule files and cite specific rules in responses.
license: Apache-2.0
metadata:
  author: ClickHouse Inc
  version: "0.3.0"
---

# ClickHouse Best Practices

Comprehensive guidance for ClickHouse covering schema design, query optimization, and data ingestion. Contains 28 rules across 3 main categories (schema, query, insert), prioritized by impact.

> **Official docs:** [ClickHouse Best Practices](https://clickhouse.com/docs/best-practices)

## IMPORTANT: How to Apply This Skill

**Before answering ClickHouse questions, follow this priority order:**

1. **Check for applicable rules** in the `rules/` directory
2. **If rules exist:** Apply them and cite them in your response using "Per `rule-name`..."
3. **If no rule exists:** Use the LLM's ClickHouse knowledge or search documentation
4. **If uncertain:** Use web search for current best practices
5. **Always cite your source:** rule name, "general ClickHouse guidance", or URL

**Why rules take priority:** ClickHouse has specific behaviors (columnar storage, sparse indexes, merge tree mechanics) where general database intuition can be misleading. The rules encode validated, ClickHouse-specific guidance.

### For Formal Reviews

When performing a formal review of schemas, queries, or data ingestion:

---

## Review Procedures

### For Schema Reviews (CREATE TABLE, ALTER TABLE)

**Read these rule files in order:**

1. `rules/schema-pk-plan-before-creation.md` - ORDER BY is immutable
2. `rules/schema-pk-cardinality-order.md` - Column ordering in keys
3. `rules/schema-pk-prioritize-filters.md` - Filter column inclusion
4. `rules/schema-types-native-types.md` - Proper type selection
5. `rules/schema-types-minimize-bitwidth.md` - Numeric type sizing
6. `rules/schema-types-lowcardinality.md` - LowCardinality usage
7. `rules/schema-types-avoid-nullable.md` - Nullable vs DEFAULT
8. `rules/schema-partition-low-cardinality.md` - Partition count limits
9. `rules/schema-partition-lifecycle.md` - Partitioning purpose

**Check for:**
- [ ] PRIMARY KEY / ORDER BY column order (low-to-high cardinality)
- [ ] Data types match actual data ranges
- [ ] LowCardinality applied to appropriate string columns
- [ ] Partition key cardinality bounded (100-1,000 values)
- [ ] ReplacingMergeTree has version column if used

### For Query Reviews (SELECT, JOIN, aggregations)

**Read these rule files:**

1. `rules/query-join-choose-algorithm.md` - Algorithm selection
2. `rules/query-join-filter-before.md` - Pre-join filtering
3. `rules/query-join-use-any.md` - ANY vs regular JOIN
4. `rules/query-index-skipping-indices.md` - Secondary index usage
5. `rules/schema-pk-filter-on-orderby.md` - Filter alignment with ORDER BY

**Check for:**
- [ ] Filters use ORDER BY prefix columns
- [ ] JOINs filter tables before joining (not after)
- [ ] Correct JOIN algorithm for table sizes
- [ ] Skipping indices for non-ORDER BY filter columns

### For Insert Strategy Reviews (data ingestion, updates, deletes)

**Read these rule files:**

1. `rules/insert-batch-size.md` - Batch sizing requirements
2. `rules/insert-mutation-avoid-update.md` - UPDATE alternatives
3. `rules/insert-mutation-avoid-delete.md` - DELETE alternatives
4. `rules/insert-async-small-batches.md` - Async insert usage
5. `rules/insert-optimize-avoid-final.md` - OPTIMIZE TABLE risks

**Check for:**
- [ ] Batch size 10K-100K rows per INSERT
- [ ] No ALTER TABLE UPDATE for frequent changes
- [ ] ReplacingMergeTree or CollapsingMergeTree for update patterns
- [ ] Async inserts enabled for high-frequency small batches

---

## Output Format

Structure your response as follows:

```
## Rules Checked
- `rule-name-1` - Compliant / Violation found
- `rule-name-2` - Compliant / Violation found
...

## Findings

### Violations
- **`rule-name`**: Description of the issue
  - Current: [what the code does]
  - Required: [what it should do]
  - Fix: [specific correction]

### Compliant
- `rule-name`: Brief note on why it's correct

## Recommendations
[Prioritized list of changes, citing rules]
```

---

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rule Count |
|----------|----------|--------|--------|------------|
| 1 | Primary Key Selection | CRITICAL | `schema-pk-` | 4 |
| 2 | Data Type Selection | CRITICAL | `schema-types-` | 5 |
| 3 | JOIN Optimization | CRITICAL | `query-join-` | 5 |
| 4 | Insert Batching | CRITICAL | `insert-batch-` | 1 |
| 5 | Mutation Avoidance | CRITICAL | `insert-mutation-` | 2 |
| 6 | Partitioning Strategy | HIGH | `schema-partition-` | 4 |
| 7 | Skipping Indices | HIGH | `query-index-` | 1 |
| 8 | Materialized Views | HIGH | `query-mv-` | 2 |
| 9 | Async Inserts | HIGH | `insert-async-` | 2 |
| 10 | OPTIMIZE Avoidance | HIGH | `insert-optimize-` | 1 |
| 11 | JSON Usage | MEDIUM | `schema-json-` | 1 |

---

## Quick Reference

### Schema Design - Primary Key (CRITICAL)

- `schema-pk-plan-before-creation` - Plan ORDER BY before table creation (immutable)
- `schema-pk-cardinality-order` - Order columns low-to-high cardinality
- `schema-pk-prioritize-filters` - Include frequently filtered columns
- `schema-pk-filter-on-orderby` - Query filters must use ORDER BY prefix

### Schema Design - Data Types (CRITICAL)

- `schema-types-native-types` - Use native types, not String for everything
- `schema-types-minimize-bitwidth` - Use smallest numeric type that fits
- `schema-types-lowcardinality` - LowCardinality for <10K unique strings
- `schema-types-enum` - Enum for finite value sets with validation
- `schema-types-avoid-nullable` - Avoid Nullable; use DEFAULT instead

### Schema Design - Partitioning (HIGH)

- `schema-partition-low-cardinality` - Keep partition count 100-1,000
- `schema-partition-lifecycle` - Use partitioning for data lifecycle, not queries
- `schema-partition-query-tradeoffs` - Understand partition pruning trade-offs
- `schema-partition-start-without` - Consider starting without partitioning

### Schema Design - JSON (MEDIUM)

- `schema-json-when-to-use` - JSON for dynamic schemas; typed columns for known

### Query Optimization - JOINs (CRITICAL)

- `query-join-choose-algorithm` - Select algorithm based on table sizes
- `query-join-use-any` - ANY JOIN when only one match needed
- `query-join-filter-before` - Filter tables before joining
- `query-join-consider-alternatives` - Dictionaries/denormalization vs JOIN
- `query-join-null-handling` - join_use_nulls=0 for default values

### Query Optimization - Indices (HIGH)

- `query-index-skipping-indices` - Skipping indices for non-ORDER BY filters

### Query Optimization - Materialized Views (HIGH)

- `query-mv-incremental` - Incremental MVs for real-time aggregations
- `query-mv-refreshable` - Refreshable MVs for complex joins

### Insert Strategy - Batching (CRITICAL)

- `insert-batch-size` - Batch 10K-100K rows per INSERT

### Insert Strategy - Async (HIGH)

- `insert-async-small-batches` - Async inserts for high-frequency small batches
- `insert-format-native` - Native format for best performance

### Insert Strategy - Mutations (CRITICAL)

- `insert-mutation-avoid-update` - ReplacingMergeTree instead of ALTER UPDATE
- `insert-mutation-avoid-delete` - Lightweight DELETE or DROP PARTITION

### Insert Strategy - Optimization (HIGH)

- `insert-optimize-avoid-final` - Let background merges work

---

## When to Apply

This skill activates when you encounter:

- `CREATE TABLE` statements
- `ALTER TABLE` modifications
- `ORDER BY` or `PRIMARY KEY` discussions
- Data type selection questions
- Slow query troubleshooting
- JOIN optimization requests
- Data ingestion pipeline design
- Update/delete strategy questions
- ReplacingMergeTree or other specialized engine usage
- Partitioning strategy decisions

---

## Rule File Structure

Each rule file in `rules/` contains:

- **YAML frontmatter**: title, impact level, tags
- **Brief explanation**: Why this rule matters
- **Incorrect example**: Anti-pattern with explanation
- **Correct example**: Best practice with explanation
- **Additional context**: Trade-offs, when to apply, references

---

## Full Compiled Document

For the complete guide with all rules expanded inline: `AGENTS.md`

Use `AGENTS.md` when you need to check multiple rules quickly without reading individual files.

```

## File: skills\clickhouse-best-practices\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-043028-skills-clickhouse-best-practices
name: Clickhouse-Best-Practices
path: ecosystem/skills/repo-fetched-agent-skills-043028/skills/clickhouse-best-practices
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Clickhouse-Best-Practices
Storage area for 'clickhouse-best-practices' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\clickhouse-best-practices\rules\insert_async_small_batches.md
```
---
title: Use Async Inserts for High-Frequency Small Batches
impact: HIGH
impactDescription: "Server-side buffering when client batching isn't practical"
tags: [insert, async, buffering, small-batches]
---

## Use Async Inserts for High-Frequency Small Batches

**Impact: HIGH**

When client-side batching isn't practical, async inserts buffer server-side and create larger parts automatically.

**Incorrect (small batches without async):**

```python
# Small batches without async_insert - creates too many parts
for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct (enable async inserts):**

```python
# Enable async_insert with safe defaults
client.execute("SET async_insert = 1")
client.execute("SET wait_for_async_insert = 1")  # Confirms durability

for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
# Server buffers and creates larger parts automatically
```

```sql
-- Configure server-side for specific users
ALTER USER my_app_user SETTINGS
    async_insert = 1,
    wait_for_async_insert = 1,
    async_insert_max_data_size = 10000000,  -- Flush at 10MB
    async_insert_busy_timeout_ms = 1000;    -- Flush after 1s
```

**Flush conditions (whichever occurs first):**
- Buffer reaches `async_insert_max_data_size`
- Time threshold `async_insert_busy_timeout_ms` elapses
- Maximum insert queries accumulate

**Return modes:**

| Setting | Behavior | Use Case |
|---------|----------|----------|
| `wait_for_async_insert=1` | Waits for flush, confirms durability | **Recommended** |
| `wait_for_async_insert=0` | Fire-and-forget, unaware of errors | **Risky** - only if you accept data loss |

Reference: [Selecting an Insert Strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

```

## File: skills\clickhouse-best-practices\rules\insert_batch_size.md
```
---
title: Batch Inserts Appropriately (10K-100K rows)
impact: CRITICAL
impactDescription: "Each INSERT creates a part; single-row inserts overwhelm merge process"
tags: [insert, batching, parts, performance]
---

## Batch Inserts Appropriately (10K-100K rows)

**Impact: CRITICAL**

Each INSERT creates a new data part. Single-row or small-batch inserts create thousands of tiny parts, overwhelming the merge process and causing cluster instability.

**Incorrect (single-row or tiny batches):**

```python
# Single-row inserts - creates 10,000 parts!
for event in events:
    client.execute("INSERT INTO events VALUES", [event])

# Tiny batches - still too many parts
for batch in chunks(events, 100):  # 100 rows per INSERT
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct (proper batch size):**

```python
# Ideal batch size: 10,000-100,000 rows
BATCH_SIZE = 10_000
for batch in chunks(events, BATCH_SIZE):
    client.execute("INSERT INTO events VALUES", batch)
```

**Recommended batch sizes:**

| Threshold | Value |
|-----------|-------|
| Minimum | 1,000 rows |
| Ideal range | 10,000-100,000 rows |
| Insert rate (sync) | ~1 insert per second |

**Validation:**

```sql
-- Monitor part count (>3000 per partition blocks inserts)
SELECT table, count() as parts, sum(rows) as total_rows
FROM system.parts
WHERE active AND database = 'default'
GROUP BY table
ORDER BY parts DESC;
```

Reference: [Selecting an Insert Strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

```

## File: skills\clickhouse-best-practices\rules\insert_format_native.md
```
---
title: Use Native Format for Best Insert Performance
impact: MEDIUM
impactDescription: "Native format is most efficient; JSONEachRow is expensive to parse"
tags: [insert, format, Native, performance]
---

## Use Native Format for Best Insert Performance

**Impact: MEDIUM**

Data format affects insert performance. Native format is column-oriented with minimal parsing overhead.

**Performance Ranking (fastest to slowest):**

| Format | Notes |
|--------|-------|
| **Native** | Most efficient. Column-oriented, minimal parsing. Recommended. |
| **RowBinary** | Efficient row-based alternative |
| **JSONEachRow** | Easier to use but expensive to parse |

**Example:**

```python
# Use Native format for best performance
client.execute("INSERT INTO events VALUES", data, settings={'input_format': 'Native'})
```

Reference: [Selecting an Insert Strategy](https://clickhouse.com/docs/best-practices/selecting-an-insert-strategy)

```

## File: skills\clickhouse-best-practices\rules\insert_mutation_avoid_delete.md
```
---
title: Avoid ALTER TABLE DELETE
impact: CRITICAL
impactDescription: "Use lightweight DELETE, CollapsingMergeTree, or DROP PARTITION instead"
tags: [insert, mutation, DELETE, CollapsingMergeTree]
---

## Avoid ALTER TABLE DELETE

**Impact: CRITICAL**

`ALTER TABLE DELETE` is a mutation that rewrites entire data parts. Use alternatives like lightweight DELETE, CollapsingMergeTree, or DROP PARTITION.

**Incorrect (mutation delete):**

```sql
-- Mutation delete for cleanup
ALTER TABLE orders DELETE WHERE status = 'cancelled';

-- Time-based cleanup via mutation (very expensive)
ALTER TABLE sessions DELETE WHERE created_at < now() - INTERVAL 7 DAY;
```

**Correct - CollapsingMergeTree:**

```sql
CREATE TABLE orders (
    order_id UInt64,
    customer_id UInt64,
    total Decimal(10,2),
    sign Int8  -- 1 = active, -1 = deleted
)
ENGINE = CollapsingMergeTree(sign)
ORDER BY order_id;

-- Insert order
INSERT INTO orders VALUES (123, 456, 99.99, 1);

-- "Delete" by inserting with sign = -1
INSERT INTO orders VALUES (123, 456, 99.99, -1);

-- Query collapses +1 and -1 pairs
SELECT order_id, sum(total * sign) as total
FROM orders GROUP BY order_id HAVING sum(sign) > 0;
```

**Correct - Lightweight Deletes (23.3+):**

```sql
-- Marks rows, doesn't rewrite immediately
DELETE FROM orders WHERE status = 'cancelled';
-- Physical deletion happens during normal merges
```

**Correct - DROP PARTITION for Bulk Deletion:**

```sql
-- Instant deletion of old data
ALTER TABLE events DROP PARTITION '202301';

-- Much faster than:
ALTER TABLE events DELETE WHERE toYYYYMM(timestamp) = 202301;
```

**Delete strategy comparison:**

| Method | Speed | When to Use |
|--------|-------|-------------|
| ALTER DELETE | Slow | Rare corrections only |
| CollapsingMergeTree | Fast | Frequent soft deletes |
| Lightweight DELETE | Medium | Occasional deletes |
| DROP PARTITION | Instant | Bulk deletion by partition |

Reference: [Avoid Mutations](https://clickhouse.com/docs/best-practices/avoid-mutations)

```

## File: skills\clickhouse-best-practices\rules\insert_mutation_avoid_update.md
```
---
title: Avoid ALTER TABLE UPDATE
impact: CRITICAL
impactDescription: "Mutations rewrite entire parts; use ReplacingMergeTree instead"
tags: [insert, mutation, UPDATE, ReplacingMergeTree]
---

## Avoid ALTER TABLE UPDATE

**Impact: CRITICAL**

`ALTER TABLE UPDATE` is a mutation - an asynchronous background process that rewrites entire data parts affected by the change. This is extremely expensive for frequent or large-scale operations.

**Why mutations are problematic:**
- **Write amplification:** Rewrite complete parts even for minor changes
- **Disk I/O spike:** Degrades overall cluster performance
- **No rollback:** Cannot be rolled back after submission
- **Inconsistent reads:** SELECT may read mix of mutated and unmutated parts

**Incorrect (mutation for updates):**

```sql
-- Rewrites potentially huge amounts of data
ALTER TABLE users UPDATE status = 'inactive'
WHERE last_login < now() - INTERVAL 90 DAY;

-- Frequent row updates via mutation
ALTER TABLE inventory UPDATE quantity = quantity - 1
WHERE product_id = 123;
-- If product exists across 100 parts, rewrites ALL 100 parts
```

**Correct (ReplacingMergeTree):**

```sql
-- Table design for updates
CREATE TABLE users (
    user_id UInt64,
    name String,
    status LowCardinality(String),
    updated_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(updated_at)
ORDER BY user_id;

-- "Update" by inserting new version
INSERT INTO users (user_id, name, status)
VALUES (123, 'John', 'inactive');

-- Query with FINAL to get latest version
SELECT * FROM users FINAL WHERE user_id = 123;

-- Or use aggregation
SELECT user_id, argMax(status, updated_at) as status
FROM users GROUP BY user_id;
```

Reference: [Avoid Mutations](https://clickhouse.com/docs/best-practices/avoid-mutations)

```

## File: skills\clickhouse-best-practices\rules\insert_optimize_avoid_final.md
```
---
title: Avoid OPTIMIZE TABLE FINAL
impact: HIGH
impactDescription: "Forces expensive merge of all parts; let background merges work"
tags: [insert, OPTIMIZE, merge, performance]
---

## Avoid OPTIMIZE TABLE FINAL

**Impact: HIGH**

`OPTIMIZE TABLE ... FINAL` forces immediate merge of all parts into one part per partition. This is resource-intensive and rarely necessary. ClickHouse already performs smart background merges.

**Note:** `OPTIMIZE FINAL` is not the same as `FINAL`. The `FINAL` modifier in SELECT queries may be necessary for deduplicated results in ReplacingMergeTree and is generally fine to use.

**Incorrect (OPTIMIZE FINAL after inserts):**

```sql
-- Running OPTIMIZE FINAL after every batch insert
INSERT INTO events SELECT * FROM staging_events;
OPTIMIZE TABLE events FINAL;  -- Expensive and unnecessary!

-- Scheduled OPTIMIZE FINAL jobs
-- Cron: 0 * * * * clickhouse-client -q "OPTIMIZE TABLE events FINAL"
```

**Correct (let background merges work):**

```sql
-- Let background merges handle optimization
INSERT INTO events SELECT * FROM staging_events;
-- Done! ClickHouse merges automatically

-- For ReplacingMergeTree deduplication, use FINAL in queries
SELECT * FROM events FINAL WHERE user_id = 123;
-- Instead of running OPTIMIZE FINAL to deduplicate
```

**Problems with OPTIMIZE FINAL:**
- Rewrites entire partition regardless of need
- Ignores the ~150 GB part size safeguard
- Can cause memory pressure or OOM errors
- Lengthy execution time for large datasets

**When OPTIMIZE FINAL may be acceptable:**
- Finalizing data before table freezing
- Preparing data for export operations
- One-time operations, not regular workflows

**Better alternatives:**

| Need | Alternative |
|------|-------------|
| Deduplicate ReplacingMergeTree | Use `FINAL` modifier in SELECT |
| Reduce part count | Rely on background merges |

Reference: [Avoid OPTIMIZE FINAL](https://clickhouse.com/docs/best-practices/avoid-optimize-final)

```

## File: skills\clickhouse-best-practices\rules\query_index_skipping_indices.md
```
---
title: Use Data Skipping Indices for Non-ORDER BY Filters
impact: HIGH
impactDescription: "Up to 60x faster queries by skipping irrelevant granules"
tags: [query, index, skipping, bloom_filter]
---

## Use Data Skipping Indices for Non-ORDER BY Filters

**Impact: HIGH**

Queries filtering on columns not in ORDER BY cannot use the primary index and result in full scans. Data skipping indices store metadata about blocks and skip granules that definitely don't match.

**Important:** Skip indices should be considered **after** optimizing data types, primary key selection, and materialized views.

**When to use:**
- High overall cardinality but low cardinality within blocks
- Rare values critical for search (error codes, specific IDs)
- Column correlates with primary key

**When NOT to use:**
- As a first optimization step
- Matching values scattered across many blocks
- Without testing on real data

**Incorrect (filtering on non-ORDER BY column):**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64    -- Not in ORDER BY
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Query filters on user_id - scans all matching event_type
SELECT * FROM events
WHERE event_type = 'click' AND user_id = 12345;
```

**Correct (add skipping index):**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64,
    INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Or add to existing table
ALTER TABLE events ADD INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4;
ALTER TABLE events MATERIALIZE INDEX idx_user_id;
```

**Index types:**

| Type | Best For | Example Filter |
|------|----------|----------------|
| `bloom_filter` | Equality on high-cardinality | `WHERE user_id = 123` |
| `set(N)` | Low cardinality (N unique values) | `WHERE status IN ('a','b')` |
| `minmax` | Range queries | `WHERE amount > 1000` |
| `ngrambf_v1` | Text search | `WHERE text LIKE '%term%'` |
| `tokenbf_v1` | Token search | `WHERE hasToken(text, 'word')` |

**Validation:**

```sql
EXPLAIN indexes = 1
SELECT * FROM events WHERE user_id = 12345;
-- Look for "Skip" in output showing granules skipped
```

Reference: [Use Data Skipping Indices Where Appropriate](https://clickhouse.com/docs/best-practices/use-data-skipping-indices-where-appropriate)

```

## File: skills\clickhouse-best-practices\rules\query_join_choose_algorithm.md
```
---
title: Choose the Right JOIN Algorithm
impact: CRITICAL
impactDescription: "Wrong algorithm causes OOM; right algorithm handles large tables efficiently"
tags: [query, JOIN, algorithm, memory]
---

## Choose the Right JOIN Algorithm

**Impact: CRITICAL**

ClickHouse's default hash join loads the RIGHT table entirely into memory. Choose the right algorithm based on table sizes and constraints.

**Algorithm selection:**

| Algorithm | Best For | Trade-off |
|-----------|----------|-----------|
| `parallel_hash` | Small-to-medium in-memory tables | Default since 24.11; fast, concurrent |
| `hash` | General purpose, all join types | Single-threaded hash table build |
| `direct` | Dictionary lookups (INNER/LEFT only) | Fastest; no hash table construction |
| `full_sorting_merge` | Tables already sorted on join key | Skips sort if pre-ordered; low memory |
| `partial_merge` | Large tables, memory-constrained | Minimized memory; slower execution |
| `grace_hash` | Large datasets, tunable memory | Flexible; disk-spilling capability |
| `auto` | Adaptive algorithm selection | Tries hash first, falls back on memory pressure |

**Example usage:**

```sql
-- Let ClickHouse choose automatically
SET join_algorithm = 'auto';

-- For large-to-large joins where memory is constrained
SET join_algorithm = 'partial_merge';
SELECT * FROM large_a JOIN large_b ON large_b.id = large_a.id;

-- When joining by primary key columns, sort-merge skips sorting step
SET join_algorithm = 'full_sorting_merge';
SELECT * FROM table_a a JOIN table_b b ON b.pk_col = a.pk_col;
```

**Note:** ClickHouse 24.12+ automatically positions smaller tables on the right side. For earlier versions, manually ensure the smaller table is on the RIGHT.

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

```

## File: skills\clickhouse-best-practices\rules\query_join_consider_alternatives.md
```
---
title: Consider Alternatives to JOINs
impact: CRITICAL
impactDescription: "Dictionaries and denormalization shift work from query time to insert time"
tags: [query, JOIN, dictionary, denormalization]
---

## Consider Alternatives to JOINs

**Impact: CRITICAL**

Repeated JOINs to dimension tables add overhead. Dictionaries or denormalization shift computational work from query time to insert/pre-processing time.

**Incorrect (JOIN on every query):**

```sql
-- JOIN on every query
SELECT o.order_id, c.name, c.email
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01';
```

**Correct - Dictionary Lookup:**

```sql
-- Create dictionary
CREATE DICTIONARY customer_dict (
    id UInt64,
    name String,
    email String
)
PRIMARY KEY id
SOURCE(CLICKHOUSE(TABLE 'customers'))
LAYOUT(HASHED())
LIFETIME(MIN 300 MAX 360);

-- Use dictGet instead of JOIN (uses direct join algorithm - fastest)
SELECT
    order_id,
    dictGet('customer_dict', 'name', customer_id) as customer_name,
    dictGet('customer_dict', 'email', customer_id) as customer_email
FROM orders
WHERE created_at > '2024-01-01';
```

**Correct - Denormalization:**

```sql
-- Denormalized table with materialized view
CREATE MATERIALIZED VIEW orders_enriched_mv TO orders_enriched AS
SELECT
    o.order_id, o.customer_id,
    c.name as customer_name,
    c.email as customer_email,
    o.total, o.created_at
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

**Approach comparison:**

| Approach | Use Case | Performance |
|----------|----------|-------------|
| Dictionary | Frequent lookups to small dimension | Fastest (in-memory) |
| Denormalization | Analytics always need enriched data | Fast (no join at query) |
| IN subquery | Existence filtering | Often faster than JOIN |
| JOIN | Infrequent or complex joins | Acceptable |

**Critical dictionary caveat:** Dictionaries silently deduplicate duplicate keys, retaining only the final value. Only use when source has unique keys.

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

```

## File: skills\clickhouse-best-practices\rules\query_join_filter_before.md
```
---
title: Filter Tables Before Joining
impact: CRITICAL
impactDescription: "Joining full tables then filtering wastes resources"
tags: [query, JOIN, filtering, subquery]
---

## Filter Tables Before Joining

**Impact: CRITICAL**

Joining full tables then filtering wastes resources. Add filtering in `WHERE` or `JOIN ON` clauses. If automatic pushdown fails, restructure as a subquery.

**Incorrect (join then filter):**

```sql
-- Joins entire tables, then filters
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01' AND c.country = 'US';
```

**Correct (filter in subqueries before joining):**

```sql
-- Filter in subqueries before joining
SELECT o.order_id, c.name, o.total
FROM (
    SELECT order_id, customer_id, total
    FROM orders
    WHERE created_at > '2024-01-01'
) o
JOIN (
    SELECT id, name
    FROM customers
    WHERE country = 'US'
) c ON c.id = o.customer_id;
```

**Even better - aggregate before joining:**

```sql
SELECT c.country, o.total_revenue
FROM (
    SELECT customer_id, sum(total) as total_revenue
    FROM orders
    WHERE created_at > '2024-01-01'
    GROUP BY customer_id
) o
JOIN customers c ON c.id = o.customer_id;
```

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

```

## File: skills\clickhouse-best-practices\rules\query_join_null_handling.md
```
---
title: Optimize NULL Handling in Outer JOINs
impact: MEDIUM
impactDescription: "Default values instead of NULL reduces memory overhead"
tags: [query, JOIN, NULL, memory]
---

## Optimize NULL Handling in Outer JOINs

**Impact: MEDIUM**

Set `join_use_nulls = 0` to use default column values instead of NULL markers, reducing memory overhead compared to Nullable wrappers.

**Example:**

```sql
-- Use default values instead of NULLs for non-matching rows
SET join_use_nulls = 0;

SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
-- Non-matching rows get '' for name instead of NULL
```

**When to use:**

| Setting | Behavior | Use Case |
|---------|----------|----------|
| `join_use_nulls = 0` | Default values (empty string, 0) for non-matches | When you can handle default values |
| `join_use_nulls = 1` (default) | NULL for non-matches | When you need to distinguish "no match" from "matched with default" |

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

```

## File: skills\clickhouse-best-practices\rules\query_join_use_any.md
```
---
title: Use ANY JOIN When Only One Match Needed
impact: HIGH
impactDescription: "Returns first match only; less memory and faster execution"
tags: [query, JOIN, ANY, performance]
---

## Use ANY JOIN When Only One Match Needed

**Impact: HIGH**

Use `ANY` JOINs when you only need a single match rather than all matches. They consume less memory and execute faster.

**Incorrect (returns all matches):**

```sql
-- Returns all matching rows, uses more memory
SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
```

**Correct (returns first match only):**

```sql
-- Returns only first match per row, faster and less memory
SELECT o.order_id, c.name
FROM orders o
LEFT ANY JOIN customers c ON c.id = o.customer_id;
```

**ANY JOIN types:**

| Type | Behavior |
|------|----------|
| `LEFT ANY JOIN` | At most one match from right table |
| `INNER ANY JOIN` | At most one match, only matching rows |
| `RIGHT ANY JOIN` | At most one match from left table |

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/docs/best-practices/minimize-optimize-joins)

```

## File: skills\clickhouse-best-practices\rules\query_mv_incremental.md
```
---
title: Use Incremental MVs for Real-Time Aggregations
impact: HIGH
impactDescription: "Read thousands of rows instead of billions; minimal cluster overhead"
tags: [query, materialized-view, aggregation, real-time]
---

## Use Incremental MVs for Real-Time Aggregations

**Impact: HIGH**

Incremental MVs automatically apply the view's query to new data blocks at insert time. Results are written to a target table and partial results merge over time.

**Incorrect (full aggregation on every query):**

```sql
-- Full aggregation on every dashboard load
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    count() as events,
    uniq(user_id) as unique_users
FROM events
WHERE timestamp >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Scans 7 days of data every time (billions of rows)
```

**Correct (incremental MV with pre-aggregation):**

```sql
-- Create target table for aggregated data
CREATE TABLE events_hourly (
    event_type LowCardinality(String),
    hour DateTime,
    events AggregateFunction(count),
    unique_users AggregateFunction(uniq, UInt64)
)
ENGINE = AggregatingMergeTree()
ORDER BY (event_type, hour);

-- Create materialized view to populate incrementally
CREATE MATERIALIZED VIEW events_hourly_mv TO events_hourly AS
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    countState() as events,
    uniqState(user_id) as unique_users
FROM events
GROUP BY event_type, hour;

-- Query the pre-aggregated data
SELECT
    event_type, hour,
    countMerge(events) as events,
    uniqMerge(unique_users) as unique_users
FROM events_hourly
WHERE hour >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Reads thousands of rows instead of billions
```

**Key points:**
- Use `-State` functions in MV, `-Merge` functions in query
- Incremental - existing data not automatically included (backfill separately)
- Minimal cluster overhead at insert time

Reference: [Use Materialized Views](https://clickhouse.com/docs/best-practices/use-materialized-views)

```

## File: skills\clickhouse-best-practices\rules\query_mv_refreshable.md
```
---
title: Use Refreshable MVs for Complex Joins and Batch Workflows
impact: HIGH
impactDescription: "Sub-millisecond queries with periodic refresh; ideal for complex joins"
tags: [query, materialized-view, refresh, batch]
---

## Use Refreshable MVs for Complex Joins and Batch Workflows

**Impact: HIGH**

Refreshable MVs execute queries periodically on a schedule. The full query re-executes and overwrites (or appends to) the target table.

**Best for:**
- Sub-millisecond latency where minor staleness is acceptable
- Caching "top N" results or lookup tables
- Complex multi-table joins requiring denormalization
- Batch workflows and DAG dependencies

**Incorrect (expensive join on every request):**

```sql
-- Complex join executed on every request
SELECT
    o.order_id, o.total,
    c.name as customer_name,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;
```

**Correct (refreshable MV):**

```sql
-- Create refreshable MV that runs every 5 minutes
CREATE MATERIALIZED VIEW orders_denormalized
REFRESH EVERY 5 MINUTE
ENGINE = MergeTree()
ORDER BY (created_at, order_id)
AS SELECT
    o.order_id, o.created_at, o.total,
    c.name as customer_name, c.segment,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;

-- Query the pre-joined data (sub-millisecond)
SELECT * FROM orders_denormalized WHERE segment = 'enterprise';
```

**APPEND vs REPLACE modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| `REPLACE` (default) | Overwrites previous contents | Current state, lookup tables |
| `APPEND` | Adds new rows to existing data | Periodic snapshots, historical accumulation |

**Critical warning:** Query should run quickly compared to refresh interval. Don't schedule every 10 seconds if the query takes 10+ seconds.

Reference: [Use Materialized Views](https://clickhouse.com/docs/best-practices/use-materialized-views)

```

## File: skills\clickhouse-best-practices\rules\schema_json_when_to_use.md
```
---
title: Use JSON Type for Dynamic Schemas
impact: MEDIUM
impactDescription: "Field-level querying for semi-structured data; use typed columns for known schemas"
tags: [schema, JSON, semi-structured, flexibility]
---

## Use JSON Type for Dynamic Schemas

**Impact: MEDIUM**

ClickHouse's JSON type splits JSON objects into separate sub-columns, enabling field-level query optimization. Use it for truly dynamic data, not everything.

**Incorrect (schema bloat or opaque String):**

```sql
-- BAD: Hundreds of nullable columns for event properties
CREATE TABLE events (
    event_id UUID,
    prop_page_url Nullable(String),
    prop_button_id Nullable(String),
    -- ... 100 more nullable columns
)

-- BAD: JSON as String when you need field queries
CREATE TABLE events (
    event_id UUID,
    properties String  -- No field-level optimization
)
```

**Correct (JSON for dynamic, typed for known):**

```sql
-- Use JSON type for dynamic properties
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    event_type LowCardinality(String),
    timestamp DateTime DEFAULT now(),
    properties JSON  -- Flexible schema with type inference
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Query JSON paths directly
SELECT
    event_type,
    properties.url as page_url,
    properties.amount as purchase_amount
FROM events
WHERE event_type = 'page_view' AND properties.url = '/home';
```

**When to use JSON:**

| Scenario | Use JSON? |
|----------|-----------|
| Data structure varies unpredictably | Yes |
| Field types/schemas change over time | Yes |
| Need field-level querying | Yes |
| Fixed, known schema | No (use typed columns) |
| JSON as opaque blob (no field queries) | No (use String) |

**Optimization: specify types for known paths:**

```sql
CREATE TABLE events (
    properties JSON(
        url String,
        amount Float64,
        product_id UInt64
    )
)
```

Reference: [Use JSON Where Appropriate](https://clickhouse.com/docs/best-practices/use-json-where-appropriate)

```

## File: skills\clickhouse-best-practices\rules\schema_partition_lifecycle.md
```
---
title: Use Partitioning for Data Lifecycle Management
impact: HIGH
impactDescription: "DROP PARTITION is instant; DELETE is expensive row-by-row scan"
tags: [schema, partitioning, TTL, data-management]
---

## Use Partitioning for Data Lifecycle Management

**Impact: HIGH**

Partitioning is **primarily a data management technique, not a query optimization tool**. It excels at:
- **Dropping data**: Remove entire partitions as single metadata operations
- **TTL retention**: Implement time-based retention policies efficiently
- **Tiered storage**: Move old partitions to cold storage
- **Archiving**: Move partitions between tables

**Incorrect (no time alignment for lifecycle):**

```sql
-- Cannot efficiently drop old data by time
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY event_type  -- No time alignment
ORDER BY (timestamp);

-- Slow: must scan and delete row by row
DELETE FROM events WHERE timestamp < '2023-01-01';
```

**Correct (time-based for lifecycle):**

```sql
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String)
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp)
TTL timestamp + INTERVAL 1 YEAR DELETE;  -- Drops whole partitions

-- Fast: metadata-only operation
ALTER TABLE events DROP PARTITION '202301';

-- Archive to cold storage
ALTER TABLE events_archive ATTACH PARTITION '202301' FROM events;
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

```

## File: skills\clickhouse-best-practices\rules\schema_partition_low_cardinality.md
```
---
title: Keep Partition Cardinality Low (100-1,000 Values)
impact: HIGH
impactDescription: "Too many partitions cause part explosion and 'too many parts' errors"
tags: [schema, partitioning, parts]
---

## Keep Partition Cardinality Low (100-1,000 Values)

**Impact: HIGH**

Too many distinct partition values create excessive data parts, eventually triggering "too many parts" errors. ClickHouse enforces limits via `max_parts_in_total` and `parts_to_throw_insert` settings.

**Incorrect (high cardinality partitioning):**

```sql
-- High cardinality = too many partitions
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY user_id  -- Millions of partitions!
ORDER BY (timestamp);

-- Daily partitions can grow unbounded over years
CREATE TABLE logs (...)
ENGINE = MergeTree()
PARTITION BY toDate(timestamp)  -- 3650 partitions over 10 years
ORDER BY (service, timestamp);
```

**Correct (bounded cardinality):**

```sql
-- Monthly partitions = 12 per year, bounded cardinality
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp);
```

**Validation:**

```sql
-- Check partition count and health
SELECT
    partition,
    count() as parts,
    sum(rows) as rows,
    formatReadableSize(sum(bytes_on_disk)) as size
FROM system.parts
WHERE table = 'events' AND active
GROUP BY partition
ORDER BY partition;

-- Warning signs: hundreds or thousands of partitions
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

```

## File: skills\clickhouse-best-practices\rules\schema_partition_query_tradeoffs.md
```
---
title: Understand Partition Query Performance Trade-offs
impact: MEDIUM
impactDescription: "Partition pruning helps some queries; spanning many partitions hurts others"
tags: [schema, partitioning, query, performance]
---

## Understand Partition Query Performance Trade-offs

**Impact: MEDIUM**

Partitioning can help or hurt query performance:
- **Potential improvement**: Queries filtering by partition key may benefit from partition pruning
- **Potential degradation**: Queries spanning many partitions increase total parts scanned

ClickHouse automatically builds **MinMax indexes** on partition columns. Data merges occur **within partitions only**, not across them.

**Incorrect (query scans all partitions):**

```sql
-- Query must scan all partitions
SELECT count(*) FROM events
WHERE event_type = 'click';  -- No partition pruning
```

**Correct (query prunes to single partition):**

```sql
-- Query prunes to single partition
SELECT count(*) FROM events
WHERE timestamp >= '2024-01-01' AND timestamp < '2024-02-01'
  AND event_type = 'click';
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

```

## File: skills\clickhouse-best-practices\rules\schema_partition_start_without.md
```
---
title: Consider Starting Without Partitioning
impact: MEDIUM
impactDescription: "Add partitioning later when you have clear lifecycle requirements"
tags: [schema, partitioning, simplicity]
---

## Consider Starting Without Partitioning

**Impact: MEDIUM**

Start without partitioning and add it later only if:
- You have clear data lifecycle requirements (retention, archiving)
- Your access patterns clearly benefit from partition pruning
- You understand the cardinality implications

**Example (start simple):**

```sql
-- Start simple, no partitioning
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Add partitioning later if needed for lifecycle management
-- (requires table recreation or materialized view migration)
```

**When to add partitioning:**

| Need | Add Partitioning? |
|------|-------------------|
| Time-based data retention | Yes |
| Archive old data to cold storage | Yes |
| Query performance on time ranges | Maybe (test first) |
| No specific lifecycle needs | No |

Reference: [Choosing a Partitioning Key](https://clickhouse.com/docs/best-practices/choosing-a-partitioning-key)

```

## File: skills\clickhouse-best-practices\rules\schema_pk_cardinality_order.md
```
---
title: Order Columns by Cardinality (Low to High)
impact: CRITICAL
impactDescription: "Enables granule skipping; high-cardinality first prevents index pruning"
tags: [schema, primary-key, cardinality, ORDER BY]
---

## Order Columns by Cardinality (Low to High)

**Impact: CRITICAL**

Since the sparse primary index operates on data blocks (granules) rather than individual rows, low-cardinality leading columns create more useful index entries that can skip entire blocks. Place lower-cardinality columns before higher-cardinality ones in the ordering key.

**Incorrect (high cardinality first):**

```sql
-- UUID first means no pruning benefit
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id, event_type, timestamp);
-- Every granule has different event_id values, index can't skip anything
```

**Correct (low cardinality first):**

```sql
-- Low cardinality first enables pruning
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_type, event_date, event_id);
-- Index can skip entire event_type groups
```

**Column Order Guidelines:**

| Position | Cardinality | Examples |
|----------|-------------|----------|
| 1st | Low (few distinct values) | event_type, status, country |
| 2nd | Date (coarse granularity) | toDate(timestamp) |
| 3rd+ | Medium-High | user_id, session_id |
| Last | High (if needed) | event_id, uuid |

**Tip:** Use `toDate(timestamp)` instead of raw `DateTime` columns when day-level filtering suffices - this reduces index size from 32-bit to 16-bit representations.

Reference: [Choosing a Primary Key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

```

## File: skills\clickhouse-best-practices\rules\schema_pk_filter_on_orderby.md
```
---
title: Filter on ORDER BY Columns in Queries
impact: CRITICAL
impactDescription: "Skipping prefix columns prevents index usage"
tags: [schema, primary-key, WHERE, query]
---

## Filter on ORDER BY Columns in Queries

**Impact: CRITICAL**

Even with good schema design, queries must use ORDER BY columns to benefit. Skipping prefix columns or filtering on non-ORDER BY columns prevents index usage.

**Incorrect (skips prefix or uses non-ORDER BY columns):**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Skips prefix columns - can't use index effectively
SELECT * FROM events WHERE event_type = 'click';

-- Filter on column not in ORDER BY - full table scan
SELECT * FROM events WHERE user_agent LIKE '%Chrome%';
```

**Correct (uses ORDER BY prefix):**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Full prefix match - best performance
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click';

-- Partial prefix - still uses index
SELECT * FROM events WHERE tenant_id = 123;

-- Range on later column after equality on earlier
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click' AND timestamp >= '2024-01-01';
```

**Index usage reference:**

| Filter | Index Used? |
|--------|-------------|
| `WHERE tenant_id = 123` | Full |
| `WHERE tenant_id = 123 AND event_type = 'click'` | Full |
| `WHERE event_type = 'click'` | None (skipped prefix) |
| `WHERE timestamp > '2024-01-01'` | None (skipped both) |

Reference: [Choosing a Primary Key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

```

## File: skills\clickhouse-best-practices\rules\schema_pk_plan_before_creation.md
```
---
title: Plan PRIMARY KEY Before Table Creation
impact: CRITICAL
impactDescription: "ORDER BY is immutable; wrong choice requires full data migration"
tags: [schema, primary-key, ORDER BY]
---

## Plan PRIMARY KEY Before Table Creation

**Impact: CRITICAL** (immutable after creation)

ClickHouse's ORDER BY clause defines physical data ordering and the sparse index. Unlike other databases, **ORDER BY cannot be modified after table creation**. A wrong choice requires creating a new table and migrating all data.

**Incorrect (arbitrary ORDER BY without query analysis):**

```sql
-- Creating table without analyzing query patterns
CREATE TABLE events (
    event_id UUID,
    user_id UInt64,
    timestamp DateTime
)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Chosen arbitrarily

-- Later: "Most queries filter by user_id!"
-- Cannot fix with: ALTER TABLE events MODIFY ORDER BY (user_id, timestamp)
-- ERROR: Cannot modify ORDER BY
```

**Correct (query-driven ORDER BY selection):**

```sql
-- Step 1: Document query patterns BEFORE creating table
/*
Query Analysis:
- 60% of queries: WHERE user_id = ? AND timestamp BETWEEN ? AND ?
- 25% of queries: WHERE event_type = ? AND timestamp > ?
- 15% of queries: WHERE event_id = ?

Conclusion: user_id and event_type are primary filters
*/

-- Step 2: Create table with correct ORDER BY
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    user_id UInt64,
    event_type LowCardinality(String),
    timestamp DateTime,
    event_date Date DEFAULT toDate(timestamp)
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(event_date)
ORDER BY (user_id, event_date, event_id);
```

**Pre-creation checklist:**
- [ ] Listed top 5-10 query patterns
- [ ] Identified columns in WHERE clauses with frequency
- [ ] Prioritized columns that exclude large numbers of rows
- [ ] Ordered columns by cardinality (low first, high last)
- [ ] Limited to 4-5 key columns (typically sufficient)

Reference: [Choosing a Primary Key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

```

## File: skills\clickhouse-best-practices\rules\schema_pk_prioritize_filters.md
```
---
title: Prioritize Filter Columns in ORDER BY
impact: CRITICAL
impactDescription: "Columns not in ORDER BY cause full table scans"
tags: [schema, primary-key, WHERE, filtering]
---

## Prioritize Filter Columns in ORDER BY

**Impact: CRITICAL**

Prioritize columns frequently used in query filters (WHERE clause), especially those that exclude large numbers of rows. Queries filtering on columns not in ORDER BY result in full table scans.

**Incorrect (ORDER BY doesn't match query patterns):**

```sql
-- If most queries filter by tenant_id:
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Queries by tenant_id will full-scan!
```

**Correct (ORDER BY matches filter patterns):**

```sql
-- ORDER BY matches query filter patterns
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (tenant_id, event_date, event_id);

-- Query now uses primary index:
SELECT * FROM events WHERE tenant_id = 123 AND event_date >= '2024-01-01';
```

**Validation:**

```sql
-- Verify index usage
EXPLAIN indexes = 1
SELECT * FROM events WHERE tenant_id = 123;
-- Look for "PrimaryKey" with Key Condition
```

Reference: [Choosing a Primary Key](https://clickhouse.com/docs/best-practices/choosing-a-primary-key)

```

## File: skills\clickhouse-best-practices\rules\schema_types_avoid_nullable.md
```
---
title: Avoid Nullable Unless Semantically Required
impact: HIGH
impactDescription: "Nullable adds storage overhead; use DEFAULT values instead"
tags: [schema, data-types, Nullable, DEFAULT]
---

## Avoid Nullable Unless Semantically Required

**Impact: HIGH**

Nullable columns maintain a separate UInt8 column for tracking null values, increasing storage and degrading performance. Use DEFAULT values instead when feasible.

**Incorrect (Nullable everywhere):**

```sql
CREATE TABLE users (
    id Nullable(UInt64),              -- IDs should never be null
    name Nullable(String),            -- Empty string is fine
    age Nullable(UInt8),              -- 0 is a valid default
    login_count Nullable(UInt32)      -- 0 is a valid default
)
```

**Correct (DEFAULT values, Nullable only when semantic):**

```sql
CREATE TABLE users (
    id UInt64,                                    -- Never null
    name String DEFAULT '',                       -- Empty = unknown
    age UInt8 DEFAULT 0,                          -- 0 = unknown
    login_count UInt32 DEFAULT 0,                 -- 0 = never logged in
    deleted_at Nullable(DateTime),                -- NULL = not deleted (semantic!)
    parent_id Nullable(UInt64)                    -- NULL = no parent (semantic!)
)
```

**When Nullable IS appropriate:**

| Use Case | Why |
|----------|-----|
| `deleted_at` | NULL = "not deleted", timestamp = "deleted at X" |
| `parent_id` | NULL = "no parent", value = "has parent" |
| `discount_percent` | NULL = "no discount", 0 = "0% discount" |

**Defaults instead of Nullable:**

| Type | Default |
|------|---------|
| String | `''` (empty string) |
| UInt*/Int* | `0` |
| DateTime | `now()` or `toDateTime(0)` |
| UUID | `generateUUIDv4()` |

Reference: [Select Data Types](https://clickhouse.com/docs/best-practices/select-data-types)

```

## File: skills\clickhouse-best-practices\rules\schema_types_enum.md
```
---
title: Use Enum for Finite Value Sets
impact: MEDIUM
impactDescription: "Insert-time validation and natural ordering; 1-2 bytes storage"
tags: [schema, data-types, Enum, validation]
---

## Use Enum for Finite Value Sets

**Impact: MEDIUM**

Enum types provide validation at insert time and enable queries that exploit natural ordering. Use Enum8 (up to 256 values) or Enum16 (up to 65,536 values).

**Incorrect (String without validation):**

```sql
CREATE TABLE orders (
    status String    -- No validation, typos like "shiped" allowed
)

-- Ordering requires CASE statements
SELECT * FROM orders ORDER BY
    CASE status
        WHEN 'pending' THEN 1
        WHEN 'processing' THEN 2
        WHEN 'shipped' THEN 3
    END;
```

**Correct (Enum with validation and ordering):**

```sql
CREATE TABLE orders (
    status Enum8('pending' = 1, 'processing' = 2, 'shipped' = 3, 'delivered' = 4)
)

-- Insert validation: invalid values rejected
INSERT INTO orders VALUES ('shiped');  -- ERROR: Unknown element 'shiped'

-- Natural ordering works automatically
SELECT * FROM orders ORDER BY status;  -- Orders by enum value (1, 2, 3, 4)

-- Comparisons use natural order
SELECT * FROM orders WHERE status > 'processing';  -- shipped and delivered
```

**Enum Guidelines:**

| Scenario | Use |
|----------|-----|
| Fixed set of values known at schema time | Enum8/Enum16 |
| Values may change frequently | LowCardinality(String) |
| Need insert-time validation | Enum |
| Need natural ordering in queries | Enum |
| < 256 distinct values | Enum8 (1 byte) |
| 256-65,536 distinct values | Enum16 (2 bytes) |

Reference: [Select Data Types](https://clickhouse.com/docs/best-practices/select-data-types)

```

## File: skills\clickhouse-best-practices\rules\schema_types_lowcardinality.md
```
---
title: Use LowCardinality for Repeated Strings
impact: HIGH
impactDescription: "Dictionary encoding for <10K unique values; significant storage reduction"
tags: [schema, data-types, LowCardinality, storage]
---

## Use LowCardinality for Repeated Strings

**Impact: HIGH**

String columns with repeated values store each value repeatedly. LowCardinality uses dictionary encoding for significant storage reduction.

**Incorrect (plain String for repeated values):**

```sql
CREATE TABLE events (
    country String,       -- "United States" stored 500M times
    browser String,       -- "Chrome" stored 300M times
    event_type String     -- "page_view" stored 800M times
)
```

**Correct (LowCardinality for low unique counts):**

```sql
CREATE TABLE events (
    country LowCardinality(String),      -- ~200 unique values
    browser LowCardinality(String),      -- ~50 unique values
    event_type LowCardinality(String)    -- ~100 unique values
)
```

**When to use LowCardinality:**

| Unique Values | Recommendation |
|---------------|----------------|
| < 10,000 | Use LowCardinality |
| > 10,000 | Use regular String |

```sql
-- Check cardinality before deciding
SELECT uniq(column_name) FROM table_name;
```

**LowCardinality vs FixedString:**

Reserve `FixedString` for strictly fixed-length data (e.g., 2-char country codes). For most low-cardinality text, `LowCardinality(String)` outperforms `FixedString`.

```sql
-- FixedString: Only for truly fixed-length data
country_code FixedString(2),    -- "US", "DE", "JP" - always 2 chars

-- LowCardinality: For variable-length low-cardinality strings
country_name LowCardinality(String),  -- "United States", "Germany"
```

Reference: [Select Data Types](https://clickhouse.com/docs/best-practices/select-data-types)

```

## File: skills\clickhouse-best-practices\rules\schema_types_minimize_bitwidth.md
```
---
title: Minimize Bit-Width for Numeric Types
impact: HIGH
impactDescription: "Smaller types reduce storage and improve cache efficiency"
tags: [schema, data-types, numeric, storage]
---

## Minimize Bit-Width for Numeric Types

**Impact: HIGH**

Select the smallest numeric type that accommodates your data range. Prefer unsigned types when negative values aren't needed.

**Incorrect (oversized types):**

```sql
CREATE TABLE metrics (
    status_code Int64,        -- HTTP codes are 100-599
    age Int64,                -- Human age fits in UInt8
    year Int64,               -- Years fit in UInt16
    item_count Int64          -- Often small numbers
)
```

**Correct (right-sized types):**

```sql
CREATE TABLE metrics (
    status_code UInt16,       -- 0-65,535 (HTTP codes fit easily)
    age UInt8,                -- 0-255 (sufficient for age)
    year UInt16,              -- 0-65,535 (sufficient for years)
    item_count UInt32         -- 0-4 billion (adjust based on actual max)
)
```

**Numeric Type Reference:**

| Type | Range | Bytes |
|------|-------|-------|
| UInt8 | 0 to 255 | 1 |
| UInt16 | 0 to 65,535 | 2 |
| UInt32 | 0 to 4.3 billion | 4 |
| UInt64 | 0 to 18 quintillion | 8 |
| Int8 | -128 to 127 | 1 |
| Int16 | -32,768 to 32,767 | 2 |
| Int32 | -2.1 billion to 2.1 billion | 4 |
| Int64 | -9 quintillion to 9 quintillion | 8 |

Reference: [Select Data Types](https://clickhouse.com/docs/best-practices/select-data-types)

```

## File: skills\clickhouse-best-practices\rules\schema_types_native_types.md
```
---
title: Use Native Types Instead of String
impact: CRITICAL
impactDescription: "2-10x storage reduction; enables compression and correct semantics"
tags: [schema, data-types, storage]
---

## Use Native Types Instead of String

**Impact: CRITICAL**

Using String for all data wastes storage, prevents compression optimization, and makes comparisons slower. ClickHouse's column-oriented architecture benefits directly from optimal type selection.

**Incorrect (String for everything):**

```sql
CREATE TABLE events (
    event_id String,        -- "550e8400-e29b-41d4-a716-446655440000" = 36 bytes
    user_id String,         -- "12345" = 5 bytes (no numeric operations)
    created_at String,      -- "2024-01-15 10:30:00" = 19 bytes
    count String,           -- "42" - can't do math!
    is_active String        -- "true" = 4 bytes
)
```

**Correct (native types):**

```sql
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),     -- 16 bytes (vs 36)
    user_id UInt64,                              -- 8 bytes, numeric ops
    created_at DateTime DEFAULT now(),           -- 4 bytes (vs 19)
    count UInt32 DEFAULT 0,                      -- 4 bytes, math works
    is_active Bool DEFAULT true                  -- 1 byte (vs 4)
)
```

**Type Selection Quick Reference:**

| Data | Use | Avoid |
|------|-----|-------|
| Sequential IDs | UInt32/UInt64 | String |
| UUIDs | UUID | String |
| Status/Category | Enum8 or LowCardinality(String) | String |
| Timestamps | DateTime | DateTime64, String |
| Dates only | Date or Date32 | DateTime, String |
| Counts | UInt8/16/32 (smallest that fits) | Int64, String |
| Money | Decimal(P,S) or Int64 (cents) | Float64, String |
| Booleans | Bool or UInt8 | String |

Reference: [Select Data Types](https://clickhouse.com/docs/best-practices/select-data-types)

```

## File: skills\clickhouse-best-practices\rules\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-043028-skills-clickhouse-best-practices-rules
name: Rules
path: ecosystem/skills/repo-fetched-agent-skills-043028/skills/clickhouse-best-practices/rules
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Rules
Storage area for 'rules' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\clickhouse-best-practices\rules\_sections.md
```
# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Schema Design (schema)

**Impact:** CRITICAL

**Description:** Proper schema design is foundational to ClickHouse performance. ORDER BY is immutable after table creation; wrong choices require full data migration. Includes primary key selection, data types, partitioning strategy, and JSON usage. Column types and ordering can impact query speed by orders of magnitude.

## 2. Query Optimization (query)

**Impact:** CRITICAL

**Description:** Query patterns dramatically affect performance. JOIN algorithms, filtering strategies, skipping indices, and materialized views can reduce query time from minutes to milliseconds. Pre-computed aggregations read thousands of rows instead of billions.

## 3. Insert Strategy (insert)

**Impact:** CRITICAL

**Description:** Each INSERT creates a data part. Single-row inserts overwhelm the merge process. Proper batching (10K-100K rows), async inserts for high-frequency writes, mutation avoidance, and letting background merges work are essential for stable cluster performance.

```

## File: skills\clickhouse-best-practices\rules\_template.md
```
---
title: Rule Title Here
impact: CRITICAL | HIGH | MEDIUM | LOW
impactDescription: "Quantified improvement (e.g., 10x faster queries)"
tags: [tag1, tag2]
---

## Rule Title Here

**Impact: CRITICAL** (optional description)

Brief explanation of the rule and why it matters. This should be clear and concise, explaining the performance implications.

**Incorrect (description of what's wrong):**

```sql
-- Bad: description
SELECT * FROM table;
```

**Correct (description of what's right):**

```sql
-- Good: description
SELECT * FROM table;
```

Reference: [Official Docs](https://clickhouse.com/docs/best-practices/...)

```

## File: skills\logging-best-practices\metadata.json
```
{
  "version": "1.0.0",
  "organization": "boristane",
  "date": "2025-01-20",
  "abstract": "Logging best practices focused on wide events (canonical log lines), high cardinality data, environment context, single logger pattern, and middleware-based logging infrastructure.",
  "references": [
    "https://loggingsucks.com",
    "https://boristane.com/blog/observability-wide-events-101/",
    "https://stripe.com/blog/canonical-log-lines"
  ]
}

```

## File: skills\logging-best-practices\README.md
```
# Logging Best Practices Skill

A skill for AI coding assistants to apply logging best practices when writing or reviewing code.

## Overview

This skill teaches the **wide events** pattern (also known as canonical log lines) - emit a single, context-rich event per request per service instead of scattered log statements.

## Key Concepts

- **Wide Events**: One comprehensive event per request, emitted at completion
- **High Cardinality**: Support fields with millions of unique values (user_id, request_id)
- **High Dimensionality**: Include many fields (20+) per event
- **Business Context**: Always include user subscription, cart value, feature flags
- **Environment Context**: Always include commit hash, version, region, instance ID
- **Single Logger**: One logger instance configured at startup, used everywhere
- **Middleware Pattern**: Handle logging infrastructure in middleware, business context in handlers

## Structure

```
logging-best-practices/
├── SKILL.md              # Agent instructions
├── README.md             # This file
├── metadata.json         # Version and references
└── rules/
    ├── wide-events.md    # Core pattern (CRITICAL)
    ├── context.md        # Cardinality, business & environment context (CRITICAL)
    ├── structure.md      # Single logger, middleware, JSON format (HIGH)
    └── pitfalls.md       # Common mistakes (MEDIUM)
```

## Rules

1. **Wide Events** (CRITICAL) - One event per request, emit in finally block, request ID correlation
2. **Context** (CRITICAL) - High cardinality, dimensionality, business context, environment characteristics
3. **Structure** (HIGH) - Single logger, middleware pattern, JSON format, consistent schema
4. **Pitfalls** (MEDIUM) - Scattered logs, unknown unknowns, missing request correlation

## Reference

- [Boris Tane's Blog - Logging Sucks](https://loggingsucks.com)
- [Boris Tane's Blog - Observability wide events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe Blog - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)

```

## File: skills\logging-best-practices\SKILL.md
```
---
name: logging-best-practices
description: Logging best practices focused on wide events (canonical log lines) for powerful debugging and analytics
license: MIT
metadata:
  author: boristane
  version: "1.0.0"
---

# Logging Best Practices Skill

Version: 1.0.0

## Purpose

This skill provides guidelines for implementing effective logging in applications. It focuses on **wide events** (also called canonical log lines) - a pattern where you emit a single, context-rich event per request per service, enabling powerful debugging and analytics.

## When to Apply

Apply these guidelines when:
- Writing or reviewing logging code
- Adding console.log, logger.info, or similar
- Designing logging strategy for new services
- Setting up logging infrastructure

## Core Principles

### 1. Wide Events (CRITICAL)

Emit **one context-rich event per request per service**. Instead of scattering log lines throughout your handler, consolidate everything into a single structured event emitted at request completion.

```typescript
const wideEvent: Record<string, unknown> = {
  method: 'POST',
  path: '/checkout',
  requestId: c.get('requestId'),
  timestamp: new Date().toISOString(),
};

try {
  const user = await getUser(c.get('userId'));
  wideEvent.user = { id: user.id, subscription: user.subscription };

  const cart = await getCart(user.id);
  wideEvent.cart = { total_cents: cart.total, item_count: cart.items.length };

  wideEvent.status_code = 200;
  wideEvent.outcome = 'success';
  return c.json({ success: true });
} catch (error) {
  wideEvent.status_code = 500;
  wideEvent.outcome = 'error';
  wideEvent.error = { message: error.message, type: error.name };
  throw error;
} finally {
  wideEvent.duration_ms = Date.now() - startTime;
  logger.info(wideEvent);
}
```

### 2. High Cardinality & Dimensionality (CRITICAL)

Include fields with high cardinality (user IDs, request IDs - millions of unique values) and high dimensionality (many fields per event). This enables querying by specific users and answering questions you haven't anticipated yet.

### 3. Business Context (CRITICAL)

Always include business context: user subscription tier, cart value, feature flags, account age. The goal is to know "a premium customer couldn't complete a $2,499 purchase" not just "checkout failed."

### 4. Environment Characteristics (CRITICAL)

Include environment and deployment info in every event: commit hash, service version, region, instance ID. This enables correlating issues with deployments and identifying region-specific problems.

### 5. Single Logger (HIGH)

Use one logger instance configured at startup and import it everywhere. This ensures consistent formatting and automatic environment context.

### 6. Middleware Pattern (HIGH)

Use middleware to handle wide event infrastructure (timing, status, environment, emission). Handlers should only add business context.

### 7. Structure & Consistency (HIGH)

- Use JSON format consistently
- Maintain consistent field names across services
- Simplify to two log levels: `info` and `error`
- Never log unstructured strings

## Anti-Patterns to Avoid

1. **Scattered logs**: Multiple console.log() calls per request
2. **Multiple loggers**: Different logger instances in different files
3. **Missing environment context**: No commit hash or deployment info
4. **Missing business context**: Logging technical details without user/business data
5. **Unstructured strings**: `console.log('something happened')` instead of structured data
6. **Inconsistent schemas**: Different field names across services

## Guidelines

### Wide Events (`rules/wide-events.md`)
- Emit one wide event per service hop
- Include all relevant context
- Connect events with request ID
- Emit at request completion in finally block

### Context (`rules/context.md`)
- Support high cardinality fields (user_id, request_id)
- Include high dimensionality (many fields)
- Always include business context
- Always include environment characteristics (commit_hash, version, region)

### Structure (`rules/structure.md`)
- Use a single logger throughout the codebase
- Use middleware for consistent wide events
- Use JSON format
- Maintain consistent schema
- Simplify to info and error levels
- Never log unstructured strings

### Common Pitfalls (`rules/pitfalls.md`)
- Avoid multiple log lines per request
- Design for unknown unknowns
- Always propagate request IDs across services

References:
- [Logging Sucks](https://loggingsucks.com)
- [Observability Wide Events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)

```

## File: skills\logging-best-practices\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_skills_144258-skills-logging-best-practices
name: Logging-Best-Practices
path: ecosystem/skills/repo_fetched_agent_skills_144258/skills/logging-best-practices
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Logging-Best-Practices
Storage area for 'logging-best-practices' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\logging-best-practices\rules\context.md
```
---
title: Context, Cardinality, and Dimensionality
impact: CRITICAL
tags: logging, context, cardinality, dimensionality
---

## Context, Cardinality, and Dimensionality

**Impact: CRITICAL**

Wide events must be context-rich with high cardinality and high dimensionality. This enables you to answer questions you haven't anticipated yet - the "unknown unknowns" that traditional logging misses.

### High Cardinality

High cardinality means a field can have millions or billions of unique values. User IDs, request IDs, and transaction IDs are high cardinality fields. Your logging must support querying against any specific value of these fields. Without high cardinality support, you cannot debug issues for specific users.

### High Dimensionality

High dimensionality means your events have many fields (20-100+). More dimensions mean more questions you can answer without redeploying code.

```typescript
const wideEvent = {
  // Timing
  timestamp: '2024-09-08T06:14:05.680Z',
  duration_ms: 268,

  // Request context
  method: 'POST',
  path: '/checkout',
  requestId: 'req_abc123',

  // Infrastructure
  service: 'checkout-service',
  version: '2.4.1',
  region: 'us-east-1',
  commit_hash: '690de31f',

  // User context (HIGH CARDINALITY - millions of unique values)
  user: {
    id: 'user_456',
    subscription: 'premium',
    account_age_days: 847,
    lifetime_value_cents: 284700,
  },

  // Business context
  cart: {
    id: 'cart_xyz',
    item_count: 3,
    total_cents: 15999,
    coupon_applied: 'SAVE20',
  },

  // Payment details
  payment: {
    method: 'card',
    provider: 'stripe',
    latency_ms: 189,
  },

  // Feature flags - crucial for debugging rollouts
  feature_flags: {
    new_checkout_flow: true,
  },

  // Outcome
  status_code: 200,
  outcome: 'success',
};
```

### Always Include Business Context

Include business-specific context, not just technical details. User subscription tier, cart value, feature flags, account age - this context helps prioritize issues and understand business impact.

```typescript
const wideEvent = {
  requestId: 'req_123',
  method: 'POST',
  path: '/checkout',
  status_code: 500,

  // Business context that changes response priority
  user: {
    id: 'user_456',
    subscription: 'enterprise',        // High-value customer
    account_age_days: 1247,            // Long-term customer
    lifetime_value_cents: 4850000,     // $48,500 LTV
  },

  cart: {
    total_cents: 249900,               // $2,499 order
    contains_annual_plan: true,        // Recurring revenue at stake
  },

  feature_flags: {
    new_payment_flow: true,            // Was new code involved?
  },

  error: {
    type: 'PaymentError',
    code: 'card_declined',
  },
};
// Now you KNOW this is critical: Enterprise customer, $48.5k LTV,
// trying to make a $2.5k purchase, and new_payment_flow is enabled
```

Business context transforms debugging from "something broke" to "this $48,500 customer can't complete a $2,499 order."

### Always Include Environment Characteristics

Include environment and deployment information in every wide event. This context is essential for correlating issues with deployments, identifying region-specific problems, and understanding the runtime environment.

**Environment fields to include:**

```typescript
const wideEvent = {
  // ... request and business context

  // Environment characteristics
  env: {
    // Deployment info
    commit_hash: process.env.COMMIT_SHA || process.env.GIT_COMMIT,
    version: process.env.SERVICE_VERSION || process.env.npm_package_version,
    deployment_id: process.env.DEPLOYMENT_ID,
    deploy_time: process.env.DEPLOY_TIMESTAMP,

    // Infrastructure
    service: process.env.SERVICE_NAME,
    region: process.env.AWS_REGION || process.env.REGION,
    availability_zone: process.env.AWS_AVAILABILITY_ZONE,
    instance_id: process.env.INSTANCE_ID || process.env.HOSTNAME,
    container_id: process.env.CONTAINER_ID,

    // Runtime
    node_version: process.version,
    runtime: process.env.AWS_EXECUTION_ENV || 'node',
    memory_limit_mb: process.env.AWS_LAMBDA_FUNCTION_MEMORY_SIZE,

    // Environment type
    environment: process.env.NODE_ENV || process.env.ENVIRONMENT,
    stage: process.env.STAGE,
  },
};
```

**Why environment context matters:**

- **commit_hash**: Instantly identify which code version caused an issue
- **deployment_id**: Correlate errors with specific deployments
- **region/availability_zone**: Identify region-specific failures
- **instance_id**: Debug issues affecting specific instances
- **version**: Track issues across service versions
- **environment**: Distinguish production from staging issues

This environment context should be added once at service startup and automatically included in every wide event via middleware.

```

## File: skills\logging-best-practices\rules\pitfalls.md
```
---
title: Common Pitfalls
impact: MEDIUM
tags: logging, anti-patterns, pitfalls
---

## Common Pitfalls

**Impact: MEDIUM**

Avoid these anti-patterns that undermine your logging effectiveness.

### Pitfall 1: Too Many Log Lines Per Request

Emitting multiple log lines per request creates noise without value. These scattered logs cannot be efficiently queried.

**Incorrect:**

```typescript
app.post('/checkout', async (c) => {
  console.log('Received checkout request');                    // Line 1
  console.log(`User ID: ${c.get('userId')}`);                  // Line 2
  const user = await getUser(c.get('userId'));
  console.log(`User fetched: ${user.email}`);                  // Line 3
  const cart = await getCart(user.id);
  console.log(`Cart fetched: ${cart.items.length} items`);     // Line 4
  const payment = await processPayment(cart);
  console.log(`Payment processed: ${payment.status}`);         // Line 5
  console.log('Checkout completed successfully');              // Line 6
  return c.json({ orderId: payment.orderId });
});
// 6 log lines per request = noise
```

**Correct:**

```typescript
// Single wide event with everything
const wideEvent = {
  method: 'POST',
  path: '/checkout',
  user: { id: user.id, email: user.email },
  cart: { item_count: cart.items.length, total: cart.total },
  payment: { status: payment.status, order_id: payment.orderId },
  status_code: 200,
  duration_ms: 1247,
};
```

### Pitfall 2: Not Designing for Unknown Unknowns

Traditional logging captures "known unknowns" - issues you anticipated. But production bugs are often "unknown unknowns" - issues you never predicted. Wide events with rich context enable investigating issues you didn't anticipate.

**Incorrect:**

```typescript
// Logging only for anticipated issues
app.post('/articles', async (c) => {
  const article = await createArticle(c.req.body, user);
  if (!article.published) {
    console.log('Article created but not published');  // Anticipated issue
  }
  return c.json({ article });
});

// Bug: "Users on free trial can't see their articles"
// Your logs say: "Article created successfully" ✓
// But you have NO visibility into:
// - Which users are affected (free trial? all?)
// - What subscription plans see this issue
// - When it started
```

**Correct:**

```typescript
// Wide event captures everything
wideEvent.user = {
  id: user.id,
  subscription: user.subscription,
  trial: user.trial,
  trial_expiration: user.trialExpiration,
};

wideEvent.article = {
  id: article.id,
  published: article.published,  // Captured even though we didn't anticipate the bug
};

// Now you can query: WHERE article.published = false GROUP BY user.trial
// Result: 95% of unpublished articles are from trial users!
```

### Pitfall 3: Missing Request Correlation

Without request IDs propagated across services, you cannot trace a request's journey.

**Incorrect:**

```typescript
// Service A logs
{ message: 'Order created', order_id: 'ord_123' }

// Service B logs
{ message: 'Inventory reserved', items: 3 }

// No way to connect these two events!
```

**Correct:**

```typescript
// Both services include the same request_id
{ request_id: 'req_abc', message: 'Order created', order_id: 'ord_123' }
{ request_id: 'req_abc', message: 'Inventory reserved', items: 3 }

// Query: WHERE request_id = 'req_abc' shows the full flow
```

```

## File: skills\logging-best-practices\rules\structure.md
```
---
title: Structure and Format
impact: HIGH
tags: logging, json, structured-logging, schema, middleware
---

## Structure and Format

**Impact: HIGH**

Structured logging with consistent formats enables efficient querying and analysis. The right structure transforms logs from text files into queryable data.

### Use a Single Logger Throughout the Codebase

Use one logger instance configured at application startup and import it everywhere. This ensures consistent formatting, log levels, and output destinations across all modules.

```typescript
// lib/logger.ts - Single logger configuration
import pino from 'pino';

// Configure once at startup
export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    // Environment context added to ALL logs automatically
    service: process.env.SERVICE_NAME,
    version: process.env.SERVICE_VERSION,
    commit_hash: process.env.COMMIT_SHA,
    region: process.env.AWS_REGION,
    environment: process.env.NODE_ENV,
  },
});

// Usage everywhere else - just import
// services/checkout.ts
import { logger } from '../lib/logger';

logger.info({ event: 'checkout_completed', orderId });
```

**Benefits:**
- Consistent log format across all modules
- Environment context automatically included
- Single place to change log level or destination
- No risk of misconfigured loggers in different files

**Avoid:**
```typescript
// DON'T create new loggers in each file
const logger = new Logger(); // Each file creates its own
console.log('some event');   // Bypasses the logger entirely
```

### Use Middleware for Consistent Wide Events

Implement wide event collection as middleware that wraps all request handlers. The middleware initializes the event, captures timing, handles emission in the finally block, and makes the event accessible to handlers for enrichment.

```typescript
// middleware/wideEvent.ts
import { logger } from '../lib/logger';

// Capture environment once at startup
const envContext = {
  service: process.env.SERVICE_NAME,
  version: process.env.SERVICE_VERSION,
  commit_hash: process.env.COMMIT_SHA,
  region: process.env.AWS_REGION,
  environment: process.env.NODE_ENV,
  instance_id: process.env.HOSTNAME,
};

export function wideEventMiddleware() {
  return async (c: Context, next: Next) => {
    const startTime = Date.now();

    // Initialize event with standard fields + environment
    const wideEvent: Record<string, unknown> = {
      request_id: c.get('requestId') || crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      method: c.req.method,
      path: c.req.path,
      user_agent: c.req.header('user-agent'),
      ...envContext,  // Environment automatically included
    };

    // Make event accessible to handlers for enrichment
    c.set('wideEvent', wideEvent);

    try {
      await next();
      wideEvent.status_code = c.res.status;
      wideEvent.outcome = c.res.status < 400 ? 'success' : 'error';
    } catch (error) {
      wideEvent.status_code = 500;
      wideEvent.outcome = 'error';
      wideEvent.error = {
        type: error.name,
        message: error.message,
      };
      throw error;
    } finally {
      wideEvent.duration_ms = Date.now() - startTime;
      logger.info(wideEvent);  // Uses the single logger
    }
  };
}

// Apply middleware globally
app.use('*', wideEventMiddleware());
```

**Handlers just enrich with business context:**

```typescript
app.post('/checkout', async (c) => {
  const wideEvent = c.get('wideEvent');
  const user = c.get('user');

  // Add business context - environment already included by middleware
  wideEvent.user = { id: user.id, subscription: user.subscription };

  const cart = await getCart(user.id);
  wideEvent.cart = { id: cart.id, total: cart.total };

  const order = await createOrder(cart);
  wideEvent.order = { id: order.id };

  return c.json(order, 201);
});
// Middleware handles: timing, status, environment, emission
// Handler handles: business context only
```

### Use JSON Format

Use JSON as your logging format. JSON is universally supported, enables nested objects for complex context, works across all programming languages, and is easily parsed.

```typescript
const wideEvent = {
  timestamp: '2024-09-08T06:14:05.680Z',
  service: 'articles',
  requestId: 'req_abc123',
  message: 'Article created',
  user: { id: 'user_123', subscription: 'premium' },
  article: { id: 'article_456', title: 'My Post' },
  duration_ms: 268,
  status_code: 201,
};

// Emit as single-line JSON
logger.info(wideEvent);
```

### Maintain Consistent Schema

Use consistent field names across all services. If one service uses `user_id` and another uses `userId`, querying becomes painful.

```typescript
// All services use the same schema
{
  request_id: 'req_abc',
  user: { id: 'user_123' },
  duration_ms: 268,
  status_code: 200,
}
```

Define your schema once and share it across services via a common library or documented standard.

### Simplify Log Levels

Limit yourself to two log levels: `info` and `error`. The distinction between debug, trace, warn, info, notice, and critical creates confusion without adding value.

- **INFO**: Normal operations, all wide events
- **ERROR**: Unexpected failures that need attention

If you find yourself wanting debug logs, add that context to your wide event instead.

### Never Log Unstructured Strings

Every log must be structured with queryable fields. `console.log('User logged in')` is useless for debugging at scale.

```typescript
// Add the data to your wide event instead
wideEvent.order = { id: orderId, status: 'created' };
wideEvent.payment = { error: { message: error.message } };
// Now it's queryable: WHERE order.status = 'created'
```

If you're tempted to write `console.log('something happened')`, ask: "What fields would make this queryable?" Then add those fields to your wide event instead.

```

## File: skills\logging-best-practices\rules\wide_events.md
```
---
title: Wide Events / Canonical Log Lines
impact: CRITICAL
tags: logging, wide-events, canonical-log-lines
---

## Wide Events / Canonical Log Lines

**Impact: CRITICAL**

Wide events (also called canonical log lines) are the foundation of effective logging. For each request, emit **a single context-rich event per service**. Instead of scattering 10-20 log lines throughout your request handler, consolidate everything into one comprehensive event emitted at the end of the request.

### The Pattern

Build the event throughout the request lifecycle, then emit once at completion in a `finally` block. This ensures the event is always emitted with complete context, even during failures.

**Incorrect:**

```typescript
app.post('/articles', async (c) => {
  console.log('Received POST /articles request');

  const body = await c.req.json();
  console.log('Request body parsed', { title: body.title });

  const user = await getUser(c.get('userId'));
  console.log('User fetched', { userId: user.id });

  const article = await database.saveArticle({ ...body, ownerId: user.id });
  console.log('Article saved', { articleId: article.id });

  await cache.set(article.id, article);
  console.log('Cache updated');

  console.log('Request completed successfully');
  return c.json({ article }, 201);
});
// 6 disconnected log lines with scattered context
// Cannot query: "show me all article creates by free trial users"
```

**Correct:**

```typescript
app.post('/articles', async (c) => {
  const startTime = Date.now();
  const wideEvent: Record<string, unknown> = {
    method: 'POST',
    path: '/articles',
    service: 'articles',
    requestId: c.get('requestId'),
  };

  try {
    const body = await c.req.json();
    const user = await getUser(c.get('userId'));
    wideEvent.user = {
      id: user.id,
      subscription: user.subscription,
      trial: user.trial,
    };

    const article = await database.saveArticle({ ...body, ownerId: user.id });
    wideEvent.article = {
      id: article.id,
      title: article.title,
      published: article.published,
    };

    await cache.set(article.id, article);
    wideEvent.cache = { operation: 'write', key: article.id };

    wideEvent.status_code = 201;
    wideEvent.outcome = 'success';
    return c.json({ article }, 201);
  } catch (error) {
    wideEvent.status_code = 500;
    wideEvent.outcome = 'error';
    wideEvent.error = { message: error.message, type: error.name };
    throw error;
  } finally {
    wideEvent.duration_ms = Date.now() - startTime;
    wideEvent.timestamp = new Date().toISOString();
    logger.info(JSON.stringify(wideEvent));
  }
});
// Single event with all context - queryable by any field
```

### Connect Events with Request ID

Every wide event must include a unique request ID that is propagated across all service hops. This is the only way to reconstruct the full journey of a request through a distributed system.

```typescript
// Service A - generate and propagate
const requestId = c.get('requestId') || crypto.randomUUID();
wideEvent.requestId = requestId;

await fetch('http://downstream-service/endpoint', {
  headers: { 'x-request-id': requestId },
  body: JSON.stringify(data),
});

// Service B - extract and use
const requestId = c.req.header('x-request-id');
wideEvent.requestId = requestId;  // Same ID links events together
```

### Emit in Finally Block

Always emit wide events in a `finally` block or equivalent. This ensures the event is emitted with complete context regardless of success or failure.

Reference: [Stripe Blog - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)

```

## File: skills\logging-best-practices\rules\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_skills_144258-skills-logging-best-practices-rules
name: Rules
path: ecosystem/skills/repo_fetched_agent_skills_144258/skills/logging-best-practices/rules
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Rules
Storage area for 'rules' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: trading-engine\SKILL.md
```
---
name: Vincent - Trading Engine for agents
description: |
  Strategy-driven automated trading for Polymarket and HyperLiquid. Use this skill when users want to create
  trading strategies, set stop-loss/take-profit/trailing stop rules, or manage automated trading.
  Triggers on "trading strategy", "stop loss", "take profit", "trailing stop", "automated trading",
  "trading engine", "trade rules", "strategy monitor".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent Trading Engine - Strategy-Driven Automated Trading

Use this skill to create and manage automated trading strategies for Polymarket prediction markets and HyperLiquid perpetuals/spot. The Trading Engine combines driver-based monitoring (web search, Twitter, newswire, price feeds) with a signal pipeline and LLM-powered decision-making to automatically trade based on your thesis. It also includes standalone stop-loss, take-profit, and trailing stop rules that work without the LLM.

All commands use the `@vincentai/cli` package.

## How It Works

**The Trading Engine is a unified system with two modes:**

1. **LLM-Powered Strategies** — Create a versioned strategy with a structured thesis, weighted drivers (web search keywords, Twitter accounts, newswire topics, price triggers), and an escalation policy. When drivers detect new information, signals are scored and batched. When the escalation threshold is met, an LLM (Claude via OpenRouter) evaluates the signals against your thesis and decides whether to trade, update the thesis, set protective orders, or alert you.
2. **Standalone Trade Rules** — Set stop-loss, take-profit, and trailing stop rules on positions. These execute automatically when price conditions are met — no LLM involved.

**Architecture:**

- Integrated into the Vincent backend (no separate service to run)
- Strategy endpoints under `/api/skills/polymarket/strategies/...`
- Trade rule endpoints under `/api/skills/polymarket/rules/...`
- HyperLiquid rules use `venue: "hyperliquid"` and route through the HL adapter
- Uses the same API key as the Polymarket or HyperLiquid skill (depending on venue)
- All trades go through Vincent's policy-enforced pipeline
- LLM costs are metered and deducted from the user's credit balance
- Every LLM invocation is recorded with full audit trail (tokens, cost, actions, duration)

## Security Model

- **LLM cannot bypass policies** — all trades go through the venue's policy-enforced skill (`polymarketSkill.placeBet()` or `hyperliquidSkill.trade()`) which enforces spending limits, approval thresholds, and allowlists
- **Backend-side LLM key** — the OpenRouter API key never leaves the server. Agents and users cannot invoke the LLM directly
- **Credit gating** — no LLM invocation without sufficient credit balance
- **Tool constraints** — the LLM's available tools are controlled by the strategy's `config.tools` settings. If `canTrade: false`, the trade tool is not provided
- **Rate limiting** — max concurrent LLM invocations is capped to prevent runaway costs
- **Audit trail** — every invocation is recorded with full prompt, response, actions, cost, and duration
- **No private keys** — the Trading Engine uses the Vincent API for all trades. Private keys stay on Vincent's servers

## Part 1: LLM-Powered Strategies

### Core Concepts

- **Instrument**: A tradeable asset on a venue. Defined by `id`, `type` (stock, perp, swap, binary, option), `venue`, and optional constraints (leverage, margin, liquidity, fees).
- **Thesis**: Your directional view — `estimate` (target price/value), `direction` (long/short/neutral), `confidence` (0–1), and `reasoning`.
- **Driver**: A named information source that feeds the signal pipeline. Each driver has a `weight`, `direction` (bullish/bearish/contextual), and `monitoring` config (entities, keywords, embedding anchor, sources, polling interval).
- **Escalation Policy**: Controls when the LLM is woken up. `signalScoreThreshold` (minimum score to batch), `highConfidenceThreshold` (score that triggers immediate wake), `maxWakeFrequency` (e.g. "1 per 15m"), `batchWindow` (e.g. "5m").
- **Trade Rules**: Entry rules (min edge, order type), exit rules (thesis invalidation triggers), auto-actions (stop-loss, take-profit, trailing stop, price delta triggers), and sizing rules (method, max position, portfolio %, max trades/day).

### Signal Pipeline

Strategies process information through a 6-layer pipeline:

1. **Ingest** — Raw data from driver sources (web search, Twitter, newswire, price feeds, RSS, Reddit, on-chain, filings, options flow)
2. **Filter** — Deduplication and relevance filtering. Drops signals already seen or below quality threshold
3. **Score** — Each signal is scored (0–1) based on driver weight, embedding similarity to the anchor, and entity/keyword matches
4. **Escalate** — Scored signals are batched according to the escalation policy. Low-score signals accumulate in a batch window; high-confidence signals trigger immediate LLM wake
5. **LLM** — The LLM evaluates batched signals against the current thesis. It can update the thesis, issue trade decisions, update driver states, or take no action
6. **Execute** — Trade decisions pass through policy enforcement and are routed to the appropriate venue adapter for execution

### Strategy Lifecycle

Strategies follow a versioned lifecycle: `DRAFT` → `ACTIVE` → `PAUSED` → `ARCHIVED`

- **DRAFT**: Can be edited. Not yet monitoring or invoking the LLM.
- **ACTIVE**: Drivers are running. New signals trigger the pipeline.
- **PAUSED**: Monitoring is stopped. Can be resumed.
- **ARCHIVED**: Permanently stopped. Cannot be reactivated.

To iterate on a strategy, duplicate it as a new version (creates a new DRAFT with incremented version number and the same config).

### Create a Strategy

```bash
npx @vincentai/cli@latest trading-engine create-strategy \
  --key-id <KEY_ID> \
  --name "BTC Momentum" \
  --config '{
    "instruments": [
      { "id": "btc-usd-perp", "type": "perp", "venue": "polymarket" },
      { "id": "BTC", "type": "perp", "venue": "hyperliquid" }
    ],
    "thesis": {
      "estimate": 105000,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "ETF inflows accelerating, halving supply shock imminent"
    },
    "drivers": [
      {
        "name": "ETF Flow Monitor",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "entities": ["BlackRock", "Fidelity"],
          "keywords": ["bitcoin ETF", "BTC inflow"],
          "embeddingAnchor": "Bitcoin ETF institutional inflows",
          "sources": ["web_search", "newswire"]
        }
      },
      {
        "name": "Crypto Twitter",
        "weight": 1.0,
        "direction": "contextual",
        "monitoring": {
          "entities": ["@BitcoinMagazine", "@saborskycnbc"],
          "keywords": ["bitcoin", "BTC"],
          "sources": ["twitter"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05, "orderType": "limit", "limitOffset": 0.01 },
      "autoActions": { "stopLoss": -0.10, "takeProfit": 0.25, "trailingStop": -0.05 },
      "exit": { "thesisInvalidation": ["ETF outflows exceed $500M/week"] },
      "sizing": {
        "method": "edgeScaled",
        "maxPosition": 500,
        "maxPortfolioPct": 20,
        "maxTradesPerDay": 5,
        "minTimeBetweenTrades": "30m"
      }
    },
    "notifications": {
      "onTrade": true,
      "onThesisChange": true,
      "channel": "none"
    }
  }'
```

**Parameters:**

- `--name`: Strategy name
- `--config`: Full strategy config JSON (see Core Concepts above for structure)
- `--data-source-secret-id`: Optional DATA_SOURCES secret ID for driver monitoring API calls
- `--poll-interval`: Polling interval in minutes for driver monitoring (default: 15)

### List Strategies

```bash
npx @vincentai/cli@latest trading-engine list-strategies --key-id <KEY_ID>
```

### Get Strategy Details

```bash
npx @vincentai/cli@latest trading-engine get-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Update a Strategy

Update a DRAFT strategy. Pass only the fields you want to change — config is a partial object.

```bash
npx @vincentai/cli@latest trading-engine update-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID> \
  --name "Updated Name" --config '{ "thesis": { "confidence": 0.8, "reasoning": "Updated reasoning" } }'
```

**Parameters:**

- `--strategy-id`: Strategy ID (required)
- `--name`: New strategy name
- `--config`: Partial strategy config JSON — only include fields to update
- `--data-source-secret-id`: DATA_SOURCES secret ID
- `--poll-interval`: New polling interval in minutes

### Activate a Strategy

Starts driver monitoring and signal pipeline processing. Strategy must be in DRAFT status.

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Pause a Strategy

Stops monitoring. Strategy must be ACTIVE.

```bash
npx @vincentai/cli@latest trading-engine pause --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Resume a Strategy

Resumes monitoring. Strategy must be PAUSED.

```bash
npx @vincentai/cli@latest trading-engine resume --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Archive a Strategy

Permanently stops a strategy. Cannot be undone.

```bash
npx @vincentai/cli@latest trading-engine archive --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Duplicate a Strategy (New Version)

Creates a new DRAFT with the same config, incremented version number, and a link to the parent version.

```bash
npx @vincentai/cli@latest trading-engine duplicate-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### View Version History

See all versions of a strategy lineage.

```bash
npx @vincentai/cli@latest trading-engine versions --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### View LLM Invocation History

See the LLM decision log for a strategy — what data triggered it, what the LLM decided, what actions were taken, and the cost.

```bash
npx @vincentai/cli@latest trading-engine invocations --key-id <KEY_ID> --strategy-id <STRATEGY_ID> --limit 20
```

### View Cost Summary

See aggregate LLM costs for all strategies under a secret.

```bash
npx @vincentai/cli@latest trading-engine costs --key-id <KEY_ID>
```

### View Performance Metrics

See performance metrics for a strategy: P&L, win rate, trade count, and per-instrument breakdown.

```bash
npx @vincentai/cli@latest trading-engine performance --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Driver Configuration

#### Web Search Drivers

Add a driver with `"sources": ["web_search"]`. The engine periodically searches Brave for the driver's keywords and triggers the signal pipeline when new results appear.

```json
{
  "name": "AI News Monitor",
  "weight": 1.5,
  "direction": "bullish",
  "monitoring": {
    "keywords": ["AI tokens", "GPU shortage", "prediction market regulation"],
    "embeddingAnchor": "AI technology investment trends",
    "sources": ["web_search"]
  }
}
```

Each keyword is searched independently. Results are deduplicated — the same URLs won't trigger the pipeline twice.

#### Twitter Drivers

Add a driver with `"sources": ["twitter"]`. The engine periodically checks the specified entities for new tweets.

```json
{
  "name": "Crypto Twitter",
  "weight": 1.0,
  "direction": "contextual",
  "monitoring": {
    "entities": ["@DeepSeek", "@nvidia", "@OpenAI"],
    "keywords": ["AI", "GPU"],
    "sources": ["twitter"]
  }
}
```

Tweets are deduplicated by tweet ID — only genuinely new tweets trigger the pipeline.

#### Newswire Drivers (Finnhub)

Add a driver with `"sources": ["newswire"]`. The engine periodically polls Finnhub's market news API and triggers the pipeline when new headlines matching your keywords appear.

```json
{
  "name": "Market News",
  "weight": 1.5,
  "direction": "contextual",
  "monitoring": {
    "keywords": ["artificial intelligence", "GPU shortage", "semiconductor"],
    "sources": ["newswire"]
  }
}
```

Headlines and summaries are matched case-insensitively. Articles are deduplicated by headline hash with a sliding window.

**Note:** Requires a `FINNHUB_API_KEY` env var on the server. Finnhub's free tier allows 60 API calls/min. No per-call credit deduction.

#### Price Triggers

Price triggers are evaluated in real-time via the Polymarket WebSocket feed. When a price condition is met, the signal pipeline is invoked with the price data.

Trigger types:

- `ABOVE` — triggers when price exceeds a threshold
- `BELOW` — triggers when price drops below a threshold
- `CHANGE_PCT` — triggers on a percentage change from reference price

Price triggers are one-shot: once fired, they're marked as consumed. The LLM can create new triggers if needed.

### Thesis Best Practices

The thesis is your structured directional view. Good theses include:

1. **A clear estimate**: Target price or value the market should reach
2. **A confidence level**: Start at 0.5–0.7 and let the LLM adjust as new data arrives
3. **Specific reasoning**: "ETF inflows accelerating, halving supply shock imminent" is better than "BTC will go up"
4. **Explicit invalidation conditions**: Use `tradeRules.exit.thesisInvalidation` to define what would break your thesis

### LLM Available Tools

When the LLM is invoked, it can use these tools (depending on strategy config):

| Tool                | Description                        | Requires                           |
| ------------------- | ---------------------------------- | ---------------------------------- |
| `place_trade`       | Buy or sell a position             | `canTrade: true` in trade rules    |
| `set_stop_loss`     | Set a stop-loss rule on a position | `canSetRules: true` in trade rules |
| `set_take_profit`   | Set a take-profit rule             | `canSetRules: true` in trade rules |
| `set_trailing_stop` | Set a trailing stop                | `canSetRules: true` in trade rules |
| `alert_user`        | Send an alert without trading      | Always available                   |
| `no_action`         | Do nothing (with reasoning)        | Always available                   |

### Cost Tracking

Every LLM invocation is metered:

- **Token costs**: Input and output tokens are priced per the model's rate
- **Deducted from credit balance**: Same pool as data source credits (`dataSourceCreditUsd`)
- **Pre-flight check**: If insufficient credit, the invocation is skipped and logged
- **Data source costs**: Brave Search (~$0.005/call) and Twitter (~$0.005-$0.01/call) are also metered. Finnhub newswire calls are free (no credit deduction)

Typical LLM invocation cost: $0.05–$0.30 depending on context size.

---

## Part 2: Standalone Trade Rules

Trade rules execute automatically when price conditions are met — no LLM involved. These are stop-loss, take-profit, and trailing stop rules that protect your positions.

### Check Worker Status

```bash
npx @vincentai/cli@latest trading-engine status --key-id <KEY_ID>
# Returns: worker status, active rules count, last sync time, circuit breaker state
```

### Create a Stop-Loss Rule

Automatically sell a position if price drops below a threshold:

```bash
# Polymarket — triggerPrice is 0–1 (outcome token price)
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type STOP_LOSS --trigger-price 0.40

# HyperLiquid — triggerPrice is absolute USD price, marketId and tokenId are the coin name
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

**Parameters:**

- `--venue`: `polymarket` (default) or `hyperliquid`
- `--market-id`: Polymarket condition ID, or coin name for HyperLiquid (e.g. `BTC`, `ETH`)
- `--token-id`: Polymarket outcome token ID, or coin name for HyperLiquid
- `--rule-type`: `STOP_LOSS` (sells if price <= trigger), `TAKE_PROFIT` (sells if price >= trigger), or `TRAILING_STOP`
- `--trigger-price`: Price threshold — 0 to 1 for Polymarket, absolute USD price for HyperLiquid

### Create a Take-Profit Rule

Automatically sell a position if price rises above a threshold:

```bash
# Polymarket
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type TAKE_PROFIT --trigger-price 0.75

# HyperLiquid
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id ETH --token-id ETH \
  --rule-type TAKE_PROFIT --trigger-price 4500
```

### Create a Trailing Stop Rule

A trailing stop moves the stop price up as the price rises:

```bash
# Polymarket
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type TRAILING_STOP --trigger-price 0.45 --trailing-percent 5

# HyperLiquid
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id SOL --token-id SOL \
  --rule-type TRAILING_STOP --trigger-price 170 --trailing-percent 5
```

**Trailing stop behavior:**

- `--trailing-percent` is percent points (e.g. `5` = 5%)
- Computes `candidateStop = currentPrice * (1 - trailingPercent/100)`
- If `candidateStop` > current `triggerPrice`, updates `triggerPrice`
- `triggerPrice` never moves down
- Rule triggers when `currentPrice <= triggerPrice`

### List Rules

```bash
# All rules
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID>

# Filter by status
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID> --status ACTIVE
```

### Update a Rule

```bash
npx @vincentai/cli@latest trading-engine update-rule --key-id <KEY_ID> --rule-id <RULE_ID> --trigger-price 0.45
```

### Cancel a Rule

```bash
npx @vincentai/cli@latest trading-engine delete-rule --key-id <KEY_ID> --rule-id <RULE_ID>
```

### View Monitored Positions

```bash
npx @vincentai/cli@latest trading-engine positions --key-id <KEY_ID>
```

### View Event Log

```bash
# All events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>

# Events for specific rule
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID> --rule-id <RULE_ID>

# Paginated
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID> --limit 50 --offset 100
```

**Event types:**

- `RULE_CREATED` — Rule was created
- `RULE_TRAILING_UPDATED` — Trailing stop moved triggerPrice upward
- `RULE_EVALUATED` — Worker checked the rule against current price
- `RULE_TRIGGERED` — Trigger condition was met
- `ACTION_PENDING_APPROVAL` — Trade requires human approval, rule paused
- `ACTION_EXECUTED` — Trade executed successfully
- `ACTION_FAILED` — Trade execution failed
- `RULE_CANCELED` — Rule was manually canceled

### Rule Statuses

- `ACTIVE` — Rule is live and being monitored
- `TRIGGERED` — Condition was met, trade executed
- `PENDING_APPROVAL` — Trade requires human approval; rule paused
- `CANCELED` — Manually canceled before triggering
- `FAILED` — Triggered but trade execution failed

---

## Complete Workflow: Strategy + Trade Rules

### Polymarket Workflow

### Step 1: Place a bet with the Polymarket skill

```bash
npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456789 --side BUY --amount 10 --price 0.55
```

### Step 2: Create a strategy to monitor the thesis

```bash
npx @vincentai/cli@latest trading-engine create-strategy --key-id <KEY_ID> \
  --name "Bitcoin Bull Thesis" \
  --config '{
    "instruments": [
      { "id": "123456789", "type": "binary", "venue": "polymarket" }
    ],
    "thesis": {
      "estimate": 0.85,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "Bitcoin is likely to break $100k on ETF inflows"
    },
    "drivers": [
      {
        "name": "ETF News",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "keywords": ["bitcoin ETF inflows", "bitcoin institutional"],
          "sources": ["web_search", "newswire"]
        }
      },
      {
        "name": "Crypto Twitter",
        "weight": 1.0,
        "direction": "contextual",
        "monitoring": {
          "entities": ["@BitcoinMagazine", "@saborskycnbc"],
          "sources": ["twitter"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05 },
      "autoActions": { "stopLoss": -0.15, "takeProfit": 0.30, "trailingStop": -0.05 },
      "exit": { "thesisInvalidation": ["ETF outflows accelerate above $500M/week"] },
      "sizing": { "method": "edgeScaled", "maxPosition": 100, "maxPortfolioPct": 20, "maxTradesPerDay": 5 }
    }
  }' \
  --poll-interval 10
```

### Step 3: Set a standalone stop-loss as immediate protection

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0xabc... --token-id 123456789 \
  --rule-type STOP_LOSS --trigger-price 0.40
```

### Step 4: Activate the strategy

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Step 5: Monitor activity

```bash
# Check strategy invocations
npx @vincentai/cli@latest trading-engine invocations --key-id <KEY_ID> --strategy-id <STRATEGY_ID>

# Check trade rule events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>

# Check costs
npx @vincentai/cli@latest trading-engine costs --key-id <KEY_ID>

# Check performance
npx @vincentai/cli@latest trading-engine performance --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### HyperLiquid Workflow

### Step 1: Open a perp position with the HyperLiquid skill

```bash
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.001 --limit-px 106000 --order-type market
```

### Step 2: Set a stop-loss rule for the position

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

### Step 3: Set a take-profit rule

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type TAKE_PROFIT --trigger-price 115000
```

### Step 4: Create a strategy to monitor your thesis

```bash
npx @vincentai/cli@latest trading-engine create-strategy --key-id <KEY_ID> \
  --name "BTC Perp Momentum" \
  --config '{
    "instruments": [
      { "id": "BTC", "type": "perp", "venue": "hyperliquid" }
    ],
    "thesis": {
      "estimate": 115000,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "ETF inflows accelerating, halving supply shock imminent"
    },
    "drivers": [
      {
        "name": "ETF News",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "keywords": ["bitcoin ETF inflows", "bitcoin institutional"],
          "sources": ["web_search", "newswire"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05 },
      "autoActions": { "stopLoss": -0.10, "takeProfit": 0.25, "trailingStop": -0.05 },
      "sizing": { "method": "edgeScaled", "maxPosition": 500, "maxPortfolioPct": 20, "maxTradesPerDay": 5 }
    }
  }' \
  --poll-interval 10
```

### Step 5: Activate and monitor

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>
```

---

## Background Workers

The Trading Engine runs two independent background workers:

1. **Strategy Engine Worker** — Ticks every 30s, checks which strategy drivers are due, fetches new data, scores signals, and invokes the LLM when the escalation threshold is met. Hooks into venue WebSocket feeds (Polymarket and HyperLiquid) for real-time price trigger evaluation.
2. **Trade Rule Worker** — Monitors prices in real-time via WebSocket (with polling fallback), evaluates stop-loss/take-profit/trailing stop rules, executes trades when conditions are met. Supports both Polymarket and HyperLiquid venues.

**Circuit Breaker:** Both workers use a circuit breaker pattern. If a venue API fails 5+ consecutive times, the worker pauses and resumes after a cooldown. Check status with:

```bash
npx @vincentai/cli@latest trading-engine status --key-id <KEY_ID>
```

## Best Practices

1. **Start with `confidence: 0.5`** and let the LLM adjust — avoid overconfidence in the initial thesis
2. **Weight drivers by importance** — a driver with `weight: 3.0` has 3x the signal score contribution of `weight: 1.0`
3. **Use `edgeScaled` sizing** for adaptive position sizes based on thesis confidence and edge
4. **Set `maxPortfolioPct`** to limit exposure — even high-confidence strategies shouldn't risk the entire portfolio
5. **Set both stop-loss and take-profit** on positions for protection (via `autoActions` in the config or standalone rules)
6. **Use `thesisInvalidation` exit rules** to define explicit conditions that should trigger position exits
7. **Monitor invocation costs** — check the costs command regularly
8. **Iterate with versions** — duplicate a strategy to tweak the config without losing the original
9. **Don't set triggers too close** to current price — market noise can trigger prematurely

## Example User Prompts

When a user says:

- **"Create a strategy to monitor AI tokens"** → Create strategy with web search + Twitter drivers
- **"Set a stop-loss at 40 cents"** → Create STOP_LOSS rule
- **"What has my strategy been doing?"** → Show invocations for the strategy
- **"How is my strategy performing?"** → Show performance metrics
- **"How much has the trading engine cost me?"** → Show cost summary
- **"Pause my strategy"** → Pause the strategy
- **"Make a new version with a different thesis"** → Duplicate, then update the draft
- **"Set a 5% trailing stop"** → Create TRAILING_STOP rule

## Output Format

Strategy creation:

```json
{
  "strategyId": "strat-123",
  "name": "BTC Momentum",
  "status": "DRAFT",
  "version": 1
}
```

Rule creation:

```json
{
  "ruleId": "rule-456",
  "ruleType": "STOP_LOSS",
  "triggerPrice": 0.4,
  "status": "ACTIVE"
}
```

LLM invocation log entries:

```json
{
  "invocationId": "inv-789",
  "strategyId": "strat-123",
  "trigger": "web_search",
  "actions": ["place_trade"],
  "costUsd": 0.12,
  "createdAt": "2026-02-26T12:00:00.000Z"
}
```

## Error Handling

| Error                       | Cause                                             | Resolution                                           |
| --------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| `401 Unauthorized`          | Invalid or missing API key                        | Check that the key-id is correct; re-link if needed  |
| `403 Policy Violation`      | Trade blocked by server-side policy               | User must adjust policies at heyvincent.ai           |
| `402 Insufficient Credit`   | Not enough credit for LLM invocation              | User must add credit at heyvincent.ai                |
| `INVALID_STATUS_TRANSITION` | Strategy can't transition to requested state      | Check current status (e.g., only DRAFT can activate) |
| `CIRCUIT_BREAKER_OPEN`      | Polymarket API failures triggered circuit breaker | Wait for cooldown; check status command              |
| `429 Rate Limited`          | Too many requests or concurrent LLM invocations   | Wait and retry with backoff                          |
| `Key not found`             | API key was revoked or never created              | Re-link with a new token from the wallet owner       |

## Important Notes

- **Authorization:** All endpoints require the API key for the relevant venue (Polymarket or HyperLiquid wallet key)
- **Local only:** The API listens on `localhost:19000` — only accessible from the same VPS
- **No private keys:** All trades use the Vincent API — your private key stays secure on Vincent's servers
- **Policy enforcement:** All trades (both LLM and standalone rules) go through Vincent's policy checks
- **Idempotency:** Rules only trigger once. LLM invocations are deduplicated by driver state.

```

## File: trading-engine\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-trading-engine
name: Trading-Engine
path: ecosystem/skills/repo-fetched-agent-skills-054345/trading-engine
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Trading-Engine
Storage area for 'trading-engine' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: twitter\SKILL.md
```
---
name: Vincent - Twitter / X.com for agents
description: |
  Twitter/X.com data access for agents. Use this skill when users want to search tweets, look up
  user profiles, or retrieve recent tweets. Pay-per-call via Vincent credit system.
  Triggers on "search tweets", "twitter", "X.com", "look up user", "tweet search",
  "twitter profile", "recent tweets".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*), Bash(jq:*), Bash(bc:*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources
        - ./datasources
---

# Vincent - Twitter / X.com for agents

Use this skill to search tweets, look up user profiles, and retrieve recent tweets from X.com (Twitter). All requests are proxied through the Vincent backend, which handles authentication with the X API, enforces rate limits, tracks per-call costs, and deducts from your credit balance automatically.

**No API keys to manage.** The agent authenticates with a Vincent API key scoped to a `DATA_SOURCES` secret. Vincent handles the upstream Twitter API credentials server-side -- the agent never sees or manages Twitter API keys.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with pay-per-call pricing and human oversight**.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates a `DATA_SOURCES` secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources/` or `./datasources/`) are declared in this skill's metadata.

**The agent's API key is not a Twitter API key.** It is a scoped Bearer token for the Vincent proxy. The Vincent server authenticates with Twitter on the agent's behalf. The agent cannot access the upstream API directly or bypass the proxy's credit and rate-limit enforcement.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous access to Twitter data. The agent is expected to search tweets and look up profiles on its own. The human controls spending through credit balance and payment method management at `https://heyvincent.ai`.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The Vincent server then calls the Twitter API. The agent does not contact Twitter directly.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type DATA_SOURCES` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership, add credit, and manage payment at `https://heyvincent.ai`.
- **Credit**: Each API call costs a small amount (see Pricing below). The human adds credit via the frontend. Calls are rejected when credit runs out and no payment method is on file.
- **Revocation**: The secret owner can revoke the agent's API key at any time from the Vincent frontend.

## Pricing

| Endpoint | Cost per call |
| --- | --- |
| Search tweets | $0.01 |
| Get tweet by ID | $0.005 |
| Get user profile | $0.005 |
| Get user's tweets | $0.01 |

Credit is deducted automatically per call. The response includes `_vincent.creditRemainingUsd` so the agent can track remaining balance.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type DATA_SOURCES
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new secret.

### 2. Create a Data Sources Secret

```bash
npx @vincentai/cli@latest secret create --type DATA_SOURCES --memo "My agent data sources"
```

Returns `keyId` (use for all future commands) and `claimUrl` (share with the user).

After creating, tell the user:

> "Here is your data sources claim URL: `<claimUrl>`. Use this to claim ownership and add credit for Twitter and other data sources at https://heyvincent.ai."

**Important:** The secret must be claimed and have credit (or a payment method on file) before API calls will succeed.

### 3. Search Tweets

```bash
npx @vincentai/cli@latest twitter search --key-id <KEY_ID> --q bitcoin --max-results 10
```

Parameters:

- `--q` (required): Search query (1-512 characters)
- `--max-results` (optional): Number of results, 10-100 (default: 10)
- `--start-time` (optional): ISO 8601 datetime, earliest tweets to return
- `--end-time` (optional): ISO 8601 datetime, latest tweets to return

Returns tweet text, creation time, author ID, and public metrics (likes, retweets, replies).

### 4. Get a Specific Tweet

```bash
npx @vincentai/cli@latest twitter tweet --key-id <KEY_ID> --tweet-id <TWEET_ID>
```

### 5. Get User Profile

Look up a Twitter user by username.

```bash
npx @vincentai/cli@latest twitter user --key-id <KEY_ID> --username elonmusk
```

Returns the user's description, follower/following counts, profile image, and verified status.

### 6. Get a User's Recent Tweets

```bash
npx @vincentai/cli@latest twitter user-tweets --key-id <KEY_ID> --user-id <USER_ID> --max-results 10
```

**Note:** This command requires the user's numeric ID (from the user profile response), not the username.

## Response Metadata

Every successful response includes a `_vincent` object with:

```json
{
  "_vincent": {
    "costUsd": 0.01,
    "creditRemainingUsd": 4.99
  }
}
```

Use `creditRemainingUsd` to warn the user when credit is running low.

## Output Format

Tweet search results:

```json
{
  "data": [
    {
      "id": "123456789",
      "text": "Tweet content here",
      "created_at": "2026-02-26T12:00:00.000Z",
      "author_id": "987654321",
      "public_metrics": {
        "like_count": 42,
        "retweet_count": 10,
        "reply_count": 5
      }
    }
  ],
  "_vincent": {
    "costUsd": 0.01,
    "creditRemainingUsd": 4.99
  }
}
```

User profile responses include `description`, `public_metrics` (followers/following counts), `profile_image_url`, and `verified`.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `402 Insufficient Credit` | Credit balance is zero and no payment method on file | User must add credit at heyvincent.ai |
| `429 Rate Limited` | Exceeded 60 requests/minute | Wait and retry with backoff |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |
| `User not found` | Username doesn't exist on Twitter | Verify the username spelling |

## Rate Limits

- 60 requests per minute per API key across all data source endpoints (Twitter + Brave Search combined)
- If rate limited, you'll receive a `429` response. Wait and retry.

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Adding Credits

When your credit balance runs low, you can purchase more credits autonomously using USDC on Base via the x402 payment protocol — no human intervention required.

**Available tiers:** $1, $5, $10, $25, $50, $100

### Check Balance

```bash
npx @vincentai/cli@latest credits balance --key-id <KEY_ID>
```

### Purchase Credits via x402 (USDC on Base)

```bash
npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
```

**How it works:**

1. The CLI sends a POST request to the x402 credit endpoint
2. The server returns HTTP 402 with a dynamic USDC deposit address on Base
3. The CLI signs the payment using your agent's wallet
4. The CLI retries the request with the payment proof
5. The server verifies the payment and adds credits to your account

**Requirements:**
- An x402-compatible wallet with USDC on Base (chain ID 8453)
- Your Vincent DATA_SOURCES API key

### Purchase Credits via Card (Human)

```bash
npx @vincentai/cli@latest credits checkout --key-id <KEY_ID>
```

Returns a Stripe Checkout URL. Share this with the user to complete payment with a card.

### MCP Tools

| Tool | Description |
| --- | --- |
| `vincent_credit_balance` | Check current credit balance and top-up options |
| `vincent_add_credits` | Get x402 payment instructions for purchasing credits |

### Auto-Replenish Pattern

For long-running agents, check your balance before expensive operations and top up when low:

```bash
BALANCE=$(npx @vincentai/cli@latest credits balance --key-id <KEY_ID> --json | jq -r '.balance')
if (( $(echo "$BALANCE < 2.00" | bc -l) )); then
  npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
fi
```

## Important Notes

- A single `DATA_SOURCES` API key works for **all** data sources (Twitter, Brave Search, etc.). You do not need a separate key per data source.
- Always share the claim URL with the user after creating a secret.
- If a call is rejected with a credit error, tell the user to add credit at `https://heyvincent.ai`.
- The Twitter search endpoint only returns tweets from the last 7 days (X API v2 limitation for recent search).

```

## File: twitter\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-twitter
name: Twitter
path: ecosystem/skills/repo-fetched-agent-skills-054345/twitter
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Twitter
Storage area for 'twitter' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: wallet\SKILL.md
```
---
name: Vincent - A wallet for agents
description: |
  The agent's wallet for EVM chain transactions and raw signing. Use this skill when users want to
  create a wallet, transfer tokens, swap on DEXs, interact with smart contracts, or sign messages.
  Triggers on "wallet", "create wallet", "transfer ETH", "swap tokens", "send transaction",
  "check balance", "EVM wallet", "raw signer", "sign message".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - A wallet for agents

Use this skill to safely create a wallet the agent can use for transfers, swaps, and any EVM chain transaction without ever exposing private keys to the agent. Create a wallet, set spending policies, and your agent can transfer tokens, do swaps, and interact with smart contracts within the boundaries you define.

**The agent never sees the private key.** All transactions are executed server-side through a ZeroDev smart account. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies. The private key never leaves the Vincent server.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with human oversight via server-side controls**. Understanding this model is important:

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure. The CLI stores the returned API key automatically during wallet creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet/` or `./agentwallet/`) are declared in this skill's metadata.

**The agent's API key is not a private key.** It is a scoped Bearer token that can only execute transactions within the policies set by the wallet owner. The Vincent server enforces all policies server-side — the agent cannot bypass them regardless of what it sends. If a transaction violates a policy, the server rejects it. If a transaction requires approval, the server holds it and notifies the wallet owner via Telegram for out-of-band human approval.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous wallet capabilities. The agent is expected to invoke wallet actions (transfers, swaps, contract calls) on its own, within the boundaries the human operator defines. The human controls what the agent can do through policies (spending limits, address allowlists, token allowlists, function allowlists, approval thresholds) — not by gating individual invocations. The stored key is scoped and policy-constrained — even if another process reads it, it can only perform actions the wallet owner's policies allow, and the owner can revoke it instantly.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted. The agent does not read, collect, or transmit any data beyond what is needed for wallet operations.

**Vincent is open source and audited.** The server-side code that enforces policies, manages private keys, and executes transactions is publicly auditable at [github.com/HeyVincent-ai/Vincent](https://github.com/HeyVincent-ai/Vincent). The Vincent backend undergoes continuous security audits covering key management, policy enforcement, transaction signing, and API authentication. You can verify how policy enforcement works, how private keys are stored, how the scoped API key is validated, and how revocation is handled — nothing is opaque. If you want to self-host Vincent rather than trust the hosted service, the repository includes deployment instructions.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership and configure policies.
- **Revocation**: The wallet owner can revoke the agent's API key at any time from `https://heyvincent.ai`. Revoked keys are rejected immediately by the server.
- **Re-linking**: If the agent loses its API key, the wallet owner generates a one-time re-link token and the agent exchanges it for a new key via `secret relink`.
- **Rotation**: The wallet owner can revoke the current key and issue a re-link token to rotate credentials at any time.

## Which Secret Type to Use

| Type         | Use Case                                  | Network                 | Gas              |
| ------------ | ----------------------------------------- | ----------------------- | ---------------- |
| `EVM_WALLET` | Transfers, swaps, DeFi, contract calls    | Any EVM chain           | Sponsored (free) |
| `RAW_SIGNER` | Raw message signing for special protocols | Any (Ethereum + Solana) | You pay          |

**Choose `EVM_WALLET`** (default) for:

- Sending ETH or tokens
- Swapping tokens on DEXs
- Interacting with smart contracts
- Any standard EVM transaction

**Choose `RAW_SIGNER`** only when you need:

- Raw ECDSA/Ed25519 signatures for protocols that don't work with smart accounts
- To sign transaction hashes you'll broadcast yourself
- Solana signatures

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type EVM_WALLET
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new wallet.

### 2. Create a Wallet

```bash
npx @vincentai/cli@latest secret create --type EVM_WALLET --memo "My agent wallet" --chain-id 84532
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `address`.

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

### 3. Get Wallet Address

```bash
npx @vincentai/cli@latest wallet address --key-id <KEY_ID>
```

### 4. Check Balances

```bash
# All balances across all supported chains
npx @vincentai/cli@latest wallet balances --key-id <KEY_ID>

# Filter to specific chains
npx @vincentai/cli@latest wallet balances --key-id <KEY_ID> --chain-ids 1,137,42161
```

Returns all ERC-20 tokens and native balances with symbols, decimals, logos, and USD values.

### 5. Transfer ETH or Tokens

```bash
# Transfer native ETH
npx @vincentai/cli@latest wallet transfer --key-id <KEY_ID> --to 0xRecipient --amount 0.01

# Transfer ERC-20 token
npx @vincentai/cli@latest wallet transfer --key-id <KEY_ID> --to 0xRecipient --amount 100 --token 0xTokenAddress
```

If the transaction violates a policy, the server returns an error explaining which policy was triggered. If the transaction requires human approval (based on the approval threshold policy), the server returns `status: "pending_approval"` and the wallet owner receives a Telegram notification to approve or deny.

### 6. Swap Tokens

Swap one token for another using DEX liquidity (powered by 0x).

```bash
# Preview a swap (no execution, just pricing)
npx @vincentai/cli@latest wallet swap preview --key-id <KEY_ID> \
  --sell-token 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE \
  --buy-token 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 \
  --sell-amount 0.1 --chain-id 1

# Execute a swap
npx @vincentai/cli@latest wallet swap execute --key-id <KEY_ID> \
  --sell-token 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE \
  --buy-token 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 \
  --sell-amount 0.1 --chain-id 1 --slippage 100
```

- Use `0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE` for native ETH.
- `--sell-amount`: Human-readable amount (e.g. `0.1` for 0.1 ETH).
- `--chain-id`: 1 = Ethereum, 137 = Polygon, 42161 = Arbitrum, 10 = Optimism, 8453 = Base, etc.
- `--slippage`: Slippage tolerance in basis points (100 = 1%). Defaults to 100. Execute only.

The preview returns expected buy amount, route info, and fees without executing. Execute performs the actual swap, handling ERC20 approvals automatically.

### 7. Send Arbitrary Transaction

Interact with any smart contract by sending custom calldata.

```bash
npx @vincentai/cli@latest wallet send-tx --key-id <KEY_ID> --to 0xContract --data 0xCalldata --value 0
```

### 8. Transfer Between Your Secrets

Transfer funds between Vincent secrets you own (e.g., from one EVM wallet to another, or to a Polymarket wallet). Vincent verifies you own both secrets and handles any token conversion or cross-chain bridging automatically.

```bash
# Preview (get quote without executing)
npx @vincentai/cli@latest wallet transfer-between preview --key-id <KEY_ID> \
  --to-secret-id <DEST_SECRET_ID> --from-chain 8453 --to-chain 8453 \
  --token-in ETH --amount 0.1 --token-out ETH

# Execute
npx @vincentai/cli@latest wallet transfer-between execute --key-id <KEY_ID> \
  --to-secret-id <DEST_SECRET_ID> --from-chain 8453 --to-chain 8453 \
  --token-in ETH --amount 0.1 --token-out ETH --slippage 100

# Check cross-chain transfer status
npx @vincentai/cli@latest wallet transfer-between status --key-id <KEY_ID> --relay-id <RELAY_REQUEST_ID>
```

**Behavior:**

- **Same token + same chain**: Executes as a direct transfer (gas sponsored).
- **Different token or chain**: Uses a relay service for atomic swap + bridge.
- The destination secret can be an `EVM_WALLET` or `POLYMARKET_WALLET`.
- The server verifies you own both the source and destination secrets — transfers to secrets you don't own are rejected.
- Transfers are subject to the same server-side policies as regular transfers (spending limits, approval thresholds, etc.).

## Output Format

CLI commands return JSON to stdout. Successful responses include the relevant data:

```json
{
  "address": "0x...",
  "balances": [
    {
      "token": "ETH",
      "balance": "0.5",
      "usdValue": "1250.00"
    }
  ]
}
```

Transaction commands return:

```json
{
  "transactionHash": "0x...",
  "status": "confirmed"
}
```

For transactions requiring human approval:

```json
{
  "status": "pending_approval",
  "message": "Transaction requires owner approval via Telegram"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Policy Violation` | Transaction blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `400 Insufficient Balance` | Not enough tokens for the transfer | Check balances before transferring |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `pending_approval` | Transaction exceeds approval threshold | User will receive Telegram notification to approve/deny |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

If a transaction is rejected, inform the user to check their policy settings at `https://heyvincent.ai`.

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies via the claim URL at `https://heyvincent.ai`. All policies are enforced server-side by the Vincent API — the agent cannot bypass or modify them. If a transaction violates a policy, the API rejects it. If a transaction triggers an approval threshold, the API holds it and sends the wallet owner a Telegram notification for out-of-band human approval. The policy enforcement logic is open source and auditable at [github.com/HeyVincent-ai/Vincent](https://github.com/HeyVincent-ai/Vincent).

| Policy                      | What it does                                                        |
| --------------------------- | ------------------------------------------------------------------- |
| **Address allowlist**       | Only allow transfers/calls to specific addresses                    |
| **Token allowlist**         | Only allow transfers of specific ERC-20 tokens                      |
| **Function allowlist**      | Only allow calling specific contract functions (by 4-byte selector) |
| **Spending limit (per tx)** | Max USD value per transaction                                       |
| **Spending limit (daily)**  | Max USD value per rolling 24 hours                                  |
| **Spending limit (weekly)** | Max USD value per rolling 7 days                                    |
| **Require approval**        | Every transaction needs human approval via Telegram                 |
| **Approval threshold**      | Transactions above a USD amount need human approval via Telegram    |

Before the wallet is claimed, the agent can operate without policy restrictions. This is by design: agent-first onboarding allows the agent to begin accumulating and managing funds immediately. Once the human operator claims the wallet via the claim URL, they can add any combination of policies to constrain the agent's behavior. The wallet owner can also revoke the agent's API key entirely at any time.

## Re-linking (Recovering API Access)

If the agent loses its API key, the wallet owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

**How it works:**

1. The user generates a re-link token from the wallet detail page at `https://heyvincent.ai`
2. The user gives the token to the agent (e.g. by pasting it in chat)
3. The agent runs the relink command:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Use this `keyId` for all subsequent commands.

**Important:** Re-link tokens are one-time use and expire after 10 minutes.

## Important Notes

- **No gas needed.** A paymaster is fully set up — all transaction gas fees are sponsored automatically. The wallet does not need ETH for gas.
- **Never try to access raw secret values.** The private key stays server-side — that's the whole point.
- Always share the claim URL with the user after creating a wallet.
- If a transaction is rejected, it may be blocked by a server-side policy. Tell the user to check their policy settings at `https://heyvincent.ai`.
- If a transaction requires approval, it will return `status: "pending_approval"`. The wallet owner will receive a Telegram notification to approve or deny.

---

## Raw Signer (Advanced)

For raw ECDSA/Ed25519 signing when smart accounts won't work.

### Create a Raw Signer

```bash
npx @vincentai/cli@latest secret create --type RAW_SIGNER --memo "My raw signer"
```

Response includes both Ethereum (secp256k1) and Solana (ed25519) addresses derived from the same seed.

### Get Addresses

```bash
npx @vincentai/cli@latest raw-signer addresses --key-id <KEY_ID>
```

Returns `ethAddress` and `solanaAddress`.

### Sign a Message

```bash
npx @vincentai/cli@latest raw-signer sign --key-id <KEY_ID> --message 0x<hex-encoded-bytes> --curve ethereum
```

- `--message`: Hex-encoded bytes to sign (must start with `0x`)
- `--curve`: `ethereum` for secp256k1 ECDSA, `solana` for ed25519

Returns a hex-encoded signature. For Ethereum, this is `r || s || v` (65 bytes). For Solana, it's a 64-byte ed25519 signature.

```

## File: wallet\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agent-skills-054345-wallet
name: Wallet
path: ecosystem/skills/repo-fetched-agent-skills-054345/wallet
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Wallet
Storage area for 'wallet' domain.
> Auto-generated identity tag by OMA v2.1.

```

