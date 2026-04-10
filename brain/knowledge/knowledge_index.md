---
id: knowledge-index
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.436460
---

# ðŸ—‚ï¸ Knowledge Index
**Last Updated:** 2026-04-07

## ðŸ—ºï¸ System Map (READ FIRST)
- [AI_OS_SYSTEM_MAP.md](AI_OS_SYSTEM_MAP.md) â€” **MASTER REFERENCE** â€” ToÃ n bá»™ há»‡ thá»‘ng OmniClaw: org structure, 21 depts, 4 gates, 5 workflows, 5 memory layers, agents, skills, file rules, boot sequence, commands
- [MASTER_SYSTEM_MAP.md](corp/MASTER_SYSTEM_MAP.md) â€” **SYSTEM MAP v2 (2026-03-23)** â€” Boot â†’ Corp Cycle 8-phase â†’ 21 Depts â†’ 3-Tier Plugin â†’ Agent Memory â†’ Knowledge Flow â†’ Escalation â†’ CLI Commands

## ðŸ›ï¸ Governance & Identity (Tier 0-1)
- [CLAUDE.md](../../.claude/skills/supabase-postgres-best-practices/CLAUDE.md) â€” Master entry point, boot sequence, directory map
- [SOUL.md](general/SOUL.md) â€” Platform identity & core values
- [AGENTS.md](bmad_repo/agents.md) â€” Agent roster, hierarchy, decision authority
- [GOVERNANCE.md](general/GOVERNANCE.md) â€” Safety anchors
- [THESIS.md](general/THESIS.md) â€” 40 Pillars (The WHY)

## âš™ï¸ Operations & Governance (Tier 2)
- [ORCHESTRATION_SOP.md](../rules/security/rules/ORCHESTRATION_SOP.md) â€” 6-phase multi-agent loop
- [WORKFLOW.md](bmad_repo/workflow.md) â€” Event-driven operational workflow (v2)
- [APPROVAL_GATES.md](general/APPROVAL_GATES.md) â€” 4 universal approval gates
- [LEARNING_CYCLE_PROTOCOL.md](../rules/security/rules/LEARNING_CYCLE_PROTOCOL.md) â€” Self-improvement loop
- [CLAUDE_CODE_MANAGER.md](general/CLAUDE_CODE_MANAGER.md) â€” 3 roles, fix-retry, receipts

## ðŸ”§ Skill System
- [SKILL_SPEC.md](general/SKILL_SPEC.md) â€” Skill schema standard
- [SKILL_REGISTRY.json](../brain/registry/SKILL_REGISTRY.json) â€” 103+ registered entries
- [EXTERNAL_SKILL_SOURCES.yaml](../brain/registry/EXTERNAL_SKILL_SOURCES.yaml) â€” 15+ external sources
- **Domain Packs** (`skills/domains/`):
  - `google-workspace/` â€” gas, sheets, sheets-performance
  - `databases/` â€” supabase-postgres
  - `finance/` â€” cost-manager, edge-compute
  - `frontend/` â€” hitl-gateway-enforcer, fsd-architectural-linter
  - `pos/` â€” pos-event-sourcing-auditor

## ðŸ“‹ Prompt Templates (runes/)
- [brainstorm_prompt.md](general/brainstorm_prompt.md) â€” Visual-First brainstorm template
- [report_prompt.md](general/report_prompt.md) â€” Vietnamese Mermaid report template
- [task_prompt.md](general/task_prompt.md) â€” execution_template fill guide


## ðŸ”’ Security & Ingestion Protocol

