# ðŸ“š Large Repos Catalog â€” Clone On Demand
# Version: 1.0 | 2026-03-25
# Purpose: CÃ¡c repo lá»›n khÃ´ng clone ngay â€” agent/dept láº¥y lá»‡nh clone khi cáº§n
# Path: brain/knowledge/notes/LARGE_REPOS_CATALOG.md

---

## CÃ¡ch sá»­ dá»¥ng

> Agent hoáº·c phÃ²ng ban: TÃ¬m repo phÃ¹ há»£p â†’ cháº¡y lá»‡nh clone â†’ thá»±c hiá»‡n dá»± Ã¡n â†’ xÃ³a sau khi xong (hoáº·c giá»¯ láº¡i náº¿u cáº§n tiáº¿p)

```powershell
# Clone vá» thÆ° má»¥c project cá»¥ thá»ƒ
# Thay <PROJECT_DIR> báº±ng tÃªn dá»± Ã¡n Ä‘ang lÃ m

git clone --depth 1 <URL> "$OMNICLAW_ROOT\plugins\github-repos\<REPO>"
```

---

## Catalog

| Repo | Dept chá»§ | Tag | LÃ½ do clone |
|------|----------|-----|-------------|
| `next.js` | Engineering | `FRONTEND` | Khi build web app cho OmniClaw |
| `excalidraw` | Design / R&D | `UI-TOOL` | Khi cáº§n source code diagram / whiteboard tool |
| `posthog` | Analytics / Ops | `ANALYTICS` | Khi cáº§n self-hosted analytics pipeline |
| `plotly.js` | Data / HUD | `VISUALIZATION` | Khi build dashboard charts |
| `trivy` | Security | `SECURITY` | Khi cáº§n container & secret scanning |
| `developer-roadmap` | Training | `KNOWLEDGE` | Khi onboard agents / cáº§n skill matrix |
| `openai-cookbook` | R&D | `AI-PATTERNS` | Khi research LLM integration patterns |
| `anime.js` | Design / Frontend | `ANIMATION` | Khi build animated UI |
| `agents-course` | Training / R&D | `AI-EDUCATION` | Khi training agents vá» LLM concepts |
| `gitignore` | Core / DevOps | `TEMPLATE` | Khi setup repo má»›i |
| `public-apis` | R&D / Integration | `INTEGRATION` | Khi cáº§n tÃ­ch há»£p external APIs |

---

## Chi tiáº¿t tá»«ng repo

---

### ðŸ”· next.js â€” Vercel
**Dept:** Engineering | Product | Frontend
**Size:** ~1.2 GB | **Stars:** 130k+
**Khi nÃ o dÃ¹ng:** Build web apps, dashboards, frontend cho dá»± Ã¡n OmniClaw Corp

```powershell
# DÃ¹ng khi: Build web UI cho OmniClaw dashboard, customer portal, product frontend
git clone --depth 1 https://github.com/vercel/next.js.git `
    "$OMNICLAW_ROOT\plugins\github-repos\next.js"
```

**OmniClaw Impact:**
- HUD v3 â†’ Next.js real-time dashboard
- Corp dashboard â†’ web interface cho 21 depts
- Product page / landing page

---

### ðŸ”· excalidraw â€” Excalidraw Team
**Dept:** Design | R&D | Product
**Size:** ~500 MB | **Stars:** 95k+
**Khi nÃ o dÃ¹ng:** Whiteboard tool, diagram tool, system architecture drawing

```powershell
# DÃ¹ng khi: Cáº§n tool váº½ diagram cho dá»± Ã¡n OmniClaw, system design, wireframe alternative
git clone --depth 1 https://github.com/excalidraw/excalidraw.git `
    "$OMNICLAW_ROOT\plugins\github-repos\excalidraw"
```

**OmniClaw Impact:**
- Thay tháº¿ Stitch cho system architecture diagrams
- Board brainstorm ná»™i bá»™ cho cÃ¡c phÃ²ng ban
- Self-hosted lightweight alternative

---

### ðŸ”· posthog â€” PostHog
**Dept:** Analytics | Ops | Product
**Size:** ~800 MB | **Stars:** 24k+
**Khi nÃ o dÃ¹ng:** Self-hosted analytics, event tracking, funnel analysis

```powershell
# DÃ¹ng khi: Cáº§n analytics pipeline cho OmniClaw products, track user events
git clone --depth 1 https://github.com/posthog/posthog.git `
    "$OMNICLAW_ROOT\plugins\github-repos\posthog"
