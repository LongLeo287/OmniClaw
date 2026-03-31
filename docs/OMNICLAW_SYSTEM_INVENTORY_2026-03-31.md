# OmniClaw System Inventory
**Date:** 2026-03-31 | **Version:** v12.0.0 | **Cycle:** 11

Complete inventory of all workflows, pipelines, SOPs, automations, skills, and bridge/API components in the OmniClaw system.

---

## 1. WORKFLOWS (`ecosystem/workflows/`)

### Corp Operations (53 total)

| File | Purpose |
|------|---------|
| `antigravity-boot.md` | Antigravity session boot protocol — loads full OmniClaw Corp state |
| `corp-daily-cycle.md` | Daily corp operational cycle (SRE, CEO handoffs) |
| `corp-learning-loop.md` | Retro & learning loop trigger (`aos corp retro`) |
| `pre-session.md` | Pre-session freshness checks SOP |
| `claude-code-handoff.md` | Handoff protocol from Antigravity → Claude Code |
| `knowledge-ingest.md` | Knowledge ingest pipeline (`aos ingest <source>`) |
| `agent-auto-create.md` | Auto-create agent profile from domain gap analysis |
| `create-dept.md` | Create new department workflow |
| `repo-catalog-update.md` | Weekly master repo catalog update |
| `skill-install.md` | Install new skill into SKILL_REGISTRY |
| `plugin-install.md` | Install new plugin into PLUGIN_REGISTRY |
| `agent-task-dispatch.md` | Dispatch tasks to agents via blackboard |
| `client-intake.md` | Client intake (CIV) gateway |
| `security-audit.md` | Security audit workflow |
| `backup-restore.md` | Backup and restore procedures |
| `deployment-checklist.md` | Deployment pre-flight checklist |
| `escalation-protocol.md` | L1/L2/L3 escalation handling |
| `post-session.md` | Post-session shutdown and state save |
| `onboarding.md` | New agent/team member onboarding |
| `ontology-update.md` | Update knowledge graph ontology |

### Pipeline Workflows (8 core pipelines)

| Pipeline | Trigger | Flow |
|----------|---------|------|
| `knowledge-ingest.md` | `aos ingest <source>` or file_created in vault | Crawl → Parse → LightRAG index → mem0 store → Link entities |
| `agent-auto-create.md` | Domain gap detected by auto_evolution_engine | Gap analysis → Profile gen → AGENTS.md update → Register skill |
| `create-dept.md` | Missing department detected | Create dept YAML → assign agents → GOVERNANCE.md update |
| `repo-catalog-update.md` | Weekly cron (Monday 00:00) | GitHub API check → version delta → rebuild catalog → notify CEO |
| `client-intake.md` | CEO provides link/repo | CIV Format 6 → blackboard task → Claude Code queue |
| `security-audit.md` | On-demand / scheduled | Scan configs → check secrets → validate auth → report |
| `ontology-update.md` | Knowledge ingest completion | Extract entities → link graph → purge orphans |
| `corp-daily-cycle.md` | `aos corp start` | Pulse check → KPI review → task queue → CEO briefing |

---

## 2. SOPs (`brain/brain/corp/sops/` and `brain/knowledge/notes/`)

| SOP | File | Scope |
|-----|------|-------|
| CLIENT_INTAKE_GATEWAY | `brain/brain/corp/sops/CLIENT_INTAKE_GATEWAY.md` | CIV intake for repos/links |
| RULE-STORAGE-01 | `brain/knowledge/notes/RULE-STORAGE-01-storage-location.md` | Where files go |
| RULE-STRUCTURE-01 | `brain/knowledge/notes/RULE-STRUCTURE-01-system-structure.md` | Dir structure rules |
| RULE-DYNAMIC-01 | `brain/knowledge/notes/RULE-DYNAMIC-01-no-hardcode.md` | No hardcoded paths policy |
| RULE-TIER-01 | CLAUDE.md inline | 3-Tier plugin architecture |
| RULE-AGENT-MECHANICS-01 | CLAUDE.md inline | Agent context mechanics |
| RULE-CONTEXT7-01 | CLAUDE.md inline | Real-time library docs (anti-hallucination) |
| RULE-SEQUENTIAL-THINKING-01 | CLAUDE.md inline | Deep reasoning chain-of-thought |
| RULE-GIT-NATIVE-01 | CLAUDE.md inline | Git operations priority order |

---

## 3. AGENT MESSAGE QUEUE (`ecosystem/workforce/agents/mq/`)

| File | Owner | Status |
|------|-------|--------|
| `claude_code_tasks.md` | Claude Code | Active task queue |
| `antigravity_tasks.md` | Antigravity | Active task queue |
| `sre_tasks.md` | SRE-Agent | Active task queue |
| `intake_tasks.md` | intake-chief-agent | Active task queue |
| `knowledge_tasks.md` | knowledge_agent | Active task queue |
| `orchestrator_tasks.md` | orchestrator_pro | Active task queue |
| `security_tasks.md` | sec-agent | Active task queue |

---

