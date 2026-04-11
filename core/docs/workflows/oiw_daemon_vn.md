---
id: oiw-daemon-vn
type: document
owner: SYSTEM
lang: vi
---

# OmniClaw Ingestion Daemon (OID) V2.5

> ** :**   
> **:** System Automation (Daemon)
> **  :** `registry-manager-agent` & `intake-chief-agent`

[**🇬🇧 View in English**](oiw_daemon.md) | [**Quay    Docs**](../README-vn.md)

---


**OmniClaw Ingestion Daemon (OID)**    kinh     trung   OmniClaw.  thay   script       **Pipeline 8 Giai **     .

OID     daemon    (`omniclaw_oid_daemon.py`).       vault    "ticket" tri  ,    dung  tham  (URL, GitHub Repo,  ),    ,   tri ,    registry OmniClaw,    **   **    lao  (sinh Agent  Skill ).

**  :**
- **Zero-Trust Security:**       ly     Strix  khi    .
- **Zero-Token Overhead:** Routing, deduplication,    ban     qua script     (No/Not...
- **Auto-Evolution:**   sinh Agent    (`create_agent.py`)    Meta-Skill (`Skill Creator Ultra`)          .

---


Khi ticket   `storage/vault/DATA/`, daemon  thi  sau:

- Daemon   poll `storage/vault/DATA/`  file `KI-*.json`  .
- File    an . JSON No/Not...

- Ticket       index `0`  `ACCEPTED_Q`.
-     , ticket No/Not...
- Sau `MAX_RETRIES = 3`, ticket      `REJECTED_Q`  xem   .

- MD5 hashing URL/Repo       No/Not...

- Pattern matching  Domain/Category   cho   No/Not...
-   output: `ai_ml`, `frontend`, `marketing`, `security`.

- Daemon  script Pwsh (`system/security/QUARANTINE/vet_repo.ps1`)  sandbox   repository.
- Code  → `vetted/repos/` | Code   →    trong `QUARANTINE/isolation/`.

OID  thi   fetch        100%:
- **  1:** Shallow Native Git Clone (Nhanh )
- **  2:** Full Native Git Clone
- **  3:** Github API Zipball  ( qua block Git port/IP)

- `registry_indexer.py`:  Repo  Agent  `system/registry/SYSTEM_INDEX.yaml`.
- `ki_indexer.py`:  artifact tri    Graph trung  (`brain/knowledge/KI_INDEX.md`).

-  Domain         , OID   Agent Scaffolding.
-  thi `create_agent.py`  sinh Agent   -3     domain .

-      Dashboard CEO qua `blackboard.json`.
-  Warning.

-   `omniclaw_cleanup_crew.py`   ticket `.json`     OS .

---


```powershell
$env:OMNICLAW_ROOT = "D:\LongLeo\OmniClaw CORP\OmniClaw"
python system/automations/daemons/omniclaw_oid_daemon.py
```

1.  file JSON ticket: `storage/vault/DATA/KI-TEST-001.json`
2.   tin ticket:
```json
{
  "id": "TICKET-999",
  "source": "https://github.com/example/awesome-python-plugin",
  "triage": { "domain": "backend_engineering" }
}
```
3. Theo  OID logs trong terminal  xem pipeline 8 giai   thi real-time.

1.  link  GitHub shortcode  URL  OmniClaw Telecom Bot.
2. `telegram_dispatch.py`      ticket    `storage/vault/DATA/`.

---


- **Log File:** `system/automations/daemons/logs/oid_daemon.log`
- **Hash Database:** `system/automations/daemons/oid/processed_hashes.json`
- **  Error.

> *     Antigravity | OmniClaw V3.1*

