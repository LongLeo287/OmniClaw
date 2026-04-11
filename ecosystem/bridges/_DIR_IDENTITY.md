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

## Core Function

Launch scripts acting as gateways managed exclusively by the OBD Harbor. These bridges enforce port isolation and ensure no external connections can bypass the OBD perimeter without explicit authorization.

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