- [Clone Security Protocol](../rules/security/rules/clone_security_protocol.md) â€” MANDATORY pre-clone rules, quarantine zone, absolute rules
- [Repo Vetting Knowledge](general/repo_vetting_knowledge.md) â€” Supply chain attacks, detection patterns, repo trust ratings
- [Security Shield Skill](../../.claude/skills/supabase-postgres-best-practices/SKILL.md) â€” /vet-repo, /scan, /secure-patch
- [Vet Script](../skills/security_shield/vet_repo.ps1) â€” 7-scan PowerShell automation (git hooks, npm, network, secrets...)
- [Knowledge Ingest Workflow](general/knowledge-ingest.md) â€” 7-phase pipeline: intake â†’ scan â†’ classify â†’ enrich â†’ route â†’ archive â†’ notify
- [Agent Auto-Create Protocol](general/agent-auto-create.md) â€” Auto-create new agents when knowledge has no existing agent
- [Secure External Ingestion](general/ingest-external.md) â€” Legacy ingest (see knowledge-ingest.md for v2)

## ðŸ¤– AI Agent Systems
- [Agentic Patterns](agent_architecture/agentic_patterns.md) â€” 10 core patterns: ReAct, Reflection, Planning, Multi-Agent, Meta-Controller...
- [BMAD Method](bmad_repo/bmad_method.md) â€” Agile AI development framework: 4-phase cycle, agent personas, Party Mode
- [AI Integration](ai-ml/ai-integration.md) â€” AI integration patterns
- [Multi-Agent Orchestration](agent_architecture/multi-agent-orchestration.md)
- [MCP Server Architecture](architecture/mcp_server_architecture.md)
- [Star Office UI](ui/star_office_ui.md) â€” Pixel-art AI Agent dashboard: 6 states, multi-agent office, memory â†’ visual card, desktop pet mode (4.7K â˜…, MIT)

## ðŸ› ï¸ Claude Code Ecosystem  
- [Claude Code Ecosystem](claude_bp_repo/claude_code_ecosystem.md) â€” everything-claude-code, claude-mem plugin, best practices
- [Local AI Explanation](ai-ml/local_ai_explanation.md)
- [Safe AI Strategy](ai-ml/safe_ai_strategy.md)

## ðŸ”¬ AI/ML Deep Dives
- [AI Capability Deep Dive](ai-ml/ai_capability_deep_dive.md)
- [Intelligence Upgrade Analysis](general/intelligence_upgrade_analysis.md)
- [LightRAG](./lightrag_deep_dive.md) *(pending Phase 11)*

## ðŸ—ï¸ Architecture & Design
- [Architect Handbook](architecture/architect_handbook.md) â€” DDD, Hexagonal, SOLID patterns
- [Phase 8 Tech Spec](general/phase8_tech_spec.md)
- [DSA Patterns](general/dsa_patterns.md)

## ðŸŒ Web & Extensions
- [Chrome Extension API](general/chrome-extension-api.md)
- [Bookmark UX Patterns](general/bookmark-ux-patterns.md)

- [References](general/references.md) â€” All external repos
- [Repo Analysis Report](general/repo_analysis_report.md) â€” âœ… CLONE / ðŸ“š LEARN-ONLY / â­ï¸ SKIP decisions
- [GitHub Repos Index](catalog/github_repos_index.md) â€” 177 repos categorized (DATA/Github.txt ingested 2026-03-15)

## ðŸ“¥ DATA Library â€” Ingested Knowledge

- [Github Archives Library](library/github_archives/master_github.txt) â€” 2000+ extracted GitHub repositories categorized by skills and architecture (Assimilated from legacy v1 system into OmniClaw 21 Department structure).
  - Contains 14 sanitized segments (e.g. `ecommerce_growth_affiliate_coupons.txt`, `tools_for_working.txt`) in `library/github_archives/`.
