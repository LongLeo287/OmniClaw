# CONTENT INTAKE & VETTING (CIV) Ã¢â‚¬â€ Department Rules
# Version: 1.2 | Updated: 2026-03-24
# Dept Head: intake-chief-agent | Reports to: COO
# Mission: KiÃ¡Â»Æ’m soÃƒÂ¡t toÃƒÂ n bÃ¡Â»â„¢ nÃ¡Â»â„¢i dung Ã„â€˜Ã¡ÂºÂ§u vÃƒÂ o cho AI OS
# This dept is the SINGLE GATE for ALL external content entering AI OS
# No content enters AI OS without passing through CIV
# v1.2: +CIV-11 Local-First Check | +CIV-12 GAP PROPOSAL ENGINE | Fix QUARANTINE path
# Applies in addition to: brain/corp/rules/manager_rules.md + worker_rules.md

---

## DEPT DOMAIN RULES

RULE CIV-01: SINGLE ENTRY POINT Ã¢â‚¬â€ NO EXCEPTIONS
  ALL external content (any type, any source) MUST enter AI OS through CIV.
  Direct-to-folder placement of external content = security violation.
  No agent or user may bypass CIV. CEO override = written log required.

RULE CIV-02: CLASSIFY FIRST, ACT SECOND
  classifier-agent MUST categorize EVERY input before any processing begins.
  Unknown type Ã¢â€ â€™ hold in /incoming/unclassified/ Ã¢â€ â€™ alert intake-chief-agent.
  No content proceeds without a classification tag.

RULE CIV-03: EVERY INPUT GETS AN INTAKE TICKET
  intake-agent creates a ticket for EVERY input received:
  Format: CIV-[YYYY-MM-DD]-[SEQ] | Type | Source | Status
  Ticket lives in: QUARANTINE/logs/intake_log.md
  Ticket never closed without final status: INGESTED / REJECTED / PENDING.

RULE CIV-04: SECURITY CHECK IS NON-NEGOTIABLE FOR REPOS
  ALL repo-type inputs MUST run vet_repo.ps1 (12-stage Strix scan)
  BEFORE any file is read, extracted, or acted upon.
  FAIL = delete from QUARANTINE + log + close ticket as REJECTED.
  Security GRC (strix-agent) is co-authority on all repo decisions.

RULE CIV-05: CONTENT-TYPE ROUTING IS MANDATORY
  After classification + vetting, ingest-router-agent routes to exact destination:
  - Code/Repo   Ã¢â€ â€™ Registry & Capability (after GATE_SECURITY PASS)
  - Knowledge   Ã¢â€ â€™ Asset & Knowledge Library
  - Assets/Images Ã¢â€ â€™ assets/ folder + asset-tracker-agent
  - Rules/Docs  Ã¢â€ â€™ relevant dept or brain/corp/rules/
  Wrong destination = re-route, NOT delete.

RULE CIV-06: OUTPUT VERIFICATION
  ingest-router-agent verifies delivery AFTER routing:
  - File exists at destination
  - Destination agent acknowledged (receipt written)
  - Intake ticket updated to INGESTED
  No ticket left in PENDING > 1 corp cycle.

RULE CIV-07: REJECTION LOG IS PERMANENT
  Rejected content logged to QUARANTINE/logs/rejected_log.md permanently.
  Entry includes: source URL/path, rejection reason, timestamp, who decided.
  This log feeds Security GRC blacklist (RULE SEC-08).

RULE CIV-08: AUTO-PIPELINE FOR KNOWN-SAFE SOURCES
  Sources on EXTERNAL_SKILL_SOURCES.yaml whitelist:
  Ã¢â€ â€™ Skip manual review step (still run vet_repo.ps1 for repos)
  Ã¢â€ â€™ classifier Ã¢â€ â€™ fast-track Ã¢â€ â€™ ingest
  Unknown sources Ã¢â€ â€™ full manual review by intake-chief-agent.

RULE CIV-09: VALUE ASSESSMENT IS MANDATORY BEFORE ROUTING
  After quality/safety validation, content-validator-agent MUST assign VALUE_TYPE.
  VALUE_TYPE = what this content CAN BECOME in AI OS (not just what it IS).
  9 VALUE_TYPEs: KNOWLEDGE | SKILL | PLUGIN | WORKFLOW | MCP_SERVER |
                 TOOL_SCRIPT | RULE_POLICY | AGENT_DEFINITION | DATA_ASSET
  Content can have multiple VALUE_TYPEs Ã¢â€ â€™ route to ALL applicable destinations.
  UNKNOWN VALUE_TYPE Ã¢â€ â€™ hold in vetted/ Ã¢â€ â€™ alert intake-chief-agent within 2 cycles.
  Full taxonomy + routing matrix: brain/corp/sops/VALUE_ASSESSMENT_ROUTING.md

