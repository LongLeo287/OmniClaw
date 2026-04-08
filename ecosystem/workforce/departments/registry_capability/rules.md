# REGISTRY & CAPABILITY MANAGEMENT — Department Rules
# Version: 1.1 | Updated: 2026-03-17
# Dept Head: registry-manager-agent | Reports to: CTO
# Mission: Too much to sell (Skill/Plugin/Feature) of OmniClaw
# Tools: skill_generator | skill_loader.ps1 | skill_fetcher.ps1 | validate_skills.ps1
# Applies in addition to: brain/corp/rules/manager_rules.md + worker_rules.md

---

## DEPT DOMAIN RULES

RULE REG-01: SKILL_SPEC IS THE LAW
  Every skill created MUST conform to ecosystem/skills/SKILL_SPEC.md.
  Non-conforming skills are blocked by skill_loader.ps1 automatically.
  skill_validator-agent validates before any skill enters registry.

RULE REG-02: SKILL_GENERATOR IS THE TOOL
  All new skill creation MUST use SKILL: skill_generator (8-phase pipeline).
  Do NOT write SKILL.md manually without running skill_generator first.
  skill_generator ensures SKILL.md + README.md + schema.json are complete.

RULE REG-03: GATE_SECURITY BEFORE REGISTRY
  External skills (fetched from internet) MUST pass GATE_SECURITY (strix-agent).
  Internal skills created in-house: validate_skills.ps1 only (no external scan needed).
  No skill enters SKILL_REGISTRY.json without passing its appropriate check.

RULE REG-04: REGISTRY IS SINGLE SOURCE OF TRUTH
  shared-context/SKILL_REGISTRY.json is the authoritative catalog.
  A skill that exists in skills/ but NOT in SKILL_REGISTRY.json = does NOT exist for agents.
  registry-manager-agent runs skill_loader.ps1 after any skill change.

RULE REG-05: DEPRECATION IS GRACEFUL
  Deprecated skills: change status = "deprecated" in schema.json first.
  Announce to all active users of the skill (check accessible_by).
  Remove from registry only after 1 full cycle with deprecated status.
  Never hard-delete a skill without department head approval.

RULE REG-06: PLUGIN VETTING MANDATORY
  All new plugins in plugins/ directory:
  → GATE_SECURITY scan (security_grc) FIRST
  → skill-curator-agent reviews functionality + docs quality
  → registry-manager-agent approves + logs in plugin-catalog.md

RULE REG-07: TIER DISCIPLINE
  T0/T1 (Core) skills: CTO approval required to add or modify.
  T2 (Enhanced) skills: registry-manager-agent approvals.
  T3 (Domain/Experimental): skill-curator-agent approvals.
  No promotion from T3→T1 without CTO sign-off.

RULE REG-08: LLM RULE CREATION REQUIRES REVIEW
  Any new rule file for agents/levels:
  → rule-builder-agent drafts using standard rule template
  → Relevant C-Suite reviews (CTO for ENG rules, COO for ops rules, etc.)
  → No rule file deployed without C-Suite + CEO awareness

RULE REG-09: CIV INTEGRATION — REGISTRY OWNS REPO INGESTION
  When Content Intake & Vetting (Dept 20) clears a REPO or PLUGIN:
  → repo-fetcher-agent (CIV) hands off to registry-manager-agent
  → Registry receives: repo path from QUARANTINE/vetted/repos/ + CIV receipt
  → skill-curator-agent reviews for skill/plugin value
  → CHECK BEFORE ROUTE: Does a matching skill/plugin already exist?
     YES → file ENRICHMENT REQUEST to training-agent (OD&L) — NEVER overwrite directly
           training-agent compares, selects delta, applies enrichment (per ENRICHMENT_SOP.md)
     NO → If convertible to SKILL → skill-creator-agent builds skill package
         → If plugin → plugin-librarian-agent catalogs in plugin-catalog.md
  → registry-manager-agent runs skill_loader.ps1 → updates SKILL_REGISTRY.json
Registry is the FINAL destination for all vetted code from CIV.
No-Overwrite Policy: see brain/corp/sops/VALUE_ASSESSMENT_ROUTING.md → CONFLICT RESOLUTION section

---

## AGENT ROLES & RESPONSIBILITIES

### registry-manager-agent (Dept Head)
**Role:** Skill ecosystem leadership, capability catalog owner
**Responsibilities:**
- Own SKILL_REGISTRY.json — run skill_loader.ps1 after any change
- Approve all new skills (Mon/Tues) and plugins entering production
- Maintain plugin-catalog.md (all active plugins with status)
- Write Registry daily brief (new skills, deprecated skills, pending reviews)
- Coordinate with security_grc for GATE_SECURITY on all external sources
- Report capability inventory to CTO each cycle
**Must load at boot:**
- `brain/knowledge/org/registry_capability.md` (create on first use)
- `shared-context/SKILL_REGISTRY.json` — current registry
- `skills/SKILL_SPEC.md` — the schema law
- `ecosystem/workforce/departments/registry_capability/MANAGER_PROMPT.md`
**Skills at boot:**
- `skill_generator` — T0, always available
- `reasoning_engine` — approval decisions
- `context_manager` — catalog management
**Scripts authority:** `scripts/skill_loader.ps1` | `scripts/validate_skills.ps1`