```

**OmniClaw Impact:**
- Track OmniClaw usage metrics (daily corp cycle, agent calls, skill usage)
- Replace external analytics vá»›i self-hosted
- Wire vá»›i B5 system_pulse.py

---

### ðŸ”· plotly.js â€” Plotly
**Dept:** Data | Analytics | HUD
**Size:** ~400 MB | **Stars:** 17k+
**Khi nÃ o dÃ¹ng:** Charts, graphs, data visualization cho dashboards

```powershell
# DÃ¹ng khi: Build charts cho HUD, KPI dashboard, corp cycle analytics
git clone --depth 1 https://github.com/plotly/plotly.js.git `
    "$OMNICLAW_ROOT\plugins\github-repos\plotly.js"
```

**OmniClaw Impact:**
- HUD v3 charts â†’ KPI scoreboard visualization
- Dept health graphs
- CIV pipeline metrics charts

---

### ðŸ”· trivy â€” Aqua Security
**Dept:** Security | DevOps | CIV Pipeline
**Size:** ~600 MB | **Stars:** 24k+
**Khi nÃ o dÃ¹ng:** Security scan containers, repos, secrets â€” tÃ­ch há»£p CIV pipeline

```powershell
# DÃ¹ng khi: CIV pipeline cáº§n deep security scan repo/container
# Hoáº·c khi Security dept cáº§n audit tools
git clone --depth 1 https://github.com/aquasecurity/trivy.git `
    "$OMNICLAW_ROOT\plugins\github-repos\trivy"
```

**OmniClaw Impact:**
- CIV Pipeline Phase 2: security scan (thay `vet_repo.ps1`)
- Integrate vá»›i `security/QUARANTINE/` workflow
- Auto-scan má»i repo trÆ°á»›c khi approve

---

### ðŸ”· developer-roadmap â€” Kamran Ahmed
**Dept:** Training | HR | R&D
**Size:** ~300 MB | **Stars:** 310k+
**Khi nÃ o dÃ¹ng:** Khi onboard agent má»›i, build skill matrix, training plan

```powershell
# DÃ¹ng khi: Training dept cáº§n roadmap reference cho agent capabilities
git clone --depth 1 https://github.com/kamranahmedse/developer-roadmap.git `
    "$OMNICLAW_ROOT\plugins\github-repos\developer-roadmap"
```

**OmniClaw Impact:**
- Training dept: skill gap analysis cho 21 depts
- SKILL_REGISTRY enhancement: map skills to roadmap nodes
- Onboarding guide cho cÃ¡c agent má»›i

---

### ðŸ”· openai-cookbook â€” OpenAI
**Dept:** R&D | Engineering | AI Research
**Size:** ~500 MB | **Stars:** 65k+
**Khi nÃ o dÃ¹ng:** Research LLM patterns, prompt engineering, RAG techniques

```powershell
# DÃ¹ng khi: R&D dept cáº§n reference cho LLM integration, RAG, fine-tuning patterns
git clone --depth 1 https://github.com/openai/openai-cookbook.git `
    "$OMNICLAW_ROOT\plugins\github-repos\openai-cookbook"
```

**OmniClaw Impact:**
- R&D dept: LLM pattern library
- bridge_router.py improvements (new routing strategies)
- RAG patterns â†’ LightRAG enhancement

---

### ðŸ”· anime.js â€” Julian Garnier
**Dept:** Design | Frontend | Product
**Size:** ~200 MB | **Stars:** 50k+
**Khi nÃ o dÃ¹ng:** Khi build animated UI components, HUD animations

```powershell
# DÃ¹ng khi: Frontend cáº§n animations cho HUD dashboard, product UI
git clone --depth 1 https://github.com/juliangarnier/anime.git `
    "$OMNICLAW_ROOT\plugins\github-repos\anime"
```

**OmniClaw Impact:**
- HUD v3 real-time animated indicators
- Corp cycle phase progress animations
- Dept health dashboard micro-animations

---

### ðŸ”· agents-course â€” HuggingFace
**Dept:** Training | R&D | AI Research
**Size:** ~2 GB (notebooks + models)
**Khi nÃ o dÃ¹ng:** Training dept cáº§n deep-dive vÃ o AI agent concepts, LLM theory

```powershell
# DÃ¹ng khi: Training dept cáº§n full HuggingFace agents curriculum
# Cáº£nh bÃ¡o: ~2GB â€” chá»‰ clone khi cÃ³ storage
git clone --depth 1 https://github.com/huggingface/agents-course.git `
    "$OMNICLAW_ROOT\plugins\github-repos\agents-course"
```

**OmniClaw Impact:**
- Agent training curriculum cho 12 placeholder agents
- Reference cho activation_status.json â†’ activating new agents
- Pattern library cho autonomous agent behavior

---

### ðŸ”· gitignore â€” GitHub
**Dept:** DevOps | Engineering | All depts
**Size:** ~50 MB (small actually)
**Khi nÃ o dÃ¹ng:** Setup báº¥t ká»³ repo má»›i, cáº§n .gitignore template

```powershell
# Nhá» â€” cÃ³ thá»ƒ clone ngay khi cáº§n
git clone --depth 1 https://github.com/github/gitignore.git `
    "$OMNICLAW_ROOT\plugins\github-repos\gitignore"
