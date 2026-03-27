# Headroom Context Compression â€” API Bridge Integration Plan
# Source: awesome-llm-apps KI | Target: API Bridge port 7000 | Nova 2026-03-21

## Background
**Headroom** lÃ  LLM optimization tool giáº£m API costs **50-90%** qua intelligent context compression.
Há»— trá»£ MCP, persistent memory, vÃ  lÃ  drop-in wrapper cho existing API calls.

## Cost Problem
AI OS API Bridge (port 7000) routes táº¥t cáº£ LLM calls. Náº¿u khÃ´ng compress context:
- Long sessions (nhÆ° Nova CEO intake) â†’ massive token usage
- Multi-agent workflows â†’ context duplicated qua nhiá»u agents
- 100 repo ingestion batch â†’ cÃ³ thá»ƒ tá»‘n nhiá»u API budget

## Headroom Architecture

```
                        Before Headroom:
Agent â†’ [Full Context 100k tokens] â†’ LLM API â†’ Cost $$$$

                        After Headroom:
Agent â†’ [Full Context] â†’ Headroom Compressor â†’ [Compressed 10-50k] â†’ LLM API â†’ Cost $
                                              â†“
                                    [Persistent Memory Cache]
                                    [MCP Memory Server]
```

## Integration Points vá»›i AI OS

### Option A: Middleware táº¡i API Bridge (Port 7000)
```
                AI OS API Bridge (:7000)
                â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
Agent calls â†’ â”‚  Route â†’ LLM Router     â”‚
              â”‚  â”‚                       â”‚
              â”‚  â–¼                       â”‚
              â”‚  Headroom Compressor     â”‚ â† INSERT HERE
              â”‚  â”‚                       â”‚
              â”‚  â–¼                       â”‚
              â”‚  LLM Provider (Ollama/   â”‚
              â”‚  Claude/Gemini/etc.)     â”‚
              â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### Option B: Per-Agent Wrapper (Nova-specific)
- Nova wraps calls vá»›i Headroom trÆ°á»›c khi gá»­i Ä‘áº¿n API bridge
- Tiáº¿t kiá»‡m cho long-running intake sessions

### Option C: MCP Memory Server (Recommended)
- Headroom expose MCP server â†’ AI OS MCP cluster Ä‘á»c compressed + cached context
- Agents share compressed context â†’ khÃ´ng ai pháº£i re-send full context

## Implementation Steps

### Step 1: Install Headroom
```bash
# CÃ i tá»« awesome-llm-apps pattern
pip install headroom-context
# hoáº·c check repo: advanced_llm_apps/llm_optimization_tools/headroom_context_optimization/
```

### Step 2: Configure for API Bridge
```python
# Trong <AI_OS_ROOT>\api-bridge\main.py (hoáº·c tÆ°Æ¡ng Ä‘Æ°Æ¡ng)
from headroom import HeadroomCompressor

compressor = HeadroomCompressor(
    compression_ratio=0.5,      # Target: 50% compression
    persistent_memory=True,     # Cache across sessions
    mcp_enabled=True,           # Expose via MCP
    mcp_port=7010               # Headroom MCP on port 7010
)

# Wrap LLM calls
def route_to_llm(context, model):
    compressed = compressor.compress(context)
    return llm_router.call(compressed, model)
```

### Step 3: Cost Monitoring
```python
# Log cost savings má»—i request
compressor.log_savings()  
# Output: "Saved 67% tokens | Original: 45k | Compressed: 14.8k"
```

## Projected Savings (AI OS Estimate)

| Use Case | Tokens/Session | Savings 60% | Monthly Est. |
|----------|---------------|-------------|--------------|
| Nova CEO intake | 50k | 30k saved | Significant |
| Multi-agent routing | 20k | 12k saved | Medium |
| Batch 2 repo scan | 200k | 120k saved | High |
| **Total estimate** | ~1M/month | **~600k saved** | **$$$ significant** |

## Action Items
- [ ] Locate Headroom source tá»« awesome-llm-apps repo
- [ ] Review headroom_context_optimization/ directory
- [ ] Test táº¡i Nova's own API calls trÆ°á»›c (safe sandbox)
- [ ] Deploy vÃ o API bridge port 7000 sau khi test
- [ ] Monitor cost dashboard (ClawTask port 7474)

## LiÃªn káº¿t
- Source: `brain/knowledge/repos/awesome-llm-apps/` â†’ `advanced_llm_apps/llm_optimization_tools/headroom_context_optimization/`
- API Bridge config: `<AI_OS_ROOT>\` (check running process)
- Port 7000 = Universal REST API Bridge (confirmed active)

