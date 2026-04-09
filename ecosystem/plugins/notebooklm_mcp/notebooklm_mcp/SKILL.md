---
id: notebooklm_mcp
name: NotebookLM MCP Gateway
version: 1.2.1
tier: 2
status: active
author: OmniClaw OMA
updated: 2026-04-05
domain: core
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
  - Antigravity
dependencies: []
exposed_functions:
  - name: list_notebooks
    description: Fetch the list of available notebooks in NotebookLM.
    input: "none"
    output: "json (array of notebooks)"
  - name: ask_notebooklm
    description: Ask questions and extract information from Google NotebookLM via Gemini/Claude.
    input: "string (query), string (notebook_id)"
    output: "string (answer text and citations)"
consumed_by:
  - knowledge_enricher
  - orchestrator_pro
emits_events:
  - notebooklm_query_completed
listens_to:
  - trigger_notebook_sync
tags: [knowledge, mcp, google-workspace, rag]
---

# NotebookLM MCP Gateway (Skill)

## 📌 Overview
This skill allows OmniClaw to connect with **Google NotebookLM** via the Model Context Protocol (MCP). Agents can directly leverage NotebookLM's massive document parsing capabilities (PDFs, Videos, Docs) and use the Gemini API to extract knowledge without being constrained by local agent context limits.

## ⚙️ Agent Guidelines
1. **Initialize Connection**: The MCP protocol is implemented via Node.js (`src/index.ts` in `CIV/RECALL_notebooklm_mcp`). Ensure you have the appropriate API keys or `.env` configuration.
2. **Invoke Commands**:
   - To retrieve available documents/notebooks: Call `list_notebooks`.
   - To analyze or ask a question about a large file: Call `ask_notebooklm`.
3. **Citation Analysis**: The results include citations. Aggregate them properly and provide accurate references when responding to the User.

## ⚠️ Technical Notes (OER/OHD Guardrails)
- Do not make abusive repetitive calls. Batch queries if possible to avoid Rate Limits.
- Audio and Video files are natively supported by NotebookLM. Delegate multimedia parsing directly to NotebookLM instead of using a standalone audio skill!
