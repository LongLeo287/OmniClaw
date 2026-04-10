# CIV INTAKE LOG — QUARANTINE
# Version: 1.0 | Owner: intake-chief-agent
# Updated: 2026-03-17

---

## ACTIVE TICKETS

---

### CIV-2026-03-17-001

```
Source:   https://github.com/agentskills/agentskills
Type:     REPO
Staged:   QUARANTINE/incoming/repos/agentskills-agentskills/
Status:   RECEIVED → CLASSIFYING → VALIDATED → VETTED → ROUTED ✅
Opened:   2026-03-17T16:16:48+07:00
Closed:   2026-03-17T16:20:00+07:00
```

Classification: REPO — GitHub URL, has SKILL.md, .git structure, org=agentskills
Vet result: PASS (maintained by Anthropic, official agentskills.io spec, Apache-2.0 licensed)
Quality score: 10/10 — Official spec repo, foundational reference
VALUE_TYPES: SKILL, KNOWLEDGE, WORKFLOW
Primary value: SKILL (contains SKILL.md spec + reference SDK + example skills)
- SKILL: defines the open format our AI OS already uses — reference implementation
- KNOWLEDGE: documentation on skill architecture and design patterns
- WORKFLOW: documents how agents discover, load, and execute skills

Routing receipt:
- → skills/agentskills-spec/ — skill-creator-agent: catalog as foundational spec
- → knowledge/agent_architecture/ — knowledge-curator: index as core reference
- → workflows/agent-skill-discovery.md — archivist: extract skill lifecycle workflow
Notified: skill-creator-agent, knowledge-curator-agent, archivist-agent

---

### CIV-2026-03-17-002

```
Source:   https://github.com/mukul975/Anthropic-Cybersecurity-Skills
Type:     REPO
Staged:   QUARANTINE/incoming/repos/anthropic-cybersecurity-skills/
Status:   RECEIVED → CLASSIFYING → VALIDATED → VETTED → ROUTED ✅
Opened:   2026-03-17T16:16:48+07:00
Closed:   2026-03-17T16:20:00+07:00
```

Classification: REPO — GitHub URL, skill collection repo
Vet result: PASS (Apache-2.0, community-maintained, NOT official Anthropic — name refers to agentskills.io compatibility)
Security flag: Contains offensive cybersec techniques (malware analysis, dark web monitoring).
  PASS for ingestion | RESTRICTED_DEPLOY — Security GRC review required before agent use.
Quality score: 9/10 — 734 structured skills, MITRE ATT&CK mapped, multi-platform compatible
VALUE_TYPES: SKILL, KNOWLEDGE
Primary value: SKILL (734 cybersec skills — AWS S3 Audit, Azure AD, GCP, APT Analysis, DFIR, SOC, Container Sec)

Routing receipt:
- → skills/cybersecurity/ (new bundle folder) — skill-creator-agent: bulk catalog 734 skills, tag [RESTRICTED_DEPLOY]
- → knowledge/cybersecurity/mitre_attck/ — knowledge-curator: MITRE mapping index
Enrichment alert → strix-agent (Security GRC): LOAD 734 cybersec skills after Security GRC review
Notified: skill-creator-agent, knowledge-curator-agent, strix-agent

---

### CIV-2026-03-17-003

```
Source:   https://github.com/dantech0xff/ui-ux-pro-max-skill-fork
Type:     REPO
Staged:   QUARANTINE/incoming/repos/ui-ux-pro-max-skill-fork/
Status:   RECEIVED → CLASSIFYING → VALIDATED → VETTED → ROUTED ✅
Opened:   2026-03-17T16:16:48+07:00
Closed:   2026-03-17T16:20:00+07:00
```

Classification: REPO — GitHub URL, fork of nextlevelbuilder/ui-ux-pro-max-skill
Original repo: nextlevelbuilder/ui-ux-pro-max-skill (42.8k stars, 4.1k forks, v2.1.3)
Vet result: PASS (fork of high-reputation source, skill format only, no executable code risk)
Quality score: 8/10 — High-quality fork of a well-starred skill; may contain customizations
VALUE_TYPES: SKILL, KNOWLEDGE
Primary value: SKILL (UI/UX design intelligence — multi-platform professional design AI skill)

Routing receipt:
- → skills/ui-ux/ui-ux-pro-max/ — skill-creator-agent: catalog skill, tag as fork of v2.1.3
- → knowledge/design/ui_ux_patterns/ — knowledge-curator: design patterns knowledge
Enrichment alert → Engineering + Marketing depts: ui-ux-pro-max skill available for design work
Notified: skill-creator-agent, knowledge-curator-agent, training-agent

---

## ENRICHMENT ALERTS — Cycle 2026-03-17

| Ticket | Alert To | Content | Priority |
|--------|----------|---------|----------|
| CIV-001 | skill-creator-agent | agentskills spec + SDK | HIGH |
| CIV-002 | strix-agent + Security GRC | 734 cybersec skills [RESTRICTED_DEPLOY] | HIGH |
| CIV-003 | training-agent → Engineering + Marketing | ui-ux-pro-max design skill | MEDIUM |

---

## STATS — Cycle 2026-03-17

