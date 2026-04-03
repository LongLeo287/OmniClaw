---
id: ki-reference-misc-01
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.742991
---

# KI-REFERENCE-MISC-01 — Miscellaneous Reference Notes
**Source:** gitagent, wtfjs, gitignore, agentql, tinyfish-cookbook, archon, ag-live-code, seeaifirst, pattern-craft, plotly.js, zixfelw/ag-live-code
**Date:** 2026-03-23 | **Verdict:** REFERENCE — quick notes per repo

---

## agentql (tinyfish-io) — GraphQL-like Web Query

### Pattern: Structured Web Extraction
'''python
# Instead of parsing HTML manually:
from agentql import query

# Define structure with GraphQL-like syntax
result = query("""
{
    products {
        name
        price
        rating
        in_stock
    }
}
""", url="https://shop.example.com")
'''
**OmniClaw:** Firecrawl already covers this. Know this pattern if structured extraction is needed outside of Firecrawl.

---

## Archon (coleam00) — OmniClaw Reference Architecture

### Archon OS Structure (to learn from)
'''
Archon/
├── knowledge/      # Persistent knowledge base (OmniClaw: brain/)
├── tasks/          # Task queue (OmniClaw: ClawTask)
├── agents/         # Agent definitions (OmniClaw: brain/agents/)
├── tools/          # Tool wrappers (OmniClaw: tools/)
└── memory/         # Memory layer (OmniClaw: Mem0 + LightRAG)
'''
**Takeaway:** OmniClaw Corp's structure is similar to Archon's. Validated approach. No changes needed.

---

## TinyFish Cookbook (tinyfish-io) — n8n + AgentQL Patterns

### n8n Workflow Patterns for OmniClaw
'''
Trigger: Webhook or Schedule
   ↓
HTTP Request Node → Firecrawl API
   ↓
Code Node → Process data (Python/JS)
   ↓
OpenAI/Claude Node → Analyze
   ↓
Slack/Email Node → Notify
'''
**OmniClaw Application:** DEFER Phase 6 — n8n as an automation layer for recurring Corp tasks.

---

## wtfjs (denysdovhan) — JavaScript Edge Cases

### Top OmniClaw–relevant JS quirks to remember:
'''javascript
// KNOW THESE TO AVOID BUGS:

// 1. typeof null === 'object'  (NOT 'null'!)
typeof null === 'object'  // true — always use `=== null` check

// 2. NaN is not equal to itself
NaN === NaN  // false — use Number.isNaN()

// 3. String + Number
'5' + 3    // '53' (string concat, NOT 8)
'5' - 3    // 2   (coercion to number for -)

// 4. Array sort is alphabetical by default
[1, 10, 9, 2].sort()      // [1, 10, 2, 9] — WRONG!
[1, 10, 9, 2].sort((a,b) => a-b)  // [1, 2, 9, 10] — correct

// 5. 0.1 + 0.2 !== 0.3
0.1 + 0.2 === 0.3  // false → use toFixed() or decimal libraries
'''
**OmniClaw:** Apply when the agent writes JavaScript. The framework-standards skill should reference these.

---

## gitignore (github/gitignore) — Templates

### Use when creating a new project:
'''bash
# Node.js project
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore

# Python project
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

# Combined (Node + Python)
wget https://www.toptal.com/developers/gitignore/api/node,python,macos,windows

# OmniClaw specific ignores (add manually):
echo "ops/secrets/\n*.env\nbrain/private/\ntelemetry/logs/*.log" >> .gitignore
'''

---

## pattern-craft (megh-bari) — CSS Patterns

Use the web tool directly (do not clone the repo):
'''
URL: https://patterncraft.fun
→ Select pattern → Copy CSS → Paste into stylesheet
'''
Patterns: Dots, Lines, Crosshatch, Waves, Hexagons, Triangles...

---

## plotly.js — Data Visualization

### When OmniClaw needs charts (use CDN, don't clone):
'''html
<script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
<script>
Plotly.newPlot('myDiv', [{
    x: dates,
    y: kpi_values,
    type: 'scatter',
    mode: 'lines+markers',
    name: 'OmniClaw KPIs'
}], {
    title: 'OmniClaw Corp KPI Dashboard',
    template: 'plotly_dark'
});
</script>
'''
**OmniClaw:** Use for KPI visualization dashboard (Dept 9 Analytics).

---

## ag-live-code (zixfelw — VN dev)

Live code viewer integrated with Antigravity — the agent can stream code changes in real-time.
**Status:** Track repo — evaluate when a real-time code collaboration feature is needed.

*KI Note v1.0 | 2026-03-23 | Consolidated misc references*
