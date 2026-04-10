---
id: knowledge-ingest
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:01.317429
---

# Department: registry_capability
# knowledge-ingest.md â€” Knowledge Ingestion Pipeline
# Version: 2.0 | Updated: 2026-03-22 | Created: 2026-03-22
# Authority: Tier 2 (Operations)
# Agents: intake-chief-agent â†’ strix-agent â†’ knowledge_navigator â†’ knowledge_enricher â†’ archivist
# Trigger: "omniclaw ingest <source>" OR agent drops file into intake queue

---

## Overview

Every piece of external knowledge (URL, doc, repo, bug fix, research dump) passes through this pipeline before entering the OmniClaw brain.

```
SOURCE (URL / File / Repo / Bug Fix / Research)
    â”‚
    â–¼
[1] INTAKE       intake-chief-agent    â€” receive + queue
    â”‚
    â–¼
[2] SECURITY     strix-agent           â€” scan for threats/injections
    â”‚
    â–¼
[3] CLASSIFY     knowledge_navigator   â€” find target dept + domain
    â”‚
    â–¼
[4] ENRICH       knowledge_enricher    â€” metadata + cross-links
    â”‚
    â–¼
    â”œâ”€â”€ Agent exists for this domain? â”€â”€YESâ”€â”€â–º [5a] Link to agent memory
    â””â”€â”€ No agent found?               â”€â”€NOâ”€â”€â”€â–º [5b] â†’ agent-auto-create workflow
    â”‚
    â–¼
[6] ARCHIVE      archivist             â€” persist to brain/knowledge/
    â”‚
    â–¼
[7] NOTIFY       notification_bridge   â€” alert CEO if significant new knowledge
```

---

## Supported Source Types

| Type | Input format | Trigger keyword |
|------|-------------|----------------|
| URL / webpage | `https://...` | `omniclaw ingest url <url>` |
| Local file | `.md`, `.pdf`, `.txt` | `omniclaw ingest file <path>` |
| Git repo | GitHub/GitLab URL | `omniclaw ingest repo <url>` |
| Bug fix lesson | Task receipt + diff | Auto-trigger after task COMPLETE |
| Research dump | Free text | `omniclaw ingest text "<content>"` |
| Web search | Query string | `omniclaw ingest search "<query>"` |

---

## Phase 1: Intake (intake-chief-agent)

```
1. Receive source â†’ create intake ticket:
   {
     "id": "KI-<timestamp>",
     "source_type": "url|file|repo|lesson|text|search",
     "source": "<value>",
     "submitted_by": "<agent_id>",
     "timestamp": "<ISO8601>",
     "status": "PENDING"
   }

2. If URL/repo: fetch content via **web_intelligence skill** (firecrawl_adapter):
   ```python
   from plugins.firecrawl.firecrawl_adapter import get_firecrawl
   fc = get_firecrawl()
   # Single URL:
   content = fc.research_url(source)
   # Full site/repo docs (limit=50):
   pages = fc.crawl_site(source, limit=50)
   ```
   â†’ Fallback order: self-hosted (localhost:3002) â†’ cloud â†’ noop (log warning)
   â†’ Rule: RULE-WEB-01: NEVER write custom HTTP code, always use firecrawl_adapter
3. If local file: read and extract text
4. If search: query web_intelligence.search("<query>"), collect top 3 results
5. Save raw content to: security/QUARANTINE/<KI-id>/ (temporary holding)
6. Update ticket status â†’ "SECURITY_SCAN"
```

---

## Phase 2: Security Scan (strix-agent â€” GATE)

```
strix-agent reads from: security/QUARANTINE/<KI-id>/

Checks:
  â–¡ Prompt injection patterns (forbidden instruction overrides)
  â–¡ Malicious code snippets
  â–¡ Credential/token exposure
  â–¡ Known malware domains (if URL source)
  â–¡ License conflicts (if repo source â€” GPL incompatibility)
  â–¡ Binary/Macro inspection via `vet_media_docs.py` (if PDF/DOCX/Image)

Results:
  PASS â†’ move to brain/knowledge/staging/<KI-id>/
         update ticket status â†’ "CLASSIFYING"
  FAIL â†’ move to security/QUARANTINE/REJECTED/<KI-id>/
         write ESCALATION_REPORT to brain/memory/corp_memory/escalations.md
         notify CEO via notification_bridge
         STOP â€” do not proceed further
```

---

## Phase 3: Classification (knowledge_navigator)

