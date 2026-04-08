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
ecosystem/workforce/                                  [ECO_CORE] Distributed Nodes. View Regional Maps: [Agents (115 nodes)](../../../ecosystem/workforce/agents/_REGIONAL_MAP.md) | [Subagents (37 nodes)](../../../ecosystem/workforce/subagents/_REGIONAL_MAP.md) | [Departments (28 nodes)](../../../ecosystem/workforce/departments/_REGIONAL_MAP.md) | [System](../../../ecosystem/workforce/system/_REGIONAL_MAP.md)
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


## 13. DOCUMENTED MODULES INDEX
Danh sách các Module/Thư viện có chứa tài liệu hướng dẫn (README hoặc Folder docs/):

- brain\knowledge
- brain\knowledge\bmad_repo
- brain\knowledge\claude_bp_repo
- brain\knowledge\corp\proposals
- brain\knowledge\docs
- brain\knowledge\frameworks\deer_flow
- brain\knowledge\frameworks\hermes_agent
- brain\knowledge\general\dir_quarantine
- brain\knowledge\general\misc_docs
- brain\knowledge\general\orchestrator_pro_domain\orchestrator_pro\scripts
- brain\knowledge\general\reasoning_engine_domain\reasoning_engine\scripts
- brain\knowledge\general\repo_orphan_sweep_aaai2026
- brain\knowledge\general\resilience_engine_domain\resilience_engine\scripts
- brain\knowledge\repo_hermes_agent
- brain\knowledge\repo_hyperspace_db
- brain\knowledge\repo_mempalace
- brain\knowledge\repo_orphan_sweep_acl
- brain\knowledge\repo_orphan_sweep_colm2025
- brain\knowledge\repo_orphan_sweep_docs_101008
- brain\knowledge\repo_orphan_sweep_docs_105907
- brain\knowledge\repo_orphan_sweep_examples
- brain\knowledge\repo_orphan_sweep_i18n
- brain\knowledge\repo_orphan_sweep_i18n_101008
- brain\knowledge\repo_orphan_sweep_scripts_100804
- brain\knowledge\repo_orphan_sweep_tests
- brain\knowledge\repo_orphan_sweep_tests_100807
- brain\knowledge\repo_orphan_sweep_tests_101008
- brain\knowledge\repo_orphan_sweep_tests_101212
- brain\knowledge\repo_orphan_sweep_website
- brain\knowledge\repositories\ClawRouter
- brain\knowledge\repositories\ClawTeam
- brain\knowledge\repositories\ClawWork
- brain\knowledge\repositories\ClawX
- brain\knowledge\repositories\ContribAI
- brain\knowledge\repositories\Dopamine
- brain\knowledge\repositories\agentops
- brain\knowledge\repositories\chat_quality_agent
- brain\knowledge\repositories\claude_code_game_studios
- brain\knowledge\repositories\claude_code_game_studios\.claude
- brain\knowledge\repositories\claude_code_remote
- brain\knowledge\repositories\claude_code_templates
- brain\knowledge\repositories\claude_subconscious
- brain\knowledge\repositories\code_review_graph
- brain\knowledge\repositories\codex
- brain\knowledge\repositories\codex\.devcontainer
- brain\knowledge\repositories\codymaster
- brain\knowledge\repositories\crotmail
- brain\knowledge\repositories\database_js
- brain\knowledge\repositories\developer_roadmap
- brain\knowledge\repositories\distil_text2sql
- brain\knowledge\repositories\documentation
- brain\knowledge\repositories\everything_claude_code
- brain\knowledge\repositories\everything_claude_code\.claude-plugin
- brain\knowledge\repositories\everything_claude_code\.kiro
- brain\knowledge\repositories\everything_claude_code\.kiro\hooks
- brain\knowledge\repositories\everything_claude_code\.opencode
- brain\knowledge\security
- brain\knowledge\skills_standard_repo
- brain\registry
- brain\rules
- core
- core\docs
- core\ops\scripts
- core\ops\secrets
- core\security\QUARANTINE
- core\security\QUARANTINE\incoming\repos\yt_dlp
- core\security\QUARANTINE\vetted\repos\chat_quality_agent
- core\security\QUARANTINE\vetted\repos\chat_quality_agent\frontend
- ecosystem\plugins\claude-mem
- ecosystem\plugins\notebooklm_mcp\notebooklm_mcp
- ecosystem\plugins\repo-fetched-absolufy-imports-072207
- ecosystem\plugins\repo-fetched-antigravity-mobile-035838
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\autoqa
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\autoqa\scripts
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\core
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\docs
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\docs\src\pages
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\extensions\assistant-extension
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\foundation-models-server
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\mlx-server
- ecosystem\plugins\repo-fetched-atomic-chat-035451-035604\web-app
- ecosystem\plugins\repo-fetched-jsoncrack-vscode-035842
- ecosystem\plugins\repo-fetched-jsoncrack.com-035846
- ecosystem\plugins\repo-fetched-jsoncrack.com-035846\apps\vscode
- ecosystem\plugins\repo-fetched-jsoncrack.com-035846\packages\jsoncrack-react
- ecosystem\plugins\repo-fetched-tookie-osint-034731
- ecosystem\plugins\repo-fetched-tookie-osint-034731\docs\readmelang
- ecosystem\plugins\repo_civ_fetched_claudy_registry_121551
- ecosystem\plugins\repo_civ_fetched_cli2_123057
- ecosystem\plugins\repo_civ_fetched_firecrawl_go
- ecosystem\plugins\repo_civ_fetched_firecrawl_mcp_server_124705
- ecosystem\plugins\repo_civ_fetched_gitingest_extension
- ecosystem\plugins\repo_civ_fetched_go_colorable_123058
- ecosystem\plugins\repo_civ_fetched_go_isatty_123100
- ecosystem\plugins\repo_civ_fetched_go_sqlite3_123101
- ecosystem\plugins\repo_civ_fetched_llm_lean_log_114459
- ecosystem\plugins\repo_civ_fetched_localtunnel_114458
- ecosystem\plugins\repo_civ_fetched_locomotive_scroll_114503
- ecosystem\plugins\repo_fetched_adaptive_platform_ui_135413
- ecosystem\plugins\repo_fetched_adaptive_platform_ui_135413\example
- ecosystem\plugins\repo_fetched_adaptive_platform_ui_135413\example\ios\Runner\Assets.xcassets\LaunchImage.imageset
- ecosystem\plugins\repo_fetched_adaptive_platform_ui_135413\test
- ecosystem\plugins\repo_fetched_claude_plugins_official_123528
- ecosystem\plugins\repo_fetched_claude_plugins_official_123528_123606
- ecosystem\plugins\repo_fetched_claude_plugins_official_123550
- ecosystem\plugins\repo_hexhog
- ecosystem\plugins\repo_lessmsi
- ecosystem\plugins\repo_lightrag
- ecosystem\plugins\repo_liquid_glass
- ecosystem\plugins\repo_orphan_sweep_byterover
- ecosystem\plugins\repo_orphan_sweep_hindsight
- ecosystem\plugins\repo_orphan_sweep_holographic
- ecosystem\plugins\repo_orphan_sweep_honcho
- ecosystem\plugins\repo_orphan_sweep_mem0
- ecosystem\plugins\repo_orphan_sweep_mempalace
- ecosystem\plugins\repo_orphan_sweep_openviking
- ecosystem\plugins\repo_orphan_sweep_retaindb
- ecosystem\plugins\repo_orphan_sweep_supermemory
- ecosystem\skills\repo-fetched-agent-skill-creator-052030
- ecosystem\skills\repo-fetched-agent-skill-creator-052030\references\examples\stock-analyzer
- ecosystem\skills\repo-fetched-agent-skill-creator-052030\references\templates
- ecosystem\skills\repo-fetched-agent-skills-043028
- ecosystem\skills\repo-fetched-agent-skills-043028\skills\clickhouse-best-practices
- ecosystem\skills\repo-fetched-agent-skills-054345
- ecosystem\skills\repo-fetched-agent-skills-124622
- ecosystem\skills\repo-fetched-agent-skills-124622\skills\apify-actor-development\references
- ecosystem\skills\repo-fetched-agentskills-111221
- ecosystem\skills\repo-fetched-agentskills-111221\docs
- ecosystem\skills\repo-fetched-agentskills-111221\skills-ref
- ecosystem\skills\repo-fetched-agentskills-111250
- ecosystem\skills\repo-fetched-agentskills-111250\docs
- ecosystem\skills\repo-fetched-agentskills-111250\skills-ref
- ecosystem\skills\repo-fetched-swiftui-agent-skill-035836
- ecosystem\skills\repo_civ_fetched_awesome_legal_skills_105805
- ecosystem\skills\repo_civ_fetched_claude_skill_homeassistant_104045
- ecosystem\skills\repo_civ_fetched_gah_121554
- ecosystem\skills\repo_civ_fetched_goddd_121543
- ecosystem\skills\repo_civ_fetched_lobsters_114454
- ecosystem\skills\repo_claude_code
- ecosystem\skills\repo_claude_code\examples\settings
- ecosystem\skills\repo_claude_code\plugins
- ecosystem\skills\repo_claude_code\plugins\agent-sdk-dev
- ecosystem\skills\repo_claude_code\plugins\claude-opus-4-5-migration
- ecosystem\skills\repo_claude_code\plugins\code-review
- ecosystem\skills\repo_claude_code\plugins\commit-commands
- ecosystem\skills\repo_claude_code\plugins\explanatory-output-style
- ecosystem\skills\repo_claude_code\plugins\feature-dev
- ecosystem\skills\repo_claude_code\plugins\frontend-design
- ecosystem\skills\repo_claude_code\plugins\hookify
- ecosystem\skills\repo_claude_code\plugins\learning-output-style
- ecosystem\skills\repo_claude_code\plugins\plugin-dev
- ecosystem\skills\repo_claude_code\plugins\plugin-dev\skills\command-development
- ecosystem\skills\repo_claude_code\plugins\plugin-dev\skills\hook-development\scripts
- ecosystem\skills\repo_claude_code\plugins\plugin-dev\skills\plugin-structure
- ecosystem\skills\repo_claude_code\plugins\pr-review-toolkit
- ecosystem\skills\repo_claude_code\plugins\ralph-wiggum
- ecosystem\skills\repo_fetched_agent_config_144305
- ecosystem\skills\repo_fetched_agent_skills_144258
- ecosystem\skills\repo_fetched_agent_skills_144258\skills\logging-best-practices
- ecosystem\skills\repo_fetched_claude_config_144310
- ecosystem\skills\repo_fetched_claude_scientific_skills_061121
- ecosystem\skills\repo_guardrails
- ecosystem\skills\repo_insanely_fast_whisper
- ecosystem\skills\repo_kore_memory
- ecosystem\skills\repo_orphan_sweep_benchmarks
- ecosystem\skills\repo_qwen2_5_omni
- ecosystem\skills\smart_memory\scripts
- ecosystem\skills\smart_memory\smart_memory\scripts
- ecosystem\workflows\automations\daemons\oid
- ecosystem\workflows\repo-fetched-agency-swarm-102257
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339\examples
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339\examples\fastapi_integration
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339\src\agency_swarm\integrations
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339\src\agency_swarm\ui\demos\copilot
- ecosystem\workflows\repo-fetched-agency-swarm-102257-102339\tests
- ecosystem\workflows\repo-fetched-agency-swarm-102257\.claude
- ecosystem\workflows\repo-fetched-agency-swarm-102257\examples
- ecosystem\workflows\repo-fetched-agency-swarm-102257\examples\fastapi_integration
- ecosystem\workflows\repo-fetched-agency-swarm-102257\src\agency_swarm\integrations
- ecosystem\workflows\repo-fetched-agency-swarm-102257\src\agency_swarm\ui\demos\copilot
- ecosystem\workflows\repo-fetched-agency-swarm-102257\tests
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\.changeset
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\docs\design
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\examples
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\packages\core
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\packages\plugins\notifier-discord
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\packages\plugins\notifier-openclaw
- ecosystem\workflows\repo-fetched-agent-orchestrator-044700\packages\plugins\runtime-tmux
- ecosystem\workflows\repo-fetched-agent-teams-lite-052705
- ecosystem\workflows\repo-fetched-agent-teams-lite-052705\examples\opencode\plugins
- ecosystem\workflows\repo-fetched-ai-coding-tools-120213
- ecosystem\workflows\repo-fetched-ai-coding-tools-120213\candle
- ecosystem\workflows\repo-fetched-ai-coding-tools-120213\claude-history-tool
- ecosystem\workflows\repo-fetched-ai-coding-tools-120213\mcp-cli
- ecosystem\workflows\repo-fetched-ai-coding-tools-120220
- ecosystem\workflows\repo-fetched-ai-coding-tools-120220\candle
- ecosystem\workflows\repo-fetched-ai-coding-tools-120220\claude-history-tool
- ecosystem\workflows\repo-fetched-ai-coding-tools-120220\mcp-cli
- ecosystem\workflows\repo-fetched-formcn-034209
- ecosystem\workflows\repo-fetched-formcn-034453
- ecosystem\workflows\repo-fetched-formcn-034736
- ecosystem\workflows\repo-fetched-open-higgsfield-ai-034330
- ecosystem\workflows\repo-fetched-open-higgsfield-ai-034601
- ecosystem\workflows\repo-fetched-open-higgsfield-ai-034914
- ecosystem\workflows\repo-fetched-taipy-035751
- ecosystem\workflows\repo-fetched-taipy-035751\doc\gui\examples
- ecosystem\workflows\repo-fetched-taipy-035751\doc\gui\extension
- ecosystem\workflows\repo-fetched-taipy-035751\frontend
- ecosystem\workflows\repo-fetched-taipy-035751\frontend\taipy
- ecosystem\workflows\repo-fetched-taipy-035751\frontend\taipy-gui
- ecosystem\workflows\repo-fetched-taipy-035751\taipy\common
- ecosystem\workflows\repo-fetched-taipy-035751\taipy\core
- ecosystem\workflows\repo-fetched-taipy-035751\taipy\gui
- ecosystem\workflows\repo-fetched-taipy-035751\taipy\rest
- ecosystem\workflows\repo-fetched-taipy-035751\taipy\templates
- ecosystem\workflows\repo-fetched-taipy-035751\tools
- ecosystem\workflows\repo_civ_fetched_awesome_eventstorming_121545
- ecosystem\workflows\repo_civ_fetched_claudy_releases_121553
- ecosystem\workflows\repo_civ_fetched_kubernetes_104131
- ecosystem\workflows\repo_civ_fetched_langgraph_105719
- ecosystem\workflows\repo_civ_fetched_llmware_112844
- ecosystem\workflows\repo_fetched_100_dathere_com_161900
- ecosystem\workflows\repo_fetched_9router_165252
- ecosystem\workflows\repo_fetched_agent_os_145840
- ecosystem\workflows\repo_homebrew_core
- ecosystem\workflows\repo_kong
- ecosystem\workflows\repo_litgpt
- ecosystem\workflows\repo_litserve
- ecosystem\workflows\repo_orphan_sweep_tblite
- ecosystem\workforce\subagents\chief-of-staff

### ecosystem/workforce
- ecosystem/workforce/subagents/chief-of-staff
- ecosystem/workforce/system
