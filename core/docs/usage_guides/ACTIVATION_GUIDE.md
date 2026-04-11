# OmniClaw Activation Guide

This guide covers the current, shipped bootstrap flow for the `main` branch.

## 1. Install The Local CLI

```bash
git clone https://github.com/LongLeo287/OmniClaw.git "OmniClaw"
cd "OmniClaw"
npm install -g .
```

If you do not want a global install on Windows, you can run:

```bat
omniclaw.bat doctor
```

## 2. Validate The Workspace

Run the built-in doctor command first:

```bash
omniclaw doctor
```

Useful environment variables:

- `OMNICLAW_ROOT`: absolute path to the OmniClaw repository
- `OMNICLAW_MODELS_ROOT`: absolute path to the shared models vault
- `OMNICLAW_REMOTE_ROOT`: optional path to the future OmniClaw REMOTE project
- `OMNICLAW_UI_ROOT`: optional path to the future OmniClaw UI project
- `OMNICLAW_SYSTEM_PULSE_SCRIPT`: explicit path to the System Pulse daemon script if it lives outside the default repo layout

## 3. Start Local Bridges Manually

Examples:

```bash
python ecosystem/bridges/launch_ollama.py
python ecosystem/bridges/launch_mem0.py
python ecosystem/bridges/launch_firecrawl.py
python ecosystem/bridges/launch_lightrag.py
python ecosystem/bridges/launch_model_ai.py --repair
```

Runtime policy:

- Bridges should launch a real service or fail fast.
- Dependency installation belongs in explicit repair/bootstrap flows.
- Shared services such as `qdrant` should not be torn down by unrelated launchers.

## 4. Known Scope

The current repository is the OmniClaw core workspace.

- `OmniClaw REMOTE` is not required for the local core to bootstrap.
- `OmniClaw UI` is not required for the local core to bootstrap.
- Bridges that target those future projects will fail clearly until those projects are provisioned.
