---
id: repo-kittentts
type: api
owner: OA
registered_at: 2026-04-05T17:52:18.068002
tags: ["auto-cloned", "Text-to-Speech", "ONNX", "Edge AI", "oa-assimilated"]
---

# kittentts

## Assimilation Report
Kitten TTS is an open-source, lightweight Text-to-Speech (TTS) library designed for high-quality voice synthesis on CPU using ONNX models. It emphasizes portability and efficiency, making it ideal for edge devices and resource-constrained environments.

## Application for OmniClaw
OmniClaw can integrate Kitten TTS as a core 'Voice Synthesis API' module. This allows OmniClaw to generate highly customized, low-latency audio outputs for its agents' interactions (e.g., character voices, system feedback). The blueprint involves wrapping the ONNX inference logic into a standardized OmniClaw service call, enabling agents to specify voice parameters (voice ID, model size, emotional tone) directly in their prompts, thereby enhancing the realism and immersion of the multi-agent conversational experience.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Kitten TTS

<p align="center">
  <img width="607" height="255" alt="Kitten TTS" src="https://github.com/user-attachments/assets/f4646722-ba78-4b25-8a65-81bacee0d4f6" />
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/KittenML/KittenTTS-Demo"><img src="https://img.shields.io/badge/Demo-Hugging%20Face%20Spaces-orange" alt="Hugging Face Demo"></a>
  <a href="https://discord.com/invite/VJ86W4SURW"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://kittenml.com"><img src="https://img.shields.io/badge/Website-kittenml.com-blue" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-green.svg" alt="License"></a>
</p>

> **New:** Kitten TTS v0.8 is out -- 15M, 40M, and 80M parameter models now available.

Kitten TTS is an open-source, lightweight text-to-speech library built on ONNX. With models ranging from 15M to 80M parameters (25-80 MB on disk), it delivers high-quality voice synthesis on CPU without requiring a GPU.

> **Status:** Developer preview -- APIs may change between releases.

**Commercial support is available.** For integration assistance, custom voices, or enterprise licensing, [contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview).

## Table of Contents

