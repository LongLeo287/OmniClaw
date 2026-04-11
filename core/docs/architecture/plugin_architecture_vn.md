---
id: plugin-architecture-vn
type: document
owner: SYSTEM
lang: vi
---


OmniClaw     Plugin 3           an .  code    internet,   file  ,   thi script      qua   .

[**🇬🇧 View in English**](plugin_architecture.md) | [**Quay    Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---


    trong   `system/ops/`.       AI   "" —     , sinh subagent,   `blackboard.json`.

 trong   `ecosystem/plugins/`.           ba   qua quy  **CIV (Content Intake)**        `SKILL_REGISTRY.json`.
- ** :** Git scraper   , RAG vector injector, Terminal shell tool.
- **Quy :**  khi    plugin  2 ,  10 (Strix Security)   payload     .

 server      **Model Context Protocol (MCP)**.
- OmniClaw    MCP Host    Connecting...
-     OS       ba,    trong sandbox  . AI     schema    .

---


   **V5.0**,   `ecosystem/plugins/`   vai   **"Kho " (Cold Storage)  **. 
       tham , metadata  code .

**  Server           ** (vd:   `docker-compose up -d`     )    RAM       ro.
Thay  , OmniClaw   theo   **"  -  " (Opt-In / Air-Gapped)**:
1. **  Harbor:**  Plugin  lai   Docker ( `Firecrawl` hay `Mem0`),        file Bridge  trong `ecosystem/bridges/` (vd: `launch_firecrawl.py`).
2. **   tay:**  khi    ( Harbor)       ,  file Bridge      `docker compose up <service>`.
3. **   :** Ngay khi   , Bridge     `docker compose stop <service>`   ,     Container         .

   skill  plugin cho OmniClaw,    quy   Giao   3 :
1. ** Ly:** Code plugin  (do R&D  OIW )     `storage/vault/quarantine/`.
2. **   ( 10):** Agent   (`strix-agent`) Checking...
3. **  ( 14):**  Registry Manager (`registry-manager-agent`)    file-level  di  code    `ecosystem/skills/`,   schema       `SKILL_REGISTRY.json`. No/Not...

---


 14 (`registry-manager-agent`)   **"  Do Truy "**  `brain/knowledge/`:
* ** :**  14   ,             `brain/knowledge/` thay  cho  plugin    . ** agent  thi  , CTO, Orchestrator,  plugin   No/Not...
* **   :**   `ecosystem/`  `brain/knowledge/`      :   **   **.        xem,  No/Not...