- [Legacy Ops Python](library/legacy_python_ops/) â€” Core Python scripts (`aios_orchestrator.py`, etc.) extracted from the v1 system for research purposes (Read-only).
- [Legacy Agents Memory](library/legacy_agent_memories/) â€” Preserved prompts and mnemonic blocks from 85+ legacy subagents, acting as reference material for the modern 21 Head Agents (Read-only).
- [Legacy Orphan Archives](library/legacy_orphan_archives/) â€” Preserved loose fragments, prompts, and unassigned text knowledge swept from the v1 system during final vaporization.
- [CIV Pipeline State](../core/telemetry/civ_pipeline_state/_DIR_IDENTITY.md) â€” Assimilated Content Intake & Vetting legacy pipeline telemetry and state logs.
- [KI Snapshots](ki_snapshots/_DIR_IDENTITY.md) â€” 140+ native JSON snapshot files for OA daemon episodic memory.
- [AI Workflow Best Practices](ai-ml/ai_workflow_best_practices.md) â€” 10 major topics: React boilerplate, Skill creation, Multi-agent, 8-layer prompting, Claude Code tips, AI-first design, Security, Gen AI structure, Antigravity tips, Agent Skills (DATA/POST.txt)
- [GitHub Repos Index](catalog/github_repos_index.md) â€” 177 repos from DATA/Github.txt, categorized by function, showing which are already installed as plugins
- [Non-Cloneable Repos Analysis](general/non_cloneable_repos_analysis.md) â€” 23 repos analyzed via GitHub README: Auto-Claude (12-agent GUI), ProxyPal (multi-AI proxy), SkillSentry (9-layer security), marketingskills (35 skills), trainingAI (8-level Vietnamese AI guide), ChatDev, llmfit, autoclip, SmartTube, social downloader, aPix/SDVN, SpringBoot skill, Clean Arch Next.js + more
- **LobsterBoard** (plugins/LobsterBoard/) â€” Self-hosted drag-and-drop dashboard (60+ widgets). OpenClaw-compatible. **Antigravity, Claude Code, Gemini, Cursor** usage monitoring widgets built-in. Node.js server.

- [ACTIVATION_BOARD](./ACTIVATION_BOARD.md) ï¿½ ?? T?t c? plugin/service c?n kï¿½ch ho?t/m? localhost: LobsterBoard (port 3000), Remote Bridge (port 5001), LightRAG (port 9621), Firecrawl (port 3002), AI OS Dashboard (port 19000)


### Session 6 â€” Ingested 2026-03-19

