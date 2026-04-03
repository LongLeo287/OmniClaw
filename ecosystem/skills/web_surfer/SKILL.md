---
name: web-surfer
description: Deep Web Surfing skill for Agent.
---

# Web Surfer Skill
**Origin:** Extracted from Awesome-Agent-Skills repository.

## Description
Empowers Sub-Agent to call browser tools (like Puppeteer, Playwright, or MCP Browser) to look up the open web instead of relying solely on training data.

## Usage
- When prompt requests "Research...", Agent automatically parses Keyword and calls `Browser_Tool`.
- Ability to read HTML DOM and transform into clean Markdown structure.

## Rules
1. **Ad Filter:** Will be blocked at URLs containing spam or gambling flags, only access Wikipedia, Official Docs, Github, StackOverflow.
2. **No Deep Click (Max Depth 2):** Only click to inner page links, do not click to 3rd level to avoid infinite loops.
