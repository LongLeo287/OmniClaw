---
id: ki-context7-deep-01
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.660478
---

# KI-CONTEXT7-DEEP-01 — Context7: Real-Time Doc Injection for LLM
**Loại:** Deep Analysis — MCP Integration
**Nguồn:** github.com/upstash/context7 + context7.com/docs + context7.com/docs/api-guide
**Ngày:** 2026-03-23 | **Verdict:** ✅ APPROVE — Tier 1 candidate
**Priority:** P1 — Implement ngay

---

## 1. Problem: context7 giải quyết (WHY — Quan trọng nhất)

| Problem: | Description: | Tác động in OmniClaw |
|--------|-------|---------------------|
| ❌ Outdated training data | LLM biết API of Next.js 12, nhưng đang code with Next.js 15 | Agent viết code sai, debug mất giờ |
| ❌ Hallucinated APIs | Agent "bịa" function not tồn tại | Code crash, mất trust |
| ❌ Generic answers | not biết version-specific behavior | Sai config, deprecated patterns |

**Context7 giải quyết:** Pull docs real-time from source → inject vào prompt → Agent has thông tin chính xác, hiện tại.

---

## 2. Cách hoạt động (HOW)

```
User prompt: "Create Next.js middleware with JWT check. use context7"
                                    ↓
              context7 nhận thấy from khóa "use context7"
                                    ↓
              → resolve-library-id("next.js")     → /vercel/next.js
                                    ↓
              → query-docs("/vercel/next.js", "middleware JWT")
                                    ↓
              → Fetch real-time docs from nextjs.org/docs
                                    ↓
              → Inject docs vào prompt context
                                    ↓
              Agent viết code đúng cú pháp Next.js 15 ✅
```

---

## 3. Hai mode hoạt động

### Mode A: CLI + Skill (not cần MCP server)
```bash
npx ctx7 setup --claude   # Claude Code
npx ctx7 setup --cursor   # Cursor / Antigravity
npx ctx7 setup             # Auto-detect
```
- Cài Skill vào agent
- Dùng CLI commands: `ctx7 library <name>` and `ctx7 docs <libraryId>`
- **Phù hợp nhất for OmniClaw Corp hiện tại** (not cần MCP server riêng)

### Mode B: MCP Server (Full integration)
- Đăng ký Context7 MCP server in config
- Agent gọi MCP tools trực tiếp
- **Phù hợp for Phase 2** khi MCP infrastructure already ổn định

---

## 4. MCP Tools (API)

| Tool | Tham số | Features: |
|------|---------|-----------|
| `resolve-library-id` | `libraryName` (required), `query` (required) | Tìm library ID from tên |
| `query-docs` | `libraryId` (required), `query` (required) | Lấy documentation snippet |

**Library ID format:** `/owner/repo` — Example:
- `/vercel/next.js` → Next.js docs
- `/supabase/supabase` → Supabase docs  
- `/facebook/react` → React docs
- `/mongodb/docs` → MongoDB docs

---

## 5. REST API v2 (for custom integration)

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

### Python workflow mẫu:
```python
import requests
headers = {"Authorization": "Bearer CONTEXT7_API_KEY"}

# 1. Tìm library ID
libs = requests.get("https://context7.com/api/v2/libs/search",
    headers=headers,
    params={"libraryName": "supabase", "query": "auth email"}).json()
lib_id = libs[0]["id"]  # "/supabase/supabase"

# 2. Lấy docs
docs = requests.get("https://context7.com/api/v2/context",
    headers=headers,
    params={"libraryId": lib_id, "query": "email password sign-up"}).json()
```

---

## 6. Rate Limits & Plans

| Tier | Rate limit | Usage: |
|------|-----------|-----------|
| not has API key | Thấp (anonymous) | Demo/test |
| Free API key | Cao hơn | OmniClaw daily use |
| Enterprise | not giới hạn | Production scale |

**Action:** Đăng ký free API key tại **context7.com/dashboard**
→ Set `CONTEXT7_API_KEY` vào `MASTER.env`

