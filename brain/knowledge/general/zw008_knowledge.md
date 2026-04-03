---
id: zw008-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:48.002798
---

# KNOWLEDGE EXTRACT: zw008
> **Extracted on:** 2026-03-30 18:01:32
> **Source:** zw008

---

## File: `VMware-AIops.md`
```markdown
# 📦 zw008/VMware-AIops [🔖 PENDING/APPROVE]
🔗 https://github.com/zw008/VMware-AIops
🌐 https://skills.sh/zw008/VMware-AIops

## Meta
- **Stars:** ⭐ 27 | **Forks:** 🍴 5
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
VMware vCenter/ESXi AI-powered monitoring and operations. Two skills: vmware-monitor (read-only, safe) and vmware-aiops (full operations) | Claude Code Skill

## README (trích đầu)
```
<!-- mcp-name: io.github.zw008/vmware-aiops -->
# VMware AIops

English | [中文](README-CN.md)

AI-powered VMware vCenter/ESXi VM lifecycle and deployment tool — 31 tools across 6 categories.

> **Companion skills** handle everything else:
>
> | Skill | Scope | Install |
> |-------|-------|---------|
> | **[vmware-monitor](https://github.com/zw008/VMware-Monitor)** | Read-only: inventory, health, alarms, events, metrics | `uv tool install vmware-monitor` |
> | **[vmware-storage](https://github.com/zw008/VMware-Storage)** | Datastores, iSCSI, vSAN management | `uv tool install vmware-storage` |
> | **[vmware-vks](https://github.com/zw008/VMware-VKS)** | Tanzu Namespaces, TKC cluster lifecycle | `uv tool install vmware-vks` |
>
> **Need read-only monitoring only?** Use [VMware-Monitor](https://github.com/zw008/VMware-Monitor) — zero destructive code in the codebase.

[![ClawHub](https://img.shields.io/badge/ClawHub-vmware--aiops-orange)](https://clawhub.ai/skills/vmware-aiops)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install-blue)](https://skills.sh/zw008/VMware-AIops)
[![Claude Code Marketplace](https://img.shields.io/badge/Claude_Code-Marketplace-blueviolet)](https://github.com/zw008/VMware-AIops)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

### Quick Install (Recommended)

Works with Claude Code, Cursor, Codex, Gemini CLI, Trae, and 30+ AI agents:

```bash
# Via Skills.sh
npx skills add zw008/VMware-AIops

# Via ClawHub
clawhub install vmware-aiops
```

### PyPI Install (No GitHub Access Required)

```bash
# Install via uv (recommended)
uv tool install vmware-aiops

# Or via pip
pip install vmware-aiops

# China mainland mirror (faster)
pip install vmware-aiops -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Claude Code Plugin Install

```bash
# Add marketplace
/plugin marketplace add zw008/VMware-AIops

# Install plugin
/plugin install vmware-ops

# Use the skill
/vmware-ops:vmware-aiops
```

---

## Capabilities Overview

### What This Skill Does

| Category | Tools | Count |
|----------|-------|:-----:|
| **VM Lifecycle** | power on/off, TTL auto-delete, clean slate | 6 |
| **Deployment** | OVA, template, linked clone, batch clone/deploy | 8 |
| **Guest Ops** | exec commands, upload/download files, provision | 5 |
| **Plan/Apply** | multi-step planning with rollback | 4 |
| **Cluster** | create, delete, HA/DRS config, add/remove hosts | 6 |
| **Datastore** | browse files, scan for images | 2 |

### CLI vs MCP: Which Mode to Use

| Scenario | Recommended | Why |
|----------|:-----------:|-----|
| **Local/small models** (Ollama, Qwen <32B) | **CLI** | ~2K tokens context vs ~10K for MCP; small models struggle with many tool schemas |
| **Token-sensitive workflows** | **CLI** | SKILL.md + Bash tool = minimal overhead |
| **Cloud models** (Claude, GPT-4o) | Either | Both work; MCP gives structured JSON I/O |
| **Automated pipelines / Agent chaining** | **MCP** | Type-safe parameters, structured out
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

