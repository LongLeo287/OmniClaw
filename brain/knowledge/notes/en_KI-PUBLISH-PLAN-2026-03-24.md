---
id: ki-publish-plan-2026-03-24
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.718450
---

# OmniClaw — Distribution & Publishing Plan
# Status: DRAFT | Saved: 2026-03-24 | For: CEO Brainstorm
# Retrieve when needed: "find omniclaw publish plan"

---

## CONTEXT

OmniClaw Corp currently runs fully local on the CEO's machine.
Problem: the system is heavy (~GB due to plugins, vector DB, models) → cannot push raw to GitHub.
Core question: **How to distribute OmniClaw to other users?**

---

## DISTRIBUTION ARCHITECTURE (2-Tier)

### Tier 1 — GitHub Core (~5MB)
'''
Includes: All code/config/markdown — NO data/models

✅ corp/           — 21 dept prompts, rules, sops
✅ brain/          — agents defs, shared-context, governance
✅ ops/            — scripts, workflows (37), configs
✅ kho/            — registries (rules/prompts/plugins/mcp/llm/agents)
✅ hud/            — HUD.md template
✅ skills/         — SKILL.md files only (no heavy code)
✅ security/       — vet_repo.ps1
✅ .env.example    — template keys (no real values)
✅ requirements.txt — pinned dependencies
✅ README.md        — setup guide

❌ .env            — gitignore (secrets)
❌ plugins/        — gitignore (100+ repos, GB size)
❌ brain/knowledge/lightrag_db/ — gitignore (vector DB)
❌ infra/          — gitignore (Docker images, binaries)
❌ telemetry/      — gitignore (logs)
❌ security/QUARANTINE/incoming/ — gitignore (quarantine data)
'''

### Tier 2 — Setup Script (user-installed)
'''powershell
# ops/scripts/setup.ps1
# User clones repo → runs this script once → full system ready

1. pip install -r requirements.txt          (lightrag, mem0, supabase...)
2. ollama pull gemma2:2b                    (local LLM)
3. ollama pull nomic-embed-text             (embeddings)
4. Clone plugins from plugin-manifest.json   (optional: user chooses tier1/tier2)
5. Copy .env.example → .env               (user fills in keys)
6. python ops/scripts/lightrag_server.py  (init LightRAG fresh DB)
7. Run ops/scripts/update_hud.ps1          (first HUD snapshot)
'''

---

## DISTRIBUTION OPTIONS

### Option A — Open Source (GitHub Public)
'''
Pros:  Open community, easy sharing, good SEO
Cons:  Code/prompts exposed, competitors can copy
Best for: Template/skeleton version (no CEO data/customization)
'''

### Option B — Private Repo + Invite
'''
Pros:  Controlled access, high security
Cons:  Limited collaborators (GitHub Free: 3 people)
Best for: CEO and internal team (<5 people)
'''

### Option C — GitHub Template Repo
'''
Pros:  User clicks "Use this template" → clones to their account → setups
Cons:  Need to maintain 2 versions (template + CEO private)
Best for: Distributing to clients or selling OmniClaw templates
'''

### Option D — Packaged Release (ZIP)
'''
Pros:  Full system, no git knowledge required
Cons:  Heavy if data is included, updates are difficult
Best for: CEO wants to hand over to a non-tech-savvy client
'''

### Option E — Docker (Future)
'''
Pros:  One-click deploy, isolated environment
Cons:  Requires Docker knowledge, heavy image
Best for: Cloud deployment (VPS, server)
Files: docker-compose.yml + Dockerfile
Ref:  PROP_2026-03-23_OBSERVABILITY_LAYER (already pending)
'''

---

## USER CLASSIFICATION

| User Type | What they want | Solution |
|---|---|---|
| CEO (myself) | Backup + versioning | Private GitHub + git push |
| Internal team | Use together | Private repo + invite + shared .env |
| Professional client | Pre-configured system | Option D (ZIP) or E (Docker) |
| Developer/Builder | Customize themselves | Option A/C (template) |
| Non-tech | Plug-and-play | Need to build a Setup Wizard (future) |

---

## PUBLISH ROADMAP

### Phase 1 — Right now (30 minutes)
'''
[x] Create standard .gitignore
[x] requirements.txt (pinned)
[x] .env.example
[ ] git commit + push to private repo
'''

### Phase 2 — Short-term
'''
[ ] ops/scripts/setup.ps1 (bootstrap script)
[ ] Professional README.md (install guide, architecture overview)
[ ] plugin-manifest.json (list of plugins with download URLs)
[ ] ops/workflows/export_ai_os_template.md (this workflow already exists)
'''

### Phase 3 — Mid-term (when there are other users)
'''
[ ] Split into a GitHub Template repo
[ ] Create CHANGELOG.md (version history)
[ ] Video demo / documentation site
[ ] Pricing model (if selling)
'''

### Phase 4 — Long-term (scale)
'''
[ ] Docker Compose full stack
[ ] One-click VPS deploy (Digital Ocean App Platform, Railway)
[ ] Setup Wizard UI (web-based)
[ ] Multi-tenant architecture (multiple CEOs running simultaneously)
'''

---

## FILES TO DO IMMEDIATELY (when CEO decides to push)

| File | Description: | Time |
|---|---|---|
| `.gitignore` | Exclude plugins/, DB, secrets | 5 minutes |
| `requirements.txt` | Pinned pip dependencies | 5 minutes |
| `.env.example` | Template keys | 5 minutes |
| `ops/scripts/setup.ps1` | Bootstrap full install | 30 minutes |
| `README.md` | Architecture + install guide | 20 minutes |

**Total:** ~1 hour → OmniClaw is ready for distribution

---

## QUESTIONS FOR BRAINSTORMING (when CEO needs to decide)

1.  Distribution goal: for the internal team or for clients/community?
2.  Do you want to monetize the OmniClaw template?
3.  Which parts of OmniClaw are "secret" (CEO customization) and which are "template"?
4.  Cloud deploy or local-only?
5.  Target user: technical (developer) or non-technical?

---

*Plan v1.0 | 2026-03-24 | Retrieve: "omniclaw plan publish" or read this file*
*Location: brain/knowledge/notes/KI-PUBLISH-PLAN-2026-03-24.md*
