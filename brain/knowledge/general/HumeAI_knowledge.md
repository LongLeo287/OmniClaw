---
id: humeai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.924258
---

# KNOWLEDGE EXTRACT: HumeAI
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** HumeAI

---

## File: `tada.md`
```markdown
# 📦 HumeAI/tada [🔖 PENDING/APPROVE]
🔗 https://github.com/HumeAI/tada
🌐 https://www.hume.ai/blog/opensource-tada

## Meta
- **Stars:** ⭐ 914 | **Forks:** 🍴 93
- **Language:** Jupyter Notebook | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Open Source Speech Language Model

## README (trích đầu)
```
<!-- ---
license: llama3.2
language:
  - en
tags:
  - tts
  - text-to-speech
  - speech-language-model
--- -->

<h1 align="center">TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment</h1>

<p align="center">
  <a href="https://arxiv.org/abs/2602.23068"><img src="https://img.shields.io/badge/arXiv-Paper-b31b1b.svg" alt="Paper"></a>
  <a href="https://huggingface.co/spaces/HumeAI/tada"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-blue" alt="Demo"></a>
  <a href="https://www.hume.ai/blog/opensource-tada"><img src="https://img.shields.io/badge/Blog-Post-orange.svg" alt="Blog"></a>
  <a href="https://huggingface.co/collections/HumeAI/tada"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Collection-yellow" alt="Collection"></a>
  <a href="https://pypi.org/project/hume-tada/"><img src="https://img.shields.io/badge/PyPI-hume--tada-3775A9.svg?logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://github.com/HumeAI/tada/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

<img width="2400" height="1260" alt="image" src="https://github.com/user-attachments/assets/800eb8c5-eb6f-4e03-b8f3-150055a6cdfc" />

<p align="center"><br/><em>A unified speech-language model that synchronizes speech and text into a single, cohesive stream via 1:1 alignment.</em></p>

---

TADA achieves high-fidelity synthesis and generation with a fraction of the computational overhead required by traditional models. By leveraging a novel tokenizer and architectural design, each autoregressive step covers one text token, dynamically determining its duration and prosody — eliminating fixed frame rates and transcript hallucination.

## Updates

**March 2026**
- Encoder no longer loaded inside `TadaForCausalLM` — saves ~2.5 GB VRAM. Load it separately only when encoding new prompts.
- Added `EncoderOutput.save()` / `EncoderOutput.load()` for prompt caching — encode once, reuse without the encoder.
- Default flow matching steps reduced from 20 to 10 (no perceptible quality loss, ~1.3x faster).
- bf16 inference support via `torch_dtype=torch.bfloat16` — halves model memory (~9 GB for 3B).
- `model.compile()` for torch.compile optimization — ~0.12x RTF on H100 with cached prompts.

## Key Features

- **1:1 Token Alignment** — The tokenizer encodes audio into a sequence of vectors that perfectly matches the number of text tokens.
- **Dynamic Duration Synthesis** — Generates the full speech segment for a text token in a single autoregressive step, regardless of length.
- **Dual-Stream Generation** — Generates a text token and the speech for the preceding token simultaneously, maintaining the same context length as text-only generation.
- **Efficiency & Reliability** — Superior expressiveness and natural flow while significantly reducing computational cost.

## How It Works

### The Tokenization Schema

TADA unifies modalities by ensuring that for every word
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

