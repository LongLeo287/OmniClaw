---
id: data-packaging-sync-vn
type: document
owner: SYSTEM
lang: vi
---


[**🇬🇧 View in English**](data_packaging_sync.md) | [**Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

   end-to-end  sao       Brain, State  Memory  OmniClaw,      ba hub cloud: **HuggingFace**, **Google Drive**,  **GitHub**.     quy     No/Not...

---

    Git repository        No/Not...

Script     thao  vault    :
**`system/ops/scripts/omniclaw_data_push.py`**

  minh     ba      :
1. `brain/memory/` (Long-term Agent Experience Memory)
2. `storage/vault/` (Library of Raw Extracted Data and Media Assets)
3. `ecosystem/plugins/` (Third-Party Repositories and Agent Source Code)

 asset     an   **HuggingFace Dataset**  **Google Drive** Vault .

> **⚠️ Warning.

---

Khi    fork  clone OmniClaw  Github, `storage/vault`  `brain/memory`     .
 Loading...
**`python system/ops/scripts/omniclaw_data_pull.py`**

Script    `snapshot_download`  HuggingFace  RClone `copy`  **    rehydrate**      . Links  No/Not...

---

   commit code GitHub , quy      sao  "active session soul"   chat    Operator.

**Script  Thi:**
```bash
powershell -ExecutionPolicy Bypass -File system\ops\scripts\memory\backup_soul.ps1
```

**  :**
1. Sao  file `.pb`        Agent  .
2. Thu gom   logic    trong   `brain/`   UUID .
3. Payload        file Zip : `soul_backup.zip`.
4. Sau khi  phong xong, file  dock an    buffer     .  sau  Operator    push Git Commit  .

---

Ngay khi Operator   **Git Push**   code   `main`, hai Guardian GitHub Actions CI   :

- **`.github/workflows/omniclaw-tests.yml`:**   Checking...
- **`.github/workflows/omniclaw-validate.yml`:**  qua metadata   quan   `SKILL_REGISTRY.json`    YAML agent.    Skill   AI code           , No/Not...

---

        Git Push   theo     .      OmniClaw     .

