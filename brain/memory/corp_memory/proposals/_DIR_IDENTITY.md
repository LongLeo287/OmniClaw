---
id: memory_corp_proposals
type: proposal_repository
namespace: brain.memory.corp_memory.proposals
owner: USER_CEO
status: standard_v5
description: "CEO Inbox for agent proposals. Orchestrator scans for approvals."
registered_by: OA_Auditor
---

# `corp_memory/proposals` Identity (CEO Inbox)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory handles Architectural Proposals submitted by AI to the CEO. 
> The Orchestrator automatically tracks this folder. When the CEO marks `[x] APPROVE` in any markdown file, it generates an implementation task and moves the document to `brain/archive/proposals/`.