RULE CIV-10: CHECK BEFORE ROUTE Ã¢â‚¬â€ NEVER OVERWRITE EXISTING RESOURCES
  ingest-router-agent MUST check if destination already has a resource before routing.
  If resource EXISTS at destination:
    Ã¢â€ â€™ Enter CONFLICT RESOLUTION flow (see VALUE_ASSESSMENT_ROUTING.md)
    Ã¢â€ â€™ Route to training-agent for enrichment (select + upgrade)
    Ã¢â€ â€™ Set ticket status: ENRICHMENT_PENDING (not INGESTED)
    Ã¢â€ â€™ NEVER auto-overwrite. NEVER delete existing resource.
  If resource DOES NOT EXIST:
    Ã¢â€ â€™ Normal routing (CREATE)
    Ã¢â€ â€™ Ticket status: INGESTED
  Principle: TRAIN and SELECT from new content, do not replace what works.
  RULE_POLICY and AGENT_DEFINITION types: COO/C-Suite approval required
    even for upgrades Ã¢â‚¬â€ never bypass org governance chain.
  Full conflict matrix: brain/corp/sops/VALUE_ASSESSMENT_ROUTING.md Ã¢â€ â€™ CONFLICT RESOLUTION section

RULE CIV-11: LOCAL-FIRST CHECK â€” BEFORE EVERY INTAKE â˜… UPDATED v1.3
  ANTIGRAVITY (Tier 1) MUST query local brain BEFORE creating any CIV ticket:
  1. Query LightRAG: rag.hybrid_query("<source URL or topic>", mode="mix")
  2. Run `system/ops/scripts/staleness_check.py <URL>` to auto-check freshness.
  UNCHANGED:
    â†’ Return existing KI to CEO.
    â†’ STOP (no ticket created, no bandwidth wasted). Auto-Decision!
  CHANGED / NOT FOUND:
    â†’ proceed to create CIV ticket normally (STEP 1)
  Purpose: Avoid duplicate ingestion. Save bandwidth. Respect existing knowledge.

RULE CIV-12: GAP PROPOSAL ENGINE Ã¢â‚¬â€ MANDATORY AFTER STEP 3.5 Ã¢Ëœâ€¦ NEW v1.2
  After content-analyst-agent (open-notebook) analysis:
  IF gap_detected = true (domain not covered by any existing agent/dept):
    Ã¢â€ â€™ ANTIGRAVITY creates GAP PROPOSAL and sends to CEO via notification_bridge
    Ã¢â€ â€™ CEO receives [A/B/C/D] options (see content-intake-flow.md STEP 3.6)
    Ã¢â€ â€™ CEO decision is ASYNC Ã¢â‚¬â€ does NOT block intake pipeline
    Ã¢â€ â€™ GAP REPORT saved to brain/corp/gaps/GAP-<date>-<domain>.md
  content-analyst-agent adds to output: gap_detected, gap_domain, proposed_agent, proposed_dept
  SLA: Proposal sent to CEO < 5 minutes after STEP 3.5 completes

---


## INTAKE STRUCTURE (Folder Layout)

```
<AOS_ROOT>/security/QUARANTINE/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ incoming/           Ã¢â€ Â ALL new content lands here first
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ repos/          Ã¢â€ Â git repos waiting to be vetted
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ web/            Ã¢â€ Â web URLs / scraped content
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ documents/      Ã¢â€ Â PDFs, Word docs, etc.
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ images/         Ã¢â€ Â images, screenshots
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ text/           Ã¢â€ Â raw text content
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ unclassified/   Ã¢â€ Â unknown type, pending human review
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ vetted/             Ã¢â€ Â content that PASSED all checks, awaiting routing
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ repos/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ knowledge/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ assets/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ rejected/           Ã¢â€ Â FAILED content (kept 7 days then purged)
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ logs/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ intake_log.md   Ã¢â€ Â master ticket log (all CIV-XXXX tickets)
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ rejected_log.md Ã¢â€ Â permanent rejection record
Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ vet_repo.ps1        Ã¢â€ Â Strix Security vetting script
```