- **[temm1e](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** â€” Rust autonomous AI agent runtime. 15MB idle, 31ms cold start. Î»-Memory + Blueprints. `T1`
- **[awesome-openclaw-skills](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** â€” Curated catalog 5400+ OpenClaw skills, 30+ categories. By VoltAgent. `T1`
- **[GitNexus](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** â€” Zero-server code intelligence. Knowledge graph + Graph RAG. Browser-native + MCP server. `T1`
- **[OSINT-CTFs](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** â€” Directory OSINT CTF platforms. Security training reference. `T2`
- **[forgewright](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** â€” Antigravity plugin. SaaS/game lifecycle pipeline. 48 skills, 19 modes, 15 protocols. By buiphucminhtam. `T1`


## Session 7 â€” Ingested 2026-03-19

### Research Papers (1)
| File | Topic |
|------|-------|
| knowledge/tinylora_reasoning_13params.md | TinyLoRA: 13-param fine-tuning for LLM reasoning (arxiv 2602.04118) |

### Platform Knowledge (1)
| File | Topic |
|------|-------|
| knowledge/clawtask_agent_orchestration.md | ClawTask: AI agent task orchestration platform |

### Plans & Roadmaps (1)
| File | Topic |
|------|-------|
| knowledge/fine_tuning_plan_tinylora.md | TinyLoRA fine-tuning roadmap for 21 OmniClaw agents |

### Platform / Orchestration (1)
| File | Topic |
|------|-------|
| knowledge/repos/paperclip/knowledge.md | Paperclip: open-source orchestration for zero-human companies |

---

## Session 8 ï¿½ Ingested 2026-03-23

### Governance & System Maps (4)
| File | Topic |
|------|-------|
| MASTER_SYSTEM_MAP.md | System Map v2 ï¿½ Boot ? 8-phase Corp Cycle ? 21 Depts ? 3-Tier Plugin ? Agent Memory ? Escalation ? CLI |
| ops/workflows/repo-evaluation.md | Repo Evaluation Gate (CIV Gate 1) ï¿½ 5-step: APPROVE / DEFER / REJECT |
| brain/knowledge/general/GOVERNANCE.md | v2 ï¿½ Plugin & Repo Governance Policy, 3-Tier Architecture added |
| plugins/plugin-catalog.md | v2.0 ï¿½ All 35+ repos have explicit VERDICT + ?? REFERENCE category |

### Knowledge Items ï¿½ Agent & Plugin Patterns (3 KI Notes)
| File | Topic |
|------|-------|
| notes/KI-AGENT-ARCHITECTURES-01.md | 17 Agentic Architecture Patterns with AI OS mapping |
| notes/KI-AGENCY-AGENTS-CHERRY-PICK-01.md | agency-agents gap analysis: 6 missing agents + cherry-pick guide |
| notes/KI-GRAPHRAG-CONCEPTS-01.md | GraphRAG community detection concept ? apply to LightRAG |

### Department SOPs Updated (3)
| Dept | File | Update |
|------|------|--------|
| Dept 4 (Registry) | corp/memory/departments/registry_capability.md | Full SOP v2 |
| Dept 10 (Security) | corp/memory/departments/security_grc.md | Full SOP v2 ï¿½ 3-Tier enforcement |
| Dept 20 (CIV) | corp/memory/departments/content_intake.md | Full SOP v2 ï¿½ GATE 1 owner |

### Learning Loop (Cycle 8 Retro)
| File | Type |
|------|------|
| brain/memory/corp_memory/proposals/RETRO_2026-03-23.md | Cycle 8 Retrospective ï¿½ 5 patterns, 5 lessons, 3 proposals |
| brain/memory/corp_memory/proposals/PROPOSAL_2026-03-23_session-improvements.md | 3 CEO Proposals pending |
| corp/memory/global/decisions_log.md | +4 LESSON_LEARNED entries (permanent) |

---

## Session 8 additions ï¿½ 2026-03-23 (continued)

### Deep Analysis KI Notes
| File | Topic |
|------|-------|
| notes/KI-CONTEXT7-DEEP-01.md | Context7: MCP doc injection ï¿½ 50.2k stars, REST API v2, 2 modes (CLI+Skill / MCP), action plan 5 buoc, risk analysis |

---

## Session 8 additions ï¿½ KI Notes from REFERENCE Repos (2026-03-23)

| KI File | Content | Source Repos |
|---------|---------|--------------|
| notes/KI-CONTEXT7-DEEP-01.md | Context7 deep analysis ï¿½ REST API, 2 modes, action plan | upstash/context7 |
| notes/KI-MULTI-AGENT-PATTERNS-01.md | Agentic RL, HTIL, LLM Router, Circuit Breaker, Token Budget | agentscope + agenttrafficcontrol |
| notes/KI-GIT-NATIVE-AGENT-01.md | Git-native agent: audit trail, SOD, SkillsFlow, versioned agents | open-gitagent/gitagent |
| notes/KI-SKILL-COST-MODEL-01.md | 5-Layer skill: triggers, not_for, 4C verification, context_budget, fallback chains | rune-kit/rune |
| notes/KI-MCP-SERVER-INDEX-01.md | 40+ category MCP server index, top picks for AI OS | punkpeye/awesome-mcp-servers |
| notes/KI-TOKEN-REDUCTION-01.md | 6.8x token reduction via knowledge graph, ReAct pattern, 3-type memory | code-review-graph + agents-course |
| notes/KI-AI-STACK-LANDSCAPE-01.md | AI OS vs market gap analysis, Copilot patterns, NL-to-analytics | seeaifirst + awesome-copilot + ossinsight |
| notes/KI-REFERENCE-MISC-01.md | agentql, Archon, n8n patterns, JS quirks, gitignore templates, plotly, pattern-craft | 9 misc repos |

---

## Session 9 â€” OmniClaw TNN POS Extraction (2026-04-06)

### Knowledge Items â€” Tiem Nuoc Nho Architecture Patterns
| File | Topic | Source Repos |
|------|-------|--------------|
| gas_clasp_backend_DISTILLED.md | Kiáº¿n trÃºc Serverless No-DB, dÃ¹ng GAS & Clasp CLI | Tiem_Nuoc_Nho_v5 |
| cloud_to_lan_hardware_proxy_DISTILLED.md | Local Proxy Server, in LAN tá»« Cloud Vercel | Tiem_Nuoc_Nho_v5 |
| pos_offline_first_react_DISTILLED.md | Offline-first POS, Stale-while-revalidate, Virtuoso | Tiem_Nuoc_Nho_v5 |

---

## Session 10 â€” Infrastructure Hardening (2026-04-07)

### System Rules & Architecture Constraints (3 files)
| File | Rule ID | Description |
|------|---------|-------------|
| `brain/corp/gaps/GAP-2026-04-07-vault-recursion.md` | `GAP-002` | Post-mortem: Vault-in-databases recursion tá»« ZIP extract V1. Defines RULE-ARCH-01/02/03 |
| `vault/assets/databases/_DIR_IDENTITY.md` | `RULE-ARCH-02` | Constraint lock cho database zone â€” chá»‰ cho phÃ©p engine namespace vÃ  file `.db/.sqlite/.json` |
| `core/docs/_DIR_IDENTITY.md` | N/A | Khai bÃ¡o Ä‘á»‹nh danh khu vá»±c Docs, quy Ä‘á»‹nh 100% song ngá»¯ (EN/VN) cho má»i file tÃ i liá»‡u |

### Documentation (1 file)
| File | Rule ID | Description |
|------|---------|-------------|
| `core/docs/README-vn.md` | N/A | Báº£n dá»‹ch tiáº¿ng Viá»‡t cá»§a README, tuÃ¢n thá»§ quy táº¯c song ngá»¯ |

### Utilities & Watchdogs (5 files)
| File | Rule ID | Description |
|------|---------|-------------|
| `core/ops/scripts/utils/safe_fs.py` | `RULE-FS-01` | Safe rename/merge trÃªn Windows NTFS â€” ngÄƒn data loss do case-insensitive path collision |
| `core/ops/scripts/utils/db_hygiene_sweep.py` | `RULE-ARCH-03` | OMA Watchdog lÃ m sáº¡ch Data Zone |
| `vault/archives/` | `RULE-ARCH-01` | [GLACIER] Tráº¡m lÆ°u trá»¯ dá»¯ liá»‡u nÃ©n/bÃ£ rÃ¡c |
| `core/bridge/*.py` | N/A | Fix rÃ² rá»‰ cáº¥u trÃºc: XÃ³a sáº¡ch hardcode `system/` thÃ nh `core/` |
| `core/config/config.json` | `RULE-ARCH-01` | Quy hoáº¡ch cáº¥u trÃºc: Di dá»i táº­p trung cáº¥u hÃ¬nh ra khá»i khu logic `core/ops/scripts/` |
| `core/daemons/daemon_utils.py` | N/A | Fix rÃ² rá»‰ cáº¥u trÃºc há»‡ thá»‘ng: Thay Ä‘á»•i hardcode `system/ops/secrets/MASTER.env` thÃ nh `core/` |
| `core/daemons/_DIR_IDENTITY.md` | N/A | Äá»‹nh danh Ä‘áº§y Ä‘á»§ 7 Daemons (Bao hÃ m cáº£ OSF Firewall) báº±ng song ngá»¯ |

### Architecture Decisions (session)
| Decision | Detail |
|----------|--------|
| `QUARANTINE` â†’ `vault/QUARANTINE` | TÃ¡ch báº¡ch Logic (`core/`) khá»i Data Dropzone (`vault/`). Anti-pattern ghi táº¡i GAP-002 |
| `databases/vault/` â†’ Vaporized | Lá»—i Ä‘á»‡ quy tá»« ZIP V1 extract. Watchdog deployed Ä‘á»ƒ auto-enforce |
| `brain/knowledge/corp/docs/` â†’ `core/docs/` | **Discoverability Fix:** 27 docs files chuyá»ƒn vá» Front Door `core/docs/` Ä‘á»ƒ User tÃ¬m tháº¥y ngay. Sub-folders: `architecture/`, `usage_guides/`, `workflows/` |

