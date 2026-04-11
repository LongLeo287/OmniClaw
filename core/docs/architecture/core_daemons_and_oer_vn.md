---
id: core-daemons-oer-vn
type: document
owner: SYSTEM
lang: vi
---


> ** :** CEO (LongLeo) | ** :** 5.0 | **:** 2026-04-11
> ** :**    —    thay         sinh   .

[**🇻🇳 View in English**](core_daemons_and_oer.md) | [**Quay  Docs**](../README-vn.md)

     **8 Core Daemons**  OmniClaw OS  **Pipeline   Zero-Trust**      Skill, Plugin, Agent  Workflow gia   sinh .

---


     vi  Zero-Trust,    sinh       qua 8 Agent   (Daemon)  trong 3  ban     (`system_daemons`, `system_health`, `system_security`):

| Node ID | Designation | Vai  Chung |  Ban |
| :--- | :--- | :--- | :--- |
| **`oma_architect`**| OmniClaw Map Architect |     | `system_daemons` |
| **`oap_pipeline`** | Omnibus Assimilation |   Pipeline | `system_daemons` |
| **`oer_registry`**| OmniClaw Ecosystem Registry |     | `system_daemons` |
| **`oiw_intake`** | OmniClaw Intake Worker | Thu   | `system_daemons` |
| **`osf_warden`** | OmniClaw Sandbox Firewall |     | `system_security` |
| **`ohd_healer`** | OmniClaw Health Daemon |     | `system_health` |
| **`oa_academy`** | OmniClaw Academy |    Thi | `system_daemons` |
| **`obd_harbor`** | OmniClaw Bridge Daemon | Harbor Master /    | `system_security` |

---


|   | OMA | OAP | OER | OIW | OSF | OHD | OA | OBD |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|      &  danh | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
|   Triage | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
|   `REGISTRY.json` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Clone   / Thu  | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
|    Ly ( ) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
|  File (Lint/Auto-Heal) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
|  tich logic &   | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
|   Localhost / Bridges | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

> [!CAUTION]
> **  Zero-Trust**:   8 Daemons             .   daemon         , Orchestrator      ngay  .

---


    5.0, **OBD (OmniClaw Bridge Daemon)**            Connecting...
* **No/Not...
* **  `127.0.0.1`:**   toang `0.0.0.0`        khi     API Gateway cho   truy .
* **  MCP:**  module   qua `stdio`  Claude/Cursor     danh               .

Chi       (Bridge), tham  `ecosystem/bridges/README-vn.md`.

---

*Core Daemons v5.0 — OmniClaw Corp — 2026-04-11*
