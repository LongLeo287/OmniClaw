---
id: ki-batch02-group4-nova-tools
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.363213
---

# KI Batch 2 — Group 4: NotebookLM Prompts + AgentsView + Agency-Agents
**Ingested:** 2026-03-21 | **Nova Batch 2** | Presentation + Monitoring + Agent Library

---

## KI: Awesome NotebookLM Prompts — Slide Design Prompt Library
**Category:** Dept 5 (Marketing) + Dept 16 (OD&L) | Nova output quality tool

### What It Is
700+ field-tested NotebookLM/Kael.im slide design prompts from real creators. Curated from Twitter/X power users, researchers, founders, designers.

### Style Categories (14 Styles)
| Style | Vibe |
|-------|------|
| Modern Newspaper | Swiss Style, Bauhaus, asymmetrical |
| Sharp Minimalism | Strict grid, whitespace luxury |
| Yellow × Black | Dynamic fashion magazine |
| Neo-Retro Dev Deck | Engineering notes + pixel art |
| Anti-Gravity | Living artifact, Apple + DeepMind |
| Manga / Magazine | Pop illustrations, street style |
| Classic Pop | Sculpture × vaporwave |
| Tech/Art/Neon | Constructivism, avant-garde |
| Premium Mockup | Apple device showcase |
| Digital / Neo / Pop | Vitamin pop, organic shapes |
| Sports / Energy | Dynamic, athletic, bold italic |
| Pink Street | Pop deformed illustrations |
| Seminar Minimal | White bg, red accent, portrait |
| Royal Blue × Red | Watercolor artistic |

### Key Insight for OmniClaw
- **Anti-Gravity style** = perfect for OmniClaw/Nova reports (it literally references DeepMind + Apple)
- **Neo-Retro Dev Deck** = best for CEO briefings on agent architecture
- Each prompt specifies: color palette, typography rules, layout variations, what to avoid

### OmniClaw Integration
- **Nova report generation**: Use prompts when generating CEO slidedeck presentations
- **Dept 5 (Marketing)**: marketing materials generation guide
- **Kael.im** (kael.im/home) = 100 free pages/day via referral (nbp) → free slides!

---

## KI: AgentsView — Multi-Agent Session Analytics
**Category:** Dept 18 (Monitoring) + Dept 22 (Data Upgrade) | Agent observability

### What It Is
Local-first desktop + web app to browse, search, analyze AI agent coding sessions.
Supports **11 agents**: Claude Code, Codex, Gemini, Copilot, Cursor, OpenCode, Amp, iFlow, VSCode Copilot, Pi, **OpenClaw**.

### Core Features
- Full-text search across ALL agent sessions (FTS5 SQLite)
- Analytics dashboard: activity heatmaps, tool usage, velocity, project breakdowns
- Live updates via SSE during active sessions
- Vim-style keyboard navigation (j/k/[/])
- Export sessions to HTML or GitHub Gist
- **100% local** — no accounts, no network, single binary

### Agent Session Directories
```
Claude Code: ~/.claude/projects/
Gemini (Nova): ~/.gemini/
OpenClaw: ~/.openclaw/agents/
```

### Quick Install (Windows)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://agentsview.io/install.ps1 | iex"
agentsview  # starts at http://127.0.0.1:8080
```

### OmniClaw Integration
- **Dept 18 (Monitoring)**: Deploy to monitor all OmniClaw agent sessions
- **Nova sessions**: Gemini dir (`~/.gemini/`) is already tracked
- **OpenClaw sessions**: Also tracked if using ClawTask
- **CEO dashboard**: agentsview analytics → agent productivity KPIs

---

## KI: Agency-Agents — 144 Specialized Agent Library
**Category:** Dept 21 (Agent Dev) + Dept 4 (Registry) | MASSIVE skill expansion

### What It Is
Complete AI agency in code: 144+ specialized agents across 12 divisions. Personality-driven, deliverable-focused, production-ready.

### 12 Divisions with Key Agents
| Division | Agent Count | OmniClaw Relevance |
|---------|-------------|-----------------|
| Engineering | 23 agents | AI Engineer, Security Eng, Autonomous Optimization Architect |
| Design | 8 agents | UI Designer, Brand Guardian |
| Marketing | 25 agents | Content Creator, SEO, China market specialists |
| Sales | 8 agents | Outbound, Deal Strategist |
| Product | 5 agents | Sprint Prioritizer, Trend Researcher |
| Project Mgmt | 6 agents | Studio Producer, Project Shepherd |
| Testing | 8 agents | Reality Checker, Evidence Collector |
| Support | 6 agents | Analytics Reporter, Infrastructure Maintainer |
| Spatial Computing | 6 agents | XR Interface, Vision Pro |
| Specialized | 24 agents | **Agents Orchestrator, MCP Builder, Compliance Auditor** |
| Game Dev | 17 agents | Unity, Unreal, Godot, Blender, Roblox |
| Paid Media | 7 agents | PPC, Tracking |

### TOP Priority Agents for OmniClaw
1. **Agents Orchestrator** (`specialized/agents-orchestrator.md`) → Dept 13/Nova
2. **Autonomous Optimization Architect** (`engineering/engineering-autonomous-optimization-architect.md`) → Dept 13 + API Bridge
3. **MCP Builder** (`specialized/specialized-mcp-builder.md`) → Dept 8 + Tech
4. **Security Engineer** (`engineering/engineering-security-engineer.md`) → Dept 10 (Strix)
5. **Infrastructure Maintainer** (`support/support-infrastructure-maintainer.md`) → Dept 8 (Ops)
6. **Compliance Auditor** (`specialized/compliance-auditor.md`) → Dept 20 (CIV)
7. **Analytics Reporter** (`support/support-analytics-reporter.md`) → Dept 18

### Antigravity Native Support ✅
```bash
# Install all 144 agents as Antigravity skills
./scripts/install.sh --tool antigravity
# Installs to: ~/.gemini/antigravity/skills/agency-<slug>/
```

### OmniClaw Integration
- **Dept 4 (Registry)**: Register top 20 agents into OmniClaw skill registry
- **Dept 21 (Agent Dev)**: Use agency-agents SKILL.md templates as blueprints
- **Install for Antigravity**: Run installer → 144 skills available instantly
- **Chinese market coverage**: 15+ China-specific agents (WeChat, Douyin, Xiaohongshu, Baidu)

---

## Batch 2 Summary Routes
| Repo | Primary Dept | Priority |
|------|-------------|---------|
| awesome-notebooklm-prompts | Dept 5 + 16 | MEDIUM |
| agentsview | Dept 18 (Monitoring) | HIGH — install now |
| agency-agents | Dept 4 + 21 + all | CRITICAL — 144 agents for OmniClaw |
