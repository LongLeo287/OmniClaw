---
id: ki-publish-plan-2026-03-24
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.718450
---

# OmniClaw â€” Distribution & Publishing Plan
# Status: DRAFT | Saved: 2026-03-24 | For: CEO Brainstorm
# Retrieve when needed: "find omniclaw publish plan"

---

## CONTEXT

OmniClaw Corp currently runs fully local on the CEO's machine.
Problem: the system is heavy (~GB due to plugins, vector DB, models) â†’ cannot push raw to GitHub.
Core question: **How to distribute OmniClaw to other users?**

---

## DISTRIBUTION ARCHITECTURE (2-Tier)

### Tier 1 â€” GitHub Core (~5MB)
'''
Includes: All code/config/markdown â€” NO data/models

âœ… corp/           â€” 21 dept prompts, rules, sops
âœ… brain/          â€” agents defs, brain/memory, governance
âœ… ops/            â€” scripts, workflows (37), configs
âœ… kho/            â€” registries (rules/prompts/plugins/mcp/llm/agents)
âœ… hud/            â€” HUD.md template
âœ… skills/         â€” SKILL.md files only (no heavy code)
âœ… security/       â€” vet_repo.ps1
âœ… .env.example    â€” template keys (no real values)
âœ… requirements.txt â€” pinned dependencies
âœ… README.md        â€” setup guide

âŒ .env            â€” gitignore (secrets)
âŒ plugins/        â€” gitignore (100+ repos, GB size)
âŒ brain/knowledge/lightrag_db/ â€” gitignore (vector DB)
âŒ infra/          â€” gitignore (Docker images, binaries)
âŒ telemetry/      â€” gitignore (logs)
âŒ security/QUARANTINE/incoming/ â€” gitignore (quarantine data)
'''

### Tier 2 â€” Setup Script (user-installed)
'''powershell
# ops/scripts/setup.ps1
# User clones repo â†’ runs this script once â†’ full system ready

1. pip install -r requirements.txt          (lightrag, mem0, supabase...)
2. ollama pull gemma2:2b                    (local LLM)
3. ollama pull nomic-embed-text             (embeddings)
4. Clone plugins from plugin-manifest.json   (optional: user chooses tier1/tier2)
5. Copy .env.example â†’ .env               (user fills in keys)
6. python ops/scripts/lightrag_server.py  (init LightRAG fresh DB)
7. Run ops/scripts/update_hud.ps1          (first HUD snapshot)
'''

---

## DISTRIBUTION OPTIONS

### Option A â€” Open Source (GitHub Public)
'''
Pros:  Open community, easy sharing, good SEO
Cons:  Code/prompts exposed, competitors can copy
Best for: Template/skeleton version (no CEO data/customization)
'''

### Option B â€” Private Repo + Invite
'''
Pros:  Controlled access, high security
Cons:  Limited collaborators (GitHub Free: 3 people)
Best for: CEO and internal team (<5 people)
'''

### Option C â€” GitHub Template Repo
'''
Pros:  User clicks "Use this template" â†’ clones to their account â†’ setups
Cons:  Need to maintain 2 versions (template + CEO private)
Best for: Distributing to clients or selling OmniClaw templates
'''

### Option D â€” Packaged Release (ZIP)
'''
Pros:  Full system, no git knowledge required
Cons:  Heavy if data is included, updates are difficult
Best for: CEO wants to hand over to a non-tech-savvy client
'''

### Option E â€” Docker (Future)
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

### Phase 1 â€” Right now (30 minutes)
'''
[x] Create standard .gitignore
[x] requirements.txt (pinned)
[x] .env.example
[ ] git commit + push to private repo
'''

### Phase 2 â€” Short-term
'''
[ ] ops/scripts/setup.ps1 (bootstrap script)
[ ] Professional README.md (install guide, architecture overview)
[ ] plugin-manifest.json (list of plugins with download URLs)
[ ] ops/workflows/export_ai_os_template.md (this workflow already exists)
'''

### Phase 3 â€” Mid-term (when there are other users)
'''
[ ] Split into a GitHub Template repo
[ ] Create CHANGELOG.md (version history)
[ ] Video demo / documentation site
[ ] Pricing model (if selling)
'''

### Phase 4 â€” Long-term (scale)
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

**Total:** ~1 hour â†’ OmniClaw is ready for distribution

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

