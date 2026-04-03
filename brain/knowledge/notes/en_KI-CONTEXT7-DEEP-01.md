---
id: ki-context7-deep-01
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.660478
---

# KI-CONTEXT7-DEEP-01 — Context7: Real-Time Doc Injection for LLMs
**Type:** Deep Analysis — MCP Integration
**Source:** github.com/upstash/context7 + context7.com/docs + context7.com/docs/api-guide
**Date:** 2026-03-23 | **Verdict:** ✅ APPROVE — Tier 1 candidate
**Priority:** P1 — Implement immediately

---

## 1. Problem Solved by context7 (WHY — The Most Important Part)

| Problem: | Description: | Impact on OmniClaw |
|---|---|---|
| ❌ Outdated training data | LLM knows Next.js 12 API, but is coding with Next.js 15 | Agent writes incorrect code, debugging takes hours |
| ❌ Hallucinated APIs | Agent "invents" a non-existent function | Code crashes, trust is lost |
| ❌ Generic answers | Doesn't know version-specific behavior | Wrong config, deprecated patterns |

**Context7 solves this:** Pulls real-time docs from the source → injects them into the prompt → Agent has accurate, current information.

---

## 2. How It Works (HOW)

'''
User prompt: "Create Next.js middleware with JWT check. use context7"
                                    ↓
              context7 detects the keyword "use context7"
                                    ↓
              → resolve-library-id("next.js")     → /vercel/next.js
                                    ↓
              → query-docs("/vercel/next.js", "middleware JWT")
                                    ↓
              → Fetch real-time docs from nextjs.org/docs
                                    ↓
              → Inject docs into prompt context
                                    ↓
              Agent writes correct Next.js 15 syntax ✅
'''

---

## 3. Two Operating Modes

### Mode A: CLI + Skill (No MCP server needed)
'''bash
npx ctx7 setup --claude   # Claude Code
npx ctx7 setup --cursor   # Cursor / Antigravity
npx ctx7 setup             # Auto-detect
'''
- Installs a Skill into the agent
- Use CLI commands: `ctx7 library <name>` and `ctx7 docs <libraryId>`
- **Best fit for OmniClaw Corp currently** (no separate MCP server required)

### Mode B: MCP Server (Full integration)
- Register Context7 MCP server in the config
- Agent calls MCP tools directly
- **Suitable for Phase 2** when the MCP infrastructure is stable

---

## 4. MCP Tools (API)

| Tool | Parameters | Features: |
|---|---|---|
| `resolve-library-id` | `libraryName` (required), `query` (required) | Finds library ID from name |
| `query-docs` | `libraryId` (required), `query` (required) | Retrieves documentation snippet |

**Library ID format:** `/owner/repo` — Example:
- `/vercel/next.js` → Next.js docs
- `/supabase/supabase` → Supabase docs
- `/facebook/react` → React docs
- `/mongodb/docs` → MongoDB docs

---

## 5. REST API v2 (For custom integration)

### Endpoint 1: Search Library
'''
GET /api/v2/libs/search?libraryName=react&query=hooks
Authorization: Bearer CONTEXT7_API_KEY

Response:
[{
  "id": "/facebook/react",
  "name": "React",
  "totalSnippets": 1250,
  "trustScore": 95,
  "benchmarkScore": 88,
  "versions": ["v18.2.0", "v17.0.2"]
}]
'''

### Endpoint 2: Get Context (Documentation)
'''
GET /api/v2/context?libraryId=/facebook/react&query=useEffect&type=txt
Authorization: Bearer CONTEXT7_API_KEY

Response:
[{
  "title": "Using the Effect Hook",
  "content": "The Effect Hook lets you perform side effects...",
  "source": "react.dev/reference/react/useEffect"
}]
'''

### Sample Python workflow:
'''python
import requests
headers = {"Authorization": "Bearer CONTEXT7_API_KEY"}

# 1. Find library ID
libs = requests.get("https://context7.com/api/v2/libs/search",
    headers=headers,
    params={"libraryName": "supabase", "query": "auth email"}).json()
lib_id = libs[0]["id"]  # "/supabase/supabase"

# 2. Get docs
docs = requests.get("https://context7.com/api/v2/context",
    headers=headers,
    params={"libraryId": lib_id, "query": "email password sign-up"}).json()
'''

