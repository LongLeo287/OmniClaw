# 🧩 OmniClaw Ecosystem Plugins

**Plugins** act as the external augmentation modules and third-party integrations for the OmniClaw Artificial Intelligence Operating System (`v5.0`). 

While OmniClaw Core is strictly self-contained, this directory houses massive specialized external systems (RAG Engines, MCP Servers, Vectors Databases, Web Scrapers) that extend AI capabilities.

[🇻🇳 Xem bản Tiếng Việt (Vietnamese)](README-vn.md)

---

## 🛑 Ecosystem Golden Rules

1. **Passive Storage Only!**
   Plugins located here are typically *libraries* or *static binaries*. Do NOT execute background network servers directly from this folder.
   If a plugin requires an active Web Server, API Interface, or Daemon loop (e.g., LightRAG, Mem0, Ollama, Firecrawl), it **MUST** be launched and orchestrated exclusively via the `ecosystem/bridges/` directory to adhere to the OBD Harbor Firewall rules.
2. **Zero-Trust Boundaries:**
   Plugins are considered "External". If a plugin fails, crashes, or is corrupted, it must never take down the Core OS. Never tightly couple OmniClaw's central loop to rely on a specific plugin.
3. **Spec Compliance:**
   If you download or write a custom tool to put here, it must follow `plugin_spec.md`. Keep documentation strictly English for Machine Readers.

---

## 🛠️ Navigating the Catalogs

This directory contains master logs recording hundreds of AI tools evaluated by The System:
* **`plugin_catalog.md`**: Approved/Pending/Archived specific logic and architecture plugins.
* **`master_repo_catalog.md`**: A master ledger of raw Github Repositories scraped for future integration. 

*OmniClaw V5.0 | Core Ecosystem Documentation*
