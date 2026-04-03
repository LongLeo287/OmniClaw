---
id: plugin-catalog
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.660713
---

# OmniClaw Plugin Catalog
# Version: 3.0 | Updated: 2026-03-24 | Owner: Dept 4 (Registry) + Dept 20 (CIV)
# Evaluated via: ops/workflows/repo-evaluation.md

> **Status legend:**
> - 👁️ = Read/Surveyed
> - 📚 = Reference for learning (not integrating tool — extract knowledge/patterns into brain/knowledge/notes/)
> - 🔖 = Retained (DEFER — use later, state reason)
> - ✅ = In use (track version)
> - ⚡ = Integrating
> - ❌ = Completely removed (REJECT — not used, not learned — state reason)
> - ⏸️ = Unread (needs repo-evaluation.md run)

---

## COGNITIVE PLUGINS (Memory, RAG, Knowledge)

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `LightRAG` | ✅ ACTIVE | Tier 1 | No conflict | Core RAG engine. check weekly. OPEN-004 in progress. |
| `mem0` | ✅ ACTIVE | Tier 1 | Safe | Phase 1 DONE. Hooks: onTaskStart/onTaskComplete/onHandoff. |
| `open-notebook` | ✅ ACTIVE | Tier 2 | — | Nova primary tool. Port 8502/5055. NO Changes:. |
| `open-notebooklm` | ✅ ACTIVE | Tier 2 | — | Audio podcast gen. NO Changes:. |
| `notebooklm-skill` | ✅ ACTIVE | Tier 2 | — | NotebookLM browser automation. Nova primary. |
| `nexusrag` | 🔖 DEFER → Phase 6 | Tier 2 | ⚠️ Overlap LightRAG | **Verdict:** DEFER. Can add UI for LightRAG after PoC. DO NOT deploy separately. |
| `graphrag` | 📚 REFERENCE | — | ⚠️ Overlap LightRAG | **Verdict:** REFERENCE. Tool not used (API-costly), but learn concept **Community Detection** + entity-type extraction. KI: `brain/knowledge/notes/KI-GRAPHRAG-CONCEPTS-01.md` |
| `cognee` | 🔖 DEFER → Phase 6 | Tier 2 | ⚠️ Partial overlap LightRAG | **Verdict:** DEFER. Wait until LightRAG PoC (OPEN-004). If LightRAG is enough then REJECT. |
| `ai-tagger` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Semantic auto-tagging for Knowledge pipeline. No conflict. Integrate when Knowledge dept needs. |
| `smart-search` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Hybrid search (semantic + keyword). Integrate after LightRAG stable. No conflict. |
| `claude-mem` | 📚 REFERENCE | — | ⚠️ Overlap mem0 | **Verdict:** REFERENCE. Tool not used (mem0 better), but learn for handling Claude-specific memory patterns if future API compatibility required. |
| `autoresearchclaw` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Auto research agent — add for web-researcher workflow. Evaluate when Dept R&D needs auto agent. |
| `openrag` | ❌ REJECT | Tier 3 | ❌ nexusrag better | **Verdict:** Previously REJECTED. nexusrag is more complete. Now rejecting both since LightRAG covers. |
| `neural-memory-repo` | 🔖 DEFER → Phase 6 | Tier 2 | Safe | **Verdict:** DEFER. Neural memory implementation — evaluate when advanced memory needed. |
| `notebooklm-mcp` | 👁️ | Tier 2 | Safe | **Verdict:** Read. MCP server for NotebookLM API with session support. |
| `notebooklm-mcp-cli` | ✅ ACTIVE | Tier 2 | — | Active. NotebookLM MCP bridge. |
| `langextract` | ✅ ACTIVE | Tier 2 | — | Active, NO Changes:. check monthly. |

---

