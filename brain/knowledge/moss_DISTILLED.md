---
id: moss
type: knowledge
owner: OA_Triage
---
# moss
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# MOSS-TTS Family

<br>

<p align="center">
  <img src="./assets/OpenMOSS_Logo.png" height="70" align="middle" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="./assets/mosi-logo.png" height="50" align="middle" />
</p>




<div align="center">
  <a href="https://clawhub.ai/luogao2333/moss-tts-voice"><img src="https://img.shields.io/badge/🦞_OpenClaw-Skills-8A2BE2" alt="OpenClaw"></a>
  <a href="https://huggingface.co/collections/OpenMOSS-Team/moss-tts"><img src="https://img.shields.io/badge/Huggingface-Models-orange?logo=huggingface&amp"></a>
  <a href="https://modelscope.cn/collections/OpenMOSS-Team/MOSS-TTS"><img src="https://img.shields.io/badge/ModelScope-Models-lightgrey?logo=modelscope&amp"></a>
  <a href="https://mosi.cn/#models"><img src="https://img.shields.io/badge/Blog-View-blue?logo=internet-explorer&amp"></a>
  <a href="https://arxiv.org/abs/2603.18090"><img src="https://img.shields.io/badge/Arxiv-2603.18090-red?logo=Arxiv&amp"></a>

  <a href="https://studio.mosi.cn"><img src="https://img.shields.io/badge/AIStudio-Try-green?logo=internet-explorer&amp"></a>
  <a href="https://studio.mosi.cn/docs/moss-tts"><img src="https://img.shields.io/badge/API-Docs-00A3FF?logo=fastapi&amp"></a>
  <a href="https://x.com/Open_MOSS"><img src="https://img.shields.io/badge/Twitter-Follow-black?logo=x&amp"></a>
  <a href="https://discord.gg/Xf3aXddCjc"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp"></a>
  <a href="./assets/wechat.jpg"><img src="https://img.shields.io/badge/WeChat-Join-07C160?logo=wechat&amp;logoColor=white" alt="WeChat"></a>
</div>


[English](README.md) | [简体中文](README_zh.md)


