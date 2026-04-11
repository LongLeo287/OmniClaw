---
id: CAPABILITY-MAP-001-vn
type: REFERENCE
domain: [system, skills, plugins, discovery]
dept: all
lang: vi
created: 2026-03-22
version: 1.0
authority: registry_capability
---


> ** :** `knowledge_navigator`  file  trong Giai  3   skill/plugin  cho  domain tag thay    .
>       ~65% → ~90% khi  CAPABILITY_MAP + LightRAG.

[**🇬🇧 View in English**](SKILLS_MAP.md) | [**Quay    Docs**](../README-vn.md)

---


```
  (Giai  1): knowledge_navigator  CAPABILITY_MAP.md → 90%  
 THEO (Giai  2): LightRAG graph index   SKILL.md + manifest.json → 95%+
                          : python ops/scripts/index_skills_lightrag.py
 LAI (Giai  3):     GitNexus →      
                           : npx gitnexus analyze (trong OmniClaw root)
```

---


### ai_ml (AI/ML, LLM, RAG, Embeddings)
| Nhu  |  |  |   |
|------|-----|------|------|
|   tri  / RAG | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
| Graph-based RAG | `LightRAG` | plugin | plugins/LightRAG/ |
|     | `open-notebook` | plugin | plugins/open-notebook/ |
|     | `notebooklm-skill` | plugin | plugins/notebooklm-skill/ |
|     | `multi-source-aggregation` | skill | ecosystem/skills/multi-source-aggregation/ |
|   +   | `reasoning_engine` | skill | ecosystem/skills/reasoning_engine/ |
|    | `cognitive_reflector` | skill | ecosystem/skills/cognitive_reflector/ |
|   LLM | `llm_router` | skill | ecosystem/skills/llm_router/ |
| NLP +     | `langextract` | plugin | plugins/langextract/ |

### backend (Python, API, FastAPI, Node.js)
| Nhu  |  |  |   |
|------|-----|------|------|
| Shell + scripts | `shell_assistant` | skill | ecosystem/skills/shell_assistant/ |
| QA production | `production_qa` | skill | ecosystem/skills/production_qa/ |
| Lint   | `fsd_architectural_linter` | skill | ecosystem/skills/domains/frontend/ |
| Resilience + retry | `resilience_engine` | skill | ecosystem/skills/resilience_engine/ |
| Profiling   | `performance_profiler` | skill | ecosystem/skills/performance_profiler/ |
|   | `diagnostics_engine` | skill | ecosystem/skills/diagnostics_engine/ |

### web_frontend (React, Vue, HTML, CSS, UI)
| Nhu  |  |  |   |
|------|-----|------|------|
|  UI/UX | `visual_excellence` | skill | ecosystem/skills/visual_excellence/ |
|  UI PRO | `ui-ux-pro-max` | plugin | plugins/ui-ux-pro-max/ |
| Accessibility | `accessibility_grounding` | skill | ecosystem/skills/accessibility_grounding/ |
| SEO/AEO | `seo-aeo-optimization` | skill | ecosystem/skills/seo-aeo-optimization/ |

| Nhu  |  |  |   |
|------|-----|------|------|
| Shell + deployment | `shell_assistant` | skill | ecosystem/skills/shell_assistant/ |
| Resilience | `resilience_engine` | skill | ecosystem/skills/resilience_engine/ |
|   | `diagnostics_engine` | skill | ecosystem/skills/diagnostics_engine/ |
| Deploy Cloudflare | `cloudflare-skills` | plugin | plugins/cloudflare-skills/ |
| Deploy Vercel | `vercel-agent-skills` | plugin | plugins/vercel-agent-skills/ |

### cybersecurity (CVE, pentest, OWASP, secrets)
| Nhu  |  |  |   |
|------|-----|------|------|
|  GATE_SECURITY | `security_shield` | skill | ecosystem/skills/security_shield/ |
|   repo | `skill_sentry` | skill | ecosystem/skills/skill_sentry/ |
|     | `zeroleaks` | plugin | plugins/zeroleaks/ |
| Theo  CVE | `cybersecurity` | skill | ecosystem/skills/cybersecurity/ |
|  Cert | `cerberus-cve-tool` | plugin | plugins/cerberus-cve-tool/ |