---

## 7. Tích hợp vào OmniClaw — Action Plan

### Step 1: Cài CLI + Skill (Ngay hôm nay)
```bash
# for Antigravity (Cursor-compatible)
npx ctx7 setup --cursor

# for Claude Code
npx ctx7 setup --claude
```

### Step 2: Thêm Rule vào GEMINI.md + CLAUDE.md
```
Always use Context7 when needing library/API documentation, code generation,
or setup steps — without requiring explicit user request.
```
*(Rule tự động kích hoạt, not cần user gõ "use context7" mỗi lần)*

### Step 3: Đăng ký API key
- Truy cập: context7.com/dashboard
- Copy key vào: `$OMNICLAW_ROOT\MASTER.env`
- Biến môi trường: `CONTEXT7_API_KEY=xxx`

### Bước 4: Test validation
```bash
ctx7 library next.js "middleware JWT"
ctx7 docs /vercel/next.js "middleware auth"
```

### Bước 5 (Phase 2): Nâng lên MCP mode
- Thêm Context7 MCP server vào MCP config
- Agents sẽ gọi `resolve-library-id` + `query-docs` natively
- Theo dõi: Dept 4 (Registry) quản lý

---

## 8. Libraries OmniClaw thường dùng — Nên configure

| Library cần | Context7 ID (ước tính) |
|------------|------------------------|
| Next.js | `/vercel/next.js` |
| Supabase | `/supabase/supabase` |
| Firecrawl | Kiểm tra tại context7.com |
| LangChain | `/langchain-ai/langchain` |
| FastAPI | `/tiangolo/fastapi` |
| React | `/facebook/react` |
| Tailwind CSS | `/tailwindlabs/tailwindcss` |
| Prisma | `/prisma/prisma` |
| Cloudflare Workers | `/cloudflare/workers-sdk` |
| Playwright | `/microsoft/playwright` |

---

## 9. Đánh giá Media (Trust Signals)

| Nguồn | Nhận xét |
|-------|---------|
| Better Stack | *"Free Tool Makes Cursor 10x Smarter"* |
| Cole Medin | *"This is Hands Down the BEST MCP Server for AI Coding Assistants"* |
| AICodeKing | *"Makes CLINE 100X MORE EFFECTIVE!"* |
| Income Stream Surfers | *"Context7 + SequentialThinking MCPs: Is This AGI?"* |

**GitHub stats:** ⭐ 50.2k stars · 🍴 2.4k forks · 55 releases · MIT License
**Backed by:** Upstash (production-grade serverless Redis/Kafka company)

---

## 10. So sánh with OmniClaw hiện tại

| Capability | OmniClaw hiện tại | OmniClaw + Context7 |
|-----------|---------------|-----------------|
| Code generation with Next.js 15 | Dùng training data 2024 | Real-time docs 2026 |
| Supabase auth API | has thể outdated | Luôn version-specific |
| Firecrawl SDK methods | May hallucinate | Exact API |
| Agent viết migration scripts | Generic | Version-aware |

**Kết luận:** Context7 is layer **chống hallucination API** thiết yếu — đặc biệt quan trọng khi OmniClaw Corp build products with the library Changes: nhanh (Next.js, Supabase, Tailwind v4...).

---

## 11. Conflicts & Risks

| Risk | Mức độ | Mitigation |
|------|--------|------------|
| API key rate limit | Thấp | Free plan đủ dùng hàng ngày |
| Community-contributed docs has thể sai | Trung bình | Context7 has trustScore and report system |
| Backend/API/crawler is private | Thấp | not cần self-host — SaaS |
| Phụ thuộc internet | Thấp | Fallback: agent dùng training knowledge nếu ctx7 down |

**not has conflict with stack hiện tại** (LightRAG, Firecrawl, Mem0).

---

*KI Note version 1.0 | Phân tích: Antigravity | 2026-03-23*
*Ticket: CIV-2026-03-23-BATCH03 | Approved: Pending CEO*

