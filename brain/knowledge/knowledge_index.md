---
id: knowledge-index
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.436460
---

# 🗂️ Knowledge Index
**Last Updated:** 2026-04-07

## 🗺️ System Map (READ FIRST)
- [AI_OS_SYSTEM_MAP.md](AI_OS_SYSTEM_MAP.md) — **MASTER REFERENCE** — Toàn bộ hệ thống OmniClaw: org structure, 21 depts, 4 gates, 5 workflows, 5 memory layers, agents, skills, file rules, boot sequence, commands
- [MASTER_SYSTEM_MAP.md](corp/MASTER_SYSTEM_MAP.md) — **SYSTEM MAP v2 (2026-03-23)** — Boot → Corp Cycle 8-phase → 21 Depts → 3-Tier Plugin → Agent Memory → Knowledge Flow → Escalation → CLI Commands

## 🏛️ Governance & Identity (Tier 0-1)
- [CLAUDE.md](../../.claude/skills/supabase-postgres-best-practices/CLAUDE.md) — Master entry point, boot sequence, directory map
- [SOUL.md](general/SOUL.md) — Platform identity & core values
- [AGENTS.md](bmad_repo/agents.md) — Agent roster, hierarchy, decision authority
- [GOVERNANCE.md](general/GOVERNANCE.md) — Safety anchors
- [THESIS.md](general/THESIS.md) — 40 Pillars (The WHY)

## ⚙️ Operations & Governance (Tier 2)
- [ORCHESTRATION_SOP.md](../rules/security/rules/ORCHESTRATION_SOP.md) — 6-phase multi-agent loop
- [WORKFLOW.md](bmad_repo/workflow.md) — Event-driven operational workflow (v2)
- [APPROVAL_GATES.md](general/APPROVAL_GATES.md) — 4 universal approval gates
- [LEARNING_CYCLE_PROTOCOL.md](../rules/security/rules/LEARNING_CYCLE_PROTOCOL.md) — Self-improvement loop
- [CLAUDE_CODE_MANAGER.md](general/CLAUDE_CODE_MANAGER.md) — 3 roles, fix-retry, receipts

## 🔧 Skill System
- [SKILL_SPEC.md](general/SKILL_SPEC.md) — Skill schema standard
- [SKILL_REGISTRY.json](../shared-context/SKILL_REGISTRY.json) — 103+ registered entries
- [EXTERNAL_SKILL_SOURCES.yaml](../shared-context/EXTERNAL_SKILL_SOURCES.yaml) — 15+ external sources
- **Domain Packs** (`skills/domains/`):
  - `google-workspace/` — gas, sheets, sheets-performance
  - `databases/` — supabase-postgres
  - `finance/` — cost-manager, edge-compute
  - `frontend/` — hitl-gateway-enforcer, fsd-architectural-linter
  - `pos/` — pos-event-sourcing-auditor

## 📋 Prompt Templates (runes/)
- [brainstorm_prompt.md](general/brainstorm_prompt.md) — Visual-First brainstorm template
- [report_prompt.md](general/report_prompt.md) — Vietnamese Mermaid report template
- [task_prompt.md](general/task_prompt.md) — execution_template fill guide


## 🔒 Security & Ingestion Protocol

- [Clone Security Protocol](../rules/security/rules/clone_security_protocol.md) — MANDATORY pre-clone rules, quarantine zone, absolute rules
- [Repo Vetting Knowledge](general/repo_vetting_knowledge.md) — Supply chain attacks, detection patterns, repo trust ratings
- [Security Shield Skill](../../.claude/skills/supabase-postgres-best-practices/SKILL.md) — /vet-repo, /scan, /secure-patch
- [Vet Script](../skills/security_shield/vet_repo.ps1) — 7-scan PowerShell automation (git hooks, npm, network, secrets...)
- [Knowledge Ingest Workflow](general/knowledge-ingest.md) — 7-phase pipeline: intake → scan → classify → enrich → route → archive → notify
- [Agent Auto-Create Protocol](general/agent-auto-create.md) — Auto-create new agents when knowledge has no existing agent
- [Secure External Ingestion](general/ingest-external.md) — Legacy ingest (see knowledge-ingest.md for v2)