---

## 6. Rate Limits & Plans

| Tier | Rate limit | Usage: |
|---|---|---|
| No API key | Low (anonymous) | Demo/test |
| Free API key | Higher | OmniClaw daily use |
| Enterprise | Unlimited | Production scale |

**Action:** Register for a free API key at **context7.com/dashboard**
→ Set `CONTEXT7_API_KEY` in `MASTER.env`

---

## 7. Integration into OmniClaw — Action Plan

### Step 1: Install CLI + Skill (Today)
'''bash
# For Antigravity (Cursor-compatible)
npx ctx7 setup --cursor

# For Claude Code
npx ctx7 setup --claude
'''

### Step 2: Add Rule to GEMINI.md + CLAUDE.md
'''
Always use Context7 when needing library/API documentation, code generation,
or setup steps — without requiring explicit user request.
'''
*(Rule activates automatically, no need for the user to type "use context7" each time)*

### Step 3: Register API key
- Go to: context7.com/dashboard
- Copy key to: `$OMNICLAW_ROOT\MASTER.env`
- Environment variable: `CONTEXT7_API_KEY=xxx`

### Step 4: Test validation
'''bash
ctx7 library next.js "middleware JWT"
ctx7 docs /vercel/next.js "middleware auth"
'''

### Step 5 (Phase 2): Upgrade to MCP mode
- Add Context7 MCP server to MCP config
- Agents will call `resolve-library-id` + `query-docs` natively
- Monitored by: Dept 4 (Registry) management

---

## 8. Commonly Used OmniClaw Libraries — Should be configured

| Library Needed | Context7 ID (estimated) |
|---|---|
| Next.js | `/vercel/next.js` |
| Supabase | `/supabase/supabase` |
| Firecrawl | Check at context7.com |
| LangChain | `/langchain-ai/langchain` |
| FastAPI | `/tiangolo/fastapi` |
| React | `/facebook/react` |
| Tailwind CSS | `/tailwindlabs/tailwindcss` |
| Prisma | `/prisma/prisma` |
| Cloudflare Workers | `/cloudflare/workers-sdk` |
| Playwright | `/microsoft/playwright` |

---

## 9. Media Evaluation (Trust Signals)

| Source | Comment |
|---|---|
| Better Stack | *"Free Tool Makes Cursor 10x Smarter"* |
| Cole Medin | *"This is Hands Down the BEST MCP Server for AI Coding Assistants"* |
| AICodeKing | *"Makes CLINE 100X MORE EFFECTIVE!"* |
| Income Stream Surfers | *"Context7 + SequentialThinking MCPs: Is This AGI?"* |

**GitHub stats:** ⭐ 50.2k stars · 🍴 2.4k forks · 55 releases · MIT License
**Backed by:** Upstash (production-grade serverless Redis/Kafka company)

---

## 10. Comparison with Current OmniClaw

| Capability | Current OmniClaw | OmniClaw + Context7 |
|---|---|---|
| Code generation with Next.js 15 | Uses 2024 training data | Real-time 2026 docs |
| Supabase auth API | Potentially outdated | Always version-specific |
| Firecrawl SDK methods | May hallucinate | Exact API |
| Agent writes migration scripts | Generic | Version-aware |

**Conclusion:** Context7 is an essential **API hallucination prevention** layer — especially critical as OmniClaw Corp builds products with rapidly changing libraries (Next.js, Supabase, Tailwind v4...).

---

## 11. Conflicts & Risks

| Risk | Level | Mitigation |
|---|---|---|
| API key rate limit | Low | Free plan is sufficient for daily use |
| Community-contributed docs may be wrong | Medium | Context7 has a trustScore and report system |
| Backend/API/crawler is private | Low | No need to self-host — SaaS |
| Internet dependency | Low | Fallback: agent uses training knowledge if ctx7 is down |

**No conflicts with the current stack** (LightRAG, Firecrawl, Mem0).

---

*KI Note version 1.0 | Analysis: Antigravity | 2026-03-23*
*Ticket: CIV-2026-03-23-BATCH03 | Approved: Pending CEO*
