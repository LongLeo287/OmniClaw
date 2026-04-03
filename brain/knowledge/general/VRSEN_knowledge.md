---
id: vrsen-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:42.041603
---

# KNOWLEDGE EXTRACT: VRSEN
> **Extracted on:** 2026-03-30 17:59:00
> **Source:** VRSEN

---

## File: `agency-swarm.md`
```markdown
# 📦 VRSEN/agency-swarm [🔖 PENDING/APPROVE]
🔗 https://github.com/VRSEN/agency-swarm
🌐 https://agency-swarm.ai/

## Meta
- **Stars:** ⭐ 4120 | **Forks:** 🍴 1007
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Reliable Multi-Agent Orchestration Framework

## README (trích đầu)
```
# 🐝 Agency Swarm

![Framework](https://firebasestorage.googleapis.com/v0/b/vrsen-ai/o/public%2Fgithub%2FLOGO_BG_large_bold_shadow%20(1).jpg?alt=media&token=8c681331-2a7a-4a69-b21b-3ab1f9bf1a23)

## Overview

The **Agency Swarm** is a framework for building multi-agent applications. It leverages and extends the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), providing specialized features for creating, orchestrating, and managing collaborative swarms of AI agents.

This framework continues the original vision of Arsenii Shatokhin (aka VRSEN) to simplify the creation of AI agencies by thinking about automation in terms of real-world organizational structures, making it intuitive for both agents and users.

**Migrating from v0.x?** Please see our [Migration Guide](https://agency-swarm.ai/migration/guide) for details on adapting your project to this new SDK-based version.

[![Docs](https://img.shields.io/website?label=Docs&up_message=available&url=https://agency-swarm.ai/)](https://agency-swarm.ai)
[![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen)](https://github.com/VRSEN/agency-swarm/actions?query=branch%3Amain+event%3Apush)
[![Subscribe on YouTube](https://img.shields.io/youtube/channel/subscribers/UCSv4qL8vmoSH7GaPjuqRiCQ)](https://youtube.com/@vrsen/)
[![Follow on Twitter](https://img.shields.io/twitter/follow/__vrsen__.svg?style=social&label=Follow%20%40__vrsen__)](https://twitter.com/__vrsen__)
[![Join our Discord!](https://img.shields.io/discord/1200037936352202802?label=Discord)](https://discord.gg/cw2xBaWfFM)
[![Agents-as-a-Service](https://img.shields.io/website?label=Agents-as-a-Service&up_message=For%20Business&url=https%3A%2F%2Fvrsen.ai)](https://agents.vrsen.ai)

### Key Features

- **Customizable Agent Roles**: Define distinct agent roles (e.g., CEO, Virtual Assistant, Developer) with tailored instructions, tools, and capabilities within the Agency Swarm framework, leveraging the underlying OpenAI Agents SDK.
- **Full Control Over Prompts/Instructions**: Maintain complete control over each agent’s guiding prompts (instructions) for precise behavior customization.
- **Type-Safe Tools**: Develop tools using Pydantic models for automatic argument validation, compatible with the OpenAI Agents SDK’s `FunctionTool` format.
- **Orchestrated Agent Communication**: Agents communicate via a dedicated `send_message` tool, with interactions governed by explicit, directional `communication_flows` defined on the `Agency`.
- **Flexible State Persistence**: Manage conversation history by providing `load_threads_callback` and `save_threads_callback` to the `Agency`, enabling persistence across sessions (e.g., DB/file storage).
- **Multi-Agent Orchestration**: Build agent workflows on the OpenAI Agents SDK foundation, enhanced by Agency Swarm’s structured orchestration layer.
- **Production-Ready Focus**: Built for reliability and designed for easy deployment in real-world environments.

## Installation

```bash
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

