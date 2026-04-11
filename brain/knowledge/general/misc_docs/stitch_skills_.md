---
id: ki-stitch-skills-2026-03-25
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.767592
---

# KI Note â€” google-labs-code/stitch-skills
# Type: REPO | Source: https://github.com/google-labs-code/stitch-skills
# CIV Ticket: CIV-2026-03-25-002
# Intake Date: 2026-03-25
# Value Type: SKILLS (CRITICAL) â€” Google official Stitch agent skills

---

## Summary

**stitch-skills** lÃ  repo chÃ­nh thá»©c tá»« Google Labs chá»©a các agent skills cho Stitch MCP. 7 skills sáºµn sÃ ng dùng vá»›i `npx skills add`.

---

## Available Skills

| Skill | Description: | Relevance |
|-------|-------|-----------|
| `stitch-design` | Unified entry point â€” prompt enhancement + design system + Stitch MCP | â­â­â­ CRITICAL |
| `stitch-loop` | Multi-page website tá»« 1 prompt | â­â­â­ CRITICAL |
| `design-md` | Táº¡o DESIGN.md tá»« Stitch project | â­â­â­ HIGH |
| `enhance-prompt` | Vague â†’ polished Stitch-optimized prompt | â­â­â­ HIGH |
| `react-components` | Stitch screens â†’ React component systems | â­â­ HIGH |
| `remotion` | Walkthrough videos tá»« Stitch project | â­ MED |
| `shadcn-ui` | shadcn/ui integration expert | â­â­ MED |

---

## Install

```bash
# Install all Stitch skills globally
npx skills add google-labs-code/stitch-skills --skill stitch-design --global
npx skills add google-labs-code/stitch-skills --skill stitch-loop --global
npx skills add google-labs-code/stitch-skills --skill design-md --global
npx skills add google-labs-code/stitch-skills --skill enhance-prompt --global
```

---

## CIV Assessment

| Criterion | Score | Notes |
|-----------|-------|-------|
| Relevance to OmniClaw | 10/10 | CEO Ä‘ang dùng Stitch MCP |
| Security risk | NONE | Official Google source |
| Integration effort | LOW | npx install |
| Value type | SKILLS |  |

**Verdict:** âœ… APPROVE â€” Install táº¥t cáº£, Ä‘áº·c biá»‡t `stitch-design` + `stitch-loop` + `enhance-prompt`

---

## Action Items

- [ ] Run: `npx skills add google-labs-code/stitch-skills --skill stitch-design --global`
- [ ] Run: `npx skills add google-labs-code/stitch-skills --skill stitch-loop --global`
- [ ] Run: `npx skills add google-labs-code/stitch-skills --skill enhance-prompt --global`
- [ ] Run: `npx skills add google-labs-code/stitch-skills --skill design-md --global`
- [ ] Add entries to `brain/registry/SKILL_REGISTRY.json`
- [ ] Register in `kho/plugins/registry.json`

---

*KI Note v1.0 | CIV-2026-03-25-002 | Intake: Antigravity | 2026-03-25*

