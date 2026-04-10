---
id: ki-batch03-claude-mem
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.574339
---

# KI: claude-mem â€” Auto Memory cho Claude Code Sessions

## Metadata
- **Source:** https://github.com/thedotmack/claude-mem
- **Category:** Claw Variant / Memory / Plugin
- **Priority:** ðŸ”´ CRITICAL â€” Giáº£i quyáº¿t memory/context problem
- **Ingested:** 2026-03-21
- **Batch:** 03

## TÃ³m Táº¯t
Plugin Claude Code tá»± Ä‘á»™ng **capture táº¥t cáº£ hÃ nh Ä‘á»™ng** trong session, compress báº±ng AI (claude-agent-sdk), vÃ  inject láº¡i relevant context vÃ o future sessions. **215 Releases** â€” actively maintained.

## CÆ¡ Cháº¿ Hoáº¡t Äá»™ng
1. **Capture** â€” Tá»± Ä‘á»™ng ghi láº¡i má»i thá»© Claude lÃ m trong session
2. **Compress** â€” DÃ¹ng AI Ä‘á»ƒ tÃ³m táº¯t vÃ  nÃ©n thÃ´ng tin
3. **Store** â€” LÆ°u memories theo project/context
4. **Inject** â€” ÄÆ°a relevant context vÃ o session má»›i tá»± Ä‘á»™ng

## TÃ­nh NÄƒng
- Automatic capture (no manual effort)
- AI compression (claude-agent-sdk)
- MCP Search Tools â€” tÃ¬m memories tá»« session cÅ©
- Beta: Advanced memory retrieval
- TÃ­ch há»£p vá»›i **OpenClaw Gateway** (ðŸ¦ž)
- Windows setup support

## Architecture
- Hook vÃ o Claude Code session lifecycle
- Persistent memory store
- Semantic search qua MCP tools

## LiÃªn Quan OmniClaw  
- **CRITICAL CONNECTION**: Giáº£i quyáº¿t Ä‘Ãºng Problem: "máº¥t context" giá»¯a sessions
- TÆ°Æ¡ng tá»± nhÆ°ng **tá»± Ä‘á»™ng hÆ¡n** `brain/memory/blackboard.json`
- Káº¿t há»£p vá»›i `pre-session.md` â†’ inject memory tá»± Ä‘á»™ng
- CÃ³ thá»ƒ thay tháº¿/bá»• sung cho manual `hot-cache.md` system

## Comparison vá»›i OmniClaw hiá»‡n táº¡i
| Feature | OmniClaw (Manual) | claude-mem (Auto) |
|---------|---------------|-------------------|
| Session capture | Manual viáº¿t vÃ o blackboard | Auto capture |
| Compression | Manual summarize | AI compressed |
| Injection | pre-session.md (manual read) | Auto inject |
| Search | Manual | MCP search tools |

## OmniClaw Action
```
STATUS: ðŸ”´ CRITICAL â€” Evaluate vÃ  test cÃ i vÃ o Claude Code
COMMAND: npx @thedotmack/claude-mem (check actual install method)
BENEFIT: Giáº£i quyáº¿t context loss giá»¯a Claude sessions
```

