---
id: tada
type: knowledge
owner: OA_Triage
---
# tada
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

TADA unifies modalities by ensuring that for every word or subword token, there is exactly one corresponding speech vector. This synchronized stream allows the model to "understand" the precise timing of speech relative to text.

### Dynamic Autoregression

Most TTS models require a fixed number of steps to produce one second of audio (e.g., 50 frames per second). TADA breaks this constraint:

- Each autoregressive step covers one text token.
- The model dynamically determines the duration and prosody for that specific token.
- This results in a more natural flow and eliminates transcript hallucination.

## Evaluation

<table>
  <tr>
    <td><img src="figures/CER.png" alt="CER" height="300px"></td>
    <td><img src="figures/real-time.png" alt="Speed" height="300px"></td>
  </tr>
  <tr>
    <td><img src="figures/naturalness.png" alt="Naturalness MOS" height="280px"></td>
    <td><img src="figures/speaker-sim.png" alt="Speaker Similarity" height="270px"></td>
  </tr>
</table>

## Prerequisites

TADA models are built on [Meta Llama 3.2](https://huggingface.co/meta-llama). You must request access to the Llama models before using TADA:

- Visit [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) or [meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B) and accept the license agreement

## Installation

```bash
pip install hume-tada
```

### Build from source

```bash
git clone https://github.com/HumeAI/tada.git
cd tada
pip install -e .
```

## Models

| Model | Base Model | HuggingFace Hub |
|-------|-----------|-----------------|
| TADA-1B | Llama 3.2 1B | [`HumeAI/tada-1b`](https://huggingface.co/HumeAI/tada-1b) |
| TADA-3B-ML | Llama 3.2 3B | [`HumeAI/tada-3b-ml`](https://huggingface.co/HumeAI/tada-3b-ml) |

All models use the same encoder ([`HumeAI/tada-codec`](https://huggingface.co/HumeAI/tada-codec)) and can be loaded using the same API.

## Run Inference

### Text-to-Speech

```python
import torch
import torchaudio

from tada.modules.encoder import Encoder, EncoderOutput
from tada.modules.tada import TadaForCausalLM

device = "cuda"

# Encoder is loaded separately (not inside the model)
encoder = Encoder.from_pretrained("HumeAI/tada-codec", subfolder="encoder").to(device)
model = TadaForCausalLM.from_pretrained("HumeAI/tada-3b-ml", torch_dtype=torch.bfloat16).to(device)

audio, sample_rate = torchaudio.load("samples/ljspeech.wav")
audio = audio.to(device)
prompt_text = "The examination and testimony of the experts, enabled the commission to conclude that five shots may have been fired."
prompt = encoder(
    audio, text=[prompt_text], sample_rate=sample_rate
)

# Optional: save prompt to skip encoder on future runs
# prompt.save("prompt_cache.pt")
# prompt = EncoderOutput.load("prompt_cache.pt", device=device)

output = model.generate(
    prompt=prompt,
    text="Please call Stella. Ask her to bring these things with her from the store.",
)
```

### Multilingual Generation

TADA supports multilingual speech synthesis via language-specific aligners. Pass the `language` parameter when loading the encoder to use the appropriate aligner for your target language.

```python
import torch
import torchaudio

from tada.modules.encoder import Encoder
from tada.modules.tada import TadaForCausalLM

device = "cuda"
encoder = Encoder.from_pretrained("HumeAI/tada-codec", subfolder="encoder", language="ja").to(device)
model = TadaForCausalLM.from_pretrained("HumeAI/tada-3b-ml", torch_dtype=torch.bfloat16).to(device)

# Load a reference audio clip in the target language
audio, sample_rate = torchaudio.load("samples/ja_prompt.wav")
audio = audio.to(device)

# For non-English prompts, provide the transcript so the encoder uses forced alignment
# instead of the built-in ASR (which is English-only)
prompt_text = "このムキムキのお兄さんがいるし バーだし少し高そうだと思いますよねこのバーの料金設定は良心的でした まあそんなに高くなかったです"
prompt = encoder(audio, text=[prompt_text], sample_rate=sample_rate)

output = model.generate(
    prompt=prompt,
    text="今日はとても良い天気ですね。散歩に行きましょう。",
)
```

Supported languages: `ar`, `ch`, `de`, `es`, `fr`, `it`, `ja`, `pl`, `pt`. When `language` is not specified, the default English aligner is used.

> **Note:** For non-English prompts, you should provide the transcript of the reference audio via the `text` parameter. The encoder's built-in ASR is English-only. The generation will still work, but alignment quality will be degraded.

You can inspect the prompt alignment to verify it looks correct:

```python
prompt.print_alignment(model.tokenizer)
```

This shows a dot-span visualization of the token-to-audio alignment — dots represent frame gaps, tokens appear at their aligned positions:

```
34 tokens | 10.50s audio
······The··exam····ination··and·····test···imony··of···the
```

- If alignment looks wrong (tokens bunched together, missing tokens, nonsensical text), check that you provided the correct transcript.
- This is especially important for non-English prompts where the built-in ASR cannot be used.

### Speech continuation

Provide `num_extra_steps` if you want to generate text-speech continuation of the prompt:

```python
output = model.generate(
    prompt=prompt,
    num_extra_steps=50
)
```

## 📚 Citation

If you use this project in your research, please cite our paper:

```bibtex
@article{dang2026tada,
  title={TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment},
  author={Dang, Trung and Rao, Sharath and Gupta, Ananya and Gagne, Christopher and Tzirakis, Panagiotis and Baird, Alice and Cłapa, Jakub Piotr and Chin, Peter and Cowen, Alan},
  journal={arXiv preprint arXiv:2602.23068},
  year={2026}
}
```

## License

This repository contains both model weights and code, which are licensed separately:

- **Model weights** are licensed under the Llama 3.2 Community License Agreement  
- **Code** in this repository is licensed under the MIT License  

You must comply with the terms of the Llama 3.2 license when using the models.

See:
- `LICENSE` for the Llama 3.2 license
- `LICENSE_CODE` for the MIT license

## Contact

[Hume AI](https://hume.ai) is an empathic AI research company. We research the datasets, tools, and models needed to give empathy to AI models to serve human wellbeing. If you're interested in any of our product or research collaborations, please reach out to us at hello@hume.ai.

## Acknowledgements

This project is built using Llama 3.2.

Llama 3.2 is licensed under the Llama 3.2 Community License.

```

### File: apple\README.md
```md
# MLX-TADA

TADA speech synthesis on Apple Silicon via [MLX](https://github.com/ml-explore/mlx).

Also available on PyPI: `pip install mlx-tada`

## Setup

```bash
cd apple
uv venv
uv pip install -e .
```

For auto-transcription of reference audio (optional):
```bash
uv pip install mlx-whisper
```

## Weights

Download a reference audio clip:
```bash
curl -O "https://storage.googleapis.com/hume_reference_speakers/ljspeech.wav"
```

Pre-converted weights are downloaded and cached automatically. You still need [gated access to Llama 3.2](https://huggingface.co/meta-llama/Llama-3.2-1B) for the tokenizer:

```python
from mlx_tada import TadaForCausalLM, save_wav

model = TadaForCausalLM.from_pretrained("HumeAI/mlx-tada-3b", quantize=4)
ref = model.load_reference("ljspeech.wav")
out = model.generate("Hello, this is a test of TADA speech synthesis.", ref)
save_wav(out.audio, "output.wav")
```

Available models:
- [`HumeAI/mlx-tada-1b`](https://huggingface.co/HumeAI/mlx-tada-1b) — 1B English-only (~4.3 GB)
- [`HumeAI/mlx-tada-3b`](https://huggingface.co/HumeAI/mlx-tada-3b) — 3B multilingual (~8.9 GB)

### Offline Use

To download weights locally for offline inference:
```python
from huggingface_hub import snapshot_download
snapshot_download("HumeAI/mlx-tada-3b", local_dir="./weights/3b")
```

Then load from the local path:
```python
model = TadaForCausalLM.from_weights("./weights/3b", quantize=4)
```

## Generate Speech

### CLI

```bash
uv run python -m mlx_tada.generate \
  --weights ./weights/3b \
  --audio ljspeech.wav \
  --text "The history of artificial intelligence is a fascinating journey that spans decades of research and innovation. It all began in the 1950s when pioneers like Alan Turing first posed the question of whether machines could think." \
  --output output.wav
```

With 4-bit quantization (10x faster, 60% less memory):
```bash
uv run python -m mlx_tada.generate \
  --weights ./weights/3b \
  --audio ljspeech.wav \
  --text "The history of artificial intelligence is a fascinating journey that spans decades of research and innovation. It all began in the 1950s when pioneers like Alan Turing first posed the question of whether machines could think." \
  --quantize 4 \
  --output output.wav
```

### Python

```python
from mlx_tada import TadaForCausalLM, save_wav

model = TadaForCausalLM.from_pretrained("HumeAI/mlx-tada-3b", quantize=4)
ref = model.load_reference("ljspeech.wav")
out = model.generate("The history of artificial intelligence is a fascinating journey that spans decades of research and innovation. It all began in the 1950s when pioneers like Alan Turing first posed the question of whether machines could think.", ref)
save_wav(out.audio, "output.wav")

# out.audio     - numpy float32 array (24kHz)
# out.duration  - audio duration in seconds
# out.rtf       - real-time factor
# out.num_tokens
```

### Inference Options

Control generation behavior with `InferenceOptions`:

```python
from mlx_tada import TadaForCausalLM, InferenceOptions, save_wav

model = TadaForCausalLM.from_weights("./weights/3b", quantize=4)
ref = model.load_reference("ljspeech.wav")

opts = InferenceOptions(
    acoustic_cfg_scale=1.6,
    duration_cfg_scale=1.0,
    num_flow_matching_steps=10,
    time_schedule="logsnr",
    cfg_schedule="cosine",
)

out = model.generate(text="Hello world, today is a nice day.", reference=ref, inference_options=opts)
save_wav(out.audio, "output.wav")
```

The following inference options from the PyTorch version are **not currently supported** in MLX:
- `speed_up_factor`
- `num_acoustic_candidates`
- `scorer`
- `negative_condition_source`
- `text_only_logit_scale`
- `spkr_verification_weight`

### Speech Continuation

Use `num_extra_steps` to let the model generate speech beyond the provided text. The model continues speaking naturally and stops when it produces an end-of-sequence token:

```python
from mlx_tada import TadaForCausalLM, InferenceOptions, save_wav

model = TadaForCausalLM.from_weights("./weights/3b", quantize=4)
ref = model.load_reference("ljspeech.wav")

opts = InferenceOptions(
    acoustic_cfg_scale=1.6,
    num_flow_matching_steps=10,
    time_schedule="logsnr",
)

out = model.generate(
    text="The history of artificial intelligence is a fascinating journey that spans decades of research and innovation.",
    reference=ref,
    inference_options=opts,
    num_extra_steps=50,
)
save_wav(out.audio, "output.wav")
```

### Save and Reuse References

```python
from mlx_tada import Reference

ref = model.load_reference("ljspeech.wav")
ref.save("speaker.npz")

ref = Reference.load("speaker.npz")
out = model.generate("Reusing the same voice.", ref)
```

### Save Audio

```python
from mlx_tada import save_wav
save_wav(out.audio, "output.wav")
```

## Debug Logging

```bash
DEBUG=1 uv run python -m mlx_tada.generate \
  --weights ./weights/3b \
  --audio ljspeech.wav \
  --text "Hello"
```

```python
from mlx_tada import setup_logging

setup_logging()
```

## Running Tests

```bash
MLX_WEIGHTS=./weights/1b uv run pytest tests/ -v
```

```

### File: apple\tests\test_aligner.py
```py
import math
import os
from pathlib import Path

import mlx.core as mx
import numpy as np
import pytest

from mlx_tada.aligner import Aligner, align_text_tokens
from mlx_tada.audio import load_audio, resample_audio
from mlx_tada.model import load_weights

SAMPLE_DIR = Path(__file__).parent.parent.parent / "tada" / "samples"
WEIGHTS_DIR = Path(os.environ.get("MLX_WEIGHTS", "mlx_weights"))


@pytest.fixture(scope="module")
def aligner():
    aligner = Aligner()
    load_weights(aligner, WEIGHTS_DIR / "aligner" / "weights.safetensors")
    mx.eval(aligner.parameters())
    return aligner


@pytest.fixture(scope="module")
def tokenizer():
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")


def test_align_text_tokens_basic():
    np.random.seed(42)
    probs = np.random.randn(10, 5).astype(np.float32)
    text_tokens = np.array([1, 3, 4], dtype=np.int64)
    positions = align_text_tokens(probs, text_tokens)
    assert len(positions) == 3
    assert all(positions[i] <= positions[i + 1] for i in range(len(positions) - 1))


def test_align_text_tokens_single_token():
    probs = np.zeros((5, 3), dtype=np.float32)
    probs[2, 1] = 10.0
    positions = align_text_tokens(probs, np.array([1], dtype=np.int64))
    assert positions == [2]


def test_aligner_ljspeech(aligner, tokenizer):
    audio_path = str(SAMPLE_DIR / "ljspeech.wav")
    text = "The examination and testimony of the experts, enabled the commission to conclude that five shots may have been fired."

    audio_24k, sr = load_audio(audio_path, target_sr=24000)
    audio_16k = resample_audio(audio_24k, 24000, 16000).reshape(1, -1)
    audio_len = len(audio_24k)

    text_token_ids = tokenizer.encode(text, add_special_tokens=False)
    text_tokens_np = np.array([text_token_ids], dtype=np.int64)
    input_lengths = np.array([math.ceil(audio_len / sr * 50)], dtype=np.int64)

    token_positions, token_masks = aligner(
        mx.array(audio_16k),
        text_tokens_np,
        input_lengths,
        tokenizer.eos_token_id,
    )

    text_tokens_str = tokenizer.convert_ids_to_tokens(text_token_ids)

    assert list(zip(text_tokens_str, token_positions[0].tolist())) == [
        ("The", 2),
        ("Ġexamination", 31),
        ("Ġand", 47),
        ("Ġtestimony", 58),
        ("Ġof", 85),
        ("Ġthe", 92),
        ("Ġexperts", 114),
        (",", 149),
        ("Ġenabled", 156),
        ("Ġthe", 176),
        ("Ġcommission", 189),
        ("Ġto", 208),
        ("Ġconclude", 228),
        ("Ġthat", 266),
        ("Ġfive", 280),
        ("Ġshots", 298),
        ("Ġmay", 316),
        ("Ġhave", 323),
        ("Ġbeen", 332),
        ("Ġfired", 347),
        (".", 377),
    ]

    assert token_masks.shape[1] == input_lengths[0]
    assert token_masks.sum() == len(text_token_ids)


def test_aligner_logits_shape(aligner):
    audio_path = str(SAMPLE_DIR / "ljspeech.wav")
    audio_24k, _ = load_audio(audio_path, target_sr=24000)
    audio_16k = resample_audio(audio_24k, 24000, 16000).reshape(1, -1)

    logits = aligner.wav2vec2(mx.array(audio_16k))
    mx.eval(logits)

    assert logits.shape[0] == 1
    assert logits.shape[2] == 128256
    assert logits.shape[1] > 300


def test_aligner_output_masks_binary(aligner, tokenizer):
    audio_path = str(SAMPLE_DIR / "ljspeech.wav")
    text = "The examination and testimony of the experts, enabled the commission to conclude that five shots may have been fired."

    audio_24k, sr = load_audio(audio_path, target_sr=24000)
    audio_16k = resample_audio(audio_24k, 24000, 16000).reshape(1, -1)
    audio_len = len(audio_24k)

    text_token_ids = tokenizer.encode(text, add_special_tokens=False)
    text_tokens_np = np.array([text_token_ids], dtype=np.int64)
    input_lengths = np.array([math.ceil(audio_len / sr * 50)], dtype=np.int64)

    _, token_masks = aligner(
        mx.array(audio_16k),
        text_tokens_np,
        input_lengths,
        tokenizer.eos_token_id,
    )

    unique_vals = set(token_masks.flatten().tolist())
    assert unique_vals <= {0, 1}

```

