---
name: MaxKB Knowledge Base Platform
tier: 2
source: https://github.com/1Panel-dev/MaxKB
version: latest
status: ingested
ingested: 2026-03-17
security: PASS (manual review - 9 false positives: CJK i18n unicode + standard Vue JWT auth)
---

# MaxKB — Enterprise AI Knowledge Base & RAG Platform

## What It Is
MaxKB ("Max Knowledge Brain") is an open-source platform for building enterprise AI agents with a complete RAG pipeline. 20k+ GitHub stars. Stack: Vue.js + Python/Django + LangChain + PostgreSQL/pgvector.

## Core Capabilities

### RAG Pipeline
- Upload documents / crawl web automatically
- Auto text splitting, vectorization, indexing
- Reduce LLM hallucination, high quality Q&A

### Agentic Workflow Engine
- Visual workflow builder (drag & drop)
- Integrated function library
- **MCP tool-use support** — compatible with the OmniClaw MCP ecosystem
- Complex AI Orchestration without code

### Model Support (Model-Agnostic)
- Private: DeepSeek, Llama, Qwen (via Ollama)
- Public: OpenAI, Claude, Gemini, AWS Bedrock
- Multi-modal: text, image, audio, video

### Knowledge Base Features
- Multi-type: General / Web / Lark / Workflow KB
- Tag management, batch export
- Embedding + reranker models

## OmniClaw Integration

### Connect to OmniClaw
- **RAG Agent**: `subagents/rag-specialist/` can use MaxKB as a backend
- **MCP Bridge**: MaxKB MCP support → integration with `tools/mcp_ecosystem_overview.md`
- **Complement**: NexusRAG (high-perf local) + MaxKB (enterprise UI + multi-user) = RAG duo
- **Deploy**: Docker-based, integrated with `devops-agent`

### Activation (local deploy)
```bash
# Deploy via Docker
docker compose up -d

# Or via 1Panel app store with Ollama + Llama 3
```

## Use Cases in OmniClaw
- Enterprise knowledge search agent
- Internal company Q&A bot with beautiful UI
- Multi-user knowledge base with decentralization
- Scientific research agent backend (used with claude-scientific-skills)

## Security Notes
- 9 CRITICAL → all confirmed FALSE POSITIVES:
  - `localStorage.getItem` = Vue.js JWT session management (standard)
  - Unicode escapes = CJK/Chinese i18n strings in TypeScript
- No crypto miners, no real cookie theft, no supply chain attack