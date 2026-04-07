---
id: capability_integrators
name: OmniClaw Intake & Registry Integrators
type: operational_capability
owner: OIW Daemon / CIV Agent
authorized_agents: ["civ-agent", "registry-manager-agent"]
status: active
---

# Capability Profile: Remote Integrators & Intake Flow

## Overview
This suite of scripts arms the OmniClaw Intake Worker (OIW) and `civ-agent` with robust automation to synchronize external data streams (GitHub, Telegram, registries) directly into the core ecosystem.

## Core Assets & Workflows

1. `batch_clone.py` & `check_repos.py`
   - **Purpose**: Validates local cloned content against the authoritative `D:\OmniClaw\data\Github.txt` list, identifying missing assets and batch cloning them automatically.
   - **Workflow Location**: OIW daemon invokes this during the Phase 0 (System Health) or Content Intake operations to ensure repository data sync.

2. `wire_repo_demand.py`
   - **Purpose**: Hooks the Telegram messaging router to listen for repository-on-demand requests, validating clearance and pushing the URL to OIW for deep verification.
   - **Workflow Location**: Used by `civ-agent` as a frontline gatekeeper listener.

3. `register_skills.py`
   - **Purpose**: Safely patches `brain/shared-context/SKILL_REGISTRY.json` ensuring no duplication, maintaining the integrity of the live capability map.
   - **Workflow Location**: Called by `registry-manager-agent` (or OER daemon) after a new capability is successfully forged.

## OA Academy Understanding
OA relies on this pipeline to deliver clean, vetted repositories into the assimilation zone. By delegating repository acquisition and registration entirely to these Integrator scripts, OA can focus strictly on deep NLP analysis and architectural upgrading, completely decoupled from networking nuances.
