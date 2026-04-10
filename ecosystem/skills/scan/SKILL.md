---
name: scan
description: Scan a project with sentrux to get structural health grades (A-F) across 14 dimensions including coupling, cycles, cohesion, dead code, and test coverage. Use when the user wants to check code quality, architecture health, or before/after an agent session.
---

# Sentrux Scan

Use the sentrux MCP tools to analyze the current project:

1. Call `scan` with the current working directory to get an overview
2. If the user wants details, call `health` for code health breakdown or `architecture` for structural analysis
3. For agent session governance, use `session_start` before coding and `session_end` after to detect degradation

Available MCP tools: `scan` · `health` · `architecture` · `coupling` · `cycles` · `hottest` · `evolution` · `dsm` · `test_gaps` · `check_rules` · `session_start` · `session_end` · `rescan` · `blast_radius` · `level`

$ARGUMENTS