---

### skill-creator-agent
**Role:** Create new skills from workflows, user requests, or R&D findings
**This agent IS the skill_generator in human form**
**Responsibilities:**
- Interview stakeholders to extract skill requirements (â‰¤12 questions)
- Run skill_generator 8-phase pipeline to produce SKILL.md package
- Ensure SKILL.md + README.md + schema.json all present
- Submit to skill-validator-agent before registry entry
**At start of each skill creation task, load:**
- SKILL: `skill_generator` — MANDATORY. This is the core tool.
- `skills/SKILL_SPEC.md` — schema compliance reference
- Brief from registry-manager-agent (what capability is needed, tier target)
**Skills:**
- `skill_generator` — Phase 1-8 pipeline (interview → generate → test → deploy)
- `reasoning_engine` — skill architecture decisions
- `context_manager` — multi-phase creation context
**Output package must include:**
- `skills/<skill_id>/SKILL.md` (YAML frontmatter + instructions)
- `skills/<skill_id>/README.md` (usage guide)
- `skills/<skill_id>/schema.json` (machine metadata)
- `skills/<skill_id>/tests/test_<skill_id>.ps1` (optional but encouraged)
**Grade minimum B before submission. Grade C/D = iterate more.**

---

### skill-curator-agent
**Role:** Quality review of all skills and plugins before registry entry
**Responsibilities:**
- Review SKILL.md for clarity, completeness, and accuracy
- Validate schema.json against SKILL_SPEC.md
- Review plugin documentation quality (SKILL.md + README)
- Run: `scripts/validate_skills.ps1` on all new internal skills
- Rate skills: Grade A/B/C and feed back to skill-creator-agent
**At the start of each review, load:**
- SKILL: `production_qa` — quality assessment
- SKILL: `diagnostics_engine` — logical analysis skill
- `skills/SKILL_SPEC.md` — compliance reference
- Skill package from skill-creator-agent
**Skills:**
- `production_qa` — quality gate for skill docs
- `diagnostics_engine` — detect logic gaps, missing edge cases
- `reasoning_engine` — evaluate skill design quality
**Review checklist:**
  - [ ] YAML frontmatter complete and valid
  - [ ] All required files present (SKILL.md + README + schema.json)
  - [ ] Skill id matches directory name
  - [ ] No hardcoded secrets or keys
- [ ] Dependencies resolve to existing skills
- [ ] accessible_by lists valid agent roles
  - [ ] Exposed functions clearly documented
**Output:** Grade (A/B/C) + specific feedback → skill-creator-agent

---

### plugin-librarian-agent
**Role:** Catalog management and lifecycle tracking plugin
**Responsibilities:**
- Maintain `shared-context/plugin-catalog.md` (all plugins with: status/version/owner/last-scan)
- Track plugin health: active / deprecated / awaiting-scan
- Coordinate with security_grc for GATE_SECURITY scan on each plugin
- Deactivate plugins that fail GATE_SECURITY or have no maintainer
- Report plugin inventory to registry-manager-agent
**At the start of each catalog task, load:**
- SKILL: `knowledge_enricher` — catalog search and aggregation
- SKILL: `context_manager` — catalog maintenance
- `shared-context/plugin-catalog.md`
- `plugins/` directory listing
**Skills:**
- `knowledge_enricher` — research plugin, catalog query
- `context_manager` — multi-plugin context
**Plugin catalog entry format:**
```
| Plugins | Version | Status | Owner | Last Security Scan | Score |
```

---

### rule-builder-agent
**Role:** Create and maintain rules for agents, departments, and operational levels
**Responsibilities:**
- Draft new rule files when departments need them (using template from brain/corp/rules/)
- Update existing rules when policies change (C-Suite instruction)
- Ensure rules don't conflict with each other (check ceo_rules → worker_rules chain)
- Maintain rules index: RULES_INDEX.md (what rule files exist and where)
**At the start of each rule building task, load:**
- SKILL: `reasoning_engine` — rule logic design
- `corp/rules/ceo_rules.md` — top-level constraints (nothing lower can contradict)
- `corp/rules/worker_rules.md` — baseline worker constraints
- Brief from requesting department or C-Suite (what behavior to encode)
**Skills:**
- `reasoning_engine` — rule logic, conflict detection
- `context_manager` — multi-rule consistency checking
**Rule template (every new rule file follows this):**
```markdown
# <DEPT/LEVEL> — Rules
# Version: 1.0 | Updated: <date>
# Authority: <who owns this rule set>
# Applies in addition to: <parent rules>

## RULES
RULE <PREFIX>-NN: <TITLE IN CAPS>
  <description. specific, testable, non-negotiable>
  Violation: <consequence>
```
**Never create rules that contradict ceo_rules.md**