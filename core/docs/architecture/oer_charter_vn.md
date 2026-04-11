---
id: oer-charter-vn
type: document
owner: SYSTEM
lang: vi
---

# OER_CHARTER.md - OmniClaw Ecosystem Registry

** :** CEO (LongLeo) | **Daemon Class:** Core Daemon #4
**  :**  14 (`registry-manager-agent`)
** :** 2026-04-02

[**🇬🇧 View in English**](OER_CHARTER.md) | [**Quay  Docs**](../README-vn.md)

---


OER (OmniClaw Ecosystem Registry)  **Core Daemon  **  OmniClaw OS.
Trong khi OIW thu , OHD    OA   — **OER    **.

OER    duy     :
-  ID duy  cho   Skill, Plugin, Agent  Workflow.
-   duy  `SKILL_REGISTRY.json` (  khai  sinh ).
- Di  artifact      `ecosystem/`.
-    Free-Pass  `brain/knowledge/`     .

No/Not...

---


OER         duy : `brain/registry/SKILL_REGISTRY.json`.
 Skill, Plugin, Agent, Workflow   trong OmniClaw   ID do OER   khi Orchestrator    .

**  ID:**
|  Asset |   ID |   |
|---|---|---|
| Skill | `SKILL-xxxx` | `SKILL-0104` |
| Plugin | `PLG-xxxx` | `PLG-0021` |
| Agent | `AGT-xxxx` | `AGT-0015` |
| Workflow | `WRK-xxxx` | `WRK-0008` |
| Department | `DEPT-xx` | `DEPT-22` |

 khi pipeline    , OER    asset    trong `SKILL_REGISTRY.json`.     , OER        ID asset   cho   .

OER    **sau khi**     sau   :
-   `OHD_CLEAN` ( cung    minh, zero IOC)
-   `OA_APPROVED` ( >= 70,   8    xem )
- `SKILL.md`  manifest     1 (Engineering) 
-  trong `storage/vault/quarantine/`   giao  

OER sau :
1.  ID duy  cho asset.
2. Sao  artifact  `quarantine/`    `ecosystem/`.
3.   `SKILL_REGISTRY.json`  metadata  .
4. Ghi receipt  `telemetry/qa_receipts/gate_oer/`.
5.   Orchestrator       .

---


```
[TRIGGER: CEO / Orchestrator / Dept Lead]
        |
 [GATE 0: OER Checking...
        |
 [GIAI  1: OIW — Thu  & Gitingest]
   - Clone repo  storage/vault/quarantine/
   -   .md qua gitingest
        |
 [GIAI  2: OHD —  Sinh &   Cung ]
   - : system/security/supply_chain_scan.ps1
   - : npm audit (JS), pip-audit (Python)
   -  : OHD_CLEAN | Timestamp
        |        \___FAIL_-> OA Blacklist + Warning.
 [GIAI  3: OA —   &  ]
   -  9 (Strix):    >= 70
   -  12 (Legal): Checking...
   - Xem  8  
   -  : OA_APPROVED | Score
        |        \___FAIL_-> OA Faculty Report + 
 [GIAI  4:  1 (Engineering) —  ]
   - : SKILL.md / plugin manifest
   - : unit tests
   -   trong: quarantine/ ( ,  )
        |
 [GIAI  5: OER —  ]
   -  ID duy 
   -   ecosystem/[tier]/
   -  : SKILL_REGISTRY.json
   - Ghi: telemetry receipt
   -  : Orchestrator "REGISTERED"
```

---


|   |  `ecosystem/` | Ghi `ecosystem/` |   Registry |
|---|---|---|---|
| **OER ( 14)** |  | ** (DUY )** | ** (DUY )** |
| OA |  ( ) | No/Not...
| OHD | No/Not...
| OIW | No/Not...
| Orchestrator |  | No/Not...
| CTO / C-Suite |  | No/Not...
|   agent  | No/Not...

---


| Daemon | Vai  | Giao cho OER |   OER |
|---|---|---|---|
| OIW | Thu   |     ly |   slot  |
| OHD |   |  `OHD_CLEAN` |    theo  |
| OA |   |  `OA_APPROVED` |   Blacklist   thi |

---

*OER Charter v1.0 — OmniClaw Corp — 2026-04-02*
