---
id: blaizzy-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.967010
---

# KNOWLEDGE EXTRACT: Blaizzy
> **Extracted on:** 2026-03-30 17:30:50
> **Source:** Blaizzy

---

## File: `mlx-audio.md`
```markdown
# 📦 Blaizzy/mlx-audio [🔖 PENDING/APPROVE]
🔗 https://github.com/Blaizzy/mlx-audio


## Meta
- **Stars:** ⭐ 6393 | **Forks:** 🍴 511
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon.

## README (trích đầu)
```
<a href="https://trendshift.io/repositories/13625" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13625" alt="Blaizzy%2Fmlx-audio | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

# MLX-Audio

The best audio processing library built on Apple's MLX framework, providing fast and efficient text-to-speech (TTS), speech-to-text (STT), and speech-to-speech (STS) on Apple Silicon.

## Features

- Fast inference optimized for Apple Silicon (M series chips)
- Multiple model architectures for TTS, STT, and STS
- Multilingual support across models
- Voice customization and cloning capabilities
- Adjustable speech speed control
- Interactive web interface with 3D audio visualization
- OpenAI-compatible REST API
- Quantization support (3-bit, 4-bit, 6-bit, 8-bit, and more) for optimized performance
- Swift package for iOS/macOS integration

## Installation

### Using pip
```bash
pip install mlx-audio
```

### Using uv to install only the command line tools
Latest release from pypi:
```bash
uv tool install --force mlx-audio --prerelease=allow
```

Latest code from github:
```bash
uv tool install --force git+https://github.com/Blaizzy/mlx-audio.git --prerelease=allow
```

### For development or web interface:

```bash
git clone https://github.com/Blaizzy/mlx-audio.git
cd mlx-audio
pip install -e ".[dev]"
```

## Quick Start

### Command Line

```bash
# Basic TTS generation
mlx_audio.tts.generate --model mlx-community/Kokoro-82M-bf16 --text 'Hello, world!' --lang_code a

# With voice selection and speed adjustment
mlx_audio.tts.generate --model mlx-community/Kokoro-82M-bf16 --text 'Hello!' --voice af_heart --speed 1.2 --lang_code a

# Play audio immediately
mlx_audio.tts.generate --model mlx-community/Kokoro-82M-bf16 --text 'Hello!' --play  --lang_code a

# Save to a specific directory
mlx_audio.tts.generate --model mlx-community/Kokoro-82M-bf16 --text 'Hello!' --output_path ./my_audio  --lang_code a
```

### Python API

```python
from mlx_audio.tts.utils import load_model

# Load model
model = load_model("mlx-community/Kokoro-82M-bf16")

# Generate speech
for result in model.generate("Hello from MLX-Audio!", voice="af_heart"):
    print(f"Generated {result.audio.shape[0]} samples")
    # result.audio contains the waveform as mx.array
```

## Supported Models

### Text-to-Speech (TTS)

| Model | Description | Languages | Repo |
|-------|-------------|-----------|------|
| **Kokoro** | Fast, high-quality multilingual TTS | EN, JA, ZH, FR, ES, IT, PT, HI | [mlx-community/Kokoro-82M-bf16](https://huggingface.co/mlx-community/Kokoro-82M-bf16) |
| **Qwen3-TTS** | Alibaba's multilingual TTS with voice design | ZH, EN, JA, KO, + more | [mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16) |
| **CSM** | Conversational Speech Model with voice cloning | EN | [mlx-community/csm-1b](https://huggingface.co/mlx-community/csm-1b) |
| **Dia** | Dialog
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

