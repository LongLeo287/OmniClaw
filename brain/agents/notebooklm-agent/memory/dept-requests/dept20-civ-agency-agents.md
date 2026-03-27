# CIV Vetting Report â€” agency-agents
**Dept 20 (CIV) | Date:** 2026-03-21 | **Analyst:** Nova (Dept 13 â†’ Dept 20)
**Repo Path:** `<AI_OS_ROOT>\brain\knowledge\repos\agency-agents\`

---

## ðŸ“š Sources
ðŸ“š Sources: 1 repo | Types: GitHub OSS | Date: 2026-03-21
ðŸ”§ Tool: Manual read (README.md + directory scan)
ðŸ¢ Dept: Dept 20 (CIV) â†’ Dept 4 (Registry) â†’ Dept 21 (Agent Dev)

---

## 1. Repo Overview
| Field | Value |
|-------|-------|
| **Repo** | agency-agents |
| **Loáº¡i** | AI Agent Persona Library |
| **License** | MIT (open source) |
| **Há»— trá»£ Antigravity** | âœ… Native (`./scripts/install.sh --tool antigravity`) |
| **Privacy Tier** | PUBLIC â€” OSS, khÃ´ng nháº¡y cáº£m |
| **Strix Scan** | ChÆ°a cháº¡y (xem má»¥c 4) |

## 2. Content Analysis
- **144 agent files** chia thÃ nh 12 divisions (folders)
- **Format:** Markdown `.md` (SKILL.md-compatible)
- **Scope:** Engineering, Design, Marketing, Sales, Specialized, Game Dev, etc.
- **KhÃ´ng cÃ³:** binary files, API keys, hardcoded credentials

## 3. AI OS Alignment
| Division | Depts Phá»¥c Vá»¥ | Priority |
|---------|--------------|---------|
| specialized/ (24 agents) | Dept 13, 20, 8, 18 | HIGH |
| engineering/ (23 agents) | Dept 1, 3, 10, 21 | HIGH |
| support/ (6 agents) | Dept 8, 18, 19 | MEDIUM |
| product/ (5 agents) | Dept 17, 13 | MEDIUM |
| marketing/ (25 agents) | Dept 5 | LOW-MEDIUM |
| game-development/ (17 agents) | N/A hiá»‡n táº¡i | LOW |

## 4. Risk Assessment
| Risk | Level | Mitigation |
|------|-------|-----------|
| Malicious code | LOW | Markdown only, no executables |
| Data leakage | NONE | No credentials/PII |
| Strix scan | PENDING | Run Strix CLI scan before full activation |
| Prompt injection via agent personas | LOW | Review agent SYSTEM prompts before use |

## 5. CIV Verdict

> **âœ… APPROVED â€” Conditional**
>
> agency-agents Ä‘Æ°á»£c phÃ©p deploy vÃ o AI OS vá»›i Ä‘iá»u kiá»‡n:
> 1. Chá»‰ install **specialized/ + engineering/ + support/** (72 files â€” low risk)
> 2. Run Strix scan trong vÃ²ng 7 ngÃ y â†’ upload káº¿t quáº£ Dept 10
> 3. Dept 4 Ä‘Äƒng kÃ½ chÃ­nh thá»©c vÃ o plugin registry

## 6. Proposed Install Path
```
<AI_OS_ROOT>\plugins\agency-agents\     â† Plugin directory (D: drive)
â”œâ”€â”€ SKILL.md
â”œâ”€â”€ specialized/ (24 agents)
â”œâ”€â”€ engineering/ (23 agents)
â””â”€â”€ support/ (6 agents)
```

**Routing:** â†’ Dept 4 (Registry) Ä‘á»ƒ Ä‘Äƒng kÃ½ â†’ CEO approval deploy

