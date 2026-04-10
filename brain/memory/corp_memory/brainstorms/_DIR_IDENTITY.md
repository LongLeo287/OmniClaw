---
id: memory_corp_brainstorms
type: memory_buffer
namespace: brain.memory.corp_memory.brainstorms
owner: OSF_Daemon
status: standard_v5
description: "Volatile storage for multi-agent brainstorming sessions and raw ideation."
registered_by: OA_Auditor
---

# `corp_memory/brainstorms` Identity (Ideation Buffer)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory contains volatile brainstorming logs generated dynamically by agents.
> - Logs must flow according to the `brainstormtemplate.md` structure.
> - Output files (except templates/identity) are excluded from Git to prevent repository bloat.

## 1. Directory Purpose
Functions as a short-term creative workspace room. When multiple agents (e.g., from the Strategy or R&D departments) are brought together to solve a complex problem or innovate, they dump their raw ideas, discussions, and directions here before finalizing them into a formal Proposal.

## 2. Compliance Rules
- Files inside this directory are temporary working documents. 
- The master template `brainstormtemplate.md` must be retained unchanged.