## DATA PLUGINS (Web, Scraping, Extraction)

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `firecrawl` | ✅ ACTIVE | Tier 1 | Safe | Phase 2 DONE. Pipeline: Firecrawl→LangExtract→LightRAG. |
| `gitingest` | 🔖 DEFER → Phase 4 | Tier 2 | Safe | **Verdict:** DEFER. GitHub repo → LLM context. Supplement for GitNexus when repo feeding to RAG needed. Integrate when Dept Engineering requires. |
| `scrapling` | 🔖 DEFER → Phase 5 | Tier 2 | ⚠️ Overlap Firecrawl | **Verdict:** DEFER as BACKUP ONLY. Use when Firecrawl has no API key (self-hosted down). DO NOT integrate in parallel. |
| `scrapling-mcp` | ❌ REJECT | Tier 3 | ❌ Duplicate scrapling + Firecrawl | **Verdict:** REJECT. MCP wrapper of scrapling — Firecrawl MCP adapter is better. 2 layers redundant. |
| `agent-browser` | 🔖 DEFER → Phase 4 | Tier 2 | Safe | **Verdict:** DEFER. Browser automation for agent (for JS-rendered content). Supplement Firecrawl for JS-heavy cases. Integrate when Dept Engineering requires. |
| `cerberus-cve-tool` | 🔖 DEFER → Phase 3 | Tier 2 | Safe (security) | **Verdict:** DEFER. CVE scanning — Dept 10 (Security) owned. Integrate into nemoclaw-strix-scan.md pipeline. |
| `pageindex` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Page indexing system — evaluate when web crawling needs grow. |
| `dbcooper` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Database cooperation tools — evaluate when multi-db ops needed. |

---

## ORCHESTRATION PLUGINS (Multi-agent, Workflow)

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `crewai` | ✅ ACTIVE | Tier 1 | Check vs AgAuto | Phase 4 DONE. AI Squad Controller UI live on ClawTask. |
| `bmad-method` | ✅ ACTIVE | Tier 2 | — | Active. BMAD agile method. |
| `MaxKB` | 🔖 DEFER → Phase 7 | Tier 2 | ⚠️ Overlap ClawTask + RAG | **Verdict:** DEFER. Enterprise platform — evaluate only if dedicated KB for client is needed. Currently LightRAG + ClawTask suffice. |
| `all-agentic-architectures` | 📚 REFERENCE | — | — | **Verdict:** REFERENCE. 17 Agent Architectures (Reflection, ReAct, PEV, Blackboard, ToT, Metacognitive...). KI: `brain/knowledge/notes/KI-AGENT-ARCHITECTURES-01.md` |
| `agency-agents` | 📚 CHERRY-PICK | — | — | **Verdict:** CHERRY-PICK. 144 agent templates — do not run install script. Cherry-pick only OmniClaw-missing agents (Code Reviewer, MCP Builder, Incident Commander...). KI: `brain/knowledge/notes/KI-AGENCY-AGENTS-CHERRY-PICK-01.md` |
| `Mini-Agent` | 📚 REFERENCE | — | — | **Verdict:** REFERENCE. Read to learn lightweight agent design pattern. Do not integrate framework, only extract pattern. |
| `AntigravityManager` | 🔖 DEFER → Phase 5 | Tier 2 | Check overlap | **Verdict:** DEFER pending dedup check with antigravity-manager. Might be same repo. Await confirmation. |
| `antigravity-manager` | 🔖 DEFER → Phase 5 | Tier 2 | Check overlap | **Verdict:** DEFER. Dedup check with AntigravityManager. If duplicate → keep 1, REJECT the other. |
| `AstrBot` | 🔖 DEFER → Phase 5 | Tier 2 | Check vs nullclaw | **Verdict:** DEFER. Bot framework — compare with nullclaw (current Telegram bot). If nullclaw is enough → REJECT. |
| `deepagents` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Deep agent framework — evaluate when advanced agent capabilities needed. |
| `pixel-agents` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Pixel-based agents — evaluate when visual processing needed. |
| `openclaw` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. OpenClaw framework — evaluate when open-source claw tools needed. |
| `openclaw-command-center` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. OpenClaw command center — evaluate when centralized control needed. |
| `openclaw-rl` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. OpenClaw reinforcement learning — evaluate when RL capabilities needed. |
| `oh-my-openagent` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Open agent framework — evaluate when extensible agent system needed. |

---

