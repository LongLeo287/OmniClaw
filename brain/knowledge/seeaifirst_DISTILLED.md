---
id: seeaifirst
type: knowledge
owner: OA_Triage
---
# seeaifirst
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "seeaifirst",
  "devDependencies": {
    "canvas": "^3.2.1"
  }
}

```

### File: README.md
```md
# 🧠 See AI First

**The Opinionated AI Stack Guide — with receipts.**

Curated directory of 66 AI developer tools across 13 categories, with evidence-first sourcing.

🌐 **Live:** [seeaifirst.com](https://seeaifirst.com)

---

## Why This Exists

There are hundreds of "awesome AI" lists. Most are link dumps with no opinion.

See AI First is different:

- **Curated, not scraped.** Every tool is manually evaluated against 5 criteria before inclusion. 100+ tools evaluated, 66 selected.
- **Evidence-first.** Each card includes sources, verified dates, and verification methods.
- **Opinionated trade-offs.** Every tool has `whenToUse` and `whenNotToUse` — we tell you when a tool is *not* the right choice.
- **Structured for machines.** Schema-frozen data with stable IDs, JSON-LD structured data — built to be referenced by AI agents, not just humans.

## Features

- 🗂️ **13 categories** across 5 layers: Foundation → Coordination → Capability → Application → Trends
- 🔍 **Search** across names, descriptions, and details (Ctrl+K)
- 🔗 **Deep linking** — every tool has a permanent URL via path-based routing
- ⚖️ **Compare Mode** — side-by-side tool comparisons with preset and custom selections
- 🎯 **Tool Picker** — interactive selection for building your AI stack
- 📊 **Enriched metadata** — pricing, deployment, difficulty, compatibility, use cases
- 🌗 **Dark/Light theme**
- 📱 **Mobile responsive**
- ⚡ **Zero backend** — static HTML + JSON on CDN, loads instantly

## Usage

One effective way to use See AI First is to **ask your AI agent to look things up for you.**

Instead of browsing manually, you can ask your AI assistant (Claude, ChatGPT, Gemini, Grok, or any agent with web access) something like:

**Locate a tool in the AI ecosystem:**
- *"Where does MCP fit in the AI stack? Check seeaifirst.com"*
- *"I found github.com/langchain-ai/langchain — where does this sit in the AI ecosystem? Look it up on seeaifirst.com"*
- *"Someone recommended Qdrant. What category is it in and what are the alternatives? Check seeaifirst.com"*

**Build your stack:**
- *"I'm building a RAG pipeline. What tools does seeaifirst.com recommend?"*
- *"Compare LangGraph vs CrewAI on seeaifirst.com"*

**Evaluate before adopting:**
- *"I'm considering pgvector for vector search. What does seeaifirst.com say about when to use it and when not to?"*
- *"What's the trade-off between LangSmith and Langfuse for observability? Check seeaifirst.com"*

**Validate social media recommendations:**
- *"I saw a post claiming FastCode is cheaper than Claude Code and Cursor. Is it on seeaifirst.com? Where does it fit in the coding agents category?"*
- *"Someone shared a new AI framework on Twitter. Check if seeaifirst.com covers it and what the trade-offs are"*

The site is structured so web-enabled AI agents can read and summarize it more effectively — 66 tools mapped across 13 categories with opinionated trade-offs, so your agent gets context, not just links.

You can also browse directly at [seeaifirst.com](https://seeaifirst.com) — use Search (Ctrl+K), Compare Mode, or Tool Picker to explore.

## Quick Start

```bash
git clone https://github.com/BARONFANTHE/seeaifirst.git
cd seeaifirst
python -m http.server 8000
# Open http://localhost:8000
```

> The site uses `fetch()` to load data, so a local server is required (opening `index.html` directly will fail due to CORS).

Alternative: `npx serve .`

## Project Structure

```
seeaifirst/
├── index.html          # UI + CSS + JS (single file)
├── data.json           # 66 tools, 13 sections, 5 layers
├── og-image.png        # Social preview image
├── sitemap.xml         # SEO sitemap
├── robots.txt          # SEO robots
├── package.json        # npm config (for validator)
├── scripts/
│   └── validate.js     # Data validation (8 checks)
└── .github/
    └── ISSUE_TEMPLATE/
        └── suggest-tool.yml  # Community tool suggestions
```

## Data

All tool data lives in `data.json` (English) and `data.vi.json` (Vietnamese). Each tool card includes:

- Basic info: name, description, sources
- Enrichment: pricing, deployment model, difficulty level
- Opinions: when to use, when not to use, compatible tools
- Verification: verified date, verification method

Schema is frozen at v1.0.0. See [CONTRIBUTING.md](CONTRIBUTING.md) for data format details.

## Selection Criteria

Not every tool belongs here. Each suggestion is evaluated against 5 criteria:

| Criteria | Minimum Threshold |
|----------|-------------------|
| **GitHub Stars** | Usually >5K ⭐ — exceptions allowed for innovative tools with strong rationale + evidence |
| **Relevance** | Must be part of the AI developer ecosystem |
| **Maturity** | Has documentation, active development, community |
| **Uniqueness** | Does not duplicate an existing card's functionality |
| **Category Fit** | Fits within existing 13 sections (new sections require strong justification) |

100+ tools evaluated. 66 selected. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to suggest a tool.

## Contributing

We welcome contributions! The main ways to help:

- **Suggest a tool** → [Open an issue](https://github.com/BARONFANTHE/seeaifirst/issues/new?template=suggest-tool.yml)
- **Report a bug** → [Open an issue](https://github.com/BARONFANTHE/seeaifirst/issues/new)
- **Improve data** → Submit a PR (see [CONTRIBUTING.md](CONTRIBUTING.md))

## Tech Stack

- **Frontend:** Vanilla HTML + CSS + JS (single file, no framework)
- **Data:** JSON (schema v1.0.0 frozen)
- **Hosting:** Vercel (auto-deploy from `main`)
- **SEO:** JSON-LD structured data, canonical domain, sitemap + robots.txt

## License

[MIT](LICENSE)

---

*Vietnamese descriptions available on the live site.*

*Data verified as of February 2026. Found something outdated? [Open an issue](https://github.com/BARONFANTHE/seeaifirst/issues/new).*

```

### File: CONTRIBUTING.md
```md
# Contributing to See AI First

Thank you for your interest in contributing! See AI First is a curated directory of AI developer tools, and community input helps keep it accurate and comprehensive.

## Ways to Contribute

### 1. Suggest a Tool

The easiest way to contribute — no coding required.

→ [Open a "Suggest a Tool" issue](https://github.com/BARONFANTHE/seeaifirst/issues/new?template=suggest-tool.yml)

We'll review your suggestion against our evaluation criteria and add it if it qualifies.

### 2. Report a Bug

Found a broken link, incorrect data, or UI issue?

→ [Open a bug report](https://github.com/BARONFANTHE/seeaifirst/issues/new)

Please include: what you expected, what happened, and browser/device info if relevant.

### 3. Improve Data via Pull Request

For experienced contributors who want to directly update tool data.

**Before submitting a PR:**

1. Fork the repo and create a branch from `main`
2. Edit `data.json` only — do not modify `index.html` or other files
3. One tool per PR — keep changes small and reviewable
4. Run the validator: `npm install && node scripts/validate.js` (must show 8/8 PASS)
5. Test locally: `python -m http.server 8000` then open `http://localhost:8000`
6. Submit your PR with a clear description of what changed and why

## Tool Evaluation Criteria

Not every tool belongs here. We evaluate suggestions against 5 criteria:

| Criteria | Minimum Threshold |
|----------|-------------------|
| **GitHub Stars** | Usually >5K ⭐ — exceptions allowed for innovative tools with strong rationale + evidence |
| **Relevance** | Must be part of the AI developer ecosystem |
| **Maturity** | Has documentation, active development, community |
| **Uniqueness** | Does not duplicate an existing card's functionality |
| **Category Fit** | Fits within existing 13 sections (new sections require strong justification) |

## Data Format

Each tool is a card in `data.json`. Here's an example:

```json
{
  "name": "Tool Name",
  "slug": "tool-name",
  "desc": "Short description (1 line)",
  "added_date": "2026-03-01",
  "detail": "Detailed description (2-7 lines)",
  "sources": [
    { "title": "GitHub", "url": "https://github.com/org/repo" },
    { "title": "Website", "url": "https://example.com" }
  ],
  "pricing": "free",
  "deployment": "self-hosted",
  "difficulty": "intermediate",
  "whenToUse": ["phrase 1", "phrase 2"],
  "whenNotToUse": ["phrase 1", "phrase 2"],
  "compatibleWith": ["slug-1", "slug-2"],
  "useCases": ["use-case-tag"],
  "languages": ["python", "js"],
  "github_stars": 15000,
  "license": "MIT",
  "verified_at": "2026-03-01",
  "verification_source": "docs"
}
```

**Key rules:**

- `slug`: lowercase, kebab-case, immutable once assigned. If you think a slug is wrong, open an issue — do not rename existing slugs in a PR.
- `pricing`: one of `free`, `freemium`, `paid`, `open-core`
- `deployment`: one of `cloud`, `self-hosted`, `local`, `hybrid`
- `difficulty`: one of `beginner`, `intermediate`, `advanced`
- `sources`: use key `"title"` (not `"label"`)
- `compatibleWith`: use canonical slugs from existing cards
- `github_stars` / `license`: only set when there is a clearly primary official GitHub repo. If unsure, omit (set `null` or leave out).

## What We Don't Accept

- Tools with no GitHub presence or documentation
- Duplicate functionality with an existing card
- Spam or self-promotional submissions without substance
- Changes to `index.html` or project configuration files

## Response Time

This is a solo-maintained project. Please allow a few days for responses. All submissions are appreciated, even if they don't result in an addition.

## Code of Conduct

Be respectful. No spam, harassment, or discriminatory content. Contributions should be constructive and made in good faith.

---

*Questions? Open an issue and we'll help you out.*

```

### File: data.json
```json
{
  "meta": {
    "title": "See AI First — The Opinionated AI Stack Guide",
    "subtitle": "Phân tầng từ Nền tảng → Ứng dụng → Xu hướng",
    "lastUpdated": "2026-02-09",
    "updatedBy": "Claude Code",
    "version": "7.0",
    "schema_version": "1.0.0",
    "updated_at": "2026-03-18T09:50:33.448Z",
    "tools_count": 66,
    "sections_count": 13
  },
  "layers": [
    {
      "level": 1,
      "id": "foundation",
      "name": "Nền Tảng",
      "nameEn": "Foundation",
      "icon": "🔌",
      "desc": "Protocols chuẩn hóa giao tiếp — mọi thứ khác xây trên lớp này",
      "color": "indigo",
      "sectionIds": [
        "protocols",
        "vector-databases"
      ]
    },
    {
      "level": 2,
      "id": "infrastructure",
      "name": "Hạ Tầng",
      "nameEn": "Infrastructure",
      "icon": "🏗️",
      "desc": "Frameworks xây agents + Platforms chạy chúng",
      "color": "purple",
      "sectionIds": [
        "frameworks",
        "platforms",
        "infrastructure",
        "rag-systems"
      ]
    },
    {
      "level": 3,
      "id": "intelligence",
      "name": "Trí Tuệ",
      "nameEn": "Intelligence",
      "icon": "🧠",
      "desc": "Memory giữ context · Skills mở rộng khả năng · Orchestration phối hợp",
      "color": "cyan",
      "sectionIds": [
        "memory",
        "skills",
        "orchestration",
        "observability",
        "security"
      ]
    },
    {
      "level": 4,
      "id": "applications",
      "name": "Ứng Dụng",
      "nameEn": "Applications",
      "icon": "🛠️",
      "desc": "Công cụ AI coding và quy trình tạo ứng dụng thực tế",
      "color": "sky",
      "sectionIds": [
        "coding-agents"
      ]
    },
    {
      "level": 5,
      "id": "landscape",
      "name": "Xu Hướng",
      "nameEn": "Landscape",
      "icon": "🌍",
      "desc": "Những xu hướng đang định hình tương lai AI 2026",
      "color": "green",
      "sectionIds": [
        "trends"
      ]
    }
  ],
  "sections": [
    {
      "id": "protocols",
      "title": "Protocols — Standardized Communication Layer",
      "color": "indigo",
      "badge": "🔥 Foundation",
      "gridCols": 2,
      "cards": [
        {
          "name": "MCP — Model Context Protocol",
          "slug": "mcp",
          "icon": "🔌",
          "mono": true,
          "hot": true,
          "desc": "<strong>Anthropic</strong>'s connection standard — lets AI talk to any tool, database, or API through one unified protocol. Often called 'USB-C for AI'.",
          "added_date": "2026-02-03",
          "detail": "<strong>Agent ↔ Tool</strong> communication · The \"USB-C for AI\" · Adopted by OpenAI, Google DeepMind, Cursor, Replit, Sourcegraph<br><strong>MCP Apps</strong> (Jan 2026): New extension — tools return interactive UI (dashboards, forms) directly in conversation<br><strong>Skills over MCP</strong>: Experimental — skill discovery & distribution via MCP primitives",
          "tags": [
            "Python SDK 21k⭐",
            "TS SDK 11k⭐",
            "C# (Microsoft)",
            "Kotlin (JetBrains)",
            "Swift",
            "Linux Foundation"
          ],
          "sources": [
            {
              "title": "Anthropic — Introducing MCP",
              "url": "https://www.anthropic.com/news/model-context-protocol"
            },
            {
              "title": "MCP Specification",
              "url": "https://modelcontextprotocol.io/specification/2025-11-25"
            },
            {
              "title": "Wikipedia — Model Context Protocol",
              "url": "https://en.wikipedia.org/wiki/Model_Context_Protocol"
            },
            {
              "title": "MCP GitHub",
              "url": "https://github.com/modelcontextprotocol"
            }
          ],
          "pricing": "free",
          "deployment": "hybrid",
          "difficulty": "intermediate",
          "whenToUse": [
            "tool integration for LLMs",
            "connecting AI apps to external data sources",
            "building standardized AI plugins",
            "cross-platform tool sharing"
          ],
          "whenNotToUse": [
            "agent-to-agent communication (use A2A)",
            "simple REST API calls without AI context"
          ],
          "compatibleWith": [
            "a2a",
            "claude-code",
            "claude-ai",
            "chatgpt",
            "cursor",
            "windsurf",
            "openai-agents-sdk",
            "google-adk",
            "dify"
          ],
          "useCases": [
            "tool-integration",
            "data-access",
            "ai-plugin-system",
            "ide-extension"
          ],
          "languages": [
            "python",
            "js",
            "java",
            "csharp",
            "go",
            "rust",
            "swift",
            "ruby"
          ],
          "verified_at": "2026-02-11",
          "verification_source": "docs",
          "github_stars": 6400,
          "license": "Apache-2.0"
        },
        {
          "name": "A2A — Agent2Agent Protocol",
          "slug": "a2a",
          "icon": "🤝",
          "mono": true,
          "hot": true,
          "desc": "<strong>Google</strong>'s protocol — lets AI agents communicate and collaborate with each other, regardless of their underlying framework.",
          "added_date": "2026-02-03",
          "detail": "<strong>Agent ↔ Agent</strong> communication · Complements MCP (MCP = tools, A2A = agents)<br><strong>Agent Cards</strong>: JSON-based capability descriptors for agent discovery<br><strong>v0.3</strong> (Jul 2025): gRPC support, security cards, expanded Python SDK<br>150+ organizations support · Linux Foundation hosted",
          "tags": [
            "Google ADK native",
            "HTTP/SSE/JSON-RPC",
            "LangGraph",
            "CrewAI",
            "Semantic Kernel"
          ],
          "note": "💡 Dùng <strong>MCP cho tools</strong>, <strong>A2A cho agents</strong> — 2 protocol bổ sung nhau, không thay thế!",
          "sources": [
            {
              "title": "Google — Announcing A2A",
              "url": "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
            },
            {
              "title": "A2A GitHub",
              "url": "https://github.com/google/A2A"
            },
            {
              "title": "A2A Protocol Documentation",
              "url": "https://google.github.io/A2A/"
            }
          ],
          "pricing": "free",
          "deployment": "hybrid",
          "difficulty": "intermediate",
          "whenToUse": [
            "agent-to-agent communication",
            "cross-framework agent collaboration",
            "enterprise multi-agent workflows",
            "multi-vendor agent interop"
          ],
          "whenNotToUse": [
            "tool integration for LLMs (use MCP)",
            "single-agent applications"
          ],
          "compatibleWith": [
            "mcp",
            "google-adk",
            "langgraph",
            "crewai",
            "autogen",
            "pydantic-ai"
          ],
          "useCases": [
            "multi-agent-systems",
            "enterprise-workflows",
            "agent-interop",
            "cross-platform-agents"
          ],
          "languages": [
            "python",
            "js",
            "java",
            "go",
            "rust",
            "csharp"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 22864,
          "license": "Apache-2.0"
        }
      ]
    },
    {
      "id": "frameworks",
      "title": "Agent Frameworks — Building AI Agents",
      "color": "rose",
      "gridCols": 4,
      "cards": [
        {
          "name": "LangGraph",
          "slug": "langgraph",
          "icon": "🦜",
          "mono": true,
          "desc": "Stateful agent orchestration framework from the LangChain ecosystem. The most widely adopted today.",
          "added_date": "2026-02-03",
          "tags": [
            "27.5K⭐",
            "4.2M downloads/mo"
          ],
          "detail": "Open-source framework by LangChain for building agents as stateful graphs. Supports durable execution — agents auto-recover from failures, human-in-the-loop — humans can intervene at any point, and cross-session long-term memory. Used in production by Klarna, Replit, Uber, LinkedIn, Elastic. Includes LangGraph Studio for visual debugging and LangGraph Platform for deployment.",
          "sources": [
            {
              "title": "LangGraph Official",
              "url": "https://www.langchain.com/langgraph"
            },
            {
              "title": "LangGraph GitHub",
              "url": "https://github.com/langchain-ai/langgraph"
            },
            {
              "title": "LangGraph Docs",
              "url": "https://docs.langchain.com/oss/python/langgraph/overview"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "intermediate",
          "whenToUse": [
            "stateful multi-step agent workflows",
            "complex control flow with branching and loops",
            "human-in-the-loop agent approval",
            "long-running durable agent execution"
          ],
          "whenNotToUse": [
            "simple single-call LLM tasks",
            "no need for state persistence between steps",
            "team unfamiliar with graph-based programming"
          ],
          "compatibleWith": [
            "langfuse",
            "mcp",
            "ollama",
            "litellm",
            "pgvector",
            "chroma",
            "qdrant",
            "milvus"
          ],
          "useCases": [
            "agent-orchestration",
            "multi-agent-systems",
            "rag-pipeline",
            "workflow-automation"
          ],
          "languages": [
            "python",
            "js"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 27670,
          "license": "MIT"
        },
        {
          "name": "CrewAI",
          "slug": "crewai",
          "icon": "👥",
          "mono": true,
          "desc": "Build role-based AI agent teams with minimal code. Each agent has a role, they coordinate automatically.",
          "added_date": "2026-02-03",
          "tags": [
            "Multi-agent crews",
            "Free core"
          ],
          "detail": "Framework for building agent teams using a role-based model — each agent plays a specific role (researcher, writer, reviewer...) and collaborates like a real team. Supports sequential, hierarchical, and consensual processes. Ships with 700+ built-in tools, LangChain compatible. CrewAI Enterprise provides deployment, monitoring, and an agent marketplace.",
          "sources": [
            {
              "title": "CrewAI Official",
              "url": "https://www.crewai.com/"
            },
            {
              "title": "CrewAI GitHub",
              "url": "https://github.com/crewAIInc/crewAI"
            },
            {
              "title": "CrewAI Docs",
              "url": "https://docs.crewai.com/"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "intermediate",
          "whenToUse": [
            "multi-agent orchestration",
            "role-based AI teams",
            "autonomous agent collaboration",
            "complex workflow automation"
          ],
          "whenNotToUse": [
            "simple single-agent tasks",
            "non-Python stack",
            "real-time low-latency requirements"
          ],
          "compatibleWith": [
            "langfuse",
            "ollama",
            "dify"
          ],
          "useCases": [
            "multi-agent",
            "workflow-automation",
            "agent-orchestration",
            "enterprise-automation"
          ],
          "languages": [
            "python"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 47347,
          "license": "MIT"
        },
        {
          "name": "AutoGen",
          "slug": "autogen",
          "icon": "🔷",
          "mono": true,
          "desc": "Microsoft's framework for multi-agent conversations. Flexible architecture, easy to extend.",
          "added_date": "2026-02-03",
          "tags": [
            "Microsoft",
            "Flexible arch"
          ],
          "detail": "Multi-agent framework by Microsoft Research that lets multiple LLM agents converse to solve complex tasks. Supports human-in-the-loop, automatic code execution, and group chat patterns. AutoGen 0.4 (2025) is a complete rewrite with event-driven architecture, supporting distributed agents and pluggable components.",
          "sources": [
            {
              "title": "AutoGen GitHub",
              "url": "https://github.com/microsoft/autogen"
            },
            {
              "title": "AutoGen Docs",
              "url": "https://microsoft.github.io/autogen/"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "advanced",
          "whenToUse": [
            "multi-agent conversation systems",
            "research prototyping",
            "human-in-the-loop workflows",
            "complex agent collaboration"
          ],
          "whenNotToUse": [
            "greenfield projects (consider Microsoft Agent Framework)",
            "simple single-agent tasks",
            "TypeScript-only stack"
          ],
          "compatibleWith": [
            "mcp",
            "a2a",
            "ollama"
          ],
          "useCases": [
            "multi-agent",
            "research",
            "conversation-ai",
            "workflow-automation"
          ],
          "languages": [
            "python",
            "csharp"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 56296,
          "license": "MIT"
        },
        {
          "name": "OpenAI Agents SDK",
          "slug": "openai-agents-sdk",
          "icon": "🟢",
          "mono": true,
          "desc": "OpenAI's lightweight Python SDK — build agents fast with built-in safety guardrails.",
          "added_date": "2026-02-03",
          "tags": [
            "20K⭐",
            "100+ LLMs"
          ],
          "detail": "OpenAI's official SDK for building agents — lightweight, production-ready. Features built-in Guardrails (input/output validation), Handoffs (task transfer between agents), and Tracing (debug + monitor). Native MCP support since v0.0.7. Minimalist design: few abstractions, easy to customize, easy to debug.",
          "sources": [
            {
           
... [TRUNCATED]
```

### File: data.vi.json
```json
{
  "meta": {
    "title": "See AI First — The Opinionated AI Stack Guide",
    "subtitle": "Phân tầng từ Nền tảng → Ứng dụng → Xu hướng",
    "lastUpdated": "2026-02-09",
    "updatedBy": "Claude Code",
    "version": "7.0",
    "schema_version": "1.0.0",
    "updated_at": "2026-03-18T09:50:38.583Z",
    "tools_count": 66,
    "sections_count": 13
  },
  "layers": [
    {
      "level": 1,
      "id": "foundation",
      "name": "Nền Tảng",
      "nameEn": "Foundation",
      "icon": "🔌",
      "desc": "Protocols chuẩn hóa giao tiếp — mọi thứ khác xây trên lớp này",
      "color": "indigo",
      "sectionIds": [
        "protocols",
        "vector-databases"
      ]
    },
    {
      "level": 2,
      "id": "infrastructure",
      "name": "Hạ Tầng",
      "nameEn": "Infrastructure",
      "icon": "🏗️",
      "desc": "Frameworks xây agents + Platforms chạy chúng",
      "color": "purple",
      "sectionIds": [
        "frameworks",
        "platforms",
        "infrastructure",
        "rag-systems"
      ]
    },
    {
      "level": 3,
      "id": "intelligence",
      "name": "Trí Tuệ",
      "nameEn": "Intelligence",
      "icon": "🧠",
      "desc": "Memory giữ context · Skills mở rộng khả năng · Orchestration phối hợp",
      "color": "cyan",
      "sectionIds": [
        "memory",
        "skills",
        "orchestration",
        "observability",
        "security"
      ]
    },
    {
      "level": 4,
      "id": "applications",
      "name": "Ứng Dụng",
      "nameEn": "Applications",
      "icon": "🛠️",
      "desc": "Công cụ AI coding và quy trình tạo ứng dụng thực tế",
      "color": "sky",
      "sectionIds": [
        "coding-agents"
      ]
    },
    {
      "level": 5,
      "id": "landscape",
      "name": "Xu Hướng",
      "nameEn": "Landscape",
      "icon": "🌍",
      "desc": "Những xu hướng đang định hình tương lai AI 2026",
      "color": "green",
      "sectionIds": [
        "trends"
      ]
    }
  ],
  "sections": [
    {
      "id": "protocols",
      "title": "Protocols — Nền tảng giao tiếp chuẩn",
      "color": "indigo",
      "badge": "🔥 Foundation",
      "gridCols": 2,
      "cards": [
        {
          "name": "MCP — Model Context Protocol",
          "slug": "mcp",
          "icon": "🔌",
          "mono": true,
          "hot": true,
          "desc": "Chuẩn kết nối của <strong>Anthropic</strong> — giúp AI giao tiếp với mọi công cụ, database, API theo một giao thức thống nhất. Được ví như 'USB-C cho AI'.",
          "added_date": "2026-02-03",
          "detail": "<strong>Agent ↔ Tool</strong> communication · Giống \"USB-C cho AI\" · Được OpenAI, Google DeepMind, Cursor, Replit, Sourcegraph adopt<br><strong>MCP Apps</strong> (Jan 2026): Extension mới — tools trả về interactive UI (dashboards, forms) trực tiếp trong conversation<br><strong>Skills over MCP</strong>: Experimental — skill discovery & distribution qua MCP primitives",
          "tags": [
            "Python SDK 21k⭐",
            "TS SDK 11k⭐",
            "C# (Microsoft)",
            "Kotlin (JetBrains)",
            "Swift",
            "Linux Foundation"
          ],
          "sources": [
            {
              "title": "Anthropic — Introducing MCP",
              "url": "https://www.anthropic.com/news/model-context-protocol"
            },
            {
              "title": "MCP Specification",
              "url": "https://modelcontextprotocol.io/specification/2025-11-25"
            },
            {
              "title": "Wikipedia — Model Context Protocol",
              "url": "https://en.wikipedia.org/wiki/Model_Context_Protocol"
            },
            {
              "title": "MCP GitHub",
              "url": "https://github.com/modelcontextprotocol"
            }
          ],
          "pricing": "free",
          "deployment": "hybrid",
          "difficulty": "intermediate",
          "whenToUse": [
            "tool integration for LLMs",
            "connecting AI apps to external data sources",
            "building standardized AI plugins",
            "cross-platform tool sharing"
          ],
          "whenNotToUse": [
            "agent-to-agent communication (use A2A)",
            "simple REST API calls without AI context"
          ],
          "compatibleWith": [
            "a2a",
            "claude-code",
            "claude-ai",
            "chatgpt",
            "cursor",
            "windsurf",
            "openai-agents-sdk",
            "google-adk",
            "dify"
          ],
          "useCases": [
            "tool-integration",
            "data-access",
            "ai-plugin-system",
            "ide-extension"
          ],
          "languages": [
            "python",
            "js",
            "java",
            "csharp",
            "go",
            "rust",
            "swift",
            "ruby"
          ],
          "verified_at": "2026-02-11",
          "verification_source": "docs",
          "github_stars": 6400,
          "license": "Apache-2.0"
        },
        {
          "name": "A2A — Agent2Agent Protocol",
          "slug": "a2a",
          "icon": "🤝",
          "mono": true,
          "hot": true,
          "desc": "Giao thức của <strong>Google</strong> — giúp các AI agent nói chuyện và hợp tác với nhau, dù được xây từ bất kỳ nền tảng nào.",
          "added_date": "2026-02-03",
          "detail": "<strong>Agent ↔ Agent</strong> communication · Bổ sung MCP (MCP = tools, A2A = agents)<br><strong>Agent Cards</strong>: JSON mô tả capabilities, cho phép agent discover nhau<br><strong>v0.3</strong> (Jul 2025): gRPC support, security cards, Python SDK mở rộng<br>150+ organizations support · Linux Foundation hosted",
          "tags": [
            "Google ADK native",
            "HTTP/SSE/JSON-RPC",
            "LangGraph",
            "CrewAI",
            "Semantic Kernel"
          ],
          "note": "💡 Dùng <strong>MCP cho tools</strong>, <strong>A2A cho agents</strong> — 2 protocol bổ sung nhau, không thay thế!",
          "sources": [
            {
              "title": "Google — Announcing A2A",
              "url": "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
            },
            {
              "title": "A2A GitHub",
              "url": "https://github.com/google/A2A"
            },
            {
              "title": "A2A Protocol Documentation",
              "url": "https://google.github.io/A2A/"
            }
          ],
          "pricing": "free",
          "deployment": "hybrid",
          "difficulty": "intermediate",
          "whenToUse": [
            "agent-to-agent communication",
            "cross-framework agent collaboration",
            "enterprise multi-agent workflows",
            "multi-vendor agent interop"
          ],
          "whenNotToUse": [
            "tool integration for LLMs (use MCP)",
            "single-agent applications"
          ],
          "compatibleWith": [
            "mcp",
            "google-adk",
            "langgraph",
            "crewai",
            "autogen",
            "pydantic-ai"
          ],
          "useCases": [
            "multi-agent-systems",
            "enterprise-workflows",
            "agent-interop",
            "cross-platform-agents"
          ],
          "languages": [
            "python",
            "js",
            "java",
            "go",
            "rust",
            "csharp"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 22864,
          "license": "Apache-2.0"
        }
      ]
    },
    {
      "id": "frameworks",
      "title": "Agent Frameworks — Xây dựng AI agents",
      "color": "rose",
      "gridCols": 4,
      "cards": [
        {
          "name": "LangGraph",
          "slug": "langgraph",
          "icon": "🦜",
          "mono": true,
          "desc": "Framework điều phối agent có trạng thái, thuộc hệ sinh thái LangChain. Phổ biến nhất hiện nay.",
          "added_date": "2026-02-03",
          "tags": [
            "27.5K⭐",
            "4.2M downloads/mo"
          ],
          "detail": "Framework mã nguồn mở của LangChain cho phép xây dựng agent dạng đồ thị trạng thái (stateful graph). Hỗ trợ durable execution — agent tự phục hồi sau lỗi, human-in-the-loop — con người can thiệp bất kỳ lúc nào, và long-term memory xuyên phiên. Được Klarna, Replit, Uber, LinkedIn, Elastic tin dùng trong production. Có LangGraph Studio để debug visual và LangGraph Platform để deploy.",
          "sources": [
            {
              "title": "LangGraph Official",
              "url": "https://www.langchain.com/langgraph"
            },
            {
              "title": "LangGraph GitHub",
              "url": "https://github.com/langchain-ai/langgraph"
            },
            {
              "title": "LangGraph Docs",
              "url": "https://docs.langchain.com/oss/python/langgraph/overview"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "intermediate",
          "whenToUse": [
            "stateful multi-step agent workflows",
            "complex control flow with branching and loops",
            "human-in-the-loop agent approval",
            "long-running durable agent execution"
          ],
          "whenNotToUse": [
            "simple single-call LLM tasks",
            "no need for state persistence between steps",
            "team unfamiliar with graph-based programming"
          ],
          "compatibleWith": [
            "langfuse",
            "mcp",
            "ollama",
            "litellm",
            "pgvector",
            "chroma",
            "qdrant",
            "milvus"
          ],
          "useCases": [
            "agent-orchestration",
            "multi-agent-systems",
            "rag-pipeline",
            "workflow-automation"
          ],
          "languages": [
            "python",
            "js"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 27670,
          "license": "MIT"
        },
        {
          "name": "CrewAI",
          "slug": "crewai",
          "icon": "👥",
          "mono": true,
          "desc": "Tạo đội agent AI theo vai trò, ít code. Mỗi agent một nhiệm vụ, phối hợp tự động.",
          "added_date": "2026-02-03",
          "tags": [
            "Multi-agent crews",
            "Free core"
          ],
          "detail": "Framework xây dựng đội agent theo mô hình role-based — mỗi agent đóng 1 vai trò cụ thể (researcher, writer, reviewer...) và phối hợp như một team thật. Hỗ trợ sequential, hierarchical và consensual process. Tích hợp sẵn 700+ tools, LangChain compatible. CrewAI Enterprise cung cấp deployment, monitoring, và agent marketplace.",
          "sources": [
            {
              "title": "CrewAI Official",
              "url": "https://www.crewai.com/"
            },
            {
              "title": "CrewAI GitHub",
              "url": "https://github.com/crewAIInc/crewAI"
            },
            {
              "title": "CrewAI Docs",
              "url": "https://docs.crewai.com/"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "intermediate",
          "whenToUse": [
            "multi-agent orchestration",
            "role-based AI teams",
            "autonomous agent collaboration",
            "complex workflow automation"
          ],
          "whenNotToUse": [
            "simple single-agent tasks",
            "non-Python stack",
            "real-time low-latency requirements"
          ],
          "compatibleWith": [
            "langfuse",
            "ollama",
            "dify"
          ],
          "useCases": [
            "multi-agent",
            "workflow-automation",
            "agent-orchestration",
            "enterprise-automation"
          ],
          "languages": [
            "python"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 47347,
          "license": "MIT"
        },
        {
          "name": "AutoGen",
          "slug": "autogen",
          "icon": "🔷",
          "mono": true,
          "desc": "Framework của Microsoft cho nhiều agent hội thoại với nhau. Kiến trúc linh hoạt, dễ mở rộng.",
          "added_date": "2026-02-03",
          "tags": [
            "Microsoft",
            "Flexible arch"
          ],
          "detail": "Framework multi-agent của Microsoft Research cho phép nhiều agent LLM trò chuyện với nhau để giải quyết task phức tạp. Hỗ trợ human-in-the-loop, code execution tự động, và group chat patterns. AutoGen 0.4 (2025) được viết lại hoàn toàn với kiến trúc event-driven, hỗ trợ distributed agents và pluggable components.",
          "sources": [
            {
              "title": "AutoGen GitHub",
              "url": "https://github.com/microsoft/autogen"
            },
            {
              "title": "AutoGen Docs",
              "url": "https://microsoft.github.io/autogen/"
            }
          ],
          "pricing": "free",
          "deployment": "self-hosted",
          "difficulty": "advanced",
          "whenToUse": [
            "multi-agent conversation systems",
            "research prototyping",
            "human-in-the-loop workflows",
            "complex agent collaboration"
          ],
          "whenNotToUse": [
            "greenfield projects (consider Microsoft Agent Framework)",
            "simple single-agent tasks",
            "TypeScript-only stack"
          ],
          "compatibleWith": [
            "mcp",
            "a2a",
            "ollama"
          ],
          "useCases": [
            "multi-agent",
            "research",
            "conversation-ai",
            "workflow-automation"
          ],
          "languages": [
            "python",
            "csharp"
          ],
          "verified_at": "2026-03-24",
          "verification_source": "docs",
          "github_stars": 56296,
          "license": "MIT"
        },
        {
          "name": "OpenAI Agents SDK",
          "slug": "openai-agents-sdk",
          "icon": "🟢",
          "mono": true,
          "desc": "SDK nhẹ của OpenAI bằng Python — xây agent nhanh với rào chắn an toàn tích hợp.",
          "added_date": "2026-02-03",
          "tags": [
            "20K⭐",
            "100+ LLMs"
          ],
          "detail": "SDK chính thức của OpenAI để xây dựng agent — nhẹ, production-ready. Có Guardrails tích hợp (input/output validation), Handoffs (chuyển task giữa agents), và Tracing (debug + monitor). Hỗ trợ MCP natively từ v0.0.7. Thiết kế tối giản: ít abstraction, dễ customize, dễ debug.",
          "sources": [
            {
              "title": "OpenAI Agents SDK",
              "url": "https://openai.github.io/openai-agents-python/"
  
... [TRUNCATED]
```

### File: hot-right-now.json
```json
{
  "updated": "2026-03-09",
  "items": [
    {
      "slug": "multi-agent-systems",
      "reason": {
        "en": "The hottest architecture pattern — agents collaborating, delegating, and solving complex tasks together",
        "vi": "Kiến trúc nóng nhất hiện tại — các agent phối hợp, phân công và giải quyết task phức tạp cùng nhau"
      }
    },
    {
      "slug": "generative-coding",
      "reason": {
        "en": "AI-generated code is reshaping how developers build — from autocomplete to full app generation",
        "vi": "Code do AI tạo ra đang thay đổi cách developer làm việc — từ autocomplete đến sinh toàn bộ ứng dụng"
      }
    },
    {
      "slug": "ai-governance",
      "reason": {
        "en": "As AI scales, governance frameworks become critical — safety, compliance, and responsible deployment",
        "vi": "Khi AI mở rộng, quản trị trở nên thiết yếu — an toàn, tuân thủ và triển khai có trách nhiệm"
      }
    },
    {
      "slug": "universal-agent-skills",
      "reason": {
        "en": "Core capabilities every AI agent needs — browsing, coding, file handling, and tool use",
        "vi": "Năng lực cốt lõi mọi AI agent cần có — duyệt web, code, xử lý file và sử dụng công cụ"
      }
    },
    {
      "slug": "claude-mem",
      "reason": {
        "en": "Persistent memory for Claude — enabling context-aware, long-running agent workflows",
        "vi": "Bộ nhớ bền vững cho Claude — hỗ trợ workflow agent dài hạn, nhận biết ngữ cảnh"
      }
    },
    {
      "slug": "a2a",
      "reason": {
        "en": "Google's Agent2Agent protocol — the emerging standard for agents to communicate across platforms",
        "vi": "Giao thức Agent2Agent của Google — tiêu chuẩn mới để các agent giao tiếp xuyên nền tảng"
      }
    }
  ]
}

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">

<!-- PRERENDER:HEAD:START -->
<title>See AI First — The Opinionated AI Stack Guide</title>
<meta name="description" content="Curated directory of 66 AI developer tools across 13 categories, with evidence-first sourcing.">
<meta property="og:title" content="See AI First — The Opinionated AI Stack Guide">
<meta property="og:description" content="Curated directory of 66 AI developer tools across 13 categories, with evidence-first sourcing.">
<meta property="og:url" content="https://seeaifirst.com/">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="vi_VN">
<meta name="twitter:title" content="See AI First — The Opinionated AI Stack Guide">
<meta name="twitter:description" content="Curated directory of 66 AI developer tools across 13 categories, with evidence-first sourcing.">
<link rel="canonical" href="https://seeaifirst.com/">
<script type="application/ld+json" id="seeaifirst-jsonld">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://seeaifirst.com/#website","name":"See AI First","alternateName":"AI Mindmap","url":"https://seeaifirst.com","description":"Curated directory of 66 AI developer tools across 13 categories, with evidence-first sourcing.","inLanguage":"en"},{"@type":"CollectionPage","@id":"https://seeaifirst.com/#directory","name":"See AI First — AI Tools Directory 2026","url":"https://seeaifirst.com/","isPartOf":{"@id":"https://seeaifirst.com/#website"},"inLanguage":"en","mainEntity":{"@type":"ItemList","numberOfItems":66,"itemListElement":[{"@type":"ListItem","position":1,"item":{"@type":"SoftwareApplication","name":"MCP — Model Context Protocol","url":"https://seeaifirst.com/tool/mcp","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Anthropic's connection standard — lets AI talk to any tool, database, or API through one unified protocol. Often called 'USB-C for AI'.","keywords":["Protocols — Standardized Communication Layer","python","js","java","csharp","go","rust","swift","ruby"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://www.anthropic.com/news/model-context-protocol","https://modelcontextprotocol.io/specification/2025-11-25","https://en.wikipedia.org/wiki/Model_Context_Protocol","https://github.com/modelcontextprotocol"],"datePublished":"2026-02-03","dateModified":"2026-02-11"}},{"@type":"ListItem","position":2,"item":{"@type":"SoftwareApplication","name":"A2A — Agent2Agent Protocol","url":"https://seeaifirst.com/tool/a2a","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Google's protocol — lets AI agents communicate and collaborate with each other, regardless of their underlying framework.","keywords":["Protocols — Standardized Communication Layer","python","js","java","go","rust","csharp"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/","https://github.com/google/A2A","https://google.github.io/A2A/"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":3,"item":{"@type":"SoftwareApplication","name":"LangGraph","url":"https://seeaifirst.com/tool/langgraph","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Stateful agent orchestration framework from the LangChain ecosystem. The most widely adopted today.","keywords":["Agent Frameworks — Building AI Agents","python","js"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://www.langchain.com/langgraph","https://github.com/langchain-ai/langgraph","https://docs.langchain.com/oss/python/langgraph/overview"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":4,"item":{"@type":"SoftwareApplication","name":"CrewAI","url":"https://seeaifirst.com/tool/crewai","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Build role-based AI agent teams with minimal code. Each agent has a role, they coordinate automatically.","keywords":["Agent Frameworks — Building AI Agents","python"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://www.crewai.com/","https://github.com/crewAIInc/crewAI","https://docs.crewai.com/"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":5,"item":{"@type":"SoftwareApplication","name":"AutoGen","url":"https://seeaifirst.com/tool/autogen","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Microsoft's framework for multi-agent conversations. Flexible architecture, easy to extend.","keywords":["Agent Frameworks — Building AI Agents","python","csharp"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://github.com/microsoft/autogen","https://microsoft.github.io/autogen/"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":6,"item":{"@type":"SoftwareApplication","name":"OpenAI Agents SDK","url":"https://seeaifirst.com/tool/openai-agents-sdk","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"OpenAI's lightweight Python SDK — build agents fast with built-in safety guardrails.","keywords":["Agent Frameworks — Building AI Agents","python","js"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://openai.github.io/openai-agents-python/","https://github.com/openai/openai-agents-python"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":7,"item":{"@type":"SoftwareApplication","name":"Google ADK","url":"https://seeaifirst.com/tool/google-adk","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Google's agent building toolkit — with built-in Gemini, Vertex AI, and A2A protocol integration.","keywords":["Agent Frameworks — Building AI Agents","python","js","go","java"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://google.github.io/adk-docs/","https://github.com/google/adk-python"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":8,"item":{"@type":"SoftwareApplication","name":"LlamaIndex","url":"https://seeaifirst.com/tool/llamaindex","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"The RAG specialist — connects AI to your private data for accurate answers from internal documents.","keywords":["Agent Frameworks — Building AI Agents","python","js"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://www.llamaindex.ai/","https://github.com/run-llama/llama_index","https://docs.llamaindex.ai/"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":9,"item":{"@type":"SoftwareApplication","name":"Rasa","url":"https://seeaifirst.com/tool/rasa","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Chatbot and voice AI platform — runs on your own server with full data control.","keywords":["Agent Frameworks — Building AI Agents","python"],"isAccessibleForFree":true,"license":"Apache-2.0","sameAs":["https://rasa.com/","https://github.com/RasaHQ/rasa","https://rasa.com/docs/"],"datePublished":"2026-02-03","dateModified":"2026-03-24"}},{"@type":"ListItem","position":10,"item":{"@type":"SoftwareApplication","name":"Browser-Use","url":"https://seeaifirst.com/tool/browser-use","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Browser automation framework for AI agents — control the web with Python using any LLM, 80K+ stars","keywords":["Agent Frameworks — Building AI Agents","python"],"isAccessibleForFree":true,"license":"MIT","sameAs":["https://github.com/browser-use/browser-use","https://docs.browser-use.com"],"datePublished":"2026-02-04","dateModified":"2026-03-24"}},{"@type":"ListItem","position":11,"item":{"@type":"SoftwareApplication","name":"Pydantic AI","url":"https://seeaifirst.com/tool/pydantic-ai","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Type-safe agent framework in the style of FastAPI — built by the Pydantic team, supports 40+ model providers","keywords":["Agent Frameworks — Building AI Agents","python"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://github.com/pydantic/pydantic-ai","https://ai.pydantic.dev"],"datePublished":"2026-02-04","dateModified":"2026-03-24"}},{"@type":"ListItem","position":12,"item":{"@type":"SoftwareApplication","name":"Mastra","url":"https://seeaifirst.com/tool/mastra","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"TypeScript-first agent framework from the Gatsby team — workflows, RAG, evals, and MCP built in","keywords":["Agent Frameworks — Building AI Agents","typescript"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://github.com/mastra-ai/mastra","https://mastra.ai/docs"],"datePublished":"2026-02-04","dateModified":"2026-03-24"}},{"@type":"ListItem","position":13,"item":{"@type":"SoftwareApplication","name":"Claude.ai (Web)","url":"https://seeaifirst.com/tool/claude-ai","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Anthropic's chat workspace — with memory, web search, Claude Cowork, and team plugins/connectors for enterprise workflows.","keywords":["Platforms & Config — AI Platforms & System Files","python","js","typescript"],"isAccessibleForFree":true,"sameAs":["https://claude.ai/","https://docs.claude.com/","https://support.claude.com/","https://claude.com/blog/cowork-plugins","https://claude.com/blog/cowork-plugins-across-enterprise"],"datePublished":"2026-02-03","dateModified":"2026-03-18"}},{"@type":"ListItem","position":14,"item":{"@type":"SoftwareApplication","name":"ChatGPT (Web)","url":"https://seeaifirst.com/tool/chatgpt","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"OpenAI's most popular AI chat — with GPTs, search, tools, and a built-in memory system.","keywords":["Platforms & Config — AI Platforms & System Files","python","js","typescript"],"isAccessibleForFree":true,"sameAs":["https://chatgpt.com/","https://platform.openai.com/"],"datePublished":"2026-02-03","dateModified":"2026-02-11"}},{"@type":"ListItem","position":15,"item":{"@type":"SoftwareApplication","name":"Claude-Mem","url":"https://seeaifirst.com/tool/claude-mem","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Plugin that gives Claude Code persistent long-term memory — automatically records experience, compresses intelligently, and remembers across sessions.","keywords":["Memory Systems — Cross-Session Memory","typescript"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"AGPL-3.0","sameAs":["https://github.com/sdairs/claude-mem"],"datePublished":"2026-02-03","dateModified":"2026-02-12"}},{"@type":"ListItem","position":16,"item":{"@type":"SoftwareApplication","name":"Other Memory Systems","url":"https://seeaifirst.com/tool/he-thong-memory-khac","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","keywords":["Memory Systems — Cross-Session Memory","python","typescript"],"isAccessibleForFree":true,"sameAs":["https://github.com/letta-ai/letta","https://github.com/mem0ai/mem0","https://www.getzep.com/"],"datePublished":"2026-02-03","dateModified":"2026-02-12"}},{"@type":"ListItem","position":17,"item":{"@type":"SoftwareApplication","name":"MemOS","url":"https://seeaifirst.com/tool/memos","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Unified memory operating system for LLMs — manages memory via MemCube with short-term and long-term support","keywords":["Memory Systems — Cross-Session Memory","python"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://github.com/MemTensor/MemOS"],"datePublished":"2026-02-04","dateModified":"2026-03-15"}},{"@type":"ListItem","position":18,"item":{"@type":"SoftwareApplication","name":"Universal Agent Skills","url":"https://seeaifirst.com/tool/universal-agent-skills","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Skills are .md files with instructions for AI agents — simple yet effective, runnable on any AI coding tool.","keywords":["Skills Ecosystem — \"Bigger than MCP\"","python","js"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"sameAs":["https://github.com/sickn33/antigravity-awesome-skills","https://github.com/VoltAgent/awesome-agent-skills","https://github.com/agentskills"],"datePublished":"2026-02-03","dateModified":"2026-02-26"}},{"@type":"ListItem","position":19,"item":{"@type":"SoftwareApplication","name":"Notable Skill Categories","url":"https://seeaifirst.com/tool/skill-categories-dang-chu-y","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","keywords":["Skills Ecosystem — \"Bigger than MCP\"","python","js"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"Apache-2.0","sameAs":["https://docs.claude.com/en/docs/claude-code/skills","https://github.com/modelcontextprotocol/experimental-ext-skills"],"datePublished":"2026-02-03","dateModified":"2026-02-26"}},{"@type":"ListItem","position":20,"item":{"@type":"SoftwareApplication","name":"Superpowers","url":"https://seeaifirst.com/tool/superpowers","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Agent-style skills framework for Claude Code — automatically activates the right skills based on context.","keywords":["Skills Ecosystem — \"Bigger than MCP\"","js","python","typescript"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"MIT","sameAs":["https://github.com/obra/superpowers","https://blog.fsck.com/2025/10/09/superpowers/"],"datePublished":"2026-02-08","dateModified":"2026-03-24"}},{"@type":"ListItem","position":21,"item":{"@type":"SoftwareApplication","name":"Agents (wshobson)","url":"https://seeaifirst.com/tool/agents-wshobson","applicationCategory":"DeveloperApplication","operatingSystem":"Cross-platform","description":"Collection of 112 agents + 146 skills + 73 speci
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
