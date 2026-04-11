---
id: activation-guide
type: document
owner: SYSTEM
tags: [startup, runtime, public-bootstrap]
---

# OmniClaw Activation Guide

This guide reflects the public OmniClaw runtime that actually exists in this repository.

## Runtime Layers

1. `omniclaw doctor`
Checks workspace markers and required local dependencies.

2. `omniclaw startup`
Rebuilds registries/maps and runs the Python startup health checks.

3. `omniclaw core`
Starts the public core processes:
- Bridge Gateway
- Orchestrator watch loop

## Recommended Startup Flow

```bash
omniclaw doctor
omniclaw startup
omniclaw core
```

## Commands

### Doctor

```bash
omniclaw doctor
```

Verifies:
- workspace root markers
- required files
- `git`, `node`, `python`
- optional `docker`

### Startup

```bash
omniclaw startup
```

This command:
- rebuilds tool and skill registries
- regenerates ecosystem maps
- runs the startup health/status refresh

Optional:

```bash
omniclaw startup --no-sync
omniclaw startup --check-only
```

### Core

```bash
omniclaw core
```

Starts:
- bridge gateway on `127.0.0.1:8000`
- orchestrator watch loop with a 30-second interval

Optional:

```bash
omniclaw core --port 8001
omniclaw core --interval 10
omniclaw core --no-bridge
omniclaw core --no-orchestrator
```

### Status

```bash
omniclaw status
```

Prints runtime-local status for:
- bridge port
- blackboard
- system router
- startup HUD
- receipt store

## Tool-Agnostic Usage

The same startup flow is intended to be usable from:
- Claude Code
- Codex
- Antigravity

They should all rely on the same local commands rather than separate bootstrap paths.

## Public Core Daemons

For the public repository, the only startup-managed long-running processes with clear runtime evidence are:

1. `Bridge Gateway`
Implemented by `core/bridge/main.py`

2. `Orchestrator Watch Loop`
Implemented by `core/ops/omniclaw_orchestrator.py`

Other daemon concepts may exist in rules or docs, but should not be treated as bootable public runtime processes unless they have an executable entrypoint in the repository.