### marketing (SEO, content, social, campaigns)
| Nhu  |  |  |   |
|------|-----|------|------|
| Web intelligence | `web_intelligence` | skill | ecosystem/skills/web_intelligence/ |
| SEO/AEO | `seo-aeo-optimization` | skill | ecosystem/skills/seo-aeo-optimization/ |
|    | `channel_manager` | skill | ecosystem/skills/channel_manager/ |
|   | `notification_bridge` | skill | ecosystem/skills/notification_bridge/ |

| Nhu  |  |  |   |
|------|-----|------|------|
|     | `reasoning_engine` | skill | ecosystem/skills/reasoning_engine/ |
|   tri  | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
|   Web | `web_intelligence` | skill | ecosystem/skills/web_intelligence/ |

| Nhu  |  |  |   |
|------|-----|------|------|
| Theo  chi  | `cost_manager_skill` | skill | ecosystem/skills/domains/finance/ |
|     | `performance_profiler` | skill | ecosystem/skills/performance_profiler/ |
|     | `insight_engine` | skill | ecosystem/skills/insight_engine/ |

### knowledge_mgmt (KI, memory, index, graph)
| Nhu  |  |  |   |
|------|-----|------|------|
|   tri  | `knowledge_navigator` | skill | ecosystem/skills/knowledge_navigator/ |
|   tri  | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
|   () | `cosmic_memory` | skill | ecosystem/skills/cosmic_memory/ |
|   ( ) | `smart_memory` | skill | ecosystem/skills/smart_memory/ |
|   ( kinh) | `neural_memory` | skill | ecosystem/skills/neural_memory/ |
|   | `archivist` | skill | ecosystem/skills/archivist/ |
| Graph RAG | `LightRAG` | plugin | plugins/LightRAG/ |
|   context | `context_manager` | skill | ecosystem/skills/context_manager/ |

| Nhu  |  |  |   |
|------|-----|------|------|
|  skill | `skill_generator` | skill | ecosystem/skills/skill_generator/ |
| Sentry skill | `skill_sentry` | skill | ecosystem/skills/skill_sentry/ |
|  agent | `orchestrator_pro` | skill | ecosystem/skills/orchestrator_pro/ |
|     | `proposal_engine` | skill | ecosystem/skills/proposal_engine/ |

| Nhu  |  |  |   |
|------|-----|------|------|
|   code | `gitnexus-exploring` | skill | tools/gitnexus-web/gitnexus/skills/ |
|     | `gitnexus-impact-analysis` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Truy  bug | `gitnexus-debugging` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Refactoring | `gitnexus-refactoring` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Review PR | `gitnexus-pr-review` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Truy  Cypher graph | `gitnexus-cli` | skill | tools/gitnexus-web/gitnexus/skills/ |

---


|   |     |    |
|-----------|-----------|---------| 
|        | `LightRAG` (mix mode) | 95%+ |
|   quan  code | `GitNexus` (cypher) | 95%+ |
|     plugin | `GitNexus` (impact tool) | 90%+ |
|   qua  | `cosmic_memory` / `smart_memory` | 85%+ |
| Web scraping | `web_intelligence` / `langextract` | 85%+ |
|    (repo) | `security_shield` / `zeroleaks` | 95%+ |
|  UI | `visual_excellence` / `ui-ux-pro-max` | 90%+ |
|   tri  | `knowledge_enricher` + `open-notebook` | 90%+ |
|   agent | `orchestrator_pro` / `corp_orchestrator` | 90%+ |
|    CEO | `notification_bridge` | 99%+ |

---


```
   CHO: < >
    │
    ├─  AI/RAG/Memory?        → LightRAG, knowledge_enricher, open-notebook
    ├─  code/repo?            → GitNexus (explore/impact/debug/refactor)
    ├─   ?              → security_shield, zeroleaks, skill_sentry
    ├─  UI?                   → visual_excellence, ui-ux-pro-max
    ├─  deployment?           → shell_assistant, cloudflare-skills, vercel-agent-skills
    ├─     ?   → langextract, web_intelligence, knowledge_enricher
    ├─   ?               → cosmic_memory → smart_memory → LightRAG
    └─ No/Not...
                                  Checking...
```

---

*    v1.0 | 2026-03-22 |   : registry-manager-agent*
*Checking...