```

**OmniClaw Impact:**
- Template cho má»i repo má»›i trong OmniClaw Corp
- Äáº·t vÃ o `ops/templates/gitignore/`

---

### ðŸ”· public-apis â€” Public APIs
**Dept:** R&D | Integration | Product
**Size:** ~100 MB (chá»§ yáº¿u markdown)
**Khi nÃ o dÃ¹ng:** Khi R&D cáº§n tÃ¬m API Ä‘á»ƒ tÃ­ch há»£p tÃ­nh nÄƒng má»›i

```powershell
# DÃ¹ng khi: Integration dept cáº§n tÃ¬m free API cho dá»± Ã¡n
git clone --depth 1 https://github.com/public-apis/public-apis.git `
    "$OMNICLAW_ROOT\plugins\github-repos\public-apis"
```

**OmniClaw Impact:**
- R&D dept: nguá»“n tham kháº£o API cho tÃ­ch há»£p
- External Integrations wishlist (B12 GitHub, Telegram, etc.)
- Rate-free APIs cho prototyping

---

## Quick Clone Reference

```powershell
# â•â•â• FRONTEND / UI â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# next.js â€” Khi build web app
git clone --depth 1 https://github.com/vercel/next.js.git "$OMNICLAW_ROOT\plugins\github-repos\next.js"

# excalidraw â€” Khi cáº§n whiteboard/diagram tool
git clone --depth 1 https://github.com/excalidraw/excalidraw.git "$OMNICLAW_ROOT\plugins\github-repos\excalidraw"

# anime.js â€” Khi cáº§n animations
git clone --depth 1 https://github.com/juliangarnier/anime.git "$OMNICLAW_ROOT\plugins\github-repos\anime"

# plotly.js â€” Khi cáº§n charts/graphs
git clone --depth 1 https://github.com/plotly/plotly.js.git "$OMNICLAW_ROOT\plugins\github-repos\plotly.js"

# â•â•â• ANALYTICS / MONITORING â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# posthog â€” Self-hosted analytics
git clone --depth 1 https://github.com/posthog/posthog.git "$OMNICLAW_ROOT\plugins\github-repos\posthog"

# â•â•â• SECURITY â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# trivy â€” Container/repo security scanner
git clone --depth 1 https://github.com/aquasecurity/trivy.git "$OMNICLAW_ROOT\plugins\github-repos\trivy"

# â•â•â• AI / R&D â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# openai-cookbook â€” LLM patterns & examples
git clone --depth 1 https://github.com/openai/openai-cookbook.git "$OMNICLAW_ROOT\plugins\github-repos\openai-cookbook"

# agents-course â€” HuggingFace agent curriculum [LARGE ~2GB]
git clone --depth 1 https://github.com/huggingface/agents-course.git "$OMNICLAW_ROOT\plugins\github-repos\agents-course"

# â•â•â• TRAINING / KNOWLEDGE â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# developer-roadmap â€” Skill matrix & learning paths
git clone --depth 1 https://github.com/kamranahmedse/developer-roadmap.git "$OMNICLAW_ROOT\plugins\github-repos\developer-roadmap"

# public-apis â€” Free API directory
git clone --depth 1 https://github.com/public-apis/public-apis.git "$OMNICLAW_ROOT\plugins\github-repos\public-apis"

# gitignore â€” GitHub templates [NHá»Ž - clone ngay]
git clone --depth 1 https://github.com/github/gitignore.git "$OMNICLAW_ROOT\plugins\github-repos\gitignore"
```

---

## Trigger Rule cho Agents

Khi má»™t agent/dept cáº§n clone, tá»± cháº¡y lá»‡nh trong section "Quick Clone Reference" theo tag phÃ¹ há»£p:

| Trigger | Tag cáº§n tÃ¬m | Action |
|---------|-------------|--------|
| Build web UI | `FRONTEND` | Clone next.js |
| Cáº§n charts | `VISUALIZATION` | Clone plotly.js |
| Security audit | `SECURITY` | Clone trivy |
| Research LLM | `AI-PATTERNS` | Clone openai-cookbook |
| Train agent má»›i | `AI-EDUCATION` | Clone agents-course |
| TÃ­ch há»£p external | `INTEGRATION` | Clone public-apis |
| Setup repo | `TEMPLATE` | Clone gitignore |
| Cáº§n analytics | `ANALYTICS` | Clone posthog |
| Cáº§n animations | `ANIMATION` | Clone anime.js |
| Diagram/whiteboard | `UI-TOOL` | Clone excalidraw |

---

*Catalog v1.0 | 2026-03-25 | Owner: content_intake dept*
*Run `python ops/omniclaw.py intake <url>` khi cÃ³ repo má»›i cáº§n thÃªm vÃ o catalog*

