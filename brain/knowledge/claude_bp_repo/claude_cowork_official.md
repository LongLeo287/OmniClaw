---
source: https://support.claude.com/en/articles/13345190-get-started-with-cowork
ingested_at: 2026-03-16T10:27:00+07:00
domain: AI|Product|Agentic|Desktop
trust_level: HIGHEST
vet_status: PASS
tags: [claude-cowork, anthropic, desktop-app, agentic, file-automation, browser-automation, connectors, official-docs]
---

# Claude Cowork — Official Anthropic Agentic Desktop Tool

**Source:** https://support.claude.com/en/articles/13345190-get-started-with-cowork  
**Platform:** Claude Desktop App (macOS + Windows)  
**Status:** Research Preview  
**Tier required:** Claude Pro, Max, Team, hoặc Enterprise

---

## Tổng quan

> "Claude Cowork biến Claude thành một digital coworker — delegate outcomes, không phải prompts."

Claude Cowork = **agentic mode** trong Claude Desktop App. Thay vì chat từng bước, user mô tả **outcome** muốn đạt được → Claude tự break down + execute.

**Chạy trong:** Virtual machine (sandboxed) có file access

---

## Setup (Step-by-Step)

```
1. Download Claude Desktop app → claude.com/download
2. Cần subscription: Pro / Max / Team / Enterprise
3. Mở Claude Desktop → tab "Cowork" 
   (switch từ chat mode sang task execution mode)
4. Grant file access → chỉ định folders Claude được phép access
5. Mô tả task → Claude trình bày plan → user approve → execute
```

### Personalization
```
working-folder/
├── about-me.md          ← Thông tin về user (context file)
├── voice-and-style.md   ← Cách viết mong muốn (context file)
└── [project files]

+ Settings → Global Instructions → Apply to every Cowork session
```

---

## Core Capabilities

### 1. Autonomous Task Execution
```
User: "Analyze Q1 sales data and prepare executive summary"
Cowork:
  1. Đọc CSV files
  2. Tạo Excel với formulas
  3. Tạo PowerPoint presentation  
  4. Viết Word document summary
  → Deliver finished outputs
```
- Break complex tasks → subtasks
- Coordinate **multiple workstreams in parallel**
- Transparent progress (user thấy reasoning)

### 2. Direct File Interaction
Files Claude có thể làm việc:
- ✅ Excel (với formulas)
- ✅ PowerPoint presentations
- ✅ Word documents (formatted)
- ✅ CSV, JSON, Markdown
- ✅ Code files
- ✅ Read/write/move/rename/organize/create

### 3. Connectors & Plugins
Tích hợp external services:
| Connector | Capability |
|-----------|-----------|
| Google Drive | Read/write cloud files |
| Notion | Read/update pages |
| Asana | Task management |
| Canva | Design automation |
| + specialized skills | Custom capabilities |

### 4. Browser Automation (Chrome Extension)
```
Cài "Claude in Chrome" extension →
Cowork có thể:
  - Navigate web pages
  - Click buttons
  - Fill forms
  - Take screenshots
  - Interact with web content
```
> ⚠️ Security risk: monitor carefully khi grant browser access (prompt injection)

### 5. Scheduled Tasks
```
"Every Monday 9am, pull last week's metrics and email summary"
→ Cowork sets up cron schedule
→ Runs automatically, delivers results
```

### 6. Parallel Sessions
```
Session 1: "Prepare Q1 report" ─────────────── [running]
Session 2: "Research competitor pricing" ─────  [running]
Session 3: "Draft client proposal" ──────────── [running]
→ Queue up work → return to finished results
```

---

## Limitations (Research Preview)

| Limitation | Details |
|-----------|---------|
| **Must stay open** | Desktop app phải mở, không run background |
| **No session sync** | Không share/sync across devices |
| **No persistent memory** | Sessions không nhớ lần trước (workaround: context files) |
| **Internet risks** | Prompt injection khi web access enabled |
| **Sandboxed** | File access phải explicit grant |
| **Explicit approval** | File deletion cần confirm |

---

## Architecture (Inferred)

```
┌─────────────────────────────────────────────┐
│  Claude Desktop App                         │
│                                             │
│  ┌──────────┐  ┌──────────────────────────┐ │
│  │ Chat mode│  │ Cowork mode              │ │
│  │          │  │                          │ │
│  │          │  │  ┌────────────────────┐  │ │
│  │          │  │  │ Virtual Machine    │  │ │
│  │          │  │  │ (sandboxed)        │  │ │
│  │          │  │  │ - File access      │  │ │
│  │          │  │  │ - Browser (Chrome) │  │ │
│  │          │  │  └────────────────────┘  │ │
│  └──────────┘  │                          │ │
│                │  Connectors: GDrive,     │ │
│                │  Notion, Asana, Canva    │ │
│                └──────────────────────────┘ │
└─────────────────────────────────────────────┘
```

---

## So sánh với OmniClaw

| Feature | Claude Cowork | OmniClaw |
|---------|--------------|-------|
| Platform | Claude Desktop (official) | Antigravity + VSCode |
| File access | VM sandboxed | Direct filesystem |
| Browser | Chrome extension | browser_subagent tool |
| Scheduling | Built-in | Không có (Planned) |
| Parallel tasks | Multiple sessions | Không native |
| Memory | Context files | `.ai-memory/` + blackboard |
| Skills | Connectors + plugins | skills/ + plugins/ |
| Subscription | Pro/Max/Team/Enterprise | Free (Antigravity) |

---

## Patterns Học Được

### Pattern 1: Context Files > Persistent Memory
```
Thay vì cố persist memory giữa sessions:
→ Dùng files làm "persistent context"
→ `about-me.md`, `project-context.md`, `current-goals.md`
→ Đặt vào working directory
→ Auto-load mỗi session

OmniClaw đã có: `pre-session.md`, `blackboard.json`
→ Improve format theo Cowork pattern
```

### Pattern 2: Global Instructions
```
Settings-level instructions → apply mọi session
OmniClaw equivalent: CLAUDE.md / rules/AGENTS.md
→ Đây là OmniClaw đã làm đúng rồi
```

### Pattern 3: Plan → Approve → Execute Gate
```
Cowork: luôn show plan trước → user approve → execute
OmniClaw: nên adopt pattern này cho complex tasks
→ Không tự execute large changes mà không có approval
```

### Pattern 4: Parallel Workstreams
```
Cowork native: nhiều independent sessions
OmniClaw: spawn-agent pattern (khanhbkqt/spawn-agent)
→ Correlate với kiến thức spawn-agent đã nạp
```

---

## Relevance cho OmniClaw

**Trực tiếp liên quan:**
- Claude Cowork + open-claude-cowork → Đây là Anthropic's vision cho agentic desktop
- OmniClaw đang build similar capability independently
- Context files pattern → OmniClaw `pre-session.md` cần update format
- Plan-first gate → adopt vào OmniClaw workflow

**OmniClaw hiện tại đã có gì tương đương:**
- ✅ `pre-session.md` = Global Instructions
- ✅ `blackboard.json` = Context files
- ✅ skills/ = Connectors/Plugins  
- ✅ `mcp/config.json` = Tool access
- ❌ Scheduling = Chưa có
- ❌ Parallel sessions native = Chưa có (workaround: spawn-agent)

---

## References
- [Official Docs](https://support.claude.com/en/articles/13345190-get-started-with-cowork)
- [Claude Desktop](https://claude.com/download)
- [DataCamp overview](https://datacamp.com)
- [Forbes article](https://forbes.com)