```
knowledge_navigator reads staged content and determines:

1. Domain tags (e.g., "backend", "ai-ml", "security", "marketing", "legal")
2. Target department (from org_chart.yaml departments list)
3. Knowledge type:
   - REFERENCE  â†’ API docs, specs, standards
   - LESSON     â†’ Bug fix insights, post-mortem lessons
   - RESEARCH   â†’ New concepts, papers, patterns
   - TOOL       â†’ New skill/plugin discovered
   - PATTERN    â†’ Reusable architecture or code pattern
```

### Domain â†’ Agent Matching Algorithm

```
STEP A: Extract domain tags from content
  â†’ NLP-style keyword extraction on title, headings, summary
  â†’ Map to standard domain vocabulary:
    "react", "vue", "html", "css"         â†’ web_frontend
    "python", "api", "fastapi", "backend"  â†’ backend
    "docker", "ci/cd", "devops", "k8s"    â†’ devops
    "model", "llm", "rag", "embedding"    â†’ ai_ml
    "security", "cve", "pentest", "owasp" â†’ cybersecurity
    "gdpr", "contract", "legal", "ip"     â†’ legal
    "seo", "content", "blog", "social"    â†’ marketing
    "finance", "cost", "budget", "api_cost"â†’ finance
    "test", "qa", "coverage", "e2e"       â†’ qa_testing
    "memory", "knowledge", "ki", "graph"  â†’ knowledge_mgmt
    "agent", "skill", "register", "plugin"â†’ registry
    [unmatched]                            â†’ general / CEO-escalate

  âš¡ SHORTCUT: Read brain/knowledge/CAPABILITY_MAP.md first!
     â†’ Domain â†’ Skill/Plugin lookup table (60+ entries, 12 domains)
     â†’ Decision tree included
     â†’ 90% accuracy WITHOUT LightRAG service running
     â†’ 95%+ WITH LightRAG: python ops/scripts/index_skills_lightrag.py
        then query: aquery("what skill does X?", mode="mix")

STEP B: Identify relevant agents
  Source 1 â€” org_chart.yaml:
    â†’ Find target_dept with matching domain
    â†’ dept.head + dept.workers = candidate agents
  Source 2 â€” AGENTS.md:
    â†’ Scan each agent's role description for domain keyword overlap
    â†’ If overlap â‰¥ 1 term â†’ add to relevant_agents
  Source 3 â€” SKILL_REGISTRY.json:
    â†’ Find skills matching domain_tags
    â†’ Skills â†’ accessible_by[] â†’ add those agents to relevant_agents

STEP C: Score confidence
  0.9+  â†’ Clear match (domain term exact match in agent role/skills)
  0.7-0.89 â†’ Strong match (domain cluster match in dept scope)
  0.5-0.69 â†’ Weak match (only dept-level match, no specific agent)
  < 0.5 â†’ Unknown domain â†’ escalate to CEO with options

STEP D: Gap detection
  IF relevant_agents = [] AND knowledge_type IN [TOOL, RESEARCH]:
    â†’ GAP_CONFIRMED: no agent covers this domain
    â†’ Proceed to Phase 5b (agent-auto-create)
  IF relevant_agents = [] AND knowledge_type IN [REFERENCE, LESSON]:
    â†’ Route to target_dept head as general knowledge
    â†’ No new agent needed
  IF confidence < 0.5:
    â†’ Escalate to CEO: show 3 options
      A) assign to <nearest dept>
      B) create new agent
      C) ignore (mark as LOW_PRIORITY archive)
```

```
4. Write classification result:
   brain/knowledge/staging/<KI-id>/classification.json:
   {
     "domain_tags": [...],
     "target_dept": "<dept_name>",
     "knowledge_type": "REFERENCE|LESSON|RESEARCH|TOOL|PATTERN",
     "relevant_agents": ["<agent_id>", ...],
     "confidence": 0.0-1.0,
     "gap_detected": true|false,
     "gap_reason": "<why no agent covers this>"
   }

5. If confidence < 0.5 â†’ escalate to CEO with classification options
```

---

## Phase 4: Enrichment (knowledge_enricher)