## 🤖 AI Agent Systems
- [Agentic Patterns](agent_architecture/agentic_patterns.md) — 10 core patterns: ReAct, Reflection, Planning, Multi-Agent, Meta-Controller...
- [BMAD Method](bmad_repo/bmad_method.md) — Agile AI development framework: 4-phase cycle, agent personas, Party Mode
- [AI Integration](ai-ml/ai-integration.md) — AI integration patterns
- [Multi-Agent Orchestration](agent_architecture/multi-agent-orchestration.md)
- [MCP Server Architecture](architecture/mcp_server_architecture.md)
- [Star Office UI](ui/star_office_ui.md) — Pixel-art AI Agent dashboard: 6 states, multi-agent office, memory → visual card, desktop pet mode (4.7K ★, MIT)

## 🛠️ Claude Code Ecosystem  
- [Claude Code Ecosystem](claude_bp_repo/claude_code_ecosystem.md) — everything-claude-code, claude-mem plugin, best practices
- [Local AI Explanation](ai-ml/local_ai_explanation.md)
- [Safe AI Strategy](ai-ml/safe_ai_strategy.md)

## 🔬 AI/ML Deep Dives
- [AI Capability Deep Dive](ai-ml/ai_capability_deep_dive.md)
- [Intelligence Upgrade Analysis](general/intelligence_upgrade_analysis.md)
- [LightRAG](./lightrag_deep_dive.md) *(pending Phase 11)*

## 🏗️ Architecture & Design
- [Architect Handbook](architecture/architect_handbook.md) — DDD, Hexagonal, SOLID patterns
- [Phase 8 Tech Spec](general/phase8_tech_spec.md)
- [DSA Patterns](general/dsa_patterns.md)

## 🌐 Web & Extensions
- [Chrome Extension API](general/chrome-extension-api.md)
- [Bookmark UX Patterns](general/bookmark-ux-patterns.md)

- [References](general/references.md) — All external repos
- [Repo Analysis Report](general/repo_analysis_report.md) — ✅ CLONE / 📚 LEARN-ONLY / ⏭️ SKIP decisions
- [GitHub Repos Index](catalog/github_repos_index.md) — 177 repos categorized (DATA/Github.txt ingested 2026-03-15)

## 📥 DATA Library — Ingested Knowledge

- [Github Archives Library](library/github_archives/master_github.txt) — 2000+ extracted GitHub repositories categorized by skills and architecture (Assimilated from legacy v1 system into OmniClaw 21 Department structure).
  - Contains 14 sanitized segments (e.g. `ecommerce_growth_affiliate_coupons.txt`, `tools_for_working.txt`) in `library/github_archives/`.
- [Legacy Ops Python](library/legacy_python_ops/) — Core Python scripts (`aios_orchestrator.py`, etc.) extracted from the v1 system for research purposes (Read-only).
- [Legacy Agents Memory](library/legacy_agent_memories/) — Preserved prompts and mnemonic blocks from 85+ legacy subagents, acting as reference material for the modern 21 Head Agents (Read-only).
- [Legacy Orphan Archives](library/legacy_orphan_archives/) — Preserved loose fragments, prompts, and unassigned text knowledge swept from the v1 system during final vaporization.
- [CIV Pipeline State](../core/telemetry/civ_pipeline_state/_DIR_IDENTITY.md) — Assimilated Content Intake & Vetting legacy pipeline telemetry and state logs.
- [KI Snapshots](ki_snapshots/_DIR_IDENTITY.md) — 140+ native JSON snapshot files for OA daemon episodic memory.
- [AI Workflow Best Practices](ai-ml/ai_workflow_best_practices.md) — 10 major topics: React boilerplate, Skill creation, Multi-agent, 8-layer prompting, Claude Code tips, AI-first design, Security, Gen AI structure, Antigravity tips, Agent Skills (DATA/POST.txt)
- [GitHub Repos Index](catalog/github_repos_index.md) — 177 repos from DATA/Github.txt, categorized by function, showing which are already installed as plugins
- [Non-Cloneable Repos Analysis](general/non_cloneable_repos_analysis.md) — 23 repos analyzed via GitHub README: Auto-Claude (12-agent GUI), ProxyPal (multi-AI proxy), SkillSentry (9-layer security), marketingskills (35 skills), trainingAI (8-level Vietnamese AI guide), ChatDev, llmfit, autoclip, SmartTube, social downloader, aPix/SDVN, SpringBoot skill, Clean Arch Next.js + more
- **LobsterBoard** (plugins/LobsterBoard/) — Self-hosted drag-and-drop dashboard (60+ widgets). OpenClaw-compatible. **Antigravity, Claude Code, Gemini, Cursor** usage monitoring widgets built-in. Node.js server.

