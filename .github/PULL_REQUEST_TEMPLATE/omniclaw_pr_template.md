[**🇻🇳 Xem Phiên Bản Tiếng Việt (Vietnamese)**](omniclaw_pr_template-vn.md)

---
name: Pull Request
about: Submit a patch, tool, or agent upgrade
---

[**🇻🇳 Xem Phiên Bản Tiếng Việt (Vietnamese)**](omniclaw_pr_template-vn.md)

## 🛠 Area of Update
- [ ] Core Infra (Tier 1) / Bootstrapper
- [ ] Plugin / Tool (Tier 2/3)
- [ ] Agent Roster / Role / Prompt
- [ ] System Rules / Governance (`SOUL.md`, `GEMINI.md`, etc.)
- [ ] Knowledge Injection / RAG Memory

## 📖 Description
Please briefly explain what this update does and why it is necessary.

## ✅ Checklist (Mandatory)
- [ ] Code has been scanned for security (No embedded API keys / Personal Passwords / `.env`).
- [ ] New features DO NOT execute Root OS commands directly unless explicitly authorized (`SafeToAutoRun` strict policies).
- [ ] (If New Plugin) Strict adherence to the Lazy-Load 3-Tier architecture.
- [ ] Updated `SKILL_REGISTRY.json` or `AGENTS.md` (if applicable).

## 🧠 Communication Impact (CEO Facing)
Does this update change how the CEO commands the system?
(If yes, briefly explain the new command / new information flow).
