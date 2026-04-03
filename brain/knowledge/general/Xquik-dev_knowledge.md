---
id: xquik-dev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.289921
---

# KNOWLEDGE EXTRACT: Xquik-dev
> **Extracted on:** 2026-03-30 18:01:19
> **Source:** Xquik-dev

---

## File: `x-twitter-scraper.md`
```markdown
# 📦 Xquik-dev/x-twitter-scraper [🔖 PENDING/APPROVE]
🔗 https://github.com/Xquik-dev/x-twitter-scraper
🌐 https://xquik.com

## Meta
- **Stars:** ⭐ 23 | **Forks:** 🍴 1
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
X (Twitter) data platform skill for AI coding agents. 99 REST API endpoints, 9 MCP tools, 20 extraction types, HMAC webhooks. Reads from $0.00015/call — 66x cheaper than the official X API. Works with Claude Code, Cursor, Codex, Copilot, Windsurf & 40+ agents.

## README (trích đầu)
```
# X API / Twitter Scraper Skill for AI Coding Agents

An [AI agent skill](https://skills.sh) that gives coding agents deep knowledge of the [Xquik](https://xquik.com) X (Twitter) real-time data platform. 99 REST API endpoints, 9 MCP tools, HMAC webhooks, 20 bulk extraction tools, and write actions.

**The cheapest X data API on the market** — reads from $0.00015/call (66x cheaper than the official X API).

Works with **40+ AI coding agents** including Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, Windsurf, VS Code, Cline, Roo Code, Goose, Amp, Augment, Continue, OpenHands, Trae, OpenCode, and more.

## Pricing

Xquik is dramatically cheaper than every alternative for X/Twitter data access.

### vs Official X API

| | Xquik | X API Basic | X API Pro |
|---|---|---|---|
| **Monthly cost** | **$20** | $100 | $5,000 |
| **Cost per tweet read** | **$0.00015** | ~$0.01 | ~$0.005 |
| **Cost per user lookup** | **$0.00015** | ~$0.01 | ~$0.005 |
| **Write actions** | **$0.0003** | Limited | Limited |
| **Bulk extraction** | **$0.00015/result** | Not available | Not available |
| **Monitoring + webhooks** | **Free** | Not available | Not available |
| **Giveaway draws** | **$0.00015/entry** | Not available | Not available |
| **MCP server** | **Included** | Not available | Not available |

### Per-Operation Costs (1 credit = $0.00015)

| Operation | Credits | Cost |
|-----------|---------|------|
| Read (tweet, user, search, timeline, bookmarks, etc.) | 1 | $0.00015 |
| Follow check, article | 7 | $0.00105 |
| Write (tweet, like, retweet, follow, DM, etc.) | 2 | $0.0003 |
| Extraction / draw | 1/result | $0.00015/result |
| Monitors, webhooks, radar, compose, drafts, integrations | 0 | **Free** |

### Pay-Per-Use (No Subscription)

Two options for pay-per-use without a monthly subscription:

- **Credits (Stripe)**: Top up credits via `POST /credits/topup` ($10 minimum). 1 credit = $0.00015. Works with all 99 endpoints.
- **MPP (USDC)**: 8 X-API read endpoints accept anonymous payments via Machine Payments Protocol. No account needed. SDK: `npm i mppx`.

## Installation

Install via the [skills CLI](https://skills.sh) (auto-detects your installed agents):

```bash
npx skills add Xquik-dev/x-twitter-scraper
```

### Manual Installation

<details>
<summary>Claude Code</summary>

```bash
git clone https://github.com/Xquik-dev/x-twitter-scraper.git .claude/skills/x-twitter-scraper
```
</details>

<details>
<summary>Codex / Cursor / Gemini CLI / GitHub Copilot</summary>

```bash
git clone https://github.com/Xquik-dev/x-twitter-scraper.git .agents/skills/x-twitter-scraper
```
</details>

<details>
<summary>Windsurf</summary>

```bash
git clone https://github.com/Xquik-dev/x-twitter-scraper.git .windsurf/skills/x-twitter-scraper
```
</details>

<details>
<summary>Cline</summary>

```bash
git clone https://github.com/Xquik-dev/x-twitter-scraper.git .agents/skills/x-twitter-scraper
```
</details>

<details>
<summary>Roo Code</summary>

```bash
git c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

