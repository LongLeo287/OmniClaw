---
id: memory_corp_gaps
type: gap_repository
namespace: brain.memory.corp_memory.gaps
owner: OSF_Daemon
status: standard_v5
description: "Volatile complaint box for agents to document missing skills and tool gaps."
registered_by: OA_Auditor
---

# `corp_memory/gaps` Identity (System Anomalies)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory acts as the architectural feedback loop for AI Workers. 
> Files inside (`GAP_<Task>.md`) are generated automatically by agents when they encounter unrecoverable blockers (Circuit Breakers).

## 1. Compliance Rules
- Because these are granular, short-lived bug reports intended for the Architectural Daemon, they are classified as **Volatile Cache**.
- By `.gitignore` Rule 13, all gap reports (except the template) are blocked from GitHub sync.