---
id: ki-publish-plan-2026-03-24
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.718450
---

# OmniClaw â€” Distribution & Publishing Plan
# Status: DRAFT | Saved: 2026-03-24 | For: CEO Brainstorm
# Retrieve khi cáº§n: "tÃ¬m plan publish OmniClaw"

---

## Bá»I Cáº¢NH

OmniClaw Corp hiá»‡n cháº¡y full local trên máy CEO.
Problem: há»‡ thá»‘ng náº·ng (~GB do plugins, vector DB, models) â†’ không thá»ƒ push raw lên GitHub.
Câu há»i cá»‘t lõi: **Distribute OmniClaw cho user khác nhÆ° tháº¿ nÃ o?**

---

## Architecture PHÃ‚N PHá»I (2-Tier)

### Tier 1 â€” GitHub Core (~5MB)
```
Gá»“m: Táº¥t cáº£ code/config/markdown â€” KHÃ”NG có data/models

âœ… corp/           â€” 21 dept prompts, rules, sops
âœ… brain/          â€” agents defs, brain/memory, governance
âœ… ops/            â€” scripts, workflows (37), configs
âœ… kho/            â€” registries (rules/prompts/plugins/mcp/llm/agents)
âœ… hud/            â€” HUD.md template
âœ… skills/         â€” SKILL.md files only (no heavy code)
âœ… security/       â€” vet_repo.ps1
âœ… .env.example    â€” template keys (không có giá trá»‹ tháº­t)
âœ… requirements.txt â€” pinned dependencies
âœ… README.md        â€” setup guide

âŒ .env            â€” gitignore (secrets)
âŒ plugins/        â€” gitignore (100+ repos, GB size)
âŒ brain/knowledge/lightrag_db/ â€” gitignore (vector DB)
âŒ infra/          â€” gitignore (Docker images, binaries)
âŒ telemetry/      â€” gitignore (logs)
âŒ security/QUARANTINE/incoming/ â€” gitignore (quarantine data)
```

### Tier 2 â€” Setup Script (user tá»± cÃ i)
```powershell
# ops/scripts/setup.ps1
# User clone repo â†’ cháº¡y script nÃ y 1 láº§n â†’ full system ready

1. pip install -r requirements.txt          (lightrag, mem0, supabase...)
2. ollama pull gemma2:2b                    (local LLM)
3. ollama pull nomic-embed-text             (embeddings)
4. Clone plugins tá»« plugin-manifest.json   (optional: user chá»n tier1/tier2)
5. Copy .env.example â†’ .env               (user Ä‘iá»n keys)
6. python ops/scripts/lightrag_server.py  (init LightRAG fresh DB)
7. Run ops/scripts/update_hud.ps1          (first HUD snapshot)
```

---

## OPTIONS PHÃ‚N PHá»I

### Option A â€” Open Source (GitHub Public)
```
Pros:  Community má»Ÿ, dá»… chia sáº», SEO tá»‘t
Cons:  Code/prompts lá»™, competitor copy Ä‘Æ°á»£c
Best for: Template/skeleton version (không có CEO data/customization)
```

### Option B â€” Private Repo + Invite
```
Pros:  Kiá»ƒm soát access, báº£o máº­t cao
Cons:  Giá»›i háº¡n collaborators (GitHub Free: 3 ngÆ°á»i)
Best for: CEO vÃ  team internal (<5 ngÆ°á»i)
```

### Option C â€” GitHub Template Repo
```
Pros:  User click "Use this template" â†’ clone vá» â†’ setup
Cons:  Cáº§n maintain 2 versions (template + CEO private)
Best for: Phân phá»‘i cho clients hoáº·c bán OmniClaw template
```

### Option D â€” Packaged Release (ZIP)
```
Pros:  Full system, không cáº§n git knowledge
Cons:  Náº·ng náº¿u include data, update khó
Best for: CEO muá»‘n trao tay cho client không tech-savvy
```

### Option E â€” Docker (TÆ°Æ¡ng lai)
```
Pros:  One-click deploy, isolate environment
Cons:  Cáº§n Docker knowledge, náº·ng image
Best for: Cloud deployment (VPS, server)
Files: docker-compose.yml + Dockerfile
Ref:  PROP_2026-03-23_OBSERVABILITY_LAYER (Ä‘ã pending)
```

---

## PHÃ‚N LOáº I USER

| User Type | Muá»‘n gÃ¬ | Solution |
|-----------|---------|---------|
| CEO (chÃ­nh mÃ¬nh) | Backup + version | Private GitHub + git push |
| Team internal | Cùng dùng | Private repo + invite + shared .env |
| Client chuyên nghiá»‡p | System Ä‘ã configured | Option D (ZIP) hoáº·c E (Docker) |
| Developer/Builder | Tá»± customize | Option A/C (template) |
| Không tech | Plug-and-play | Cáº§n build Setup Wizard (tÆ°Æ¡ng lai) |

---

## ROADMAP PUBLISH

### Phase 1 â€” Ngay bây giá» (30 phút)
```
[x] Táº¡o .gitignore chuáº©n
[x] requirements.txt (pinned)
[x] .env.example
[ ] git commit + push lên private repo
```

### Phase 2 â€” Ngáº¯n háº¡n
```
[ ] ops/scripts/setup.ps1 (bootstrap script)
[ ] README.md chuyên nghiá»‡p (install guide, architecture overview)
[ ] plugin-manifest.json (list plugins vá»›i download URL)
[ ] ops/workflows/export_ai_os_template.md (Ä‘ã có workflow nÃ y)
```

### Phase 3 â€” Trung háº¡n (khi có user khác)
```
[ ] Tách thÃ nh GitHub Template repo
[ ] Táº¡o CHANGELOG.md (version history)
[ ] Video demo / documentation site
[ ] Pricing model (náº¿u bán)
```

### Phase 4 â€” DÃ i háº¡n (scale)
```
[ ] Docker Compose full stack
[ ] One-click VPS deploy (Digital Ocean App Platform, Railway)
[ ] Setup Wizard UI (web-based)
[ ] Multi-tenant architecture (nhiá»u CEO cùng cháº¡y)
```

---

## FILES Cáº¦N LÃ€M NGAY (khi CEO quyáº¿t Ä‘á»‹nh push)

| File | Description: | Thá»i gian |
|------|-------|----------|
| `.gitignore` | Exclude plugins/, DB, secrets | 5 phút |
| `requirements.txt` | pip dependencies pinned | 5 phút |
| `.env.example` | Template keys | 5 phút |
| `ops/scripts/setup.ps1` | Bootstrap full install | 30 phút |
| `README.md` | Architecture + install guide | 20 phút |

**Tá»•ng:** ~1 giá» â†’ OmniClaw sáºµn sÃ ng distribute

---

## CÃ‚U Há»ŽI CHO BRAINSTORM (khi CEO cáº§n quyáº¿t Ä‘á»‹nh)

1. Má»¥c tiêu distribute: cho team ná»™i bá»™ hay cho client/cá»™ng Ä‘á»“ng?
2. Có muá»‘n monetize OmniClaw template không?
3. Pháº§n nÃ o cá»§a OmniClaw lÃ  "secret" (CEO customization) vÃ  pháº§n nÃ o lÃ  "template"?
4. Cloud deploy hay local-only?
5. Target user: technical (developer) hay non-technical?

---

*Plan v1.0 | 2026-03-24 | Retrieve: "omniclaw plan publish" hoáº·c Ä‘á»c file nÃ y*
*Location: brain/knowledge/notes/KI-PUBLISH-PLAN-2026-03-24.md*

