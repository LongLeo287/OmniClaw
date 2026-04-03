---
id: pnnbao97-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.905982
---

# KNOWLEDGE EXTRACT: pnnbao97
> **Extracted on:** 2026-03-30 17:51:04
> **Source:** pnnbao97

---

## File: `sea-g2p.md`
```markdown
# 📦 pnnbao97/sea-g2p [🔖 PENDING/APPROVE]
🔗 https://github.com/pnnbao97/sea-g2p


## Meta
- **Stars:** ⭐ 81 | **Forks:** 🍴 20
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fast multilingual text-to-phoneme converter for South East Asian languages.

## README (trích đầu)
```
# 🦭 SEA-G2P

<img width="1221" height="656" alt="image" src="https://github.com/user-attachments/assets/01220177-815b-4012-8f65-8a2a86beddf9" />

Fast multilingual text-to-phoneme converter for South East Asian languages.  
>**Author**: [Pham Nguyen Ngoc Bao](https://github.com/pnnbao97)

## 🚀 Used By

SEA-G2P is the core phonemization engine powering:

- [**VieNeu-TTS**](https://github.com/pnnbao97/VieNeu-TTS): An advanced on-device Vietnamese Text-to-Speech model with instant voice cloning.

By using SEA-G2P, VieNeu-TTS achieves high-fidelity pronunciation and seamless Vietnamese-English code-switching.

## Installation

```bash
pip install sea-g2p
```

## Usage

### Simple Pipeline

```python
from sea_g2p import SEAPipeline

pipeline = SEAPipeline(lang="vi")

# Single text
result = pipeline.run("Giá SP500 hôm nay là 4.200,5 điểm.")
print(result)
#zˈaːɜ ˈɛɜt̪ pˈe nˈam tʃˈam hˈom nˈaj lˌaː2 bˈoɜn ŋˈi2n hˈaːj tʃˈam fˈəɪ4 nˈam ɗˈiɛ4m.

# Batch processing (Parallel)
texts = ["Giá cổ phiếu tăng từ $0.000045 lên $1,234.5678 trong 3.5×10^6 giao dịch.", "Hãy gửi email đến support@example.com."] * 1000
results = pipeline.run(texts)
```

### Individual Modules

```python
from sea_g2p import Normalizer, G2P

normalizer = Normalizer(lang="vi")
g2p = G2P(lang="vi")

# Automatic parallel processing when list is passed
texts = ["Giá cổ phiếu tăng từ $0.000045 lên $1,234.5678 trong 3.5×10^6 giao dịch.", "Hãy gửi email đến support@example.com."]
normalized = normalizer.normalize(texts)
print(normalized)
#['giá cổ phiếu tăng từ không chấm không không không không bốn lăm <en>u s d</en> lên một nghìn hai trăm ba mươi bốn phẩy năm sáu bảy tám <en>u s d</en> trong ba chấm năm nhân mười mũ sáu giao dịch.', 'hãy gửi email đến <en>support</en> a còng <en>example</en> chấm com.']
phonemes = g2p.convert(normalized)
print(phonemes)
#['zˈaːɜ kˈo4 fˈiɛɜw t̪ˈaŋ t̪ˌy2 xˌoŋ tʃˈəɜm xˌoŋ xˌoŋ xˌoŋ xˌoŋ bˈoɜn lˈam jˈuː ˈɛs dˈiː lˈen mˈo6t̪ ŋˈi2n hˈaːj tʃˈam bˈaː mˈyəj bˈoɜn fˈəɪ4 nˈam sˈaɜw bˈa4j t̪ˈaːɜm jˈuː ˈɛs dˈiː tʃˈɔŋ bˈaː tʃˈəɜm nˈam ɲˈən mˈyə2j mˈu5 sˈaɜw zˈaːw zˈi6c.', 'hˈa5j ɣˈy4j ˈiːmeɪl ɗˌeɜn səpˈɔːɹt ˈaː kˈɔ2ŋ ɛɡzˈæmpəl tʃˈəɜm kˈɔm.']
```

## Features

- **Blazing Fast**: Core engine rewritten in Rust with binary mmap lookup.
- **Multithreading**: Automatic parallel processing using Rayon/Rust for batch inputs.
- **Zero Dependency**: Pre-compiled wheels for Windows, Linux, and macOS.
- **Smart Normalization**: Specialized for Vietnamese (numbers, dates, technical terms).
- **Bilingual Support**: Handles mixed Vietnamese/English text seamlessly.

## 📊 Performance

The following benchmarks were conducted on a dataset of **1,000,000 sentences**:

| Module | Implementation | Throughput | 
| :--- | :--- | :--- | 
| **Normalizer** | Rust Core (Parallel) | **~41,000 sentences/s** |
| **G2P** | Rust Core (Parallel) | **~415,000 sentences/s** |

**Total Pipeline Throughput**: **~37,000 sentences/s**
*(Tested on CPython 3.12, Windows 11, Multithreaded)*

## Technical Architect
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `VieNeu-TTS.md`
```markdown
# 📦 pnnbao97/VieNeu-TTS [🔖 PENDING/APPROVE]
🔗 https://github.com/pnnbao97/VieNeu-TTS
🌐 https://docs.vieneu.io/docs/sdk/overview

## Meta
- **Stars:** ⭐ 966 | **Forks:** 🍴 319
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Vietnamese TTS with instant voice cloning • On-device • Real-time CPU inference • 24kHz audio quality • Chuyển văn bản thành giọng nói tiếng Việt • Text to speech tiếng Việt • TTS tiếng Việt 

## README (trích đầu)
```
# 🦜 VieNeu-TTS

[![Awesome](https://img.shields.io/badge/Awesome-NLP-green?logo=github)](https://github.com/keon/awesome-nlp)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/yJt8kzjzWZ)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1b9PO-lcGZX9pEkEwQmu8MfhSnjxKrALW?usp=sharing)
[![Hugging Face 0.5B](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-0.5B-yellow)](https://huggingface.co/pnnbao-ump/VieNeu-TTS)
[![Hugging Face 0.3B](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-0.3B-orange)](https://huggingface.co/pnnbao-ump/VieNeu-TTS-0.3B)

<img width="1087" height="710" alt="image" src="https://github.com/user-attachments/assets/5534b5db-f30b-4d27-8a35-80f1cf6e5d4d" />

**VieNeu-TTS** is an advanced on-device Vietnamese Text-to-Speech (TTS) model with **instant voice cloning**.

> [!TIP]
> **Voice Cloning:** All model variants (including GGUF) support instant voice cloning with just **3-5 seconds** of reference audio.

This project features two core architectures trained on the [VieNeu-TTS-1000h](https://huggingface.co/datasets/pnnbao-ump/VieNeu-TTS-1000h) dataset:
- **VieNeu-TTS (0.5B):** An enhanced model optimized for maximum stability.
- **VieNeu-TTS-0.3B:** A specialized model **trained from scratch** using the VieNeu-TTS-1000h dataset, delivering 2x faster inference and ultra-low latency.

These represent a significant upgrade with the following improvements:
- **Enhanced pronunciation**: More accurate and stable Vietnamese pronunciation powered by the [sea-g2p](https://github.com/pnnbao97/sea-g2p) library
- **Code-switching support**: Seamless transitions between Vietnamese and English powered by the [sea-g2p](https://github.com/pnnbao97/sea-g2p) library
- **Better voice cloning**: Higher fidelity and speaker consistency
- **Real-time synthesis**: 24 kHz waveform generation on CPU or GPU
- **Multiple model formats**: Support for PyTorch, GGUF Q4/Q8 (CPU optimized), and ONNX codec

VieNeu-TTS delivers production-ready speech synthesis fully offline.  

**Author:** Phạm Nguyễn Ngọc Bảo

---

[<img width="600" height="595" alt="VieNeu-TTS Demo" src="https://github.com/user-attachments/assets/021f6671-2d7f-4635-91fb-88b2ab0ddbcd" />](https://github.com/user-attachments/assets/021f6671-2d7f-4635-91fb-88b2ab0ddbcd)

---

## 📌 Table of Contents

1. [🦜 Installation & Web UI](#installation)
2. [📦 Using the Python SDK](#sdk)
3. [🐳 Docker & Remote Server](#docker-remote)
4. [🎯 Custom Models](#custom-models)
5. [🛠️ Fine-tuning Guide](#finetuning)
6. [🔬 Model Overview](#backbones)
7. [🐋 Deployment with Docker (Compose)](#docker)
8. [🚀 Roadmap](#roadmap)
9. [🤝 Support & Contact](#support)

---

## 🦜 1. Installation & Web UI <a name="installation"></a>

> *For Intel arc gpu user, [read the Intel Arc GPU section below](#intel-arc).*

### Installation Steps
1. **Clone the Repo:**
   ```bash
   git 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

