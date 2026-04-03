---
id: ki-batch02-group2-n8n-qwen
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.328499
---

# KI Batch 2 — Group 2: n8n Atom + Qwen-Agent
**Ingested:** 2026-03-21 | **Nova Batch 2** | Automation + LLM Framework

---

## KI: n8n Atom — AI-Powered Workflow Automation
**Category:** Dept 8 (Operations) | Workflow engine for OmniClaw

### What It Is
World's first n8n client inside VSCode/Cursor/Antigravity. Converts n8n workflows into **file-based format** (.n8n) for version control + AI-driven building.

n8n itself: **400+ integrations**, AI-native platform with LangChain, self-hostable.

### Key Innovation
```
Old way: Manual UI drag-n-drop → workflows in DB → no git, no AI
New way: .n8n files → git commit → AI builds/edits JSON → version control
```

### n8n (Core Platform) Capabilities
- Code when needed: JavaScript/Python + npm packages
- AI-Native: LangChain-based AI agent workflows
- 400+ integrations (Notion, Slack, Gmail, GitHub, etc.)
- 900+ workflow templates
- Self-hostable (fair-code license)

### Deployment for OmniClaw
```bash
# Quick start local
npx -y @atom8n/n8n@latest

# Docker (persistent)
docker volume create n8n_data
docker run -d --name n8n-atom -p 5888:5888 -v n8n_data:/home/node/.n8n atom8n/n8n:fork
# Editor: http://localhost:5888
```

### n8n + Antigravity = "Vibe Building"
- Antigravity edits `.n8n` JSON files directly
- AI can describe workflow in natural language → Antigravity builds it
- CEO said: "Materializes vision of VS Code as true AI cockpit"

### OmniClaw Integration
- **Dept 8 (Ops)**: Primary workflow automation engine for OmniClaw
- **setup-n8n repo**: Already have n8n setup config in knowledge store
- **Nova intake**: n8n webhook → Nova receives new data automatically
- **Workflows to build**: 
  - CEO Standing Order intake automation
  - Dept-request routing webhook
  - Synthesis log auto-update

---

## KI: Qwen-Agent — Alibaba's Agent Framework
**Category:** Dept 13 (R&D) + Dept 21 (Agent Dev) | Alternative LLM backend

### What It Is
Framework for developing LLM applications using Qwen models. Tool use + planning + RAG + memory. Powers Qwen Chat production app.

**Latest**: Qwen3.5 (Feb 2026) + DeepPlanning benchmark + MCP support

### Core Architecture
```python
# Minimal agent with tools + PDF
bot = Assistant(
    llm={'model': 'qwen-max-latest'},
    function_list=['code_interpreter'],  # Built-in tools
    files=['doc.pdf']  # Can read files directly
)
```

### Standout Features for OmniClaw

#### 1. MCP Native Support
```python
pip install qwen-agent[mcp]
# Configure any MCP server in mcpServers config
# → Connects to OmniClaw MCP cluster instantly
```

#### 2. 1M Token Document QA (CRITICAL for Nova)
```
Fast RAG solution: outperforms native long-context on benchmarks
→ Nova can query entire codebases (1M tokens) efficiently
```

#### 3. Parallel Function Calls (default)
- Multiple tools called simultaneously → faster agent execution
- Supports ReActChat + FnCallAgent patterns

#### 4. Local Deployment via Ollama
```python
llm_cfg = {
    'model': 'qwen3-32b',
    'model_server': 'http://localhost:11434/v1',  # Ollama
    'api_key': 'EMPTY',
}
```
→ Can route through OmniClaw API Bridge (port 7000) with OpenAI-compatible API

### OmniClaw Integration  
- **LLM Router**: Add Qwen models to OmniClaw routing (currently Claude/Gemini/Ollama)
- **Nova's 1M doc QA**: Use Qwen RAG for large repo/document intake
- **Dept 21 training**: Qwen-Agent framework as additional agent design pattern
- **Qwen3.5 demo**: `examples/assistant_qwen3.5.py` → reference implementation

### Config for API Bridge
```python
llm_cfg = {
    'model': 'qwen3-32b',
    'model_server': 'http://localhost:7000/v1',  # OmniClaw API Bridge!
    'api_key': 'EMPTY',
}
```

---

## Routes
| Repo | Department | Priority |
|------|-----------|----------|
| n8n Atom | Dept 8 (Ops) − deploy immediately | HIGH |
| Qwen-Agent | Dept 13 (Nova) − 1M doc QA + router addition | MEDIUM |
