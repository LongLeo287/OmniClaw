---
id: getting-started
type: document
owner: SYSTEM
tags: [bootstrap, public]
---

# 🚀 Getting Started with OmniClaw

Welcome aboard! This guide will walk you through setting up OmniClaw, booting your first AI orchestrator, and linking your local workspace.

[**🇻🇳 Vietnamese Translation**](getting_started_vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Prerequisites

Before bootstrapping the current OmniClaw core repository, ensure you have:
- **Node.js (v18+)** for the bootstrap CLI and JavaScript tooling.
- **Python 3** for core scripts and bridge launchers.
- **Git** for repository workflows.
- **Docker Desktop** (optional) for bridge-managed local services.

## 2. Installation Setup

```bash
git clone https://github.com/LongLeo287/OmniClaw.git "OmniClaw"
cd "OmniClaw"
npm install -g .
omniclaw doctor
```

On Windows, you can also run:

```powershell
.\omniclaw.bat doctor
```

## 3. First Boot

The public bootstrap path is diagnostic-first:

1. Resolve the workspace root with `omniclaw doctor`.
2. Inspect external project roots with `omniclaw paths`.
3. Load the boot prompt that matches your interface:
   - `brain/agents/claude.md`
   - `brain/agents/gemini.md`

`OmniClaw REMOTE` and `OmniClaw UI` are optional sibling projects. They are not required for the core repository to pass baseline diagnostics.

## 4. Next Steps

- Read [**Activation Guide**](activation_guide.md) for environment variables and repair modes.
- Read [**Agent Commands**](agent_commands.md) for current invocation patterns.
- Read [**Data Packaging & Sync**](../workflows/data_packaging_sync.md) only if your deployment needs external state backup or rehydration.

