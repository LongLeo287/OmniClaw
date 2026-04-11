# OmniClaw Activation Guide

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
omniclaw doctor
```

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

Examples:

```bash
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
