---
id: enrichment_sop
type: system_rule
registered: true
---

# KNOWLEDGE ENRICHMENT SOP
# Version: 2.0 | Updated: 2026-04-10
# Owner: OA (Academy Daemon)
# Purpose: Define HOW the System integrates HIGH-VALUE knowledge

---

## ENRICHMENT TRIGGER CONDITIONS

The Knowledge Graph is enriched when ANY of these occur:

| Trigger | Source | Priority |
|---------|--------|----------|
| Raw GitHub repo successfully indexed | OAP Pipeline | HIGH |
| Human explicitly tags a note with `[TRAIN]` | Human / Workspace | HIGH |
| AI Agent produces an exceptional outcome | Claude/Gemini | MEDIUM |
| New skill added to `SKILL_REGISTRY.json` | OER Daemon | LOW |

## ENRICHMENT PIPELINE

**1. Verification (OSF):**
All incoming raw code/data must bypass the OSF Sandbox. If Malicious → Quarantine.

**2. Deep Assimilation (OAP):**
OAP chunks the markdown documents into logical domains. It moves it to `brain/knowledge/`.

**3. Vectorization / Registration:**
OER adds the document reference into the `FAST_KNOWLEDGE_INDEX.json`.
From this moment on, AI Agents can use Semantic Search skills against this enriched metadata.

## THE GOLDEN RULE OF ENRICHMENT

The **Master Prompts** (e.g. `gemini.md`) NEVER hardcode specific knowledge text inside themselves. Instead, agents are dynamically enriched during execution by querying the Knowledge Graph (`brain/knowledge/`) using their `SKILL_REGISTRY.json` tools.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