- Total received: 3
- Classified: 3 (100%)
- Vetted PASS: 3 | FAIL: 0
- Routed: 3 (100%)
- Pending: 0
- **CIV-20260326-TaxHacker** | 2026-03-26 21:52:19 | REPO | https://github.com/vas3k/TaxHacker | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-waoowaoo** | 2026-03-26 21:52:21 | REPO | https://github.com/saturndec/waoowaoo | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-gitagent** | 2026-03-26 21:52:24 | REPO | https://github.com/open-gitagent/gitagent | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agenttrafficcontrol** | 2026-03-26 21:52:30 | REPO | https://github.com/gkamradt/agenttrafficcontrol | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-code-review-graph** | 2026-03-26 21:52:31 | REPO | https://github.com/tirth8205/code-review-graph | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-web-check** | 2026-03-26 22:02:00 | REPO | https://github.com/Lissy93/web-check | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agents-course** | 2026-03-26 22:02:02 | REPO | https://github.com/huggingface/agents-course | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-xpfarm** | 2026-03-26 22:02:04 | REPO | https://github.com/A3-N/xpfarm | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-AIDA** | 2026-03-26 22:02:05 | REPO | https://github.com/Vasco0x4/AIDA | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-distil-text2sql** | 2026-03-26 22:02:06 | REPO | https://github.com/distil-labs/distil-text2sql | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-public-apis** | 2026-03-26 22:02:08 | REPO | https://github.com/public-apis/public-apis | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ossinsight** | 2026-03-26 22:02:12 | REPO | https://github.com/pingcap/ossinsight | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-codymaster** | 2026-03-26 22:02:14 | REPO | https://github.com/tody-agent/codymaster | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-trivy** | 2026-03-26 22:02:37 | REPO | https://github.com/aquasecurity/trivy | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-awesome-copilot** | 2026-03-26 22:02:42 | REPO | https://github.com/github/awesome-copilot | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-awesome-agent-skills** | 2026-03-26 22:02:43 | REPO | https://github.com/VoltAgent/awesome-agent-skills | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-spec-kit** | 2026-03-26 22:02:48 | REPO | https://github.com/github/spec-kit | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-wtfjs** | 2026-03-26 22:02:49 | REPO | https://github.com/denysdovhan/wtfjs | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-gitignore** | 2026-03-26 22:02:51 | REPO | https://github.com/github/gitignore | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agentscope** | 2026-03-26 22:02:58 | REPO | https://github.com/agentscope-ai/agentscope | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Observer** | 2026-03-26 22:03:01 | REPO | https://github.com/Roy3838/Observer | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-everything-claude-code** | 2026-03-26 22:03:04 | REPO | https://github.com/affaan-m/everything-claude-code | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-hyperspace-db** | 2026-03-26 22:03:07 | REPO | https://github.com/YARlabs/hyperspace-db | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agentune** | 2026-03-26 22:03:08 | REPO | https://github.com/tqdat410/agentune | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-seeaifirst** | 2026-03-26 22:03:10 | REPO | https://github.com/BARONFANTHE/seeaifirst | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agent-skills-standard** | 2026-03-26 22:03:12 | REPO | https://github.com/HoangNguyen0403/agent-skills-standard | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-rune** | 2026-03-26 22:03:13 | REPO | https://github.com/rune-kit/rune | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Archon** | 2026-03-26 22:03:15 | REPO | https://github.com/coleam00/Archon | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-plotly.js** | 2026-03-26 22:03:31 | REPO | https://github.com/plotly/plotly.js/ | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-vibe-kanban** | 2026-03-26 22:03:37 | REPO | https://github.com/BloopAI/vibe-kanban | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ag-live-code** | 2026-03-26 22:03:38 | REPO | https://github.com/zixfelw/ag-live-code | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-pattern-craft** | 2026-03-26 22:03:48 | REPO | https://github.com/megh-bari/pattern-craft | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-wifi-card** | 2026-03-26 22:03:49 | REPO | https://github.com/bndw/wifi-card | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-hexhog** | 2026-03-26 22:03:51 | REPO | https://github.com/DVDTSB/hexhog | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Understand-Anything** | 2026-03-26 22:03:54 | REPO | https://github.com/Lum1104/Understand-Anything | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Vane** | 2026-03-26 22:03:58 | REPO | https://github.com/ItzCrazyKns/Vane | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-claude-inspector** | 2026-03-26 22:04:00 | REPO | https://github.com/kangraemin/claude-inspector | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-tinyfish-cookbook** | 2026-03-26 22:04:04 | REPO | https://github.com/tinyfish-io/tinyfish-cookbook | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agentql** | 2026-03-26 22:04:06 | REPO | https://github.com/tinyfish-io/agentql | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-posthog** | 2026-03-26 22:04:57 | REPO | https://github.com/posthog/posthog | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-excalidraw** | 2026-03-26 22:05:02 | REPO | https://github.com/excalidraw/excalidraw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-database-js** | 2026-03-26 22:05:03 | REPO | https://github.com/planetscale/database-js | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-crotmail** | 2026-03-26 22:05:04 | REPO | https://github.com/imnoob59/crotmail | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-prebuiltui** | 2026-03-26 22:05:09 | REPO | https://github.com/prebuiltui/prebuiltui | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-claude-code-templates** | 2026-03-26 22:05:15 | REPO | https://github.com/davila7/claude-code-templates | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-documentation** | 2026-03-26 22:05:17 | REPO | https://github.com/feature-sliced/documentation | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-magicui** | 2026-03-26 22:05:20 | REPO | https://github.com/magicuidesign/magicui | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-OptikR** | 2026-03-26 22:05:23 | REPO | https://github.com/OptikR/OptikR | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-developer-roadmap** | 2026-03-26 22:05:33 | REPO | https://github.com/kamranahmedse/developer-roadmap | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-pathway** | 2026-03-26 22:05:43 | REPO | https://github.com/pathwaycom/pathway | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-hermes-agent** | 2026-03-26 22:06:36 | REPO | https://github.com/nousresearch/hermes-agent | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-anime** | 2026-03-26 22:06:38 | REPO | https://github.com/juliangarnier/anime | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-system_prompts_leaks** | 2026-03-26 22:06:39 | REPO | https://github.com/asgeirtj/system_prompts_leaks | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-port-killer** | 2026-03-26 22:06:41 | REPO | https://github.com/productdevbook/port-killer | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-opencode** | 2026-03-26 22:06:49 | REPO | https://github.com/anomalyco/opencode | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-free-llm-api-resources** | 2026-03-26 22:07:04 | REPO | https://github.com/cheahjs/free-llm-api-resources | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-react-doctor** | 2026-03-26 22:07:06 | REPO | https://github.com/millionco/react-doctor | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-npkill** | 2026-03-26 22:07:09 | REPO | https://github.com/voidcosmos/npkill | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-My-Brain-Is-Full-Crew** | 2026-03-26 22:07:10 | REPO | https://github.com/gnekt/My-Brain-Is-Full-Crew | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-FinRL** | 2026-03-26 22:07:13 | REPO | https://github.com/AI4Finance-Foundation/FinRL | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agent-orchestrator** | 2026-03-26 22:07:15 | REPO | https://github.com/ComposioHQ/agent-orchestrator | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-openclaw** | 2026-03-26 22:07:23 | REPO | https://github.com/openclaw/openclaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-TradingAgents** | 2026-03-26 22:07:24 | REPO | https://github.com/TauricResearch/TradingAgents | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-deer-flow** | 2026-03-26 22:07:27 | REPO | https://github.com/bytedance/deer-flow | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-tulip** | 2026-03-26 22:07:28 | REPO | https://github.com/OpenAttackDefenseTools/tulip | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-termote** | 2026-03-26 22:07:30 | REPO | https://github.com/lamngockhuong/termote | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-trans-faster** | 2026-03-26 22:07:31 | REPO | https://github.com/SangVoM/trans-faster | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-lstack** | 2026-03-26 22:07:33 | REPO | https://github.com/marixdev/lstack | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-rsync** | 2026-03-26 22:07:34 | REPO | https://github.com/RsyncProject/rsync | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-llm-lean-log** | 2026-03-26 22:07:36 | REPO | https://github.com/loclv/llm-lean-log | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-pentagi** | 2026-03-26 22:07:37 | REPO | https://github.com/vxcontrol/pentagi | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-chat-quality-agent** | 2026-03-26 22:07:39 | REPO | https://github.com/tanviet12/chat-quality-agent | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-picoclaw** | 2026-03-26 22:07:42 | REPO | https://github.com/sipeed/picoclaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-claude-subconscious** | 2026-03-26 22:07:43 | REPO | https://github.com/letta-ai/claude-subconscious | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-llmfit** | 2026-03-26 22:07:45 | REPO | https://github.com/AlexsJones/llmfit | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-goclaw** | 2026-03-26 22:07:47 | REPO | https://github.com/nextlevelbuilder/goclaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-NemoClaw** | 2026-03-26 22:07:49 | REPO | https://github.com/NVIDIA/NemoClaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ClawWork** | 2026-03-26 22:08:27 | REPO | https://github.com/HKUDS/ClawWork | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ClawX** | 2026-03-26 22:08:35 | REPO | https://github.com/ValueCell-ai/ClawX | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ClawRouter** | 2026-03-26 22:08:40 | REPO | https://github.com/BlockRunAI/ClawRouter | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ClawTeam** | 2026-03-26 22:08:42 | REPO | https://github.com/HKUDS/ClawTeam | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-clawhub** | 2026-03-26 22:08:43 | REPO | https://github.com/openclaw/clawhub | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-AutoResearchClaw** | 2026-03-26 22:08:47 | REPO | https://github.com/aiming-lab/AutoResearchClaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-MetaClaw** | 2026-03-26 22:08:55 | REPO | https://github.com/aiming-lab/MetaClaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-PUAClaw** | 2026-03-26 22:08:57 | REPO | https://github.com/puaclaw/PUAClaw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-poco-claw** | 2026-03-26 22:09:03 | REPO | https://github.com/poco-ai/poco-claw | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-lobsters** | 2026-03-26 22:09:06 | REPO | https://github.com/lobsters/lobsters | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-LobsterAI** | 2026-03-26 22:09:08 | REPO | https://github.com/netease-youdao/LobsterAI | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-lobster** | 2026-03-26 22:09:21 | REPO | https://github.com/aardappel/lobster | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-OpenSandbox** | 2026-03-26 22:09:26 | REPO | https://github.com/alibaba/OpenSandbox | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Lazy-downloader** | 2026-03-26 22:09:27 | REPO | https://github.com/tranhaonguyendev/Lazy-downloader | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-waybacktweets** | 2026-03-26 22:09:28 | REPO | https://github.com/claromes/waybacktweets | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-autoresearch** | 2026-03-26 22:09:30 | REPO | https://github.com/karpathy/autoresearch | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-browser-use** | 2026-03-26 22:09:31 | REPO | https://github.com/browser-use/browser-use | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-stitchSkill** | 2026-03-26 22:09:33 | REPO | https://github.com/arinnem/stitchSkill | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-stitch-skills** | 2026-03-26 22:09:34 | REPO | https://github.com/google-labs-code/stitch-skills | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Memento-Skills** | 2026-03-26 22:09:38 | REPO | https://github.com/Memento-Teams/Memento-Skills | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-project-nomad** | 2026-03-26 22:09:40 | REPO | https://github.com/Crosstalk-Solutions/project-nomad | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-firecrawl** | 2026-03-26 22:09:51 | REPO | https://github.com/firecrawl/firecrawl | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-claude-hud** | 2026-03-26 22:09:52 | REPO | https://github.com/jarrodwatts/claude-hud | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-agent-skill-creator** | 2026-03-26 22:09:55 | REPO | https://github.com/FrancyJGLisboa/agent-skill-creator | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-SoulSync** | 2026-03-26 22:09:58 | REPO | https://github.com/Nezreka/SoulSync | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-prompts.chat** | 2026-03-26 22:10:05 | REPO | https://github.com/f/prompts.chat | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-markitdown** | 2026-03-26 22:10:07 | REPO | https://github.com/microsoft/markitdown | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Kaku** | 2026-03-26 22:10:16 | REPO | https://github.com/tw93/Kaku | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-HolyClaude** | 2026-03-26 22:10:20 | REPO | https://github.com/CoderLuii/HolyClaude | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-OpenSpace** | 2026-03-26 22:10:25 | REPO | https://github.com/HKUDS/OpenSpace | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-openhay** | 2026-03-26 22:10:27 | REPO | https://github.com/openhay-ai/openhay | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-OpenClaw-bot-review** | 2026-03-26 22:10:29 | REPO | https://github.com/xmanrui/OpenClaw-bot-review | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-MetaDetective** | 2026-03-26 22:10:31 | REPO | https://github.com/franckferman/MetaDetective | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-hello-agents** | 2026-03-26 22:10:41 | REPO | https://github.com/datawhalechina/hello-agents | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Star-Office-UI** | 2026-03-26 22:10:44 | REPO | https://github.com/ringhyacinth/Star-Office-UI | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-quran-validator** | 2026-03-26 22:10:49 | REPO | https://github.com/yazinsai/quran-validator | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-auto-maintainer** | 2026-03-26 22:10:51 | REPO | https://github.com/yazinsai/auto-maintainer | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-OpenOats** | 2026-03-26 22:10:52 | REPO | https://github.com/yazinsai/OpenOats | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-claude-code-remote** | 2026-03-26 22:10:54 | REPO | https://github.com/yazinsai/claude-code-remote | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ai-spreadsheet** | 2026-03-26 22:10:55 | REPO | https://github.com/yazinsai/ai-spreadsheet | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-town** | 2026-03-26 22:10:57 | REPO | https://github.com/yazinsai/town | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-awp-skill** | 2026-03-26 22:10:59 | REPO | https://github.com/awp-core/awp-skill | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-awesome-opensource-data-engineering** | 2026-03-26 22:11:00 | REPO | https://github.com/gunnarmorling/awesome-opensource-data-engineering | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-skills** | 2026-03-26 22:11:01 | REPO | https://github.com/slavingia/skills | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Claw-CLI** | 2026-03-26 22:11:07 | REPO | https://github.com/jiulingyun/Claw-CLI | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-formulae.brew.sh** | 2026-03-26 22:11:08 | REPO | https://github.com/Homebrew/formulae.brew.sh | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-terravision** | 2026-03-26 22:11:12 | REPO | https://github.com/patrickchugh/terravision | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-openzalo** | 2026-03-26 22:11:13 | REPO | https://github.com/darkamenosa/openzalo | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-graphiti** | 2026-03-26 22:11:15 | REPO | https://github.com/getzep/graphiti | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-tookie-osint** | 2026-03-26 22:11:17 | REPO | https://github.com/Alfredredbird/tookie-osint | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Machine-Learning-Projects** | 2026-03-26 22:11:36 | REPO | https://github.com/shsarv/Machine-Learning-Projects | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-ContribAI** | 2026-03-26 22:11:38 | REPO | https://github.com/tang-vu/ContribAI | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-maptoposter** | 2026-03-26 22:11:58 | REPO | https://github.com/originalankur/maptoposter | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Claude-Code-Game-Studios** | 2026-03-26 22:12:00 | REPO | https://github.com/Donchitos/Claude-Code-Game-Studios | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Dopamine** | 2026-03-26 22:12:02 | REPO | https://github.com/opa334/Dopamine | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-free-programming-books** | 2026-03-26 22:12:04 | REPO | https://github.com/EbookFoundation/free-programming-books | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-litellm** | 2026-03-26 22:12:47 | REPO | https://github.com/BerriAI/litellm | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-codex** | 2026-03-26 22:12:50 | REPO | https://github.com/openai/codex | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-pageel-cms** | 2026-03-26 22:12:52 | REPO | https://github.com/pageel/pageel-cms | STATUS: Bố trí vào QUARANTINE
- **CIV-20260326-Open-Higgsfield-AI** | 2026-03-26 22:12:54 | REPO | https://github.com/Anil-matcha/Open-Higgsfield-AI | STATUS: Bố trí vào QUARANTINE
| 2026-03-27 19:47 | affitor-affiliate-skills | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | antigravity-deck-tysonnbt | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | antigravity-kit | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | autoresearchclaw | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | awesome-openclaw-agents | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | cerberus-hackunderway | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | claude-octopus | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | claude-scientific-skills | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | deepagents-langchain | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | fbi-watchdog | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | MaxKB | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | okara-crypto | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | openrag | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | affitor-affiliate-skills | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | antigravity-deck-tysonnbt | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | antigravity-kit | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | autoresearchclaw | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | awesome-openclaw-agents | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | cerberus-hackunderway | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | claude-octopus | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | claude-scientific-skills | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | deepagents-langchain | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | fbi-watchdog | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | MaxKB | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | okara-crypto | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:47 | openrag | INGESTED | Batch ingest from QUARANTINE |
| 2026-03-27 19:57 | Claude-Usage-Checker | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/0xAstroAlpha/Claude-Usage-Checker |
| 2026-03-27 19:57 | agent-skills-standard | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HoangNguyen0403/agent-skills-standard |
| 2026-03-27 19:57 | MiniMax-MCP-JS | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/MiniMax-AI/MiniMax-MCP-JS |
| 2026-03-27 19:57 | notebooklm-mcp | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/PleasePrompto/notebooklm-mcp |
| 2026-03-27 19:57 | notebooklm-skill | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/PleasePrompto/notebooklm-skill |
| 2026-03-27 19:57 | zeroleaks | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ZeroLeaks/zeroleaks |
| 2026-03-27 19:57 | everything-claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/affaan-m/everything-claude-code |
| 2026-03-27 19:57 | claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/anthropics/claude-code |
| 2026-03-27 19:57 | claudekit | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/carlrannaberg/claudekit |
| 2026-03-27 19:57 | skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/cloudflare/skills |
| 2026-03-27 19:57 | langextract | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/google/langextract |
| 2026-03-27 19:57 | notebooklm-mcp-cli | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/jacob-bd/notebooklm-mcp-cli |
| 2026-03-27 19:57 | port-killer | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/productdevbook/port-killer |
| 2026-03-27 19:57 | claude-mem | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/thedotmack/claude-mem |
| 2026-03-27 19:57 | context7 | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/upstash/context7 |
| 2026-03-27 19:57 | agent-skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vercel-labs/agent-skills |
| 2026-03-27 19:57 | AntigravityManager | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Draculabo/AntigravityManager |
| 2026-03-27 19:57 | OpenSpec | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Fission-AI/OpenSpec |
| 2026-03-27 19:57 | ClawWork | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HKUDS/ClawWork |
| 2026-03-27 19:57 | BMAD-METHOD | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/bmad-code-org/BMAD-METHOD |
| 2026-03-27 19:57 | open-notebooklm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/gabrielchua/open-notebooklm |
| 2026-03-27 19:57 | open-notebook | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/lfnovo/open-notebook |
| 2026-03-27 19:57 | antigravity-kit | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vudovn/antigravity-kit |
| 2026-03-27 19:57 | LightRAG | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HKUDS/LightRAG |
| 2026-03-27 19:57 | firecrawl | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/firecrawl/firecrawl |
| 2026-03-27 19:57 | mem0 | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/mem0ai/mem0 |
| 2026-03-27 19:57 | assistant-context | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huynamboz/assistant-context |
| 2026-03-27 19:57 | awesome-claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/hesreallyhim/awesome-claude-code |
| 2026-03-27 19:57 | LobsterBoard | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/curbob/LobsterBoard |
| 2026-03-27 19:57 | awesome | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/sindresorhus/awesome |
| 2026-03-27 19:57 | public-apis | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/public-apis/public-apis |
| 2026-03-27 19:57 | vscode | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/microsoft/vscode |
| 2026-03-27 19:57 | Claude-Usage-Checker | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/0xAstroAlpha/Claude-Usage-Checker |
| 2026-03-27 19:58 | agent-skills-standard | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HoangNguyen0403/agent-skills-standard |
| 2026-03-27 19:58 | MiniMax-MCP-JS | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/MiniMax-AI/MiniMax-MCP-JS |
| 2026-03-27 19:58 | notebooklm-mcp | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/PleasePrompto/notebooklm-mcp |
| 2026-03-27 19:58 | notebooklm-skill | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/PleasePrompto/notebooklm-skill |
| 2026-03-27 19:58 | zeroleaks | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ZeroLeaks/zeroleaks |
| 2026-03-27 19:58 | everything-claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/affaan-m/everything-claude-code |
| 2026-03-27 19:58 | claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/anthropics/claude-code |
| 2026-03-27 19:58 | claudekit | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/carlrannaberg/claudekit |
| 2026-03-27 19:58 | skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/cloudflare/skills |
| 2026-03-27 19:58 | langextract | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/google/langextract |
| 2026-03-27 19:58 | notebooklm-mcp-cli | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/jacob-bd/notebooklm-mcp-cli |
| 2026-03-27 19:58 | port-killer | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/productdevbook/port-killer |
| 2026-03-27 19:58 | claude-mem | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/thedotmack/claude-mem |
| 2026-03-27 19:58 | context7 | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/upstash/context7 |
| 2026-03-27 19:58 | agent-skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vercel-labs/agent-skills |
| 2026-03-27 19:58 | AntigravityManager | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Draculabo/AntigravityManager |
| 2026-03-27 19:58 | OpenSpec | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Fission-AI/OpenSpec |
| 2026-03-27 19:59 | ClawWork | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HKUDS/ClawWork |
| 2026-03-27 19:59 | BMAD-METHOD | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/bmad-code-org/BMAD-METHOD |
| 2026-03-27 19:59 | open-notebooklm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/gabrielchua/open-notebooklm |
| 2026-03-27 20:00 | open-notebook | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/lfnovo/open-notebook |
| 2026-03-27 20:00 | antigravity-kit | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vudovn/antigravity-kit |
| 2026-03-27 20:00 | LightRAG | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HKUDS/LightRAG |
| 2026-03-27 20:00 | firecrawl | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/firecrawl/firecrawl |
| 2026-03-27 20:00 | mem0 | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/mem0ai/mem0 |
| 2026-03-27 20:00 | assistant-context | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huynamboz/assistant-context |
| 2026-03-27 20:00 | awesome-claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/hesreallyhim/awesome-claude-code |
| 2026-03-27 20:00 | LobsterBoard | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/curbob/LobsterBoard |
| 2026-03-27 20:00 | awesome | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/sindresorhus/awesome |
| 2026-03-27 20:00 | public-apis | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/public-apis/public-apis |
| 2026-03-27 20:01 | vscode | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/microsoft/vscode |
| 2026-03-27 20:07 | ohmyzsh | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ohmyzsh/ohmyzsh |
| 2026-03-27 20:08 | n8n | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/n8n-io/n8n |
| 2026-03-27 20:08 | gitignore | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/github/gitignore |
| 2026-03-27 20:08 | ollama | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ollama/ollama |
| 2026-03-27 20:08 | transformers | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huggingface/transformers |
| 2026-03-27 20:08 | langflow | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/langflow-ai/langflow |
| 2026-03-27 20:08 | langchain | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/langchain-ai/langchain |
| 2026-03-27 20:09 | kubernetes | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/kubernetes/kubernetes |
| 2026-03-27 20:10 | generative-ai-for-beginners | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/microsoft/generative-ai-for-beginners |
| 2026-03-27 20:10 | awesome-llm-apps | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Shubhamsaboo/awesome-llm-apps |
| 2026-03-27 20:10 | llama.cpp | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ggml-org/llama.cpp |
| 2026-03-27 20:10 | whisper | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/openai/whisper |
| 2026-03-27 20:10 | spec-kit | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/github/spec-kit |
| 2026-03-27 20:10 | llm-course | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/mlabonne/llm-course |
| 2026-03-27 20:10 | gpt4all | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/nomic-ai/gpt4all |
| 2026-03-27 20:10 | ragflow | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/infiniflow/ragflow |
| 2026-03-27 20:11 | vllm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vllm-project/vllm |
| 2026-03-27 20:11 | codex | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/openai/codex |
| 2026-03-27 20:11 | gpt4free | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/xtekky/gpt4free |
| 2026-03-27 20:11 | agency-agents | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/msitarzewski/agency-agents |
| 2026-03-27 20:11 | private-gpt | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/zylon-ai/private-gpt |
| 2026-03-27 20:11 | autoresearch | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/karpathy/autoresearch |
| 2026-03-27 20:12 | anything-llm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Mintplex-Labs/anything-llm |
| 2026-03-27 20:12 | docling | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/docling-project/docling |
| 2026-03-27 20:12 | awesome-claude-skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ComposioHQ/awesome-claude-skills |
| 2026-03-27 20:12 | oh-my-openagent | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/code-yeongyu/oh-my-openagent |
| 2026-03-27 20:12 | helix | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/helix-editor/helix |
| 2026-03-27 20:12 | cli | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/cli/cli |
| 2026-03-27 20:12 | aider | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Aider-AI/aider |
| 2026-03-27 20:12 | TradingAgents | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/TauricResearch/TradingAgents |
| 2026-03-27 20:12 | awesome-openclaw-skills | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/VoltAgent/awesome-openclaw-skills |
| 2026-03-27 20:13 | litellm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/BerriAI/litellm |
| 2026-03-27 20:13 | learn-claude-code | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/shareAI-lab/learn-claude-code |
| 2026-03-27 20:13 | nanobot | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/HKUDS/nanobot |
| 2026-03-27 20:13 | claude-cookbooks | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/anthropics/claude-cookbooks |
| 2026-03-27 20:13 | vim-plug | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/junegunn/vim-plug |
| 2026-03-27 20:13 | zsh-autosuggestions | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/zsh-users/zsh-autosuggestions |
| 2026-03-27 20:14 | trivy | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/aquasecurity/trivy |
| 2026-03-27 20:14 | paperclip | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/paperclipai/paperclip |
| 2026-03-27 20:14 | agents | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/wshobson/agents |
| 2026-03-27 20:14 | pytorch-lightning | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Lightning-AI/pytorch-lightning |
| 2026-03-27 20:14 | openai-python | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/openai/openai-python |
| 2026-03-27 20:14 | AstrBot | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/AstrBotDevs/AstrBot |
| 2026-03-27 20:14 | langgraph | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/langchain-ai/langgraph |
| 2026-03-27 20:14 | authelia | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/authelia/authelia |
| 2026-03-27 20:14 | agents-course | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huggingface/agents-course |
| 2026-03-27 20:14 | awesome-copilot | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/github/awesome-copilot |
| 2026-03-27 20:14 | smolagents | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huggingface/smolagents |
| 2026-03-27 20:14 | RAG_Techniques | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/NirDiamant/RAG_Techniques |
| 2026-03-27 20:15 | awesome-generative-ai-guide | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/aishwaryanr/awesome-generative-ai-guide |
| 2026-03-27 20:15 | gitleaks | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/gitleaks/gitleaks |
| 2026-03-27 20:15 | trufflehog | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/trufflesecurity/trufflehog |
| 2026-03-27 20:15 | agent-browser | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/vercel-labs/agent-browser |
| 2026-03-27 20:15 | mlx | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ml-explore/mlx |
| 2026-03-27 20:15 | claude-code-templates | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/davila7/claude-code-templates |
| 2026-03-27 20:15 | Scrapegraph-ai | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/ScrapeGraphAI/Scrapegraph-ai |
| 2026-03-27 20:15 | flash-attention | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Dao-AILab/flash-attention |
| 2026-03-27 20:15 | cli | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/googleworkspace/cli |
| 2026-03-27 20:15 | zsh-syntax-highlighting | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/zsh-users/zsh-syntax-highlighting |
| 2026-03-27 20:15 | claude-code-best-practice | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/shanraisshan/claude-code-best-practice |
| 2026-03-27 20:16 | serve | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/jina-ai/serve |
| 2026-03-27 20:16 | swarm | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/openai/swarm |
| 2026-03-27 20:16 | skyvern | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/Skyvern-AI/skyvern |
| 2026-03-27 20:16 | fastfetch | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/fastfetch-cli/fastfetch |
| 2026-03-27 20:16 | peft | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/huggingface/peft |
| 2026-03-27 20:16 | GenAI_Agents | INGESTED | Full pipeline via active_repos_pipeline.py | https://github.com/NirDiamant/GenAI_Agents |
| 2026-03-27 22:01 | Claude-Usage-Checker.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/0xAstroAlpha/Claude-Usage-Checker.git |
| 2026-03-27 22:01 | agentops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AgentOps-AI/agentops |
| 2026-03-27 22:01 | claude-seo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AgriciDaniel/claude-seo |
| 2026-03-27 22:01 | llmfit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlexsJones/llmfit |
| 2026-03-27 22:01 | BSA_Browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlexxEG/BSA_Browser |
| 2026-03-27 22:08 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeyVincent-ai/agent-skills |
| 2026-03-27 22:09 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Joannis/claude-skills |
| 2026-03-27 22:10 | Gemini-ChatBot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Gemini-ChatBot |
| 2026-03-27 22:10 | Getting-Started-with-Gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Getting-Started-with-Gemini |
| 2026-03-27 22:17 | pragmastat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AndreyAkinshin/pragmastat |
| 2026-03-27 22:17 | Auto-Claude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AndyMik90/Auto-Claude |
| 2026-03-27 22:17 | phoenix | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Arize-ai/phoenix |
| 2026-03-27 22:17 | kore-memory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Auriti-Labs/kore-memory |
| 2026-03-27 22:17 | SwiftUI-Agent-Skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AvdLee/SwiftUI-Agent-Skill |
| 2026-03-27 22:17 | VibeSec-Skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BehiSecc/VibeSec-Skill |
| 2026-03-27 22:17 | ClawRouter | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BlockRunAI/ClawRouter |
| 2026-03-27 22:17 | ai-marketing-claude-code-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BrianRWagner/ai-marketing-claude-code-skills |
| 2026-03-27 22:17 | ai-marketing-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BrianRWagner/ai-marketing-skills |
| 2026-03-27 22:17 | chainlit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Chainlit/chainlit |
| 2026-03-27 22:17 | chrome-devtools-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| 2026-03-27 22:17 | agent-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ClickHouse/agent-skills |
| 2026-03-27 22:17 | claude-workflow-v2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/claude-workflow-v2 |
| 2026-03-27 22:17 | claude-workflow-v2.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/claude-workflow-v2.git |
| 2026-03-27 22:17 | threejs-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/threejs-skills |
| 2026-03-27 22:17 | agent-orchestrator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/agent-orchestrator |
| 2026-03-27 22:17 | open-claude-cowork | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/open-claude-cowork |
| 2026-03-27 22:17 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/skills |
| 2026-03-27 22:17 | notebooklm_source_automation | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DataNath/notebooklm_source_automation |
| 2026-03-27 22:17 | charlie-cfo-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/EveryInc/charlie-cfo-skill |
| 2026-03-27 22:17 | QueryWeaver | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FalkorDB/QueryWeaver |
| 2026-03-27 22:17 | QueryWeaver.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FalkorDB/QueryWeaver.git |
| 2026-03-27 22:17 | all-agentic-architectures | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FareedKhan-dev/all-agentic-architectures |
| 2026-03-27 22:17 | claude-code-ultimate-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FlorianBruniaux/claude-code-ultimate-guide |
| 2026-03-27 22:17 | agent-skill-creator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FrancyJGLisboa/agent-skill-creator |
| 2026-03-27 22:17 | agent-teams-lite | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Gentleman-Programming/agent-teams-lite |
| 2026-03-27 22:17 | giskard | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Giskard-AI/giskard |
| 2026-03-27 22:17 | giskard-oss | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Giskard-AI/giskard-oss |
| 2026-03-27 22:17 | Local-NotebookLM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Goekdeniz-Guelmez/Local-NotebookLM |
| 2026-03-27 22:17 | generative-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/GoogleCloudPlatform/generative-ai |
| 2026-03-27 22:17 | .github | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/.github |
| 2026-03-27 22:17 | ClawTeam | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/ClawTeam |
| 2026-03-27 22:17 | ClawWork.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/ClawWork.git |
| 2026-03-27 22:17 | FastCode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/FastCode |
| 2026-03-27 22:17 | nanobot.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/nanobot.git |
| 2026-03-27 22:17 | materials-simulation-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeshamFS/materials-simulation-skills |
| 2026-03-27 22:17 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeyVincent-ai/agent-skills.git |
| 2026-03-27 22:17 | claude_skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Jamie-BitFlight/claude_skills |
| 2026-03-27 22:17 | claude-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Jeffallan/claude-skills |
| 2026-03-27 22:17 | baoyu-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JimLiu/baoyu-skills |
| 2026-03-27 22:17 | clawport-ui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JohnRiceML/clawport-ui |
| 2026-03-27 22:17 | claude-scientific-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/K-Dense-AI/claude-scientific-skills |
| 2026-03-27 22:17 | Gemini-ChatBot | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanM45/Gemini-ChatBot |
| 2026-03-27 22:17 | Getting-Started-with-Gemini | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanM45/Getting-Started-with-Gemini |
| 2026-03-27 22:17 | kilocode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Kilo-Org/kilocode |
| 2026-03-27 22:17 | taste-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Leonxlnx/taste-skill |
| 2026-03-27 22:17 | maxclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lichas/maxclaw |
| 2026-03-27 22:17 | Mini-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/Mini-Agent |
| 2026-03-27 22:17 | MiniMax-AI.github.io | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/MiniMax-AI/MiniMax-AI.github.io |
| 2026-03-27 22:17 | MiniMax-M1 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-M1 |
| 2026-03-27 22:17 | MiniMax-M2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-M2 |
| 2026-03-27 22:17 | MiniMax-MCP | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-MCP |
| 2026-03-27 22:17 | lightllm | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ModelTC/lightllm |
| 2026-03-27 22:17 | auto-accept-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Munkhin/auto-accept-agent |
| 2026-03-27 22:17 | Guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA-NeMo/Guardrails |
| 2026-03-27 22:17 | NeMo-Guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/NeMo-Guardrails |
| 2026-03-27 22:18 | NemoClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/NemoClaw |
| 2026-03-27 22:18 | OpenShell | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/OpenShell |
| 2026-03-27 22:27 | TensorRT-LLM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/TensorRT-LLM |
| 2026-03-27 22:27 | garak | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/garak |
| 2026-03-27 22:27 | nvidia-docker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/nvidia-docker |
| 2026-03-27 22:27 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/NoizAI/skills |
| 2026-03-27 22:28 | claude-win11-speckit-update-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NotMyself/claude-win11-speckit-update-skill |
| 2026-03-27 22:28 | hermes-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NousResearch/hermes-agent |
| 2026-03-27 22:28 | tulip | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenAttackDefenseTools/tulip |
| 2026-03-27 22:28 | ai-sdk-provider | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenRouterTeam/ai-sdk-provider |
| 2026-03-27 22:28 | AI-Research-SKILLs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Orchestra-Research/AI-Research-SKILLs |
| 2026-03-27 22:28 | AI-research-SKILLs | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Orchestra-Research/AI-research-SKILLs |
| 2026-03-27 22:28 | nutrient-agent-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PSPDFKit-labs/nutrient-agent-skill |
| 2026-03-27 22:28 | ResumeSkills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Paramchoudhary/ResumeSkills |
| 2026-03-27 22:28 | claude-code-system-prompts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Piebald-AI/claude-code-system-prompts |
| 2026-03-27 22:32 | posthog | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PostHog/posthog |
| 2026-03-27 22:32 | Qwen | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen |
| 2026-03-27 22:32 | Qwen-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen-Agent |
| 2026-03-27 22:32 | Qwen-Agent.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen-Agent.git |
| 2026-03-27 22:32 | Qwen2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen2 |
| 2026-03-27 22:32 | Qwen2.5-Omni | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen2.5-Omni |
| 2026-03-27 22:32 | Qwen3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3 |
| 2026-03-27 22:32 | Qwen3-ASR | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-ASR |
| 2026-03-27 22:32 | Qwen3-ASR.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-ASR.git |
| 2026-03-27 22:33 | Qwen3-TTS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-TTS |
| 2026-03-27 22:33 | Qwen3-TTS.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-TTS.git |
| 2026-03-27 22:33 | qwen-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/qwen-code |
| 2026-03-27 22:33 | FlashRAG | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RUC-NLPIR/FlashRAG |
| 2026-03-27 22:33 | opc-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ReScienceLab/opc-skills |
| 2026-03-27 22:33 | Rootly-MCP-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rootly-AI-Labs/Rootly-MCP-server |
| 2026-03-27 22:33 | rootly-mcp-server | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Rootly-AI-Labs/rootly-mcp-server |
| 2026-03-27 22:33 | tutor-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RoundTable02/tutor-skills |
| 2026-03-27 22:33 | metube-browser-extension | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rpsl/metube-browser-extension |
| 2026-03-27 22:33 | dev-browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SawyerHood/dev-browser |
| 2026-03-27 22:33 | dev-browser.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SawyerHood/dev-browser.git |
| 2026-03-27 22:34 | claude-speed-reader | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SeanZoR/claude-speed-reader |
| 2026-03-27 22:34 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Shpigford/skills |
| 2026-03-27 22:34 | guardrails | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ShreyaR/guardrails |
| 2026-03-27 22:34 | pyragify | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ThomasBury/pyragify |
| 2026-03-27 22:34 | tinyclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TinyAGI/tinyclaw |
| 2026-03-27 22:34 | SuperAGI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TransformerOptimus/SuperAGI |
| 2026-03-27 22:34 | agency-swarm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VRSEN/agency-swarm |
| 2026-03-27 22:34 | ClawX | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ValueCell-ai/ClawX |
| 2026-03-27 22:34 | awesome-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/awesome-agent-skills |
| 2026-03-27 22:34 | awesome-ai-agent-papers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/awesome-ai-agent-papers |
| 2026-03-27 22:34 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/VoltAgent/skills |
| 2026-03-27 22:35 | voltagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/voltagent |
| 2026-03-27 22:35 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/WordPress/agent-skills |
| 2026-03-27 22:35 | agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/WordPress/agent-skills.git |
| 2026-03-27 22:35 | x-twitter-scraper | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Xquik-dev/x-twitter-scraper |
| 2026-03-27 22:35 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ZackKorman/skills |
| 2026-03-27 22:35 | Antigravity-Skills-Chronicle | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Zaious/Antigravity-Skills-Chronicle |
| 2026-03-27 22:35 | makepad-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ZhangHanDong/makepad-skills |
| 2026-03-27 22:35 | web-quality-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/addyosmani/web-quality-skills |
| 2026-03-27 22:35 | web-quality-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/addyosmani/web-quality-skills.git |
| 2026-03-27 22:35 | manim_skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adithya-s-k/manim_skill |
| 2026-03-27 22:35 | manim_skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adithya-s-k/manim_skill.git |
| 2026-03-27 22:35 | everything-claude-code.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/affaan-m/everything-claude-code.git |
| 2026-03-27 22:35 | agentscope | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agentscope-ai/agentscope |
| 2026-03-27 22:36 | agentskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agentskills/agentskills |
| 2026-03-27 22:37 | AutoResearchClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aiming-lab/AutoResearchClaw |
| 2026-03-27 22:38 | MetaClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aiming-lab/MetaClaw |
| 2026-03-27 22:38 | claude-bootstrap | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/alinaqi/claude-bootstrap |
| 2026-03-27 22:38 | clearml | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/allegroai/clearml |
| 2026-03-27 22:38 | angular-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/analogjs/angular-skills |
| 2026-03-27 22:38 | angular-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/analogjs/angular-skills.git |
| 2026-03-27 22:39 | opencode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anomalyco/opencode |
| 2026-03-29 20:14 | affitor-affiliate-skills | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | antigravity-deck-tysonnbt | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | antigravity-kit | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | autoresearchclaw | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | awesome-openclaw-agents | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | cerberus-hackunderway | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | claude-octopus | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | claude-scientific-skills | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | deepagents-langchain | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | fbi-watchdog | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | MaxKB | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | okara-crypto | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:14 | openrag | REJECTED | WARN: Repo không có README và không có source code rõ ràng |
| 2026-03-29 20:16 | authentik | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/goauthentik/authentik |
| 2026-03-29 20:16 | lazy.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/folke/lazy.nvim |
| 2026-03-29 20:16 | pgvector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pgvector/pgvector |
| 2026-03-29 20:16 | telescope.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nvim-telescope/telescope.nvim |
| 2026-03-29 20:16 | docs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/docs |
| 2026-03-29 20:16 | evals | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/evals |
| 2026-03-29 20:16 | trl | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/trl |
| 2026-03-29 20:16 | tiktoken | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/tiktoken |
| 2026-03-29 20:16 | web-llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlc-ai/web-llm |
| 2026-03-29 20:16 | free-llm-api-resources | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cheahjs/free-llm-api-resources |
| 2026-03-29 20:16 | gitmoji | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/carloscuesta/gitmoji |
| 2026-03-29 20:16 | superagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forwardemail/superagent |
| 2026-03-29 20:16 | camel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/camel |
| 2026-03-29 20:16 | pydantic-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pydantic/pydantic-ai |
| 2026-03-29 20:16 | openfang | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RightNow-AI/openfang |
| 2026-03-29 20:16 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/skills |
| 2026-03-29 20:16 | llmware | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/llmware-ai/llmware |
| 2026-03-29 20:16 | claude-plugins-official | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-plugins-official |
| 2026-03-29 20:16 | Agent-Skills-for-Context-Engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering |
| 2026-03-29 20:16 | deepeval | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/confident-ai/deepeval |
| 2026-03-29 20:16 | gitingest | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coderamp-labs/gitingest |
| 2026-03-29 20:16 | oauth2-proxy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/oauth2-proxy/oauth2-proxy |
| 2026-03-29 20:16 | cron | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/robfig/cron |
| 2026-03-29 20:16 | outlines | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dottxt-ai/outlines |
| 2026-03-29 20:16 | litgpt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/litgpt |
| 2026-03-29 20:16 | ragas | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vibrantlabsai/ragas |
| 2026-03-29 20:16 | rust-clippy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rust-lang/rust-clippy |
| 2026-03-29 20:16 | ludwig | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ludwig-ai/ludwig |
| 2026-03-29 20:16 | axolotl | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/axolotl-ai-cloud/axolotl |
| 2026-03-29 20:16 | llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonw/llm |
| 2026-03-29 20:16 | charts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bitnami/charts |
| 2026-03-29 20:16 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/skills |
| 2026-03-29 20:16 | usql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/xo/usql |
| 2026-03-29 20:16 | opencode-antigravity-auth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NoeFabris/opencode-antigravity-auth |
| 2026-03-29 20:16 | accelerate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/accelerate |
| 2026-03-29 20:16 | nvim-cmp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hrsh7th/nvim-cmp |
| 2026-03-29 20:16 | huobao-drama | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/chatfire-AI/huobao-drama |
| 2026-03-29 20:16 | go-sqlite3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mattn/go-sqlite3 |
| 2026-03-29 20:16 | roadmap | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/roadmap |
| 2026-03-29 20:16 | mlx-examples | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ml-explore/mlx-examples |
| 2026-03-29 20:16 | packer.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wbthomason/packer.nvim |
| 2026-03-29 20:16 | concurrently | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-cli-tools/concurrently |
| 2026-03-29 20:16 | notebooklm-py | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/teng-lin/notebooklm-py |
| 2026-03-29 20:16 | kimi-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MoonshotAI/kimi-cli |
| 2026-03-29 20:16 | alasql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlaSQL/alasql |
| 2026-03-29 20:16 | better-sqlite3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/WiseLibs/better-sqlite3 |
| 2026-03-29 20:16 | nvim-dap | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mfussenegger/nvim-dap |
| 2026-03-29 20:16 | claude-code-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code-action |
| 2026-03-29 20:16 | guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/guardrails-ai/guardrails |
| 2026-03-29 20:16 | hindsight | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vectorize-io/hindsight |
| 2026-03-29 20:16 | claude-context | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zilliztech/claude-context |
| 2026-03-29 20:16 | Cronicle | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/Cronicle |
| 2026-03-29 20:16 | pixel-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pablodelucca/pixel-agents |
| 2026-03-29 20:16 | vale | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vale-cli/vale |
| 2026-03-29 20:16 | octosql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cube2222/octosql |
| 2026-03-29 20:16 | learn-ai-engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ashishps1/learn-ai-engineering |
| 2026-03-29 20:16 | build-push-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/build-push-action |
| 2026-03-29 20:16 | notebooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/unslothai/notebooks |
| 2026-03-29 20:16 | Kode-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode-Agent |
| 2026-03-29 20:16 | AI-Project-Gallery | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/AI-Project-Gallery |
| 2026-03-29 20:16 | Auto-claude-code-research-in-sleep | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep |
| 2026-03-29 20:16 | mlx-lm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ml-explore/mlx-lm |
| 2026-03-29 20:16 | agent-os | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/buildermethods/agent-os |
| 2026-03-29 20:16 | oasis | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/oasis |
| 2026-03-29 20:16 | LitServe | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/LitServe |
| 2026-03-29 20:16 | n8n-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/czlonkowski/n8n-skills |
| 2026-03-29 20:16 | fast-graphrag | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/circlemind-ai/fast-graphrag |
| 2026-03-29 20:16 | pocket-tts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kyutai-labs/pocket-tts |
| 2026-03-29 20:16 | code-review-graph | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tirth8205/code-review-graph |
| 2026-03-29 20:16 | google-maps-scraper | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gosom/google-maps-scraper |
| 2026-03-29 20:16 | huggingface_hub | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/huggingface_hub |
| 2026-03-29 20:16 | nvim-dap-ui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rcarriga/nvim-dap-ui |
| 2026-03-29 20:16 | clickhouse-go | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ClickHouse/clickhouse-go |
| 2026-03-29 20:16 | autoclip | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zhouxiaoka/autoclip |
| 2026-03-29 20:16 | ai-engineering-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sumanth077/ai-engineering-toolkit |
| 2026-03-29 20:16 | awesome-notebooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jupyter-naas/awesome-notebooks |
| 2026-03-29 20:16 | pgvectorscale | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/timescale/pgvectorscale |
| 2026-03-29 20:16 | LLM-Finetuning | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ashishpatel26/LLM-Finetuning |
| 2026-03-29 20:16 | agency-agents-zh | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jnMetaCode/agency-agents-zh |
| 2026-03-29 20:16 | griptape | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/griptape-ai/griptape |
| 2026-03-29 20:16 | gemini-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-gemini/gemini-skills |
| 2026-03-29 20:16 | lighteval | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/lighteval |
| 2026-03-29 20:16 | uptrain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/uptrain-ai/uptrain |
| 2026-03-29 20:16 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vuejs-ai/skills |
| 2026-03-29 20:16 | agent-scan | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/snyk/agent-scan |
| 2026-03-29 20:16 | awesome-openclaw-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mergisi/awesome-openclaw-agents |
| 2026-03-29 20:16 | opencode-openai-codex-auth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/numman-ali/opencode-openai-codex-auth |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/apify/agent-skills |
| 2026-03-29 20:16 | claude-subconscious | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/letta-ai/claude-subconscious |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/supabase/agent-skills |
| 2026-03-29 20:16 | docker-otel-lgtm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/docker-otel-lgtm |
| 2026-03-29 20:16 | awesome-notebookLM-prompts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/serenakeyitan/awesome-notebookLM-prompts |
| 2026-03-29 20:16 | gitagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-gitagent/gitagent |
| 2026-03-29 20:16 | chart-testing | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/helm/chart-testing |
| 2026-03-29 20:16 | Youtube-clipper-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/op7418/Youtube-clipper-skill |
| 2026-03-29 20:16 | advanced-context-engineering-for-coding-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents |
| 2026-03-29 20:16 | agent-sandbox | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kubernetes-sigs/agent-sandbox |
| 2026-03-29 20:16 | n8n-hosting | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/n8n-io/n8n-hosting |
| 2026-03-29 20:16 | n8n-docs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/n8n-io/n8n-docs |
| 2026-03-29 20:16 | claw0 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/claw0 |
| 2026-03-29 20:16 | cmp-nvim-lsp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hrsh7th/cmp-nvim-lsp |
| 2026-03-29 20:16 | login-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/login-action |
| 2026-03-29 20:16 | claude-code-settings | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/feiskyer/claude-code-settings |
| 2026-03-29 20:16 | setup-buildx-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/setup-buildx-action |
| 2026-03-29 20:16 | agentql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinyfish-io/agentql |
| 2026-03-29 20:16 | agent-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/softaworks/agent-toolkit |
| 2026-03-29 20:16 | poco-claw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/poco-ai/poco-claw |
| 2026-03-29 20:16 | claude-code-transcripts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonw/claude-code-transcripts |
| 2026-03-29 20:16 | metadata-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/metadata-action |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/callstackincubator/agent-skills |
| 2026-03-29 20:16 | ai-hands-on | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Ramakm/ai-hands-on |
| 2026-03-29 20:16 | nvim-dap-virtual-text | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/theHamsta/nvim-dap-virtual-text |
| 2026-03-29 20:16 | aws-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/itsmostafa/aws-agent-skills |
| 2026-03-29 20:16 | markdownlint-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/igorshubovych/markdownlint-cli |
| 2026-03-29 20:16 | ai-devkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codeaholicguy/ai-devkit |
| 2026-03-29 20:16 | gentle-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Gentleman-Programming/gentle-ai |
| 2026-03-29 20:16 | ddd-leaven-v2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BottegaIT/ddd-leaven-v2 |
| 2026-03-29 20:16 | clawsec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/prompt-security/clawsec |
| 2026-03-29 20:16 | markdownlint-cli2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DavidAnson/markdownlint-cli2 |
| 2026-03-29 20:16 | react-timeline-editor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/xzdarcy/react-timeline-editor |
| 2026-03-29 20:16 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jezweb/claude-skills |
| 2026-03-29 20:16 | k8s-monitoring-helm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/k8s-monitoring-helm |
| 2026-03-29 20:16 | app-store-connect-cli-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rudrankriyam/app-store-connect-cli-skills |
| 2026-03-29 20:16 | agentsview | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wesm/agentsview |
| 2026-03-29 20:16 | chatgpt-prompt-splitter | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jupediaz/chatgpt-prompt-splitter |
| 2026-03-29 20:16 | setup-qemu-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/setup-qemu-action |
| 2026-03-29 20:16 | Ticket-Bot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sayrix/Ticket-Bot |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hashicorp/agent-skills |
| 2026-03-29 20:16 | vscode-antlr4 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mike-lischke/vscode-antlr4 |
| 2026-03-29 20:16 | webgpu-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dgreenheck/webgpu-claude-skill |
| 2026-03-29 20:16 | go-diff | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sourcegraph/go-diff |
| 2026-03-29 20:16 | poutine | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boostsecurityio/poutine |
| 2026-03-29 20:16 | cargotracker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/eclipse-ee4j/cargotracker |
| 2026-03-29 20:16 | sympozium | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sympozium-ai/sympozium |
| 2026-03-29 20:16 | llm-mux | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nghyane/llm-mux |
| 2026-03-29 20:16 | claude-skill-homeassistant | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/komal-SkyNET/claude-skill-homeassistant |
| 2026-03-29 20:16 | dbt-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dbt-labs/dbt-agent-skills |
| 2026-03-29 20:16 | PentestOPS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/0xBugatti/PentestOPS |
| 2026-03-29 20:16 | agent-config | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/agent-config |
| 2026-03-29 20:16 | agenttrafficcontrol | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gkamradt/agenttrafficcontrol |
| 2026-03-29 20:16 | distil-text2sql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/distil-labs/distil-text2sql |
| 2026-03-29 20:16 | kode-agent-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/kode-agent-sdk |
| 2026-03-29 20:16 | codex-cli-best-practice | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/codex-cli-best-practice |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/intellectronica/agent-skills |
| 2026-03-29 20:16 | shareAI-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/shareAI-skills |
| 2026-03-29 20:16 | chat-quality-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tanviet12/chat-quality-agent |
| 2026-03-29 20:16 | agent-teams | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dsclca12/agent-teams |
| 2026-03-29 20:16 | gitingest-extension | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coderamp-labs/gitingest-extension |
| 2026-03-29 20:16 | pydoclint | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jsh9/pydoclint |
| 2026-03-29 20:16 | claude-code-hooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-hooks |
| 2026-03-29 20:16 | ai-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sanjay3290/ai-skills |
| 2026-03-29 20:16 | kpi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kobotoolbox/kpi |
| 2026-03-29 20:16 | notebooklm-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jacob-bd/notebooklm-cli |
| 2026-03-29 20:16 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/better-auth/skills |
| 2026-03-29 20:16 | open-claude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tkattkat/open-claude |
| 2026-03-29 20:16 | neural-memory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nhadaututtheky/neural-memory |
| 2026-03-29 20:16 | ffuf_claude_skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jthack/ffuf_claude_skill |
| 2026-03-29 20:16 | claude-code-production-grade-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-production-grade-plugin |
| 2026-03-29 20:16 | shellcheck-precommit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/koalaman/shellcheck-precommit |
| 2026-03-29 20:16 | codacy-analysis-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codacy/codacy-analysis-cli |
| 2026-03-29 20:16 | agent-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sanity-io/agent-toolkit |
| 2026-03-29 20:16 | claude-inspector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kangraemin/claude-inspector |
| 2026-03-29 20:16 | eventsourcing-java-example | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Pragmatists/eventsourcing-java-example |
| 2026-03-29 20:16 | lang-sql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codemirror/lang-sql |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gokapso/agent-skills |
| 2026-03-29 20:16 | DocGenius-Revolutionizing-PDFs-with-AI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/DocGenius-Revolutionizing-PDFs-with-AI |
| 2026-03-29 20:16 | setup-n8n | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ndoanh266/setup-n8n |
| 2026-03-29 20:16 | diginext | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/digitopvn/diginext |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boristane/agent-skills |
| 2026-03-29 20:16 | linear-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wrsmith108/linear-claude-skill |
| 2026-03-29 20:16 | codacy-analysis-cli-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codacy/codacy-analysis-cli-action |
| 2026-03-29 20:16 | pypict-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/omkamal/pypict-claude-skill |
| 2026-03-29 20:16 | End-to-End-Airbnb-Price-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/End-to-End-Airbnb-Price-Prediction |
| 2026-03-29 20:16 | claude-code-ultimate-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/marketingjuliancongdanh79-pixel/claude-code-ultimate-guide |
| 2026-03-29 20:16 | n8n-atom-fork | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/khanh-atom/n8n-atom-fork |
| 2026-03-29 20:16 | dev-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fvadicamo/dev-agent-skills |
| 2026-03-29 20:16 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wendylabsinc/claude-skills |
| 2026-03-29 20:16 | github-clone-count-badge | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MShawon/github-clone-count-badge |
| 2026-03-29 20:16 | task-runner-launcher | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/n8n-io/task-runner-launcher |
| 2026-03-29 20:16 | pg0 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vectorize-io/pg0 |
| 2026-03-29 20:16 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fal-ai-community/skills |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neondatabase/agent-skills |
| 2026-03-29 20:16 | claude-code-status-line | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-status-line |
| 2026-03-29 20:16 | spawn-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/khanhbkqt/spawn-agent |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/typefully/agent-skills |
| 2026-03-29 20:16 | pixl-chart | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-chart |
| 2026-03-29 20:16 | RGSS-Decryptor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/usagirei/RGSS-Decryptor |
| 2026-03-29 20:16 | windows-gmsa | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kubernetes-sigs/windows-gmsa |
| 2026-03-29 20:16 | ai-coding-tools | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/andyfischer/ai-coding-tools |
| 2026-03-29 20:16 | sdvn_apix_python | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/StableDiffusionVN/sdvn_apix_python |
| 2026-03-29 20:16 | grafana-github-actions | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/grafana-github-actions |
| 2026-03-29 20:16 | notebooklm-podcast-automator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upamune/notebooklm-podcast-automator |
| 2026-03-29 20:16 | custom-plugin-java | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pluginagentmarketplace/custom-plugin-java |
| 2026-03-29 20:16 | VMware-AIops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zw008/VMware-AIops |
| 2026-03-29 20:16 | codymaster | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tody-agent/codymaster |
| 2026-03-29 20:16 | shared-workflows | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/shared-workflows |
| 2026-03-29 20:16 | claude-code-startup-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rameerez/claude-code-startup-skills |
| 2026-03-29 20:16 | awesome-claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jmanhype/awesome-claude-code |
| 2026-03-29 20:16 | novel-llm-26 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/novel-llm-26 |
| 2026-03-29 20:16 | claude-ecom | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/takechanman1228/claude-ecom |
| 2026-03-29 20:16 | hindsight-cookbook | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vectorize-io/hindsight-cookbook |
| 2026-03-29 20:16 | varlock-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wrsmith108/varlock-claude-skill |
| 2026-03-29 20:16 | tinybird-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinybirdco/tinybird-agent-skills |
| 2026-03-29 20:16 | Virat-Kohli-Score-Analytics | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Virat-Kohli-Score-Analytics |
| 2026-03-29 20:16 | pixl-server-storage | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-storage |
| 2026-03-29 20:16 | Chatbot-Using-Langchain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Chatbot-Using-Langchain |
| 2026-03-29 20:16 | context-and-tools | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/netlify/context-and-tools |
| 2026-03-29 20:16 | charts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/paradedb/charts |
| 2026-03-29 20:16 | claude-code-codex-cursor-gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-codex-cursor-gemini |
| 2026-03-29 20:16 | cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/atxp-dev/cli |
| 2026-03-29 20:16 | awesome-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/phuryn/awesome-agent-skills |
| 2026-03-29 20:16 | claude-openclaw-bridge | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ericblue/claude-openclaw-bridge |
| 2026-03-29 20:16 | Conversational-Chatbot-using-Langchain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Conversational-Chatbot-using-Langchain |
| 2026-03-29 20:16 | claude-memory-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hanfang/claude-memory-skill |
| 2026-03-29 20:16 | llm-lean-log | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/loclv/llm-lean-log |
| 2026-03-29 20:16 | BlogBoard-AI-Blog-Generator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/BlogBoard-AI-Blog-Generator |
| 2026-03-29 20:16 | claude-apple-bridges | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/more-io/claude-apple-bridges |
| 2026-03-29 20:16 | agentune | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tqdat410/agentune |
| 2026-03-29 20:16 | claude-code-skill-maker-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-skill-maker-plugin |
| 2026-03-29 20:16 | claude-code-software-engineer-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-software-engineer-plugin |
| 2026-03-29 20:16 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonwong/agent-skills |
| 2026-03-29 20:16 | xyops-shell-image | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyops-shell-image |
| 2026-03-29 20:17 | Claude-Usage-Checker | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/0xAstroAlpha/Claude-Usage-Checker |
| 2026-03-29 20:18 | agent-skills-standard | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HoangNguyen0403/agent-skills-standard |
| 2026-03-29 20:18 | MiniMax-MCP-JS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-MCP-JS |
| 2026-03-29 20:18 | notebooklm-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PleasePrompto/notebooklm-mcp |
| 2026-03-29 20:18 | notebooklm-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PleasePrompto/notebooklm-skill |
| 2026-03-29 20:18 | zeroleaks | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ZeroLeaks/zeroleaks |
| 2026-03-29 20:18 | everything-claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/affaan-m/everything-claude-code |
| 2026-03-29 20:18 | claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code |
| 2026-03-29 20:18 | claudekit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/carlrannaberg/claudekit |
| 2026-03-29 20:18 | langextract | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google/langextract |
| 2026-03-29 20:18 | notebooklm-mcp-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jacob-bd/notebooklm-mcp-cli |
| 2026-03-29 20:18 | port-killer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/productdevbook/port-killer |
| 2026-03-29 20:19 | claude-mem | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thedotmack/claude-mem |
| 2026-03-29 20:19 | context7 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/upstash/context7 |
| 2026-03-29 20:19 | AntigravityManager | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Draculabo/AntigravityManager |
| 2026-03-29 20:19 | OpenSpec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Fission-AI/OpenSpec |
| 2026-03-29 20:19 | ClawWork | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/HKUDS/ClawWork |
| 2026-03-29 20:19 | BMAD-METHOD | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bmad-code-org/BMAD-METHOD |
| 2026-03-29 20:19 | open-notebooklm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gabrielchua/open-notebooklm |
| 2026-03-29 20:19 | open-notebook | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lfnovo/open-notebook |
| 2026-03-29 20:19 | antigravity-kit | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vudovn/antigravity-kit |
| 2026-03-29 20:19 | LightRAG | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/LightRAG |
| 2026-03-29 20:19 | firecrawl | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/firecrawl/firecrawl |
| 2026-03-29 20:20 | mem0 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mem0ai/mem0 |
| 2026-03-29 20:20 | assistant-context | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huynamboz/assistant-context |
| 2026-03-29 20:20 | awesome-claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hesreallyhim/awesome-claude-code |
| 2026-03-29 20:20 | LobsterBoard | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/curbob/LobsterBoard |
| 2026-03-29 20:20 | awesome | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/awesome |
| 2026-03-29 20:20 | public-apis | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/public-apis/public-apis |
| 2026-03-29 20:20 | ohmyzsh | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ohmyzsh/ohmyzsh |
| 2026-03-29 20:21 | gitignore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/gitignore |
| 2026-03-29 20:21 | ollama | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ollama/ollama |
| 2026-03-29 20:22 | transformers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/transformers |
| 2026-03-29 20:23 | markdownlint-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/igorshubovych/markdownlint-cli |
| 2026-03-29 20:23 | GitNexus | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/abhigyanpatwari/GitNexus |
| 2026-03-29 20:23 | rest-api | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agilecrm/rest-api |
| 2026-03-29 20:23 | langflow | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/langflow-ai/langflow |
| 2026-03-29 20:23 | async-profiler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/async-profiler |
| 2026-03-29 20:23 | objstore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thanos-io/objstore |
| 2026-03-29 20:23 | quivr | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QuivrHQ/quivr |
| 2026-03-29 20:23 | excalidraw-mcp-app | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/antonpk1/excalidraw-mcp-app |
| 2026-03-29 20:23 | docutranslate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/xunbu/docutranslate |
| 2026-03-29 20:24 | homebrew-bundle | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Homebrew/homebrew-bundle |
| 2026-03-29 20:24 | cli.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/atxp-dev/cli.git |
| 2026-03-29 20:24 | xpfarm | REJECTED | Bad pattern: xpfarm | https://github.com/A3-N/xpfarm |
| 2026-03-29 20:24 | xpfarm | REJECTED | BLOCKED: pattern 'xpfarm' trong tên repo | https://github.com/A3-N/xpfarm |
| 2026-03-29 20:24 | langchain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/langchain-ai/langchain |
| 2026-03-29 20:24 | kubernetes | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/kubernetes/kubernetes |
| 2026-03-29 20:24 | langroid | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/langroid/langroid |
| 2026-03-29 20:24 | hotkeys | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TanStack/hotkeys |
| 2026-03-29 20:24 | tree-sitter-rust | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tree-sitter/tree-sitter-rust |
| 2026-03-29 20:24 | lobsters | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lobsters/lobsters |
| 2026-03-29 20:25 | upx | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upx/upx |
| 2026-03-29 20:25 | generative-ai-for-beginners | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/generative-ai-for-beginners |
| 2026-03-29 20:26 | vllm.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vllm-project/vllm.git |
| 2026-03-29 20:26 | qsv-sniffer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jqnatividad/qsv-sniffer |
| 2026-03-29 20:26 | awesome-llm-apps | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Shubhamsaboo/awesome-llm-apps |
| 2026-03-29 20:26 | chat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel/chat |
| 2026-03-29 20:26 | zsh-autosuggestions.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zsh-users/zsh-autosuggestions.git |
| 2026-03-29 20:26 | build-push-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/build-push-action |
| 2026-03-29 20:26 | golangci-lint | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/golangci/golangci-lint |
| 2026-03-29 20:26 | llama.cpp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ggml-org/llama.cpp |
| 2026-03-29 20:26 | whisper | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/whisper |
| 2026-03-29 20:26 | sympozium | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlexsJones/sympozium |
| 2026-03-29 20:26 | spec-kit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/spec-kit |
| 2026-03-29 20:27 | llm-course | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlabonne/llm-course |
| 2026-03-29 20:27 | gpt4all | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nomic-ai/gpt4all |
| 2026-03-29 20:27 | ragflow | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/infiniflow/ragflow |
| 2026-03-29 20:27 | plotly.js | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/plotly/plotly.js |
| 2026-03-29 20:28 | gemini-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-gemini/gemini-cli |
| 2026-03-29 20:28 | xxhash-rust | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DoumanAsh/xxhash-rust |
| 2026-03-29 20:28 | vllm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vllm-project/vllm |
| 2026-03-29 20:29 | pyroscope | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/pyroscope |
| 2026-03-29 20:29 | gitingest-extension | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lcandy2/gitingest-extension |
| 2026-03-29 20:29 | Hello-World.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/octocat/Hello-World.git |
| 2026-03-29 20:29 | gddo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/golang/gddo |
| 2026-03-29 20:29 | codex | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/codex |
| 2026-03-29 20:29 | gpt4free | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/xtekky/gpt4free |
| 2026-03-29 20:29 | agency-agents | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/msitarzewski/agency-agents |
| 2026-03-29 20:29 | private-gpt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zylon-ai/private-gpt |
| 2026-03-29 20:29 | autoresearch | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/karpathy/autoresearch |
| 2026-03-29 20:29 | emdash | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/generalaction/emdash |
| 2026-03-29 20:29 | oas-kit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Mermade/oas-kit |
| 2026-03-29 20:30 | anything-llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Mintplex-Labs/anything-llm |
| 2026-03-29 20:30 | PyMuPDF | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pymupdf/PyMuPDF |
| 2026-03-29 20:30 | hivemind-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shynlee04/hivemind-plugin |
| 2026-03-29 20:30 | node-gyp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/electron/node-gyp |
| 2026-03-29 20:30 | cronicle | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/cronicle |
| 2026-03-29 20:30 | docling | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docling-project/docling |
| 2026-03-29 20:30 | php-ddd-cargo-sample | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codeliner/php-ddd-cargo-sample |
| 2026-03-29 20:30 | Diabetes-Prediction-using-Machine-Learning | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Diabetes-Prediction-using-Machine-Learning |
| 2026-03-29 20:30 | hotkeys | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/tanstack/hotkeys |
| 2026-03-29 20:30 | awesome-claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/awesome-claude-skills |
| 2026-03-29 20:30 | opc-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/resciencelab/opc-skills.git |
| 2026-03-29 20:30 | vouch-proxy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vouch/vouch-proxy |
| 2026-03-29 20:31 | cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cli/cli |
| 2026-03-29 20:31 | langchain | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/langchain-ai/langchain |
| 2026-03-29 20:31 | isort | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PyCQA/isort |
| 2026-03-29 20:31 | oh-my-openagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/code-yeongyu/oh-my-openagent |
| 2026-03-29 20:31 | pgvector.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pgvector/pgvector.git |
| 2026-03-29 20:31 | helix | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/helix-editor/helix |
| 2026-03-29 20:31 | cli | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/cli/cli |
| 2026-03-29 20:31 | aider | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Aider-AI/aider |
| 2026-03-29 20:31 | Flowise | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FlowiseAI/Flowise |
| 2026-03-29 20:31 | orbitron | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/theleagueof/orbitron |
| 2026-03-29 20:31 | anything-llm | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Mintplex-Labs/anything-llm |
| 2026-03-29 20:31 | TradingAgents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TauricResearch/TradingAgents |
| 2026-03-29 20:31 | awesome-openclaw-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/VoltAgent/awesome-openclaw-skills |
| 2026-03-29 20:31 | code-review-graph | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tirth8205/code-review-graph |
| 2026-03-29 20:31 | shared-workflows | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/shared-workflows |
| 2026-03-29 20:32 | CommandQuery | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hlaueriksson/CommandQuery |
| 2026-03-29 20:32 | n8n-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/czlonkowski/n8n-skills |
| 2026-03-29 20:32 | typescript-ddd-course | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CodelyTV/typescript-ddd-course |
| 2026-03-29 20:32 | tiktok-bulk-downloader-desktop-app | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/minhchi1509/tiktok-bulk-downloader-desktop-app |
| 2026-03-29 20:32 | temm1e.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/temm1e-labs/temm1e.git |
| 2026-03-29 20:32 | xyops-nginx-sso | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyops-nginx-sso |
| 2026-03-29 20:33 | zeroclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zeroclaw-labs/zeroclaw |
| 2026-03-29 20:33 | 9router | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/decolua/9router |
| 2026-03-29 20:33 | claude-apple-bridges | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/more-io/claude-apple-bridges |
| 2026-03-29 20:33 | go-sqlite3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mattn/go-sqlite3 |
| 2026-03-29 20:33 | authelia | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/authelia/authelia |
| 2026-03-29 20:33 | hig-doctor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/raintree-technology/hig-doctor |
| 2026-03-29 20:33 | litellm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BerriAI/litellm |
| 2026-03-29 20:33 | learn-claude-code | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/shareAI-lab/learn-claude-code |
| 2026-03-29 20:34 | trulens | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/truera/trulens |
| 2026-03-29 20:34 | nanobot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/nanobot |
| 2026-03-29 20:34 | reflex | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/reflex-dev/reflex |
| 2026-03-29 20:34 | LitServe | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/LitServe |
| 2026-03-29 20:34 | private-gpt | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zylon-ai/private-gpt |
| 2026-03-29 20:34 | godotdec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Bioruebe/godotdec |
| 2026-03-29 20:34 | claude-cookbooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-cookbooks |
| 2026-03-29 20:34 | vim-plug | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/junegunn/vim-plug |
| 2026-03-29 20:34 | charts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/paradedb/charts |
| 2026-03-29 20:34 | zsh-autosuggestions | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zsh-users/zsh-autosuggestions |
| 2026-03-29 20:34 | get-shit-done | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gsd-build/get-shit-done |
| 2026-03-29 20:34 | markdown-printer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/levz0r/markdown-printer |
| 2026-03-29 20:35 | EventSourcing.NetCore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/oskardudycz/EventSourcing.NetCore |
| 2026-03-29 20:35 | VMware-AIops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zw008/VMware-AIops |
| 2026-03-29 20:35 | trivy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aquasecurity/trivy |
| 2026-03-29 20:35 | paperclip | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/paperclipai/paperclip |
| 2026-03-29 20:35 | agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wshobson/agents |
| 2026-03-29 20:35 | pytorch-lightning | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/pytorch-lightning |
| 2026-03-29 20:35 | gsd-2.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gsd-build/gsd-2.git |
| 2026-03-29 20:35 | project-manager | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mkopylec/project-manager |
| 2026-03-29 20:35 | openai-python | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/openai-python |
| 2026-03-29 20:36 | pgrx | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pgcentralfoundation/pgrx |
| 2026-03-29 20:36 | playwright-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lackeyjb/playwright-skill |
| 2026-03-29 20:36 | AstrBot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AstrBotDevs/AstrBot |
| 2026-03-29 20:36 | langgraph | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/langchain-ai/langgraph |
| 2026-03-29 20:36 | autoclip | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zhouxiaoka/autoclip |
| 2026-03-29 20:36 | setup-n8n | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ndoanh266/setup-n8n |
| 2026-03-29 20:36 | ora | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/ora |
| 2026-03-29 20:36 | next-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/next-skills |
| 2026-03-29 20:36 | Medical-Assisstant | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Medical-Assisstant |
| 2026-03-29 20:36 | pixl-server-user | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-user |
| 2026-03-29 20:36 | hindsight | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nicoloboschi/hindsight |
| 2026-03-29 20:36 | authelia | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/authelia/authelia |
| 2026-03-29 20:36 | dvc | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/iterative/dvc |
| 2026-03-29 20:37 | agents-course | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/agents-course |
| 2026-03-29 20:37 | awesome-copilot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/awesome-copilot |
| 2026-03-29 20:37 | smolagents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/smolagents |
| 2026-03-29 20:37 | RAG_Techniques | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NirDiamant/RAG_Techniques |
| 2026-03-29 20:38 | awesome-generative-ai-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aishwaryanr/awesome-generative-ai-guide |
| 2026-03-29 20:38 | gitleaks | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gitleaks/gitleaks |
| 2026-03-29 20:38 | trufflehog | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/trufflesecurity/trufflehog |
| 2026-03-29 20:38 | agent-browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/agent-browser |
| 2026-03-29 20:38 | mlx | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ml-explore/mlx |
| 2026-03-29 20:40 | claude-code-templates | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/davila7/claude-code-templates |
| 2026-03-29 20:40 | antigravity-awesome-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sickn33/antigravity-awesome-skills |
| 2026-03-29 20:40 | openai-python | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openai/openai-python |
| 2026-03-29 20:40 | Scrapegraph-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ScrapeGraphAI/Scrapegraph-ai |
| 2026-03-29 20:40 | flash-attention | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Dao-AILab/flash-attention |
| 2026-03-29 20:40 | zsh-syntax-highlighting | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zsh-users/zsh-syntax-highlighting |
| 2026-03-29 20:40 | claude-code-best-practice | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-best-practice |
| 2026-03-29 20:40 | serve | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jina-ai/serve |
| 2026-03-29 20:40 | swarm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/swarm |
| 2026-03-29 20:41 | Skill_Seekers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yusufkaraaslan/Skill_Seekers |
| 2026-03-29 20:41 | jaq | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/01mf02/jaq |
| 2026-03-29 20:41 | py_assimilator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/knucklesuganda/py_assimilator |
| 2026-03-29 20:41 | llmware | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/llmware-ai/llmware |
| 2026-03-29 20:41 | skyvern | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Skyvern-AI/skyvern |
| 2026-03-29 20:41 | fastfetch | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/fastfetch-cli/fastfetch |
| 2026-03-29 20:42 | peft | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/peft |
| 2026-03-29 20:42 | GenAI_Agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NirDiamant/GenAI_Agents |
| 2026-03-29 20:42 | markitdown | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/markitdown |
| 2026-03-29 20:42 | goconvey | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/smartystreets/goconvey |
| 2026-03-29 20:42 | Flight-Fare-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Flight-Fare-Prediction |
| 2026-03-29 20:42 | qsv-docopt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/qsv-docopt |
| 2026-03-29 20:42 | domhandler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fb55/domhandler |
| 2026-03-29 20:42 | firecrawl-go | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mendableai/firecrawl-go |
| 2026-03-29 20:42 | Virat-Kohli-Score-Analytics | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Virat-Kohli-Score-Analytics |
| 2026-03-29 20:43 | authentik | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/goauthentik/authentik |
| 2026-03-29 20:43 | lazy.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/folke/lazy.nvim |
| 2026-03-29 20:43 | pgvector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pgvector/pgvector |
| 2026-03-29 20:44 | telescope.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nvim-telescope/telescope.nvim |
| 2026-03-29 20:44 | opik | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/comet-ml/opik |
| 2026-03-29 20:44 | mq-conv | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-conv |
| 2026-03-29 20:44 | NanoBanana-PPT-Skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/op7418/NanoBanana-PPT-Skills |
| 2026-03-29 20:45 | codebuff | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CodebuffAI/codebuff |
| 2026-03-29 20:45 | ansi-regex | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/chalk/ansi-regex |
| 2026-03-29 20:45 | crush | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/charmbracelet/crush |
| 2026-03-29 20:45 | bump-homebrew-formula-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mislav/bump-homebrew-formula-action |
| 2026-03-29 20:45 | library | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ddd-by-examples/library |
| 2026-03-29 20:45 | UniExtract2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Bioruebe/UniExtract2 |
| 2026-03-29 20:45 | npkill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/voidcosmos/npkill |
| 2026-03-29 20:45 | pixl-json-stream | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-json-stream |
| 2026-03-29 20:45 | CR2-Repair-Tool | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DRCRecoveryData/CR2-Repair-Tool |
| 2026-03-29 20:45 | node-cqrs-eventdenormalizer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thenativeweb/node-cqrs-eventdenormalizer |
| 2026-03-29 20:45 | fullstack-starter-template | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sairyss/fullstack-starter-template |
| 2026-03-29 20:46 | qsv | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/qsv |
| 2026-03-29 20:46 | vue-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hyf0/vue-skills.git |
| 2026-03-29 20:46 | showdown | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/showdownjs/showdown |
| 2026-03-29 20:46 | Doclify | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Doclify |
| 2026-03-29 20:46 | awesome-notebookLM-prompts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/serenakeyitan/awesome-notebookLM-prompts |
| 2026-03-29 20:46 | system-design-patterns | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sairyss/system-design-patterns |
| 2026-03-29 20:47 | plane | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/makeplane/plane |
| 2026-03-29 20:47 | httpcache | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gregjones/httpcache |
| 2026-03-29 20:47 | domain-driven-hexagon | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sairyss/domain-driven-hexagon |
| 2026-03-29 20:47 | node-eventstore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adrai/node-eventstore |
| 2026-03-29 20:47 | ansi-styles | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/chalk/ansi-styles |
| 2026-03-29 20:48 | turborepo.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel/turborepo.git |
| 2026-03-29 20:48 | domain-story-modeler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wps/domain-story-modeler |
| 2026-03-29 20:48 | xyrun | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyrun |
| 2026-03-29 20:49 | MoneyPrinterTurbo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harry0703/MoneyPrinterTurbo |
| 2026-03-29 20:49 | ollamaMQ | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Chleba/ollamaMQ |
| 2026-03-29 20:49 | AIDA | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Vasco0x4/AIDA |
| 2026-03-29 20:49 | event-sourcing-cqrs-examples | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/andreschaffer/event-sourcing-cqrs-examples |
| 2026-03-29 20:49 | Champollion | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Orvid/Champollion |
| 2026-03-29 20:49 | Qt-Linguist | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thurask/Qt-Linguist |
| 2026-03-29 20:49 | eventcatalog | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boyney123/eventcatalog |
| 2026-03-29 20:49 | eslint-react | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rel1cx/eslint-react |
| 2026-03-29 20:49 | boltdbcache | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/birkelund/boltdbcache |
| 2026-03-29 20:49 | tree-sitter-javascript | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tree-sitter/tree-sitter-javascript |
| 2026-03-29 20:49 | egon.io | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/WPS/egon.io |
| 2026-03-29 20:49 | samply | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mstange/samply |
| 2026-03-29 20:50 | eShopOnWeb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dotnet-architecture/eShopOnWeb |
| 2026-03-29 20:50 | slonik | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gajus/slonik |
| 2026-03-29 20:52 | lobehub | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lobehub/lobehub |
| 2026-03-29 20:52 | metube-firefox-addon | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nanocortex/metube-firefox-addon |
| 2026-03-29 20:52 | pg0 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vectorize-io/pg0 |
| 2026-03-29 20:52 | jOOQ | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jOOQ/jOOQ |
| 2026-03-29 20:52 | mirrors-mypy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pre-commit/mirrors-mypy |
| 2026-03-29 20:52 | Grabbit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/socratespap/Grabbit |
| 2026-03-29 20:52 | pg_textsearch | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/timescale/pg_textsearch |
| 2026-03-29 20:53 | pi-mono | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/badlogic/pi-mono |
| 2026-03-29 20:53 | cosign-installer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sigstore/cosign-installer |
| 2026-03-29 20:53 | mqt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mqt |
| 2026-03-29 20:53 | pyroscope-dotnet | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/pyroscope-dotnet |
| 2026-03-29 20:53 | Acontext-Examples | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/memodb-io/Acontext-Examples |
| 2026-03-29 20:53 | pypict-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/omkamal/pypict-claude-skill |
| 2026-03-29 20:53 | dotfiles | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thieung/dotfiles |
| 2026-03-29 20:53 | browser-use | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/browser-use/browser-use |
| 2026-03-29 20:53 | mirrors-eslint | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pre-commit/mirrors-eslint |
| 2026-03-29 20:53 | us-census-bureau-data-api-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/us-census-bureau-data-api-mcp |
| 2026-03-29 20:53 | Mole | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tw93/Mole |
| 2026-03-29 20:53 | Star-Office-UI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ringhyacinth/Star-Office-UI |
| 2026-03-29 20:53 | ag-auto-click-scroll | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zixfelw/ag-auto-click-scroll |
| 2026-03-29 20:53 | mq-update | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-update |
| 2026-03-29 20:54 | ddd-modulith | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/janikredpandadev/ddd-modulith |
| 2026-03-29 20:54 | paperclip.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/paperclipai/paperclip.git |
| 2026-03-29 20:54 | agent-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/softaworks/agent-toolkit |
| 2026-03-29 20:54 | Bio.cs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Bioruebe/Bio.cs |
| 2026-03-29 20:54 | metadata-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docker/metadata-action |
| 2026-03-29 20:54 | pyfiglet | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pwaller/pyfiglet |
| 2026-03-29 20:55 | seeaifirst | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BARONFANTHE/seeaifirst |
| 2026-03-29 20:55 | LLM-Finetuning | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ashishpatel26/LLM-Finetuning |
| 2026-03-29 20:55 | IDDD_Samples | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VaughnVernon/IDDD_Samples |
| 2026-03-29 20:55 | node-cqrs-domain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adrai/node-cqrs-domain |
| 2026-03-29 20:56 | ArtifactsBenchmark | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Tencent-Hunyuan/ArtifactsBenchmark |
| 2026-03-29 20:56 | agent-browser.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/agent-browser.git |
| 2026-03-29 20:56 | pyupgrade | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/asottile/pyupgrade |
| 2026-03-29 20:56 | web-check | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lissy93/web-check |
| 2026-03-29 20:56 | xyops-nginx | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyops-nginx |
| 2026-03-29 20:56 | Wine-Quality-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Wine-Quality-Prediction |
| 2026-03-29 20:56 | jooq | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jooq/jooq |
| 2026-03-29 20:56 | node-isdoc-pdf.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deltazero-cz/node-isdoc-pdf.git |
| 2026-03-29 20:56 | subgrid | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hoangvu12/subgrid |
| 2026-03-29 20:56 | pprof-nodejs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DataDog/pprof-nodejs |
| 2026-03-29 20:56 | commanded | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/commanded/commanded |
| 2026-03-29 20:58 | univer.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dream-num/univer.git |
| 2026-03-29 20:58 | waoowaoo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/saturndec/waoowaoo |
| 2026-03-29 20:58 | jsonnet-bundler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jsonnet-bundler/jsonnet-bundler |
| 2026-03-29 20:58 | ossinsight | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pingcap/ossinsight |
| 2026-03-29 20:59 | pattern-craft | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/megh-bari/pattern-craft |
| 2026-03-29 21:00 | FinRL | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AI4Finance-Foundation/FinRL |
| 2026-03-29 21:00 | camelot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camelot-dev/camelot |
| 2026-03-29 21:00 | triton.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/triton-lang/triton.git |
| 2026-03-29 21:00 | node-eventstore | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/thenativeweb/node-eventstore |
| 2026-03-29 21:00 | txtai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neuml/txtai |
| 2026-03-29 21:00 | mcp-server-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/figma/mcp-server-guide |
| 2026-03-29 21:01 | nuclei | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/projectdiscovery/nuclei |
| 2026-03-29 21:01 | swarm | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openai/swarm |
| 2026-03-29 21:01 | Tetris.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dtrupenn/Tetris.git |
| 2026-03-29 21:01 | playwright | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/playwright |
| 2026-03-29 21:01 | VoxCPM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenBMB/VoxCPM |
| 2026-03-29 21:12 | nixpkgs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NixOS/nixpkgs |
| 2026-03-29 21:13 | vue-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hyf0/vue-skills |
| 2026-03-29 21:13 | litgpt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/litgpt |
| 2026-03-29 21:13 | all-contributors | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/all-contributors/all-contributors |
| 2026-03-29 21:13 | codespell | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codespell-project/codespell |
| 2026-03-29 21:13 | broadway | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/broadway/broadway |
| 2026-03-29 21:13 | quotio | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nguyenphutrong/quotio |
| 2026-03-29 21:13 | gaia-ui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/theexperiencecompany/gaia-ui |
| 2026-03-29 21:13 | eventstore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/slashdotdash/eventstore |
| 2026-03-29 21:13 | utagedec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Bioruebe/utagedec |
| 2026-03-29 21:13 | Medicine-Recognition-System | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Medicine-Recognition-System |
| 2026-03-29 21:13 | Flight-Fare-Prediction | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanM45/Flight-Fare-Prediction |
| 2026-03-29 21:13 | Virat-Kohli-Score-Analytics | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanMurapaka45/Virat-Kohli-Score-Analytics |
| 2026-03-29 21:13 | claude-plugins-official | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-plugins-official |
| 2026-03-29 21:13 | docling | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/docling-project/docling |
| 2026-03-29 21:14 | temm1e.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/temm1e/temm1e.git |
| 2026-03-29 21:14 | automated-price-tracking | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BexTuychiev/automated-price-tracking |
| 2026-03-29 21:14 | custom-plugin-java | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pluginagentmarketplace/custom-plugin-java |
| 2026-03-29 21:14 | rust-csv | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jqnatividad/rust-csv |
| 2026-03-29 21:14 | pixl-logger | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-logger |
| 2026-03-29 21:14 | lang-sql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codemirror/lang-sql |
| 2026-03-29 21:14 | octosql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cube2222/octosql |
| 2026-03-29 21:14 | configstore | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/configstore |
| 2026-03-29 21:15 | trufflehog.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/trufflesecurity/trufflehog.git |
| 2026-03-29 21:15 | release-it | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/release-it/release-it |
| 2026-03-29 21:15 | mirrors-yapf | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pre-commit/mirrors-yapf |
| 2026-03-29 21:15 | ai-hands-on | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Ramakm/ai-hands-on |
| 2026-03-29 21:16 | temm1e | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/temm1e/temm1e |
| 2026-03-29 21:16 | claude-openclaw-bridge | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ericblue/claude-openclaw-bridge |
| 2026-03-29 21:16 | xTuring | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/stochasticai/xTuring |
| 2026-03-29 21:16 | otel-profiling-java | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/otel-profiling-java |
| 2026-03-29 21:16 | cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/googleworkspace/cli |
| 2026-03-29 21:16 | tui-studio | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jalonsogo/tui-studio |
| 2026-03-29 21:16 | MediatR | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/LuckyPennySoftware/MediatR |
| 2026-03-29 21:16 | react-enterprise-boilerplate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fdhhhdjd/react-enterprise-boilerplate |
| 2026-03-29 21:16 | opentelemetry-ruby | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-telemetry/opentelemetry-ruby |
| 2026-03-29 21:16 | message-db | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/message-db/message-db |
| 2026-03-29 21:16 | DDD-starter-dotnet | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/itlibrium/DDD-starter-dotnet |
| 2026-03-29 21:16 | ag-live-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zixfelw/ag-live-code |
| 2026-03-29 21:17 | zombodb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zombodb/zombodb |
| 2026-03-29 21:17 | awesome-llm-apps | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Shubhamsaboo/awesome-llm-apps |
| 2026-03-29 21:17 | mq-tui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-tui |
| 2026-03-29 21:17 | typescript-basic-skeleton | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CodelyTV/typescript-basic-skeleton |
| 2026-03-29 21:17 | DocGenius-Revolutionizing-PDFs-with-AI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/DocGenius-Revolutionizing-PDFs-with-AI |
| 2026-03-29 21:17 | agent-browser | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/agent-browser |
| 2026-03-29 21:27 | rust | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rust-lang/rust |
| 2026-03-29 21:27 | docs | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/RichardLitt/docs |
| 2026-03-29 21:28 | vexor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/scarletkc/vexor |
| 2026-03-29 21:28 | agentsview.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wesm/agentsview.git |
| 2026-03-29 21:28 | polars | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pola-rs/polars |
| 2026-03-29 21:28 | zsh-syntax-highlighting | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zsh-users/zsh-syntax-highlighting |
| 2026-03-29 21:30 | weaviate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/weaviate/weaviate |
| 2026-03-29 21:30 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vuejs-ai/skills.git |
| 2026-03-29 21:30 | excalidraw-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/excalidraw/excalidraw-mcp |
| 2026-03-29 21:30 | goddd | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/marcusolsson/goddd |
| 2026-03-29 21:30 | IDDD_Samples_NET | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/VaughnVernon/IDDD_Samples_NET |
| 2026-03-29 21:30 | ava | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/avajs/ava |
| 2026-03-29 21:31 | DeepSpeed | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deepspeedai/DeepSpeed |
| 2026-03-29 21:32 | ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel/ai |
| 2026-03-29 21:32 | pyo3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PyO3/pyo3 |
| 2026-03-29 21:32 | Student-Perfomance-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Student-Perfomance-Prediction |
| 2026-03-29 21:32 | fold-case | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dmoscrop/fold-case |
| 2026-03-29 21:34 | lobe-chat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lobehub/lobe-chat |
| 2026-03-29 21:34 | killercoda | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/killercoda |
| 2026-03-29 21:34 | swarm.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/swarm.git |
| 2026-03-29 21:34 | Acontext | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/memodb-io/Acontext |
| 2026-03-29 21:34 | sympozium | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/sympozium-ai/sympozium |
| 2026-03-29 21:34 | paradedb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/paradedb/paradedb |
| 2026-03-29 21:34 | wormhole | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agrinman/wormhole |
| 2026-03-29 21:34 | tree-sitter-ql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tree-sitter/tree-sitter-ql |
| 2026-03-29 21:35 | ai-engineering-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Sumanth077/ai-engineering-toolkit |
| 2026-03-29 21:35 | unsloth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/unslothai/unsloth |
| 2026-03-29 21:35 | xpfarm | REJECTED | Bad pattern: xpfarm | https://github.com/canuk40/xpfarm |
| 2026-03-29 21:35 | xpfarm | REJECTED | BLOCKED: pattern 'xpfarm' trong tên repo | https://github.com/canuk40/xpfarm |
| 2026-03-29 21:35 | neural-memory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nhadaututtheky/neural-memory |
| 2026-03-29 21:35 | csvw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/w3c/csvw |
| 2026-03-29 21:36 | flake8 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PyCQA/flake8 |
| 2026-03-29 21:36 | End-to-End-Airbnb-Price-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/End-to-End-Airbnb-Price-Prediction |
| 2026-03-29 21:36 | cloudnative-pg | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudnative-pg/cloudnative-pg |
| 2026-03-29 21:36 | gpt4free | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/xtekky/gpt4free |
| 2026-03-29 21:36 | pixl-unit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-unit |
| 2026-03-29 21:36 | cloudflared | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudflare/cloudflared |
| 2026-03-29 21:36 | supports-color | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/chalk/supports-color |
| 2026-03-29 21:36 | performa-satellite | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/performa-satellite |
| 2026-03-29 21:36 | mq-docs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-docs |
| 2026-03-29 21:36 | dasel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tomwright/dasel |
| 2026-03-29 21:36 | pg-schema-diff.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/paradedb/pg-schema-diff.git |
| 2026-03-29 21:37 | ReactiveTraderCloud | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AdaptiveConsulting/ReactiveTraderCloud |
| 2026-03-29 21:37 | terraform-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/antonbabenko/terraform-skill |
| 2026-03-29 21:37 | awf | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TUAN130294/awf |
| 2026-03-29 21:37 | symfony-ddd-wishlist | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/franzose/symfony-ddd-wishlist |
| 2026-03-29 21:37 | DevSkim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/DevSkim |
| 2026-03-29 21:37 | gender_guesser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Raduc4/gender_guesser |
| 2026-03-29 21:37 | act | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nektos/act |
| 2026-03-29 21:37 | gm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aheckmann/gm |
| 2026-03-29 21:37 | registry | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/registry |
| 2026-03-29 21:37 | temm1e | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/temm1e |
| 2026-03-29 21:37 | TradingAgents | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/TauricResearch/TradingAgents |
| 2026-03-29 21:38 | goclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nextlevelbuilder/goclaw |
| 2026-03-29 21:38 | Checking-Password-Strength-using-Machine-Learning | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Checking-Password-Strength-using-Machine-Learning |
| 2026-03-29 21:38 | ohmyzsh | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ohmyzsh/ohmyzsh |
| 2026-03-29 21:38 | nodeQA | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nodemationqa/nodeQA |
| 2026-03-29 21:38 | luau | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Roblox/luau |
| 2026-03-29 21:38 | GenAI_Agents | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/NirDiamant/GenAI_Agents |
| 2026-03-29 21:38 | homebrew-brew | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pyroscope-io/homebrew-brew |
| 2026-03-29 21:38 | oncecache | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neilotoole/oncecache |
| 2026-03-29 21:39 | Scritchy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ToJans/Scritchy |
| 2026-03-29 21:39 | pg-schema-diff | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/paradedb/pg-schema-diff |
| 2026-03-29 21:39 | Stringly.Typed | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mission202/Stringly.Typed |
| 2026-03-29 21:39 | package-template | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/napi-rs/package-template |
| 2026-03-29 21:39 | hindsight | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/hindsight-ai/hindsight |
| 2026-03-29 21:39 | Projac | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BitTacklr/Projac |
| 2026-03-29 21:39 | azure-go-ddd-boilerplate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/joshpme/azure-go-ddd-boilerplate |
| 2026-03-29 21:39 | lobster | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aardappel/lobster |
| 2026-03-29 21:39 | iOS-Accessibility-Audit-Skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ramzesenok/iOS-Accessibility-Audit-Skill |
| 2026-03-29 21:39 | grex | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pemistahl/grex |
| 2026-03-29 21:39 | mq-java | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-java |
| 2026-03-29 21:40 | spec-kit.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/github/spec-kit.git |
| 2026-03-29 21:40 | Agent-Skills-for-Context-Engineering.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering.git |
| 2026-03-29 21:40 | node-lru-cache | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/isaacs/node-lru-cache |
| 2026-03-29 21:40 | pinyin-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/batterseapower/pinyin-toolkit |
| 2026-03-29 21:40 | swift-patterns-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/efremidze/swift-patterns-skill |
| 2026-03-29 21:40 | chat-quality-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tanviet12/chat-quality-agent |
| 2026-03-29 21:40 | clawhub | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openclaw/clawhub |
| 2026-03-29 21:40 | End-to-End-Chest-Disease-Classification | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification |
| 2026-03-29 21:40 | gdrive-manager.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/habitual69/gdrive-manager.git |
| 2026-03-29 21:40 | find-cache-dir | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/avajs/find-cache-dir |
| 2026-03-29 21:40 | Prompt_Engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NirDiamant/Prompt_Engineering |
| 2026-03-29 21:41 | agency-agents-zh | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jnMetaCode/agency-agents-zh |
| 2026-03-29 21:41 | qsv-easy-windows-installer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/qsv-easy-windows-installer |
| 2026-03-29 21:41 | Adobe-Camera-Profiles-Unlocker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/phanxuanquang/Adobe-Camera-Profiles-Unlocker |
| 2026-03-29 21:41 | gah | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/get-gah/gah |
| 2026-03-29 21:41 | citation-check-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/serenakeyitan/citation-check-skill |
| 2026-03-29 21:41 | MiniMax-AI.github.io | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-AI.github.io |
| 2026-03-29 21:42 | claw0 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/claw0 |
| 2026-03-29 21:42 | pdfplumber | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jsvine/pdfplumber |
| 2026-03-29 21:42 | awesome-openclaw-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mergisi/awesome-openclaw-agents |
| 2026-03-29 21:42 | agent-os | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/buildermethods/agent-os |
| 2026-03-29 21:42 | ai.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/stripe/ai.git |
| 2026-03-29 21:42 | otel-profiling-ruby | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pyroscope-io/otel-profiling-ruby |
| 2026-03-29 21:42 | jsoncrack.com | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AykutSarac/jsoncrack.com |
| 2026-03-29 21:42 | agents-course.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/agents-course.git |
| 2026-03-29 21:42 | acefile | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/droe/acefile |
| 2026-03-29 21:42 | WikidataMCP.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/philippesaade-wmde/WikidataMCP.git |
| 2026-03-29 21:44 | payload | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/payloadcms/payload |
| 2026-03-29 21:44 | update-notifier | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/update-notifier |
| 2026-03-29 21:44 | ChatDev | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenBMB/ChatDev |
| 2026-03-29 21:44 | awesome-go | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/avelino/awesome-go |
| 2026-03-29 21:44 | superagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forwardemail/superagent |
| 2026-03-29 21:44 | cmp-nvim-lsp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hrsh7th/cmp-nvim-lsp |
| 2026-03-29 21:44 | pyroscope-java | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pyroscope-io/pyroscope-java |
| 2026-03-29 21:44 | upsonic | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upsonic/upsonic |
| 2026-03-29 21:44 | Chatbot-Using-Langchain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Chatbot-Using-Langchain |
| 2026-03-29 21:45 | gman | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/benbalter/gman |
| 2026-03-29 21:45 | datapusher-plus | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/datapusher-plus |
| 2026-03-29 21:45 | springboot-best-practices | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mduongvandinh/springboot-best-practices |
| 2026-03-29 21:45 | spoondec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Bioruebe/spoondec |
| 2026-03-29 21:45 | ios-simulator-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/conorluddy/ios-simulator-skill |
| 2026-03-29 21:45 | OSINT-CTFs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ubikron/OSINT-CTFs |
| 2026-03-29 21:45 | RAG_Techniques | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/NirDiamant/RAG_Techniques |
| 2026-03-29 21:45 | how-to-ralph-wiggum | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ghuntley/how-to-ralph-wiggum |
| 2026-03-29 21:46 | pylint | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pylint-dev/pylint |
| 2026-03-29 21:46 | firecrawl-claude-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/firecrawl-claude-plugin |
| 2026-03-29 21:46 | peft | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/huggingface/peft |
| 2026-03-29 21:46 | pandasql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yhat/pandasql |
| 2026-03-29 21:46 | comlink | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/GoogleChromeLabs/comlink |
| 2026-03-29 21:46 | skill-generator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/marketingjuliancongdanh79-pixel/skill-generator |
| 2026-03-29 21:46 | dotfiles | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/username/dotfiles |
| 2026-03-29 21:46 | agentql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinyfish-io/agentql |
| 2026-03-29 21:46 | booster | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boostercloud/booster |
| 2026-03-29 21:46 | agentune | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tqdat410/agentune |
| 2026-03-29 21:46 | dev-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fvadicamo/dev-agent-skills |
| 2026-03-29 21:46 | ai-devkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codeaholicguy/ai-devkit |
| 2026-03-29 21:47 | baoyu-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jimliu/baoyu-skills.git |
| 2026-03-29 21:47 | react-grab | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aidenybai/react-grab |
| 2026-03-29 21:47 | node-imap | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mscdex/node-imap |
| 2026-03-29 21:47 | aginews-podcast | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ericciarla/aginews-podcast |
| 2026-03-29 21:47 | nblm-rs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/K-dash/nblm-rs |
| 2026-03-29 21:47 | nvim-dap-ui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rcarriga/nvim-dap-ui |
| 2026-03-29 21:47 | cron | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/robfig/cron |
| 2026-03-29 21:47 | gitingest | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coderamp-labs/gitingest |
| 2026-03-29 21:48 | fastapi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fastapi/fastapi |
| 2026-03-29 21:48 | beautiful_prose | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SHADOWPR0/beautiful_prose |
| 2026-03-29 21:48 | magic-wormhole | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/magic-wormhole/magic-wormhole |
| 2026-03-29 21:48 | gentleman-ai-installer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gentleman-programming/gentleman-ai-installer |
| 2026-03-29 21:48 | pyroscope-java | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/grafana/pyroscope-java |
| 2026-03-29 21:48 | go-colorable | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mattn/go-colorable |
| 2026-03-29 21:48 | JESA | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yreynhout/JESA |
| 2026-03-29 21:52 | posthog.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/posthog/posthog.git |
| 2026-03-29 21:52 | pixl-xyapp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/pixl-xyapp |
| 2026-03-29 21:52 | npm-to-yarn | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bgub/npm-to-yarn |
| 2026-03-29 21:52 | ForgeTerm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/eliophan/ForgeTerm |
| 2026-03-29 21:53 | pathway | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pathwaycom/pathway |
| 2026-03-29 21:53 | linear-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wrsmith108/linear-claude-skill |
| 2026-03-29 21:53 | ARW-NEF-Repair-Tool | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DRCRecoveryData/ARW-NEF-Repair-Tool |
| 2026-03-29 21:53 | AggregateSource | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yreynhout/AggregateSource |
| 2026-03-29 21:53 | openchatbi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zhongyu09/openchatbi |
| 2026-03-29 21:53 | test_keys.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/trufflesecurity/test_keys.git |
| 2026-03-29 21:53 | syncview-desktop | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hgck000/syncview-desktop |
| 2026-03-29 21:53 | ai-devkit.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Codeaholicguy/ai-devkit.git |
| 2026-03-29 21:53 | claude-code-software-engineer-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-software-engineer-plugin |
| 2026-03-29 21:53 | eventstore | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/commanded/eventstore |
| 2026-03-29 21:53 | pixl-request | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-request |
| 2026-03-29 21:53 | stitch-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-labs-code/stitch-skills |
| 2026-03-29 21:53 | mq-python | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-python |
| 2026-03-29 21:53 | xyplug-sample-npx | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyplug-sample-npx |
| 2026-03-29 21:53 | surge | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/surge-downloader/surge |
| 2026-03-29 21:54 | opentelemetry-python | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-telemetry/opentelemetry-python |
| 2026-03-29 21:54 | hindsight.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nicoloboschi/hindsight.git |
| 2026-03-29 21:54 | WellAlly-health | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huifer/WellAlly-health |
| 2026-03-29 21:54 | EventFlow.Example | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OKTAYKIR/EventFlow.Example |
| 2026-03-29 21:54 | encoding-sniffer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fb55/encoding-sniffer |
| 2026-03-29 21:54 | Spam-Email-Detection | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Spam-Email-Detection |
| 2026-03-29 21:54 | hyfetch | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hykilpikonna/hyfetch |
| 2026-03-29 21:54 | typedi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/typestack/typedi |
| 2026-03-29 21:54 | spec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ulid/spec |
| 2026-03-29 21:54 | claude-code.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code.git |
| 2026-03-29 21:54 | FBMediaDownloader | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HoangTran0410/FBMediaDownloader |
| 2026-03-29 21:54 | tree-sitter-c | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tree-sitter/tree-sitter-c |
| 2026-03-29 21:55 | modelcontextprotocol | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/modelcontextprotocol |
| 2026-03-29 21:55 | rust-clippy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rust-lang/rust-clippy |
| 2026-03-29 21:55 | typescript-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/typescript-sdk |
| 2026-03-29 21:56 | rq | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dflemstr/rq |
| 2026-03-29 21:57 | selenium | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SeleniumHQ/selenium |
| 2026-03-29 21:57 | books | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/frappe/books |
| 2026-03-29 21:58 | wasm-bindgen | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wasm-bindgen/wasm-bindgen |
| 2026-03-29 21:58 | nanobot | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/HKUDS/nanobot |
| 2026-03-29 21:58 | VieNeu-TTS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pnnbao97/VieNeu-TTS |
| 2026-03-29 21:58 | EquinoxProject | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/EduardoPires/EquinoxProject |
| 2026-03-29 21:58 | schemas | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/esd-org-uk/schemas |
| 2026-03-29 21:58 | file-format | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mmalecot/file-format |
| 2026-03-29 21:58 | nvim-cmp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hrsh7th/nvim-cmp |
| 2026-03-29 21:58 | claude-code-skill-maker-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-skill-maker-plugin |
| 2026-03-29 21:58 | ndjson-spec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ndjson/ndjson-spec |
| 2026-03-29 21:58 | agents-course | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/huggingface/agents-course |
| 2026-03-29 21:58 | pyroscope-lambda-extension | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/pyroscope-lambda-extension |
| 2026-03-29 21:58 | m-r | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gregoryyoung/m-r |
| 2026-03-29 22:00 | mlflow | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlflow/mlflow |
| 2026-03-29 22:00 | superpowers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/obra/superpowers |
| 2026-03-29 22:00 | marten | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JasperFx/marten |
| 2026-03-29 22:01 | crawlee | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/apify/crawlee |
| 2026-03-29 22:01 | mlua | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlua-rs/mlua |
| 2026-03-29 22:01 | mirrors-yapf.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pre-commit/mirrors-yapf.git |
| 2026-03-29 22:01 | google-maps-scraper | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gosom/google-maps-scraper |
| 2026-03-29 22:01 | agency-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/msitarzewski/agency-agents |
| 2026-03-29 22:01 | uvloop | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MagicStack/uvloop |
| 2026-03-29 22:01 | hexhog | REJECTED | Bad pattern: hexhog | https://github.com/DVDTSB/hexhog |
| 2026-03-29 22:01 | hexhog | REJECTED | BLOCKED: pattern 'hexhog' trong tên repo | https://github.com/DVDTSB/hexhog |
| 2026-03-29 22:01 | dotfiles.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thieung/dotfiles.git |
| 2026-03-29 22:01 | node-cqrs-domain | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/thenativeweb/node-cqrs-domain |
| 2026-03-29 22:01 | mq-task | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-task |
| 2026-03-29 22:02 | Diamond-Price-Prediction | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Diamond-Price-Prediction |
| 2026-03-29 22:02 | chalk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/chalk/chalk |
| 2026-03-29 22:02 | LlamaFactory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hiyouga/LlamaFactory |
| 2026-03-29 22:02 | strix.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/usestrix/strix.git |
| 2026-03-29 22:02 | apple-hig-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/raintree-technology/apple-hig-skills |
| 2026-03-29 22:02 | litellm | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/BerriAI/litellm |
| 2026-03-29 22:02 | tree-sitter-c-sharp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tree-sitter/tree-sitter-c-sharp |
| 2026-03-29 22:02 | pixl-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server |
| 2026-03-29 22:02 | jsonschema-rs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Stranger6667/jsonschema-rs |
| 2026-03-29 22:02 | pixl-server-unbase | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-unbase |
| 2026-03-29 22:02 | runtime-spec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/opencontainers/runtime-spec |
| 2026-03-29 22:02 | xysat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xysat |
| 2026-03-29 22:02 | telescope.nvim | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nvim-telescope/telescope.nvim |
| 2026-03-29 22:02 | typescript-ddd-example | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CodelyTV/typescript-ddd-example |
| 2026-03-29 22:02 | ui-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ibelick/ui-skills |
| 2026-03-29 22:03 | vite-plugin-react | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vitejs/vite-plugin-react |
| 2026-03-29 22:03 | Cirqus | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/d60/Cirqus |
| 2026-03-29 22:03 | explicit-architecture-php | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hgraca/explicit-architecture-php |
| 2026-03-29 22:03 | Rock-and-Mine-Detection | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Rock-and-Mine-Detection |
| 2026-03-29 22:03 | otel-profiling-go | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/otel-profiling-go |
| 2026-03-29 22:03 | FsUno | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thinkbeforecoding/FsUno |
| 2026-03-29 22:03 | nuxt-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/onmax/nuxt-skills.git |
| 2026-03-29 22:03 | jsoncrack.com.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AykutSarac/jsoncrack.com.git |
| 2026-03-29 22:03 | docopt.rs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/docopt/docopt.rs |
| 2026-03-29 22:04 | prompt-eng-interactive-tutorial | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/prompt-eng-interactive-tutorial |
| 2026-03-29 22:04 | symfony-7-es-cqrs-boilerplate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jorge07/symfony-7-es-cqrs-boilerplate |
| 2026-03-29 22:04 | docsonnet | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jsonnet-libs/docsonnet |
| 2026-03-29 22:04 | oauth2-proxy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/oauth2-proxy/oauth2-proxy |
| 2026-03-29 22:04 | MarketInsight | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/MarketInsight |
| 2026-03-29 22:04 | End-to-End-Movie-Recommendation-System | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/End-to-End-Movie-Recommendation-System |
| 2026-03-29 22:04 | csvlens | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/YS-L/csvlens |
| 2026-03-29 22:05 | eventcatalog.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/event-catalog/eventcatalog.git |
| 2026-03-29 22:05 | ktab | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dunkbing/ktab |
| 2026-03-29 22:05 | luau | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/luau-lang/luau |
| 2026-03-29 22:05 | browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lightpanda-io/browser |
| 2026-03-29 22:06 | plotly.js.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/plotly/plotly.js.git |
| 2026-03-29 22:06 | obsidian-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kepano/obsidian-skills.git |
| 2026-03-29 22:06 | test-builds | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/readthedocs/test-builds |
| 2026-03-29 22:06 | OptikR | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OptikR/OptikR |
| 2026-03-29 22:06 | hyperfine | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sharkdp/hyperfine |
| 2026-03-29 22:07 | 9router.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/decolua/9router.git |
| 2026-03-29 22:07 | ai-devkit | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Codeaholicguy/ai-devkit |
| 2026-03-29 22:07 | awesome-claude-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ComposioHQ/awesome-claude-skills |
| 2026-03-29 22:07 | excalidraw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/excalidraw/excalidraw |
| 2026-03-29 22:07 | open-lovable | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/open-lovable |
| 2026-03-29 22:07 | emittery | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/emittery |
| 2026-03-29 22:08 | n8n-docs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/n8n-io/n8n-docs |
| 2026-03-29 22:08 | dxt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/dxt |
| 2026-03-29 22:08 | acpms | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thaonv7995/acpms |
| 2026-03-29 22:08 | model-hierarchy-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zscole/model-hierarchy-skill |
| 2026-03-29 22:08 | grafonnet-lib | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/grafonnet-lib |
| 2026-03-29 22:08 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zackkorman/skills.git |
| 2026-03-29 22:08 | context7 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upstash/context7 |
| 2026-03-29 22:08 | go-ddd-sample | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/takashabe/go-ddd-sample |
| 2026-03-29 22:08 | agent-teams-lite.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gentleman-programming/agent-teams-lite.git |
| 2026-03-29 22:08 | neko | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HaxeFoundation/neko |
| 2026-03-29 22:09 | bmad-method-test-architecture-enterprise | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise |
| 2026-03-29 22:09 | awesome-copilot | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/github/awesome-copilot |
| 2026-03-29 22:09 | docs | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dream-num/docs |
| 2026-03-29 22:09 | pyroscope-rs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/pyroscope-rs |
| 2026-03-29 22:09 | Vane | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ItzCrazyKns/Vane |
| 2026-03-29 22:09 | dbt-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dbt-labs/dbt-agent-skills |
| 2026-03-29 22:09 | packer.nvim | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wbthomason/packer.nvim |
| 2026-03-29 22:09 | flash-attention | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Dao-AILab/flash-attention |
| 2026-03-29 22:09 | patchright | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Kaliiiiiiiiii-Vinyzu/patchright |
| 2026-03-29 22:09 | Chatbot-Using-Langchain | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanMurapaka45/Chatbot-Using-Langchain |
| 2026-03-29 22:09 | flake8 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pycqa/flake8 |
| 2026-03-29 22:09 | deveel.repository | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deveel/deveel.repository |
| 2026-03-29 22:09 | univer-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dream-num/univer-mcp |
| 2026-03-29 22:09 | aws-agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/itsmostafa/aws-agent-skills.git |
| 2026-03-29 22:09 | xsv | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Yomguithereal/xsv |
| 2026-03-29 22:09 | diginext | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/digitopvn/diginext |
| 2026-03-29 22:10 | Kode-agent-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode-agent-sdk |
| 2026-03-29 22:10 | bandit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PyCQA/bandit |
| 2026-03-29 22:10 | data-structure-protocol | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/k-kolomeitsev/data-structure-protocol |
| 2026-03-29 22:10 | repomix | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yamadashy/repomix |
| 2026-03-29 22:11 | seaweedfs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/seaweedfs/seaweedfs |
| 2026-03-29 22:11 | agent-teams | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dsclca12/agent-teams |
| 2026-03-29 22:11 | my-translator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/phuc-nt/my-translator |
| 2026-03-29 22:11 | sanitize.css | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/csstools/sanitize.css |
| 2026-03-29 22:11 | LexiQuest-Modular-DDD | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ryletko/LexiQuest-Modular-DDD |
| 2026-03-29 22:11 | context7.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upstash/context7.git |
| 2026-03-29 22:11 | eventsourcing | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/johnbywater/eventsourcing |
| 2026-03-29 22:12 | event-source-cqrs-sample | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ddd-by-examples/event-source-cqrs-sample |
| 2026-03-29 22:12 | Merp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mastreeno/Merp |
| 2026-03-29 22:12 | dvc | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/treeverse/dvc |
| 2026-03-29 22:12 | mlx-lm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ml-explore/mlx-lm |
| 2026-03-29 22:12 | langgraph | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/langchain-ai/langgraph |
| 2026-03-29 22:12 | vale | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/errata-ai/vale |
| 2026-03-29 22:12 | xan | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/medialab/xan |
| 2026-03-29 22:12 | nlayerappv3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cesarcastrocuba/nlayerappv3 |
| 2026-03-29 22:12 | agent-sandbox | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kubernetes-sigs/agent-sandbox |
| 2026-03-29 22:12 | jsxer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AngeloD2022/jsxer |
| 2026-03-29 22:13 | GARbro | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/morkt/GARbro |
| 2026-03-29 22:13 | deer-flow | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bytedance/deer-flow |
| 2026-03-29 22:13 | lenis | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/darkroomengineering/lenis |
| 2026-03-29 22:13 | WorldVQA | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MoonshotAI/WorldVQA |
| 2026-03-29 22:13 | End-to-End-Airbnb-Price-Prediction | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanMurapaka45/End-to-End-Airbnb-Price-Prediction |
| 2026-03-29 22:13 | test_keys | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/trufflesecurity/test_keys |
| 2026-03-29 22:13 | whatlang-rs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/greyblake/whatlang-rs |
| 2026-03-29 22:14 | phlare | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grafana/phlare |
| 2026-03-29 22:14 | ai-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sanjay3290/ai-skills |
| 2026-03-29 22:14 | mq-edit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-edit |
| 2026-03-29 22:14 | Antigravity-Manager | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lbjlaq/Antigravity-Manager |
| 2026-03-29 22:14 | distil-text2sql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/distil-labs/distil-text2sql |
| 2026-03-29 22:14 | kimi-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MoonshotAI/kimi-cli |
| 2026-03-29 22:14 | contextio | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dolmen-go/contextio |
| 2026-03-29 22:14 | hyphen | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ytiurin/hyphen |
| 2026-03-29 22:15 | voicebox.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jamiepine/voicebox.git |
| 2026-03-29 22:15 | go-strftime | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ncruces/go-strftime |
| 2026-03-29 22:15 | DeepSpeed | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/microsoft/DeepSpeed |
| 2026-03-29 22:15 | opentelemetry-ebpf-profiler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-telemetry/opentelemetry-ebpf-profiler |
| 2026-03-29 22:15 | tree-sitter-elixir | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/elixir-lang/tree-sitter-elixir |
| 2026-03-29 22:15 | RL4LMs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/allenai/RL4LMs |
| 2026-03-29 22:15 | gitleaks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gitleaks/gitleaks |
| 2026-03-29 22:15 | fifomu | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neilotoole/fifomu |
| 2026-03-29 22:15 | bmad-builder | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bmad-code-org/bmad-builder |
| 2026-03-29 22:15 | TikTokDownloader | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JoeanAmier/TikTokDownloader |
| 2026-03-29 22:15 | gitagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-gitagent/gitagent |
| 2026-03-29 22:16 | sq | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neilotoole/sq |
| 2026-03-29 22:16 | adv-es-cqrs-ddd | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sebastianharko/adv-es-cqrs-ddd |
| 2026-03-29 22:16 | demo-2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/codedspaces/demo-2 |
| 2026-03-29 22:16 | ragflow | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/infiniflow/ragflow |
| 2026-03-29 22:16 | varlock-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wrsmith108/varlock-claude-skill |
| 2026-03-29 22:16 | hyperspace-db | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/YARlabs/hyperspace-db |
| 2026-03-29 22:16 | tantivy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/quickwit-oss/tantivy |
| 2026-03-29 22:16 | zsh-syntax-highlighting.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zsh-users/zsh-syntax-highlighting.git |
| 2026-03-29 22:16 | metube | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/alexta69/metube |
| 2026-03-30 11:00 | Claude-Usage-Checker.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/0xAstroAlpha/Claude-Usage-Checker.git |
| 2026-03-30 11:00 | agentops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AgentOps-AI/agentops |
| 2026-03-30 11:00 | claude-seo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AgriciDaniel/claude-seo |
| 2026-03-30 11:00 | llmfit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlexsJones/llmfit |
| 2026-03-30 11:00 | BSA_Browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AlexxEG/BSA_Browser |
| 2026-03-30 11:00 | pragmastat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AndreyAkinshin/pragmastat |
| 2026-03-30 11:00 | Auto-Claude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AndyMik90/Auto-Claude |
| 2026-03-30 11:00 | phoenix | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Arize-ai/phoenix |
| 2026-03-30 11:00 | kore-memory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Auriti-Labs/kore-memory |
| 2026-03-30 11:00 | SwiftUI-Agent-Skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/AvdLee/SwiftUI-Agent-Skill |
| 2026-03-30 11:00 | VibeSec-Skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BehiSecc/VibeSec-Skill |
| 2026-03-30 11:00 | ClawRouter | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BlockRunAI/ClawRouter |
| 2026-03-30 11:00 | ai-marketing-claude-code-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BrianRWagner/ai-marketing-claude-code-skills |
| 2026-03-30 11:00 | ai-marketing-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BrianRWagner/ai-marketing-skills |
| 2026-03-30 11:00 | chainlit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Chainlit/chainlit |
| 2026-03-30 11:00 | chrome-devtools-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ClickHouse/agent-skills |
| 2026-03-30 11:00 | claude-workflow-v2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/claude-workflow-v2 |
| 2026-03-30 11:00 | claude-workflow-v2.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/claude-workflow-v2.git |
| 2026-03-30 11:00 | threejs-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/CloudAI-X/threejs-skills |
| 2026-03-30 11:00 | agent-orchestrator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/agent-orchestrator |
| 2026-03-30 11:00 | open-claude-cowork | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/open-claude-cowork |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ComposioHQ/skills |
| 2026-03-30 11:00 | notebooklm_source_automation | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DataNath/notebooklm_source_automation |
| 2026-03-30 11:00 | deepteam | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/DeepTeamAI/deepteam |
| 2026-03-30 11:00 | charlie-cfo-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/EveryInc/charlie-cfo-skill |
| 2026-03-30 11:00 | QueryWeaver | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FalkorDB/QueryWeaver |
| 2026-03-30 11:00 | QueryWeaver.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FalkorDB/QueryWeaver.git |
| 2026-03-30 11:00 | claude-code-ultimate-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FlorianBruniaux/claude-code-ultimate-guide |
| 2026-03-30 11:00 | agent-skill-creator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/FrancyJGLisboa/agent-skill-creator |
| 2026-03-30 11:00 | agent-teams-lite | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Gentleman-Programming/agent-teams-lite |
| 2026-03-30 11:00 | giskard | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Giskard-AI/giskard |
| 2026-03-30 11:00 | giskard-oss | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Giskard-AI/giskard-oss |
| 2026-03-30 11:00 | Local-NotebookLM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Goekdeniz-Guelmez/Local-NotebookLM |
| 2026-03-30 11:00 | generative-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/GoogleCloudPlatform/generative-ai |
| 2026-03-30 11:00 | .github | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/.github |
| 2026-03-30 11:00 | ClawTeam | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/ClawTeam |
| 2026-03-30 11:00 | ClawWork.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/ClawWork.git |
| 2026-03-30 11:00 | FastCode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/FastCode |
| 2026-03-30 11:00 | nanobot.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HKUDS/nanobot.git |
| 2026-03-30 11:00 | materials-simulation-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeshamFS/materials-simulation-skills |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeyVincent-ai/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/HeyVincent-ai/agent-skills.git |
| 2026-03-30 11:00 | claude_skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Jamie-BitFlight/claude_skills |
| 2026-03-30 11:00 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Jeffallan/claude-skills |
| 2026-03-30 11:00 | baoyu-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JimLiu/baoyu-skills |
| 2026-03-30 11:00 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Joannis/claude-skills |
| 2026-03-30 11:00 | clawport-ui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/JohnRiceML/clawport-ui |
| 2026-03-30 11:00 | Gemini-ChatBot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Gemini-ChatBot |
| 2026-03-30 11:00 | Getting-Started-with-Gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanM45/Getting-Started-with-Gemini |
| 2026-03-30 11:00 | Gemini-ChatBot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Gemini-ChatBot |
| 2026-03-30 11:00 | Getting-Started-with-Gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/KalyanMurapaka45/Getting-Started-with-Gemini |
| 2026-03-30 11:00 | kilocode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Kilo-Org/kilocode |
| 2026-03-30 11:00 | taste-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Leonxlnx/taste-skill |
| 2026-03-30 11:00 | maxclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lichas/maxclaw |
| 2026-03-30 11:00 | MiniMax-M1 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-M1 |
| 2026-03-30 11:00 | MiniMax-M2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/MiniMax-AI/MiniMax-M2 |
| 2026-03-30 11:00 | lightllm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ModelTC/lightllm |
| 2026-03-30 11:00 | auto-accept-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Munkhin/auto-accept-agent |
| 2026-03-30 11:00 | Guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA-NeMo/Guardrails |
| 2026-03-30 11:00 | NeMo-Guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/NeMo-Guardrails |
| 2026-03-30 11:00 | NemoClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/NemoClaw |
| 2026-03-30 11:00 | TensorRT-LLM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/TensorRT-LLM |
| 2026-03-30 11:00 | garak | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/garak |
| 2026-03-30 11:00 | nvidia-docker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NVIDIA/nvidia-docker |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NoizAI/skills |
| 2026-03-30 11:00 | claude-win11-speckit-update-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NotMyself/claude-win11-speckit-update-skill |
| 2026-03-30 11:00 | hermes-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NousResearch/hermes-agent |
| 2026-03-30 11:00 | tulip | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenAttackDefenseTools/tulip |
| 2026-03-30 11:00 | ai-sdk-provider | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenRouterTeam/ai-sdk-provider |
| 2026-03-30 11:00 | AI-Research-SKILLs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Orchestra-Research/AI-Research-SKILLs |
| 2026-03-30 11:00 | AI-research-SKILLs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Orchestra-Research/AI-research-SKILLs |
| 2026-03-30 11:00 | nutrient-agent-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PSPDFKit-labs/nutrient-agent-skill |
| 2026-03-30 11:00 | ResumeSkills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Paramchoudhary/ResumeSkills |
| 2026-03-30 11:00 | claude-code-system-prompts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Piebald-AI/claude-code-system-prompts |
| 2026-03-30 11:00 | posthog | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PostHog/posthog |
| 2026-03-30 11:00 | Qwen | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen |
| 2026-03-30 11:00 | Qwen-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen-Agent |
| 2026-03-30 11:00 | Qwen-Agent.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen-Agent.git |
| 2026-03-30 11:00 | Qwen2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen2 |
| 2026-03-30 11:00 | Qwen2.5-Omni | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen2.5-Omni |
| 2026-03-30 11:00 | Qwen3 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3 |
| 2026-03-30 11:00 | Qwen3-ASR | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-ASR |
| 2026-03-30 11:00 | Qwen3-ASR.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-ASR.git |
| 2026-03-30 11:00 | Qwen3-TTS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-TTS |
| 2026-03-30 11:00 | Qwen3-TTS.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/Qwen3-TTS.git |
| 2026-03-30 11:00 | qwen-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/QwenLM/qwen-code |
| 2026-03-30 11:00 | FlashRAG | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RUC-NLPIR/FlashRAG |
| 2026-03-30 11:00 | opc-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ReScienceLab/opc-skills |
| 2026-03-30 11:00 | Rootly-MCP-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rootly-AI-Labs/Rootly-MCP-server |
| 2026-03-30 11:00 | rootly-mcp-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rootly-AI-Labs/rootly-mcp-server |
| 2026-03-30 11:00 | tutor-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RoundTable02/tutor-skills |
| 2026-03-30 11:00 | metube-browser-extension | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rpsl/metube-browser-extension |
| 2026-03-30 11:00 | dev-browser | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SawyerHood/dev-browser |
| 2026-03-30 11:00 | dev-browser.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SawyerHood/dev-browser.git |
| 2026-03-30 11:00 | Scrapegraph-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ScrapeGraphAI/Scrapegraph-ai |
| 2026-03-30 11:00 | claude-speed-reader | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/SeanZoR/claude-speed-reader |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Shpigford/skills |
| 2026-03-30 11:00 | guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ShreyaR/guardrails |
| 2026-03-30 11:00 | skyvern | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Skyvern-AI/skyvern |
| 2026-03-30 11:00 | pyragify | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ThomasBury/pyragify |
| 2026-03-30 11:00 | tinyclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TinyAGI/tinyclaw |
| 2026-03-30 11:00 | SuperAGI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TransformerOptimus/SuperAGI |
| 2026-03-30 11:00 | agency-swarm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VRSEN/agency-swarm |
| 2026-03-30 11:00 | ClawX | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ValueCell-ai/ClawX |
| 2026-03-30 11:00 | Scrapegraph-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VinciGit00/Scrapegraph-ai |
| 2026-03-30 11:00 | awesome-ai-agent-papers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/awesome-ai-agent-papers |
| 2026-03-30 11:00 | awesome-openclaw-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/awesome-openclaw-skills |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/skills |
| 2026-03-30 11:00 | voltagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/VoltAgent/voltagent |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/WordPress/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/WordPress/agent-skills.git |
| 2026-03-30 11:00 | x-twitter-scraper | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Xquik-dev/x-twitter-scraper |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ZackKorman/skills |
| 2026-03-30 11:00 | Antigravity-Skills-Chronicle | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Zaious/Antigravity-Skills-Chronicle |
| 2026-03-30 11:00 | makepad-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ZhangHanDong/makepad-skills |
| 2026-03-30 11:00 | web-quality-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/addyosmani/web-quality-skills |
| 2026-03-30 11:00 | web-quality-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/addyosmani/web-quality-skills.git |
| 2026-03-30 11:00 | manim_skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adithya-s-k/manim_skill |
| 2026-03-30 11:00 | manim_skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/adithya-s-k/manim_skill.git |
| 2026-03-30 11:00 | everything-claude-code.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/affaan-m/everything-claude-code.git |
| 2026-03-30 11:00 | agentscope | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agentscope-ai/agentscope |
| 2026-03-30 11:00 | agentskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agentskills/agentskills |
| 2026-03-30 11:00 | agno | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/agno-ai/agno |
| 2026-03-30 11:00 | MetaClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/aiming-lab/MetaClaw |
| 2026-03-30 11:00 | claude-bootstrap | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/alinaqi/claude-bootstrap |
| 2026-03-30 11:00 | clearml | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/allegroai/clearml |
| 2026-03-30 11:00 | angular-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/analogjs/angular-skills |
| 2026-03-30 11:00 | angular-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/analogjs/angular-skills.git |
| 2026-03-30 11:00 | opencode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anomalyco/opencode |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/antfu/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/antfu/skills.git |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/agent-skills |
| 2026-03-30 11:00 | claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code |
| 2026-03-30 11:00 | claude-code-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code-action |
| 2026-03-30 11:00 | claude-cookbooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-cookbooks |
| 2026-03-30 11:00 | courses | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/courses |
| 2026-03-30 11:00 | hindsight-cookbook | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/hindsight-cookbook |
| 2026-03-30 11:00 | hindsight.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/hindsight.git |
| 2026-03-30 11:00 | mcpb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/mcpb |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/skills.git |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/apify/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/apify/agent-skills.git |
| 2026-03-30 11:00 | stitchSkill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/arinnem/stitchSkill |
| 2026-03-30 11:00 | kore-memory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/auriti-web-design/kore-memory |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/better-auth/skills |
| 2026-03-30 11:00 | binance-skills-hub | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/binance/binance-skills-hub |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boristane/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/boristane/agent-skills.git |
| 2026-03-30 11:00 | agent-config | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/agent-config |
| 2026-03-30 11:00 | claude-config | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/claude-config |
| 2026-03-30 11:00 | claude-config.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/claude-config.git |
| 2026-03-30 11:00 | browser-use.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/browser-use/browser-use.git |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/callstackincubator/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/callstackincubator/agent-skills.git |
| 2026-03-30 11:00 | camel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/camel |
| 2026-03-30 11:00 | oasis | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/oasis |
| 2026-03-30 11:00 | free-llm-api-resources | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cheahjs/free-llm-api-resources |
| 2026-03-30 11:00 | fast-graphrag | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/circlemind-ai/fast-graphrag |
| 2026-03-30 11:00 | clawdata | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/clawdata/clawdata |
| 2026-03-30 11:00 | threejs-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudai-x/threejs-skills.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudflare/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudflare/skills.git |
| 2026-03-30 11:00 | deepeval | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/confident-ai/deepeval |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/copilot/skills |
| 2026-03-30 11:00 | marketingskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coreyhaines31/marketingskills |
| 2026-03-30 11:00 | marketingskills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coreyhaines31/marketingskills.git |
| 2026-03-30 11:00 | us-census-bureau-data-api-mcp.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/us-census-bureau-data-api-mcp.git |
| 2026-03-30 11:00 | dbt-agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dbt-labs/dbt-agent-skills.git |
| 2026-03-30 11:00 | Product-Manager-Skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deanpeters/Product-Manager-Skills |
| 2026-03-30 11:00 | haystack | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deepset-ai/haystack |
| 2026-03-30 11:00 | webgpu-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dgreenheck/webgpu-claude-skill |
| 2026-03-30 11:00 | webgpu-claude-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dgreenheck/webgpu-claude-skill.git |
| 2026-03-30 11:00 | cloudflare-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dmmulroy/cloudflare-skill |
| 2026-03-30 11:00 | outlines | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dottxt-ai/outlines |
| 2026-03-30 11:00 | code-interpreter | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/e2b-dev/code-interpreter |
| 2026-03-30 11:00 | platform-design-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ehmo/platform-design-skills |
| 2026-03-30 11:00 | awesome-notebooklm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/etewiah/awesome-notebooklm |
| 2026-03-30 11:00 | ragas | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/explodinggradients/ragas |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/expo/skills |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/fal-ai-community/skills |
| 2026-03-30 11:00 | claude-code-settings | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/feiskyer/claude-code-settings |
| 2026-03-30 11:00 | mcp-server-guide.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/figma/mcp-server-guide.git |
| 2026-03-30 11:00 | cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/cli |
| 2026-03-30 11:00 | cli.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/cli.git |
| 2026-03-30 11:00 | create-llmstxt-py | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/create-llmstxt-py |
| 2026-03-30 11:00 | firesearch | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/firesearch |
| 2026-03-30 11:00 | open-lovable.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/open-lovable.git |
| 2026-03-30 11:00 | open-researcher | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/open-researcher |
| 2026-03-30 11:00 | andrej-karpathy-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forrestchang/andrej-karpathy-skills |
| 2026-03-30 11:00 | andrej-karpathy-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forrestchang/andrej-karpathy-skills.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/getsentry/skills |
| 2026-03-30 11:00 | agenttrafficcontrol | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gkamradt/agenttrafficcontrol |
| 2026-03-30 11:00 | My-Brain-Is-Full-Crew | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gnekt/My-Brain-Is-Full-Crew |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gokapso/agent-skills |
| 2026-03-30 11:00 | gemini-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-gemini/gemini-skills |
| 2026-03-30 11:00 | stitch-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-labs-code/stitch-skills.git |
| 2026-03-30 11:00 | gemini-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google/gemini-cli |
| 2026-03-30 11:00 | guardrails | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/guardrails-ai/guardrails |
| 2026-03-30 11:00 | claude-memory-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hanfang/claude-memory-skill |
| 2026-03-30 11:00 | mq-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-mcp |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hashicorp/agent-skills |
| 2026-03-30 11:00 | awesome-claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hesreallyhim/awesome-claude-code |
| 2026-03-30 11:00 | lighteval | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/lighteval |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/skills.git |
| 2026-03-30 11:00 | smolagents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huggingface/smolagents |
| 2026-03-30 11:00 | Claude-Ally-Health | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huifer/Claude-Ally-Health |
| 2026-03-30 11:00 | advanced-context-engineering-for-coding-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents |
| 2026-03-30 11:00 | ui-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ibelick/ui-skills.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/inference-sh/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/inference-sh/skills.git |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/intellectronica/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/intellectronica/agent-skills.git |
| 2026-03-30 11:00 | aws-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/itsmostafa/aws-agent-skills |
| 2026-03-30 11:00 | notebooklm-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jacob-bd/notebooklm-cli |
| 2026-03-30 11:00 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jeffallan/claude-skills |
| 2026-03-30 11:00 | claude-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jeffallan/claude-skills.git |
| 2026-03-30 11:00 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jezweb/claude-skills |
| 2026-03-30 11:00 | claude-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jezweb/claude-skills.git |
| 2026-03-30 11:00 | pixl-server-storage | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-storage |
| 2026-03-30 11:00 | baoyu-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jimliu/baoyu-skills |
| 2026-03-30 11:00 | awesome-claude-code | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jmanhype/awesome-claude-code |
| 2026-03-30 11:00 | ffuf_claude_skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jthack/ffuf_claude_skill |
| 2026-03-30 11:00 | claude-inspector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kangraemin/claude-inspector |
| 2026-03-30 11:00 | obsidian-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kepano/obsidian-skills |
| 2026-03-30 11:00 | spawn-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/khanhbkqt/spawn-agent |
| 2026-03-30 11:00 | claude-skill-homeassistant | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/komal-SkyNET/claude-skill-homeassistant |
| 2026-03-30 11:00 | swarms | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kyegomez/swarms |
| 2026-03-30 11:00 | playwright-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lackeyjb/playwright-skill.git |
| 2026-03-30 11:00 | awesome-legal-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lawvable/awesome-legal-skills |
| 2026-03-30 11:00 | claude-subconscious | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/letta-ai/claude-subconscious |
| 2026-03-30 11:00 | llm-lean-log | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/loclv/llm-lean-log |
| 2026-03-30 11:00 | openclaw-worker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/longtho638-jpg/openclaw-worker |
| 2026-03-30 11:00 | claude-code-ultimate-guide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/marketingjuliancongdanh79-pixel/claude-code-ultimate-guide |
| 2026-03-30 11:00 | recursive-decomposition-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/massimodeluisa/recursive-decomposition-skill |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mcollina/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mcollina/skills.git |
| 2026-03-30 11:00 | personal-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/me/personal-skills |
| 2026-03-30 11:00 | personal-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/me/personal-skills.git |
| 2026-03-30 11:00 | firecrawl-mcp-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mendableai/firecrawl-mcp-server |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/agent-skills.git |
| 2026-03-30 11:00 | multi-agent-systems | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/multi-agent-systems |
| 2026-03-30 11:00 | playwright-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/playwright-mcp |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/skills |
| 2026-03-30 11:00 | llm-course | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlabonne/llm-course |
| 2026-03-30 11:00 | web-llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlc-ai/web-llm |
| 2026-03-30 11:00 | mcpb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/mcpb |
| 2026-03-30 11:00 | Agent-Skills-for-Context-Engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering |
| 2026-03-30 11:00 | claude-code-production-grade-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-production-grade-plugin |
| 2026-03-30 11:00 | claude-code-production-grade-plugin.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-production-grade-plugin.git |
| 2026-03-30 11:00 | skyclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/skyclaw |
| 2026-03-30 11:00 | clawdirect | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/napoleond/clawdirect |
| 2026-03-30 11:00 | clawdirect.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/napoleond/clawdirect.git |
| 2026-03-30 11:00 | ironclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nearai/ironclaw |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/neondatabase/agent-skills |
| 2026-03-30 11:00 | ui-ux-pro-max-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| 2026-03-30 11:00 | firecrawl-openai-realtime | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nickscamara/firecrawl-openai-realtime |
| 2026-03-30 11:00 | claude-code-in-chrome-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nicobailon/claude-code-in-chrome-mcp |
| 2026-03-30 11:00 | hermes-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nousresearch/hermes-agent |
| 2026-03-30 11:00 | nullclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nullclaw/nullclaw |
| 2026-03-30 11:00 | opencode-openai-codex-auth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/numman-ali/opencode-openai-codex-auth |
| 2026-03-30 11:00 | opencode-openai-codex-auth.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/numman-ali/opencode-openai-codex-auth.git |
| 2026-03-30 11:00 | graphql.js | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/octokit/graphql.js |
| 2026-03-30 11:00 | founder-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ognjengt/founder-skills |
| 2026-03-30 11:00 | nuxt-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/onmax/nuxt-skills |
| 2026-03-30 11:00 | Youtube-clipper-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/op7418/Youtube-clipper-skill |
| 2026-03-30 11:00 | evals | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/evals |
| 2026-03-30 11:00 | openai-cookbook | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/openai-cookbook |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/skills |
| 2026-03-30 11:00 | pixel-agents.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pablodelucca/pixel-agents.git |
| 2026-03-30 11:00 | pgvector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pgvector/pgvector |
| 2026-03-30 11:00 | WikidataMCP | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/philippesaade-wmde/WikidataMCP |
| 2026-03-30 11:00 | pm-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/phuryn/pm-skills |
| 2026-03-30 11:00 | poco-claw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/poco-ai/poco-claw |
| 2026-03-30 11:00 | posthog | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/posthog/posthog |
| 2026-03-30 11:00 | clawsec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/prompt-security/clawsec |
| 2026-03-30 11:00 | PUAClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/puaclaw/PUAClaw |
| 2026-03-30 11:00 | nanoclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/qwibitai/nanoclaw |
| 2026-03-30 11:00 | claude-code-startup-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rameerez/claude-code-startup-skills |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/remotion-dev/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/remotion-dev/skills.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/replicate/skills |
| 2026-03-30 11:00 | skill-rails-upgrade | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/robzolkos/skill-rails-upgrade |
| 2026-03-30 11:00 | routeLLM | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/routeLLM/routeLLM |
| 2026-03-30 11:00 | app-store-connect-cli-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rudrankriyam/app-store-connect-cli-skills |
| 2026-03-30 11:00 | agent-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sanity-io/agent-toolkit |
| 2026-03-30 11:00 | claude-code-codex-cursor-gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-codex-cursor-gemini |
| 2026-03-30 11:00 | claude-code-hooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-hooks |
| 2026-03-30 11:00 | claude-code-status-line | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-status-line |
| 2026-03-30 11:00 | claude-code-voice-hooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-voice-hooks |
| 2026-03-30 11:00 | novel-llm-26 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/novel-llm-26 |
| 2026-03-30 11:00 | Kode-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode-Agent |
| 2026-03-30 11:00 | kode-agent-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/kode-agent-sdk |
| 2026-03-30 11:00 | shareAI-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/shareAI-skills |
| 2026-03-30 11:00 | antigravity-awesome-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sickn33/antigravity-awesome-skills.git |
| 2026-03-30 11:00 | claude-code-transcripts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonw/claude-code-transcripts |
| 2026-03-30 11:00 | llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonw/llm |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonwong/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonwong/agent-skills.git |
| 2026-03-30 11:00 | picoclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sipeed/picoclaw |
| 2026-03-30 11:00 | skillhub-desktop | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/skillhub-club/skillhub-desktop |
| 2026-03-30 11:00 | creative-director-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/smixs/creative-director-skill |
| 2026-03-30 11:00 | agent-scan | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/snyk/agent-scan |
| 2026-03-30 11:00 | agent-toolkit.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/softaworks/agent-toolkit.git |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/supabase/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/supabase/agent-skills.git |
| 2026-03-30 11:00 | superdesign-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/superdesigndev/superdesign-skill |
| 2026-03-30 11:00 | superdesign-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/superdesigndev/superdesign-skill.git |
| 2026-03-30 11:00 | claude-ecom | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/takechanman1228/claude-ecom |
| 2026-03-30 11:00 | notebooklm-py | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/teng-lin/notebooklm-py |
| 2026-03-30 11:00 | test-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/test-org/test-skills |
| 2026-03-30 11:00 | playwright-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/testdino-hq/playwright-skill |
| 2026-03-30 11:00 | pgvectorscale | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/timescale/pgvectorscale |
| 2026-03-30 11:00 | tinybird-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinybirdco/tinybird-agent-skills |
| 2026-03-30 11:00 | open-claude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tkattkat/open-claude |
| 2026-03-30 11:00 | open-claude.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tkattkat/open-claude.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/trailofbits/skills |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/transloadit/skills |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/typefully/agent-skills |
| 2026-03-30 11:00 | notebooklm-podcast-automator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upamune/notebooklm-podcast-automator |
| 2026-03-30 11:00 | us-census-bureau-data-api-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/uscensusbureau/us-census-bureau-data-api-mcp |
| 2026-03-30 11:00 | skill-repo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/user/skill-repo |
| 2026-03-30 11:00 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/agent-skills |
| 2026-03-30 11:00 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/agent-skills.git |
| 2026-03-30 11:00 | next-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/next-skills.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/skills.git |
| 2026-03-30 11:00 | ragas | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vibrantlabsai/ragas |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/video-db/skills |
| 2026-03-30 11:00 | superagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/visionmedia/superagent |
| 2026-03-30 11:00 | vllm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vllm-project/vllm |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vuejs-ai/skills |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vueuse/skills |
| 2026-03-30 11:00 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vueuse/skills.git |
| 2026-03-30 11:00 | pentagi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vxcontrol/pentagi |
| 2026-03-30 11:00 | skillsentry | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vythanhtra/skillsentry |
| 2026-03-30 11:00 | Auto-claude-code-research-in-sleep | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep |
| 2026-03-30 11:00 | convexskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/waynesutton/convexskills |
| 2026-03-30 11:00 | convexskills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/waynesutton/convexskills.git |
| 2026-03-30 11:00 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wendylabsinc/claude-skills |
| 2026-03-30 11:00 | WikidataMCP | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wmde/WikidataMCP |
| 2026-03-30 11:00 | agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wshobson/agents |
| 2026-03-30 11:00 | x-article-publisher-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wshuyi/x-article-publisher-skill |
| 2026-03-30 11:00 | all-agentic-architectures.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/your-username/all-agentic-architectures.git |
| 2026-03-30 11:00 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zackkorman/skills |
| 2026-03-30 11:00 | AI-research-SKILLs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zechenzhangAGI/AI-research-SKILLs |
| 2026-03-30 11:00 | claude-context | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zilliztech/claude-context |
| 2026-03-30 11:00 | aws-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zxkane/aws-skills |
| 2026-03-30 13:12 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/antfu/skills |
| 2026-03-30 13:12 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/antfu/skills.git |
| 2026-03-30 13:12 | agent-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/agent-skills |
| 2026-03-30 13:12 | claude-code-action | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/claude-code-action |
| 2026-03-30 13:12 | claude-code.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/claude-code.git |
| 2026-03-30 13:12 | claude-plugins-official | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/claude-plugins-official |
| 2026-03-30 13:12 | courses | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/courses |
| 2026-03-30 13:12 | dxt | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/dxt |
| 2026-03-30 13:12 | hindsight.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/hindsight.git |
| 2026-03-30 13:12 | mcpb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/mcpb |
| 2026-03-30 13:12 | prompt-eng-interactive-tutorial | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/prompt-eng-interactive-tutorial |
| 2026-03-30 13:12 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/anthropics/skills |
| 2026-03-30 13:12 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/anthropics/skills.git |
| 2026-03-30 13:12 | terraform-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/antonbabenko/terraform-skill |
| 2026-03-30 13:12 | excalidraw-mcp-app | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/antonpk1/excalidraw-mcp-app |
| 2026-03-30 13:12 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/apify/agent-skills.git |
| 2026-03-30 13:12 | stitchSkill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/arinnem/stitchSkill |
| 2026-03-30 13:12 | LLM-Finetuning | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ashishpatel26/LLM-Finetuning |
| 2026-03-30 13:12 | kore-memory | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/auriti-web-design/kore-memory |
| 2026-03-30 13:12 | binance-skills-hub | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/binance/binance-skills-hub |
| 2026-03-30 13:12 | agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/boristane/agent-skills.git |
| 2026-03-30 13:12 | agent-config | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/agent-config |
| 2026-03-30 13:12 | claude-config | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/claude-config |
| 2026-03-30 13:12 | claude-config.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/brianlovin/claude-config.git |
| 2026-03-30 13:12 | browser-use | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/browser-use/browser-use |
| 2026-03-30 13:12 | browser-use.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/browser-use/browser-use.git |
| 2026-03-30 13:12 | agent-os | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/buildermethods/agent-os |
| 2026-03-30 13:12 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/callstackincubator/agent-skills.git |
| 2026-03-30 13:13 | camel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/camel |
| 2026-03-30 13:13 | oasis | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/camel-ai/oasis |
| 2026-03-30 13:13 | free-llm-api-resources | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cheahjs/free-llm-api-resources |
| 2026-03-30 13:13 | fast-graphrag | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/circlemind-ai/fast-graphrag |
| 2026-03-30 13:13 | clawdata | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/clawdata/clawdata |
| 2026-03-30 13:13 | threejs-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudai-x/threejs-skills.git |
| 2026-03-30 13:13 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudflare/skills.git |
| 2026-03-30 13:13 | opik | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/comet-ml/opik |
| 2026-03-30 13:13 | deepeval | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/confident-ai/deepeval |
| 2026-03-30 13:13 | ios-simulator-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/conorluddy/ios-simulator-skill |
| 2026-03-30 13:13 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/copilot/skills |
| 2026-03-30 13:14 | marketingskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coreyhaines31/marketingskills |
| 2026-03-30 13:14 | marketingskills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coreyhaines31/marketingskills.git |
| 2026-03-30 13:14 | n8n-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/czlonkowski/n8n-skills |
| 2026-03-30 13:14 | us-census-bureau-data-api-mcp | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dathere/us-census-bureau-data-api-mcp |
| 2026-03-30 13:14 | us-census-bureau-data-api-mcp.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dathere/us-census-bureau-data-api-mcp.git |
| 2026-03-30 13:14 | dbt-agent-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dbt-labs/dbt-agent-skills |
| 2026-03-30 13:14 | dbt-agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dbt-labs/dbt-agent-skills.git |
| 2026-03-30 13:14 | Product-Manager-Skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deanpeters/Product-Manager-Skills |
| 2026-03-30 13:14 | webgpu-claude-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dgreenheck/webgpu-claude-skill |
| 2026-03-30 13:14 | webgpu-claude-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dgreenheck/webgpu-claude-skill.git |
| 2026-03-30 13:14 | cloudflare-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dmmulroy/cloudflare-skill |
| 2026-03-30 13:14 | outlines | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dottxt-ai/outlines |
| 2026-03-30 13:14 | univer-mcp | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dream-num/univer-mcp |
| 2026-03-30 13:14 | agent-teams | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dsclca12/agent-teams |
| 2026-03-30 13:14 | code-interpreter | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/e2b-dev/code-interpreter |
| 2026-03-30 13:14 | swift-patterns-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/efremidze/swift-patterns-skill |
| 2026-03-30 13:14 | platform-design-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ehmo/platform-design-skills |
| 2026-03-30 13:14 | claude-openclaw-bridge | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ericblue/claude-openclaw-bridge |
| 2026-03-30 13:14 | awesome-notebooklm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/etewiah/awesome-notebooklm |
| 2026-03-30 13:14 | excalidraw-mcp | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/excalidraw/excalidraw-mcp |
| 2026-03-30 13:14 | ragas | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/explodinggradients/ragas |
| 2026-03-30 13:14 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/expo/skills |
| 2026-03-30 13:14 | claude-code-settings | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/feiskyer/claude-code-settings |
| 2026-03-30 13:14 | mcp-server-guide | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/figma/mcp-server-guide |
| 2026-03-30 13:14 | mcp-server-guide.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/figma/mcp-server-guide.git |
| 2026-03-30 13:14 | cli | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/firecrawl/cli |
| 2026-03-30 13:14 | cli.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/firecrawl/cli.git |
| 2026-03-30 13:14 | create-llmstxt-py | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/create-llmstxt-py |
| 2026-03-30 13:15 | firesearch | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/firesearch |
| 2026-03-30 13:15 | open-lovable | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/firecrawl/open-lovable |
| 2026-03-30 13:15 | open-lovable.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/open-lovable.git |
| 2026-03-30 13:15 | open-researcher | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/open-researcher |
| 2026-03-30 13:15 | andrej-karpathy-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forrestchang/andrej-karpathy-skills |
| 2026-03-30 13:15 | andrej-karpathy-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forrestchang/andrej-karpathy-skills.git |
| 2026-03-30 13:15 | superagent | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/forwardemail/superagent |
| 2026-03-30 13:15 | dev-agent-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/fvadicamo/dev-agent-skills |
| 2026-03-30 13:15 | agent-teams-lite.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gentleman-programming/agent-teams-lite.git |
| 2026-03-30 13:15 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/getsentry/skills |
| 2026-03-30 13:15 | agenttrafficcontrol | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gkamradt/agenttrafficcontrol |
| 2026-03-30 13:15 | My-Brain-Is-Full-Crew | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gnekt/My-Brain-Is-Full-Crew |
| 2026-03-30 13:15 | gemini-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-gemini/gemini-skills |
| 2026-03-30 13:15 | stitch-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/google-labs-code/stitch-skills |
| 2026-03-30 13:15 | stitch-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google-labs-code/stitch-skills.git |
| 2026-03-30 13:15 | gemini-cli | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/google/gemini-cli |
| 2026-03-30 13:15 | google-maps-scraper | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gosom/google-maps-scraper |
| 2026-03-30 13:15 | claude-memory-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hanfang/claude-memory-skill |
| 2026-03-30 13:15 | mq-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq-mcp |
| 2026-03-30 13:15 | agents-course.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/huggingface/agents-course.git |
| 2026-03-30 13:15 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/huggingface/skills.git |
| 2026-03-30 13:15 | Claude-Ally-Health | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/huifer/Claude-Ally-Health |
| 2026-03-30 13:15 | advanced-context-engineering-for-coding-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents |
| 2026-03-30 13:15 | vue-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/hyf0/vue-skills |
| 2026-03-30 13:15 | vue-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/hyf0/vue-skills.git |
| 2026-03-30 13:15 | ui-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ibelick/ui-skills |
| 2026-03-30 13:15 | ui-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ibelick/ui-skills.git |
| 2026-03-30 13:15 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/inference-sh/skills |
| 2026-03-30 13:15 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/inference-sh/skills.git |
| 2026-03-30 13:15 | agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/intellectronica/agent-skills.git |
| 2026-03-30 13:15 | aws-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/itsmostafa/aws-agent-skills |
| 2026-03-30 13:15 | aws-agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/itsmostafa/aws-agent-skills.git |
| 2026-03-30 13:15 | notebooklm-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jacob-bd/notebooklm-cli |
| 2026-03-30 13:15 | notebooklm-mcp | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jacob-bd/notebooklm-mcp |
| 2026-03-30 13:15 | claude-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jeffallan/claude-skills |
| 2026-03-30 13:15 | claude-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jeffallan/claude-skills.git |
| 2026-03-30 13:15 | claude-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jezweb/claude-skills.git |
| 2026-03-30 13:15 | pixl-server-storage | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-storage |
| 2026-03-30 13:15 | baoyu-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jimliu/baoyu-skills |
| 2026-03-30 13:15 | baoyu-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jimliu/baoyu-skills.git |
| 2026-03-30 13:15 | awesome-claude-code | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jmanhype/awesome-claude-code |
| 2026-03-30 13:15 | agency-agents-zh | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jnMetaCode/agency-agents-zh |
| 2026-03-30 13:16 | crewAI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/joaomdmoura/crewAI |
| 2026-03-30 13:16 | openclaw-command-center | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jontsai/openclaw-command-center |
| 2026-03-30 13:16 | ffuf_claude_skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jthack/ffuf_claude_skill |
| 2026-03-30 13:16 | claude-inspector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kangraemin/claude-inspector |
| 2026-03-30 13:16 | obsidian-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kepano/obsidian-skills |
| 2026-03-30 13:16 | obsidian-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/kepano/obsidian-skills.git |
| 2026-03-30 13:16 | spawn-agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/khanhbkqt/spawn-agent |
| 2026-03-30 13:16 | claude-skill-homeassistant | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/komal-SkyNET/claude-skill-homeassistant |
| 2026-03-30 13:16 | agent-sandbox | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/kubernetes-sigs/agent-sandbox |
| 2026-03-30 13:16 | playwright-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/lackeyjb/playwright-skill |
| 2026-03-30 13:16 | playwright-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lackeyjb/playwright-skill.git |
| 2026-03-30 13:16 | awesome-legal-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/lawvable/awesome-legal-skills |
| 2026-03-30 13:17 | claude-subconscious | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/letta-ai/claude-subconscious |
| 2026-03-30 13:17 | browser | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/lightpanda-io/browser |
| 2026-03-30 13:17 | llmware | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/llmware-ai/llmware |
| 2026-03-30 13:17 | llm-lean-log | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/loclv/llm-lean-log |
| 2026-03-30 13:17 | openclaw-worker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/longtho638-jpg/openclaw-worker |
| 2026-03-30 13:17 | skill-generator | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/marketingjuliancongdanh79-pixel/skill-generator |
| 2026-03-30 13:17 | recursive-decomposition-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/massimodeluisa/recursive-decomposition-skill |
| 2026-03-30 13:17 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/mcollina/skills |
| 2026-03-30 13:17 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/mcollina/skills.git |
| 2026-03-30 13:17 | firecrawl | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mendableai/firecrawl |
| 2026-03-30 13:17 | firecrawl-go | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/mendableai/firecrawl-go |
| 2026-03-30 13:17 | firecrawl-mcp-server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mendableai/firecrawl-mcp-server |
| 2026-03-30 13:17 | awesome-openclaw-agents | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/mergisi/awesome-openclaw-agents |
| 2026-03-30 13:17 | agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/agent-skills |
| 2026-03-30 13:17 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/agent-skills.git |
| 2026-03-30 13:17 | playwright-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/playwright-mcp |
| 2026-03-30 13:17 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/skills |
| 2026-03-30 13:17 | web-llm | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mlc-ai/web-llm |
| 2026-03-30 13:17 | mcpb | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/modelcontextprotocol/mcpb |
| 2026-03-30 13:17 | claude-apple-bridges | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/more-io/claude-apple-bridges |
| 2026-03-30 13:17 | Agent-Skills-for-Context-Engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering |
| 2026-03-30 13:17 | Agent-Skills-for-Context-Engineering.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering.git |
| 2026-03-30 13:17 | claude-code-production-grade-plugin | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-production-grade-plugin |
| 2026-03-30 13:17 | claude-code-production-grade-plugin.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/claude-code-production-grade-plugin.git |
| 2026-03-30 13:17 | claude-code-skill-maker-plugin | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nagisanzenin/claude-code-skill-maker-plugin |
| 2026-03-30 13:17 | claude-code-software-engineer-plugin | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nagisanzenin/claude-code-software-engineer-plugin |
| 2026-03-30 13:17 | skyclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nagisanzenin/skyclaw |
| 2026-03-30 13:17 | clawdirect | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/napoleond/clawdirect |
| 2026-03-30 13:17 | clawdirect.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/napoleond/clawdirect.git |
| 2026-03-30 13:18 | ironclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nearai/ironclaw |
| 2026-03-30 13:18 | goclaw | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nextlevelbuilder/goclaw |
| 2026-03-30 13:18 | ui-ux-pro-max-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| 2026-03-30 13:18 | llm-mux | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nghyane/llm-mux |
| 2026-03-30 13:18 | neural-memory | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nhadaututtheky/neural-memory |
| 2026-03-30 13:18 | firecrawl-openai-realtime | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nickscamara/firecrawl-openai-realtime |
| 2026-03-30 13:18 | hermes-agent | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nousresearch/hermes-agent |
| 2026-03-30 13:18 | nullclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nullclaw/nullclaw |
| 2026-03-30 13:18 | opencode-openai-codex-auth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/numman-ali/opencode-openai-codex-auth |
| 2026-03-30 13:18 | opencode-openai-codex-auth.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/numman-ali/opencode-openai-codex-auth.git |
| 2026-03-30 13:18 | founder-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ognjengt/founder-skills |
| 2026-03-30 13:18 | pypict-claude-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/omkamal/pypict-claude-skill |
| 2026-03-30 13:18 | nuxt-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/onmax/nuxt-skills |
| 2026-03-30 13:18 | nuxt-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/onmax/nuxt-skills.git |
| 2026-03-30 13:18 | NanoBanana-PPT-Skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/op7418/NanoBanana-PPT-Skills |
| 2026-03-30 13:18 | Youtube-clipper-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/op7418/Youtube-clipper-skill |
| 2026-03-30 13:18 | gitagent | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/open-gitagent/gitagent |
| 2026-03-30 13:18 | evals | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openai/evals |
| 2026-03-30 13:18 | openai-cookbook.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openai/openai-cookbook.git |
| 2026-03-30 13:18 | swarm.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openai/swarm.git |
| 2026-03-30 13:18 | clawhub | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openclaw/clawhub |
| 2026-03-30 13:19 | openclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/openclaw/openclaw |
| 2026-03-30 13:19 | pixel-agents | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pablodelucca/pixel-agents |
| 2026-03-30 13:19 | pixel-agents.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pablodelucca/pixel-agents.git |
| 2026-03-30 13:19 | WikidataMCP | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/philippesaade-wmde/WikidataMCP |
| 2026-03-30 13:19 | WikidataMCP.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/philippesaade-wmde/WikidataMCP.git |
| 2026-03-30 13:19 | pm-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/phuryn/pm-skills |
| 2026-03-30 13:19 | poco-claw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/poco-ai/poco-claw |
| 2026-03-30 13:19 | posthog | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/posthog/posthog |
| 2026-03-30 13:19 | posthog.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/posthog/posthog.git |
| 2026-03-30 13:19 | clawsec | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/prompt-security/clawsec |
| 2026-03-30 13:19 | PUAClaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/puaclaw/PUAClaw |
| 2026-03-30 13:19 | nanoclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/qwibitai/nanoclaw |
| 2026-03-30 13:19 | apple-hig-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/raintree-technology/apple-hig-skills |
| 2026-03-30 13:19 | claude-code-startup-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rameerez/claude-code-startup-skills |
| 2026-03-30 13:19 | iOS-Accessibility-Audit-Skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ramzesenok/iOS-Accessibility-Audit-Skill |
| 2026-03-30 13:19 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/remotion-dev/skills |
| 2026-03-30 13:19 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/remotion-dev/skills.git |
| 2026-03-30 13:19 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/replicate/skills |
| 2026-03-30 13:19 | opc-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/resciencelab/opc-skills.git |
| 2026-03-30 13:19 | skill-rails-upgrade | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/robzolkos/skill-rails-upgrade |
| 2026-03-30 13:19 | app-store-connect-cli-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rudrankriyam/app-store-connect-cli-skills |
| 2026-03-30 13:19 | agent-toolkit | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/sanity-io/agent-toolkit |
| 2026-03-30 13:19 | ai-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/sanjay3290/ai-skills |
| 2026-03-30 13:19 | awesome-notebookLM-prompts | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/serenakeyitan/awesome-notebookLM-prompts |
| 2026-03-30 13:19 | citation-check-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/serenakeyitan/citation-check-skill |
| 2026-03-30 13:19 | claude-code-codex-cursor-gemini | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-codex-cursor-gemini |
| 2026-03-30 13:19 | claude-code-hooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-hooks |
| 2026-03-30 13:19 | claude-code-status-line | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-status-line |
| 2026-03-30 13:19 | claude-code-voice-hooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/claude-code-voice-hooks |
| 2026-03-30 13:20 | novel-llm-26 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/novel-llm-26 |
| 2026-03-30 13:20 | Kode-Agent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode-Agent |
| 2026-03-30 13:20 | Kode-agent-sdk | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/shareAI-lab/Kode-agent-sdk |
| 2026-03-30 13:20 | claw0 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/shareAI-lab/claw0 |
| 2026-03-30 13:20 | kode-agent-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/kode-agent-sdk |
| 2026-03-30 13:20 | shareAI-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/shareAI-skills |
| 2026-03-30 13:20 | antigravity-awesome-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/sickn33/antigravity-awesome-skills |
| 2026-03-30 13:22 | antigravity-awesome-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sickn33/antigravity-awesome-skills.git |
| 2026-03-30 13:22 | claude-code-transcripts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/simonw/claude-code-transcripts |
| 2026-03-30 13:22 | agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/simonwong/agent-skills.git |
| 2026-03-30 13:22 | picoclaw | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sipeed/picoclaw |
| 2026-03-30 13:22 | skillhub-desktop | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/skillhub-club/skillhub-desktop |
| 2026-03-30 13:22 | creative-director-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/smixs/creative-director-skill |
| 2026-03-30 13:22 | agent-scan | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/snyk/agent-scan |
| 2026-03-30 13:22 | agent-toolkit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/softaworks/agent-toolkit |
| 2026-03-30 13:22 | agent-toolkit.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/softaworks/agent-toolkit.git |
| 2026-03-30 13:22 | agent-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/supabase/agent-skills.git |
| 2026-03-30 13:22 | superdesign-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/superdesigndev/superdesign-skill |
| 2026-03-30 13:22 | superdesign-skill.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/superdesigndev/superdesign-skill.git |
| 2026-03-30 13:22 | claude-ecom | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/takechanman1228/claude-ecom |
| 2026-03-30 13:22 | chat-quality-agent | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/tanviet12/chat-quality-agent |
| 2026-03-30 13:22 | notebooklm-py | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/teng-lin/notebooklm-py |
| 2026-03-30 13:22 | playwright-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/testdino-hq/playwright-skill |
| 2026-03-30 13:22 | tinybird-agent-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinybirdco/tinybird-agent-skills |
| 2026-03-30 13:22 | open-claude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tkattkat/open-claude |
| 2026-03-30 13:22 | open-claude.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tkattkat/open-claude.git |
| 2026-03-30 13:22 | agentune | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/tqdat410/agentune |
| 2026-03-30 13:22 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/trailofbits/skills |
| 2026-03-30 13:23 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/transloadit/skills |
| 2026-03-30 13:23 | notebooklm-podcast-automator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upamune/notebooklm-podcast-automator |
| 2026-03-30 13:23 | us-census-bureau-data-api-mcp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/uscensusbureau/us-census-bureau-data-api-mcp |
| 2026-03-30 13:23 | all-agentic-architectures | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/username/all-agentic-architectures |
| 2026-03-30 13:23 | agent-browser.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/agent-browser.git |
| 2026-03-30 13:23 | agent-skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/agent-skills.git |
| 2026-03-30 13:23 | next-skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/next-skills |
| 2026-03-30 13:23 | next-skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel-labs/next-skills.git |
| 2026-03-30 13:23 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/skills |
| 2026-03-30 13:23 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel-labs/skills.git |
| 2026-03-30 13:23 | ragas | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vibrantlabsai/ragas |
| 2026-03-30 13:23 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/video-db/skills |
| 2026-03-30 13:23 | superagent | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/visionmedia/superagent |
| 2026-03-30 13:23 | vllm.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vllm-project/vllm.git |
| 2026-03-30 13:23 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vuejs-ai/skills.git |
| 2026-03-30 13:23 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vueuse/skills |
| 2026-03-30 13:23 | skills.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vueuse/skills.git |
| 2026-03-30 13:23 | pentagi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vxcontrol/pentagi |
| 2026-03-30 13:23 | skillsentry | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vythanhtra/skillsentry |
| 2026-03-30 13:23 | Auto-claude-code-research-in-sleep | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep |
| 2026-03-30 13:23 | convexskills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/waynesutton/convexskills |
| 2026-03-30 13:23 | convexskills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/waynesutton/convexskills.git |
| 2026-03-30 13:23 | agentsview | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wesm/agentsview |
| 2026-03-30 13:23 | agentsview.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/wesm/agentsview.git |
| 2026-03-30 13:23 | WikidataMCP | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/wmde/WikidataMCP |
| 2026-03-30 13:23 | linear-claude-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/wrsmith108/linear-claude-skill |
| 2026-03-30 13:23 | varlock-claude-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/wrsmith108/varlock-claude-skill |
| 2026-03-30 13:23 | x-article-publisher-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wshuyi/x-article-publisher-skill |
| 2026-03-30 13:23 | Skill_Seekers | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/yusufkaraaslan/Skill_Seekers |
| 2026-03-30 13:23 | skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zackkorman/skills |
| 2026-03-30 13:23 | skills.git | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zackkorman/skills.git |
| 2026-03-30 13:23 | AI-research-SKILLs | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zechenzhangAGI/AI-research-SKILLs |
| 2026-03-30 13:23 | zeroclaw | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zeroclaw-labs/zeroclaw |
| 2026-03-30 13:24 | claude-context | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zilliztech/claude-context |
| 2026-03-30 13:24 | model-hierarchy-skill | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zscole/model-hierarchy-skill |
| 2026-03-30 13:24 | aws-skills | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zxkane/aws-skills |
| 2026-03-30 13:24 | Scrapegraph-ai | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/VinciGit00/Scrapegraph-ai |
| 2026-03-30 13:24 | graphql.js | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/octokit/graphql.js |
| 2026-03-30 13:24 | pgvector.git | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pgvector/pgvector.git |
| 2026-03-30 13:24 | pgvectorscale | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/timescale/pgvectorscale |
| 2026-03-30 13:24 | code-review-graph | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/tirth8205/code-review-graph |
| 2026-03-30 13:25 | easy-vibe | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/datawhalechina/easy-vibe |
| 2026-03-30 13:25 | sentrux | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sentrux/sentrux |
| 2026-03-30 13:25 | claude-usage-tracker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/658jjh/claude-usage-tracker |
| 2026-03-30 13:25 | Unity-MCP | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/IvanMurzak/Unity-MCP |
| 2026-03-30 13:25 | chops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Shpigford/chops |
| 2026-03-30 13:25 | trustgraph | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/trustgraph-ai/trustgraph |
| 2026-03-30 13:26 | last30days-skill | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mvanhorn/last30days-skill |
| 2026-03-30 13:26 | gstack | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/garrytan/gstack |
| 2026-03-30 13:26 | skills | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/MiniMax-AI/skills |
| 2026-03-30 13:26 | myclaude | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/stellarlinkco/myclaude |
| 2026-03-30 13:27 | vibe-kanban | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/BloopAI/vibe-kanban |
| 2026-03-30 13:27 | Dorothy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Charlie85270/Dorothy |
| 2026-03-30 13:27 | clickhouse-go | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ClickHouse/clickhouse-go |
| 2026-03-30 13:27 | codebuff | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/CodebuffAI/codebuff |
| 2026-03-30 13:27 | Scrapling | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/D4Vinci/Scrapling |
| 2026-03-30 13:27 | engram | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Gentleman-Programming/engram |
| 2026-03-30 13:27 | gentle-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Gentleman-Programming/gentle-ai |
| 2026-03-30 13:27 | patchright | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Kaliiiiiiiiii-Vinyzu/patchright |
| 2026-03-30 13:27 | MarketInsight | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KalyanM45/MarketInsight |
| 2026-03-30 13:27 | n8n-atom | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/KhanhPham2411/n8n-atom |
| 2026-03-30 13:27 | Bambo | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/LB-Young/Bambo |
| 2026-03-30 13:27 | LitGPT | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Lightning-AI/LitGPT |
| 2026-03-30 13:27 | LitServe | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Lightning-AI/LitServe |
| 2026-03-30 13:27 | litgpt | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lightning-AI/litgpt |
| 2026-03-30 13:27 | web-check | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Lissy93/web-check |
| 2026-03-30 13:27 | Understand-Anything | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Lum1104/Understand-Anything |
| 2026-03-30 13:27 | uvloop | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/MagicStack/uvloop |
| 2026-03-30 13:27 | kimi-cli | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/MoonshotAI/kimi-cli |
| 2026-03-30 13:27 | context-engineering-kit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NeoLabHQ/context-engineering-kit |
| 2026-03-30 13:27 | Prompt_Engineering | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/NirDiamant/Prompt_Engineering |
| 2026-03-30 13:27 | opencode-antigravity-auth | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/NoeFabris/opencode-antigravity-auth |
| 2026-03-30 13:27 | openapi-generator | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/OpenAPITools/openapi-generator |
| 2026-03-30 13:28 | axolotl | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenAccess-AI-Collective/axolotl |
| 2026-03-30 13:28 | ChatDev | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/OpenBMB/ChatDev |
| 2026-03-30 13:28 | MOSS-TTS | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OpenMOSS/MOSS-TTS |
| 2026-03-30 13:28 | planning-with-files | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/OthmanAdi/planning-with-files |
| 2026-03-30 13:28 | flake8 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/PyCQA/flake8 |
| 2026-03-30 13:28 | pyo3 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/PyO3/pyo3 |
| 2026-03-30 13:28 | quivr | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/QuivrHQ/quivr |
| 2026-03-30 13:28 | ai-hands-on | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Ramakm/ai-hands-on |
| 2026-03-30 13:28 | openfang | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/RightNow-AI/openfang |
| 2026-03-30 13:28 | Observer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Roy3838/Observer |
| 2026-03-30 13:28 | rune | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Rune-kit/rune |
| 2026-03-30 13:28 | system-design-patterns | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Sairyss/system-design-patterns |
| 2026-03-30 13:28 | ai-engineering-toolkit | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Sumanth077/ai-engineering-toolkit |
| 2026-03-30 13:28 | tinyagi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/TinyAGI/tinyagi |
| 2026-03-30 13:28 | dasel | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/TomWright/dasel |
| 2026-03-30 13:29 | unstructured | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/Unstructured-IO/unstructured |
| 2026-03-30 13:29 | Upsonic | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Upsonic/Upsonic |
| 2026-03-30 13:29 | hyperspace-db | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/YARlabs/hyperspace-db |
| 2026-03-30 13:29 | xsv | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/Yomguithereal/xsv |
| 2026-03-30 13:29 | GitNexus | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/abhigyanpatwari/GitNexus |
| 2026-03-30 13:29 | runner-images | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/actions/runner-images |
| 2026-03-30 13:29 | deeplake | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/activeloopai/deeplake |
| 2026-03-30 13:29 | rest-api | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/agilecrm/rest-api |
| 2026-03-30 13:29 | react-grab | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/aidenybai/react-grab |
| 2026-03-30 13:29 | alasql | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/alasql/alasql |
| 2026-03-30 13:29 | OpenSandbox | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/alibaba/OpenSandbox |
| 2026-03-30 13:29 | learn-ai-engineering | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ashishps1/learn-ai-engineering |
| 2026-03-30 13:29 | async-profiler | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/async-profiler/async-profiler |
| 2026-03-30 13:29 | awesome-go | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/avelino/awesome-go |
| 2026-03-30 13:29 | axolotl | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/axolotl-ai-cloud/axolotl |
| 2026-03-30 13:29 | pi-mono | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/badlogic/pi-mono |
| 2026-03-30 13:29 | eta | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/bgub/eta |
| 2026-03-30 13:30 | blinko | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/blinko-space/blinko |
| 2026-03-30 13:30 | blinko | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/blinkospace/blinko |
| 2026-03-30 13:30 | bmad-method-test-architecture-enterprise | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise |
| 2026-03-30 13:30 | forgewright | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/buiphucminhtam/forgewright |
| 2026-03-30 13:30 | deer-flow | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/bytedance/deer-flow |
| 2026-03-30 13:30 | oh-my-pi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/can1357/oh-my-pi |
| 2026-03-30 13:30 | just | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/casey/just |
| 2026-03-30 13:30 | chalk | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/chalk/chalk |
| 2026-03-30 13:30 | crush | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/charmbracelet/crush |
| 2026-03-30 13:30 | clearml | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/clearml/clearml |
| 2026-03-30 13:31 | workerd | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cloudflare/workerd |
| 2026-03-30 13:31 | oh-my-opencode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/code-yeongyu/oh-my-opencode |
| 2026-03-30 13:31 | gitingest | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/coderamp-labs/gitingest |
| 2026-03-30 13:31 | Archon | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/coleam00/Archon |
| 2026-03-30 13:31 | API-mega-list | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/cporter202/API-mega-list |
| 2026-03-30 13:31 | crewAI | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/crewAIInc/crewAI |
| 2026-03-30 13:32 | camoufox | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/daijro/camoufox |
| 2026-03-30 13:32 | qsv | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/dathere/qsv |
| 2026-03-30 13:32 | 9router | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/decolua/9router |
| 2026-03-30 13:32 | DeepSpeed | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/deepspeedai/DeepSpeed |
| 2026-03-30 13:33 | OmniRoute | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/diegosouzapw/OmniRoute |
| 2026-03-30 13:33 | distil-text2sql | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/distil-labs/distil-text2sql |
| 2026-03-30 13:33 | build-push-action | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/docker/build-push-action |
| 2026-03-30 13:33 | univer | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/dream-num/univer |
| 2026-03-30 13:33 | memspan | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ericblue/memspan |
| 2026-03-30 13:33 | eta | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/eta-dev/eta |
| 2026-03-30 13:33 | prompts.chat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/f/prompts.chat |
| 2026-03-30 13:33 | firecrawl-discord-bot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/firecrawl/firecrawl-discord-bot |
| 2026-03-30 13:33 | firecrawl-mcp-server | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/firecrawl/firecrawl-mcp-server |
| 2026-03-30 13:33 | supertest | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/forwardemail/supertest |
| 2026-03-30 13:33 | clarity-gate | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/frmoretto/clarity-gate |
| 2026-03-30 13:33 | emdash | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/generalaction/emdash |
| 2026-03-30 13:33 | engram | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gentleman-programming/engram |
| 2026-03-30 13:33 | gentleman-ai-installer | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gentleman-programming/gentleman-ai-installer |
| 2026-03-30 13:33 | how-to-ralph-wiggum | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ghuntley/how-to-ralph-wiggum |
| 2026-03-30 13:34 | developer-kit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/giuseppe-trisciuoglio/developer-kit |
| 2026-03-30 13:34 | colly | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gocolly/colly |
| 2026-03-30 13:34 | prr-kit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/goldynlabs/prr-kit |
| 2026-03-30 13:34 | pprof | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/google/pprof |
| 2026-03-30 13:34 | gpustack | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gpustack/gpustack |
| 2026-03-30 13:35 | gradio | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gradio-app/gradio |
| 2026-03-30 13:35 | pyroscope | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/grafana/pyroscope |
| 2026-03-30 13:35 | griptape | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/griptape-ai/griptape |
| 2026-03-30 13:35 | grpc | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/grpc/grpc |
| 2026-03-30 13:35 | GSD-2 | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/gsd-build/GSD-2 |
| 2026-03-30 13:35 | get-shit-done | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gsd-build/get-shit-done |
| 2026-03-30 13:35 | gsd-2 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/gsd-build/gsd-2 |
| 2026-03-30 13:35 | gdrive-manager | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/habitual69/gdrive-manager |
| 2026-03-30 13:35 | mq | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/harehare/mq |
| 2026-03-30 13:35 | awesome-ddd | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/heynickc/awesome-ddd |
| 2026-03-30 13:35 | LLaMA-Factory | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hiyouga/LLaMA-Factory |
| 2026-03-30 13:35 | LlamaFactory | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/hiyouga/LlamaFactory |
| 2026-03-30 13:35 | CodexKit | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/hoavdc/CodexKit |
| 2026-03-30 13:36 | yyjson | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ibireme/yyjson |
| 2026-03-30 13:36 | privateGPT | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/imartinez/privateGPT |
| 2026-03-30 13:36 | voicebox | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jamiepine/voicebox |
| 2026-03-30 13:36 | pixl-server-web | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jhuckaby/pixl-server-web |
| 2026-03-30 13:36 | jina | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jina-ai/jina |
| 2026-03-30 13:36 | qsv | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jqnatividad/qsv |
| 2026-03-30 13:36 | awesome-notebooks | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/jupyter-naas/awesome-notebooks |
| 2026-03-30 13:36 | async-profiler | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/jvm-profiling-tools/async-profiler |
| 2026-03-30 13:36 | data-structure-protocol | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/k-kolomeitsev/data-structure-protocol |
| 2026-03-30 13:36 | awesome-nlp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/keon/awesome-nlp |
| 2026-03-30 13:37 | modular-monolith-with-ddd | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kgrzybek/modular-monolith-with-ddd |
| 2026-03-30 13:37 | n8n-atom-fork | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/khanh-atom/n8n-atom-fork |
| 2026-03-30 13:38 | kreuzberg | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kreuzberg-dev/kreuzberg |
| 2026-03-30 13:38 | pocket-tts | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/kyutai-labs/pocket-tts |
| 2026-03-30 13:38 | langroid | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/langroid/langroid |
| 2026-03-30 13:38 | Antigravity-Manager | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/lbjlaq/Antigravity-Manager |
| 2026-03-30 13:38 | garak | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/leondz/garak |
| 2026-03-30 13:38 | lobe-chat | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/lobehub/lobe-chat |
| 2026-03-30 13:38 | lobehub | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/lobehub/lobehub |
| 2026-03-30 13:38 | ludwig | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ludwig-ai/ludwig |
| 2026-03-30 13:38 | xan | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/medialab/xan |
| 2026-03-30 13:38 | Acontext | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/memodb-io/Acontext |
| 2026-03-30 13:38 | Acontext-Examples | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/memodb-io/Acontext-Examples |
| 2026-03-30 13:38 | acontext | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/memodb-io/acontext |
| 2026-03-30 13:38 | torchtune | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/meta-pytorch/torchtune |
| 2026-03-30 13:38 | DeepSpeed | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/microsoft/DeepSpeed |
| 2026-03-30 13:39 | autogen | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/autogen |
| 2026-03-30 13:39 | markitdown | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/microsoft/markitdown |
| 2026-03-30 13:39 | promptflow | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/promptflow |
| 2026-03-30 13:40 | semantic-kernel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/microsoft/semantic-kernel |
| 2026-03-30 13:40 | react-doctor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/millionco/react-doctor |
| 2026-03-30 13:40 | simpleaichat | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/minimaxir/simpleaichat |
| 2026-03-30 13:40 | mlx-examples | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/ml-explore/mlx-examples |
| 2026-03-30 13:40 | mlx-lm | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ml-explore/mlx-lm |
| 2026-03-30 13:40 | mlflow | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/mlflow/mlflow |
| 2026-03-30 13:40 | modelcontextprotocol | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/modelcontextprotocol/modelcontextprotocol |
| 2026-03-30 13:40 | python-sdk | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/python-sdk |
| 2026-03-30 13:40 | servers | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/modelcontextprotocol/servers |
| 2026-03-30 13:40 | typescript-sdk | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/modelcontextprotocol/typescript-sdk |
| 2026-03-30 13:41 | pdf.js | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mozilla/pdf.js |
| 2026-03-30 13:41 | LocalAI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/mudler/LocalAI |
| 2026-03-30 13:41 | temm1e | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nagisanzenin/temm1e |
| 2026-03-30 13:41 | LobsterAI | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/netease-youdao/LobsterAI |
| 2026-03-30 13:41 | context-and-tools | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/netlify/context-and-tools |
| 2026-03-30 13:41 | txtai | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/neuml/txtai |
| 2026-03-30 13:41 | quotio | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/nguyenphutrong/quotio |
| 2026-03-30 13:42 | hindsight | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/nicoloboschi/hindsight |
| 2026-03-30 13:42 | superpowers | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/obra/superpowers |
| 2026-03-30 13:42 | superpowers-lab | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/obra/superpowers-lab |
| 2026-03-30 13:42 | octokit.rb | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/octokit/octokit.rb |
| 2026-03-30 13:42 | opentelemetry-collector | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/open-telemetry/opentelemetry-collector |
| 2026-03-30 13:42 | opentelemetry-ebpf-profiler | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/open-telemetry/opentelemetry-ebpf-profiler |
| 2026-03-30 13:42 | opentelemetry-java-instrumentation | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/open-telemetry/opentelemetry-java-instrumentation |
| 2026-03-30 13:42 | lobster | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/openclaw/lobster |
| 2026-03-30 13:42 | opencode | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/opencode-ai/opencode |
| 2026-03-30 13:42 | serena | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/oraios/serena |
| 2026-03-30 13:42 | gping | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/orf/gping |
| 2026-03-30 13:42 | planning-with-files | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/othmanadi/planning-with-files |
| 2026-03-30 13:42 | paradedb | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/paradedb/paradedb |
| 2026-03-30 13:42 | pathway | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pathwaycom/pathway |
| 2026-03-30 13:42 | aider | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/paul-gauthier/aider |
| 2026-03-30 13:42 | pinchtab | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pinchtab/pinchtab |
| 2026-03-30 13:42 | ossinsight | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pingcap/ossinsight |
| 2026-03-30 13:42 | xyops | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pixlcore/xyops |
| 2026-03-30 13:42 | katana | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/projectdiscovery/katana |
| 2026-03-30 13:42 | prometheus-operator | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/prometheus-operator/prometheus-operator |
| 2026-03-30 13:42 | flake8 | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pycqa/flake8 |
| 2026-03-30 13:43 | pydantic-ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pydantic/pydantic-ai |
| 2026-03-30 13:43 | pyroscope | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/pyroscope-io/pyroscope |
| 2026-03-30 13:43 | torchtune | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/pytorch/torchtune |
| 2026-03-30 13:43 | Star-Office-UI | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/ringhyacinth/Star-Office-UI |
| 2026-03-30 13:45 | tldw_server | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/rmusser01/tldw_server |
| 2026-03-30 13:46 | llama_index | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/run-llama/llama_index |
| 2026-03-30 13:46 | rune | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/rune-kit/rune |
| 2026-03-30 13:47 | saleor | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/saleor/saleor |
| 2026-03-30 13:47 | vexor | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/scarletkc/vexor |
| 2026-03-30 13:47 | scrapy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/scrapy/scrapy |
| 2026-03-30 13:47 | codex-cli-best-practice | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shanraisshan/codex-cli-best-practice |
| 2026-03-30 13:47 | Kode | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode |
| 2026-03-30 13:47 | Kode-cli | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shareAI-lab/Kode-cli |
| 2026-03-30 13:47 | better-all | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/shuding/better-all |
| 2026-03-30 13:47 | hivemind-plugin | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/shynlee04/hivemind-plugin |
| 2026-03-30 13:47 | ShipSwift | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/signerlabs/ShipSwift |
| 2026-03-30 13:47 | got | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sindresorhus/got |
| 2026-03-30 13:48 | skypilot | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/skypilot-org/skypilot |
| 2026-03-30 13:48 | podcastfy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/souzatharsis/podcastfy |
| 2026-03-30 13:48 | dspy | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/stanfordnlp/dspy |
| 2026-03-30 13:49 | beads | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/steveyegge/beads |
| 2026-03-30 13:49 | xTuring | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/stochasticai/xTuring |
| 2026-03-30 13:49 | ai | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/stripe/ai |
| 2026-03-30 13:49 | ralph-tui | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/subsy/ralph-tui |
| 2026-03-30 13:49 | sympozium | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/sympozium-ai/sympozium |
| 2026-03-30 13:49 | temm1e | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/temm1e-labs/temm1e |
| 2026-03-30 13:49 | dotfiles | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/thieung/dotfiles |
| 2026-03-30 13:49 | agentql | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/tinyfish-io/agentql |
| 2026-03-30 13:49 | tinyfish-cookbook | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tinyfish-io/tinyfish-cookbook |
| 2026-03-30 13:49 | dasel | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tomwright/dasel |
| 2026-03-30 13:50 | cognee | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/topoteretes/cognee |
| 2026-03-30 13:50 | trulens | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/truera/trulens |
| 2026-03-30 13:50 | typedi | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/typestack/typedi |
| 2026-03-30 13:50 | Antigravity-Deck | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/tysonnbt/Antigravity-Deck |
| 2026-03-30 13:50 | crawl4ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/unclecode/crawl4ai |
| 2026-03-30 13:50 | notebooks | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/unslothai/notebooks |
| 2026-03-30 13:50 | unsloth | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/unslothai/unsloth |
| 2026-03-30 13:50 | upsonic | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/upsonic/upsonic |
| 2026-03-30 13:51 | uptrain | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/uptrain-ai/uptrain |
| 2026-03-30 13:51 | strix | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/usestrix/strix |
| 2026-03-30 13:51 | reader | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vakra-dev/reader |
| 2026-03-30 13:51 | TaxHacker | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vas3k/TaxHacker |
| 2026-03-30 13:51 | hindsight | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vectorize-io/hindsight |
| 2026-03-30 13:52 | ai | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/vercel/ai |
| 2026-03-30 13:52 | chat | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/vercel/chat |
| 2026-03-30 13:52 | OpenViking | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/volcengine/OpenViking |
| 2026-03-30 13:52 | wandb | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wandb/wandb |
| 2026-03-30 13:52 | weave | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wandb/weave |
| 2026-03-30 13:52 | Warp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/warpdotdev/Warp |
| 2026-03-30 13:52 | tmux-ide | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/wavyrai/tmux-ide |
| 2026-03-30 13:53 | Verba | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/weaviate/Verba |
| 2026-03-30 13:53 | weaviate | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/weaviate/weaviate |
| 2026-03-30 13:53 | ws | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/websockets/ws |
| 2026-03-30 13:53 | docutranslate | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/xunbu/docutranslate |
| 2026-03-30 13:53 | repomix | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/yamadashy/repomix |
| 2026-03-30 13:53 | babyagi | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yoheinakajima/babyagi |
| 2026-03-30 13:53 | yt-dlp | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/yt-dlp/yt-dlp |
| 2026-03-30 13:53 | frontend-slides | INGESTED_AS_KNOWLEDGE | Nén thành .md và xóa raw clone | https://github.com/zarazhangrui/frontend-slides |
| 2026-03-30 13:53 | openchatbi | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zhongyu09/openchatbi |
| 2026-03-30 13:53 | autoclip | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zhouxiaoka/autoclip |
| 2026-03-30 13:53 | VMware-AIops | REJECTED | WARN: Repo trống, không có code hay docs | https://github.com/zw008/VMware-AIops |