```
knowledge_enricher processes classified content:

1. metadata_enrichment:
   - Add: source, date, domain_tags, knowledge_type, related_skills
   - Extract: key concepts, definitions, warnings, best practices

2. contextual_linking:
   - Cross-link to existing knowledge entries in brain/knowledge/
   - Link to relevant SKILL_REGISTRY.json entries
   - Link to relevant agent AGENT.md files

3. Create final knowledge entry:
   brain/knowledge/<domain>/<KI-id>.md:
   ---
   id: <KI-id>
   source: <url|file|agent>
   type: REFERENCE|LESSON|RESEARCH|TOOL|PATTERN
   domain: [tags]
   dept: <target_dept>
   agents: [relevant agent IDs]
   created: <ISO8601>
   ---
   [Extracted and structured content]
   [Cross-links]
   [Key takeaways]
```

---

## Phase 5: Agent Routing

### 5a. Agent Exists â†’ Link to Memory

```
IF relevant_agents is not empty:
  For each agent in relevant_agents:
    Append to corp/memory/agents/<agent_id>.md:
    ## [DATE] â€” New Knowledge: <KI-id>
    Type: <knowledge_type>
    Summary: <1-2 sentence summary>
    Full entry: brain/knowledge/<domain>/<KI-id>.md
```

### 5b. No Agent â†’ Trigger agent-auto-create

```
IF relevant_agents is empty AND knowledge_type = "TOOL" or "RESEARCH":
  â†’ Invoke: ops/workflows/agent-auto-create.md
  Pass: { ki_id, domain_tags, knowledge_type, target_dept }

  Wait for agent-auto-create result (async â€” may span cycles):

  CASE: CEO APPROVES new agent
    â†’ Update KI ticket: status = "AGENT_CREATED"
    â†’ Link KI entry to new agent's AGENT.md once created
    â†’ Proceed to Phase 6 (Archive) normally

  CASE: CEO REJECTS new agent
    â†’ Update KI ticket: status = "NO_AGENT_ASSIGNED"
    â†’ Route knowledge to nearest dept head as general reference:
       Append to corp/memory/agents/<target_dept_head>.md
    â†’ Proceed to Phase 6 (Archive) â€” knowledge is NOT discarded

  CASE: CEO requests MODIFY (Phase 2 loop)
    â†’ KI ticket stays in "PENDING_AGENT_CREATION" status
    â†’ Phase 6 waits until agent-auto-create resolves
    â†’ SLA: max 3 cycles â€” if unresolved â†’ escalate to CSO

  CASE: agent-auto-create fails (strix REJECTED or system error)
    â†’ Update KI ticket: status = "AGENT_CREATION_FAILED"
    â†’ Route as "NO_AGENT_ASSIGNED" (see above)
    â†’ Write reason to ticket for post-mortem
```

---

## Phase 6: Archive (archivist)

```
1. Move from staging â†’ final location:
   brain/knowledge/staging/<KI-id>/ â†’ brain/knowledge/<domain>/<KI-id>/

2. Update knowledge index:
   brain/knowledge/INDEX.md â€” append new entry

3. Update dept brief if significant:
   brain/memory/corp_memory/daily_briefs/<target_dept>.md

4. Write archivist receipt:
   telemetry/receipts/knowledge_ingest/<KI-id>_receipt.json

5. Clean staging: delete brain/knowledge/staging/<KI-id>/
```

---

## Phase 7: Notify CEO (if significant)

```
Conditions that trigger CEO notification:
  - knowledge_type = "TOOL" (new capability discovered)
  - knowledge_type = "RESEARCH" + confidence > 0.8
  - Security scan FAILED (always notify)
  - New agent was created via agent-auto-create

Notification format: B2 TASK_RECEIPT
Channel: notification_bridge â†’ Telegram
```

---

## Integration Points

| System | How it connects |
|--------|----------------|
| `corp-learning-loop.md` | After each cycle retro â†’ auto-trigger ingest for all LESSON-type findings |
| `SKILL_REGISTRY.json` | TOOL-type knowledge â†’ propose new skill registration |
| `org_chart.yaml` | Target dept determined by classification; new agents linked here |
| `security/QUARANTINE/` | All raw content staged here first |
| `brain/knowledge/` | Final destination for all enriched knowledge |
| `blackboard.json` | Intake tickets tracked as tasks; agents pick up via blackboard |

---

## Triggers

```
Manual:    "omniclaw ingest <source>"
Auto:      After any task COMPLETE receipt â†’ extract LESSON
Auto:      After any bug fix â†’ run with source_type=lesson
On-demand: "omniclaw search <query>" â†’ ingest + return summary to CEO
Weekly:    archivist runs backfill_knowledge to cross-link orphan entries
```

---

*"Knowledge that isn't ingested is knowledge that's lost. Every input is an opportunity to improve."*