MOSS‑TTS Family is an open‑source **speech and sound generation model family** from [MOSI.AI](https://mosi.cn/#hero) and the [OpenMOSS team](https://www.open-moss.com/). It is designed for **high‑fidelity**, **high‑expressiveness**, and **complex real‑world scenarios**, covering stable long‑form speech, multi‑speaker dialogue, voice/character design, environmental sound effects, and real‑time streaming TTS.

## News
* 2026.3.31: 📄 Our technical reports for [MOSS-TTSD](https://arxiv.org/pdf/2603.19739) and [MOSS-VoiceGenerator](https://arxiv.org/pdf/2603.28086) are now available on arXiv!
* 2026.3.26: 📘 Added a tutorial on fine-tuning the MOSS-TTS-Realtime!
* 2026.3.20: 📄 Our [technical report](https://arxiv.org/pdf/2603.18090) is now available on arXiv!
* 2026.3.18: 🚀 Added a first-class MOSS-TTS `llama.cpp` implementation in the companion repository [`OpenMOSS/llama.cpp`](https://github.com/OpenMOSS/llama.cpp/tree/moss-tts-firstclass), including end-to-end docs and a runnable pipeline for GGUF backbone inference plus ONNX audio codec decoding. See the [first-class e2e guide](https://github.com/OpenMOSS/llama.cpp/blob/moss-tts-firstclass/docs/moss-tts-firstclass-e2e.md).
* 2026.3.16: 📘 Added a tutorial on fine-tuning the MossTTSLocal architecture, suitable for MOSS-TTS-Local-Transformer!
* 2026.3.12: 🚀 Added SGLang backend support for the `MossTTSDelay` architecture, enabling efficient inference for MOSS-TTS (Delay) and MOSS-SoundEffect, with around **3× faster** generation throughput!
* 2026.3.11: 📘 Added a tutorial on fine-tuning the MossTTSDelay architecture, suitable for MOSS-TTS(Delay), MOSS-TTSD, MOSS-VoiceGenerator, and MOSS-SoundEffect!
* 2026.3.10: ⚡️ Significantly optimized the VRAM usage of llama.cpp inference pipeline. Now 8B model fits onto 8GB GPUs!
* 2026.3.4: 🚀 Added **PyTorch-free inference support** — enabling lightweight on-device deployment via **llama.cpp + ONNX Runtime**. Quantized **GGUF weights** are released at [OpenMOSS-Team/MOSS-TTS-GGUF](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-GGUF), and the **ONNX audio tokenizer** is available at [OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX). See the [llama.cpp backend](#llamacpp-backend-torch-free-inference) for details.
* 2026.3.4: 🎉 We add MOSS-TTS skills in [ClawHub](https://clawhub.ai) of 🦞 OpenClaw: [feishu-voice-tts](https://clawhub.ai/helloeveryworlds/feishu-voice-tts) and [moss-tts-voice](https://clawhub.ai/luogao2333/moss-tts-voice).
* 2026.2.10: 🎉🎉🎉 We have released [MOSS-TTS Family](https://huggingface.co/collections/OpenMOSS-Team/moss-tts). Check our [Blog](https://mosi.cn/#models) for more details! Our **Huggingface Space** is here: [MOSS-TTS](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS), [MOSS-TTSD-v1.0](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTSD-v1.0), [MOSS-VoiceGenerator](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-VoiceGenerator).


## Demo

<div align="center">
  <video src="https://gist.github.com/user-attachments/assets/fdce9f66-20ec-45e8-9615-89606ae2fbe8" width="70%" poster=""> </video>
</div>

## Contents

- [Introduction](#introduction)
- [Model Architecture](#model-architecture)
- [Released Models](#released-models)
- [Supported Languages](#supported-languages)
- [Quickstart](#quickstart)
  - [OpenClaw API Skills](#openclaw-api-skills)
  - [Environment Setup](#environment-setup)
  - [(Optional) Install FlashAttention 2](#optional-install-flashattention-2)
  - [MOSS-TTS Basic Usage](#moss-tts-basic-usage)
- [Fine-Tuning](#fine-tuning)
- [llama.cpp Backend (Torch-Free Inference)](#llamacpp-backend-torch-free-inference)
- [SGLang Backend (Accelerated Inference)](#sglang-backend-accelerated-inference)
- [Evaluation](#evaluation)
  - [MOSS-TTS](#moss-tts-seed-tts-eval)
  - [MOSS-TTSD](#moss-ttsd-subjective--ttsd-eval)
  - [MOSS-VoiceGenerator](#moss-voicegenerator-subjective)
- [MOSS-Audio-Tokenizer](#moss-audio-tokenizer)
  - [Introduction](#mat-intro)
  - [Model Weights](#model-weights)
  - [Objective Reconstruction Evaluation](#objective-reconstruction-evaluation)
- [More Information](#more-information)
  - [Community Projects](#community-projects)
- [Citation](#citation)


## Introduction

<p align="center">
  <img src="./assets/moss_tts_family.jpeg" width="85%" />
</p>

When a single piece of audio needs to **sound like a real person**, **pronounce every word accurately**, **switch speaking styles across content**, **remain stable over tens of minutes**, and **support dialogue, role‑play, and real‑time interaction**, a single TTS model is often not enough. The **MOSS‑TTS Family** breaks the workflow into five production‑ready models that can be used independently or composed into a complete pipeline.

- **MOSS‑TTS**: The flagship production model featuring high fidelity and optimal zero-shot voice cloning. It supports **long-speech generation**, **fine-grained control over Pinyin, phonemes, and duration**, as well as **multilingual/code-switched synthesis**.
- **MOSS‑TTSD**: A spoken dialogue generation model for expressive, multi-speaker, and ultra-long dialogues. The new **v1.0 version** achieves **industry-leading performance on objective metrics** and **outperformed top closed-source models like Doubao and Gemini 2.5-pro** in subjective evaluations. You can visit the [MOSS-TTSD repository](https://github.com/OpenMOSS/MOSS-TTSD) for details.
- **MOSS‑VoiceGenerator**: An open-source voice design model capable of generating diverse voices and styles directly from text prompts, **without any reference speech**. It unifies voice design, style control, and synthesis, functioning independently or as a design layer for downstream TTS. Its performance **surpasses other top-tier voice design models in arena ratings**.
- **MOSS‑TTS‑Realtime**: A multi-turn context-aware model for real-time voice agents. It uses incremental synthesis to ensure natural and coherent replies, making it **ideal for building low-latency voice agents when paired with text models**. The TTFB (Time To First Byte) of MOSS-TTS-Realtime reaches 180 ms, and the $T_{\text{LLM-first-sentence}} + T_{\text{MOSS-TTS-Realtime-TTFB}}$ is 377 ms.
- **MOSS‑SoundEffect**: A content creation model specialized in **sound effect generation** with wide category coverage and controllable duration. It generates audio for natural environments, urban scenes, biological sounds, human actions, and musical fragments, suitable for film, games, and interactive experiences.


## Model Architecture

We train **MossTTSDelay** and **MossTTSLocal** as complementary baselines under one training/evaluation setup: **Delay** emphasizes long-context stability, inference speed, and production readiness, while **Local** emphasizes lightweight flexibility and strong objective performance for streaming-oriented systems. Together they provide reproducible references for deployment and research.

**MossTTSRealtime** is not a third comparison baseline; it is a capability-driven design for voice agents. By modeling multi-turn context from both prior text and user acoustics, it delivers low-latency streaming speech that stays coherent and voice-consistent across turns.


| Architecture  | Core Mechanism | Arch Details |
|---|---|---|
| `MossTTSDelay` |  Multi‑head parallel RVQ prediction with delay‑pattern scheduling | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_delay/README.md) |
| `MossTTSLocal` | Time‑synchronous RVQ blocks with a depth transformer | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_local/README.md) |
| `MossTTSRealtime` | Hierarchical text–audio inputs for realtime synthesis | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_realtime/README.md) |

## Released Models


| Model | Architecture | Size | Model Card | Hugging Face | ModelScope |
|---|---|---:|---|---|---|
| **MOSS-TTS** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS) |
|  | `MossTTSLocal` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Local-Transformer) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS-Local-Transformer) |
| **MOSS‑TTSD‑V1.0** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_ttsd_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTSD-v1.0) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTSD-v1.0) |
| **MOSS‑VoiceGenerator** | `MossTTSDelay` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_voice_generator_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-VoiceGenerator) |
| **MOSS‑SoundEffect** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_sound_effect_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-SoundEffect) |
| **MOSS‑TTS‑Realtime** | `MossTTSRealtime` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_realtime_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Realtime) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS-Realtime) |

## Supported Languages

MOSS-TTS, MOSS-TTSD and MOSS-TTS-Realtime currently supports **20 languages**:

| Language | Code | Flag | Language | Code | Flag | Language | Code | Flag |
|---|---|---|---|---|---|---|---|---|
| Chinese | zh | 🇨🇳 | English | en | 🇺🇸 | German | de | 🇩🇪 |
| Spanish | es | 🇪🇸 | French | fr | 🇫🇷 | Japanese | ja | 🇯🇵 |
| Italian | it | 🇮🇹 | Hungarian | hu | 🇭🇺 | Korean | ko | 🇰🇷 |
| Russian | ru | 🇷🇺 | Persian (Farsi) | fa | 🇮🇷 | Arabic | ar | 🇸🇦 |
| Polish | pl | 🇵🇱 | Portuguese | pt | 🇵🇹 | Czech | cs | 🇨🇿 |
| Danish | da | 🇩🇰 | Swedish | sv | 🇸🇪 | | | |
| Greek | el | 🇬🇷 | Turkish | tr | 🇹🇷 |  |  |  |


## Quickstart

### OpenClaw API Skills

We add MOSS-TTS skills in [ClawHub](https://clawhub.ai) of 🦞 OpenClaw. You can get your API key from [MOSI AI Studio](https://studio.mosi.cn).

| Skill | Description | Install |
|---|---|---|
| [`feishu-voice-tts`](https://clawhub.ai/helloeveryworlds/feishu-voice-tts) | Send voice messages in Feishu | `clawhub install feishu-voice-tts` |
| [`moss-tts-voice`](https://clawhub.ai/luogao2333/moss-tts-voice) | Call MOSS-TTS API to generate speech | `clawhub install moss-tts-voice` |

### Environment Setup

We recommend a clean, isolated Python environment with **Transformers 5.0.0** to avoid dependency conflicts.

#### Using Conda

```bash
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

Install all required dependencies:

```bash
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

#### Using `uv`

```bash
# Install uv first: https://docs.astral.sh/uv/getting-started/installation/
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install --torch-backend cu128 -e ".[torch-runtime]"
```

#### (Optional) Install FlashAttention 2

For better speed and lower GPU memory usage, you can install FlashAttention 2 if your hardware supports it.

If you use Conda/pip:

```bash
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime,flash-attn]"
```

If your machine has limited RAM and many CPU cores, you can cap build parallelism:

```bash
MAX_JOBS=4 pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime,flash-attn]"
```

If you use `uv`:

```bash
uv pip install --torch-backend cu128 -e ".[torch-runtime,flash-attn]"
```

If your machine has limited RAM and many CPU cores, you can cap build parallelism:

```bash
MAX_JOBS=4 uv pip install --torch-backend cu128 -e ".[torch-runtime,
... [TRUNCATED]
```

### File: README_zh.md
```md
# MOSS-TTS 家族



<br>

<p align="center" style="display:flex; justify-content:center; align-items:center; gap:24px;">
  <img src="./assets/OpenMOSS_Logo.png" height="80" style="display:block; transform: translateY(0px);" />
  <img src="./assets/mosi-logo.png" height="50" style="display:block; transform: translateY(-8px);" />
</p>



<div align="center">
  <a href="https://clawhub.ai/luogao2333/moss-tts-voice"><img src="https://img.shields.io/badge/🦞_OpenClaw-Skills-8A2BE2" alt="OpenClaw"></a>
  <a href="https://huggingface.co/collections/OpenMOSS-Team/moss-tts"><img src="https://img.shields.io/badge/Huggingface-Models-orange?logo=huggingface&amp"></a>
  <a href="https://modelscope.cn/collections/OpenMOSS-Team/MOSS-TTS"><img src="https://img.shields.io/badge/ModelScope-Models-lightgrey?logo=modelscope&amp"></a>
  <a href="https://mosi.cn/#models"><img src="https://img.shields.io/badge/Blog-View-blue?logo=internet-explorer&amp"></a>
  <a href="https://arxiv.org/abs/2603.18090"><img src="https://img.shields.io/badge/Arxiv-2603.18090-red?logo=Arxiv&amp"></a>

  <a href="https://studio.mosi.cn"><img src="https://img.shields.io/badge/AIStudio-Try-green?logo=internet-explorer&amp"></a>
  <a href="https://studio.mosi.cn/docs/moss-tts"><img src="https://img.shields.io/badge/API-Docs-00A3FF?logo=fastapi&amp"></a>
  <a href="https://x.com/Open_MOSS"><img src="https://img.shields.io/badge/Twitter-Follow-black?logo=x&amp"></a>
  <a href="https://discord.gg/fvm5TaWjU3"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp"></a>
  <a href="./assets/wechat.jpg"><img src="https://img.shields.io/badge/WeChat-Join-07C160?logo=wechat&amp;logoColor=white" alt="WeChat"></a>
  
</div>


[English](README.md) | [简体中文](README_zh.md)


MOSS‑TTS 家族是由 [MOSI.AI](https://mosi.cn/#hero) 与 [OpenMOSS 团队](https://www.open-moss.com/) 推出的开源 **语音与声音生成模型家族**。该系列面向 **高保真**、**高表现力** 与 **复杂真实场景** 设计，覆盖稳定长文本语音、多说话人对话、音色/角色设计、环境音效以及实时流式 TTS 等能力。

<a id="news"></a>
## 新闻
* 2026.3.31: 📄 [MOSS-TTSD](https://arxiv.org/pdf/2603.19739) 和 [MOSS-VoiceGenerator](https://arxiv.org/pdf/2603.28086) 的技术报告现已在arXiv上发布！
* 2026.3.26: 📘 新增 MOSS-TTS-Realtime 微调教程！
* 2026.3.20: 📄 我们的[技术报告](https://arxiv.org/pdf/2603.18090)现已在arXiv上发布！
* 2026.3.18：🚀 在配套仓库 [`OpenMOSS/llama.cpp`](https://github.com/OpenMOSS/llama.cpp/tree/moss-tts-firstclass) 中新增了 first-class MOSS-TTS `llama.cpp` 实现，提供 GGUF backbone 推理与 ONNX 音频编解码器解码的端到端可运行链路。可从 [first-class e2e 指南](https://github.com/OpenMOSS/llama.cpp/blob/moss-tts-firstclass/docs/moss-tts-firstclass-e2e_zh.md) 开始。
* 2026.3.16：📘 新增 MossTTSLocal 架构微调教程，适用于 MOSS-TTS-Local-Transformer！
* 2026.3.12：🚀 新增面向 `MossTTSDelay` 架构的 SGLang 后端支持，可用于 MOSS-TTS（Delay）和 MOSS-SoundEffect 的高效推理，生成吞吐可提升约 **3 倍**！
* 2026.3.11：📘 新增 MossTTSDelay 架构微调教程，适用于 MOSS-TTS（Delay）、MOSS-TTSD、MOSS-VoiceGenerator 和 MOSS-SoundEffect！
* 2026.3.10：⚡️ 大幅优化了 llama.cpp 推理管线的显存占用。现在 8B 模型可以运行在 8GB 显存的 GPU 上！
* 2026.3.4：新增 **无 PyTorch 推理** 支持 — 通过 [llama.cpp](https://github.com/ggerganov/llama.cpp) + ONNX Runtime 实现端侧轻量部署。量化 GGUF 权重发布于 [`OpenMOSS-Team/MOSS-TTS-GGUF`](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-GGUF)，ONNX 音频编解码器发布于 [`OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX`](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX)。详见 [llama.cpp 后端](#llamacpp-后端无-pytorch-推理)。
* 2026.3.4：🎉 我们在 🦞 龙虾 的 [ClawHub](https://clawhub.ai) 平台上架了 MOSS-TTS skills：[feishu-voice-tts](https://clawhub.ai/helloeveryworlds/feishu-voice-tts) 与 [moss-tts-voice](https://clawhub.ai/luogao2333/moss-tts-voice)。
* 2026.2.10：🎉🎉🎉 我们已发布 [MOSS-TTS Family](https://huggingface.co/collections/OpenMOSS-Team/moss-tts)。更多详情请查看我们的 [Blog](https://mosi.cn/#models)！我们的 Huggingface Space 在这里：[MOSS-TTS](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS), [MOSS-TTSD-v1.0](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTSD-v1.0), [MOSS-VoiceGenerator](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-VoiceGenerator).

## 演示

<div align="center">
  <video src="https://gist.github.com/user-attachments/assets/fdce9f66-20ec-45e8-9615-89606ae2fbe8" width="70%" poster=""> </video>
</div>


## 目录

- [介绍](#introduction)
- [模型架构](#architecture)
- [已发布模型](#released-models)
- [支持的语言](#supported-languages)
- [快速开始](#quickstart)
  - [OpenClaw API Skills](#openclaw-api-skills)
  - [环境准备](#environment-setup)
  - [（可选）安装 FlashAttention 2](#optional-install-flashattention-2)
  - [基础用法](#moss-tts-basic-usage)
  - [微调](#fine-tuning)
- [llama.cpp 后端（无 PyTorch 推理）](#llamacpp-后端无-pytorch-推理)
- [SGLang 后端（加速推理）](#sglang-后端加速推理)
- [评测](#evaluation)
  - [MOSS-TTS 评测](#eval-moss-tts)
  - [MOSS-TTSD 评测](#eval-moss-ttsd)
  - [MOSS-VoiceGenerator 评测](#eval-moss-voicegenerator)
- [语音编解码器](#audio-tokenizer)
  - [介绍](#audio-tokenizer-intro)
  - [模型权重](#model-weights)
  - [重建质量客观评测](#重建质量客观评测)
- [更多信息](#more-information-zh)
  - [社区项目](#community-projects-zh)
- [引用](#引用)


<a id="introduction"></a>
## 介绍

<p align="center">
  <img src="./assets/moss_tts_family.jpeg" width="85%" />
</p>

当一段音频需要 **听起来像真实的人类**、**准确发音**、**在不同内容间切换说话风格**、**稳定持续数十分钟**，并且 **支持对话、角色扮演与实时交互** 时，单一 TTS 模型往往不足以胜任。**MOSS‑TTS 家族**将工作流拆分为 5 个可独立使用、亦可组合成完整管线的量产级模型。

- **MOSS‑TTS**：MOSS‑TTS 是家族中的旗舰量产级 TTS 基础模型，**核心能力是高保真以及最优性能的零样本语音克隆**，支持**长文本长语音生成**、**拼音、音标与时长精细控制**，以及**多语种/中英混合合成**。它可作为大规模旁白、配音和语音产品的核心底座。
- **MOSS‑TTSD**：MOSS‑TTSD 是对话语音生成模型，用于生成高表现力、多说话人、超长连续对话的音频。本次我们更新了全新的**v1.0版本**，相比于0.7版本，它在音色相似度，说话人切换准确率，词错误率等**客观指标上取得了业界最优的性能**，在竞技场主观评测中，也**战胜了豆包、Gemini2.5-pro**等顶尖闭源模型。详情请访问 [MOSS-TTSD 仓库](https://github.com/OpenMOSS/MOSS-TTSD)。
- **MOSS‑VoiceGenerator**：MOSS‑VoiceGenerator 是开源音色设计模型，可从文本风格指令直接生成多样的说话人音色或风格，**无需参考音频**。它统一音色设计、风格控制与内容合成，可独立创作，也可作为下游 TTS 的音色设计层。模型性能在**竞技场评分上超过了其余等顶尖音色设计模型**。
- **MOSS‑TTS‑Realtime**：MOSS‑TTS‑Realtime 是面向实时语音智能体的多轮上下文感知实时 TTS 模型。它结合多轮对话中的文本与历史语音信号进行低时延增量合成，使多轮回复保持连贯、自然且音色一致。**非常适合搭配文本模型构建低时延语音智能体**。MOSS‑TTS‑Realtime 的 TTFB（Time To First Byte）达到180ms，$T_{\text{LLM-first-sentence}} + T_{\text{MOSS-TTS-Realtime-TTFB}}$ 整体为377ms。
- **MOSS‑SoundEffect**：MOSS‑SoundEffect 是面向内容制作的**音效生成**模型，具备广泛类别覆盖与可控时长能力。它能根据文本指令生成自然环境、城市场景、生物、人类动作与类音乐片段等音频，适用于影视、游戏、交互体验和数据合成。

<a id="architecture"></a>
## 模型架构

我们在统一训练/评测框架下将 **MossTTSDelay** 与 **MossTTSLocal** 作为互补基线：**Delay** 更强调长上下文稳定性、推理速度与工程可用性，**Local** 更强调轻量灵活和面向流式场景的客观指标表现。二者共同提供可复现、可对比的落地与研究参考。

**MossTTSRealtime** 不是第三个对比基线，而是面向语音智能体的能力型设计。它同时利用历史文本与用户语音声学信息建模多轮上下文，以低时延流式合成保持回复连贯和音色一致。


| 架构  | 核心机制 | 架构细节 |
|---|---|---|
| `MossTTSDelay` |  多头并行 RVQ 预测，结合延迟模式调度 | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_delay/README.md) |
| `MossTTSLocal` | 基于深度 Transformer 的时间同步 RVQ 模块 | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_local/README.md) |
| `MossTTSRealtime` | 用于实时合成的分层文本-音频输入 | [![Arch Details](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](moss_tts_realtime/README.md) |

<a id="released-models"></a>
## 模型概览

| Model | Architecture | Size | Model Card | Hugging Face | ModelScope |
|---|---|---:|---|---|---|
| **MOSS-TTS** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS) |
|  | `MossTTSLocal` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Local-Transformer) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS-Local-Transformer) |
| **MOSS‑TTSD‑V1.0** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_ttsd_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTSD-v1.0) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTSD-v1.0) |
| **MOSS‑VoiceGenerator** | `MossTTSDelay` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_voice_generator_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-VoiceGenerator) |
| **MOSS‑SoundEffect** | `MossTTSDelay` | 8B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_sound_effect_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-SoundEffect) |
| **MOSS‑TTS‑Realtime** | `MossTTSRealtime` | 1.7B | [![Model Card](https://img.shields.io/badge/Model%20Card-View-blue?logo=markdown)](docs/moss_tts_realtime_model_card.md) | [![Hugging Face](https://img.shields.io/badge/Huggingface-Model-orange?logo=huggingface)](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Realtime) | [![ModelScope](https://img.shields.io/badge/ModelScope-Model-lightgrey?logo=modelscope)](https://modelscope.cn/models/openmoss/MOSS-TTS-Realtime) |

<a id="supported-languages"></a>

## 支持的语言

MOSS-TTS、MOSS-TTSD 和 MOSS-TTS-Realtime 目前支持 **20 种语言**：

| Language | Code | Flag | Language | Code | Flag | Language | Code | Flag |
|---|---|---|---|---|---|---|---|---|
| 中文 | zh | 🇨🇳 | 英语 | en | 🇺🇸 | 德语 | de | 🇩🇪 |
| 西班牙语 | es | 🇪🇸 | 法语 | fr | 🇫🇷 | 日语 | ja | 🇯🇵 |
| 意大利语 | it | 🇮🇹 | 匈牙利语 | hu | 🇭🇺 | 韩语 | ko | 🇰🇷 |
| 俄语 | ru | 🇷🇺 | 波斯语（法尔西语） | fa | 🇮🇷 | 阿拉伯语 | ar | 🇸🇦 |
| 波兰语 | pl | 🇵🇱 | 葡萄牙语 | pt | 🇵🇹 | 捷克语 | cs | 🇨🇿 |
| 丹麦语 | da | 🇩🇰 | 瑞典语 | sv | 🇸🇪 | | | |
| 希腊语 | el | 🇬🇷 | 土耳其语 | tr | 🇹🇷 |  |  |  |



<a id="quickstart"></a>
## 快速开始

### OpenClaw API Skills

我们在🦞 龙虾 的 [ClawHub](https://clawhub.ai) 平台上架了 MOSS-TTS skills。API Key 可在 [MOSI AI Studio](https://studio.mosi.cn) 获取。

| Skill | 说明 | 安装命令 |
|---|---|---|
| [`feishu-voice-tts`](https://clawhub.ai/helloeveryworlds/feishu-voice-tts) | 在飞书发送语音消息 | `clawhub install feishu-voice-tts` |
| [`moss-tts-voice`](https://clawhub.ai/luogao2333/moss-tts-voice) | 调用 MOSS-TTS API 生成语音 | `clawhub install moss-tts-voice` |

<a id="environment-setup"></a>
### 环境准备

建议使用干净的 Python 环境。

#### 使用 Conda

```bash
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

安装全部依赖：

```bash
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

#### 使用 `uv`

```bash
# 请先安装 uv：https://docs.astral.sh/uv/getting-started/installation/
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install --torch-backend cu128 -e ".[torch-runtime]"
```
<a id="optional-install-flashattention-2"></a>
#### （可选）安装 FlashAttention 2

如果你的硬件支持，可以安装 FlashAttention 2 以提升速度并降低显存占用。

如果你使用 Conda/pip：

```bash
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime,flash-attn]"
```

如果机器内存较小、CPU 核数较多，可以限制并行编译数：

```bash
MAX_JOBS=4 pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime,flash-attn]"
```

如果你使用 `uv`：

```bash
uv pip install --torch-backend cu128 -e ".[torch-runtime,flash-attn]"
```

如果机器内存较小、CPU 核心较多，可以限制并行编译数：

```bash
MAX_JOBS=4 uv pip install --torch-backend cu128 -e ".[torch-runtime,flash-attn]"
```

说明：
- 依赖统一在 `pyproject.toml` 中管理，当前固定了 `torch==2.9.1+cu128` 和 `torchaudio==2.9.1+cu128`。
- `uv` 方案中使用 `--torch-backend cu128`，由 uv 处理 PyTorch CUDA 轮子来源，同时其余依赖仍使用默认安全索引策略解析。
- 如果需要其他后端，可将 `cu128` 替换为目标后端（例如 `cpu`、`cu126`）。
- 如果 FlashAttention 2 编译失败，可以跳过，直接使用默认 attention 后端。
- FlashAttention 2 仅支持部分 GPU，通常搭配 `torch.float16` 或 `torch.bfloat16` 使用。


<a id="moss-tts-basic-usage"></a>
### MOSS‑TTS 基础用法

如果你更希望使用 Gradio 界面，我们为 4 个主模型提供了对应脚本：

| Model | Script | 
|---|---|
| MOSS-TTS | [clis/moss_tts_app.py](clis/moss_tts_app.py) |
| MOSS-TTSD | [clis/moss_ttsd_app.py](clis/moss_ttsd_app.py) | 
| MOSS-VoiceGenerator | [clis/moss_voice_generator_app.py](clis/moss_voice_generator_app.py) | 
| MOSS-SoundEffect | [clis/moss_sound_effect_app.py](clis/moss_sound_effect_app.py) |

MOSS-TTS-Realtime 的 Gradio demo 请直接参考 [MOSS-TTS-Realtime Model Card](docs/moss_tts_realtime_model_card.md)

```python
from pathlib import Path
import importlib.util
import torch
import torchaudio
from transformers import AutoModel, AutoProcessor
# Disable the broken cuDNN SDPA backend
torch.backends.cuda.enable_cudnn_sdp(False)
# Keep these enabled as fallbacks
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(True)


pretrained_model_name_or_path = "OpenMOSS-Team/MOSS-TTS"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

def resolve_attn_implementation() -> str:
    # Prefer FlashAttention 2 when package + device conditions are met.
    if (
        device == "cuda"
        and importlib.util.find_spec("flash_attn") is not None
        and dtype in {torch.float16, torch.bfloat16}
    ):
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            return "flash_attention_2"

    # CUDA fallback: use PyTorch SDPA kernels.
    if device == "cuda":
        return "sdpa"

    # CPU fallback.
    return "eager"


attn_implementation = resolve_attn_implementation()
print(f"[INFO] Using attn_implementation={attn_implementation}")

processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)

text_1 = "亲爱的你，\n你好呀。\n\n今天，我想用最认真、最温柔的声音，对你说一些重要的话。\n这些话，像一颗小小的星星，希望能在你的心里慢慢发光。\n\n首先，我想祝你——\n每天都能平平安安、快快乐乐。\n\n希望你早上醒来的时候，\n窗外有光，屋子里很安静，\n你的心是轻轻的，没有着急，也没有害怕。\n\n希望你吃饭的时候胃口很好，\n走路的时候脚步稳稳，\n晚上睡觉的时候，能做一个又一个甜甜的梦。\n\n我希望你能一直保持好奇心。\n对世界充满问题，\n对天空、星星、花草、书本和故事感兴趣。\n当你问“为什么”的时候，\n希望总有人愿意认真地听你说话。\n\n我也希望你学会温柔。\n温柔地对待朋友，\n温柔地对待小动物，\n也温柔地对待自己。\n\n如果有一天你犯了错，\n请不要太快责怪自己，\n因为每一个认真成长的人，\n都会在路上慢慢学会更好的方法。\n\n愿你拥有勇气。\n当你站在陌生的地方时，\n当你第一次举手发言时，\n当你遇到困难、感到害怕的时候，\n希望你能轻轻地告诉自己：\n“我可以试一试。”\n\n就算没有一次成功，也没有关系。\n失败不是坏事，\n它只是告诉你，你正在努力。\n\n我希望你学会分享快乐。\n把开心的事情告诉别人，\n把笑声送给身边的人，\n因为快乐被分享的时候，\n会变得更大、更亮。\n\n如果有一天你感到难过，\n我希望你知道——\n难过并不丢脸，\n哭泣也不是软弱。\n\n愿你能找到一个安全的地方，\n慢慢把心里的话说出来，\n然后再一次抬起头，看见希望。\n\n我还希望你能拥有梦想。\n这个梦想也许很大，\n也许很小，\n也许现在还说不清楚。\n\n没关系。\n梦想会和你一
... [TRUNCATED]
```

### File: docs\moss_sound_effect_model_card.md
```md
# MOSS-SoundEffect Model Card

**MOSS-SoundEffect** is the **environment sound & sound effect generation model** in the **MOSS‑TTS Family**. It generates ambient soundscapes and concrete sound effects directly from text descriptions, and is designed to complement speech content with immersive context in production workflows.


## 1. Overview

### 1.1 TTS Family Positioning

MOSS-SoundEffect is designed as an audio generation backbone for creating high-fidelity environmental and action sounds from text, serving both scalable content pipelines and a strong research baseline for controllable audio generation.

**Design goals**
* **Coverage & richness**: broad sound taxonomy with layered ambience and realistic texture
* **Composability**: easy integration into creative pipelines (games/film/tools) and synthetic data generation setups


### 1.2 Key Capabilities
MOSS‑SoundEffect focuses on **contextual audio completion** beyond speech, enabling creators and systems to enrich scenes with believable acoustic environments and action‑level cues.

**What it can generate**
- **Natural environments**: e.g., “fresh snow crunching under footsteps.”
- **Urban environments**: e.g., “a sports car roaring past on the highway.”
- **Animals & creatures**: e.g., “early morning park with birds chirping in a quiet atmosphere.”
- **Human actions**: e.g., “clear footsteps echoing on concrete at a steady rhythm.”

**Why it matters**
- Completes **scene immersion** for narrative content, film/TV, documentaries, games, and podcasts.
- Supports **voice agents** and interactive systems that need ambient context, not just speech.
- Acts as the **sound‑design layer** of the MOSS‑TTS Family’s end‑to‑end workflow.



### 1.3 Model Architecture
**MOSS-SoundEffect** employs the **MossTTSDelay** architecture (see [moss_tts_delay/README.md](../moss_tts_delay/README.md)), reusing the same discrete token generation backbone for audio synthesis. A text prompt (optionally with simple control tags such as **duration**) is tokenized and fed into the Delay-pattern autoregressive model to predict **RVQ audio tokens** over time. The generated tokens are then decoded by the audio tokenizer/vocoder to produce high-fidelity sound effects, enabling consistent quality and controllable length across diverse SFX categories.



### 1.4 Released Models
**Recommended decoding hyperparameters**
| Model | audio_temperature | audio_top_p | audio_top_k | audio_repetition_penalty |
|---|---:|---:|---:|---:|
| **MOSS-SoundEffect** | 1.5 | 0.6 | 50 | 1.2 |


## 2. Quick Start



```python
from pathlib import Path
import importlib.util
import torch
import torchaudio
from transformers import AutoModel, AutoProcessor
# Disable the broken cuDNN SDPA backend
torch.backends.cuda.enable_cudnn_sdp(False)
# Keep these enabled as fallbacks
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(True)


pretrained_model_name_or_path = "OpenMOSS-Team/MOSS-SoundEffect"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

def resolve_attn_implementation() -> str:
    # Prefer FlashAttention 2 when package + device conditions are met.
    if (
        device == "cuda"
        and importlib.util.find_spec("flash_attn") is not None
        and dtype in {torch.float16, torch.bfloat16}
    ):
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            return "flash_attention_2"

    # CUDA fallback: use PyTorch SDPA kernels.
    if device == "cuda":
        return "sdpa"

    # CPU fallback.
    return "eager"


attn_implementation = resolve_attn_implementation()
print(f"[INFO] Using attn_implementation={attn_implementation}")

processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)

text_1 = "雷声隆隆，雨声淅沥。"
text_2 = "清晰脚步声在水泥地面回响，节奏稳定。"

conversations = [
    [processor.build_user_message(ambient_sound=text_1)],
    [processor.build_user_message(ambient_sound=text_2)]
]

model = AutoModel.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
    attn_implementation=attn_implementation,
    torch_dtype=dtype,
).to(device)
model.eval()

batch_size = 1

save_dir = Path("inference_root")
save_dir.mkdir(exist_ok=True, parents=True)
sample_idx = 0
with torch.no_grad():
    for start in range(0, len(conversations), batch_size):
        batch_conversations = conversations[start : start + batch_size]
        batch = processor(batch_conversations, mode="generation")
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=4096,
        )

        for message in processor.decode(outputs):
            audio = message.audio_codes_list[0]
            out_path = save_dir / f"sample{sample_idx}.wav"
            sample_idx += 1
            torchaudio.save(out_path, audio.unsqueeze(0), processor.model_config.sampling_rate)
```

### Input Types

**UserMessage**
| Field | Type | Required | Description |
|---|---|---:|---|
| `ambient_sound` | `str` | Yes | Description of environment sound & sound effect |
| `tokens` | `int` | No | Expected number of audio tokens. **1s ≈ 12.5 tokens**. |

```

### File: docs\moss_ttsd_model_card.md
```md
# MOSS-TTSD

**MOSS-TTSD** is a long-form spoken dialogue generation model that enables highly expressive multi-party conversational speech synthesis across multiple languages. It supports continuous long-duration generation, flexible multi-speaker dialogue control, and state-of-the-art zero-shot voice cloning with only short reference audio. MOSS-TTSD is designed for real-world long-form content creation, including podcasts, audiobook, sports and esports commentary, dubbing, crosstalk, and entertainment scenarios.


## 1. Overview

### 1.1 TTS Family Positioning
MOSS-TTSD is the Long-Form Dialogue Specialist in our open-source TTS Family. While our foundational models focus on high-fidelity single-speaker synthesis, MOSS-TTSD extends this capability into the realm of complex, multi-party interactions. It is designed to bridge the gap between distinct audio samples and cohesive, continuous conversation.

**Design Goals**
- **Authentic Interaction**: Capturing the natural rhythm, overlaps, and dynamics of human conversation.
- **Sustained Coherence**: Maintaining speaker identity and contextual consistency over extended durations (up to 1 hour).
- **Production Adaptability**: Serving diverse high-end scenarios from rigorous audiobook narration to dynamic sports commentary.

### 1.2 Key Capabilities
MOSS-TTSD transforms static text into living conversations, offering features specifically optimized for multi-speaker environments:

- **Multi-Party Conversational Generation** — Unlike traditional TTS which optimizes for reading, MOSS-TTSD masters the rhythm of conversation. It supports 1 to 5 speakers with flexible control, handling natural turn-taking, overlapping speech patterns, and distinct persona maintenance.

- **Extreme Long-Context Modeling** — Moving beyond short-sentence generation, the model is architected for stability over long durations, supporting up to 60 minutes of coherent audio in a single session without losing speaker identity or prosodic quality.

- **Diverse Scenario Adaptation** — The model is fine-tuned on high-variability scenarios to handle different speaking styles:
  - Conversational Media: AI Podcasts, Interviews.
  - Dynamic Commentary: High-energy Sports/Esports shouting and analysis.
  - Entertainment: Audiobooks (narrator + characters), Dubbing, and Crosstalk (Xiangsheng).

- **Multilingual & Zero-Shot Cloning** — Features state-of-the-art zero-shot voice cloning requiring only short reference audio (3-10s), with robust cross-lingual performance across major languages including Chinese, English, Japanese, and European languages.

### 1.3 Model Architecture

MOSS-TTSD is built on top of **Delay Pattern (MossTTSDelay)** from our MOSS-TTS foundation model — a single Transformer backbone with multi-head parallel prediction using delay scheduling for multi-codebook audio tokens. 

For full architecture details, see **`moss_tts_delay/README.md`**.

### 1.4 Released Models

| Model | Architecture | NVQ | Parameters |
|-------|-------------|-----|------------|
| MOSS-TTSD | Delay Pattern (MossTTSDelay) | 16 | 8B |

**Recommended decoding hyperparameters**

| Model | audio_temperature | audio_top_p | audio_top_k | audio_repetition_penalty |
|---|---:|---:|---:|---:|
| **MOSS-TTSD** | 1.1 | 0.9 | 50 | 1.1 |

## 2. Quick Start

MOSS-TTSD uses a **continuation** workflow: provide reference audio for each speaker, their transcripts as a prefix, and the dialogue text to generate. The model continues in each speaker's identity.

```python
from pathlib import Path
import importlib.util
import torch
import torchaudio
from transformers import AutoModel, AutoProcessor
# Disable the broken cuDNN SDPA backend
torch.backends.cuda.enable_cudnn_sdp(False)
# Keep these enabled as fallbacks
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(True)

pretrained_model_name_or_path = "OpenMOSS-Team/MOSS-TTSD-v1.0"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

def resolve_attn_implementation() -> str:
    # Prefer FlashAttention 2 when package + device conditions are met.
    if (
        device == "cuda"
        and importlib.util.find_spec("flash_attn") is not None
        and dtype in {torch.float16, torch.bfloat16}
    ):
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            return "flash_attention_2"

    # CUDA fallback: use PyTorch SDPA kernels.
    if device == "cuda":
        return "sdpa"

    # CPU fallback.
    return "eager"


attn_implementation = resolve_attn_implementation()
print(f"[INFO] Using attn_implementation={attn_implementation}")

processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)

model = AutoModel.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
    attn_implementation=attn_implementation,
    torch_dtype=dtype,
).to(device)
model.eval()

# --- Inputs ---

# Use audio from ./assets/audio to avoid downloading from the cloud.
prompt_audio_speaker1 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_02_s1.wav"
prompt_audio_speaker2 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_02_s2.wav"
prompt_text_speaker1 = "[S1] In short, we embarked on a mission to make America great again for all Americans."
prompt_text_speaker2 = "[S2] NVIDIA reinvented computing for the first time after 60 years. In fact, Erwin at IBM knows quite well that the computer has largely been the same since the 60s."

text_to_generate = "[S1] Listen, let's talk business. China. I'm hearing things. People are saying they're catching up. Fast. What's the real scoop? Their AI—is it a threat? [S2] Well, the pace of innovation there is extraordinary, honestly. They have the researchers, and they have the drive. [S1] Extraordinary? I don't like that. I want us to be extraordinary. Are they winning? [S2] I wouldn't say winning, but their progress is very promising. They are building massive clusters. They're very determined. [S1] Promising. There it is. I hate that word. When China is promising, it means we're losing. It's a disaster, Jensen. A total disaster. "

# --- Load & resample audio ---

target_sr = int(processor.model_config.sampling_rate)
wav1, sr1 = torchaudio.load(prompt_audio_speaker1)
wav2, sr2 = torchaudio.load(prompt_audio_speaker2)

if wav1.shape[0] > 1:
    wav1 = wav1.mean(dim=0, keepdim=True)
if wav2.shape[0] > 1:
    wav2 = wav2.mean(dim=0, keepdim=True)
if sr1 != target_sr:
    wav1 = torchaudio.functional.resample(wav1, sr1, target_sr)
if sr2 != target_sr:
    wav2 = torchaudio.functional.resample(wav2, sr2, target_sr)

# --- Build conversation ---

reference_audio_codes = processor.encode_audios_from_wav([wav1, wav2], sampling_rate=target_sr)
concat_prompt_wav = torch.cat([wav1, wav2], dim=-1)
prompt_audio = processor.encode_audios_from_wav([concat_prompt_wav], sampling_rate=target_sr)[0]

full_text = f"{prompt_text_speaker1} {prompt_text_speaker2} {text_to_generate}"

conversations = [
    [
        processor.build_user_message(
            text=full_text,
            reference=reference_audio_codes,
        ),
        processor.build_assistant_message(
            audio_codes_list=[prompt_audio]
        ),
    ],
]

# --- Inference ---

batch_size = 1

save_dir = Path("inference_root")
save_dir.mkdir(exist_ok=True, parents=True)
sample_idx = 0
with torch.no_grad():
    for start in range(0, len(conversations), batch_size):
        batch_conversations = conversations[start : start + batch_size]
        batch = processor(batch_conversations, mode="continuation")
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=2000,
        )

        for message in processor.decode(outputs):
            audio = message.audio_codes_list[0]
            out_path = save_dir / f"sample{sample_idx}.wav"
            sample_idx += 1
            torchaudio.save(out_path, audio.unsqueeze(0), processor.model_config.sampling_rate)

```

### Input Types

**UserMessage**

| Field | Type | Required | Description |
|---|---|---:|---|
| `text` | `str` | Yes | Full dialogue text including speaker tags (`[S1]`, `[S2]`, ...) and prompt transcripts. |
| `reference` | `List` | Yes | Per-speaker reference audio codes from `processor.encode_audios_from_wav()`. |

**AssistantMessage**

| Field | Type | Required | Description |
|---|---|---:|---|
| `audio_codes_list` | `List` | Yes | Concatenated prompt audio codes for all speakers. |

### Generation Hyperparameters

| Parameter | Type | Default | Description |
|---|---|---:|---|
| `max_new_tokens` | `int` | — | Controls total generated audio tokens. **1s ≈ 12.5 tokens**. |
| `audio_temperature` | `float` | 1.1 | Higher values increase variation; lower values stabilize prosody. |
| `audio_top_p` | `float` | 0.9 | Nucleus sampling cutoff. |
| `audio_top_k` | `int` | 50 | Top-K sampling. |
| `audio_repetition_penalty` | `float` | 1.1 | >1.0 discourages repeating patterns. |


## 3. Evaluation
### Objective Evaluation(TTSD-eval)



We introduce a robust evaluation framework leveraging **MMS-FA** for alignment and **wespeaker** for embedding extraction to ensure precise speaker attribution.



- **Method**: Forced-alignment based segmentation + Similarity-based speaker verification.

- **Metrics**: 
  - **Speaker Attribution Accuracy (ACC)**
  - **Speaker Similarity (SIM)**
  - **Word Error Rate (WER)** computed using **Whisper-large-v3**.

- **Dataset**: 100 multi-turn dialogues (CN/EN) spanning 30s–720s. Covers diverse scenarios including Podcasts, TV dubbing, and Crosstalk. 

Please refer to [TTSD-eval](https://github.com/OpenMOSS/TTSD-eval) for the code and data.
<br>

| Model | ZH - SIM | ZH - ACC | ZH - WER | EN - SIM | EN - ACC | EN - WER |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Comparison with Open-Source Models** | | | | | | |
| MOSS-TTSD | **0.7949** | **0.9587** | **0.0485** | **0.7326** | **0.9626** | 0.0988 |
| MOSS-TTSD v0.7 | 0.7423 | 0.9391 | 0.0517 | 0.6743 | 0.9266 | 0.1612 |
| Vibevoice 7B | 0.7590 | 0.9222 | 0.0570 | 0.7140 | 0.9554 | **0.0946** |
| Vibevoice 1.5 B | 0.7415 | 0.8798 | 0.0818 | 0.6961 | 0.9353 | 0.1133 |
| FireRedTTS2 | 0.7383 | 0.9022 | 0.0768 | - | - | - |
| Higgs Audio V2 | - | - | - | 0.6860 | 0.9025 | 0.2131 |
| **Comparison with Proprietary Models** | | | | | | |
| Eleven V3 | 0.6970 | 0.9653 | **0.0363** | 0.6730 | 0.9498 | **0.0824** |
| MOSS-TTSD (elevenlabs_voice) | **0.8165** | **0.9736** | 0.0391 | **0.7304** | **0.9565** | 0.1005 |
| | | | | | | |
| gemini-2.5-pro-preview-tts | - | - | - | 0.6786 | 0.9537 | **0.0859** |
| gemini-2.5-flash-preview-tts | - | - | - | 0.7194 | 0.9511 | 0.0871 |
| MOSS-TTSD (gemini_voice) | - | - | - | **0.7893** | **0.9655** | 0.0984 |
| | | | | | | |
| Doubao_Podcast | 0.8034 | 0.9606 | **0.0472** | - | - | - |
| MOSS-TTSD (doubao_voice) | **0.8226** | **0.9630** | 0.0571 | - | - | - |

### Subjective Evaluation
For open-source models, annotators are asked to score each sample pair in terms of speaker attribution accuracy, voice similarity, prosody, and overall quality. Following the methodology of the LMSYS Chatbot Arena, we compute Elo ratings and confidence intervals for each dimension.
![alt text](../assets/VS_Open-Source_Models.jpg)

For closed-source models, annotators are only asked to choose the overall preferred one in each pair, and we compute the win rate accordingly.
![alt text](../assets/VS_Proprietary_Models.png)
```

### File: docs\moss_tts_model_card.md
```md
# MOSS-TTS Model Card

**MOSS-TTS** is a next-generation, production-grade TTS foundation model focused on **voice cloning**, **ultra-long stable speech generation**, **token-level duration control**, **multilingual & code-switched synthesis**, and **fine-grained Pinyin/phoneme-level pronunciation control**. It is built on a clean autoregressive discrete-token recipe that emphasizes high-quality audio tokenization, large-scale diverse pre-training data, and efficient discrete token modeling.



## 1. Overview

### 1.1 TTS Family Positioning
MOSS-TTS is the **flagship base model** in our open-source **TTS Family**. It is designed as a production-ready synthesis backbone that can serve as the primary high-quality engine for scalable voice applications, and as a strong research baseline for controllable TTS and discrete audio token modeling.

**Design goals**
- **Production readiness**: robust voice cloning with stable, on-brand speaker identity at scale
- **Controllability**: duration and pronunciation controls that integrate into real workflows
- **Long-form stability**: consistent identity and delivery for extended narration
- **Multilingual coverage**: multilingual and code-switched synthesis as first-class capabilities



### 1.2 Key Capabilities

MOSS-TTS delivers state-of-the-art quality while providing the fine-grained controllability and long-form stability required for production-grade voice applications, from zero-shot cloning and hour-long narration to token- and phoneme-level control across multilingual and code-switched speech.

* **State-of-the-art evaluation performance** — top-tier objective and subjective results across standard TTS benchmarks and in-house human preference testing, validating both fidelity and naturalness.
* **Zero-shot Voice Cloning (Voice Clone)** — clone a target speaker’s timbre (and part of speaking style) from short reference audio, without speaker-specific fine-tuning.
* **Ultra-long Speech Generation (up to 1 hour)** — support continuous long-form speech generation for up to one hour in a single run, designed for extended narration and long-session content creation.
* **Token-level Duration Control** — control pacing, rhythm, pauses, and speaking rate at token resolution for precise alignment and expressive delivery.
* **Phoneme-level Pronunciation Control** — supports:

  * pure **Pinyin** input
  * pure **IPA** phoneme input
  * mixed **Chinese / English / Pinyin / IPA** input in any combination
* **Multilingual support** — high-quality multilingual synthesis with robust generalization across languages and accents.
* **Code-switching** — natural mixed-language generation within a single utterance (e.g., Chinese–English), with smooth transitions, consistent speaker identity, and pronunciation-aware rendering on both sides of the switch.



### 1.3 Model Architecture

MOSS-TTS includes **two complementary architectures**, both trained and released to explore different performance/latency tradeoffs and to support downstream research.

**Architecture A: Delay Pattern (MossTTSDelay)**
- Single Transformer backbone with **(n_vq + 1) heads**.
- Uses **delay scheduling** for multi-codebook audio tokens.
- Strong long-context stability, efficient inference, and production-friendly behavior.

**Architecture B: Global Latent + Local Transformer (MossTTSLocal)**
- Backbone produces a **global latent** per time step.
- A lightweight **Local Transformer** emits a token block per step.
- **Streaming-friendly** with simpler alignment (no delay scheduling).

**Why train both?**
- **Exploration of architectural potential** and validation across multiple generation paradigms.
- **Different tradeoffs**: Delay pattern tends to be faster and more stable for long-form synthesis; Local is smaller and excels on objective benchmarks.
- **Open-source value**: two strong baselines for research, ablation, and downstream innovation.

For full details, see:
- **`moss_tts_delay/README.md`**
- **`moss_tts_local/README.md`**



### 1.4 Released Models

| Model | Description |
|---|---|
| **MossTTSDelay-8B** | **Recommended for production**. Faster inference, stronger long-context stability, and robust voice cloning quality. Best for large-scale deployment and long-form narration. |
| **MossTTSLocal-1.7B** | **Recommended for evaluation and research**. Smaller model size with SOTA objective metrics. Great for quick experiments, ablations, and academic studies. |

**Recommended decoding hyperparameters (per model)**

| Model | audio_temperature | audio_top_p | audio_top_k | audio_repetition_penalty |
|---|---:|---:|---:|---:|
| **MossTTSDelay-8B** | 1.7 | 0.8 | 25 | 1.0 |
| **MossTTSLocal-1.7B** | 1.0 | 0.95 | 50 | 1.1 |




## 2. Quick Start

> Tip: For production usage, prioritize **MossTTSDelay-8B**. The examples below use this model; **MossTTSLocal-1.7B** supports the same API, and a practical walkthrough is available in [moss_tts_local/README.md](../moss_tts_local/README.md).

MOSS-TTS provides a convenient `generate` interface for rapid usage. The examples below cover:
1. Direct generation (Chinese / English / Pinyin / IPA)
2. Voice cloning
3. Duration control

```python
from pathlib import Path
import importlib.util
import torch
import torchaudio
from transformers import AutoModel, AutoProcessor
# Disable the broken cuDNN SDPA backend
torch.backends.cuda.enable_cudnn_sdp(False)
# Keep these enabled as fallbacks
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(True)


pretrained_model_name_or_path = "OpenMOSS-Team/MOSS-TTS"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

def resolve_attn_implementation() -> str:
    # Prefer FlashAttention 2 when package + device conditions are met.
    if (
        device == "cuda"
        and importlib.util.find_spec("flash_attn") is not None
        and dtype in {torch.float16, torch.bfloat16}
    ):
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            return "flash_attention_2"

    # CUDA fallback: use PyTorch SDPA kernels.
    if device == "cuda":
        return "sdpa"

    # CPU fallback.
    return "eager"


attn_implementation = resolve_attn_implementation()
print(f"[INFO] Using attn_implementation={attn_implementation}")

processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)

text_1 = "亲爱的你，\n你好呀。\n\n今天，我想用最认真、最温柔的声音，对你说一些重要的话。\n这些话，像一颗小小的星星，希望能在你的心里慢慢发光。\n\n首先，我想祝你——\n每天都能平平安安、快快乐乐。\n\n希望你早上醒来的时候，\n窗外有光，屋子里很安静，\n你的心是轻轻的，没有着急，也没有害怕。\n\n希望你吃饭的时候胃口很好，\n走路的时候脚步稳稳，\n晚上睡觉的时候，能做一个又一个甜甜的梦。\n\n我希望你能一直保持好奇心。\n对世界充满问题，\n对天空、星星、花草、书本和故事感兴趣。\n当你问“为什么”的时候，\n希望总有人愿意认真地听你说话。\n\n我也希望你学会温柔。\n温柔地对待朋友，\n温柔地对待小动物，\n也温柔地对待自己。\n\n如果有一天你犯了错，\n请不要太快责怪自己，\n因为每一个认真成长的人，\n都会在路上慢慢学会更好的方法。\n\n愿你拥有勇气。\n当你站在陌生的地方时，\n当你第一次举手发言时，\n当你遇到困难、感到害怕的时候，\n希望你能轻轻地告诉自己：\n“我可以试一试。”\n\n就算没有一次成功，也没有关系。\n失败不是坏事，\n它只是告诉你，你正在努力。\n\n我希望你学会分享快乐。\n把开心的事情告诉别人，\n把笑声送给身边的人，\n因为快乐被分享的时候，\n会变得更大、更亮。\n\n如果有一天你感到难过，\n我希望你知道——\n难过并不丢脸，\n哭泣也不是软弱。\n\n愿你能找到一个安全的地方，\n慢慢把心里的话说出来，\n然后再一次抬起头，看见希望。\n\n我还希望你能拥有梦想。\n这个梦想也许很大，\n也许很小，\n也许现在还说不清楚。\n\n没关系。\n梦想会和你一起长大，\n在时间里慢慢变得清楚。\n\n最后，我想送你一个最最重要的祝福：\n\n愿你被世界温柔对待，\n也愿你成为一个温柔的人。\n\n愿你的每一天，\n都值得被记住，\n都值得被珍惜。\n\n亲爱的你，\n请记住，\n你是独一无二的，\n你已经很棒了，\n而你的未来，\n一定会慢慢变得闪闪发光。\n\n祝你健康、勇敢、幸福，\n祝你永远带着笑容向前走。"
text_2 = "We stand on the threshold of the AI era.\nArtificial intelligence is no longer just a concept in laboratories, but is entering every industry, every creative endeavor, and every decision. It has learned to see, hear, speak, and think, and is beginning to become an extension of human capabilities. AI is not about replacing humans, but about amplifying human creativity, making knowledge more equitable, more efficient, and allowing imagination to reach further. A new era, jointly shaped by humans and intelligent systems, has arrived."
text_3 = "nin2 hao3，qing3 wen4 nin2 lai2 zi4 na3 zuo4 cheng2 shi4？"
text_4 = "nin2 hao3，qing4 wen3 nin2 lai2 zi4 na4 zuo3 cheng4 shi3？"
text_5 = "您好，请问您来自哪 zuo4 cheng2 shi4？"
text_6 = "/həloʊ, meɪ aɪ æsk wɪtʃ sɪti juː ɑːr frʌm?/"

# Use audio from ./assets/audio to avoid downloading from the cloud.
ref_audio_1 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_zh.wav"
ref_audio_2 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_en.m4a"

conversations = [
    # Direct TTS (no reference)
    [processor.build_user_message(text=text_1)],
    [processor.build_user_message(text=text_2)],
    # Pinyin or IPA input
    [processor.build_user_message(text=text_3)],
    [processor.build_user_message(text=text_4)],
    [processor.build_user_message(text=text_5)],
    [processor.build_user_message(text=text_6)],
    # Voice cloning (with reference)
    [processor.build_user_message(text=text_1, reference=[ref_audio_1])],
    [processor.build_user_message(text=text_2, reference=[ref_audio_2])],
    # Duration control
    [processor.build_user_message(text=text_2, tokens=325)],
    [processor.build_user_message(text=text_2, tokens=600)],
]

model = AutoModel.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
    attn_implementation=attn_implementation,
    torch_dtype=dtype,
).to(device)
model.eval()

batch_size = 1

save_dir = Path("inference_root")
save_dir.mkdir(exist_ok=True, parents=True)
sample_idx = 0
with torch.no_grad():
    for start in range(0, len(conversations), batch_size):
        batch_conversations = conversations[start : start + batch_size]
        batch = processor(batch_conversations, mode="generation")
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=4096,
        )

        for message in processor.decode(outputs):
            audio = message.audio_codes_list[0]
            out_path = save_dir / f"sample{sample_idx}.wav"
            sample_idx += 1
            torchaudio.save(out_path, audio.unsqueeze(0), processor.model_config.sampling_rate)

```

### Continuation + Voice Cloning (Prefix Audio + Text)

MOSS-TTS supports continuation-based cloning: provide a prefix audio clip in the assistant message, and make sure the **prefix transcript** is included in the text. The model continues in the same speaker identity and style.

```python
from pathlib import Path
import importlib.util
import torch
import torchaudio
from transformers import AutoModel, AutoProcessor
# Disable the broken cuDNN SDPA backend
torch.backends.cuda.enable_cudnn_sdp(False)
# Keep these enabled as fallbacks
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(True)


pretrained_model_name_or_path = "OpenMOSS-Team/MOSS-TTS"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

def resolve_attn_implementation() -> str:
    # Prefer FlashAttention 2 when package + device conditions are met.
    if (
        device == "cuda"
        and importlib.util.find_spec("flash_attn") is not None
        and dtype in {torch.float16, torch.bfloat16}
    ):
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            return "flash_attention_2"

    # CUDA fallback: use PyTorch SDPA kernels.
    if device == "cuda":
        return "sdpa"

    # CPU fallback.
    return "eager"


attn_implementation = resolve_attn_implementation()
print(f"[INFO] Using attn_implementation={attn_implementation}")

processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True
)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)

text_1 = "亲爱的你，\n你好呀。\n\n今天，我想用最认真、最温柔的声音，对你说一些重要的话。\n这些话，像一颗小小的星星，希望能在你的心里慢慢发光。\n\n首先，我想祝你——\n每天都能平平安安、快快乐乐。\n\n希望你早上醒来的时候，\n窗外有光，屋子里很安静，\n你的心是轻轻的，没有着急，也没有害怕。\n\n希望你吃饭的时候胃口很好，\n走路的时候脚步稳稳，\n晚上睡觉的时候，能做一个又一个甜甜的梦。\n\n我希望你能一直保持好奇心。\n对世界充满问题，\n对天空、星星、花草、书本和故事感兴趣。\n当你问“为什么”的时候，\n希望总有人愿意认真地听你说话。\n\n我也希望你学会温柔。\n温柔地对待朋友，\n温柔地对待小动物，\n也温柔地对待自己。\n\n如果有一天你犯了错，\n请不要太快责怪自己，\n因为每一个认真成长的人，\n都会在路上慢慢学会更好的方法。\n\n愿你拥有勇气。\n当你站在陌生的地方时，\n当你第一次举手发言时，\n当你遇到困难、感到害怕的时候，\n希望你能轻轻地告诉自己：\n“我可以试一试。”\n\n就算没有一次成功，也没有关系。\n失败不是坏事，\n它只是告诉你，你正在努力。\n\n我希望你学会分享快乐。\n把开心的事情告诉别人，\n把笑声送给身边的人，\n因为快乐被分享的时候，\n会变得更大、更亮。\n\n如果有一天你感到难过，\n我希望你知道——\n难过并不丢脸，\n哭泣也不是软弱。\n\n愿你能找到一个安全的地方，\n慢慢把心里的话说出来，\n然后再一次抬起头，看见希望。\n\n我还希望你能拥有梦想。\n这个梦想也许很大，\n也许很小，\n也许现在还说不清楚。\n\n没关系。\n梦想会和你一起长大，\n在时间里慢慢变得清楚。\n\n最后，我想送你一个最最重要的祝福：\n\n愿你被世界温柔对待，\n也愿你成为一个温柔的人。\n\n愿你的每一天，\n都值得被记住，\n都值得被珍惜。\n\n亲爱的你，\n请记住，\n你是独一无二的，\n你已经很棒了，\n而你的未来，\n一定会慢慢变得闪闪发光。\n\n祝你健康、勇敢、幸福，\n祝你永远带着笑容向前走。"
text_2 = "We stand on the threshold of the AI era.\nArtificial intelligence is no longer just a concept in laboratories, but is entering every industry, every creative endeavor, and every decision. It has learned to see, hear, speak, and think, and is beginning to become an extension of human capabilities. AI is not about replacing humans, but about amplifying human creativity, making knowledge more equitable, more efficient, and allowing imagination to reach further. A new era, jointly shaped by humans and intelligent systems, has arrived."
ref_text_1 = "太阳系八大行星之一。"
ref_text_2 = "But I really can't complain about not having a normal college experience to you."
# Use audio from ./assets/audio to avoid downloading from the cloud.
ref_audio_1 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_zh.wav"
ref_audio_2 = "https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_en.m4a"

conversations = [
    # Continuatoin only
    [
        processor.build_user_message(text=ref_text_1 + text_1),
        processor.build_assistant_message(audio_codes_list=[ref_audio_1])
    ],
    # Continuation with voice cloning
    [
        processor.build_user_message(text=ref_text_2 + text_2, reference=[ref_audio_2]),
        processor.build_assistant_message(audio_codes_list=[ref_audio_2])
    ],
]

model = AutoModel.from_pretrained(
    pretrained_model_name_or_path,
    trust_remote_code=True,
    attn_implementation=attn_implementation,
    torch_dtype=dtype,
).to(device)
model.eval()

batch_size = 1

save_dir = Path("inference_root")
save_dir.mkdir(exist_ok=True, parents=True)
sample_idx = 0
with torch.no_grad():
    for start in range(0, len(conversations), batch_size):
        batch_conversations = conversations[start : start + batch_size]
        batch = processor(batch_conversations, mode="continuation")
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=att
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
