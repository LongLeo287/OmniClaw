---
id: system-overview-vn
type: document
owner: SYSTEM
lang: vi
---


OmniClaw          , bao  **28 " Ban"    **      AI Agent      qua     .

[**🇬🇧 View in English**](system_overview.md) | [**Quay    Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---


    ta     Loading...

1. **CEO ( 0)**:    (). Cung      cao.
2. **Orchestrator / C-Suite ( 1)**:    Agent  (vd: Antigravity).     ,     ,     .
3. **  Ban ( 2)**:  LLM Agent       `rules/`  (vd: QA Manager, Frontend Engineer, CIV Chief).
4. **Subagent   ( 3)**:  Agent     sinh ra   thi logic   (vd: git-protector, doc-parser)   sau khi  .


  file trong `ecosystem/workforce/`  chia   AI   ranh   :
- **`agents/`**:  116      .
- **`subagents/`**:  37      .
- **`departments/`**:   28  ban theo   huy.
- **`system/`**:     —   code  thi.    prompt   (`corp_prompts/`)     Daemon (`daemons/`).


          qua     (`brain/`):

- **`blackboard.json`**:         .  Agent A     ,    blackboard  Agent B (QA Testing)         .
- **RAG &   Tri **:       graph-DB (`brain/knowledge`)         tham     .


Trong  28  Ban,    quan   :
- ** 01 (Engineering)**:    ,  code,   .
- ** 10 (Strix Security)**:   plugin, xem  payload,       (Zero Trust).
- ** 20 (CIV - Content Intake)**:   GitHub repo, PDF,   web    cho Graph Local Memory.
- ** 22 (Operations)**:      git sync, hook sao   quy  deep cleaner.

> *    JSON  cho  , AI tham  `brain/corp/org_chart.yaml`  `AGENTS.md`.*
