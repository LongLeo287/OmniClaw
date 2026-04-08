---
id: knowledge_map
title: OmniClaw Knowledge Base — Topology Map
authority: OA
version: 1.0.0
created: 2026-04-06
status: ACTIVE
---

# 🗺️ OmniClaw Knowledge Base — Topology Map

**Authority:** OA Daemon | **Registry:** OER | **Physical:** OHD
**Location:** `D:\LongLeo\OC\brain\knowledge\` (~6.8 GB post-cleanup)

---

## Architecture Overview

```
OmniClaw OS
└── brain/
    └── knowledge/                     [ROOT — NO_TOUCH — OER]
        ├── general/                   [5,882 MB — 3,274 files]
        │   ├── *_knowledge.md (1,433) ← standard crawled KD
        │   ├── github.com_*_knowledge.md (849) ← github crawled KD
        │   ├── tech_reports/   (34)   ← bug reports, issue analysis
        │   ├── lightrag_docs/  (3)    ← LightRAG documentation
        │   ├── web_perf_guide/ (8)    ← web performance guides
        │   └── misc_docs/      (933)  ← unclassified docs
        │       └── omniclaw_internal/ (69) ← OC internal docs
        │
        ├── repositories/              [925 MB — 227 repos]
        │   ├── FETCHED_ClawWork_*     [474 MB — OC own project]
        │   ├── FETCHED_courses_*      [88 MB  — AI courses]
        │   ├── FETCHED_deeplake_*     [60 MB  — vector DB]
        │   ├── FETCHED_codebuff_*     [45 MB  — AI editor]
        │   ├── FETCHED_Docs_*         [65 MB  — claude docs]
        │   ├── FETCHED_FlashRAG_*     [36 MB  — RAG system]
        │   └── ... 221 more repos
        │
        ├── api/                       [935 MB — 3 API repos]
        │   ├── repo_litellm/          [935 MB — LLM proxy]
        │   ├── repo_hotkeys/          [~3 MB  — hotkeys]
        │   └── repo_kittentts/        [~0.1 MB — TTS]
        │
        ├── repos/                     [Junction Links — 624 entries]
        │   └── → storage/vault/ARCHIVE/ (0 broken)
        │
        ├── library/          [30 MB]  ← curated docs
        ├── bmad_repo/        [1.2 MB] ← BMAD methodology
        ├── skills_standard_repo/ [0.6 MB] ← skills standard
        ├── claude_bp_repo/   [0.5 MB] ← Claude best practices
        ├── corp/             [0.4 MB] ← corporate KB
        ├── frameworks/       [6.5 MB] ← deer_flow, hermes_agent
        ├── repo_godi13hub_io/ [20 MB] ← GodiHub site snap
        ├── repo_hyperspace_db/ [6 MB] ← HyperSpace DB
        │
        └── Domain Knowledge (47 folders, ~1 MB total):
            ai_ml/ | architecture/ | agent_architecture/
            security/ | cybersecurity/ | networking/ | web/
            data/ | automation/ | devops/ | design/
            dev_tooling/ | iot/ | it_infra/ | performance/
            media/ | corp_feeds/ | notes/ | catalog/
            distilled/ | project_learnings/ | strategy/
            rd_ingest/ | staging/ | updates/ | system_health/
            legacy/ | CIV/ | ui/
```

---

## Department → Knowledge Base Connections

```
OmniClaw Org
├── od_learning        ──HAS_ACCESS_TO──► knowledge_base  [training domain]
├── rd                 ──HAS_ACCESS_TO──► knowledge_base  [research domain]
├── engineering        ──HAS_ACCESS_TO──► knowledge_base  [technical reference]
├── content_intake     ──HAS_ACCESS_TO──► knowledge_base  [content processing]
├── content_review     ──HAS_ACCESS_TO──► knowledge_base  [review reference]
├── archivist          ──HAS_ACCESS_TO──► knowledge_base  [archive/index]
├── asset_library      ──HAS_ACCESS_TO──► knowledge_base  [asset registry]
├── registry_capability──HAS_ACCESS_TO──► knowledge_base  [OER indexing]
│                      ──OWNS──────────► knowledge_base  [governance]
└── operations         ──MANAGES_PHYSICAL► knowledge_base [OHD physical]
```

---

## Registry Coverage Map

| Category | Skills | Coverage |
|---|---|---|
| Knowledge Packs (`general/`) | 2,814 | ✅ 100% |
| Fetched Repos (`repositories/` + `api/` + `frameworks/` + `repo_*/`) | 268 | ✅ 100% |
| Curated Docs | 7 | ✅ 100% |
| Domain KB folders | 17 | ✅ 100% |
| System skills (brain non-knowledge) | 6 | ✅ 100% |
| **TOTAL SKILL_REGISTRY** | **3,788** | **✅ 100%** |

---

## Data Flow

```
External Source
      │
      ▼
  OIW Intake ──► brain/knowledge/repositories/ [FETCHED]
      │
      ▼
  Knowledge Crawler ──► brain/knowledge/general/ [KNOWLEDGE_DUMP .md]
      │
      ▼
  OA/OER Vetting ──► ecosystem/skills/*/schema.json [REGISTERED]
      │
      ▼
  SKILL_REGISTRY.json [3,788 entries indexed]
      │
      ▼
  FAST_INDEX.json [3,111 entries fast-lookup]
      │
      ▼
  Departments via ORG_GRAPH edges [HAS_ACCESS_TO: knowledge_base]
```

---

## Storage Topology

```
Local (Primary Working Copy):
  D:\LongLeo\OC\brain\knowledge\  [6.8 GB]

Remote Primary Storage:
  HuggingFace Dataset: longleo/omniclaw-knowledge-base [public/private dataset]
  Google Drive: OmniClaw/knowledge/ [shared drive mount]

Git:
  EXCLUDED — brain/knowledge/ folders in .gitignore
  Boundary rule: brain/rules/KNOWLEDGE_BASE_BOUNDARY.md
```

---

## Key Policies

| Rule | Value |
|---|---|
| Modification | OER approval required |
| Deletion | PROHIBITED without OER + OA joint approval |
| Git commit | NEVER |
| Fragmentation | PROHIBITED (keep in place decision 2026-04-06) |
| Sync trigger | Manual — on significant content change |
| Audit cycle | After each major intake batch |