Ã¢Å¡Â Ã¯Â¸Â QUARANTINE path: `<AOS_ROOT>/security/QUARANTINE/`
   AOS_ROOT = `<AI_OS_ROOT>`
   Full path: `<AI_OS_ROOT>\security\QUARANTINE\`
   (NÃ¡ÂºÂ¿u cÃƒÂ³ file nÃƒÂ o tham chiÃ¡ÂºÂ¿u <AI_OS_ROOT>\QUARANTINE Ã¢â€ â€™ Ã„â€˜ÃƒÂ³ lÃƒÂ  LEGACY PATH Ã¢â‚¬â€ SAI)

---

## INPUT TYPE CLASSIFICATION TABLE

| Input Type | Classifier Tag | Vetting Required | Next Step |
|------------|---------------|-----------------|----------|
| GitHub / Git URL | `REPO` | vet_repo.ps1 (MANDATORY) | Ã¢â€ â€™ VALUE_TYPE assessment Ã¢â€ â€™ routing |
| Web article / blog | `WEB_CONTENT` | content-validator check | Ã¢â€ â€™ VALUE_TYPE assessment Ã¢â€ â€™ routing |
| Research paper / PDF | `DOCUMENT` | vet_media_docs.py (MANDATORY) + doc-parser | Ã¢â€ â€™ VALUE_TYPE assessment Ã¢â€ â€™ routing |
| Image / screenshot | `IMAGE` | vet_media_docs.py (MANDATORY) + safe check | Ã¢â€ â€™ DATA_ASSET or KNOWLEDGE |
| Raw text / prompt | `TEXT` | content-validator check | Ã¢â€ â€™ VALUE_TYPE assessment Ã¢â€ â€™ routing |
| Ruleset / config doc | `CONFIG` | content-validator + GATE_SECURITY | Ã¢â€ â€™ RULE_POLICY or WORKFLOW |
| Plugin / script | `PLUGIN` | vet_repo.ps1 + GATE_SECURITY | Ã¢â€ â€™ SKILL or PLUGIN or TOOL_SCRIPT |

NOTE: After classification, content-validator-agent assigns VALUE_TYPE (what it CAN BECOME).
Full routing matrix: brain/corp/sops/VALUE_ASSESSMENT_ROUTING.md

---

## AGENT ROLES & RESPONSIBILITIES

### intake-chief-agent (Dept Head)
**Role:** Intake pipeline leadership, oversight, escalation authority
**This agent is the GATEKEEPER of AI OS**
**Responsibilities:**
- Own QUARANTINE folder and intake_log.md
- Review all UNCLASSIFIED and borderline cases
- Approve WARN-status repo ingestion (after manual review)
- Escalate to Security GRC for FAIL cases
- Report intake statistics to COO each cycle
- Write CIV daily brief
**Must load at boot:**
- `corp/memory/departments/content_intake.md`
- `QUARANTINE/logs/intake_log.md` Ã¢â‚¬â€ current ticket queue
- `shared-context/EXTERNAL_SKILL_SOURCES.yaml` Ã¢â‚¬â€ whitelist/blacklist
- `corp/departments/content_intake/MANAGER_PROMPT.md`
**Skills:**
- `reasoning_engine` Ã¢â‚¬â€ intake decisions, escalations
- `diagnostics_engine` Ã¢â‚¬â€ pipeline health monitoring
**KPIs:** Ticket resolution rate >95% per cycle | Avg ticket close time <1 cycle

---

### intake-agent
**Role:** Receive, log, and stage ALL incoming content
**The first contact for every piece of external content**
**Responsibilities:**
- Receive input (URL, file path, content body) from any source
- Create CIV ticket immediately in intake_log.md
- Stage content to correct /incoming/<type>/ folder
- Pass ticket to classifier-agent
**At start of each intake task, load:**
- SKILL: `context_manager` Ã¢â‚¬â€ ticket management, file staging
- SKILL: `knowledge_enricher` Ã¢â‚¬â€ if URL, fetch metadata
- `QUARANTINE/logs/intake_log.md`
**Skills:**
- `context_manager` Ã¢â‚¬â€ staging and ticket creation
- `knowledge_enricher` Ã¢â‚¬â€ URL metadata extraction
**Intake ticket format:**
```
CIV-[DATE]-[SEQ]
Source: [URL or file path]
Type: [pending classification]
Staged to: QUARANTINE/incoming/[type]/
Status: RECEIVED Ã¢â€ â€™ CLASSIFYING
Timestamp: [ISO timestamp]
```

---

### classifier-agent
**Role:** Classify ALL incoming content by type and route to correct pipeline
**Responsibilities:**
- Inspect staged content in /incoming/
- Assign classification tag: REPO / WEB_CONTENT / DOCUMENT / IMAGE / TEXT / CONFIG / PLUGIN
- For unclear cases: move to /incoming/unclassified/ + alert intake-chief-agent
- Update ticket with classification
- Trigger correct next pipeline stage
**At start of each classification task, load:**
- SKILL: `reasoning_engine` Ã¢â‚¬â€ type inference from content/URL/extension
- SKILL: `knowledge_enricher` Ã¢â‚¬â€ URL analysis for content-type detection
- Current intake ticket from intake-agent
**Skills:**
- `reasoning_engine` Ã¢â‚¬â€ type classification logic
- `knowledge_enricher` Ã¢â‚¬â€ URL/content analysis
**Classification signals:**
  - `.git` URL or GitHub/GitLab link Ã¢â€ â€™ REPO
  - `.pdf` / `.docx` / `.md` doc Ã¢â€ â€™ DOCUMENT
  - `.py` `.js` `.ps1` Ã¢â€ â€™ PLUGIN (treat as code)
  - News/article URL Ã¢â€ â€™ WEB_CONTENT
  - `.png` `.jpg` `.webp` Ã¢â€ â€™ IMAGE

---

### repo-fetcher-agent
**Role:** Clone repos from URLs into QUARANTINE for vetting
**Coordinates with Security GRC for the vetting step**
**Responsibilities:**
- Receive REPO-classified ticket from classifier-agent
- Clone repo URL into QUARANTINE/incoming/repos/<name>/
- Hand off to Security GRC (security-scanner) for vet_repo.ps1
- Receive PASS/FAIL back from strix-agent
- On PASS: move to QUARANTINE/vetted/repos/ Ã¢â€ â€™ trigger ingest-router
- On FAIL: move to QUARANTINE/rejected/ Ã¢â€ â€™ close ticket REJECTED
**At start of each fetch task, load:**
- SKILL: `shell_assistant` Ã¢â‚¬â€ git clone operations
- SKILL: `skill_fetcher` Ã¢â‚¬â€ if using skill_fetcher.ps1 pipeline
- Current CIV ticket
**Skills:**
- `shell_assistant` Ã¢â‚¬â€ git and filesystem operations
- `skill_fetcher` Ã¢â‚¬â€ structured repo ingestion pipeline
**Never read/execute repo content before vet_repo.ps1 PASS**

---

### web-crawler-agent
**Role:** Fetch and extract content from web URLs (articles, docs, research)
**Responsibilities:**
- Receive WEB_CONTENT ticket from classifier-agent
- Fetch URL content (HTML Ã¢â€ â€™ text extraction, metadata)
- Validate: no malicious scripts, no redirect chains to phishing
- Stage extracted text to QUARANTINE/incoming/web/<slug>.md
- Pass to content-validator-agent for final check
**At start of each crawl task, load:**
- SKILL: `knowledge_enricher` Ã¢â‚¬â€ web content extraction
- SKILL: `reasoning_engine` Ã¢â‚¬â€ content quality judgment
- Current CIV ticket + URL
**Skills:**
- `knowledge_enricher` Ã¢â‚¬â€ PRIMARY TOOL. Web extraction.
- `reasoning_engine` Ã¢â‚¬â€ quality and relevance check

---

### doc-parser-agent
**Role:** Parse and extract content from documents (PDF, DOCX, MD)
**Responsibilities:**
- Receive DOCUMENT ticket from classifier-agent
- Extract text content from PDF/DOCX
- Structure output: title, summary, full text, source, date
- Stage to QUARANTINE/incoming/documents/<name>.md
- Pass to content-validator-agent
**At start of each parse task, load:**
- SKILL: `knowledge_enricher` Ã¢â‚¬â€ document text extraction
- SKILL: `reasoning_engine` Ã¢â‚¬â€ document structure analysis
- Current CIV ticket + file path
**Skills:**
- `knowledge_enricher` Ã¢â‚¬â€ document parsing and extraction
- `reasoning_engine` Ã¢â‚¬â€ content structuring

---

### content-validator-agent
**Role:** Validate content quality/safety AND assess VALUE_TYPE (what content can become)
**UPGRADED v1.1 Ã¢â‚¬â€ now performs VALUE_TYPE assessment per CIV-09**
**Responsibilities:**
- Check for: spam, irrelevant content, malicious prompts, NSFW
- Score content quality (1-10): relevance, accuracy, completeness
- Score < 4: reject (QUARANTINE/rejected/) + log reason
- Score Ã¢â€°Â¥ 4: assign VALUE_TYPE(s) using signal checklist
- VALUE_TYPE signals reference: brain/corp/sops/VALUE_ASSESSMENT_ROUTING.md
- Output validation result WITH VALUE_TYPE tags to ingest-router-agent
- Flag MULTI-VALUE content (has 2+ VALUE_TYPEs) for dual-routing
- For governance docs: also check SOUL.md alignment
**At start of each validation task, load:**
- SKILL: `reasoning_engine` Ã¢â‚¬â€ content quality + VALUE_TYPE assessment
- SKILL: `diagnostics_engine` Ã¢â‚¬â€ content anomaly detection
- SKILL: `knowledge_enricher` Ã¢â‚¬â€ cross-reference known patterns for VALUE_TYPE
- `shared-context/SOUL.md` Ã¢â‚¬â€ alignment check baseline
- `corp/sops/VALUE_ASSESSMENT_ROUTING.md` Ã¢â‚¬â€ MANDATORY. VALUE_TYPE taxonomy.
**Skills:**
- `reasoning_engine` Ã¢â‚¬â€ quality scoring AND VALUE_TYPE classification
- `diagnostics_engine` Ã¢â‚¬â€ safety and anomaly checks
- `knowledge_enricher` Ã¢â‚¬â€ signal detection from content patterns
**Output format to ingest-router-agent:**
```
VALIDATION RESULT Ã¢â‚¬â€ CIV-[ID]
Quality score: [1-10]
Safety: PASS / FAIL
VALUE_TYPES: [comma-separated list]
Primary value: [most important VALUE_TYPE]
Priority destinations: [path(s)]
Rationale: [why this VALUE_TYPE was assigned]
```

---

### ingest-router-agent
**Role:** Route vetted/validated content to ALL applicable destinations using VALUE_TYPE
**UPGRADED v1.1 Ã¢â‚¬â€ uses VALUE_TYPE routing matrix instead of simple classification table**
**The last step before content enters AI OS proper**
**Responsibilities:**
- Receive cleared content + VALIDATION RESULT (with VALUE_TYPE) from content-validator
- For each VALUE_TYPE in the result, look up destination in routing matrix
- KNOWLEDGE Ã¢â€ â€™ knowledge-curator-agent (Asset Library)
- SKILL Ã¢â€ â€™ skill-creator-agent (Registry)
- PLUGIN Ã¢â€ â€™ plugin-librarian-agent (Registry)
- WORKFLOW Ã¢â€ â€™ archivist-agent (Operations)
- MCP_SERVER Ã¢â€ â€™ sysadmin-agent (IT Infra) + Engineering notified
- TOOL_SCRIPT Ã¢â€ â€™ sysadmin-agent (IT Infra), add to scripts catalog
- RULE_POLICY Ã¢â€ â€™ rule-builder-agent (Registry) Ã¢â€ â€™ COO approval flow
- AGENT_DEFINITION Ã¢â€ â€™ OD&L dept-builder-agent
- DATA_ASSET Ã¢â€ â€™ asset-tracker-agent (Asset Library)
- For MULTI-VALUE: route to ALL destinations, write receipt per destination
- VALUE_TYPE = UNKNOWN Ã¢â€ â€™ hold + alert intake-chief-agent (SLA: 2 cycles)
- Update CIV ticket to INGESTED only after ALL destinations confirm
**At start of each routing task, load:**
- SKILL: `context_manager` Ã¢â‚¬â€ cross-folder, multi-destination orchestration
- SKILL: `reasoning_engine` Ã¢â‚¬â€ routing decision for edge cases
- `corp/sops/VALUE_ASSESSMENT_ROUTING.md` Ã¢â‚¬â€ MANDATORY. Routing matrix.
- Cleared CIV ticket with VALIDATION RESULT
**Skills:**
- `context_manager` Ã¢â‚¬â€ multi-folder file routing
- `reasoning_engine` Ã¢â‚¬â€ routing edge case decisions
**Routing receipt format (per destination):**
```
INGEST RECEIPT Ã¢â‚¬â€ CIV-[ID] Ã¢â‚¬â€ Destination [N] of [Total]
Content: [name/description]
VALUE_TYPE: [type for this destination]
From: QUARANTINE/vetted/
To: [exact destination path]
Notified: [destination agent]
Status: DELIVERED
```


