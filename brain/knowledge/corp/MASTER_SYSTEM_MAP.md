---
id: master_system_map
type: corp_document
registered: true
---

# OmniClaw -- Master System Map
# Version: 2.0 | Date: 2026-03-24 | Owner: Antigravity
# Authority: Tier 0 -- Single Source of Truth for all operational flows
# NOTE: v2.0 rewritten clean UTF-8 (v1.0 had cp1252 corruption)

---

## 1. BOOT SEQUENCE

Using Antigravity? --> Read GEMINI.md   (loads FIRST every session)
Using Claude Code? --> Read CLAUDE.md

Antigravity: GEMINI.md -> AI_OS_CONTEXT.md -> blackboard.json -> SKILL_REGISTRY.json
Claude Code: CLAUDE.md -> SOUL.md -> GOVERNANCE.md -> AGENTS.md -> blackboard.json

---

## 2. CORP DAILY CYCLE (8 Phases)

Trigger: "omniclaw corp start" | Ref: core/ops/workflows/corp-daily-cycle.md

Phase 0: SYSTEM HEALTH (ports, blackboard, skill-discovery-auto)
Phase 1: CEO BRIEF (mission, kpi, escalations, proposals)
Phase 2: C-SUITE PLANNING (depts goals -> blackboard)
Phase 3: DEPT HEADS EXECUTE (21 dept briefs)
Phase 4: WORKER EXECUTION (tasks -> receipts)
Phase 5: QA GATE (core/ops/workflows/qa-gate.md)
Phase 6: CEO REVIEW (-> decisions_log.md)
Phase 7: RETRO & RESET (RETRO_<date>.md, kpi update, IDLE reset)
Phase 8: SKILL HARVEST (skill-discovery-auto -> SKILL_REGISTRY update)

---

## 3. DEPT STRUCTURE -- 21 Departments

TIER 0: EXECUTIVE
  CEO (Human) | C-Suite: CFO, COO, CMO, CTO

TIER 1: CORE BUSINESS (11 depts)
  01 Engineering         backend-architect-agent   [AUTONOMOUS]
  02 QA Testing          test-manager-agent        [GATE]
  03 IT Infra            it-manager-agent          [AUTONOMOUS]
  04 Marketing           growth-agent              [AUTONOMOUS]
  05 Support             channel-agent             [AUTONOMOUS]
  06 HR & People         hr-manager-agent          [GATE]
  07 core/security/GRC        strix-agent               [GATE -- ALL new tools]
  08 Finance             cost-manager-agent        [GATE]
  09 Planning/PMO        pmo-agent                 [AUTONOMOUS]
  10 Monitoring          monitor-agent             [AUTONOMOUS]
  11 Operations          ops-agent                 [AUTONOMOUS]

TIER 2: SPECIALIZED (7 depts)
  12 Legal               legal-agent               [GATE]
  13 R&D                 rd-lead-agent             [AUTONOMOUS]
  14 OD/Learning         learning-agent            [AUTONOMOUS]
  15 Client Reception    reception-agent           [AUTONOMOUS]
  16 Strategy            product-manager-agent     [GATE]
  17 System Health       system-health-agent       [AUTONOMOUS]
  18 Content Review      review-chief-agent        [GATE]

TIER 3: GOVERNANCE (3 depts)
  19 Content Intake/CIV  civ-agent                 [GATE 1 -- All External]
  20 Registry/Capability registry-manager-agent    [AUTONOMOUS]
  21 Asset Library       library-manager-agent     [AUTONOMOUS]

TIER 4: FACILITY (1 dept)
  22 Cleanup & Sanitation facility-agent           [AUTONOMOUS] -- Skill: facility_cleanup

---

## 4. PLUGIN TIERS (RULE-TIER-01)

TIER 1 (always on): Mem0, Firecrawl, LightRAG, CrewAI, GitNexus
TIER 2 (lazy-load): vibe-kanban, agentune, tai-video, etc.
TIER 3 (blacklisted): Conflict with Tier 1 -- abort on detection

---

## 5. CIV PIPELINE v1.2

Rule: RULE-CIV-01 in GEMINI.md + CLAUDE.md
Ref:  core/ops/workflows/content-intake-flow.md

STEP 0: LightRAG :9621 local check
STEP 1: CIV ticket -> vault/QUARANTINE/incoming/<type>/
STEP 2: classifier-agent -> REPO|WEB|DOC|IMAGE|TEXT|PLUGIN
STEP 3A (REPO): vet_repo.ps1 (12-stage) + strix scan
STEP 3.5: content-analyst (open-notebook :5055 OR Claude Code fallback) -- 6 Qs
STEP 3.6: GAP PROPOSAL -> CEO Telegram [A/B/C/D] (ASYNC)
STEP 4: content-validator -> quality score + VALUE_TYPE (9 types)
STEP 5: ingest-router -> skill-discovery-auto + knowledge-distribution-flow

---

## 6. COMMAND MAP

omniclaw corp start    -> corp-daily-cycle.md (full 8 phases)
omniclaw corp brief    -> Phase 1 CEO BRIEF only
omniclaw ingest <url>  -> content-intake-flow.md
omniclaw skill health  -> skill-discovery-auto.md
omniclaw retro         -> corp-learning-loop.md
Any link/repo/URL -> RULE-CIV-01 (auto-trigger CIV)

---

## 7. SKILLS (14 installed)

Registry: brain/shared-context/SKILL_REGISTRY.json
Fast Index: brain/shared-context/FAST_INDEX.json

