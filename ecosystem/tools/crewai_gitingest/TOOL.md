---
id: crewai_gitingest
name: CrewAI Gitingest Tool
status: active
integration_type: python_script
accessible_by:
  - Orchestrator
  - CrewAI Agents
tags: [github, code-analysis, crewai]
---

# Gitingest Code Repo Analyzer

## Overview
This native Python script functions as a `BaseTool` for CrewAI or direct orchestrator calls. It ingests an entire GitHub repository using the `gitingest` module, returning the directory tree and the first 3000 characters of the codebase for prompt context.

## Instructions
Invoke the tool by passing a valid GitHub URL. It requires the `gitingest` pip module installed on the host OS.
