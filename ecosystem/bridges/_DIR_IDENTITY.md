---
id: ecosystem_bridges
type: directory_identity
namespace: ecosystem.bridges
owner: OSF_Daemon
status: hardened_v5
description: "Launch scripts and dynamic bridges acting as the strict perimeter firewall connecting OmniClaw core OBD Harbor to designated AI architectures and UI/Remote interfaces."
registered_by: OMA_AI_FORGER
tags: ["bridges", "launcher", "integration", "obd-perimeter"]
forged_at: 2026-04-11
---

# Bridges Identity

Launch scripts and dynamic bridges acting as the strict perimeter firewall connecting OmniClaw core OBD Harbor to designated AI architectures, external MCP pipelines, and UI/Remote interfaces.

---

## Chức Năng (Tiếng Việt)

Cổng gác (Bridge) và các kịch bản đánh thức (Launcher) được quản lý độc quyền bởi mỏ neo OBD (OBD Harbor). Các bridge này đóng vai trò cách ly cổng mạng, đảm bảo không có kết nối nào có thể vượt rào kết nối thẳng vào hệ sinh thái OmniClaw khi chưa được cấp phép (mở cảng) từ OBD.

## Topological View

```mermaid
graph TD
  Parent("ecosystem") --> Node("bridges")
  Node --> B1("launch_9router.py")
  Node --> B2("launch_firecrawl.py")
  Node --> B3("launch_lightrag.py")
  Node --> B4("launch_mem0.py")
  Node --> B5("launch_model_ai.py")
  Node --> B6("launch_nullclaw.py")
  Node --> B7("launch_ollama.py")
  Node --> B8("launch_omniclaw_remote.py")
  Node --> B9("launch_omniclaw_ui.py")
  Node --> B10("launch_open_notebook.py")
  Node --> B11("launch_openclaw.py")
  Node --> B12("launch_system_pulse.py")
```

---
*OmniClaw V5.0 | Forged by OMA AI Architect | ecosystem.bridges | 2026-04-11*