## UI PLUGINS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `ui-ux-pro-max` | ✅ ACTIVE | Tier 2 | — | Active. Premium UI generation. |
| `LobsterBoard` | ✅ ACTIVE | Tier 2 | — | Beta, audit needed. Dashboard UI. |
| `lobe-chat` | 🔖 DEFER → Phase 7 | Tier 2 | ⚠️ Overlap nullclaw | **Verdict:** DEFER. Full AI chat platform — evaluate only if CEO wants public chat UI superior to nullclaw. |
| `antigravity-deck` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Presentation/deck tool for Antigravity. Review when Dept Marketing needs slide generation. |
| `antigravity-mobile` | 🔖 DEFER → Phase 7 | Tier 2 | Safe | **Verdict:** DEFER. Mobile UI — integrate when mobile app plan is clear. |
| `PerformanceStudio` | 🔖 DEFER → Phase 4 | Tier 2 | Safe | **Verdict:** DEFER. Performance monitoring UI — review alongside prometheus-grafana. Dept 14 (Monitoring) owns. |
| `prometheus-grafana-alerts` | 🔖 DEFER → Phase 4 | Tier 2 | Safe | **Verdict:** DEFER. Monitoring stack — integrate into Dept 14 (Monitoring/Inspection). Phase 3 ops. |
| `agentsview` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Agent visualization — add to ClawTask Dashboard. Integrate when AI Squad UI expansion needed. |
| `gaia-ui` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. GAIA user interface — evaluate when needed for GAIA. |
| `lenis` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Smooth scrolling library — evaluate when UI smoothness needed. |

---

## BRIDGE / INTEGRATION PLUGINS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `openspec` | ✅ ACTIVE | Tier 2 | — | Active. OpenSpec automation. |
| `e2b` | 🔖 DEFER → Phase 4 | Tier 2 | Safe | **Verdict:** DEFER. Code execution sandbox — integrate into ACP console (Dept Engineering). Phase 3. |
| `cloud-sync` | 🔖 DEFER → Phase 6 | Tier 2 | Safe | **Verdict:** DEFER. Cloud sync — need to specify provider (S3, GCS?) before integrating. |
| `MiniMax-MCP` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. MiniMax API bridge — integrate when LLM Router needs MiniMax model (Example: video/audio gen). |
| `MiniMax-MCP-JS` | ❌ REJECT | Tier 3 | ❌ Duplicate MiniMax-MCP | **Verdict:** REJECT. JS version of MiniMax-MCP — Python version prioritized as OmniClaw is Python-first. |
| `OpenSandbox` | ❌ REJECT | Tier 3 | ❌ Duplicate e2b | **Verdict:** REJECT. e2b maintained better, has docs, team, and is preferred to OpenSandbox. |
| `OpenShell` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Open shell interface — evaluate when enhanced shell needed. |
| `openviking` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Viking-inspired tools — evaluate for historical/Norse-themed tools. |
| `mcp-client` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. MCP client tools — evaluate when enhanced MCP client needed. |
| `context7` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Real-time library documentation system. |

---

## SECURITY PLUGINS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `zeroleaks` | ✅ ACTIVE | Tier 2 | — | Active. Secret leak prevention. check monthly. |
| `claude-bug-bounty` | ❌ REJECT | Tier 3 | — | **Verdict:** REJECT. This is a flow/methodology, not an integrable tool. Reference docs, do not clone into system. |
| `trufflehog` | 🔖 DEFER → Phase 3 | Tier 2 | Safe — complement zeroleaks | **Verdict:** DEFER. Secret scanning deep scan (Git history). Complements zeroleaks. Dept 10 (Security) integrates into strix-scan pipeline. |
| `GitHacker` | ❌ REJECT | Tier 3 | ⚠️ Offensive tool | **Verdict:** REJECT. Git exploitation tool — offensive security. OmniClaw uses defensive tools only. |
| `identYwaf` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Identity WAF protection — evaluate when advanced web security needed. |
| `kong-reverse-engineer` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Kong reverse engineering — evaluate for API gateway reverse engineering. |

---

## SKILL PACKS (Reference — not standalone plugins)

