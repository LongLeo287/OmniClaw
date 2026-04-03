---
id: nvidia-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.476763
---

# KNOWLEDGE EXTRACT: NVIDIA
> **Extracted on:** 2026-03-30 17:49:31
> **Source:** NVIDIA

---

## File: `garak.md`
```markdown
# 📦 NVIDIA/garak [🔖 PENDING/APPROVE]
🔗 https://github.com/NVIDIA/garak
🌐 https://discord.gg/uVch4puUCs

## Meta
- **Stars:** ⭐ 7376 | **Forks:** 🍴 845
- **Language:** HTML | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
the LLM vulnerability scanner

## README (trích đầu)
```
# garak, LLM vulnerability scanner

*Generative AI Red-teaming & Assessment Kit*

`garak` checks if an LLM can be made to fail in a way we don't want. `garak` probes for hallucination, data leakage, prompt injection, misinformation, toxicity generation, jailbreaks, and many other weaknesses. If you know `nmap` or `msf` / Metasploit Framework, garak does somewhat similar things to them, but for LLMs. 

`garak` focuses on ways of making an LLM or dialog system fail. It combines static, dynamic, and adaptive probes to explore this.

`garak`'s a free tool. We love developing it and are always interested in adding functionality to support applications. 

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Tests/Linux](https://github.com/NVIDIA/garak/actions/workflows/test_linux.yml/badge.svg)](https://github.com/NVIDIA/garak/actions/workflows/test_linux.yml)
[![Tests/Windows](https://github.com/NVIDIA/garak/actions/workflows/test_windows.yml/badge.svg)](https://github.com/NVIDIA/garak/actions/workflows/test_windows.yml)
[![Tests/OSX](https://github.com/NVIDIA/garak/actions/workflows/test_macos.yml/badge.svg)](https://github.com/NVIDIA/garak/actions/workflows/test_macos.yml)
[![Documentation Status](https://readthedocs.org/projects/garak/badge/?version=latest)](http://garak.readthedocs.io/en/latest/?badge=latest)
[![arXiv](https://img.shields.io/badge/cs.CL-arXiv%3A2406.11036-b31b1b.svg)](https://arxiv.org/abs/2406.11036)
[![discord-img](https://img.shields.io/badge/chat-on%20discord-yellow.svg)](https://discord.gg/uVch4puUCs)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/garak)](https://pypi.org/project/garak)
[![PyPI](https://badge.fury.io/py/garak.svg)](https://badge.fury.io/py/garak)
[![Downloads](https://static.pepy.tech/badge/garak)](https://pepy.tech/project/garak)
[![Downloads](https://static.pepy.tech/badge/garak/month)](https://pepy.tech/project/garak)


## Get started
### > See our user guide! [docs.garak.ai](https://docs.garak.ai/)
### > Join our [Discord](https://discord.gg/uVch4puUCs)!
### > Project links & home: [garak.ai](https://garak.ai/)
### > Twitter: [@garak_llm](https://twitter.com/garak_llm)
### > DEF CON [slides](https://garak.ai/garak_aiv_slides.pdf)!

<hr>

## LLM support

currently supports:
* [hugging face hub](https://huggingface.co/models) generative models
* [replicate](https://replicate.com/) text models
* [openai api](https://platform.openai.com/docs/introduction) chat & continuation models
* [aws bedrock](https://aws.amazon.com/bedrock/) foundation models
* [litellm](https://www.litellm.ai/)
* pretty much anything accessible via REST
* gguf models like [llama.cpp](https://github.com/ggerganov/llama.cpp) version >= 1046
* .. and many more LLMs!

## Install:

`garak` is a command-line tool. It's developed in Linux and OSX.

##
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `NemoClaw.md`
```markdown
# 📦 NVIDIA/NemoClaw [🔖 PENDING/APPROVE]
🔗 https://github.com/NVIDIA/NemoClaw
🌐 https://docs.nvidia.com/nemoclaw/latest/

## Meta
- **Stars:** ⭐ 17004 | **Forks:** 🍴 1898
- **Language:** JavaScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Run OpenClaw more securely inside NVIDIA OpenShell with managed inference

## README (trích đầu)
```
# NVIDIA NemoClaw: Reference Stack for Running OpenClaw in OpenShell

<!-- start-badges -->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md)
[![Project Status](https://img.shields.io/badge/status-alpha-orange)](https://github.com/NVIDIA/NemoClaw/blob/main/docs/about/release-notes.md)
<!-- end-badges -->

<!-- start-intro -->
NVIDIA NemoClaw is an open source reference stack that simplifies running [OpenClaw](https://openclaw.ai) always-on assistants more safely.
It installs the [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) runtime, part of NVIDIA Agent Toolkit, which provides additional security for running autonomous agents.
It also includes open source models such as [NVIDIA Nemotron](https://build.nvidia.com).
<!-- end-intro -->

> **Alpha software**
>
> NemoClaw is available in early preview starting March 16, 2026.
> This software is not production-ready.
> Interfaces, APIs, and behavior may change without notice as we iterate on the design.
> The project is shared to gather feedback and enable early experimentation.
> We welcome issues and discussion from the community while the project evolves.

---

## Quick Start

Follow these steps to get started with NemoClaw and your first sandboxed OpenClaw agent.

> **ℹ️ Note**
>
> NemoClaw creates a fresh OpenClaw instance inside the sandbox during onboarding.

<!-- start-quickstart-guide -->

### Prerequisites

Check the prerequisites before you start to ensure you have the necessary software and hardware to run NemoClaw.

#### Hardware

| Resource | Minimum        | Recommended      |
|----------|----------------|------------------|
| CPU      | 4 vCPU         | 4+ vCPU          |
| RAM      | 8 GB           | 16 GB            |
| Disk     | 20 GB free     | 40 GB free       |

The sandbox image is approximately 2.4 GB compressed. During image push, the Docker daemon, k3s, and the OpenShell gateway run alongside the export pipeline, which buffers decompressed layers in memory. On machines with less than 8 GB of RAM, this combined usage can trigger the OOM killer. If you cannot add memory, configuring at least 8 GB of swap can work around the issue at the cost of slower performance.

#### Software

| Dependency | Version                          |
|------------|----------------------------------|
| Linux      | Ubuntu 22.04 LTS or later |
| Node.js    | 20 or later |
| npm        | 10 or later |
| Container runtime | Supported runtime installed and running |
| [OpenShell](https://github.com/NVIDIA/OpenShell) | Installed |

#### Container Runtime Support

| Platform | Supported runtimes | Notes |
|----------|--------------------|-------|
| Linux | Docker | Primary supported path today |
| macOS (Apple Silicon) | Colima, Docker Desktop | Recommended runtimes for supported 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `OpenShell.md`
```markdown
# 📦 NVIDIA/OpenShell [🔖 PENDING/APPROVE]
🔗 https://github.com/NVIDIA/OpenShell
🌐 https://docs.nvidia.com/openshell/latest/

## Meta
- **Stars:** ⭐ 3868 | **Forks:** 🍴 378
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenShell is the safe, private runtime for autonomous AI agents.

## README (trích đầu)
```
# OpenShell

[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](https://github.com/NVIDIA/OpenShell/blob/main/LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-openshell-orange?logo=pypi)](https://pypi.org/project/openshell/)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](SECURITY.md)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](https://docs.nvidia.com/openshell/latest/index.html)
[![Project Status](https://img.shields.io/badge/status-alpha-orange)](https://docs.nvidia.com/openshell/latest/about/release-notes.html)

OpenShell is the safe, private runtime for autonomous AI agents. It provides sandboxed execution environments that protect your data, credentials, and infrastructure — governed by declarative YAML policies that prevent unauthorized file access, data exfiltration, and uncontrolled network activity.

OpenShell is built agent-first. The project ships with agent skills for everything from cluster debugging to policy generation, and we expect contributors to use them.

> **Alpha software — single-player mode.** OpenShell is proof-of-life: one developer, one environment, one gateway. We are building toward multi-tenant enterprise deployments, but the starting point is getting your own environment up and running. Expect rough edges. Bring your agent.

## Quickstart

### Prerequisites

- **Docker** — Docker Desktop (or a Docker daemon) must be running.

### Install

**Binary (recommended):**

```bash
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
```

**From PyPI (requires [uv](https://docs.astral.sh/uv/)):**

```bash
uv tool install -U openshell
```

Both methods install the latest stable release by default. To install a specific version, set `OPENSHELL_VERSION` (binary) or pin the version with `uv tool install openshell==<version>`. A [`dev` release](https://github.com/NVIDIA/OpenShell/releases/tag/dev) is also available that tracks the latest commit on `main`.

### Create a sandbox

```bash
openshell sandbox create -- claude  # or opencode, codex, copilot
```

A gateway is created automatically on first use. To deploy on a remote host instead, pass `--remote user@host` to the create command.

The sandbox container includes the following tools by default:

| Category   | Tools                                                    |
| ---------- | -------------------------------------------------------- |
| Agent      | `claude`, `opencode`, `codex`, `copilot`                 |
| Language   | `python` (3.13), `node` (22)                             |
| Developer  | `gh`, `git`, `vim`, `nano`                               |
| Networking | `ping`, `dig`, `nslookup`, `nc`, `traceroute`, `netstat` |

For more details see https://github.com/NVIDIA/OpenShell-Community/tree/main/sandboxes/base.

### See network policy in action

Every sandbox starts with **minimal outbound access**. You open additional access with a short YAML 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `TensorRT-LLM.md`
```markdown
# 📦 NVIDIA/TensorRT-LLM [🔖 PENDING/APPROVE]
🔗 https://github.com/NVIDIA/TensorRT-LLM
🌐 https://nvidia.github.io/TensorRT-LLM

## Meta
- **Stars:** ⭐ 13192 | **Forks:** 🍴 2218
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.

## README (trích đầu)
```
<div align="center">

TensorRT LLM
===========================
<h4>TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports
state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs.</h4>

[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://nvidia.github.io/TensorRT-LLM/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/NVIDIA/TensorRT-LLM)
[![python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org/downloads/release/python-3123/)
[![python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org/downloads/release/python-31012/)
[![cuda](https://img.shields.io/badge/cuda-13.1.1-green)](https://developer.nvidia.com/cuda-downloads)
[![torch](https://img.shields.io/badge/torch-2.10.0-green)](https://pytorch.org)
[![version](https://img.shields.io/badge/release-1.3.0rc9-green)](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/version.py)
[![license](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE)

[Architecture](https://nvidia.github.io/TensorRT-LLM/developer-guide/overview.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Performance](https://nvidia.github.io/TensorRT-LLM/developer-guide/perf-overview.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Examples](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Documentation](https://nvidia.github.io/TensorRT-LLM/)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Roadmap](https://github.com/NVIDIA/TensorRT-LLM/issues?q=is%3Aissue%20state%3Aopen%20label%3Aroadmap)

---
<div align="left">

## Tech Blogs

<!-- Use github markdown link to link for the latest blog since the doc build has not happened yet. When the doc build is updated, it should be updated to the webpage link. -->
* [03/16] Optimizing MoE Communication with One-Sided AlltoAll Over NVLink
✨ [➡️ link](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog18_Optimizing_MoE_Communication_with_One_Sided_AlltoAll_Over_NVLink.md)

* [03/04] Sparse Attention in TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog17_Sparse_Attention_in_TensorRT-LLM.html)

* [02/06] Accelerating Long-Context Inference with Skip Softmax Attention
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog16_Accelerating_Long_Context_Inference_with_Skip_Softmax_Attention.html)

* [01/09] Optimizing DeepSeek-V3.2 on NVIDIA Blackwell GPUs
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs)

* [10/13] Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Performance Boundary)
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog14_Scaling_Expert_Parallelism_in_TensorRT-LLM_part3.html)

* [09/26] Inference Time Compute Implementatio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

