# Figma Context MCP Usage Guide

## Identity
- **Department**: Dept 03 (Design & UX)
- **Agent**: `ui-ux-architect`
- **Tool Name**: `figma-context-mcp` (via local node execution)

## Description
This MCP plugin allows agents to fetch direct structural data (layers, typography, colors, padding, etc.) from Figma design files to translate into perfectly exact Tailwind/React/CSS code.

## Setup Requirements
1. Log into your Figma account.
2. Go to **Settings > Personal access tokens** and create a new token.
3. Open `D:\LongLeo\OmniClaw\.env` and add:
   ```env
   # Figma MCP Integration
   FIGMA_API_KEY=your_token_here
   ```
4. Restart OmniClaw's context server configuration or reload the agent profile.

## Usage Commands
When tasked with a UI layout update, the `ui-ux-architect` agent can autonomously call the `get_figma_data` MCP tool with the URL of the Figma file or frame.

- The system uses `D:\LongLeo\OmniClaw\vault\tmp\sandbox_env\QUARANTINE_figma-context-mcp\dist\bin.js`.
- It processes node IDs and extracts CSS values, meaning you no longer have to guess font sizes or pixel gaps.