| Repo | Verdict | Notes |
|------|---------|---------|
| `agent-skills-standard` | ✅ ACTIVE | Standard skill templates. |
| `anthropic-skills` | ✅ ACTIVE | Anthropic extensions. |
| `antigravity-kit` | ✅ ACTIVE (auto-load) | Core kit. |
| `cloudflare-skills` | ✅ ACTIVE | Cloudflare deployment. |
| `vercel-agent-skills` | ✅ ACTIVE | Vercel deployment. |
| `vercel-labs-skills` | ✅ ACTIVE | Vercel labs. |
| `carlrannaberg-claudekit` | ✅ ACTIVE | ClaudeKit fork. |
| `claudekit` | ✅ ACTIVE | Core ClaudeKit. |
| `antigravity-awesome-skills` | 🔖 DEFER → Phase 4 | **Verdict:** DEFER. Review skill list for missing skills in SKILL_REGISTRY.json → cherry-pick and import, do not clone all. |
| `awesome-agent-skills` | 🔖 DEFER → Phase 4 | **Verdict:** DEFER. Same as above — cherry-pick, do not clone. |
| `awesome-claude-skills` | 🔖 DEFER → Phase 4 | **Verdict:** Same — cherry-pick relevant Claude-specific skills for OmniClaw. |
| `ai-engineering-toolkit` | 🔖 DEFER → Phase 5 | **Verdict:** DEFER. Comprehensive toolkit — evaluate when Dept Engineering needs toolkit expansion. |
| `api-mega-list` | 🔖 REFERENCE | **Verdict:** REFERENCE ONLY. API list — non-integrated. Consult for finding new APIs. |
| `affiliate-skills` | 👁️ | Reference | Affiliate marketing skills — reference for marketing automation. |
| `affitor-affiliate-skills` | 👁️ | Reference | Affiliate marketing skills — reference for marketing automation. |
| `affitor-network` | 👁️ | Reference | Affiliate network tools — reference for network expansion. |
| `composio-awesome-claude-skills` | 👁️ | Reference | Composio Claude skills — reference for integration. |
| `skills-chronicle` | 👁️ | Reference | Skills chronicle — for skill tracking. |
| `skills-manager` | 👁️ | Reference | Skills management — for skill lifecycle. |
| `skill-generator` | 🔖 DEFER → Phase 5 | **Verdict:** DEFER. Skill generation tools — evaluate for auto-generated skills. |

---

## AUTOMATION & WORKFLOW PLUGINS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `ag-auto-click-scroll` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Auto click and scroll automation — evaluate for UI automation. |
| `agent-smart-memo` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Smart memo agent — evaluate for enhanced memo. |
| `agentsview` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Agent visualization — evaluate for agent visualization. |
| `assistant-context` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Assistant context management — evaluate for context management. |
| `hivemind-plugin` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Hivemind collaboration — evaluate for distributed intelligence. |

---

## DEVELOPMENT TOOLS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `claude-code-best-practice` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Claude Code best practices — reference for coding standards. |
| `claude-code-prod-plugin` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Claude Code production plugin — reference for production setup. |
| `claude-code-setup` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Claude Code setup — reference for initialization. |
| `claude-code-templates` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Claude Code templates — reference for project templates. |
| `everything-claude-code` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Everything Claude Code — comprehensive reference. |
| `learn-claude-code` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Learning Claude Code — educational reference. |
| `ralph-claude-code` | 👁️ | Tier 2 | Safe | **Verdict:** Read. Ralph Claude Code tools — reference for alternate implementations. |

---

## AI & ML TOOLS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `claude-octopus` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claude Octopus tool — evaluate for advanced Claude capabilities. |
| `claude-scientific-skills` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Scientific skills for Claude — evaluate for scientific computing. |
| `claude-usage-checker` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claude usage checker — evaluate for usage monitoring. |
| `claude-ws` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claude WebSocket interface — evaluate for WebSocket communication. |
| `generative-ai-beginners` | 📚 REFERENCE | — | Safe | **Verdict:** REFERENCE. Generative AI for beginners — educational reference. |
| `learn-ai-engineering` | 📚 REFERENCE | — | Safe | **Verdict:** REFERENCE. AI engineering learning — educational reference. |
| `llm-finetuning` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. LLM fine-tuning tools — evaluate for model customization. |
| `llm-mux` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. LLM multiplexer — evaluate for LLM routing. |
| `qwen2-omni` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Qwen2 Omni model — evaluate for multi-modal models. |

---

## COMMUNICATION & COLLABORATION

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `antigravity-switcher` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Antigravity mode switcher — evaluate for mode switching. |
| `vscode-antigravity-cockpit` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. VSCode Antigravity cockpit — evaluate for VSCode integration. |
| `claudy-registry` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claudy registry — evaluate for registry system. |

---

## UTILITIES & SUPPORT TOOLS

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `awesome-openclaw-agents` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Awesome OpenClaw agents — evaluate for OpenClaw agents. |
| `awesome-web-agents` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Awesome web agents — evaluate for web automation. |
| `bmad-method` | ✅ ACTIVE | Tier 2 | — | Active. BMAD agile method. |
| `ccpoke` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. CC Poke tool — evaluate for Claude poking. |
| `claws` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claw tools — evaluate for enhanced claw tools. |
| `clawwork` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Claw work tools — evaluate for improved claw workflow. |
| `fbi-watchdog` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Security watchdog — evaluate for enhanced security monitoring. |
| `port-killer` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Port killing utility — evaluate for port management. |
| `setup-n8n` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. n8n setup tools — evaluate for workflow automation. |
| `simonw-llm` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Simon Willison LLM tools — evaluate for specific LLM utilities. |

