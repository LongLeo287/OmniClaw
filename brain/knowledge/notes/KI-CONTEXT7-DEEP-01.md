# KI-CONTEXT7-DEEP-01 â€” Context7: Real-Time Doc Injection cho LLM
**Loáº¡i:** Deep Analysis â€” MCP Integration
**Nguá»“n:** github.com/upstash/context7 + context7.com/docs + context7.com/docs/api-guide
**NgÃ y:** 2026-03-23 | **Verdict:** âœ… APPROVE â€” Tier 1 candidate
**Priority:** P1 â€” Implement ngay

---

## 1. Váº¥n Ä‘á» context7 giáº£i quyáº¿t (WHY â€” Quan trá»ng nháº¥t)

| Váº¥n Ä‘á» | MÃ´ táº£ | TÃ¡c Ä‘á»™ng trong AI OS |
|--------|-------|---------------------|
| âŒ Outdated training data | LLM biáº¿t API cá»§a Next.js 12, nhÆ°ng Ä‘ang code vá»›i Next.js 15 | Agent viáº¿t code sai, debug máº¥t giá» |
| âŒ Hallucinated APIs | Agent "bá»‹a" function khÃ´ng tá»“n táº¡i | Code crash, máº¥t trust |
| âŒ Generic answers | KhÃ´ng biáº¿t version-specific behavior | Sai config, deprecated patterns |

**Context7 giáº£i quyáº¿t:** Pull docs real-time tá»« source â†’ inject vÃ o prompt â†’ Agent cÃ³ thÃ´ng tin chÃ­nh xÃ¡c, hiá»‡n táº¡i.

---

## 2. CÃ¡ch hoáº¡t Ä‘á»™ng (HOW)

```
User prompt: "Create Next.js middleware with JWT check. use context7"
                                    â†“
              context7 nháº­n tháº¥y tá»« khÃ³a "use context7"
                                    â†“
              â†’ resolve-library-id("next.js")     â†’ /vercel/next.js
                                    â†“
              â†’ query-docs("/vercel/next.js", "middleware JWT")
                                    â†“
              â†’ Fetch real-time docs tá»« nextjs.org/docs
                                    â†“
              â†’ Inject docs vÃ o prompt context
                                    â†“
              Agent viáº¿t code Ä‘Ãºng cÃº phÃ¡p Next.js 15 âœ…
```

---

## 3. Hai mode hoáº¡t Ä‘á»™ng

### Mode A: CLI + Skill (KhÃ´ng cáº§n MCP server)
```bash
npx ctx7 setup --claude   # Claude Code
npx ctx7 setup --cursor   # Cursor / Antigravity
npx ctx7 setup             # Auto-detect
```
- CÃ i Skill vÃ o agent
- DÃ¹ng CLI commands: `ctx7 library <name>` vÃ  `ctx7 docs <libraryId>`
- **PhÃ¹ há»£p nháº¥t cho AI OS Corp hiá»‡n táº¡i** (khÃ´ng cáº§n MCP server riÃªng)

### Mode B: MCP Server (Full integration)
- ÄÄƒng kÃ½ Context7 MCP server trong config
- Agent gá»i MCP tools trá»±c tiáº¿p
- **PhÃ¹ há»£p cho Phase 2** khi MCP infrastructure Ä‘Ã£ á»•n Ä‘á»‹nh

---

## 4. MCP Tools (API)

| Tool | Tham sá»‘ | Chá»©c nÄƒng |
|------|---------|-----------|
| `resolve-library-id` | `libraryName` (required), `query` (required) | TÃ¬m library ID tá»« tÃªn |
| `query-docs` | `libraryId` (required), `query` (required) | Láº¥y documentation snippet |

**Library ID format:** `/owner/repo` â€” vÃ­ dá»¥:
- `/vercel/next.js` â†’ Next.js docs
- `/supabase/supabase` â†’ Supabase docs  
- `/facebook/react` â†’ React docs
- `/mongodb/docs` â†’ MongoDB docs

---

## 5. REST API v2 (Cho custom integration)

### Endpoint 1: Search Library
```
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
```

### Endpoint 2: Get Context (Documentation)
```
GET /api/v2/context?libraryId=/facebook/react&query=useEffect&type=txt
Authorization: Bearer CONTEXT7_API_KEY

Response:
[{
  "title": "Using the Effect Hook",
  "content": "The Effect Hook lets you perform side effects...",
  "source": "react.dev/reference/react/useEffect"
}]
```

### Python workflow máº«u:
```python
import requests
headers = {"Authorization": "Bearer CONTEXT7_API_KEY"}

# 1. TÃ¬m library ID
libs = requests.get("https://context7.com/api/v2/libs/search",
    headers=headers,
    params={"libraryName": "supabase", "query": "auth email"}).json()
lib_id = libs[0]["id"]  # "/supabase/supabase"

# 2. Láº¥y docs
docs = requests.get("https://context7.com/api/v2/context",
    headers=headers,
    params={"libraryId": lib_id, "query": "email password sign-up"}).json()
```

---

## 6. Rate Limits & Plans

| Tier | Rate limit | CÃ¡ch dÃ¹ng |
|------|-----------|-----------|
| KhÃ´ng cÃ³ API key | Tháº¥p (anonymous) | Demo/test |
| Free API key | Cao hÆ¡n | AI OS daily use |
| Enterprise | KhÃ´ng giá»›i háº¡n | Production scale |

