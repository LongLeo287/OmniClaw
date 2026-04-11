# OmniClaw Activation Guide

<<<<<<< HEAD
This guide separates OmniClaw into two boot paths.

## 1. Agent System

Use this when the goal is to run OmniClaw as the project-facing agent layer.
This path should leave OmniClaw ready for user work, with skills, plugins,
memory state, routing, and orchestrator readiness all checked.

Commands:

```bash
=======
This guide covers the smallest reliable path to bootstrap the OmniClaw core repository for local use.

## Prerequisites

- Node.js 18 or newer
- Git
- Python 3
- Docker Desktop if you plan to launch bridge-managed services

## Bootstrap

```bash
git clone https://github.com/LongLeo287/OmniClaw.git "OmniClaw"
cd "OmniClaw"
npm install -g .
>>>>>>> origin/main
omniclaw doctor
omniclaw startup
omniclaw watch 30
omniclaw agent-status
```

<<<<<<< HEAD
Meaning:

- `omniclaw startup` runs the agent boot path and validates user-facing readiness.
- `omniclaw watch 30` keeps the orchestrator polling in watch mode.
- `omniclaw agent-status` reports agent-side routing and activation state.

Scope:
=======
If you do not want to install the CLI globally, run the local Windows wrapper instead:

```powershell
.\omniclaw.bat doctor
```

## Root Resolution

`omniclaw` resolves the workspace in this order:

1. `OMNICLAW_ROOT`
2. The current working directory
3. Parent directories that contain both `brain/rules/_DIR_IDENTITY.md` and `ecosystem/_REGIONAL_MAP.md`

Optional external project roots:

- `OMNICLAW_REMOTE_ROOT`
- `OMNICLAW_UI_ROOT`
- `OMNICLAW_MODELS_ROOT`
- `OMNICLAW_SYSTEM_PULSE_SCRIPT`

`OmniClaw REMOTE` and `OmniClaw UI` are optional sibling projects and are not required to bootstrap the core repository.

## Diagnostics

```bash
omniclaw help
omniclaw paths
omniclaw doctor
```

`omniclaw doctor` checks:

- required OmniClaw topology files
- bridge compose topology
- core registry scripts
- runtime availability for `git`, `node`, and `python`
- optional Docker availability

## Manual Bridge Launches
>>>>>>> origin/main

- orchestrator
- agent routing
- skill registry
- tool registry
- plugin inventory
- memory state
- workforce-facing execution flow

Constraint:

- the agent system may use OmniClaw, but it must not trigger self-healing, repair, registry mutation, or core-improvement flows

Excluded from this flow:

- core daemon maintenance
- bridge, UI, remote, port provisioning

## 2. Core Daemon System

Use this when the goal is to repair, maintain, sync, and upgrade OmniClaw itself.
This path is for the internal daemon side of OmniClaw, not for project-facing use.

Commands:

```bash
<<<<<<< HEAD
omniclaw doctor
omniclaw core-daemon
omniclaw core-loop 120
omniclaw core-status
omniclaw sync
```

Meaning:

- `omniclaw core-daemon` runs core startup preflight for the maintenance layer.
- `omniclaw core-loop 120` keeps internal upkeep running.
- `omniclaw core-status` reports internal state readiness.
- `omniclaw sync` refreshes internal registries and maps.

Scope:

- blackboard state
- trust matrix compliance
- daemon activation state
- registry and telemetry upkeep
- self-maintenance readiness
- system repair and improvement flows

Excluded from this flow:

- orchestrator watch for external project work
- bridge, UI, remote, port provisioning

## Operating Rule

Keep these two boot paths separate and logical:

- `Khởi động OmniClaw` => boot the agent system.
- `Khởi động Core Daemon` => boot the internal core daemon system.
=======
python ecosystem/bridges/launch_ollama.py
python ecosystem/bridges/launch_model_ai.py
python ecosystem/bridges/launch_system_pulse.py
```

Bridge launchers now follow a fail-fast policy:

- they do not create fake healthy ports
- they do not auto-install dependencies on the hot path unless explicit repair mode is enabled
- they do not assume `OmniClaw REMOTE` or `OmniClaw UI` are inside the core repository

## Repair Modes

Some scripts support explicit repair behavior through flags or environment variables such as:

- `--repair`
- `OMNICLAW_BRIDGE_REPAIR=1`
- `OMNICLAW_ASSIMILATOR_REPAIR=1`

Use repair mode intentionally during provisioning, not as part of steady-state runtime.
>>>>>>> origin/main
