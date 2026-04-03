---
id: uscensusbureau-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:39.845287
---

# KNOWLEDGE EXTRACT: uscensusbureau
> **Extracted on:** 2026-03-30 17:58:06
> **Source:** uscensusbureau

---

## File: `us-census-bureau-data-api-mcp.md`
```markdown
# 📦 uscensusbureau/us-census-bureau-data-api-mcp [🔖 PENDING/APPROVE]
🔗 https://github.com/uscensusbureau/us-census-bureau-data-api-mcp
🌐 https://www.census.gov

## Meta
- **Stars:** ⭐ 57 | **Forks:** 🍴 19
- **Language:** TypeScript | **License:** CC0-1.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

## README (trích đầu)
```
# U.S. Census Bureau Data API MCP
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/blob/main/LICENSE)
[![MCP Project Build](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml)
[![MCP Project - Lint](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml)
[![MCP Server - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml)
[![MCP Database - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml)
![MCP Server - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/0589e2c69696f077eef7d6af818a108b/raw/badge.svg)
![MCP Database - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/ae50d82d94893c2e674f7f742aea958e/raw/badge.svg)

Bringing _official_ Census Bureau statistics to AI assistants everywhere.

The *U.S. Census Bureau Data API MCP* is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that connects AI assistants with data from the Census Data API and other official Census Bureau sources. This project is built using the [MCP Typescript SDK](https://github.com/modelcontextprotocol/typescript-sdk).

## Contents
* [Getting Started](#getting-started)
* [Using the MCP Server](#using-the-mcp-server)
* [How the MCP Server Works](#how-the-mcp-server-works)
* [Development](#development)
* [MCP Server Architecture](#mcp-server-architecture)
* [Available Methods](#available-methods)
* [Available Tools](#available-tools)
* [Available Prompts](#available-prompts)
* [Helper Scripts](#helper-scripts)
* [Additional Information](#additional-information)

## Getting Started
To get started, you will need:

* A valid Census Bureau [Data API key](https://api.census.gov/data/key_signup.html)
* Docker (i.e. Docker Desktop)
* Node 18+

## Using the MCP Server
To use the U.S. Census Bureau Data API MCP server:
1. Clone or download the project locally.
2. In a terminal window, navigate to the project’s root directory and run `docker compose --profile prod run --rm census-mcp-db-init sh -c "npm run migrate:up && npm run seed"` to pull data from the Census Data API into the local database. *This is only required on first-time setup.*
3. Configure your AI Assistant to use the MCP Server (see below).
4. Start your AI Assistant.

Here is an example configuration file that includes the appropriate scripts for launching the MCP Ser
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