- [ACTIVATION_BOARD](./ACTIVATION_BOARD.md) � ?? T?t c? plugin/service c?n k�ch ho?t/m? localhost: LobsterBoard (port 3000), Remote Bridge (port 5001), LightRAG (port 9621), Firecrawl (port 3002), AI OS Dashboard (port 19000)


### Session 6 — Ingested 2026-03-19

- **[temm1e](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** — Rust autonomous AI agent runtime. 15MB idle, 31ms cold start. λ-Memory + Blueprints. `T1`
- **[awesome-openclaw-skills](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** — Curated catalog 5400+ OpenClaw skills, 30+ categories. By VoltAgent. `T1`
- **[GitNexus](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** — Zero-server code intelligence. Knowledge graph + Graph RAG. Browser-native + MCP server. `T1`
- **[OSINT-CTFs](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** — Directory OSINT CTF platforms. Security training reference. `T2`
- **[forgewright](../../vault/archives/archive_legacy/awesome-openclaw-skills/knowledge.md)** — Antigravity plugin. SaaS/game lifecycle pipeline. 48 skills, 19 modes, 15 protocols. By buiphucminhtam. `T1`


## Session 7 — Ingested 2026-03-19

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

## Session 8 � Ingested 2026-03-23

### Governance & System Maps (4)
| File | Topic |
|------|-------|
| MASTER_SYSTEM_MAP.md | System Map v2 � Boot ? 8-phase Corp Cycle ? 21 Depts ? 3-Tier Plugin ? Agent Memory ? Escalation ? CLI |
| ops/workflows/repo-evaluation.md | Repo Evaluation Gate (CIV Gate 1) � 5-step: APPROVE / DEFER / REJECT |
| shared-context/GOVERNANCE.md | v2 � Plugin & Repo Governance Policy, 3-Tier Architecture added |
| plugins/plugin-catalog.md | v2.0 � All 35+ repos have explicit VERDICT + ?? REFERENCE category |

### Knowledge Items � Agent & Plugin Patterns (3 KI Notes)
| File | Topic |
|------|-------|
| notes/KI-AGENT-ARCHITECTURES-01.md | 17 Agentic Architecture Patterns with AI OS mapping |
| notes/KI-AGENCY-AGENTS-CHERRY-PICK-01.md | agency-agents gap analysis: 6 missing agents + cherry-pick guide |
| notes/KI-GRAPHRAG-CONCEPTS-01.md | GraphRAG community detection concept ? apply to LightRAG |

### Department SOPs Updated (3)
| Dept | File | Update |
|------|------|--------|
| Dept 4 (Registry) | corp/memory/departments/registry_capability.md | Full SOP v2 |
| Dept 10 (Security) | corp/memory/departments/security_grc.md | Full SOP v2 � 3-Tier enforcement |
| Dept 20 (CIV) | corp/memory/departments/content_intake.md | Full SOP v2 � GATE 1 owner |

### Learning Loop (Cycle 8 Retro)
| File | Type |
|------|------|
| brain/shared-context/corp/proposals/RETRO_2026-03-23.md | Cycle 8 Retrospective � 5 patterns, 5 lessons, 3 proposals |
| brain/shared-context/corp/proposals/PROPOSAL_2026-03-23_session-improvements.md | 3 CEO Proposals pending |
| corp/memory/global/decisions_log.md | +4 LESSON_LEARNED entries (permanent) |

---

## Session 8 additions � 2026-03-23 (continued)

### Deep Analysis KI Notes
| File | Topic |
|------|-------|
| notes/KI-CONTEXT7-DEEP-01.md | Context7: MCP doc injection � 50.2k stars, REST API v2, 2 modes (CLI+Skill / MCP), action plan 5 buoc, risk analysis |

---

## Session 8 additions � KI Notes from REFERENCE Repos (2026-03-23)

| KI File | Content | Source Repos |
|---------|---------|--------------|
| notes/KI-CONTEXT7-DEEP-01.md | Context7 deep analysis � REST API, 2 modes, action plan | upstash/context7 |
| notes/KI-MULTI-AGENT-PATTERNS-01.md | Agentic RL, HTIL, LLM Router, Circuit Breaker, Token Budget | agentscope + agenttrafficcontrol |
| notes/KI-GIT-NATIVE-AGENT-01.md | Git-native agent: audit trail, SOD, SkillsFlow, versioned agents | open-gitagent/gitagent |
| notes/KI-SKILL-COST-MODEL-01.md | 5-Layer skill: triggers, not_for, 4C verification, context_budget, fallback chains | rune-kit/rune |
| notes/KI-MCP-SERVER-INDEX-01.md | 40+ category MCP server index, top picks for AI OS | punkpeye/awesome-mcp-servers |
| notes/KI-TOKEN-REDUCTION-01.md | 6.8x token reduction via knowledge graph, ReAct pattern, 3-type memory | code-review-graph + agents-course |
| notes/KI-AI-STACK-LANDSCAPE-01.md | AI OS vs market gap analysis, Copilot patterns, NL-to-analytics | seeaifirst + awesome-copilot + ossinsight |
| notes/KI-REFERENCE-MISC-01.md | agentql, Archon, n8n patterns, JS quirks, gitignore templates, plotly, pattern-craft | 9 misc repos |

---

## Session 9 — OmniClaw TNN POS Extraction (2026-04-06)

### Knowledge Items — Tiem Nuoc Nho Architecture Patterns
| File | Topic | Source Repos |
|------|-------|--------------|
| gas_clasp_backend_DISTILLED.md | Kiến trúc Serverless No-DB, dùng GAS & Clasp CLI | Tiem_Nuoc_Nho_v5 |
| cloud_to_lan_hardware_proxy_DISTILLED.md | Local Proxy Server, in LAN từ Cloud Vercel | Tiem_Nuoc_Nho_v5 |
| pos_offline_first_react_DISTILLED.md | Offline-first POS, Stale-while-revalidate, Virtuoso | Tiem_Nuoc_Nho_v5 |

---

## Session 10 — Infrastructure Hardening (2026-04-07)

### System Rules & Architecture Constraints (3 files)
| File | Rule ID | Description |
|------|---------|-------------|
| `brain/corp/gaps/GAP-2026-04-07-vault-recursion.md` | `GAP-002` | Post-mortem: Vault-in-databases recursion từ ZIP extract V1. Defines RULE-ARCH-01/02/03 |
| `vault/assets/databases/_DIR_IDENTITY.md` | `RULE-ARCH-02` | Constraint lock cho database zone — chỉ cho phép engine namespace và file `.db/.sqlite/.json` |
| `core/docs/_DIR_IDENTITY.md` | N/A | Khai báo định danh khu vực Docs, quy định 100% song ngữ (EN/VN) cho mọi file tài liệu |

### Documentation (1 file)
| File | Rule ID | Description |
|------|---------|-------------|
| `core/docs/README-vn.md` | N/A | Bản dịch tiếng Việt của README, tuân thủ quy tắc song ngữ |

### Utilities & Watchdogs (5 files)
| File | Rule ID | Description |
|------|---------|-------------|
| `core/ops/scripts/utils/safe_fs.py` | `RULE-FS-01` | Safe rename/merge trên Windows NTFS — ngăn data loss do case-insensitive path collision |
| `core/ops/scripts/utils/db_hygiene_sweep.py` | `RULE-ARCH-03` | OMA Watchdog làm sạch Data Zone |
| `vault/archives/` | `RULE-ARCH-01` | [GLACIER] Trạm lưu trữ dữ liệu nén/bã rác |
| `core/bridge/*.py` | N/A | Fix rò rỉ cấu trúc: Xóa sạch hardcode `system/` thành `core/` |
| `core/config/config.json` | `RULE-ARCH-01` | Quy hoạch cấu trúc: Di dời tập trung cấu hình ra khỏi khu logic `core/ops/scripts/` |
| `core/daemons/daemon_utils.py` | N/A | Fix rò rỉ cấu trúc hệ thống: Thay đổi hardcode `system/ops/secrets/MASTER.env` thành `core/` |
| `core/daemons/_DIR_IDENTITY.md` | N/A | Định danh đầy đủ 7 Daemons (Bao hàm cả OSF Firewall) bằng song ngữ |

### Architecture Decisions (session)
| Decision | Detail |
|----------|--------|
| `QUARANTINE` → `vault/QUARANTINE` | Tách bạch Logic (`core/`) khỏi Data Dropzone (`vault/`). Anti-pattern ghi tại GAP-002 |
| `databases/vault/` → Vaporized | Lỗi đệ quy từ ZIP V1 extract. Watchdog deployed để auto-enforce |
| `brain/knowledge/corp/docs/` → `core/docs/` | **Discoverability Fix:** 27 docs files chuyển về Front Door `core/docs/` để User tìm thấy ngay. Sub-folders: `architecture/`, `usage_guides/`, `workflows/` |