## 4. AUTOMATIONS (`system/automations/AUTOMATION_REGISTRY.yaml`)

### Local Daemons (always-on)

| Name | Path | Owner | Description |
|------|------|-------|-------------|
| `system_pulse` | `system/automations/daemons/system_pulse.py` | SRE-Agent | Heartbeat monitor — resource/crash alerts |
| `update_hud` | `system/automations/daemons/update_hud.ps1` | system | Continuous HUD/dashboard update loop |
| `handoff_to_claude_code` | `system/automations/daemons/handoff_to_claude_code.ps1` | Antigravity | Session handoff shell |
| `auto_sync_omniclaw` | `system/automations/daemons/auto_sync_omniclaw.ps1` | sec-agent | Auto-push backup every 60s |
| `memory_daemon` | `system/ops/scripts/memory_daemon.py` | knowledge_agent | mem0ai + Qdrant long-term memory |
| `agent_bus` | `system/ops/scripts/agent_bus.py` | orchestrator_pro | SQLite pub/sub event bus |

### Local On-Demand

| Name | Path | Port | Description |
|------|------|------|-------------|
| `remote_bridge_gateway` | `system/bridge/main.py` | 8000 | FastAPI gateway for Remote/bots traffic |

### Event-Driven

| Name | Trigger | Path | Owner |
|------|---------|------|-------|
| `process_github_queue` | Vault inbox file created | `system/automations/events/process_github_queue.py` | intake-chief-agent |
| `auto_evolution_engine` | `file_created: storage/vault/DATA/.*` | `ecosystem/workflows/knowledge-ingest.md` + 2 more | registry-manager-agent |
| `repo_active_monitor` | CEO command: `update repos` | `system/ops/scripts/repo_eval_github_api.py` | archivist |

### Cron

| Name | Schedule | Path | Owner |
|------|----------|------|-------|
| `ontology_sweep` | Weekly (Friday) | `system/ops/scripts/ontology_auditor.py` | sre-agent |
| `repo_catalog_updater` | Weekly (Monday 00:00) | `system/ops/scripts/build_master_catalog.py` + 2 more | knowledge_navigator |

### Remote Services (run from `AI_OS_REMOTE_ROOT`)

| Name | Port | Status | Description |
|------|------|--------|-------------|
| `telegram_bridge` | — | active | Telegram ↔ OmniClaw bridge |
| `clawtask_stack` | 7474 | on_demand | ClawTask API + NullClaw workspace |
| `lightrag_server` | 9621 | on_demand | LightRAG RAG server |

---

## 5. LAUNCHERS

| File | Purpose |
|------|---------|
| `system/bridge/open_port.bat` | Start FastAPI bridge on port 8000 (manual) |
| `system/bridge/bridge_daemon.py` | Supervisor/watchdog for bridge (auto-restart on crash) |
| `omniclaw.bat` | Root launcher → setup.ps1 → PowerShell dashboard |
| `setup.ps1` | Full environment bootstrap |
| `system/automations/daemons/handoff_to_claude_code.ps1` | Session handoff to Claude Code |
| `system/infra/start-infrastructure.bat` | Start all infra services (LightRAG, AgentBus, Mem0, etc.) |

---

## 6. BRIDGE / API GATEWAY (`system/bridge/`)

### Files

| File | Role |
|------|------|
| `main.py` | FastAPI app v2.0 — routes all traffic |
| `passport_issuer.py` | VaultKeeper — token issue/verify/revoke/persist |
| `customs_checkpoint.py` | Payload inspection — SQL/XSS/shell/prompt injection detection |
| `bridge_daemon.py` | Watchdog supervisor (auto-restarts uvicorn on crash) |
| `open_port.bat` | Manual launcher with env setup |
| `__init__.py` | Package marker |

### Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/dock/bots/{platform}` | HQ Token | Social bot webhooks (zalo/telegram/facebook/discord/line/whatsapp) |
| `POST` | `/dock/mcp/dispatch` | HQ Token | MCP tool agent calls |
| `POST` | `/dock/agentic_ai/sync` | HQ Token | OpenClaw AI sync |
| `POST` | `/dock/cloud/webhook` | HQ Token | Supabase/GCloud updates |
| `POST` | `/dock/dashboard/ui_command` | HQ Token | Web/Mobile UI commands |
| `POST` | `/vault/auth/issue_temp_pass` | Master Key | Issue temporary token |
| `POST` | `/vault/auth/revoke` | HQ Token | Revoke token |
| `GET` | `/vault/auth/list` | HQ Token (OMNICLAW_HQ level) | List active tokens |
| `GET` | `/health` | None | Health check |

### Auth Levels

| Level | Access |
|-------|--------|
| `OMNICLAW_HQ` | Full access — issue/revoke tokens, list all |
| `VIP` | Full dock access + vip_payload_scan |
| `SYSTEM_BOT` | Full dock access |
| `BOT` | Dock access |
| `GUEST` | Dock access + strict_payload_scan |

### Dispatch Flow

