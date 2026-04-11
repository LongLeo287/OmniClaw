---
id: data-intake-vn
type: document
owner: SYSTEM
lang: vi
---



 sinh  OmniClaw   theo   Zero-Trust  .  code   ba, repository,  plugin     sandbox   trong `system/security/QUARANTINE_INCOMING`   qua     khi  thi.  `git clone`   `/brain`  `/ecosystem/plugins/`           . Thay  ,    `gitingest`  `gitnexus`    codebase repository   file `.md`  `.txt` ,  khi commit    tri .

        an ,    pipeline CIV do  20 (CIV)   10 (Strix)  .

[**🇬🇧 View in English**](data_intake.md) | [**Quay    Docs**](../README-vn.md)


1. **   :**   URL    repository     corpus OmniClaw.
2. ** :**  URL     danh      danh  theo  `storage/vault/DATA/Github.txt`.
3. **  :**      minh          quan    repository.
   ```ps1
   python system/ops/scripts/omniclaw_deep_evaluator.py
   ```
4. **  Pipeline  :**  thi pipeline   . Script    repository  No/Not...
   ```ps1
   python system/ops/scripts/active_repos_pipeline.py
   ```


* **No/Not...
* **   :** Pipeline      Markdown  code sang      cho LLM  RAG engine.


         source code     repository  clone, :

```ps1
python system/ops/scripts/omniclaw_repo_analyzer.py
```

* ** :**    tri  `.md`    `brain/knowledge/processed_repos/`.
* **  (ARCHIVE):**    source code  sang vault     `storage/vault/ARCHIVE/`     Github   repository  to.
* **  (Knowledge Cleanup):**  ,  `python system/ops/scripts/clean_knowledge.py`       AI/ML,    UI   danh    trong `brain/knowledge/`.
