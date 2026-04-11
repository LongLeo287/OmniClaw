---
id: oap-architecture-vn
type: document
owner: SYSTEM
lang: vi
---


[**🇬🇧 View in English**](OAP_ARCHITECTURE.md) | [**Quay    Docs**](../README-vn.md)


**Pipeline   OER (OAP)**    trao   trung   OmniClaw OS.    quy        (repository, knowledge drop, code )      "Assimilated Node"    cao ,         trong   Brain.

  daemon  script        OmniClaw    5 giai    . Sai         .

---


- **Actor:** `civ_intake_processor.py` / `sandbox_intake_pipeline.py`
- ** :**  ➔ `vault/quarantine`
- **Quy :**
  -       internet    .
  -      quarantine  sandbox_env.
  - No/Not...

- **Actor:** `osf_malware_censor.py` (   OSF Quarantine Guard)
- ** :** `vault/quarantine`
- **Quy :**
  - OSF    script   quy      `OSF_THREAT_INTELLIGENCE.json`.
  - Checking...
  - ** :**
    - `0` (/Pass):  sang Giai  3.
    - `1` (/Fail):  Pipeline.   OHD  Vaporization.

- **Actor:** `oa_inbox_triage.py` (   OA)
- ** :** `vault/tmp/state_queues/OER_INBOX`
- **Quy :**
  -   an     INBOX .
  - OA  hash       .
  - Deduplication  ra       logic.

- **Actor:** `oa_swallow_engine.py` (  Swallow)
- ** :** `vault/tmp/state_queues/OER_INBOX`
- **Quy :**
  -      scrape,      quy.
  - Boilerplate No/Not...
  -       Markdown   cao: `*_DISTILLED.md`.
  -      OMA Robo Purger  .

- **Actor:** `oma_knowledge_mapper.py` & `skill_loader.ps1`
- ** :** `brain/knowledge/assimilated_repos/` & `ecosystem/skills/`
- **Quy :**
  -  tri            .
  -   `_DIR_IDENTITY.md`       node con.
  - `SKILL_REGISTRY.json`  `LIBRARY_GRAPH.json`      .

---

Pipeline OAP   OmniClaw  ,     No/Not...

>   script trong `core/ops/scripts`  Git repository   OSF  khi  . No/Not...

---


      ("file pollution")      Ouroboros  , Daemon     extension file      artifact   :

- ** :** File  No/Not...
- **Quy :** No/Not...

- ** :**
  1. `[RepoName]_DISTILLED.md`: Logic/      .
  2. `_DIR_IDENTITY.md`:     .
- **Quy :** File code  (`.py, .js`) ** **   trong  Brain.

- ** :**
  1. `SKILL.md`: Plugin markdown  thi .
  2. `*.json` (Registry): `SKILL_REGISTRY.json`, `LIBRARY_GRAPH.json`, `OSF_THREAT_INTELLIGENCE.json`.
- **Quy :**  file JSON  MD   node     .    cho      OmniClaw.

*  file No/Not...
