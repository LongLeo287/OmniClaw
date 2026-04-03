# SKILL: OpenClaw Core Tools
# Competence: Worker & Manager
# Description: A powerful CLI toolkit that allows Agents to surf the web, run code, or manage memory.

## Settings & Requirements
- For agents running in environments with the `openclaw` CLI installed.
- Confirm the tool is available on your device with the command `npx openclaw status` (if using locally) or call `openclaw` directly.

## Use

### 1. Browser & Surfing the Web (Browser & Search)
You can reliably read the content of a URL:
```bash
openclaw tools call web_fetch url="https://example.com"
```
Scan search content (Semantic Search):
```bash
openclaw tools call web_search query="latest framework changes"
```

### 2. Safe Shell Code Execution (Exec)
```bash
openclaw tools call exec command="ls -la"
```

### 3. Memory Indexing
If you change the memory file in the `/memory/` directory, you need to tell OpenClaw to run the index again for Vector Search to work:
```bash
openclaw memory index
```

### 4. Semantic Search in Internal Memory
If you need to review old lessons related to a Topic:
```bash
openclaw memory search "cognitive reflection concept"
```

## Attention (Vietnamese)
> **For Agents (Self-reflection):** This is a very deep system tool. Only use when there is a clear directive or when LLM's built-in tools are not capable enough (for example, need to bypass captcha, need to load Vector DB).
