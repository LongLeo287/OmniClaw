---
id: binance-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.825902
---

# KNOWLEDGE EXTRACT: binance
> **Extracted on:** 2026-03-30 17:30:49
> **Source:** binance

---

## File: `binance-skills-hub.md`
```markdown
# 📦 binance/binance-skills-hub [🔖 PENDING/APPROVE]
🔗 https://github.com/binance/binance-skills-hub


## Meta
- **Stars:** ⭐ 570 | **Forks:** 🍴 109
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto

## README (trích đầu)
```
# Binance Skills Hub

Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. Search tokens, execute trades, track wallets, monitor signals, and interact with DeFi protocols, all through natural language.

Built by Binance. Built for everyone.

We're not building this just for Binance products. Skills Hub is designed for the entire crypto ecosystem: any agent, any framework, any chain. Whether you're building on LangChain, CrewAI, or your own stack, your agents can plug into crypto with a few lines of config.

---

## About This Repository

Each skill lives in its own folder and contains a `SKILL.md` file with YAML frontmatter and structured instructions.

Browse the existing skills to understand patterns and naming conventions before contributing.

---

## Installation

Get started with Binance Skills Hub in a single command. Works with various agents such as OpenClaw and Claude Code.

### Prerequisites

Before installing Binance Skills Hub, ensure you have the following prerequisites:

* **Node.js** (version 22 or higher)

### Install Skills Hub

Run the following command to add Binance Skills Hub to your project:

```bash
npx skills add https://github.com/binance/binance-skills-hub
```

### Authentication

For Binance Skills, certain endpoints require you to provide Binance API credentials. You can do this by setting environment variables, using a secrets file (such as `.env` or `.openclaw/secrets.env`) , or sending them directly to the agent in the chat. For more details, see the [Security](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#security) section in each skill.

---

## Contribution

We welcome contributions.

To add a new skill:

1. **Fork the repository** and create a new branch:

   ```bash
   git checkout -b feature/<skill-name>
   ```

2. **Create a new folder** containing a `SKILL.md` file.

3. **Follow the required format:**

   ```markdown
   ---
   title: <Skill Name>
   description: A clear description of what the skill does and when to use it.
   metadata:
     version: <Skill Version>
     author: <Your Github Username>
   license: MIT
   ---

   # <Skill Name>

   [Add instructions, examples, and guidelines here]
   ```

4. **Open a Pull Request** to `main` for review.
   Once approved, the skill will be merged.

---

## Disclaimer

Binance Skills Hub is an informational tool only. Binance Skills Hub and its outputs are provided to you on an “as is” and “as available” basis, without representation or warranty of any kind. It does not constitute investment, financial, trading or any other form of advice; represent a recommendation to buy, sell or hold any assets; guarantee the accuracy, timeliness or completeness of the data or analysis presented. Your use of Binance Skills Hub and any information provided in connection with this feature is at your own risk, and you are solely responsible for evaluating the information provided and for all trading decisions made by
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