```
External Request
    → customs_checkpoint.inspect_cargo()   ← Security scan
    → passport_issuer.verify_passport()    ← Auth check
    → _publish_event()                     ← Dispatch
        → AgentBus.publish() (SQLite)      ← Primary
        → blackboard.json inbound_queue    ← Fallback
```

---

## 7. SKILLS (`ecosystem/skills/` — 179 entries in SKILL_REGISTRY.json)

### Categories

| Category | Count | Examples |
|----------|-------|---------|
| AI/LLM | ~25 | context7, sequential-thinking, claude-mcp, openai-mcp |
| Web/Scraping | ~15 | firecrawl, scrapling, playwright, browseruse |
| Knowledge/RAG | ~12 | lightrag, mem0, qdrant, knowledge-graph |
| Code/Dev | ~20 | git-mcp, github-mcp, code-review, refactor |
| Data/Analytics | ~18 | pandas-ai, data-viz, sql-agent, excel-agent |
| Communication | ~10 | telegram-mcp, discord-mcp, slack-mcp, zalo-agent |
| Image/Media | ~8 | dall-e, stable-diffusion, video-gen, ocr |
| Productivity | ~12 | calendar, task-manager, note-taker, search |
| Security | ~8 | vault, auth, secrets-manager, audit |
| Infrastructure | ~10 | docker-mcp, k8s-mcp, terraform-mcp, monitoring |
| Other | ~21 | misc specialized skills |

### Key Skills

| Skill | Path | Description |
|-------|------|-------------|
| `context7` | `ecosystem/skills/context7/SKILL.md` | Real-time library docs anti-hallucination |
| `sequential-thinking` | `ecosystem/skills/sequential-thinking/SKILL.md` | Chain-of-thought reasoning |
| `git-mcp` | `ecosystem/skills/git-mcp/SKILL.md` | Git operations via MCP |
| `firecrawl` | `ecosystem/skills/firecrawl/SKILL.md` | Web crawling and scraping |
| `lightrag` | `ecosystem/skills/lightrag/SKILL.md` | GraphRAG knowledge retrieval |
| `mem0` | `ecosystem/skills/mem0/SKILL.md` | Persistent memory across sessions |

---

## 8. DEPARTMENT RULES (`ecosystem/workforce/departments/`)

24 departments with rules files:

| Department | Key Agents |
|------------|-----------|
| Engineering | claude-code, antigravity, orchestrator_pro |
| SRE | sre-agent, system_pulse daemon |
| Security | sec-agent, vault-keeper |
| Knowledge | knowledge_agent, knowledge_navigator, archivist |
| Intake | intake-chief-agent |
| Communications | channel-agent, telegram-bridge |
| IT | it-manager-agent |
| Registry | registry-manager-agent |
| Bridge | bridge-commander-agent |

---

## 9. SCRIPTS (`system/ops/scripts/`)

| Script | Purpose |
|--------|---------|
| `omniclaw_repair_wave*.py` | Bulk repair scripts (Waves 1-9) — path/branding fixes |
| `fix_skill_registry.py` | Fix SKILL_REGISTRY.json paths + null entries |
| `omniclaw_context_injector.py` | Inject OmniClaw context into NullClaw workspace |
| `agent_bus.py` | SQLite pub/sub event bus daemon |
| `memory_daemon.py` | mem0ai + Qdrant long-term memory daemon |
| `ontology_auditor.py` | Weekly ontology sweep — zero unlinked entities |
| `build_master_catalog.py` | Build MASTER_REPO_CATALOG.md |
| `repo_eval_github_api.py` | GitHub API health check for active repos |
| `validate_skills.ps1` | Validate all skills against SKILL_REGISTRY |
| `global_url_extractor.py` | Extract URLs from all files |

---

## 10. MCP SERVERS (`system/infra/mcp/`)

| Server | Type | Purpose |
|--------|------|---------|
| `omniclaw-workspace` | Node.js | OmniClaw workspace MCP tools |
| `gitnexus` | npx | Git operations |
| `minimax-mcp` | uvx | Minimax AI tools |
| `scrapling-mcp` | Python | Web scraping |
| `firecrawl-mcp` | Node.js | Web crawling |
| `context7` | npx | Real-time library docs |

Config: `system/infra/mcp/config.json`

---

## 11. REPAIR HISTORY (Wave Log)

| Wave | Date | Scope | Result |
|------|------|-------|--------|
| 1-4 | 2026-03-28 | Initial path fixes, 135 double ecosystem/ bugs, 292 bare refs | Fixed |
| 5 | 2026-03-29 | OmniClaw rebrand across 575 files | Fixed |
| 6-8 | 2026-03-30 | Plugin config, MCP config, CI pipeline fixes | Fixed |
| 9 | 2026-03-31 | AOS_ROOT→OMNICLAW_ROOT, 448 replacements across ecosystem/brain/system | Fixed |
| 10 | 2026-03-31 | Bridge v2.0 rewrite, SKILL_REGISTRY cleanup (18+20 null entries removed), antigravity-boot paths | Fixed |

---

*Generated: 2026-03-31 | Source: Explore agent full scan + Wave 10 audit*