---

## CONTENT & MEDIA

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `videocaptioner` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Video captioning — evaluate for video processing. |
| `vieneu-tts` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Vietnamese TTS — evaluate for Vietnamese speech synthesis. |
| `vinagent` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Vietnamese agent tools — evaluate for Vietnam-specific needs. |
| `okara-crypto` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Crypto tools — evaluate for cryptocurrency features. |

---

## LEARNING & COGNITIVE

| Repo | Verdict | Tier | Conflict check | Notes |
|------|---------|------|----------------|---------|
| `socraticode` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Socratic learning tools — evaluate for Socratic method learning. |
| `think-better` | 🔖 DEFER → Phase 5 | Tier 2 | Safe | **Verdict:** DEFER. Better thinking tools — evaluate for cognitive improvement. |

---

## VERSION TRACKING — Tier 1 (Always Active)

| Plugin | Tier | Check frequency | Update command |
|--------|------|----------------|--------------|
| `LightRAG` | 1 | Weekly | `cd plugins/LightRAG && git pull` |
| `firecrawl` | 1 | Weekly | `pip install --upgrade firecrawl-py` |
| `mem0` | 1 | Weekly | `pip install --upgrade mem0ai` |
| `crewai` | 1 | Weekly | `pip install --upgrade crewai` |
| `open-notebook` | 2 | Monthly | `git pull` |
| `langextract` | 2 | Monthly | `git pull` |
| `zeroleaks` | 2 | Monthly | `git pull` |
| `antigravity-kit` | 2 | Weekly | `git pull` |

---

## INTEGRATION PRIORITY QUEUE (Updated)

```
✅ DONE: Phase 1 — mem0 (Tier 1 Core Memory)
✅ DONE: Phase 2 — firecrawl (Tier 1 Web Intelligence)
✅ DONE: Phase 3 — LightRAG (Tier 1 Knowledge Graph)
✅ DONE: Phase 4 — CrewAI (Tier 1 Multi-Agent)
✅ DONE: Catalog Evaluation — All repos have VERDICT

⏳ Phase 3 (Next): cerberus-cve-tool → trufflehog (Dept 10 Security pipeline)
⏳ Phase 4 (Next): gitingest + agent-browser + e2b (Dept Engineering tools)
⏳ Phase 4 (Next): PerformanceStudio + prometheus-grafana (Dept 14 Monitoring)
⏳ Phase 4 (Next): Skill cherry-pick from antigravity-awesome-skills / awesome-claude-skills
⏳ Phase 5 (Later): agentsview, antigravity-deck, MiniMax-MCP, ai-tagger
⏳ Phase 5 (Later): AstrBot (compare vs nullclaw first), AntigravityManager (dedup check)
⏳ Phase 5 (Later): All deferred plugins based on departmental needs
⏳ Phase 6 (Future): cognee, nexusrag (after LightRAG PoC review), cloud-sync
⏳ Phase 7 (Future): MaxKB, lobe-chat, antigravity-mobile
```

---

## REJECT SUMMARY — Reasons why each repo was removed

| Repo | REJECT Reason |
|------|--------------|
| `graphrag` | Duplicate LightRAG, costly cloud API, LightRAG is better locally |
| `claude-mem` | Duplicate mem0, only supports Claude, mem0 is cross-platform |
| `openrag` | nexusrag is better, now both replaced by LightRAG |
| `scrapling-mcp` | Duplicate Firecrawl MCP adapter, 2 redundant layers |
| `agency-agents` | Duplicate OmniClaw Corp agent system is more complete |
| `Mini-Agent` | Duplicate sub-agent layer of OmniClaw |
| `MiniMax-MCP-JS` | Duplicate MiniMax-MCP Python version, OmniClaw is Python-first |
| `OpenSandbox` | Duplicate e2b, e2b better maintained |
| `claude-bug-bounty` | Methodology, not a tool, cannot be integrated |
| `GitHacker` | Offensive security tool, OmniClaw uses only defensive |

---

*Last updated: 2026-03-24 | CIV Verdict by: Claude Code (automated)*
*"Every repo earns its place. No clone without verdict."*

---
