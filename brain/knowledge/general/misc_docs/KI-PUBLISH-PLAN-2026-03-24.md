---
id: ki-publish-plan-2026-03-24
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.698815
---

# OmniClaw — Distribution & Publishing Plan
# Status: DRAFT | Saved: 2026-03-24 | For: CEO Brainstorm
# Retrieve when needed: "find OmniClaw publish plan"

---

## CONTEXT

OmniClaw Corp currently runs fully locally on the CEO's machine.
Problem: The system is heavy (~GB due to plugins, vector DB, models) → cannot push raw to GitHub.
Core question: **How to distribute OmniClaw to other users?**

---

## DISTRIBUTION ARCHITECTURE (2-Tier)

### Tier 1 — GitHub Core (~5MB)
```
Includes: All code/config/markdown — NO data/models

✅ corp/           — 21 dept prompts, rules, sops
✅ brain/          — agents defs, shared-context, governance
✅ ops/            — scripts, workflows (37), configs
✅ kho/            — registries (rules/prompts/plugins/mcp/llm/agents)
✅ hud/            — HUD.md template
✅ skills/         — SKILL.md files only (no heavy code)
✅ security/       — vet_repo.ps1
✅ .env.example    — template keys (no actual values)
✅ requirements.txt — pinned dependencies
✅ README.md        — setup guide

❌ .env            — gitignore (secrets)
❌ plugins/        — gitignore (100+ repos, GB size)
❌ brain/knowledge/lightrag_db/ — gitignore (vector DB)
❌ infra/          — gitignore (Docker images, binaries)
❌ telemetry/      — gitignore (logs)
❌ security/QUARANTINE/incoming/ — gitignore (quarantine data)
```

### Tier 2 — Setup Script (user self-install)
```powershell
# ops/scripts/setup.ps1
# User clones repo → runs this script once → full system ready

1. pip install -r requirements.txt          (lightrag, mem0, supabase...)
2. ollama pull gemma2:2b                    (local LLM)
3. ollama pull nomic-embed-text             (embeddings)
4. Clone plugins from plugin-manifest.json   (optional: user chooses tier1/tier2)
5. Copy .env.example → .env               (user fills in keys)
6. python ops/scripts/lightrag_server.py  (init LightRAG fresh DB)
7. Run ops/scripts/update_hud.ps1          (first HUD snapshot)
```

---

## DISTRIBUTION OPTIONS

### Option A — Open Source (GitHub Public)
```
Pros:  Open community, easy sharing, good SEO
Cons:  Code/prompts exposed, competitors can copy
Best for: Template/skeleton version (without CEO data/customization)
```

### Option B — Private Repo + Invite
```
Pros:  Access control, high security
Cons:  Limited collaborators (GitHub Free: 3 people)
Best for: CEO and internal team (<5 people)
```

### Option C — GitHub Template Repo
```
Pros:  User clicks "Use this template" → clones → setup
Cons:  Need to maintain 2 versions (template + CEO private)
Best for: Distributing to clients or selling OmniClaw template
```

### Option D — Packaged Release (ZIP)
```
Pros:  Full system, no git knowledge needed
Cons:  Heavy if including data, difficult updates
Best for: CEO wants to hand off to non-tech-savvy client
```

### Option E — Docker (Future)
```
Pros:  One-click deploy, isolated environment
Cons:  Requires Docker knowledge, heavy image
Best for: Cloud deployment (VPS, server)
Files: docker-compose.yml + Dockerfile
Ref:  PROP_2026-03-23_OBSERVABILITY_LAYER (pending)
```

---

## USER CLASSIFICATION

| User Type | What they want | Solution |
|-----------|----------------|----------|
| CEO (myself) | Backup + version | Private GitHub + git push |
| Internal team | Shared use | Private repo + invite + shared .env |
| Professional client | Pre-configured system | Option D (ZIP) or E (Docker) |
| Developer/Builder | Self-customize | Option A/C (template) |
| Non-technical | Plug-and-play | Need to build Setup Wizard (future) |

---

## PUBLISH ROADMAP

### Phase 1 — Right now (30 minutes)
```
[x] Create standard .gitignore
[x] requirements.txt (pinned)
[x] .env.example
[ ] git commit + push to private repo
```

### Phase 2 — Short term
```
[ ] ops/scripts/setup.ps1 (bootstrap script)
[ ] Professional README.md (install guide, architecture overview)
[ ] plugin-manifest.json (list plugins with download URLs)
[ ] ops/workflows/export_ai_os_template.md (workflow already exists)
```

### Phase 3 — Medium term (when there are other users)
```
[ ] Split into GitHub Template repo
[ ] Create CHANGELOG.md (version history)
[ ] Video demo / documentation site
[ ] Pricing model (if selling)
```

### Phase 4 — Long term (scale)
```
[ ] Docker Compose full stack
[ ] One-click VPS deploy (Digital Ocean App Platform, Railway)
[ ] Setup Wizard UI (web-based)
[ ] Multi-tenant architecture (multiple CEOs running together)
```

---

## FILES TO CREATE IMMEDIATELY (when CEO decides to push)

| File | Description | Time |
|------|-------------|------|
| `.gitignore` | Exclude plugins/, DB, secrets | 5 minutes |
| `requirements.txt` | pip dependencies pinned | 5 minutes |
| `.env.example` | Template keys | 5 minutes |
| `ops/scripts/setup.ps1` | Bootstrap full install | 30 minutes |
| `README.md` | Architecture + install guide | 20 minutes |

**Total:** ~1 hour → OmniClaw ready to distribute

---

## QUESTIONS FOR BRAINSTORM (when CEO needs to decide)

1. Distribution goal: internal team or clients/community?
2. Do you want to monetize OmniClaw template?
3. Which part of OmniClaw is "secret" (CEO customization) and which is "template"?
4. Cloud deploy or local-only?
5. Target user: technical (developer) or non-technical?

---

*Plan v1.0 | 2026-03-24 | Retrieve: "omniclaw plan publish" or read this file*
*Location: brain/knowledge/notes/KI-PUBLISH-PLAN-2026-03-24.md*