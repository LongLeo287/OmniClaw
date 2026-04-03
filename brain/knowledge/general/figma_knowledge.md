---
id: figma-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:24.136303
---

# KNOWLEDGE EXTRACT: figma
> **Extracted on:** 2026-03-30 17:37:00
> **Source:** figma

---

## File: `mcp-server-guide.md`
```markdown
# 📦 figma/mcp-server-guide [🔖 PENDING/APPROVE]
🔗 https://github.com/figma/mcp-server-guide
🌐 https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server

## Meta
- **Stars:** ⭐ 661 | **Forks:** 🍴 51
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A guide on how to use the Figma MCP server

## README (trích đầu)
```
# Figma MCP Server Guide

The Figma MCP server brings Figma directly into your workflow by providing important design information and context to AI agents generating code from Figma design files.

> [!NOTE]
> Rate limits apply to Figma MCP server tools that read data from Figma. Some tools, such as those that write to Figma files, are exempt from the rate limits.
> <br><br>
> Users on the Starter plan or with View or Collab seats on paid plans will be limited to up to 6 tool calls per month.
> <br><br>
> Users with a [Dev or Full seat](https://help.figma.com/hc/en-us/articles/27468498501527-Updates-to-Figma-s-pricing-seats-and-billing-experience#h_01JCPBM8X2MBEXTABDM92HWZG4) on the [Professional, Organization, or Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features) have per minute rate limits, which follow the same limits as the Tier 1 [Figma REST API](https://developers.figma.com/brain/knowledge/docs_legacy/rest-api/rate-limits/). As with Figma’s REST API, Figma reserves the right to change rate limits.

For the complete set of Figma MCP server docs, see our [developer documentation](https://developers.figma.com/brain/knowledge/docs_legacy/figma-mcp-server/). By using the Figma MCP server and the related resources (including these skills), you agree to the [Figma Developer Terms](https://www.figma.com/legal/developer-terms/). These skills are currently available as a Beta feature.

## Features

- **Write to the canvas** (remote server only): Create and modify native Figma content directly from your MCP client. With the right skills, agents can build and update frames, components, variables, and auto layout in your Figma files using your design system as the source of truth.

    **Note:** We're quickly improving how Figma supports AI agents. The write to canvas feature will eventually be a usage-based paid feature, but is currently available for free during the beta period.

- **Generate code from selected frames**

  Select a Figma frame and turn it into code. Great for product teams building new flows or iterating on app features.

- **Extract design context**

  Pull in variables, components, and layout data directly into your IDE. This is especially useful for design systems and component-based workflows.

- **Code smarter with Code Connect**

  Boost output quality by reusing your actual components. Code Connect keeps your generated code consistent with your codebase.

  [Learn more about Code Connect →](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect)

- **Generate Figma designs from web pages** *(rolling out)*

  Capture, import, or convert a web page into a Figma design directly from your AI coding agent.

## Installation & Setup

### Connect to the Figma MCP server

Different MCP clients require slightly different setups. Follow the instructions below for your specific client to connect to the Figma MCP server.

#### VS Code

1. Use the shortcut `⌘ Shift P` to search for `MCP:Add Server`.
2. Select `HTTP`.
3. Paste t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