- [Features](#features)
- [Available Models](#available-models)
- [Demo](#demo)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [System Requirements](#system-requirements)
- [Roadmap](#roadmap)
- [Commercial Support](#commercial-support)
- [Community and Support](#community-and-support)
- [License](#license)

## Features

- **Ultra-lightweight** -- Model sizes from 25 MB (int8) to 80 MB, suitable for edge deployment
- **CPU-optimized** -- ONNX-based inference runs efficiently without a GPU
- **8 built-in voices** -- Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, and Leo
- **Adjustable speech speed** -- Control playback rate via the `speed` parameter
- **Text preprocessing** -- Built-in pipeline handles numbers, currencies, units, and more
- **24 kHz output** -- High-quality audio at a standard sample rate

## Available Models

| Model | Parameters | Size | Download |
|---|---|---|---|
| kitten-tts-mini | 80M | 80 MB | [KittenML/kitten-tts-mini-0.8](https://huggingface.co/KittenML/kitten-tts-mini-0.8) |
| kitten-tts-micro | 40M | 41 MB | [KittenML/kitten-tts-micro-0.8](https://huggingface.co/KittenML/kitten-tts-micro-0.8) |
| kitten-tts-nano | 15M | 56 MB | [KittenML/kitten-tts-nano-0.8](https://huggingface.co/KittenML/kitten-tts-nano-0.8-fp32) |
| kitten-tts-nano (int8) | 15M | 25 MB | [KittenML/kitten-tts-nano-0.8-int8](https://huggingface.co/KittenML/kitten-tts-nano-0.8-int8) |

> **Note:** Some users have reported issues with the `kitten-tts-nano-0.8-int8` model. If you encounter problems, please [open an issue](https://github.com/KittenML/KittenTTS/issues).

## Demo

https://github.com/user-attachments/assets/d80120f2-c751-407e-a166-068dd1dd9e8d

### Try it online

Try Kitten TTS directly in your browser on [Hugging Face Spaces](https://huggingface.co/spaces/KittenML/KittenTTS-Demo).

## Quick Start

### Prerequisites

- Python 3.8 or later
- pip

### Installation

```bash
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
```

### Basic Usage

```python
from kittentts import KittenTTS

model = KittenTTS("KittenML/kitten-tts-mini-0.8")
audio = model.generate("This high-quality TTS model runs without a GPU.", voice="Jasper")

import soundfile as sf
sf.write("output.wav", audio, 24000)
```

### Advanced Usage

```python
# Adjust speech speed (default: 1.0)
audio = model.generate("Hello, world.", voice="Luna", speed=1.2)

# Save directly to a file
model.generate_to_file("Hello, world.", "output.wav", voice="Bruno", speed=0.9)

# List available voices
print(model.available_voices)
# ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
```

### Using with GPU

```
pip install -r requirements_gpu.txt
```

```python
m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda")
```

Check out `example_cuda.py` 

## API Reference

### `KittenTTS(model_name, cache_dir=None)`

Load a model from Hugging Face Hub.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model_name` | `str` | `"KittenML/kitten-tts-nano-0.8"` | Hugging Face repository ID |
| `cache_dir` | `str` | `None` | Local directory for caching downloaded model files |

### `model.generate(text, voice, speed, clean_text)`

Synthesize speech from text, returning a NumPy array of audio samples at 24 kHz.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `str` | -- | Input text to synthesize |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name (see available voices) |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `clean_text` | `bool` | `False` | Preprocess text (expand numbers, currencies, etc.) |

### `model.generate_to_file(text, output_path, voice, speed, sample_rate, clean_text)`

Synthesize speech and write directly to an audio file.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `str` | -- | Input text to synthesize |
| `output_path` | `str` | -- | Path to save the audio file |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `sample_rate` | `int` | `24000` | Audio sample rate in Hz |
| `clean_text` | `bool` | `True` | Preprocess text (expand numbers, currencies, etc.) |

### `model.available_voices`

Returns a list of available voice names: `['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']`

## System Requirements

- **Operating system:** Linux, macOS, or Windows
- **Python:** 3.8 or later
- **Hardware:** Runs on CPU; no GPU required
- **Disk space:** 25-80 MB depending on model variant

A virtual environment (conda, venv, or similar) is recommended to avoid dependency conflicts.

## Roadmap

- [ ] Release optimized inference engine
- [ ] Release mobile SDK
- [ ] Release higher quality TTS models
- [ ] Release multilingual TTS
- [ ] Release KittenASR
- [ ] Need anything else? [Let us know](https://github.com/KittenML/KittenTTS/issues)

## Commercial Support

We offer commercial support for teams integrating Kitten TTS into their products. This includes integration assistance, custom voice development, and enterprise licensing.

[Contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview) or email info@stellonlabs.com to discuss your requirements.

## Community and Support

- **Discord:** [Join the community](https://discord.com/invite/VJ86W4SURW)
- **Website:** [kittenml.com](https://kittenml.com)
- **Custom support:** [Request form](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview)
- **Email:** info@stellonlabs.com
- **Issues:** [GitHub Issues](https://github.com/KittenML/KittenTTS/issues)

## License

This project is licensed under the [Apache License 2.0](LICENSE).

```

### File: requirements.txt
```txt
espeakng_loader
phonemizer
onnxruntime
soundfile
numpy
huggingface_hub

```

### File: setup.py
```py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kittentts",
    version="0.8.1",
    author="KittenML",
    author_email="",
    description="Ultra-lightweight text-to-speech model with just 15 million parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kittenml/kittentts",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "espeakng_loader",
        "phonemizer",
        "onnxruntime",
        "soundfile",
        "numpy",
        "huggingface_hub",
    ],
    keywords="text-to-speech, tts, speech-synthesis, neural-networks, onnx",
    project_urls={
        "Bug Reports": "https://github.com/kittenml/kittentts/issues",
        "Source": "https://github.com/kittenml/kittentts",
    },
)

```

### File: example.py
```py
from kittentts import KittenTTS

# it will run blazing fast on any GPU. But this example will run on CPU.

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8") # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-micro-0.8") # 40M version (balances speed and quality )
# m = KittenTTS("KittenML/kitten-tts-nano-0.8") # 15M version (tiny and faster )


# Step 2: Generate the audio 

# this is a sample from the TinyStories dataset. 
text ="""One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. """


# available_voices : ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
voice = 'Bruno'



audio = m.generate(text=text, voice=voice )

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)
print(f"Audio saved to output.wav")
```

### File: example_cuda.py
```py
from kittentts import KittenTTS

# This example will runs on GPU.

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda") # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-micro-0.8") # 40M version (balances speed and quality )
# m = KittenTTS("KittenML/kitten-tts-nano-0.8") # 15M version (tiny and faster )


# Step 2: Generate the audio 

# this is a sample from the TinyStories dataset. 
text ="""One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. """


# available_voices : ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
voice = 'Bruno'



audio = m.generate(text=text, voice=voice )

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)
print(f"Audio saved to output.wav")
```

### File: example_streaming.py
```py
import numpy as np
import soundfile as sf
from kittentts import KittenTTS

SAMPLE_RATE = 24000

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8")  # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda")  # GPU version
# m = KittenTTS("KittenML/kitten-tts-micro-0.8")  # 40M version
# m = KittenTTS("KittenML/kitten-tts-nano-0.8")  # 15M version (tiny and faster)

# Step 2: Define text and voice
text = """One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. Lily wanted to use the needle to sew a button on her shirt. She asked her mom for help."""

voice = "Bruno"

# Optional: try to import sounddevice for real-time playback
try:
    import sounddevice as sd
    has_audio = True
except (ImportError, OSError):
    has_audio = False

# Step 3: Stream audio chunk by chunk
print("Streaming audio...")
chunks = []
for i, chunk in enumerate(m.generate_stream(text=text, voice=voice)):
    audio = chunk.squeeze()
    chunks.append(audio)
    print(f"  Chunk {i + 1}: {len(audio)} samples ({len(audio) / SAMPLE_RATE:.2f}s)")
    if has_audio:
        sd.play(audio, samplerate=SAMPLE_RATE)
        sd.wait()

# Save the full audio
full_audio = np.concatenate(chunks)
sf.write("output_streaming.wav", full_audio, SAMPLE_RATE)
print(f"Audio saved to output_streaming.wav ({len(full_audio) / SAMPLE_RATE:.2f}s total)")

```

### File: requirements_gpu.txt
```txt
espeakng_loader
phonemizer
onnxruntime-gpu
soundfile
numpy
huggingface_hub
nvidia-cublas-cu12                                             
nvidia-cudnn-cu12                                                                                                                                                                    
nvidia-cuda-runtime-cu12                                       
nvidia-curand-cu12                                                                                                                                                                   
nvidia-cufft-cu12 
nvidia-cusolver-cu12                                                                                                                                                                 
nvidia-cusparse-cu12                                           
nvidia-nvjitlink-cu12

```

