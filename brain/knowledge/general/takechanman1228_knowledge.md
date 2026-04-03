---
id: takechanman1228-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:20.921375
---

# KNOWLEDGE EXTRACT: takechanman1228
> **Extracted on:** 2026-03-30 17:54:14
> **Source:** takechanman1228

---

## File: `claude-ecom.md`
```markdown
# 📦 takechanman1228/claude-ecom [🔖 PENDING/APPROVE]
🔗 https://github.com/takechanman1228/claude-ecom


## Meta
- **Stars:** ⭐ 17 | **Forks:** 🍴 3
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skill that turns order or sales CSV data into business reviews, with KPI decomposition, prioritized findings, and next actions powered by a Python backend.

## README (trích đầu)
```


<p align="center">
  <img src="assets/banner.png" alt="Claude Ecom" width="100%">
</p>

# claude-ecom

Turn order/sales CSV into a business review — KPI decomposition, prioritized findings, and concrete next actions. One command.

<p align="center">
  <img src="assets/claude_ecom_demo.gif" alt="claude-ecom demo" width="100%">
</p>

---

## Who This Is For

- Data Analysts / Marketers who write monthly business reviews from scratch every time
- D2C brand owners, retail managers, or ecommerce managers without an analyst on staff
- Anyone who knows revenue dropped but can't explain why

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/takechanman1228/claude-ecom/v0.1.3/install.sh | bash

# Drop your orders CSV, Start Claude Code, and run:
/ecom review
```

Requires: Claude Code CLI, Python 3.10+, and git

### Alternative: Install as a Claude Code plugin

```
/plugin marketplace add takechanman1228/claude-ecom
/plugin install claude-ecom@claude-ecom
/reload-plugins
```

Restart Claude Code. The Python backend installs automatically on session start.
The command becomes `/claude-ecom:ecom review` when installed as a plugin.

## What You Get

A single `REVIEW.md` that reads like a consultant wrote it:


```
# Business Review
> Revenue reached $9.37M for the year, essentially flat YoY (-1.7%), despite strong
> short-term momentum — the last 90 days surged 84% and November posted +28.5%,
> both driven by Q4 seasonal demand rather than structural growth. The flat annual...
```

```
           30d Pulse       90d Momentum     365d Structure
Revenue    $1.47M (+ 28%)  $3.73M (+ 84%)   $9.37M (= -2%)
Orders     3,499 (+ 26%)   8,814 (+ 60%)    24,812 (- 11%)
AOV        $419 (+ 2%)     $424 (+ 15%)     $378 (+ 10%)
Customers  1,676 (+ 11%)   2,918 (+ 51%)    4,296 (= flat)
...
```
```
Revenue $9.37M (YoY: -1.7%)
├── 🔴 New Customer Revenue $1.45M (15.5%)
│   ├── New Customers: 1,559 (-57.8%)
│   └── New Customer AOV: $305
└── 🟢 Existing Customer Revenue $7.92M (84.5%)
    ├── Returning Customers: 2,737 (+345%)
    ├── Returning AOV: $395
    └── Repeat Purchase Rate: 75.4%
```
Executive summary → Multi-horizon dashboard → KPI trees with 🔴/🟢 signals → Findings with "what / why / what to do" → Prioritized action plan with deadlines, success metrics, and guardrails.
[See a full example output →](examples/online-retail-ii/REVIEW.md)


## Commands

| Command | Description |
|---------|-------------|
| `/ecom review` | Full business review — auto-selects 30d / 90d / 365d |
| `/ecom review 30d` / `90d` / `365d` | Focus on a specific period |
| `/ecom review How's retention?` | Ask a question instead of a full report |

## Input

Any e-commerce/retail orders CSV works. 

Required columns: order ID, order date, customer ID or email, revenue (after discounts, before tax/shipping).
Optional (enables deeper analysis): quantity, SKU or product name, discount amount. In many cases, column names don't need to match exactly.


## How It Works


```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