agent-shield | agentshield | agentune | context7 | continuous-learning-v2
ecc-patterns | framework-standards | git-mcp | observability | sequential-thinking
tai-video | trivy | understand-anything | vibe-kanban

---

## 8. SERVICES

Ollama        :11434  LIVE   (gemma2:2b + nomic-embed-text)
ClawTask API  :7474   LIVE   (8 modules: llm,ollama,bot,notebook,setup,gitnexus,ag_auto,deepagents)
GitNexus      :4747   LIVE   (local code graph — ecocore/tools/gitnexus/gitnexus_server.py)
ag-auto-accept :7476  LIVE   (subprocess auto-accept — ecocore/tools/ag-auto-accept/ag_auto_accept.py)
DeepAgents ACP :8765  LIVE   (agent comms protocol — ecocore/ecocore/plugins/deepagents/main.py)
LightRAG      :9621   START: python core/ops/scripts/lightrag_server.py
open-notebook :5055   FALLBACK: Claude Code RESEARCHER role
Langfuse/LobeChat    [ASSIMILATED] -> monitor-agent & channel-agent (Plug & Play Strategy)

---

## 9. NOTIFICATIONS

Ref: core/ops/workflows/notification-bridge.md
Config: .env TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID (@aios_corp_bot)

Alert -> Telegram | blackboard.json | escalations.md | core/telemetry/receipts/
Types: GAP_PROPOSAL, SECURITY_ALERT, CIV_COMPLETE, SYSTEM_ERROR, ...

---

## 10. CANONICAL PATHS

brain/shared-context/brain/corp/kpi_scoreboard.json
brain/shared-context/brain/corp/escalations.md
brain/shared-context/brain/corp/mission.md
brain/shared-context/brain/corp/proposals/
brain/shared-context/brain/corp/daily_briefs/
brain/shared-context/blackboard.json
brain/shared-context/SKILL_REGISTRY.json
brain/corp/memory/departments/<dept>.md
brain/corp/memory/global/decisions_log.md
brain/corp/memory/global/gaps_register.md
brain/corp/gaps/GAP-<date>-<domain>.md
brain/corp/gaps/GAP-2026-04-07-vault-recursion.md     [NEW] Vault recursion anti-pattern — RULE-ARCH-01/02/03
vault/QUARANTINE/
vault/archives/                                       [GLACIER] Legacy systems, heavy ZIP backups, dead letters
vault/assets/databases/_DIR_IDENTITY.md               [RULE-ARCH-02] Constraint lock for database zone
core/bridge/                                          [GATEWAY] Remote Bridge API, Customs, Passport Issuer
core/daemons/                                         [NERVOUS_SYSTEM] The 9 resident AI Daemons (7 Pillars, 2 Sub-Guards)
core/config/                                          [REGISTRY] Centralized deployment parameters and env configs
core/docs/                                            [PUBLIC] User-facing documentation (Front Door)
core/docs/_DIR_IDENTITY.md                            Identity card and bilingual policy
ecosystem/workforce/agents/                           [[OER_MAPPED] 107 Autonomous Agent nodes - View Regional Map](../../../ecosystem/workforce/agents/_REGIONAL_MAP.md)
ecosystem/workforce/subagents/                        [[OER_MAPPED] 37 Ephemeral Single-Task Subagent nodes - View Regional Map](../../../ecosystem/workforce/subagents/_REGIONAL_MAP.md)
core/docs/README.md                                   Entry point — doc index (English)
core/docs/README-vn.md                                Entry point — doc index (Vietnamese)
core/docs/architecture/                               System architecture docs
core/docs/usage_guides/                               How-to guides for users
core/docs/workflows/                                  Operational workflow docs
core/telemetry/receipts/
core/telemetry/civ_pipeline_state/
brain/knowledge/ki_snapshots/
brain/knowledge/library/github_archives/
brain/knowledge/library/legacy_python_ops/
brain/knowledge/library/legacy_agent_memories/
brain/knowledge/library/legacy_orphan_archives/
core/ops/scripts/utils/
core/ops/scripts/utils/safe_fs.py                     [RULE-FS-01] Safe rename/merge for Windows NTFS
core/ops/scripts/utils/db_hygiene_sweep.py            [RULE-ARCH-03] Watchdog — auto-purge forbidden dirs in databases/
AOS_ROOT: $OMNICLAW_ROOT

---

## 11. HANDOFF PROTOCOL

Ref: core/ops/workflows/claude-code-handoff.md

Antigravity -> Claude Code:
  blackboard.json handoff_trigger:ACTIVE + target_agent:Claude Code
  ecocore/workforce/agents/mq/claude_code_tasks.md (task detail)

Claude Code unique capabilities:
  bash execution | sub-agents isolated context | 200K code gen | DEVELOPER->QA self-review

Claude Code -> Antigravity:
  blackboard.json handoff_trigger:COMPLETE + target_agent:Antigravity

---

*v2.0 | 2026-03-24 | Clean UTF-8 rewrite*

---

## 12. ASSIMILATED FORGERS & INTEGRATORS (LEGACY V3.1)

Ref: `core/ops/scripts/legacy_forgers/` and `core/ops/scripts/integrators/`

Sau quá trình thanh lọc OAP, các siêu công cụ sinh học từ AI OS cũ đã được đồng hóa thành công vào mạng lưới OmniClaw:
- **Legacy Forgers**: `agent_generator.js`, `skill_creator_ultra.js`
- **Integrators**: `wire_repo_demand.py`, `register_skills.py`, `batch_clone.py`, `check_repos.py`