**Action:** ÄÄƒng kÃ½ free API key táº¡i **context7.com/dashboard**
â†’ Set `CONTEXT7_API_KEY` vÃ o `MASTER.env`

---

## 7. TÃ­ch há»£p vÃ o AI OS â€” Action Plan

### BÆ°á»›c 1: CÃ i CLI + Skill (Ngay hÃ´m nay)
```bash
# Cho Antigravity (Cursor-compatible)
npx ctx7 setup --cursor

# Cho Claude Code
npx ctx7 setup --claude
```

### BÆ°á»›c 2: ThÃªm Rule vÃ o GEMINI.md + CLAUDE.md
```
Always use Context7 when needing library/API documentation, code generation,
or setup steps â€” without requiring explicit user request.
```
*(Rule tá»± Ä‘á»™ng kÃ­ch hoáº¡t, khÃ´ng cáº§n user gÃµ "use context7" má»—i láº§n)*

### BÆ°á»›c 3: ÄÄƒng kÃ½ API key
- Truy cáº­p: context7.com/dashboard
- Copy key vÃ o: `<AI_OS_ROOT>\MASTER.env`
- Biáº¿n mÃ´i trÆ°á»ng: `CONTEXT7_API_KEY=xxx`

### BÆ°á»›c 4: Test validation
```bash
ctx7 library next.js "middleware JWT"
ctx7 docs /vercel/next.js "middleware auth"
```

### BÆ°á»›c 5 (Phase 2): NÃ¢ng lÃªn MCP mode
- ThÃªm Context7 MCP server vÃ o MCP config
- Agents sáº½ gá»i `resolve-library-id` + `query-docs` natively
- Theo dÃµi: Dept 4 (Registry) quáº£n lÃ½

---

## 8. Libraries AI OS thÆ°á»ng dÃ¹ng â€” NÃªn configure

| Library cáº§n | Context7 ID (Æ°á»›c tÃ­nh) |
|------------|------------------------|
| Next.js | `/vercel/next.js` |
| Supabase | `/supabase/supabase` |
| Firecrawl | Kiá»ƒm tra táº¡i context7.com |
| LangChain | `/langchain-ai/langchain` |
| FastAPI | `/tiangolo/fastapi` |
| React | `/facebook/react` |
| Tailwind CSS | `/tailwindlabs/tailwindcss` |
| Prisma | `/prisma/prisma` |
| Cloudflare Workers | `/cloudflare/workers-sdk` |
| Playwright | `/microsoft/playwright` |

---

## 9. ÄÃ¡nh giÃ¡ Media (Trust Signals)

| Nguá»“n | Nháº­n xÃ©t |
|-------|---------|
| Better Stack | *"Free Tool Makes Cursor 10x Smarter"* |
| Cole Medin | *"This is Hands Down the BEST MCP Server for AI Coding Assistants"* |
| AICodeKing | *"Makes CLINE 100X MORE EFFECTIVE!"* |
| Income Stream Surfers | *"Context7 + SequentialThinking MCPs: Is This AGI?"* |

**GitHub stats:** â­ 50.2k stars Â· ðŸ´ 2.4k forks Â· 55 releases Â· MIT License
**Backed by:** Upstash (production-grade serverless Redis/Kafka company)

---

## 10. So sÃ¡nh vá»›i AI OS hiá»‡n táº¡i

| Capability | AI OS hiá»‡n táº¡i | AI OS + Context7 |
|-----------|---------------|-----------------|
| Code generation vá»›i Next.js 15 | DÃ¹ng training data 2024 | Real-time docs 2026 |
| Supabase auth API | CÃ³ thá»ƒ outdated | LuÃ´n version-specific |
| Firecrawl SDK methods | May hallucinate | Exact API |
| Agent viáº¿t migration scripts | Generic | Version-aware |

**Káº¿t luáº­n:** Context7 lÃ  layer **chá»‘ng hallucination API** thiáº¿t yáº¿u â€” Ä‘áº·c biá»‡t quan trá»ng khi AI OS Corp build products vá»›i cÃ¡c library thay Ä‘á»•i nhanh (Next.js, Supabase, Tailwind v4...).

---

## 11. Conflicts & Risks

| Risk | Má»©c Ä‘á»™ | Mitigation |
|------|--------|------------|
| API key rate limit | Tháº¥p | Free plan Ä‘á»§ dÃ¹ng hÃ ng ngÃ y |
| Community-contributed docs cÃ³ thá»ƒ sai | Trung bÃ¬nh | Context7 cÃ³ trustScore vÃ  report system |
| Backend/API/crawler lÃ  private | Tháº¥p | KhÃ´ng cáº§n self-host â€” SaaS |
| Phá»¥ thuá»™c internet | Tháº¥p | Fallback: agent dÃ¹ng training knowledge náº¿u ctx7 down |

**KhÃ´ng cÃ³ conflict vá»›i stack hiá»‡n táº¡i** (LightRAG, Firecrawl, Mem0).

---

*KI Note version 1.0 | PhÃ¢n tÃ­ch: Antigravity | 2026-03-23*
*Ticket: CIV-2026-03-23-BATCH03 | Approved: Pending CEO*

