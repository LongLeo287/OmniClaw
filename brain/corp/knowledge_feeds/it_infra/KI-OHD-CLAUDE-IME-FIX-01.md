# KI-OHD-CLAUDE-IME-FIX-01

## OIW Ingestion Metadata
- **Source**: https://github.com/0x0a0d/fix-vietnamese-claude-code
- **Ingested via**: OIW (Universal Ingestion Workflow)
- **Date**: 2026-04-01
- **Value Category**: KNOWLEDGE & TOOL_SCRIPT
- **Owner**: `it_infra` / `system_health`

## Description

The original Anthropic `claude-code` CLI has an underlying issue in handling specific Input Method Editors (IMEs) for Vietnamese (such as Unikey, EVKey, PHTV). When typing Vietnamese, the terminal fails to buffer the keystrokes properly, resulting in broken character rendering and non-functional commands.

This GitHub repository provides an executable patch:
```sh
npx fix-vietnamese-claude-code
```

## OmniClaw System Integration (OHD)

Instead of running this manually, OmniClaw automatically applies this patch as a "Medical Filter" via the `handoff_to_claude_code.ps1` script every time a handoff occurs.

### Workflow
1. Antigravity sets `handoff_trigger = 'READY'` in blackboard.
2. `handoff_to_claude_code.ps1` initiates.
3. Script performs 5 safety checks.
4. **[OHD Intervention]**: `npx -y fix-vietnamese-claude-code` runs silently to patch the current `claude-code` binary locally.
5. Claude Code launches with proper Vietnamese IME support.

### Note on Updates
Because Claude Code forcefully unpatches itself during every version update (e.g. `claude update`), applying this fix automatically right before execution ensures that OmniClaw developers remain uninterrupted regardless of Claude's background updates.
